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

[See Select the Salesforce Release for a Scratch Org for more information.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_scratch_orgs_version_selection.htm)

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

_[Salesforce DX Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev)_

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

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

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

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

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

[SearchLayoutButtonsDisplayed](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_tooling.meta/api_tooling/tooling_api_objects_searchlayout.htm#searchlayoutbuttonsdisplayed)

**Properties**
Nillable

**Description**

The list of buttons available in list views for an object.

This field is equivalent to the `listViewButtons` [field on SearchLayouts](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_searchlayouts.htm) in Metadata
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

[SearchLayoutFieldsDisplayed](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_tooling.meta/api_tooling/tooling_api_objects_searchlayout.htm#searchlayoutfieldsdisplayed)

**Properties**
Nillable

**Description**

The list of fields displayed in a search result for the object. The name field is required. It’s
always displayed as the first column header, so it isn’t included in this list; all additional fields
are included. The field name relative to the object name, for example MyCustomField__c,
is specified for each custom field.


Standard Objects SearchLayout

**Field** **Details**

This field is equivalent to `searchResultsAdditionalFields` [on SearchLayouts](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_searchlayouts.htm)
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
latitude and longitude coordinates. This field is available in the API only.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects ServiceAppointment

**Field Name** **Details**

**Description**
Indicates whether a service resource was automatically assigned to the
appointment. The default value is false.

This field is available in API version 49.0 and later.

```
IsBundle

IsBundleMember

IsManuallyBundled

IsOffsiteAppointment

LastReferencedDate

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

**Type**
dateTime


Standard Objects ServiceAppointment

**Field Name** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The date when the service appointment was last modified. Its label in the user
interface is `Last Modified Date` .

```
LastViewedDate

Latitude

Longitude

```

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

This field is available in the API only.

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

This field is available in the API only.


Standard Objects ServiceAppointment

**Field Name** **Details**

```
OwnerId

ParentRecordId

ParentRecordStatusCategory

ParentRecordType

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

**Type**
string


Standard Objects ServiceAppointment

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
(Read only) The type of parent record: Account, Asset, Lead, Opportunity, Work
Order, or Work Order Line Item.

```
PostalCode

RelatedBundleId

SchedEndTime

SchedStartTime

```

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

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects ServiceAppointment

**Field Name** **Details**

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

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update


Standard Objects ServiceAppointment

**Field Name** **Details**

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
line item. If Lightning Scheduler is also in use, this field is editable. However, users
see an error if they update it to list a different work type than the parent record’s
work type.

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
this field, a developer can change the object's name in a managed package and the changes
are reflected in a subscriber's organization.

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
[The SharingRules Metadata API type is enabled for all orgs.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_sharingrules.htm)

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

_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_sharingrules.htm)_ : SharingRules

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
[The SharingRules Metadata API type is enabled for all orgs.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_sharingrules.htm)


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
this field, a developer can change the object's name in a managed package and the changes
are reflected in a subscriber's organization. Corresponds to **Rule Name** in the user interface.

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
this field, a developer can change the object's name in a managed package and the changes
are reflected in a subscriber's organization.

When creating large sets of data, always specify a unique `DeveloperName` for each
record. If no `DeveloperName` is specified, performance slows down while Salesforce
generates one for each record.

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
appointments in a specified time period. The Capacities related list shows a
resource’s capacity.

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
crew. This field is hidden for all users by default. To use it, update its field-level
security settings in Setup and add it to your service resource page layouts.


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
[The SharingRules Metadata API type is enabled for all orgs.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_sharingrules.htm)

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
this field, a developer can change the object's name in a managed package and the changes
are reflected in a subscriber's organization. Corresponds to **Rule Name** in the user interface.

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
latitude and longitude coordinates. This field is available in the API only.

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
90 with up to 15 decimal places. This field is available in the API only.

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
180 with up to 15 decimal places. This field is available in the API only.

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

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`

Note: If you include session-based permission sets in a permission set group, the permissions in them don’t require session-based
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
Create, Filter, Group, Sort

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
Create, Filter, Group, Nillable, Sort

**Description**
The session details, such as device used and browser.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

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
Create, Filter, Group, Sort

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

           And PermissionSetId = :sessionPermSetId LIMIT 1];

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

```

To deactivate a session-based permission set for the current session, delete the matching SessionPermSetActivation record. Removing
that record ends the activation for that permission set in that session. In this example, a `deactivate()` method is added to the class
from the previous example.

```
   public PageReference deactivate() {

      List<SessionPermSetActivation> activations = [

        SELECT Id

        FROM SessionPermSetActivation

        WHERE AuthSessionId = :sessionId

           AND PermissionSetId = :sessionPermSetId

      ];

      if (!activations.isEmpty()) {

        delete activations;

      }

      return null;

   }

### SetupAssistantStep

```

For internal use only.

### SetupAuditTrail

Represents changes you or other admins made in your org’s Setup area for at least the last 180 days. This object is available in API version
15.0 and later.

Note: SetupAuditTrail is not a supported standard controller. Using SetupAuditTrail as a standard controller in a Visualforce page
results in an error.


Standard Objects SetupAuditTrail

Supported Calls

`query()`, `retrieve()`

Note: Aggregate queries aren’t supported on this object. For example, `SELECT count() FROM SetupAuditTrail`
works but `SELECT count(Id) FROM SetupAuditTrail` fails.

Fields

**Field** **Details**

```
Action

CreatedByContext

CreatedByIssuer

DelegateUser

```

**Type**
string

**Properties**
Filter, Sort

**Description**
The category of the change made in Setup. For example, a value of _`PermSetCreate`_
indicates that an administrator created a permission set. The `Display` field contains more
specific information.

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


### Standard Objects SetupEntityAccess

**Field** **Details**

```
Display

Section

```

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


Standard Objects SetupEntityAccess

**Field Name** **Details**

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


Standard Objects SetupEntityAccess

**Field Name** **Details**

**•** In API version 62.0 and later, `MessagingChannel` for messaging channels

**•** In API version 58.0 and later, `OrgWideEmailAddress` for
organization-wide email addresses

**•** In API version 28.0 and later, `ServiceProvider` for service providers

**•** In API version 60.0 and later, `StandardInvocableActionType` for
standard invocable actions.

**•** In API version 28.0 and later, `TabSet` for apps

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


### Standard Objects ShapeRepresentation

Let’s say the previous query returned the AppMenuItem `ApplicationId` 02uD0000000GIiMIAW. Using this ID, you can now run a
query to find out if a user has access to the Recruiting app:

```
   SELECT Id, SetupEntityId, SetupEntityType

   FROM SetupEntityAccess

   WHERE ParentId

   IN

     (SELECT PermissionSetId

     FROM PermissionSetAssignment

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


### Standard Objects SharingRecordCollection

**Field** **Details**

**Description**
Date when the org shape was last referenced. This field is read-only.

```
LastViewedDate

Name

Status

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date when the org shape was last viewed. This field is read-only.

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


Standard Objects SharingRecordCollection

Fields

**Field** **Details**

```
Description

GroupId

LastAdded

LastReferencedDate

LastViewedDate

Name

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the record collection.

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


### Standard Objects SharingRecordCollectionItem

**Field** **Details**

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the record collection.

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

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the related record collection.


### Standard Objects SharingRecordCollectionMember

**Field** **Details**

```
Description

ItemId

Name

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the record collection item.

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

```

**Type**
picklist

**Properties**
Read, Edit


### Standard Objects Shift

**Field** **Details**

**Description**
The access level on the related record collection.

```
CollectionId

UserOrGroupId

### Shift

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the related record collection.

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

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects Shift

**Field** **Details**

**Description**
Sets a background color when shifts are displayed in the UI. Use a 3- or 6-digit hexadecimal
format, for example #FF00FF. Available in API version 54.0 and later.

```
EndTime

IsHolidayShift

IsNonStandard

JobProfileId

Label

```

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date and time that the shift ends.

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


Standard Objects Shift

**Field** **Details**

```
LastReferencedDate

LastViewedDate

OwnerId

RecordsetFilterCriteriaId

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


Standard Objects Shift

**Field** **Details**

**Refers To**
RecordsetFilterCriteria

```
ServiceResourceId

ServiceTerritoryId

ShiftNumber

ShiftTemplateId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the service resource the shift belongs to. Available in API versions 47.0 and later.

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


Standard Objects Shift

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The shift template ID, if the shift was created from a shift template. Available in API version
53.0 and later.

This is a relationship field.

**Relationship Name**
ShiftTemplate

**Relationship Type**
Lookup

**Refers To**
ShiftTemplate

```
StartTime

Status

StatusCategory

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


### Standard Objects ShiftHistory

**Field** **Details**

**•** `Confirmed`

```
TimeSlotType

```

Usage

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Type of time slot for the shift. The same setup values as the `TimeSlot` field in the
OperatingHours object.

Possible values are:

**•** `Normal` (default value)

**•** `Extended`

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


Standard Objects ShiftHistory

Special Access Rules

Field Service must be enabled in your organization, and field tracking for shift fields must be configured.

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


### Standard Objects ShiftOwnerSharingRule

**Field** **Details**

**Relationship Name**
### Shift

**Relationship Type**
Lookup

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
[The SharingRules Metadata API type is enabled for all orgs.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_sharingrules.htm)

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


Standard Objects ShiftOwnerSharingRule

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object's name in a managed package and the changes
are reflected in a subscriber's organization. Corresponds to **Rule Name** in the user interface.

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


### Standard Objects ShiftPattern

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the User or Group being granted access.

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


Standard Objects ShiftPattern

**Field** **Details**

```
LastReferencedDate

LastViewedDate

Name

OwnerId

PatternLength

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the shift pattern was last used.

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


### Standard Objects ShiftPatternEntry

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ShiftPatternChangeEvent (API version 54.0)**
Change events are available for the object.

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

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
`DayOrder` links the shift template to the specific day within the shift pattern duration that
the template. For example, if the DayOrder is 2 then a shift from the associated template is
created on the second day of the pattern.


Standard Objects ShiftPatternEntry

**Field** **Details**

```
LastReferencedDate

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
The date that the shift pattern entry was last used.

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


### Standard Objects ShiftSegment

**Field** **Details**

This is a relationship field.

**Relationship Name**
ShiftTemplate

**Relationship Type**
Lookup

**Refers To**
ShiftTemplate

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

```

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date and time when the shift segment ends.


Standard Objects ShiftSegment

**Field** **Details**

```
IsInAdherence

Name

SegmentTypeId

ShiftId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the agent is in adherence ( `true` ) or not ( `false` ) for the scheduled
segment activity.

The default value is `true` .

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


### Standard Objects ShiftSegmentType

**Field** **Details**

**Refers To**
### Shift

```
StartTime

### ShiftSegmentType

```

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date and time when the shift segment starts.

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


Standard Objects ShiftSegmentType

**Field** **Details**

Possible values are:

**•** `Break` —Break times, such as a coffee or lunch break.

**•** `NonWork` —Non-working activities, such as training or meetings.

**•** `Work` —Work activities, such as answering calls, responding to chats, or handling cases.

```
Color

Description

DeveloperName

IsActive

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Sets a background color when shift activities of this type are displayed in the UI. Use a 3- or
6-digit hexadecimal format, for example #FF00FF.

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
this field, a developer can change the object's name in a managed package and the changes
are reflected in a subscriber's organization.

When creating large sets of data, always specify a unique `DeveloperName` for each
record. If no `DeveloperName` is specified, performance slows down while Salesforce
generates one for each record.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


### Standard Objects ShiftShare

**Field** **Details**

**Description**
Indicates if the shift segment type is active ( `true` ) or not ( `false` ).

The default value is `true` .

```
Language

MasterLabel

ServicePresenceStatusId

### ShiftShare

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the shift segment type.

Possible values are the languages that Workforce Engagement supports.

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


Standard Objects ShiftShare

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

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


### Standard Objects ShiftStatus

**Field** **Details**

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


Standard Objects ShiftStatus

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
Uniquely identifies a picklist value so it can be retrieved without using an ID or master label.

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


### Standard Objects ShiftTemplate

**Field** **Details**

**Description**
Describes the status of the shift using static values. Possible values are:

**•** `Tentative`

**•** `Published`

**•** `Confirmed`

Usage

Scheduling and dispatching service resources using shift data is not supported in API version 46.0.

### ShiftTemplate

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


Standard Objects ShiftTemplate

**Field** **Details**

**Description**
Additional information about the shift like number of breaks or activities.

```
Duration

IsActive

IsNonStandard

JobProfileId

```

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
How long the shift lasts. The unit of measurement for this field is determined by
`ShiftTemplateDurationType` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the shift is active or inactive.

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


Standard Objects ShiftTemplate

**Field** **Details**

```
LastReferencedDate

LastViewedDate

Name

OwnerId

RecordsetFilterCriteriaId

```

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


Standard Objects ShiftTemplate

**Field** **Details**

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

```
ShiftTemplateDurationType

StartTime

TimeSlotType

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The unit of measurement for the shift template duration.

Possible values are:

**•** `H` —Hours

**•** `M` —Minutes

The default value is `H` .

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


### Standard Objects Shipment

Associated Objects

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

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

At least one of these features must be enabled:

**•** Order Management

**•** Field Service

**•** B2B Commerce

**•** Consumer Goods Cloud Retail Execution

Fields

**Field Name** **Details**

```
ActualDeliveryDate

DeliveredToId

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


Standard Objects Shipment

**Field Name** **Details**

**Description**
The person or entity the product was delivered to.

This is a polymorphic relationship field.

**Relationship Name**
DeliveredTo

**Relationship Type**
Lookup

**Refers To**
Group, User

```
DeliveryMethodId

Description

DestinationLocationId

ExpectedDeliveryDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The delivery method used for the shipment.

This field is available in API version 51.0 and later.

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


Standard Objects Shipment

**Field Name** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date the product is expected to be delivered.

```
FulfillmentOrderId

LastReferencedDate

LastViewedDate

OrderSummaryId

OwnerId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The fulfillment order that the shipment belongs to.

This field is available in API version 51.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last interacted with this record, directly or
indirectly.

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


Standard Objects Shipment

**Field Name** **Details**

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

```
Provider

ReturnOrderId

ShipFromAddress

ShipFromCity

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The company or person making the transfer.

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


Standard Objects Shipment

**Field Name** **Details**

**Description**
The city of the address where the shipment originates.

```
ShipFromCountry

ShipFromGeocodeAccuracy

ShipFromLatitude

ShipFromLongitude

```

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

**Description**
Accuracy level of the geocode for the address where the shipment originates.
See Compound Field Considerations and Limitations for details on geolocation
compound fields.

Note: This field is available in the API only.

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


Standard Objects Shipment

**Field Name** **Details**

Note: This field is available in the API only.

```
ShipFromPostalCode

ShipFromState

ShipFromStreet

ShipToAddress

ShipToCity

ShipToCountry

```

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

**Description**
The state of the address where the shipment originates.

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


Standard Objects Shipment

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country of the address where the shipment is delivered.

```
ShipToGeocodeAccuracy

ShipToLatitude

ShipToLongitude

ShipToName

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Accuracy level of the geocode for the address where the shipment is delivered.
See Compound Field Considerations and Limitations for details on geolocation
compound fields.

Note: This field is available in the API only.

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


Standard Objects Shipment

**Field Name** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The shipment recipient.

```
ShipToPostalCode

ShipToState

ShipToStreet

ShipmentNumber

SourceLocationId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code of the address where the shipment is delivered.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The state of the address where the shipment is delivered.

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


Standard Objects Shipment

**Field Name** **Details**

**Relationship Name**
SourceLocation

**Relationship Type**
Lookup

**Refers To**
Location

```
Status

TotalItemsQuantity

TrackingNumber

TrackingUrl

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The status of the shipment. The picklist includes the following values, which can
be customized:

**•** _`Created`_ —Shipment has been created.

**•** _`Delivered`_ —Shipment has been delivered.

**•** _`In Transit`_ —Shipment is in transit.

**•** _`Shipped`_ —Order has been shipped.

**•** _`Voided`_ —Shipment has been cancelled.

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


### Standard Objects ShipmentItem

**Field Name** **Details**

**Description**
URL of website used for tracking the shipment.

Associated Objects

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


Standard Objects ShipmentItem

Fields

**Field** **Details**

```
Description

ExpectedDeliveryDate

FulfillmentOrderLineItemId

OrderItemSummaryId

Product2Id

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


Standard Objects ShipmentItem

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Product2

```
Quantity

ReturnOrderLineItemId

ShipmentId

ShipmentItemNumber

```

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

**Description**
For a return ShipmentItem, the associated ReturnOrderLineItem.

This field is available in API version 53.0 and later.

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


### Standard Objects ShippingCarrier

**Field** **Details**

```
TrackingNumber

TrackingUrl

```

Associated Objects

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


Standard Objects ShippingCarrier

Fields

**Field** **Details**

```
ExternalReference

LastReferencedDate

LastViewedDate

ManagedShippingCarrier

Name

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


Standard Objects ShippingCarrier

**Field** **Details**

**Description**
Name of the shipping carrier associated with the delivery.

```
ShipFromCountry

```

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


Standard Objects ShippingCarrier

**Field** **Details**

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


Standard Objects ShippingCarrier

**Field** **Details**

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


Standard Objects ShippingCarrier

**Field** **Details**

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


Standard Objects ShippingCarrier

**Field** **Details**

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


Standard Objects ShippingCarrier

**Field** **Details**

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


Standard Objects ShippingCarrier

**Field** **Details**

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


### Standard Objects ShippingCarrierMethod

**Field** **Details**

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

### ShippingCarrierMethod

Shipping service provided by a shipping carrier. Examples include Ground, 2Day, and NextDay. Service depends on the range of transit
times available for each carrier. This object is available in API version 61.0 and later.

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


Standard Objects ShippingCarrierMethod

**Field** **Details**

```
LastViewedDate

ManagedShippingCarrierMethod

MaxTransitTime

MinTransitTime

Name

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
Salesforce-managed shipping carrier method that provides estimated transit times. This field
is available in API version 65.0 and later.

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


Standard Objects ShippingCarrierMethod

**Field** **Details**

```
OwnerId

ShippingCarrierId

ShippingScope

TransitTimeUnit

```

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


### Standard Objects ShippingConfigurationSet

**Field** **Details**

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Unit of measurement used for transit time. Specifies the time interval in which the minimum
and maximum transit times are expressed.

The available options are:

**•** `Days`

**•** `Hours`

**•** `Weeks`

### ShippingConfigurationSet

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


Standard Objects ShippingConfigurationSet

**Field** **Details**

**Description**
Name of the shipping configuration set.

```
OwnerId

ProcessTime

ProcessTimeUnit

TargetRecordId

```

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

**Refers To**
Group, User

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


### Standard Objects ShippingConfigSetProduct

**Field** **Details**

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


### Standard Objects ShippingRateArea

**Field** **Details**

**Description**
ID of the Product2 record that is associated with shipping configuration set record.

This field is a relationship field.

**Relationship Name**
Product2

**Refers To**
Product2

```
ShippingProfileId

### ShippingRateArea

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the shipping profile.

This field is a relationship field.

**Relationship Name**
ShippingProfile

**Relationship Type**
Master-detail

**Refers To**
ShippingConfigurationSet (the master object)

A designated geographical area that’s available for shipping. This object is available in API version 59.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

The ShippingRateArea object is available only if the B2B Commerce or D2C Commerce license is enabled.


### Standard Objects ShippingRateGroup

Fields

**Field** **Details**

```
Countries

Name

Regions

### `ShippingRateGroupId` ShippingRateGroup

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

**Description**
Reserved for future use.

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


### Standard Objects SignupRequest

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

The ShippingRateGroup object is available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

```
Name

ShippingProfileId

### SignupRequest

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the shipping rate group.

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


Standard Objects SignupRequest

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`

Fields

**Field Name** **Details**

```
AuthCode

Company

ConnectedAppCallbackUrl

ConnectedAppConsumerKey

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


Standard Objects SignupRequest

**Field Name** **Details**

```
Country

CreatedOrgId

CreatedOrgInstance

Edition

ErrorCode

```

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
the sign-up request has been processed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The server instance of the new trial org, for example, “na8.” This field is available in API version
29.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The Salesforce template that is used to create the trial org. Possible values are `Partner`
`Group`, `Professional`, `Partner Professional`, `Sales Enterprise`,
`Professional TSO`, `Enterprise`, `Partner Enterprise`, `Service`
`Professional`, `Enterprise TSO`, `Developer`, and `Partner Developer` .
This field is available in API version 35.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects SignupRequest

**Field Name** **Details**

**Description**
The error code if the sign-up request isn’t successful. The system provides this read-only field
for support purposes.

```
FirstName

LastName

PreferredLanguage

ResolvedTemplateId

ShouldConnectToEnvHub

```

**Type**
string

**Properties**
Create, Filter, Nillable, Sort

**Description**
The first name of the admin user for the trial sign-up.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The last name of the admin user for the trial sign-up.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The language of the trial org being created. Specify the language using a language code listed
[under Fully Supported Languages in Supported Languages in Salesforce Help. For example,](https://help.salesforce.com/articleView?id=faq_getstart_what_languages_does.htm&type=5&language=en_US)
use _`zh_CN`_ for simplified Chinese. The value you select overrides the language set by the
locale. If you specify an invalid language, the org defaults to the default language of the country.
Likewise, if you specify a language that isn’t supported by the Salesforce edition associated
with your trial template, the trial org defaults to the default language of the country. This field
is available in API version 35.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Populated during the sign-up request and for internal use by Salesforce. This field is available
in API version 35.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort


Standard Objects SignupRequest

**Field Name** **Details**

**Description**
When set to `true`, the trial org is connected to the Environment Hub. The sign-up must take
place in the hub main org or a spoke org. This field is available in API version 35.0 and later.

```
SignupEmail

SignupSource

Status

Subdomain

SuppressSignupEmails

```

**Type**
email

**Properties**
Create, Filter, Group, Sort

**Description**
The email address of the admin user for the trial sign-up.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
A user-specified description of the trial sign-up, up to 60 characters. This field is available in
API version 36.0 and later.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
The status of the request. Possible values are `New`, `In Progress`, `Error`, or `Success` .
The default is `New` .

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The My Domain name for the new trial org used in the org’s login and application URLs. In
Developer Edition orgs, your name must contain at least 3 characters and no more than 27
characters. In all other editions, it must be at least 3 characters and no more than 34 characters.
It can include letters, numbers, and hyphens, but you can’t start the name with a hyphen.

If you don’t choose a My Domain during sign-up, Salesforce assigns one for you based on your
company name. If you don’t like the one we set, you can change it.

[For details, see My Domain in Salesforce Help.](https://help.salesforce.com/articleView?id=domain_name_overview.htm&language=en_US)

**Type**
boolean


Standard Objects SignupRequest

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
When set to `true`, no sign-up emails are sent when the trial org is created. This field is used
for the Proxy Signup feature and is available in API version 29.0 and later.

```
TemplateId

TrialDays

TrialSourceOrgId

Username

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the Trialforce template that is the basis for the trial sign-up. Salesforce
must approve the template. If you don’t specify an edition, a template ID is required.

**Type**
anyType

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
The duration of the trial sign-up in days. Must be equal to or less than the trial days for the
approved Trialforce template. If not provided, it defaults to the trial duration specified for the
Trialforce template.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character org ID of the Trialforce Source Organization (TSO) from which the Trialforce
template was created.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The username of the admin user for the trial sign-up. It must follow the address convention
[specified in RFC822: www.w3.org/Protocols/rfc822/#z10.](http://www.w3.org/Protocols/rfc822/#z10)


Standard Objects SignupRequest

Usage

The Java class uses REST API to create a SignupRequest object. It authenticates to the Trialforce Management Organization (TMO) and
then posts a request to the SignupRequest object.

Here are the variables to specify in this example.

**•** SERVER—The name of the host server for the TMO, for example, _`yourInstance`_ .salesforce.com.

**•** USERNAME—The admin username for the TMO.

**•** PASSWORD—The concatenation of the admin password and the security token for the TMO. To get an email with the security token,
from your personal settings in Salesforce, select **Reset My Security Token** and click **Reset Security Token** .

**•** CLIENT_ID—From Setup in Salesforce, in the Quick Find box, enter _`Apps`_, and then select **Apps** . Under Connected Apps, click **New** .
Enter values for the required fields (Callback URL is required, but you can initially set it to any valid URL because it’s not used). Grant
full access for the OAuth scopes in the Selected OAuth Scopes selector, and click **Save** . Then copy the value of Consumer Key and
use it for this variable.

**•** CLIENT_SECRET—On the same page, click **Click to reveal** . Then copy the value of Consumer Secret and use it for this variable.

```
   public class IsvSignupDriver {

      private static final String SERVER = server_name : port ;

      private static final String USERNAME = tmo_username ;

      private static final String PASSWORD = tmo_passwordsecurity_token ;

      private static final String CLIENT_ID = consumer_key ;

      private static final String CLIENT_SECRET = consumer_secret ;

      private static SignupRequestInfo signupRequest = null;

      public static String createSignupRequest (SignupRequestInfo sr)

       throws JSONException, IOException {

        JSONObject createResponse = null;

        signupRequest = sr;

        JSONObject loginResponse = login(SERVER, USERNAME, PASSWORD);

        String instanceUrl = loginResponse.getString("instance_url");

        String accessToken = loginResponse.getString("access_token");

        createResponse = create(instanceUrl, accessToken);

        System.out.println("Created SignupRequest object: " + createResponse + "\n");

        return createResponse.toString();

      }

      /* Authenticates to the TMO using the required credentials */

      private static JSONObject login(String server, String username, String password)

       throws ClientProtocolException, IOException, JSONException {

        String authEndPoint = server + "/services/oauth2/token";

        HttpClient httpclient = new DefaultHttpClient();

        try {

           HttpPost post = new HttpPost(authEndPoint);

           List<NameValuePair> params = new ArrayList<NameValuePair>();

           params.add(new BasicNameValuePair("grant_type", "password"));

           params.add(new BasicNameValuePair("client_id", CLIENT_ID));

           params.add(new BasicNameValuePair("client_secret", CLIENT_SECRET));

           params.add(new BasicNameValuePair("username", username));

           params.add(new BasicNameValuePair("password", password));

```


Standard Objects SignupRequest

```
           post.setEntity(new UrlEncodedFormEntity(params, Consts.UTF_8));

           BasicResponseHandler handler = new BasicResponseHandler();

           String response = httpclient.execute(post, handler);

           return new JSONObject(response);

        } finally {

           httpclient.getConnectionManager().shutdown();

        }

      }

      /* Posts a request to the SignupRequest object */

      private static JSONObject create(String instanceUrl, String accessToken)

       throws ClientProtocolException, IOException, JSONException {

        HttpClient httpClient = new DefaultHttpClient();

        try {

           HttpPost post = new HttpPost(instanceUrl +

            "/services/data/v27.0/sobjects/SignupRequest/");

             post.setHeader("Authorization", "Bearer " + accessToken);

             post.setHeader("Content-Type", "application/json");

             JSONObject requestBody = new JSONObject();

             requestBody.put("TemplateId", signupRequest.getTemplateID());

             requestBody.put("SignupEmail", signupRequest.getEmail());

             requestBody.put("username", signupRequest.getUsername());

             requestBody.put("Country", "US");

             requestBody.put("Company", signupRequest.getCompanyName());

             requestBody.put("lastName", signupRequest.getLastName());

             StringEntity entity = new StringEntity(requestBody.toString());

             post.setEntity(entity);

             BasicResponseHandler handler = new BasicResponseHandler();

             String response = httpClient.execute(post, handler);

             return new JSONObject(response);

        } finally {

           httpClient.getConnectionManager().shutdown();

        }

      }

   }

```

Error Codes

If the sign-up fails, the system generates an error code that can help you identify the cause. This table shows the most important error
codes.


Standard Objects SignupRequest

Associated Objects

This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**•** SignupRequestFeed–Feed tracking is available for the object.

**•** SignupRequestHistory–History is available for tracked fields of the object.


### Standard Objects Site

**•** SignupRequestOwnerSharingRule–Sharing rules are available for the object

**•** SignupRequestShare–Sharing is available for the object.

### Site

Represents a public website that is integrated with an org. This object is available in API version 16.0 and later.

To access this object, Digital Experiences, Salesforce Sites, or Site.com must be enabled.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

**•** Customer Portal users can’t access this object.

**•** To view this object, you must have the View Setup and Configuration permission.

Fields

**Field** **Description**

```
AdminId

AnalyticsTrackingCode

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The site administrator designated as the contact for the site. This user receives
site-related communications from site visitors and from Salesforce.

This is a relationship field.

**Relationship Name**
Admin

**Relationship Type**
Lookup

**Refers To**
User

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The tracking code associated with your site. This code can be used by services
like Google Analytics to track page request data for your site.


Standard Objects Site

**Field** **Description**

```
ArchiveStatus

ArchivedById

ArchivedDate

ClickjackProtectionLevel

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The archived status of a site. Possible values are:

**•** `NotArchived`

**•** `TemporaritlyArchived`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user that archived the site.

**Relationship Name:**
ArchivedBy

**Relationship Type:**
Lookup

**Refers To:**
User

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when the site was archived.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Sets the clickjack protection level. The options are:

**•** `AllowAllFraming` —Allow framing by any page (no protection)

**•** `SameOriginOnly` —Allow framing by the same origin only
(recommended)

**•** `NoFraming` —Don’t allow framing by any page (most protection)

This field is available in API version 30.0 and later.


Standard Objects Site

**Field** **Description**

```
DailyBandwidthLimit

DailyBandwidthUsed

DailyRequestTimeLimit

DailyRequestTimeUsed

Description

GuestRecordDefaultOwnerId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The rolling 24-hour daily bandwidth limit for the sites in your organization.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The current rolling 24-hour daily bandwidth usage for the sites in your
organization.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The rolling 24-hour daily service request time limit for the sites in your
organization. Service request time is calculated as the total server time in minutes
required to generate pages for the site.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The current rolling 24-hour daily service request time for the sites in your
organization.

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
An optional description of the site.

**Type**
reference


Standard Objects Site

**Field** **Description**

**Properties**
Filter, Group, Nillable, Sort

**Description**
A user in the Salesforce org that is the default owner of records created by
unauthenticated (guest) users.

This is a relationship field.

**Relationship Name**
GuestRecordDefaultOwner

**Relationship Type**
Lookup

**Refers To**
User

```
GuestUserId

MasterLabel

MonthlyPageViewsEntitlement

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The site or Experience Cloud sites specific user that anonymous, unauthenticated
users run as when interacting with the site.

This is a relationship field.

**Relationship Name**
GuestUser

**Relationship Type**
Lookup

**Refers To**
User

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The name of the site as it appears in the user interface.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects Site

**Field** **Description**

**Description**
The number of page views allowed for the current calendar month for the sites
in your organization.

```
Name

OptionsAllowGuestPaymentsApi

OptionsAllowGuestSupportApi

OptionsAllowHomePage

OptionsAllowStandardAnswersPages

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The name used when referencing the site in the API.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether unauthenticated guest users can access the Payments API
( `true` ) or not ( `false` ). The default is `false` . This field is available in API version
49.0 and later.

**Type**
boolean

**Properties**
Filter

**Description**
The option to enable unauthenticated users to access the Support API.

**Type**
boolean

**Properties**
Filter

**Description**
The option to enable the standard page associated with the Home tab
( `/home/home.jsp` ).

**Type**
boolean

**Properties**
Filter


Standard Objects Site

**Field** **Description**

**Description**
The option to enable standard pages associated with an answers Experience
Cloud site. If you want to use default Answers pages (such as AnswersHome),
enable these pages.

```
OptionsAllowStandardIdeasPages

OptionsAllowStandardLookups

OptionsAllowStandardPortalPages

OptionsAllowStandardSearch

OptionsBrowserXssProtection

```

**Type**
boolean

**Properties**
Filter

**Description**
The option to enable standard pages associated with an Ideas Experience Cloud
site. If you want to use default Ideas pages (such as IdeasHome), enable these
pages.

**Type**
boolean

**Properties**
Filter

**Description**
The option to enable the standard lookup pages. These are the windows
associated with lookup fields on Visualforce pages.

**Type**
boolean

**Properties**
Filter

**Description**
The option to enable authenticated users to access the standard Salesforce pages.

**Type**
boolean

**Properties**
Filter

**Description**
The option to enable the standard search pages. To allow public users to perform
standard searches, enable these pages.

**Type**
boolean

**Properties**
Filter


Standard Objects Site

**Field** **Description**

**Description**
The option to enable the browser's cross-site scripting protection.

```
OptionsCachePublicVfPagesInProxies

OptionsContentSniffingProtection

OptionsCookieConsent

OptionsCspUpgradeInsecureRequests

OptionsEnableFeeds

```

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether proxy servers cache this site’s publicly available pages only for
unauthenticated guest users ( `true` ) or not ( `false` ). When this field is `false`,
this site’s cache-enabled Visualforce pages are cached in the web browser for
both authenticated and unauthenticated users. The default is `true` . See
[Configure Site Caching in Salesforce Help for more information.](https://help.salesforce.com/articleView?id=platform.sites_caching.htm&type=5&language=en_US)

This field is available in API version 52.0 and later.

**Type**
boolean

**Properties**
Filter

**Description**
The option to enable content-sniffing protection.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether only required Salesforce-supplied cookies are allowed within
the site ( `true` ) or all cookies types are allowed: required, functional, and
advertising ( `false` ). The default is `false` . This field is available in API version
52.0 and later.

**Type**
boolean

**Properties**
Filter

**Description**
This field is removed in API version 52.0 and later. In API version 51.0 and earlier,
the value in the field is ignored.

**Type**
boolean


Standard Objects Site

**Field** **Description**

**Properties**
Filter

**Description**
The option that displays the Syndication Feeds related list, where you can create
and manage syndication feeds for users on your public sites. This field is visible
only if you have the feature enabled for your organization.

```
OptionsHasStoredPathPrefix

OptionsRedirectToCustomDomain

OptionsReferrerPolicyOriginWhenCrossOrigin

OptionsRequireHttps

```

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether this Experience Cloud site has a customized urlPathPrefix
( `true` ) or instead uses the Experience Cloud site's `UrlPathPrefix` plus `/s`
( `false` ). The default is `false` . In other sites, this field has no effect. This field
is available in API version 50.0 and later.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether requests to this site’s system-managed URLs are redirected to
the HTTPS custom domain serving this site ( `true` ) or not ( `false` ).
System-managed site URLs end in `*.my.salesforce-sites.com` or
`*.my.site.com` . In Experience Cloud sites, the default is `false` . In Salesforce
Sites, the default is `true` .

If multiple custom domains serve this site and this field is set to true, requests
are routed to the site’s primary custom URL only if it’s an HTTPS custom domain.
Otherwise, requests are redirected to the first HTTPS custom domain associated
with this site, in alphanumeric order. If no HTTPS custom domain serves this site,
this option has no effect.

This field is available in API version 52.0 and later.

**Type**
boolean

**Properties**
Filter

**Description**
The option to enable referrer policy (origin-when-cross-origin).

**Type**
boolean


Standard Objects Site

**Field** **Description**

**Properties**
Filter

**Description**
This field is removed in API version 52.0 and later. In API version 51.0 and earlier,
the value in the field is ignored.

```
SiteType

Status

Subdomain

TopLevelDomain

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Identifies whether the site is a Visualforce (Salesforce Sites) or a Site.com site.
`SiteType` is available in API version 21.0 and later. In API version 26.0 and
later, if Experience Cloud sites are enabled for your Salesforce org, the site could
also be a Network Visualforce or Network Site.com site.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status for the site. For example, `Active` or `In Maintenance` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If you enabled Salesforce Sites or Digital Experiences before you enabled enhanced
domains on your My Domain, this field returns this site’s previous subdomain.
For example, if your domain was `mycompany.force.com`, then
`mycompany` is the subdomain.

If you enabled Salesforce Sites or Digital Experiences after you enabled enhanced
domains, this field returns a null value.

**Type**
url

**Properties**
Filter, Nillable


### Standard Objects SiteDetail

**Field** **Description**

**Description**
The optional branded custom Web address that you registered with a third-party
domain name registrar. The custom Web address acts as an alias to your Salesforce
address.

Beginning with API version 21.0, `TopLevelDomain` is no longer available.
Instead, use the Domain and DomainSite objects.

```
UrlPathPrefix

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique Salesforce URL that the public uses to access this site.

Use this read-only object to query or retrieve information on your site.

Associated Objects

This object has the following associated objects. Unless noted, these associated objects are available in the same API version as this
object.

**SiteFeed**

Feed tracking is available for the object.

**SiteHistory**

History is available for tracked fields of the object.

### SiteDetail

Represents the details of a Salesforce site or Experience Cloud site. Available in API Version 38.0 and later.

Supported SOAP Calls

`describeSObjects()`, `query()`

Supported REST HTTP Methods

```
GET

```


### Standard Objects SiteDomain

Fields

**Field** **Details**

```
DurableId

IsRegistrationEnabled

SecureUrl

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Site object.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the site allows users to sign up.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URL of the website.

Note: SiteDetail fields are exposed in SOAP API version 45.0 and later. You can use Tooling API to query for SiteDetail fields in
guest user mode in API version 44.0 and earlier. In API version 45.0 and later, use SOAP API to get this data in guest user mode.
SiteDetail is still exposed in Tooling API to User Profiles with the ViewSetup permission.

### SiteDomain SiteDomain is a read-only object, and a one-to-many replacement for the Site.TopLevelDomain field. This object is available in API version

21.0, and has been deprecated as of API version 26.0. In API version 26.0 and later, use the Domain and DomainSite objects instead.

To access this object, Digital Experiences, Salesforce Sites, or Site.com must be enabled.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

**•** Customer Portal users can’t access this object.


### Standard Objects SiteEventLog

**•** To view this object, you must have the View Setup and Configuration permission.

Fields

**Field** **Description**

```
Domain

SiteId

DomainType

```

Usage

**Type**
url

**Properties**
Filter, Sort

**Description**
The branded custom Web address within the global namespace identified by
this domain's type. In the Domain Name System (DNS) global namespace, this
field is the custom Web address that you registered with a third-party domain
name registrar. The custom Web address can be used to access the site of this
domain.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the associated Site.

**Type**
picklist

**Properties**
Filter, Group, Sort, Nillable

**Description**
The global namespace that this custom Web address belongs to. This value is
set to DNS for custom Web addresses in the global DNS. This field is available in
version 24.0 of the API.

Use this read-only object to query the domains that are associated with each site in your organization.

### SiteEventLog SiteEventLog stores details of Site.com requests. Requests can originate from the browser (UI). This object is available in API version 62.0

and later.


Standard Objects SiteEventLog

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
ClientIp

CpuTime

DatabaseTotalTime

HttpHeaders

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

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
The HTTP headers that were sent in the request.


Standard Objects SiteEventLog

**Field** **Details**

```
HttpMethod

IsApi

IsError

IsFirstRequest

IsGuest

IsSecure

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The HTTP method of the request. For example: GET, POST, PUT, and so on.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
True if this page was an error page.

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
True if this page is the first Visualforce transaction in the request.

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
True if this page was a guest (unauthenticated) request.

The default value is `false` .

**Type**
boolean


Standard Objects SiteEventLog

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
True if this request is secure.

The default value is `false` .

```
LoginKey

PageName

QueryString

RequestIdentifier

RequestStatus

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring. For example:
GeJCsym5eyvtEK2I.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the Visualforce page that was requested.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The SOQL query, if one was performed.

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


Standard Objects SiteEventLog

**Field** **Details**

**Description**
The status of the request for a page view or user interface action. This field can have a blank
value.

For example:

**•** `S`                   - Success. Salesforce handled the request successfully. If an Apex controller throws
an exception, this status is also returned.

**•** `F`                   - Failure. Typically 4xx or 5xx HTTP codes, such as no permission to view page, page
took too long to render, page is read-only.

**•** `U`                   - Undefined.

**•** `A` —Authorization error.

**•** `R`                   - Redirect. Typically a 3xx HTTP code, possibly initiated by an Apex controller in a
Visualforce page.

**•** `N` —Not Found. 404 error.

```
RequestType

RunTime

SessionKey

```

**Type**
String

**Description**
The request type.

Possible values are:

**•** `page` —a normal request for a page

**•** `content_UI` —a content request for a page that originated in the user interface

**•** `content_apex` —a content request initiated by an Apex call

**•** `PDF_UI` —a request for a page in PDF format through the user interface

**•** `PDF_apex` —a request for PDF format by an Apex call (usually a Web Service call)

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


Standard Objects SiteEventLog

**Field** **Details**

```
SiteIdentifier

Timestamp

Uri

UserIdentifier

UserType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the Site.com site.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT. For example: `20130715233322.670` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URI of the page that’s receiving the request. For example: `home/home.jsp` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 18-character ID of the user who’s using Salesforce services through the UI or the API.
For example: `00530000009M943YAS` .

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


### Standard Objects SiteHistory

**Field** **Details**

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

### SiteHistory

Represents the history of changes to the values in the fields of a site. This object is generally available in API version 18.0 and later.

To access this object, Salesforce Sites must be enabled for your organization.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Special Access Rules

**•** Customer Portal users can't access this object.

**•** To view this object, you must have the “View Setup and Configuration” permission.

Fields

**Field** **Details**

```
DataType

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Data type of the field that was changed.


### Standard Objects SiteIframeWhitelistUrl

**Field** **Details**

```
Field

NewValue

OldValue

SiteId

```

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
The last value of the field before it was changed.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the associated Site.

This is a relationship field.

**Relationship Name**
### Site

**Relationship Type**
Lookup

**Refers To**
### Site

### SiteIframeWhitelistUrl

Represents a list of external domains that you allow to frame your Salesforce site or Experience Cloud site pages. This object is available
in API version 44.0 and later.


### Standard Objects SiteRedirectMapping

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

**•** Customer Portal users can’t access this object.

**•** To view this object, you must have the “View Setup and Configuration” permission.

Fields

**Field Name** **Details**

```
SiteId

Url

### SiteRedirectMapping

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the site to include in the inline frame.

This is a relationship field.

**Relationship Name**
### Site

**Relationship Type**
Lookup

**Refers To**
### Site

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The domain allowed to frame your Salesforce site or Experience Cloud site page.
Accepts these formats: example, example.com, *example.com, and
https://example.com.

Represents a site redirect from an external site to an Experience Cloud site. This object is available in API version 52.0 and later.


Standard Objects SiteRedirectMapping

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

This object is available only if Digital Experiences is enabled for your org and Create and Set Up Experiences is enabled.

Fields

**Field** **Details**

```
Action

IsActive

IsDynamic

SiteId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of the redirect.

Possible values are:

**•** `Permanent`

**•** `Temporary`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the redirect is enabled.

Default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a redirect rule is dynamic.

Default value is `false` . This field is available in API version 57.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


### Standard Objects Skill

**Field** **Details**

**Description**
The ID of the site for the redirect.

This field is a relationship field.

**Relationship Name**
Site

**Relationship Type**
Lookup

**Refers To**
Site

```
Source

Target

```

Usage

**Type**
url

**Properties**
Create, Filter, Sort

**Description**
The URL of the site you want to redirect.

**Type**
url

**Properties**
Create, Filter, Sort

**Description**
The URL of the Experience Cloud site you want to users to visit.

If you build a new site on Experience Cloud but you also have an old site on a different platform, ensure that users visit the new site. Use
SiteRedirectMapping to redirect users from the external site to the Experience Cloud site.

### Skill

Represents a category or group of Chat users or service resources in Field Service or Workforce Engagement. This object is available in
API version 24.0 and later.

Note: For information about WDC skills on a user's profile, see the ProfileSkill topic.

Supported Calls

`create()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects Skill

Fields

**Field Name** **Details**

```
Description

DeveloperName

Language

LastViewedDate

MasterLabel

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the skill.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with
a letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. In managed packages, this field prevents naming
conflicts on package installations. With this field, a developer can change the
object’s name in a managed package and the changes are reflected in a
subscriber’s organization.

When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance slows down
while Salesforce generates one for each record.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The language of the skill.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed the skill.

**Type**
string


### Standard Objects SkillLevelDefinition

**Field Name** **Details**

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**

The name of the skill.

```
TypeId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The skill type associated with the skill.

This field is a relationship field.

This field is available in API version 58.0 and later.

**Relationship Name**
Type

**Refers To**
SkillType

**Chat**
Use this object to assign Chat users to groups based on their abilities. The skills associated with a LiveChatButton determine which
agents receive chat requests that come in through that button.

**Field Service**
Use this object to track certifications and areas of expertise in your workforce. After you create a skill, you can:

**•** Assign it to a service resource via the Skills related list on the resource’s detail page. When you assign a skill to a service resource,
you can specify their skill level and the duration of the skill.

**•** Add it as a required skill via the Skill Requirements related list on any work type, work order, or work order line item. When you
add a required skill to a work record, you can specify the skill level.

**Workforce Engagement**
Use this object to specify areas of expertise in your workforce. After you create a skill, you can:

**•** Assign it to a service resource via the Skills related list on the resource’s detail page.

**•** Add it as a required skill via the Skill Requirements related list on a job profile.

### SkillLevelDefinition

Represents a skill which can be acquired by completing enablement site (myTrailhead) modules. This object is available in API version
51.0 and later.


Standard Objects SkillLevelDefinition

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The org must have a Workforce Engagement license and an Enablement Sites (myTrailhead) license. User must have at least one Workforce
Engagement permission set assigned to them: Workforce Engagement Analyst, Workforce Engagement Planner, Workforce Engagement
Agent.

Fields

**Field** **Details**

```
Description

IsAutoApproved

LearningContent

OwnerId

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Describes the mapping.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Whether this mapping auto-approves.

The default value is 'false'.

**Type**
string

**Properties**
Filter, Nillable

**Description**
The titles of the Trailhead modules associated to this mapping.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The user who owns the Skill Level Definition.

This is a polymorphic relationship field.


### Standard Objects SkillLevelProgress

**Field** **Details**

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

```
SkillId

### `SkillLevel`

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The skill that this mapping is for.

This is a relationship field.

**Relationship Name**
### Skill

**Relationship Type**
Lookup

**Refers To**
### Skill

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The level to assign for the skill.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SkillLevelDefinitionOwnerSharingRule on page 65**
Sharing rules are available for the object.

**SkillLevelDefinitionShare on page 67**
Sharing is available for the object.

### SkillLevelProgress

Represents training progress for a given user. This object is available in API version 51.0 and later.


Standard Objects SkillLevelProgress

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The org must have a Workforce Engagement license and an Enablement Sites (myTrailhead) license. User must have at least one Workforce
Engagement permission set assigned to them: Workforce Engagement Analyst, Workforce Engagement Planner, Workforce Engagement
Agent.

Fields

**Field** **Details**

```
CompletedCount

CompletedDate

OwnerId

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Number of modules that have been completed towards this Skill Mapping.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date when this progress was completed.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of skill level progress.

This is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User


Standard Objects SkillLevelProgress

**Field** **Details**

```
ServiceResourceId

SkillLevelDefinitionId

SkillMasterLabel

Status

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The Service Resource that will be granted a service resource skill when the progress is
complete.

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
The corresponding skill mapping for this progress.

This is a relationship field.

**Relationship Name**
SkillLevelDefinition

**Relationship Type**
Lookup

**Refers To**
SkillLevelDefinition

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The master label of the Skill associated with the associated SkillLevelDefinition.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update


### Standard Objects SkillProfile

**Field** **Details**

**Description**
Represents the status of the progress.

Possible values are:

**•** `A` —Approved

**•** `R` —Review

### • S —Started

The default value is 'S'.

```
TotalCount

```

Associated Objects

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The total number of modules that need to be completed.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SkillLevelProgressOwnerSharingRule on page 65**
Sharing rules are available for the object.

**SkillLevelProgressShare on page 67**
Sharing is available for the object.

### SkillProfile

Represents a join between Skill and Profile. This object is available in API version 24.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `update()`, `retrieve()`

Fields

**Field Name** **Details**

```
ProfileId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort


### Standard Objects SkillRequirement

**Field Name** **Details**

**Description**

The ID of the profile.

```
SkillId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The ID of the skill.

Use this object to assign specific skills to specific profiles.

### SkillRequirement

Represents a skill that is required to complete a particular task in Field Service, Omni-Channel, Salesforce Scheduler, or Workforce
Engagement. Skill requirements can be added to pending service routing objects in Omni-Channel. They can be added to work types,
work orders, and work order line items in Field Service and Lightning Scheduler. And they can be added to job profiles in Workforce
Engagement. This object is available in API version 38.0 and later. You also can add skill requirements to work items in Omni-Channel
skills-based routing using API version 42.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `update()`, `upsert()`

Special Access Rules

If you want to use SkillRequirement for Field Service use cases, then Field Service must be enabled.

If you want to use SkillRequirement only for Omni-Channel skills-based routing use cases, then you don't need Field Service to be enabled.

If you want to use SkillRequirement for Workforce Engagement use cases, then Workforce Engagement must be enabled.

Fields

**Field Name** **Details**

```
IsAdditionalSkill

```

**Type**
boolean


Standard Objects SkillRequirement

**Field Name** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates that a skill is additional. After a designated timeout period, a skill marked
as additional is dropped from Omni-Channel routing. The case is then routed to
the best-matched agent even if they don’t have all the skills.

```
LastReferencedDate

LastViewedDate

RelatedRecordId

SkillId

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
The timestamp when the current user last viewed this record. If this value is null,
this record might only have been referenced ( `LastReferencedDate` ) and
not viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The record that the skill is required for. The related record can be a work order,
work order line item, work type, or pending service routing record.

This is a polymorphic relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
WorkOrder, WorkOrderLineItem, WorkType

**Type**
reference


Standard Objects SkillRequirement

**Field Name** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The skill that is required.

This is a relationship field.

**Relationship Name**
Skill

**Relationship Type**
Lookup

**Refers To**
Skill

```
SkillLevel

SkillNumber

SkillPriority

```

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
The level of the skill required. Skill levels can range from zero to 99.99. Depending
on your business needs, you can have the skill level to reflect years of experience,
certification levels, or license classes.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated number identifying the skill requirement.

**Type**
int

**Properties**
Aggregatable, Create, Filter, Group, Nillable, Sort, Update

**Description**
For additional skills, specify the order in which skills are dropped if after the
specified timeout no agent with that skill is available. Higher priority-value skills
are dropped first. Lower priority-value skills, for example 0, are dropped last. Skills
with the same priority value are dropped as a group. You can set skill priority
using skills-based routing rules or Apex code.


### Standard Objects SkillUser

Usage

**Field Service**
Skill requirements help dispatchers assign work orders to service resources with the proper expertise. You can still assign a work order,
work order line item, or related service appointment to a service resource that does _not_ have the specified skills, so skill requirements
serve more as a suggestion than a rule.

Note: If you’re using the Field Service managed package, use matching rules to ensure that appointments are only assigned to
service resources who possess the skills listed on the parent work order.

If many of your work orders require the same skills, add skill requirements to work types to save time and keep your processes consistent.
When you add a skill requirement to a work type, work orders and work order line items that use that type automatically inherit the skill
requirement. For example, if all annual maintenance visits for your Classic Refrigerator product require a Refrigerator Maintenance skill
level of at least 50, add that skill requirement to the Annual Maintenance Visit work type. When you create a work order for a customer’s
annual fridge maintenance, applying that work type adds the skill requirement as well.

**Omni-Channel**

We recommend that you use Omni-Channel flow or skills-based routing rules to create skills-based routing requests. When you do so,
work items are routed by creating a PendingServiceRouting object. The PendingServiceRouting object can have multiple SkillRequirements
objects associated with it. When a work item requires multiple skills, it’s routed to an agent who has all of the required skills. The
PendingServiceRouting object adds attributes to the work item that represent the skill (skill id), priority, skill proficiency, and timestamp.

**Workforce Engagement**

Workforce Engagement uses skill requirements to assign shifts to agents who have the right skills. You can still assign shifts to service
resources if they don’t have those skills.

In a non-Omni workflow, create a scheduling rule that matches agents to shifts based on their skills and the job profile's skill requirements.
Shift scheduling tools can then assign agents with the right skills.

Associated Objects

This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**SkillRequirementChangeEvent (API version 54.0)**
Change events are available for the object.

**SkillRequirementFeed**

Feed tracking is available for the object.

**SkillRequirementHistory**

History is available for tracked fields of the object.

### SkillUser

Represents a join between Skill and User. This object is available in API version 24.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `update()`, `query()`, `retrieve()`


### Standard Objects SlackChannelRelatedRecord

Fields

**Field Name** **Details**

```
SkillId

UserId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The ID of the skill.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The ID of the user.

Use this object to assign specific skills to specific users.

### SlackChannelRelatedRecord

Represents the related record mapping between a Slack channel and a Salesforce record that’s made when you create a Salesforce
channel. This object is available in API version 65.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
Name

```

**Type**
string

**Properties**
Filter, Sort

**Description**
The name of the related record mapping.


### Standard Objects SlaProcess

**Field** **Details**

```
RelatedRecord

SlackChannel

TopLevelTeam

```

Usage

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The Salesforce record ID associated with the related record mapping.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Slack channel ID of the Salesforce channel associated with the related record mapping.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Slack Enterprise org ID associated with the Salesforce channel.

Use this object to retrieve and query the related record mapping between a Slack channel and a Salesforce record. You can select this
object in Salesforce Flow Builder and Slack Workflow Builder to trigger actions when a Salesforce channel is created.

This object is read only. You can’t create, modify, or delete the related record mappings between Slack channels and Salesforce records
using this object.

### SlaProcess

Represents an entitlement process associated with an Entitlement. This object is available in API version 19.0 and later.

An entitlement process is a timeline that includes all the steps (MilestoneType records) that your support team must complete to resolve
cases. Each process includes the logic necessary to determine how to enforce the correct service level for your customers.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`, `search()`, `describeLayout()`


Standard Objects SlaProcess

Special Access Rules

As of Summer ’20 and later, only Salesforce admin users, users with access to the Case, Entitlement, or Work Order objects, and users
with the View Setup and Configuration permission can access this object.

Fields

**Field** **Details**

```
BusinessHoursId

Description

IsActive

IsVersionDefault

LastViewedDate

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Required. ID of the BusinessHours associated with the entitlement. Must be a valid
business hours ID.

**Type**
textarea

**Properties**
Filter, Nillable

**Description**
A description of the entitlement process.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the entitlement process is active ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the entitlement process is the default version ( `true` ) or not
( `false` ).

This field is available in API version 28.0 and later in organizations that have entitlement
versioning enabled.

**Type**
dateTime


Standard Objects SlaProcess

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The date when the SlaProcess was last viewed.

```
Name

NameNorm

SObjectType

StartDateField

```

**Type**
string

**Properties**
Filter, idLookup

**Description**
The name of the entitlement process.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The read-only value for the unique name of the entitlement process or the entitlement
process version. If entitlement versioning is enabled, this value is automatically
generated for each version of an entitlement process in this form: _`process`_
_`name`_ +_v + _`x`_, where _`x`_ is the version number (for example, “gold_support_v2”).

If entitlement versioning isn’t enabled, this value is the same as `Name` .

This field is available in API version 28.0 and later.

**Type**
picklist

**Properties**
Restricted picklist, Filter, Group, Sort

**Description**
The type of records that the entitlement process can run on. Its values are:

**•** _`Case`_

**•** _`Work Order`_

An entitlement process runs only on records that match its type. For example, a Case
entitlement process that’s applied to an entitlement runs only on cases associated
with the entitlement, not on work orders. As a best practice, therefore, manage
customers’ work orders and cases on separate entitlements.

The field label in the user interface is Entitlement Process Type.

**Type**
picklist


Standard Objects SlaProcess

**Field** **Details**

**Properties**
Filter, Restricted picklist

**Description**
The criteria for cases to enter the entitlement process. Cases can enter the process
based on:

**•** The creation date on a case

**•** A custom date/time field on a case

```
VersionMaster

VersionNotes

VersionNumber

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Identifies the sequence of versions to which this entitlement process belongs. This
field’s contents can be any value as long as it is identical among all versions of the
entitlement process.

This field is available in API version 28.0 and later in organizations that have entitlement
versioning enabled.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
The description of the entitlement process version.

This field is available in API version 28.0 and later in organizations that have entitlement
versioning enabled.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version number of the entitlement process. Must be 1 or greater.

This field is available in API version 28.0 and later in organizations that have entitlement
versioning enabled.


### Standard Objects Snippet

Usage

Use this object to query entitlement processes on entitlements.

SEE ALSO:

Entitlement

MilestoneType

CaseMilestone

### Snippet

Represents a snippet, which is a container for rich text that can be reused across Account Engagement emails and email templates. This
object is available in API version 47.0 and later.

Supported Calls

`create(),delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

### Snippets are available in Account Engagement business units with the Sales, CRM, or Service permission set license.

Fields

**Field** **Details**

```
Description

DeveloperName

LastReferencedDate

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the snippet. Limited to 32 KB.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. This field value is unique to your org and is required for a Snippet to be resolved
in marketing content. Label is **API Name** .

**Type**
dateTime


Standard Objects Snippet

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

```
LastViewedDate

Name

Type

Value

```

Associated Objects

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
Required. The name of the snippet.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of content a snippet includes. Allowable values are: Date, Image, Link, Text. This
field is for organizational purposes.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The body content of a snippet. This field can contain plain or rich text. The value of a snippet
is resolved when a marketing email is sent. The field does not support emojis, HTML, or image
files.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.


### Standard Objects SnippetAssignment

**SnippetFeed**

Feed tracking is available for the object.

### SnippetAssignment

Represents a relationship between a snippet and a campaign. Assignments are required to use snippet content in Account Engagement
emails and email templates. A snippet can be assigned to more than one campaign. This object is available in API version 47.0 and later.

Supported Calls

create( ), delete( ), describeLayout( ), describeSObjects( ), getDeleted( ), getUpdated( ), query( ), retrieve( )

Special Access Rules

Snippets are available in Account Engagement business units with the Sales, CRM, or Service permission set license.

Fields

**Field** **Details**

```
ParentId

SnippetId

### SoapApiEventLog

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the parent object

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the related snippet record

SOAP API events contain details about your org's SOAP API request activity. This object is available in API version 61.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)


Standard Objects SoapApiEventLog

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
ApiType

ClientIp

ClientName

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of API request.

Possible values are:

**•** `D` —Apex Class

**•** `E` —SOAP Enterprise

**•** `M` —SOAP Metadata

**•** `P` —SOAP Partner

**•** `S` —SOAP Apex

**•** `T` —SOAP Tooling

**•** `f` —Feed

**•** `l` —Live Agent

**•** `p` —SOAP ClientSync

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


Standard Objects SoapApiEventLog

**Field** **Details**

**Description**
The name of the client that’s using Salesforce services. This field is an optional parameter
that can be passed in API calls. If blank, the caller didn't specify a client in the CallOptions
header.

```
CpuTime

DatabaseBlocks

DatabaseCpuTime

DatabaseTotalTime

ExceptionMessage

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


Standard Objects SoapApiEventLog

**Field** **Details**

**Description**
The exception message for a SOAP API request. An exception message gives details about
errors in handling an API request, such as why an API request failed. For example:
common.exception.ApiException: startDate cannot be more than 30 days ago.

```
LoginKey

MethodName

ObjectName

RequestIdentifier

RequestSize

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
Filter, Group, Nillable, Sort

**Description**
The name of the object accessed by the API request. For example: `Account`,
`Opportunity`, `Contact`, and so on.

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


Standard Objects SoapApiEventLog

**Field** **Details**

**Description**
The size of the callout request body, in bytes.

```
RequestStatus

ResponseSize

RowsProcessed

RunTime

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
The amount of time that the request took in milliseconds.


Standard Objects SoapApiEventLog

**Field** **Details**

```
SessionKey

Timestamp

Uri

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


### Standard Objects SocialPersona

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

### SocialPersona

Represents a snapshot of a contact's profile on a social network such as Facebook or Twitter. This object is available in API version 22.0
and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
AreWeFollowing

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether a Salesforce social account is following the social persona or
not.


Standard Objects SocialPersona

**Field Name** **Details**

```
AuthorLabels

AvatarUrl

Bio

ExternalId

ExternalPictureURL

Followers

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Comma-separated list of author type tags.

**Type**
string

**Properties**
Nillable

**Description**
Retrieves the user's social network avatar. It's a read-only field and you can't
specify or update its value.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Biography of the social persona.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the social persona on the social network.

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
URL to the picture of the social persona on the social network.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects SocialPersona

**Field Name** **Details**

**Description**
Number of followers that the social persona has.

```
Following

InfluencerScore

IsBlacklisted

IsDefault

IsFollowingUs

IsVerified

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of people that the social persona is following.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Radian6 score describing the influence of the social persona. No longer used.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether the social persona is blacklisted or not.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether the social persona supplies the default avatar image that’s
displayed on the contact or account.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether the social persona is following a Salesforce social account or
not.

**Type**
boolean


Standard Objects SocialPersona

**Field Name** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether the social persona is verified or not.

```
LastReferencedDate

LastViewedDate

ListedCount

MediaProvider

MediaType

Name

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when the social persona was last referenced.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when the social persona was last viewed.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Radian6 field. No longer used.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Social network of the social persona.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Social network type of the social persona.

**Type**
string


Standard Objects SocialPersona

**Field Name** **Details**

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the social persona.

```
NumberOfFriends

NumberOfTweets

ParentId

ProfileType

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of friends that the social persona has.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of tweets made by the social persona.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the contact parent record for the social persona.

This is a polymorphic relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Account, Contact, Lead, SocialPost

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Type of profile. Values are:

**•** `Person`

**•** `Page`


Standard Objects SocialPersona

**Field Name** **Details**

```
ProfileUrl

Provider

R6SourceId

RealName

SourceApp

TopicType

```

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
URL for the profile.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Social network, such as Facebook or Twitter, of the social persona.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the social persona in Social Studio.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Real name of the social persona.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Salesforce product that created the social persona.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Type of topic, such as keyword or managed.


### Standard Objects SocialPost

Usage

The fields on a SocialPersona object don’t provide real-time data. They provide a snapshot of information from the last time Salesforce
collected a post from the social persona. Many of the Radian6-related fields are no longer accurate or used.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**SocialPersonaHistory (API version 26.0)**
History is available for tracked fields of the object.

### SocialPost

Represents a snapshot of a post on a social network such as a Facebook or Twitter. This object is available in API version 23.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
AnalyzerScore

AssignedTo

AttachmentType

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Score set on the social post in Social Studio.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
User in Social Studio that the social post is assigned to.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Type of the first attachment on the social post. Values are:


Standard Objects SocialPost

**Field Name** **Details**

**•** `APPLICATION`

**•** `AUDIO`

**•** `IMAGE`

**•** `LINK`

**•** `TEXT`

**•** `UNKNOWN`

**•** `VIDEO`

```
AttachmentUrl

Classification

CommentCount

Content

DeletedById

```

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
URL for the first attachment on the social post.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Classification for the social post, such as inquiry or customer case.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of comments on the social post.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Body of the social post.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects SocialPost

**Field Name** **Details**

**Description**
If the social post is deleted, ID of the person who deleted the social post.

This is a relationship field.

**Relationship Name**
DeletedBy

**Relationship Type**
Lookup

**Refers To**
User

```
EngagementLevel

ExternalPostId

Handle

HarvestDate

Headline

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Engagement level of the social post, such as reviewed or resolved.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the social post in its social network.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Handle of the person who posted the social post.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date and time when Social Studio collected the social post.

**Type**
string


Standard Objects SocialPost

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Headline of the social post.

```
HiddenById

InboundLinkCount

IsOutbound

KeywordGroupName

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If the social post is hidden, ID of the person who hid it.

This is a relationship field.

**Relationship Name**
HiddenBy

**Relationship Type**
Lookup

**Refers To**
User

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of links on the inbound social post.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether the social post is outbound or not.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Radian6 field that is no longer used.


Standard Objects SocialPost

**Field Name** **Details**

```
Language

LastReferencedDate

LastViewedDate

LikedBy

LikesAndVotes

MediaProvider

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Language of the social post.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date when the social post was last referenced.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date when the social post was last viewed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the managed social account in the social network that liked the social post.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Radian6 number of likes and votes on the social post.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Social network of the social post.


Standard Objects SocialPost

**Field Name** **Details**

```
MediaType

MessageType

Name

Notes

OutboundSocialAccountId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Type of social network of the social post.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Type of message. Values are:

**•** `Comment` —Facebook comment

**•** `Direct` —Twitter direct message

**•** `Post` —Facebook post

**•** `Private` —Facebook private message

**•** `Reply` —Twitter or Facebook reply

**•** `Retweet` —Twitter retweet

**•** `Tweet` —Twitter tweet

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the social post.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Notes added by Social Hub actions for the social post.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the social account used for outbound social posts.


Standard Objects SocialPost

**Field Name** **Details**

This is a relationship field.

**Relationship Name**
OutboundSocialAccount

**Relationship Type**
Lookup

**Refers To**
ExternalSocialAccount

```
OwnerId

ParentId

PersonaId

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of the social post.

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
ID of the parent record of the social post, for example, the ID of a case.

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
Create, Filter, Group, Nillable, Sort, Update


Standard Objects SocialPost

**Field Name** **Details**

**Description**
ID of the social persona who made the post.

This is a relationship field.

**Relationship Name**
Persona

**Relationship Type**
Lookup

**Refers To**
SocialPersona

```
PostPriority

PostTags

PostUrl

Posted

Provider

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Priority of the social post set in Social Studio.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Comma-separated list of tags on the social post.

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
URL for the social post.

**Type**
dateTime

**Properties**
Create, Defaulted on create, Filter, Sort, Update

**Description**
Date and time when the social post was made.

**Type**
picklist


Standard Objects SocialPost

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Social network of the social post.

```
R6PostId

R6SourceId

R6TopicId

Recipient

RecipientType

ReplyToId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
Unique ID of the post in Social Studio.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the author in Social Studio.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID for either the topic profile or the managed account in Social Studio.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the recipient of the social post in Social Studio.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Type of the recipient of the social post, such as a person.

**Type**
reference


Standard Objects SocialPost

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Dynamically generated from replyToExternalPostId in Social Studio.

This is a relationship field.

**Relationship Name**
ReplyTo

**Relationship Type**
Lookup

**Refers To**
SocialPost

```
ResponseContextExternalId

ReviewScale

ReviewScore

ReviewedStatus

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
External ID, such as a conversation ID, author ID, or post ID, for the item you’re
responding to.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Review scale for the social post.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Review score for the social post.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Status of the social post review.


Standard Objects SocialPost

**Field Name** **Details**

```
Sentiment

Shares

SourceTags

SpamRating

Status

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Sentiment of the social post. Values are:

**•** `Negative`

**•** `Neutral`

**•** `Positive`

**•** `SomewhatNegative`

**•** `SomewhatPositive`

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of times the social post has been shared.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Comma-separated list of author type tags.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Spam rating of the social post. Values are:

**•** `NotSpam`

**•** `Spam`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects SocialPost

**Field Name** **Details**

**Description**
Status of the social post. Values are:

**•** `DELETED`

**•** `FAILED`

**•** `HIDDEN`

**•** `PENDING`

**•** `PENDING_APPROVAL`

**•** `RECALL_APPROVAL`

**•** `REJECTED_APPROVAL`

**•** `REPLIED`

**•** `SENT`

**•** `UNKNOWN`

```
StatusMessage

ThreadSize

TopicProfileName

TopicType

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Status message for the social post.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Radian6 field. No longer used.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Name of the topic profile for the social post in Social Studio.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Type of topic. Values are:


Standard Objects SocialPost

**Field Name** **Details**

**•** `Keyword`

**•** `Managed`

```
TruncatedContent

UniqueCommentors

ViewCount

WhoId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Truncated content of the social post.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of unique people who commented on the social post.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of times the social post was viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Polymorphic ID of a person such as a lead or a contact.

This is a polymorphic relationship field.

**Relationship Name**
Who

**Relationship Type**
Lookup

**Refers To**
Account, Contact, Lead


### Standard Objects Solution

Usage

The fields on a SocialPost object don’t provide real-time data. They provide a snapshot of information from the last time Salesforce
collected the post from the social network. Many of the Radian6-related fields are no longer accurate or used.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SocialPostChangeEvent (API version 48.0)**
Change events are available for the object.

**SocialPostFeed (API version 26.0)**
Feed tracking is available for the object.

**SocialPostHistory (API version 26.0)**
History is available for tracked fields of the object.

**SocialPostOwnerSharingRule**

Sharing rules are available for the object.

**SocialPostShare**

Sharing is available for the object.

### Solution

Represents a detailed description of a customer issue and the resolution of that issue.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
IsDeleted

IsHtml

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


Standard Objects Solution

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the Solution is an HTML solution ( `true` ) or not ( `false` ).

```
IsOutOfDate

IsPublished

IsPublishedInPublicKb

IsReviewed

```

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Read-only field that indicates whether a solution master has been updated since the translated
version was created ( `true` ) or not ( `false` ). Note that this field does not appear in the page
layout of master solutions.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the Solution has been published ( `true` ) or not ( `false` ). A solution’s
published state does not affect how it can be used, or whether you can query, update, or
delete it. Label is **Public** . Prior to Spring ‘14, the label was **Visible in Self-Service Portal**

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the Solution has been published as a Public Solution ( `true` ) or not
( `false` ). Label is **Visible in Public Knowledge Base** .

This field only applies to solutions, not articles in the public knowledge base.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the Solution has been reviewed ( `true` ) or not ( `false` ). This flag can
only be set indirectly via the `Status` picklist. Each predefined `Status` value implies an
`IsReviewed` value. Label is **Reviewed** .


Standard Objects Solution

**Field** **Details**

```
LastReferencedDate

LastViewedDate

OwnerId

ParentId

RecordTypeId

```

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last interacted with this record, directly or indirectly.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it’s possible that the user only accessed this record or list view ( `LastReferencedDate` ),
but not viewed it.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the User who owns the Solution.

This is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Update

**Description**
ID of the master solution, if this is the translation of a master solution.

**Type**
reference

**Properties**
Create, Filter, Nillable, Update


Standard Objects Solution

**Field** **Details**

**Description**
ID of the RecordType to which the Solution is associated.

```
SolutionLanguage

SolutionName

SolutionNote

```

**Type**
picklist

**Properties**
Create, Filter, Restricted picklist, Update

**Description**
The language that the solution is written in, such as `French` or `Chinese`
`(Traditional)` .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. If a client application creates a new Solution and a value for this field is unspecified,
a hyphen (-), the default value for this field, is used. Limit: 255 characters. Label is **Title** .

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The details of the Solution record. Limit: 32,000 characters. Label is **Solution Details** . If you
have HTML Solutions enabled, any HTML tags used in this field are verified before the object
is created or updated. If invalid HTML is entered, an error is thrown. Any JavaScript used in
this field is removed before the object is created or updated.

SolutionNote operates as a special type of String. If you have HTML Solutions enabled, any
HTML tags used in this field are verified before the object is created or updated. If invalid
HTML is entered, an error is thrown. Any JavaScript used in this field is removed before the
object is created or updated.

In the following example, when the Solution displays on a detail page, the SolutionNote field
has H1 HTML formatting applied to it:

```
  trigger t on Solution (before insert) {

         Trigger.new[0].SolutionNote ='<h1>hello</h1>';

  }

```

In the following example, when the Solution displays on a detail page, the SolutionNote field
only contains _`HelloGoodbye`_ :


Standard Objects Solution

**Field** **Details**

```
                       '<javascript>Hello</javascript>Goodbye';

                    }

```

[For more information, see HTML Solutions Overview in Salesforce Help.](https://help.salesforce.com/s/articleView?id=service.sol_html_def.htm&type=5&language=en_US)

```
SolutionNumber

Status

TimesUsed

```

Usage

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
An identifying number that is assigned automatically when a solution is created. It can’t be
set directly, and it can’t be modified.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Required. The status of the solution. Directly controls the `IsReviewed` value. To obtain
the status values in the picklist, a client application can query the SolutionStatus.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Number of times this solution has been used. Label is **Num Related Case** .

Use this object to manage your organization’s solutions. Client applications can create, update, delete, and query Attachment records
associated with a solution.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**SolutionFeed (API version 18.0)**
Feed tracking is available for the object.


### Standard Objects SolutionStatus

**SolutionHistory**

History is available for tracked fields of the object.

SEE ALSO:

CategoryData

CategoryNode

### SolutionStatus

Represents the status of a Solution, such as Draft, Reviewed, and so on.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ApiName

IsDefault

IsReviewed

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
Indicates whether this is the default solution status value ( `true` ) or not ( `false` ) in the
picklist. Only one value can be the default value.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this solution status value represents a reviewed Solution ( `true` ) or not
( `false` ). Multiple solution status values can represent a reviewed Solution.


### Standard Objects SolutionTag

**Field** **Details**

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
Label for this solution status value. This display value is the internal label that does not get
translated.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number used to sort this value in the solution status picklist. These numbers are not
guaranteed to be sequential, as some previous solution status values might have been
deleted.

This object represents a value in the solution status picklist. The solution status picklist provides additional information about the status
of a Solution, such as whether a given status value represents a reviewed or unreviewed solution. Your client application can query this
object to retrieve the set of values in the solution status picklist, and then use that information while processing Solution objects to
determine more information about a given solution. For example, the application could test whether a given case has been reviewed
or not based on its `Status` value and the value of the `IsReviewed` property in the associated SolutionStatus record.

SEE ALSO:

### Solution SolutionTag

Associates a word or short phrase with a Solution.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`


Standard Objects SolutionTag

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

SolutionTag stores the relationship between its parent TagDefinition and the Solution being tagged. Tag objects act as metadata, allowing
users to describe and organize their data.


### Standard Objects SOSDeployment

When a tag is deleted, its parent TagDefinition will also be deleted if the name is not being used; otherwise, the parent remains. Deleting
a TagDefinition sends it to the Recycle Bin, along with any associated tag entries.

### SOSDeployment

Represents the general settings for deploying SOS video call capability in a native mobile application. This object is available in API
version 34.0 and later.

Supported Calls

`create()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

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
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with
a letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. In managed packages, this field prevents naming
conflicts on package installations. With this field, a developer can change the
object's name in a managed package and the changes are reflected in a
subscriber's organization.

When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance slows down
while Salesforce generates one for each record.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the deployment.

**Type**
string


Standard Objects SOSDeployment

**Field Name** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the deployment.

```
OptionsIsBackwardFacingCameraEnabled

OptionsIsEnabled

OptionsIsVoiceOnlyMode

QueueId

```

Usage

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Determines whether customers can use the backwards-facing camera on their
mobile devices to talk to SOS agents.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Determines whether the deployment is enabled for customers to request new
SOS video calls.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Determines whether video functionality is disabled for customers, making it so
customers can only talk to SOS agents using only audio.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the queue that’s associated with the SOS deployment.

Use this object to query and manage SOS deployments.


### Standard Objects SOSSession SOSSession

This object is automatically created for each SOS session and stores information about the session. This object is available in API versions
34.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
AppVersion

CaseId

ContactId

DeploymentId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The version of the customer’s mobile application in which SOS is implemented.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the case that’s associated with the SOS session.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the contact that’s associated with the SOS session.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the SOS deployment that the SOS session originated from.


Standard Objects SOSSession

**Field Name** **Details**

```
EndTime

IpAddress

LastReferencedDate

LastViewedDate

Name

OpentokSession

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time that the SOS session ended.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
To protect the customer’s privacy, this field is now blank.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the session record was last referenced by a user.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the session record was last viewed.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
The name of the session.

**Type**
encryptedstring

**Properties**
Create, Nillable, Update

**Description**
The ID of the OpenTok session that’s associated with the SOS video call.


Standard Objects SOSSession

**Field Name** **Details**

```
OwnerId

SessionDuration

SessionRecordingUrl

SosVersion

StartTime

SystemInfo

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the session record’s owner.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The amount of time that the SOS session lasted.

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The URL where the SOS session recording is stored.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The version of SOS that was used in your organization’s mobile application when
this session occurred.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time that the SOS session began.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects SOSSessionActivity

**Field Name** **Details**

**Description**
Information about the customer’s mobile device from which the SOS call
originated, such as the device’s operating system.

```
WaitDuration

```

Usage

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The amount of time the customer waited before an agent accepted the SOS
session and the call began.

Use this object to query and manage SOS session records.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**SOSSessionFeed**

Feed tracking is available for the object.

**SOSSessionHistory**

History is available for tracked fields of the object.

**SOSSessionOwnerSharingRule**

Sharing rules are available for the object.

**SOSSessionShare**

Sharing is available for the object.

### SOSSessionActivity

Captures information about specific events that occur during an SOS video call, such as when an SOS call begins or ends. This object is
available in API version 34.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`


### Standard Objects StagedEmail

Fields

**Field Name** **Details**

```
ActivityTime

Name

SessionId

Type

```

Usage

**Type**
dateTime

**Properties**
Create, Filter, Sort

**Description**
The time at which the activity occurred.

**Type**
string

**Properties**
Autonumber, Defaulted on create, idLookup, Filter, Sort

**Description**
The name of the activity.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the SOS session that’s associated with the event.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The kind of activity that occurred.

Use this object to query and manage SOS session activities.

### StagedEmail

For internal use only.


### Standard Objects StagedInviteeEmail StagedInviteeEmail

Represents an email address that is included on a calendar event but that doesn’t match an existing user, contact, or lead record. This
object is available in API version 66.0 and later.

Supported Calls

`delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`

Special Access Rules

This object is available with Einstein Activity Capture when Sync Email as Salesforce Activity is turned on.

Fields

**Field** **Details**

```
Name

OwnerId

```

**Type**
email

**Properties**
Filter, Group, idLookup, Sort

**Description**
The invited email address.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the record owner.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

### StagedUnmtchdEmailAddr

Represents data about an email address identified by Einstein Activity Capture that doesn’t match to an existing user, contact, or lead
record. These addresses are only stored temporarily. Related to StagedUnmtchdEmailAddrRela, which represents data about the email
message or calendar event activity associated with an unmatched email. This object is available in API version 66.0 and later.


Standard Objects StagedUnmtchdEmailAddr

These addresses are only stored temporarily. An unmatched email address is automatically deleted from StagedUnmtchdEmailAddr if
it converts into a contact record. To convert, a user saves it from their Suggested Contacts list or the address crosses a threshold in the
automatic contact creation setting. An unmatched email address is also deleted after 30 days from the initial appearance without
subsequent activity.

Supported Calls

`delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`,

```
   update()

```

Special Access Rules

This object is available with Einstein Activity Capture when Sync Email as Salesforce Activity is turned on. If you turn on Einstein Activity
Capture in Summer ’25 or later, Sync Email as Salesforce Activity is enabled by default.

Fields

**Field** **Details**

```
CreatedContactOrLeadId

EmailAddress

FirstName

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID for the contact or lead record created from a suggestion. Read only.

This field is a polymorphic relationship field.

**Relationship Name**
CreatedContactOrLead

**Refers To**
Contact, Lead

**Type**
email

**Properties**
Filter, Group, idLookup, Sort

**Description**
The email address of the suggested contact. This address doesn’t match any existing user,
contact, or lead. (Read only.)

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update


Standard Objects StagedUnmtchdEmailAddr

**Field** **Details**

**Description**
First name of the suggested contact.

```
IgnoreSuggestionEndDate

LastInteractionDate

LastName

OccurrenceCount

UserId

```

**Type**
date

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
If a user dismisses a suggestion, it isn't suggested again until this date.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date the user last interacted with the unmatched email address through email or a
scheduled calendar event. (Read only.)

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Last name of the suggested contact.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total number of times the user and the unmatched email address occur together. (Read
only.)

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The unique ID of the user associated with the unknown email address. (Read only.)

This field is a relationship field.


### Standard Objects StagedUnmtchdEmailAddrRela

**Field** **Details**

**Relationship Name**
User

**Refers To**
User

### StagedUnmtchdEmailAddrRela

Represents data about the message or event activity associated with an email address that Einstein Activity Capture can’t match with
an existing user, contact, or lead record. Related to StagedUnmtchdEmailAddr, which represents data about the unmatched email
address. This object is available in API version 66.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

This object is available with Einstein Activity Capture when Sync Email as Salesforce Activity is turned on. If you turn on Einstein Activity
Capture in Summer ’25 or later, Sync Email as Salesforce Activity is enabled by default.

Fields

**Field** **Details**

```
RelatedActivityId

SourceActivity

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The unique ID of the related activity record, such as an email message or calendar event.

This field is a polymorphic relationship field.

**Relationship Name**
RelatedActivity

**Refers To**
EmailMessage, Event, StagedEmail

**Type**
picklist


### Standard Objects Stamp

**Field** **Details**

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The activity type. Possible values are:

**•** `Event`

**•** `StagedEmail`

**•** `EmailAddress`

```
StagedUnmatchedEmailAddressId

### Stamp

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The unique ID of the related unmatched email address record.

This field is a relationship field.

**Relationship Name**
StagedUnmatchedEmailAddress

**Relationship Type**
Master-detail

**Refers To**
StagedUnmtchdEmailAddr

Represents a User Specialty. This object is available in API version 39.0 and later.

Create User Specialty labels. Specialties can be any term you want, up to 50 characters, including spaces and underscores.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Description**

```
Description

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects StampAssignment

**Field** **Description**

**Description**
Use this field to describe what the user specialty means and how it applies to a
user. You have a 255 character maximum including spaces and underscores.

```
MasterLabel

ParentId

### StampAssignment

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The User Specialty label that appears under the user’s profile picture. You can
create any label you want as long as it’s within the 50 character maximum,
including spaces and underscores.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The id of the org or network.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Organization

Represents assignment of a User Specialty to a user. This object is available in API version 39.0 and later.

Assign a User Specialty to users. This label appears beneath their profile photo.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`


### Standard Objects StandardInvocableActionType

Fields

**Field** **Details**

```
StampId

SubjectId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The unique id generated when creating a user specialty.

This is a relationship field.

**Relationship Name**
Stamp

**Relationship Type**
Lookup

**Refers To**
Stamp

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The id for the user getting the User Specialty label.

This is a relationship field.

**Relationship Name**
Subject

**Relationship Type**
Lookup

**Refers To**
User

### StandardInvocableActionType

Represents a collection of fields to set up granular user permissions for access to a standard invocable action in Flow Builder. This object
is available in API version 60.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`


### Standard Objects StandardShippingRate

Special Access Rules

Marketing Cloud Growth edition and the Manage Flow user permission or View Flows user permission are required.

Fields

**Field** **Details**

```
DeveloperName

Language

MasterLabel

Namespace

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The developer name and namespace combination of the invocable action. This combination
must be unique.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The language code of the invocable action. For a full list of supported languages and their
[codes, see Supported Languages. This field is available in API version 60.0 and later.](https://help.salesforce.com/s/articleView?id=xcloud.faq_getstart_what_languages_does.htm&type=5&language=en_US)

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The label for the invocable action. This display value is the internal label that doesn’t get
translated. This field is available in API version 60.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace of the invocable action. Enter a value only if you’re using the invocable action
in Flow Builder or with Apex.

### StandardShippingRate

Standard shipping rate for a store. This object is available in API version 59.0 and later.


Standard Objects StandardShippingRate

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

The StandardShippingRate object is available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

```
ConditionFactor

ConditionRangeMax

ConditionRangeMin

CurrencyIsoCode

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Conditions that affect the shipping rate.

Possible values are:

**•** `OrderPriceFactor` —Condition based on the order price value.

**•** `OrderWeightFactor` —Condition based on delivery weight. This value is available
in API version 62.0 and later.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Maximum value of the shipping rate condition.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Minimum value of the shipping rate condition. This value can't be negative.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects StandardShippingRate

**Field** **Details**

**Description**
Currency ISO code of the cart.

Possible values are:

**•** `EUR` —Euro

**•** `USD` —U.S. Dollar

The default value is `USD` .

```
Name

Price

ShippingCarrierMethodId

ShippingZoneId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the standard shipping rate.

**Type**
currency

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
Price of standard shipping.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the shipping service carrier method. This field is available in API version 61.0 and later.

This field is a relationship field.

**Relationship Name**
ShippingCarrierMethod

**Relationship Type**
Lookup

**Refers To**
ShippingCarrierMethod

**Type**
reference

**Properties**
Create, Filter, Group, Sort


Standard Objects StandardShippingRate

**Field** **Details**

**Description**
ID of the shipping zone.

This field is a relationship field.

**Relationship Name**
ShippingZone

**Relationship Type**
Parent-detail

**Refers To**
ShippingRateArea (the master object)

```
TransitTimeMax

TransitTimeMin

TransitTimeUnit

WeightUnit

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Maximum value of the shipping transit time. This field is available in API version 61.0 and
later.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Minimum value of the shipping transit time. This value can't be negative. This field is available
in API version 61.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Unit of value for shipping transit time. This field is available in API version 61.0 and later.

Possible values are:

**•** `Days`

**•** `Hours`

**•** `Weeks`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


### Standard Objects StaticResource

**Field** **Details**

**Description**
Unit of measurement for the weight of the cart items. This field is available in API version
62.0 and later.

Possible values are:

**•** `Grams`

**•** `Kilograms`

**•** `Ounces`

**•** `Pounds`

### StaticResource

Represents a static resource that can be used in Visualforce markup.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,
`update()`, `upsert()`

Fields

**Field** **Details**

```
Body

BodyLength

CacheControl

```

**Type**
base64

**Properties**
Create, Nillable, Update

**Description**
Required. Encoded file data.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Size of the file (in bytes).

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


Standard Objects StaticResource

**Field** **Details**

**Description**

The sharing policy for the static resource when cached. The cache control can have one of
these values:

**•** `Private` specifies that the static resource is accessible to all authenticated users. The
static resource is stored on the Salesforce server in a user’s individual cache for the
duration of the session.

**•** `Public` specifies that the static resource is accessible after caching to all internet traffic,
including unauthenticated users. The resource is stored on the Salesforce server in a
shared cache, which results in faster load times.

```
ContentType

Description

Name

NamespacePrefix

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Type of content. Label is **Mime Type** . Limit: 120 characters.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Text description of the static resource. Limit: 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Name of the static resource.

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


### Standard Objects StoreIntegratedService

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

Usage

Use static resources to upload content that you can reference in Visualforce markup, including archives (such as .zip and .jar files), images,
stylesheets, JavaScript, and other files. Using a static resource is preferable to uploading a file to the Documents tab because:

**•** You can package a collection of related files into a directory hierarchy and upload that hierarchy as a .zip or .jar archive.

**•** You can reference a static resource in page markup by name using the `$Resource` global variable instead of hard-coding
document IDs.

Encoded Data

The API sends and receives the binary file data encoded as a base64 data type. Prior to creating a record, clients must encode the binary
file data as base64. Upon receiving an API response, clients must decode the base64 data to binary. The SOAP client usually handles this
conversion.

Maximum Static Resource Size

You can create or update static resources to a maximum size of 5 MB. An organization can have up to 250 MB of static resources, total.

SEE ALSO:

ApexComponent

ApexPage

_Developer Guide_ [: Visualforce Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.pages.meta/pages/)

### StoreIntegratedService

Represents an association between an integration and a store. This object is available in API version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`


Standard Objects StoreIntegratedService

Special Access Rules

The StoreIntegratedService object is available only if the B2B Commerce license is enabled.

Fields

**Field** **Details**

```
Integration

ServiceProviderType

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. The integration ID.

Possible values are:

**•** If the integration is a RegisteredExternalService:

**–** The ID of the RegisteredExternalService OR

**–** [ServiceProviderType]__[DeveloperName]

**•** ServiceProviderType: Price, Inventory, Tax, or Shipment

**•** DeveloperName of RegisteredExternalService

**•** If the integration is a PaymentGateway:

**–** The ID of the PaymentGateway

**•** If the integration is a Flow:

**–** [ServiceProviderType]__[NamespacePrefix]__[ApiName]

**–** If NamespacePrefix is null, it’s [ServiceProviderType]__[ApiName]

**•** ServiceProviderType: Flow

**•** ApiName and NamespacePrefix of FlowDefinitionView

**•** If the integration is the Salesforce Standard pricing:

**–** [ServiceProviderType]__B2B_STOREFRONT__StandardPricing

**•** ServiceProviderType: Price

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. The type of integration service provider.

Possible values are:

**•** `Flow`


### Standard Objects StreamingChannel

**Field** **Details**

**•** `Inventory`

**•** `Payment`

**•** `Price`

**•** `Promotions` (this value is available in API version 53.0 and later)

**•** `Shipment`

**•** `Tax`

```
StoreId

### StreamingChannel

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The unique ID for the store.

Represents a channel that is the basis for notifying listeners of generic Streaming API events. This object is available in API version 29.0
and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

**•** This object is available only if Streaming API is enabled for your org.

**•** Users with the Create permission can create this record.

**•** You can create a permission set and grant users read and create access to all streaming channels in the org. This access isn’t for a
specific channel, like with user sharing.

**•** You can apply user sharing to StreamingChannel. You can restrict access to receiving or sending events on a channel by sharing
channels with specific users or groups. Channels shared with public read-only or read-write access send events only to clients
subscribed to the channel that also are using a user session associated with the set of shared users or groups. Only users with
read-write access to a shared channel can generate events on the channel, or modify the actual StreamingChannel record.

Fields

**Field** **Details**

```
Description

```

**Type**
string


Standard Objects StreamingChannel

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the StreamingChannel. Limit: 255 characters.

**Label:** Description

```
IsDynamic

LastReferencedDate

LastViewedDate

Name

OwnerId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
`true` if the channel gets dynamically created on subscribe if necessary, `false` otherwise.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last interacted with this record, directly or indirectly.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it's possible that the user only accessed this record or list view ( `LastReferencedDate` ),
but not viewed it.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Descriptive name of the streaming channel. Limit: 80 characters, alphanumeric
and “_”, “/” characters only. Must start with “/u/”. This value identifies the channel and must
be unique.

**Label:** Streaming Channel Name

**Type**
reference


### Standard Objects Salesforce Surveys Object Model

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the streaming channel.

**Label:** Owner Name

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

Dynamic Streaming Channel

Streaming API generic streaming supports dynamic streaming channel creation, which creates a StreamingChannel when a client first
subscribes to the channel. To enable dynamic streaming channels in your org, from Setup, enter _`User Interface`_ in the Quick
Find box, then select **User Interface** . Enable **Enable Dynamic Streaming Channel Creation** . You can also enable dynamic channel
creation in Metadata API using EventSettings.

SEE ALSO:

_[Streaming API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_streaming.meta/api_streaming/intro_stream.htm)_

### Salesforce Surveys Object Model

Learn about how Salesforce Surveys objects relate to one another in Salesforce.


### Standard Objects Survey

[This diagram represents the object model for Salesforce Surveys. For more details and a larger image, visit the Data Model Gallery.](https://developer.salesforce.com/docs/platform/data-models/guide/salesforce-surveys.html)

### Survey

Represents a survey.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`

Note: You can’t define custom fields for the Survey object using the Object Manager.

Fields

**Field Name** **Details**

```
ActiveVersionID

Description

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the survey version currently activated.

**Type**
string

**Properties**
Nillable


Standard Objects Survey

**Field Name** **Details**

**Description**
The description of the survey. This field isn’t visible in the UI.

```
DeveloperName

IsPartialSaveEnabled

LastReferencedDate

LastViewedDate

LatestVersionId

Name

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The survey’s unique API name.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether to save the partial responses for the survey ( `true` ) or not
( `false` ).

The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the current user last viewed a record related to the survey.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed the survey.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the most recent version of this survey.

**Type**
string


Standard Objects Survey

**Field Name** **Details**

**Properties**
Filter, Group, Sort

**Description**
The name of the survey that appears in the UI. This field is read-only from API
version 50.0.

```
NamespacePrefix

OwnerId

SurveyType

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
Filter, Group, Sort

**Description**
The ID of the user who created the survey.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Type of the survey. The default value is Survey.

Possible values are:

**•** `ASSESSMENT`  - Survey type for sales enablement teams. Available from
API version 58.0 and later.


### Standard Objects SurveyEmailBranding

**Field Name** **Details**

**•** `BASIC`                       - Survey with a question page with like or dislike, long text, multiple
selection, NPS, rating, short text, and single selection questions, and without
inserted participant responses, display logic, and page branching logic.

**•** `SURVEY`                       - Survey with all the available features.

```
TotalVersionsCount

```

Associated Objects

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of versions of the survey.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**SurveyChangeEvent on page 68**
Change events are available for the object.

**SurveyFeed (API version 42.0)**
Feed tracking is available for the object.

**SurveyOwnerSharingRule**

Sharing rules are available for the object.

**SurveyShare**

Sharing is available for the object.

### SurveyEmailBranding

Represents the configuration settings for invitation emails sent to survey participants for a particular survey.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

As of Spring ’20 and later, only users with the View Setup and Configuration permission can access this object.

Note: You can’t define custom fields for the SurveyEmailBranding object using the Object Manager.


Standard Objects SurveyEmailBranding

Fields

**Field Name** **Details**

```
Body

DeveloperName

FooterImageId

FromEmailAddress

HeaderImageId

```

**Type**
textarea

**Properties**
Create, Update

**Description**
The body text of the invitation email.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique API name of the email branding configuration.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the content asset that appears in the footer of the invitation email.

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The email address that appears in the “From” field when the invitation is sent to
participants.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the content asset that appears in the header of the invitation email.


Standard Objects SurveyEmailBranding

**Field Name** **Details**

```
Language

MasterLabel

Subject

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the emails. Available languages include:

**•** Chinese (Simplified)

**•** Chinese (Traditional)

**•** Danish

**•** Dutch

**•** English

**•** Finnish

**•** French

**•** German

**•** Italian

**•** Japanese

**•** Korean

**•** Norwegian

**•** Portuguese (Brazilian)

**•** Russian

**•** Spanish

**•** Spanish (Mexican)

**•** Swedish

**•** Thai

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label for these email configuration settings.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The subject of the invitation email.


### Standard Objects SurveyEngagementContext SurveyEngagementContext

Represents the context based on which a survey invitation was sent or a survey response was received. This object is available in API
version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Note: You can’t define custom fields for the SurveyEngagementContext object using the Object Manager.

Fields

**Field** **Details**

```
ContextType

ContextValue

Name

OwnerId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Context type based on which the survey invitation was sent or the response was received.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Context based on which the survey invitation was sent or the response was received.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the record's owner.


### Standard Objects SurveyInvitation

**Field** **Details**

### `SurveyInvitationId`

```
SurveyResponseId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the survey invitation.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the survey response.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**SurveyEngagementContextShare**

Sharing is available for the object.

### SurveyInvitation

Represents the invitation sent to a participant to complete the survey.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
CommunityId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the Experience Cloud site that you want to send the survey to.


Standard Objects SurveyInvitation

**Field Name** **Details**

```
ContactId

EmailBrandingId

InvitationLink

InviteExpiryDateTime

IsDefault

LastReferencedDate

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the contact who received the invitation. This field is available in API v49.0
and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the survey email branding object that’s associated with this invitation.

**Type**
url

**Properties**
Group, Nillable

**Description**
The URL to the survey that is sent to participants. To query on this field, you need
access to the associated Survey record.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time that the survey invitation expires.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether this is the default survey invitation to use when the survey
is sent to participants.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects SurveyInvitation

**Field Name** **Details**

**Description**
The timestamp for when the current user last viewed a record related to this
survey invitation.

```
LastViewedDate

LeadId

Name

OptionsAllowGuestUserResponse

OptionsAllowParticipantAccessTheirResponse

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this survey invitation.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the lead who received the invitation. This field is available in API v49.0 and
later.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the survey invitation that appears in the UI.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Determines whether participants who don’t have a Salesforce account can
complete the survey.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Determines whether participants can access a copy of their responses after they
complete the survey.


Standard Objects SurveyInvitation

**Field Name** **Details**

```
OptionsCollectAnonymousResponse

OwnerId

ParticipantId

ResponseStatus

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Determines whether participants can complete the survey anonymously.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the user who created the survey invitation.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the participant if the participant is a Salesforce contact, user, or lead.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of a participant’s response to the survey that’s associated with the
survey invitation. Possible values include:

**•** `NotStarted`  - For an invitation with a `ParticipantID`, it means
that the recipient hasn’t opened the survey. For an invitation without the
`ParticipantID`, it means that none of the recipients have opened the
survey.

**•** `Started`  - For an invitation with a `ParticipantID`, it means that
the recipient opened the survey. For an invitation without the
`ParticipantID`, it means that the survey has been opened by at least
one recipient.

**•** `Paused`  - For an invitation with a `ParticipantID`, it means that the
recipient has paused the survey. For an invitation without the
`ParticipantID`, it means that the survey has been paused by any one
of the recipients. Paused isn't available for invitations in which either
`OptionsAllowParticipantAccessTheirResponse` or
`OptionsCollectAnonymousResponse` is true.


Standard Objects SurveyInvitation

**Field Name** **Details**

**•** `PartiallyCompleted`                       - For an invitation with a `ParticipantID`
field, it means that the recipient has partially completed the survey. For an
invitation without the `ParticipantID` field, it means that at least one
recipient has partially completed the survey. Available in API version 63.0
and later.

**•** `Completed`                       - For an invitation with a `ParticipantID`, it means that
the recipient has submitted the survey. For an invitation without the
`ParticipantID`, it means that the invitation has been submitted by at
least one recipient.

```
SurveyId

UUID

UserId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the survey that’s sent in the invitation.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A unique user ID that's added to a survey invitation generated for a contact,
lead,or user.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the user who received the invitation. This field is available in API v49.0 and
later.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**SurveyInvitationChangeEvent (API version 62.0)**
Change events are available for the object.

**SurveyInvitationOwnerSharingRule**

Sharing rules are available for the object.

**SurveyInvitationShare**

Sharing is available for the object.


### Standard Objects SurveyPage SurveyPage

Represents a page, such as the title page or a question page, in a survey.

Supported Calls

`getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Note: You can’t define custom fields for the SurveyPage object using the Object Manager.

Fields

**Field** **Details**

```
DeveloperName

Name

SurveyVersionId

```

Associated Objects

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique API name of this SurveyPage object.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the survey page that appears in the UI.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The version of the survey that the page belongs to.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

### **SurveyPageChangeEvent on page 68**

Change events are available for the object.


### Standard Objects SurveyQuestion SurveyQuestion

Represents a question in a survey.

Supported Calls

`describeLayout()describeSObjects()getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Note: You can’t define custom fields for the SurveyQuestion object using the Object Manager.

Fields

**Field** **Details**

```
DeveloperName

IsDeprecated

Name

PageDisplayOrder

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The API name of the SurveyQuestion. The API name must be unique within a particular
version of the survey.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the question was deleted from the survey.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Up to the first 250 characters of the label for the question.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The order in which the page is displayed. This field is available in API version 54.0 and later.


Standard Objects SurveyQuestion

**Field** **Details**

```
PageName

QuestionChoiceCount

QuestionName

QuestionOrder

QuestionType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The label for the page. This field is available in API version 52.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of choices for the question. This field is available in API version 62.0 and later.

**Type**
textarea

**Properties**
Nillable

**Description**
The label for the question.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The order in which the question is displayed.

The label for the page. This field is available in API version 52.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of question. Possible values include:

**•** `Boolean` —This value is available in API v49.0 and later.

**•** `CSAT`

**•** `Currency`

**•** `Date`

**•** `DateTime`


Standard Objects SurveyQuestion

**Field** **Details**

**•** `FreeText`

**•** `Image`

**•** `Matrix` —This value is available in API v55.0 and later.

**•** `MultipleChoice`

**•** `MultiSelectPicklist`

**•** `NPS`

**•** `Number`

**•** `Picklist`

**•** `RadioButton`

**•** `StackRank`

**•** `Rating`

**•** `ShortText` —This value is available in API v49.0 and later.

**•** `Slider`

**•** `Toggle`

```
RelatedQuestionId

SubQuestionDisplayOrder

SurveyPageId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the parent question. This field is blank when the question itself is the parent question.
This field is available in API v55.0 and later, with Feedback Management - Starter and Feedback
Management - Growth licenses.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The order in which the question is displayed within the parent question. This field is available
in API v55.0 and later, with Feedback Management - Starter and Feedback Management Growth licenses.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Lookup to the SurveyPage that contains the question.


### Standard Objects SurveyQuestionChoice

**Field** **Details**

```
 SurveyVersionId

ValidationType

```

Associated Objects

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the SurveyVersion that the question belongs to.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The validations available for the short-text question. Possible values include:

**•** Custom - Cu

**•** Number - Nu

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SurveyQuestionChangeEvent on page 68**
Change events are available for the object.

### SurveyQuestionChoice

Represents an answer choice that a participant can select for a survey question.

Supported Calls

`describeLayout()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Note: You can’t define custom fields for the SurveyQuestionChoice object using the Object Manager.

Fields

**Field** **Details**

```
DeveloperName

```

**Type**
string

**Properties**
Filter, Group, Sort


Standard Objects SurveyQuestionChoice

**Field** **Details**

**Description**
The unique API name of the SurveyQuestionChoice object.

```
DisplayOrder

IsDeprecated

Name

QuestionId

SurveyVersionId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The order in which the question choice is displayed within the parent question. This field is
available in API v55.0 and later, with Feedback Management - Starter and Feedback
Management - Growth licenses.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a question choice was deleted from the survey.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
A label for the question choice that appears in the UI.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the SurveyQuestion object that this choice belongs to.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version of the survey that this question choice belongs to.


### Standard Objects SurveyQuestionResponse

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SurveyQuestionChoiceChangeEvent on page 68**
Change events are available for the object.

### SurveyQuestionResponse

Represents a participant’s answer to a specific question.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Note: You can’t define custom fields for the SurveyQuestionResponse object using the Object Manager.

Fields

**Field** **Details**

```
ChoiceValue

Datatype

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
Response provided by a participant for the following question types:

**•** Multiple choice

**•** Picklist

**•** Radio

**•** Ranking

**Type**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The data type of the question response. Possible values are:

**•** `Boolean` This value is available in API v49.0 and later.

**•** `Date`

**•** `Double`

**•** `Int`

**•** `Number`


Standard Objects SurveyQuestionResponse

**Field** **Details**

**•** `String`

```
DateTimeValue

DateValue

InvitationId

IsTrueOrFalse

NumberValue

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Response provided by a participant for a question of the type date time.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Response provided by a participant for a question of the type date.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the SurveyInvitation that was sent to the survey participant.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Response provided by a participant for a question type which has only two possible values:
True and False.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Response provided by a participant for the following question types:

**•** Net Promoter Score (NPS)

**•** Rating

**•** Score

**•** Slider


Standard Objects SurveyQuestionResponse

**Field** **Details**

```
QuestionChoiceId

QuestionId

Rank

ResponseId

ResponseShortText

ResponseValue

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of SurveyQuestionChoice that a participant chose in response to a question.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the SurveyQuestion that a participant provided an answer for.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Rank provided by a participant for an answer choice for the ranking question type.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the SurveyResponse that is the parent of this SurveyQuestionResponse.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Up to the first 250 characters of the response provided by a participant for a text type question.

**Type**
textarea

**Properties**
Nillable

**Description**
Response provided by a participant for a question.


### Standard Objects SurveyQuestionScore

**Field** **Details**

```
 SurveyVersionId

```

Associated Objects

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the SurveyVersion that the response belongs to.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SurveyQuestionResponseChangeEvent on page 68**
Change events are available for the object.

### SurveyQuestionScore

Represents the aggregate of responses for the following question types: date, multiple choice, picklist, radio, ranking, rating, scoring,
[slider, and Net Promoter Score](https://www.salesforce.com/content/dam/web/en_us/www/documents/legal/Agreements/product-specific-terms/net-promoter-and-nps.pdf) [®] (NPS [®] ).

Supported Calls

`delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`

Note: You can’t define custom fields for the SurveyQuestionScore object using the Object Manager.

Fields

**Field** **Details**

```
CumulativeScore

DateResponse

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Sum of the responses provided by all the participants for a question of the following types:
rating, scoring, and slider. For a question of the type ranking, sum of the weights provided
by all the participants for each item.

Note: This field is only applicable for the overall score type.

**Type**
date


Standard Objects SurveyQuestionScore

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date selected by one or more participants for a question of the type date.

Note: This field is only applicable for the individual score type.

```
Name

QuestionChoiceId

QuestionDeveloperName

QuestionId

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
For an overall score type record:

**•** Name of a question.

**•** Name of an item in a question of the type ranking.

For an individual score type record:

**•** Name of an item in a question of the type ranking.

**•** Name of a question of the type date.

**•** Response provided by one or more participants for questions of the following types:
picklist, multiple choice, rating, ranking, score, slider, NPS.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier of the answer choice selected by one or more participants. For an individual
score type record, this field is applicable for questions of the following types: picklist, radio,
multi choice, ranking and rating. For an overall score type record, this field is applicable for
questions of the type ranking.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API name of the question for which response is recorded. The API name must be unique
within a particular version of the survey.

**Type**
reference


Standard Objects SurveyQuestionScore

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier of the question for which response is recorded.

```
QuestionName

QuestionSkippedCount

ResponseCount

ResponseValue

Score

```

**Type**
textarea

**Properties**
Nillable

**Description**
Name of the question for which response is recorded.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of participants who didn’t respond to the question.

Note: This field is only applicable for the overall score type.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
For an overall score type record, number of participants who responded to the question. For
an individual score type record, number of participants who selected a particular answer
choice.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Answer choice selected by one or more participants for a question of the following types:
rating, slider, score, NPS. Rank provided by the participant for an item in a question of the
type ranking.

Note: This field is only applicable for the individual score type.

**Type**
double


Standard Objects SurveyQuestionScore

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
For an individual score type record, percentage of participants who selected a particular
answer choice.

Note: For questions of the type ranking, the percentage of participants who have
provided the same rank to an item.

For overall score type record:

**•** Average score of questions of the following question types: rating, scoring, and slider.

**•** Score of an NPS type question.

**•** Average weight provided by all participants for each item in question of the type ranking.

**•** Number of participants who responded to the question for the following question types:
date, radio, multi choice, and picklist.

```
ScoreType

SurveyId

SurveyInvitationId

SurveyVersionId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Type of the score calculated for a record. Possible values are:

**•** `Individual`

**•** `Overall`

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Unique identifier of the survey that contains the question for which scores are calculated.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier of the survey invitation for which scores are calculated.

**Type**
reference

**Properties**
Filter, Group, Sort


### Standard Objects SurveyResponse

**Field** **Details**

**Description**
Unique identifier of the survey version for which scores are calculated.

### SurveyResponse

Represents information about a participant’s response to a survey, such as the status of the response, the participant’s location, and
when the survey was completed.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,

```
   undelete()

```

Note: You can’t define custom fields for the SurveyResponse object using the Object Manager.

Fields

**Field Name** **Details**

```
CompletionDateTime

DataMapperExecutionStatus

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the participant completed the survey.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Status of all the survey data maps after a response is received. This field is available
in API v49.0 and later, with Feedback Management - Starter and Feedback
Management - Growth licenses.

Possible values are:

**•** `Pending`

**•** `InProgress`

**•** `Success`

**•** `Error`


Standard Objects SurveyResponse

**Field Name** **Details**

```
InterviewGuid

InterviewId

InvitationId

IpAddress

Language

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable

**Description**
An automatically-generated, unique ID for a saved survey response.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the FlowInterview object that’s associated with this response.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the SurveyInvitation object that’s associated with this response.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the device the participant used to take the survey.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The language that the participant used to complete the survey.

Possible values are:

**•** `af` —Afrikaans

**•** `ar` —Arabic

**•** `ar_AE` —Arabic (United Arab Emirates)

**•** `ar_BH` —Arabic (Bahrain)

**•** `ar_DZ` —Arabic (Algeria)


Standard Objects SurveyResponse

**Field Name** **Details**

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

**•** `de` —German

**•** `de_AT` —German (Austria)

**•** `de_BE` —German (Belgium)

**•** `de_CH` —German (Switzerland)

**•** `de_LU` —German (Luxembourg)

**•** `el` —Greek

**•** `en_AU` —English (Australian)

**•** `en_CA` —English (Canadian)

**•** `en_GB` —English (UK)

**•** `en_HK` —English (Hong Kong)

**•** `en_IE` —English (Ireland)

**•** `en_IN` —English (Indian)

**•** `en_MY` —English (Malaysian)

**•** `en_NZ` —English (New Zealand)

**•** `en_PH` —English (Philippines)

**•** `en_SG` —English (Singapore)

**•** `en_US` —English


Standard Objects SurveyResponse

**Field Name** **Details**

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

**•** `ga` —Irish

**•** `gu` —Gujarati

**•** `hi` —Hindi

**•** `hr` —Croatian

**•** `hu` —Hungarian

**•** `hy` —Armenian

**•** `in` —Indonesian

**•** `is` —Icelandic


Standard Objects SurveyResponse

**Field Name** **Details**

**•** `it` —Italian

**•** `it_CH` —Italian (Switzerland)

**•** `iw` —Hebrew

**•** `ja` —Japanese

**•** `ka` —Georgian

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

**•** `pl` —Polish

**•** `pt_BR` —Portuguese (Brazil)

**•** `pt_PT` —Portuguese (European)

**•** `rm` —Romansh

**•** `ro` —Romanian

**•** `ro_MD` —Romanian (Moldova)

**•** `ru` —Russian

**•** `sh` —Serbian (Latin)

**•** `sh_ME` —Montenegrin

**•** `sk` —Slovak

**•** `sl` —Slovene

**•** `sq` —Albanian

**•** `sr` —Serbian (Cyrillic)

**•** `sv` —Swedish

**•** `sw` —Swahili

**•** `ta` —Tamil

**•** `te` —Telugu

**•** `th` —Thai


Standard Objects SurveyResponse

**Field Name** **Details**

**•** `tl` —Tagalog

**•** `tr` —Turkish

**•** `uk` —Ukrainian

**•** `ur` —Urdu

**•** `vi` —Vietnamese

**•** `xh` —Xhosa

**•** `zh_CN` —Chinese (Simplified)

**•** `zh_HK` —Chinese (Hong Kong)

**•** `zh_SG` —Chinese (Singapore)

**•** `zh_TW` —Chinese (Traditional)

**•** `zu` —Zulu

```
LastReferencedDate

LastViewedDate

Latitude

Location

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that another Salesforce object last referenced this
SurveyResponse object.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that someone last viewed this SurveyResponse object.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The latitude of the participant’s location.

**Type**
location

**Properties**
Nillable

**Description**
The latitude and longitude coordinates of the participant’s location.


Standard Objects SurveyResponse

**Field Name** **Details**

```
Longitude

Name

Status

SubmitterId

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The longitude of the participant’s location.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the participant.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the survey. Possible values include:

**•** NotStarted — The participant hasn't opened the survey.

**•** Started — The participant has opened the survey.

**•** Paused — The participant has paused the survey. Paused isn't available for
invitations in which either
`OptionsAllowParticipantAccessTheirResponse` or
`OptionsCollectAnonymousResponse` is true.

**•** PartiallyCompleted — The participant has partially completed the survey.
Available in API version 63.0 and later.

**•** Completed — The participant has completed the survey.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Salesforce user, contact, or lead who completed the survey.

**Relationship Name**
Submitter

**Relationship Type**
Lookup


### Standard Objects SurveySubject

**Field Name** **Details**

**Refers To**
Contact, Lead, User

```
SurveyId

SurveyVersionId

```

Associated Objects

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the survey that the participant completed.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the version of the survey that the participant completed.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SurveyResponseChangeEvent on page 68**
Change events are available for the object.

### SurveySubject

Represents a relationship between a survey and another object, such as an account or a case.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
LastReferencedDate

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects SurveySubject

**Field Name** **Details**

**Description**
The timestamp for when the SurveySubject record was last referenced by another
object.

```
LastViewedDate

Name

ParentId

SubjectEntityType

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed the SurveySubject record.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the SurveySubject record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Unique identifier of the SurveyInvitation object or SurveyResponse object that is
associated with this survey-object relationship.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
SurveyInvitation, SurveyResponse

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Object that the survey is associated with. Possible values include:

**•** _`Account`_

**•** _`Asset`_

**•** _`Banker`_


Standard Objects SurveySubject

**Field Name** **Details**

**•** _`BranchUnit`_

**•** _`BranchUnitBusinessMember`_

**•** _`BranchUnitCustomer`_

**•** _`BusinessLicenseApplication`_

**•** _`BusinessMilestone`_

**•** _`Campaign`_

**•** _`CareProgram`_

**•** _`Case`_

**•** _`Claim`_

**•** _`ClaimParticipant`_

**•** _`Contact`_

**•** _`Employee`_

**•** _`Event`_

**•** _`Incident`_

**•** _`IndividualApplication`_

**•** _`InsurancePolicy`_

**•** _`InsurancePolicyParticipant`_

**•** _`Lead`_

**•** _`LearningItemSubmission`_ —Available in API version 58.0 and later.

**•** _`LiveChatTranscript`_

**•** _`LoyaltyProgram`_

**•** _`LoyaltyProgramMember`_

**•** _`LoyaltyProgramPartner`_

**•** _`MaterialityStakeholder`_

**•** _`MessagingSession`_

**•** _`Opportunity`_

**•** _`Order`_

**•** _`PersonalLifeEvent`_

**•** _`Producer`_

**•** _`Product2`_

**•** _`Promotion`_

**•** _`RebateProgram`_

**•** _`RetailStore`_

**•** _`ServiceAppointment`_

**•** _`ServiceResource`_

**•** _`Solution`_

**•** _`Task`_

**•** _`TransactionJournal`_


Standard Objects SurveySubject

**Field Name** **Details**

**•** _`User`_

**•** _`VideoCall`_

**•** _`Visit`_

**•** _`VoiceCall`_

**•** _`VolunteerProject`_

**•** _`WorkOrder`_

**•** Custom Objects

```
SubjectId

SurveyId

SurveyInvitationId

SurveyResponseId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the object that’s associated with the survey.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Unique identifier of the survey that’s associated with the record that’s represented
by `SubjectId` .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier of the survey invitation that's associated with another object.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier of the survey response that's associated with another object.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


### Standard Objects SurveyVersion

**SurveySubjectChangeEvent (API version 62.0)**
Change events are available for the object.

### SurveyVersion

Represents a version of a survey.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`

Note: You can’t define custom fields for the SurveyVersion object using the Object Manager.

Fields

**Field Name** **Details**

```
BrandingSetId

Description

IsTemplate

LastReferencedDate

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the branding set associated with the survey version.

**Type**
textarea

**Properties**
Nillable

**Description**
The description of this survey version.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the survey version is a template. Template surveys are
automatically shared with all users in your Salesforce org.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects SurveyVersion

**Field Name** **Details**

**Description**
The date and time that the current user last viewed a record related to the survey
version.

```
LastViewedDate

Name

SurveyId

SurveyStatus

VersionNumber

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed the survey version.

**Type**
string

**Properties**
Filter, Group, Sort

Filter, Group, Sort

Filter, Group, idLookup, Sort

**Description**
The name of the survey that appears in the UI.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the survey associated with the survey version.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of the survey. Possible values include:

**•** `Active`

**•** `Draft`

**•** `Obsolete`

**•** `InvalidDraft`

**Type**
int


### Standard Objects SurveyVersionAddlInfo

**Field Name** **Details**

**Properties**
Filter, Group, Sort

**Description**
The version number of the survey.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SurveyVersionChangeEvent on page 68**
Change events are available for the object.

### SurveyVersionAddlInfo

Represents additional information about a survey version. This information defines the default settings of a survey version. This object
is available in API version 49.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
EmailSender

EmailTemplateId

EngagementContextMetadata

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
The organization-wide email address used to send a survey invitation.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the email template that's used to send an automated survey invitation.

**Type**
string


Standard Objects SurveyVersionAddlInfo

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The custom metadata created to get the engagement context from the participants.

```
InvitationSharingRole

Language

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the users that share edit access to a survey invitation.

Possible values are:

**•** `InvitationRecordCreator`  - Owner of the record that's associated with a
survey invitation.

**•** `SurveyOwner`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Language used to create the survey.

Possible values are:

**•** `af` —Afrikaans

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


Standard Objects SurveyVersionAddlInfo

**Field** **Details**

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

**•** `de` —German

**•** `de_AT` —German (Austria)

**•** `de_BE` —German (Belgium)

**•** `de_CH` —German (Switzerland)

**•** `de_LU` —German (Luxembourg)

**•** `el` —Greek

**•** `en_AU` —English (Australian)

**•** `en_CA` —English (Canadian)

**•** `en_GB` —English (UK)

**•** `en_HK` —English (Hong Kong)

**•** `en_IE` —English (Ireland)

**•** `en_IN` —English (Indian)

**•** `en_MY` —English (Malaysian)

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


Standard Objects SurveyVersionAddlInfo

**Field** **Details**

**•** `es_MX` —Spanish (Mexico)

**•** `es_NI` —Spanish (Nicaragua)

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

**•** `ga` —Irish

**•** `gu` —Gujarati

**•** `hi` —Hindi

**•** `hr` —Croatian

**•** `hu` —Hungarian

**•** `hy` —Armenian

**•** `in` —Indonesian

**•** `is` —Icelandic

**•** `it` —Italian

**•** `it_CH` —Italian (Switzerland)

**•** `iw` —Hebrew

**•** `ja` —Japanese

**•** `ka` —Georgian

**•** `kn` —Kannada

**•** `ko` —Korean

**•** `lb` —Luxembourgish

**•** `lt` —Lithuanian

**•** `lv` —Latvian

**•** `mi` —Te reo


Standard Objects SurveyVersionAddlInfo

**Field** **Details**

**•** `mk` —Macedonian

**•** `ml` —Malayalam

**•** `mr` —Marathi

**•** `ms` —Malay

**•** `mt` —Maltese

**•** `my` —Burmese

**•** `nl_BE` —Dutch (Belgium)

**•** `nl_NL` —Dutch

**•** `no` —Norwegian

**•** `pl` —Polish

**•** `pt_BR` —Portuguese (Brazil)

**•** `pt_PT` —Portuguese (European)

**•** `rm` —Romansh

**•** `ro` —Romanian

**•** `ro_MD` —Romanian (Moldova)

**•** `ru` —Russian

**•** `sh` —Serbian (Latin)

**•** `sh_ME` —Montenegrin

**•** `sk` —Slovak

**•** `sl` —Slovene

**•** `sq` —Albanian

**•** `sr` —Serbian (Cyrillic)

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

**•** `zh_SG` —Chinese (Singapore)

**•** `zh_TW` —Chinese (Traditional)

**•** `zu` —Zulu


### Standard Objects SvcCatalogCategory

**Field** **Details**

```
Name

SurveyQuestionId

SurveyVersionId

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Name of the record.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the survey question embedded in the email template used to send automated survey
invitations.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the survey version. This field is unique within your organization

### SvcCatalogCategory

Represents a group of Service Catalog items by functional area. This object is available in API version 58.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To access this object, get the Service Catalog Access permission set license, Employee Productivity Starter license, or Employee Productivity
Plus add-on license.

Fields

**Field** **Details**

```
DeveloperName

```

**Type**
string


Standard Objects SvcCatalogCategory

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Unique developer name for the catalog item category.

```
ImageId

IsActive

Language

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Allows a builder to pick an image displayed in the catalog.

This field is a relationship field.

**Relationship Name**
Image

**Relationship Type**
Lookup

**Refers To**
ContentAsset

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Allows service catalog builders to deprecate categories or create in-draft categories.

The default value is `false` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Possible values are:

**•** `da` —Danish

**•** `de` —German

**•** `en_US` —English

**•** `es` —Spanish

**•** `es_MX` —Spanish (Mexico)

**•** `fi` —Finnish

**•** `fr` —French


### Standard Objects SvcCatalogCategoryItem

**Field** **Details**

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
ParentCategoryId

SortOrder

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Parent category of this category. Allows categories to be grouped up to a max depth of 3.

This field is a relationship field.

**Relationship Name**
ParentCategory

**Relationship Type**
Lookup

**Refers To**
### SvcCatalogCategory

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Determines the order that the category is displayed to the end user.

### SvcCatalogCategoryItem

Represents an association between a Service Catalog item and category. Service catalog items can be grouped into categories. This
object is available in API version 58.0 and later.


Standard Objects SvcCatalogCategoryItem

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To access this object, get the Service Catalog Access permission set license, Employee Productivity Starter license, or Employee Productivity
Plus add-on license.

Fields

**Field** **Details**

```
IsPrimaryCategory

SortOrder

SvcCatalogCategoryId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether the category is the primary category for a catalog item.

The default value is `false` .

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Controls the order in which catalog items appear by default when you're viewing all items
in a single category.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the category for which the service category item belongs.

This field is a relationship field.

**Relationship Name**
SvcCatalogCategory

**Relationship Type**
Lookup

**Refers To**
SvcCatalogCategory


### Standard Objects SvcCatalogFilterCriteria

**Field** **Details**

```
SvcCatalogItemDefId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the service category item definition.

This field is a relationship field.

**Relationship Name**
SvcCatalogItemDef

**Relationship Type**
Lookup

**Refers To**
SvcCatalogItemDef

### SvcCatalogFilterCriteria

Represents an eligibility rule that determines if a Service Catalog user has access to a catalog item. This object is available in API version
60.0 and later.

Supported SOAP API Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Supported REST API Methods

```
DELETE, GET, HEAD, PATCH, POST, Query

```

Special Access Rules

To access this object, get the Service Catalog Access permission set license.

Fields

**Field** **Details**

```
CriteriaRelation

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort


Standard Objects SvcCatalogFilterCriteria

**Field** **Details**

**Description**

Possible values are:

**•** `AllConditionsAreMet`

**•** `AnyConditionIsMet`

```
Description

DeveloperName

FullName

IsActive

```

**Type**
textarea

**Properties**
Nillable

**Description**
A description that states the restriction placed on a user’s access to a catalog items eligibility.

**Type**
string

**Properties**
Filter, Group, Sort

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
string

**Properties**
Create, Group, Nillable

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies if the eligibility rule is active.

The default value is `false` .


Standard Objects SvcCatalogFilterCriteria

**Field** **Details**

```
Language

ManageableState

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Supported languages for eligibility rules

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
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Describes the manageable state of a catalog item that is contained in a package.

Possible values are:

**•** `beta` —Managed-Beta

**•** `deleted` —Managed-Proposed-Deleted

**•** `deprecated` —Managed-Proposed-Deprecated

**•** `deprecatedEditable` —SecondGen-Installed-Deprecated

**•** `installed` —Managed-Installed


### Standard Objects SvcCatalogItemDef

**Field** **Details**

**•** `installedEditable` —SecondGen-Installed-Editable

**•** `released` —Managed-Released

**•** `unmanaged` —Unmanaged

```
MasterLabel

Metadata

NamespacePrefix

NumOfRelatedItems

### SvcCatalogItemDef

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The label of the eligibility rule record.

**Type**
complexvalue

**Properties**
Create, Nillable, Update

**Description**
The metadata type associated with the SvcCatalogFilterCriteria object.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of catalog items that has the eligibility rule.

Represents a service catalog item that can be requested by a service catalog user. This object is available in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `search()`,
`update()`, `upsert()`


Standard Objects SvcCatalogItemDef

Special Access Rules

To access this object, get the Service Catalog Access permission set license, Employee Productivity Starter license, or Employee Productivity
Plus add-on license.

Fields

**Field** **Details**

```
Description

DeveloperName

FlowName

FulfillmentFlowId

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The definition of the catalog item. This field is visible on the Service Catalog page.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique developer name for the catalog item.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The flow called when the user navigates to the request page for the catalog item. Available
in API version 55.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the fulfillment flow. Available in API version 56.0 and later.

This field is a relationship field.

**Relationship Name**
FulfillmentFlow

**Relationship Type**
Lookup


Standard Objects SvcCatalogItemDef

**Field** **Details**

**Refers To**
SvcCatalogFulfillmentFlow

```
ImageId

ImageReference

InternalNotes

IsActive

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The image ID used for the catalog item.

This field is a relationship field.

**Relationship Name**
Image

**Relationship Type**
Lookup

**Refers To**
ContentAsset

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Derived field from `ImageId` to expose `ContentAssetId` on item definitions. Available
in API version 61.0 and later.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A place for the Service Catalog Builder to leave internal notes about the catalog item.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Derived field from `Status` to indicate whether the service catalog item is active.

The default value is `false` .

Available in API version 59.0 and later.


Standard Objects SvcCatalogItemDef

**Field** **Details**

```
IsAvailableToAllCustomers

IsFeatured

IsGuestAccessible

IsOutOfSync

Language

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Udpate

**Description**
Indicates whether the Service Catalog item is available to all customers. The default value is
`false` .

Available in API version 61.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether a catalog item is marked as a favorite for the org. Favorites display as a
featured item on the Service Catalog home page.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the Service Catalog item can be accessed by guest users. The default value
is `false` .

Available in API version 61.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the fulfillment flow that the Service Catalog item is based on has been
updated. Available in API version 58.0 and later.

The default value is `false` . If value is `true`, try updating and saving the service catalog
item again.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects SvcCatalogItemDef

**Field** **Details**

**Description**
Supported languages for catalog items.

```
Product

ShortDescription

Status

UsageType

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The product associated with the Service Catalog item. The value is derived from `UsageType` .
Available in API version 59.0 and later.

Possible values are:

**•** `FinancialServices`

**•** `ServiceCatalog` —Default

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The short description of the catalog item.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Allows the Service Catalog Builder to control whether the flow is displayed to users within
the Service Catalog.

Possible values are:

**•** `Deprecated`

**•** `Draft` —Default

**•** `PendingChanges`

**•** `Published`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The business type for which the Service Catalog is used. Available in API version 57.0 and
later.


### Standard Objects SvcCatalogRequest

**Field** **Details**

Possible values are:

**•** `CustomerService`

**•** `Employee` —Default

**•** `FinancialServices`

**•** `Industry`

### SvcCatalogRequest

Represents a request made by a user using the Service Catalog. Catalog builders use this object to report on Service Catalog activity.
This object is available in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

To access this object, get the Service Catalog Access permission set license, Employee Productivity Starter license, or Employee Productivity
Plus add-on license.

Fields

**Field** **Details**

```
CatalogItemDescription

CatalogItemName

CatalogItemVersion

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description for the catalog item.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Name of the catalog item.

**Type**
string


Standard Objects SvcCatalogRequest

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Version for the catalog item.

This is a calculated field. Available in API version 58.0 and later.

```
ClosedDate

CurrencyIsoCode

FlowInterviewGuid

IsClosed

ItemFlowVersion

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time when the request was closed. This field is automatically populated when
`IsClosed` is 'true'.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
ISO code of the currency. Must be one of the valid alphabetic, three-letter currency ISO codes
defined by the ISO 4217 standard, such as USD, GBP, or JPY. Must be unique within your
organization. Default value is `USD` -U.S. Dollar.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Unique GUID associated with the automation that was executed as part of the catalog item.
Available in API version 60.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the request has been resolved. This field is automatically checked when
`ClosedDate` is populated.

The default value is `false` .

**Type**
string


Standard Objects SvcCatalogRequest

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Version for the item flow.

This is a calculated field.

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
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The Service Catalog request number.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID for the owner record.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup


Standard Objects SvcCatalogRequest

**Field** **Details**

**Refers To**
Group, User

```
Status

SubmitterId

SvcCatalogItemDefinitionId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the service catalog request. Available in API version 60.0 and later.

Possible values are:

**•** `CompletedExecution` —Default

**•** `CreatedRequest`

**•** `StartedExecution`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID for the submitter record.

This is a relationship field.

**Relationship Name**
Submitter

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The catalog item that was used to create this request.

This is a relationship field.

**Relationship Name**
SvcCatalogItemDefinition

**Relationship Type**
Lookup


### Standard Objects SvcCatalogReqRelatedItem

**Field** **Details**

**Refers To**
SvcCatalogItemDef

```
TargetCustomerId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The customer ID that the request was submitted for. For example, when an agent runs a
catalog item for a given contact, the contact is represented by the `TargetCustomerId` .
Available in API version 61.0 and later.

This is a polymorphic relationship field.

**Relationship Name**
TargetCustomer

**Relationship Type**
Lookup

**Refers To**
Contact, User

### SvcCatalogReqRelatedItem

Represents an item related to a Service Catalog Request. This object is available in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

To access this object, get the Service Catalog permission set license, Employee Productivity Starter license, or Employee Productivity
Plus add-on license.

Fields

**Field** **Details**

```
Name

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


Standard Objects SvcCatalogReqRelatedItem

**Field** **Details**

**Description**
The name of the related item.

```
RelatedExternalId

RelatedInternalRecordId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Text containing an ID from any external system.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Salesforce record related to this request. This reference must be for an object that has
the following characteristics.

**•** It's a standard object.

**•** It must allow custom fields.

**•** It's referencable (that is, it can be the target of a lookup).

**•** It can be the target of a custom lookup field.

**•** It contains a Name field.

**•** It isn't dependent on a junction object.

**•** It isn't a virtual object or a setup object.

This is a polymorphic relationship field.

**Relationship Name**
RelatedInternalRecord

**Relationship Type**
Lookup

**Refers To**
Account, Address, Asset, AssociatedLocation, AuthorizationForm, AuthorizationFormConsent,
AuthorizationFormDataUse, AuthorizationFormText, BusinessBrand, Case, CommSubscription,
CommSubscriptionChannelType, CommSubscriptionConsent, CommSubscriptionTiming,
Contact, ContactPointAddress, ContactPointConsent, ContactPointEmail, ContactPointPhone,
ContactPointTypeConsent, Contract, ContractLineItem, Customer, DataUseLegalBasis,
DataUsePurpose, Employee, EngagementChannelType, Entitlement, Idea, Individual,
InternalOrganizationUnit, Lead, Location, MessagingEndUser, Opportunity, Order, OrderItem,
PartyConsent, Pricebook2, ProcessException, Product2, ProfileSkill, ProfileSkillEndorsement,
ProfileSkillUser, QuickText, Recommendation, Seller, ServiceContract, SocialPersona, SocialPost,
Solution, SurveyInvitation, SurveySubject, UserProvisioningRequest, VoiceCall


### Standard Objects Swarm

**Field** **Details**

```
SvcCatalogRequestId

### Swarm

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The SvcCatalogRequest record.

This is a relationship field.

**Relationship Name**
SvcCatalogRequest

**Relationship Type**
Lookup

**Refers To**
SvcCatalogRequest

Represents a team of agents, Salesforce users, or Slack users in a Slack channel or thread dedicated to solving a problem. This problem
can be related to a support case, incident, sales opportunity, or change request. This object is available in API version 55.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

To access this object for swarming in Salesforce, enable the Run Flows and Service Cloud User user permissions. For swarming in Slack,
connect Salesforce to Slack and enable the Run Flows and Slack Service User user permissions.

Fields

**Field** **Details**

```
CollaborationRoomId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the collaboration room.

This field is a relationship field.


Standard Objects Swarm

**Field** **Details**

**Relationship Name**
CollaborationRoom

**Relationship Type**
Lookup

**Refers To**
CollaborationRoom

```
CollaborationTool

CollaborationUrl

EndedDateTime

HelpNeeded

IsDedicatedChannel

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Tool used for swarming.

Possible values are:

**•** `None`

**•** `Slack`

The default value is `None` .

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
URL of the Slack channel or thread.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date and time the swarm ended.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Short description of the problem that the swarm is trying to solve.

**Type**
boolean


Standard Objects Swarm

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates if the swarm is happening in a dedicated channel ( `true` ) or in an existing channel
( `false` ).

The default value is `false` .

```
LastReferencedDate

LastViewedDate

MessageKey

Name

OwnerId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp when the current user last accessed this record, a record related to this record,
or a list view.

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
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Slack thread or message.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the swarm.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects Swarm

**Field** **Details**

**Description**
ID of the swarm owner.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

```
RelatedRecordId

StartedDateTime

Status

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the record the swarm’s problem is related to. The record can be of, for example, a case,
incident, sales opportunity, or change request.

This field is a polymorphic relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
Account, Case, ChangeRequest, Incident, Opportunity, Problem, User

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date and time the swarm started.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Status of the swarm.

Possible values are:

**•** `Closed`


### Standard Objects SwarmMember

**Field** **Details**

**•** `In Progress`

**•** `New`

**•** `Waiting (Custom)`

The default value is `New` .

```
UsageType

```

Associated Objects

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Type of swarm.

Possible values are:

**•** `CareMgmt` —Care Coordination

**•** `DealRoom` —Sales Channel

**•** `PartnerChannel` —Partner Account Channel

**•** `Swarming`

The default value is `Swarming` .

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SwarmFeed on page 55**
Feed tracking is available for the object.

**SwarmHistory on page 63**
History is available for tracked fields of the object.

**SwarmOwnerSharingRule on page 65**
Sharing rules are available for the object.

**SwarmShare on page 67**
Sharing is available for the object.

### SwarmMember

Represents a Salesforce member, such as an agent, of a swarm. This object is available in API version 55.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects SwarmMember

Special Access Rules

To access this object for swarming in Salesforce, enable the Run Flows and Service Cloud User user permissions. For swarming in Slack,
connect Salesforce to Slack and enable the Run Flows and Slack Service User user permissions.

Fields

**Field** **Details**

```
AssignedDateTime

CompletedDateTime

HelpNeeded

LastReferencedDate

LastViewedDate

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date and time the member is added to the swarm.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date and time the member exits the swarm or the swarm closes.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Short description of the problem that the swarm is trying to solve.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects SwarmMember

**Field** **Details**

**Description**
Timestamp when the current user last viewed this record or list view. If this value is null, the
user might have only accessed this record or list view ( `LastReferencedDate` ) but not
viewed it.

```
Name

OwnerId

RelatedRecordId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the swarm or record number.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the Salesforce user assigned to a swarm.

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
Create, Filter, Group, Sort, Update

**Description**
ID of the record the swarm’s problem is related to. The record can be of, for example, a case,
incident, sales opportunity, or change request.

This field is a polymorphic relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
Account, Case, ChangeRequest, Incident, Opportunity, Problem, User


Standard Objects SwarmMember

**Field** **Details**

```
Status

SwarmId

```

Associated Objects

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Status of the swarm member or swarm.

Possible values are:

**•** `Closed`

**•** `In Progress`

**•** `New`

The default value is `New` .

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the swarm the member belongs to.

This field is a relationship field.

**Relationship Name**
Swarm

**Relationship Type**
Lookup

**Refers To**
Swarm

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SwarmMemberFeed on page 55**
Feed tracking is available for the object.

**SwarmMemberHistory on page 63**
History is available for tracked fields of the object.

**SwarmMemberOwnerSharingRule on page 65**
Sharing rules are available for the object.

**SwarmMemberShare on page 67**
Sharing is available for the object.


### Standard Objects TabDefinition TabDefinition

Represents a custom tab. Returns only the tabs that the current user has access to. This object is available in API version 43.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `search()`

Fields

**Field Name** **Details**

```
DurableId

IsAvailableInAloha

IsAvailableInDesktop

IsAvailableInLightning

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Unique identifier for the tab. Always retrieve this value before using it, because
the value isn’t guaranteed to stay the same from one release to the next. Simplify
queries by using this field instead of making multiple queries.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether the tab is available in Salesforce Classic.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether the tab is available on desktop.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether the tab is available in Lightning Experience.


Standard Objects TabDefinition

**Field Name** **Details**

```
IsAvailableInMobile

IsCustom

Label

MobileUrl

Name

SobjectName

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether the tab is available in the Salesforce mobile app.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether the tab is a custom tab created by admins in the org.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The localized label corresponding to the `MasterLabel` field in the Tooling
API object.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The URL that can be used to launch this tab in the Salesforce mobile app.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The developer name of the tab.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects TagDefinition

**Field Name** **Details**

**Description**

The name of the sObject corresponding to the tab.

```
Url

### TagDefinition

```

Defines the attributes of child Tag objects.

Supported Calls

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The URL that can be used to launch this tab on desktop.

`delete()`, `describeSObjects()`, `query()`, `retrieve()`, `search()`, `undelete()`, `update()`

Special Access Rules

As of Summer ’20 and later, only authenticated internal and external users can access this object.

Fields

**Field** **Detail**

```
Name

Type

```

**Type**
string

**Properties**
Filter, Nillable, Update

**Description**
Identifies the tag word or phrase.

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
Defines the visibility of a tag. Possible value are:

**•** **Public** : The tag can be viewed and manipulated between all users in an organization.


Standard Objects TagDefinition

**Field** **Detail**

**•** **Personal** : The tag can be viewed or manipulated only by a user with a matching
`OwnerId` .

Usage

When you create a tag for a record, an association is created with to a corresponding TagDefinition:

**•** If the value in the tag's `Name` field is new, a new TagDefinition record is automatically created and becomes the parent of the tag.

**•** If the value in the tag's `Name` field already exists in a TagDefinition, that TagDefinition automatically becomes the parent of the tag.

Each TagDefinition record has a one-to-many relationship with its child tag records.

The following standard objects represent tags for records:

**•** AccountTag

**•** AssetTag

**•** CampaignTag

**•** CaseTag

**•** ContactTag

**•** ContractTag

**•** DocumentTag

**•** EventTag

**•** LeadTag

**•** NoteTag

**•** OpportunityTag

**•** SolutionTag

**•** TaskTag

Custom objects may also be tagged. Tags for custom objects are identified by a suffix of two underscores immediately followed by the
word `tag` . For example, a custom object named `Meeting` has a corresponding tag named Meeting__tag in that organization’s
WSDL. Meeting__tag is only valid for `Meeting` objects.

TagDefinition is useful for mass operations on any tag record. For instance, if you want to rename existing tags, you can search for the
appropriate TagDefinition object, update it, and the child tag's `Name` values are also changed. The following Java example replaces all
`WC` tags with the phrase `West Coast` :

```
   public void tagDefinitionSample() {

     String soqlQuery = "SELECT Id, Name FROM TagDefinition " +

       "WHERE Name = 'WC'";

     QueryResult qResult = null;

     try {

       qResult = connection.query(soqlQuery);

      TagDefinition tagDef = (TagDefinition) qResult.getRecords()[0];

      tagDef.setName("West Coast");

      connection.update(new SObject[]{tagDef});

     } catch (ConnectionException ce) {

      ce.printStackTrace();

```


### Standard Objects Task

```
     }

   }

```

When a tag is deleted, its parent TagDefinition will also be deleted if the name is not being used; otherwise, the parent remains. Deleting
a TagDefinition sends it to the Recycle Bin, along with any associated tag entries.

### Task

Represents a business activity such as making a phone call or other to-do items. In the user interface, Task and Event records are collectively
referred to as activities.

Note: Task fields related to calls are exclusive to Salesforce CRM Call Center. Also, `query()`, `delete()`, and `update()`
aren't allowed with tasks related to more than one contact in API versions 23.0 and earlier.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Field Type**

```
AccountId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the ID of the related Account. The `AccountId` is determined as follows.

If the value of `WhatId` is any of these objects, Salesforce uses that object's `AccountId` .

**•** Account

**•** Opportunity

**•** Contract

**•** Custom object that is a child of Account

If the value of the `WhatId` field is any other object, and the value of the `WhoId` field is a
Contact object, then Salesforce uses that contact’s `AccountId` . (If your organization uses
Shared Activities, then Salesforce uses the `AccountId` of the primary contact.)

Otherwise, Salesforce sets the value of the `AccountId` field to `null` .

For information on IDs, see ID Field Type.

This is a relationship field.

**Relationship Name**
Account


Standard Objects Task

**Field** **Field Type**

**Relationship Type**
Lookup

**Refers To**
Account

```
ActivityDate

CallDisposition

CallDurationInSeconds

CallObject

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Represents the due date of the task. This field has a timestamp that is always set to midnight
in the Coordinated Universal Time (UTC) time zone. The timestamp is not relevant; do not
attempt to alter it to accommodate time zone differences. Label is **Due Date** .

This field can’t be set or updated for a recurring task ( `IsRecurrence` is `true` ).

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Represents the result of a given call, for example, “we'll call back,” or “call unsuccessful.” Limit
is 255 characters.

Not subject to field-level security, available for any user in an organization with Salesforce
CRM Call Center.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Duration of the call in seconds.

Not subject to field-level security, available for any user in an organization with Salesforce
CRM Call Center.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Name of a call center. Limit is 255 characters.


Standard Objects Task

**Field** **Field Type**

Not subject to field-level security, available for any user in an organization with Salesforce
CRM Call Center.

```
CallType

CompletedDateTime

ConnectionReceivedId

ConnectionSentId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The type of call being answered. Possible values are:

**•** `Inbound`

**•** `Internal`

**•** `Outbound`

When working with PushTopic, the `CallType` values display as `1` for `Inbound`, `0` for
`Internal`, and `2` for `Outbound` .

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

The status is a dynamic enum. If the Closed mapping is changed it won’t cause an update
of existing tasks. Only new insert/update operations are affected.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the PartnerNetworkConnection that shared this record with your organization. This
field is available if you enabled Salesforce to Salesforce.

**Type**
reference


Standard Objects Task

**Field** **Field Type**

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the PartnerNetworkConnection that you shared this record with. This field is available
if Salesforce to Salesforce is enabled. This field is supported in API versions 14.0 and earlier.
In API version 15.0 and later, this field’s value is null. You can use the new
PartnerNetworkRecordConnection object to forward records to connections.

```
Description

IsArchived

IsClosed

IsHighPriority

IsRecurrence

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Contains a text description of the task. The text provided in the Description field shows in
the Comments field on the task record detail page.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the event has been archived. The default value of this field is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the task has been completed ( `true` ) or not ( `false` ). The default value
of this field is `false` . Is only set indirectly via the `Status` picklist. Label is **Closed** .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates a high-priority task. This field is derived from the `Priority` field. The default
value of this field is `false` .

**Type**
boolean


Standard Objects Task

**Field** **Field Type**

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the task is scheduled to repeat itself ( `true` ) or only occurs once ( `false` ).
The default value of this field is `false` . This field is read-only on update, but not on create.
If this field value is `true`, then `RecurrenceStartDateOnly`,
`RecurrenceEndDateOnly`, `RecurrenceType`, and any recurrence fields associated
with the given recurrence type must be populated. See Usage section.

```
IsReminderSet

IsVisibleInSelfService

OwnerId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a popup reminder has been set for the task ( `true` ) or not ( `false` ). The
default value of this field is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a task associated with an object can be viewed in the Customer Portal
( `true` ) or not ( `false` ).

If your organization has digital experiences enabled, tasks marked
`IsVisibleInSelfService` are visible to any external user in the Experience Cloud
site, as long as the user has access to the record the task was created on.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the User or Group who owns the record. Label is **Assigned To ID** . This field accepts
Groups of type Queue only.

In the user interface, Group IDs correspond with the queue’s list view names. To create or
update tasks assigned to Group, use v48.0 or later.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup


Standard Objects Task

**Field** **Field Type**

**Refers To**
Group, User

```
Priority

RecurrenceActivityId

RecurrenceDayOfMonth

RecurrenceDayOfWeekMask

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Required. Indicates the importance or urgency of a task, such as high or low. The default
value of this field is `Normal` .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Read-only. Not required on create. ID of the main record of the recurring task. Subsequent
occurrences have the same value in this field.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The day of the month in which the task repeats.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The day or days of the week on which the task repeats. This field contains a bitmask. The
values are as follows:

**•** `Sunday = 1`

**•** `Monday = 2`

**•** `Tuesday = 4`

**•** `Wednesday = 8`

**•** `Thursday = 16`

**•** `Friday = 32`

**•** `Saturday = 64`


Standard Objects Task

**Field** **Field Type**

Multiple days are represented as the sum of their numerical values. For example, Tuesday
and Thursday = 4 + 16 = 20.

```
RecurrenceEndDateOnly

RecurrenceInstance

RecurrenceInterval

RecurrenceMonthOfYear

RecurrenceRegeneratedType

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The last date on which the task repeats. This field has a timestamp that is always set to
midnight in the Coordinated Universal Time (UTC) time zone. The timestamp is not relevant;
do not attempt to alter it to accommodate time zone differences.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The frequency of the recurring task.

Possible values are:

**•** `First` —1st

**•** `Fourth` —4th

**•** `Last` —last

**•** `Second` —2nd

**•** `Third` —3rd

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The interval between recurring tasks.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The month of the year in which the task repeats.

**Type**
picklist


Standard Objects Task

**Field** **Field Type**

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Represents what triggers a repeating task to repeat. Add this field to a page layout together
with the `RecurrenceInterval` field, which determines the number of days between
