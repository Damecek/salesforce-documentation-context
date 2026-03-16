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
Shows how two records relate to each other.

Possible values are:

**•** `Root Cause`

**•** `Similar`

The default value is 'Root Cause'.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
This field is unique within your organization.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CaseRelatedIssueChangeEvent on page 68 (API version 59.0)**
Change events are available for the object.

**CaseRelatedIssueFeed on page 55**
Feed tracking is available for the object.


### Standard Objects CaseShare

**CaseRelatedIssueHistory on page 63**
History is available for tracked fields of the object.

### CaseShare

Represents a sharing entry on a Case.

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual` . Sharing entries
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

Supported Calls

`describeSObjects()`, `create()`, `delete()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

As of Summer ’20 and later, only users with access to the Case object can access this object.

Fields

The properties available for some fields depend on the default organization-wide sharing settings. The properties listed are true for the
default settings of such fields.

**Field** **Details**

```
CaseAccessLevel

CaseId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Level of access that the User or Group has to the Case. The possible values are:

**•** `Read`

**•** `Edit`

**•** `All` This value isn’t valid for creating or deleting records.

This field must be set to an access level that is higher than the organization’s default access
level for cases.

**Type**
reference


Standard Objects CaseShare

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the Case associated with this sharing entry. This field can't be updated.

This is a relationship field.

**Relationship Name**
Case

**Relationship Type**
Lookup

**Refers To**
Case

```
IsDeleted

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
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only permitted
value is `Manual` . If no value is specified, the field defaults to `Manual` . All other `RowCause`
values are read-only. After the sharing entry is created, this field can’t be edited.

Valid values include:

**•** `Manual` —The User or Group has access because a user with “All” access manually
shared the Case with them.

**•** `Owner` —The User is the owner of the Case.

**•** `ImplicitChild` —The User or Group has access to the Case on the Account
associated with this Case. After faster account sharing recalculation is enabled for your
org, sharing entries with this value aren’t returned in queries. Instead of storing implicit
child shares, record access is determined dynamically.

**•** `RelatedPortalUser` —The portal user is the contact on the Case.

**•** `Rule` —The User or Group has access via a Case sharing rule.

**•** `GuestRule` —The User or Group has access via a Case guest user sharing rule.

**•** `Team` —The User or Group has team access.


### Standard Objects CaseSolution

**Field** **Details**

**•** `LpuImplicit` —The User has access to records owned by high-volume Experience
Cloud site users via a share group.

**•** `ARImplicit` —The User, who belongs to a partner or customer account, has access
to the Case via an account relationship data sharing rule.

```
UserOrGroupId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the User or Group that has been given access to the Case. This field can't be updated.

This is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Relationship Type**
Lookup

**Refers To**
Group, User

This object allows you to determine which users and groups can view and edit Case records owned by other users. If you attempt to
create a record that matches an existing record, request updates any modified fields and returns the existing record.

Note: After faster account sharing recalculation is enabled for your org, we no longer store implicit share records between accounts
and their child case records. Sharing entries that have a value of `ImplicitChild` in the `RowCause` field aren’t returned
when you query this object. Instead, the system dynamically determines whether users can access child case records when they
try to access them. This change speeds up ownership and sharing recalculation for accounts.

[For more information, see the Faster Account Sharing Recalculation knowledge article.](https://help.salesforce.com/s/articleView?id=000394638&type=1&language=en_US)

SEE ALSO:

AccountShare

LeadShare

OpportunityShare

### CaseSolution

Represents the association between a Case and a Solution.


Standard Objects CaseSolution

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
CaseId

IsDeleted

SolutionId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the Case associated with the Solution.

This is a relationship field.

**Relationship Name**
Case

**Relationship Type**
Lookup

**Refers To**
Case

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
Create, Filter, Group, Sort

**Description**
Required. ID of the Solution associated with the case.

This is a relationship field.

**Relationship Name**
Solution

**Relationship Type**
Lookup

**Refers To**
Solution


### Standard Objects CaseStatus

Usage

You can't update this object via the API. If you attempt to create a record that matches an existing record, the request simply returns
the existing record.

SEE ALSO:

CaseShare

SolutionStatus

### CaseStatus

Represents the status of a Case, such as New, On Hold, or In Process.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ApiName

IsClosed

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
Indicates whether this case status value represents a closed Case ( `true` ) or not ( `false` ).
Multiple case status values can represent a closed Case.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


### Standard Objects CaseSubjectParticle

**Field** **Details**

**Description**
Indicates whether this is the default case status value ( `true` ) or not ( `false` ) in the picklist.

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
Label for this case status value. This display value is the internal label that does not get
translated.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number used to sort this value in the case status picklist. These numbers are not guaranteed
to be sequential, as some previous case status values might have been deleted.

This object represents a value in the case status picklist. The case status picklist provides additional information about the status of a
Case, such as whether a given `Status` value represents an open or closed case. Query the CaseStatus object to retrieve the set of
values in the case status picklist, and then use that information while processing Case records to determine more information about a
given case. For example, the application could test whether a given case is open or closed based on its `Status` value and the value
of the `IsClosed` property in the associated CaseStatus object.

SEE ALSO:

Overview of Salesforce Objects and Fields

### CaseSubjectParticle

Represents the Social Business Rules custom format for the **Case Subject** field on cases created from inbound social posts. This object
is available in API version 41.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects CaseSubjectParticle

Fields

**Field** **Details**

```
DeveloperName

Index

Language

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name for the CaseSubjectParticle object.

This name can contain only underscores and alphanumeric characters, and must be unique
in your org. It must begin with a letter, not include spaces, not end with an underscore, and
not contain two consecutive underscores. This field is automatically generated, but you can
supply your own value if you create the record using the API.

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance may slow while
Salesforce generates one for each record.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
int

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. The order in which the custom **Case Subject** is generated, meaning if the social
network is 0 and the social message is 1, then the subject generates as `Twitter |`
`Tweet` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the case subject field.

Possible values are:

**•** `ar` —Arabic

**•** `da` —Danish

**•** `de` —German

**•** `en_US` —English

**•** `es` —Spanish

**•** `es_MX` —Spanish (Mexico)


Standard Objects CaseSubjectParticle

**Field** **Details**

**•** `fi` —Finnish

**•** `fr` —French

**•** `it` —Italian

**•** `iw` —Hebrew

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

TextField

Type

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label for the case subject field.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies inbound social content added to **Case Subject** in case records.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. Specifies the custom **Case Subject** format from which inbound social content
appears in case records.

Possible values are:

**•** `ColonSeparator`

**•** `Content` —Message

**•** `HyphenSeparator`


### Standard Objects CaseTag

**Field** **Details**

**•** `MessageType`

**•** `PipeSeparator`

**•** `ProvidedString`

**•** `RealName`

**•** `Sentiment`

**•** `SocialHandle`

**•** `SocialNetwork`

**•** `Source`

Usage

In the Salesforce UI, case subjects are brief descriptions of cases. They are what agents see on cases first. Social Business Rules specify
the brief descriptions of cases created from social posts. Using CaseSubjectParticle objects you can build your own case subject format,
where each object represents a social post's component. For example, combining CaseSubjectParticle objects with components for
types `MessageType`, `RealName`, and `SocialNetwork` results in "Tweet Customer123 Twitter".

### CaseTag

Associates a word or short phrase with a Case

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
ItemId

Name

```

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


### Standard Objects CaseTeamMember

**Field Name** **Details**

**Description**
Name of the tag. If this value does not already exist, a new TagDefinition is created and
becomes the parent of this Tag object. Otherwise, a TagDefinition with the same name
becomes the parent of this Tag object. Parent relationships are created automatically.

```
TagDefinitionId

Type

```

Usage

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

CaseTag stores the relationship between its parent TagDefinition and the Case being tagged. Tag objects act as metadata, allowing users
to describe and organize their data.

When a tag is deleted, its parent TagDefinition will also be deleted if the name is not being used; otherwise, the parent remains. Deleting
a TagDefinition sends it to the Recycle Bin, along with any associated tag entries.

### CaseTeamMember

Represents a case team member, who works with a team of other users to help resolve a case.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
upsert()

```


Standard Objects CaseTeamMember

Special Access Rules

As of Spring ’20 and later, only users with read access to the Case object can access this object.

When accessing from Apex code, use the `WITH USER_MODE` clause to enable field-level and object-level security permissions checking
for `SOQL SELECT` [queries, including subqueries and cross-object relationships. See Enforce User Mode for Database Operations.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_enforce_usermode.htm)

Fields

**Field** **Details**

```
MemberId

ParentId

TeamRoleId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the user or contact who is a member on a case team.

This is a polymorphic relationship field.

**Relationship Name**
Member

**Relationship Type**
Lookup

**Refers To**
Contact, User

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the case with which the case team member is associated.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Case

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects CaseTeamMember

**Field** **Details**

**Description**
The ID of the case team role with which the case team member is associated.

This is a relationship field.

**Relationship Name**
TeamRole

**Relationship Type**
Lookup

**Refers To**
CaseTeamRole

```
TeamTemplateId

TeamTemplateMemberId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the predefined team with which the case team member is associated.

This is a relationship field.

**Relationship Name**
TeamTemplate

**Relationship Type**
Lookup

**Refers To**
CaseTeamTemplate

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the team member included in a predefined case team.

This is a relationship field.

**Relationship Name**
TeamTemplateMember

**Relationship Type**
Lookup

**Refers To**
CaseTeamTemplateMember


### Standard Objects CaseTeamRole CaseTeamRole

Represents a case team role. Every case team member has a role on a case, such as “Customer Contact” or “Case Manager.”

Supported Calls

`create()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

As of Spring ’20 and later, only users with read access to the Case object can access this object.

Fields

**Field** **Details**

```
AccessLevel

Name

PreferencesVisibleInCSP

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A value that represents the type of access granted to the target Group for cases. The possible
values are:

**•** `None`

**•** `Read`

**•** `Edit`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the case team role.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether or not the case team role is visible to Customer Portal users.


### Standard Objects CaseTeamTemplate CaseTeamTemplate

Represents a predefined case team, which is a group of users that helps resolve a case.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Special Access Rules

As of Spring ’20 and later, only users with read access to the Case object can access this object.

Fields

**Field** **Details**

```
Description

Name

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A text description of the predefined case team.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the predefined case team.

### CaseTeamTemplateMember

Represents a member on a predefined case team, which is a group of users that helps resolve cases.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
upsert()

```

Special Access Rules

As of Spring ’20 and later, only users with read access to the Case object can access this object.


### Standard Objects CaseTeamTemplateRecord

Fields

**Field** **Details**

```
MemberId

TeamRoleId

TeamTemplateId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the user or contact who is a team member on a predefined case team.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the predefined case team member's case team role.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the predefined case team's template.

### CaseTeamTemplateRecord

The CaseTeamTemplateRecord object is a linking object between the Case and CaseTeamTemplate objects. To assign a predefined case
team to a case (customer inquiry), create a CaseTeamTemplateRecord record and point the `ParentId` to the case and the
`TeamTemplateId` to the predefined case team.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

As of Spring ’20 and later, only users with read access to the Case object can access this object.


### Standard Objects CategoryData

Fields

**Field** **Details**

```
ParentId

TeamTemplateId

### CategoryData

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the case with which the case team template record is associated.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Case

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the predefined case team with which the case team template record is associated.

This is a relationship field.

**Relationship Name**
TeamTemplate

**Relationship Type**
Lookup

**Refers To**
CaseTeamTemplate

Represents a logical grouping of Solution records.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
upsert()

```


Standard Objects CategoryData

Special Access Rules

Customer Portal users can't access this object.

Fields

**Field** **Details**

```
 CategoryNodeId

 IsDeleted

 RelatedSobjectId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the CategoryNode associated with the solution.

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
Create, Filter, Group, Sort, Update

**Description**
ID of the solution related to the category.

This object allows you to assign one or more categories to a Solution. It is an intermediate data table with two foreign keys that defines
the relationship between a CategoryNode and a Solution record.

CategoryData has two foreign keys:

**•** The first foreign key, `CategoryNodeId`, refers to the ID of a CategoryNode.

**•** The other foreign key, `RelatedSobjectId`, refers to a Solution ID.

This is a many-to-many relationship, so there can be multiple rows returned with a `CategoryNodeId` . A Solution can be associated
with multiple categories.

SEE ALSO:

Overview of Salesforce Objects and Fields


### Standard Objects CategoryNode CategoryNode

Represents a tree of Solution categories.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Special Access Rules

**•** Customer Portal users can't access this object.

**•** Attempting to delete a CategoryNode that has children (referred by CategoryNode.Parent), or is referred to elsewhere, causes a
failure.

Fields

**Field** **Details**

```
MasterLabel

ParentId

SortOrder

SortStyle

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label for the category node.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the parent of this node, if any.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the sort order of child CategoryNode objects.

**Type**
picklist


### Standard Objects CategoryNodeLocalization

**Field** **Details**

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates whether the sort order is alphabetical or custom.

Usage

A CategoryNode defines a category of solutions. In the user interface, you can edit category definitions from Setup by entering _`Solution`_
_`Categories`_ in the `Quick Find` box, then selecting **Solution Categories** .

SEE ALSO:

CategoryData

Solution

### CategoryNodeLocalization

When the Translation Workbench is enabled for your organization, the CategoryNodeLocalization object provides the translation of the
label of a solution category.

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
CategoryNodeId

```

**Type**
reference

**Properties**
Create, Filter, Nillable

**Description**
The ID of the solution CategoryNode that is being translated.


Standard Objects CategoryNodeLocalization

**Field** **Details**

```
LanguageLocaleKey

Language

```

**Type**
picklist

**Properties**
Create, Filter, Nillable, Restricted picklist

**Description**

This field is available in API version 16.0 and earlier. It is the same as the `Language`
field.

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

**•** Bulgarian: `bg`


Standard Objects CategoryNodeLocalization

**Field** **Details**

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

**•** Armenian: `hy`


Standard Objects CategoryNodeLocalization

**Field** **Details**

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

**•** German (Switzerland): `de_CH`


Standard Objects CategoryNodeLocalization

**Field** **Details**

**•** Greek (Cyprus): `el_CY`

**•** Greenlandic: `kl`

**•** Gujarati: `gu`

**•** Hawaiian: `haw`

**•** Haitian Creole: `ht`

**•** Hindi: `hi`

**•** Hmong: `hmn`

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

**•** Punjabi: `pa`

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


Standard Objects CategoryNodeLocalization

**Field** **Details**

**•** Spanish (Chile): `es_CL`

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

**•** Yiddish: `ji`

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


### Standard Objects ChangeRequest

**Field** **Details**

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix
of the org for all objects that support it, unless an object is in an installed managed
package. In that case, the object has the namespace prefix of the installed
managed package. This field’s value is the namespace prefix of the Developer
Edition org of the package developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set only
for objects that are part of an installed managed package. All other objects have
no namespace prefix.

```
 Value

```

Usage

**Type**
string

**Properties**
Create, Filter, Nillable, Update

**Description**
The actual translated label for the solution category. Label is **Translation** .

Use this object to translate the labels of your solution categories into a supported language. Users with the Translation Workbench
enabled can view category node translations, but either the “Customize Application,” “Manage Translation,” or “Manage Categories”
permission is required to create or update category node translations.

SEE ALSO:

ScontrolLocalization

WebLinkLocalization

### ChangeRequest

Represents a decision to implement a formal request for a change (RFC). This object is available in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
BusinessJustification

```

**Type**
textarea


Standard Objects ChangeRequest

**Field** **Details**

**Properties**
Create, Nillable, Update

**Description**
A description of the business reason to implement the change. This field can store up to 32
KB of data, but only the first 255 characters display in reports.

```
BusinessReason

Category

ChangeRequestNumber

ChangeType

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The core reason for creating the change request.

Possible values are:

**•** `t2`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of change request. Administrators set field values.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The unique, system-generated change request number.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of change request. Administrators set field values.

Possible values are:

**•** `Emergency`

**•** `Major`

**•** `Normal`

**•** `Standard`


Standard Objects ChangeRequest

**Field** **Details**

```
Description

EstimatedEndTime

EstimatedStartTime

FinalReviewDateTime

FinalReviewNotes

Impact

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the change request. This field can store up to 32 KB of data, but only the
first 255 characters display in reports.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time (in UTC) when the change request is estimated to be implemented.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The estimated date and time (in UTC) when the change request is implemented.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time (in UTC) when the change request was reviewed.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Notes left by the change request reviewer. This field can store up to 32 KB of data, but only
the first 255 characters display in reports.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects ChangeRequest

**Field** **Details**

**Description**
Shows the impact of a requested change.

Possible values are:

**•** `High`

**•** `Low`

**•** `Medium`

The default value is 'High'.

```
LastReferencedDate

LastViewedDate

OwnerId

Priority

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
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
A polymorphic relationship field that represents the user or group assigned as the change
reviewer.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
picklist


Standard Objects ChangeRequest

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The impact and urgency of a requested change.

Possible values are:

**•** `Critical`

**•** `High`

**•** `Low`

**•** `Moderate`

The default value is 'Critical'.

```
RemediationPlan

ReviewerId

RiskImpactAnalysis

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the steps required to resolve the incident. This field can store up to 32 KB
of data, but only the first 255 characters display in reports.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the user who reviewed the change request.

This is a relationship field.

**Relationship Name**
Reviewer

**Relationship Type**
Lookup

**Refers To**
User

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
An assessment of the risk involved with the implementation of the change request.
Administrators set field values, and each value can have up to 20 characters.


Standard Objects ChangeRequest

**Field** **Details**

```
RiskLevel

Status

StatusCode

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The risk level associated with adopting the requested change.

Possible values are:

**•** `High`

**•** `Low`

**•** `Medium`

The default value is 'High'.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Represents any custom or granular stages a customer may want to track. This will be a
dependent picklist.

Possible values are:

**•** `Approved`

**•** `Canceled`

**•** `Closed`

**•** `Implementing`

**•** `New`

**•** `Open`

**•** `Planning`

**•** `Rejected`

**•** `Reviewed`

**•** `Scheduled`

The default value is 'New'.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of the change.

Possible values are:


### Standard Objects ChangeRequestRelatedIssue

**Field** **Details**

**•** `Approved`

**•** `Canceled`

**•** `Closed`

**•** `Implementing`

**•** `New`

**•** `Open`

**•** `Planning`

**•** `Rejected`

**•** `Reviewed`

**•** `Scheduled`

The default value is 'New'.

```
Subject

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
A brief description of the requested change.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ChangeRequestChangeEvent on page 68 (API version 59.0)**
Change events are available for the object.

**ChangeRequestFeed on page 55**
Feed tracking is available for the object.

**ChangeRequestHistory on page 63**
History is available for tracked fields of the object.

**ChangeRequestOwnerSharingRule on page 65**
Sharing rules are available for the object.

**ChangeRequestShare on page 67**
Sharing is available for the object.

### ChangeRequestRelatedIssue

Represents a junction object that relates a ChangeRequest to an Incident or Problem due to a service failure. This object is available in
API version 53.0 and later.


Standard Objects ChangeRequestRelatedIssue

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ChangeRequestId

Name

RelatedEntityType

RelatedIssueId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ChangeRequest ID that's linked to the Problem or Incident.

**Relationship Name**
ChangeRequest

**Relationship Type**
Lookup

**Refers To**
ChangeRequest

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
A description of the change request as it relates to the problem or incident.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The name of the related object type.

Possible values are:

**•** `Incident`

**•** `Problem`

**Type**
reference

**Properties**
Create, Filter, Group, Sort


### Standard Objects ChangeRequestRelatedItem

**Field** **Details**

**Description**
A polymorphic relationship field that represents the related Problem or Incident.

**Relationship Name**
RelatedIssue

**Relationship Type**
Lookup

**Refers To**
Incident, Problem

```
RelationshipType

```

Associated Objects

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Shows how the ChangeRequest and Incident or Problem records relate to each other.

Possible values are:

**•** `Caused By`

**•** `Fixed By`

The default value is 'Caused By'.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ChangeRequestRelatedIssueChangeEvent on page 68**
Change events are available for the object.

**ChangeRequestRelatedIssueFeed on page 55**
Feed tracking is available for the object.

**ChangeRequestRelatedIssueHistory on page 63**
History is available for tracked fields of the object.

### ChangeRequestRelatedItem

Represents a junction object that relates a ChangeRequest to an Asset. This object is available in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`


Standard Objects ChangeRequestRelatedItem

Fields

**Field** **Details**

```
AssetId

ChangeRequestId

Comment

ImpactLevel

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The Asset ID that’s linked to the ChangeRequest.

This field is a relationship field.

**Relationship Name**
Asset

**Relationship Type**
Lookup

**Refers To**
Asset

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ChangeRequest ID that’s linked to the Asset.

This field is a relationship field.

**Relationship Name**
ChangeRequest

**Relationship Type**
Lookup

**Refers To**
ChangeRequest

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the change request as it relates to the item.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update


Standard Objects ChangeRequestRelatedItem

**Field** **Details**

**Description**
The related item's impact on the change request.

Possible values are:

**•** `High`

**•** `Low`

**•** `Medium`

The default value is `High` .

```
Name

RelationshipType

```

Associated Objects

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The auto-generated ID of the item that's related to the change request.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Shows how the ChangeRequest and Asset records relate to each other.

Possible values are:

**•** `Broke Item`

**•** `Fixed Item`

The default value is `Broke Item` .

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ChangeRequestRelatedItemChangeEvent on page 68**
Change events are available for the object.

**ChangeRequestRelatedItemFeed on page 55**
Feed tracking is available for the object.

**ChangeRequestRelatedItemHistory on page 63**
History is available for tracked fields of the object.


### Standard Objects ChangeSetOperationEventLog ChangeSetOperationEventLog

Change Set Operation events contain information from change set migrations. This object is available in API version 65.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
ChangeSetName

ClientIp

CpuTime

LoginKey

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the change set.

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

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ChangeSetOperationEventLog

**Field** **Details**

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring.

```
OperationType

RequestIdentifier

RunTime

SessionKey

TargetOrganizationIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The operation that’s being performed.

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

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the organization that’s receiving the change set.


### Standard Objects ChannelObjectLinkingRule

**Field** **Details**

```
Timestamp

Uri

UserIdentifier

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp at which the log event was generated.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
URI of the page receiving the request.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.
For example: `00530000009M943` .

### ChannelObjectLinkingRule

Represents a rule for linking a channel interaction with an object (such as Lead or Contact). This object is available in API version 47.0
and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ActionForNoRecordFound

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects ChannelObjectLinkingRule

**Field** **Details**

**Description**
Action to take when no matching records are found.

Possible values are:

**•** `CreateNewRecordAndLink` —Create Record and Link (Recommended)

**•** `PromptAgent` —Prompt Agent

```
ActionForSingleRecordFound

ChannelType

Description

DeveloperName

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Action to take when one matching record is found.

Possible values are:

**•** `AutoLink` —Auto-Link Record (Recommended)

**•** `PromptAgent` —Prompt Agent

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of channel used for this rule.

Possible values are:

**•** `FacebookMessenger`

**•** `Phone`

**•** `Text`

**•** `WeChat`

**•** `WhatsApp`

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description for this linking rule.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects ChannelObjectLinkingRule

**Field** **Details**

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance may slow while
Salesforce generates one for each record.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

```
IsLinkedRecordOpenedAsSubTab

IsRuleActive

Language

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether to open the linked record as a subtab when the link is established.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the rule is active.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language for this linking rule.

Possible values are:

**•** `ar` —Arabic

**•** `bg` —Bulgarian

**•** `cs` —Czech

**•** `da` —Danish

**•** `de` —German

**•** `el` —Greek

**•** `en_GB` —English (UK)


Standard Objects ChannelObjectLinkingRule

**Field** **Details**

**•** `en_US` —English

**•** `es` —Spanish

**•** `es_MX` —Spanish (Mexico)

**•** `fi` —Finnish

**•** `fr` —French

**•** `hr` —Croatian

**•** `hu` —Hungarian

**•** `in` —Indonesian

**•** `it` —Italian

**•** `iw` —Hebrew

**•** `ja` —Japanese

**•** `ko` —Korean

**•** `nl_NL` —Dutch

**•** `no` —Norwegian

**•** `pl` —Polish

**•** `pt_BR` —Portuguese (Brazil)

**•** `pt_PT` —Portuguese (European)

**•** `ro` —Romanian

**•** `ru` —Russian

**•** `sk` —Slovak

**•** `sl` —Slovene

**•** `sv` —Swedish

**•** `th` —Thai

**•** `tr` —Turkish

**•** `uk` —Ukrainian

**•** `vi` —Vietnamese

**•** `zh_CN` —Chinese (Simplified)

**•** `zh_TW` —Chinese (Traditional)

```
MasterLabel

ObjectToLink

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique label name for this rule.

**Type**
picklist


### Standard Objects ChannelProgram

**Field** **Details**

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of object to link to the channel interaction.

Possible values are:

**•** `Contact`

```
 RuleName

### ChannelProgram

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Name of the rule as it appears in the UI. Maximum length is 80 characters.

Represents a channel program that vendors use to market and sell their products through channel partners. This object is available in
API version 41.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
Category

Description

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Category of the channel program. Categories group channel programs by type.
For example, a reseller category would include all the different regional reseller
channel programs.

**Type**
textarea


Standard Objects ChannelProgram

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the channel program.

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
Indicates whether the channel program is active. New channel programs are
inactive by default.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related
to this record, or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, the user might have only accessed this record or list view
( `LastReferencedDate` ) but not viewed it.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Name of the channel program.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


### Standard Objects ChannelProgramLevel

**Field Name** **Details**

**Description**
ID of the owner of the channel program.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ChannelProgramFeed**

Feed tracking is available for the object.

**ChannelProgramHistory**

History is available for tracked fields of the object.

**ChannelProgramOwnerSharingRule**

Sharing rules are available for the object.

**ChannelProgramShare**

Sharing is available for the object.

### ChannelProgramLevel

Represents a level, based on member experience, in a channel program. This object is available in API version 41.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
Description

LastReferencedDate

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the channel program level.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects ChannelProgramLevel

**Field Name** **Details**

**Description**
The timestamp when the current user last accessed this record, a record related
to this record, or a list view.

```
LastViewedDate

Name

OwnerId

ProgramId

Rank

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, the user might have only accessed this record or list view
( `LastReferencedDate` ) but not viewed it.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the channel program level.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Required. ID of the user who is the owner of the record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the channel program.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An integer associated with the level. For example, 1 represents the lowest level,
2 the next level up, etc.


### Standard Objects ChannelProgramMember

**Field Name** **Details**

```
RecordTypeId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
ID of the record type assigned to this object.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ChannelProgramLevelFeed**

Feed tracking is available for the object.

**ChannelProgramLevelHistory**

History is available for tracked fields of the object.

**ChannelProgramLevelOwnerSharingRule**

Sharing rules are available for the object.

**ChannelProgramLevelShare (API version 43.0)**
Sharing is available for the object.

### ChannelProgramMember

Represents a partner who is a member of a channel program. This object is available in API version 41.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
LastReferencedDate

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Most recent date referenced. This field is available in API version 45.0 and later.


Standard Objects ChannelProgramMember

**Field Name** **Details**

```
LastViewedDate

LevelId

Name

OwnerId

PartnerId

ProgramId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Most recent date viewed. This field is available in API version 45.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the channel program level.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the channel program member.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Required. ID of the user who is the owner of the record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the partner.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the channel program.


### Standard Objects ChatterActivity

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ChannelProgramMemberFeed (API version 46.0)**
Feed tracking is available for the object.

**ChannelProgramMemberHistory (API version 46.0)**
History is available for tracked fields of the object.

**ChannelProgramMemberOwnerSharingRule**

Sharing rules are available for the object.

**ChannelProgramMemberShare (API version 43.0)**
Sharing is available for the object.

### ChatterActivity ChatterActivity represents the number of posts and comments made by a user and the number of comments and likes on posts and

comments received by the same user. This object is available in API version 23.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
CommentCount

CommentReceivedCount

InfluenceRawRank

```

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of FeedComments made by the ParentId.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of FeedComments received by the ParentId.

**Type**
int

**Properties**
Filter, Group, Sort


Standard Objects ChatterActivity

**Field Name** **Details**

**Description**
Number indicating the ParentId’s Chatter influence rank, which is calculated based
on the ParentId’s ChatterActivity statistics, relative to the other users in the
organization. This field is available in API version 26.0 and later.

```
LikeReceivedCount

NetworkId

ParentId

PostCount

```

Usage

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of FeedLikes received by the ParentId.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the Experience Cloud site to which the ChatterActivity belongs. This field is
available only if digital experiences is enabled in your org. This field is available in API
version 26.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the object type to which the ChatterActivity is related. In API version 66.0, the
`ParentId` must be a `UserId` or SelfServiceUser ID.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of FeedItems made by the ParentId.

**•** Use this object to reference the Chatter activity statistics, which include the number of posts and comments made by a user and
the number of comments and likes on posts and comments received by the same user.


### Standard Objects ChatterAnswersActivity

**•** You can directly query for ChatterActivity.

```
     SELECT Id, PostCount, LikeReceivedCount

     FROM ChatterActivity

     WHERE ParentId = UserId

```

Note: To query ChatterActivity, you must provide the `ParentId` . In API version 66.0, the `ParentId` must be a `UserId`
or SelfServiceUser ID.

**•** A ChatterActivity record is created for users the first time they post or comment. Users who have never posted or commented don’t
have ChatterActivity records. If users make only one post and then delete it, they do have ChatterActivity records. In both cases, the
user interface displays zeros for their Chatter activity.

**•** Use the `InfluenceRawRank` field to reference a user’s Chatter influence rank. This field is available in API version 26.0 and later.

SEE ALSO:

FeedItem

FeedComment

FeedLike

### ChatterAnswersActivity

Represents the reputation of a User in Chatter Answers zones.This object is available in API version 25.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
BestAnswerReceivedCount

BestAnswerSelectedCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of best answers the User has received from other users.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of best answers the User has selected.


Standard Objects ChatterAnswersActivity

**Field Name** **Details**

```
QuestionsCount

QuestionSubscrCount

QuestionSubscrReceivedCount

QuestionUpVotesCount

QuestionUpVotesReceivedCount

RepliesCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of Question records posted by the User.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of Question records the User has selected to follow.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of users following Question records posted by the User.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of up votes the User has marked on Question records posted by
other users.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of up votes the User has received from other users on the Question
records he or she has posted.

**Type**
int


Standard Objects ChatterAnswersActivity

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of Reply records posted by the User.

```
ReplyDownVotesCount

ReplyDownVotesReceivedCount

ReplyUpVotesCount

ReplyUpVotesReceivedCount

ReportAbuseOnQuestionsCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of down votes the User has marked on Reply records posted by
other users.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of down votes the User has received from other users on the Reply
records he or she has posted.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of up votes the User has marked on the Reply records posted by
other users.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of up votes the User has received from other users on the Reply
records he or she has posted.

**Type**
int


Standard Objects ChatterAnswersActivity

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of abuses that the User has reported on Question records posted
by other users.

```
ReportAbuseOnRepliesCount

ReportAbuseReceivedOnQnCount

ReportAbuseReceivedOnReCount

UserId

CommunityId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of abuses that the User has reported on Reply records posted by
other users.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of abuses reported by other users on the Question records posted
by the User.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

the number of abuses reported by other users on the Reply records posted by
the User.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The User ID associated with this reputation.

**Type**
reference


### Standard Objects ChatterAnswersReputationLevel

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**

The ID for the zone associated with this reputation.

Usage

Use this object to view metrics on User activity in Chatter Answers. For example, you can use the ChatterAnswersActivity object to view
the number of Question records a user is following in Chatter Answers zones.

SEE ALSO:

Question

Reply

User

### ChatterAnswersReputationLevel

Represents a reputation level within a Chatter Answers zone. This object is available in API version 26.0 and later.

Note: With the Spring ’18 release, Salesforce no longer supports Chatter Answers. Users of Chatter Answers can post, answer,
comment, or view existing Chatter Answers data, but support and updates are scheduled to end. We recommend transitioning
[to Chatter Questions. For more information, see End of Support for Chatter Answers in Spring ’18.](https://help.salesforce.com/apex/HTViewSolution?urlname=Chatter-Answers-to-Retire-in-Spring-18)

Supported Calls

`create()`, `delete()`, `query()`, `retrieve()`, `update()`

Fields

**Field** **Details**

```
CommunityID

Name

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

ID of the zone for which you’re creating the reputation level.

**Type**
string


### Standard Objects ChatterConversation

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**

Name of the reputation level.

```
Value

```

Usage

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**

Minimum number of points for this level.

Use to create or edit reputation levels for the zone.

### ChatterConversation

Represents a private conversation in Chatter, consisting of messages that conversation members have sent or received. This object is
available in API version 23.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
Id

```

**Type**
ID

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
ID of the conversation.


### Standard Objects ChatterConversationMember

Usage

Use this object to identify private conversations in Chatter. Users can access this object if they have the Manage Chatter Messages and
Direct Messages permission. This object is read-only via the API and is provided only to allow administrators to view users' Chatter
messages; for example, for compliance purposes.

SEE ALSO:

### ChatterConversationMember

ChatterMessage

### ChatterConversationMember

Represents a member of a private conversation in Chatter. A member has either sent messages to or received messages from other
conversation participants. This object is available in API version 23.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
ConversationId

MemberId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the associated ChatterConversation.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the conversation member.


### Standard Objects ChatterExtension

Usage

Use this object to view members of private conversations in Chatter. Users can access this object if they have the Manage Chatter
Messages and Direct Messages permission. This object is read-only via the API and is provided only to allow administrators to view users'
Chatter messages; for example, for compliance purposes.

SEE ALSO:

ChatterConversation

ChatterMessage

### ChatterExtension

Represents a Rich Publisher App that’s integrated with the Chatter publisher. This object is available in API version 41.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CompositionComponentEnumOrId

Description

DeveloperName

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The ID of the composition component for the Rich Publisher App. This field requires a value.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The description of your custom Rich Publisher App. This field requires a value.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the developer who is responsible for the app.


Standard Objects ChatterExtension

**Field** **Details**

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

```
ExtensionName

HeaderText

HoverText

IconId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of your extension. This field requires a value.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The text to show in the header of your app composer. Header text is required for Lightning
type extensions.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The text to show when a user mouses over your extension’s icon. Mouse-over text is required
for Lightning type extensions.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The icon to show in the Chatter publisher. Use an existing file asset ID from your org. This
field requires a value.

This is a relationship field.

**Relationship Name**
Icon

**Relationship Type**
Lookup

**Refers To**
ContentAsset


Standard Objects ChatterExtension

**Field** **Details**

```
IsProtected

Language

MasterLabel

NamespacePrefix

RenderComponentEnumOrId

Type

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
An auto-generated value. It currently has no impact.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language used for this instance of the `ChatterExtension` . This field requires a
value.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The master label for the `ChatterExtension` object. This field requires a value.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The prefix to use for the extension’s namespace.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The rendering component of the Rich Publisher App that you provide. It’s comprised of the
`lightning:availableForChatterExtensionRenderer` interface. This field
requires a value.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


### Standard Objects ChatterExtensionConfig

**Field** **Details**

**Description**
Describes the type of the extension. Currently, the only value supported is _`Lightning`_ .
Included to allow for other possible types in the future.

### ChatterExtensionConfig

Configuration for the Chatter extension for Experience Cloud sites. This object is available in API version 41.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CanCreate

CanRead

ChatterExtensionId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
### Determines whether the ChatterExtension can create an instance that appears by

rendering.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
### Determines whether the ChatterExtension can be viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
### The ID of the ChatterExtension .

This is a relationship field.

**Relationship Name**
### ChatterExtension


### Standard Objects ChatterMessage

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
ChatterExtension

```
NetworkId

Position

### ChatterMessage

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Experience Cloud site where the `ChatterExtension` is deployed.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The position of the `ChatterExtension` icon in the Chatter publisher.

Represents a message sent as part of a private conversation in Chatter. This object is available in API version 23.0 and later.

Supported Calls

`delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`

Fields

**Field Name** **Details**

```
Body

ConversationId

```

**Type**
textarea

**Properties**
Update

**Description**
Text of the message.

**Type**
reference


Standard Objects ChatterMessage

**Field Name** **Details**

**Properties**
Filter, Group, Sort

**Description**
ID of the conversation that the message is associated with.

```
SenderId

SenderNetworkId

SentDate

```

Usage

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the sender.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the Experience Cloud site from which the message was sent. This field is
available only if digital experiences is enabled in your org.

This field is available in API version 32.0 and later.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
Date the message was sent.

Use this object to view and delete messages sent or received via private conversations in Chatter. Users can access this object if they
have the Manage Chatter Messages and Direct Messages permission. Users with the Moderate Experiences Chatter Messages permission
can access this object in Experience Cloud sites they’re a member of, only if the message has been flagged as inappropriate. This object
is provided to allow administrators to view and delete users’ Chatter messages, for example, for compliance purposes.

Messages are hard deleted. That is, they’re removed completely without a trip to the Recycle Bin.

Deleting a message that resulted from sharing a file with someone doesn’t also delete the file.

SEE ALSO:

ChatterConversation

ChatterConversationMember


### Standard Objects ClientBrowser ClientBrowser

Represents a cookie added to the browser upon login, and also includes information about the browser application where the cookie
was inserted. This object is available in version 28.0 and later.

Supported Calls

`describeSObjects()`, `delete()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
FullUserAgent

LastUpdate

ProxyInfo

UsersId

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Detailed information about the client (browser). For example, `Mozilla/5.0`

```
  (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.1)

  Gecko/2008070208 Firefox/3.0.1

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Represents the last time the cookie was changed.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The browser’s current proxy information.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user associated with this item.

This is a relationship field.


### Standard Objects CollaborationGroup

**Field** **Details**

**Relationship Name**
Users

**Relationship Type**
Lookup

**Refers To**
User

Usage

At every login, the device the login request is from is checked against the known devices using ClientBrowser. A match means a cookie
was found on the browser that matches an entry in the ClientBrowser table, so the device is known. No match means that no matching
cookie was found, so the device is unknown, and the user is asked to confirm their identity.

### CollaborationGroup

Represents a Chatter group. This object is available in API version 19.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `search()`, `update()`,

```
   upsert()

```

Special Access Rules

The visibility of information in groups depends on the type of group and the user’s permissions.

**•** **Members** : Any user with the Create and Own New Chatter Groups permission can create public, private, and unlisted groups,
including in any Experience Cloud sites they belong to.

**•** **Owners and managers** : Users can modify group details for any group they own or manage. Owners can also delete groups they
own.

**•** **Nonmembers** : These user permissions allow group access regardless of group membership.

**–** View All Data—Allows users to view all public and private groups across their org and its Experience Cloud sites. Users with this
permission can’t view unlisted group information, unless they have the Modify Unlisted Groups permission as well.

**–** Modify All Data—Allows users to view, modify, and delete all public and private groups across their org and its Experience Cloud
sites. Users with this permission can’t view or modify unlisted group information, unless they have the Manage Unlisted Groups
permission as well.

**–** Create and Set Up Experiences—Allows users to view, modify, and delete all public and private groups in Experience Cloud sites.

**–** Manage Unlisted Groups—Allows users to search for, access, and modify any unlisted group in an org and its Experience Cloud
sites.

**–** Data Export—Allows users to export any data from Salesforce, including private and unlisted group data from an org and its
Experience Cloud sites.


Standard Objects CollaborationGroup

**•** **Apex and Visualforce** : Apex code runs in system mode, which means that the permissions of the current user aren’t taken into
account.

**–** Visualforce pages that display groups might expose unlisted or private group data to users who aren’t members.

**–** Because system mode disregards the user’s permissions, all users who are accessing a Visualforce page that’s showing a group
can act as an owner of that group.

**–** AppExchange apps that are written in Apex and that access all groups will expose unlisted groups to users who aren’t members.

To limit and manage access to the unlisted and private groups in your org:

**•** Explicitly filter out unlisted and private group information from SOQL queries in all Apex code.

**•** Use permission sets, profile-level permissions, and sharing checks in your code to further limit group access.

**•** Use Apex triggers on the CollaborationGroup object to monitor and manage the creation of groups. In Setup, enter _`Group`_
_`Triggers`_ in the `Quick Find` box, then select **Group Triggers** to add triggers.

Fields

**Field** **Details**

```
AnnouncementId

BannerPhotoUrl

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Contains the ID of the Announcement last associated with the group. This field is available
in API version 30.0 and later.

This is a relationship field.

**Relationship Name**
Announcement

**Relationship Type**
Lookup

**Refers To**
Announcement

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
The URL for the group's banner photo.

The URL is updated every time a photo is uploaded and reflects the most recent photo. If a
newer photo has been uploaded, the URL returned for an older photo is not guaranteed to
return a photo. Query this field for the URL of the most recent photo.

This field is available in API version 36.0 and later.


Standard Objects CollaborationGroup

**Field** **Details**

```
CanHaveGuests

CollaborationType

Description

FullPhotoUrl

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If set to `true`, indicates that a group allows customers. Chatter customers are people outside
your company's email domains. Customers can see only the groups they're invited to. They
can interact only with members of those groups. Customers can’t see any Salesforce
information.

This field is available starting in API version 23.0, but groups that allow customers are
accessible from earlier API versions. However, when accessed from earlier API versions, groups
that allow customers aren't distinguishable from private groups. We strongly recommend
that you upgrade to the latest API version. If you must use an earlier version, name groups
that allow customers to indicate that they include customers.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of Chatter group. Available values are:

**•** `Public` —Anyone can see and post updates. Anyone can join a public group.

**•** `Private` —Only members can see the group feed and post updates. Non-members
can only see the group name and a few other details in list views, search, and on the
group page. The group's owner or managers must add members who request to join
the group.

**•** `Unlisted` —Only members and users with the Manage Unlisted Groups permission
can see the group and post updates. Other users can’t access the group or see it in lists,
search, and feeds.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Description of the group.

**Type**
url

**Properties**
Filter, Nillable, Sort


Standard Objects CollaborationGroup

**Field** **Details**

**Description**
The URL for the group's profile photo.

The URL is updated every time a photo is uploaded and reflects the most recent photo. If a
newer photo has been uploaded, the URL returned for an older photo is not guaranteed to
return a photo. Query this field for the URL of the most recent photo.

This field is available in API version 20.0 and later.

```
GroupEmail

HasPrivateFieldsAccess

InformationBody

InformationTitle

```

**Type**
email

**Properties**
Nillable, Sort

**Description**
The email address for posting to the group. For private groups, only visible to members and
users with Modify All Data or View All Data permissions.

This field is available in API version 29.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If set to `true`, indicates that a user can see the `InformationBody` and
`InformationTitle` fields in a private group. This field is set to `true` for members of
a private group and users with Modify All Data or View All Data permissions.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The text of the Information section. For private groups, only visible to members and users
with Modify All Data or View All Data permissions.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The title of the Information section. For private groups, only visible to members and users
with Modify All Data or View All Data permissions.


Standard Objects CollaborationGroup

**Field** **Details**

```
IsArchived

IsAutoArchiveDisabled

IsBroadcast

LastFeedModifiedDate

LastReferencedDate

LastViewedDate

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the group is archived ( `true` ) or not ( `false` ).

This field is available in API version 28.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether automatic archiving is disabled for the group ( `true` ) or not ( `false` ).

This field is available in API version 29.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the group is a broadcast group ( `true` ) or not ( `false` ).

This field is available in API version 36.0 and later.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date of the last post or comment on the group.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
datetime


Standard Objects CollaborationGroup

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced ( `LastReferencedDate` ) and not viewed.

```
MediumPhotoUrl

MemberCount

Name

NetworkId

OwnerId

```

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
The URL for the larger, cropped photo size.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of members in the group.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the group. Group names must be unique across public and private groups. Unlisted
groups don’t require unique names.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the Experience Cloud site that this group is part of. This field is available only if digital
experiences is enabled in your org.

You can only add a `NetworkId` when creating a group. You can’t change or add a
`NetworkId` for an existing group. This field is available in API version 26.0 and later.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects CollaborationGroup

**Field** **Details**

**Description**
ID of the owner of the group. Only the current group owner or people with the Modify All
Data permission can update the `OwnerId` .

This is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

```
SmallPhotoUrl

```

Usage

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
The URL for a thumbnail of the group's profile photo.

The URL is updated every time a photo is uploaded and reflects the most recent photo. If a
newer photo has been uploaded, the URL returned for an older photo is not guaranteed to
return a photo. Query this field for the URL of the most recent photo.

This field is available in API version 20.0 and later.

Use this object to create, edit, or delete groups in an org or Experience Cloud site. Deleting a group permanently deletes all posts and
comments to the group. It also deletes all files and links posted to the group and removes the files from other locations where they were
shared.

As a Chatter group member, you can post to the group using the CollaborationGroupFeed object. As a Chatter group owner or manager,
you can add or remove group members using the CollaborationGroupMember object, post announcements to the group using the
Announcement object, and accept or decline requests to join private groups using the CollaborationGroupMemberRequest object.
Additionally, the group owner, manager, or your Salesforce system administrator can invite people to join the group using the
CollaborationInvitation object.

The Salesforce system administrator doesn’t need to be a member of the group in order to send invitations using the API.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.


### Standard Objects CollaborationGroupMember

**CollaborationGroupFeed**

Feed tracking is available for the object.

SEE ALSO:

### CollaborationGroupMember CollaborationGroupMemberRequest CollaborationGroupMember

Represents a member of a Chatter group. This object is available in API version 19.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `describeLayout()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CollaborationGroupId

CollaborationRole

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the associated CollaborationGroup.

This is a relationship field.

**Relationship Name**
### CollaborationGroup

**Relationship Type**
Lookup

**Refers To**
### CollaborationGroup

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The role of a group member. Group owners and managers can change roles for members
of their groups. The valid values are:


Standard Objects CollaborationGroupMember

**Field** **Details**

**•** `Standard` —Indicates that a user is a group member. Members can post and comment
in the group.

**•** `Admin` —Indicates that a user is a group manager. Managers can post and comment,
change member roles, edit group settings, add and remove members, delete posts and
comments, and edit the group information field.

Note: To change the group owner, use the `OwnerId` field on the
CollaborationGroup object.

```
LastFeedAccessDate

MemberId

NotificationFrequency

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when a group member last accessed the group’s feed. The value is only
updated when a member explicitly consumes the group’s feed, not when the member sees
group posts in other feeds, like the profile feed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the group member.

This is a relationship field.

**Relationship Name**
Member

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Required. The frequency at which Salesforce sends Chatter group email digests to this
member. Can only be set by the member or users with the “Modify All Data” permission.
The valid values are:

**•** `D` —Daily

**•** `W` —Weekly


### Standard Objects CollaborationGroupMemberRequest

**Field** **Details**

**•** `N` —Never

**•** `P` —On every post

The default value is specified by the member in their Chatter email settings. In communities,
the `Email on every post` option is disabled once more than 10,000 members
choose this setting for the group. All members who had this option selected are automatically
switched to `Daily digests` .

Usage

Use this object to view, create, and delete Chatter group members. You must be a group owner or manager to create members for
private Chatter groups.

SEE ALSO:

### CollaborationGroup CollaborationGroupMemberRequest CollaborationGroupMemberRequest

Represents a request to join a private Chatter group. This object is available in API version 21.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CollaborationGroupId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the private Chatter group.

This is a relationship field.

**Relationship Name**
### CollaborationGroup

**Relationship Type**
Lookup


Standard Objects CollaborationGroupMemberRequest

**Field** **Details**

**Refers To**
CollaborationGroup

```
RequesterId

ResponseMessage

Status

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the user requesting to join the group; must be the ID of the context user.

This is a relationship field.

**Relationship Name**
Requester

**Relationship Type**
Lookup

**Refers To**
User

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Optional message to be included in the notification email when `Status` is `Declined` .

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the request. Available values are:

**•** `Accepted`

**•** `Declined`

**•** `Pending`

This object represents a request to join a private Chatter group, and can be used to accept or decline requests to join private groups you
own or manage. On create, an email is sent to the owner and managers of the private group to be accepted or declined. When the
`Status` is `Accepted` or `Declined`, an email is sent to notify the requester. When the `Status` is `Declined`, a
`ResponseMessage` is optionally included to provide additional details.


### Standard Objects CollaborationGroupRecord

Note the following when working with requests:

**•** Users with the “Modify All Data” or “View All Data” permission can view records for all groups, regardless of membership.

**•** A user can be a member of 300 groups. Requests to join groups count against this limit.

**•** `Status` can't be specified on create.

**•** You can only update a request when the `Status` is `Pending` .

**•** You can't delete or update a request with a `Status` of `Accepted` or `Declined` .

SEE ALSO:

### CollaborationGroup

CollaborationGroupMember

### CollaborationGroupRecord

Represents the records associated with Chatter groups.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CollaborationGroupId

NetworkId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the Chatter group.

This is a relationship field.

**Relationship Name**
### CollaborationGroup

**Relationship Type**
Lookup

**Refers To**
### CollaborationGroup

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects CollaborationInvitation

**Field** **Details**

**Description**
Optional. The ID of the Experience Cloud site that the group belongs to. Available from API
version 34.0.

```
RecordId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. The ID of the record associated with the Chatter group.

This is a polymorphic relationship field.

**Relationship Name**
Record

**Relationship Type**
Lookup

**Refers To**
Account, Campaign, Case, Contact, Contract, Lead, Opportunity

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CollaborationGroupRecordChangeEvent (API version 62.0)**
Change events are available for the object.

### CollaborationInvitation

Represents an invitation to join Chatter, either directly or through a group. This object is available in API version 21.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Invitations are available if “Allow Invitations” is enabled for your organization.

Invitations are limited to your allowed domain(s) unless the invite is sent from a private group that allows customers. Allowed domains
are set by the administrator.

Invitations to customers are available if “Allow Customer Invitations” is enabled for your organization. Users must have the “Invite
Customers to Chatter” permission to send invitations to people outside their Chatter domain.


Standard Objects CollaborationInvitation

Fields

**Field** **Details**

```
InvitedUserEmail

InvitedUserEmailNormalized

InviterId

OptionalMessage

ParentId

SharedEntityId

```

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The email address for the user invited to join Chatter. Label is `Invited Email` .

**Type**
email

**Properties**
Filter, Group, Sort

**Description**
A normalized version of the `InvitedUserEmail` entered. Label is `Invited Email`
`(Normalized)` .

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The person that initiated the invitation.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
An optional message from the person sending the invitation to the person receiving it.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Used when the email address on the invitation is different than the one entered when the
invitee accepts the invitation.

**Type**
reference


Standard Objects CollaborationInvitation

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the user or group associated with this invitation.

**•** If the invitation is to join Chatter, the `SharedEntityId` is the ID of the User that
created the invitation. The invitee will auto-follow the inviter.

**•** If the invitation is to join a group within Chatter, the `SharedEntityId` is the ID of
the Chatter CollaborationGroup.

**•** To invite a customer, set `SharedEntityId` to the ID of the private
CollaborationGroup with Allow Customers turned on.

```
Status

```

Usage

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the invitation. Possible values are:

**•** `Sent`

**•** `Accepted`

**•** `Canceled`

Use this object to create or delete (cancel) invitations to join Chatter. You can either invite a user to join Chatter directly or as part of a
CollaborationGroup.

Note: To invite someone to join a CollaborationGroup, you must be either the owner or a manager of the group or a Salesforce
system administrator.

The Salesforce system administrator doesn’t need to be a member of the group in order to send invitations using the API.

When the person accepts your CollaborationGroup invitation, they join the CollaborationGroup and Chatter as well.

Note: You can't send invitations to users of the organization the invite was sent from.

Invited users can view profiles, post on their feed, and join groups, but they can't see your Salesforce data or records.

If your organization allows groups with customers, owners and managers of private groups with the “Allow Customers” setting, as well
as system administrators, can use this object to invite customers.

Java Samples

The following example shows how to send an invitation to join Chatter:

```
public void invitePeople(String inviterUserId, String invitedEmail) throws Exception {

   CollaborationInvitation invitation = new CollaborationInvitation();

```


### Standard Objects CollaborationRoom

```
      invitation.setSharedEntityId(inviterUserId);//pass the userId of the inviter

      invitation.setInvitedUserEmail(invitedEmail);//email of the invited user

      insert(invitation);

   }

```

The following example shows how to send an invitation to a customer user from a group that allows customers:

```
   public void inviteToGroup(String GroupName, String invitedEmail) throws Exception {

      QueryResult qr = query("select id from collaborationgroup where name = '" +

        GroupName); //pass the group name

      String groupId = qr.getRecords()[0].getId();

      CollaborationInvitation invitation = new CollaborationInvitation();

      invitation.setSharedEntityId(groupId);//pass the groupId

      invitation.setInvitedUserEmail(invitedEmail);//email of the invited user

      insert(invitation);

   }

```

Apex Samples

```
   String emailAddress = 'bob@external.com';

   CollaborationGroup chatterGroup = [SELECT Id

       FROM CollaborationGroup

       WHERE Name='All acme.com'

       LIMIT 1];

   CollaborationInvitation inv = New CollaborationInvitation();

   inv.SharedEntityId = chatterGroup.id;

   inv.InvitedUserEmail = emailAddress;

   try {

     Insert inv;

   } catch(DMLException e){

     System.debug('There was an error with the invite: '+e);

   }

### CollaborationRoom

```

Represents a collaboration room, which links Salesforce to a Slack channel used by applications with specific use cases, such as swarming
or reporting. This object is available in API version 55.0 and later.

Supported Calls

`create()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`search()`, `update()`, `upsert()`

Special Access Rules

To access this object, enable the Slack Terms of Service and one of:

**•** Sales Cloud for Slack App

**•** Service Cloud for Slack App


Standard Objects CollaborationRoom

**•** CRM Analytics for Slack App

**•** Industries Cloud for Slack App

**•** Health Cloud for Slack App

Fields

**Field** **Details**

```
IsArchived

IsAutoJoin

IsExternal

LastReferencedDate

LastViewedDate

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the collaboration room is archived ( `true` ) or not ( `false` ).

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether new users automatically join the collaboration room. Used for Sales Cloud
for Slack App.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether external users are members of the Slack channel ( `true` ) or not ( `false` ).

The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime


### Standard Objects CollabDocumentMetric

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp when the current user last viewed this record or list view. If this value is null, the
user might have only accessed this record or list view ( `LastReferencedDate` ) but not
viewed it.

```
Name

PlatformKey

TeamKey

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of collaboration room.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the Slack channel.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the Slack workspace.

### CollabDocumentMetric

Represents the engagement metrics for a Quip thread (document or spreadsheet) that’s linked to a Salesforce record. This object is
available in API version 50.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects CollabDocumentMetric

Fields

**Field** **Details**

```
Document

Site

SourceTemplate

DocumentTitle

MetricDate

MetricDateOnly

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The Quip thread ID.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Quip site in which the thread is located.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The ID of the template (if any) on which a Quip thread is based.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The title of the thread.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the metric was gathered in your local time zone.

**Type**
date

**Properties**
Filter, Nillable, Sort


Standard Objects CollabDocumentMetric

**Field** **Details**

**Description**
The date that the metric was gathered in UTC. Available in API version 55.0 and later.

```
LastUpdatedDate

LastUpdatedDateOnly

ViewerCount

UpdateCount

EditorCount

CommenterCount

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the thread was created, last edited, or last shared in your local time zone.

**Type**
date

**Properties**
Filter, Nillable, Sort

**Description**
The date that the thread was created, last edited, or last shared in UTC. Available in API version
55.0 and later.

**Type**
int

**Properties**
Filter, Nillable, Sort

**Description**
The number of thread views by user for the specified MetricDate.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of edits made on the thread on a given day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
For the specified MetricDate, the number of users who edited the Quip thread.

**Type**
int


### Standard Objects CollabDocumentMetricRecord

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
For the specified MetricDate, the number of users who commented on the Quip thread.

### CollabDocumentMetricRecord

Represents an association between a CollabDocumentMetric and a Salesforce record.It tracks which Salesforce record, such as an Account
or Contact, is linked to a Quip thread for which metrics were gathered using CollabDocumentMetric. CollabDocumentMetricRecord is
available in API version 50.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ParentRecord

QuipDocumentMetric

MetricDate

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Salesforce record.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the CollabDocumentMetric record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the metric was gathered in your local time zone.


### Standard Objects CollabTemplateMetric

**Field** **Details**

```
MetricDateOnly

EntityType

```

**Type**
date

**Properties**
Filter, Nillable, Sort

**Description**
The date that the metric was gathered in UTC. Available in API version 55.0 and later.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The object type of the Salesforce record, such as Account or Contact.

### CollabTemplateMetric

Represents the engagement metrics for a Quip template.This object is available in API version 50.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
Template

TemplateTitle

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The ID of the template.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The title of the template.


Standard Objects CollabTemplateMetric

**Field** **Details**

```
Site

MetricDate

MetricDateOnly

LastUpdatedDate

LastUpdatedDateOnly

TotalDocumentCount

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Quip site on which the template is available.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the metric was gathered in your local time zone.

**Type**
date

**Properties**
Filter, Nillable, Sort

**Description**
The date that the metric was gathered in UTC. Available in API version 55.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the thread was created, last edited, or last shared in your local time zone.

**Type**
date

**Properties**
Filter, Nillable, Sort

**Description**
The date that the thread was created, last edited, or last shared in UTC. Available in API version
55.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects CollabTemplateMetricRecord

**Field** **Details**

**Description**
The number of documents created based on the template.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CollabTemplateMetricChangeEvent (API version 62.0)**
Change events are available for the object.

### CollabTemplateMetricRecord

Represents an association between a CollabTemplateMetric and a Salesforce record.It tracks which Salesforce record, such as an Account
or Contact, is linked to a Quip template for which metrics were gathered using CollabTemplateMetric. CollabTemplateMetricRecord is
available in API version 50.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ParentRecord

QuipDocumentMetric

MetricDate

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Salesforce record.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the CollabTemplateMetric record.

**Type**
dateTime


### Standard Objects CollabUserEngagementMetric

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The date that the metric was gathered in your local time zone.

```
MetricDateOnly

EntityType

```

**Type**
date

**Properties**
Filter, Nillable, Sort

**Description**
The date that the metric was gathered in UTC. Available in API version 55.0 and later.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The object type of the Salesforce record, such as Account or Contact.

### CollabUserEngagementMetric

Represents the user engagement metrics for a Quip thread in a Quip template or document. This object is available in API version 50.0
and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
CommentCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of comments by the user for the specified `MetricDate` .


Standard Objects CollabUserEngagementMetric

**Field** **Details**

```
EditCount

MetricDate

MetricDateOnly

Name

QuipThread

QuipThreadTitle

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of edits by the user for the specified `MetricDate` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the metric was gathered in your local time zone.

**Type**
date

**Properties**
Filter, Nillable, Sort

**Description**
The date that the metric was gathered in UTC. Available in API version 55.0 and later.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The unique name of the CollabUserEngagementMetric object.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The Quip thread ID.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The title of the Quip document, sheet, slide, and so forth.


Standard Objects CollabUserEngagementMetric

**Field** **Details**

```
QuipThreadType

QuipUser

SalesforceUserId

Site

SourceTemplate

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of Quip thread. The possible values are:

**•** `CHAT`

**•** `DOCUMENT`

**•** `SHEET`

**•** `SLIDE`

**•** `TEMPLATE`

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The ID of the Quip user.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Salesforce user.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Quip site.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The ID of the source template.


### Standard Objects CollabUserEngmtRecordLink

**Field** **Details**

```
ViewCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of views by the user for the specified `MetricDate` .

### CollabUserEngmtRecordLink

Represents an association between a CollabUserEngagementMetric and a Salesforce record. It tracks which Salesforce record, such as
an Account or Contact, is associated with the user engagement metric. This object is available in API version 50.0 and later.

Note: The CollabUserEngmtRecordLink object is now deprecated. You can still access user engagement metrics for metric dates
before August 12, 2021. To obtain user engagement metric for dates starting from August 12, 2021, follow the instructions in the
[Quip Engagement Metrics documentation.](https://help.salesforce.com/articleView?id=xcloud.quip_template_metrics.htm&type=5&language=en_US)

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
MetricDate

Name

ObjectType

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date of the gathered metric.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The unique name of the CollabUserEngmtRecordLink object.

**Type**
string


### Standard Objects ColorDefinition

**Field** **Details**

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The object type of the Salesforce record, such as Account or Contact.

```
ParentRecordId

UserEngagementMetricId

### ColorDefinition

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Salesforce record.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the CollabUserEngagementMetric record.

Represents the color-related metadata for a custom tab. This object is available in API version 43.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Fields

**Field Name** **Details**

### `Color`

```
Context

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The color described in web color RGB format—for example, “00FF00”.

**Type**
string


### Standard Objects ContCalloutSummaryEventLog

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**

The color context, which determines whether the color is the main color (or
primary) for the tab.

```
DurableId

TabDefinitionId

Theme

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

A unique virtual Salesforce ID for the color.

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

### ContCalloutSummaryEventLog

Continuation Callout Summary events contain information about all of the asynchronous callouts performed during a transaction, their
response status codes, execution times, and URL endpoint destinations. This object is available in API version 65.0 and later.


Standard Objects ContCalloutSummaryEventLog

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
ContinuationIdentifier

Duration

IsSuccess

OriginRequestIdentifier

RequestFormSize

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A unique ID identifying a sequence of events within a request.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Total duration of continuation, in milliseconds.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the continuation was successful or not.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the request that initiated a callout.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ContCalloutSummaryEventLog

**Field** **Details**

**Description**
Continuation request form size, in bytes. Depending on how many HTTP requests were used
in a continuation, this field can contain up to three space-separated values.

```
RequestIdentifier

ResponseSize

StatusCode

Timestamp

Url

```

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
The size of the callout response, in bytes. Depending on how many HTTP requests were used
in a continuation, this field can contain up to three space-separated values.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The HTTP status or internal code returned by the remote endpoint. A status code of 200
indicates that the request was successful. Other status code values indicate the type of
problem that was encountered. Depending on how many HTTP requests were used in a
continuation, this field can contain up to three space-separated values.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT. For example, `20130715233322.670` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects CombinedAttachment

**Field** **Details**

**Description**
The callout endpoint URL. Depending on how many HTTP requests were used in a
continuation, this field can contain up to three space-separated values.

```
UserIdentifier

VisualforceControllerSize

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
Continuation Visualforce controller size, in bytes. Depending on how many HTTP requests
were used in a continuation, this field can contain up to three space-separated values.

### CombinedAttachment

This read-only object contains all notes, attachments, Google Docs, documents uploaded to libraries in Salesforce CRM content, and
files added to Chatter that are associated with a record.

Supported Calls

```
describeSObjects()

```

Fields

**Field Name** **Details**

```
ContentSize

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The size of the document in bytes for documents smaller than 2 GB.


Standard Objects CombinedAttachment

**Field Name** **Details**

In API version 66.0 and later, we recommend that you use the
`ContentSizeLong` field even for documents smaller than 2 GB.

```
ContentSizeLong

ContentUrl

ExternalDataSourceName

ExternalDataSourceType

FileExtension

```

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

**Description**
The name of the external data source in which the document is stored. This field
is set only for external documents that are connected to Salesforce.

This field is available in API version 32.0 and later.

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


Standard Objects CombinedAttachment

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**

File extension of the document.

This field is available in API version 31.0 and later.

```
FileType

ParentId

```

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

The ID of the parent object.

This is a relationship field.

**Relationship Name**
Parent

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


Standard Objects CombinedAttachment

**Field Name** **Details**

CommSubscriptionTiming, ConsumptionSchedule, Contact, ContactEncounter,
ContactEncounterParticipant, ContentWorkspace, Contract, ConversationEntry,
CoverageBenefit, CoverageBenefitItem, CredentialStuffingEventStore, CreditMemo,
CreditMemoLine, Dashboard, DashboardComponent, DataStream,
DelegatedAccount, DocumentChecklistItem, EmailMessage, EmailTemplate,
EngagementChannelType, EnhancedLetterhead, EnrollmentEligibilityCriteria,
Event, HealthcareFacility, HealthcareFacilityNetwork, HealthcarePayerNetwork,
HealthcarePractitionerFacility, HealthcareProvider, HealthcareProviderNpi,
HealthcareProviderSpecialty, HealthcareProviderTaxonomy, Identifier,
IdentityDocument, Image, IndividualApplication, Invoice, InvoiceLine, Lead,
ListEmail, Location, MarketSegment, MarketSegmentActivation, MemberPlan,
MessagingSession, MktCalculatedInsight, OperatingHours, Opportunity, Order,
OrderItem, Organization, OtherComponentTask, PartyConsent, PersonEducation,
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

```
RecordType

SharingOption

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The parent object type.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Controls whether sharing is frozen for a file. Only Salesforce admins and file
owners with Collaborator access to the file can modify this field. The default is
`Allowed`, which means that new shares are allowed. When set to
`Restricted`, new shares are prevented without affecting existing shares.

This field is available in API versions 35.0 and later.


### Standard Objects CommerceEntitlementBuyerGroup

**Field Name** **Details**

```
Title

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Title of the attached file.

Use this object to list all notes, attachments, documents uploaded to libraries in Salesforce CRM content, and files added to Chatter for
a record, such as a related list on a detail page.

To determine if an object supports the CombinedAttachment object, call `describeSObject()` on the object. For example,
`describeSObject('Account')` returns all the child relationships of the Account object, including `CombinedAttachment` .
You can then query the CombinedAttachment child relationship.

```
SELECT Name, (SELECT Title FROM CombinedAttachments)

FROM Account

```

You can’t directly query CombinedAttachment.

### CommerceEntitlementBuyerGroup

Represents the entitlement policy for a buyer group. This object is available in API version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`

Special Access Rules

The CommerceEntitlementBuyerGroup object is available when you meet these requirements. The B2B Commerce license is enabled.
The Commerce Buyer and Entitlements Integrator permission is granted.

Fields

**Field** **Details**

```
BuyerGroupId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort


### Standard Objects CommerceEntitlementPolicy

**Field** **Details**

**Description**
The unique ID for the buyer group.

```
CurrencyIsoCode

Name

PolicyId

```

Associated Objects

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The standard code for the currency.

Possible values are:

**•** `GBP` —British Pound

**•** `USD` —U.S. Dollar

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the entitlement buyer group.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique ID for the entitlement policy.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CommerceEntitlementBuyerGroupChangeEvent on page 68**
Change events are available for the object.

### CommerceEntitlementPolicy

Represents an entitlement policy, which determines what products and prices a user can see. This object is available in API version 49.0
and later.


Standard Objects CommerceEntitlementPolicy

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The CommerceEntitlementPolicy object is available only if the B2B Commerce license is enabled.

Fields

**Field** **Details**

```
CanViewPrice

CanViewProduct

CurrencyIsoCode

Description

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether a user can view the price of a product ( `true` ) or not ( `false` ). Default
value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether a user can view the product ( `true` ) or not ( `false` ). Default value is
`false` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The standard code for the currency.

Possible values are:

**•** `GBP` —British Pound

**•** `USD` —U.S. Dollar

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects CommerceEntitlementPolicy

**Field** **Details**

**Description**
The entitlement policy description.

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
Determines if the entitlement policy is active ( `true` ) or inactive ( `false` ). Default value is
`false` .

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
The timestamp for when the current user last viewed this record. If this value is null, it can
mean that the record was only referenced ( `LastReferencedDate` ) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the entitlement policy.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The unique ID for the entitlement policy owner.


### Standard Objects CommerceEntitlementPolicyShare

Associated Objects

This object has the following associated objects. Except where noted, these objects are available in the same API version as
CommerceEntitlementPolicy.

**CommerceEntitlementPolicyChangeEvent on page 68**
Change events are available for the object.

**CommerceEntitlementPolicyOwnerFeed on page 55**
Feed tracking is available for the object.

**CommerceEntitlementPolicyHistory on page 63**
History is available for tracked fields of the object.

**CommerceEntitlementPolicyOwnerSharingRule**

Sharing rules are available for this object.

### CommerceEntitlementPolicyShare

Represents the entitlement rule for sharing products and prices with users other than the owner. This object is available in API version
49.0 and later.

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual` . Sharing entries
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

The CommerceEntitlementPolicyShare object is available only if the B2B Commerce license is enabled.

Fields

**Field** **Details**

```
AccessLevel

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Possible values are:

**•** `All` —Owner


Standard Objects CommerceEntitlementPolicyShare

**Field** **Details**

**•** `Edit` —Read/Write

**•** `Read` —Read Only

```
ParentId

RowCause

UserOrGroupId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique ID of the parent entitlement policy.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only permitted
value is `Manual` . If no value is specified, the field defaults to `Manual` . All other `RowCause`
values are read-only. After the sharing entry is created, this field can’t be edited.

Possible values are:

**•** `CompliantCollaboration` —Compliant Data Sharing

**•** `GuestParentImplicit` —Associated guest user sharing

**•** `GuestPersonImplicit` —Associated Guest User Sharing

**•** `GuestRule` —Guest User Sharing Rule

**•** `ImplicitChild` —Account Sharing

**•** `ImplicitParent` —Associated record owner or sharing

**•** `ImplicitPerson` —Person Contact

**•** `Manual` —Manual Sharing

**•** `Owner`

**•** `Rule` —Sharing Rule

**•** `SurveyShare` —Survey Sharing Rule

**•** `Team` —Sales Team

**•** `Territory` —Territory Assignment Rule

**•** `Territory2AssociationManual` —Territory Manual

**•** `Territory2Forecast` —Territory assignment for forecasting and reporting

**•** `TerritoryManual` —Territory Manual

**•** `TerritoryRule` —Territory Sharing Rule

**Type**
reference


### Standard Objects CommerceEntitlementProduct

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
The unique ID of the associated user or buyer group.

### CommerceEntitlementProduct

Represents the entitlement policy for a product. This object is available in API version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`

Special Access Rules

The CommerceEntitlementProduct object is available when you meet these requirements. The B2B Commerce license is enabled. The
Commerce Buyer and Entitlements Integrator permission is granted.

Fields

**Field** **Details**

```
CurrencyIsoCode

Name

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The standard code for the currency.

Possible values are:

**•** `GBP` —British Pound

**•** `USD` —U.S. Dollar

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The product entitlement policy name.


### Standard Objects CommissionSchedule

**Field** **Details**

```
PolicyId

ProductId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique ID for the product entitlement policy.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique ID for the product referenced in the entitlement policy.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CommerceEntitlementProductChangeEvent on page 68**
Change events are available for the object.

### CommissionSchedule

Represents a commission calculation and rate definition. Calculates commission values for a commissionable event.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ApplicableObject

```

**Type**
multipicklist

**Properties**
Create, Filter, Nillable, Restricted picklist, Update

**Description**
The object for which this Commission Schedule calculates commissions.


Standard Objects CommissionSchedule

**Field** **Details**

Possible values are:

**•** `Contract`

**•** `InsurancePolicy`

**•** `Producer`

**•** `Quote`

```
CalcProcessInputMapping

CalcProcessOutput

CalcProcessOutputConvNotation

CalculationProcessName

CalculationType

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The input mappings from the object fields to the variables used in the commission calculation.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The formula applied to this Commission Schedule’s process output that calculates the final
commission amount.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
An optimized version of the CalcProcessOutput formula that calculates the commission. Not
user-editable.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the Integration Procedure, Calculation Matrix, or Calculation Procedure this
Commission Schedule uses for calculations.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


Standard Objects CommissionSchedule

**Field** **Details**

**Description**
The type of calculation or process used when this Commission Schedule is used.

Possible values are:

**•** `Amount`

**•** `CalculationMatrix`

**•** `CalculationProcedure`

**•** `IntegrationProcedure`

**•** `Rate`

```
CommissionAmount

CommissionRate

CommissionStructureType

EffectiveEndDate

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The commission amount for the Commission Schedule when the process type is Amount.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The commission percentage for the Commission Schedule when the process type is Rate.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates whether the commission calculation is Flat or Tiered when the process type is
Matrix.

Possible values are:

**•** `Flat`

**•** `Tiered`

The default value is `Flat` .

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects CommissionSchedule

**Field** **Details**

**Description**
The effective end date of the Commission Schedule.

```
EffectiveStartDate

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
The effective start date of the Commission Schedule.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the Commission Schedule is active.

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
possible that this record was referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the Commission Schedule.

**Type**
reference


### Standard Objects CommissionScheduleAssignment

**Field** **Details**

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

```
TierDefinition

```

Associated Objects

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Internal-only. Applies when the CalculationType is CalculationMatrix.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CommissionScheduleChangeEvent on page 68**
Change events are available for the object in API version 62.0 and later.

**CommissionScheduleFeed**

Feed tracking is available for the object.

**CommissionScheduleHistory**

History is available for tracked fields of the object.

**CommissionScheduleOwnerSharingRule**

Sharing rules are available for the object.

**CommissionScheduleShare**

Sharing is available for the object.

### CommissionScheduleAssignment

Represents the commission calculation applicable to a specific product or producer for one or multiple commissionable events.


Standard Objects CommissionScheduleAssignment

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CommissionableEventType

CommissionScheduleId

EffectiveEndDate

```

**Type**
multipicklist

**Properties**
Create, Filter, Nillable, Restricted picklist, Update

**Description**
The event that results in the commission calculation.

Possible values are:

**•** `Contracting`

**•** `Endorsement`

**•** `Issue Policy`

**•** `Policy Issuance`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

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

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The last date when the Commission Schedule is in effect for the product or producer.


Standard Objects CommissionScheduleAssignment

**Field** **Details**

```
EffectiveStartDate

LastReferencedDate

LastViewedDate

MaxCommissionAmount

MaxCommissionRate

MinCommissionAmount

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The first date when the Commission Schedule is in effect for the product or producer.

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
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The maximum commission calculated for the product or producer for a commissionable
event. Constrains the output from the Commission Schedule.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The maximum commission rate that a producer receives for a commissionable event.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects CommissionScheduleAssignment

**Field** **Details**

**Description**
The minimum commission calculated for the product or producer for a commissionable
event. Constrains the output from the Commission Schedule.

```
MinCommissionRate

Name

ProducerId

Product2Id

```

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The minimum commission rate that a producer receives for a commissionable event.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the Commission Schedule Assignment.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The producer, broker, brokerage, or other user who receives the commission.

This is a relationship field.

**Relationship Name**
Producer

**Relationship Type**
Lookup

**Refers To**
Producer

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The product for which commissions are calculated.

This is a relationship field.

**Relationship Name**
Product2


### Standard Objects CommSubscription

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Product2

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CommissionScheduleAssignmentChangeEvent on page 68**
Change events are available for the object in API version 62.0 and later.

**CommissionScheduleAssignmentFeed**

Feed tracking is available for the object.

**CommissionScheduleAssignmentHistory**

History is available for tracked fields of the object.

**CommissionScheduleAssignmentOwnerSharingRule on page 65**
Sharing rules are available for the object.

**CommissionScheduleAssignmentShare on page 67**
Sharing is available for the object.

### CommSubscription

Represents the subscription options for a specific communication. This object is available in API version 48.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
DataUsePurposeId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the data use purpose record associated with the communication subscription.


Standard Objects CommSubscription

**Field** **Details**

```
IsDefault

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
Indicates if this communication subscription is the default ( `true` ) or not ( `false` ). This field
has a default value of `false` . Only one communication subscription record can be the
default.

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
Required. Name of the communication subscription record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the account owner associated with this customer.

This is a polymorphic relationship field.

**Relationship Name**
Owner


### Standard Objects CommSubscriptionChannelType

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Group, User

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**CommSubscriptionChangeEvent (API version 61.0)**
Change events are available for the object.

**CommSubscriptionFeed**

Feed tracking is available for the object.

**CommSubscriptionHistory**

History is available for tracked fields of the object.

**CommSubscriptionOwnerSharingRule**

Sharing rules are available for the object.

**CommSubscriptionShare**

Sharing is available for the object.

### CommSubscriptionChannelType

Represents the engagement channel through which you can reach a customer for a communication subscription. This object is available
in API version 48.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CommunicationSubscriptionId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the associated communication subscription record.

This is a relationship field.


Standard Objects CommSubscriptionChannelType

**Field** **Details**

**Relationship Name**
CommunicationSubscription

**Relationship Type**
Lookup

**Refers To**
CommSubscription

```
EngagementChannelTypeId

LastReferencedDate

LastViewedDate

MessagingChannelUsageId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the associated engagement channel type record.

This is a relationship field.

**Relationship Name**
EngagementChannelType

**Relationship Type**
Lookup

**Refers To**
EngagementChannelType

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
reference

**Properties**
Filter, Group, Sort


Standard Objects CommSubscriptionChannelType

**Field** **Details**

**Description**
The ID of the associated Messaging channel usage record, which is in turn associated with
a messaging channel.

This is a relationship field.

**Relationship Name**
MessagingChannelUsage

**Relationship Type**
Lookup

**Refers To**
MessagingChannelUsage

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
Required. Name of the communication subscription channel type record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID account owner associated with this customer.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**CommSubscriptionChannelTypeChangeEvent (API version 61.0)**
Change events are available for the object.

**CommSubscriptionChannelTypeFeed**

Feed tracking is available for the object.


### Standard Objects CommSubscriptionConsent

**CommSubscriptionChannelTypeHistory**

History is available for tracked fields of the object.

**CommSubscriptionChannelTypeOwnerSharingRule**

Sharing rules are available for the object.

**CommSubscriptionChannelTypeShare**

Sharing is available for the object.

### CommSubscriptionConsent

Represents a customer’s consent to a communication subscription. This object is available in API version 48.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

With certain page layout and field-level security settings, some fields aren't visible or editable.

**Field** **Details**

```
BusinessBrandId

CommSubscriptionChannelTypeId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Business Brand that the individual has given consent to for a communication
subscription. This is a relationship field. This field is available in API version 53.0 and later.

**Relationship Name**
BusinessBrand

**Relationship Type**
Lookup

**Refers To**
BusinessBrand

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the associated communication subscription channel type record.

This is a relationship field.


Standard Objects CommSubscriptionConsent

**Field** **Details**

**Relationship Name**
CommSubscriptionChannelType

**Relationship Type**
Lookup

**Refers To**
CommSubscriptionChannelType

```
ConsentCapturedDateTime

ConsentCapturedSource

ConsentGiverId

ContactPointId

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Required. Date when the customer’s consent was captured.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. Source through which consent was captured. For example, user@example.com
or www.example.com.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the person who gave consent to the communication subscription on behalf of the
contact point.

Note: If the contact point gave consent, don't use `ConsentGiverId` .

This is a polymorphic relationship field.

**Relationship Name**
ConsentGiver

**Relationship Type**
Lookup

**Refers To**
Account, Contact, Individual, User

**Type**
reference


Standard Objects CommSubscriptionConsent

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the contact point, such as an Individual or person account, associated with the
communication subscription consent.

This is a polymorphic relationship field.

**Relationship Name**
ContactPoint

**Relationship Type**
Lookup

**Refers To**
ContactPointAddress, ContactPointEmail, ContactPointPhone

```
DataUsePurposeId

EffectiveFromDate

EffectiveToDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Represents the record for data use purpose that you want to associate this consent with.
This field is available in API version 57.0 and later.

This is a relationship field.

**Relationship Name**
DataUsePurpose

**Relationship Type**
Lookup

**Refers To**
DataUsePurpose

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. Date when consent starts.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Date when consent ends. This field is restricted by field-level security.


Standard Objects CommSubscriptionConsent

**Field** **Details**

```
EngagementChannelTypeId

LastReferencedDate

LastViewedDate

Name

OwnerId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Represents the contact method you want to apply consent to. This field is available in API
version 57.0 and later.

This is a relationship field.

**Relationship Name**
EngagementChannelType

**Relationship Type**
Lookup

**Refers To**
EngagementChannelType

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
Required. Name of the communication subscription consent record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects CommSubscriptionConsent

**Field** **Details**

**Description**
The ID of the account owner associated with this customer.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

```
PartyId

PartyRoleId

PrivacyConsentStatus

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the record based on the Individual object that you want to associate consent
with. This field is available in API version 57.0 and later.

This is a relationship field.

**Relationship Name**
Party

**Relationship Type**
Lookup

**Refers To**
Individual

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Party Role for the individual you want to associate consent with. This is a
polymorphic relationship field. This field is available in API version 53.0 and later.

**Relationship Name**
PartyRole

**Relationship Type**
Lookup

**Refers To**
Customer, Seller

**Type**
picklist


### Standard Objects CommSubscriptionTiming

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Identifies whether the individual or person account associated with this record agrees to
this form of contact.

Possible values are:

**•** `NotSeen`

**•** `OptIn`

**•** `OptInPending` —Available in API version 58.0 and later.

**•** `OptOut`

**•** `OptOutPending` —Available in API version 58.0 and later.

**•** `Seen`

The default value is `NotSeen` . This field is available in API version 57.0 and later.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CommSubscriptionConsentChangeEvent (API version 49.0)**
Change events are available for the object.

**CommSubscriptionConsentFeed**

Feed tracking is available for the object.

**CommSubscriptionConsentHistory**

History is available for tracked fields of the object.

**CommSubscriptionConsentOwnerSharingRule**

Sharing rules are available for the object.

**CommSubscriptionConsentShare**

Sharing is available for the object.

### CommSubscriptionTiming

Represents a customer's timing preferences for receiving a communication subscription. This object is available in API version 48.0 and
later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects CommSubscriptionTiming

Fields

**Field** **Details**

```
CommSubscriptionConsentId

LastReferencedDate

LastViewedDate

Name

Offset

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the associated communication subscription consent record.

This is a relationship field.

**Relationship Name**
CommSubscriptionConsent

**Relationship Type**
Lookup

**Refers To**
CommSubscriptionConsent

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
Required. Name of the communication subscription timing record.

**Type**
double


Standard Objects CommSubscriptionTiming

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The amount of time before or after an event or the specific day of the week to communicate
with the contact point. Set the unit of time in the `Unit` field.

For example, if you set `Unit` as _`Week`_ and `Offset` as _`-4`_, communicate with the contact
point four weeks before the event. If you set `Offset` as _`4`_, communicate with the contact
point four weeks after the event.

```
PreferredTimeEnd

PreferredTimeStart

PreferredTimeZone

Unit

```

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
End of the preferred time span in which to reach the customer.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Start of the preferred time span in which to reach the customer.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Time zone of the preferred time span.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The unit of time that works with the `Offset` field to determine the communication timing.

Possible values are:

**•** `Day`

**•** `DayOfWeek`

**•** `Hour`

**•** `Month`


### Standard Objects Community (Zone)

**Field** **Details**

**•** `Week`

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**CommSubscriptionTimingChangeEvent (API version 62.0)**
Change events are available for the object.

**CommSubscriptionTimingFeed**

Feed tracking is available for the object.

**CommSubscriptionTimingHistory**

History is available for tracked fields of the object.

### Community (Zone)

Represents a zone that contains Idea or Question objects.

Note: Starting with the Summer ’13 release, Chatter Answers and Ideas communities were renamed to zones. In API version 28,
### the API object label has changed to Zone, but the API type is still Community .

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
CanCreateCase

DataCategoryName

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether users can ask private questions in the zone using Chatter Answers.

**Type**
string

**Properties**
Filter, Nillable, Group, Sort

**Description**
The data category associated with the zone.


Standard Objects Community (Zone)

**Field** **Details**

```
Description

HasChatterService

IsActive

IsPublished

Name

NetworkId

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
Text description of the zone.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether Chatter Answers is available in the zone.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the zone is active or inactive. An idea or question can only be posted to
an active zone.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the zone is available in portals.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the zone.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects ConcurApexLimitEventLog

**Field** **Details**

**Description**
ID of the Experience Cloud site that this zone is associated with. This field is available only if
digital experiences is enabled in your org. This field is available in API version 66.0 and later.

Usage

Use this object to create a zone in Ideas, Chatter Answers, or Answers. Zones help organize ideas and questions into logical groups and
are shared by the Ideas, Answers, and Chatter Answers.

### ConcurApexLimitEventLog

Concurrent Apex Limit event logs contain information about long-running concurrent Apex requests in your org that Salesforce terminated
after reaching your org’s concurrency limit. Requests with an established Apex context that execute for 5 seconds are counted towards
your org’s limit of concurrent long-running requests. (Asynchronous requests don’t count towards the limit.) When the long-running
requests exceed the org default limit, additional long-running requests are denied. This object is available in API version 61.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
RequestCount

RequestIdentifier

```

**Type**
int

**Properties**
Filter, Nillable, Sort

**Description**
Count of requests with an established Apex context executing for longer than 5 seconds in
your org.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ConcurApexLimitEventLog

**Field** **Details**

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `RequestIdentifier` . For example:
`3nWgxWbDKWWDIk0FKfF5DV` .

```
RequestLimit

RequestUri

Timestamp

UserIdentifier

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Maximum count of requests with an established Apex context that can execute for longer
than 5 seconds. When `RequestCount` reaches this limit, then additional long-running
Apex requests are terminated. (Asynchronous requests don’t count towards the limit.) See
_Apex Developer Guide_ [: Lightning Platform Apex Limits. For example:](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_gov_limits.htm#in_topic_non_transactional_gov_limits_section) `10` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URI of the long-running Apex request that Salesforce terminated. For example:
`/apex/ApexClassName` .

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


### Standard Objects ConnectedApplication ConnectedApplication

Represents a connected app and its details; all fields are read-only.

Connected apps link client applications, third-party services, other Salesforce organizations, apps, and resources to your organization.
The connected app configuration specifies authorization and security settings for these resources. This object exposes the settings for
a specified connected app.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
MobileSessionTimeout

MobileStartUrl

Name

NamedUserUvidTimeout

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**

Length of time after which the system logs out inactive mobile users.

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**

Users are directed to this URL after they’ve authenticated when the app is accessed
from a mobile device.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**

The unique name for this object.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


Standard Objects ConnectedApplication

**Field Name** **Details**

**Description**

The timeout value for a JSON Web Token (JWT)-based access token that's issued
to a named user. This field defines the timeout only if the app is configured to
have an app-specific timeout. If the app uses the user's session timeout, the
timeout value is defined based on the user's profile or the org session settings.
For more information about defining JWT-based access token timeout, see
[Configure a Connected App to Issue JWT-Based Access Tokens.](https://help.salesforce.com/s/articleView?id=xcloud.jwt_connectedapp_enable.htm&language=en_US)

These values are available in API version 59.0 and later.

**•** `1` —1 Minute

**•** `5` —5 Minutes

**•** `10` —10 Minutes

**•** `15` —15 Minutes

**•** `30` —30 Minutes

These values are available in API version 65.0 and later.

**•** `60` —1 Hour

**•** `90` —90 Minutes

**•** `120` —2 Hours

**•** `240` —4 Hours

**•** `480` —8 Hours

**•** `720` —12 Hours

This field is available in API version 59.0 and later.

```
OptionsAllowAdminApprovedUsersOnly

```

**Type**
boolean

**Properties**
Filter

**Description**

Indicates whether access is limited to users granted approval to use the connected
app by an administrator. Manage profiles for the app by editing each profile’s
Access list.

`OptionsCodeCredentialGuestEnabled` Reserved for future use.

`OptionsFullContentPushNotifications` For internal use only.

```
OptionsHasSessionLevelPolicy

```

**Type**
boolean

**Properties**
Filter

**Description**

Specifies whether the connected app requires a High Assurance level session.


Standard Objects ConnectedApplication

**Field Name** **Details**

`OptionsIsInternal` For internal use only.

```
OptionsRefreshTokenValidityMetric

OptionsTokenExchangeManageBitEnabled

PinLength

RefreshTokenValidityPeriod

StartUrl

```

**Type**
boolean

**Properties**
Filter

**Description**

Specifies whether the refresh token validity is based on duration or inactivity. If
`true`, the token validity is measured based on the last use of the token;
otherwise, it’s based on the token duration.

**Type**
boolean

**Properties**
Filter

**Description**

If `true`, the OAuth 2.0 token exchange flow is enabled.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

For mobile apps, this field is the PIN length requirement for users of the connected
app. Valid values are `4`, `5`, `6`, `7`, or `8` .

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The duration of an authorization token until it expires in hours, months, or days
as set in the connected app management page.

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**

If the app isn’t accessed from a mobile device, users are directed to this URL after
they’ve authenticated.


### Standard Objects ConferenceNumber

**Field Name** **Details**

```
UvidTimeout

### ConferenceNumber

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

The timeout value for a JWT-based access token that's issued to an unknown
user as a result of the guest user variation of the Authorization Code and
Credentials Flow. JWT-based access tokens issued during this flow variation
always contain a UVID.

This field defines the timeout only if the app is configured to have an app-specific
timeout. If the app uses the user's session timeout, the timeout value is defined
based on the user's profile or the org session settings. For more information about
[defining JWT-based access token timeout, see Configure a Connected App to](https://help.salesforce.com/s/articleView?id=xcloud.jwt_connectedapp_enable.htm&language=en_US)
[Issue JWT-Based Access Tokens.](https://help.salesforce.com/s/articleView?id=xcloud.jwt_connectedapp_enable.htm&language=en_US)

These values are available in API version 59.0 and later.

**•** `1` —1 Minute

**•** `5` —5 Minutes

**•** `10` —10 Minutes

**•** `15` —15 Minutes

**•** `30` —30 Minutes

These values are available in API version 65.0 and later.

**•** `60` —1 Hour

**•** `90` —90 Minutes

**•** `120` —2 Hours

**•** `240` —4 Hours

**•** `480` —8 Hours

**•** `720` —12 Hours

This field is available in API version 59.0 and later.

Holds the telephone number for an external event shown in the Salesforce Today feature in the Salesforce mobile app. This object is
available in API version 35.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`


Standard Objects ConferenceNumber

Special Access Rules

The Salesforce Today app is available in Salesforce for Android and Salesforce for iOS. It’s not available in the Salesforce desktop site.
Access to Today is available only if you grant Calendar permission to the Salesforce mobile app.

Fields

**Field** **Details**

```
AccessCode

ExternalEventId

IsLocked

Label

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the access code to enter in order to validate identity and join the call.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the external event associated with the conference number.

This field is a relationship field.

**Relationship Name**
ExternalEvent

**Refers To**
ExternalEvent

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Returns `true` if the conference number is locked, or `false` if it’s not.

The default value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the conference number.


### Standard Objects Consumption Rate

**Field** **Details**

```
MayEdit

Name

Number

Vendor

```

Associated Objects

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

Indicates whether the conference number can be edited ( `true` ) or not ( `false` ).

The default value is `false` .

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the conference call’s organizer.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The phone number used to connect to the conference call.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The vendor or company associated with the conference number.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ConferenceNumberChangeEvent**

### Consumption Rate

Consumption rates describe the billing rate for a range of usage within a consumption schedule. All consumption schedules require at
least one consumption rate in order to rate usage on a usage product. This object is available in API version 45.0 and later.

The consumption rate sets a quantity-based boundary for usage and defines how much your product costs when its usage falls within
that boundary. Consumption rates price usage at a per-unit fee or a flat fee across the entire range of usage.


Standard Objects Consumption Rate

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ConsumptionScheduleId

CurrencyIsoCode

Description

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The consumption schedule that contains the consumption rate.

This is a relationship field.

**Relationship Name**
ConsumptionSchedule

**Relationship Type**
Lookup

**Refers To**
ConsumptionSchedule

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled.

Possible values are:

**•** `AUD` —Australian Dollar

**•** `CAD` —Canadian Dollar

**•** `GBP` —British Pound

**•** `JPY` —Japanese Yen

**•** `USD` —U.S. Dollar

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the consumption rate.


Standard Objects Consumption Rate

**Field** **Details**

```
LowerBound

Name

Price

PricingMethod

ProcessingOrder

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The lowest quantity of usage for the consumption rate.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Required. Default name of this record. Label is **Product Name** .

**Type**
currency

**Properties**
Create, Filter, Sort, Update

**Description**
The price for usage that falls within the consumption rate’s bounds.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
How Salesforce applies the consumption rate’s price to the total quantity of usage within a
usage summary.

Possible values are:

**•** `FlatFee` —Salesforce applies the rate’s price to the entire quantity of usage.

**•** `PerUnit` —Salesforce applies the rate’s price to each individual quantity of usage
within the usage summary.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The order for processing the usage rate across multiple rates. Consumption rates are evaluated
beginning with the lowest processing order.


### Standard Objects Consumption Schedule

**Field** **Details**

```
UpperBound

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The highest quantity of usage for the consumption rate.

### Consumption Schedule

A consumption schedule organizes a set of consumption rates by which usage-based products are quoted and billed. This object is
available in API version 45.0 and later.

Salesforce uses consumption schedules to group consumption rates. Your consumption schedule defines the unit of measurement and
rating method for the schedule's rates. It also defines the billing frequency that Salesforce Billing uses to invoice a usage product.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
BillingTerm

BillingTermUnit

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The number used with the billing term unit to determine billing frequency.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The unit used with the billing term to determine billing frequency

Possible values are:

**•** `Month`  

**•** `Quarter`  

**•** `Year`  


Standard Objects Consumption Schedule

**Field** **Details**

```
CurrencyIsoCode

Description

IsActive

LastReferencedDate

LastViewedDate

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled.

Possible values are:

**•** `AUD` —Australian Dollar

**•** `CAD` —Canadian Dollar

**•** `GBP` —British Pound

**•** `JPY` —Japanese Yen

**•** `USD` —U.S. Dollar

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the consumption schedule.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this record is active ( `true` ) or not ( `false` ). Label is **Active** .

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


Standard Objects Consumption Schedule

**Field** **Details**

**Description**

The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view ( `LastReferencedDate` ) but
not viewed it.

```
MatchingAttribute

Name

NumberOfRates

OwnerId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Salesforce Billing matches usage with a consumption schedule if the records share Matching
Attribute value.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Default name of this record. Label is **Product Name** .

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of consumption rates in this consumption schedule.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The user who owns a consumption schedule record.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User


Standard Objects Consumption Schedule

**Field** **Details**

```
RatingMethod

SBQQ__Category__c

Type

UnitOfMeasure

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A specific use case to rate usage against the schedule. This field is the controlling picklist for
the Type field.

Possible values are:

**•** `Tier`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
This field is available only with Salesforce CPQ.

You can define custom categories to organize consumption schedules in separate tabs on
sales rep UI. If you do this, make sure to create a field set for each category.

Possible values are:

**•** `Rates`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Defines how rate tiers are calculated.

Possible values are:

**•** `Range` —The schedule prices only using the tier that applies to the usage quantity.

**•** `Slab` —Usage within a given bound receives pricing equal to its tier’s value.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A unit of measure defines how you quantify instances of usage for your usage products. For
example, if your usage product is a cloud storage subscription, you could provide a value of
GB for your unit of measure.


### Standard Objects Contact

**Field** **Details**

```
 blng__BillingRule__c

 blng__RevenueRecognitionRule__c

 blng__TaxRule__c

### Contact

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
This field is available only with Salesforce Billing.

Salesforce Billing invoices usage summaries based off their related consumption schedule's
billing rule.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
This field is available only with Salesforce Billing.

Salesforce Billing recognizes usage summary revenue based off the summary's related revenue
recognition rule.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
This field is available only with Salesforce Billing.

Salesforce Billing taxes usage summary invoice lines based off the summary's related tax
rule.

Represents a contact, which is a person associated with an account.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `merge()`,
`query()`, `retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects Contact

Special Access Rules

Customer Portal users can access only portal-enabled contacts.

Fields

**Field** **Details**

```
AccountId

ActionCadenceAssigneeId

ActionCadenceId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the account that’s the parent of this contact.

We recommend that you update up to 50 contacts simultaneously when changing the
accounts on contacts enabled for a Customer Portal or partner portal. We also recommend
that you make this update after business hours.

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
Filter, Group, Nillable, Sort

**Description**
The ID of the sales rep designated to work the lead through their assigned cadence. This
field is available in API version 48.0 and later when the Sales Engagement license is enabled.
To see this field, the user also needs the Sales Engagement User or Sales Engagement Quick
Cadence Creator user permission set.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the lead’s assigned cadence. This field is available in API version 48.0 and later when
the Sales Engagement license is enabled. To see this field, the user also needs the Sales
Engagement User or Sales Engagement Quick Cadence Creator user permission set.


Standard Objects Contact

**Field** **Details**

```
ActionCadenceState

ActiveTrackerCount

ActivityMetricId

```

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
The number of cadences that are actively running on this contact. This field is available in
API version 57.0 and later when the Sales Engagement license is enabled. To see this field,
the user also needs the Sales Engagement User or Sales Engagement Quick Cadence Creator
user permission set.

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


Standard Objects Contact

**Field** **Details**

```
ActivityMetricRollupId

AssistantName

AssistantPhone

Birthdate

```

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
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The assistant’s name.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The assistant’s phone number. Label is **Asst. Phone** .

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The contact’s birthdate.

Filter criteria for report filters, list view filters, and SOQL queries ignore the year portion of
the `Birthdate` field. For example, this SOQL query returns contacts with birthdays later
in the year than today:

```
  SELECT Name, Birthdate

  FROM Contact

  WHERE Birthdate > TODAY

```


Standard Objects Contact

**Field** **Details**

```
BuyerAttributes

CanAllowPortalSelfReg

CleanStatus

```

**Type**
multipicklist

**Properties**
Create, Filter, Nillable, Restricted picklist, Update

**Description**
If Automatic Contact Enhancements or Buyer Relationship Map is enabled, this field contains
the role of the contact in the opportunity or account. Possible values are:

**•** `BusinessUser` —For example, an end user. Key value.

**•** `Buyer` —Key value

**•** `Champion` —Key value

**•** `DecisionMaker` —Shown in green on a contact in the buyer relationship map UI.
Key value.

**•** `Detractor` —Shown in red on a contact in the buyer relationship map UI. Key value.

**•** `Evaluator`

**•** `ExecutiveSponsor` —Key value

**•** `TechnicalExpert`

Key values represent key contacts on an opportunity or account. If a buyer relationship map
doesn’t have contacts with key values, then Salesforce prompts you to add them. Having all
key values represented on the map provides a full view of the deal or account, increasing
sales success.

Warning: To ensure that the buyer relationship map feature works as expected,
don't modify field values. For example, if you change `Detractor` to `Detract`,
the value isn’t shown in red in a buyer relationship map.

This field is available with all profiles except custom and minimum-access. To provide access,
use field-level security in Object Manager.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this contact can self-register for your Customer Portal ( `true` ) or not
( `false` ).

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects Contact

**Field** **Details**

**Description**
Indicates the record’s clean status as compared with Data.com. Values include: `Matched`,
`Different`, `Acknowledged`, `NotFound`, `Inactive`, `Pending`, `SelectMatch`,
or `Skipped` .

Several values for `CleanStatus` appear with different labels on the contact record.

**•** `Matched` appears as `In Sync`

**•** `Acknowledged` appears as `Reviewed`

**•** `Pending` appears as `Not Compared`

```
ConnectionReceivedId

ConnectionSentId

ContactSource

Department

```

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
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
If Automatic Contact Creation is enabled, this field indicates whether the contact was created
automatically. A possible value is:

**•** `Auto Create`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The contact’s department.


Standard Objects Contact

**Field** **Details**

```
DepartmentGroup

Description

DoNotCall

Email

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
If Automatic Contact Enhancements or Buyer Relationship Map is enabled, this field contains
the business unit, function, or department that the contact belongs to in the organization.
Possible values are:

**•** `chiefExecutive` —Key value

**•** `customerSuccess` —For example, wealth management, consumer banking, subject
matter experts, or healthcare research experts.

**•** `finance` —Includes pricing and procurement. Key value.

**•** `humanResources`

**•** `legal` —Key value

**•** `marketing`

**•** `other`

**•** `sales`

**•** `support` —For example, tech support or customer support.

**•** `tech` —For example, IT or engineering. Key value.

Key values represent key contacts on an opportunity or account. If a buyer relationship map
doesn’t have contacts with key values, then Salesforce prompts you to add them. Having all
key values represented on the map provides a full view of the deal or account, increasing
sales success. This field is available with all profiles except custom and minimum-access. To
provide access, use field-level security in Object Manager.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the contact. Label is **Contact Description** up to 32 KB.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates that the contact doesn’t want to receive calls.

**Type**
email


Standard Objects Contact

**Field** **Details**

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The contact’s email address.

```
EmailBouncedDate

EmailBouncedReason

Fax

FirstCallDateTime

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
If bounce management is activated and an email sent to the contact results in a hard bounce,
the date and time of the bounce.

Note: Email bounce functionality isn't triggered by record updates, including updates
to this field.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If bounce management is activated and an email sent to the contact results in a hard bounce,
the reason for the bounce.

Note: Email bounce functionality isn't triggered by record updates, including updates
to this field.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The contact’s fax number. Label is **Business Fax** .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time of the first call placed to the contact. This field is available in API version
48.0 and later when the Sales Engagement license is enabled. To see this field, the user also
needs the Sales Engagement User or Sales Engagement Quick Cadence Creator user
permission set.


Standard Objects Contact

**Field** **Details**

```
FirstEmailDateTime

FirstName

GenderIdentity

HasOptedOutOfEmail

HasOptedOutOfFax

HomePhone

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time of the first email sent to the contact. This field is available in API version
48.0 and later when the Sales Engagement license is enabled. To see this field, the user also
needs the Sales Engagement User or Sales Engagement Quick Cadence Creator user
permission set.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The contact’s first name up to 40 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The contact’s internal experience of their gender, which may or may not correspond to their
designated sex at birth.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the contact doesn’t want to receive email from Salesforce ( `true` ) or does
( `false` ). Label is **Email Opt Out** .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the contact prohibits receiving faxes.

**Type**
phone


Standard Objects Contact

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The contact’s home phone number. Label is **Home Phone** .

```
IndividualId

IsDeleted

IsEmailBounced

IsPersonAccount

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the data privacy record associated with this contact. This field is available if Data
Protection and Privacy is enabled.

This is a relationship field.

**Relationship Name**
Individual

**Relationship Type**
Lookup

**Refers To**
Individual

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
If bounce management is activated and an email is sent to a contact, indicates whether the
email results in a soft or hard bounce ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects Contact

**Field** **Details**

**Description**
Read only. Indicates whether this account has a record type of Person Account ( `true` ) or
not ( `false` ). Label is **Is Person Account** .

```
IsPriorityRecord

Jigsaw

JigsawContactId

LastActivityDate

```

**Type**
boolean

**Properties**
Defaulted on create, Group

**Description**
Shows whether the user has marked the contact as important ( _`True`_ ) or not ( _`False`_ ). The
default value is `false` . Available in API version 59.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
References the company’s ID in Data.com. If an account has a value in this field, it means
that the account was imported from Data.com. If the field value is `null`, the account wasn’t
imported from Data.com. Maximum size is 20 characters. Available in API version 22.0 and
later. Label is **Data.com Key** .

Important: The `Jigsaw` field is exposed in the API to support troubleshooting for
import errors and reimporting of corrected data. Do not modify this value.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the contact in reference to `Jigsaw` .

Important: The `Jigsaw` field is exposed in the API to support troubleshooting for
import errors and reimporting of corrected data. Don’t modify the value in the
`Jigsaw` field.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Value is the most recent of either:

**•** Due date of the most recent event logged against the record.


Standard Objects Contact

**Field** **Details**

**•** Due date of the most recently closed task associated with the record.

```
LastName

LastReferencedDate

LastViewedDate

LeadSource

MailingAddress

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. Last name of the contact up to 80 characters.

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
Create, Filter, Group, Nillable, Sort, Update

**Description**
The source of the lead that was converted to this contact.

**Type**
address

**Properties**
Filter, Nillable

**Description**
The compound form of the mailing address. Read-only. For details on compound address
fields, see Address Compound Fields.


Standard Objects Contact

**Field** **Details**

```
MailingCity

MailingCountry

MailingCountryCode

MailingGeocodeAccuracy

MailingLatitude

MailingLongitude

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Mailing address details.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Mailing address details.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO codes for the mailing address’s state and country.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update, Query, Restricted picklist, Nillable

**Description**
Accuracy level of the geocode for the mailing address. For details on geolocation compound
field, see Compound Field Considerations and Limitations.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `MailingLongitude` to specify the precise geolocation of a mailing address.
Acceptable values are numbers between –90 and 90 up to 15 decimal places. For details on
geolocation compound fields, see Compound Field Considerations and Limitations.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects Contact

**Field** **Details**

**Description**
Used with `MailingLatitude` to specify the precise geolocation of a mailing address.
Acceptable values are numbers between –180 and 180 up to 15 decimal places. For details
on geolocation compound fields, see Compound Field Considerations and Limitations.

```
MailingPostalCode

MailingState

MailingStateCode

MailingStreet

MasterRecordId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Mailing address details.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Mailing address details.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO codes for the mailing address’s state and country.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Street address for mailing address.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
If this record was deleted as the result of a merge, this field contains the ID of the record that
remains. If this record was deleted for any other reason, or hasn’t been deleted, the value is
`null` .

This is a relationship field.


Standard Objects Contact

**Field** **Details**

**Relationship Name**
MasterRecord

**Relationship Type**
Lookup

**Refers To**
Contact

```
MiddleName

MobilePhone

Name

OtherAddress

OtherCity

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The contact’s middle name. Maximum size is 40 characters.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Contact’s mobile phone number. Label is **Mobile Phone** .

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Concatenation of `FirstName`, `MiddleName`, `LastName`, and `Suffix` up to 203
characters, including whitespaces.

**Type**
address

**Properties**
Filter, Nillable

**Description**
The compound form of the other address. Read-only. For details on compound address fields,
see Address Compound Fields.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects Contact

**Field** **Details**

**Description**
Alternate address details.

```
OtherCountry

OtherCountryCode

OtherGeocodeAccuracy

OtherLatitude

OtherLongitude

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Alternate address details.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO codes for the alternate address’s state and country.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Accuracy level of the geocode for the other address. For details on geolocation compound
fields, see Compound Field Considerations and Limitations.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `OtherLongitude` to specify the precise geolocation of an alternate address.
Acceptable values are numbers between –90 and 90 up to 15 decimal places. For details on
geolocation compound fields, see Compound Field Considerations and Limitations.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `OtherLatitude` to specify the precise geolocation of an alternate address.
Acceptable values are numbers between –180 and 180 up to 15 decimal places. For details
on geolocation compound fields, see Compound Field Considerations and Limitations.


Standard Objects Contact

**Field** **Details**

```
OtherPhone

OtherPostalCode

OtherState

OtherStateCode

OtherStreet

OwnerId

```

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Phone for alternate address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Alternate address details.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Alternate address details.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO codes for the alternate address’s state and country.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Street for alternate address.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the account associated with this contact.


Standard Objects Contact

**Field** **Details**

This is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

```
Phone

PhotoUrl

Pronouns

```

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Phone number for the contact. Label is **Business Phone** .

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**

Path to be combined with the URL of a Salesforce instance ( _Example:_
https:// _`yourInstance`_ .salesforce.com/) to generate a URL to request the social network
profile image associated with the contact. Generated URL returns an HTTP redirect (code
302) to the social network profile image for the contact.

Empty if Social Accounts and Contacts isn't enabled or if Social Accounts and Contacts is
disabled for the requesting user.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The contact’s personal pronouns, reflecting their gender identity. Others can use these
pronouns to refer to the contact in the third person. The entry is selected from a picklist of
available values, which the administrator sets. Maximum 40 characters.

Possible values are:

**•** `He/Him`

**•** `He/They`

**•** `Not Listed`

**•** `She/Her`

**•** `She/They`


Standard Objects Contact

**Field** **Details**

**•** `They/Them`

```
RecordTypeId

ReportsToId

Salutation

ScheduledResumeDateTime

```

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
ID of the record type assigned to this object.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the contact that this contact reports to.

This is a relationship field.

**Relationship Name**
ReportsTo

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Honorific abbreviation, word, or phrase to be used in front of name in greetings, such as Dr.
or Mrs.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the action cadence tracker is going to resume after it’s paused or
on a wait step. This field is available in API version 54.0 and later when the Sales Engagement
license is enabled. To see this field, the user also needs the Sales Engagement User or Sales
Engagement Quick Cadence Creator user permission set.


Standard Objects Contact

**Field** **Details**

```
Suffix

Title

TitleType

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Name suffix of the contact. Maximum size is 40 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Title of the contact, such as CEO or Vice President.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
If Automatic Contact Enhancements or Buyer Relationship Map is enabled, this field contains
the hierarchical position that the contact holds in the organization. In the UI, this field is
shown as Seniority Level. Possible values are:

**•** `ceo` —Key value

**•** `directorOrManager` —Key value

**•** `executive` —Key value

**•** `individualContributor`

**•** `vp` —VP or Head of Department. Key value.

Key values represent key contacts on an opportunity or account. If a buyer relationship map
doesn’t show contacts with key values, then Salesforce prompts you to add them. Having
all key values represented on the map provides a complete picture of the deal or account,
increasing sales success. This field is available with all profiles except custom and
minimum-access. To provide access, use field-level security in Object Manager.

Note: When importing contact data, users need the Set Audit Fields upon Record Creation permission to assign values to audit
fields such as `CreatedDate` . Audit fields are automatically updated during API operations unless you set these fields yourself.

Usage

Use this object to manage individual people who are associated with an account. You can create, query, delete, or update any attachment
associated with a contact.

Create or update contacts by converting a lead with the `convertLead()` call.


### Standard Objects ContactCenterChannel

Associated Objects

This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**AccountChangeEvent (API version 44.0)**
Change events are available for the object.

**ContactFeed (API version 18.0)**
Feed tracking is available for the object.

**ContactHistory (API version 11.0)**
History is available for tracked fields of the object.

**ContactOwnerSharingRule**

Sharing rules are available for the object.

**ContactShare**

Sharing is available for the object.

SEE ALSO:

Overview of Salesforce Objects and Fields

### ContactCenterChannel

Represents a junction object that relates a Bring Your Own Channel for Contact Center as a Service (CCaaS) messaging channel to a
CallCenter object for Bring Your Own Channel for CCaaS. This object also represents the routing details for a voicemail configuration and
routing information for callback requests. This object is available in API version 56.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To access this object, Service Cloud Voice with Amazon Connect, Service Cloud Voice with Partner Telephony, Service Cloud Voice with
Partner Telephony from Amazon Connect, or Bring Your Own Channel for Contact Center as a Service (CCaaS) must be enabled. To
access this object, you must be a SysAdmin user or have ViewSetup user permissions.

Fields

**Field** **Details**

```
ChannelId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects ContactCenterChannel

**Field** **Details**

**Description**
For Bring Your Own Channel for CCaaS, this field represents the unique ID of the Bring Your
Own Channel messaging channel (MessagingChannel) that’s associated with the contact
center (CallCenterId). Available in API version 60.0 and later.

This field is a relationship field.

**Relationship Name**
Channel

**Refers To**
MessagingChannel

```
ContactCenterId

OmniCallbackFallbackQueueId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
This field is a relationship field. For Bring Your Own Channel for CCaaS, this field represents
the unique ID of the contact center (CallCenterId) that’s associated with the Bring Your Own
Channel messaging channel (MessagingChannel). Available in API version 60.0 and later.

This field is a relationship field.

**Relationship Name**
ContactCenter

**Relationship Type**
Master-detail

**Refers To**
CallCenter (the master object)

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If callbacks are configured for the contact center and the contact center uses Omni-Channel
Unified Routing, this field represents the unique ID of the fallback queue to use if contact
request routing through an Omni-Channel flow fails. Don't change the value in this field.
Instead, configure contact request routing in Lightning Experience.

Available in API version 65.0 and later.

This field is a relationship field.

**Relationship Name**
OmniCallbackFallbackQueue

**Refers To**
Group


Standard Objects ContactCenterChannel

**Field** **Details**

```
OmniCallbackHandler

UserId

VoicemailFallbackQueueId

VoicemailHandler

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
If callbacks are configured for the contact center and the contact center uses Omni-Channel
Unified Routing, this field represents the unique ID of the flow or queue used to route contact
requests. Don't change the value in this field. Instead, configure contact request routing in
Lightning Experience.

Available in API version 65.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Available in API version 63.0 only. For internal use.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If voicemail routing is configured for the contact center, this field represents the unique ID
of the fallback queue to use if voicemail routing fails. Don't change the value in this field.
Instead, configure voicemail routing in Lightning Experience.

This field is a relationship field.

**Relationship Name**
VoicemailFallbackQueue

**Refers To**
Group

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
If voicemail routing is configured for the contact center, this field represents the unique ID
of the flow used to route voicemails. Don't change the value in this field. Instead, configure
voicemail routing in Lightning Experience.


### Standard Objects ContactCleanInfo ContactCleanInfo

Stores the metadata Data.com Clean uses to determine a contact record’s clean status. Helps you automate the cleaning or related
processing of contact records. ContactCleanInfo includes a number of bit vector fields.

Note: When your Data.com Prospector or Data.com Clean contract expires, Data.com features, objects, and fields will be removed
from your org.

To support customers’ needs around compliance and to remain a leader in trust and privacy, Salesforce removed all contact data
from the Data.com service on February 1, 2021.

[For more information, see Data.com Prospector and Clean Retirement.](https://help.salesforce.com/articleView?id=000270376&language=en_US&type=1)

Contact Clean Info provides a snapshot of the data in your Salesforce contact record and its matched Data.com record at the time the
Salesforce record was cleaned.

Contact Clean Info includes a number of bit vector fields, whose component fields each correspond to individual object fields and provide
related data or status information about those fields. For example, the bit vector field `IsDifferent` has an `IsDifferentEmail`
field. If the `IsDifferentEmail` field’s value is `False`, that means the `Email` field value is _the same_ on the Salesforce contact
record and its matched Data.com record.

### ContactCleanInfo bit vector fields include:

**•** `CleanedBy` indicates who (a user) or what (a Clean job) cleaned the contact record.

**•** `IsDifferent` indicates whether or not a field on the contact record has a value that differs from the corresponding field on the
matched Data.com record.

**•** `IsFlaggedWrong` indicates whether or not a field on the contact record has a value that is flagged as wrong to Data.com.

**•** `IsReviewed` indicates whether or not a field on the contact record is in a `Reviewed` state, which means that the value was
reviewed but not accepted.

Fields

**Field Name** **Details**

```
Address

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
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Details for the billing address of the contact.


Standard Objects ContactCleanInfo

**Field Name** **Details**

```
CleanedByJob

CleanedByUser

ContactId

ContactStatusDataDotCom

Country

```

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact record was cleaned by a Data.com Clean job ( `true` )
or not ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact record was cleaned by a Salesforce user ( `true` )
or not ( `false` ).

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The unique, system-generated ID assigned when the contact record was created.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
The status of the contact per Data.com. Values are: `Contact is Active`
`per Data.com`, `Phone is Wrong per Data.com`, `Email is`
`Wrong per Data.com`, `Phone and Email are Wrong per`
`Data.com`, `Contact Not at Company per Data.com`, `Contact`
`is Inactive per Data.com`, `Company this contact`
`belongs to is out of business per Data.com`, `Company`

```
  this contact belongs to never existed per Data.com
```

or `Email address is invalid per Data.com` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ContactCleanInfo

**Field Name** **Details**

**Description**

Details for the billing address of the contact.

```
DataDotComID

Email

FirstName

IsDifferentCity

IsDifferentCountry

IsDifferentCountryCode

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID Data.com maintains for the contact.

**Type**
email

**Properties**
Filter, Group, Nillable, Sort

**Description**
The email address for the contact.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The contact’s first name.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact’s `City` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact’s `Country` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean


Standard Objects ContactCleanInfo

**Field Name** **Details**

**Properties**
Filter

**Description**
Indicates whether the contact’s `Country Code` field value is different from
the corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

```
IsDifferentEmail

IsDifferentFirstName

IsDifferentLastName

IsDifferentPhone

IsDifferentPostalCode

```

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact’s `Email` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact’s `First Name` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact’s `Last Name` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact’s `Phone` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter


Standard Objects ContactCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the contact’s `Postal Code` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

```
IsDifferentState

IsDifferentStateCode

IsDifferentStreet

IsDifferentTitle

IsFlaggedWrongAddress

```

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact’s `State` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact’s `State Code` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact’s `Street` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact’s `Title` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update


Standard Objects ContactCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the contact’s `Address` field value is flagged as wrong to
Data.com ( `true` ) or not ( `false` ).

```
IsFlaggedWrongEmail

IsFlaggedWrongName

IsFlaggedWrongPhone

IsFlaggedWrongTitle

IsInactive

```

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the contact’s `Email` field value is flagged as wrong to
Data.com ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the contact’s `Name` field value is flagged as wrong to Data.com
( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the contact’s `Phone` field value is flagged as wrong to
Data.com ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the contact’s `Title` field value is flagged as wrong to
Data.com ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects ContactCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the contact has been reported to Data.com as _`Inactive`_
( `true` ) or not ( `false` ).

```
IsReviewedAddress

IsReviewedEmail

IsReviewedName

IsReviewedPhone

IsReviewedTitle

```

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the contact’s `Address` field value is in a `Reviewed` state
( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the contact’s `Email` field value is in a `Reviewed` state
( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the contact’s `Name` field value is in a `Reviewed` state
( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the contact’s `Phone` field value is in a `Reviewed` state
( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update


Standard Objects ContactCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the contact’s `Title` field value is in a `Reviewed` state
( `true` ) or not ( `false` ).

```
LastMatchedDate

LastName

LastStatusChangedById

LastStatusChangedDate

Latitude

```

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date the contact record was last matched and linked to a Data.com record.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The contact’s last name.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of who or what last changed the record’s `Clean Status` field value:
a Salesforce user or a Clean job.

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


Standard Objects ContactCleanInfo

**Field Name** **Details**

```
Longitude

Name

Phone

PostalCode

State

Street

```

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
Field label is **Contact Clean Info Name** . The name of the contact. Maximum
size is 255 characters.

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
The phone number for the contact.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Details for the billing address of the contact.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Details for the billing address of the contact.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects ContactDailyMetric

**Field Name** **Details**

**Description**

Details for the billing address of the contact.

```
Title

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The contact’s title.

Developers can create triggers that read the Contact Clean Info fields to help automate the cleaning or related processing of contact
records.

Create a customized set of `Title` field values. Use triggers to map values from fields on imported or cleaned records onto a standard
set of values.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ContactCleanInfoChangeEvent (API version 62.0)**
Change events are available for the object.

### ContactDailyMetric

Represents the daily engagement metrics for a contact. This object is available in API version 52.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Inbox must be enabled.


Standard Objects ContactDailyMetric

Fields

**Field** **Details**

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
The number of calls in the day for this contact with the call result Call Back Later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the day for this contact with the call result Left Voicemail.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the day for this contact with the call result Meaningful Connect.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the day for this contact with the call result Not Interested.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the day for this contact with no call result specified.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ContactDailyMetric

**Field** **Details**

**Description**
The number of calls in the day for this contact with the call result Unqualified.

```
AllEmailsBouncedCount

AllEmailsDeliveredCount

AllEmailsDeliveredRate

AllEmailsHardBouncedCount

AllEmailsOutOfOfficeCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total of hard and soft bounced emails for this contact in the day.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of successfully delivered emails for this contact in the day.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of tracked emails sent that were successfully delivered to this contact. This
field is a calculated field.

Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of hard bounced emails for this contact in the day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that triggered an out of office reply for this contact in the day.


Standard Objects ContactDailyMetric

**Field** **Details**

```
AllEmailsSentCount

AllEmailsSoftBouncedCount

AllEmailsTrackedSentCount

AllEmailsUntrackedSentCount

AllTotalCallsCount

ContactId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact in the day.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails soft bounced for this contact in the day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact with engagement tracking enabled in the day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact without engagement tracking enabled in the day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of calls to this contact with all call results in the day.

This is a calculated field.

**Type**
reference

**Properties**
Filter, Group, Sort


Standard Objects ContactDailyMetric

**Field** **Details**

**Description**
The ID of the related contact.

This is a relationship field.

**Relationship Name**
Contact

**Relationship Type**
Lookup

**Refers To**
Contact

```
DailyCutOffTimeStamp

Date

DateInt

HardBounceTrackableSends

InboundEngagementsCount

```

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
The number of emails sent to this contact with hard bounce tracking.

Available in API version 54.0 and later.

**Type**
int


Standard Objects ContactDailyMetric

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of inbound engagements for this contact in the day. This field is a calculated
field. The value is the sum of `UniqueEmailsOpenedCount`,
`UniqueEmailsRepliedCount`, and `UniqueEmailsLinkClickedCount` .

Available in API version 58.0 and later.

```
LinkClickTrackableSends

OpenTrackableSends

OutOfOfficeTrackableSends

OutboundEngagementsCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact with link click tracking.

Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact with open tracking.

Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact with out-of-office tracking.

Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of outbound engagements for this contact in the day. This field is a calculated
field. The value is the sum of `AllTotalCallsCount` and
`AllEmailsDeliveredCount` .

Available in API version 58.0 and later.


Standard Objects ContactDailyMetric

**Field** **Details**

```
ReplyTrackableSends

SoftBounceTrackableSends

TrackableSendHardBounceRate

TrackableSendLinkClickRate

TrackableSendOpenRate

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact with reply tracking.

Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact with soft bounce tracking.

Available in API version 54.0 and later.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this contact with hard bounce tracking that hard bounced.
This field is a calculated field.

Available in API version 54.0 and later.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this contact with link tracking that had link clicks. This field
is a calculated field.

Available in API version 54.0 and later.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this contact with open tracking that were opened by the
recipient. This field is a calculated field.


Standard Objects ContactDailyMetric

**Field** **Details**

Available in API version 54.0 and later.

```
TrackableSendOutOfOfficeRate

TrackableSendReplyRate

TrackableSendSoftBounceRate

UniqueEmailsLinkClickedCount

UniqueEmailsOpenedCount

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this contact with out-of-office tracking that received
out-of-office replies. This field is a calculated field.

Available in API version 54.0 and later.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this contact with reply tracking that received replies. This
field is a calculated field.

Available in API version 54.0 and later.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this contact with soft bounce tracking that soft bounced.
This field is a calculated field.

Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of individual emails in which the contact clicked a link in the day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects ContactMonthlyMetric

**Field** **Details**

**Description**
The number of individual emails opened by the contact in the day.

```
UniqueEmailsRepliedCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of individual emails replied to by the contact in the day.

### ContactMonthlyMetric

Represents the monthly engagement metrics for a contact. This object is available in API version 52.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Inbox must be enabled.

Fields

**Field** **Details**

```
AllCallsCallBackLater

AllCallsLeftVoicemail

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this contact with the call result Call Back Later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this contact with the call result Left Voicemail.


Standard Objects ContactMonthlyMetric

**Field** **Details**

```
AllCallsMeaningfulConnect

AllCallsNotInterested

AllCallsUncategorized

AllCallsUnqualified

AllEmailsBouncedCount

AllEmailsDeliveredCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this contact with the call result Meaningful Connect.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this contact with the call result Not Interested.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this contact with no call result specified.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this contact with the call result Unqualified.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total of hard and soft bounced emails for this contact in the month.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ContactMonthlyMetric

**Field** **Details**

**Description**
The number of successfully delivered emails for this contact in the month.

This is a calculated field.

```
AllEmailsDeliveredRate

AllEmailsHardBouncedCount

AllEmailsOutOfOfficeCount

AllEmailsSentCount

AllEmailsSoftBouncedCount

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of tracked emails sent that were successfully delivered to this contact.
Available in API version 54.0 and later.

This field is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of hard bounced emails for this contact in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that triggered an out of office reply for this contact in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact in the month.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails soft bounced for this contact in the month.


Standard Objects ContactMonthlyMetric

**Field** **Details**

```
AllEmailsTrackedSentCount

AllEmailsUntrackedSentCount

AllTotalCallsCount

ContactId

HardBounceTrackableSends

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact with engagement tracking enabled in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact without engagement tracking enabled in the
month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of calls to this contact with all call results in the month.

This is a calculated field.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related contact.

This is a relationship field.

**Relationship Name**
Contact

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ContactMonthlyMetric

**Field** **Details**

**Description**
The number of emails sent to this contact with hard bounce tracking. Available in API version
54.0 and later.

```
LinkClickTrackableSends

Month

MonthInt

OpenTrackableSends

OutOfOfficeTrackableSends

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact with link click tracking. Available in API version
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
The month in which the engagement occurred, in yyyymm format.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact with open tracking. Available in API version 54.0
and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact with out-of-office tracking. Available in API version
54.0 and later.


Standard Objects ContactMonthlyMetric

**Field** **Details**

```
ReplyTrackableSends

SoftBounceTrackableSends

TrackableSendHardBounceRate

TrackableSendLinkClickRate

TrackableSendOpenRate

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact with reply tracking. Available in API version 54.0
and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact with soft bounce tracking. Available in API version
54.0 and later.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this contact with hard bounce tracking that hard bounced.
Available in API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this contact with link tracking that had link clicks. Available
in API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this contact with open tracking that were opened by the
recipient. Available in API version 54.0 and later.


Standard Objects ContactMonthlyMetric

**Field** **Details**

This field is a calculated field.

```
TrackableSendOutOfOfficeRate

TrackableSendReplyRate

TrackableSendSoftBounceRate

UniqueEmailsLinkClickedCount

UniqueEmailsOpenedCount

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this contact with out-of-office tracking that received
out-of-office replies. Available in API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this contact with reply tracking that received replies.
Available in API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this contact with soft bounce tracking that soft bounced.
Available in API version 54.0 and later.

This field is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of individual emails in which the contact clicked a link in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects ContactPointAddress

**Field** **Details**

**Description**
The number of individual emails opened by the contact in the month.

```
UniqueEmailsRepliedCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of individual emails replied to by the contact in the month.

### ContactPointAddress

Represents a contact’s billing or shipping address, which is associated with an individual or person account. This object is available in
API version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ActiveFromDate

ActiveToDate

Address

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the contact’s address became active.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the contact’s address is no longer active.

**Type**
address


Standard Objects ContactPointAddress

**Field** **Details**

**Properties**
Filter, Nillable

**Description**
The full address.

```
AddressFirstName

AddressLastName

AddressMiddleName

AddressType

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
First name associated with the address.

The field is available only if the B2B Commerce license is enabled.

This field is available in API version 57.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Last name associated with the address.

The field is available only if the B2B Commerce license is enabled.

This field is available in API version 57.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Middle name associated with the address.

The field is available only if the B2B Commerce license is enabled.

This field is available in API version 57.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the type of address.

Possible values are:

**•** `Billing`


Standard Objects ContactPointAddress

**Field** **Details**

**•** `Shipping`

```
BestTimeToContactEndTime

BestTimeToContactStartTime

BestTimeToContactTimezone

City

CompanyName

ContactPointPhoneId

```

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The latest time to contact the individual.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The earliest time to contact the individual.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The time zone applied to the best time to contact the individual.

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
Company name associated with the address.

The field is available only if the B2B Commerce license is enabled.

This field is available in API version 57.0 and later.

**Type**
reference


Standard Objects ContactPointAddress

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Represents the primary phone number associated with this address.

This is a relationship field.

**Relationship Name**
ContactPointPhone

**Relationship Type**
Lookup

**Refers To**
ContactPointPhone

```
Country

GeocodeAccuracy

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The address country.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The level of accuracy of a location’s geographical coordinates compared with its physical
address. A geocoding service typically provides this value based on the address’s latitude
and longitude coordinates.

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


Standard Objects ContactPointAddress

**Field** **Details**

```
IsDefault

IsPrimary

IsThirdPartyAddress

LastReferencedDate

LastViewedDate

Latitude

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a contact’s address is the preferred method of communication ( `true` )
or not ( `false` ). The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a contact’s address is their primary address ( `true` ) or not ( `false` ). The
default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the address is associated with a third party ( `true` ) or not ( `false` ). The
default value is `false` .

This field is available in API version 57.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last referenced a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced ( `LastReferencedDate` ) and not viewed.

**Type**
double


Standard Objects ContactPointAddress

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `Longitude` to specify the precise geolocation of the address. Acceptable values
are numbers between –90 and 90 with up to 15 decimal places.

```
Longitude

Name

OwnerId

ParentId

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `Latitude` to specify the precise geolocation of the address. Acceptable values
are numbers between –180 and 180 with up to 15 decimal places.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. The name of the contact point address record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the account’s owner associated with this contact.

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


Standard Objects ContactPointAddress

**Field** **Details**

**Description**
The ID of the contact’s parent record. Only an individual or account can be a contact’s parent.
Because this is a master-detail relationship, users must have Edit access to the parent record
to create or modify a Contact Point Address.

This is a polymorphic relationship field.

**Relationship Name**
Parent

**Relationship Type**
Master-detail

**Refers To**
Account, Individual

```
PhoneNumber

PostalCode

PreferenceRank

State

```

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Phone number associated with the address.

The field is available only if the B2B Commerce license is enabled.

This field is available in API version 57.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The address postal code.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Preference rank when there are multiple contact point addresses.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The address state.


### Standard Objects ContactPointConsent

**Field** **Details**

```
Street

UsageType

```

Associated Objects

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The address street.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specify the usage type of this address. For instance, whether it’s a work address or a home
address.

Possible values are:

**•** `Home`

**•** `Inactive`

**•** `Temporary`

**•** `Work`

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ContactPointAddressChangeEvent**

Change events are available for the object.

**ContactPointAddressHistory**

History is available for tracked fields of the object.

**ContactPointAddressShare**

Sharing is available for the object.

### ContactPointConsent

Represents a customer's consent to be contacted via a specific contact point, such as an email address or phone number. This object is
available in API version 48.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects ContactPointConsent

Fields

With certain page layout and field-level security settings, some fields aren't visible or editable.

**Field** **Details**

```
BusinessBrandId

CaptureContactPointType

CaptureDate

CaptureSource

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Business Brand that the individual has given consent to for a contact point. This
is a relationship field. This field is available in API version 53.0 and later.

**Relationship Name**
BusinessBrand

**Relationship Type**
Lookup

**Refers To**
BusinessBrand

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

**Type**
string


Standard Objects ContactPointConsent

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. Indicates how you captured consent. For example, a website or online form.

```
ContactPointId

DataUsePurposeId

DoubleConsentCaptureDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the contact point record through which the customer is consenting to be contacted.

This is a polymorphic relationship field.

**Relationship Name**
ContactPoint

**Relationship Type**
Lookup

**Refers To**
ContactPointAddress, ContactPointEmail, ContactPointPhone

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the data use purpose record that you want to associate this consent with.

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
Create, Filter, Nillable, Sort, Update

**Description**
Date when double opt-in was captured.


Standard Objects ContactPointConsent

**Field** **Details**

```
EffectiveFrom

EffectiveTo

EngagementChannelTypeId

LastReferencedDate

LastViewedDate

Name

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date when consents starts.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

Date when consent ends.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

ID of the engagement channel record through which the customer is consenting to be
contacted.

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


Standard Objects ContactPointConsent

**Field** **Details**

**Description**
Name of the contact point type consent record.

```
OwnerId

PartyRoleId

PrivacyConsentStatus

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the account owner associated with this customer.

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
The ID of the Party Role for the individual you want to associate consent with. This is a
polymorphic relationship field. This field is available in API version 53.0 and later.

**Relationship Name**
PartyRole

**Relationship Type**
Lookup

**Refers To**
Customer, Seller

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. Identifies whether the individual or person account associated with this record
agrees to this form of contact.

Possible values are:

**•** `NotSeen`

**•** `OptIn`


### Standard Objects ContactPointEmail

**Field** **Details**

**•** `OptInPending` —Available in API version 58.0 and later.

**•** `OptOut`

**•** `Seen`

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ContactPointConsentChangeEvent**

Change events are available for the object.

**ContactPointConsentHistory**

History is available for tracked fields of the object.

**ContactPointConsentOwnerSharingRule**

Sharing rules are available for the object.

**ContactPointConsentShare**

Sharing is available for the object.

### ContactPointEmail

Represents a contact’s email, which is associated with an individual or person account. This object is available in API version 48.0 and
later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ActiveFromDate

ActiveToDate

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the contact’s email became active.

**Type**
date


Standard Objects ContactPointEmail

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the contact’s email is no longer active.

```
BestTimeToContactEndTime

BestTimeToContactStartTime

BestTimeToContactTimezone

EmailAddress

EmailDomain

EmailLatestBounceDateTime

```

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The latest time to contact the individual.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The earliest time to contact the individual.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The timezone applied to the best time to contact the individual.

**Type**
email

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The email address of the contact.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The domain of the contact’s email, which is everything after the @ sign.

**Type**
dateTime


Standard Objects ContactPointEmail

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time when an email failed to reach its recipient.

```
EmailLatestBounceReasonText

EmailMailBox

IsPrimary

LastReferencedDate

LastViewedDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The reason why the email didn’t reach its recipient.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A subset of the contact’s email, which is everything before the @ sign.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a contact’s email is their primary email ( `true` ) or not ( `false` ).

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


Standard Objects ContactPointEmail

**Field** **Details**

```
Name

OwnerId

ParentId

UsageType

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Required. The name of the contact point email record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the account’s owner associated with this contact.

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
The ID of the contact’s parent. Only an individual or account can be a contact’s parent.

This is a polymorphic relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Account, Individual

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects ContactPointPhone

**Field** **Details**

**Description**
Specify the usage type of this email. For instance, whether it’s a work email or a temporary
email.

Possible values are:

**•** `Home`

**•** `Temp`

**•** `Work`

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ContactPointConsentChangeEvent**

Change events are available for the object.

**ContactPointEmailHistory**

History is available for tracked fields of the object.

**ContactPointEmailOwnerSharingRule**

Sharing rules are available for the object.

**ContactPointEmailShare**

Sharing is available for the object.

### ContactPointPhone

Represents a contact’s phone number, which is associated with an individual or person account. This object is available in API version
48.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ActiveFromDate

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects ContactPointPhone

**Field** **Details**

**Description**
The date when the contact’s phone number became active.

```
ActiveToDate

AreaCode

BestTimeToContactEndTime

BestTimeToContactStartTime

BestTimeToContactTimezone

ExtensionNumber

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the contact’s phone number is no longer active.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The area code of the phone number’s location for the contact.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The latest time to contact the individual.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The earliest time to contact the individual.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The timezone applied to the best time to contact the individual.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects ContactPointPhone

**Field** **Details**

**Description**
The phone number extension for the contact.

```
FormattedInternationalPhoneNumber

FormattedNationalPhoneNumber

IsBusinessPhone

IsFaxCapable

IsPersonalPhone

IsPrimary

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The internationally recognized format for the contact’s phone number.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The nationally recognized format for the contact’s phone number.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a contact’s phone number is a business number ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a contact’s phone number is a fax number ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a contact’s phone number is a personal number ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects ContactPointPhone

**Field** **Details**

**Description**
Indicates whether a contact’s phone number is their primary number ( `true` ) or not ( `false` ).

```
IsSmsCapable

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
Indicates whether a contact’s phone number can receive text messages ( `true` ) or not
( `false` ).

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
Filter, Group, idLookup, Nillable, Sort

**Description**
Required. The name of the contact point phone record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the account’s owner associated with this contact.

This is a polymorphic relationship field.


Standard Objects ContactPointPhone

**Field** **Details**

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

```
ParentId

PhoneType

PreferenceRank

TelephoneNumber

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the contact’s parent. Only an individual or account can be a contact’s parent.

This is a polymorphic relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Account, Individual

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of phone number for the contact.

Possible values are:

**•** `Home`

**•** `Mobile`

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specify how this phone numbers ranks in terms of preference among the contact’s other
phone numbers.

**Type**
phone


### Standard Objects ContactPointTypeConsent

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The phone number for the contact.

```
UsageType

```

Associated Objects

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specify the usage type of this number. For instance, whether it’s a work phone or a home
phone.

Possible values are:

**•** `Home`

**•** `Temp`

**•** `Work`

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ContactPointConsentChangeEvent**

Change events are available for the object.

**ContactPointPhoneHistory**

History is available for tracked fields of the object.

**ContactPointPhoneOwnerSharingRule**

Sharing rules are available for the object.

**ContactPointPhoneShare**

Sharing is available for the object.

### ContactPointTypeConsent

Represents consent for a contact point type, such as email or phone. This object is available in API version 45.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects ContactPointTypeConsent

Special Access Rules

This object is available if Data Protection and Privacy is enabled.

Fields

With certain page layout and field-level security settings, some fields aren't visible or editable.

**Field Name** **Details**

```
BusinessBrandId

CaptureContactPointType

CaptureDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Business Brand that the individual has given consent to for a contact
point type. this is a relationship field. This field is available in API version 53.0 and
later.

**Relationship Name**
BusinessBrand

**Relationship Type**
Lookup

**Refers To**
BusinessBrand

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Required. Indicates how you captured consent. Possible values are:

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


Standard Objects ContactPointTypeConsent

**Field Name** **Details**

```
CaptureSource

ContactPointType

DataUsePurposeId

DoubleConsentCaptureDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. Indicates how you captured consent. For example, a website or online
form.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Required. Represents the contact method you want to apply consent to. Possible
values are:

**•** `Email`

**•** `MailingAddress`

**•** `Phone`

**•** `Social`

**•** `Web`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Represents the record for data use purpose that you want to associate this consent
with.

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
Create, Filter, Nillable, Sort, Update


Standard Objects ContactPointTypeConsent

**Field Name** **Details**

**Description**
Date when double opt-in was captured.

```
EffectiveFrom

EffectiveTo

EngagementChannelType

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date when consents starts.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

Date when consent ends.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Required if a `ContactPointType` isn’t selected. Represents the contact
method you want to apply consent to. Possible values are:

**•** `Billboard`

**•** `Email`

**•** `MailingAddress`

**•** `Phone`

**•** `SMS`

**•** `Social`

**•** `Web`

This is a relationship field.

**Relationship Name**
EngagementChannelType

**Relationship Type**
Lookup

**Refers To**
EngagementChannelType


Standard Objects ContactPointTypeConsent

**Field Name** **Details**

```
LastReferencedDate

LastViewedDate

Name

OwnerId

PartyId

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
Name of the contact point type consent record.

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
reference


Standard Objects ContactPointTypeConsent

**Field Name** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. Represents the record based on the Individual object you want to
associate consent with.

This is a relationship field.

**Relationship Name**
Party

**Relationship Type**
Lookup

**Refers To**
Individual

```
PartyRoleId

PrivacyConsentStatus

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Party Role for the individual you want to associate consent with.
This is a polymorphic relationship field. This field is available in API version 53.0
and later.

**Relationship Name**
PartyRole

**Relationship Type**
Lookup

**Refers To**
Customer, Seller

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. Identify whether the individual associated with this record agrees to
this form of contact. Possible values are:

**•** `NotSeen`

**•** `Seen`

**•** `OptIn`

**•** `OptInPending` —Available in API version 58.0 and later.

**•** `OptOut`

**•** `OptOutPending` —Available in API version 58.0 and later.


### Standard Objects ContactOwnerSharingRule

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ContactPointConsentChangeEvent (API version 47.0)**
Change events are available for the object.

**ContactPointTypeConsentHistory**

History is available for tracked fields of the object.

**ContactPointTypeConsentOwnerSharingRule**

Sharing rules are available for the object.

**ContactPointTypeConsentShare**

Sharing is available for the object.

### ContactOwnerSharingRule

Represents the rules for sharing a contact with a User other than the owner.

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
ContactAccessLevel

Description

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A value that represents the type of access granted to the target Group, UserRole, or
User for Contacts. The possible values are:

**•** `Read`

**•** `Edit`

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects ContactOwnerSharingRule

**Field** **Details**

**Description**
A description of the sharing rule. Maximum size is 1000 characters. This field is available
in API version 29.0 and later.

```
DeveloperName

GroupId

Name

UserOrGroupId

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
performance may slow while Salesforce generates one for each record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the source group. A Contact owned by a User in the source Group
triggers the rule to give access.

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


### Standard Objects ContactRequest

**Field** **Details**

**Description**
The ID representing the User or Group being granted access.

Usage

Use this object to manage the sharing rules for contacts.

SEE ALSO:

### Contact

ContactShare

_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_sharingrules.htm)_ : SharingRules

### ContactRequest

Represents a customer’s request for support to get back to them about an issue. This object is available in API version 45.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
AvailableCallbackAttempts

DelayBetweenCallbackAttempts

```

**Type**
integer

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the number of retries that are possible for a voice callback. Applies to
calls routed through Omni-Channel Unified Routing. Valid values are `0` through
`5` . The default is `0` .

Available in API version 66.0 and later.

**Type**
integer

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects ContactRequest

**Field Name** **Details**

**Description**
Specifies the delay between voice callback attempts in minutes. Applies to calls
routed through Omni-Channel Unified Routing. Valid values are `0` through
`10,080`, and the default is `0` .

Available in API version 66.0 and later.

```
IsCallback

LastReferencedDate

LastViewedDate

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines how a voice call callback is handled after an agent accepts the callback
work item.

If set to `true`, when an agent accepts the work item, the Omni-Channel utility
doesn’t immediately dial the callback phone number. Instead, the agent can
determine how to handle the call. For example, after the agent accepts the work
item, they can view the callback details, transfer the call, or contact the end user
at another phone number. If the agent makes a call by using click-to-dial, the
call appears as a Callback call in the Omni-Channel utility.

If set to `false`, when the agent accepts the work item in the Omni-Channel
utility, the contact request is opened. The agent can review callback details. If
they call with click-to-dial, the call appears as an Outbound call in the
Omni-Channel utility.

The default value is `false` . Available in API version 60.0 and later.

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


Standard Objects ContactRequest

**Field Name** **Details**

```
Name

OwnerId

PreferredChannel

PreferredPhone

RequestDescription

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The contact request number.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the Salesforce record that owns the request.

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
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The channel the customer selected as their preferred method of communication
in the contact request flow. For example:

**•** Phone

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The phone number the customer provided when requesting help in the contact
request flow.

**Type**
textarea


Standard Objects ContactRequest

**Field Name** **Details**

**Properties**
Create, Nillable, Update

**Description**
The description of the customer’s issue that they provided when requesting help
in the contact request flow.

```
RequestReason

Status

WhatId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The reason the customer provided when requesting help in the contact request
flow. These values are customizable in Object Manager. The default values are:

**•** Account

**•** Billing

**•** Case

**•** General

**•** Order

**•** Other

**•** Product

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The status of the contact request. For example:

**•** Abandoned

**•** Attempted

**•** Contacted

**•** New

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Salesforce record the contact request is related to, such as an account,
case, opportunity, voice call, or work order.

This is a polymorphic relationship field.


Standard Objects ContactRequest

**Field Name** **Details**

**Relationship Name**
What

**Relationship Type**
Lookup

**Refers To**
Account, Case, Contact Request, Opportunity, WorkOrder

```
WhoId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Salesforce contact record the contact request is related to, such as a
contact, lead, or user.

This is a polymorphic relationship field.

**Relationship Name**
Who

**Relationship Type**
Lookup

**Refers To**
Contact, Lead, User

Contact request records are created when a customer fills out an online form. This form is created using a flow that uses the type
`ContactRequestFlow` . There’s a guided setup experience to create this flow on the Customer Contact Requests page in Setup.
You then add the flow to an Experience Cloud site using either the Flows component or the Contact Request Button & Flow component.

Contact Request works in Experience Cloud sites, whether they require authentication or not. Make sure that your users have the Run
Flows permission, including your Guest User profile. Without this permission, members won’t see the button or the form to submit
contact requests.

By default, all Standard User and System Administrator profiles have access to the object. Make sure that your users profiles, like service
agents, have at least read access on the contact request object.

You can create queues for contact requests and route them with Omni-Channel.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ContactRequestOwnerSharingRule**

Sharing rules are available for the object.


### Standard Objects ContactRequestShare **ContactRequestShare**

Sharing is available for the object.

SEE ALSO:

_Salesforce Help_ [: Set Up and Manage Contact Requests](https://help.salesforce.com/articleView?id=contact_request.htm&language=en_US)

### ContactRequestShare

Represents a list of access levels to a ContactRequest with an explanation of the access level. This object is available in API version 45.0
and later.

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual` . Sharing entries
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

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
Level of access that the User or Group has to contact requests. The possible values
are:

**•** `Read`

**•** `Edit`

**•** `All` (This value is not valid for `create()` or `update()` calls.)

This value must be set to an access level that is higher than the organization’s
default access level for contact requests.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


Standard Objects ContactRequestShare

**Field Name** **Details**

**Description**
ID of the parent object, if any.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
ContactRequest

```
RowCause

UserOrGroupId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only
permitted value is `Manual` . If no value is specified, the field defaults to `Manual` .
All other `RowCause` values are read-only. After the sharing entry is created,
this field can’t be edited.

Possible values are:

**•** `Manual` —The User or Group has access because a user with “All” access
manually shared the ContactRequest with them.

**•** `Owner` —The User is the owner of the ContactRequest.

**•** `Rule` —The User or Group has access via a ContactRequest sharing rule.

**•** `GuestRule` —The User or Group has access via a ContactRequest guest
user sharing rule.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the User or Group that has been given access to the ContactRequest.

This is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Relationship Type**
Lookup

**Refers To**
Group, User


### Standard Objects ContactShare

Usage

This object lets you determine which users and groups can view and edit ContactRequest records owned by other users.

If you attempt to create a new record that matches an existing record, the `create()` call updates any modified fields and returns the
existing record.

SEE ALSO:

_Salesforce Help_ [: Set Up and Manage Contact Requests](https://help.salesforce.com/articleView?id=contact_request.htm&language=en_US)

### ContactShare

Represents a list of access levels to a Contact along with an explanation of the access level. For example, if you have access to a record
because you own it, the `ContactAccessLevel` is `All` and `RowCause` is Owner.

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual` . Sharing entries
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

As of Summer ’20 and later, only users with access to the Contact object can access this object.

Fields

**Field** **Details**

```
ContactId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the Contact associated with this sharing entry. This field can't be updated.

This is a relationship field.

**Relationship Name**
### Contact

**Relationship Type**
Lookup


Standard Objects ContactShare

**Field** **Details**

**Refers To**
Contact

```
ContactAccessLevel

IsDeleted

RowCause

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Level of access that the User or Group has to cases associated with the account Contact. The
possible values are:

**•** `Read`

**•** `Edit`

**•** `All` This value is not valid for create or update.

This field must be set to an access level that is higher than the organization’s default access
level for contacts.

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
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only permitted
value is `Manual` . If no value is specified, the field defaults to `Manual` . All other `RowCause`
values are read-only. After the sharing entry is created, this field can’t be edited. Valid values
include:

**•** `Rule` —The User or Group has access via a Contact sharing rule.

**•** `GuestRule` —The User or Group has access via a Contact guest user sharing rule.

**•** `ImplicitChild` —The User or Group has access to the Contact via sharing access on
the associated Account. After faster account sharing recalculation is enabled for your org,
sharing entries with this value aren’t returned in queries. Instead of storing implicit child
shares, record access is determined dynamically.

**•** `ImplicitPerson` —The User or Group has access to the business contact of a person
account via access to the person account itself.


### Standard Objects ContactSuggestionInsight

**Field** **Details**

**•** `GuestPersonImplicit` —The guest user has access to the business contact of a
person account via a Contact sharing rule.

**•** `PortalImplicit` —The Contact is associated with the portal user.

**•** `LpuImplicit` —The User has access to records owned by high-volume Experience
Cloud site users via a share group.

**•** `ARImplicit` —The User, who belongs to a partner or customer account, has access
to the Contact via an account relationship data sharing rule.

**•** `Manual` —The User or Group has access because a User with “All” access manually shared
the Contact with them.

**•** `Owner` —The User is the owner of the Contact.

```
 UserOrGroupId

```

Usage

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the User or Group that has been given access to the Contact. This field can't be updated.

This is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Relationship Type**
Lookup

**Refers To**
Group, User

This object allows you to determine which users and groups can view or edit Contact records owned by other users.

Note: After faster account sharing recalculation is enabled for your org, we no longer store implicit share records between accounts
and their child contact records. Sharing entries that have a value of `ImplicitChild` in the `RowCause` field aren’t returned
when you query this object. Instead, the system dynamically determines whether users can access child contact records when
they try to access them. This change speeds up ownership and sharing recalculation for accounts.

[For more information, see the Faster Account Sharing Recalculation knowledge article.](https://help.salesforce.com/s/articleView?id=000394638&type=1&language=en_US)

SEE ALSO:

AccountShare

### ContactSuggestionInsight

Represents a suggestion for a new contact record. Available in API versions 45.0 and later.


Standard Objects ContactSuggestionInsight

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

To add or decline contact suggestions, users need a Sales Cloud Einstein license and edit access on accounts. As of the Spring ’20 release,
Pardot and Sales Engagement users no longer have access to this object.

Fields

**Field Name** **Details**

```
AccountId

Address

City

ContactTitle

Country

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related account.

**Type**
address

**Properties**
Filter, Nillable

**Description**
The address of the suggested contact.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The city of the suggested contact.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The title of the suggested contact.

**Type**
string


Standard Objects ContactSuggestionInsight

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The country of the suggested contact.

```
CreatedRecordId

CurrencyIsoCode

Division

Email

FirstName

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the created contact record.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The division of the suggested contact.

**Type**
email

**Properties**
Filter, Group, Nillable, Sort

**Description**

The email address of the suggested contact.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The first name of the suggested contact.


Standard Objects ContactSuggestionInsight

**Field Name** **Details**

```
GeocodeAccuracy

LastName

LastOperationUserId

LastReferencedDate

LastViewedDate

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Accuracy level of the geocode for the address. See Compound Field
Considerations and Limitations for details on geolocation compound fields.

Note: This field is available in the API only.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The last name of the suggested contact.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who last performed a related operation.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related
to this record, or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, the user might have only accessed this record or list view
( `LastReferencedDate` ) but not viewed it.


Standard Objects ContactSuggestionInsight

**Field Name** **Details**

```
Latitude

Longitude

Phone

PostalCode

RationaleLabel

State

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Used in conjunction with `Longitude` to specify the precise geolocation of an
address.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Used in conjunction with `Latitude` to specify the precise geolocation of an
address.

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
The phone number of the suggested contact.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The postal code of the suggested contact.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The reason why this entry is a suggested contact.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects ContactTag

**Field Name** **Details**

**Description**
The state of the suggested contact.

```
Status

Street

```

Usage

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the suggested contact. Possible values include:

**•** New

**•** Pending

**•** Added

**•** Declined

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
The street of the suggested contact.

This object is read-only and isn’t supported in workflows, triggers, process builder, or Visualforce pages.

### ContactTag

Associates a word or short phrase with a Contact.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
ItemId

```

**Type**
reference


Standard Objects ContactTag

**Field Name** **Details**

**Properties**
Create, Filter

**Description**
ID of the tagged item.

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

ContactTag stores the relationship between its parent TagDefinition and the Contact being tagged. Tag objects act as metadata, allowing
users to describe and organize their data.

When a tag is deleted, its parent TagDefinition will also be deleted if the name is not being used; otherwise, the parent remains. Deleting
a TagDefinition sends it to the Recycle Bin, along with any associated tag entries.


### Standard Objects ContentAsset ContentAsset

Represents a Salesforce file that has been converted to an asset file in a custom app in Lightning Experience. Use asset files for org setup
and configuration. Asset files can be packaged and referenced by other components. This object is available in API version 38.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

**•** Only admin users can edit or delete ContentAssets.

**•** Users with file access can create and query ContentAssets.

**•** It isn’t necessary to create asset files for regular, collaborative use of Salesforce Files. “Assetize” files only when they’re used in setup
and configuration situations.

**•** Neither the file (ContentDocument) nor the asset settings record (ContentAssets) can be deleted if the asset file is referenced by
another component.

### • ContentAsset doesn’t support search or most recently used (MRU) lists. • ContentAsset doesn’t support Apex triggers.

Fields

**Field** **Details**

```
ContentDocumentId

DeveloperName

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the document.

This is a relationship field.

**Relationship Name**
ContentDocument

**Relationship Type**
Lookup

**Refers To**
ContentDocument

**Type**
string


Standard Objects ContentAsset

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the asset file in the API. ContentAsset.DeveloperName:

**•** must be 40 characters or fewer

**•** must begin with a letter

**•** can contain only underscores and alphanumeric characters

**•** can’t include spaces

**•** can’t end with an underscore

**•** can’t contain 2 consecutive underscores

In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

```
IsVisibleByExternalUsers

Language

MasterLabel

NamespacePrefix

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether unauthenticated users can see the asset file.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language for this document. This field defaults to the user's language unless the org is
multi-language enabled. Specifies the language of the labels returned. The value must be a
valid user locale (language and country), such as `de_DE` or `en_GB` . For more information
on locales, see the `Language` field on the CategoryNodeLocalization object.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label for the asset file. This internal label doesn’t get translated.

**Type**
string


### Standard Objects ContentBody

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix associated with this object. Each Developer Edition organization that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can
refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

### ContentBody

Represents the body of a file in Salesforce CRM Content or Salesforce Files. This object is available in API version 40.0 and later.

Supported Calls

```
   describeSObjects()

```

Special Access Rules

Cannot be queried, inserted, updated, or deleted directly.

Fields

**Field** **Details**

```
Id

```

Usage

**Type**
ID

**Properties**
, Filter, Group, idLookup, Sort

**Description**
ID of the file body.

### ContentBody is intended for internal Salesforce use. If you need to access the file content body, please use ContentVersion on page 1525. ContentDistribution

Represents information about sharing a document externally. This object is available in API version 32.0 and later.


Standard Objects ContentDistribution

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

**•** Content deliveries must be enabled to query content deliveries.

**•** Users (including users with the “View All Data” permission) can query only the files that they have access to. If the file is managed
by a Content Library, the user must have “Deliver Content” enabled in the library permission definition and be a member of the
library. If the file isn’t managed by a Content Library, the user must have the “Enable Creation of Content Deliveries for Salesforce
Files” permission.

**•** Users can query the `DistributionPublicUrl` and `Password` fields only if they are the file owner, if the file is shared with
them, or if the `RelatedRecordId` specifies a record that the users can access.

**•** If the shared document is deleted, the delete cascades to any associated ContentDistribution. The ContentDistribution is still queryable
by using the `QueryAll` verb.

**•** If the shared document is archived, the only fields that users can edit are `ExpiryDate` and `PreferencesExpires` .

**•** Customer Portal users can’t access this object.

**•** Guest users of Experience Cloud sites can't access or create this object.

**•** Chatter Free users can’t access this object.

Fields

**Field Name** **Details**

```
ContentDocumentId

ContentDownloadUrl

ContentVersionId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the shared document.

**Type**
string

**Properties**
Sort, Nillable

**Description**
The link for downloading the file. This field is available in API version 40.0 and
later.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


Standard Objects ContentDistribution

**Field Name** **Details**

**Description**
ID of the shared document version.

This is a relationship field.

**Relationship Name**
ContentVersion

**Relationship Type**
Lookup

**Refers To**
ContentVersion

```
DistributionPublicUrl

ExpiryDate

FirstViewDate

LastViewDate

Name

```

**Type**
string

**Properties**
Nillable, Sort

**Description**
URL of the link to the shared document.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date when the shared document becomes inaccessible.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date when the shared document is first viewed.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date when the shared document was last viewed.

**Type**
string


Standard Objects ContentDistribution

**Field Name** **Details**

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the content delivery.

```
OwnerId

PdfDownloadUrl

Password

PreferencesAllowOriginalDownload

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the user who owns the shared document.

This is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
string

**Properties**
Sort, Nillable

**Description**
The link for downloading the file as a PDF. This field is available in API version
40.0 and later.

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
A password that allows access to a shared document.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, the shared document can be downloaded as the file type that it
was uploaded as.


Standard Objects ContentDistribution

**Field Name** **Details**

When `false`, download availability depends on whether a preview of the file
exists. If a preview exists, the file can’t be downloaded. If a preview doesn’t exist,
the file can still be downloaded.

If the shared document is a link, it can’t be downloaded.

```
PreferencesAllowPDFDownload

PreferencesAllowViewInBrowser

PreferencesExpires

PreferencesLinkLatestVersion

PreferencesNotifyOnVisit

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, the shared document can be downloaded as a PDF if the original
file type is PDF or if a PDF preview has been generated.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, a preview of the shared document can be viewed in a Web browser.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, access to the shared document expires on the date that’s specified
by `ExpiryDate` .

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, users see the most recent version of a shared document. When
`false`, users see the version of the document that’s shared, even if it isn’t the
most recent version.

**Type**
boolean

**Properties**
Create, Filter, Update


Standard Objects ContentDistribution

**Field Name** **Details**

**Description**
When `true`, the owner of the shared document is emailed the first time that
someone views or downloads the shared document.

```
PreferencesNotifyRndtnComplete

PreferencesPasswordRequired

RelatedRecordId

ViewCount

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, the owner of the shared document is emailed when renditions of
the shared document that can be previewed in a Web browser are generated.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, a password, specified by `Password`, is required to access the
shared document.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the record, such as an Account, Campaign, or Case, that the shared document
is related to.

This is a polymorphic relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
Account, Campaign, Case, Contact, EmailMessage, Lead, ListEmail, Opportunity

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times that the shared document has been viewed.


Standard Objects ContentDistribution

Usage

Use this object to create, update, delete, or query information about a document shared externally via a link or via Salesforce CRM Content
delivery.

The ContentDistribution object supports triggers before and after these operations: insert, update, delete. It supports triggers after
undelete.

Example: The VP of Marketing wants file authors to specify whether their files can be shared with external people using content
delivery. He also wants some files to have a password. You can add a custom field `DeliveryPolicy` on the ContentVersion
object. Make the custom field a picklist with the values, `Allowed`, `Blocked`, and `Password required` . Add the field to
the ContentVersion layout so that the user can set the delivery policy per file. Then, add an insert trigger for the ContentDistribution
object to enforce the rules based on the delivery policy set in the file.

Note: The `ContentVersionId` for `ContentDistribution` must be unique.

This trigger for the ContentDistribution object enforces the delivery policy rules for each file:

```
      trigger deliveryPolicy on ContentDistribution (before insert) {

        for (ContentDistribution cd : trigger.new) {

           String versionId = DeliveryPolicyHelper.getContentVersionId(cd);

           ContentVersion version = [select DeliveryPolicy__c from ContentVersion where

      Id = :versionId];

           String policy = version.DeliveryPolicy__c;

           if (policy.equals('Blocked')) {

             cd.addError('This file is not allowed to be delivered.');

           } else if (policy.equals('Password required')){

             if (!DeliveryPolicyHelper.requirePassword(cd)) {

               cd.addError('To deliver this file, set a password.');

             }

           }

        }

      }

```

The trigger calls this helper class:

```
      public class DeliveryPolicyHelper {

        public static String getContentVersionId(ContentDistribution cd) {

           if (cd.ContentVersionId != null) {

             return cd.ContentVersionId;

           } else {

             String versionId = [select LatestPublishedVersionId from ContentDocument

      where Id = :cd.ContentDocumentId].get(0).LatestPublishedVersionId;

             return versionId;

           }

        }

        public static boolean requirePassword(ContentDistribution cd) {

           return cd.PreferencesPasswordRequired;

        }

      }

```

Important: Apex has a per organization limit of 10 concurrent requests that last longer than 5 seconds. A trigger that uploads
files can easily hit this limit.


### Standard Objects ContentDistributionEventLog ContentDistributionEventLog

Content Distribution events contain information about content distributions and deliveries to users. This object is available in API version
65.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
Action

DeliveryIdentifier

DeliveryLocation

RelatedObjectIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The action that’s used when a delivery is viewed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the content delivery.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The location of the delivery.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects ContentDistributionView

**Field** **Details**

**Description**
The 15-character ID of the record that’s associated with the delivery distribution.

```
RequestIdentifier

Timestamp

UserIdentifier

VersionIdentifier

```

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
The access time of Salesforce services in GMT. For example, `20130715233322.670` .

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
The 15-character ID of the content version.

### ContentDistributionView

Represents information about views of a shared document. This read-only object is available in API version 32.0 and later.

Supported Calls

`delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`


Standard Objects ContentDistributionView

Special Access Rules

**•** Content deliveries must be enabled to query content deliveries.

**•** Users (including users with the “View All Data” permission) can query only the files that they have access to. If the file is managed
by a Content Library, the user must have “Deliver Content” enabled in the library permission definition and be a member of the
library. If the file isn’t managed by a Content Library, the user must have the “Enable Creation of Content Deliveries for Salesforce
Files” permission.

**•** ContentDistributionView can be deleted by an admin.

**•** If the shared document is deleted, the delete cascades to any associated ContentDistributionView. The ContentDistributionView is
still queryable by using the `QueryAll` verb.

**•** Customer Portal users can’t access this object.

**•** Chatter Free users can’t access this object.

Fields

**Field Name** **Details**

```
DistributionId

IsDownload

IsInternal

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the content delivery that the document is part of.

This is a relationship field.

**Relationship Name**
Distribution

**Relationship Type**
Lookup

**Refers To**
ContentDistribution

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
`true` if the shared document is downloaded; `false` if the shared document
is viewed.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


### Standard Objects ContentDocument

**Field Name** **Details**

**Description**
`true` if the shared document is viewed by a user in the same organization;
`false` if viewed by an external user.

```
ParentViewId

```

Usage

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of this instance of accessing the shared document.

Use this read-only object to query information about users who are accessing shared documents.

### ContentDocument

Represents a document that was uploaded to a library in Salesforce Files or Salesforce CRM content. This object is available in versions
17.0 and later for Salesforce CRM.This object is available in API version 21.0 and later for Salesforce Files.

The maximum number of documents that can be published is 30,000,000. Archived files count toward this limit and toward storage
usage limits.

**•** Contact Manager, Group, Professional, Enterprise, Unlimited, and Performance Edition customers can publish a maximum of 200,000
new versions per 24-hour period.

**•** Developer Edition and trial users can publish a maximum of 2,500 new versions per 24-hour period.

Supported Calls

`delete()`, `describeLayout()describeSObjects()`, `query()`, `retrieve()`, `search()`, `undelete()`,

```
update()

```

Special Access Rules

**•** By default, users (including users with the View All Data permission) can only query files they have access to, including:

**–** Salesforce files in their personal library and in libraries they're a member of, regardless of library permissions (API version 17.0
and later).

**–** Salesforce files they own, shared directly with them, posted on their profile, or posted on groups they can see (API version 21.0
and later).

Turn on the Query All Files permission to let your View All Data users bypass the restrictions on querying files.

**–** Query All Files returns all files, including files in non-member libraries and files in unlisted groups.

**–** Users can’t edit, upload new versions, or delete files they don’t have access to.

**–** View All Data permission is required to enable Query All Files.


Standard Objects ContentDocument

**•** For API version 62.0 and later, enable the Query Non Vetoed Files permission in Data Cloud orgs to let your integration or API users
view and SOQL query only public and non-vetoed files in the org.

**•** Customer and partner portal users must have the View Content in Portal permission to query content in libraries where they have
access.

**•** A Salesforce CRM content document can be deleted if any of these statements is true.

**–** The document is published into a personal library or is in the user's upload queue.

**–** The document is published into a public library, the user trying to delete the document is the file owner, and is a member of
that library.

**–** The document is published into a public library and the user trying to delete the document isn’t the owner but has the Manage
Library or Delete Content library permission enabled.

For API version 25.0 and later, you can change ownership of Salesforce Files and Salesforce CRM content documents.

**•** A user can change ownership of a Salesforce CRM content document or Salesforce file if any of these statements is true.

**–** The user is the current owner.

**–** The user has the Modify All Data permission enabled.

**–** For a file in a Content Library, the user either has the Manage Salesforce CRM content permission enabled, or has the Manage
Library permission enabled for the library containing the document.

Note: When the owner of a ContentDocument is changed, ContentDocumentLink may be triggered. This action deletes the
ContentDocumentLink to the old owner and inserts one to the new owner. When you change document ownership, keep
these considerations in mind.

**–** The user who’s becoming the document owner must be a visible, active user. The original owner can be inactive.

**–** If the new document owner doesn’t have access to the library that contains the document, library administrators must
give the new owner membership to the library.

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
The ID of the user who archived the document.

This field is available in API version 24.0 and later.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date when the document was archived.


Standard Objects ContentDocument

**Field** **Details**

This field is available in API version 24.0 and later.

```
ContentAssetId

ContentModifiedDate

ContentSize

ContentSizeLong

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
If the ContentDocument is an asset file, this field points to the asset. For most entities, the
value of this field is `null` .

This field is available in API version 38.0 and later.

This is a relationship field.

**Relationship Name**
ContentAsset

**Relationship Type**
Lookup

**Refers To**
ContentAsset

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the document was modified.

`ContentModifiedDate` updates when, for example, the document is renamed or a
new document version is uploaded. When you’re uploading the first version of a document,
`ContentModifiedDate` can be set to the current time or anytime in the past.

This field is available in API version 32.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The size of the document in bytes for documents smaller than 2 GB.

This field is available in API version 31.0 and later. In API version 65.0 and later, we recommend
that you use the `ContentSizeLong` field even for files smaller than 2 GB.

**Type**
long


Standard Objects ContentDocument

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**

The size of the document in bytes up to 10 GB.

This field is available in API version 65.0 and later.

```
Description

Division

FileExtension

FileType

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort, Update

**Description**

A description of the document.

This field is available in API version 31.0 and later.

**Type**
picklist

**Properties**
Defaulted on Create, Filter, Group, Restricted picklist, Sort

**Description**
A logical segment of your organization's data. For example, if your company is organized
into different business units, you could create a division for each business unit, such as “North
America,” “Healthcare,” or “Consulting.” Available only if the organization has the Division
permission enabled.

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

Type of document, determined by the file extension.

This field is available in API version 31.0 and later.


Standard Objects ContentDocument

**Field** **Details**

```
IsArchived

IsInternalOnly

LastReferencedDate

LastViewedDate

LatestPublishedVersionId

```

**Type**
boolean

**Properties**
Defaulted on Create, Filter, Group, Sort, Update

**Description**
Indicates whether the document was archived ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Defaulted on Create, Filter, Group, Sort, Update

**Description**
Indicates that a file is for internal use only. When `true`, prevents users with the Query Non
Vetoed Files permission from viewing and performing SOQL query on public and non vetoed
files in a Data Cloud org. Default value is `false` .

This field is available in API version 62.0 and later.

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
record might only have been referenced ( `LastReferencedDate` ) and not viewed.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the latest document version (ContentVersion).

This is a relationship field.

**Relationship Name**
LatestPublishedVersion


Standard Objects ContentDocument

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
ContentVersion

`MalwareScanDate` (Beta)

`MalwareScanStatus` (Beta)

```
OwnerId

```

**Type**
dateTime

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date the document was scanned for malware. This field is available as a beta feature in
API version 66.0 and later.

Note: The `MalwareScanDate` field is a pilot or beta service that is subject to
[the Beta Services Terms at Agreements - Salesforce.com or a written Unified Pilot](https://www.salesforce.com/company/legal/agreements/)
[Agreement if executed by Customer, and applicable terms in the Product Terms](https://ptd.salesforce.com/)
[Directory. Use of this pilot or beta service is at the Customer's sole discretion.](https://ptd.salesforce.com/)

**Type**
picklist

**Properties**
Filter, Group, Sort

**Description**
Indicates whether the document was scanned for malware and whether it’s safe or malicious.
This field is available in API version 66.0 and later.

**•** `NotScanned` —The file hasn’t yet been scanned for malware. This is the default value.

**•** `Scheduled` —The file scan is in progress.

**•** `Clean` —The file was scanned and doesn’t contain malware.

**•** `Malicious` —The file was scanned and contains malware.

**•** `Skipped` —The file can’t be scanned because it’s either larger than 100 MB or it’s a
Salesforce-generated file, such as a Content Note.

**•** `Failed` —The file wasn’t scanned because of an error.

Note: The `MalwareScanStatus` field is a pilot or beta service that is subject
[to the Beta Services Terms at Agreements - Salesforce.com or a written Unified Pilot](https://www.salesforce.com/company/legal/agreements/)
[Agreement if executed by Customer, and applicable terms in the Product Terms](https://ptd.salesforce.com/)
[Directory. Use of this pilot or beta service is at the Customer's sole discretion.](https://ptd.salesforce.com/)

**Type**
reference

**Properties**
Filter, Group, Sort, Update


Standard Objects ContentDocument

**Field** **Details**

**Description**
ID of the owner of this document.

This is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

```
ParentId

PublishStatus

SharingOption

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
ID of the library that owns the document. Created automatically when inserting a
ContentVersion via the API for the first time.

This field is available in API version 24.0 and later when Salesforce CRM content is enabled.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**

Indicates if and how the document is published. Valid values are:

**•** `P` —The document is published to a public library and is visible to other users. Label is
**Public** .

**•** `R` —The document is published to a personal library and is not visible to other users.
Label is **Personal Library** .

**•** `U` —The document is not published because publishing was interrupted. Label is **Upload**
**Interrupted** .

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Controls whether sharing is frozen for a file. Only administrators and file owners with
Collaborator access to the file can modify this field. Default is `Allowed`, which means that
new shares are allowed. When set to `Restricted`, new shares are prevented without
affecting existing shares.


Standard Objects ContentDocument

**Field** **Details**

This field is available in API versions 35.0 and later.

```
SharingPrivacy

Title

```

Usage

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Controls sharing privacy for a file. Only administrators and file owners with Collaborator
access to the file can modify this field.

Valid values are:

**•** `N` —Default. Label is **Visible to Anyone With Record Access**

**•** `P` —The file is private on records but can be shared selectively with others. Label is
**Private on Records** .

This field is available in API versions 41.0 and later.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort, Update

**Description**

The title of a document.

**•** Use this object to retrieve, query, update, and delete the latest version of a document in a library or a Salesforce file. Use the
ContentVersion object to create, query, retrieve, search, edit, and update a specific version of a Salesforce CRM content document
or Salesforce file.

**•** A document record is a container for multiple version records. You create a version to add a document to the system. The new
version contains the actual file data which allows the document to have multiple versions. The version stores the body of the uploaded
document.

**•** To create a document, create version via the ContentVersion object without setting the `ContentDocumentId` . This process
automatically creates a parent document record. When adding a new version of the document, you must specify an existing
`ContentDocumentId` which initiates the revision process for the document. When the latest version is published, the title,
owner, and publish status fields are updated in the document.

**•** You can’t add new versions of archived documents.

**•** When you delete a document, all versions of that document are deleted, including ratings, comments, and tags.

**•** A ContentDocument insert trigger executes when a file (ContentDocument) is added to the file library.

**•** A ContentDocument delete trigger executes when a file is deleted, but the cascaded ContentDocumentLink delete does not trigger
ContentDocumentLink triggers.

**•** The `query()` call doesn’t return archived documents. The `queryAll()` call returns archived documents.


### Standard Objects ContentDocumentHistory

**•** To query a file that is accessible only through a record share, you must specify the content ID of the file. When SOQL querying the
ContentDocument object, the `ContentDocumentId` must be compounded by an AND operator.

For example,

```
     SELECT Id, Title FROM ContentDocument

     WHERE (Id = '<ContentDocumentId>' and Title LIKE '%<title>%'

     SELECT Id, Title, MyCustomField_c FROM ContentDocument

     WHERE (Id IN ('<Id1>', '<Id2>')) AND (Title LIKE '%<title1>%' OR (Title LIKE '%<title2>%')

```

**•** If you query versions in the API, versions with a `PublishStatus` of `Upload Interrupted` are not returned.

**•** Assign topics to ContentDocument using `TopicAssignment` in API version 37.0 or later.

Associated Objects

This object has the following associated objects. Unless noted, associated objects are available in the same API version as this object.

**ContentDocumentChangeEvent on page 68 (API version 55.0)**
Change events are available for the object.

**ContentDocumentFeed (API version 20.0)**
Feed tracking is available for the object.

### **ContentDocumentHistory**

History is available for tracked fields of the object.

SEE ALSO:

### ContentDocumentHistory

ContentVersion

### ContentDocumentHistory

Represents the history of a document. This object is available in versions 17.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Special Access Rules

**•** Customer and Partner Portal users must have the “View Content in Portal” permission to query content in libraries where they have
access.

**•** A user can query all versions of a document from their personal library and any version that is part of or shared with a library where
they are a member, regardless of library permissions.


Standard Objects ContentDocumentHistory

Fields

**Field** **Details**

```
ContentDocumentId

DataType

Division

Field

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the document.

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
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Data type of the field that was changed.

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
picklist

**Properties**
Filter, Group, Sort, Restricted picklist

**Description**
The name of the field that was changed. Possible values include:

**•** `contentDocPublished` —The document is published into a library.


### Standard Objects ContentDocumentLink

**Field** **Details**

**•** `contentDocUnpublished` —The document is archived or removed from a library,
either directly or when the owning library is changed.

**•** `contentDocRepublished` —The document is removed from the archive.

**•** `contentDocFeatured` —The document is featured.

**•** `contentDocSubscribed` —The document is subscribed to.

**•** `contentDocUnsubscribed` —The document is no longer subscribed to.

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
The new value of the field that was changed.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The latest value of the field before it was changed.

Use this read-only object to query the history of a document.

SEE ALSO:

### ContentDocument ContentDocumentLink

Represents the link between a Salesforce CRM Content document, Salesforce file, or ContentNote and where it's shared. A file can be
shared with other users, groups, records, and Salesforce CRM Content libraries. This object is available in versions 21.0 and later for
Salesforce CRM Content documents and Salesforce Files.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects ContentDocumentLink

Special Access Rules

**•** In API versions 59.0 and later, enable the Query All Files permission to query without a filter on `id`, `LinkedEntityId`, and
`documentID` fields. The View All Data permission is required to enable Query All Files.

**•** In API versions 33.0 and later, you can create and delete ContentDocumentLink objects with a `LinkedEntityId` of any record
type that can be tracked in the feed, even if feed tracking is disabled for that record type.

**•** In API versions 25.0 and later, you can create ContentDocumentLink objects with a `LinkEntityId` of type User, CollaborationGroup,
or Organization.

**•** In API versions 21.0 and later, users with explicit Viewer access (the file has been directly shared with the user) to a file can delete
ContentDocumentLink objects between the file and other users who have Viewer access. In the same API versions, any user with
Viewer access to a file can delete ContentDocumentLink objects between the file and organizations or groups of which they are a
member.

**•** For orgs with Digital Experiences enabled, a document can only be shared with users and groups that are a part of the Experience
Cloud site the file was created in.

Fields

**Field** **Details**

```
ContentDocumentId

LinkedEntityId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the document.

This is a relationship field.

**Relationship Name**
ContentDocument

**Relationship Type**
Lookup

**Refers To**
ContentDocument

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the linked object. Can include Chatter users, groups, records (any that support Chatter
feed tracking including custom objects), and Salesforce CRM Content libraries.

Using the API only, you can relate notes to custom settings.

This is a polymorphic relationship field.


Standard Objects ContentDocumentLink

**Field** **Details**

**Relationship Name**
LinkedEntity

**Relationship Type**
Lookup

**Refers To**
Account, Accreditation, ActivationTarget, ActivationTrgtIntOrgAccess, ApiAnomalyEventStore,
AssessmentIndicatorDefinition, AssessmentTask, AssessmentTaskContentDocument,
AssessmentTaskDefinition, AssessmentTaskIndDefinition, AssessmentTaskOrder, Asset,
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
CareRequestItem, CareSpecialty, CareSpecialtyTaxonomy, CareTaxonomy, Case, CodeSet,
CollaborationGroup, CommSubscription, CommSubscriptionChannelType,
CommSubscriptionConsent, CommSubscriptionTiming, ConsumptionSchedule, Contact,
ContactEncounter, ContactEncounterParticipant, ContentWorkspace, Contract,
ConversationEntry, CoverageBenefit, CoverageBenefitItem, CredentialStuffingEventStore,
CreditMemo, CreditMemoLine, Dashboard, DashboardComponent, DataStream,
DelegatedAccount, DocumentChecklistItem, EmailMessage, EmailTemplate,
EngagementChannelType, EnhancedLetterhead, EnrollmentEligibilityCriteria, Event,
HealthcareFacility, HealthcareFacilityNetwork, HealthcarePayerNetwork,
HealthcarePractitionerFacility, HealthcareProvider, HealthcareProviderNpi,
HealthcareProviderSpecialty, HealthcareProviderTaxonomy, Identifier, Image,
IndividualApplication, Invoice, InvoiceLine, Lead, ListEmail, Location, MarketSegment,
MarketSegmentActivation, MemberPlan, MessagingSession, MktCalculatedInsight,
OperatingHours, Opportunity, Order, OrderItem, Organization, OtherComponentTask,
OutgoingEmail, PartyConsent, PersonEducation, PersonLanguage, PersonLifeEvent,
PersonName, PlanBenefit, PlanBenefitItem, Product2, ProductFulfillmentLocation, ProductItem,
ProductItemTransaction, ProductRequest, ProductRequestLineItem, ProductRequired,
ProductTransfer, ProfileSkill, ProfileSkillEndorsement, ProfileSkillUser, ProviderSearchSyncLog,
PurchaserPlan, PurchaserPlanAssn, ReceivedDocument, Report, ReportAnomalyEventStore,
ResourceAbsence, ResourcePreference, ReturnOrder, ReturnOrderLineItem,
ServiceAppointment, ServiceResource, ServiceResourceSkill, ServiceTerritory,
ServiceTerritoryMember, ServiceTerritoryWorkType, SessionHijackingEventStore, Shift,
Shipment, ShipmentItem, Site, SkillRequirement, SocialPost, Solution, Task,
ThreatDetectionFeedback, Topic, User, Visit, VisitedParty, Visitor, VoiceCall, VolunteerProject,
WorkBadgeDefinition, WorkOrder, WorkOrderLineItem, WorkType, WorkTypeGroup,
WorkTypeGroupMember


Standard Objects ContentDocumentLink

**Field** **Details**

```
ShareType

Visibility

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Required. The permission granted to the user of the shared file in a library. This is determined
by the permission the user already has in the library. This field is available in API version 25.0
and later.

```
  V
```

Viewer permission. The user can explicitly view but not edit the shared file.

```
  C
```

Collaborator permission. The user can explicitly view and edit the shared file. You can
retrieve the ShareType for ContentDocumentLink, but you can't create a
ContentDocumentLink with a `ShareType` of `C` from an Apex trigger.

```
  I
```

Inferred permission. The user’s permission is determined by the related record. For shares
with a library, this is defined by the permissions the user has in that library. Inferred
permission on shares with libraries and file owners is available in API versions 21.0 and
later. Inferred permission on shares with standard objects is available in API versions 36.0
and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies whether this file is available to all users, internal users, or shared users. This field is
available in API version 26.0 and later.

`Visibility` can have the following values.

**•** `AllUsers` —The file is available to all users who have permission to see the file.

**•** `InternalUsers` —The file is available only to internal users who have permission
to see the file.

**•** `SharedUsers` —The file is available to all users who can see the feed to which the
file is posted. SharedUsers is used only for files shared with users, and is available only
when an org has private org-wide sharing on by default. The `SharedUsers` value is
available in API version 32.0 and later.

Note the following exceptions for `Visibility` .

**•** `AllUsers` & `InternalUsers` values apply to files posted on standard and custom
object records, but not to users, groups, or content libraries.

**•** For posts to a record feed, `Visibility` is set to `InternalUsers` for all internal
users by default.

**•** External users can set `Visibility` only to `AllUsers` .


Standard Objects ContentDocumentLink

**Field** **Details**

**•** On user and group posts, only internal users can set `Visibility` to
`InternalUsers` .

**•** For posts to a user feed, if the organization-wide default for user sharing is set to private,
`Visibility` is set to `SharedUsers` .

**•** Only internal users can update Visibility.

**•** Visibility can be updated on links to files posted on standard and custom object records,
but not to users, groups, or content libraries.

**•** Visibility is updatable in API version 43.0 and later.

The visibility setting on ContentDocumentLink determines a file’s visibility on a record post.
When a file has multiple references posted in a feed, the file’s visibility is determined by the most
visible setting.

Usage

Use this object to query the locations where a file is shared or query which files are linked to a particular location. For example, the
following query returns a particular document shared with a Chatter group:

```
   SELECT ContentDocument.title FROM ContentDocumentLink WHERE ContentDocumentId =

   '069D00000000so2' AND LinkedEntityId = '0D5000000089123'

```

**•** You can't run a query without filters against ContentDocumentLink.

**•** You can't filter on ContentDocument fields if you're filtering by `ContentDocumentId` . You can only filter on ContentDocument
fields if you're filtering by `LinkedEntityId` .

**•** You can't filter on the related object fields. For example, you can't filter on the properties of the account to which a file is linked. You
can filter on the properties of the file, such as the title field.

A SOQL query must filter on one of `Id`, `ContentDocumentId`, or `LinkedEntityId` .

The ContentDocumentLink object supports triggers before and after these operations: insert, update, delete. A ContentDocumentLink
trigger executes whenever there is an addition or deletion of the ContentDocumentLink. When a file is deleted, a ContentDocument
delete trigger executes, but the cascaded ContentDocumentLink delete does not trigger ContentDocumentLink triggers.

Example: This trigger for the ContentDocumentLink object prevents public XLSX files from being shared.

```
      trigger NoShareXLSX on ContentDocumentLink (after insert) {

        for (ContentDocumentLink cdl : trigger.new) {

           if (!CDLHelper.isSharingAllowed(cdl)) {

             cdl.addError('Sorry, you cannot share this file.');

           }

        }

      }

```

The trigger calls this helper class.

```
      public class CDLHelper {

        /**

         * Gets FileExtension of the inserted content.

         */

```


Standard Objects ContentDocumentLink

```
        public static String getFileExtension(ContentDocumentLink cdl) {

           String fileExtension;

           String docId = cdl.ContentDocumentId;

          FileExtension = [select FileExtension from ContentVersion where ContentDocumentId

      = :docId].get(0).FileExtension;

           return FileExtension;

        }

        /**

         * Checks the file's PublishStatus and FileExtension to decide whether user can

      share the file with others.

         * PublishStatus 'P' means the document is in a public library.

         */

        public static boolean isSharingAllowed(ContentDocumentLink cdl) {

           String docId = cdl.ContentDocumentId;

          ContentVersion version = [select PublishStatus,FileExtension from ContentVersion

      where ContentDocumentId = :docId].get(0);

           if (version.PublishStatus.equals('P') && (version.FileExtension != null &&

      version.FileExtension.equals('xlsx'))) {

             return false;

           }

           return true;

        }

        /**

         * Gets the parent account name if the file is linked to an account.

         */

        public static String getAccountName(ContentDocumentLink cdl) {

           String name;

           String id = cdl.LinkedEntityId;

           if (id.substring(0,3) == '001') {

             name = [select Name from Account where Id = :id].get(0).Name;

           }

           return name;

        }

      }

```

Important: Apex has a per organization limit of 10 concurrent requests that last longer than 5 seconds. A trigger that uploads
files, like bulk `ContentVersion` creation, can easily hit the SOQL queries limit.

Associated Objects

This object has the following associated objects. Unless noted, associated objects are available in the same API version as this object.

**ContentDocumentLinkChangeEvent on page 68 (API version 55.0)**
Change events are available for the object.

SEE ALSO:

ContentDocument


### Standard Objects ContentDocumentListViewMapping ContentDocumentListViewMapping

Represents an association between a ListView and a Quip ContentDocument. Applies to Quip file types only. Maintains the mapping
between a list view and Quip document when the list view is exported to a newly created Quip document. This object is available in API
version 44.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

To use this object, the Files Connect and Quip permissions must be enabled in the org.

To insert and update this object through the API, the QuipMassAction gater permission must also be enabled.

Fields

**Field** **Details**

```
ContentDocumentId

LastReferencedDate

LastViewedDate

ListViewId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the document.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this document.

**Type**
reference


### Standard Objects ContentDocumentSubscription

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the list view associated with the document.

```
Name

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the document.

ContentDocumentListViewMapping is used primarily by the Quip list view integration feature. Only Quip file types (Quip sheets and
docs) are supported. The ContentDocumentId field must point to a Quip file.

### ContentDocumentSubscription

Represents a subscription for a user following or commenting on a file in a library. This object is available in API version 42.0 and later.

Supported Calls

`delete()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Only users with Modify All Data permission have access to this object.

Fields

**Field** **Details**

```
ContentDocumentId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the file.

This is a relationship field.


### Standard Objects ContentDocLinkEventLog

**Field** **Details**

**Relationship Name**
ContentDocument

**Relationship Type**
Lookup

**Refers To**
ContentDocument

```
IsCommentSub

IsDocumentSub

UserId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether the user made comments on the file.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether the user follows the file.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user following or commenting on the file.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

### ContentDocLinkEventLog

Content Document Link events contain sharing information for content documents. This object is available in API version 65.0 and later.


Standard Objects ContentDocLinkEventLog

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
DocumentIdentifier

RequestIdentifier

SharedWithObjectIdentifier

SharingOperation

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the document that’s being shared.

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
Who the document was shared with.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of sharing operation on the document.

**Possible Values**

**•** `INSERT`

**•** `UPDATE`


### Standard Objects ContentFolder

**Field** **Details**

**•** `DELETE`

```
SharingPermission

Timestamp

UserIdentifier

### ContentFolder

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
What permissions the document was shared with.

**Possible Values**

**•** `V` : Viewer

### • C : Collaborator

**•** `I` : Inferred—that is, the sharing permissions were inferred from a relationship between
the viewer and document. For example, a document’s owner has a sharing permission
to the document itself. Or, a document can be a part of a content collection, and the
viewer has sharing permissions to the collection rather than explicit permissions to the
document directly.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.

For example: `00530000009M943`

Represents a folder in a content library for adding files. This object is available in API version 34.0 and later.


Standard Objects ContentFolder

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

**•** Salesforce CRM Content or Chatter must be enabled to access ContentFolder.

**•** All users with a content feature license can modify folders in their personal library.

**•** To modify a folder, the user must be a member of the library and have permission to modify folders.

Fields

**Field Name** **Details**

```
Name

ParentContentFolderId

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the folder.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the ParentFolder.

This is a relationship field.

**Relationship Name**
ParentContentFolder

**Relationship Type**
Lookup

**Refers To**
ContentFolder

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ContentFolderChangeEvent (API version 62.0)**
Change events are available for the object.


### Standard Objects ContentFolderItem ContentFolderItem

Represents a file (ContentDocument) or folder (ContentFolder) that resides in a ContentFolder in a ContentWorkspace. This object is
available in API version 35.0 and later.

Supported Calls

`describeSObjects()`, `describeLayout()`, `query()`, `retrieve()`

Special Access Rules

Fields

**Field Name** **Details**

```
ContentSize

ContentSizeLong

FileExtension

FileType

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The size of the file or folder in bytes, when the size is smaller than 2 GB.

In API version 66.0 and later, we recommend that you use the
`ContentSizeLong` field even for files smaller than 2 GB.

**Type**
long

**Properties**
Filter, Group, Nillable, Sort

**Description**

The size of the file or folder in bytes up to 10 GB.

This field is available in API version 66.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Specifies the file extension if the ContentFolderItem is a file.

**Type**
string


### Standard Objects ContentFolderLink

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**

Specifies the type of file if the ContentFolderItem is a file.

```
IsFolder

ParentContentFolderId

Title

### ContentFolderLink

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates that the ContentFolderItem is a folder, and not a file.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The ID of the ContentFolder that the ContentFolderItem resides in.

This is a relationship field.

**Relationship Name**
ParentContentFolder

**Relationship Type**
Lookup

**Refers To**
### ContentFolder

**Type**
string

**Properties**
Filter, Group, Sort

**Description**

The name of the file or folder.

Defines the association between a library and its root folder. This object is available in API version 34.0 and later.


Standard Objects ContentFolderLink

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

**•** Salesforce CRM Content must be enabled to access ContentFolderLink.

**•** ContentFolderLink is read-only in the context of a library.

Fields

**Field Name** **Details**

```
ContentFolderId

EnableFolderStatus

ParentEntityId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the folder.

This is a relationship field.

**Relationship Name**
ContentFolder

**Relationship Type**
Lookup

**Refers To**
ContentFolder

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the status of enabling folders for the library. Valid values are:

**•** `C`  - Completed folder enablement

**•** `S`  - Started folder enablement

**•** `F`  - Failed folder enablement

This field is available in API version 39.0 and later.

**Type**
reference

**Properties**
Filter, Group, Sort


### Standard Objects ContentFolderMember

**Field Name** **Details**

**Description**
Name of the entity the folder hierarchy is linked to.

### ContentFolderMember

Defines the association between a file and a folder. This object is available in API version 34.0 and later.

Supported Calls

`describeSObjects()`, `delete()`, `query()`, `retrieve()`, `update()`

Special Access Rules

**•** Salesforce CRM Content or Chatter must be enabled to access ContentFolderMember.

**•** All users with a content feature license can modify folders in their personal library.

**•** To modify ContentFolderMember, the user must be a member of the library and have permission to modify folders.

Fields

**Field Name** **Details**

```
ChildRecordId

ParentContentFolderId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the file.

This is a relationship field.

**Relationship Name**
ChildRecord

**Relationship Type**
Lookup

**Refers To**
ContentDocument

**Type**
reference

**Properties**
Filter, Group, Sort, Update


### Standard Objects ContentHubItem

**Field Name** **Details**

**Description**
ID of the folder the file is in.

This is a relationship field.

**Relationship Name**
ParentContentFolder

**Relationship Type**
Lookup

**Refers To**
ContentFolder

### ContentHubItem

Represents a file or folder in a Files Connect external data source, such as Microsoft SharePoint or OneDrive for Business. This object is
available in API version 33.0 and later.

Special Access Rules

Chatter and Files Connect must be enabled for the organization.

Supported Calls

`describeSObjects()`, `query()`, `search()`

Fields

**Field Name** **Details**

```
ContentHubRepositoryId

ContentItemSize

```

**Type**
reference

**Properties**
Filter, Group, Nillable

**Description**
The ID for the related external data source described by the ContentHubRepository
object.

**Type**
long

**Properties**
Group, Nillable


Standard Objects ContentHubItem

**Field Name** **Details**

**Description**
The size of the file or folder. Available in API version 65.0 and later.

```
ContentModifiedDate

ContentSize

Description

ExternalContentUrl

ExternalDocumentUrl

ExternalId

```

**Type**
dateTime

**Properties**
Nillable

**Description**
Date the file or folder content last changed.

**Type**
int

**Properties**
Group, Nillable

**Description**
The size of the file or folder that's less than 2 GB.

**Type**
string

**Properties**
Filter, Group, Nillable

**Description**
Explanation of item in external data source.

**Type**
url

**Properties**
Group, Nillable

**Description**
The URL of the document content in the external data source.

**Type**
url

**Properties**
Group, Nillable

**Description**
The URL of the detail page in the external data source.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ContentHubItem

**Field Name** **Details**

**Description**
ID for the file or folder in the external data source.

```
FileExtension

FileType

IsFolder

MimeType

Name

Owner

```

**Type**
string

**Properties**
Group, Nillable

**Description**
File format extension, such as .doc or .pdf

**Type**
string

**Properties**
Group, Nillable

**Description**
Complete file type, such as “Microsoft Word Document.”

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether item is a folder or file.

**Type**
string

**Properties**
Filter, Group, Nillable

**Description**
MIME type of the content.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Name of the file or folder in the external data source.

**Type**
string

**Properties**
Filter, Group, Nillable


Standard Objects ContentHubItem

**Field Name** **Details**

**Description**
Username of the content owner in the external data source.

```
ParentId

Title

UpdatedBy

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable

**Description**
The ID of the parent folder for the record.

This field isn’t returned in queries or searches of the ContentHubItem object. It
supports only WHERE clauses, such as the following:

```
  WHERE ContentHubRepositoryId = <ID of external

  source> and ParentId = <ID of parent folder or
```

`record>` .

Or specify `WHERE ParentId = <name of root folder>` to return
the children of the root folder.

Tip: The ParentId field supports both Salesforce IDs (in the format
“0CHxxx”) and external IDs.

**Type**
string

**Properties**
Group, Nillable

**Description**
The title that appears in the content, which often differs from the `Name` of the
containing file or folder.

**Type**
string

**Properties**
Group, Nillable

**Description**
Username for the person who last updated the file.

The following SOQL query examples show how to retrieve files and folders from a Files Connect external data source. These examples
use placeholders for ID values for the repository ID and folder IDs. Before running these queries, replace the placeholders with valid ID
values for your external data source and folders.


### Standard Objects ContentHubRepository Important: You must filter queries and searches on ContentHubItem with the ContentHubRepositoryId field; for

example, `SELECT Id FROM ContentHubItem WHERE ContentHubRepositoryId = <ID of external`
`data source>` .

**Example 1:** Get the ID and name of the root folder in an external file source.

```
   SELECT Id, Name

   FROM ContentHubItem

   WHERE ContentHubRepositoryId = ' <repository ID> ' AND ParentId = NULL

```

**Example 2:** List all folders and files under the specified root folder.

```
   SELECT Id, Name

   FROM ContentHubItem

   WHERE ContentHubRepositoryId = ' <repository ID> ' AND ParentId = ' <root folder ID> '

```

**Example 3:** List all external file data sources by querying ContentHubRepository.

```
   SELECT DeveloperName

   FROM ContentHubRepository

```

**Example 4:** List all files and folders in a given folder and external file source.

```
   SELECT Id, Name

   FROM ContentHubItem

   WHERE ContentHubRepositoryId = ' <repository ID> ' AND ParentId = ' <parent folder ID> '

```

**Example 5:** To return only folders in the result set, add `IsFolder = true` in the `WHERE` clause to a query that returns files and
folders. For example, the following query lists all folders under the root folder.

```
   SELECT Id, Name

   FROM ContentHubItem

   WHERE ContentHubRepositoryId = ' <repository ID> ' AND ParentId = ' <root folder ID> '

       AND IsFolder = true

```

**Example 6:** Retrieve a link that is used to open the specified document in an external source.

```
   SELECT ExternalDocumentUrl

   FROM ContentHubItem

   WHERE ContentHubRepositoryId = ' <repository ID> ' AND Id = ' <document ID> '

```

**SOSL Example:** Retrieve the ID and name of all documents that contain the search string. The result set is limited to the first 10 documents.

```
   FIND {<search string>}

   RETURNING ContentHubItem(Id, Name

                  WHERE ContentHubRepositoryId = ' <repository ID> ')

   LIMIT 10

### ContentHubRepository

```

Represents a Files Connect external data source such as Microsoft SharePoint or OneDrive for Business. This object is available in API
version 33.0 and later.


Standard Objects ContentHubRepository

Special Access Rules

Chatter and Files Connect must be enabled for the organization.

Supported Calls

`describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
DeveloperName

MasterLabel

Type

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique name of the record in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with
a letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. This field is automatically generated but you can supply
your own value if you create the record using the API.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is specified,
performance may slow while Salesforce generates one for each record.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Master label for the external data source. This display value is the internal label
and does not get translated.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The data source type. Possible values are:

**•** `contenthubGoogleDrive`

**•** `contenthubOffice365`

**•** `contenthubOneDrive`

**•** `contenthubSharepoint`


### Standard Objects ContentNote

**Field Name** **Details**

**•** `contenthubBox`

**•** `contenthubQuip`

### ContentNote

Represents a note created with the enhanced note-taking tool, released in Winter ’16. This object is available in API version 32.0 and
later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `search()`, `update()`

Special Access Rules

**•** Notes must be enabled.

Fields

**Field** **Details**

### `Content`

```
ContentModifiedDate

```

**Type**
base64

**Properties**
Create, Nillable, Update

**Description**
The content or body of the note, which can include properly formatted HTML or plain text.
When a document is uploaded or downloaded via the API, it must be base64 encoded (for
### upload) or decoded (for download). Any special characters within plain text in the Content

field must be escaped. You can escape special characters by calling
`content.escapeHtml4()` . If the input contains unsafe HTML characters or new lines,
we automatically strip them out before saving the content.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the document was modified. ContentModifiedDate updates when, for example,
the document is renamed or a new document version is uploaded.

This field is available in API version 48.0 and later.


Standard Objects ContentNote

**Field** **Details**

```
ContentSize

ContentSizeLong

FileExtension

FileType

IsReadOnly

LastViewedDate

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The size of the note in bytes for notes smaller than 2 GB. In API version 66.0 and later, use
the `ContentSizeLong` field.

**Type**
long

**Properties**
Filter, Group, Nillable, Sort

**Description**

The size of the note in bytes, up to 10 GB.

This field is available in API version 66.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
File extension of the note.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Type of file for the note. All notes have a file type of `SNOTE` .

**Type**
boolean

**Properties**
Defaulted on create, Group, Sort

**Description**
Indicates whether the note is read only.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects ContentNote

**Field** **Details**

**Description**
The date the note was last viewed. This field is available in API version 35.0 and later.

```
LatestContentId

LatestPublishedVersionId

OwnerId

SharingPrivacy

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Lookup to the note's ContentBody. This field is available in API version 52.0 and later.

This is a relationship field.

**Relationship Name**
LatestContent

**Relationship Type**
Lookup

**Refers To**
ContentBody

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the ContentVersion for the latest published version of the note.

**Type**
reference

**Properties**
Create (for users assigned the Set Audit Fields Upon Creation permission), Defaulted on
create, Filter, Group, Sort, Update (for users assigned the Set Audit Fields Upon Creation
permission)

**Description**
ID of the owner of the note.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Controls sharing privacy for a file. Only Salesforce admins and file owners with Collaborator
access to the file can modify this field. Default is `Visible to Anyone With Record`
`Access` . When set to `Private on Records`, the file is private on records but can
be shared selectively with others.


Standard Objects ContentNote

**Field** **Details**

This field is available in API versions 41.0 and later.

```
TextPreview

Title

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A preview of the note’s content. This field is available in API version 35.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Namefield, Sort, Update

**Description**
Title of the note.

**•** Use ContentNote to create, query, retrieve, search, edit, and update notes.

**•** ContentNote is built on ContentVersion, and so it has many of the same usages.

**•** Not all fields can be set for notes. Only the `Content` and `Title` fields can be updated.

**•** The maximum file size that you can upload via the SOAP API is 50 MB. When a document is uploaded or downloaded via the API,
it’s converted to base64. This conversion increases the document size by approximately 37%. Account for the base64 conversion
increase so that the file you plan to upload is less than 50 MB after conversion.

**•** You can convert old Note records to Lightning Experience, so users can view and edit notes from the Notes & Attachments related
list in Lightning Experience. Users can edit their converted notes, which are accessible from the Notes related list and Notes tab.
Copy old Note records to newly created ContentNote records. Users assigned the Set Audit Fields Upon Creation permission can set
the owner, created date, and last modified date on ContentNote records.

**•** SOQL and SOSL queries on the ContentNote return only the most recent version of the note.

**•** To relate a note to a record, use `ContentDocumentLink` . Review the `LinkedEntityID` field in `ContentDocumentLink`
for a list of objects that notes can relate to.

For example, the following Apex code creates a note and escapes any special characters so they’re converted to their HTML equivalents.

Note: Apex code doesn’t need to be encoded to base64 before it’s uploaded and downloaded.

```
ContentNote cn = new ContentNote();

cn.Title = 'test1';

String body = 'Hello World. Before insert/update, escape special characters such as ", ',

 &, and other standard escape characters.';

cn.Content = Blob.valueOf(body.escapeHTML4());

insert(cn);

```


### Standard Objects ContentNotification

In this example, the following code creates a note using text that is already formatted as HTML, so it doesn’t need to be escaped.

```
   ContentNote cn = new ContentNote();

   cn.Title = 'test2';

   String body = '<b>Hello World. Because this text is already formatted as HTML, it does not

    need to be escaped.

   Special characters such as &quot;, etc. must already use their HTML equivalents.</b>';

   cn.Content = body;

   insert(cn);

### ContentNotification

```

Represents a notification for a file. This object is available in API version 42.0 and later.

Supported Calls

`delete()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Only users with Modify All Data permission have access to this object.

Fields

**Field** **Details**

```
EntityIdentifierId

EntityType

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the object with the notification.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Type of object with the notification. One of the following.

**•** `ContentDocument`

**•** `ContentTagName`

**•** `ContentVersion`

**•** `ContentWorkspace`

**•** `ContentWorkspacePermission`


### Standard Objects ContentTagSubscription

**Field** **Details**

**•** `User`

```
Nature

Subject

Text

UsersId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Type of notification.

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
Subject of the notification.

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
Text of the notification.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who received the notification.

This is a relationship field.

**Relationship Name**
Users

**Relationship Type**
Lookup

**Refers To**
User

### ContentTagSubscription

Represents a subscription for a user following a tag on a file. This object is available in API version 42.0 and later.


### Standard Objects ContentTaxonomy

Supported Calls

`delete()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Only users with Modify All Data permission have access to this object.

Fields

**Field** **Details**

```
UserId

### ContentTaxonomy

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the user following the tag on the file.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

Represents a content taxonomy, which is used to classify and organize Salesforce CMS content. To create a hierarchy of terms in a content
taxonomy, use this object in addition to the ContentTaxonomyTerm, ContentTaxonomyRelatedTerm, and
### ContentTaxonomyTermRelatedTerm objects. This object is available in API version 63.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

To view this object, users need the permission View Content Taxonomy enabled. To edit this object, users need View Content Taxonomy
and Manage Content Taxonomy enabled.


### Standard Objects ContentTaxonomyRelatedTerm

Fields

**Field** **Details**

```
Description

Language

Name

```

SEE ALSO:

### ContentTaxonomyRelatedTerm

ContentTaxonomyTerm

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the content taxonomy. This description appears in the API and in the Content
Taxonomy tab in the Digital Experiences App. The maximum length is 255 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The combined language and locale ISO code.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the content taxonomy.

ContentTaxonomyTermRelatedTerm

ContentTaxonomyTermRelationshipType

### ContentTaxonomyRelatedTerm

Represents the relationship between a term and the content taxonomy to which the term belongs. This object is available in API version
63.0 and later.

Supported Calls

`create()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`


Standard Objects ContentTaxonomyRelatedTerm

Special Access Rules

To view this object, users need the permission View Content Taxonomy enabled. To edit this object, users need View Content Taxonomy
and Manage Content Taxonomy enabled.

Fields

**Field** **Details**

```
ContentTaxonomyId

ContentTaxonomyTermId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the content taxonomy to which the term belongs.

This field is a relationship field.

**Relationship Name**
ContentTaxonomy

**Relationship Type**
Lookup

**Refers To**
ContentTaxonomy object

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the term that belongs to the content taxonomy.

This field is a relationship field.

**Relationship Name**
ContentTaxonomyTerm

**Relationship Type**
Lookup

**Refers To**
ContentTaxonomyTerm object


### Standard Objects ContentTaxonomyTerm

Usage

To include a term in a taxonomy, you must use this object in addition to the ContentTaxonomyTerm and ContentTaxonomy objects.

SEE ALSO:

### ContentTaxonomy ContentTaxonomyTerm ContentTaxonomyTerm

Represents a term in a content taxonomy. Terms describe what content is or how it's used, and they’re organized in parent-child
relationships in the taxonomy hierarchy. This object is available in API version 63.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

To view this object, users need the permission View Content Taxonomy enabled. To edit this object, users need View Content Taxonomy
and Manage Content Taxonomy enabled.

Fields

**Field** **Details**

```
Description

DeveloperName

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the content taxonomy term. This description appears in the API and in the
Content Taxonomy tab in the Digital Experiences App. The maximum length is 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The unique name of the content taxonomy term in the API. This field is unique within your
organization. The name:

**•** must be 80 characters or fewer

**•** must begin with a letter


### Standard Objects ContentTaxonomyTermRelatedTerm

**Field** **Details**

**•** can contain only underscores and alphanumeric characters

**•** can't include spaces

**•** can't end with an underscore

**•** can't contain 2 consecutive underscores

```
ExternalId

Name

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The external ID of the content taxonomy term.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the content taxonomy term. The name must be between 2 and 255 characters
long.

To include a term in a taxonomy, you must also use the objects ContentTaxonomyRelatedTerm and ContentTaxonomy. If you create
only a ContentTaxonomyTerm, then the term isn’t considered part of the taxonomy, and isn't visible. To relate this term to another term
in your taxonomy, use the object ContentTaxonomyTermRelatedTerm.

SEE ALSO:

### ContentTaxonomy

ContentTaxonomyRelatedTerm

### ContentTaxonomyTermRelatedTerm ContentTaxonomyTermRelatedTerm

Represents the relationship between two terms in a content taxonomy. This object is available in API version 63.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,

```
undelete()

```


Standard Objects ContentTaxonomyTermRelatedTerm

Special Access Rules

To view this object, users need the permission View Content Taxonomy enabled. To edit this object, users need View Content Taxonomy
and Manage Content Taxonomy enabled.

Fields

**Field** **Details**

```
ContentTaxonomyId

ContentTaxonomyTermId

ContentTaxonomyTrmRelaTypeId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the content taxonomy to which the term belongs.

This field is a relationship field.

**Relationship Name**
ContentTaxonomy

**Relationship Type**
Lookup

**Refers To**
ContentTaxonomy object

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the primary term that has a relationship with another term.

This field is a relationship field.

**Relationship Name**
ContentTaxonomyTerm

**Relationship Type**
Lookup

**Refers To**
ContentTaxonomyTerm object

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the type of relationship between the two taxonomy terms.


### Standard Objects ContentTaxonomyTermRelationshipType

**Field** **Details**

This field is a relationship field.

**Relationship Name**
ContentTaxonomyTrmRelaType

**Relationship Type**
Lookup

**Refers To**
### ContentTaxonomyTermRelationshipType object

```
RelatedContentTaxonomyTermId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the term that is related to the primary term.

This field is a relationship field.

**Relationship Name**
RelatedContentTaxonomyTerm

**Relationship Type**
Lookup

**Refers To**
ContentTaxonomyTerm object

To relate a term to another term in a content taxonomy, use this object in addition to the ContentTaxonomyTerm object. This object
can’t be updated. You can only create and delete it.

SEE ALSO:

### ContentTaxonomyTerm ContentTaxonomyTermRelationshipType

Represents the type of relationship between two terms in a content taxonomy. This object is available in API version 63.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

To view this object, users need the permission View Content Taxonomy enabled.


### Standard Objects ContentTransferEventLog

Fields

**Field** **Details**

```
ContentTaxonomyTrmRelaCatg

Description

Name

```

Usage

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Category of the relationship type.

Possible values are:

**•** `HasBroader`

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
Description of the relationship type.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Name of the relationship type.

ContentTaxonomyRelationshipType can’t be created, updated, or deleted. In API version 63.0, the default category for the relationship
type is HasBroader.

### ContentTransferEventLog ContentTransferEventLog stores information about content transfer events, such as downloads, uploads, and previews. This information

includes events performed on files and attachments to records. This object is available in API version 62.0 and later.

Supported Calls

`describeSObjects()`, `query()`


Standard Objects ContentTransferEventLog

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
DocumentIdentifier

FilePreviewType

FileSize

FileType

OperationType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the document that’s being shared.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The content type of the file preview.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The size of rendition being added (bytes).

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The content type of the file version.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The operation that’s being performed.


Standard Objects ContentTransferEventLog

**Field** **Details**

**Possible Values**

**•** `meta_deploy`

**•** `meta_list`

**•** `meta_retrieve`

**•** `meta_synchronous_create`

**•** `meta_synchronous_read`

**•** `meta_synchronous_upsert`

```
RequestIdentifier

Timestamp

UserIdentifier

VersionIdentifier

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
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 18-character ID of the user who’s using Salesforce services through the UI or the API.

For example: `00530000009M943YAS`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the content version.


### Standard Objects ContentUserSubscription ContentUserSubscription

Represents a subscription for a user following another user. This object is available in API version 42.0 and later.

Supported Calls

`delete()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Only users with Modify All Data permission have access to this object.

Fields

**Field** **Details**

```
SubscribedToUserId

SubscriberUserId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who is followed by another user.

This is a relationship field.

**Relationship Name**
SubscribedToUser

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who follows another user.

This is a relationship field.

**Relationship Name**
SubscriberUser

**Relationship Type**
Lookup


### Standard Objects ContentVersion

**Field** **Details**

**Refers To**
User

### ContentVersion

Represents a specific version of a document in Salesforce CRM content or Salesforce Files. This object is available in versions 17.0 and
later for Salesforce CRM content documents. This object is available in versions 20.0 and later for Salesforce Files.

The maximum number of versions that can be published in a 24-hour period is 200,000.

Note: Depending on how files are shared, queries on ContentDocument and ContentVersion without specifying an ID don’t
return all files a user has access to. For example, if a user only has access to a file because they have access to a record that the file
is shared with, the file won't be returned in a query such as "SELECT Id FROM ContentDocument."

Supported Calls

`create()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `search()`, `update()`, `upsert()`

Special Access Rules

**•** All users with a content feature license can create versions in their personal library. Customer and Partner Portal users must also
supply the `NetworkId` of the Experience Cloud site in the request.

**•** By default, users (including users with the “View All Data” permission) can only query files they have access to, including:

**–** Salesforce Files in their personal library and in libraries they're a member of, regardless of library permissions (API version 17.0
and later).

**–** Salesforce Files they own, shared directly with them, posted on their profile, or posted on groups they can see (API version 21.0
and later).

Enable the Query All Files permission to let your View All Data users bypass the restrictions on querying files.

**–** Query All Files returns all files, including files in non-member libraries and files in unlisted groups.

**–** Users can’t edit, upload new versions, or delete files they don’t have access to.

**–** View All Data permission is required to enable Query All Files.

**•** All users can update versions in their personal library.

**•** The owner of a version or document can update the document if they’re a member of the library, regardless of library permissions.

**•** To update a Salesforce CRM Content document, the user must be a member of the library with one of these library privileges enabled:

**–** Add Content

**–** Add Content On Behalf of Others

**–** Manage Library

**•** Customer and Partner Portal users must have the View Content in Portal permission to query content in libraries where they have
access.

**•** Customer and Partner Portal users can only publish, version, or edit documents if they have a Salesforce CRM Content feature license.

**•** `FileType` is defined by either `ContentUrl` for links or `PathOnClient` for documents, but not both.


Standard Objects ContentVersion

**•** In API version 34.0 and later, any file can be shared with libraries, whether the file originated in Chatter or in Salesforce CRM Content.

**•** [In API version 39.0 and later, custom Apex download handlers can be created that can control access to documents. See the Apex](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dev_guide.htm)
[Developer Guide for more information.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dev_guide.htm)

Fields

**Field** **Details**

```
Checksum

ContentBodyId

ContentDocumentId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
MD5 checksum for the file.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Allows inserting a file version independently of the file blob being uploaded. This field is
available for query and insert only. It can only point to a ContentBody record. This field is
available in API version 40.0 and later.

This is a relationship field.

**Relationship Name**
ContentBody

**Relationship Type**
Lookup

**Refers To**
ContentBody

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the document.

This is a relationship field.

**Relationship Name**
ContentDocument

**Relationship Type**
Lookup


Standard Objects ContentVersion

**Field** **Details**

**Refers To**
ContentDocument

```
ContentLocation

ContentModifiedById

ContentModifiedDate

ContentSize

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Origin of the document. Valid values are:

**•** **S** —Document is located within Salesforce. Label is **Salesforce** .

**•** **E** —Document is located outside of Salesforce. Label is **External** .

**•** **L** —Document is located on a social network and accessed via Social Customer Service.
Label is **Social Customer Service** .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the user who modified the document.

This is a relationship field.

**Relationship Name**
ContentModifiedBy

**Relationship Type**
Lookup

**Refers To**
User

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**

Date the document was modified.

`ContentModifiedDate` updates when, for example, the document is renamed or a
new document version is uploaded. When uploading the first version of a document,
`ContentModifiedDate` can be set to the current time or any time in the past.

**Type**
int


Standard Objects ContentVersion

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The size of the document in bytes for documents smaller than 2 GB. The value is zero for links.

In API version 66.0 and later, we recommend that you use the `ContentSizeLong` field
even for documents smaller than 2 GB.

```
ContentSizeLong

ContentUrl

Description

Division

```

**Type**
long

**Properties**
Filter, Group, Nillable, Sort

**Description**

The size of the document in bytes up to 10 GB. The value is zero for links.

This field is available in API version 66.0 and later.

**Type**
url

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
URL for links. This is only set for links. One of the fields that determines the `FileType` . The
character limit in API versions 33.0 and later is 1,300. The character limit in API versions 32.0
and earlier was 255.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Description of the content version.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A logical segment of your organization's data. For example, if your company is organized
into different business units, you could create a division for each business unit, such as “North
America,” “Healthcare,” or “Consulting.” Available only if the org has the Division permission
enabled.


Standard Objects ContentVersion

**Field** **Details**

```
ExternalDataSourceId

ExternalDocumentInfo1

ExternalDocumentInfo2

FeaturedContentBoost

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the external document referenced in the `ExternalDataSource` object.

This is a relationship field.

**Relationship Name**
ExternalDataSource

**Relationship Type**
Lookup

**Refers To**
ExternalDataSource

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Stores the URL of the file in the external content repository. The integration from the external
source determines the content for this string. After the reference or copy is created, the URL
of the external file is updated when you:

**•** Republish a file reference in Lightning Experience

**•** Open the document

**•** Create a file reference in the Connect REST API with `reuseReference` set to true.

When the file is updated, the shared link is updated to the most current version.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Contains the external file ID. Salesforce determines the content for this string, which is private.
The content can change without notice, depending on the external system. After the file
reference is created, this field isn’t updated, even if the file path changes.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ContentVersion

**Field** **Details**

**Description**
Read only. Designates a document as featured.

```
FeaturedContentDate

FileExtension

FileType

FirstPublishLocationId

```

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Date the document was featured.

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
Filter, Group, Sort

**Description**
Type of content determined by `ContentUrl` for links or `PathOnClient` for documents.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

ID of the location where the version was first published. If the version is first published into
a user's personal library or My Files, the field will contain the ID of the user who owns the
personal library or My Files. In Lightning Experience, if the first version is published into a
public library, the field will contain the ID of that library.

Accepts all record IDs supported by ContentDocumentLink (anything a file can be attached
to, like records and groups).

Setting `FirstPublishLocationId` allows you to create a file and share it with an
initial record/group in a single transaction, and have the option to create more links to share
the file with other records or groups later. When a file is created, it’s automatically linked to
the record, and PublishStatus will change to Public from Pending/Personal.


Standard Objects ContentVersion

**Field** **Details**

This field is only set the first time a version is published via the API.
`FirstPublishLocationId` can’t be set to another ID when a new content version
is inserted.

Note: Salesforce updates the `FirstPublishLocationId` updates automatically
when a new `OwnerId` is added to the `ContentVersion` . For example, when
you publish a new version with a different `OwnerId` than the current `OwnerId`,
the `FirstPublishLocationId` of all previous versions updates to the previous
`OwnerId` . The new published version sets the `FirstPublishLocationId`
to the new `OwnerId` .

This is a polymorphic relationship field.

**Relationship Name**
FirstPublishLocation

**Relationship Type**
Lookup

**Refers To**
Account, Accreditation, ActivationTarget, ActivationTrgtIntOrgAccess, ApiAnomalyEventStore,
AssessmentIndicatorDefinition, AssessmentTask, AssessmentTaskContentDocument,
AssessmentTaskDefinition, AssessmentTaskIndDefinition, AssessmentTaskOrder, Asset,
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
CareRequestItem, CareSpecialty, CareSpecialtyTaxonomy, CareTaxonomy, Case, CodeSet,
CollaborationGroup, CommSubscription, CommSubscriptionChannelType,
CommSubscriptionConsent, CommSubscriptionTiming, ConsumptionSchedule, Contact,
ContactEncounter, ContactEncounterParticipant, ContentWorkspace, Contract,
ConversationEntry, CoverageBenefit, CoverageBenefitItem, CredentialStuffingEventStore,
CreditMemo, CreditMemoLine, Dashboard, DashboardComponent, DataStream,
DelegatedAccount, DocumentChecklistItem, EmailMessage, EmailTemplate,
EngagementChannelType, EnhancedLetterhead, EnrollmentEligibilityCriteria, Event,
HealthcareFacility, HealthcareFacilityNetwork, HealthcarePayerNetwork,
HealthcarePractitionerFacility, HealthcareProvider, HealthcareProviderNpi,
HealthcareProviderSpecialty, HealthcareProviderTaxonomy, Identifier, Image,
IndividualApplication, Invoice, InvoiceLine, Lead, ListEmail, Location, MarketSegment,
MarketSegmentActivation, MemberPlan, MessagingSession, MktCalculatedInsight,
OperatingHours, Opportunity, Order, OrderItem, Organization, OtherComponentTask,
OutgoingEmail, PartyConsent, PersonEducation, PersonLanguage, PersonLifeEvent,
PersonName, PlanBenefit, PlanBenefitItem, Product2, ProductFulfillmentLocation, ProductItem,
ProductItemTransaction, ProductRequest, ProductRequestLineItem, ProductRequired,


Standard Objects ContentVersion

**Field** **Details**

ProductTransfer, ProfileSkill, ProfileSkillEndorsement, ProfileSkillUser, ProviderSearchSyncLog,
PurchaserPlan, PurchaserPlanAssn, ReceivedDocument, Report, ReportAnomalyEventStore,
ResourceAbsence, ResourcePreference, ReturnOrder, ReturnOrderLineItem,
ServiceAppointment, ServiceResource, ServiceResourceSkill, ServiceTerritory,
ServiceTerritoryMember, ServiceTerritoryWorkType, SessionHijackingEventStore, Shift,
Shipment, ShipmentItem, Site, SkillRequirement, SocialPost, Solution, Task,
ThreatDetectionFeedback, Topic, User, Visit, VisitedParty, Visitor, VoiceCall, VolunteerProject,
WorkBadgeDefinition, WorkOrder, WorkOrderLineItem, WorkType, WorkTypeGroup,
WorkTypeGroupMember

```
IsAssetEnabled

IsLatest

IsMajorVersion

Language

```

**Type**
boolean

**Properties**
Create, Group, Defaulted on create

**Description**
Can be specified on insert of ContentVersion to automatically convert a ContentDocument
file into a ContentAsset. This field can be SOQL queried, but it can’t be edited. This field is
available in API version 38.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this is the latest version of the document ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
`true` if the document is a major version; `false` if the document is a minor version. Major
versions can’t be replaced.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language for this document. This field defaults to the org’s default language unless the
multi language setting is enabled.


Standard Objects ContentVersion

**Field** **Details**

Specifies the language of the labels returned. The value must be a valid user locale (language
and country), such as `de_DE` or `en_GB` . For more information on locales, see the
`Language` field on the CategoryNodeLocalization object.

`MalwareScanDate` (Beta)

`MalwareScanStatus` (Beta)

```
NegativeRatingCount

```

**Type**
dateTime

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date the document was scanned for malware. This field is available as a beta feature in
API version 66.0 and later.

Note: The `MalwareScanDate` field is a pilot or beta service that is subject to the
[Beta Services Terms at Agreements - Salesforce.com or a written Unified Pilot](https://www.salesforce.com/company/legal/agreements/)
[Agreement if executed by Customer, and applicable terms in the Product Terms](https://ptd.salesforce.com/)
[Directory. Use of this pilot or beta service is at the Customer's sole discretion.](https://ptd.salesforce.com/)

**Type**
picklist

**Properties**
Filter, Group, Sort

**Description**
Indicates whether the document was scanned for malware and whether it’s safe or malicious.
This field is available in API version 66.0 and later.

Valid values are:

**•** `NotScanned` —The file hasn’t yet been scanned for malware. This is the default value.

**•** `Scheduled` —The file scan is in progress.

**•** `Clean` —The file was scanned and doesn’t contain malware.

**•** `Malicious` —The file was scanned and it contains malware.

**•** `Skipped` —The file can’t be scanned because it’s either larger than 100 MB or it’s a
Salesforce-generated file, such as a Content Note.

**•** `Failed` —The file wasn’t scanned because of an error.

Note: The `MalwareScanStatus` field is a pilot or beta service that is subject to
[the Beta Services Terms at Agreements - Salesforce.com or a written Unified Pilot](https://www.salesforce.com/company/legal/agreements/)
[Agreement if executed by Customer, and applicable terms in the Product Terms](https://ptd.salesforce.com/)
[Directory. Use of this pilot or beta service is at the Customer's sole discretion.](https://ptd.salesforce.com/)

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ContentVersion

**Field** **Details**

**Description**
Read only. The number of times different users have given the document a thumbs down.

Rating counts for the latest version are not version-specific. If Version 1 receives 10
thumbs-down votes, and Version 2 receives 2 thumbs-down votes, the
`NegativeRatingCount` on Version 2 is 12. However, rating counts are not retroactive
for prior versions. The `NegativeRatingCount` on Version 1 is 10.

```
NetworkId

Origin

OwnerId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the Experience Cloud site that this file originated from. This field is available in API version
26.0 and later, if digital experiences is enabled for your org.

You can add a `NetworkId` only when creating a file. You can’t change or add a
`NetworkId` for an existing file.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The source of the content version. Valid values are:

**•** **C** —Content document from the user's personal library. Label is **Content** . The
`FirstPublishLocationId` must be the user's ID. If
`FirstPublishLocationId` is left blank, it defaults to the user's ID.

**•** **H** —Salesforce file from the user's My Files. Label is **Chatter** . The
`FirstPublishLocationId` must be the user's ID. If
`FirstPublishLocationId` is left blank, it defaults to the user's ID. Origin can
only be set to **H** if Chatter is enabled for your organization.

This field defaults to C. Label is **Content Origin** .

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of this document.

This is a relationship field.

**Relationship Name**
Owner


Standard Objects ContentVersion

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
User

```
PathOnClient

PositiveRatingCount

PublishStatus

RatingCount

```

**Type**
string

**Properties**
Create, Filter, Nillable, Sort

**Description**
The complete path of the document. One of the fields that determines the `FileType` .

Note: Specify a complete path including the file extension in order for the document
to be visible in the Preview tab.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Read only. The number of times different users have given the document a thumbs up.

Rating counts for the latest version are not version-specific. If Version 1 receives 10 thumbs-up
votes, and Version 2 receives 2 thumbs-up votes, the `PositiveRatingCount` on Version
2 is 12. However, rating counts are not retroactive for prior versions. The
`PositiveRatingCount` on Version 1 is 10.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Indicates if and how the document is published. Valid values are:

**•** `P` —The document is published to a public library and is visible to other users. Label is
**Public** .

**•** `R` —The document is published to a personal library and is not visible to other users.
Label is **Personal Library** .

**•** `U` —The document is not published because publishing was interrupted. Label is **Upload**
**Interrupted** .

**Type**
int


Standard Objects ContentVersion

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Read only. Total number of positive and negative ratings.

```
ReasonForChange

RecordTypeId

SharingOption

SharingPrivacy

```

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The reason why the document was changed. This field can only be set when inserting a new
version (revising) a document.

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
ID of the record type of the version.

Custom fields are restricted in `RecordTypeId` . When an administrator creates a custom
field via the API it must be added to at least one page layout:

**•** If the custom field is added to the page layout associated with the General record type,
the `RecordTypeId` that corresponds to that record type does not have to be set on
the version record.

**•** If the custom field is added to the page layout associated with a custom record type, the
`RecordTypeId` that corresponds to that record type must be set on the version
record.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Controls whether sharing is frozen for a file. Only administrators and file owners with
Collaborator access to the file can modify this field. Default is `Allowed`, which means that
new shares are allowed. When set to `Restricted`, new shares are prevented without
affecting existing shares.

This field is available in API versions 35.0 and later.

**Type**
picklist


Standard Objects ContentVersion

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Controls sharing privacy for a file. Only administrators and file owners with Collaborator access
to the file can modify this field. Default is `Visible to Anyone With Record`
`Access` . When set to `Private on Records`, the file is private on records but can be
shared selectively with others.

This field is available in API versions 41.0 and later.

```
TagCsv

TextPreview

Title

VersionData

```

**Type**
textarea

**Properties**
Create, Nillable, Sort, Update

**Description**
Text used to apply tags to a content version via the API.

**Type**
string

**Properties**
Nillable, Filter,Group, Sort

**Description**
A preview of a document. Available in API version 35.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**

The title of a document.

**Type**
base64

**Properties**
Create, Nillable, Update

**Description**
The content or body of the note, which can include properly formatted HTML or plain text.
When a document is uploaded or downloaded via the API, it should be base64 encoded (for
upload) or decoded (for download). Any special characters within plain text in the `Content`
field must be escaped. You can escape special characters by calling
`content.escapeHtml4()` .

This field can't be set for links.


Standard Objects ContentVersion

**Field** **Details**

The maximum file size you can upload via the SOAP API is 50 MB. When a document is
uploaded or downloaded via the API, it is converted to base64 and stored in `VersionData` .
This conversion increases the document size by approximately 37%. Account for the base64
conversion increase so that the file you plan to upload is less than 50 MB after conversion.

If a custom Apex download handler is active, this field is accessed from the API, and the
download is not allowed, Salesforce will return a
`CONTENT_CUSTOMIZED_DOWNLOAD_EXCEPTION` error.

```
VersionDataURL

VersionNumber

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URL used to fetch a file from the binary data endpoint. This field is only populated on
direct queries to ContentVersion, and not when queried through a related entity’s foreign
key to ContentVersion.

If available, access preview images of a file by appending a `thumb` query parameter to this
URL. For example:

```
  myContentVersion.VersionDataUrl + '?thumb=THUMB240BY180'

```

Available `thumb` parameter values are:

**•** `THUMB720BY480`  - corresponds to the `big-thumbnail` preview format

**•** `THUMB240BY180`  - corresponds to the `thumbnail` preview format

**•** `THUMB120BY90`  - corresponds to the `tiny-thumbnail` preview format

[See File Preview in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/connect_resources_files_preview_format.htm) _Connect REST API Developer Guide_ for additional details about file
previews.

This field can't be set for links.

This field is available in API versions 55.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version number. The number increments with each version of the document, for example,
1, 2, 3.


Standard Objects ContentVersion

Usage

**•** Use this object to create, query, retrieve, search, edit, and update a specific version of a Salesforce CRM Content document or Salesforce
file. Use the ContentDocument object to retrieve, query, update, and delete the latest version of a document, but not a content pack,
in a library or a Salesforce file.

**•** Use this object to create, query, retrieve, search, edit, and update a specific version of a Salesforce file. Use the ContentDocument
object to retrieve, query, update, and delete the latest version of a Salesforce file.

**•** To query a file that is shared only with a record, you must specify the content ID of the file.

**•** Not all fields can be set for Salesforce Files.

**•** You can only update a version if it is the latest version and if it is published.

**•** You can't archive versions.

**•** Using API version 32.0 and later, you can update record types on versions.

**•** You can't delete a version via the API.

**•** The maximum file size you can upload via the SOAP API is 50 MB. When a document is uploaded or downloaded via the API, it is
converted to base64 and stored in `VersionData` . This conversion increases the document size by approximately 37%. Account
for the base64 conversion increase so that the file you plan to upload is less than 50 MB after conversion.

**•** To download a document via the API, you must export the `VersionData` of the document. This does not increase the download
count.

**•** When you upload a document from your local drive using the Data Loader, you must specify the actual path in both `VersionData`
and `PathOnClient` . `VersionData` identifies the location and extracts the format and `PathOnClient` identifies the type
of document being uploaded.

**•** SOQL queries on the ContentVersion object return all versions of the document. SOSL searches on the ContentVersion object return
only the most recent version of the document.

**•** To query a file that is accessible only through a record share, you must specify the content ID of the file. When SOQL querying the
ContentVersion object, either the `ContentVersionId` or the `ContentDocumentId` must be compounded by an AND
operator.

For example,

```
     SELECT FileExtension, Title FROM ContentVersion

     WHERE (ContentDocumentId = '<ContentDocumentId>' or Id='<ContentVersionId>') and

     IsLatest=true

     SELECT Id, VersionData, FileExtension, Title FROM ContentVersion

     WHERE ContentDocumentId='<ContentDocumentId>' AND FirstPublishLocationId =

     '<FirstPublishLocationId>'

```

**•** If you query versions in the API, versions with a `PublishStatus` of `Upload Interrupted` are not returned.

**•** Documents published into a personal library assume the default record type that is set for the user profile of the person publishing
the document (General, if no default is set for the user profile).

Note: An administrator can rename the default ( _Content Version Layout_ ) page layout.

**•** Contact Manager, Group, Professional, Enterprise, Unlimited, and Performance Edition customers can publish a maximum of 200,000
new versions per 24–hour period. Developer Edition and trial users can publish a maximum of 2,500 new versions per 24–hour
period.

**•** Custom validation rules can prevent an update of documents published into a personal library via the API.


Standard Objects ContentVersion

Applying Tags to ContentVersion Records

Tags can be applied to ContentVersion records using either Enterprise or Partner API.

To apply tags to a ContentVersion record, set a value in the `TagCsv` field. For example, setting this field to `one,two,three` creates
and associates three tags to that version.

**•** The maximum length of the `TagCsv` field is 2,000 characters.

**•** The maximum length of an individual tag is 100 characters.

**•** When tags are applied to a version, the content is indexed automatically and the tags are searchable.

**•** You can't apply tags to a `TagCsv` that is published into a personal library. You can apply tags to a `TagCsv` that's in a shared
library or folder.

**•** You can't apply tags using the ContentDocument object.

**•** You can't change or delete tag names. You can remove tags from a document, but that doesn't delete the tag.

**•** Tags are case insensitive. You can't have two tags with the same name even if they use different uppercase and lowercase letters.
The case of the original tag is always used.

To delete tags from a ContentVersion record, perform a standard API update, and remove any values from the `TagCsv` field that you
want to delete. For example, if the original `TagCsv` is `one,two,three`, perform an API update specifying `one,three` in the
`TagCsv` field to delete `two` . To delete all tags from a ContentVersion you perform a standard API update by setting the field to `null` .

If you create a ContentVersion record and want to revise it via the API, you insert another ContentVersion record but associate it to the
same ContentDocument record as the original. This has an impact on tagging:

**•** If you insert the revision and do not set any value in the `TagCsv` field, any tags applied to the previous version are automatically
applied to the new version.

**•** If you insert the revision and specify a new `TagCsv` field, no tags transfer over and the tags you specify are applied instead.

When you perform a SOQL query for a ContentVersion record and select the `TagCsv` field, all the tags associated with that record are
returned. The tags in the string are always ordered alphabetically even if they were inserted in a different order. You can't use the
`TagCsv` field as part of a filter in a SOQL query. You can't query all tags in your organization.

Library tagging rules:

**•** API tagging respects the tagging restrictions that exist on any library that the document is published into. For example, if the library
is in restricted tagging mode and only allows tags `one,three`, you can't save a version with a `TagCsv` of `one,two,three` .

**•** If the library is in guided tagging mode, you can apply tags to the ContentVersion. You can't query the value of guided tags on a
library, but you can query the tagging model of a library.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ContentVersionChangeEvent on page 68 (API version 55.0)**
Change events are available for the object.

**ContentVersionHistory**

History is available for tracked fields of the object.

SEE ALSO:

ContentDocument

ContentVersionHistory


### Standard Objects ContentVersionComment ContentVersionComment

Represents a comment on a version of a file. This object is available in API version 42.0 and later.

Supported Calls

`delete()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Only users with Modify All Data permission have access to this object.

Fields

**Field** **Details**

```
ContentDocumentId

ContentVersionId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the file.

This is a relationship field.

**Relationship Name**
ContentDocument

**Relationship Type**
Lookup

**Refers To**
ContentDocument

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the version of the file.

This is a relationship field.

**Relationship Name**
### ContentVersion

**Relationship Type**
Lookup


### Standard Objects ContentVersionHistory

**Field** **Details**

**Refers To**
### ContentVersion

```
UserComment

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
ID of the user who commented on the file.

### ContentVersionHistory

Represents the history of a specific version of a document. This object is available in version 17.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Special Access Rules

**•** Customer and Partner Portal users must have the “View Content in Portal” permission to query content in libraries where they have
access.

**•** A user can query all versions of a document from their personal library and any version that is part of or shared with a library where
they are a member, regardless of library permissions.

Note: To record an event in `contentVersionViewed`, make sure:

**•** All files are published to a Content Library.

**•** The details page is viewed in Salesforce Classic.

Fields

**Field** **Details**

```
ContentVersionId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the version.


Standard Objects ContentVersionHistory

**Field** **Details**

This is a relationship field.

**Relationship Name**
ContentVersion

**Relationship Type**
Lookup

**Refers To**
ContentVersion

```
DataType

Division

Field

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
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
A logical segment of your organization's data. For example, if your company is organized
into different business units, you could create a division for each business unit, such as “North
America,” “Healthcare,” or “Consulting.” Available only if the organization has the Division
permission enabled.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The name of the field that was changed. Possible values include:

**•** `contentVersionCreated` —A new version is created.

**•** `contentVersionUpdated` —The title, description, or any custom field on the
version is changed.

**•** `contentVersionDownloaded` —A version is downloaded.

**•** `contentVersionViewed` —The version details are viewed.

**•** `contentVersionRated` —The version is rated.

**•** `contentVersionCommented` —The version receives a comment.

**•** `contentVersionDataReplaced` —The new version replaces the previous version,
which can happen only when the new version is uploaded immediately after the previous
version.


### Standard Objects ContentVersionRating

**Field** **Details**

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
The new value of the field that was changed.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The latest value of the field before it was changed.

Use this read-only object to query the history of a document version.

SEE ALSO:

### ContentVersion ContentVersionRating

Represents a rating on a version of a file. This object is available in API version 42.0 and later.

Supported Calls

`delete()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Only users with Modify All Data permission have access to this object.

Fields

**Field** **Details**

```
ContentVersionId

```

**Type**
reference


Standard Objects ContentVersionRating

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
ID of the version of the file.

This is a relationship field.

**Relationship Name**
ContentVersion

**Relationship Type**
Lookup

**Refers To**
ContentVersion

```
Rating

UserComment

UserId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Rating of the file.

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
Comment made by the user who rated the file.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who rated the file.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User


### Standard Objects ContentWorkspace ContentWorkspace

Represents a content library. This object is available in versions 17.0 and later.

Note: This object doesn’t apply to personal libraries.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Note: create( ), update( ) and delete( ) on ContentWorkspace are supported in API version 40.0 and later only.

Special Access Rules

**•** The Access Libraries user permission allows orgs to make libraries available to users without requiring that they have the legacy
Salesforce CRM Content license. This permission is available for profiles and permission sets on most standard user licenses, and isn’t
available for High Volume Customer Portal, Customer Community, or Chatter Free licenses. Available in API versions 40.0 and later.

**•** Users with the Create Libraries user perm or the Manage Salesforce CRM Content administrator permission can create libraries
(ContentWorkspaces) from the Libraries tab in Salesforce Classic and from the API.

**•** Customer and Partner Portal users can only edit the library document object if they have a Salesforce CRM Content feature license.

**•** Customer and Partner Portal users can query this object if they have the “View Content in Portal” permission. A user can query all
public libraries where they’re members, regardless of library permissions.

**•** Automated process users can’t publish documents to libraries (ContentWorkspaces).

Fields

**Field** **Details**

```
DefaultRecordTypeId

Description

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the default content type for the library. Content types are the containers
for custom fields in Salesforce CRM Content.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Text description of the content library.


Standard Objects ContentWorkspace

**Field** **Details**

```
DeveloperName

IsRestrictContentTypes

IsRestrictLinkedContentTypes

Name

NamespacePrefix

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique name of the library in the API. Allows a link to the library to be
packaged when an asset file is added to a package. Although libraries aren’t a
packageable entity, references to libraries with a developer name will be
included in the package when asset files are packaged. These links can then
be restored in the target org.

This name can contain only underscores and alphanumeric characters, and
must be unique in your org. It must begin with a letter, not include spaces, not
end with an underscore, and not contain two consecutive underscores. Label
is Unique Name.

This field is available in API version 39.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read only. Indicates whether content types have been restricted ( `true` ) or
not ( `false` ).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read only. Indicates whether linked content types have been restricted ( `true` )
or not ( `false` ).

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the library.

**Type**
string


Standard Objects ContentWorkspace

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique name of the library in the API. Allows a link to the library to be
packaged when an asset file is added to a package. Limit: 15 characters. This
field is available in API version 39.0 and later.

```
RootContentFolderId

ShouldAddCreatorMembership

TagModel

WorkspaceImageId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of root folder of the library. This field is available in API version 39.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Group

**Description**
Automatically create a library membership for the user creating the library. Note
this field isn’t meant for query and always returns false in query. This field is
available in API version 40.0 and later.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of tagging assigned to a library. Valid values are:

**•** `U`  - Unrestricted. No restrictions on tagging. Users can enter any tag when
publishing or editing content.

**•** `G`  - Guided. Users can enter any tag when publishing or editing content,
but they’re also offered a list of suggested tags.

**•** `R`  - Restricted. Users must choose from a list of suggested tags.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects ContentWorkspace

**Field** **Details**

**Description**
ID of a library image. Image files can be assigned to libraries for branding and
easy identification. Library image is visible to all users, even if they aren’t library
members. This field is available in API version 43.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of a library image. Image files can be assigned to libraries for branding and
easy identification. Library image is visible to all users, even if they are not library
members. This field is available in API version 43.0 and later.

This is a relationship field.

**Relationship Name**
WorkspaceImage

**Relationship Type**
Lookup

**Refers To**
ContentAsset

```
WorkspaceType

```

Usage

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Differentiates between different types of libraries. Valid values are:

**•** `R`  - Regular library

**•** `B`  - Org asset library

This field is available in API version 39.0 and later.

Use this object to query libraries to find out where documents can be published.

If the content type isn’t specified when publishing a new version into a library, it is determined by the `DefaultRecordTypeId` of
the primary library.

As of 40.0, you can create, update, or delete a library via the API.

SEE ALSO:

ContentWorkspaceDoc


### Standard Objects ContentWorkspaceDoc ContentWorkspaceDoc

Represents a link between a document and a public library in Salesforce CRM Content. This object is available in versions 17.0 and later.

Note: This object does not apply to documents and versions in a personal library.

Supported Calls

`create()`, `delete()`, `describeSObjects()query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

**•** Customer and Partner Portal users must have the “View Content in Portal” permission in order to query and obtain content in libraries
where they have access.

**•** Customer and Partner Portal users can only edit documents if they have a Salesforce CRM Content feature license.

**•** To create a ContentWorkspaceDoc, you must be a member of the library with one of these library privileges enabled:

**–** “Add Content”

**–** “Add Content On Behalf of Others”

**–** “Manage Library”

**•** To query all library documents in a library, a user must be a member of that library, regardless of library permissions.

Fields

**Field** **Details**

```
ContentDocumentId

ContentWorkspaceId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Read only. ID of the library document.

This is a relationship field.

**Relationship Name**
ContentDocument

**Relationship Type**
Lookup

**Refers To**
ContentDocument

**Type**
reference


Standard Objects ContentWorkspaceDoc

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
Read only. ID of the library.

This is a relationship field.

**Relationship Name**
ContentWorkspace

**Relationship Type**
Lookup

**Refers To**
ContentWorkspace

```
IsOwner

```

Usage

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read only. Indicates whether the library owns the document and determines
permissions for that document ( `true` ) or not ( `false` ). Documents can belong to
more than one library, but only one library owns the document and determines its
permissions.

**•** Use this object to link a document to one or more libraries.

**•** To share a document with additional libraries, create additional ContentWorkspaceDoc records which join the document to the
additional libraries.

**•** Inserting a ContentWorkspaceDoc triggers the publish process for public libraries.

**•** A document can be published into many public libraries, but it will always be owned by one library which controls the security of
the document.

**•** A document can only be published into the document owner's personal library. You can't publish into another user's personal library.
Personal libraries are not visible via the API.

**•** To publish a document into a personal library, you must specify your user ID as the first publish location ID. If you leave the first
publish location ID blank, it defaults to the current user's ID.

**•** A document can be published from a personal library into a public library, but once it has been published into the public library, it
can't be published into the personal library again.

**•** You can't publish a document from a personal library into a public library that has restricted content types.

**•** You can't update or delete a library document via the API.

SEE ALSO:

ContentWorkspace


### Standard Objects ContentWorkspaceMember ContentWorkspaceMember

Represents a member of a content library. This object is available in API version 40.0 and later.

Manage library membership from the API.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

A user can create/update/delete memberships if they have the Manage Salesforce CRM Content admin perm or the Manage Library
permission for the library concerned.

Fields

**Field** **Details**

```
ContentWorkspaceId

ContentWorkspacePermissionId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the library.

This is a relationship field.

**Relationship Name**
### ContentWorkspace

**Relationship Type**
Lookup

**Refers To**
### ContentWorkspace

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The id of the library permission or role.

This is a relationship field.

**Relationship Name**
ContentWorkspacePermission


### Standard Objects ContentWorkspacePermission

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
### ContentWorkspacePermission

```
MemberId

MemberType

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group,Namepointing, Sort

**Description**
ID of the library member (the member is either a user or a group).

This is a polymorphic relationship field.

**Relationship Name**
Member

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
picklist

**Properties**
Filter, Group, Nillable,Restricted picklist, Sort

**Description**
The type of library member. Valid values are:

**•** G - Group

**•** U - User

Use this object to create, update, or delete members from a library.

### ContentWorkspacePermission

Represents a library permission. This object is available in API version 40.0 and later.

A library permission is a group of privileges assigned to each content library member. It determines which tasks a member can perform
in a particular library. The same user can have a different library permission in each of his or her libraries.

Note: Library permissions do not apply to personal libraries. All library users can save files in their personal libraries.


Standard Objects ContentWorkspacePermission

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

The ability to create permissions requires either the Manage Salesforce CRM Content admin perm or the Manage Content Permissions
user perm.

Fields

**Field** **Details**

```
Description

Name

PermissionsAddComment

PermissionsAddContent

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Namefield, Sort, Update

**Description**
Name of the library.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Permission for user to post comments to any content in the library and view all comments
in the library. Users can edit or delete their own comments.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Permission for user to publish new content to the library, upload new content versions, or
restore archived (deleted) content. Content authors can also change any tags associated
with their content and archive or delete their own content.


Standard Objects ContentWorkspacePermission

**Field** **Details**

```
PermissionsAddContentOBO

PermissionsArchiveContent

PermissionsChatterSharing

PermissionsDeleteContent

PermissionsDeliverContent

PermissionsFeatureContent

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Permission for user to choose an author when publishing content in the library.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Permission for user to archive and restore any content in the library.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Permission for user to make content from this library accessible outside of the library, sharing
with a record or in Chatter. From a record or from Chatter, select a file from the library and
attach it to a record or a post.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Permission for user to delete any content in the library. Authors can undelete their own
content from the Recycle Bin.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Permission for user to share content outside the org via a content delivery or public link.

**Type**
boolean

**Properties**
Create, Filter, Update


Standard Objects ContentWorkspacePermission

**Field** **Details**

**Description**
Permission for user to identify any content in the library as “featured.”

```
PermissionsManageWorkspace

PermissionsModifyComments

PermissionsOrganizeFileAndFolder

PermissionsTagContent

PermissionsViewComments

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Permission for user to perform any action in the library. This privilege is required to edit a
library’s name and description, add or remove library members, or delete a library. Manage
Library is a super permission which provides all other permission options listed except Deliver
Content. Creating a library requires the Manage Salesforce CRM Content app permission or
Create Libraries system permission.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Permission for user to edit or delete comments made to any content in the library.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Permission for user to create, rename, and delete folders in libraries.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Permission for user to add tags when publishing content or editing content details in the
library.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Permission for user to view comments.


### Standard Objects ContentWorkspaceSubscription

**Field** **Details**

```
Type

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Provides the type of access a user has to a library. Valid values are:

**•** Library Administrator

**•** Author

**•** Viewer

**•** Custom

### ContentWorkspaceSubscription

Represents a subscription for a user following a library. This object is available in API version 42.0 and later.

Supported Calls

`delete()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Only users with Modify All Data permission have access to this object.

Fields

**Field** **Details**

```
ContentWorkspaceId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the library.

This is a relationship field.

**Relationship Name**
### ContentWorkspace

**Relationship Type**
Lookup


### Standard Objects ContextParamMap

**Field** **Details**

**Refers To**
ContentWorkspace

```
UserId

### ContextParamMap

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user following the library.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

Represents optional context data for a Conversation or a ConversationParticipant. This object is available in API version 57.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ContextEntityId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Conversation or ConversationParticipant record.

This field is a polymorphic relationship field.

**Relationship Type**
Lookup

**Refers To**
Conversation, ConversationParticipant


### Standard Objects Contract

**Field** **Details**

```
MapKey

MapValue

### Contract

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The key for the context data.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The value for the context data.

Represents a contract (a business agreement) associated with an Account.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AccountId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort,Update

**Description**
Required. ID of the Account associated with this contract.

This field is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account


Standard Objects Contract

**Field** **Details**

```
ActivatedById

ActivatedDate

ActivityMetricId

ActivityMetricRollupId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort,Update

**Description**
ID of the User who activated this contract.

This field is a relationship field.

**Relationship Name**
ActivatedBy

**Relationship Type**
Lookup

**Refers To**
User

**Type**
dateTime

**Properties**
Filter, Nillable, Sort, Update

**Description**
Date and time when this contract was activated.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
When Einstein Activity Capture with Activity Metrics is enabled, the ID of the related activity
metric.

This field is a relationship field.

**Relationship Name**
ActivityMetric

**Refers To**
ActivityMetric

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects Contract

**Field** **Details**

**Description**
When Einstein Activity Capture with Activity Metrics is enabled, the ID of the related activity
metric rollup.

This field is a relationship field.

**Relationship Name**
ActivityMetricRollup

**Refers To**
ActivityMetricRollup

```
AggregationStrategy

BillingAddress

BillingCity

BillingCountry

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The aggregation strategy when creating a pricing contract.

Valid value is `Cumulative` . This field is available with Revenue Cloud in API version 64.0
and later.

**Type**
address

**Properties**
Filter, Nillable

**Description**
The compound form of the billing address. Read-only. See Address Compound Fields for
details on compound address fields.

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
Details for the billing address of this account. The maximum size is 80 characters.


Standard Objects Contract

**Field** **Details**

```
BillingCountryCode

BillingGeocodeAccuracy

BillingLatitude

BillingLongitude

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO country code for the contract's billing address.

**Type**
picklist

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

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `BillingLongitude` to specify the precise geolocation of a billing address.
Acceptable values are numbers between –90 and 90 with up to 15 decimal places.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects Contract

**Field** **Details**

**Description**
Used with `BillingLatitude` to specify the precise geolocation of a billing address.
Acceptable values are numbers between –180 and 180 with up to 15 decimal places.

```
BillingPostalCode

BillingState

BillingStateCode

BillingStreet

CompanySignedDate

CompanySignedId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the billing address of this account. The maximum size is 20 characters.

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
The ISO state code for the contract's billing address.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Street address for the billing address.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date your organization signed the contract.

**Type**
reference


Standard Objects Contract

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the user who signed the contract.

This field is a relationship field.

**Relationship Name**
CompanySigned

**Relationship Type**
Lookup

**Refers To**
User

```
ContractNumber

ContractTerm

CustomerSignedDate

CustomerSignedId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Number of the contract.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of months that the contract is valid.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the customer signed the contract.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Contact who signed this contract.

This field is a relationship field.


Standard Objects Contract

**Field** **Details**

**Relationship Name**
CustomerSigned

**Relationship Type**
Lookup

**Refers To**
Contact

```
CustomerSignedTitle

Description

EndDate

HasContractCotermination

IsPricingContract

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Title of the customer who signed the contract.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the contract.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort,

**Description**
Read-only. Calculated end date of the contract. This value is calculated by adding the
`ContractTerm` to the `StartDate` . If the **Auto-calculate Contract End Date** setting
is disabled, the contract end date is editable.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the contract can be coterminated ( `true` ) or not ( `false` ).

The default value is `false` . This field is available with Revenue Cloud in API version 65.0
and later.

**Type**
boolean


Standard Objects Contract

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the contract has related contract item prices ( `true` ) or if there are no
contract item prices for the contract ( `false` ). This field is available with Revenue Cloud in
API version 63.0 and later.

```
IsDeleted

LastActivityDate

LastApprovedDate

LastReferencedDate

LastViewedDate

```

**Type**
boolean

**Properties**
Defaulted on create or filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
The label is **Deleted** .

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Value is the most recent:

**•** The due date of the most recent event is logged against the record.

**•** The due date of the most recently closed task associated with the record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Last date the contract was approved.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
datetime


Standard Objects Contract

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it’s possible that the user only accessed this record or list view ( `LastReferencedDate` )
but didn’t view it.

```
OwnerExpirationNotice

OwnerId

Pricebook2Id

PricingSource

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Number of days ahead of the contract end date (15, 30, 45, 60, 90, and 120). Used to notify
the owner in advance that the contract is ending.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the user who owns the contract.

This field is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the pricebook, if any, associated with this contract.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects Contract

**Field** **Details**

**Description**
Source of the pricing for the contract.

Valid values are:

**•** `LastTransaction`

**•** `PriceBookListPrice` —Price Book or List Price

Available in API version 60.0 and later.

```
RecordTypeId

RenewalTerm2

RenewalTermUnit

ShippingAddress

```

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
ID of the record type assigned to this object.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The default subscription term for renewals. For example, if the Renewal Term Unit is months
and you want a 6-month term, set the Renewal Term to 6. Available in API version 60.0 and
later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The unit of time for a subscription term.

Valid values are:

**•** `Annual` —UI label is **Years**

**•** `Months`

**•** `Quarterly` —Available in API version 61.0 and later.

**•** `Semi-Annual` —Available in API version 61.0 and later.

Available in API version 60.0 and later.

**Type**
address

**Properties**
Filter, Nillable


Standard Objects Contract

**Field** **Details**

**Description**
The compound form of the shipping address. Read-only. See Address Compound Fields for
details on compound address fields.

```
ShippingCity

ShippingCountry

ShippingCountryCode

ShippingGeocodeAccuracy

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details of the shipping address. City maximum size is 40 characters.

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
The ISO country code for the contract's shipping address.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The accuracy of the geocode for the shipping address.

Valid values are:

**•** `Address`

**•** `Block`

**•** `City`

**•** `County`

**•** `ExtendedZip`

**•** `NearAddress`

**•** `Neighborhood`

**•** `State`


Standard Objects Contract

**Field** **Details**

**•** `Street`

**•** `Unknown`

**•** `Zip`

Available in API version 60.0 and later.

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
Used with `ShippingLongitude` to specify the precise geolocation of a shipping address.
Acceptable values are numbers between –90 and 90 with up to 15 decimal places.

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
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details of the shipping address. The postal code maximum size is 20 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details of the shipping address. The maximum size for the state is 80 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO state code for the contract's shipping address.


Standard Objects Contract

**Field** **Details**

```
ShippingStreet

SourceQuoteId

SpecialTerms

StartDate

Status

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street address of the shipping address. The maximum size is 255 characters.

**Type**
reference

**Properties**
Create, Filter, Group, Sort,Update

**Description**
ID of the source quote associated with this contract. This field is available with Revenue Cloud
in API version 64.0 and later.

This field is a relationship field.

**Relationship Name**
Contract

**Relationship Type**
Lookup

**Refers To**
Quote

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Special terms that apply to the contract.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort,Update

**Description**
Start date for this contract. The label is **Contract Start Date** .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update


Standard Objects Contract

**Field** **Details**

**Description**
The picklist of values that indicate order status. Each value is within one of two status
categories defined in `StatusCode` . For example, the status picklist may contain: Ready
to Ship, Shipped, Received as values within the Activated `StatusCode` .

Valid values are:

**•** `Activated`

**•** `Draft`

**•** `In Approval Process`

Available in API version 60.0 and later.

```
StatusCode

UnitPriceUplift

```

Usage

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status category for the contract. A contract can be Draft, InApproval, or Activated. Label
is **Status Category** .

Valid values are:

**•** `Activated`

**•** `Draft`

**•** `InApproval`

Available in API version 60.0 and later.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates the percentage increase of a line item’s unit price. This field is available with Revenue
Cloud in API version 64.0 and later.

The Contract object represents a business agreement.

The `Status` field specifies the current state of a contract. Status strings (defined in the ContractStatus object) represent its current
state ( `Draft`, `InApproval`, or `Activated` ).

Client applications must initially create a Contract in a non-Activated state. Client applications can subsequently activate a Contract by
updating it and setting the value in its `Status` field to `Activated` ; however, the `Status` field is the only field you can update
when activating the Contract.


### Standard Objects ContractContactRole

After a Contract has been activated, your client application can't change its status; however, before activation, your client application
can change the status value from `Draft` to `InApproval` via the API. Also, your client application can delete contracts whose status
is `Draft` or `InApproval` but not when a contract status is `Activated` .

Client applications can use the API to create, update, delete, and query any Attachment associated with a contract.

Associated Objects

This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**AccountChangeEvent (API version 46.0)**
Change events are available for the object.

**ContractFeed (API version 18.0)**
Feed tracking is available for the object.

**ContractHistory**

History is available for tracked fields of the object.

SEE ALSO:

### ContractContactRole

ContractStatus

### ContractContactRole

Represents the role that a Contact plays on a Contract.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ContactId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the Contact associated with this Contract.

This is a relationship field.

**Relationship Name**
Contact


Standard Objects ContractContactRole

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Contact

```
ContractId

IsDeleted

IsPrimary

Role

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the Contract.

This is a relationship field.

**Relationship Name**
Contract

**Relationship Type**
Lookup

**Refers To**
Contract

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
Create, Defaulted on create, Filter, Group, Sort,Update

**Description**
Specifies whether this Contact plays the primary role on this Contract ( `true` ) or not ( `false` ).
Each contract has one primary contact role. Default is `false` . Labels is **Primary** .

**Type**
picklist

**Properties**
Create, Filter, Nillable, Group, Sort, Update


### Standard Objects ContractLineItem

**Field** **Details**

**Description**
Name of the role played by the Contact on this Contract, such as Decision Maker, Approver,
Buyer, and so on. Must be unique—there can't be multiple records in which the
`ContractId`, `ContactId`, and `Role` values are identical. Different contacts can play
the same role on the same contract. A contact can play different roles on the same contract.

SEE ALSO:

ContractStatus

### ContractLineItem

Represents a product covered by a service contract (customer support agreement). This object is available in API version 18.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AssetId

Description

Discount

```

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
Required. ID of the Asset associated with the contract line item. Must be a valid asset ID.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the contract line item.

**Type**
percent

**Properties**
Create, Filter, Nillable, Update


Standard Objects ContractLineItem

**Field** **Details**

**Description**
The discount for the product as a percentage.

When updating, if you specify `Discount` without specifying `TotalPrice`, the
`TotalPrice` will be adjusted to accommodate the new `Discount` value, and the
`UnitPrice` will be held constant.

If you specify both `Discount` and `Quantity`, you must also specify either
`TotalPrice` or `UnitPrice` so the system can determine which one to automatically
adjust.

```
EndDate

LastReferencedDate

LastViewedDate

LineItemNumber

ListPrice

```

**Type**
date

**Properties**
Create, Filter, Nillable, Update

**Description**
The last day the contract line item is in effect.

**Type**
date

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
date

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view ( `LastReferencedDate` ) but
not viewed it.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Update

**Description**
Automatically-generated number that identifies the contract line item.

**Type**
currency


Standard Objects ContractLineItem

**Field** **Details**

**Properties**
Filter, Nillable

**Description**
Corresponds to the `UnitPrice` on the PricebookEntry that is associated with this line
item, which can be in the standard pricebook or a custom pricebook. A client application
can use this information to show whether the unit price (or sales price) of the line item differs
from the pricebook entry list price.

```
LocationId

ParentContractLineItemId

PricebookEntryId

Product2Id

Quantity

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The location associated with the contract line item.

If you have access to the location entity, it doesn’t necessarily mean you can access the
location id field. To access the location, you must have `userHasLocation` user access.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The line item’s parent line item, if it has one.

**Type**
reference

**Properties**
Create, Filter, Update

**Description**
Required. ID of the associated PricebookEntry.

Only exists if Product2 is enabled.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The product related to the contract line item.

**Type**
double


Standard Objects ContractLineItem

**Field** **Details**

**Properties**
Create, Filter, Update

**Description**
Number of units of the contract line item (product) included in the associated service contract.

```
RootContractLineItemId

ServiceContractId

StartDate

Status

Subtotal

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
(Read only) The top-level line item in a contract line item hierarchy. Depending on where a
line item lies in the hierarchy, its root could be the same as its parent.

**Type**
reference

**Properties**
Create, Filter

**Description**
Required. ID of the ServiceContract associated with the contract line item. Must be a valid
service contract ID.

**Type**
date

**Properties**
Create, Filter, Nillable, Update

**Description**
The first day the contract line item is in effect.

**Type**
picklist

**Properties**
Filter, Nillable

**Description**
Status of the contract line item.

**Type**
currency

**Properties**
Filter, Nillable

**Description**
Contract line item's sales price multiplied by the `Quantity` .


### Standard Objects ContractLineOutcome

**Field** **Details**

```
TotalPrice

UnitPrice

```

Associated Objects

**Type**
currency

**Properties**
Filter, Nillable

**Description**
This field is available only for backward compatibility. It represents the total price of the
ContractLineItem

If you specify `Discount` and `Quantity`, this field or `UnitPrice` is required.

This field is nillable, but you can't set both `TotalPrice` and `UnitPrice` to null in the
same update request. To insert the `TotalPrice` for a contract line item via the API (given
only a unit price and the quantity), calculate this field as the unit price multiplied by the
quantity.

**Type**
currency

**Properties**
Create, Filter, Update

**Description**
The unit price for the contract line item. In the user interface, this field’s value is calculated
by dividing the total price of the contract line item by the quantity listed for that line item.
Label is **Sales Price** .

This field or `TotalPrice` is required. You can’t specify both.

If you specify `Discount` and `Quantity`, this field or `TotalPrice` is required.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ContractLineItemChangeEvent (API version 44.0)**
Change events are available for the object.

**ContractLineItemFeed**

Feed tracking is available for the object.

**ContractLineItemHistory**

History is available for tracked fields of the object.

### ContractLineOutcome

Represents information on a contract line outcome’s captured data and other related parameters that are used when capturing data.
This object is available in API version 58.0 and later.


Standard Objects ContractLineOutcome

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

**•** Field Service must be enabled.

**•** Entitlements must be enabled.

Fields

**Field** **Details**

```
CalculationMethod

CaptureFrequency

ComplianceStatus

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The method used for calculating the contract line outcome’s captured data to determine
the outcome value. Select `Average` or `As Captured` to calculate the contract line
outcome. `Average` calculates the outcome value based on the average of all data captured
to date. `As Captured` calculates the outcome value based on the asset’s current data at
the time of the compliance check.

Possible values are:

**•** `AsCaptured`

**•** `Average`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The frequency at which data capturing and contract compliance check for the contract line
outcome occurs.

Possible values are:

**•** `Daily`

**•** `Monthly`

**•** `Weekly`

**Type**
picklist


Standard Objects ContractLineOutcome

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates if the criteria were met. Compliant–The outcome is compliant with the contract.
Not Compliant–The outcome isn’t compliant with the contract. Not Available–The outcome’s
compliance information isn’t available yet. Invalid–The outcome isn’t valid because the
option selected for the Criteria Field of the recordset filter criteria was deleted. To restart the
calculation, create a new contract line outcome.

Possible values are:

**•** `Compliant`

**•** `Invalid`

**•** `NotAvailable`

**•** `NotCompliant`

The default value is `NotAvailable` .

```
ContractLineItemId

Description

EndDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The contract line item associated with the contract line outcome.

This field is a relationship field.

**Relationship Name**
ContractLineItem

**Relationship Type**
Lookup

**Refers To**
ContractLineItem

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the contract line outcome.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update


Standard Objects ContractLineOutcome

**Field** **Details**

**Description**
The contract line outcome's data capture end date.

```
LastReferencedDate

LastViewedDate

Name

NextDataCaptureDate

OwnerId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the contract line outcome was last modified. Its UI label is Last
Modified Date.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the contract line outcome was last viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the contract line outcome.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date of the next data capture and compliance check based on the capture frequency.
The date is auto-populated and updated after each capture

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The contract line outcome’s owner. By default, the owner is the user who created the contract
line outcome record. Its UI label is Contract Line Outcome Owner.

This field is a polymorphic relationship field.


Standard Objects ContractLineOutcome

**Field** **Details**

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

```
RecordsetFilterCriteriaId

ServiceContractId

StartDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the recordset filter criteria in which the contract line outcome’s conditions are
defined.

This field is a relationship field.

**Relationship Name**
RecordsetFilterCriteria

**Relationship Type**
Lookup

**Refers To**
RecordsetFilterCriteria

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The service contract associated with the contract line item and the contract line outcome.

This field is a relationship field.

**Relationship Name**
ServiceContract

**Relationship Type**
Lookup

**Refers To**
ServiceContract

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update


### Standard Objects ContractLineOutcomeData

**Field** **Details**

**Description**
The contract line outcome's data capture start date.

Usage

Use this object to define the data capture frequency and other related parameters that are used when capturing data in order to evaluate
a service contract’s compliance.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ContractLineOutcomeChangeEvent on page 68**
Change events are available for the object.

**ContractLineOutcomeFeed on page 55**
Feed tracking is available for the object.

**ContractLineOutcomeHistory on page 63**
History is available for tracked fields of the object.

**ContractLineOutcomeOwnerSharingRule on page 65**
Sharing rules are available for the object.

**ContractLineOutcomeShare on page 67**
Sharing is available for the object.

SEE ALSO:

### ContractLineOutcomeData ContractLineOutcomeData

Represents the contract line outcome’s captured data. It stores the data that was captured between the contract line outcome’s start
date and end date. This object is available in API version 58.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

**•** Field Service must be enabled.

**•** Entitlements must be enabled.


Standard Objects ContractLineOutcomeData

Fields

**Field** **Details**

```
CalculatedValue

CaptureDate

ContractLineOutcomeId

KeyPerformanceIndicator

LastReferencedDate

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The value calculated based on the contract line outcome’s calculation method and the
captured data.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date and time when the data was captured.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The contract line outcome associated with the contract line outcome data record.

This field is a relationship field.

**Relationship Name**
ContractLineOutcome

**Relationship Type**
Lookup

**Refers To**
ContractLineOutcome

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The key performance indicators (fields or asset attributes) that define the contract line
outcome’s compliance status.

**Type**
dateTime


Standard Objects ContractLineOutcomeData

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the contract line outcome data record was last modified. Its UI label
is Last Modified Date.

```
LastViewedDate

Name

Value

```

Associated Objects

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the contract line outcome data record was last viewed.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the contract line outcome data record.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The actual value of the key performance indicator.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ContractLineOutcomeDataChangeEvent on page 68**
Change events are available for the object.

**ContractLineOutcomeDataFeed on page 55**
Feed tracking is available for the object.

**ContractLineOutcomeDataHistory on page 63**
History is available for tracked fields of the object.

**ContractLineOutcomeDataOwnerSharingRule on page 65**
Sharing rules are available for the object.

**ContractLineOutcomeDataShare on page 67**
Sharing is available for the object.


### Standard Objects ContractStatus ContractStatus

Represents the status of a Contract, such as Draft, InApproval, Activated, Terminated, or Expired.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

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
Uniquely identifies a picklist value so it can be retrieved without using an id or primary label.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this is the default contract status value ( `true` ) or not ( `false` ) in the
picklist.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Label for this contract status value. This display value is the internal label that does not get
translated.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects ContractTag

**Field** **Details**

**Description**
Number used to sort this value in the contract status picklist. These numbers are not
guaranteed to be sequential, as some previous contract status values might have been
deleted.

```
 StatusCode

```

Usage

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Code indicating the status of a contract. One of the following values:

**•** `Draft`

**•** `InApproval`

**•** `Activated`

Two other values ( `Terminated` and `Expired` ) are defined but are not available for use
via the API.

This object represents a value in the contract status picklist. The contract status picklist provides additional information about the status
of a Contract, such as its current state ( `Draft`, `InApproval`, or `Activated` ). You can query these records to retrieve the set of
values in the contract status picklist, and then use that information while processing Contract objects to determine more information
about a given contract. For example, the application could test whether a given contract is activated based on its `Status` value and
the value of the `StatusCode` property in the associated ContractStatus object.

SEE ALSO:

ContractContactRole

### ContractTag

Associates a word or short phrase with a Contract.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`


Standard Objects ContractTag

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

ContractTag stores the relationship between its parent TagDefinition and the Contract being tagged. Tag objects act as metadata,
allowing users to describe and organize their data.


### Standard Objects ConvAnalysisSummary

When a tag is deleted, its parent TagDefinition will also be deleted if the name is not being used; otherwise, the parent remains. Deleting
a TagDefinition sends it to the Recycle Bin, along with any associated tag entries.

### ConvAnalysisSummary

Represents the information stored for each run or refresh of Sales Signals. This object is available in API version 63.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Users need the Sales Signals permission set and the Sales Signals feature must be enabled.

Fields

**Field** **Details**

```
AnalysisDate

DataModelVersion

Error

FlowIdentifier

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date when the actual data analysis was done, accounting for the delay between the
refresh start time and the data analysis.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The data model version generated by Hawking.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The error message sent by Hawking when a refresh fails.

**Type**
string


Standard Objects ConvAnalysisSummary

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
Required. The UUID used to track the Hawking flow ID.

```
RefreshDate

Status

TotalCalls

TotalMentions

```

**Type**
dateTime

**Properties**
Create, Filter, Sort

**Description**
Required. The date when the admin started the refresh of their ECI data for processing.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. The status of the refresh or run.

Possible values are:

**•** `FAILED`

**•** `PARTIALLY_FAILED`

**•** `PROCESSING`

**•** `SUCCESS`

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The total number of calls that were analyzed for Sales Signals.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The total number of mentions or keywords that were analyzed.


### Standard Objects ConvAnalysisTopic ConvAnalysisTopic

Represents a topic generated from the Sales Signals refresh or run. For example, a product experiencing issues due to high pricing could
be a topic identified through the analysis of multiple calls. This object is available in API version 63.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Users need the Sales Signals permission set and the Sales Signals feature must be enabled.

Fields

**Field** **Details**

```
CallPercentage

Category

ConvAnalysisSummaryId

```

**Type**
double

**Properties**
Create, Filter, Sort

**Description**
Required. The percentage of calls that apply to a topic, out of the total number of calls that
were analyzed.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
Required. A classification or grouping used to filter topics. This field is used in conjunction
with `Keyword` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. The conversation analysis summary associated with the topic.

This field is a relationship field.

**Relationship Name**
ConvAnalysisSummary


Standard Objects ConvAnalysisTopic

**Field** **Details**

**Relationship Type**
Master-detail

**Refers To**
ConvAnalysisSummary (the parent object)

```
GenerationsIdentifier

Keyword

MentionCount

Order

Summary

```

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
Required. The ID used to track the LLM-generated response for feedback purposes.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
Required. A specific word used in conjunction with `Category` to filter topics. For example,
`Product:Salesforce`, where the keyword is Salesforce.

**Type**
int

**Properties**
Create, Filter, Group, Sort

**Description**
Required. The number of call insights associated with the topic.

**Type**
int

**Properties**
Create, Filter, Group, Sort

**Description**
Required. A numerical value used to sort topics in a sequence.

**Type**
textarea

**Properties**
Create, Update

**Description**
Required. A detailed explanation of the topic.


Standard Objects ConvAnalysisTopic

**Field** **Details**

```
Title

TopicSentiment

TotalCalls

TotalCallsForCategoryKeyword

TotalMentionsForCategoryKeyword

TurnIdentifier

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The title of the topic that describes it.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The sentiment of the topic, whether it’s negative, neutral, or positive.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The total number of calls analyzed for the topic.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The total number of calls analyzed for `category:keyword` . Multiple topics can be under
a single `category:keyword` .

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The total number of mentions analyzed for `category:keyword` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort


### Standard Objects ConvAnalysisTopicEntry

**Field** **Details**

**Description**
UUID that is generated and used to track a group of LLM-generated content.

### ConvAnalysisTopicEntry

Represents a single entry under the ConvAnalysisTopic object. An entry represents a segment of a video or voice call that is associated
with a conversation analysis topic. This object is available in API version 63.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Users need the Sales Signals permission set and the Sales Signals feature must be enabled.

Fields

**Field** **Details**

```
BulletGenerationsIdentifier

CallId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The generation ID used to track the LLM-generated response for feedback purposes.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The unique identifier of the voice or video call that corresponds to the entry.

This field is a polymorphic relationship field.

**Relationship Name**
Call

**Refers To**
VideoCall, VoiceCall


### Standard Objects Conversation

**Field** **Details**

```
ConvAnalysisTopicId

SnippetStartTime

Summary

### Conversation

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. The conversation analysis topic associated with the entry.

This field is a relationship field.

**Relationship Name**
ConvAnalysisTopic

**Relationship Type**
Master-detail

**Refers To**
ConvAnalysisTopic (the parent object)

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The timestamp when the call is associated with the current topic entry.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The LLM-generated call summary that corresponds to the parent topic.

Represents a conversation between an end user and an agent. Available in API version 49.0 and later.

Note: This object is available for Einstein Conversation Insights customers whose data is stored natively on the Salesforce Platform.
If you turned on Einstein Conversation Insights for the first time starting in Spring ’26, this object is available to query and access
using Salesforce tools. For existing ECI customers, data migration and access to related Salesforce Platform objects is scheduled
to begin in Summer ’26.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`


Standard Objects Conversation

Fields

**Field** **Details**

```
ConversationChannelId

ConversationIdentifier

EndTime

Name

StartTime

```

**Type**
reference

**Properties**
Filter, Group, idLookup, Sort

**Description**
The record ID of the channel used to initialize the conversation. This can either be a messaging
channel for the Messaging product or a call center for the Service Cloud Voice product.
Available in API version 50.0 and later.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
A unique identifier generated for the conversation.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that a conversation ends.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The autogenerated name of the conversation.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that a conversation starts.


### Standard Objects ConversationApiLog ConversationApiLog

Logs of an API operation on a specific conversation object done using the Conversation Service API. This object is available in API version
63.0 and later.

[This object stores the logs of operations done on the Conversation Service API. The Conversation Service API enables you to interact](https://developer.salesforce.com/docs/service/conversation-service-api/overview)
with conversational data on the Conversation Platform, offering tools to manage, access, and maintain your data effectively.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
Action

Name

Operation

OwnerId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The specific action performed using the Conversation Service API.

Possible values are:

**•** `Delete`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Autogenerated name of the logs.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
Name of the operation that triggered the Conversation Srevice API log.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects ConversationApiLog

**Field** **Details**

**Description**
Owner ID that triggered the Conversation API log.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

```
RequestedById

RequestedDate

RequestedEntityIdentifier

RequestedEntityType

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The User ID that triggered the Conversation API log.

This field is a relationship field.

**Relationship Name**
RequestedBy

**Refers To**
User

**Type**
dateTime

**Properties**
Create, Filter, Sort

**Description**
The date of the operation that triggered the Conversation API log.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The entity ID being created, updated, or deleted.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of entity being created, updated, or deleted.

Possible values are:


### Standard Objects ConversationContextEntry

**Field** **Details**

**•** `MessagingEndUser` —Messaging End User

```
Status

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the Conversation API operation.

Possible values are:

**•** `Completed`

**•** `Enqueued`

**•** `Failed`

**•** `InProgress` —In Progress

**•** `Requested`

### ConversationContextEntry

Represents the context of a message or an event in the chat history between an agent and a messaging user. This object is available in
API version 47.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

As of Summer ’20 and later, only authenticated internal and external users can access this object.

Fields

**Field** **Details**

### `ConversationContextEntryName`

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The autogenerated number of the entry.


### Standard Objects ConversationChannelDefinition

**Field** **Details**

```
 CustomDetailContextKey

 CustomDetailContextValue

 ParentId

```

Associated Objects

**Type**
textarea

**Properties**
Create, Nillable

**Description**
The key or name of the pre-chat field specified by the admin in the pre-chat implementation,
for example, `customer_email` .

**Type**
textarea

**Properties**
Create, Nillable

**Description**
The value entered in the pre-chat field by a user before starting the chat.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The Conversation ID this entry is associated with.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ConversationContextChangeEvent (API version 62.0)**
Change events are available for the object.

### ConversationChannelDefinition

Represents a configurable definition of a conversation channel that’s implemented for Interaction Service for Bring Your Own Channel
for Messaging and Bring Your Own Channel for CCaaS messaging channels. This object is available in API version 60.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects ConversationChannelDefinition

Special Access Rules

To access this object, interaction service must be configured. Access to standard objects requires Salesforce admin privileges or the
Customize Application permission.

Fields

**Field** **Details**

```
CapabilitiesSupportsCustomChannelParameters

CapabilitiesSupportsDoubleOptInConsent

CapabilitiesSupportsExplicitConsent

CapabilitiesSupportsImplicitConsent

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether admins can configure custom parameters and parameter mappings for
messaging channels. Custom parameters and parameter mappings are used to pass additional
information at runtime to Omni-Channel flows. The default value is _`false`_ . Available in API
version 61.0.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the channel supports ( _`true`_ ) the Double Opt-In consent level. The default
value is _`false`_ . If set to true, then `capabilitiesSupportsExplicitConsent`
must also be set to true. This field is optional and isn’t supported for Bring Your Own Channel
for Messaging. It's only supported for Bring Your Own Channel for CCaaS.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the channel supports ( _`true`_ ) the Explicit Opt-In consent level. This field
is optional.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the channel supports ( _`true`_ ) the Implicit Opt-In consent level. This value
is required and must always be set to true. The default value is false.


Standard Objects ConversationChannelDefinition

**Field** **Details**

```
CapabilitiesSupportsIsoCountryCode

CapabilitiesSupportsKeywords

ConnectedAppOauthLink

ConnectedAppType

ConsentOwner

```

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the channel supports ( _`true`_ ) ISO country codes. The default value is false.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the channel supports ( _`true`_ ) keywords. The default value is false.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
DO NOT SET OR CHANGE THIS VALUE. This value is automatically generated. This field
represents the OAuth link for the external client app (ECA) or connected app if the
ConnectedAppType is `Partner` . This is a string identifier to the ECA or connected app
containing the partner Org ID and the consumer ID minus the key prefixes.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The owner of the external client app (ECA) or connected app used to manage authentication
between Salesforce Interaction Service and the Messaging or CCaaS partner’s system.

Possible values are:

**•** `Partner`

**•** `Customer`

The default value is `Partner` .

If set to _`Partner`_, the partner creates the ECA or connected app and includes it in their
managed package. If set to _`Customer`_, the admin creates the ECA or connected app.

Available in API version 62.0.

**Type**
picklist


Standard Objects ConversationChannelDefinition

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The system the customer uses to manage consent levels.

Possible values are:

**•** `Partner`

**•** `Salesforce`

The default value is `Salesforce` .

For example, if set to _`Salesforce`_, consent levels are managed by the Salesforce system.
If set to _`Partner`_, consent levels are managed by the partner’s telephony system.

For Bring Your Own Channel for Messaging, this value must be set to _`Salesforce`_ .

```
ConversationVendorInfoId

customEventChnlAddrIdField

CustomEventPayloadField

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The _`ConversationChannelDefinition.ConversationVendorInfoId`_
value used to link this record to the ConversationVendorInfo record. For example,
0m8000000000000123.

This field is a relationship field.

**Relationship Name**
ConversationVendorInfo

**Relationship Type**
Lookup

**Refers To**
ConversationVendorInfo

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The mapping field that points to the custom field used to point to the
`ChannelAddressIdentifier` field.

This field is deprecated in API version 60.0 and will be removed in API version 61.0. Use a
combination of `customEventTypeField` and `customEventPayloadField`
instead.

**Type**
picklist


Standard Objects ConversationChannelDefinition

**Field** **Details**

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The mapping field that points to the custom field used to point to the `Payload` field in
the format _`<orgNamespace>`_ __ _`<CustomFieldName>`_ __c. This is the API name of
the custom Payload field in the custom platform event. For example, devorg__Payload__c.

```
customEventRecipientField

CustomEventTypeField

CustomIconId

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The mapping field that points to the custom field used to point to the Recipient field.

This field is deprecated in API version 60.0 and will be removed in API version 61.0. Use a
combination of `customEventTypeField` and `customEventPayloadField`
instead.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The mapping field that points to the custom field used to point to the Platform event type
(EventType) field, in the format _`<orgNamespace>`_ __ _`<CustomFieldName>`_ __c. This
is the API name of the custom EventType field in the custom platform event. For example,
devorg__EventType__c.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
For Bring Your Own Channel for Messaging and Bring Your Own Channel for CCaaS, this field
represents the name of the status resource image used to identify the channel integration,
such as a channel logo. For the best results, set the image size to 50px x 50px and save the
image in SVG file format. This field is optional. Available in API version 61.0 and later.

This field is a relationship field.

**Relationship Name**
CustomIcon

**Relationship Type**
Lookup


Standard Objects ConversationChannelDefinition

**Field** **Details**

**Refers To**
StaticResource

```
CustomPlatformEvent

CustomerConnectedAppOauthLink

DeveloperName

EventCapabilitiesIsInboundAcknwOptionExposed

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The API name of the custom platform event created for the Interaction Service API in the
format _`<orgNamespace>`_ __ _`<CustomPlatformEventName>`_ __e. For example,
devorg__TestEvent__e.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
DO NOT SET OR CHANGE THIS VALUE. This value is automatically generated. This field
represents the OAuth link for the external client app or connected app created by an admin
if the ConnectedAppType is `Customer` . Available in API version 62.0.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique name of the custom metadata type object in the API in the format
_`<Prefix>`_ _ _`<ConversationChannelDefinition>`_, where _`Prefix`_ matches
the prefix you gave to the name of the Interaction Service external client app or connected
app. For example, Partner1_ChannelDefinition1, where Partner1 is the prefix and
ChannelDefinition1 is the given name.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the partner supports read receipts and delivery receipts for inbound
messages ( `true` ) or whether the partner doesn’t support these inbound acknowledgments
and the functionality is hidden from the Salesforce admin in the Messaging settings ( `false` ).
The default value is `false` .

This field is available in API version 65.0 and later. Use this field instead of
`IsInboundReceiptsEnabled` .


Standard Objects ConversationChannelDefinition

**Field** **Details**

```
EventCapabilitiesIsProgressIndicatorOptExposed

EventCapabilitiesIsRoutingWorkResultSupported

EventCapabilitiesIsTypingIndicatorOptionHidden

IsConferenceSupported

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the partner supports progress indicators for AI agents ( `true` ) or whether
the partner doesn’t support them and the functionality is hidden from the Salesforce admin
in the Messaging settings ( `false` ). The default value is `false` .

This field is available in API version 65.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the Routing Work Result event is sent as a Custom Platform event ( `true` )
or not ( `false` ). The default value is `false` .

This field is available in API version 65.0 and later. Use this field instead of
`IsRoutingWorkResultEnabled` .

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the partner doesn’t support typing indicators for outbound messages and
the functionality is hidden from the Salesforce admin in the Messaging settings ( `true` ) or
whether outbound typing indicators are supported by the partner ( `false` ). The default
value is `false`, meaning the outbound typing indicator feature is supported by default.
To disable the outbound typing indicator feature, set this value to `true` .

This field is available in API version 65.0 and later. Use this field instead of
`IsTypingIndicatorDisabled` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the partner supports conferencing for Bring Your Own Channel ( `true` ),
or not ( `false` ). With conferencing, more than two participants are allowed in a Messaging
session. The default is `false` .

This field is available in API version 64.0 and later.


Standard Objects ConversationChannelDefinition

**Field** **Details**

```
IsInboundReceiptsEnabled

IsRoutingWorkResultEnabled

IsTypingIndicatorDisabled

MasterLabel

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the partner supports read receipts and delivery receipts for inbound
messages ( `true` ) or whether the partner doesn’t support these inbound acknowledgements
and the functionality is hidden from the Salesforce admin in the Messaging settings ( `false` ).
The default value is `false` .

Available in API versions 63.0 to 65.0. In API version 66.0 and later, this field is removed. Use
`EventCapabilitiesIsInboundAcknwOptionExposed` instead.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the Routing Work Result event is sent as a Custom Platform event or not.

The default value is `false` .

Available in API versions 64.0 and 65.0. In API version 66.0 and later, this field is removed.
Use `EventCapabilitiesIsRoutingWorkResultSupported` instead.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the partner doesn’t support typing indicators for outbound messages and
the functionality is hidden from the Salesforce admin in the Messaging settings ( `true` ) or
whether outbound typing indicators are supported by the partner ( `false` ). The default
value is `false`, meaning the outbound typing indicator feature is supported by default.
To disable the outbound typing indicator feature, set this value to `true` .

Available in API versions 63.0 to 65.0. In API version 66.0 and later, this field is removed. Use
`EventCapabilitiesIsTypingIndicatorOptionHidden` instead.

**Type**
string

**Properties**
Filter, Group, Sort


Standard Objects ConversationChannelDefinition

**Field** **Details**

**Description**
The UI label name for the custom metadata type object in the API. This name appears in
several places in the UI, so include the partner channel name for easy identification. For
example, Channel Definition 1.

```
MaxParticipantsForCnfrOverride

NamespacePrefix

RoutingOwner

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the limit for how many participants can be in a messaging conference. If set, this
field overrides the platform limit for the number of participants in a conference. If not set or
if set to a value higher than the messaging platform limit, the limit defaults to the messaging
platform limit of how many participants can be in a messaging conference at one time.

This field is available in API version 64.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can
refer to a component in a managed package by using the
_`namespacePrefix`_ __ _`componentName`_ notation. The namespace prefix can have
one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

`NamespacePrefix` is null if the publisher is Salesforce.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The system the customer uses to manage routing for Bring Your Own Channel for Messaging
or Bring Your Own Channel for CCaaS.


### Standard Objects ConversationEntry

**Field** **Details**

Possible values are:

**•** `Partner`

**•** `Salesforce`

The default value is `Salesforce` .

For example, if set to _`Salesforce`_, routing is managed by the Salesforce system. If set to
_`Partner`_, routing is managed by the partner’s system.

For Bring Your Own Channel for Messaging, this value must be set to _`Salesforce`_ .

### ConversationEntry

Represents a message or event in a voice call or messaging session. The schema on this page only applies to conversation entries for
[legacy chat. Refer to the ConversationEntry (Off-Core) schema in the Messaging Object Model guide to see the ConversationEntry schema](https://developer.salesforce.com/docs/service/messaging-object-model/guide/overview.html)
for Enhanced Channels. This object is available in API version 43.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To use the ConversationEntry object, enable the Access Conversation Entries user permission, which is available in API version 50.0 and
later. Earlier versions do not require permissions.

Fields

**Field** **Details**

```
ActorId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the author. The possible values can be `null` or any ID in the following domain
set:

**•** `BotDefinition`

**•** `LiveChatVisitor`

**•** `MessagingEndUser`

**•** `User`

This is a polymorphic relationship field.


Standard Objects ConversationEntry

**Field** **Details**

**Relationship Name**
Actor

**Relationship Type**
Lookup

**Refers To**
MessagingEndUser, User

```
ActorName

ActorType

ClientDuration

ClientTimestamp

```

**Type**
string

**Properties**
Create, Filter, Nillable, Sort

**Description**
The name of the author sending the message or event.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The author of this entry in the chat history. The valid values include:

**•** `Agent`

**•** `Bot`

**•** `EndUser`

**•** `Supervisor`

**•** `System`

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The length in milliseconds for the entry. This field is used with voice messages and other
applicable use cases. This value may be 0 if not set by the client. This field is available in API
version 51.0 and later.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort


Standard Objects ConversationEntry

**Field** **Details**

**Description**
The timestamp sent by the client when it generated the entry. This field is available in API
version 51.0 and later.

```
ConversationId

EntryEndTime

EntryTime

EntryTimeMilliSecs

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The MessagingSession ID this entry belongs to.

This is a polymorphic relationship field.

**Relationship Name**
Conversation

**Relationship Type**
Lookup

**Refers To**
MessagingSession, VoiceCall

**Type**
datetime

**Properties**
Create, Filter, Nillable, Sort

**Description**
The timestamp that this entry ended in the chat history. This field is available in API version
48.0 and later.

**Type**
datetime

**Properties**
Create, Filter, Sort

**Description**
The timestamp of this entry in the chat history.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The milliseconds value for the time when an entry was received by the server. Note that the
related `EntryTime` field does not provide millisecond accuracy. This field is available in
API version 51.0 and later.


Standard Objects ConversationEntry

**Field** **Details**

```
EntryType

HasAttachments

Message

MessageDeliverTime

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of entry in the chat history. Can be a message ( `text` ) or an event. The possible
values include:

**•** `Text`

**•** `AdminOptedIn`

**•** `AdminOptedOut`

**•** `BotEscalated`

**•** `ChatbotClosedIdleSession`

**•** `ChatbotEndedChatByAction` —Conversation ended by automated action

**•** `ChatbotEndedTransferNotConfigured` —Conversation ended because
transfer fail is not configured

**•** `ChatbotEstablished`

**•** `ChatbotNotEstablished`

**•** `EndUserOptedIn`

**•** `EndUserOptedOut`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a message has attachments associated with it ( `true` ) or not ( `false` ).

**Type**
textarea

**Properties**
Create, Nillable

**Description**
The message or event sent by the author. In ConversationEntry records for enhanced
Messaging channels or Messaging for In-App and Web, the Message field is blank due to
data storage differences from standard channels.

**Type**
datetime

**Properties**
Create, Filter, Nillable, Sort


Standard Objects ConversationEntry

**Field** **Details**

**Description**
Unused field reserved for future use.

```
MessageIdentifier

MessageReadTime

MessageSendTime

MessageStatus

MessageStatusCode

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The unique ID for the message. Maximum size is 36 characters.

**Type**
datetime

**Properties**
Create, Filter, Nillable, Sort

**Description**
Unused field reserved for future use.

**Type**
datetime

**Properties**
Create, Filter, Nillable, Sort

**Description**
Unused field reserved for future use.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of the message sent by the author. The valid values include:

**•** `Delivered`

**•** `Error`

**•** `Pending`

**•** `Read`

**•** `Sent`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects ConversationEntry

**Field** **Details**

**Description**
The code associated with a message status. `MessageStatusCode` is only populated
when a message is undeliverable

```
Seq

ServerReceivedTimestamp

```

Usage

**Type**
int

**Properties**
Create, Filter, Group, Sort

**Description**
The sequence position of this entry in the chat history.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
The timestamp recorded when the server received the entry. This is a unique value and is
used for ordering. This value can also be referred to as the “transcripted timestamp.” This
field is available in API version 51.0 and later.

Important: The schema on this page only applies to conversation entries for legacy chat. The legacy chat product is in
maintenance-only mode, and we won't continue to build new features. Refer to the ConversationEntry (Off-Core) schema in the
[Messaging Object Model guide to see the ConversationEntry schema for Enhanced Channels.](https://developer.salesforce.com/docs/service/messaging-object-model/guide/overview.html)

In standard SMS, WhatsApp, and Facebook Messenger channels, a ConversationEntry record is created for each message sent by a
messaging end user or an agent, bot, or automation. Each ConversationEntry record is associated with a MessagingSession record, which
represents the interaction between the messaging end user and the business. Access and work with ConversationEntry records like any
standard object. You can report on messaging activity and track the conversation workflow end to end. You can also download or delete
transcripts, redact sensitive text, and customize your workflows with solutions built on the ConversationEntry object.

In enhanced Messaging channels, Messaging for In-App and Web, and Service Cloud Voice ("enhanced channels"), inbound and outbound
messages are processed in one of two ways depending on your location.

**•** A ConversationEntry record is created but the `Message` field is blank, or

**•** No ConversationEntry record is created.

To get the fullest picture of conversations in enhanced channels, use Data Cloud, the Connect REST API, or the Conversation Transcript
[Export tool to access transcripts. See Accessing Messaging and Voice Conversation Data.](https://help.salesforce.com/s/articleView?id=service.conversation_transcript_access.htm&type=5&language=en_US)

Note: ConversationEntry records aren’t created until the messaging session ends and the agent closes the session tab. One
exception is for the first message in any standard messaging session, whose ConversationEntry record is created immediately.


### Standard Objects ConversationParticipant ConversationParticipant

Represents an active participant in a conversation. A new ConversationParticipant record is created each time a participant joins a
conversation. This object is available in API version 49.0 and later.

Note: This object is available for Einstein Conversation Insights customers whose data is stored natively on the Salesforce Platform.
If you turned on Einstein Conversation Insights for the first time starting in Spring ’26, this object is available to query and access
using Salesforce tools. For existing ECI customers, data migration and access to related Salesforce Platform objects is scheduled
to begin in Summer ’26.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
AppType

ConversationId

JoinedTime

LastActiveTime

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of app used by the participant, such as messaging, chatbot, live_message, agent.
The nillable property is available in API version 51.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The record ID of the conversation that this participant is part of.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date and time that a participant joined a conversation.

**Type**
dateTime

**Properties**
Filter, Sort


Standard Objects ConversationParticipant

**Field** **Details**

**Description**
The date and time that a participant was last active during a conversation.

```
LeftTime

Name

ParticipantContext

ParticipantEntityId

ParticipantKey

ParticipantRole

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that a participant left a conversation.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The autogenerated name of the conversation participants.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
An identifier, such as a Facebook page, to add context about this participant.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the record connected to this participant record, such as a Contact, Messaging End
User, or User record.

**Type**
string

**Properties**
Filter, idLookup, Group, Nillable, Sort

**Description**
A value that uniquely identifies this participant.

**Type**
string


### Standard Objects ConvIntelligenceSignalRule

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The role of this participant in the conversation, such as Agent, End User, or Supervisor.

### ConvIntelligenceSignalRule

Represents a conversation intelligence signal rule. The rule triggers actions based on real-time intelligence signals from your telephony
system or keywords mentioned by support reps or customers. The rule contains a set of conditions (subrules) and the filter logic used
to evaluate those conditions to determine whether to trigger actions. This object is available in API version 62.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

This type requires an add-on license for Service Cloud Voice for Amazon Connect, Service Cloud Voice for Partner Telephony with Amazon
Connect, Service Cloud Voice for Partner Telephony, or Digital Engagement.

Fields

**Field** **Details**

```
ActionType

ActionValue

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

Required. Action to take based on the conversation intelligence signal detected during a
conversation. Possible values are:

Possible values are:

**•** `AlertSupervisor` –Sends an alert to the supervisor.

**•** `AlertSupervisorAndAgent` –Sends an alert to the rep and supervisor.

**•** `LaunchFlow` –Triggers an auto-launched flow. If set, also set `ActionValue` .

**•** `LaunchNBA` –Recommends the next best action to the rep.

**Type**
string


Standard Objects ConvIntelligenceSignalRule

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Action to perform based on the `ActionType` specified.

If `ActionType` is set to `LaunchFlow`, this value is the `DeveloperName` of the flow
to be launched. For example, EmailAlert.

For all other `ActionType` values, don’t set this parameter.

```
ConversationChannelId

Criteria

DeveloperName

IsActive

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**

Required. ID ( `ChannelAddressIdentifier` ) of the Messaging channel or name
( `InternalName` ) of the Voice channel.

This field is a polymorphic relationship field.

**Relationship Name**
ConversationChannel

**Refers To**
CallCenter, MessagingChannel

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. Filter logic applied to the rule conditions (subrules). For example, ((1 AND 2) OR
3). The numbers in the formula are derived from the
`ConvIntelligenceSignalSubrule.Order` value plus 1. For example, filter logic
(1 AND 2) is calculated by adding the first condition ( `Order` =0) with the second condition
( `Order` =1).

**Type**
string

**Properties**
Required. Create, Filter, Group, Sort, Update

**Description**
API name of the conversation intelligence signal rule.

**Type**
boolean


Standard Objects ConvIntelligenceSignalRule

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Required. Indicates whether the conversation intelligence signal rule is active ( `true` ) or
inactive ( `false` ). The default value is `false` .

```
Label

ParticipantRole

Service

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Name of the conversation intelligence signal rule.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
If `Service` is set to KeywordMatch, this value determines whether the rule applies to
utterances made by reps, customers, or both roles. Possible values are:

Possible values are:

**•** `Agent`

**•** `AgentOrCustomer`

**•** `Customer`

If `Service` is not set to KeywordMatch, don’t set this parameter.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

Required. Salesforce- or partner-provided intelligence source.

For Salesforce-provided intelligence sources, set this parameter to `KeywordMatch` .

For partner-provided intelligence sources, possible values are:

**•** `AmazonConnectContactLens`

If none of the options apply to you, contact your Salesforce representative for the service
name.


### Standard Objects ConvIntelligenceSignalSubRule ConvIntelligenceSignalSubRule

Represents a condition (subrule) within a conversation intelligence signal rule. This object is available in API version 62.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

This type requires an add-on license for Service Cloud Voice for Amazon Connect, Service Cloud Voice for Partner Telephony with Amazon
Connect, Service Cloud Voice for Partner Telephony, or Digital Engagement.

Fields

**Field** **Details**

```
ConvIntelligenceSignalRuleId

OperandValue

Operator

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Unique ID of the conversation intelligence signal rule. This field is a relationship field.

**Relationship Name**
ConvIntelligenceSignalRule

**Relationship Type**
Master-detail

**Refers To**
ConvIntelligenceSignalRule (the master object)

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Value of the signal type used to determine if the rule condition is met. For example,
escalate_level_1.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


### Standard Objects ConvMessageSendRequest

**Field** **Details**

**Description**
Filter logic operator used to determine if the rule condition is met. Possible values are:

**•** `Equals`

**•** `GreaterThan`

**•** `LessThan`

**•** `NotEquals`

```
Order

Type

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Order the condition appears in relation to the other conditions in the list, with zero (0) being
the first condition listed. If `Type` is set to Keyword, the maximum value is 24. For all other
`Type` values, the maximum value is 4. This value is used when applying filter logic to the
rule.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

Type of conversation intelligence signal used by the rule to determine whether to trigger
an action. This value depends on the ConvIntelligenceSignalRule.ConversationChannelId
and ConvIntelligenceSignalRule.Service values.

If `Service` is set to KeywordMatch, possible values are:

**•** `Keyword` –A word or group of words spoken or typed.

If `Service` is set to AmazonConnectContactLens, possible values are:

**•** `Category` –Category name defined in your telephony system.

If `Service` is set to another value, contact your Salesforce representative for the
conversation intelligence signal types available for your intelligence source.

### ConvMessageSendRequest

Represents a request to send a template-based messaging component to a series of messaging users in an enhanced messaging channel
or Messaging for In-App. This object is available in API version 60.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects ConvMessageSendRequest

Special Access Rules

Messaging and its associated objects are available only in Enterprise, Unlimited, and Developer Editions for Service Cloud or Sales Cloud
with the Digital Engagement add-on license.

Fields

**Field** **Details**

```
AllowExistingSessionStatus

CommSubscriptionId

CompletedDate

FailedMessageCount

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Indicates whether the message can be sent only at certain times.

Possible values are:

**•** `Any` —Send the message regardless of whether the messaging user is engaged in an
active messaging session with the business.

**•** `Closed` —Send the message unless the messaging user is engaged in a messaging
session with a status other than Error or Ended, in which case it’s never sent.

**•** `NonActive` —Send the message unless the messaging user is engaged in a messaging
session with a status of Active, in which case it’s never sent.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the related communication subscription, if applicable. This field is a relationship
field that refers to CommSubscription.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when the request completes and all messages associated with the request
are sent or failed to be sent.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort


Standard Objects ConvMessageSendRequest

**Field** **Details**

**Description**
The number of messages that failed to be delivered to a messaging user. For example, if a
flow sends the message to 50 messaging users and 4 don’t receive the message, this value
is 4.

```
FailedMessageErrorReasons

FailedMessageIdentifiers

FailedMeuPlatformKeys

InProgressMessageCount

InProgressMessageIdentifiers

```

**Type**
textarea

**Properties**
Nillable

**Description**
The error reason for each of the failed messages. For example, if 4 messages fail to send, this
field shows the error reason for each failed message.

**Type**
textarea

**Properties**
Nillable

**Description**
The IDs of the messages that failed to send. For example, if 4 messages fail to send, this field
shows 4 message IDs.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
A list of platform keys for messaging end users with messages that failed to send. Available
in API version 65.0 and later.

**Type**
int

**Properties**
Defaulted on Create, Filter, Group, Sort

**Description**
The number of messages in the process of being sent.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
A list of IDs of the messages being sent.


Standard Objects ConvMessageSendRequest

**Field** **Details**

```
InProgressMessagingEndUserIds

InProgressMessagingSessionIds

InProgressMeuPlatformKeys

MessageDefinition

MessageDefinitionParameters

Name

```

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
A list of IDs of messaging end users with messages that are being sent. Available in API
version 65.0 and later.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
A list of IDs of messaging sessions with messages that are being sent. Available in API version
65.0 and later.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
A list of platform keys for messaging end users with messages that are being sent. Available
in API version 65.0 and later.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The name of the messaging component being sent. Only active messaging components
can be sent.

**Type**
textarea

**Properties**
Nillable

**Description**
A list of parameters used to dynamically construct the message that is being sent. Available
in API version 65.0 and later.

**Type**
string


Standard Objects ConvMessageSendRequest

**Field** **Details**

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated ID for the request that uses the format MSJ-{00000000}.

```
PendingMessageCount

PendingMessageEndUserIds

PendingMeuPlatformKeys

PendingMessageIdentifiers

RequestConsentType

```

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of messages that haven’t yet been sent.

**Type**
textarea

**Properties**
Nillable

**Description**
A list of IDs of the messaging end users with pending messages. Available in API version 65.0
and later.

**Type**
textarea

**Properties**
Nillable

**Description**
A list of platform keys of the messaging end users with pending messages. Available in API
version 65.0 and later.

**Type**
textarea

**Properties**
Nillable

**Description**
A list of IDs of the pending messages.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates whether the flow applies the consent settings of the messaging end user or the
communication subscription.


Standard Objects ConvMessageSendRequest

**Field** **Details**

Possible values are:

**•** `CommunicationSubscription`

**•** `MessagingEndUser`

```
RequestStatus

RequestType

SessionLongevityPreference

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the request.

Possible values are:

**•** `Completed`

**•** `Pending`

**•** `In Progress` —The system is actively trying to send the message. If a message can’t
be sent, the RequestStatus returns to Pending and sending is tried again later.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of request.

Possible values are:

**•** `SendNotificationMessages`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates whether to end the session after the message is sent.

Possible values are:

**•** `KeepSessionOpen` —After the flow sends the message, keep the messaging session
in a New state. If the end user doesn’t respond within 48 hours, the session ends. Use
this option if you expect customers to respond to automated messages and want service
reps to see their response in context.

**•** `EndSession` —After the flow sends the message, end the messaging session. If the
customer responds, a new messaging session is created and routed to your support
team.

**•** `KeepSessionOpenOrAppend` —If there’s an existing session with the messaging
end user in the New state, use that session to send the message. Otherwise, follow the


Standard Objects ConvMessageSendRequest

**Field** **Details**

behavior documented for the `KeepSessionOpen` option. Available in API version
65.0 and later.

```
ShouldEnforceChannelConsent

SuccessMessageCount

SuccessMessageIdentifiers

SuccessMeuPlatformKeys

TotalMessageCount

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the existing Messaging channel consent preferences are applied when
determining who receives the message. Setting this value to `true` is the most common
approach. The default value, `false`, allows you to add custom consent logic—for example,
to customize a flow to send the message to both implicitly opted-in users and explicitly
opted-in users.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
The number of messages that were successfully sent to messaging users. Delivery can occur
much later than sending, depending on factors such as the connectivity status of the recipient.
Delivery is reflected in the messaging session transcript.

**Type**
textarea

**Properties**
Nillable

**Description**
A list of IDs of the messages that were sent.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
A list of platform keys for messaging end users with messages that were sent. Available in
API version 65.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects ConversationVendorInfo

**Field** **Details**

**Description**
The number of messages that the related flow attempted to send.

This field is a calculated field.

Usage

A ConvMessageSendRequest can be generated by a flow, Apex code, or REST API call that invokes the sendConversationMessages
invocable action. Use the ConvMessageSendRequest object to query messages sent by the sendConversationMessages invocable action.

### ConversationVendorInfo

This setup object connects the partner vendor system to the Service Cloud feature. For example, for Service Cloud Voice, this object
contains information about the partner telephony or Contact Center as a Service (CCaaS) partner system. For Bring Your Own Channel
for Messaging this object contains information about the partner messaging system, and for Bring Your Own Channel for CCaaS, this
object contains information about the CCaaS partner system. This object is available in API version 52.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

This object requires an add-on license for Service Cloud Voice for Partner Telephony or Digital Engagement.

Fields

The fields in the ConversationVendorInfo object apply to all Service Cloud features unless otherwise stated in the field description. For
example, if a field applies to just one Service Cloud Voice telephony model setup or is applied differently by different partner systems,
this is stated in the field description.


Standard Objects ConversationVendorInfo


Standard Objects ConversationVendorInfo


Standard Objects ConversationVendorInfo


Standard Objects ConversationVendorInfo


Standard Objects ConversationVendorInfo


Standard Objects ConversationVendorInfo


Standard Objects ConversationVendorInfo


Standard Objects ConversationVendorInfo


Standard Objects ConversationVendorInfo


Standard Objects ConversationVendorInfo


### Standard Objects CorsWhitelistEntry CorsWhitelistEntry

Represents an entry in the cross-origin resource sharing (CORS) allowlist. Origins included in the allowlist can request REST resources
from that Salesforce org.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.

Supported Calls

`create()`, `delete()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
DeveloperName

```

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


Standard Objects CorsWhitelistEntry

**Field Name** **Details**

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance may slow while
Salesforce generates one for each record.

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

**•** Spanish (Mexico): `es_MX` Spanish (Mexico) defaults to Spanish for customer-defined
translations.

**•** Swedish: `sv`

**•** Thai: `th` The Salesforce user interface is fully translated to Thai, but Help is in English.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Primary label for the CORS allowlist entry.


Standard Objects CorsWhitelistEntry

**Field Name** **Details**

```
NamespacePrefix

UrlPattern

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
For managed packages, this field is the namespace prefix assigned to the package. For
unmanaged packages, this field is blank.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The origin URL pattern must include the HTTPS protocol (unless you’re using your localhost)
and a domain name, and can include a port. The wildcard character (*) is supported and
must be in front of a second-level domain name. For example,
`https://*.example.com` adds all subdomains of `example.com` to the allowlist.

The origin URL pattern can be an IP address. But an IP address and a domain that resolve to
the same address aren’t the same origin, and you must add them to the CORS allowlist as
separate entries.

Google Chrome [™] and Mozilla [®] Firefox [®] browser extensions are also allowed as resources in
API version 53 and later. Chrome extensions must use the prefix `chrome-extension://`
and 32 characters without digits or capital letters, for example
`chrome-extension://abdkkegmcbiomijcbdaodaflgehfffed` . Firefox
extensions must use the prefix `moz-extension://` and an 8-4-4-4-12 format of small
alphanumeric characters, for example
`moz-extension://1234ab56-78c9-1df2-3efg-4567891hi1j2` .

Cross-Origin Resource Sharing (CORS) allows web browsers to request resources from other origins. For example, using CORS, the
JavaScript for a web application at `https://www.example.com` can request a resource from
`https://www.salesforce.com` . To allow access to supported Salesforce APIs, Apex REST resources, and Lightning Out from
JavaScript code in a web browser, add the requesting origin to your Salesforce CORS allowlist.

If a browser that supports CORS makes a request to an origin in the Salesforce CORS allowlist, Salesforce returns the origin in the
`Access-Control-Allow-Origin` HTTP header, along with any additional CORS HTTP headers. If the origin isn’t included in
the allowlist, Salesforce returns HTTP status code 403.

Important: CORS doesn’t support requests for unauthenticated resources, including OAuth endpoints. You must pass an OAuth
token with requests that require it.

[CORS is a W3C recommendation to enable browsers to request resources from origins other than their own.](http://www.w3.org/TR/cors/)


### Standard Objects Coupon Coupon

A coupon associated with a promotion. This object is available in API version 54.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The Coupon object is available only if the B2B Commerce license is enabled.

Fields

**Field** **Details**

### `CouponCode`

```
CurrencyIsoCode

Description

EndDateTime

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
### Coupon code for the coupon. A buyer can use the coupon code to qualify for a promotion.

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
Description of the coupon.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects Coupon

**Field** **Details**

**Description**
The end date and time when the coupon is no longer active.

```
LastReferencedDate

LastViewedDate

Name

OwnerId

```

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

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
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the coupon.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of this coupon.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User


Standard Objects Coupon

**Field** **Details**

```
PromotionId

RedemptionLimitAllBuyers

RedemptionLimitPerBuyer

StartDateTime

Status

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the promotion associated with the coupon.

This is a relationship field.

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
Number of times this coupon can be used in total. This field is available in API version 61.0
and later.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of times this coupon can be used per customer. This field is available in API version
61.0 and later.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The start date and time when the coupon is active.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update


### Standard Objects CouponCodeRedemption

**Field** **Details**

**Description**
Status of the coupon.

Possible values are:

**•** `Active`

**•** `Inactive`

The default value is `Inactive`

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CouponChangeEvent on page 68 (API version 62.0)**
Change events are available for the object.

### CouponCodeRedemption

Tracks each coupon code redemption. This object is available in API version 58.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available through the B2B Commerce license. To access this object, the Promotions Coupon Redemption Limit user
permission must be assigned.

Fields

**Field** **Details**

```
Buyer

```

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
Information about the buyer. Can be any buyer-specific information.


Standard Objects CouponCodeRedemption

**Field** **Details**

```
CouponId

Name

OwnerId

Transaction

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the redeemed coupon.

This field is a relationship field.

**Relationship Name**
Coupon

**Relationship Type**
Lookup

**Refers To**
Coupon

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Salesforce generated coupon code, such as CCR-000000002. Can’t be edited.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who created the coupon code redemption.

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
Create, Filter, Group, idLookup, Sort

**Description**
ID of the transaction where the coupon code was redeemed. Must be a valid cart ID.


### Standard Objects CreditMemo CreditMemo

Represents a document that is used to reduce the amount that a buyer owes a seller under the terms of an earlier invoice. This object
is available in API version 48.0 and later.

A credit memo always decreases the balance of an invoice. Users can apply positive credit memos to positive invoices, for example, a
$10 credit memo reduces the balance of a $100 invoice line to $90.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,

```
   update()

```

Special Access Rules

This object is available with Order Management, Subscription Management, and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_creditmemo.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_creditmemo.htm)

Fields

**Field** **Details**

```
AppType

Balance

BillToContactId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Read-only field that indicates which Salesforce application generated the credit memo.

Possible values are:

**•** `Commerce Cloud`

**•** `Revenue Cloud`

This field is available in API versions 54.0 to 55.0

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Amount of the credit memo that's available for allocation.

**Type**
reference


Standard Objects CreditMemo

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Inherited from the account’s Bill to Account field.

This field is a relationship field.

**Relationship Name**
BillToContact

**Relationship Type**
Lookup

**Refers To**
Contact

```
BillingAccountId

CreationMode

CreditDate

```

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
The customer account associated with this credit memo.

This field is a relationship field.

**Relationship Name**
BillingAccount

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates whether the credit memo originated in Salesforce or an external system.

Possible values are:

**•** `External`

**•** `Salesforce`

This field is available in API version 55.0 and later.

**Type**
date


Standard Objects CreditMemo

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date when the credit memo was posted.

```
CreditMemoNumber

CurrencyIsoCode

Description

DocumentNumber

EffectiveDate

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
A credit memo numbering alternative to DocumentNumber, containing a number in a format
of your choice. Credit memo numbering is optional.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Three-letter ISO 4217 currency code associated with the credit memo.

The default value is USD.

This field is available in API version 55.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Description of the credit memo.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
System-generated number for organizing financial documents, for example DOC-0000123.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort


Standard Objects CreditMemo

**Field** **Details**

**Description**
Represents the effective date of the credit memo. If this field is empty, the credit date is used.
For reporting purposes only; this field drives no other logic.

This field is available in API version 55.0 and later.

```
ExternalReference

ExternalReferenceDataSource

LastReferencedDate

LastViewedDate

NetCreditsApplied

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Contains an external system’s ID for the credit memo.

This field is available in API version 55.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Contains the name of the external system that also contains the credit memo.

This field is available in API version 55.0 and later.

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
possible that this record was only referenced ( `LastReferencedDate` ) and not viewed.

**Type**
currency

**Properties**
Filter, Nillable, Sort


Standard Objects CreditMemo

**Field** **Details**

**Description**
Represents the total difference between the credit applied to and credit unapplied from the
invoice.

This field is a calculated field. This field is available in API version 55.0 and later.

```
OwnerId

ReferenceEntityId

SourceAction

```

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
The user who owns a credit memo record.

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
Filter, Group, Nillable, Sort, Update

**Description**
The ID of the record that this credit memo was generated from. For example, the order, order
summary, or invoice.

This field is a polymorphic relationship field.

**Relationship Name**
ReferenceEntity

**Relationship Type**
Lookup

**Refers To**
Invoice, Order

This field is available in API version 53.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates which Salesforce API created the credit memo.


Standard Objects CreditMemo

**Field** **Details**

Possible values are:

**•** `Invoice` —Indicates that Credit Invoice API created the credit memo and applied it
to the invoice.

**•** `NegativeInvoiceLineConversion` —Indicates that Subscription Management
created the credit memo when a negative invoice line was converted.

**•** `Standalone` —Indicates that the Credit Memo API created the credit memo.

**•** `VoidPostedInvoice` —Indicates that the Void a Posted Invoice API created the
credit memo to offset the amount that was voided on the invoice.

This field is available in API version 55.0 and later.

```
Status

TotalAdjustmentAmount

TotalAdjustmentAmountWithTax

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort, Update

**Description**
Status of the credit memo.

Possible values are:

**•** `Canceled` —Indicates that the credit memo isn't being used and doesn't have a
financial impact.

**•** `Error` —Indicates that the credit memo has an error and doesn’t have a financial impact.

**•** `Pending` —Indicates that the credit memo is being processed but hasn't yet been
posted as a financial transaction.

**•** `Posted` —The credit memo has been recorded as a financial transaction. Most fields
can’t be edited.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of `TotalAmount` values for the credit memo’s adjustment lines.

This field is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of the credit memo’s adjustment line amounts, including tax.

This field is available in API version 49.0 and later.


Standard Objects CreditMemo

**Field** **Details**

```
TotalAdjustmentTaxAmount

TotalAmount

TotalAmountWithTax

TotalChargeAmount

TotalChargeAmountWithTax

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of the credit memo’s adjustment line tax. Adjustment line balances are excluded.

This field is available in API version 49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of the credit memo’s `TotalLineAmount` and `TotalAdjustmentAmount` .

This field is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total credit memo amount, with tax included.

This field is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of `TotalAmount` values for the credit memo’s charge lines.

This field is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of the credit memo’s charge line amounts, including tax.

This field is available in API version 49.0 and later.


Standard Objects CreditMemo

**Field** **Details**

```
TotalChargeTaxAmount

TotalCreditAmountApplied

TotalCreditAmountUnapplied

 TotalTaxAmount

```

Associated Objects

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
This field is available in API version 49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Credit memo amount that's been applied to invoices.

This field is available in API version 53.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Credit memo amount that's been unapplied from invoices.

This field is available in API version 55.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of `TotalAmount` values for the credit memo’s tax lines.

This field is a calculated field.

This object has the following associated objects. If the API version isn’t specified, the associated objects are available in the same API
versions as this object. Otherwise, they’re available in the specified API version and later.

**CreditMemoFeed on page 55**
Feed tracking is available for the object.

**CreditMemoHistory on page 63**
History is available for tracked fields of the object.


### Standard Objects CreditMemoAddressGroup

**CreditMemoOwnerSharingRule on page 65**
Sharing rules are available for the object.

**CreditMemoShare on page 67**
Sharing is available for the object.

### CreditMemoAddressGroup

Stores the buyer's address information, which is used to determine the amount of tax to credit to a buyer when a credit memo is issued.
This object is available in API version 55.0 and later.

Supported Calls

`delete(), describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_creditmemoaddressgroup.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_creditmemoaddressgroup.htm)

Fields

**Field** **Details**

```
Address

City

Country

```

**Type**
address

**Properties**
Filter, Nillable

**Description**
Buyer’s address.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Buyer's city.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects CreditMemoAddressGroup

**Field** **Details**

**Description**
Buyer's country.

```
CreditMemoAddressGroupNumber

CreditMemoId

CurrencyIsoCode

GeocodeAccuracy

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated number, such as 0000123, that represents the address group.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the credit memo associated with the address group.

This field is a relationship field.

**Relationship Name**
CreditMemo

**Relationship Type**
Lookup

**Refers To**
CreditMemo

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Three-letter ISO 4217 currency code associated with the credit memo.

The default value is USD.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The accuracy rating for the geocode of the address group. An accuracy rating contains
information about the location of a latitude and longitude.

Possible values are:

**•** `Address`


Standard Objects CreditMemoAddressGroup

**Field** **Details**

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
LastReferencedDate

LastViewedDate

Latitude

Longitude

PostalCode

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this address group.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this address group.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Latitude of the buyer’s address.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Longitude of the buyer’s address.

**Type**
string


### Standard Objects CreditMemoInvApplication

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The buyer’s postal code or ZIP code.

```
State

Street

```

Associated Objects

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The buyer’s state.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
The buyer’s street number and name.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CreditMemoAddressGroupHistory on page 63**
History is available for tracked fields of the object.

### CreditMemoInvApplication

Represents an amount applied from a credit memo to an invoice. This object is available in API version 48.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,

```
update()

```

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_creditmemoinvapplication.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_creditmemoinvapplication.htm)


Standard Objects CreditMemoInvApplication

Fields

**Field** **Details**

```
Amount

AppliedDate

AssociatedLineId

CreditMemoBalance

```

**Type**
currency

**Properties**
Filter, Sort

**Description**
The amount of the credit memo that was applied to or unapplied from the invoice.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the credit memo was applied. If the credit memo invoice application's type
is `Unapplied`, this value is inherited from the Applied date of the credit memo referenced
in the AssociatedLineId.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
For a credit memo invoice application that represents an unapplied credit memo, this field
shows the original credit memo invoice application.

This field is a relationship field.

**Relationship Name**
AssociatedLine

**Relationship Type**
Lookup

**Refers To**
CreditMemoInvApplication

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The balance of a credit memo after a credit memo is applied or unapplied. This field is a
snapshot of the credit memo's balance after the action. It isn't updated after further changes
to the credit memo balance.


Standard Objects CreditMemoInvApplication

**Field** **Details**

```
CreditMemoId

CreditMemoInvoiceNumber

Date

Description

EffectiveDate

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The credit memo that was applied or unapplied.

This field is a relationship field.

**Relationship Name**
CreditMemo

**Relationship Type**
Lookup

**Refers To**
CreditMemo

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Number of the invoice to which a credit memo is applied.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date when the credit memo amount was applied to the invoice.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Description of the credit applied to an invoice.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects CreditMemoInvApplication

**Field** **Details**

**Description**
The effective date of the application or unapplication of credit. Users can provide this value
when applying or unapplying the credit memo. This field is optional and provided only for
reporting purposes. It doesn't affect the credit memo invoice application's other fields.

```
HasBeenUnapplied

ImpactAmount

InvoiceBalance

InvoiceId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Shows whether this credit memo application has been unapplied from the target invoice.

Possible values are:

**•** `NA`

**•** `No`

**•** `Yes`

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The net adjustment to the invoice's balance after a credit memo is applied or unapplied. If
a credit memo was applied, this value is the negative version of the credit memo invoice
application's `Amount` . If a credit memo was unapplied, this value is the positive version of
the credit memo invoice application's `Amount` .

This field is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The balance of the credit memo after a credit memo is applied or unapplied. This field is a
snapshot of the credit memo's balance after the action. It isn't updated after further changes
to the credit memo balance.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the invoice to which credit is applied.


### Standard Objects CreditMemoLine

**Field** **Details**

This field is a relationship field.

**Relationship Name**
Invoice

**Relationship Type**
Lookup

**Refers To**
Invoice

```
Type

UnappliedDate

```

Associated Objects

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Indicates whether the credit memo line application was generated because of an apply
action (application) or an unapply action (unapplication).

Possible values are:

**•** `Applied`

**•** `Unapplied`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when this application was unapplied from the target invoice.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CreditMemoInvApplicationFeed on page 55**
Feed tracking is available for the object.

**CreditMemoInvApplicationHistory on page 63**
History is available for tracked fields of the object.

### CreditMemoLine

Represents product, service, adjustment, or tax line items that were included in a credit memo. This object is available in API version 48.0
and later.


Standard Objects CreditMemoLine

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,

```
   update()

```

Special Access Rules

This object is available with Order Management, Subscription Management, and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_creditmemoline.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_creditmemoline.htm)

Fields

**Field** **Details**

```
AdjustmentAmount

AdjustmentAmountWithTax

AdjustmentTaxAmount

BillingAddressId

```

**Type**
currency

**Properties**
Filter, Nillable, Sort, Update

**Description**
Amount of this credit memo line item if its type is Adjustment.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of the adjustment amount and the adjustment tax amount.

This field is available in API version 49.0 and later. This field is available when Subscription
Management is enabled.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Amount of the tax related to the adjustment amount.

This field is available in API version 55.0 and later. This field is available when Subscription
Management is enabled.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects CreditMemoLine

**Field** **Details**

**Description**
ID of the billing address related to this credit memo line.

This field is a relationship field. This field is available in API version 55.0 and later. This field is
available when Subscription Management is enabled.

**Relationship Name**
BillingAddress

**Relationship Type**
Lookup

**Refers To**
CreditMemoAddressGroup

```
ChargeAmount

ChargeAmountWithTax

ChargeTaxAmount

CreditMemoId

```

**Type**
currency

**Properties**
Filter, Nillable, Sort, Update

**Description**
Amount of this credit memo line item if its type is Charge.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of the adjustment amount and the adjustment tax amount.

This field is available in API version 55.0 and later. This field is available when Subscription
Management is enabled.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Amount of the tax related to the charge amount.

This field is available in API version 55.0 and later. This field is available when Subscription
Management is enabled.

**Type**
reference

**Properties**
Filter, Group, Sort


Standard Objects CreditMemoLine

**Field** **Details**

**Description**
ID of the parent credit memo.

This field is a relationship field.

**Relationship Name**
CreditMemo

**Relationship Type**
Lookup

**Refers To**
CreditMemo

```
CurrencyIsoCode

Description

EndDate

LineAmount

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Three-letter ISO 4217 currency code associated with the credit memo line.

The default value is USD.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Description of the credit memo line.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
For credit memos made from a time-based service, the end date of the line item being
credited.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Amount of the credit memo line.

This field is a calculated field. This field is available in API version 49.0 and later.


Standard Objects CreditMemoLine

**Field** **Details**

```
Name

Product2Id

ReferenceEntityItemId

ReferenceEntityItemType

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort, Update

**Description**
Name of the credit memo line.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The product or service being credited in the credit memo line.

This field is a relationship field.

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The order product or invoice line corresponding to this credit memo line.

This field is a polymorphic relationship field. This field is available in API version 53.0 and
later.

**Relationship Name**
ReferenceEntityItem

**Relationship Type**
Lookup

**Refers To**
OrderItemSummary, OrderProduct, InvoiceLine

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects CreditMemoLine

**Field** **Details**

**Description**
The type of transaction that generated the credit memo line.

Possible values are:

**•** `DeliveryCharge`

**•** `OrderProduct`

```
ReferenceEntityItemTypeCode

RelatedLineId

ShippingAddressId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of object that generated the credit memo line.

Possible values are:

**•** `Charge`

**•** `Product`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The credit memo line related to this line item.

This field is a relationship field.

**Relationship Name**
RelatedLine

**Relationship Type**
Lookup

**Refers To**
CreditMemoLine

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the shipping address.

This field is a relationship field. This field is available in API version 55.0 and later. This field is
available when Subscription Management is enabled.

**Relationship Name**
ShippingAddress


Standard Objects CreditMemoLine

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
CreditMemoAddressGroup

```
StartDate

Status

TaxAmount

TaxCode

TaxDocumentNumber

```

**Type**
date

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
For credit memo lines generated from a time-based service, the first date of the billing for
the service.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
State of the credit memo line. Inherited from the credit memo.

**Type**
currency

**Properties**
Filter, Nillable, Sort, Update

**Description**
Total tax for the credit memo.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The code used to calculate the tax rate for the invoice line.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The document number that tracks taxes calculated for this credit memo line.


Standard Objects CreditMemoLine

**Field** **Details**

This field is available in API version 55.0 and later. This field is available when Subscription
Management is enabled.

```
TaxEffectiveDate

TaxName

TaxRate

TotalAmount

TotalAmountWithTax

TaxStatus

```

**Type**
date

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The date used to calculate the credit memo line’s `TaxAmount` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
User-defined name for applied tax.

**Type**
percent

**Properties**
Filter, Nillable, Sort, Update

**Description**
Percentage value used for calculating tax.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total amount of the credit memo line before any applicable tax.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of tax for this credit memo line, with tax included. Sum of TotalAmount and
TaxAmount.

**Type**
picklist


Standard Objects CreditMemoLine

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Tracks whether the taxes were calculated for this credit memo line.

Possible values are:

**•** `Complete`

**•** `Error`

**•** `None`

The default value is None. This field is available in API version 55.0 and later. This field is
available when Subscription Management is enabled.

```
TaxTransactionNumber

TaxTreatmentId

Type

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Tracks the transaction number of the tax calculated for this credit memo line. This field is
available in API version 55.0 and later. This field is available when Subscription Management
is enabled.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the tax treatment for the credit memo line.

This field is a relationship field. This field is available in API version 55.0 and later. This field is
available when Subscription Management is enabled.

**Relationship Name**
TaxTreatment

**Relationship Type**
Lookup

**Refers To**
TaxTreatment

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of transaction for the invoice line.


### Standard Objects Crisis

**Field** **Details**

Possible values are:

**•** `Adjustment`

**•** `Charge`

**•** `Tax`

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CreditMemoLineFeed on page 55**
Feed tracking is available for the object.

**CreditMemoLineHistory on page 63**
History is available for tracked fields of the object.

### Crisis

Represents a major crisis event that affects an Employee in an InternalOrganizationUnit. This object is available in API version 48.0 and
later. In API version 49.0 and later, this object supports reports, criteria-based sharing rules, and history tracking, plus you can exclude
individual fields from custom page layouts.

Work.com uses this object to track and describe crisis situations.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

To access this object, you must be assigned a Workplace Command Center permission set license and the Provides access to Workplace
Command Center features system permission.

Fields

**Field** **Details**

### `CrisisType`

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The type or category of crisis.


Standard Objects Crisis

**Field** **Details**

Possible values are:

**•** `Economic Crisis`

**•** `Natural Disaster`

**•** `Pandemic`

**•** `War`

```
Description

EndDate

LastReferencedDate

LastViewedDate

Name

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The crisis description.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date the crisis ended.

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
Required. The crisis record name.


### Standard Objects CronJobDetail

**Field** **Details**

```
OwnerId

StartDate

```

Associated Objects

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who currently owns this record. Default value is the user logged in to the
API to perform the create operation.

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The date the crisis started.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**CrisisHistory (API version 49.0)**
History is available for tracked fields of the object.

**CrisisOwnerSharingRule**

Sharing rules are available for the object.

**CrisisShare (API version 49.0)**
Sharing is available for the object.

SEE ALSO:

_[Workplace Command Center for Work.com Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.ajax.meta/workdotcom_dev_guide/wdc_cc_overview.htm)_ : Extend Work.com with Custom Solutions

### CronJobDetail

Contains details about the associated scheduled job, such as the job’s name and type. This object is available in API version 29.0 and
later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`


### Standard Objects CronTrigger

Fields

**Field** **Details**

```
JobType

Name

```

Usage

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of the associated scheduled job. The following are the available job types. Use the
job type value when querying for a specific job type.

**•** `1` —Data Export

**•** `3` —Dashboard Refresh

**•** `4` —Reporting Snapshot

**•** `6` —Scheduled Flow

**•** `7` —Scheduled Apex

**•** `8` —Report Run

**•** `9` —Batch Job

**•** `A` —Reporting Notification

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the associated scheduled job.

Use this object to query additional information about a scheduled job, such as the job’s name and type.

### CronTrigger

Contains schedule information for a scheduled job. CronTrigger is similar to a cron job on UNIX systems. This object is available in API
version 17.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`


Standard Objects CronTrigger

Fields

**Field** **Details**

```
CronExpression

CronJobDetailId

EndTime

NextFireTime

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The cron expression used to initiate the schedule.

Syntax:

```
  Seconds Minutes Hours Day_of_month Month Day_of_week

  Optional_year

```

See `[schedule(jobName, cronExpression, schedulableClass)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexref/apex_methods_system_system.htm)` in the
_Apex Reference Guide_ .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the CronJobDetail record containing more details about this scheduled job.

This is a relationship field.

**Relationship Name**
CronJobDetail

**Relationship Type**
Lookup

**Refers To**
CronJobDetail

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the job either finished or will finish.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects CronTrigger

**Field** **Details**

**Description**
The next date and time the job is scheduled to run. `null` if the job is not scheduled to run
again.

```
OwnerId

PreviousFireTime

StartTime

State

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Owner of the job.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The most recent date and time the job ran. `null` if the job has not run before current local
time.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the most recent iteration of the scheduled job started.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The current state of the job. The job state is managed by the system. Possible values are:

**•** `WAITING` —The job is waiting for execution.

**•** `ACQUIRED` —The job has been picked up by the system and is about to execute.

**•** `EXECUTING` —The job is executing.

**•** `COMPLETE` —The trigger has fired and is not scheduled to fire again.

**•** `ERROR` —The trigger definition has an error.

**•** `DELETED` —The job has been deleted.

**•** `PAUSED` —A job can have this state during patch and major releases. After the release
has finished, the job state is automatically set to `WAITING` or another state.


### Standard Objects CryptoProdCatgWalletGroup

**Field** **Details**

**•** `BLOCKED` —Execution of a second instance of the job is attempted while one instance
is running. This state lasts until the first job instance is completed.

**•** `PAUSED_BLOCKED` —A job has this state due to a release occurring. When the release
has finished and no other instance of the job is running, the job’s status is set to another
state.

```
TimesTriggered

TimeZoneSidKey

```

Usage

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times this job has been triggered.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Returns the timezone ID. For example, `America/Los_Angeles` .

Use this object to query scheduled jobs in your organization.

### CryptoProdCatgWalletGroup

Specifies if CryptoWalletGroup is in the allowlist or airdrop for the ProductCategory. A custom object between ProductCategory and
CryptoWalletGroup adding the CryptoWalletGroup to allowlist or airdrop. This object is available in API version 58.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object has read, create, update, delete, modify all, and view all access.


Standard Objects CryptoProdCatgWalletGroup

Fields

**Field** **Details**

```
CryptoWalletGroupId

LastReferencedDate

LastViewedDate

Name

ProductCategoryId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The CryptoWalletGroup ID.

This field is a relationship field.

**Relationship Name**
CryptoWalletGroup

**Relationship Type**
Lookup

**Refers To**
CryptoWalletGroup

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
and `LastReferenceDate` is not null, the user accessed this record or list view indirectly.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the record.

**Type**
reference


### Standard Objects CspTrustedSite

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the category.

This field is a relationship field.

**Relationship Name**
ProductCategory

**Relationship Type**
Lookup

**Refers To**
ProductCategory

```
Status

Type

### CspTrustedSite

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies if CryptoProdCatgWalletGroup is active and functional, or inactive and disabled.

Possible values are:

**•** `Active`

**•** `Inactive`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Determines whether the list of wallets is for minting allowlist or for executing an airdrop.

Possible values are:

**•** `Airdrop`

**•** `Allowlist`

Represents a trusted URL. For each CspTrustedSite, you can specify Content Security Policy (CSP) directives and permissions policy
directives. Each CSP directive allows Lightning components, third-party APIs, and WebSocket connections to access a resource type
from the trusted URL. If the Permissions-Policy HTTP header is enabled, each permissions policy directive grants the trusted URL access
to a browser feature. In API version 58.0 and earlier, CspTrustedSite included only CSP directives and was referred to as CSP Trusted Sites
in Salesforce Setup. Available in API version 39.0 and later.


Standard Objects CspTrustedSite

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CanAccessCamera

CanAccessMicrophone

Context

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this CspTrustedSite can access the user’s camera. The default value is
`false` .

This field takes effect only when the `enablePermissionsPolicy` field equals `true`
and the `grantCameraAccess` field equals `TrustedUrls` in the SecuritySettings
metadata API type.

This field is available in API version 59.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this CspTrustedSite can access the user’s microphone. The default value
is `false` .

This field takes effect only when the `enablePermissionsPolicy` field equals `true`
and the `grantMicrophoneAccess` field is `TrustedUrls` in the SecuritySettings
metadata API type.

This field is available in API version 59.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Declares the scope of the CSP directives for this trusted URL.

Possible values are:

**•** `All` —Apply the CSP directives to all supported context types.

**•** `Communities` —Apply the CSP directives to Experience Builder sites only.

**•** `FieldServiceMobileExtension` —Apply the CSP directives to the Field Service
Mobile Extensions only.


Standard Objects CspTrustedSite

**Field** **Details**

**•** `LEX` —Apply the CSP directives to Lightning Experience only.

**•** `LightningOut` —Reserved for future use. Available in API version 64.0 and later

**•** `VisualForce` —Apply the CSP directives to custom Visualforce pages only. This value
is available in API version 55.0 and later.

For custom Visualforce pages, content is restricted to trusted URLs only if the page’s
`cspHeader` attribute is set to `true` .

This field is available in API version 44.0 and later.

```
Description

DeveloperName

EndpointUrl

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the trusted URL. Limit: 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The developer name of the trusted URL.

Only users with View DeveloperName OR View Setup and Configuration permission can
view, group, sort, and filter this field.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The URL for this CspTrustedSite.

This field must include a domain name and can include a port. For example,
`https://example.com` or `https://example.com:8080` .

To reduce repetition, you can use the wildcard character `*` (asterisk). For example,
`*.example.com` . For a third-party API, the URL must begin with https://. For example,
`https://example.com` . For a WebSocket connection, the URL must begin with wss://.
For example, `wss://example.com` .

Otherwise, the URL cannot be malformed. Examples of malformed URLs that fail a syntax
check are `malformed^url.example.com`, and
`https://{subdomain}.example.com` .

To add a URL based on parameters, build the URL before you update the `EndpointUrl`
field.


Standard Objects CspTrustedSite

**Field** **Details**

```
IsActive

IsApplicableToConnectSrc

IsApplicableToFontSrc

IsApplicableToFrameSrc

IsApplicableToImgSrc

IsApplicableToMediaSrc

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this CspTrustedSite is active.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether Lightning components, third-party APIs, and WebSocket connections can
load URLs using script interfaces from this trusted URL.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether Lightning components, third-party APIs, and WebSocket connections can
load fonts from this trusted URL.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether Lightning components, third-party APIs, and WebSocket connections can
load resources contained in `<iframe>` elements from this trusted URL.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether Lightning components, third-party APIs, and WebSocket connections can
load images from this trusted URL.

**Type**
boolean


Standard Objects CspTrustedSite

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether Lightning components, third-party APIs, and WebSocket connections can
load audio and video from this trusted URL.

```
IsApplicableToStyleSrc

Language

MasterLabel

NamespacePrefix

```

Usage

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether Lightning components can load style sheets from this trusted URL.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language for the trusted URL.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Master label for this trusted URL.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Namespace prefix for this trusted URL.

For each CSPTrustedSite, at least one field starting with `grantAccess` or `isApplicableTo` must be set to `true` .

In API versions 50.0 to 58.0, if all `isApplicable` fields are `false`, the `isApplicableToImgSrc` field is set to `true` . In API
version 49.0 and earlier, if all `isApplicable` fields are `false`, those fields all default to `true` .


### Standard Objects CspViolationEventLog

To ensure smooth integration across Salesforce products, Salesforce includes URLs in each of the CSP directives that correspond to the
`isApplicable` fields, even though those URLs aren’t defined as CspTrustedSite components. Salesforce regularly updates those
URLs based on the latest requirements.

### CspViolationEventLog

CSP violation events capture details about blocked resource requests from Lightning Experience pages based on your content security
policy (CSP). This object is available in API version 63.0 and later.

This event is free for all customers with a 24-hour data retention period. The CSP violation event is available in the API but not in the
Event Monitoring Analytics app.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
BlockedUri

BlockedUriDomain

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The full string of the blocked resource. If the call to the blocked resource used a URL,
`BLOCKED_URI` is the full URL. Or,for violations with a `DIRECTIVE` of `script-src`
directives, `inline` or `eval` .

**Examples**

**•** https://www.example.com/images/picture.png

**•** file://host1:0002/media/video.mp4

**•** inline

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects CspViolationEventLog

**Field** **Details**

**Description**
If `BLOCKED_URI` is a URL, the domain for that URL. To allow resources to be loaded from
the `BLOCKED_URI`, `BLOCKED_URI_DOMAIN` is the `endpointUrl` value to add or
[update in the CspTrustedSite Metadata API.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_csptrustedsite.htm)

```
ColumnNumber

Context

Directive

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The column number in the document or worker script at which the violation occurred. This
value is relevant only when `DIRECTIVE` is `script-src` .

For those violations, use this value with `LINE_NUMBER` to identify the location of the
violation.

**Example**

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The content security policy (CSP) context for the request. The CSP context controls which
[pages can load content from a CspTrustedSite.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_csptrustedsite.htm)

CSP violation events capture details about blocked resource requests from only Lightning
Experience pages, this value is always `Lightning` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The CSP directive that blocked the resource request.

**Possible Values**

**•** `font-src`

**•** `frame-src`

**•** `img-src`

**•** `media-src`

**•** `style-src`

**•** `script-src`


Standard Objects CspViolationEventLog

**Field** **Details**

[For information on these directives and a full list of all CSP directives, see MDN Web Docs:](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy)
[Content-Security-Policy.](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy)

```
Disposition

LineNumber

RequestIdentifier

ResourceSample

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The CSP violation handling instruction for the user agent at the time of the violation.

**Possible Values**

**•** `enforce` —Enforce the policy violation. For violations with this `DISPOSITION`, the
resource request was blocked.

**•** `report` —Report the policy violation. For violations with this `DISPOSITION`, the
resource request wasn’t blocked, but the violation was reported.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The line number in the document or worker script at which the violation occurred. This value
is relevant only when `DIRECTIVE` is `script-src` . For those violations, use this value
with `COLUMN_NUMBER` to identify the location of the violation.

**Example**

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
A sample of the resource that caused the violation, usually the first 40 characters, or the
empty string.


Standard Objects CspViolationEventLog

**Field** **Details**

```
Source

SourceFile

Timestamp

UniqueIdentifier

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The page where this CSP violation originated. For example, if your CSP policy prevented an
image from loading on a Visualforce page, `SOURCE` contains the URL of that page.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URL of the script in which the violation occurred. If the violation didn’t occur in a script,
`SOURCE_FILE` is null.

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
A string identifier for the CSP violation.

Only one CSP violation event log file is available at a time. When the daily incremental event log file is generated during the daily
background process, the new file replaces the existing file.

If the event log file doesn’t exist, either the log generation process hasn’t run yet or there’s no violation data to report for that 24-hour
window. The event log file is generated only when at least one violation occurred for the day.

To collect CSP violation logs for multiple days, schedule a daily query of the CSP Violation event type via REST API. For example, you can
configure a cron job in Unix or a scheduled task in Windows to run the query.


### Standard Objects CurrencyType CurrencyType

Represents the currencies used by an organization for which the multicurrency feature is enabled.

Supported Calls

`create()`, `describeSObjects()`, `getUpdated()`, `query()`, `retrieve()`, `search()`, `update()`

Special Access Rules

**•** This object is not available in single-currency organizations.

**•** You need the “Customize Application” permission to edit this object.

**•** Your client application can't delete this object.

Fields

**Field** **Details**

```
ConversionRate

DecimalPlaces

IsActive

IsCorporate

```

**Type**
double

**Properties**
Filter

**Description**
Required. Conversion rate of this currency type against the corporate currency.

**Type**
int

**Properties**
Filter

**Description**
Required. For this currency, specifies the number of digits to the right of the decimal
point, such as zero ( `0` ) for JPY or `2` for USD.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether this currency type is active ( `true` ) or not ( `false` ). Inactive
currency types do not appear in picklists in the user interface. Label is **Active** . This
field defaults to `false` if no value is provided when updating or inserting a record.

**Type**
boolean


### Standard Objects CustExpIntlTransfSetup

**Field** **Details**

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether this currency type is the corporate currency ( `true` ) or not ( `false` ).
Label is **Corporate Currency** . All other currency conversion rates are applied against
this corporate currency. If a currency is already defined as the corporate currency in
the user interface, it can't be unset. When a non-corporate currency is set to a
corporate currency, the system reconfigures all conversion rates based on the new
corporate currency.

```
 IsoCode

```

Usage

**Type**
picklist

**Properties**
Filter, Restricted picklist

**Description**
Required. ISO code of the currency. Must be one of the valid alphabetic, three-letter
currency ISO codes defined by the ISO 4217 standard, such as `USD`, `GBP`, or `JPY` .
Must be unique within your organization. Label is **Currency ISO Code** .

This object is for multicurrency organizations only. Use this object to define the currencies your organization uses.

When updating an existing record, make sure to provide values for all fields to avoid undesired changes to the CurrencyType. For example,
if a value for `IsActive` is not provided, the default ( `false` ) is used, which could result in a currently active CurrencyType becoming
inactive.

SEE ALSO:

DatedConversionRate

Overview of Salesforce Objects and Fields

### CustExpIntlTransfSetup

Stores information for different data sources that are processed for customer insights. This object is available in API version 65.0 and
later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`


Standard Objects CustExpIntlTransfSetup

Fields

**Field** **Details**

```
DataSourceChannelName

DataSourceChannelType

IsDataProcessingPaused

IsEnabled

LastReferencedDate

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the associated communication channel, such as Web, Email, Chat, or Voice.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Specifies the channel type as standard or custom.

Possible values are:

**•** `Custom`

**•** `Standard`

The default value is `Standard` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether data processing for the channel is temporarily paused ( `true` ). Use this
field to control channel operations without deactivating the channel.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the channel is active for processing data ( `true` ).

The default value is `false` .

**Type**
dateTime


### Standard Objects CustomBrand

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when the current user last viewed or modified this record, a record related
to this record, or a list view. If this value is null, the current user has never viewed or modified
a record related to this object.

```
LastViewedDate

Name

ProcessingStartDate

### CustomBrand

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when the current user last viewed or modified this record. If this value is null,
the current user has never viewed or modified this record.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the Customer Experience Intelligence Transformer Setup record.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date to start processing data in the specified communication channel.

Represents a custom branding and color scheme. This object is available in API version 28.0 and later.

Supported Calls

`create()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

This object is available only when your org has digital experiences enabled.


### Standard Objects CustomBrandAsset

Fields

**Field Name** **Details**

```
ParentId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the parent entity that this branding applies to. The parent entity can
be an Experience Cloud site, organization, topic, or reputation level.

The branding applies to the entity that the `ParentId` references. For example,
if the `ParentId` references a network ID, the branding applies to that
Experience Cloud site only, and if the `ParentId` references an organization
ID, the branding applies to the organization that it is accessed through, and so
on. Label is `Branded Entity ID` .

Use this object along with CustomBrandAsset to apply a custom branding scheme to your Experience Cloud site. The branding scheme
for the site shows in both the user interface and in the Salesforce mobile app. You must have Create and Manage Experiences to customize
site branding.

You can also use this object to apply a custom branding scheme to your org when it is accessed through the Salesforce mobile app.

SEE ALSO:

Network

### CustomBrandAsset

Represents a branding element in a custom branding scheme. For example, a color, logo image, header image, or footer text. A
### CustomBrandAsset can apply to an Experience Cloud site or to an org using the Salesforce mobile app. This object is available in API

version 28.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

This object is available only when your org has digital experiences enabled.


Standard Objects CustomBrandAsset

Fields

**Field Name** **Details**

```
AssetCategory

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

Values include:

**•** `MotifZeronaryColor` —The background color for the header. Label
is `Zeronary motif color` .

If this CustomBrandAsset is for a network, this is the header color for the
network. If it is for an org, this is the header color when users access the
Salesforce mobile app.

**•** `MotifPrimaryColor` —The color used for the active tab. Label is
`Primary motif color` .

Not used for the Salesforce mobile app branding.

**•** `MotifSecondaryColor` —The color used for the top borders of lists
and tables. Label is `Secondary motif color` .

Not used for the Salesforce mobile app branding.

**•** `MotifTertiaryColor` —The background color for section headers on
edit and detail pages. Label is `Tertiary motif color` .

Not used for the Salesforce mobile app branding.

**•** `MotifQuaternaryColor` —If this CustomBrandAsset is for a network,
this is the background color for network pages. If it is for an org, this is the
background color on a splash page. Label is `Quaternary motif`
`color` .

**•** `MotifZeronaryComplementColor` —Font color used with
`zeronaryColor` . Label is `Zeronary motif colors`
`complement color` .

**•** `MotifPrimaryComplementColor` —Font color used with
`primaryColor` . Label is `Primary motif colors complement`
`color` .

Not used for the Salesforce mobile app branding.

**•** `MotifTertiaryComplementColor` —Font color used with
`tertiaryColor` . Label is `Tertiary motif colors`
`complement color` .

Not used for the Salesforce mobile app branding.


Standard Objects CustomBrandAsset

**Field Name** **Details**

**•** `MotifQuaternaryComplementColor` —Font color used with
`quaternaryColor` . Label is `Quaternary motif colors`
`complement color` .

Not used for the Salesforce mobile app branding.

**•** `PageHeader` —An image that appears on the header of the pages. Can
be an .html, .gif, .jpg, or .png file. Label is `Page Header` .

Not used for the Salesforce mobile app branding.

**•** `PageFooter` —An image that appears on the footer of the pages. Must
be an .html file. Label is `Page Footer` .

Not used for the Salesforce mobile app branding.

**•** `LoginFooterText` —The text that appears in the footer of the login
page. Label is `Footer text displayed on the login page` .

Not used for the Salesforce mobile app branding.

**•** `LoginLogoImageId` —The logo that appears on the login page for
external users. In the Salesforce mobile app, this logo also appears on the
Experience Cloud site splash page. Label is `Logo image displayed`
`on the login page` .

**•** `LargeLogoImageId` —Only used for the Salesforce mobile app. The
logo that appears on the splash page when you start the Salesforce mobile
app. Label is `Large logo image` .

**•** `SmallLogoImageId` —Only used for the Salesforce mobile app. The
logo that appears on the publisher in the Salesforce mobile app. Label is
`Small logo image` .

**•** `StaticLogoImageURL` —The logo that appears on the login page for
external users. Label is `Static logo image url` .

**•** `LoginQuaternaryColor` —The background color that appears on the
Experience Cloud site login page for external users. Label is `Login`
`background color` .

**•** `LoginRightFrameUrl` —The URL to the contents that appears on right
side of the Experience Cloud site login page for external users. Label is `Login`
`right frame url` .

**•** `LogoAssetId` —Navigation tile menu item images. Label is `Logo`
`asset image` .

**•** `LoginPrimaryColor` —The background color of the login button. Label
is `Login primary color` .

**•** `LoginBackgroundImageUrl` —The path to the image URL that
appears as the background on the Experience Cloud site’s login page. Label
is `Background image url` .

**•** `LargeLogoAssetId` —Navigational topic images. Label is `Large`
`logo asset image` .


Standard Objects CustomBrandAsset

**Field Name** **Details**

**•** `MediumLogoAssetId` —Featured topic images. Label is `Medium`
`logo asset image` .

```
AssetSourceId

CustomBrandId

ForeignKeyAssetId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

ID of the document uploaded to the Documents folder if the value of
`AssetCategory` is:

**•** `PageHeader`

**•** `PageFooter`

**•** `LoginLogoImageId`

**•** `LargeLogoImageId`

**•** `SmallLogoImageId`

ID of the content asset if the value of the `AssetCategory` is:

**•** `LogoAssetId`

**•** `LargeLogoAssetId`

**•** `MediumLogoAssetId`

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the associated CustomBrand .

This is a relationship field.

**Relationship Name**
CustomBrand

**Relationship Type**
Lookup

**Refers To**
CustomBrand

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects CustomFieldDisplayValue

**Field Name** **Details**

**Description**

This field was removed in API version 41.0, and is available in earlier versions for
backward compatibility only. Use `AssetSourceId` instead.

ID of the document used if the value of `AssetCategory` is `PageHeader`,
`PageFooter`, or `LoginLogoImageId` .

```
TextAsset

```

Usage

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Text used if the `AssetCategory` is `LoginFooterText` .

Use this object to add basic branding elements—color scheme, header or footer images, login page logo, or footer text—to the branding
scheme ( CustomBrand ) for your Experience Cloud site. You must have Create and Manage Experiences to customize site branding.

If you’re using digital experiences in the Salesforce mobile app, the loading page shows the logo.

SEE ALSO:

Network

### CustomFieldDisplayValue

Stores variation details for the product attribute item view. This object is available in API version 63.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

### CustomFieldDisplayValue is available only if the B2B or D2C Commerce license is enabled.


Standard Objects CustomFieldDisplayValue

Fields

**Field** **Details**

```
Color

CurrencyIsoCode

CustomFieldDisplayId

Name

PickListApiValue

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The color variation in hexadecimal value format, for example `#FF0000` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The currency ISO code allowed by the organization. Possible value is:

**•** `USD` —U.S. Dollar

The default value is `USD` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the custom field display that this variation is associated with.

This field is a relationship field.

**Relationship Name**
CustomFieldDisplay

**Refers To**
CustomFieldDisplay

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the custom field display value.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


### Standard Objects CustomHelpMenuItem

**Field** **Details**

**Description**
The API name of the color variation picklist value, for example, `red_c` .

Usage

This object only gets populated when display type in the CustomFieldDisplay object is ColorSwatch.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as
CustomFieldDisplayValue.

**CustomFieldDisplayValueChangeEvent on page 68**
Change events are available for the object.

**CustomFieldDisplayValueFeed on page 55**
Feed tracking is available for the object.

**CustomFieldDisplayValueHistory on page 63**
History is available for tracked fields of the object.

### CustomHelpMenuItem

Represents the items within a section of the Lightning Experience help menu that the admin added to display custom, org-specific help
resources. This object is available in API version 44.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Packaging Considerations

Although you can package custom Help Menu section information, the section won't appear in the Help Menu Setup page or the Help
Menu user interface of orgs where the package is installed. Instead, customers must view the data in the CustomHelpMenuItem and
CustomHelpMenuSection objects and then manually add resources on the Help Menu Setup page.

Fields

**Field** **Details**

```
LinkUrl

```

**Type**
url

**Properties**
Create, Filter, Sort, Update


### Standard Objects CustomHelpMenuSection

**Field** **Details**

**Description**
Required. The URL for the resource. Specify up to 1,000 characters.

```
MasterLabel

ParentId

SortOrder

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The name of the resource. Specify up to 100 characters.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the custom help section the item belongs to.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
### CustomHelpMenuSection

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The order of the item within the custom section. Valid values are 1 through 15.

### CustomHelpMenuSection

Represents a section of the Lightning Experience help menu that the admin added to display custom, org-specific help resources. This
object is available in API version 44.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects CustomHelpMenuSection

Packaging Considerations

Although you can package custom Help Menu section information, the section won't appear in the Help Menu Setup page or the Help
Menu user interface of orgs where the package is installed. Instead, customers must view the data in the CustomHelpMenuItem and
CustomHelpMenuSection objects and then manually add resources on the Help Menu Setup page.

Fields

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
The unique name of the custom help section in the API. This name can contain only
underscores and alphanumeric characters and must be unique in your organization. It must
begin with a letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. The label corresponds to section title in the user interface. Limit:
80 characters.

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

**•** da (Danish)

**•** de (German)

**•** en_US (English)

**•** es (Spanish)

**•** es_MX (Spanish (Mexico))

**•** fi (Finnish)

**•** fr (French)

**•** it (Italian)

**•** ja (Japanese)

**•** ko (Korean)

**•** nl_NL (Dutch)


### Standard Objects CustomHttpHeader

**Field** **Details**

**•** no (Norwegian)

**•** pt_BR (Portuguese (Brazil))

**•** ru (Russian)

**•** sv (Swedish)

**•** th (Thai)

**•** zh_CN (Chinese (Simplified))

**•** zh_TW (Chinese (Traditional))

```
MasterLabel

NamespacePrefix

### CustomHttpHeader

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The name of the resource. Specify up to 100 characters.

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

Represents a custom HTTP header that provides context information from Salesforce such as region, org details, or the role of the person
viewing the external object. This object is available in API version 43.0 and later.


Standard Objects CustomHttpHeader

Supported Calls

`describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

As of Spring ’20 and later, only authenticated internal and external users can access this object.

Fields

**Field Name** **Details**

```
Description

HeaderFieldName

HeaderFieldValue

IsActive

ParentId

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
A text description of the header field’s purpose.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Name of the header field. The name must contain at least one alphanumeric character or
underscore. It can also include: ! # $ % & ' * + - . ^ _ ` | ~

**Type**
string

**Properties**
Filter, Sort

**Description**
A formula that resolves to the value for the header. The values in the formula must evaluate
to a string. If the formula resolves to null and an empty string, the header isn’t sent.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the custom HTTP header is available to use.

**Type**
reference


### Standard Objects CustomMsgChannel

**Field Name** **Details**

**Properties**
Filter, Group, Sort

**Description**
ID of the entity that the custom HTTP header is related to.

This is a polymorphic relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
ExternalDataSource, NamedCredential

Usage

For each OData external data source, define up 10 HTTP headers to request data.

Note: HTTP headers aren’t supported on named credentials.

### CustomMsgChannel

Represents a custom conversation channel and stores event-driven Messaging settings. Custom conversation channels are implemented
for Bring Your Own Channel for Messaging and Bring Your Own Channel for CCaaS Messaging channels. This object is available in API
version 63.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Access to standard objects requires Salesforce admin privileges or the Customize Application permission.

Fields

**Field** **Details**

```
ChannelDefinitionId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects CustomMsgChannel

**Field** **Details**

**Description**
Specifies the ConversationChannelDefinition for the custom channel.

This field is a relationship field.

**Relationship Name**
ChannelDefinition

**Refers To**
ConversationChannelDefinition

```
EventCapabilitiesIsInboundAcknowledgementEnabled

EventCapabilitiesIsProgressIndicatorEnabled

EventCapabilitiesIsTypingIndicatorDisabled

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the Salesforce admin has enabled read receipts and delivery receipts for
inbound messages in the Messaging settings ( `true` ) or whether the admin hasn’t enabled
these inbound acknowledgments ( `false` ). The default value is `false`, meaning inbound
acknowledgments are disabled by default even if supported by the partner.

This field is available in API version 65.0 and later. Use this field instead of
`HasInboundReceipts` .

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the Salesforce admin has enabled AI agent progress indicators in the
Messaging settings ( `true` ) or whether the admin hasn’t enabled progress indicators
( `false` ). The default value is `false`, meaning progress indicators for AI agents are disabled
by default even if supported by the partner.

This field is available in API version 65.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the Salesforce admin has enabled typing indicators for outbound messages
in the Messaging settings ( `false` ) or whether the admin hasn’t enabled outbound typing
indicators ( `true` ). The default value is `false`, meaning the outbound typing indicators
are enabled by default.

This field is available in API version 65.0 and later. Use this field instead of
`HasTypingIndicator` .


### Standard Objects CustomNotificationType

**Field** **Details**

```
HasInboundReceipts

HasTypingIndicator

MessagingChannelId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the Salesforce admin has enabled read receipts and delivery receipts for
inbound messages in the Messaging settings ( `true` ) or whether the admin hasn’t enabled
these inbound acknowledgments ( `false` ). The default value is `false`, meaning inbound
acknowledgments are disabled by default even if supported by the partner.

Available in API versions 63.0 to 65.0. In API version 66.0 and later, this field is removed. Use
`EventCapabilitiesIsInboundAcknowledgementEnabled` instead.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the Salesforce admin has enabled typing indicators for outbound messages
in the Messaging settings ( `true` ) or whether the admin hasn’t enabled outbound typing
indicators ( `false` ). The default value is `true`, meaning the outbound typing indicator
feature is enabled by default if supported by the partner. To disable the outbound typing
indicator feature, set this value to `false` .

Available in API versions 63.0 to 65.0. In API version 66.0 and later, this field is removed. Use
`EventCapabilitiesIsTypingIndicatorDisabled` instead.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Specifies the Messaging Channel ID for the custom channel. This field is unique within your
organization.

This field is a relationship field.

**Relationship Name**
MessagingChannel

**Refers To**
MessagingChannel

### CustomNotificationType

Stores information about custom notification types. This object is available in API version 47.0 and later.


Standard Objects CustomNotificationType

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CustomNotifTypeName

Description

Desktop

DeveloperName

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Unique, Update

**Description**
Specifies a notification type name. The notification type name is unique within your
organization. The notification type name isn’t namespaced, so it can’t be duplicated across
installed packages. Maximum number of characters: 80.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies a general description of the notification type, which is displayed with the notification
type name. Maximum number of characters: 255.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the desktop delivery channel is enabled ( `true` ) or not ( `false` ). The
default value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Specifies the API name of the notification type.


### Standard Objects CustomPermission

**Field** **Details**

```
IsSlack

Language

MasterLabel

Mobile

NamespacePrefix

### CustomPermission

```

**Type**
boolean

**Properties**
Reserved for future use.

**Description**
Reserved for future use.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the language of the custom notification type. The value for this field is the language
value of the org.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Specifies the notification type label.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the mobile delivery channel is enabled ( `true` ) or not ( `false` ). The
default value is `false` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Specifies the namespace of the notification type, if installed with a managed package.

Represents a permission created to control access to a custom process or app, such as sending email. This object is available in API
version 31.0 and later.


Standard Objects CustomPermission

Supported Calls

`describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

As of Summer ’20 and later, only users who have one of these permissions can access this object:

**•** View Setup and Configuration

**•** Manage Session Permission Set Activations

**•** Assign Permission Sets

Fields

**Field Name** **Details**

```
Description

DeveloperName

IsLicensed

```

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
A description of the custom permission. Limit: 255 characters.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique name of the custom permission in the API. This name can contain
only underscores and alphanumeric characters and must be unique in your
organization. It must begin with a letter, not include spaces, not end with an
underscore, and not contain two consecutive underscores. The label corresponds
to **Name** in the user interface. Limit: 80 characters.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is specified,
performance may slow while Salesforce generates one for each record.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects CustomPermission

**Field Name** **Details**

**Description**
When enabled (true) indicates that the appropriate Salesforce license is required
before accessing the permission. This field is available in API version 50.0 and
later.

```
IsProtected

Language

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the custom permission is protected ( `true` ) or not ( `false` ).
Protected components that have been installed in other organizations can’t be
linked to or referenced by components created in the subscriber organization.
A developer can delete a protected component contained in a managed package
in a future release of the package without worrying about failing installations.
However, after a component is marked as unprotected and is released globally,
the developer can’t delete it. The default value is `false` . This field is available
in API version 50.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language of the custom permission. Valid values are:

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


Standard Objects CustomPermission

**Field Name** **Details**

**•** Spanish (Mexico): `es_MX` Spanish (Mexico) defaults to Spanish for
customer-defined translations.

**•** Swedish: `sv`

**•** Thai: `th` The Salesforce user interface is fully translated to Thai, but Help is
in English.

```
MasterLabel

NamespacePrefix

```

Usage

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The custom permission label, which corresponds to **Label** in the user interface.
Limit: 80 characters.

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

Use the CustomPermission object to determine users’ access to custom permissions.

For example, to query all permission sets where the Button1 permission is enabled:

```
SELECT Id, DeveloperName,

(select Id, Parent.Name, Parent.Profile.Name from SetupEntityAccessItems)

FROM CustomPermission

WHERE DeveloperName = 'Button1'

```


### Standard Objects CustomPermissionDependency

To query all permission sets and profiles with custom permissions:

```
   SELECT Assignee.Name, PermissionSet.Id,

   PermissionSet.Profile.Name,

   PermissionSet.isOwnedByProfile,

   PermissionSet.Label

   FROM PermissionSetAssignment

   WHERE PermissionSetId

   IN (SELECT ParentId

     FROM SetupEntityAccess

     WHERE SetupEntityType =

   'CustomPermission')

```

To query for all SetupEntityAccess rows with custom permissions:

```
   SELECT Id,ParentId,Parent.Name, SetupEntityId

   FROM SetupEntityAccess

   WHERE SetupEntityType='CustomPermission'

   AND ParentId

   IN (SELECT Id

     FROM PermissionSet

     WHERE isOwnedByProfile = false)

```

SEE ALSO:

### CustomPermissionDependency

PermissionSet

Profile

SetupEntityAccess

### CustomPermissionDependency

Represents the dependency between two custom permissions when one custom permission requires that you enable another custom
permission. This object is available in API version 32.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

As of Spring ’20 and later, only users with View Setup and Configuration permission can access this object.

Fields

**Field Name** **Details**

```
CustomPermissionId

```

**Type**
reference


Standard Objects CustomPermissionDependency

**Field Name** **Details**

**Properties**
Filter, Group, Sort

**Description**
The ID of the custom permission that requires the permission that’s specified in
`RequiredCustomPermissionId` .

This is a relationship field.

**Relationship Name**
CustomPermission

**Relationship Type**
Lookup

**Refers To**
CustomPermission

```
RequiredCustomPermissionId

```

Usage

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the custom permission that must be enabled when
`CustomPermissionId` is enabled.

This is a relationship field.

**Relationship Name**
RequiredCustomPermission

**Relationship Type**
Lookup

**Refers To**
CustomPermission

The following Apex class contains a method that returns the IDs of all custom permissions that are required for the given custom
permission ID. To use this class, save it in your organization.

```
public class CustomPermissionUtil {

  public String[] getAllRequiredCustomPermissions(String customPermId) {

    return getAllRequiredHelper(new String[]{customPermId});

  }

  private String[] getAllRequiredHelper(String[] customPermIds) {

    CustomPermissionDependency[] requiredPerms = [SELECT RequiredCustomPermissionId

                                FROM CustomPermissionDependency

                                WHERE CustomPermissionId

                                IN :customPermIds];

```


### Standard Objects Customer

```
       String[] requiredPermIds = new String[]{};

       for (CustomPermissionDependency cpd : requiredPerms) {

         requiredPermIds.add(cpd.RequiredCustomPermissionId);

       }

       if (requiredPermIds.size() > 0) {

         customPermIds.addall(getAllRequiredHelper(requiredPermIds));

         return customPermIds;

       } else {

         return customPermIds;

       }

     }

   }

```

[For more information about using Apex classes, see the Apex Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dev_guide.htm)

SEE ALSO:

CustomPermission

### Customer

Represents the customer role of an individual with respect to a particular company or organization. This object is available in API version
53.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

### `CustomerStatusType`

```
LastReferencedDate

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the customer account.

Possible values are:

**•** `Active`

**•** `Inactive`

**Type**
dateTime


Standard Objects Customer

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

```
LastViewedDate

Name

OwnerId

PartyId

```

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
Required. Name of this customer.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who owns the record.

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
Required. Represents the individual object related to this customer record.

This is a relationship field.


### Standard Objects DandBCompany

**Field** **Details**

**Relationship Name**
Party

**Relationship Type**
Lookup

**Refers To**
Individual

```
TotalLifeTimeValue

### DandBCompany

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The total revenue amount gained from this customer.

Represents a Dun & Bradstreet [®] company record, which is associated with an account added from Data.com. This object is available in
API version 25.0 and later.

Note: When your Data.com Prospector or Data.com Clean contract expires, Data.com features, objects, and fields will be removed
from your org.

To support customers’ needs around compliance and to remain a leader in trust and privacy, Salesforce removed all contact data
from the Data.com service on February 1, 2021.

[For more information, see Data.com Prospector and Clean Retirement.](https://help.salesforce.com/articleView?id=000270376&language=en_US&type=1)

Warning: You can update fields in the DandBCompany object; however, field changes may be overwritten by Data.com Clean
jobs or by using the Data.com Clean button.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Only organizations with Data.com Premium Prospector or Data.com Premium Clean can access this object.


Standard Objects DandBCompany

Fields

**Field Name** **Details**

```
Address

City

CompanyCurrencyIsoCode

Country

CountryAccessCode

```

**Type**
address

**Properties**
Filter, Nillable

**Description**
The compound form of the address. Read-only. See Address Compound Fields
for details on compound address fields.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city where a company is physically located. Maximum size is 40 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The code used to represent a company’s local currency. This data is provided by
the International Organization for Standardization (ISO) and is based on their
three-letter currency codes. For example, USD is the ISO code for United States
Dollar. Maximum size is 3 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country where a company is physically located. Maximum size is 40 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The required code for international calls. Maximum size is 4 characters.


Standard Objects DandBCompany

**Field Name** **Details**

```
CurrencyCode

Description

DomesticUltimateBusinessName

DomesticUltimateDunsNumber

DunsNumber

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The currency in which the company’s sales volume is expressed. The full list of
values can be found at the Optimizer Resources page maintained by Dun &
Bradstreet. Maximum size is 4 characters.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A brief description of the company, which may include information about its
history, its products and services, and its influence on a particular industry.
Maximum size is 32000 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The primary name of the Domestic Ultimate, which is the highest ranking
subsidiary, specified by country, within an organization’s corporate structure.
Maximum size is 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The D-U-N-S Number for the Domestic Ultimate, which is the highest ranking
subsidiary, specified by country, within an organization’s corporate structure.
Maximum size is 9 characters.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects DandBCompany

**Field Name** **Details**

**Description**
The Data Universal Numbering System (D-U-N-S) number is a unique, nine-digit
number assigned to every business location in the Dun & Bradstreet database
that has a unique, separate, and distinct operation. D-U-N-S numbers are used
by industries and organizations around the world as a global standard for business
identification and tracking. Maximum size is 9 characters.

```
EmployeeQuantityGrowthRate

EmployeesHere

EmployeesHereReliability

EmployeesTotal

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The yearly growth rate of the number of employees in a company expressed as
a decimal percentage. The data includes the total employee growth rate for the
past two years.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The number of employees at a specified location, such as a branch location.
Maximum size is 15 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The reliability of the `EmployeesHere` figure. Available values include:

**•** 0—Actual number

**•** 1—Low

**•** 2—Estimated (for all records)

**•** 3—Modeled (for non-US records)

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The total number of employees in the company, including all subsidiary and
branch locations. This data is only available on records that have a value of


Standard Objects DandBCompany

**Field Name** **Details**

_`Headquarters/Parent`_ in the `LocationStatus` field. Maximum size
is 15 characters.

```
EmployeesTotalReliability

FamilyMembers

Fax

FifthNaics

FifthNaicsDesc

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The reliability of the `EmployeesTotal` figure. Available values include:

**•** 0—Actual number

**•** 1—Low

**•** 2—Estimated (for all records)

**•** 3—Modeled (for non-US records)

A blank value indicates this data is unavailable.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The total number of family members, worldwide, within an organization, including
the Global Ultimate, its subsidiaries (if any), and its branches (if any). Maximum
size is 5 characters.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The company’s facsimile number.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional NAICS code used to further classify an organization by industry.
Maximum size is 6 characters.

**Type**
string


Standard Objects DandBCompany

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on the
corresponding NAICS code. Maximum size is 120 characters.

```
FifthSic

FifthSic8

FifthSic8Desc

FifthSicDesc

FipsMsaCode

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects DandBCompany

**Field Name** **Details**

**Description**
The Federal Information Processing Standards (FIPS) and the Metropolitan
Statistical Area (MSA) codes identify the organization’s location. The MSA codes
are defined by the US Office of Management and Budget. Maximum size is 5
characters.

```
FipsMsaDesc

FortuneRank

FourthNaics

FourthNaicsDesc

FourthSic

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s FIPS MSA code. Maximum size is 255
characters.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The numeric value of the company’s Fortune 1000 ranking. A null or blank value
means that the company isn’t ranked as a Fortune 1000 company.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional NAICS code used to further classify an organization by industry.
Maximum size is 6 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on the
corresponding NAICS code. Maximum size is 120 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects DandBCompany

**Field Name** **Details**

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

```
FourthSic8

FourthSic8Desc

FourthSicDesc

GeoCodeAccuracy

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The level of accuracy of a location’s geographical coordinates compared with its
physical address. Available values include:

**•** A – _`Non-US rooftop accuracy`_

**•** B – _`Block level`_

**•** C – _`Places the address in the correct city`_

**•** D – _`Rooftop level`_

**•** I – _`Street intersection`_

**•** M – _`Mailing address level`_


Standard Objects DandBCompany

**Field Name** **Details**

**•** N – _`Not matched`_

**•** P – _`PO BOX location`_

**•** S – _`Street level`_

**•** T – _`Census tract level`_

**•** Z – _`ZIP code level`_

**•** 0 (zero)– _`Geocode could not be assigned`_

```
GlobalUltimateBusinessName

GlobalUltimateDunsNumber

GlobalUltimateTotalEmployees

ImportExportAgent

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The primary name of the Global Ultimate, which is the highest entity within an
organization’s corporate structure and may oversee branches and subsidiaries.
Maximum size is 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The D-U-N-S Number of the Global Ultimate, which is the highest entity within
an organization’s corporate structure and may oversee branches and subsidiaries.
Maximum size is 9 characters.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The total number of employees at the Global Ultimate, which is the highest entity
within an organization’s corporate structure and may oversee branches and
subsidiaries. Maximum size is 15 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Identifies whether a business imports goods or services, exports goods or services,
and/or is an agent for goods. Available values include:

**•** A—Importer/exporter/agent


Standard Objects DandBCompany

**Field Name** **Details**

**•** B—Importer/exporter

**•** C—Importer

**•** D—Importer/agent

**•** E—Exporter/agent

**•** F—Agent (keeps no inventory and does not take title goods)

**•** G—None or data not available

**•** H—Exporter

```
IncludedInSnP500

Latitude

LegalStatus

LocationStatus

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A true or false value. If `true`, the company is listed in the S&P 500 Index. If
`false`, the company isn’t listed in the S&P 500 Index.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Used with longitude to specify a precise location, which is then used to assess
the Geocode Accuracy. Maximum size is 11 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Identifies the legal structure of an organization.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Identifies the organizational status of a company. Available values are _`Single`_
_`location`_, _`Headquarters/Parent`_, and _`Branch`_ . Available values
include:

**•** 0—Single location (no other entities report to the business)

**•** 1—Headquarters/parent (branches and/or subsidiaries report to the business)


Standard Objects DandBCompany

**Field Name** **Details**

**•** 2—Branch (secondary location to a headquarters location)

```
Longitude

MailingAddress

MailingCity

MailingCountry

MailingPostalCode

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Used with latitude to specify a precise location, which is then used to assess the
Geocode Accuracy. Maximum size is 11 characters.

**Type**
address

**Properties**
Filter, Nillable

**Description**
The compound form of the mailing address. Read-only. See Address Compound
Fields for details on compound address fields.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city where a company has its mail delivered. Maximum size is 40 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country where a company has its mail delivered. Maximum size is 40
characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code that a company uses on its mailing address. Maximum size is 20
characters.


Standard Objects DandBCompany

**Field Name** **Details**

```
MailingState

MailingStreet

MarketingPreScreen

MarketingSegmentationCluster

MinorityOwned

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The state where a company has its mail delivered. Maximum size is 20 characters.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street address where a company has its mail delivered. Maximum size is 255
characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The probability that a company will pay with a significant delay compared to the
agreed terms. The risk level is based on the standard Commercial Credit Score,
and ranges from low risk to high risk. Available values include:

**•** L— _`Low risk of delinquency`_

**•** M— _`Moderate risk of delinquency`_

**•** H— _`High risk of delinquency`_

Important: Use this information for marketing pre-screening purposes
only.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Twenty-two distinct, mutually exclusive profiles, created as a result of cluster
analysis of Dun & Bradstreet data for US organizations.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects DandBCompany

**Field Name** **Details**

**Description**
Indicates whether an organization is owned or controlled by a member of a
minority group. Available values include:

**•** Y—Minority owned

**•** N—Not minority owned

```
Name

NationalId

NationalIdType

OutOfBusiness

OwnOrRent

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The primary or registered name of a company. Maximum size is 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The identification number used in some countries for business registration and
tax collection. Maximum size is 255 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
A code value that identifies the type of national identification number used. The
full list of resources can be found at the Optimizer Resources page maintained
by Dun & Bradstreet. Maximum size is 5 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates whether the company at the specified address has discontinued
operations. Available values include:

**•** Y—Out of business

**•** N—Not out of business

**Type**
picklist


Standard Objects DandBCompany

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates whether a company owns or rents the building it occupies. Available
values include:

**•** 0—Unknown or not applicable

**•** 1—Owns

**•** 2—Rents

```
ParentOrHqBusinessName

ParentOrHqDunsNumber

Phone

PostalCode

PremisesMeasure

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The primary name of the parent or headquarters company. Maximum size is 255
characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The D-U-N-S Number for the parent or headquarters. Maximum size is 9 characters.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A company’s primary telephone number.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code that corresponds to a company’s physical location. Maximum
size is 20 characters.

**Type**
int


Standard Objects DandBCompany

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A numeric value for the measurement of the premises.

```
PremisesMeasureReliability

PremisesMeasureUnit

PrimaryNaics

PrimaryNaicsDesc

PrimarySic

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A descriptive accuracy of the measurement such as actual, estimated, or modeled.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A descriptive measurement unit such as acres, square meters, or square feet.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The six-digit North American Industry Classification System (NAICS) code is the
standard used by business and government to classify business establishments
according to their economic activity for the purpose of collecting, analyzing, and
publishing statistical data related to the US business economy. The full list of
values can be found at the Optimizer Resources page maintained by Dun &
Bradstreet. Maximum size is 6 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on its NAICS code.
Maximum size is 120 characters.

**Type**
string


Standard Objects DandBCompany

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The four-digit Standard Industrial Classification (SIC) code is used to categorize
business establishments by industry. The full list of values can be found at the
Optimizer Resources page maintained by Dun & Bradstreet. Maximum size is 4
characters.

```
PrimarySic8

PrimarySic8Desc

PrimarySicDesc

PriorYearEmployees

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The eight-digit Standard Industrial Classification (SIC) code is used to categorize
business establishments by industry. The full list of values can be found at the
Optimizer Resources page maintained by Dun & Bradstreet. Maximum size is 8
characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on its SIC code.
The full list of values can be found at the Optimizer Resources page maintained
by Dun & Bradstreet. Maximum size is 80 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on its SIC code.
Maximum size is 80 characters.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The total number of employees for the prior year.


Standard Objects DandBCompany

**Field Name** **Details**

```
PriorYearRevenue

PublicIndicator

SalesTurnoverGrowthRate

SalesVolume

SalesVolumeReliability

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The annual revenue for the prior year.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates whether ownership of the company is public or private. Available values
include:

**•** Y—Public

**•** N—Private

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The increase in annual revenue from the previous value for an equivalent period
expressed as a decimal percentage.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The total annual sales revenue in the headquarters’ local currency. Dun &
Bradstreet tracks revenue data for publicly traded companies, Global Ultimates,
Domestic Ultimates, and some headquarters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The reliability of the `SalesVolume` figure. Available values include:

**•** 0—Actual number


Standard Objects DandBCompany

**Field Name** **Details**

**•** 1—Low

**•** 2—Estimated (for all records)

**•** 3—Modeled (for non-US records)

```
SecondNaics

SecondNaicsDesc

SecondSic

SecondSic8

SecondSic8Desc

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional NAICS code used to further classify an organization by industry.
Maximum size is 6 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on the
corresponding NAICS code. Maximum size is 120 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects DandBCompany

**Field Name** **Details**

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

```
SecondSicDesc

SixthNaics

SixthNaicsDesc

SixthSic

SixthSic8

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional NAICS code used to further classify an organization by industry.
Maximum size is 6 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on the
corresponding NAICS code. Maximum size is 120 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects DandBCompany

**Field Name** **Details**

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

```
SixthSic8Desc

SixthSicDesc

SmallBusiness

State

StockExchange

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates whether the company is designated a small business as defined by the
Small Business Administration of the US government. Available values include:

**•** Y—Small business site

**•** N—Not small business site

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The state where a company is physically located. Maximum size is 20 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects DandBCompany

**Field Name** **Details**

**Description**
The corresponding exchange for a company’s stock symbol. For example: NASDAQ
or NYSE. Maximum size is 16 characters.

```
StockSymbol

Street

Subsidiary

ThirdNaics

ThirdNaicsDesc

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The abbreviation used to identify publicly traded shares of a particular stock.
Maximum size is 6 characters.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street address where a company is physically located. Maximum size is 255
characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates whether a company is more than 50 percent owned by another
organization. Available values include:

**•** 0—Not subsidiary of another organization

**•** 3—Subsidiary of another organization

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional NAICS code used to further classify an organization by industry.
Maximum size is 6 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects DandBCompany

**Field Name** **Details**

**Description**
A brief description of an organization’s line of business, based on the
corresponding NAICS code. Maximum size is 120 characters.

```
ThirdSic

ThirdSic8

ThirdSic8Desc

ThirdSicDesc

TradeStyle1

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects DandBCompany

**Field Name** **Details**

**Description**
A name, different from its legal name, that an organization may use for conducting
business. Similar to “Doing business as” or “DBA”. Maximum size is 255 characters.

```
TradeStyle2

TradeStyle3

TradeStyle4

TradeStyle5

URL

UsTaxId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional tradestyle used by the organization. Maximum size is 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional tradestyle used by the organization. Maximum size is 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional tradestyle used by the organization. Maximum size is 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional tradestyle used by the organization. Maximum size is 255 characters.

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An organization’s primary website address. Maximum size is 104 characters.

**Type**
string


### Standard Objects Dashboard

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The identification number for the company used by the Internal Revenue Service
(IRS) in the administration of tax laws. Also referred to as Federal Taxpayer
Identification Number. Maximum size is 9 characters.

```
WomenOwned

YearStarted

```

Usage

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates whether a company is more than 50 percent owned or controlled by
a woman. Available values include:

**•** Y—Owned by a woman

**•** N—Not owned by a woman, or unknown

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The year the company was established or the year when current ownership or
management assumed control of the company. Maximum size is 4 characters.

Use this object to manage D&B Company records in your organization.

### Dashboard

Represents a dashboard, which shows data from custom reports as visual components. Access is read-only. This object is available in
API version 20.0 and later.

Supported Calls

`describeSObjects()`, `describeLayout()`, `query()`, `retrieve()`, `search()`


Standard Objects Dashboard

Fields

**Field** **Details**

```
BackgroundDirection

BackgroundEnd

BackgroundStart

ChartTheme

ColorPalette

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Returns the direction of the background fade. Available values are:

**•** `Top to Bottom`

**•** `Left to Right`

**•** `Diagonal` (default value)

Label is `Background Fade Direction` .

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Returns the ending fade color in hexadecimal. Label is `Ending Color` .

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Returns the starting fade color in hexadecimal. Label is `Starting Color` .

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Returns the background theme used for charts.

Possible values are:

**•** `dark` —Dark Background

**•** `light` —Light Background

**Type**
picklist


Standard Objects Dashboard

**Field** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Returns the color palette used for the dashboard.

Possible values are:

**•** `Default` —Default Palette

**•** `accessible` —Mineral(Accessible) Palette

**•** `bluegrass` —Bluegrass Palette

**•** `colorSafe` —Color Safe Palette

**•** `dusk` —Dusk Palette

**•** `earth` —Lake Palette

**•** `fire` —Fire Palette

**•** `gray` —Gray Palette

**•** `heat` —Heat Palette

**•** `justice` —Wildflowers Palette

**•** `nightfall` —Nightfall Palette

**•** `pond` —Pond Palette

**•** `sunrise` —Sunrise Palette

**•** `tropic` —Ocean Palette

**•** `unity` —Aurora Palette

**•** `water` —Water Palette

**•** `watermelon` —Watermelon Palette

```
DashboardResultRefreshedDate

DashboardResultRunningUser

Description

```

**Type**
string

**Properties**
Nillable

**Description**
Returns the date on which the dashboard results were last refreshed.

**Type**
string

**Properties**
Nillable

**Description**
The user whose security settings were used to generate the dashboard results.

**Type**
string


Standard Objects Dashboard

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Returns the description of the dashboard. Limit: 255 characters.

```
DeveloperName

FolderId

FolderName

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Required. The unique name of the object in the API. This name can contain only
underscores and alphanumeric characters, and must be unique in your org. It
must begin with a letter, not include spaces, not end with an underscore, and
not contain two consecutive underscores. In managed packages, this field
prevents naming conflicts on package installations. With this field, a developer
can change the object’s name in a managed package and the changes are
reflected in a subscriber’s organization. Label is `Dashboard Unique Name` .

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is
specified, performance may slow while Salesforce generates one for each
record.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Required. Returns the ID of the Folder that contains the dashboard. See Folder.

This is a relationship field.

**Relationship Name**
Folder

**Relationship Type**
Lookup

**Refers To**
Folder, User

**Type**
string

**Properties**
Filter, Nillable, Sort


Standard Objects Dashboard

**Field** **Details**

**Description**
Name of the folder that contains the dashboard. Available in API version 35.0
and later.

```
IsDeleted

LastReferencedDate

LastViewedDate

LeftSize

```

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not
( `false` ). Label is `Deleted` .

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related
to this record, or a list view.

**Type**
datetime

**Properties**
Filter, Nillable, Sort,

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, the user might have only accessed this record or list view
( `LastReferencedDate` ) but not viewed it.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**

Returns the size of the left column of the dashboard.

Available values are:

**•** `Narrow`

**•** `Medium`

**•** `Wide`


Standard Objects Dashboard

**Field** **Details**

```
MiddleSize

NamespacePrefix

RightSize

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

Returns the size of the middle column of the dashboard.

Available values are:

**•** `Narrow`

**•** `Medium`

**•** `Wide`

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
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**

Returns the size of the right column in the dashboard.

Available values are:

**•** `Narrow`

**•** `Medium`

**•** `Wide`


Standard Objects Dashboard

**Field** **Details**

```
RunningUserId

TextColor

Title

TitleColor

TitleSize

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Returns the ID of the running user specified for the dashboard.

If the dashboard was created in Lightning Experience and is configured to run
as the viewing user, it returns the user ID of the dashboard creator.

If the dashboard was created in Salesforce Classic and is configured to run as the
logged-in user, returns the user ID of the last specified running user.

This is a relationship field.

**Relationship Name**
RunningUser

**Relationship Type**
Lookup

**Refers To**
User

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Returns the body text color in hexadecimal. Label is `Text Color` .

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Returns the title of the dashboard. Limit: 80 characters.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Returns the title text color in hexadecimal. Label is `Title Color` .

**Type**
int


Standard Objects Dashboard

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
Returns the title font size in points. Label is `Title Size` .

```
Type

```

Supported Query Scopes

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Returns the dashboard type. Available values are:

**•** `SpecifiedUser` —The dashboard displays data according to the access
level of one specific running user.

**•** `LoggedInUser` —The dashboard displays data according to the access
level of the logged-in user.

**•** `MyTeamUser` —The dashboard displays data according to the access level
of the logged-in user, and managers can view dashboards from the point of
view of users beneath them in the role hierarchy.

Use these scopes to help specify the data that your SOQL query returns.

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

Usage

Provides read-only access to the current values in the dashboard fields.


### Standard Objects DashboardComponent

Example: Dashboards in an Inactive User’s Private Folder

This SOQL query returns dashboards saved in a specific user’s private folder.

```
   SELECT Id FROM Dashboard USING SCOPE allPrivate WHERE CreatedByID = ‘005A0000000Bc2deFG’

```

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**DashboardFeed**

Feed tracking is available for the object.

SEE ALSO:

DashboardTag

Report

### DashboardComponent

Represents a dashboard component, which can be a chart, metric, table, or gauge on a dashboard. Access is read-only. This object is
available in API version 21.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
CustomReportId

DashboardId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Requires the user permission "Manage All Private Reports and Dashboards." The ID of the
report that provides data for the dashboard component. See Report.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the dashboard that contains the dashboard component. See Dashboard.

This is a relationship field.


### Standard Objects DashboardTag

**Field** **Details**

**Relationship Name**
### Dashboard

**Relationship Type**
Lookup

**Refers To**
### Dashboard

```
Name

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the dashboard component.

Provides read only access to the current values in dashboard component fields.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**DashboardComponentFeed**

Feed tracking is available for the object.

### DashboardTag

Associates a word or short phrase with a Dashboard. This object is available in API version 20.0 and later.

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


Standard Objects DashboardTag

**Field Name** **Details**

**Description**
ID of the tagged item.

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

DashboardTag stores the relationship between its parent TagDefinition and the Dashboard being tagged. Tag objects act as metadata,
allowing users to describe and organize their data.

When a tag is deleted, its parent TagDefinition will also be deleted if the name is not being used; otherwise, the parent remains. Deleting
a TagDefinition sends it to the Recycle Bin, along with any associated tag entries.

SEE ALSO:

Dashboard


### Standard Objects DataAssessmentFieldMetric DataAssessmentFieldMetric

Represents summary statistics for matched, blank, and differing fields in account records of an org compared to records in Data.com.
This object is available in API version 37.0 and later.

Note: When your Data.com Prospector or Data.com Clean contract expires, Data.com features, objects, and fields will be removed
from your org.

To support customers’ needs around compliance and to remain a leader in trust and privacy, Salesforce removed all contact data
from the Data.com service on February 1, 2021.

[For more information, see Data.com Prospector and Clean Retirement.](https://help.salesforce.com/articleView?id=000270376&language=en_US&type=1)

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

**Child Relationships**
### DataAssessmentFieldMetric is a child object of DataAssessmentMetric object.

Fields

**Field Name** **Details**

```
DataAssessmentMetricId

FieldName

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
A unique number that identifies the parent DataAssessmentMetric record.

This is a relationship field.

**Relationship Name**
DataAssessmentMetric

**Relationship Type**
Lookup

**Refers To**
DataAssessmentMetric

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the assessed field.


### Standard Objects DataAssessmentMetric

**Field Name** **Details**

```
Name

NumMatchedBlanks

NumMatchedDifferent

NumMatchedInSync

NumUnmatchedBlanks

### DataAssessmentMetric

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An optional field used to name your record.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of matched records that contain blank fields.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of matched records that have a different value for this field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of matched records that have the same value for this field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unmatched records that contain blank fields.

Represents a summary of statistics for fields matched and unmatched in your account records with Data.com account records. This
object is available in API version 37.0 and later.


Standard Objects DataAssessmentMetric

Note: When your Data.com Prospector or Data.com Clean contract expires, Data.com features, objects, and fields will be removed
from your org.

To support customers’ needs around compliance and to remain a leader in trust and privacy, Salesforce removed all contact data
from the Data.com service on February 1, 2021.

[For more information, see Data.com Prospector and Clean Retirement.](https://help.salesforce.com/articleView?id=000270376&language=en_US&type=1)

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
Name

NumDuplicates

NumMatched

NumMatchedDifferent

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An optional field used to name your record.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of duplicate records.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of matched records.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of records in your org matched with a Data.com record that have
different fields.


### Standard Objects DataAssessmentValueMetric

**Field Name** **Details**

```
NumProcessed

NumTotal

NumUnmatched

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of records processed in the data assessment.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of records available for data assessment processing.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of records not matched.

### DataAssessmentValueMetric

Summarizes the number of fields matched for your account records with Data.com account records.This object is available in API version
37.0 and later.

Note: When your Data.com Prospector or Data.com Clean contract expires, Data.com features, objects, and fields will be removed
from your org.

To support customers’ needs around compliance and to remain a leader in trust and privacy, Salesforce removed all contact data
from the Data.com service on February 1, 2021.

[For more information, see Data.com Prospector and Clean Retirement.](https://help.salesforce.com/articleView?id=000270376&language=en_US&type=1)

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

**Child Relationships**
### DataAssessmentValueMetric is a child of DataAssessementFieldMetric.


### Standard Objects DatabaseSaveEventLog

Fields

**Field Name** **Details**

```
DataAssessmentFieldMetricId

FieldValue

Name

ValueCount

### DatabaseSaveEventLog

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
A unique number that identifies the parent DataAssessementFieldMetric record.

This is a relationship field.

**Relationship Name**
DataAssessmentFieldMetric

**Relationship Type**
Lookup

**Refers To**
DataAssessmentFieldMetric

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The value in the matched field.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An optional field used to name your record.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times this value appears in this field.

Database Save events track when records are created,updated, or deleted This object is available in API version 64.0 and later.


Standard Objects DatabaseSaveEventLog

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

DmlType

FirstObjectIdentifier

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
The type of DML operation.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Only the first object ID is logged upon an update. During record updates, the ID of that
specific row is logged. When multiple rows are updated, only a single ID is logged.


Standard Objects DatabaseSaveEventLog

**Field** **Details**

```
KeyPrefix

LoginKey

```

PlannerIdentifier

```
RequestIdentifier

RowCount

SampleFactor

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The key prefix of the entity type that was saved

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a given user’s login session. The session starts with
a login event and ends with either a logout event or the user session expiring. For example,
`lUqjLPQTWRdvRG4` .

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
event in a given transaction has the same RequestIdentifier.

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


### Standard Objects DatacloudCompany

**Field** **Details**

**Description**
Rate at which entities are logged. If the sample factor is 1 that means every entity saved was
logged. If it is 100 that means that 1/100 logs.

```
SessionKey

Timestamp

UserIdentifier

```

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
The access time of Salesforce services in GMT. For example, 2020-01-20T19:12:26.965Z.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.

### DatacloudCompany

Represents the fields for Data.com company records. This object is available in API version 30.0 or later.

Note: When your Data.com Prospector or Data.com Clean contract expires, Data.com features, objects, and fields are removed
from your org.

To support customers’ needs around compliance and to remain a leader in trust and privacy, Salesforce removed all contact data
from the Data.com service on February 1, 2021.

[For more information, see Data.com Prospector and Clean Retirement.](https://help.salesforce.com/articleView?id=000270376&language=en_US&type=1)

Supported Calls

`describeLayout()`, `describeSObjects()`, `query()`


Standard Objects DatacloudCompany

Fields

**Field Name** **Details**

```
ActiveContacts

AnnualRevenue

City

CompanyId

Country

```

**Type**
int

**Properties**
Nillable

**Description**

The number of active contacts that are associated with a company.

**Type**
currency

**Properties**
Filter, Nillable

**Description**

The amount of money that the company makes in 1 year. Annual revenue is
measured in US dollars.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

The name of the city where the company is located.

**Type**
string

**Properties**
Filter, Nillable

**Description**

A unique numerical identifier for the company and theData.com identifier for a
company.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

A string that represents the standard abbreviation for the country where the
company is located.


Standard Objects DatacloudCompany

**Field Name** **Details**

```
CountryCode

Description

DunsNumber

EmployeeQuantityGrowthRate

ExternalId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist

**Description**

A standardized name for countries of the world.

**Type**
string

**Properties**
Nillable

**Description**

A brief synopsis of the company that provides a general overview of the company
and what it does.

**Type**
string

**Properties**
Filter, Nillable

**Description**

A randomly generated nine-digit number that’s assigned by Dun & Bradstreet
(D&B) to identify unique business establishments.

**Type**
double

**Properties**
Nillable

**Description**
The yearly growth rate of the number of employees in a company expressed as
a decimal percentage. The data includes the total employee growth rate for the
past two years.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

A unique numerical identifier for the company. The `ExternalId` is a
system-generated number.


Standard Objects DatacloudCompany

**Field Name** **Details**

```
Fax

FortuneRank

FullAddress

IncludedInSnP500

Industry

IsInCrm

```

**Type**
phone

**Properties**
Nillable

**Description**

The telephone number that’s used to send and receive faxes.

**Type**
int

**Properties**
Defaulted on create, Group, Nillable

**Description**
The numeric value of the company’s Fortune 1000 ranking. A null or blank value
means that the company isn’t ranked as a Fortune 1000 company.

**Type**
string

**Properties**
Group, Nillable

**Description**
The complete address of a company, including Street, City, State, and Zip.

**Type**
string

**Properties**
Group, Nillable

**Description**
A true or false value. If `true`, the company is listed in the S&P 500 Index. If
`false`, the company isn’t listed in the S&P 500 Index.

**Type**
string

**Properties**
Nillable

**Description**
A description of the type of industry such as Telecommunications, Agriculture,
or Electronics.

**Type**
boolean


Standard Objects DatacloudCompany

**Field Name** **Details**

**Properties**
Defaulted on create, Group

**Description**

Whether the record is in Salesforce (true) or not (false).

```
IsInactive

IsOwned

NaicsCode

NaicsDesc

Name

```

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**

A true or false response. True, the company record is not active. False, the
company record is active.

**Type**
boolean

**Properties**
Defaulted on create

**Description**

A true or false value. True, your organization owns the record. False, your
organization doesn’t own the record.

**Type**
string

**Properties**
Filter, Nillable

**Description**

A value that represents the North American Industry Classification System (NAICS)
code. NAICS was created to provide details about a business’s service orientation.
The code descriptions are focused on what a business does.

**Type**
string

**Properties**
Nillable

**Description**

A description of the NAICS classification.

**Type**
string


Standard Objects DatacloudCompany

**Field Name** **Details**

**Properties**
Filter, Nillable, Sort

**Description**

The company’s name.

```
NumberOfEmployees

Ownership

Phone

PremisesMeasure

PremisesMeasureReliability

```

**Type**
int

**Properties**
Filter, Nillable

**Description**

The number of employees working for the company.

**Type**
string

**Properties**
Filter, Nillable

**Description**

The type of ownership of the company:

**•** `Public`

**•** `Private`

**•** `Government`

**•** `Other`

**Type**
phone

**Properties**
Nillable

**Description**

A numeric string containing the primary telephone number for the company.

**Type**
int

**Properties**
Group, Nillable

**Description**
A numeric value for the measurement of the premises.

**Type**
string


Standard Objects DatacloudCompany

**Field Name** **Details**

**Properties**
Group, Nillable

**Description**
A descriptive accuracy of the measurement such as actual, estimated, or modeled.

```
PremisesMeasureUnit

PriorYearEmployees

PriorYearRevenue

SalesTurnoverGrowthRate

Sic

```

**Type**
string

**Properties**
Group, Nillable

**Description**
A descriptive measurement unit such as acres, square meters, or square feet.

**Type**
int

**Properties**
Group, Nillable

**Description**

The total number of employees for the prior year.

**Type**
double

**Properties**
Nillable

**Description**

The annual revenue for the prior year.

**Type**
double

**Properties**
Nillable

**Description**
The increase in annual revenue from the previous value for an equivalent period
expressed as a decimal percentage.

**Type**
string

**Properties**
Filter, Nillable


Standard Objects DatacloudCompany

**Field Name** **Details**

**Description**

A numeric value that represents the Standard Industrial Codes (SIC). SIC is a
numbering convention that indicates what type of service a business provides.
It is a four-digit value.

```
SicCodeDesc

SicDesc

Site

State

StateCode

```

**Type**
string

**Properties**
Group, Nillable

**Description**
The SIC numeric code and descsciption for a company.

**Type**
string

**Properties**
Nillable

**Description**

A description of the SIC classification.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist

**Description**

An organizational status of the company.

**•** Branch: a secondary location to a headquarter location

**•** Headquarter: a parent company with branches or subsidiaries

**•** Single Location: a single business with no subsidiaries or branches

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

The two-letter standard abbreviation for a state.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist


Standard Objects DatacloudCompany

**Field Name** **Details**

**Description**

A standard two-letter abbreviation for states and territories of the United States.
The state where the company is located. The abbreviation can also be a province
or other equivalent to a state, depending on the country where the company is
