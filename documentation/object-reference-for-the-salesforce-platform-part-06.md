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

Knowledge__kav on page 2993 is derived from this object.

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
Knowledge__kav on page 2993). For Knowledge in Salesforce Classic, the type of article is determined by the `ArticleType` field and
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

This object represents a value in the lead status picklist (see Lead on page 3039). The lead status picklist provides additional information
about the status of a Lead on page 3039, such as whether a given status value represents a converted Lead on page 3039. Query this object
to retrieve the set of values in the lead status picklist, and then use that information while processing Lead on page 3039 objects to
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

For additional information about feeds, see FeedItem on page 2526.

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

**Description**
The state of a party in the queue.

Possible values are:

**•** `canceled`

**•** `entered`

**•** `exited`

**•** `ready`

**•** `waiting`

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time when a party signed up for the queue.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID for the queue.


### Standard Objects LoginAsEventLog LoginAsEventLog LoginAsEventLog contains details about when a user logs in as another user in your org. This object is available in API version 61.0 and

later.

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

DelegatedUserIdentifier

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
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique ID that identifies the user who’s logging in as, or impersonating, another user. For
example: `00530000009M943` .


Standard Objects LoginAsEventLog

**Field** **Details**

```
DelegatedUserName

LoginKey

RequestIdentifier

RunTime

SessionKey

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The username of the user who’s logging in as, or impersonating, another user.

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
event in a given transaction has the same `RequestIdentifier` . For example:
`3nWgxWbDKWWDIk0FKfF5DV` .

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
The impersonated user’s unique session ID. You can use this value to identify all user events
within a session. When a user logs out and logs in again, a new session is started. For Login
Event Type, this field is usually null because the event is captured before a session is created.
For example: `d7DEq/ANa7nNZZVD` .


### Standard Objects LoginEvent

**Field** **Details**

```
Timestamp

Uri

UserIdentifier

### LoginEvent

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
The URI of the page that’s receiving the request. For example: `/home/home.jsp` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique ID that identifies the user who is being logged in as, or impersonated, by another
user. For example: `005000000000123` .

[The documentation has moved to LoginEvent in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/sforce_api_objects_loginevent.htm) _Platform Events Developer Guide_ .

### LoginEventLog

Login event logs contain details about your Salesforce org's user login history. This object is available in API version 61.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.


Standard Objects LoginEventLog

Fields

**Field** **Details**

```
ApiType

ApiVersion

AuthenticatedMethodReference

BrowserType

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

**•** `I` —SOAP Cross Instance

**•** `M` —SOAP Metadata

**•** `O` —Old SOAP

**•** `P` —SOAP Partner

**•** `S` —SOAP Apex

**•** `T` —SOAP Tooling

**•** `X` —XmlRPC

**•** `f` —Feed

**•** `l` —Live Agent

**•** `p` —SOAP ClientSync

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version of the API that’s being used. For example: `36.0` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The authentication method used by a third-party identification provider for an OpenID
Connect single sign-on protocol.

**Type**
string


Standard Objects LoginEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The identifier string returned by the browser used at login.

Example values are:

**•** `Go-http-client/1.1`

**•** `Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv%3A50.0)`

```
                     Gecko/20100101 Firefox/50.0

```

**•** `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6)`

```
                     AppleWebKit/537.36 (KHTML, like Gecko)

                     Chrome/51.0.2704.84 Safari/537.36

```

```
CipherSuite

ClientIp

CpuTime

DatabaseTotalTime

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The TLS cipher suite used for the login. Values are OpenSSL-style cipher suite names, with
[hyphen delimiters. For more information, see OpenSSL Cryptography and SSL/TLS Toolkit.](https://www.openssl.org/source/)

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


Standard Objects LoginEventLog

**Field** **Details**

**Description**
The time in nanoseconds for a database round trip. Includes time spent in the JDBC driver,
network to the database, and `DatabaseTotalTime` . Compare this field to `CpuTime`
to determine whether performance issues are occurring in the database layer or in your own
code.

```
ForwardedForIp

LoginKey

LoginStatus

LoginSubType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reserved for future use.

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
The status of the login attempt. For successful logins, the value is LOGIN_NO_ERROR. All
other values indicate errors or authentication issues. For details, see Login Event Type —
LOGIN_STATUS Values on page 2287.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of login flow used. Possible values are:

**•** uiup—UI Username-Password

**•** oauthpassword—OAuth Username-Password

**•** oauthtoken—OAuth User-Agent

**•** oauthhybridtoken—OAuth User-Agent for Hybrid Apps

**•** oauthtokenidtoken—OAuth User-Agent with ID Token


Standard Objects LoginEventLog

**Field** **Details**

**•** oauthclientcredential—OAuth Client Credential

**•** oauthcode—OAuth Web Server

**•** oauthhybridauthcode—OAuth Web Server for Hybrid Apps

```
LoginType

RequestIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of login used to access the session. Possible values are:

**•** 7—AppExchange

**•** A—Application

**•** s—Certificate-based login

**•** k—Chatter Communities External User

**•** n—Chatter Communities External User Third Party SSO

**•** r—Employee Login to Community

**•** z—Lightning Login

**•** l—Networks Portal API Only

**•** 6—Remote Access Client

**•** i—Remote Access 2.0

**•** I—Other Apex API

**•** R—Partner Product

**•** w—Passwordless Login

**•** 3—Customer Service Portal

**•** q—Partner Portal Third-Party SSO

**•** 9—Partner Portal

**•** 5—SAML Idp Initiated SSO

**•** m—SAML Chatter Communities External User SSO

**•** b—SAML Customer Service Portal SSO

**•** c—SAML Partner Portal SSO

**•** h—SAML Site SSO

**•** 8—SAML Sfdc Initiated SSO

**•** E—SelfService

**•** j—Third Party SSO

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects LoginEventLog

**Field** **Details**

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `RequestIdentifier` . For example:
`3nWgxWbDKWWDIk0FKfF5DV` .

```
RequestStatus

RunTime

SessionKey

SourceIp

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The status of the request for a page view or user interface action.

Possible values are:

**•** `S` —Success. Salesforce handled the request successfully. If an Apex controller throws
an exception, this status is also returned.

**•** `F` —Failure. Typically 4xx or 5xx HTTP codes, such as no permission to view page, page
took too long to render, page is read-only.

**•** `U` —Undefined

**•** `A` —Authorization Error

**•** `R` —Redirect. Typically a 3xx HTTP code, possibly initiated by an Apex controller in a
Visualforce page.

**•** `N` —Not Found. 404 error.

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
When a user logs out and logs in again, a new session is started. For Login Event Type, this
field is usually null because the event is captured before a session is created. For example:
`d7DEq/ANa7nNZZVD` .

**Type**
string


Standard Objects LoginEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The source IP of the login request.

```
Timestamp

TransportLayerSecurityProtocol

Uri

UserIdentifier

UserName

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
The TLS protocol used for the login.

Possible values are:

**•** `1.0`

**•** `1.1`

**•** `1.2`

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


Standard Objects LoginEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The username that’s used for login.

```
UserType

Username

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

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The username that’s used for login.


### Standard Objects LoginGeo LoginGeo

Represents the geographic location of the user’s IP address for a login event. Due to the nature of geolocation technology, the accuracy
of geolocation fields (for example, country, city, postal code) may vary. This object is available in API version 34.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Only users with Manage Users permissions can access this object.

Fields

**Field** **Details**

```
City

Country

CountryIso

Latitude

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The city where the user’s IP address is physically located. This value is not localized.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The country where the user’s IP address is physically located. This value is not localized.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ISO 3166 code for the country where the user’s IP address is physically located. For more
[information, see Country Codes - ISO 3166](http://www.iso.org/iso/country_codes.htm)

**Type**
double

**Properties**
Filter, Nillable, Sort


Standard Objects LoginGeo

**Field** **Details**

**Description**
The latitude where the user’s IP address is physically located.

```
LoginTime

Longitude

PostalCode

Subdivision

```

Usage

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
Time of the login attempt, in GMT time zone.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The longitude where the user’s IP address is physically located.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The postal code where the user’s IP address is physically located. This value is not localized.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the subdivision where the user’s IP address is physically located. In the U.S., this
value is usually the state name (for example, Pennsylvania). This value is not localized.

The API allows you to do many powerful queries. A few examples are:

**Sample Query** **Query String**

Query showing the country for a login event, where `SELECT Country FROM LoginGeo WHERE Id =`
`Id=LoginGeoId` from AuthSession `'0LE###############'`

Query showing the city and postal code for a login event, where `SELECT City, PostalCode FROM LoginGeo WHERE`
`Id=LoginGeoId` from LoginHistory `Id = '0SO###############'`


### Standard Objects LoginHistory LoginHistory

Represents the login history for all successful and failed login attempts for organizations and enabled portals. This object is available in
API version 21.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Special Access Rules

With one exception, only users with Manage Users or Monitor Login History permissions can access this object. The exception is that, in
API version 37.0 and later, all users can retrieve their own login history records.

Fields

**Field** **Details**

```
ApiType

ApiVersion

Application

AuthMethodReference

```

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
Indicates the API type, for example `Soap Enterprise` . Label is **API Type** .

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
Displays the API version used by the client. Label is **API Version** .

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
The application used to access the organization. Label is **Application** .

**Type**
string


Standard Objects LoginHistory

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The authentication method used by a third-party identification provider for an OpenID
Connect single sign-on protocol. This field is available in API version 51.0 and later. Label is
**Authentication Method Reference** .

```
AuthenticationServiceId

Browser

CipherSuite

ClientVersion

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 18-character ID for an authentication service for a login event. For example, you can use
this field to identify the SAML or authentication provider configuration with which the user
logged in. This field is available in API version 34.0 and later. Label is **Authentication Service**
**Id** .

This field is a polymorphic relationship field.

**Relationship Name**
AuthenticationService

**Relationship Type**
Lookup

**Refers To**
AuthProvider, SamlSsoConfig

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
The current browser version. Label is **Browser** .

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The TLS cipher suite used for the login. Values are OpenSSL-style cipher suite names, with
[hyphen delimiters. For more information, see OpenSSL Cryptography and SSL/TLS Toolkit.](https://www.openssl.org/source/)
This field is available in API version 37.0 and later.

**Type**
string


Standard Objects LoginHistory

**Field** **Details**

**Properties**
Group, Nillable, Sort

**Description**
Version of the API client. Label is **Client Version** .

```
CountryIso

ForwardedForIp

LoginGeoId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ISO 3166 code for the country where the user’s IP address is physically located. For more
[information, see Country Codes - ISO 3166. This field is available in API version 37.0 and later.](http://www.iso.org/iso/country_codes.htm)

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The value in the `X-Forwarded-For` header of HTTP requests sent by the client. For
logins that use one or more HTTP proxies, the `X-Forwarded-For` header is sometimes
used to store the origin IP and all proxy IPs.

The `ForwardedForIp` field stores whatever value the client sends, which might not be
an IP address. The maximum length is 256 characters. Longer values are truncated. The
`ForwardedForIp` field isn’t populated for logins completed via OAuth flows or single
sign-on (SSO).

Available in API version 61.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 18-character ID for the record of the geographic location of the user for a successful or
unsuccessful login event. The accuracy of geolocation fields like country, city, or postal code
can vary because of the nature of the technology.

The Manage Users permission is required for accessing this field. This field is available in API
version 34.0 and later.

This field is a relationship field.

**Relationship Name**
LoginGeo

**Relationship Type**
Lookup


Standard Objects LoginHistory

**Field** **Details**

**Refers To**
LoginGeo

```
LoginSubType

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of login flow used.

**•** `InternalSalesforceAuthentication`  - `Internal Salesforce`

```
   Authentication

```

This subtype is for internal use only.

**•** `OauthClientCredentials`  - `OAuth Client Credentials`

**•** `OauthHybridRefreshToken`  - `OAuth Refresh Token for Hybrid`

```
   Apps

```

**•** `OauthHybridTokenExchange`  - `OAuth Token Exchange for Hybrid`

```
   Apps

```

**•** `OauthHybridUserAgent`  - `OAuth User-Agent for Hybrid Apps`

**•** `OauthHybridWebServer`  - `OAuth Web Server for Hybrid Apps`

**•** `OauthOtpLogin`  - `OAuth OTP Login`

**•** `OauthRefreshToken`  - `OAuth Refresh Token`

**•** `OauthTokenExchange`  - `OAuth Token Exchange`

**•** `OauthUserAgent`  - `OAuth User-Agent`

**•** `OauthUserAgentIdToken`  - `OAuth User-Agent with ID Token`

**•** `OauthUsernamePassword`  - `OAuth Username-Password`

**•** `OauthWebServer`  - `OAuth Web Server`

**•** `SoapApiLogin`  - `SOAP API`

This subtype is for internal use only.

**•** `SoapApiLoginMobile`  - `SOAP API (Mobile)`

This subtype is for internal use only.

**•** `SoapApiLoginNetworksPortal`  - `SOAP API (Networks Portal)`

This subtype is for internal use only.

**•** `SoapApiLoginPortal`  - `SOAP API (Portal)`

This subtype is for internal use only.

**•** `SoapApiLoginSelfService`  - `SOAP API (Self-Service)`

This subtype is for internal use only.

**•** `UiPasswordReset`  - `UI Password Reset`


Standard Objects LoginHistory

**Field** **Details**

**•** `UsernamePasswordUiLogin`                   - `UI Username-Password`

Label is **Login Subtype** .

```
LoginTime

LoginType

```

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
Time zone is based on GMT. Label is **Login Time** .

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of login used to access the session.

**•** `AppExchange`  - `AppExchange`

**•** `Application`  - `Application`

**•** `Certificate`  - `Certificate-based login`

**•** `ChatterCommunityPortalUnPwd`  - `Chatter Communities External`

```
   User

```

**•** `ChatterCommunityThirdPartySso`  - `Chatter Communities`

```
   External User Third Party SSO

```

**•** `CrossTenantLogin`  - `Cross Tenant Login` —For internal use only.

**•** `EmployeeLoginToCommunity`  - `Employee Login to Community`

**•** `HelpAndTraining`  - `Help And Training`

**•** `IeOfflineClient`  - `Offline Client`

**•** `LightningLogin`  - `Lightning Login`

**•** `NetworksPortalApiOnly`  - `Networks Portal API Only`

**•** `Oauth, Remote Access Client`  - `Remote Access Client`

**•** `Oauth2, Remote Access 2.0`  - `Remote Access 2.0`

**•** `OtherApi`  - `Other Apex API`

**•** `Partner`  - `Partner Product`

**•** `PasswordlessLogin`  - `Passwordless Login`

**•** `PasswordlessPasskeyLogin`  - `Passwordless Login via Passkeys`
(beta)

Passwordless login with passkeys is a pilot or beta service that is subject to the Beta
[Services Terms at Agreements - Salesforce.com or a written Unified Pilot Agreement if](https://www.salesforce.com/company/legal/agreements/)
[executed by Customer, and applicable terms in the Product Terms Directory. Use of this](https://ptd.salesforce.com/?_ga=2.247987783.1372150065.1709219475-629000709.1639001992)
pilot or beta service is at the Customer's sole discretion.


Standard Objects LoginHistory

**Field** **Details**

**•** `Portal`                   - `Customer Service Portal`

**•** `PortalThirdPartySso`                   - `Customer Service Portal Third-Party`

```
                     SSO

```

**•** `PrmPortalThirdPartySso`                   - `Partner Portal Third-Party SSO`

**•** `PrmPortal`                   - `Partner Portal`

**•** `Saml`                   - `SAML Idp Initiated SSO`

**•** `SamlChatterNetworks`                   - `SAML Chatter Communities External`

```
                     User SSO

```

**•** `SamlCspPortal`                   - `SAML Customer Service Portal SSO`

**•** `SamlPrmPortal`                   - `SAML Partner Portal SSO`

**•** `SamlSite`                   - `SAML Site SSO`

**•** `Saml2`                   - `SAML Sfdc Initiated SSO`

**•** `SelfService`                   - `SelfService`

**•** `ThirdPartySso`                   - `Third Party SSO`

Label is **Login Type** .

```
LoginUrl

NetworkId

OptionsIsGet

OptionsIsPost

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
URL from which the login request is coming. Label is **Login URL** .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Experience Cloud site that the user is logging in to. This field is available in API
version 31.0 and later, if Salesforce Experience Cloud sites are enabled for your org.

**Type**
boolean

**Properties**
Filter

**Description**
The HTTP method used for the session login is a GET request.

**Type**
boolean


Standard Objects LoginHistory

**Field** **Details**

**Properties**
Filter

**Description**
The HTTP method used for the session login is a POST request.

```
Platform

SourceIp

Status

TlsProtocol

```

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
Operating system on the login machine. Label is **Platform** .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the incoming client request that first reaches Salesforce during a login. For
example, `126.7.4.2` .

For clients that redirect through one or more HTTP proxies, this field stores the IP address of
the first proxy to reach Salesforce. To better identify the origin IP for these cases, check the
`ForwardedForIp` field instead.

The `SourceIp` field doesn't support the `LIKE` [comparison operator.](https://developer.salesforce.com/docs/atlas.en-us.260.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_select_comparisonoperators.htm)

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
Displays the status of the attempted login. Status is either success or a reason for failure.
Label is **Status** .

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The TLS protocol used for the login. Possible values are:

**•** `TLS 1.0`

**•** `TLS 1.1`

**•** `TLS 1.2`


Standard Objects LoginHistory

**Field** **Details**

**•** `TLS 1.3`

**•** `Unknown`

This field is available in API version 37.0 and later.

```
UserId

```

Usage

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the user logging in. Label is **User ID** .

Not all fields are filterable. You can only filter on the following fields:

**•** `AuthenticationServiceId`

**•** `CipherSuite`

**•** `CountryIso`

**•** `Id`

**•** `LoginTime`

**•** `LoginType`

**•** `LoginUrl`

**•** `NetworkId`

**•** `OptionsIsGet`

**•** `OptionsIsPost`

**•** `TlsProtocol`

**•** `UserId`

The API allows you to do many powerful queries. A few examples are:

**Sample Query** **Query String**

Simple query showing UserId & LoginTime for each user `SELECT UserId, LoginTime from LoginHistory;`

Query showing logins only after a specified date and time `SELECT UserId, LoginTime from LoginHistory`

```
                          WHERE LoginTime > 2010-09-20T22:16:30.000Z;

```

Query showing logins for a specific time interval

Query showing the authentication service for a SAML login event,
where `Id=AuthenticationServiceId` from LoginHistory

```
SELECT UserId, LoginTime from LoginHistory

WHERE LoginTime > 2010-09-20T22:16:30.000Z

AND LoginTime < 2010-09-21T22:16:30.000Z;

SELECT DeveloperName, Issuer, Version FROM

SamlSsoConfig WHERE Id =

'0LE###############'

```


### Standard Objects LoginIp

**Sample Query** **Query String**

Query showing the authentication service for an authentication
provider login event, where
`Id=AuthenticationServiceId` from LoginHistory

### LoginIp

```
SELECT Type, DeveloperName FROM

AuthProvider WHERE Id =

'0SO###############'

```

Represents a validated IP address. This object is available in version 28.0 and later.

Supported Calls

`describeSObjects()`, `delete()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ChallengeMethod

ChallengeSentDate

IsAuthenticated

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The challenge method used to confirm the user’s identity. Possible values include the
following.

**•** `Email`

**•** `SMS`

**•** `TOTP_CHOICE` : The user chooses multi-factor authentication.

**•** `TOTP_ONLY` : The user is required to use multi-factor authentication.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the user was authenticated.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, the user has already been authenticated.


### Standard Objects LogoutEventLog

**Field** **Details**

```
SourceIp

UsersId

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address the user logged in from.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user associated with this item.

This is a relationship field.

**Relationship Name**
Users

**Relationship Type**
Lookup

**Refers To**
User

At every login, the IP address of the login request is checked against the validated IP addresses using LoginIp. A match means the login
IP address is a known IP address. If there’s no match, the address is unknown, and the user is asked to confirm their identity.

### LogoutEventLog

Contains details of user sessions ending or being revoked. This object is available in API version 65.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.


Standard Objects LogoutEventLog

Fields

**Field** **Details**

```
ApiType

ApiVersion

AppType

```

**Type**

Contains details of user sessions ending or being revoked.

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
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version of the API that’s being used.

For example: `36.0` .

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The application type that was in use upon logging out.

**Example Values**

**•** `1000` : Application

**•** `1007` : SFDC Application

**•** `1014` : Chat

**•** `2501` : CTI


Standard Objects LogoutEventLog

**Field** **Details**

**•** `2514` : OAuth

**•** `3475` : SFDC Partner Portal

```
BrowserType

ClientIp

ClientVersion

IsUserInitiatedLogout

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The identifier string returned by the browser used at login.

Example values are:

**•** `Go-http-client/1.1`

**•** `Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv%3A50.0)`

```
   Gecko/20100101 Firefox/50.0

```

**•** `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6)`

```
   AppleWebKit/537.36 (KHTML, like Gecko)

   Chrome/51.0.2704.84 Safari/537.36

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
The version of the client that was in use upon logging out.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
The value is 1 if the user intentionally logged out of the organization by clicking the Logout
button. If the user’s session timed out due to inactivity or another implicit logout action, the
value is 0.


Standard Objects LogoutEventLog

**Field** **Details**

```
LoginKey

PlatformType

RequestIdentifier

ResolutionType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The code for the client platform. If a timeout caused the logout, this field is null.

**Example Values**

**•** `1000` : Windows

**•** `1008` : Windows 2003

**•** `1013` : Windows 8.1

**•** `1015` : Windows 10

**•** `2003` : Macintosh/Apple OSX

**•** `4000` : Linux

**•** `5005` : Android

**•** `5006` : iPhone

**•** `5007` : iPad

**•** `5200` : Android 10.0

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


Standard Objects LogoutEventLog

**Field** **Details**

**Description**
The screen resolution of the client. If a timeout caused the logout, this field is null.

```
SessionKey

SessionLevel

SessionType

```

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
The security level of the session that was used when logging out.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The session type that was used when logging out.

**Possible Values**

**•** `A` : API

**•** `I` : APIOnlyUser

**•** `N` : ChatterNetworks

**•** `Z` : ChatterNetworksAPIOnly

**•** `C` : Content

**•** `P` : OauthApprovalUI

**•** `O` : Oauth2

**•** `T` : SiteStudio

**•** `R` : SitePreview

**•** `S` : SubstituteUser

**•** `B` : TempContentExchange

**•** `G` : TempOauthAccessTokenFrontdoor

**•** `Y` : TempVisualforceExchange

**•** `F` : TempUIFrontdoor

**•** `U` : UI


### Standard Objects LogoutEventStream

**Field** **Details**

**•** `E` : UserSite

**•** `V` : Visualforce

**•** `W` : WDC_API

```
Timestamp

UserIdentifier

UserType

### LogoutEventStream

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

### When a customer logs out by using the Logout button, the TIMESTAMP field records the

actual logout time. However, when a customer is logged out automatically, Salesforce detects
the event by using a process that runs every 15 minutes. `TIMESTAMP` values can reflect a
logout time up to 15 minutes later than the actual automatic logout time.

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

[The documentation has moved to LogoutEventStream in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/sforce_api_objects_logouteventstream.htm) _Platform Events Developer Guide_ .

### LookedUpFromActivity

This read-only object is displayed as a related list on an activity record (an event or a task); the list contains records that have custom
lookup relationships from the activity to another object. This object is not queryable.


Standard Objects LookedUpFromActivity

Supported Calls

```
   describeSObjects()

```

Fields

**Field Name** **Details**

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

For information on IDs, see Field Types

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

**•** The date of an event if `IsAllDayEvent` is set to `true`

This field has a time stamp that is always set to midnight in the Universal Time
Coordinated (UTC) time zone. The time stamp doesn’t represent the time of the
activity; don’t attempt to alter it to accommodate time zone differences. Label
is `Date` .

**Type**
dateTime

**Properties**
Aggregate, Filter, Nillable, Sort


Standard Objects LookedUpFromActivity

**Field Name** **Details**

**Description**
Contains the event’s due date if the `IsAllDayEvent` flag is set to `false` .
The time portion of this field is always transferred in the Coordinated Universal
Time (UTC) time zone. Translate the time portion to or from a local time zone for
the user or the application, as appropriate. Label is **Due Date Time** .

The value for this field and `StartDateTime` must match, or one of them
must be `null` .

```
ActivitySubtype

ActivityType

CallDisposition

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Provides standard subtypes to facilitate creating and searching for specific activity
subtypes. This field isn’t updateable.

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
Represents one of the following values: `Call`, `Email`, `Meeting`, or `Other` .
Label is `Type` . These are default values, and can be changed.

`ActivityType` is the union of `TaskType` and `EventType` . If the same activity
appears in both dynamic picklists, duplicate activities appear.

`TaskType` and `EventType` can each have a `Call` type. Internally, they are
distinct from each other.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects LookedUpFromActivity

**Field Name** **Details**

**Description**
Represents the result of a given call; for example, “we’ll call back,” or “call
unsuccessful.” Limit is 255 characters.

```
CallDurationInSeconds

CallObject

CallType

CompletedDateTime

```

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

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time the task was saved with a Closed status.

**•** For insert, if the task is saved with a Closed status the field is set. If the task is
saved with an Open status the field is set to NULL.

**•** For update, if the task is saved with a new Closed status, the field is reset.

If the task is saved with a new non-closed status, the field is reset to NULL.

If the task is saved with the same closed status (that is, unchanged) there is
no change to the field.

Note: The status is a dynamic enum. If the Closed mapping is changed
it won’t cause an update of existing tasks. Only new insert/update
operations are affected.


Standard Objects LookedUpFromActivity

**Field Name** **Details**

```
Description

DurationInMinutes

EndDateTime

IsAllDayEvent

IsClosed

```

**Type**
textarea

**Properties**
Nillable

**Description**
Contains a description of the event or task. Limit is 32 KB.

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
Indicates the end date and time of the event or task. Available in versions 27.0
and later. This field is optional, depending on the following:

**•** If `IsAllDayEvent` is true, you can supply a value for either
`DurationInMinutes` or `EndDateTime` . Supplying values in both
fields is allowed if the values add up to the same amount of time. If both
fields are `null`, the duration defaults to one day.

**•** If `IsAllDayEvent` is false, a value must be supplied for either
`DurationInMinutes` or `EndDateTime` . Supplying values in both
fields is allowed if the values add up to the same amount of time.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If the value of this field is set to `true`, then the activity is an event spanning a
full day, and the `ActivityDate` defines the date of the event. If the value of
this field is set to `false`, then the activity may be an event spanning less than
a full day, or it may be a task. The default value of this field is `false` . Label is
`All-Day Event` .

**Type**
boolean


Standard Objects LookedUpFromActivity

**Field Name** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a task is closed ( `true` ) or not closed ( `false` ). The default
value of this field is `false` . This field is set indirectly by setting `Status` on
the task—each picklist value has a corresponding `IsClosed` value. Label is
`Closed` .

```
IsHighPriority

IsReminderSet

IsTask

IsVisibleInSelfService

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates a high-priority task. The default value of this field is `false` . This field
is derived from the `Priority` field.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a reminder is set for an activity ( `true` ) or not ( `false` ). The
default value of this field is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If the value of this field is set to `true`, then the activity is a task; if the value is
set to `false`, then the activity is an event. The default value of this field is
`false` . Label is `Task` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If the value of this field is set to `true`, then the activity can be viewed in the
self-service portal. The default value of this field is `false` . Label is `Visible`
`in Self-Service` .


Standard Objects LookedUpFromActivity

**Field Name** **Details**

```
Location

OwnerId

Priority

ReminderDateTime

StartDateTime

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If the activity is an event, then this field represents the location of the event. If
the activity is a task, then the value is `null` .

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
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Indicates the priority of a task, such as high, normal, or low. The default value of
this field is `Normal` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Represents the time at which a reminder is scheduled to fire if
`IsReminderSet` is set to `true` . If `IsReminderSet` is set to `false`,
then either the user has deselected the reminder checkbox in the user interface
or the reminder has already fired at the time indicated by the value.

**Type**
dateTime


Standard Objects LookedUpFromActivity

**Field Name** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
Indicates the start date and time of the event. Available in versions 13.0 and later.

The `StartDateTime` field contains the event start date.

However, if the event’s `IsAllDayEvent` flag is set to `true` (indicating an
all-day event), then the time stamp in the `StartDateTime` field is always
set to midnight in the Coordinated Universal Time (UTC) time zone. Don’t attempt
to alter the time stamp to account for any time zone differences.

If the event’s `IsAllDayEvent` flag is set to `false`, then you must translate
the time portion of the time stamp in the `StartDateTime` field to or from
a local time zone for the user or the application, as appropriate, and the translation
must be in the Coordinated Universal Time (UTC) time zone.

If this field has a value, then `ActivityDate` and `ActivityDateTime`
either must be `null` or must match the value of this field.

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
Indicates the current status of a task. The default value of this field is `Not`
`Started` . Each predefined status field sets a value for `IsClosed` .

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


Standard Objects LookedUpFromActivity

**Field Name** **Details**

**Description**
The `WhatId` represents nonhuman objects such as accounts, opportunities,
campaigns, cases, or custom objects. `WhatId` s are polymorphic. Polymorphic
means a `WhatId` is equivalent to the ID of a related object. The label is
`Related To ID` .

This is a polymorphic relationship field.

**Relationship Name**
What

**Relationship Type**
Lookup

**Refers To**
Account, Accreditation, AssessmentIndicatorDefinition, AssessmentTask,
AssessmentTaskContentDocument, AssessmentTaskDefinition,
AssessmentTaskOrder, Asset, AssetRelationship, AssignedResource, Award,
BoardCertification, BusinessLicense, BusinessMilestone, BusinessProfile, Campaign,
CareBarrier, CareBarrierDeterminant, CareBarrierType, CareDeterminant,
CareDeterminantType, CareDiagnosis, CareInterventionType, CareMetricTarget,
CareObservation, CareObservationComponent, CarePgmProvHealthcareProvider,
CarePreauth, CarePreauthItem, CareProgram, CareProgramCampaign,
CareProgramEligibilityRule, CareProgramEnrollee, CareProgramEnrolleeProduct,
CareProgramEnrollmentCard, CareProgramGoal, CareProgramProduct,
CareProgramProvider, CareProgramTeamMember, CareProviderAdverseAction,
CareProviderFacilitySpecialty, CareProviderSearchableField, CareRegisteredDevice,
CareRequest, CareRequestDrug, CareRequestExtension, CareRequestItem,
CareSpecialty, CareSpecialtyTaxonomy, CareTaxonomy, Case,
CommSubscriptionConsent, ContactEncounter, ContactEncounterParticipant,
ContactRequest, Contract, CoverageBenefit, CoverageBenefitItem, CreditMemo,
DelegatedAccount, DocumentChecklistItem, EnrollmentEligibilityCriteria,
HealthcareFacility, HealthcareFacilityNetwork, HealthcarePayerNetwork,
HealthcarePractitionerFacility, HealthcareProvider, HealthcareProviderNpi,
HealthcareProviderSpecialty, HealthcareProviderTaxonomy, IdentityDocument,
Image, IndividualApplication, Invoice, ListEmail, Location, MemberPlan,
Opportunity, Order, OtherComponentTask, PartyConsent, PersonLifeEvent,
PlanBenefit, PlanBenefitItem, ProcessException, Product2, ProductItem,
ProductRequest, ProductRequestLineItem, ProductTransfer, PurchaserPlan,
ReceivedDocument, ResourceAbsence, ReturnOrder, ReturnOrderLineItem,
ServiceAppointment, ServiceResource, Shift, Shipment, ShipmentItem, Solution,
Visit, VisitedParty, VolunteerProject, WorkOrder, WorkOrderLineItem

```
WhoId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects Macro

**Field Name** **Details**

**Description**
The WhoId represents a human such as a lead or a contact. WhoIds are
polymorphic. Polymorphic means a WhoId is equivalent to a contact’s ID or a
lead’s ID. The label is `Name ID` .

This is a polymorphic relationship field.

**Relationship Name**
Who

**Relationship Type**
Lookup

**Refers To**
Contact, Lead

Usage

**Query activities related to an object**

**1.** Optionally, issue a describe call against the object whose activities you wish to query, to get a suggestion of the correct SOQL
to use.

**2.** Issue a SOQL relationship query with a main clause that references the object, and an inner clause that references the activity
custom lookup relationship; for example:

```
       SELECT id, name,

       (SELECT id, subject from sponsoredact__r)

       FROM Contact

```

In this example _`sponsoredact__r`_ is a user defined relationship list.

The user interface enforces sharing rules, filtering out related-list items that a user doesn’t have permission to see.

The following restrictions on users who don’t have “View All Data” permission help prevent performance issues:

**•** In the main clause of the relationship query, you can reference only one record. For example, you can’t filter on all records where
the account name starts with ‘A’; instead, you must reference a single account record.

**•** In the inner clause of the query, you can’t use `WHERE` .

**•** In the inner clause of the query, you must specify a limit of 500 or fewer on the number of rows that are returned in the list.

**•** You must sort on `ActivityDate` in descending order and `LastModifiedDate` in descending order; you can display
nulls last. For example: `ORDER BY ActivityDate DESC NULLS LAST, LastModifiedDate DESC` .

### Macro

Represents a macro, which is a set of instructions that tells the system to perform one or more tasks. This object is available in API version
32.0 and later.


Standard Objects Macro

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
Description

FolderId

FolderName

IsAlohaSupported

IsLightningSupported

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of what this macro does.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Returns the ID of the folder that contains the macro. Available in API version 44.0 and later.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Name of the folder that contains the macro. Available in API version 44.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Specifies whether the macro is supported in Salesforce Classic.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Specifies whether the macro is supported in Lightning Experience.


Standard Objects Macro

**Field** **Details**

```
LastReferencedDate

LastViewedDate

Name

OwnerId

StartingContext

```

Usage

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the macro record was last referenced.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the macro record was last viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the macro.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of the session record.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The object the macro performs actions on. In Salesforce Classic, macros are supported on
objects with both feed-based layouts and quick actions. In Lightning Experience, macros are
supported on standard and custom objects that allow quick actions and have a customizable
page layout.

A macro definition consists of a Macro object and several associated MacroInstruction objects.


Standard Objects Macro

First, create a Macro object. Then, create MacroInstructions that specify objects, operations, conditions, and targets for the macro.

A macro contains an ordered list of macro instructions whose index field, `sortOrder`, is 0-based. If there’s an incorrect sequence of
macro instructions, the macro doesn’t execute.

If you update a macro definition or add or remove instructions from a macro, make sure that the `sortOrder` field that defines the
execution order is correct. To delete an entire macro definition, invoke the delete operation on the Macro object.

The table describes the supported macro instruction targets and how they relate to each other.

Note: Strings indicated by `<brackets>` are variables. The variable description describes the required type. For example,
`Tab.<EntityApiName>` requires the entity name. If your custom entity name is `MyCustomObject`, your target API is
`Tab.MyCustomObject__c` .

If a macro instruction listed in the table supports an implicit operation, you can use that operation as a direct child instruction without
explicitly specifying a target. The hyphens used in the table illustrate the hierarchical relationship between targets. A target isn't available
if its parent isn’t.

**Table 1: Macro Instruction Target Grammar and Hierarchy**


### Standard Objects MacroInstruction

Example: This example describes a macro that opens a quick action, sets some fields in the quick action, and submits the quick
action.

```
      0. SELECT Tab.Case

      1. SELECT QuickAction.Case.Email

      2. SET Field.EmailMessage.Subject

      3. SET Field.EmailMessage.ToAddress

      4. INSERT Field.EmailMessage.HtmlBody.cursor

      5. SUBMIT

```

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**MacroChangeEvent (API version 48.0)**
Change events are available for the object.

**MacroHistory**

History is available for tracked fields of the object.

**MacroOwnerSharingRule**

Sharing rules are available for the object.

**MacroShare**

Sharing is available for the object.

### MacroInstruction

Represents an instruction in a macro. An instruction can specify the object that the macro interacts with, the context or publisher that
the macro works within, the operation or action that the macro performs, and the target of the macro’s actions.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
MacroId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the macro that contains this instruction.


Standard Objects MacroInstruction

**Field Name** **Details**

```
Name

Operation

SortOrder

Target

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
Name of the instruction.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The action that the macro instruction performs. Valid values are:

**•** Select

**•** Set

**•** Insert

**•** Submit

**•** Close

To create macro instructions that execute conditionally, these values are available
in API version 46.0 and later.

**•** IF

**•** ELSEIF

**•** ELSE

**•** ENDIF

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Order of this instruction in the macro.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The object that’s the target of the operation. For example, the target for the active
case tab (Tab.Case) or a quick action, like the Send Email action on the case object
(QuickAction.Case.SendEmail).


Standard Objects MacroInstruction

**Field Name** **Details**

In Lightning Experience, macros are supported on standard and custom objects
that allow quick actions and have a customizable page layout.

In Salesforce Classic, macros are supported on objects with feed-based layouts
and quick actions.

You can specify relative dates and times for the following targets.

**•** DateTime

**•** Date

**•** Time

**•** DueDate

**•** Birthday

```
Value

ValueRecord

```

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Value of a field. If the operation is Select, then the value is null, because the
operation selects the object on which the macro performs an action. An
instruction can contain both a `Value` field and a `ValueRecord` field, but
only one of these fields can have a value. The other field value must be null.

To create relative dates and times, specify a valid Salesforce formula, prefaced
by `MacroFormula` . For example, the following formula creates a date that is
1 day from now:

```
  MacroFormula:NOW() + 1

```

You can’t edit custom relative formulas in the Macro Builder.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the value or record. The `ValueRecord` can be either a value or a record,
but not both. An instruction can contain both a `Value` field and a
`ValueRecord` field, but only one of these fields can have a value. The other
field value must be null.


Standard Objects MacroInstruction

Usage

MacroInstructions can specify objects, operations, conditions, and targets. For example, a macro containing these instructions performs
a quick action that sends an email.

```
       Select Email QuickAction

       Set Subject…

       Set To…

       Set Body…

       Submit

```

You can create conditional macros using `IF`, `ELSEIF`, `ELSE`, and `ENDIF` as operations. In a conditional statement, the ExpressionFilter
and ExpressionFilterCriteria objects are used to control which instructions execute. The ExpressionFilter object lets you define a logical
expression with one or more conditions. It uses a child object, ExpressionFilterCriteria, to represent each condition that is evaluated.

For example, consider the following conditional statement and macro instructions.

```
   IF (Case.Status EQUALS New) AND (Case.Origin EQUALS Phone)

       Select Email QuickAction

       Set Subject…

       Set To…

       Set Body…

       Submit

   ELSE

       Select Update Case Detail

       Update Case Description…

       Submit

   ENDIF

```

The ExpressionFilter object includes a `FilterConditionLogic` field containing `1 AND 2`, where 1 and 2 are ExpressionFilterCriteria
objects. The SortOrder field in the ExpressionFilterCriteria object maps condition 1 to `Case.Status EQUALS New`, and condition
2 to `Case.Origin EQUALS Phone` . If the conditional statement evaluates to true, then the instructions in the `IF` block are
executed; otherwise, the instructions in the `ELSE` block are executed.

Any number of macro instructions can be present inside an `IF`, `ELSEIF`, or `ELSE` block. In addition, conditions can be nested.

Data Model


### Standard Objects MacroUsage

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**MacroInstructionChangeEvent (API version 48.0)**
Change events are available for the object.

### MacroUsage

Represents macro usage on a record, including which macro was used, who used it, and how they used it. This object is available in API
version 47.0 and later.

Supported Calls

describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

delete() is supported in API version 55.0 and later.

Special Access Rules

This object is always read-only. Only users with “Modify All Data” permission can delete MacroUsage records.


Standard Objects MacroUsage

Fields

**Field** **Details**

```
AppContext

ConditionCount

ContextRecord

DurationInMs

ExecutedInstructionCount

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Context in which the macro was run. Possible values are:

**•** `Aloha` —Salesforce Classic

**•** `Lightning` —Lightning Experience

**•** `Unknown`

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of conditional instructions contained in the macro at execution.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the record on which the macro was run.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The execution time, in milliseconds, for the macro.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of macro instructions that ran successfully. If the macro completed successfully,
this value is the same as `InstructionCount` .


Standard Objects MacroUsage

**Field** **Details**

```
ExecutionEndTime

ExecutionState

FailureReason

FolderId

InstructionCount

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time at which macro execution completed.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The end state of macro execution. Possible values are

**•** `SUCCESS`

**•** `FAILURE`

**•** `CANCELED`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
If `ExecutionState` is failure, this field stores the reason for the failure. Possible values
are:

**•** `ACCESS`

**•** `GENERIC`

**•** `TIMEOUT`

**•** `UNSUPPORTED`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the folder containing the macro at the time it was used.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects MacroUsage

**Field** **Details**

**Description**
The number of instructions in the macro at the start of execution.

```
IsFromBulk

MacroID

Name

OwnerId

UserId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If true, the macro was run as a bulk macro. When a bulk macro is run on multiple records,
usage is recorded per record.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the macro.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Name of the macro.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the group or user that owns the macro.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the user that ran the macro.


### Standard Objects MailmergeTemplate

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**MacroUsageOwnerSharingRule**

Sharing rules are available for the object.

**MacroUsageShare**

Sharing is available for the object.

### MailmergeTemplate

Represents a mail merge template (a Microsoft Word document) used for performing mail merges for your organization.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

**•** All users can view this object, but you need the “Customize Application” permission to modify it.

**•** Customer Portal users can’t access this object.

Fields

**Field** **Details**

```
Body

BodyLength

```

**Type**
base64

**Properties**
Create

**Description**
Required. Microsoft Word document to use as a mail merge template. Due
to limitations with Microsoft Word mail merge templates, your client
application can specify the Body field when creating these records, but not
when updating them. Limit: 5 MB.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Length of the Microsoft Word document.


Standard Objects MailmergeTemplate

**Field** **Details**

```
Category

Description

Filename

IsDeleted

LastUsedDate

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of document template. Possible values are:

**•** `Document`

**•** `Envelope`

**•** `Label`

The default value is `Document` .

**Type**
string

**Properties**
Create, Filter,Group, Nillable, Sort, Update

**Description**
Required. Text description of this mail merge template. Limit: 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
Required. File name of the Microsoft Word document that was uploaded as
a mail merge template. Limit: 255 characters in length.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or
not ( `false` ). Label is **Deleted** .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when this MailmergeTemplate was last used.


Standard Objects MailmergeTemplate

**Field** **Details**

```
Name

SecurityOptionsAttachmentHasFlash

SecurityOptionsAttachmentHasXSSThreat

SecurityOptionsAttachmentScannedforFlash

SecurityOptionsAttachmentScannedForXSS

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Name of this mail merge template.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Required. True if Flash Injection was detected in the attachment.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Required. True if a cross site scripting threat was detected in the attachment.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Required. True if the attachment has been scanned for Flash Injection.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Required. True if the attachment has been scanned for a cross site scripting
threat.


### Standard Objects MaintenanceAsset

Usage

Use this object to manage mail merge templates for your organization.

SEE ALSO:

Overview of Salesforce Objects and Fields

### MaintenanceAsset

Represents an asset covered by a maintenance plan in field service. Assets can be associated with multiple maintenance plans.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field Name** **Details**

```
AssetId

ContractLineItemId

LastReferencedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The asset associated with the maintenance asset.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Contract line item associated with the maintenance asset. This field can only list
a contract line item that is associated with the asset, and whose parent service
contract is associated with the parent maintenance plan.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects MaintenanceAsset

**Field Name** **Details**

**Description**
The date when the maintenance asset was last modified. Its label in the user
interface is Last Modified Date.

```
LastViewedDate

MaintenanceAssetNumber

MaintenancePlanId

NextSuggestedMaintenanceDate

WorkTypeId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the product request was last viewed.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
An auto-assigned number that identifies the maintenance asset.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Maintenance plan associated with the maintenance asset.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The suggested date of service for the maintenance asset’s first work order (not
the date the work order is created). This corresponds to the work order’s
`SuggestedMaintenanceDate` . If left blank when the maintenance asset
is created, this field inherits its initial value from the related maintenance plan.

This field auto-updates after each batch is generated. Its label in the user interface
is Date of the first work order in the next batch.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects MaintenancePlan

**Field Name** **Details**

**Description**
Work type associated with the maintenance asset. Work orders generated from
the maintenance plan inherit its work type’s duration, required skills and products,
and linked articles. Maintenance assets covered by the plan use the same work
type, though you can update them to use a different one.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**MaintenanceAssetChangeEvent (API version 48.0)**
Change events are available for the object.

**MaintenanceAssetFeed**

Feed tracking is available for the object.

**MaintenanceAssetHistory**

History is available for tracked fields of the object.

### MaintenancePlan

Represents a preventive maintenance schedule for one or more assets in field service.

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
Create, Filter, Group, Nillable, Sort, Update

**Description**
The associated account, which typically represents the customer receiving the
maintenance service.


Standard Objects MaintenancePlan

**Field Name** **Details**

```
ContactId

Description

DoesAutoGenerateWorkOrders

DoesGenerateUponCompletion

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The associated contact.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A brief description of the plan.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Turns on auto-generation of work order batches for a maintenance plan and
prohibits the manual generation of work orders via the Generate Work Orders
action. If this option is selected, a new batch of work orders is generated for the
maintenance plan on the `NextSuggestedMaintenanceDate` listed on
each maintenance asset, or on the maintenance plan if no assets are included.
If a `GenerationHorizon` is specified, the date of generation is that many
days earlier.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If both this option and `DoesAutoGenerateWorkOrders` are set to true,
a new batch of work orders isn’t generated until the last work order generated
from the maintenance plan is completed. A work order is considered completed
when its status falls into one of the following status categories: Cannot Complete,
Canceled, Completed, or Closed.

If a maintenance plan covers multiple assets, work orders are generated per asset.
If a maintenance asset’s final work order is completed late, its work order
generation is delayed, which may cause a staggered generation schedule between
maintenance assets.


Standard Objects MaintenancePlan

**Field Name** **Details**

```
EndDate

Frequency

FrequencyType

GenerationHorizon

GenerationTimeframe

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The last day the maintenance plan is valid.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
(Optional) Amount of time between work orders. The unit is specified in the
`FrequencyType` field.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
(Optional) The unit of frequency:

**•** Days

**•** Weeks

**•** Months

**•** Years

For example, to perform monthly maintenance visits you need a work order for
each visit, so enter 1 as the `Frequency` and select Months.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Moves up the timing of batch generation if
`DoesAutoGenerateWorkOrders` is set to true. A generation horizon of
5 means the new batch of work orders is generated 5 days before the
maintenance asset’s (or maintenance plan’s, if there are no assets)
`NextSuggestedMaintenanceDate` . The generation horizon must be a
whole number.

**Type**
int


Standard Objects MaintenancePlan

**Field Name** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**

(Required) How far in advance work orders are generated in each batch. The unit
is specified in the `GenerationTimeframeType` field.

```
GenerationTimeframeType

LastReferencedDate

LastViewedDate

LocationId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
(Required) The generation timeframe unit:

**•** Days

**•** Weeks

**•** Months

**•** Years

For example, if you need work orders for six months, enter 6 and select Months.

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
Where the service takes place.


Standard Objects MaintenancePlan

**Field Name** **Details**

```
MaintenancePlanNumber

MaintenancePlanTitle

MaintenanceWindowEndDays

MaintenanceWindowStartDays

NextSuggestedMaintenanceDate

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
(Read Only) An auto-assigned number that identifies the maintenance plan.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A name for the maintenance plan.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Days after the suggested service date on the work order that its service
appointment can be scheduled.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Days before the suggested service date on the work order that its service
appointment can be scheduled.

The maintenance window start and end fields affect the Earliest Start Permitted
and Due Date fields on the maintenance plan’s work orders’ service appointments.
For example, if you enter 3 for both the maintenance window start and end, the
Earliest Start Permitted and the Due Date will be 3 days before and 3 days after,
respectively, the Suggested Maintenance Date on each work order. If the
maintenance window fields are left blank, the service appointment date fields
list their work order’s suggested maintenance date.

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects MaintenancePlan

**Field Name** **Details**

**Description**
The suggested date of service for the first work order (not the date the work order
is created). This corresponds to the work order’s
`SuggestedMaintenanceDate` . You can use this field to enforce a delay
before the first maintenance visit (for example, if monthly maintenance should
begin one year after the purchase date). Its label in the user interface is Date of
the first work order in the next batch.

For example, if you want the first maintenance visit to take place on May 1, enter
May 1. When you generate work orders, the earliest work order will list a suggested
maintenance date of May 1, and the dates on the later work orders will be based
on the `GenerationTimeframe` and `Frequency` .

Important: Maintenance assets also list a
`NextSuggestedMaintenanceDate`, which is initially inherited
from the maintenance plan. If the plan has maintenance assets, this date
auto-updates on the maintenance assets after each batch is generated,
but doesn’t update on the maintenance plan itself because batch timing
is calculated at the maintenance asset level. If the plan doesn’t have
maintenance assets, this date auto-updates on the maintenance plan after
each batch is generated.

```
OwnerId

ServiceContractId

StartDate

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the maintenance plan.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The service contract associated with the maintenance plan. The service contract
can’t be updated if any child maintenance asset is associated with a contract line
item from the service contract.

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The first day the maintenance plan is valid.


Standard Objects MaintenancePlan

**Field Name** **Details**

```
SvcApptGenerationMethod

WorkOrderGenerationMethod

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The service appointment generation method.

**•** One service appointment per work order

**•** One service appointment per work order line item

If your existing maintenance plans have work orders or work order line items
associated with them, you can’t change their generation methods. To change
pre-existing maintenance plan generation methods, either delete the work orders
and regenerate them or delete the maintenance plan and recreate it with the
needed generation methods.

If Work Order Generation Method is set to One work order per asset, you can’t
set a Service Appointment Generation Method.

If Work Order Generation Method is set to One work order line item per asset,
you must select a Service Appointment Generation Method.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The work order generation method.

**•** One work order per asset

**•** One work order line item per asset

If your existing maintenance plans have work orders or work order line items
associated with them, you can’t change their generation methods. To change
pre-existing maintenance plan generation methods, either delete the work orders
and regenerate them or delete the maintenance plan and recreate it with the
needed generation methods.

If Work Order Generation Method is left as None, the generation is defaulted to
one work order per asset.

When One work order line item per asset is set, and all maintenance assets have
the same Next Suggested Maintenance Date on the maintenance plan, they are
grouped in one work order. However, if maintenance assets have different Next
Suggested Maintenance Dates, multiple work orders are created for each date.

If Work Order Generation Method is set to One work order per asset, you can’t
set a Service Appointment Generation Method.


### Standard Objects MaintenanceWorkRule

**Field Name** **Details**

```
WorkOrderGenerationStatus

WorkTypeId

```

Associated Objects

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
(Read Only) Indicates the status of work order generation:

**•** NotStarted—the default value, work order generation has not started

**•** InProgress—work order generation is underway

**•** Completed—work order generation is complete

**•** Unsuccessful—it was not possible to generate work orders

You can generate only one batch at a time.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The associated work type. Work orders generated from the maintenance plan
inherit its work type’s duration, required skills and products, and linked articles.
Maintenance assets covered by the plan use the same work type, though you
can update them to use a different one.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**MaintenancePlanChangeEvent (API version 48.0)**
Change events are available for the object.

**MaintenancePlanFeed**

Feed tracking is available for the object.

**MaintenancePlanHistory**

History is available for tracked fields of the object.

**MaintenancePlanOwnerSharingRule**

Sharing rules are available for the object.

**MaintenancePlanShare**

Sharing is available for the object.

### MaintenanceWorkRule

Represents the recurrence pattern for a maintenance record. This object is available in API version 49.0 and later.


Standard Objects MaintenanceWorkRule

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
DoesFloatingWorkOrder

LastReferencedDate

LastViewedDate

Name

NextSuggestedMaintenanceDate

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates that the maintenance plan uses the floating work order adjustment. The default is
false.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the line item was last modified. Its label in the user interface is `Last`
`Modified Date` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the line item was last viewed.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of this maintenance work rule.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects MaintenanceWorkRule

**Field** **Details**

**Description**
The next date on which this rule will generate maintenance items.

```
OwnerId

ParentMaintenancePlanId

ParentMaintenanceRecordId

RecordsetFilterCriteriaId

RecurrencePattern

SortOrder

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The assigned owner of the maintenance work rule.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maintenance plan associated with the maintenance work rule.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maintenance record this work rule applies to.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the recordset filter criteria associated with this maintenance work rule. Available in API
version 52.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The RRULE that defines the pattern of recurrence for this work order rule.

**Type**
int


Standard Objects MaintenanceWorkRule

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The sort order that applies to this work order rule.

```
Title

Type

WorkTypeId

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The title of this work order rule.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of maintenance work rule. Available values are:

**•** `Criteria-based`

**•** `Calendar-based` (default)

Available in API version 52.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the work type that this work order rule generates.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**MaintenanceWorkRuleChangeEvent**

Change events are available for the object.

**MaintenanceWorkRuleFeed**

Feed tracking is available for the object.

**MaintenanceWorkRuleHistory**

History is available for tracked fields of the object.

**MaintenanceWorkRuleOwnerSharingRule**

Sharing rules are available for the object.


### Standard Objects ManagedContent

**MaintenanceWorkRuleShare**

Sharing is available for the object.

### ManagedContent

Represents managed content in a Salesforce CMS workspace for use in an Experience Cloud site or a channel. The ManagedContent
object represents the complete instance of a managed content record. It provides a consistent identifier for the managed content so
that variants of the content item can be created over time. This object is available in API version 56.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

### ManagedContent is available when the Digital Experiences app is enabled.

Fields

**Field** **Details**

```
ApiName

AuthoredManagedContentSpaceId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The unique API name of the Salesforce CMS content. Name requirements:

**•** must be 80 characters or fewer

**•** must begin with a letter

**•** can contain only underscores and alphanumeric characters

**•** can't include spaces

**•** can't end with an underscore

**•** can't contain two consecutive underscores

This field is available in API version 62.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Salesforce CMS workspace ID where the content resides.

This field is a relationship field.


Standard Objects ManagedContent

**Field** **Details**

**Relationship Name**
AuthoredManagedContentSpace

**Relationship Type**
Lookup

**Refers To**
ManagedContentSpace

```
ContentKey

ContentTypeFullyQualifiedName

Name

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Unique identifier of the content.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The fully qualified name of the content type of this CMS content. In an enhanced CMS
workspace, the `ContentTypeFullyQualifiedName` for each standard content
type is:

**•** News: `sfdc_cms__news`

**•** Image: `sfdc_cms__image`

**•** Document: `sfdc_cms__document`

In a CMS workspace, the `ContentTypeFullyQualifiedName` for each standard
content type is:

**•** News: `news`

**•** Image: `cms_image`

**•** Document: `cms_document`

In both CMS workspaces and enhanced CMS workspaces, the
`ContentTypeFullyQualifiedName` for a custom content type is the same as the
developer name of the custom content type.

This field is available in API version 62.0 and later.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort


### Standard Objects ManagedContentChannel

**Field** **Details**

**Description**
The name of the Salesforce CMS content. When you view this content in a CMS workspace,
`Name` is the title of the latest content version. In an enhanced CMS workspace, `Name` is
the title of the content in the workspace’s default language.

This field is available in API version 58.0 and later.

```
PrimaryLanguage

```

Usage

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The default language of the Salesforce CMS workspace where the content resides.

When you create or add content in a Salesforce CMS workspace, the content is uniquely identified by the Salesforce CMS workspace, a
### content key, and a default language. ManagedContent can be queried through the public sObject API. Use this object to create

and retrieve information for a specific managed content.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ManagedContentChangeEvent on page 68 (API version 62.0)**
Change events are available for the object.

### ManagedContentChannel

Represents the details of a CMS channel. CMS channels correspond to managed content publishing endpoints. They deliver published
content from your Salesforce CMS workspaces to an audience. This object is available in API version 55.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

### ManagedContentChannel is available when the Digital Experiences app is enabled.


Standard Objects ManagedContentChannel

Fields

**Field** **Details**

```
CacheControlMaxAge

Domain

DomainHostName

MediaCacheControlMaxAge

Name

```

**Type**
long

**Properties**
Filter, Group, Nillable, Sort

**Description**
The amount of time, in seconds, it takes for a requested CMS content resource in the CMS
channel to expire before a new request for the resource must be made.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The domain for a public channel. Only public channels can have an assigned domain.

Possible value is:

**•** mydomain.cdn.salesforce-experience.com

Note: The `mydomain` value is specific to the domain of the channel.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The hostname of the domain assigned to the CMS channel. Only public channels can have
an assigned domain.

**Type**
long

**Properties**
Filter, Group, Nillable, Sort

**Description**
The amount of time, in seconds, it takes for a requested CMS image or document content
resource in the CMS channel to expire before a new request for the resource must be made.
This field is available in API version 57.0 and later.

**Type**
string


Standard Objects ManagedContentChannel

**Field** **Details**

**Properties**
Filter, Group, idLookup, Sort

**Description**
Name of the CMS channel.

```
OptionsIsCacheControlPublic

OptionsIsDomainLocked

OptionsIsSearchable

Type

```

**Type**
boolean

**Properties**
Filter

**Description**
When `true`, the CMS channel connection type is public. When `false`, the cache control
is private. The default value is `false` .

**Type**
boolean

**Properties**
Filter

**Description**
When `true`, the domain set to the channel can’t be changed. Only public channels can
have this field set to `true` . If the channel type is `COMMUNITY`, the default value is `true` .
For all other channel types, the default value is `false` .

**Type**
boolean

**Properties**
Filter

**Description**
When `true`, users can search for all published CMS content types within the channel. The
default value is `false` .

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The connection type of the CMS channel. The connection type determines which audience
can access the CMS content delivered in the channel.

Possible values are:

**•** `COMMUNITY` : User access is controlled by the settings of the Experience Cloud site.

**•** `CloudToCloud` : Connects Salesforce CMS to the B2C Commerce Page Designer.

**•** `ConnectedApp` : User access to the channel is controlled by the connected application
associated with the channel.


### Standard Objects ManagedContentInfo

**Field** **Details**

**•** `PublicUnauthenticated` : No user authentication required, content can be cached
on public CDNs.

**•** `Record` : User access to the content is controlled by the user access to the associated
record. Content is only accessible to users with access to the record.

**•** `UserPermission` : This value is reserved for future use.

Usage

`ManagedContentChannel` can be queried through the public sObject API. Use this object to retrieve information for a specific
CMS channel.

### ManagedContentInfo

Allows the creation of relationship to Product using ProductMedia. This object is available in API version 49.0 to 57.0. In API version 58.0
and later, use the ManagedContent object.

Supported Calls

```
   describeSObjects()

```

Special Access Rules

You must have the B2B Commerce license and a CMS workspace to access a web store.

Usage

The CMS content import process returns a ManageContentInfo ID for each piece of content. The ManagedContentInfo entity has a 1:1
relationship with ProductMedia. To create this relationship, ProductMedia must be associated with a Product entity, for example, Product

    - ProductMedia > ManagedContentInfo. Use the ID to associate content uploaded through the API with the ProductMedia entity

### ManagedContentSpace

Represents the complete instance of a Salesforce CMS workspace that stores managed content. Users and groups with designated
permissions can access and manage the content in a CMS workspace. This object is available in API version 56.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

### ManagedContentSpace is available when the Digital Experiences app is enabled.


Standard Objects ManagedContentSpace

Fields

**Field** **Details**

ApiName

```
DefaultLanguage

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique API name of an enhanced Salesforce CMS workspace. Name requirements:

**•** must be 40 characters or fewer

**•** must begin with a letter

**•** can contain only underscores and alphanumeric characters

**•** can't include spaces

**•** can’t end with an underscore

**•** can’t contain two consecutive underscores

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Default language for the Salesforce CMS workspace.

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


### Standard Objects ManagedContentVariant

**Field** **Details**

**•** `zh_TW` —Chinese (Traditional)

```
Description

LastReferencedDate

LastViewedDate

Name

```

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
Description of the Salesforce CMS workspace.

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
Filter, Group, idLookup, Sort

**Description**
Name of the Salesforce CMS workspace.

### ManagedContentVariant

Represents a variant of a managed content item. This object is available in API version 56.0 and later.

### Managed content variants are associated with a ManagedContent object. The managed content and variants are counted as one

content record in your Salesforce org.

For example, say you have a managed content item of content type News and a default language of English. When you translate the
News content into other languages such as Spanish, Japanese, and French, a managed content variant for each language is created.


Standard Objects ManagedContentVariant

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`

Special Access Rules

`ManagedContentVariant` is available when the Digital Experiences app is enabled.

Fields

**Field** **Details**

```
ContentTypeFullyQualifiedName

IsPublished

Language

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The fully qualified name of the content type of this CMS content. In an enhanced CMS
workspace, the `ContentTypeFullyQualifiedName` for each standard content
type is:

**•** News: `sfdc_cms__news`

**•** Image: `sfdc_cms__image`

**•** Document: `sfdc_cms__document`

The `ContentTypeFullyQualifiedName` for a custom content type is the same as
the developer name of the custom content type.

This field is available in API version 62.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the managed content variant is published to a channel.

The default value is `false` .

This field is calculated.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Language of the variant.


Standard Objects ManagedContentVariant

**Field** **Details**

```
ManagedContentId

ManagedContentKey

ManagedContentVariantStatus

Name

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Globally unique identifier for the managed content item.

This field is a relationship field.

**Relationship Name**
ManagedContent

**Relationship Type**
Lookup

**Refers To**
ManagedContent

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Globally unique identifier for managed content that associates with the managed content
variant.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Publication status of the managed content.

Possible values are:

**•** `Draft`

**•** `Published`

**•** `Revised`

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Name of the managed content variant.


### Standard Objects MarketingForm

**Field** **Details**

```
UrlName

VariantType

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
URL name of the managed content variant.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Type of variant.

Possible value is:

**•** `Content`

Managed content variants are associated with a `ManagedContent` object. The managed content and managed content variants
are counted as one content record in your Salesforce org.

`ManagedContentVariant` can be queried through the public sObject API. Use this object to retrieve information for a specific
content in a certain language and format of a managed content.

### MarketingForm

Represents an Account Engagement marketing form that has been synched to Salesforce. Use forms on your website and landing pages
to collect information about visitors and turn anonymous visitors into identified prospects. This object is available in API version 42.0
and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`

Special Access Rules

To access this object, your org must use Account Engagement and users need the CRM User or Sales User permission set.


Standard Objects MarketingForm

Fields

**Field Name** **Details**

```
CampaignId

ErrorRate

LastReferencedDate

LastViewedDate

Name

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The ID of the related campaign.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**

The percentage of views that led to an error.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The timestamp that indicates when the current user last viewed a record that is
related to this form.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The date and time when the current user last viewed this record. If this value is
null, this record might only have been referenced (see
`LastReferencedDate` ) and not viewed.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**

The name of the marketing form.


Standard Objects MarketingForm

**Field Name** **Details**

```
SubmissionRate

TotalErrors

TotalSubmissions

TotalTrackedLinkClicks

TotalViews

Type

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**

The percentage of the views that led to a form submission.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The total number of times a form error prevented a submission.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The total number of times the form was successfully submitted.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The total number of link clicks from your thank you page.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The total number of times your form has been viewed. Includes multiple views
from the same visitor.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort


Standard Objects MarketingForm

**Field Name** **Details**

**Description**

Specifies the type of marketing form record, either a form or form handler.

```
UniqueErrors

UniqueSubmissions

UniqueTrackedLinkClicks

UniqueViews

```

Associated Objects

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The number of errors generated by separate visitors.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The total number of unique submissions. Removes multiple submissions from
the same prospect.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The total number of unique link clicks from your thank you page. Removes
multiple clicks from the same prospect.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The number of form views by separate visitors.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**MarketingFormEvent (API version 44.0)**
Change events are available for the object.


### Standard Objects MarketingLink

**MarketingFormFeed**

Feed tracking is available for the object.

### MarketingLink

Represents an Account Engagement marketing link record, either a custom redirect or a file, that has been synced to Salesforce. This
object is available in API version 42.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`

Special Access Rules

To access this object, your org must use Account Engagement and users need the CRM User or Sales User permission set.

Fields

**Field Name** **Details**

```
CampaignId

LastReferencedDate

LastViewedDate

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

**Description**

The timestamp that indicates when the current user last viewed a record that is
related to this marketing link.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The date and time when the current user last viewed this record. If this value is
null, this record might only have been referenced (see
`LastReferencedDate` ) and not viewed.


Standard Objects MarketingLink

**Field Name** **Details**

```
Name

TargetUrl

TotalTrackedLinkClicks

Type

UniqueTrackedLinkClicks

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**

The name of the marketing link.

**Type**
url

**Properties**
Filter, Group, Sort

**Description**

The target URL of the marketing link.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The total number of clicks for the redirect. Includes clicks from visitors and
identified prospects. When a person clicks the link multiple times, each click is
counted in this number.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**

Specifies the type of marketing link record, either a custom redirect or file.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The number of unique clicks for the redirect. Includes clicks from visitors and
identified prospects. Only the first click is counted in this number.


### Standard Objects MatchingRule

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**MarketingFormEvent (API version 44.0)**
Change events are available for the object.

**MarketingLinkFeed**

Feed tracking is available for the object.

### MatchingRule

Represents a matching rule that is used to identify duplicate records. This object is available in API version 33.0 and later.

A matching rule compares field values to determine whether a record is similar enough to existing records to be considered a duplicate.
For example, a matching rule can specify that if the `Email` and `Phone` values of two records match exactly, the records are possible
duplicates. Your organization uses matching rules with duplicate rules to define what happens when duplicates are identified.

If the rule is for a Person Account, `SobjectSubType` is automatically set to `PersonAccount` .

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

As of Summer ’20 and later, only users with the View Setup and Configuration permission can access this object.

Fields

**Field Name** **Details**

```
BooleanFilter

Description

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Specifies filter logic conditions.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
The description of the matching rule.


Standard Objects MatchingRule

**Field Name** **Details**

```
DeveloperName

Language

MasterLabel

MatchEngine

NamespacePrefix

RuleStatus

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The developer name for the matching rule.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language selected for your organization.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The name of the matching rule.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The match engine used by the matching rule.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix for matching rules for your organization.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort


Standard Objects MatchingRule

**Field Name** **Details**

**Description**
Required. The activation status of the matching rule. Values are:

**•** _`Inactive`_

**•** _`Deactivating`_

**•** _`DeactivationFailed`_

**•** _`Active`_

**•** _`Activating`_

**•** _`ActivationFailed`_

Important: The only valid values you can declare when deploying a
package are _`Active`_ and _`Inactive`_ .

```
SobjectSubtype

SobjectType

```

Usage

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Read-only. Indicates if the matching rule is defined for the `Person` subtype of
`Account` . Valid values are:

**•** `PersonAccount`

**•** `None`

If the rule is for a Person Account, `SobjectSubType` is automatically set to
`PersonAccount` .

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The object for the matching rule.

Use the Salesforce API to retrieve and view details about MatchingRule and MatchingRuleItem. Use the Salesforce Metadata API to create,
update, or delete these objects.

SEE ALSO:

MatchingRuleItem

DuplicateRule

[MatchingRule in the Salesforce Metadata API Developer's Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_matchingrule.htm)


### Standard Objects MatchingRuleItem MatchingRuleItem

Represents criteria used by a matching rule to identify duplicate records. This object is available in API version 33.0 and later.

A matching rule item determines which field the matching rule uses to identify a duplicate record. It also determines the method used
to compare value that two records have for the field. For example, a matching rule item might specify that the `Email` field values of
two records must match exactly in order for the records to be considered duplicates.

When a matching rule has multiple matching rule items, it means that multiple fields must match in order for the records to be identified
as dupcliates.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

As of Summer ’20 and later, only users with the View Setup and Configuration permission can access this object.

Fields

**Field Name** **Details**

```
BlankValueBehavior

Field

MatchingMethod

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Specifies how blank fields affect whether the fields being compared are considered
matches. Valid values are:

**•** _`MatchBlanks`_

**•** _`NullNotAllowed`_ (default)

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates which field to compare when determining if a record is similar enough
to an existing record to be considered a match.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


Standard Objects MatchingRuleItem

**Field Name** **Details**

**Description**
Defines how the fields are compared. Choose between the exact matching
method and various fuzzy matching methods. Valid values are:

**•** _`Exact`_

**•** _`FirstName`_

**•** _`LastName`_

**•** _`CompanyName`_

**•** _`Phone`_

**•** _`City`_

**•** _`Street`_

**•** _`Zip`_

**•** _`Title`_

For details on each matching method, see “Matching Methods Used with
Matching Rules” in the Salesforce Help.

```
MatchingRuleId

SortOrder

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID for the matching rule.

This is a relationship field.

**Relationship Name**
MatchingRule

**Relationship Type**
Lookup

**Refers To**
MatchingRule

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The order of the matching rule items for a matching rule.


### Standard Objects MerchAccPaymentMethodSet

Usage

Use the Salesforce SOAP API to retrieve and view details about MatchingRule and MatchingRuleItem. Use the Salesforce Metadata API
to create, update, or delete these objects.

SEE ALSO:

MatchingRule

DuplicateRule

[MatchingRule in the Salesforce Metadata API Developer's Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_matchingrule.htm)

### MerchAccPaymentMethodSet

Defines an ordered list of payment methods that are available to a merchant's cudstomer during checkout. You can configure multiple
payment method sets, each designated for a specific locale, payment region, or sale channel. This object is available in API version 58.0
and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

To access Salesforce Payments objects, you must have a Salesforce Payments license with the Payments permission enabled for your
org. Salesforce Payments entities are available only in Lightning Experience.

Fields

**Field** **Details**

```
CurrencyIsoCode

DeveloperName

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for organizations with the multicurrency feature enabled. The ISO code for
any currency allowed by the organization.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
Unique name for the object given by the Payments admin.


### Standard Objects MerchAccPaymentMethodType

**Field** **Details**

```
MerchantAccountId

PaymentMethodSetNumber

PaymentMethodSummary

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Foreign key to the MerchantAccount.

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
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Auto-assigned ID for the `MerchAccPaymentMethodSet` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Summary field that is automatically populated with comma-separated values from
### MerchAccPaymentMethodType.

This field is a calculated field.

### MerchAccPaymentMethodType

Refers to a payment method that is in a payment method set, which is defined by the `MerchAccPaymentMethodSet` object.
This object is available in API version 58.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`


Standard Objects MerchAccPaymentMethodType

Special Access Rules

To access Salesforce Payments objects, you must have a Salesforce Payments license with the Payments permission enabled for your
org. Salesforce Payments entities are available only in Lightning Experience.

Fields

**Field** **Details**

```
CurrencyIsoCode

PaymentInstrumentType

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only when the multicurrency feature is enabled. Contains the ISO code for any
currency used by the org.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of instrument the payer can pay with.

Possible values are:

**•** `us_bank_account - ACH_Debit`

**•** `affirm - Affirm`

**•** `afterpay - Afterpay`

**•** `afterpay_clearpay - Afterpay/Clearpay`

**•** `amazon_pay - Amazon Pay`

**•** `applepay - Apple Pay`

**•** `au_becs_debit - BECS_Debit`

**•** `bacs_debit - BACS_Debit`

**•** `bancontact - Bancontact`

**•** `card - Credit Cards`

**•** `cashapp - Cash App`

**•** `clearpay - Clearpay`

**•** `eps - EPS`

**•** `googlepay - Google Pay`

**•** `ideal - iDEAL`

**•** `klarna - Klarna`

**•** `link - Link`

**•** `paypal - PayPal`


Standard Objects MerchAccPaymentMethodType

**Field** **Details**

**•** `sepa_debit - SEPA Debit`

**•** `venmo - Venmo`

**•** `wechat_pay - WeChat Pay`

```
PaymentMethodSetId

PaymentMethodSetTypeNumber

SortOrder

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the MerchAccPaymentMethodSet.

This field is a relationship field.

**Relationship Name**
PaymentMethodSet

**Relationship Type**
Lookup

**Refers To**
MerchAccPaymentMethodSet

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Auto-assigned ID for the MerchAccPaymentMethodSet.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Sort order for the MechAccPaymentMethodType within the
MerchAccPaymentMethodSetExperience.

This object has these associated object. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**MerchAccPaymentMethodTypeHistory on page 63**
History is available for tracked fields of the object.


### Standard Objects MerchantAccount MerchantAccount

A type of bank account that lets a merchant accept payments from a variety of payment methods, including credit or debit cards, or
digital wallets. A Salesforce Payments merchant account is linked to an underlying payment gateway to process payments This object
is available in API version 56.0 and later.

Supported Calls

`create()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

To access Salesforce Payments objects, you must have a Salesforce Payments license and Payments must be enabled for your org.
Salesforce Payments objects are available only in Lightning Experience.

Fields

**Field** **Details**

```
AccountDescription

CountryIsoCode

CurrencyIsoCode

LastReferencedDate

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Information about the merchant account.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Country where the legal entity representing the account is.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Contains the ISO code for any currency allowed by the organization. Available only for
organizations with multi-currency enabled.

**Type**
dateTime


Standard Objects MerchantAccount

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

```
LastViewedDate

Mode

Name

OwnerId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user can have accessed this record or list view but not viewed it.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The operational mode of the merchant account. This field determines the account’s ability
to accept payments. For production, the account must be in Live mode.

Possible values are:

**•** `Connected`  - Merchant account is active but it can’t accept payments. This option is
only valid in production orgs.

**•** `Live`  - Merchant account is active and can accept payments. This option is only valid
in production orgs.

**•** `Test` –Merchant account is active but not able to accept payments. This option is only
valid in sandbox orgs, and the account can accept only test transactions.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the merchant account.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Name of the individual or group assigned to the merchant account.


Standard Objects MerchantAccount

**Field** **Details**

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

```
PaymentStatus

PayoutStatus

Status

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Merchant account is active and can accept payments.

Possible values are:

**•** `Disabled`

**•** `Enabled`

The default value is `Disabled` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Money can be moved from the payment provider account to the designated merchant
account.

Possible values are:

**•** `Disabled`

**•** `Enabled`

The default value is `Disabled` .

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates the state of the merchant account.

Possible values are:

**•** `Active`  - The merchant account can accept payments.


### Standard Objects MerchantAccountEvent

**Field** **Details**

**•** `Complete`                   - `PaymentStatus` and `DepositStatus` are enabled and all the
required information is provided.

**•** `Enabled`                   - `PaymentStatus` and `PayoutStatus` are enabled, but the payment
provider requires more information later. If the merchant doesn't provide the information,
then the account becomes restricted. The time limit that the merchant has to provide
the information is longer than the `RestrictedSoon` state.

**•** `Pending`                   - The merchant account exists but it can’t accept payments. This option
maintains backward compatibility for accounts that were created with API version 55.0
and earlier.

**•** `Rejected`                   - The account is rejected and an explanation is provided.

**•** `Restricted`                   - `PaymentStatus`, `PayoutStatus`, or both are disabled, so the
merchant account’s operation is limited.

**•** `Restricted Soon`                   - `PaymentStatus` and `PayoutStatus` are enabled, but
the payment provider requires more information. If the merchant doesn't provide the
information in a specific time period, then the account becomes restricted.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**MerchantAccountChangeEvent (API version 62.0)**
Change events are available for the object.

**MerchantAccountFeed**

Feed tracking is available for the object.

**MerchantAccountHistory**

History is available for tracked fields of the object.

**MerchantAccountOwnerSharingRule**

Sharing rules are available for the object.

**MerchantAccountShare**

Sharing is available for the object.

### MerchantAccountEvent

Represents a merchant account platform event. Subscribe to these events so you can listen and respond to them when they’re published.
For example, create a Salesforce Flow that is triggered when one of these events is published. This object is available in API version 59.0
and later.

[For more information about platform events, see the Platform Events Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_intro.htm)

Supported Calls

```
   describeSObjects()

```


Standard Objects MerchantAccountEvent

Special Access Rules

To access Salesforce Payments objects, you must have a Salesforce Payments license and Payments must be enabled for your org.
Salesforce Payments objects are available only in Lightning Experience.

Fields

**Field** **Details**

```
ChangeType

MerchantAccountId

```

**Type**
picklist

**Properties**
Restricted picklist

**Description**
Type of merchant account event, which triggers an event notification. You can write code
to listen to operate conditionally on the value of this field. For example, you can ignore a
create change but get notified of updates.

Possible values are:

**•** `Create` –Merchant account is created.

**•** `Disable` –The account is deactivated. For example, the payment provider or the
merchant disables an account due to fraudulent activity.

**•** `PaymentEnable` –The account is active and ready to receive payments.

**•** `PayoutEnable` –The account is ready to receive payouts.

**•** `Update` –Merchant account property change occurs.

**Type**
reference

**Properties**
Nillable

**Description**
Identifies the merchant account for which the event occurs.

This field is a relationship field.

**Relationship Name**
MerchantAccount

**Relationship Type**
Lookup

**Refers To**
MerchantAccount


### Standard Objects MessagingChannel MessagingChannel

Represents a communication channel that an end user can use to send a message to an agent. A communication channel can be an
SMS number, a Facebook page, or another supported messaging channel. This object is available in API version 40.0 and later.

Supported Calls

`create()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `search()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
BusinessHoursId

ChannelAddressIdentifier

ChannelDefinitionId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The operating hours for your business, when agents are available. Available only
in orgs that use Einstein Bots.

This is a relationship field.

**Relationship Name**
BusinessHours

**Relationship Type**
Lookup

**Refers To**
BusinessHours

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A UUID that identifies a deployed messaging channel. This identifier is unique
across orgs, so a channel with the same MessagingPlatformKey in a sandbox and
production will have a different ChannelAddressIdentifier for each. Available in
API version 59.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects MessagingChannel

**Field Name** **Details**

**Description**
The associated conversation channel definition, which is used only in Bring Your
Own Channel for Messaging and Bring Your Own Channel for CCaaS. Available
in API version 58.0 and later.

This field is a relationship field.

**Relationship Name**
ChannelDefinition

**Refers To**
ConversationChannelDefinition

```
ConsentType

ConversationEndResponse

CriticalWaitTime

Description

DeveloperName

```

**Type**
picklist

**Properties**
Create, defaultedOnCreate, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of consent, or opt-in, that is required to message users on this channel.
This field is available in API version 48.0 and later. Possible values are:

**•** `DoubleOptIn`

**•** `ExplicitOptIn`

**•** `ImplicitOptIn` (default value)

The property `defaultedOnCreate` has been removed in API version 51.0
and later. Now the consent type is defaulted to `ImplicitOptIn` when the
consent type isn’t set on create only for channels that support consents.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Automated response to the customer when the agent ends the conversation.
(Optional)

**Description**
Reserved for future use. This field has been deprecated as of API version 52.0.

**Description**
Reserved for future use.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects MessagingChannel

**Field Name** **Details**

**Description**
The developer name for the messaging channel. This value is a concatenation
of the messaging platform key and the message type.

```
DoubleOptInPrompt

EngagedResponse

InitialResponse

IsActive

IsAuthenticated

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Automated response to the end user to prompt them to doubly opt in to receiving
messages. Available in API version 48.0 and later.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Automated response to the customer when the conversation is accepted by the
agent. (Optional)

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
First automated response to the customer for a new conversation. (Optional)

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a channel is active and can receive messages.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a user is authenticated to a voice assistant. The org permission
Live Message Voice is required to access and update this field. Available in API
version 44.0 and later.


Standard Objects MessagingChannel

**Field Name** **Details**

```
IsoCountryCode

IsRequireDoubleOptIn

IsRestrictedToBusinessHours

IsUserMatchByExternalIdOnly

Language

MasterLabel

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Two-letter ISO 3166-1 alpha-2 code for the country that the phone number is
associated with. For example, the code for United States is `US` . Available in API
version 44.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether double opt-in is required ( `true` ) or not ( `false` ) for this
Messaging channel. Available in API version 48.0 and later.

**Description**
Reserved for future use.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether to restrict matching on customer by external ID only (and not
use the full name). This field has been deprecated as of API version 52.0.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Reserved for future use.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**

Unique name for the `MessagingChannel` .


Standard Objects MessagingChannel

**Field Name** **Details**

```
MessageType

MessagingPlatformKey

OfflineAgentsResponse

OptInPrompt

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Type of message. Possible values are:

**•** `AppleBusinessChat` —Represents Apple Messages for Business.

**•** `Custom` —Represents Bring Your Own Channel for Messaging or Bring Your
Own Channel for CCaaS. Available in API version 58.0 and later.

**•** `EmbeddedMessaging` —Represents Enhanced Chat. Available in API
version 50.0 and later.

**•** `Facebook`

**•** `Phone`

**•** `PSTNVoice` —Represents an Agentforce Voice channel that uses PSTN.
Available in API version 65.0 and later.

**•** `Text`

**•** `Voice`

**•** `WhatsApp`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Unique key for a channel that the end user can message or call based on the
MessageType.

**•** In PSTNVoice, SMS, WhatsApp, and LINE channels, the platform key is the
phone number associated with this channel.

**•** In Facebook Messenger channels, the platform key is the Facebook page ID
associated with this channel.

**•** In Apple Messages for Business channels, the platform key is the Apple
Messages identifier.

**•** In Enhanced Chat, the platform key is identical to the Channel Address
Identifier.

**Description**
Reserved for future use.

**Type**
textarea


Standard Objects MessagingChannel

**Field Name** **Details**

**Properties**
Create, Nillable, Update

**Description**

Automated response to the end user to prompt them to explicitly opt in to
receiving messages. Available in API version 49.0 and earlier.

```
OptInResponse

OptionsIdentifyEndUserLanguage

OptOutResponse

OutsideBusinessHoursResponse

PlatformType

```

**Type**
textarea

**Properties**
Create, Defaulted on create, Nillable, Update

**Description**

Automated response to the end user when they opt in to messaging. Available
in API versions 48.0 and 49.0. Use the `OptInConfirmation` field of the
MsgChannelLanguageKeyword on page 3463 object instead.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Auto-populates the Language field for this channel’s messaging users if their
locale is known. Supported for Enhanced Chat and Apple Messages for Business
only.

**Type**
textarea

**Properties**
Create, Defaulted on create, Nillable, Update

**Description**

Automated response to the end user when they opt out of messaging. Available
in API version 48.0 only. Use the `OptOutConfirmation` field of the
MsgChannelLanguageKeyword object instead.

**Description**
Reserved for future use.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort


Standard Objects MessagingChannel

**Field Name** **Details**

**Description**
Indicates whether the channel is `Standard` or `Enhanced` .

When a standard SMS or Facebook Messenger channel is upgraded, the
PlatformType changes from `Standard` to `Enhanced` . When a standard
WhatsApp channel is upgraded, the original channel’s PlatformType remains
`Standard` and a new channel is created with a PlatformType of `Enhanced` .

Enhanced Chat channels have a PlatformType of `Enhanced` .

```
RoutingConfigurationId

RoutingType

SessionHandler

TargetQueueId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Specifies which Omni-Channel routing configuration to use. This field is required
when `RoutingType` is `OmniSkills` [. To learn more, see Create Routing](https://help.salesforce.com/articleView?id=service_presence_create_routing_configuration.htm&language=en_US)
[Configurations.](https://help.salesforce.com/articleView?id=service_presence_create_routing_configuration.htm&language=en_US)

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Type used to support Omni-Channel’s different routing methods.

**•** `OmniQueue` (queue-based routing)

**•** `OmniSkills` (skills-based routing)

When this value isn’t set, `OmniQueue` is used.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The queue or Omni-Channel flow that the channel's messaging sessions are
routed to. Available in API version 51.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects MessagingChannelSkill

**Field Name** **Details**

**Description**

Queue in which incoming conversations are placed while waiting for an agent
to accept.

This is a relationship field.

**Relationship Name**
TargetQueue

**Relationship Type**
Lookup

**Refers To**
Group

```
TargetUserId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Messaging User or agent for the conversation. Available in API version 50.0 and
earlier.

While third-party messaging channels can be created via Apex, we recommend creating channels via the Messaging Settings page in
Setup. Channels created via Apex may not work and can't be deleted.

In enhanced WhatsApp, Facebook Messenger, Apple Messages for Business, and LINE channels, the flow of a channel's messaging traffic
is controlled by an associated MessagingChannelUsage record. The MessagingChannelUsage determines whether the channel is active
or deactivated.

### MessagingChannelSkill

Junction object that represents an association between MessagingChannel and Skill. This object is available in API version 45.0 and later.

For example, when we want to use Omni-Channel skills-based routing in Live message, this object maintains the mapping between the
messaging channel and the skill.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


### Standard Objects MessagingChannelUsage

Fields

**Field Name** **Details**

```
MessagingChannelId

SkillId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the MessagingChannel on page 3377.

This is a relationship field.

**Relationship Name**
### MessagingChannel

**Relationship Type**
Lookup

**Refers To**
### MessagingChannel

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the Skill on page 5029.

This is a relationship field.

**Relationship Name**
Skill

**Relationship Type**
Lookup

**Refers To**
Skill

### MessagingChannelUsage

Represents the status of an enhanced Messaging channel or of an application in a Unified Messaging channel. This object is available in
API version 60.0 and later.

A MessagingChannel can be associated with up to three MessagingChannelUsage records, each with a unique DeploymentType. The
role of a MessagingChannelUsage record differs slightly depending on whether it's used in an enhanced Messaging channel or a Unified
Messaging channel.

**•** In enhanced WhatsApp, Facebook Messenger, Apple Messages for Business, and LINE channels, each channel has one associated
### MessagingChannelUsage record with a DeploymentType of Conversation . The MessagingChannelUsage record determines

the channel's flow of messaging traffic. When you activate such a channel in Setup, its MessagingChannelUsage record updates to


Standard Objects MessagingChannelUsage

use a `DeploymentStatus` of `Active`, and messaging traffic can flow to and from Salesforce. Similarly, deactivating the
channel in Setup causes its MessagingChannelUsage record to update to a `DeploymentStatus` of `Disabled`, and stops the
flow of messaging traffic.

**•** In Unified Messaging channels, the MessagingChannelUsage record represents the status of a connected Service Cloud or Marketing
Cloud application. For example, if a WhatsApp Unified Messaging channel is connected to both Service Cloud and Marketing Cloud,
the MessagingChannel record has two associated MessagingChannelUsage records with a `DeploymentType` of `Conversation`
and `MJ`, respectively. These MessagingChannelUsage records are created when a user selects the Marketing or Service application
during Unified Messaging setup.

Supported Calls

`create()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ConsentType

DeploymentStatus

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The level of customer consent required for your business to message a customer on this
channel. Customers can opt out at any time.

Possible values are:

**•** `Implicit Opt-In` : By sending an initial message to your business, the customer
agrees to receive messages.

**•** `Explicit Opt-In` : The customer uses keywords to actively opt into receiving
messages.

**•** `Double Opt-In` : The customer uses keywords to opt in twice to receiving messages.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the connected channel or application. If the DeploymentStatus is `Active`,
messages can be sent or received (if permitted).

Possible values are:

**•** `New` —Admin selected the Marketing or Service application in Unified Messaging Setup,
or created a new enhanced WhatsApp, Facebook Messenger, Apple Messages for Business,
or LINE channel on the Messaging Settings page in Setup.

**•** `Provisioning` —Admin clicked **Connect** on an application in Unified Messaging
Setup, or **Activate** on an enhanced Messaging channel.


Standard Objects MessagingChannelUsage

**Field** **Details**

**•** `Active` —Provisioning was successful and the channel can be used to message with
customers via the connected application or channel.

**•** `Error` —Provisioning or deprovisioning wasn’t successful. The admin can retry.

**•** `Deprovisioning` —Admin clicked **Disconnect** on an application in Unified
Messaging Setup, or **Deactivate** on an enhanced Messaging channel.

**•** `Disabled` —Deprovisioning was successful and the channel or application can no
longer be used to message with customers.

```
DeploymentType

DisabledTime

ErrorReason

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Indicates whether the record is related to Service Cloud or Marketing Cloud.

Possible values are:

**•** `Conversation` —Relating to Service Cloud.

**•** `MessagingEngagement` —Relating to Marketing Cloud.

**•** `MJ` —Relating to Marketing Cloud. J stands for Journey Builder.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time the MessagingChannelUsage record entered the Disabled state after an admin
clicked **Disconnect** or **Deactivate** on the application or channel.

When the record is disabled, all inbound and outbound messages aren’t sent via the
connected application. Any sessions with a status other than Ended or Error are automatically
ended within 48 hours unless the MessagingChannelUsage record is reenabled.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
If an error occurs during connection, activation, disconnection, or deactivation of a
MessagingChannelUsage record, the ErrorReason provides more information about what
went wrong. For example, if an associated Service Cloud application for a Unified Messaging
channel is missing a fallback queue or consent keywords, the connection attempt fails with
an ErrorReason of `ProvisioningError` .

Possible values are:


Standard Objects MessagingChannelUsage

**Field** **Details**

**•** `DeprovisioningError`

**•** `InternalError`

**•** `InvalidSelection`

**•** `ProvisioningError`

```
MessagingChannelId

RoutingOverride

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The enhanced Messaging channel or Unified Messaging channel that the
MessagingChannelUsage record is associated with. A MessagingChannel can be associated
with up to three MessagingChannelUsage records.

This field is a relationship field.

**Relationship Name**
MessagingChannel

**Relationship Type**
Lookup

**Refers To**
MessagingChannel

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Applicable only to MessagingChannelUsage records with a deployment type of MJ (Marketing
Cloud). RoutingOverride indicates how messages are delivered in a unified channel where
both the Service and Marketing applications are connected.

Possible values are:

**•** `MJKeywordsOnly` —If a messaging user sends a marketing keyword that is defined
in Journey Builder, Journey Builder handles the message delivery and response. If a
messaging user sends a non-keyword message, Omni-Channel handles the message
delivery and response.

**•** `NonSessionMessages` —If a messaging user is engaged in an active Service Cloud
messaging session, Service Cloud handles message delivery and response. If the user
isn’t engaged in an active session, Journey Builder handles message delivery and response.

Regardless of the RoutingOverride value, outbound messages are always handled by Service
Cloud if the messaging user is engaged in an active Service Cloud messaging session. A
session is considered active if its status isn't Ended or Error.


### Standard Objects MessagingConfiguration MessagingConfiguration

Represents the details for a Messaging configuration. This object is available in API version 47.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
DeveloperName

Language

MasterLabel

MessagingServiceUrl

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The API name for this Messaging configuration.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language of this Messaging configuration.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The label for the Messaging configuration.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URL for the Messaging service.


### Standard Objects MessagingDeliveryError

**Field** **Details**

```
ProvisioningServiceUrl

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URL for the provisioning service.

### MessagingDeliveryError

Represents a log of triggered outbound failures to verify when a triggered outbound has failed. This object is available in API version
44.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CreatedById

CreatedDate

DestinationPhoneNumber

```

**Type**
reference

**Properties**
Defaulted on createFilter, Group, Sort

**Description**
ID of the user who created the error.

**Type**
dateTime

**Properties**
Defaulted on create, Filter, Sort

**Description**
Date the error was created.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects MessagingDeliveryError

**Field** **Details**

**Description**
The recipient of the phone call.

```
FailureReason

FlowEntity

FullMessage

Id

IsDeleted

LastModifiedById

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The provided reason for why the message failed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The entity that triggered the flow to send the message.

**Type**
textarea

**Description**
Plain error text.

**Type**
id

**Properties**
Defaulted on create, Filter, Group, idLookup, Sort

**Description**
Identifier of the error.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the error has been deleted.

**Type**
reference

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
The ID of the user who last modified the error log.


Standard Objects MessagingDeliveryError

**Field** **Details**

```
LastModifiedDate

MessagingChannelId

MessagingEndUserId

MessagingTemplateId

```

**Type**
dateTime

**Properties**
Defaulted on create, Filter, Sort

**Description**
Date when the Messaging error log was last modified.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the MessagingChannel on page 3377.

This is a relationship field.

**Relationship Name**
MessagingChannel

**Relationship Type**
Lookup

**Refers To**
MessagingChannel

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Identifier for the Messaging user.

This is a relationship field.

**Relationship Name**
MessagingEndUser

**Relationship Type**
Lookup

**Refers To**
MessagingEndUser

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Messaging template used.


### Standard Objects MessagingEndUser

**Field** **Details**

This is a relationship field.

**Relationship Name**
MessagingTemplate

**Relationship Type**
Lookup

**Refers To**
MessagingTemplate

```
Name

SystemModstamp

Type

### MessagingEndUser

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Namefield, Sort

**Description**
Name of the error. Maximum length is 80 characters.

**Type**
dateTime

**Properties**
Defaulted on create, Filter, Sort

**Description**
System modification time for the Messaging delivery error log.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The kind of event that occurred. Possible values include:

**•** `Error` (Default)

**•** `Warning`

Represents a single address—such as a phone number or Facebook page—communicating with a single Messaging channel. This
object is available in API version 40.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects MessagingEndUser

Fields

**Field** **Details**

```
AccountId

ContactId

HasInitialResponseSent

IsFullyOptedIn

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Account associated with this Messaging end user. Available in API version 43.0 and
later.

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
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the associated Contact. Available in API version 43.0 and later.

This field is a relationship field.

**Relationship Name**
Contact

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether an initial response has been sent to the Messaging end user ( `true` ) or
not ( `false` ).

**Type**
boolean


Standard Objects MessagingEndUser

**Field** **Details**

**Properties**
Defaulted on create, Filter, Sort

**Description**
Indicates whether the Messaging end user has opted in to receiving messages ( `true` ) or
not ( `false` ). This field compares the related messaging channel’s consent requirement to
the user’s consent status; if the user’s status meets the channel’s required consent level,
`IsFullyOptedIn` is set to `true` . Available in API version 48.0 and later.

```
IsOptedOut

IsoCountryCode

LastReferencedDate

LastViewedDate

LeadId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the Messaging end user has opted out of receiving messages. Available
in API version 48.0 and earlier. Use `MessagingConsentStatus` and
`IsFullyOptedIn` instead.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ISO country code associated with the Messaging end user.

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


Standard Objects MessagingEndUser

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the associated lead. Available in API version 57.0 and later.

This field is a relationship field.

**Relationship Name**
Lead

**Relationship Type**
Lookup

**Refers To**
Lead

```
Locale

Language

MessageType

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Reserved for future use.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The preferred language of the messaging user who participated in the messaging session.
SUpported for Messaging for In-App and Web and Apple Messages for Business only.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Type of message. Possible values are:

**•** `AppleBusinessChat` —Represents Apple Messages for Business.

**•** `Custom` —Represents Bring Your Own Channel. Available in API version 58.0 and later.

**•** `EmbeddedMessaging` —Represents Messaging for In-App and Web. Available in
API version 50.0 and later.

**•** `Facebook`

**•** `Phone`

**•** `Text`

**•** `Voice`


Standard Objects MessagingEndUser

**Field** **Details**

**•** `WhatsApp`

```
MessagingChannelId

MessagingConsentStatus

MessagingPlatformKey

Name

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the Messaging channel associated with the Messaging end user.

This is a relationship field.

**Relationship Name**
MessagingChannel

**Relationship Type**
Lookup

**Refers To**
MessagingChannel

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The consent status of the messaging user. This field is available in API version 48.0 and later.
Possible values are:

**•** `DoublyOptedIn`

**•** `ExplicitlyOptedIn`

**•** `ImplicitlyOptedIn`

**•** `OptedOut`

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**

The phone number, Facebook page ID, or unique key associated with this Messaging end
user.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


### Standard Objects MessagingLink

**Field** **Details**

**Description**
The name of the Messaging end user. Because this field is editable, we don’t recommend
referencing it in automation. Instead, use the Messaging Platform Key.

```
 OwnerId

 ProfilePictureUrl

```

Associated Objects

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner associated with this Messaging end user.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The URL of the Messaging end user's profile picture.

This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**MessagingEndUserChangeEvent (API version 62.0)**
Change events are available for the object.

**MessagingEndUserHistory**

History is available for tracked fields of the object.

**MessagingEndUserOwnerSharingRule**

Sharing rules are available for the object.

**MessagingEndUserShare**

Sharing is available for the object.

### MessagingLink

Represents the link between a Messaging Channel and where it's shared. This object is available in API version 47.0 and later.


Standard Objects MessagingLink

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Fields

**Field** **Details**

```
EntityType

MessagingChannelId

RecordTypeId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Possible values are:

**•** `Account`

**•** `Case`

**•** `Contact`

**•** `CustomEntityDefinition` —Custom Object Definition

**•** `Lead`

**•** `Opportunity`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The channel being shared. This is a relationship field.

**Relationship Name**
MessagingChannel

**Relationship Type**
Lookup

**Refers To**
MessagingChannel

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
This is a relationship field.

**Relationship Name**
RecordType


### Standard Objects MessagingSession

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
RecordType

```
 ShouldAttemptAutoLink

 ShouldPromptCreate

### MessagingSession

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
No longer in use. Indicated that an incoming messaging session was auto-linked to a
Salesforce contact or account based on information such as a phone number.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
No longer in use. Indicated that a contact or account was created for the messaging user if
none existed.

Represents a session on a Messaging channel. This object is available in API version 47.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AcceptTime

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time when an agent accepts an incoming Messaging session.


Standard Objects MessagingSession

**Field** **Details**

```
AgentMessageCount

AgentType

CaseId

ChannelEndUserFormula

ChannelKey

```

**Type**
int

**Properties**
Nillable

**Description**
The number of messages sent by the agent during the session.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of agent that is assigned to the Messaging session. Possible values are:

**•** `Agent`

**•** `Bot`

**•** `BotToAgent` —Bot & Agent

**•** `System` —Used for triggered outbound messages

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the case associated with this Messaging session.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
A concatenation of the Messaging channel and Messaging user.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier for the associated Messaging channel.


Standard Objects MessagingSession

**Field** **Details**

```
ChannelLocale

ChannelName

ChannelType

ConversationId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The locale of the associated Messaging channel.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the associated Messaging channel.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of the associated Messaging channel. Possible values are:

**•** `Alexa`

**•** `AppleBusinessChat` —Represents Apple Messages for Business.

**•** `EmbeddedMessaging` —Available in API version 55.0 and later.

**•** `Facebook`

**•** `GoogleHome`

**•** `Line`

**•** `Omega`

**•** `Phone`

**•** `Text`

**•** `Voice`

**•** `WeChat`

**•** `WebChat`

**•** `WhatsApp`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the related conversation. Available in API version 55.0 and later.


Standard Objects MessagingSession

**Field** **Details**

This field is a relationship field.

**Relationship Name**
Conversation

**Relationship Type**
Lookup

**Refers To**
Conversation

```
EndedByType

EndTime

EndUserAccountId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Who or what ended the enhanced messaging session. Possible values are:

**•** `Agent`

**•** `Bot`

**•** `EndUser`

**•** `System` :

**–** The session is inactive for a while, so the session ends.

**–** An automation ends the session.

**–** The session ended because of an error.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
The time when the Messaging session ended.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the end user's account record.

This is a relationship field.

**Relationship Name**
EndUserAccount

**Relationship Type**
Lookup


Standard Objects MessagingSession

**Field** **Details**

**Refers To**
Account

```
EndUserContactId

EndUserLanguage

EndUserMessageCount

LastReferencedDate

LastViewedDate

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the end user's contact record.

This is a relationship field.

**Relationship Name**
EndUserContact

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The preferred language of the messaging user who participated in the messaging session.

**Type**
int

**Properties**
Nillable

**Description**
The number of messages sent by the Messaging end user.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime


Standard Objects MessagingSession

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced (LastReferencedDate) and not viewed.

```
LeadId

MessagingChannelId

MessagingEndUserId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Lead associated with this Messaging session.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the Messaging channel associated with this Messaging session.

This is a relationship field.

**Relationship Name**
MessagingChannel

**Relationship Type**
Lookup

**Refers To**
MessagingChannel

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the Messaging end user associated with this Messaging session.

This is a relationship field.

**Relationship Name**
MessagingEndUser

**Relationship Type**
Lookup

**Refers To**
MessagingEndUser


Standard Objects MessagingSession

**Field** **Details**

```
Name

OpportunityId

Origin

OwnerId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of this Messaging session.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the opportunity record associated with this Messaging session.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The origin of this Messaging session. Possible values are:

**•** `AgentInitiated`

**•** `ConversationClose` —Messaging user deleted the conversation in Apple Messages

**•** `ConversationControlLost` —Third-party bot resumes control from Salesforce
bot or agent

**•** `Help`

**•** `InboundInitiated`

**•** `OptIn` —Opt In Status Change

**•** `OptOut` —Opt Out Status Change

**•** `TriggeredOutbound`

Messaging sessions can’t be created using Apex code. They can be created only through
customer initiation or by using Process Builder, flows, or the Start Conversation action.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner associated with this Messaging session.

This is a polymorphic relationship field.


Standard Objects MessagingSession

**Field** **Details**

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

```
PreviewDetails

SessionKey

StartTime

Status

```

**Type**
string

**Properties**
Nillable

**Description**
The preview shown to an agent for this Messaging session.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The identifier for the Messaging session.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
The time when the Messaging session started.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The status of the Messaging session. Possible values are:

**•** `New` (standard channels only)

**•** `Active`

**•** `Consent` (enhanced channels only)

**•** `Waiting`

**•** `Paused` (enhanced channels only)

**•** `Inactive` (enhanced channels only)

**•** `Ended`


Standard Objects MessagingSession

**Field** **Details**

**•** `Error` (enhanced channels only)

[To learn more about these statuses, see Lifecycle of a Messaging Session in Salesforce Help.](https://help.salesforce.com/s/articleView?id=service.messaging_life_cycle.htm&type=5&language=en_US)

```
 TargetUserId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the target user associated with this Messaging session.

This is a relationship field.

**Relationship Name**
TargetUser

**Relationship Type**
Lookup

**Refers To**
User

To monitor messaging session activity, report on the MessagingSession and MessagingSessionMetrics on page 3409 objects.
[MessagingSessionMetrics captures metrics about a messaging session, such as agent and end user response time. See Report on](https://help.salesforce.com/s/articleView?id=service.messaging_reporting.htm&type=5&language=en_US)
[Messaging Activity in Service Cloud.](https://help.salesforce.com/s/articleView?id=service.messaging_reporting.htm&type=5&language=en_US)

Associated Objects

This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**MessagingSessionChangeEvent (API version 62.0)**
Change events are available for the object.

**MessagingSessionFeed**

Feed tracking is available for the object.

**MessagingSessionHistory**

History is available for tracked fields of the object.

**MessagingSessionOwnerSharingRule**

Sharing rules are available for the object.

**MessagingSessionShare**

Sharing is available for the object.


### Standard Objects MessagingSessionMetrics MessagingSessionMetrics

Represents a metric gathered about a specific enhanced messaging session, such as average agent response time. This object is available
starting in October 2024 in API version 62.0 and later.

To reference this object in reports, create a custom report type with Messaging Session as the primary object and Messaging Session
Metrics as the secondary object.

Be sure to include the `MessagingSessionMetricType` field in your custom report. These records are available only for Messaging
sessions created after October 1, 2024.

Supported Calls

`create()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Multiple MessagingSessionMetrics records are generated when a session ends in an enhanced Messaging channel or Messaging for
In-App and Web channel. These records aren't generated for standard messaging sessions.

Fields

**Field** **Details**

```
MessagingSessionId

MessagingSessionMetricType

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the related messaging session.

This field is a relationship field.

**Relationship Name**
### MessagingSession

**Relationship Type**
Master-detail

**Refers To**
MessagingSession (the master object)

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The metric that this record captures.

Possible values are:


### Standard Objects MessagingTemplate

**Field** **Details**

**•** `AgentMessageCount` —The number of messages sent by the agent in the session.

**•** `AverageAgentResponseTime` —The average number of seconds between an
end user's message and the agent’s response in the session.

**•** `AverageEndUserResponseTime` —The average number of seconds between
an agent or bot’s message and the end user's response in the session.

**•** `EndUserMessageCount` —The number of messages sent by the end user in the
session.

**•** `MaxAgentResponseTime` —The longest span of time (in seconds) between an
end user's message and the agent’s response in the session.

**•** `MaxEndUserResponseTime`                   - The longest span of time (in seconds) between
an agent or bot’s message and the end user's response in the session.

For each closed messaging session in enhanced Messaging channels and Messaging for
In-App and Web, one MessagingSessionMetrics record is generated per
MessagingSessionMetricType value. This means that six MessagingSessionMetrics records
are generated per session.

```
MessagingSessionMetricValue

Name

```

**Type**
int

**Properties**
Create, Filter, Group, Sort

**Description**
The value of the measured metric. For example, if the MessagingSessionMetricType is
`EndUserMessageCount`, a MessagingSessionMetricValue of `12` means that the end
user sent 12 messages during the messaging session.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An autogenerated number identifying the MessagingSessionMetrics record.

### MessagingTemplate

Represents a Messaging template used to send pre-formatted messages. This object is available in API version 47.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `search()`,
`update()`, `upsert()`


Standard Objects MessagingTemplate

Fields

**Field** **Details**

```
Description

DeveloperName

Language

MasterLabel

Message

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the Messaging template.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The API name for the Messaging template.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the Messaging template.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The label of the Messaging template.

**Type**
textarea

**Properties**
Create, Update

**Description**
The body text of the Messaging template.


### Standard Objects MetadataApiOpEventLog MetadataApiOpEventLog MetadataApiOpEventLog stores details of Metadata API retrieval and deployment requests. This object is available in API version 62.0

and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
ClientIdentifier

ClientIp

CpuTime

LoginKey

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API client ID.

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
string


Standard Objects MetadataApiOpEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

```
OperationType

RequestIdentifier

RunTime

SessionKey

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The operation that’s being performed.

**Possible Values**

**•** `meta_deploy`

**•** `meta_list`

**•** `meta_retrieve`

**•** `meta_synchronous_create`

**•** `meta_synchronous_read`

**•** `meta_synchronous_upsert`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Globally unique id for a given request.

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


### Standard Objects MetadataPackage

**Field** **Details**

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

```
Timestamp

Uri

UserIdentifier

### MetadataPackage

```

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
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 18-character ID of the user who’s using Salesforce services through the UI or the API.

For example: `00530000009M943YAS`

Represents a package that has been developed in the org you’re logged in to. Applies to unlocked, unmanaged, first-generation, and
second-generation managed packages.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`


Standard Objects MetadataPackage

Fields

**Field Name** **Details**

```
Name

NamespacePrefix

PackageCategory

```

Usage

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**

The name of the package.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
For first-generation and second-generation managed packages, and unlocked
packages with namespaces, this field is the namespace prefix assigned to the
package. For unmanaged packages, or no-namespace unlocked packages, this
field is blank.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of package. Valid values are:

**•** `Application` (internal use only)

**•** `Module` (internal use only)

**•** `Package` —Represents either an unmanaged package or a first-generation
managed package.

**•** `Package2` —Represents either an unlocked package or a second-generation
managed package.

The default value is Package.

This field is available in API version 49.0 and later.

Here are examples of the types of API queries you can perform.


### Standard Objects MetadataPackageVersion

**Query** **String**

Show all managed and unmanaged packages in the org `SELECT Name, NamespacePrefix FROM`

### `MetadataPackage`

Show only managed packages in the org

### MetadataPackageVersion

```
SELECT Name, NamespacePrefix FROM

MetadataPackage WHERE NamespacePrefix <>

''

```

Represents a package version (managed or unmanaged) that has been uploaded from the org you’re logged in to.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
BuildNumber

IsDeprecated

MajorVersion

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The build number of the version. For example, if you upload two beta versions,
they have build numbers 1 and 2. Then, when you upload a non-beta version,
the build number is 3. When you upload a new version, the build number resets
to 1.

**Type**
boolean

**Properties**
Filter, Group, Sort

**Description**
Indicates whether the package version is deprecated. Available in API version
46.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects MetadataPackageVersion

**Field Name** **Details**

**Description**
The first number in a package version number. A version number either has an
`x.y` format or an `x.y.z` format. The `x` represents the major version, `y` the
minor version, and `z` the patch version.

```
MetadataPackageId

MinorVersion

Name

PatchVersion

ReleaseState

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 18-character package ID starting with `033` .

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The second number in a package version number. A version number either has
an `x.y` format or an `x.y.z` format. The `x` represents the major version, `y`
the minor version, and `z` the patch version.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**

The name of the package version.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The third number in a package version number, if present. A version number
either has an `x.y` format or an `x.y.z` format. The `x` represents the major
version, `y` the minor version, and `z` the patch version.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


Standard Objects MetadataPackageVersion

**Field Name** **Details**

**Description**
If the package version is a beta version, the value is `Beta` . Otherwise, the value
is `Released` .

Usage

Here are examples of the types of API queries you can perform.

**Query** **String**

Get all package versions for the package that has a `SELECT Id, Name, ReleaseState,`
`MetadataPackageID` of 033D00000001xQlIAI `MajorVersion, MinorVersion, PatchVersion`

```
                             FROM MetadataPackageVersion WHERE

                             MetadataPackageId = '033D00000001xQlIAI'

```

Get the package version for the package with a specific
`MetadataPackageID` and a major version greater than 1

Get released package versions for the package with a specific

```
MetadataPackageID

```

**Java Code Sample**

```
SELECT Id FROM MetadataPackageVersion WHERE

MetadataPackageId ='033D00000001xQlIAI'

AND MajorVersion > 1

SELECT Id FROM MetadataPackageVersion WHERE

MetadataPackageId = '033D00000001xQlIAI'

AND ReleaseState = 'Released'

```

Suppose you want to push version 3.4.6 of your package to all orgs. Let’s write some code to identify the orgs eligible for the upgrade.
This example demonstrates how to generate the list of subscriber orgs eligible to be upgraded to version 3.4.6 of a package.

This code sample uses the Web Services Connector (WSC).

```
// Finds all Active subscriber orgs that have the package installed

String PACKAGE_SUBSCRIBER_ORG_KEY_QUERY = "Select OrgKey from PackageSubscribers where

OrgStatus = 'Active' and InstalledStatus = 'I'";

// Finds all MetadataPackageVersions lower than the version given, including the list

// of subscribers for each version

String METADATA_PACKAGE_VERSION_QUERY = "Select Id, Name, ReleaseState, (%s) from"

 + " MetadataPackageVersion where MetadataPackageId = '%s' AND ReleaseState = 'Released'"

 + " AND (MajorVersion < 3 OR (MajorVersion = 3 and MinorVersion < 4)"

 + " OR (MajorVersion = 3 and MinorVersion = 4 and PatchVersion < 6))";

// conn is an EnterpriseConnection instance initialized with a ConnectionConfig object

// representing a connection to the developer org of the package

QueryResult results = conn.query(String.format(METADATA_PACKAGE_VERSION_QUERY,

PACKAGE_SUBSCRIBER_ORG_KEY_QUERY));

// This list will hold all of the PackageSubscriber objects that are eligible for upgrade

// to the given version

```


### Standard Objects Metric

```
   List<PackageSubscriber> subscribers = new ArrayList<>();

   for (SObject mpvso : results.getRecords()) {

     // Cast the sObject to a MetadataPackageVersion

     MetadataPackageVersion mpv = (MetadataPackageVersion) mpvso;

     // Add subscribers to our list

     if (mpv.getPackageSubscribers() != null) {

     for (SObject psso : mpv.getPackageSubscribers().getRecords()) {

      subscribers.add((PackageSubscriber) psso);

     }

    }

   }

```

**Next Step**

Create a push request using PackagePushRequest.

### Metric

The Metric object represents the components of a goal metric such as its name, metric type, and current value.

Note: The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information,
[see Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
CompletionDate

CurrentValue

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The completion date of the metric.

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
The current value of the metric.


Standard Objects Metric

**Field Name** **Details**

```
Description

DueDate

GoalId

InitialValue

IsCompletionMetric

LastComment

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the metric. The maximum length is 65,535 characters.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The due date of the metric.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the goal the metric is related to.

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
The initial value of the metric.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read only. If `true`, the metric measures whether or not the metric is finished.
If `false`, the metric measures how much is finished compared to a targeted
value.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects Metric

**Field Name** **Details**

**Description**
A comment that provides more context about the metric, such as its status or
progress. The maximum length is 255 characters.

```
LastReferencedDate

LastViewedDate

Name

OwnerId

Progress

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp that indicates when a user last viewed a record that is related to
this metric.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp that indicates when a user last viewed this metric. If this value is
null, this record might have been only referenced ( `LastReferencedDate` )
and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the metric.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the user who owns the metric.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
Read only. The overall progress of the metric.


Standard Objects Metric

**Field Name** **Details**

```
RecordTypeId

StartDate

Status

TargetValue

Weight

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the related record type.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The start date of the metric.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the metric. Possible values include:

**•** Not Started

**•** On Track

**•** Behind

**•** Critical

**•** Completed

**•** Postponed

**•** Canceled

**•** Not Completed

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
The target value of the metric.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update


### Standard Objects MetricDataLink

**Field Name** **Details**

**Description**
The weight of the metric. The sum of the weights should equal 100%.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**MetricFeed**

Feed tracking is available for the object.

**MetricHistory**

History is available for tracked fields of the object.

The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

**MetricOwnerSharingRule**

Sharing rules are available for the object.

The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

**MetricShare**

Sharing is available for the object.

### MetricDataLink

The link between the metric and the data source, such as a report.

Note: The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information,
[see Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
DatasourceFieldName

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The field name of the data source, such as a report summary field.


### Standard Objects MigratedEmail

**Field Name** **Details**

```
DataSourceId

LastSynchronizationTime

Name

TargetId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the data source.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The last time the data was synchronized.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
The name given to the data link record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the metric that the data is linked to.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**MetricDataLinkHistory**

History is available for tracked fields of the object.

The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

### MigratedEmail

For internal use only.


### Standard Objects MilestoneType MilestoneType

Represents a milestone (required step in a customer support process). This object is available in API version 18.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

As of Summer ’20 and later, only Salesforce admins, users with access to the Case, Entitlement, or Work Order objects, and users with
the View Setup and Configuration permission can access this object.

Fields

**Field** **Details**

```
Description

Name

RecurrenceType

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Update

**Description**
A description of the milestone.

**Type**
string

**Properties**
Create, Filter, idLookup, Update

**Description**
The name of the milestone.

**Type**
picklist

**Properties**
Create,Update

**Description**
The type of recurrence for the milestone.


### Standard Objects MktJourneyDcsnSetup

Usage

Use this object to query and manage the milestone type for CaseMilestone records.

SEE ALSO:

CaseMilestone

SlaProcess

### MktJourneyDcsnSetup

Represents a collection of Marketing Cloud Engagement journeys that you can interact with by using Salesforce Flow in Marketing Cloud.
This object is available in API version 65.0 and later.

You can use interaction data from a Marketing Cloud Engagement journey to trigger a Flow, or to configure decision activities in a Flow.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
BusinessUnitId

Description

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique Marketing Cloud business unit ID to use with the collection of journeys. This ID
is configured in Marketing Cloud, and is different from the Member ID (MID) or Enterprise
ID (EID) of your Marketing Cloud Engagement account.

This field is a relationship field.

**Relationship Name**
BusinessUnit

**Refers To**
BusinessUnit

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the collection of journeys.


### Standard Objects MLField

**Field** **Details**

```
EnterpriseIdentifier

Name

### MLField

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Enterprise ID (EID) of your parent Marketing Cloud Engagement account.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
A name for the collection of journeys.

Represents a single field in a data definition. This object is available in API version 50.0 and later.

Supported Calls

`delete()`, `describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
Entity

Field

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The object that contains the field.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The name of the field.


### Standard Objects MlIntentUtteranceSuggestion MlIntentUtteranceSuggestion

Represents a customer input, used for training purposes in the feedback loop process of a conversation. Admins can add these inputs
to the intent training model. This object is available in API version 51.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ConfigId

IntentSuggestion

ReviewStatus

Utterance

UtteranceCount

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The recommended intent.

**Type**
picklist

**Properties**
Filter, Group, Restricted Picklist, Sort

**Description**
Possible values are: Ignore, New

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The text input from the end user.

**Type**
integer

**Properties**
Filter, Group, Sort


### Standard Objects MLPredictionDefinition

**Field** **Details**

**Description**
A count of the Utterance field.

### MLPredictionDefinition

Represents a prediction definition that specifies details about the prediction. This object is available in API version 50.0 and later.

Supported Calls

`delete()`, `describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ApplicationId

DeveloperName

Language

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of the parent AI Application.

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


Standard Objects MLPredictionDefinition

**Field** **Details**

**Description**
The language of the prediction. Possible values are:

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

PredictionField

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Label that identifies the prediction throughout the Salesforce user interface.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Specifies the namespace of the prediction, if installed with a managed package.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects MLPredictionDefinition

**Field** **Details**

**Description**
Field that the prediction is based on.

```
PushbackField

Status

Type

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Field that the prediction writes scores to.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the prediction. Possible values are:

**•** `Disabled`

**•** `Draft`

**•** `Enabled`

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of model that returns the prediction values. Possible values are:

**•** `BinaryClassification`

**•** `DeepLearningIntentClassification`

**•** `DeepLearningNameEntityRecognition`

**•** `GlobalDeepLearningIntentClassification`

**•** `GlobalDeepLearningNameEntityRecognition`

**•** `LanguageDetection`

**•** `MulticlassClassification`

**•** `Regression`

**•** `ScoringSpecificOutcome`


### Standard Objects MLModel MLModel

Represents an AI model that can be used in Einstein Prediction Builder, Einstein Recommendation Builder, and other Einstein features.
This object is available in API version 53.0 and later.

This object contains information that represents many types of AI models. Some fields contain information for only a specific type of
model.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Available with Einstein Prediction Builder and Einstein Recommendation Builder.

Fields

**Field** **Details**

```
ApprovalStatus

Dataset

ModelType

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates whether the model is approved, pending approval, or rejected.

Possible values are:

**•** `Approved`

**•** `Pending`

**•** `Rejected`

The default value is `Pending` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the dataset used to create the model.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


Standard Objects MLModel

**Field** **Details**

**Description**
Indicates the type of model.

Possible values are:

**•** `BinaryClassification`

**•** `DecisionTree`

**•** `DeepLearningIntent`

**•** `DeepLearningNER`

**•** `GeneralizedLinearModels`

**•** `GlobalDeepLearningIntent`

**•** `GlobalDeepLearningNER`

**•** `GlobalLanguageDetection`

**•** `GradientBoostedTrees`

**•** `LinearRegression`

**•** `LinearSupportVectorClassifiers`

**•** `LogisticRegression`

**•** `MulticlassClassification`

**•** `NaiveBayes`

**•** `NeuralNet`

**•** `PopularityCount`

**•** `RandomForest`

**•** `Regression`

**•** `XGBoost`

```
Name

PredictionDefinitionId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The automatically generated ID that uniquely identifies the model.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the related prediction definition.

This field is a relationship field.

**Relationship Name**
PredictionDefinition


Standard Objects MLModel

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
MLPredictionDefinition

```
RecommendationDefinitionId

ScoringStatus

TrainingEndTime

TrainingStartTime

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the related recommendation definition.

This field is a relationship field.

**Relationship Name**
RecommendationDefinition

**Relationship Type**
Lookup

**Refers To**
MLRecommendationDefinition

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Indicates whether scoring is enabled or disabled.

Possible values are:

**•** `Disabled`

**•** `Enabled`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Indicates the date and time when the training ended.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


### Standard Objects MLModelFactor

**Field** **Details**

**Description**
Indicates the date and time when the training started.

### MLModelFactor

Represents a field value that has a positive or negative effect on the model’s score. This object is available in API version 53.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Available with Einstein Prediction Builder and Einstein Recommendation Builder.

Fields

**Field** **Details**

```
Correlation

FactorType

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Shows the strength of association between the variable and the outcome. The higher the
correlation, the greater the association.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of factor.

Possible values are:

**•** `ModelFactlet` —The field value strongly influences the outcome because the model
determined that this field is always important. For example, the model can decide that
the field `Industry` is always important to the outcome, regardless of its value.

**•** `ModelFactor` —The field value is important to the outcome because the field’s value
is significant. For example, the model can decide that the `Annual Revenue` field
value is important to the outcome because the value is above $1,000,000 or below
$50,000.


Standard Objects MLModelFactor

**Field** **Details**

```
Importance

ModelId

Name

Type

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Shows how much the variable influences the outcome. The higher the value, the greater
the impact.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related model.

This field is a relationship field.

**Relationship Name**
Model

**Relationship Type**
Lookup

**Refers To**
MLModel

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The automatically generated ID that uniquely identifies the model.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of model factor.

Possible values are:

**•** `And`

**•** `Basic`

**•** `Or`


### Standard Objects MLModelFactorComponent

**Field** **Details**

```
Weight

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Indicates how significant the field value is to the outcome or score. Model factlets tend to
have higher weights than model factors.

### MLModelFactorComponent

Represents information about the related MLModelFactor. For example, this object can represent a field value or a field range such as
“Title = CEO” or “Annual Revenue >10000000”. This object is available in API version 53.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Available with Einstein Prediction Builder and Einstein Recommendation Builder.

Fields

**Field** **Details**

```
FactorLabelKey

FeatureType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Maps the model factor component to a label that can be displayed to the user.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
`FeatureType` and `FeatureValue` indicate a feature that doesn’t have a corresponding
field. For example, to indicate the feature “Percent = 97%”, the `FeatureType` is `Percent`
and the `FeatureValue` is `97` .

Possible values are:


Standard Objects MLModelFactorComponent

**Field** **Details**

**•** `Binary`

**•** `Combobox`

**•** `Currency`

**•** `Date`

**•** `DateTime`

**•** `Email`

**•** `ID`

**•** `Integral`

**•** `MultiPicklist`

**•** `Percent`

**•** `Phone`

**•** `Picklist`

**•** `Real`

**•** `Text`

**•** `TextArea`

**•** `URL`

```
FeatureValue

LeftHandDerivedField

ModelFactorId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The feature’s value. See `FeatureType` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If the model factor component is an equation, this field represents the name of the field on
the left side of the equation. For example, if the model factor component is `Title =`
`CEO`, this value is `Title` .

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related MLModelFactor.

This field is a relationship field.


Standard Objects MLModelFactorComponent

**Field** **Details**

**Relationship Name**
ModelFactor

**Relationship Type**
Lookup

**Refers To**
MLModelFactor

```
ModelId

Name

Operator

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the related MLModel.

This field is a relationship field.

**Relationship Name**
Model

**Relationship Type**
Lookup

**Refers To**
MLModel

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The automatically generated ID that uniquely identifies the model.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
If the model factor component is an equation, this field represents the operator. For example,
if the model factor component is `Title = CEO`, the operator is `Equals` .

Possible values are:

**•** `Contains`

**•** `EndsWith`

**•** `Equals`

**•** `GreaterThan`


### Standard Objects MLModelMetric

**Field** **Details**

**•** `IsNotNull`

**•** `IsNull`

**•** `LessThan`

**•** `NotEquals`

**•** `StartsWith`

```
RightHandDerivedField

SortOrder

Value

### MLModelMetric

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If the model factor component is an equation, this field represents the name of the field on
the right side of the equation.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
If the model factor has multiple model factor components, this field indicates the order in
which this model factor component appears.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If the model factor component specifies a value, this field represents the value. For example,
if the model factor component is `Title = CEO`, this field is `CEO` .

Represents a metric or statistic about the related model, such as accuracy, precision, or RSquared. Use a model’s metrics to learn about
its performance and to compare it with other models. This object is available in API version 53.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects MLModelMetric

Special Access Rules

Available with Einstein Prediction Builder and Einstein Recommendation Builder.

Fields

**Field** **Details**

```
BasicMetricValue

ComplexMetricValue

DataSetType

EndTime

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The value of a basic metric. A basic metric is a single number. For metrics that comprise a
set of graph points, see `ComplexMetricValue` .

**Type**
textarea

**Properties**
Nillable

**Description**
The X and Y values for a complex metric. A complex metric is a coordinate on a graph. For
example, in classification models, you can use a line on a graph to create classification
categories.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of dataset.

Possible values are:

**•** `Baseline`

**•** `HoldOut`

**•** `Live`

**•** `Model`

**•** `Training`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects MLModelMetric

**Field** **Details**

**Description**
The date and time when the model training finished.

```
GraphType

MetricType

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of graph.

Possible values are:

**•** `ConfidencePlot`

**•** `ConfusionMatrixPerThreshold`

**•** `DiscountedCumulativeGainsGraph`

**•** `HitRateGraph`

**•** `KBasedRankingGraph`

**•** `LiftPlot`

**•** `MeanReciprocalRankGraph`

**•** `MultiClassConfusionMatrixPerThreshold`

**•** `MultiClassMisclassifications`

**•** `NormalizedDiscountedCumulativeGainsGraph`

**•** `PrecisionGraph`

**•** `RecallGraph`

**•** `RegressionErrorBands`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of metric.

Possible values are:

**•** `Accuracy`

**•** `AveragePrecision`

**•** `BalancedAccuracy`

**•** `DiscountedCumulativeGainAtK`

**•** `ExpectedTopAbsoluteRank`

**•** `ExpectedTopPercentileRank`

**•** `F1Score`

**•** `FMeasure`


Standard Objects MLModelMetric

**Field** **Details**

**•** `HitRateAtK`

**•** `LiftBucket`

**•** `MeanAbsoluteError`

**•** `MeanAbsoluteRank`

**•** `MeanAveragePrecisionAtK`

**•** `MeanPercentileRank`

**•** `MeanReciprocalRank`

**•** `MeanReciprocalRankAtK`

**•** `MeanTopReciprocalRank`

**•** `NormalizedDiscountedCumulativeGainsAtK`

**•** `Precision`

**•** `PrecisionAtK`

**•** `RSquared`

**•** `Recall`

**•** `RecallAtK`

**•** `RootMeanSquaredError`

**•** `auPR`

**•** `auROC`

```
ModelId

Name

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related MLModel.

This field is a polymorphic relationship field.

**Relationship Name**
Model

**Relationship Type**
Lookup

**Refers To**
MLModel

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An automatically generated ID that uniquely identifies the metric.


### Standard Objects MLRecommendationDefinition

**Field** **Details**

```
RowCount

Span

StartTime

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of rows.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The time span for the metric. Possible values are:

**•** `Day`

**•** `Hour`

**•** `Month`

**•** `SinceLastAction`

**•** `Week`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the model training started.

### MLRecommendationDefinition

For internal use only.

### MobileDeviceAppRegistration

Represents the details provided in a mobile device registration event from an app that uses the Engagement Mobile SDK. This object is
available in API version 65.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`update()`, `upsert()`


Standard Objects MobileDeviceAppRegistration

Fields

**Field** **Details**

```
DatetimeInDevice

DeviceModel

DevicePlatform

DeviceSystemToken

DeviceSystemTokenHash

DeviceTimezone

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time of the registration event, based on values provided by the device.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The model of the device that’s being registered, such as `iPhone 17` or `Google Pixel` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The operating system of the mobile device, such as `iPhone OS` or `Android` .

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A unique token that represents the mobile device. The push notification service (such as
Apple Push Notification service or Firebase Cloud Messaging) uses this token to deliver
messages to the device.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A hash of the device token.

**Type**
string


Standard Objects MobileDeviceAppRegistration

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The time zone that the device is located in when the registration event occurs.

```
DeviceVersion

Deviceid

Eventid

IsBackgroundRefreshEnabled

IsBluetoothEnabled

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The version or model number of the device.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A unique identifier for the mobile device.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A unique identifier for the registration event.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the device gives permission for the app to receive updates while it’s in
the background.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether Bluetooth is enabled on the device.


Standard Objects MobileDeviceAppRegistration

**Field** **Details**

The default value is `false` .

```
IsDst

IsLocationEnabled

IsPushEnabled

Locale

MobileAppName

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the device’s locale observes daylight saving time (DST).

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the device has location services enabled for the app.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the device has push notifications enabled for the app.

The default value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The locale string for the device, such as `en_US` or `ja_JP` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the mobile app, as configured in Setup.


Standard Objects MobileDeviceAppRegistration

**Field** **Details**

```
MobileAppVersion

MobileAppid

PartyIdentificationName

PartyIdentificationNumber

PartyIdentificationType

RegistrationDatetime

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The version number of the mobile app that generated the registration event.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A unique ID that represents the mobile app.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the party identifier for identity resolution rules.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID used for identity resolution comparisons.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A string that provides additional information about the type of party identifier used, such as
`Driver License` or `SSN` .

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update


### Standard Objects MobileSecurityAssignment

**Field** **Details**

**Description**
The date and time when the registration event occurred.

```
Registrationid

SdkVersion

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A unique ID for the registration event.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The version of the Mobile Engagement SDK that the app uses.

### MobileSecurityAssignment

Represents the assignment of mobile security policies to a profile. The policies apply to the Salesforce mobile app with Enhanced Mobile
App Security enabled. This object is available in API version 54.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Accessing this object requires the Enhanced Mobile App Security add-on subscriptions and the Enforce Enhanced Mobile App Security
user permission.

Fields

**Field** **Details**

```
DeveloperName

```

**Type**
string


Standard Objects MobileSecurityAssignment

**Field** **Details**

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
The combined language and locale ISO code, which controls the language of the
MobileSecurityAssignment.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label for this MobileSecurityAssignment value. This display value is the internal label that
doesn't get translated.

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


### Standard Objects MobileSecurityPolicy

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
ProfileId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The profile ID that the mobile security policies are assigned to.

This field is a relationship field.

**Relationship Name**
Profile

**Refers To**
Profile

### MobileSecurityPolicy

Enables mobile security policies on the Salesforce mobile app with Enhanced Mobile Security. This object is available in API version 50.0
and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Accessing this object requires the Enhanced Mobile App Security add-on subscriptions and the Enforce Enhanced Mobile App Security
user permission.


Standard Objects MobileSecurityPolicy

Fields

**Field** **Details**

```
DeveloperName

EffectiveDate

IsEnabled

Language

MasterLabel

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date a mobile security policy is enforced.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
A value indicating whether a mobile security policy is enabled.

The default value is 'false'.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The two-to five-character code that represents the language and locale ISO.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label of the mobile security policy.


Standard Objects MobileSecurityPolicy

**Field** **Details**

```
MobilePlatform

MobileSecurityAssignmentId

NamespacePrefix

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The mobile operating system.

Possible values are:

**•** `Android`

**•** `iOS`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the ID of the mobile security assignment.

This is a relationship field.

**Relationship Name**
MobileSecurityAssignment

**Relationship Type**
Lookup

**Refers To**
MobileSecurityAssignment

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


Standard Objects MobileSecurityPolicy

**Field** **Details**

**•** In orgs that aren’t Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

```
RuleValue

RuleValueType

SeverityLevel

Type

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Value of the mobile security policy rule.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of mobile security policy rule.

Possible values are:

**•** `Boolean`

**•** `Text`

**•** `TextList`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The severity level of a mobile security policy.

Possible values are:

**•** `Critical`

**•** `Error`

**•** `Info`

**•** `Warn`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of mobile security policy.


Standard Objects MobileSecurityPolicy

**Field** **Details**

Possible values are:

**•** `AllowedDeviceList` —Allowed Device List

**•** `Block3dTouch` —Block 3D Touch

**•** `BlockCalendar` —Block Calendar

**•** `BlockCamera` —Block Camera

**•** `BlockContacts` —Block Contacts

**•** `BlockCustomKeyboard` —Block Custom Keyboard

**•** `BlockFileBackup` —Block File Backup

**•** `BlockMicrophone` —Block Microphone

**•** `BlockOsSharing` —Block OS Share Actions

**•** `BlockedDeviceList` —Blocked Device List

**•** `BrowserUriScheme` —Mobile Browser URI Scheme

**•** `CheckBiometric` —Check Biometric Login Data

**•** `DevicePasscode` —Require Device Passcode

**•** `DisableUrlCaching` —Disable URL Caching

**•** `JailbrokenDevice` —Block Jailbroken Device

**•** `LogCertPin` —Log Certificate Pinning

**•** `LogEmail` —Log Email

**•** `LogPhonecall` —Log Phone Call

**•** `LogPolicyResult` —Log Security Policy Evaluation Result

**•** `LogScreenshot` —Log Screenshot

**•** `LogTextmessage` —Log SMS

**•** `LogoutAfterRestart` —Log Out User After Device Restart

**•** `LogoutOnBiometricChange` —Log Out User After Changing Biometric Login
Data

**•** `MalwareDetection` —Malware Detection

**•** `ManInMiddle` —Block Man In The Middle Attack

**•** `MaxOffline` —Maximum Days Offline Without Policy Refresh

**•** `MaximumAppVersion` —Maximum Application Version

**•** `MaximumOsVersion` —Maximum OS Version

**•** `MinimumAppVersion` —Minimum Application Version

**•** `MinimumOsVersion` —Minimum OS Version

**•** `MinimumSecurityPatchVersion` —Minimum Security Patch Version

**•** `PhonecallUriScheme` —Phone Call Application Handler

**•** `Screenshot` —Block Screenshot


### Standard Objects MobileSecurityUserMetric MobileSecurityUserMetric

Represents the metrics for users who have Enhanced Mobile Security policies enforced. This object is available in API version 51.0 and
later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Accessing this object requires the Enhanced Mobile App Security add-on subscriptions and the Enforce Enhanced Mobile App Security
user permission.

Fields

**Field** **Details**

```
MetricsDate

UserCount

```

Usage

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
The date the metrics were collected.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The number of users who have mobile security policies enforced.

A user with the Manage Enhanced Mobile App Security permission can run this SOQL query.

```
SELECT MetricsDate, UserCount

FROM MobileSecurityUserMetric

ORDER BY MetricsDate DESC

### MobileSettingsAssignment

```

Represents the assignment of a particular field service mobile settings configuration to a user profile. This object is available in API version
41.0 and later.


### Standard Objects MobSecurityCertPinConfig

Supported Calls

`create()`, `delete()`, `describeLayout()` —available in API version 51.0 and later, `describeSObjects()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field Name** **Details**

```
FieldServiceMobileSettingsId

ProfileId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of a set of field service mobile settings.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the profile to associate with the set of field service mobile settings.

### MobSecurityCertPinConfig

Configuration of mobile security certificate pinning on the Salesforce mobile app with Enhanced Mobile Security. This object is available
in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Accessing this object requires the Enhanced Mobile App Security add-on subscriptions and the Enforce Enhanced Mobile App Security
user permission.


Standard Objects MobSecurityCertPinConfig

Fields

**Field** **Details**

```
CertificateHash

DeveloperName

DomainName

IsEnabled

IsSubdomainIncluded

Language

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique identifier for the certificate.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the domain.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The default value is False.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The default value is False.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects MobSecurityCertPinConfig

**Field** **Details**

**Description**
The two-to five-character code that represents the language and locale ISO.

```
MasterLabel

MobilePlatform

MobileSecurityAssignmentId

NamespacePrefix

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The master label of the mobile security pin.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The mobile operating system.

Possible values are:

**•** `Android`

**•** `iOS`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the ID of the mobile security assignment.

This is a relationship field.

**Relationship Name**
MobileSecurityAssignment

**Relationship Type**
Lookup

**Refers To**
MobileSecurityAssignment

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can


### Standard Objects MobSecurityCertPinEvent

**Field** **Details**

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

```
SeverityLevel

Type

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The severity level of a mobile security policy.

Possible values are:

**•** `Critical`

**•** `Error`

**•** `Info`

**•** `Warn`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of pin

Possible values are:

**•** `AuthServer` —Authentication Server

**•** `Resource` —Resource

### MobSecurityCertPinEvent

The event of mobile security certificate pinning on the Salesforce mobile app with Enhanced Mobile Security. This object is available in
API version 53.0 and later.


Standard Objects MobSecurityCertPinEvent

Supported Calls

`create()`, `describeSObjects()`

Special Access Rules

Accessing this object requires the Enhanced Mobile App Security add-on subscriptions and the Enforce Enhanced Mobile App Security
user permission.

Fields

**Field** **Details**

```
AppPackageIdentifier

AppVersion

CertPinResults

DeviceIdentifier

DeviceModel

```

**Type**
string

**Properties**
Create

**Description**
The unique identifier for the certificate.

**Type**
string

**Properties**
Create

**Description**
The version of the app.

**Type**
json

**Properties**
Create

**Description**
The results of certificate pinning.

**Type**
string

**Properties**
Create

**Description**
The hardware IDs or IDs to uniquely identify a mobile device.

**Type**
string


Standard Objects MobSecurityCertPinEvent

**Field** **Details**

**Properties**
Create

**Description**
The model of the mobile device.

```
EventDate

EventDescription

EventIdentifier

EventUuid

OsName

OsVersion

```

**Type**
dateTime

**Properties**
Create, Nillable

**Description**
The date of the certificate pinning event.

**Type**
string

**Properties**
Create, Nillable

**Description**
The description of the certificate pinning event.

**Type**
string

**Properties**
Create, Nillable

**Description**
The ID of the certificate pinning event.

**Type**
string

**Properties**
Nillable

**Description**
The universally unique identifier of the event.

**Type**
string

**Properties**
Create

**Description**
The name of the operating system.

**Type**
string


### Standard Objects MsgChannelLanguageKeyword

**Field** **Details**

**Properties**
Create

**Description**
The version of the operating system.

```
ReplayId

UserId

WebkitVersion

```

**Type**
string

**Properties**
Nillable

**Description**
The position of the event in the event stream.

**Type**
reference

**Properties**
Create

**Description**
This is polymorphic relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

**Type**
string

**Properties**
Create, Nillable

**Description**
The version of the web browser engine developed by Apple.

### MsgChannelLanguageKeyword

Represents the consent configuration for a Messaging channel. This object is available in API version 48.0 and later.

Supported Calls

`describeSObjects()`, `delete()`, `query()`, `retrieve()`, `search()`


Standard Objects MsgChannelLanguageKeyword

Fields

**Field** **Details**

```
CustomKeywords

CustomResponse

DoubleOptInKeywords

HelpKeywords

HelpResponse

MasterLanguage

```

**Type**
textarea

**Properties**
Nillable

**Description**
The keywords a Messaging end user can send to receive the Custom Response.

**Type**
textarea

**Properties**
Nillable

**Description**
The automated response sent when a Messaging end user sends a Custom Keyword.

**Type**
textarea

**Properties**
Nillable

**Description**
The keywords a Messaging end user can send to doubly opt in to receiving messages.

**Type**
textarea

**Properties**
Nillable

**Description**
The keywords a Messaging end user can send to request help during a Messaging session.

**Type**
textarea

**Properties**
Nillable

**Description**
The automated response sent when a Messaging end user requests help.

**Type**
textarea


Standard Objects MsgChannelLanguageKeyword

**Field** **Details**

**Properties**

**Description**
The language used for this consent configuration.

```
MessagingChannelId

MessagingChannelUsageId

OptInConfirmation

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the associated Messaging channel.

This is a relationship field.

**Relationship Name**
MessagingChannel

**Relationship Type**
Lookup

**Refers To**
MessagingChannel

**Type**
reference

**Properties**
Filter, Group, Sort

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

**Type**
textarea

**Properties**
Nillable

**Description**
The automated response sent when a Messaging end user opts in to receiving messages.


### Standard Objects MsgChannelUsageExternalOrg

**Field** **Details**

```
OptInKeywords

OptOutConfirmation

OptOutKeywords

```

**Type**
textarea

**Properties**
Nillable

**Description**
The keywords a Messaging end user can send to explicitly opt in to receiving messages.

**Type**
textarea

**Properties**
Nillable

**Description**
The automated response sent when a Messaging end user opts out of receiving messages.

**Type**
textarea

**Properties**
Nillable

**Description**
The keywords a Messaging end user can send to opt out of receiving messages.

### MsgChannelUsageExternalOrg

Represents the Enterprise ID (EID) and Business Unit (MID) for Marketing Cloud connections in a Unified Messaging channel. This object
is available in API version 60.0 and later.

Supported Calls

`create()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ExternalOrgIdentifier

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The Enterprise ID (EID) of a Marketing Cloud connection.


### Standard Objects MyDomainDiscoverableLogin

**Field** **Details**

```
ExternalSubOrgIdentifier

MessagingChannelUsageId

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Business Unit (MID) of a Marketing Cloud connection.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The associated MessagingChannelUsage record, which must have a DeploymentType of `MJ`
(referring to Marketing Cloud Journey Builder).

This field is a relationship field.

**Relationship Name**
MessagingChannelUsage

**Relationship Type**
Lookup

**Refers To**
MessagingChannelUsage

MsgChannelUsageExternalOrg records apply only to MessagingChannelUsage records related to Marketing Cloud.

Only one MsgChannelUsageExternalOrg record can exist for each MessagingChannelUsage record with a DeploymentType of `MJ` .
MsgChannelUsageExternalOrg records are created when an admin enters the EID and MID for a Marketing Cloud application in Unified
Messaging Setup and then clicks **Connect** .

The data saved in a MsgChannelUsageExternalOrg record is used for making a connection to Marketing Cloud. If an admin disconnects
a Marketing Cloud application in Unified Messaging Setup, the saved EID and MID are used during deprovisioning.

### MyDomainDiscoverableLogin

Represents configuration settings when the My Domain login page type is Discovery. Login Discovery provides an identity-first login
experience, where the login page contains the identifier field only. Based on the identifier entered, a handler determines how to
authenticate the user. This object is available in API version 45.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects MyDomainDiscoverableLogin

Fields

**Field Name** **Details**

```
ApexHandlerId

DeveloperName

ExecuteApexHandlerAsId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The ID of the Apex handler that contains the Discovery authentication logic.

This is a relationship field.

**Relationship Name**
ApexHandler

**Relationship Type**
Lookup

**Refers To**
ApexClass

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

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The ID of the user who is executing the handler. Requires Manage User permission.

This is a relationship field.

**Relationship Name**
ExecuteApexHandlerAs


Standard Objects MyDomainDiscoverableLogin

**Field Name** **Details**

**Relationship Type**
Lookup

**Refers To**
User

```
Language

MasterLabel

UsernameLabel

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the `MasterLabel` .

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

**•** `th` (Thai)

**•** `zh_CN` (Chinese - Simplified)

**•** `zh_TW` (Chinese - Traditional)

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the action link group template.

**Type**
string


### Standard Objects MutingPermissionSet

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Login prompt on login page when the My Domain login page type is Discovery.
It supports localization with custom labels.

Usage

Use this object to access the My Domain Login Discovery Page, which is a login page type that prompts users to identity themselves
with an email address, phone number, or custom identifier. My Domain Login Discovery performs an interview-based login process,
where users are first prompted to provide identity and then authenticated. For example, users receive a verification code that they enter
to complete the login process.

### MutingPermissionSet

Represents a set of disabled permissions and is used in conjunction with PermissionSetGroup. This object is available in API version 46.0
and later.

Use a muting permission set with a permission set group to mute certain permissions. For instance, you have a subscriber org using a
managed package that contains a permission set group. To use the existing permission set group, the subscriber org can disable specific
permissions with a muting permission set. Or, perhaps you have a permission set group that contains several permission sets managed
by different departments. Use a muting permission set to disable specific permissions based on your organization's needs.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

As of Summer ’20 and later, only users who have one of these permissions can access this object:

**•** View Setup and Configuration

**•** Manage Session Permission Set Activations

**•** Assign Permission Sets

Fields

**Field Name** **Details**

```
DeveloperName

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects MutingPermissionSet

**Field Name** **Details**

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

Note: When creating large sets of data, always specify a unique DeveloperName for
each record. If no DeveloperName is specified, performance can slow while Salesforce
generates one for each record.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

```
Language

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the muting permission set.

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

**•** `th` (Thai)

**•** `zh_CN` (Chinese - Simplified)

**•** `zh_TW` (Chinese - Traditional)


### Standard Objects Name

**Field Name** **Details**

```
MasterLabel

Permissions PermissionName

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The muting permission set label for the aggregated, disabled permissions.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
One field for each permission. If `true`, the permission is disabled in the related permission
set group. The number of fields varies depending on the permissions for the organization
and license type.

To get a list of available permissions, use `describeSObjects()` .

Use MutingPermissionSet to disable specified permissions within a permission set group.

### Name

Non-queryable object that provides information about foreign key traversals when the foreign key has more than one parent.

This object is used to retrieve information from related records where the related record can be from more than one object type (a
polymorphic foreign key). For example, the owner of a case can be either a user or a group (queue). This object allows retrieval of the
owner name, whether the owner is a user or a group (queue). You can use a describe call to access the information about parents for
an object, or you can use the `who`, `what`, or `owner` fields (depending on the object) in SOQL queries. This object can’t be directly
accessed.

Supported Calls

```
describeSObjects()

```

Fields

**Field** **Details**

```
Alias

```

**Type**
string


Standard Objects Name

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user alias. This field contains a value only if the related record is a user.

```
Email

FirstName

IsActive

LastName

LastReferencedDate

```

**Type**
email

**Properties**
Filter, Group, Nillable, Sort

**Description**
The email address of the user or group (queue).

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The first name of the user, contact, or lead.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the related record is an active user ( `true` ) or not ( `false` ). This field
contains a value only if the related record is a user.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The last name of the user, contact, or lead.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last interacted with this record, directly or indirectly.
Some sample scenarios are:


Standard Objects Name

**Field** **Details**

```
LastViewedDate

MiddleName

Name

Phone

Profile

ProfileId

```

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it’s possible that the user only accessed this record or list view ( `LastReferencedDate` ),
but not viewed it.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The middle name of the user contact, or lead.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the parent of the object queried. If the parent is a user, contact, or lead, the
value is a concatenation of the `FirstName`, `MiddleName`, `LastName`, and `Suffix`
fields of the related record.

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
The phone number of the user. This field contains a value only if the related record is a user.

**Type**
reference

**Properties**
Filter, Nillable

**Description**
The Profile of the user. Only populated if the related record is a user.

**Type**
reference


Standard Objects Name

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the user’s Profile. Only populated if the related record is a user.

This field is a relationship field.

**Relationship Name**
Profile

**Relationship Type**
Lookup

**Refers To**
Profile

```
Suffix

Title

Type

Username

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name suffix of the user, contact, or lead.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The title of the user, for example CFO or CEO.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
A list of the types of sObject that can be an owner of this object. You can use this field to
filter on a type of owner, for example, return only the leads owned by a user.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects NamedCredential

**Field** **Details**

**Description**
Contains the name that a user enters to log into the API or the user interface. The value for
this field is in the form of an email address, and is only populated if the related record is a
user.

```
UserRole

 UserRoleId

```

Usage

**Type**
picklist

**Properties**
Filter, Nillable

**Description**
Name of the `Role` played by the user. Only populated for user rows.

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

To query on relationships where the parent can be more than one type of object, use `who`, `what`, or `owner` relationship fields.

SEE ALSO:

Overview of Salesforce Objects and Fields

### NamedCredential

Represents a named credential, which specifies the URL of a callout endpoint and its required authentication parameters in one definition.
A named credential can be specified as an endpoint to simplify the setup of authenticated callouts. This object is available in API version
33.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.


Standard Objects NamedCredential

Note: All credentials stored within this entity are encrypted under a framework that is consistent with other encryption frameworks
on the platform. Salesforce encrypts your credentials by auto-creating org-specific keys. Credentials encrypted using the previous
encryption scheme have been migrated to the new framework.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

As of Spring ’20 and later, only users with the View Setup and Configuration permission can access this object.

Fields

**Field Name** **Details**

```
AuthProviderId

AuthTokenEndpointUrl

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

Salesforce ID of the authentication provider, which defines the
service that provides the login process and approves access
to the external system.

Only users with the “Customize Application” and “Manage
AuthProviders” permissions can view this field.

This field is a relationship field.

This field is only valid for legacy named credentials.

This field was first available in API version 39.0, this field is
deprecated in API version 56.0.

**Relationship Name**
AuthProvider

**Relationship Type**
Lookup

**Refers To**
AuthProvider

**Type**
textarea

**Properties**
Nillable


Standard Objects NamedCredential

**Field Name** **Details**

**Description**
The URL where SON Web Tokens (JWTs) are exchanged for
access tokens.

This field is only valid for legacy named credentials.

This field was first available in API version 46.0, this field is
deprecated in API version 56.0.

```
CalloutOptionsAllowMergeFieldsInBody

CalloutOptionsAllowMergeFieldsInHeader

CalloutOptionsGenerateAuthorizationHeader

DeveloperName

```

**Type**
boolean

**Properties**
Filter

**Description**
For Apex callouts, indicates whether the code can use merge
fields to populate HTTP request bodies with org data.

This field is available in API version 35.0 and later.

**Type**
boolean

**Properties**
Filter

**Description**
For Apex callouts, indicates whether the code can use merge
fields to populate HTTP headers with org data.

This field is available in API version 35.0 and later.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether Salesforce automatically generates a
standard authorization header for each callout to the named
credential–defined endpoint.

This field is available in API version 35.0 and later.

**Type**
string

**Properties**
Filter, Group, Sort


Standard Objects NamedCredential

**Field Name** **Details**

**Description**
The unique name of the object in the API. This name can
contain only underscores and alphanumeric characters, and
must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain
two consecutive underscores. In managed packages, this field
prevents naming conflicts on package installations. With this
field, a developer can change the object’s name in a managed
package and the changes are reflected in a subscriber’s
organization.

Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this
field.

```
Endpoint

JwtAudience

JwtFormulaSubject

```

**Type**
textarea

**Properties**
Nillable

**Description**
The root URL of the endpoint.

This field is only valid for legacy named credentials.

This field is deprecated in API version 56.0.

**Type**
textarea

**Properties**
Nillable

**Description**
External service or other allowed recipients for the JSON Web
Token. Written as JSON, with a quoted string for a single
audience and an array of quoted strings for multiple audiences.
Single audience example: `“aud1”` . Multiple audiences
example: `[”aud1”, “aud2”, “aud3”]` .

This field is only valid for legacy named credentials.

This field was first available in API version 46.0, this field is
deprecated in API version 56.0.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects NamedCredential

**Field Name** **Details**

**Description**
Formula string calculating the JSON Web Token’s subject. API
names and constant strings, in single quotes, can be included.
Allows a dynamic Subject unique per user requesting the token.
For example, `'User='+$User.Id` . Use this field when
`PrincipalType` is set to `PerUser` . Corresponds to Per
User Subject in the user interface.

This field is only valid for legacy named credentials.

This field was first available in API version 46.0, this field is
deprecated in API version 56.0.

```
JwtIssuer

JwtTextSubject

JwtValidityPeriodSeconds

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Specify who issued the JSON Web Token using a case-sensitive
string.

This field is only valid for legacy named credentials.

This field was first available in API version 46.0, this field is
deprecated in API version 56.0.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Static text, without quotes, that specifies the JSON Web Token
subject. Use this field when `PrincipalType` is set to
`NamedUser` . Corresponds to Named Principal Subject in the
user interface.

This field is only valid for legacy named credentials.

This field was first available in API version 46.0, this field is
deprecated in API version 56.0.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of seconds that the JSON Web Token is valid.

This field is only valid for legacy named credentials.


Standard Objects NamedCredential

**Field Name** **Details**

This field was first available in API version 46.0, this field is
deprecated in API version 56.0.

```
Language

MasterLabel

NamespacePrefix

PrincipalType

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language of the `MasterLabel` .

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The label for the named credential. This display value is the
internal label that doesn’t get translated.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each
Developer Edition org that creates a managed package has a
unique namespace prefix. Limit: 15 characters. You can refer
to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Tracks users who are accessing the external system.
`Anonymous` implies that a user identity isn’t specified for
external system access. `Named Principal` uses one user
identity for all users to access the external system.

This field is only valid for legacy named credentials.

This field is deprecated in API version 56.0.


### Standard Objects NamedCredentialEventLog

Usage

Use the NamedCredential object to query named credentials in your organization.

Note: Some named credential fields rely on per-user authentication to connect with an external system. If an admin edits one of
these fields, then the previously authenticated credentials can get invalidated, requiring individual users to reauthenticate.

SEE ALSO:

ExternalDataUserAuth

ExternalDataSource

_Salesforce Help_ [: Named Credentials](https://help.salesforce.com/s/articleView?id=xcloud.named_credentials_about.htm&type=5&language=en_US)

_Named Credentials Developer Guide_ [: Get Started with Named Credentials](https://developer.salesforce.com/docs/platform/named-credentials/guide/get-started.html)

_[Named Credentials Developer Guide](https://developer.salesforce.com/docs/platform/named-credentials/references/named-credentials-reference/nc-api-links.html)_ : Named Credential API Links

_Apex Developer Guide_ [: Invoking Callouts Using Apex](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_callouts.htm)

_Apex Developer Guide_ [: Named Credentials as Callout Endpoints](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_callouts_named_credentials.htm)

### NamedCredentialEventLog

The Named Credential event type captures information about Apex callouts that use named credentials as their endpoints. Use this
event type to audit the installed managed packages that use named credentials. If you don’t recognize the package namespace in the
named credential event log file, then you can investigate whether a security breach has occurred. This object is available in API version
65.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
BotIdentifier

BotSessionIdentifier

```

**Type**
String

**Description**
The ID of the bot.

**Type**
String

**Description**
The bot session ID.


Standard Objects NamedCredentialEventLog

**Field** **Details**

```
CallerPackageNamespace

ClientIp

CpuTime

LoginKey

NamedCredentialName

PlannerIdentifier

```

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
If an Apex callout using a Named Credential endpoint is initiated from a package, then this
field contains the package’s namespace. If the callout isn’t initiated from a package, then
this field is empty.

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the client that is using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”.

**Type**
Double

**Properties**
Filter, Nillable, Sort

**Description**
The CPU time in milliseconds used to complete the request. This field indicates the amount
of activity taking place in the app server layer.

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring.

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the named credential that’s the endpoint of the Apex callout.

**Type**
String


Standard Objects NamedCredentialEventLog

**Field** **Details**

**Description**
The ID of the agent planner.

```
RequestIdentifier

RunTime

SessionKey

Timestamp

Uri

UserIdentifier

```

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same REQUEST_ID.

**Type**
Double

**Properties**
Filter, Nillable, Sort

**Description**
The amount of time that the request took in milliseconds..

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started.

**Type**
DateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT.

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URI of the page that’s receiving the request.

**Type**
String


### Standard Objects NamespaceRegistry

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user who is using Salesforce services through the UI or the API.

### NamespaceRegistry

Represents a namespace that you can link to scratch orgs that were created from your org’s Dev Hub. You use the namespace when
developing, packaging, and releasing an app. You can’t create this object with the API. Use the **Link Namespace** action in the Dev Hub
### graphical interface to insert a NamespaceRegistry record. This object is available in API version 41.0 and later.

Supported Calls

`delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,

```
   update()

```

Fields

**Field Name** **Details**

### `Name`

```
NamespaceOrg

NamespacePrefix

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
The name of this namespace registry entry.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The org ID of the Developer Edition org where you've registered the namespace
you want to link.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The namespace prefix that you want to link to the scratch org.


### Standard Objects NavigationLinkSet

Associated Objects

This object has these associated objects. Unless noted, they’re available in the same API version as this object.

**NamespaceRegistryFeed**

Feed tracking is available for the object.

**NamespaceRegistryHistory**

History is available for tracked fields of the object.

SEE ALSO:

ActiveScratchOrg

ScratchOrgInfo

### NavigationLinkSet

Represents the navigation menu in an Experience Cloud site. A navigation menu consists of items that users can click to go to other
parts of the site. This object is available in API version 35.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

`create()`, `delete()`, `update()`, and `upsert()` are available in API version 45.0 and later.

Special Access Rules

Navigation menus are available only in Experience Cloud sites created using Experience Builder templates. To use navigation menus in
LWR templates, you must build a custom navigation menu component.

Fields

**Field Name** **Details**

```
DeveloperName

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

Create and Update are available in API version 45.0 and later.

**Description**
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with
a letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. In managed packages, this field prevents naming
conflicts on package installations. With this field, a developer can change the
object’s name in a managed package and the changes are reflected in a
subscriber’s organization.


Standard Objects NavigationLinkSet

**Field Name** **Details**

```
Language

MasterLabel

NetworkId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

Create, Defaulted on create, Nillable, and Update are available in API version 45.0
and later.

**Description**
Language for the navigation menu. Valid values are:

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

**•** Thai: `th` The Salesforce user interface is fully translated to Thai, but Help is
in English.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

Create and Update are available in API version 45.0 and later.

**Description**

Label for the navigation menu.

**Type**
reference


### Standard Objects NavigationMenuItem

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort

Create is available in API version 45.0 and later. Update is available in API versions
45.0 to 47.0.

**Description**
ID of the Experience Cloud site.

### NavigationMenuItem

Represents a single menu item in a NavigationLinkSet. Use this object to create, delete, or update menu items in your Experience Cloud
site’s navigation menu. This object is available in API version 35.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Navigation menus are available only in Experience Cloud sites created using Experience Builder templates. To use navigation menus in
LWR templates, you must build a custom navigation menu component.

Fields

**Field Name** **Details**

```
AccessRestriction

DefaultListViewId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Determines if the menu item is available to guest users who aren’t required to
log in to the Experience Cloud site.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If the value of the `Type` field is SalesforceObject, the value is the ID of the default
list view for the object.


Standard Objects NavigationMenuItem

**Field Name** **Details**

```
DraftRowID

Label

NavigationLinkSetId

ParentId

Position

Status

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the draft navigation menu item. The ID is unique within your
organization.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The text that appears in the navigation menu for this item.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The navigation menu that this item is included in.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The parent navigation menu.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The location of the menu item in the navigation menu.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort


Standard Objects NavigationMenuItem

**Field Name** **Details**

**Description**
Represents if the navigation menu item is published or not. The values can only
be DRAFT, LIVE, or null. In API versions 42 and earlier, if the Status field is not set,
the field defaults to LIVE. When queried and Status is not part of the query filter,
only the NavigationMenuItem objects with a status of LIVE return. In API versions
43 and later, if the Status field is not set, the field defaults to DRAFT. When queried
and Status is not part of the query filter, all NavigationMenuItem objects return
regardless of status.

```
Target

TargetPrefs

Type

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
If `Type` is ExternalLink or InternalLink, the target is the URL that the link points
to. For ExternalLink, your entry looks like this: _`https://salesforce.com`_ .
For InternalLink, use a relative URL, such as _`/contactsupport`_ .

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
If `Type` is ExternalLink, determines whether a navigation menu item opens in
the same tab.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of navigation menu item. The available values are:

**•** SalesforceObject—Available objects include accounts, cases, contacts, and
custom objects.

**•** ExternalLink—Links to a URL outside of your Experience Cloud site. For
example, _`https://salesforce.com`_ .

**•** Event—An event, such as logging in, logging out, or switching accounts.
Event is internal only and can’t be used in custom components.

**•** GlobalAction—Enables users to create object records, but the new record
has no relationship with other records.

**•** InternalLink—Links to a relative URL inside your Experience Cloud site. For
example, _`/contactsupport`_ .


### Standard Objects NavigationMenuItemLocalization

**Field Name** **Details**

**•** NavigationalTopic—A dropdown list with links to the navigational topics in
your Experience Cloud site.

**•** SystemLink—A system link, such as a link to Experience Builder, Workspaces,
or Salesforce setup.

Usage

You can add up to 20 navigation menu items. You can translate navigation menu items using the Translation Workbench.

### NavigationMenuItemLocalization

Represents the translated value of a navigation menu item in an Experience Cloud site. This object is available in API version 36.0 and
later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Special Access Rules

Navigation menus are available only in Experience Cloud sites created using Experience Builder templates. To use navigation menus in
LWR templates, you must build a custom navigation menu component.

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

The language of the translated navigation menu item. The picklist contains the
following supported languages:

**•** Chinese (Simplified): `zh_CN`

**•** Chinese (Traditional): `zh_TW`

**•** Danish: `da`

**•** Dutch: `nl_NL`

**•** English: `en_US`

**•** Finnish: `fi`


Standard Objects NavigationMenuItemLocalization

**Field Name** **Details**

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

**•** Thai: `th` The Salesforce user interface is fully translated to Thai, but Help is
in English.

```
NamespacePrefix

ParentId

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
The ID of the navigation menu item that this translated value applies to.


### Standard Objects Network

**Field Name** **Details**

```
Value

### Network

```

**Type**
string

**Properties**
Create, Filter, Sort, Update

**Description**
The translated text for the navigation menu item. Label is **Translation Text** .

Represents an Experience Cloud site. Salesforce Experience Cloud lets you create branded spaces for your employees, customers, and
partners. You can customize and create experiences, whether they’re communities, sites, or portals, to meet your business needs, then
transition seamlessly between them. Experience Cloud sites let you share information, records, and files with coworkers and stakeholders
all in one place. This object is available in API version 26.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`, `update()`

Special Access Rules

This object is available only when your org has digital experiences enabled.

Fields

**Field Name** **Details**

```
AllowedExtensions

CaseCommentEmailTemplateId

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort, Update

**Description**
Specifies the types of files allowed in your site. This list of file types lets you control
what members upload and also prevents spammers from polluting your site with
inappropriate files. Available in API version 36.0 and later.

Separate file types with a comma (for example: _`jpg,docx,txt`_ ). You can
enter lowercase and uppercase letters. You can enter up to 1,000 characters. To
allow all file types, leave this field empty.

**Type**
reference


Standard Objects Network

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
ID of the email template used when submitting a comment on a case. This field
is available in API version 28.0 and later.

```
ChangePasswordEmailTemplateId

ChgEmailVerNewEmailTemplateId

ChgEmailVerOldEmailTemplateId

Description

DeviceActEmailTemplateId

```

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
ID of the email template used when notifying users that their password has been
reset.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
ID of the email template used when notifying users that their email address has
been changed. This email is sent to the user’s new email address.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
ID of the email template used when notifying users that their email address has
been changed. This email is sent to the user’s old email address.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Description of the site.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update


Standard Objects Network

**Field Name** **Details**

**Description**
ID of the email template used when users log in from an unrecognized browser,
app, or IP address. The email contains a one-time password that users enter to
verify their identity.

This field is available in API version 53.0 and later.

```
EmailFooterLogoId

EmailFooterText

EmailSenderAddress

EmailSenderName

enableImageOptimizationCDN

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
ID of the Document object that displays as an image in the footer of Chatter
emails.

**Type**
string

**Properties**
Filter, Nillable, Sort, Update

**Description**
Text that displays in the footer of Chatter emails.

**Type**
email

**Properties**
Filter, Group, Sort

**Description**
Read only. Email address from which emails are sent.

Note: To change the `EmailSenderAddress` value, you must first
specify `NewSenderAddress`, which triggers the sending of an address
change verification email. After you complete the address verification
process, `EmailSenderAddress` changes to the specified
`NewSenderAddress` .

**Type**
string

**Properties**
Filter, Group, Sort, Update

**Description**
Name from which emails are sent.

**Type**
boolean


Standard Objects Network

**Field Name** **Details**

**Properties**
Filter, Update

**Description**
The setting that optimizes cached images for guest users on all devices when a
site uses Salesforce’s CDN for Digital Experiences.

This field is available in API version 56.0 and later.

```
FirstActivationDate

ForgotPasswordEmailTemplateId

HeadlessForgotPasswordTemplateId

HeadlessRegistrationTemplateId

```

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date the site was first activated.

This field is available in API version 34.0 and later. If the site was activated or
inactive before the release of API version 34.0, this field returns the date that the
site was first created.

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
ID of the email template used when users forget their password.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
ID of the email template to use with the Headless Forgot Password Flow.

This field is available in API version 57.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
ID of the email template to use for identity verification during the Headless
Registration Flow.

This field is available in API version 59.0 and later.


Standard Objects Network

**Field Name** **Details**

```
LockoutEmailTemplateId

MaxFileSizeKb

Name

NewSenderAddress

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
ID of the email template used when users try to reset their password after locking
themselves out because of too many login attempts.

This field is available in API version 43.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Specifies the maximum file size (in KBs) that members can upload in your site.
Available in API version 36.0 and later.

Enter a number between 3072 KB and your org’s maximum file size. To use the
default limit of 2 GB, leave this field empty.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort, Update

**Description**
The name of the site.

**Type**
email

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Email address that has been entered as the new value for
`EmailSenderAddress` but hasn’t been verified yet. After a user has
requested to change the sender email address and has successfully responded
to the verification email, the `NewSenderAddress` value overwrites the value
in `EmailSenderAddress` . This value becomes the email address from which
emails are sent.

Note:

**•** If verification is pending for a new email address and you set
`NewSenderAddress` to null, the verification request is canceled.


Standard Objects Network

**Field Name** **Details**

**•** `NewSenderAddress` is automatically set to null after
`EmailSenderAddress` has been set to the new verified address.

**•** If verification is pending for a new email address, and you specify a
different new address for this field, only the latest value is retained
and used for verification.

```
OptionsActionOverrideEnabled

OptionsAllowInternalUserLogin

OptionsAllowMembersToFlag

OptionsApexCDNCachingEnabled

```

**Type**
boolean

**Properties**
Filter, Update

**Description**
Override the action that occurs when users click a default button, like New or
Edit, with a Lightning component. For example, show a custom window instead
of the one that Salesforce provides. Assign action overrides in the Object Manager.
In the UI, this setting is available in the Administration Workspace, under
**Administration**  - **Preferences** under Experience Management

This field is available in API version 49.0 and later.

**Type**
boolean

**Properties**
Filter, Update

**Description**
Specifies whether internal users can log in with their internal credentials on the
site login page.

This field is available in API version 37.0 and later.

**Type**
boolean

**Properties**
Filter, Update

**Description**
Determines whether users can flag posts, comments, or files as inappropriate.

This field is available in API version 29.0 and later. The ability to flag files is available
in version 30.0 and later.

**Type**
boolean

**Properties**
Filter, Update


Standard Objects Network

**Field Name** **Details**

**Description**
Determines whether public data from @wire calls to Apex methods is cached
only for guest users. This setting applies only to sites using Salesforce's CDN for
Digital Experiences.

This field is available in API version 55.0 and later.

```
OptionsDirectMessagesEnabled

OptionsEmbeddedLoginEnabled

OptionsEnableTalkingAboutStats

OptionsEnableTopicAssignmentRules

```

**Type**
boolean

**Properties**
Filter, Update

**Description**
Controls the availability of direct messages in an Experience Builder site.

This field is available in API version 39.0 and later.

**Type**
boolean

**Properties**
Filter, Update

**Description**
Determines whether the Embedded Login feature is enabled in a site. When
`true`, Embedded Login is turned on.

This field is available in API version 61.0 and later.

**Type**
boolean

**Properties**
Filter, Update

**Description**
Determines whether site users see how many people are discussing a topic. The
number of people discussing the topic appears as the user types the topic and
the system gives topic suggestions.

This field is available in API version 41.0 and later.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When true, displays knowledgeable people in key areas, for example, on Topic
Detail pages.


Standard Objects Network

**Field Name** **Details**

```
OptionsExpFriendlyUrlsAsDefault

OptionsExperienceBundleBasedSnaOverrideEnabled

OptionsGatherCustomerSentimentData

OptionsGuestChatterEnabled

OptionsGuestFileAccessEnabled

```

**Type**
boolean

**Properties**
Filter, Update

**Description**
When true, URL slugs are on by default for

**•** Product and Category pages of LWR Commerce stores (available in API version
58.0 and later)

**•** Custom object pages on enhanced LWR sites (available in API version 60.0
and later)

**•** Account and contact pages on enhanced LWR sites (available in API version
61.0 and later)

**Type**
boolean

**Properties**
Filter, Update

**Description**
When true, the Service Not Available Page is an auto-generated Experience
Builder-based page. When false, the Service Not Available page uses a static
resource page that is set in **Workspaces**   - **Administration**   - **Pages** . The default
value is true. Available in API version 52.0 and later.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When true, collects data about user likes, upvotes, and downvotes.

**Type**
boolean

**Properties**
Filter, Update

**Description**
Specifies whether guest users can access public Chatter groups in the site without
logging in.

**Type**
boolean

**Properties**
Filter, Update


Standard Objects Network

**Field Name** **Details**

**Description**
When true, lets guest users view asset files and CMS content that’s available to
the site. Guest users can access shared asset files and published CMS content
that’s made for external use, even if it isn’t used. Shared asset files include images
that are associated with topics, recognition badges, branding, and account
branding. This preference is automatically enabled if public access is enabled at
the page or site level in Experience Builder.

```
OptionsGuestMemberVisibility

OptionsHeadlessFrgtPswEnabled

OptionsImageOptimizationCDNEnabled

OptionsInvitationsEnabled

```

**Type**
boolean

**Properties**
Filter, Update

**Description**
When true, lets guest users see who else is part of the site, including non-guest
users. In the UI, this setting appears in the Administration Workspace under
**Administration**  - **Preferences** .

Available in API version 47.0 and later.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `true`, Headless Forgot Password Flow is enabled.

This field is available in API version 57.0 and later.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `true`, cached images are optimized to suit any device that guest users
use to access your site. This feature is available only for sites that use Salesforce’s
CDN for Digital Experiences. In the UI, this setting appears in the Administration
Workspace under **Administration**   - **Preferences** .

Available in API version 56.0 and later.

**Type**
boolean

**Properties**
Filter, Update


Standard Objects Network

**Field Name** **Details**

**Description**
Determines whether users can invite others to the site.

```
OptionsKnowledgeableEnabled

OptionsLWRExperienceConnectedAppEnabled

OptionsMemberVisibility

OptionsMobileImageOptimizationEnabled

OptionsNetworkSentimentAnalysis

```

**Type**
boolean

**Properties**
Filter, Update

**Description**
Determines whether users can see knowledgeable people for topics and endorse
people for topics.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When true, enhances the performance and scalability of Connect API calls made
from Lightning web components in an enhanced LWR site. This field is available
in API version 58.0 and later.

Note: This feature is a Beta Service. Customer may opt to try such Beta
Service in its sole discretion. Any use of the Beta Service is subject to the
[applicable Beta Services Terms provided at Agreements and Terms.](https://www.salesforce.com/company/legal/agreements/)

**Type**
boolean

**Properties**
Filter, Update

**Description**
Controls user visibility on a per-site basis. If true, the See other members of this
site preference is enabled for the selected site. This field is available in API version
45.0 and later.

**Type**
boolean

**Properties**
Filter, Update

**Description**
If true, file asset images are optimized for mobile display. This field is available in
API version 45.0 and later.

**Type**
boolean


Standard Objects Network

**Field Name** **Details**

**Properties**
Filter, Update

**Description**
If true, enables sentiment analysis in a site. In the UI, this setting is available in
the Administration Workspace, under **Administration**                              - **Preferences** . This field
is available in API version 40.0 and later.

```
OptionsNicknameDisplayEnabled

OptionsPrivateMessagesEnabled

OptionsProfileBasedLayoutsForKnowledgeSearchEnabled

```

**Type**
boolean

**Properties**
Filter, Update

**Description**
Determines whether user nicknames display instead of their first and last names
in most places in the site.

A few restrictions to keep in mind about nickname display:

**•** Records and user lookups on records show full names. Keep in mind, though,
that you can control record and user visibility with sharing rules.

**•** Mobile notifications in the Salesforce mobile app show full names. You can
turn off mobile notifications in the app to avoid this display.

**•** Searches by first, last, and full names aren’t restricted and return matches,
but the search results display only nicknames. Global search auto-complete
recommendations show any first, last, and full names that the user has
searched by or accessed via a record or another location. The recent items
list also shows first, last, and full under the same conditions.

**Type**
boolean

**Properties**
Filter, Update

**Description**
Determines whether users can send and receive Chatter messages in the site.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When true, provides a grid layout for Knowledge search results. With grid layout
in place, you can edit search profile layouts on the Knowledge object to show
and hide different search result fields for different profiles. When you enable the
standard grid layout, search-term highlighting isn’t available. This field is available
in API version 51.0 and later.


Standard Objects Network

**Field Name** **Details**

```
OptionsRecognitionBadgingEnabled

OptionsReputationEnabled

OptionsReputationRecordConversationsDisabled

OptionsSelfRegistrationEnabled

OptionsSendWelcomeEmail

```

**Type**
boolean

**Properties**
Filter, Update

**Description**
Determines whether Recognition Badges is enabled for the site.

**Type**
boolean

**Properties**
Filter, Update

**Description**
Determines if reputation is calculated and displayed for members. This field is
available in API version 31.0 and later.

**Type**
boolean

**Properties**
Filter, Update

**Description**
Disables the feed on reputation records.

**Type**
boolean

**Properties**
Filter, Update

**Description**
Determines whether customers and partners can self-register to join the site.
Customers and partners are users with External Identity, Community, Customer
Portal, or partner portal licenses. If `true`, displays a **Not a member?** link on the
login page that points to the default self-registration page. This field is available
in API version 28.0 and later.

**Type**
boolean

**Properties**
Filter, Update

**Description**
Determines whether a welcome email is sent when a new user is added to the
site.


Standard Objects Network

**Field Name** **Details**

```
OptionsShowAllNetworkSettings

OptionsSiteAsContainerEnabled

OptionsThreadedDiscussionsEnabled

OptionsTopicFilteringForKnowledgeSearchEnabled

OptionsTopicSuggestionsEnabled

```

**Type**
boolean

**Properties**
Filter, Update

**Description**
Determines whether settings in Experience Management that were hidden based
on how you set up your site are visible or remain hidden.

This field is available in API version 33.0 and later.

**Type**
boolean

**Properties**
Filter, Update

**Description**
Determines whether the site is an Experience Builder site ( `true` ) or a Salesforce
Tabs + Visualforce site ( `false` ).

This field is available in API version 29.0 and later.

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether threaded discussions are enabled for the site. Available in API
version 44.0 and later.

**Type**
boolean

**Properties**
Filter, Update

**Description**
Determines whether topic filtering is enabled for Knowledge search.

This field is available in API version 55.0 and later.

**Type**
boolean

**Properties**
Filter, Update

**Description**
Enables topic suggestions when users write posts.

This field is available in API version 41.0 and later.


Standard Objects Network

**Field Name** **Details**

```
OptionsUpDownVoteEnabled

PwdlessRegEmailTemplateId

SelfRegMicroBatchSubErrorEmailTemplateId

SelfRegProfileId

Status

```

**Type**
boolean

**Properties**
Filter, Update

**Description**
Determines whether up and down voting is enabled for the site.

This field is available in API version 41.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
ID of the email template for the welcome email that users receive when they
sign up with passwordless registration. This field is available in API version 61.0
and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
ID of the profile assigned to users who self-register using micro-batchng. Only
applies if self-registration using micro-batching is enabled for the site.

This field is available in API version 54.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
ID of the profile assigned to users who self-register. Only applies if self-registration
is enabled for the site.

This field is available in API version 29.0 and later.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Status of the site. Available values are:


Standard Objects Network

**Field Name** **Details**

**•** `Live` —The site is online and members can access it. Label is `Published` .

**•** `DownForMaintenance` —The site was previously published, but was
taken offline. Members with the Create and Set Up Experiences permission
can still access the setup for offline sites regardless of profile or membership.
Members aren’t able to access offline sites, but they still appear in the user
interface dropdown menu as `SiteName (Offline)` . Label is
`Offline` .

**•** `UnderConstruction` —The site hasn’t yet been published. When a
user’s profile is associated with the site, and they’ve Create and Set Up
Experiences permission, they can access sites in this status.

After a site is published, it can never be in this status again. Label is `Preview` .

```
UrlPathPrefix

VerificationEmailTemplateId

WelcomeEmailTemplateId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The UrlPathPrefix is a unique string at the end of the URL for the site. For example,
in the site URL _`MyDomainName`_ `.my.site.com/customers`,
`customers` is the `UrlPathPrefix` .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
ID of the email template used when users must verify their identity, for example,
when they log in without a password.

This field is available in API version 44.0 and later.

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
ID of the email template used when sending welcome emails to new members.


### Standard Objects NetworkActivityAudit

Usage

Use this object to find, view, and update sites in your org. If you’re assigned the Modify All Data, View All Data, or Create and Set Up
Experiences permission, you can view all sites in the org. Users without these permissions see only the Preview or Published sites that
they’re members of. If you’re assigned the Create and Set Up Experiences permission, you can customize site settings.

SEE ALSO:

WebStoreNetwork

### NetworkActivityAudit

Represents an audit trail of moderation actions in Experience Cloud sites. This object is available in API version 30.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available only when your org has digital experiences enabled.

Fields

**Field Name** **Details**

```
Action

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The moderation action a member performed on a post, comment, or file in an
Experience Cloud site.

Values are:

**•** Flagged as Inappropriate—A member flagged a post, comment, or file as
inappropriate.

**•** Flagged as Spam - A member flagged a post, comment, or file as spam.

**•** Unflagged—A member removed the flag from a post, comment, or file.

**•** RemovedFlags—A moderator removed all flags from a post, comment, or
file.

**•** DeletedFlaggedItem—A moderator deleted a flagged post, comment,
message, or file.


Standard Objects NetworkActivityAudit

**Field Name** **Details**

**•** DeletedPendingReviewItem—A moderator deleted a post or comment with
pending status.

**•** ModerationRuleFlag—A moderation rule flagged member-generated content.

**•** ModerationRuleBlock—A moderation rule blocked member-generated
content.

**•** ModerationRuleReplace—A moderation rule replaced member-generated
content.

**•** ModerationRuleReview—A moderation rule sent member-generated content
to be reviewed and approved by a moderator.

**•** ModerationRuleFreeze—A moderation rule froze a member because they
created content too frequently within a specific time frame.

**•** ModerationRuleNotify—A moderation rule notified moderators because a
member created content too frequently within a specific time frame.

```
Description

EntityCreatedById

EntityId

EntityType

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Notes entered by the user.

If the entity being tracked is a file, records the version number of the file when
it was flagged.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the user that created the entity being tracked.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the entity that is being tracked. The following entities are tracked:
ChatterMessage, ContentDocument, ContentVersion, FeedComment, and
FeedItem.

**Type**
picklist


Standard Objects NetworkActivityAudit

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The key prefix of the entity being tracked.

```
Name

NetworkId

ParentEntityId

ParentEntityType

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the item being tracked.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Experience Cloud site where the moderation action was performed.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the parent of the entity on which an action was performed.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The key prefix of the parent of the entity being audited.

Use this object to view an audit trail of moderation activity for your Experience Cloud sites. You must have the Modify All Data permission
to access this object.

Users with Moderate Experiences Feeds, Moderate Experiences Files, or View All Data can view the audit trail using reports in the Salesforce
user interface.


### Standard Objects NetworkAffinity NetworkAffinity

Represents a junction object that associates a user profile with a Network object, that is, with an Experience Cloud site. Use NetworkAffinity
to assign a default Experience Cloud site to a user profile. This object is available in API version 41.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To work with the NetworkAffinity object, you must have View Setup or Customize Application permission.

Fields

**Field Name** **Details**

```
NetworkId

ProfileId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the default Experience Cloud site associated with a user profile.

**Type**
reference

**Properties**
CreateFilter, Group, Sort, Update

**Description**
ID of the user profile the default Experience Cloud site is assigned to.

The default Experience Cloud site allows you to stamp site-agnostic email notifications to all users with that profile with the selected
site's branding. The default Experience Cloud site also becomes the target destination for email notification links. Site-agnostic email
notifications include notifications about records, such as cases, accounts, and opportunities.

The `NetworkId` field is not updatable through the Apex, REST API, or SOAP API. If you want to change the value for `NetworkId`,
you must delete the record and create one with the right value.

### NetworkAuthApiSettings

Represents the settings that control enablement, access, and security for the Headless Registration Flow, Headless Forgot Password
Flow, Headless Passwordless Login Flow, and their associated APIs. This object is available in API version 58.0 and later.


Standard Objects NetworkAuthApiSettings

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Headless identity features are set up via Experience Cloud sites. You must have an Experience Cloud site to access Headless Identity APIs
and store users, even if users never interact with the site directly.

Fields

**Field** **Details**

```
CustomOtpDeliveryHandlerId

DoesForgotPasswordRequireAuth

DoesPasswordLoginRequireAuth

DoesPwdlessLoginRequireAuth

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
This field is a relationship field.

The ID of a custom one-time password (OTP) delivery handler that implements the
`Auth.CustomOneTimePasswordDeliveryHandler` interface.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether authentication is required to access Headless Forgot Password API
when a password reset is requested. If `true`, an access token issued to an internal integration
user in your initial POST request to the
`/services/auth/headless/forgot_password` endpoint is required. The
access token must include the `forgot_password` scope.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether reCAPTCHA is required for headless username-password login that uses
the OAuth 2.0 for First-Party Applications draft protocol.

**Type**
boolean


Standard Objects NetworkAuthApiSettings

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether authentication is required to access Headless Passwordless Login API
when user information is submitted to Salesforce. If `true`, an access token issued to an
internal integration user is required in your initial POST request to the
`/services/auth/headless/init/passwordless/login` endpoint. The
access token must include the `pwdless_login_api` scope.

The default value is `false` . This field is available in API version 59.0 and later.

```
DoesRegistrationRequireAuth

HeadlessDiscoveryExecutionUserId

HeadlessDiscoveryHandlerId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether authentication is required to access Headless Registration API when
user registration information is submitted to Salesforce. If `true`, an access token issued to
an internal integration user in your initial POST request to the
`/services/auth/headless/init/registration` endpoint is required. The
access token must include the `user_registration_api` scope.

The default value is `false` .

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
This field is a relationship field.

The ID of an integration user account to run a headless user discovery Apex handler.

**Relationship Name**
HeadlessDiscoveryExecutionUser

**Refers To**
User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
This field is a relationship field.

The ID of an Apex class that implements the
`Auth.HeadlessUserDiscoveryHandler` interface.


Standard Objects NetworkAuthApiSettings

**Field** **Details**

**Relationship Name**
HeadlessDiscoveryHandler

**Refers To**
ApexClass

```
isFirstPartyAppsAllowed

IsForgotPwdAllowed

IsForgotPwdEmailTemplateAllowlistingEnabled

IsHeadlessUserRegistrationAllowed

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether the Experience Cloud site can use headless identity flows that use the
OAuth 2.0 for First-Party Applications draft protocol.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether the Headless Forgot Password Flow is enabled.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Descriptions**
Determines whether email template allowlisting is enabled for the Headless Registration
Flow, Headless Passwordless Login Flow, and Headless Forgot Password Flow. If `true`, the
initial request to the headless API must include an `emailtemplate` parameter that
contains only allowlisted email templates.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether the Headless Registration Flow is enabled.

The default value is `false` .


Standard Objects NetworkAuthApiSettings

**Field** **Details**

```
IsPwdlessLoginAllowed

IsRecaptchaRequiredForgotPwd

IsRecaptchaRequiredPwdlessLogin

IsRecaptchaRequiredRgstr

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether the Headless Passwordless Login Flow is enabled ( `true` ) or not
( `false` ).

The flow is disabled by default. This field is available in API version 59.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether a reCAPTCHA token is required to access Headless Forgot Password
API when a password reset is requested. If `true`, a reCAPTCHA token is required in your
initial POST request to the `/services/auth/headless/forgot_password`
endpoint.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether a reCAPTCHA token is required to access Headless Passwordless Login
API when user information is submitted to Salesforce. If `true`, a reCAPTCHA token is required
in your initial POST request to the
`/services/auth/headless/init/passwordless/login` endpoint.

By default, a reCAPTCHA token isn’t required ( `false` ). This field is available in API version
59.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether a reCAPTCHA token is required to access Headless Registration API
when user registration information is submitted to Salesforce. If `true`, a reCAPTCHA token
is required in your initial POST request to the
`/services/auth/headless/init/registration` endpoint.

The default value is `false` .


Standard Objects NetworkAuthApiSettings

**Field** **Details**

```
IsUniversalClientRgstrAllowed

IsUserDisambiguationAllowedForgotPwd

IsUserDisambiguationAllowedUsernamePwd

MaxPasswordResetAttempts

NetworkId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether self-registration and passwordless login via Universal Registration API
are enabled.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether the Headless Forgot Password Flow uses the headless user discovery
Apex handler that's specified in the `HeadlessDiscoveryHandlerId` field. The
handler enables users to reset their password with an identifier other than their username,
such as an email address, phone number, or order number.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether headless login flows use the headless user discovery Apex handler
that's specified in the `HeadlessDiscoveryHandlerId` field. The handler enables
users to log in with an identifier other than their username, such as an email address, phone
number, or order number. This field applies to the Authorization Code and Credentials Flow
and the OAuth 2.0 for First-Party Applications login flow.

The default value is `false` .

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum number of password reset attempts you allow for the Headless Forgot
Password Flow before the user must request a new one-time password (OTP).

**Type**
reference


Standard Objects NetworkAuthApiSettings

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of your Experience Cloud site. This ID is unique within your org.

This field is a relationship field.

**Relationship Name**
Network

**Relationship Type**
Lookup

**Refers To**
Network

```
RecaptchaScoreThreshold

RecaptchaSecretKey

RegistrationExecutionUserId

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The lowest reCAPTCHA score that is accepted before rejecting a request to access Headless
Identity APIs. This value must be between 0.5 and 1. Scores closer to 0.5 are more likely to
be bots, while scores closer to 1 are more likely to be valid users.

You must set a score threshold if `DoesForgotPasswordRequireAuth` or
`DoesRegistrationRequireAuth` fields are set to `true` . reCAPTCHA settings apply
to both the Headless Registration Flow and the Headless Forgot Password Flow.

Google issues a reCAPTCHA score only for reCAPTCHA v3 implementations. If you implement
reCAPTCHA v2, this field doesn’t apply.

**Type**
encryptedstring

**Properties**
Create, Nillable, Update

**Description**
The reCAPTCHA secret key from your API key pair. You get the API key pair from Google when
you set up reCAPTCHA. The secret key helps your app securely communicate with Google.

You must enter a secret key if `DoesForgotPasswordRequireAuth` or
`DoesRegistrationRequireAuth` are set to `true` . reCAPTCHA settings apply to
both the Headless Registration Flow and the Headless Forgot Password Flow.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects NetworkAuthApiSettings

**Field** **Details**

**Description**
The ID of the user who runs your headless registration Apex handler.

This field is a relationship field.

**Relationship Name**
RegistrationExecutionUser

**Relationship Type**
Lookup

**Refers To**
User

```
RegistrationHandlerId

RegistrationUserDefaultProfileId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of your headless registration Apex handler.

This field is a relationship field.

**Relationship Name**
RegistrationHandler

**Relationship Type**
Lookup

**Refers To**
ApexClass

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the default profile that gets assigned to new users when they register.

This field is a relationship field.

**Relationship Name**
RegistrationUserDefaultProfile

**Relationship Type**
Lookup

**Refers To**
Profile


### Standard Objects NetworkDataCategory NetworkDataCategory

Represents data categories in Lightning Web Runtime (LWR) Experience Cloud Sites. This object is available in API version 59.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

This object is available only when your org has Digital Experiences and Knowledge or Service Catalog enabled.

Fields

**Field** **Details**

```
DataCategoryGroupName

DataCategoryName

Description

ImageId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the data category group that contains one or more data categories.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the data category.

**Type**
textarea

**Properties**
Nillable

**Description**
Description of the data category.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Image associated with the data category.


### Standard Objects NetworkDiscoverableLogin

**Field** **Details**

This field is a relationship field.

**Relationship Name**
Image

**Relationship Type**
Lookup

**Refers To**
ManagedContent

```
Label

NetworkId

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The name of the data category shown in the UI.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the associated Experience site.

This field is a relationship field.

**Relationship Name**
### Network

**Relationship Type**
Lookup

**Refers To**
### Network

### NetworkDiscoverableLogin

Represents the Login Discoverable page from where customers and partners log in to an Experience Cloud site. Customers and partners
are users with an External Identity license or any communities license for Experience Cloud. This object is available in API version 44.0
and later.

Supported Calls

`create()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects NetworkDiscoverableLogin

Fields

**Field Name** **Details**

```
ApexHandlerId

ExecuteApexHandlerAsId

NetworkId

UsernameLabel

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The ID of the Apex handler created by the Login Discovery page type.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The ID of the user who is executing the handler.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

Unique

**Description**

The ID of `NetworkId` is unique within your org.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Log in prompt on login page when the login page type is Login Discovery.

Use this object to access the Login Discovery Page, which is a login page type that prompts users to identify themselves with an email
address, phone number, or custom identifier. DiscoverableLogin performs an interview-based login process, where users are first prompted
to provide identity and then authenticated. For example, users receive a verification code that they enter to complete the login process.

Note: The NetworkDiscoverableLogin object is created when **Login Discovery Page** is selected as the login page type on the
Login & Registration (L&R) page. If you later switch to another login page type, such as a Visualforce Page or Experience Builder
Page, the object isn’t deleted. The object persistence means you can’t delete the Apex class associated with the


### Standard Objects NetworkEmailTmplAllowlist

NetworkDiscoverableLogin object. To delete the Apex class, return to the L&R page and change the login page type back to **Login**
**Discovery page** . Select another Apex class, and then you can delete the first one.

### NetworkEmailTmplAllowlist

Represents an allowlist for the one-time password (OTP) email templates that are sent to end users during the Headless Registration
Flow, the Headless Passwordless Login Flow, and the Headless Forgot Password Flow. This object is available in API version 60.0 and
later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
EmailTemplateId

NetworkId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The IDs of the allowlisted email templates that can be sent to users during the headless
authorization flows for registration, passwordless login, and forgot password. You can list
multiple template IDs. When your app sends its initial request to Headless Registration API
or Headless Passwordless Login API, the `emailtemplate` parameter can include only
an email template ID from the allowlist. For Headless Forgot Password API, it works the same
way, but only if email template allowlisting is enabled.

This field is a relationship field.

**Relationship Name**
EmailTemplate

**Relationship Type**
Lookup

**Refers To**
EmailTemplate

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the Experience Cloud site for which the allowlist is being configured.

This field is a relationship field.


### Standard Objects NetworkFeedResponseMetric

**Field** **Details**

**Relationship Name**
### Network

**Relationship Type**
Lookup

**Refers To**
### Network NetworkFeedResponseMetric

Represents an object that stores the date and time values of question posts. It captures information for question creation, answer creation,
and when an answer is marked as best answer This object is available in API version 51.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

The NetworkFeedResponseMetric object is available only if both NetworksEnabled and ChatterEnabled org preferences are enabled.

Fields

**Field** **Details**

```
BestCommentDateTime

BestCommentId

FeedItemCreatedById

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Represents the date and time a user created an answer that was later marked as best answer.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the comment that was marked as the best answer.

**Type**
reference


Standard Objects NetworkFeedResponseMetric

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
Represents the user who created the feed item.

```
FeedItemDateTime

FeedItemId

FirstCommentDateTime

FirstCommentId

MarkedAsBestCommentDateTime

NetworkId

```

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
Represents the date and time when the feed Item was created.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Represents the unique ID of the question post.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Represents the date and time when the first comment was created.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represent the first comment on a feed Item.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Represents the date and time the user marked the answer as best answer.

**Type**
reference


### Standard Objects NetworkMember

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
Represents where the feed item was created.

```
ParentRecordId

### NetworkMember

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Represents the parent record. Parent records can include records like user, account, or group.

Represents a member of an Experience Cloud site. Members can be either users in your company or external users with portal profiles.
This object is available in API version 26.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`, `update()`

Special Access Rules

This object is available only when your org has digital experiences enabled.

Fields

**Field Name** **Details**

```
DefaultGroupNotificationFrequency

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. The default frequency for sending the member’s group
email notifications when the member joins groups in the Experience
Cloud site. The valid values are:

**•** `P` —Email on every post

**•** `D` —Daily digests

**•** `W` —Weekly digests


Standard Objects NetworkMember

**Field Name** **Details**

**•** `N` —Never

The default value is `W` . In sites, the `Email on every post`
option is disabled once more than 10,000 members choose this setting
for the group. All members who had this option selected are
automatically switched to `Daily digests` . However, this field is
not currently enabled. These values are reserved for future use.

```
DigestFrequency

LastChatterActivityDate

MemberId

NetworkId

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. The frequency for sending the member’s personal email
digest for the Experience Cloud site. The valid values are:

**•** `D` —Daily

**•** `W` —Weekly

**•** `N` —Never

The default value is `D` . However, daily and weekly personal digests
aren’t currently available in sites. These values are reserved for future
use.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The last time the member posted or commented in the Experience
Cloud site.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of a person who is a member of an Experience Cloud site.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the Experience Cloud site that the member is part of.


Standard Objects NetworkMember

**Field Name** **Details**

```
PreferencesDisableAllFeedsEmail

PreferencesDisableBestAnswerEmail

PreferencesDisableBookmarkEmail

PreferencesDisableChangeCommentEmail

PreferencesDisableDirectMessageEmail

```

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `false`, the member can automatically receive email for
updates in the Experience Cloud site, based on the types of feed emails
and digests the member has enabled.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `false`, the member automatically receives email when
someone selects their answer to a post as best. Available in API 46.0
and later.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `false`, the member automatically receives email every time
someone comments on a feed item after the member has bookmarked
it.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `false`, the member automatically receives email every time
someone comments on a change the member has made, such as an
update to their profile.

**Type**
boolean

**Properties**
Filter, Update


Standard Objects NetworkMember

**Field Name** **Details**

**Description**
When `false`, the member automatically receives email every time
someone sends them a direct message in the Experience Cloud site.

```
PreferencesDisableEndorsementEmail

PreferencesDisableFollowersEmail

PreferencesDisableItemFlaggedEmail

PreferencesDisableLaterCommentEmail

PreferencesDisableLikeEmail

```

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `false`, the member automatically receives email every time
someone endorses them for a topic.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `false`, the member automatically receives email every time
someone in the Experience Cloud site starts following the member.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `false`, the user automatically receives email every time a
member flags a post or comment. This setting only applies for
community moderators (with the Moderate Experiences Feeds
permission) and group owners or managers.

This field is available in API version 29.0 and later.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `false`, the member automatically receives email every time
someone comments on a feed item after the member has commented
on the feed item.

**Type**
boolean


Standard Objects NetworkMember

**Field Name** **Details**

**Properties**
Filter, Update

**Description**
When `false`, the member automatically receives email every time
someone comments on a feed item after the member has liked the
feed item.

```
PreferencesDisableMarketingCloudEmail

PreferencesDisableMentionsPostEmail

PreferencesDisableMessageEmail

PreferencesDisableProfilePostEmail

PreferencesDisableSharePostEmail

```

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `false`, the member automatically receives marketing emails
sent by Journey Builder. Available in API version 41.0 and later.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `false`, the member automatically receives email every time
the member is mentioned in posts.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `false`, the member automatically receives email every time
the member is sent a Chatter message.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `false`, the member automatically receives email every time
someone posts to the member’s profile.

**Type**
boolean


Standard Objects NetworkMember

**Field Name** **Details**

**Properties**
Filter, Update

**Description**
When `false`, the member automatically receives email every time
the member’s post is shared.

```
PreferencesDisCommentAfterLikeEmail

PreferencesDisMentionsCommentEmail

PreferencesDisProfPostCommentEmail

ReputationPoints

```

Usage

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `false`, the member automatically receives email every time
someone comments on a post the member has liked.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `false`, the member automatically receives email every time
the member is mentioned in comments.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `false`, the member automatically receives email every time
someone comments on posts on the member’s profile.

**Type**
double

**Properties**
Filter, Sort, Update

**Description**
The number of reputation points the user has accumulated by
performing actions in the Experience Cloud site.

Use this object to query members of a certain Experience Cloud site and to update their email notification settings. If you have Modify
All Data, View All Data, or Create and Set Up Experiences, you can view all members of any Experience Cloud site, regardless of your own


### Standard Objects NetworkMemberGroup

membership. If you have Modify All Data or Create and Set Up Experiences, you can also update any member’s email settings. Users
without these permissions can update their own email settings and can see members of the Experience Cloud sites that they’re also
members of.

Tip: You can directly update reputation points for a member via the Salesforce API. You can also use Apex triggers to send custom
notifications based on changes to reputation points.

### NetworkMemberGroup

Represents a group of members in an Experience Cloud site. Members can be either users in your internal org or external users assigned
portal profiles. An administrator adds members to an Experience Cloud site by adding a profile or a permission set, and any user with
the profile or permission set becomes a member of the site. This object is available in API version 26.0 and later.

Note: If a Chatter customer (from a customer group) is assigned a permission set that is also associated with an Experience Cloud
site, the Chatter customer won’t be added to the site.

Prior to API version 27.0, this object was called NetworkProfile.

Supported Calls

`create()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`

Note: The `upsert()` call is not supported for this object.

Special Access Rules

This object is available only when your org has digital experiences enabled.

Fields

**Field Name** **Details**

```
AssignmentStatus

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of a profile or permission set within an Experience Cloud site. Values
are:

**•** `Add Calculated` —The number of users that need to be added are
calculated and the add operation is in progress.

**•** `Added` —Users with this profile or permission set are members.

**•** `Failed Add` —Users with this profile or permission set were not
successfully made members.

**•** `Failed Remove` —Users with this profile or permission set were not
successfully removed from membership.


Standard Objects NetworkMemberGroup

**Field Name** **Details**

**•** `Remove Calculated` —The number of users that need to be removed
are calculated and the remove operation is in progress.

**•** `Waiting for Add` —The profile or permission set was added to the
Experience Cloud site, but the async process hasn’t completed yet. After the
process is complete, the status is updated to `Added` .

**•** `Waiting for Remove` —Use this status to remove all the members
belonging to a profile or permission set and remove a profile or permission
set from an Experience Cloud site.

```
NetworkId

ParentId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the Experience Cloud site that this group of members is associated with.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the profile or permission set associated with the Experience Cloud site.

Use this object to view the profiles or permission sets associated with a particular Experience Cloud site. Profiles and permission sets are
added and removed asynchronously, so you can also check the status of a profile or permission set that was updated in a site.

If you have Modify All Data, View All Data, or Create and Set Up Experiences, you can view all profiles or permission sets for any Experience
Cloud site in the org, regardless of your membership. If you have Modify All Data or Create and Set Up Experiences, you can also add
profiles or permission sets. Users without these permissions can only find profiles and permission sets for Experience Cloud sites that
they’re members of.

Sample Code

```
// Create a new NetworkMemberGroup with a profile as the ParentId

NetworkMemberGroup nmgInsert = new NetworkMemberGroup();

nmgInsert.setNetworkId('{enter your network ID : ODB...}');

nmgInsert.setParentId('enter the profile or permission set ID : 00e... or 0PS...');

SaveResult[] results = connection.create(new SObject[] { nmgInsert });

// Update an existing NetworkMemberGroup to be removed from the Network

NetworkMemberGroup nmgUpdate = new NetworkMemberGroup();

nmgUpdate.setId('enter your NetworkMemberGroup ID : 0DL...');

```


### Standard Objects NetworkModeration

```
   nmgUpdate.setAssignmentStatus('WaitingForRemove');

   SaveResult[] results = connection.update(new SObject[] { nmgUpdate });

### NetworkModeration

```

Represents a flag on an item in a community. This object is available in API version 30.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

This object is available only when your org has digital experiences enabled.

Fields

**Field Name** **Details**

```
EntityId

ModerationType

NetworkId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the post, comment, or file that was flagged.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Determines the type of flag applied to an item. Values are:

**•** FlagAsInappropriate

**•** FlagAsSpam

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the community in which the item was flagged.


### Standard Objects NetworkPageOverride

**Field Name** **Details**

```
Visibility

```

Usage

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Nillable, Sort

**Description**
Determines visibility of a flagged item. Values are:

**•** SelfAndModerators—The user who flagged the item and any moderators
can see the flagged item. This is the default value.

**•** ModeratorsOnly—Only moderators can see the flagged item. If
ModeratorsOnly is selected, only moderators can set flags using the API.

Use this object to view the items flagged for moderation within a community. Additionally, users with “Moderate Feeds” and “Modify
All Data” can remove flags.

Flags on items are created either when a member manually flags an item in a community (if flagging is enabled for that community),
or when a trigger automatically flags an item because the item met the trigger criteria.

### NetworkPageOverride

Represents information about custom pages used to override the default pages in Experience Cloud sites. You can create Experience
Builder or Visualforce pages and override the default pages in a site. Using custom pages allows you to create a more personalized
experience for your users. This object is available in API version 34.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

**•** Only users with the Create and Setup Experiences permission can update this object.

**•** You can’t override the Change Password Page with a page created using Experience Builder. You can only override it with a Visualforce
page.

Fields

**Field Name** **Details**

```
NetworkId

```

**Type**
reference


### Standard Objects NetworkSelfRegistration

**Field Name** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the Experience Cloud site where a custom page is used to override a
default page.

```
OverrideSetting

OverrideType

### NetworkSelfRegistration

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of the page used to override a default page in the Experience Cloud
site. `OverrideSetting` can take the following values:

**•** `Standard` —The standard page that comes by default with the site.

**•** `Configurable` —The page created when the Configurable Self-Reg
registration page type or the Login Discovery login page type is selected.

**•** `Designer` —A custom page created using Experience Builder.

**•** `Visualforce` —A custom page created using Visualforce.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The name of the default page in the Experience Cloud site that you want to
override with a custom page. `OverrideType` can take the following values:

**•** `LoginRequired`

**•** `ChangePassword`

**•** `ForgotPassword`

**•** `SelfReg`

**•** `Home`

Represents the account that self-registering Experience Cloud users are associated with by default. Self-registering users in an Experience
Cloud site are required to be associated with an account, which the admin must specify while setting up self-registration for the site. If
an account isn’t specified, Salesforce creates person accounts (when enabled) for self-registering users. This object is available in API
version 34.0 and later.


Standard Objects NetworkSelfRegistration

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
AccountId

ApexHandlerId

CurrencyIsoCode

ExecuteApexHandlerAsId

NetworkId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The ID of the account that self-registering users in the Experience Cloud site are
associated with.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The ID of the Apex handler created by Configurable Self-Reg registration page
type.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the org.

The default value is `USD` .

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The ID of the user who is executing the configurable self-registration handler.

**Type**
reference


Standard Objects NetworkSelfRegistration

**Field Name** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The ID of `NetworkId` is unique within your org.

You can use only one account per Experience Cloud site to assign self-registering
users.

```
OptionsDisableStandardRgstrComponent

OptionsIncludePassword

OptionsShowEmail

OptionsShowFirstName

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Determines whether you can use standard Aura and Lightning Web Runtime
(LWR) components for self-registration. If this field is `true`, self-registration flows
that use these components don’t work.

For more control over self-registration, set this field to `true` if you’re not using
the standard self-registration component.

**Type**
Boolean

**Properties**
Create, Filter, Update

**Description**

Option on Configurable Self-Reg registration page. If true, the Include Password
field is selected.

**Type**
Boolean

**Properties**
Create, Filter, Update

**Description**

Option on Configurable Self-Reg registration page. If true, the Email field appears
on the self-registration form.

**Type**
Boolean

**Properties**
Create, Filter, Update

**Description**

Option on the Configurable Self-Reg registration page. If true, the First Name
field appears on the self-registration form.


Standard Objects NetworkSelfRegistration

**Field Name** **Details**

```
OptionsShowLastName

OptionsShowMobilePhone

OptionsShowNickname

OptionsShowUsername

PermissionSetGroupId

```

**Type**
Boolean

**Properties**
Create, Filter, Update

**Description**

Option on the Configurable Self-Reg registration page. If true, the Last Name field
appears on the self-registration form.

**Type**
Boolean

**Properties**
Create, Filter, Update

**Description**

Option on the Configurable Self-Reg registration page. If true, the Mobile field
appears on the self-registration form.

**Type**
Boolean

**Properties**
Create, Filter, Update

**Description**

Option on the Configurable Self-Reg registration page. If true, the Nickname field
appears on the self-registration form.

**Type**
Boolean

**Properties**
Create, Filter, Update

**Description**

Option on the Configurable Self-Reg registration page. If true, the Username field
appears on the self-registration form.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the permission set group used for the self registration. This field is a
relationship field.

**Relationship Name**
PermissionSetGroup


### Standard Objects NetworkUserHistoryRecent

**Field Name** **Details**

**Refers To**
PermissionSetGroup

```
VerificationMethod

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of verification method that a user must supply when registering, which
can be:

**•** `SyncEmail` —User must supply an email address to verify identity.

**•** `SMS` —User must supply a phone number to verify identity.

### NetworkUserHistoryRecent

Represents an Experience Cloud site user’s history of accessed records. This object is available in API version 42.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `undelete()`

Special Access Rules

Only users with the Modify All Data permission can view and delete these data.

Fields

**Field** **Details**

```
AccessTimestamp

ActionType

```

**Type**
datetime

**Properties**
Create, Filter, Sort

**Description**
The time at which the record was accessed.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


Standard Objects NetworkUserHistoryRecent

**Field** **Details**

**Description**
Indicates the action type taken by the user. The possible values are:

**•** Read

**•** Write

```
DomainName

FeedCommentId

FeedItemId

NetworkId

NetworkUserId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The domain used to access the record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Feed comment accessed by the user.

**Type**
reference

**Properties**
Create, Filter, Group,Sort, Update

**Description**
Feed item accessed by the user.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the Experience Cloud site used to access the record or comment.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
User’s Experience Cloud site user ID to access the record or comment.


Standard Objects NetworkUserHistoryRecent

**Field** **Details**

```
RecordId

RecordKeyPrefix

Url

UserType

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The record that was accessed.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Record’s ID key prefix.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The URL from which the user accessed the record.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of user who accessed this record. The possible values include:

**•** Standard

**•** Partner

**•** Customer Portal Manager

**•** Customer Portal User

**•** Guest

**•** High Volume Portal

**•** CSN Only

**•** Self Service

Use the NetworkUserHistoryRecent object to delete comments, posts, or record access by Experience Cloud site users who would like
all such activity to be removed.


### Standard Objects Note Note

Represents a note, which is text associated with a custom object or a standard object, such as a Contact, Contract, or Opportunity.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
Body

IsDeleted

IsPrivate

OwnerId

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Body of the note. Limited to 32 KB.

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
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If `true`, only the note owner or a user with the “Modify All Data” permission can view the
note or query it via the API. Note that if a user who does not have the “Modify All Data”
permission sets this field to `true` on a note that they do not own, then they can no longer
query, delete, or update the note. Label is **Private** .

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the user who owns the note.


Standard Objects Note

**Field** **Details**

This is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

```
ParentId

Title

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the object associated with the note.

This is a polymorphic relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Account, Accreditation, AssessmentIndicatorDefinition, AssessmentTask,
AssessmentTaskContentDocument, AssessmentTaskDefinition, AssessmentTaskOrder, Asset,
Award, BoardCertification, BusinessLicense, BusinessMilestone, BusinessProfile, CareBarrier,
CareBarrierDeterminant, CareBarrierType, CareDeterminant, CareDeterminantType,
CareDiagnosis, CareMetricTarget, CareObservationComponent,
CarePgmProvHealthcareProvider, CareProgram, CareProgramCampaign,
CareProgramEligibilityRule, CareProgramEnrollee, CareProgramEnrolleeProduct,
CareProgramEnrollmentCard, CareProgramGoal, CareProgramProduct, CareProgramProvider,
CareProgramTeamMember, CareProviderAdverseAction, CareProviderFacilitySpecialty,
CareRegisteredDevice, CareRequest, CareRequestDrug, CareRequestExtension,
CareRequestItem, CareSpecialty, CareTaxonomy, CommSubscription,
CommSubscriptionChannelType, CommSubscriptionConsent, CommSubscriptionTiming,
Contact, Contract, CreditMemo, DelegatedAccount, EngagementChannelType,
EnrollmentEligibilityCriteria, HealthcareFacility, HealthcareFacilityNetwork,
HealthcarePayerNetwork, HealthcarePractitionerFacility, HealthcareProvider,
HealthcareProviderNpi, HealthcareProviderSpecialty, HealthcareProviderTaxonomy,
IdentityDocument, Image, IndividualApplication, Invoice, Lead, Location, MemberPlan,
Opportunity, Order, OtherComponentTask, PersonEducation, PersonLifeEvent, Product2,
ProductRequest, ProductRequestLineItem, PurchaserPlan, ReceivedDocument,
ServiceAppointment, ServiceResource, Shift, SocialPost, Visit, VisitedParty, Visitor,
VolunteerProject, WorkOrder, WorkOrderLineItem

**Type**
string


### Standard Objects NoteAndAttachment

**Field** **Details**

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Title of the note.

Usage

Use this object to manage notes for an object.

SEE ALSO:

Overview of Salesforce Objects and Fields

### NoteAndAttachment

This read-only object contains all notes and attachments associated with an object.

Supported Calls

```
   describeSObjects()

```

Fields

**Field** **Details**

```
IsDeleted

IsNote

IsPrivate

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
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the object contains a note ( `true` ) or an attachment ( `false` ).

**Type**
boolean


Standard Objects NoteAndAttachment

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, only the note owner or a user with the “Modify All Data” permission can view the
note or query it via the API. Note that if a regular user who does not have “Modify All Data”
permission sets this field to `true` on a note that they do not own, then they can no longer
query, delete, or update that note. Label is **Private** .

```
OwnerId

ParentId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who owns the note and attachment.

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
Filter, Group, Sort

**Description**
ID of the parent object.

This is a polymorphic relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Account, Accreditation, AssessmentIndicatorDefinition, AssessmentTask,
AssessmentTaskContentDocument, AssessmentTaskDefinition, AssessmentTaskOrder, Asset,
Award, BoardCertification, BusinessLicense, BusinessMilestone, BusinessProfile, CareBarrier,
CareBarrierDeterminant, CareBarrierType, CareDeterminant, CareDeterminantType,
CareDiagnosis, CareMetricTarget, CareObservationComponent,
CarePgmProvHealthcareProvider, CareProgram, CareProgramCampaign,
CareProgramEligibilityRule, CareProgramEnrollee, CareProgramEnrolleeProduct,
CareProgramEnrollmentCard, CareProgramGoal, CareProgramProduct, CareProgramProvider,


### Standard Objects NoteTag

**Field** **Details**

CareProgramTeamMember, CareProviderAdverseAction, CareProviderFacilitySpecialty,
CareRegisteredDevice, CareRequest, CareRequestDrug, CareRequestExtension,
CareRequestItem, CareSpecialty, CareTaxonomy, CommSubscription,
CommSubscriptionChannelType, CommSubscriptionConsent, CommSubscriptionTiming,
Contact, Contract, CreditMemo, DelegatedAccount, EngagementChannelType,
EnrollmentEligibilityCriteria, HealthcareFacility, HealthcareFacilityNetwork,
HealthcarePayerNetwork, HealthcarePractitionerFacility, HealthcareProvider,
HealthcareProviderNpi, HealthcareProviderSpecialty, HealthcareProviderTaxonomy,
IdentityDocument, Image, IndividualApplication, Invoice, Lead, Location, MemberPlan,
Opportunity, Order, OtherComponentTask, PersonEducation, PersonLifeEvent, Product2,
ProductRequest, ProductRequestLineItem, PurchaserPlan, ReceivedDocument,
ServiceAppointment, ServiceResource, Shift, SocialPost, Visit, VisitedParty, Visitor,
VolunteerProject, WorkOrder, WorkOrderLineItem

```
 Title

```

Usage

**Type**
string

**Properties**
Filter, Nillable, Group, Sort

**Description**
Title of the note.

Use this object to list all notes and attachments for an object.

To retrieve notes and attachments, issue a describe call on an object, which returns a query result for each activity since the record was
created. You can’t directly query this object.

SEE ALSO:

### Note

Attachment

### NoteTag

Associates a word or short phrase with a Note.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`


Standard Objects NoteTag

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

NoteTag stores the relationship between its parent TagDefinition and the Note being tagged. Tag objects act as metadata, allowing
users to describe and organize their data.


### Standard Objects OauthCustomScope

When a tag is deleted, its parent TagDefinition will also be deleted if the name is not being used; otherwise, the parent remains. Deleting
a TagDefinition sends it to the Recycle Bin, along with any associated tag entries.

### OauthCustomScope

Represents a permission defining the protected data that a connected app can access from an external entity when Salesforce is the
OAuth authorization provider.

An OAuth custom scope tells an external entity about a connected app’s permissions to access protected data. The OAuth custom scope
that you create in your Salesforce org corresponds to the same custom scope defined in your external entity, and assigned to the resource.

For example, you define an Order Status custom scope in your external entity that allows access to customer order status data in your
order system’s API. In Salesforce, you create an OAuth custom scope that you also name Order Status. You assign this custom scope to
the connected app requesting access to the order status API. When the external entity receives the connected app’s request to access
a customer’s order status, it validates the connected app’s access token and Order Status scope. With a successful validation, the app
can access the customer order status information in the order system’s API.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

You must have the “Manage Connected Apps” permission to access this object.

Fields

**Field Name** **Details**

```
Description

DeveloperName

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The description of the permission provided to the connected app by the scope.
The custom scope’s description must be unique, can only include alphanumeric
characters, and can be up to 60 characters long.

You can enter a custom label in place of a description. An advantage of using a
custom label is that you can maintain reusable text in a single location and
[translate the text into multiple languages. See Custom Labels.](https://help.salesforce.com/articleView?id=cl_about.htm&language=en_US)

Note: The description formatting requirements that apply to custom
scopes also apply to custom labels.

**Type**
string


Standard Objects OauthCustomScope

**Field Name** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Use when referring to the OAuth custom scope from a program. This label must
be unique, and can include only alphanumeric characters and underscores.

```
IsPublic

Language

MasterLabel

NamespacePrefix

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the object is included in the connected app’s OpenID Connect
[discovery endpoint. For more information, see OpenID Connect Discovery](https://help.salesforce.com/articleView?id=remoteaccess_using_openid_discovery_endpoint.htm&language=en_US)
[Endpoint.](https://help.salesforce.com/articleView?id=remoteaccess_using_openid_discovery_endpoint.htm&language=en_US)

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the default language defined for the developing org.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The master label for the custom scope record. This label must be unique, and
can include only alphanumeric characters and underscores.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix for an OAuth custom scope that's been installed as part
of a second-generation managed package. If the custom scope isn't packaged,
this value is empty. This field is available in API version 61.0 and later.


### Standard Objects OauthCustomScopeApp OauthCustomScopeApp

Represents the name of the connected app to which the custom scope is assigned. This object is available in API version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
OauthCustomScopeId

### OauthToken

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the connected app to which the custom scope is assigned. If the connected
app is part of a package, include the package’s namespace prefix with the connected app’s
name. Use the following format: _**`<namespace_prefix>`**_ `__` _**`<connected_app>`**_ .
Use two underscores (_) between the namespace prefix and connected app’s name.

This is a relationship field.

**Relationship Name**
### OauthCustomScope

**Relationship Type**
Lookup

**Refers To**
### OauthCustomScope

Represents an OAuth access token for connected app authentication. Use this object to create a user interface for token management.
This object is available in API version 32.0 and later.

A connected app integrates an application with Salesforce using APIs. Connected apps use standard SAML and OAuth protocols to
authenticate, provide single sign-on, and provide tokens for use with Salesforce APIs. In addition to standard OAuth capabilities, connected
apps allow Salesforce admins to set various security policies and have explicit control over who can use the corresponding apps. Each
time that a user grants access to an application, the application obtains a new access token.

Supported Calls

`describeSObjects()`, `query()`


Standard Objects OauthToken

Special Access Rules

Users with the Customize Application permission see all tokens for all users in the org. Otherwise, you see only your own tokens.

[If you try to use Apex DML operations and then query this object in the same call, you get an](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_dml_section.htm) `UncommittedWork` error with this
description.

```
   A callout was unsuccessful because of pending uncommitted work related to a process, flow,

    or Apex operation.

   Commit or roll back the work, and then try again.

```

To avoid this error, execute DML operations and queries in separate, asynchronous calls.

Fields

**Field Name** **Details**

```
AccessToken

AppMenuItemId

AppName

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The refresh token for authorization.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The unique ID for the App Picker menu item that’s associated with this OAuth
token.

This is a relationship field.

**Relationship Name**
AppMenuItem

**Relationship Type**
Lookup

**Refers To**
AppMenuItem

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The label for the connected app that’s associated with this OAuth token.


Standard Objects OauthToken

**Field Name** **Details**

```
DeleteToken

Id

LastUsedDate

RequestToken

UseCount

UserId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

A token that can be used at the revoke OAuth token endpoint to remove this
token.

**Type**
ID

**Properties**
Defaulted on create, Filter, Group, idLookup, Sort

**Description**

Reserved for future use. Currently, the value is always `null` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The most recent date when the OAuth token was used.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The authorization code that was used to request the corresponding AccessToken.
With this authorization code, you can revoke the corresponding AccessToken by
passing the DeleteToken.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

How often the token has been used.

**Type**
reference


### Standard Objects OauthTokenExchangeHandler

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**

The owner of the token.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

Usage

To delete an AccessToken, send a request to the revoke OAuth token endpoint with the DeleteToken as the parameter. For example,
the URL `https://` _`MyDomainName`_ `.my.salesforce.com/services/oauth2/revoke?token=(the Delete`
`Token)` causes the deletion of the token.

In API version 34.0 and later, this object was enhanced to help manage high instance counts. A `query()` call returns up to 500 rows.
A `queryMore()` call returns 500 more, up to 2500 total. No more records are returned after 2500. To make sure that you don’t miss
any records, issue a `COUNT()` query in a SELECT clause for OauthToken. This query gives you the total number of records. If there are
more than 2500 records, use these options to manage your results.

**•** Divide queries by filtering on fields like `UserId` to return subsets of less than 2500 records.

**•** Use `OFFSET` to get batches of 2500 records. Start with an `OFFSET` of 0 and then increment by 2500. If you use this option, we
recommend that you also use `LIMIT` to limit each query to 2500.

For example, use an initial query with this structure.

```
     SELECT <desired fields> FROM OauthToken LIMIT 2500 OFFSET 0

```

Then, run another query with an offset of 2500.

```
     SELECT <desired fields> FROM OauthToken LIMIT 2500 OFFSET 2500

```

Continue to increase the offset by 2500 until you have results for all records.

### OauthTokenExchangeHandler

Represents a token exchange handler. The token exchange handler also consists of an Apex class. During the OAuth 2.0 token exchange
flow, the token exchange handler is used to validate tokens from an external identity provider and to map users to Salesforce. This object
is available in API version 60.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects OauthTokenExchangeHandler

Special Access Rules

Fields

**Field** **Details**

```
Description

DeveloperName

IsContactCreationAllowed

IsEnabled

IsUserCreationAllowed

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
A description for your token exchange handler.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The API name for the handler.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
For internal use only.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the handler is enabled for the token exchange flow.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the handler can set up new users. During the token exchange flow, the
Apex handler maps users from the identity provider to Salesforce. If the
`IsUserCreationAllowed` field is `true`, the `canCreateUser` boolean in the


Standard Objects OauthTokenExchangeHandler

**Field** **Details**

`getUserForTokenSubject` method is `true`, and the user doesn’t exist in Salesforce,
the handler sets up a new User object, which Salesforce automatically inserts to finish creating
the user.

The default value is `false` .

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
Indicates the language used in the org where the token exchange handler was created.

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
The label of the token exchange handler record.

**Type**
string


Standard Objects OauthTokenExchangeHandler

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can
refer to a component in a managed package by using the
`namespacePrefix__componentName` notation. The namespace prefix can have
one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

```
SupportedTokenTypesAccessToken

SupportedTokenTypesIdToken

SupportedTokenTypesJwt

SupportedTokenTypesRefreshToken

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the handler supports opaque access tokens from the identity provider.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the handler supports OpenID Connect ID tokens from the identity provider.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the handler supports tokens from the identity provider that are in JWT
format, such as JWT-based access tokens.

**Type**
boolean

**Properties**
Create, Filter, Update


### Standard Objects OauthTokenExchHandlerApp

**Field** **Details**

**Description**
Indicates whether the handler supports OAuth 2.0 refresh tokens from the identity provider.

```
SupportedTokenTypesSaml2

TokenHandlerApexId

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the handler supports SAML 2.0 assertions from the identity provider.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The Apex class associated with the token exchange handler. The class contains methods to
validate the token and map users to Salesforce. It must extend the
`Oauth2TokenExchangeHandler` Apex class.

This field is a relationship field.

**Relationship Name**
TokenHandlerApex

**Relationship Type**
Lookup

**Refers To**
ApexClass

### OauthTokenExchHandlerApp

Represents the enablement settings for a specific Salesforce connected app or external client app that’s enabled for the token exchange
handler. A handler can be enabled for multiple apps. This object is available in API version 60.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects OauthTokenExchHandlerApp

Special Access Rules

Fields

**Field** **Details**

```
ApexExecutionUserId

ConnectedApplicationId

IsDefault

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the user who runs the Apex token exchange handler. We recommend that you use
an integration user.

This field is a relationship field.

**Relationship Name**
ApexExecutionUser

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The connected app that’s being used to integrate with Salesforce.

This field is a relationship field.

**Relationship Name**
ConnectedApplication

**Relationship Type**
Lookup

**Refers To**
ConnectedApplication

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the token exchange handler is the default handler for this app. During the
token exchange flow, in the token request, you can optionally include a `token_handler`


### Standard Objects ObjectDataImport

**Field** **Details**

parameter with the name of a specific handler’s Apex class. If you don’t include this parameter,
Salesforce defaults to the default handler.

The default value is `false` .

```
OauthTokenExchangeHandlerId

### ObjectDataImport

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The `OauthTokenExchangeHandler` with which these enablement settings are
associated.

This field is a relationship field.

**Relationship Name**
OauthTokenExchangeHandler

**Relationship Type**
Lookup

**Refers To**
OauthTokenExchangeHandler

Represents the data import status of one or more object records. This object is available in API version 57.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
EndDate

FileName

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time (in UTC) when the data import finished.

**Type**
string


Standard Objects ObjectDataImport

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Optional. If the data import was from a comma-delimited file (CSV), the name of the file. The
maximum length is 120 characters.

```
ObjectDataImportNumber

OwnerId

PrimaryObject

Result

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated number identifying the data import.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user who owns the data import status record.

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
Filter, Group, Restricted picklist, Sort

**Description**
The name of the primary object being imported. For example, Lead. This value is usually
provided programmatically. The maximum length is 120 characters.

**Type**
textarea

**Properties**
Nillable

**Description**
The JSON response of the data object import result, including error messages.


### Standard Objects ObjectDataImportReference

**Field** **Details**

```
Status

Type

```

Associated Objects

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The processing status of the data object import.

Possible values are:

**•** `Completed`

**•** `In Progress`

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of data import, such as from a comma-delimited file or through a connector.

Possible values are:

**•** `CSV Async`

**•** `CSV Sync`

**•** `External Record Import` —A record imported or updated by Partner Connect
[between a partner and vendor system. To see this field, enable Partner Connect. See Set](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_partner_parent.htm&type=5&language=en_US)
[Up Partner Connect as a Partner in](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_partner_parent.htm&type=5&language=en_US) _Salesforce Help_ . Available in API version 62.0 and later.

**•** `One time Connector`

This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**[ObjectDataImportChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Sharing rules are available for the object.

**ObjectDataImportOwnerSharingRule on page 65**
Sharing rules are available for the object.

**ObjectDataImportShare on page 67**
Sharing is available for the object.

### ObjectDataImportReference

Represents the relationships to the associated reference objects showing the source from which the data is imported. This object is
available in API version 57.0 and later.


### Standard Objects ObjectMetadataTag

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

ObjectDataImportReference is read only and can only be queried.

Fields

**Field** **Details**

```
ObjectDataImportId

ObjectDataImportReferenceNumber

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Foreign key to the ObjectDataImport object.

This field is a relationship field.

**Relationship Name**
ObjectDataImport

**Relationship Type**
Lookup

**Refers To**
ObjectDataImport

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Foreign key to the reference object. For example, AsyncApiJob or DatasetImportRequest.

### ObjectMetadataTag

Represents a meta tag for a store page. Meta tags in HTML documents provide structured data used by search engines for ranking and
to show content in search results. This object is available in API version 60.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `undelete()`,
`update()`, `upsert()`


Standard Objects ObjectMetadataTag

Special Access Rules

This object is available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

```
CurrencyIsoCode

Language

Name

RecordId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Possible values are:

**•** `USD` —U.S. Dollar

The default value is `USD` .

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The language of the page meta tag.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the page meta tag.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the product or product category with which this record is associated.

This is a polymorphic relationship field.

**Relationship Name**
Record

**Relationship Type**
Lookup


### Standard Objects ObjectPermissions

**Field** **Details**

**Refers To**
Product2, ProductCategory

Availability in API versions:

**•** Product2 is available in API versions 60.0 and later

**•** ProductCategory is available in API versions 63.0 and later

```
TagType

Value

### ObjectPermissions

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of the page meta tag.

Possible values are:

**•** `Description` —Meta Description

**•** `Title` —Title Tag

**Type**
textarea

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The value of the page meta tag. This value populates the HTML tag. For example, a meta tag
with a `Type` of `Title` and a `Value` of `GoBrew Espresso` renders the HTML
`<title>GoBrew Espresso</title>` for the page.

Represents the enabled object permissions for the parent PermissionSet. This object is available in API version 24.0 and later.

To grant a user access to an object, associate an ObjectPermissions record with a PermissionSet that’s assigned to a user. ObjectPermissions
records are only supported in PermissionSet, not in Profile.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

As of Summer ’20 and later, only users with the View Setup and Configuration permission can access this object.


Standard Objects ObjectPermissions

Fields

**Field Name** **Details**

```
ParentId

PermissionsCreate

PermissionsDelete

PermissionsEdit

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The `Id` of this object’s parent PermissionSet.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
PermissionSet

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
If `true`, users assigned to the parent PermissionSet can create records for this
object. Requires `PermissionsRead` for the same object to be `true` .

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
If `true`, users assigned to the parent PermissionSet can delete records for this
object. Requires `PermissionsRead` and `PermissionsEdit` for the
same object to be `true` .

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
If `true`, users assigned to the parent PermissionSet can edit records for this
object. Requires `PermissionsRead` for the same object to be `true` .


Standard Objects ObjectPermissions

**Field Name** **Details**

```
PermissionsModifyAllRecords

PermissionsRead

PermissionsViewAllFields

PermissionsViewAllRecords

SobjectType

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
If `true`, users assigned to the parent PermissionSet can edit all records for this
object, regardless of sharing settings. Requires `PermissionsRead`,
`PermissionsDelete`, `PermissionsEdit`, and
`PermissionsViewAllRecords` for the same object to be `true` .

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
If `true`, users assigned to the parent PermissionSet can view records for this
object.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
If `true`, users assigned to the parent PermissionSet can view all fields and field
data for this object. Available in API version 63.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
If `true`, users assigned to the parent PermissionSet can view all records for this
object, regardless of sharing settings. Requires `PermissionsRead` for the
same object to be `true` .

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The object’s API name. For example, `Merchandise__c` .


Standard Objects ObjectPermissions

Permission Dependencies

Some user permissions have dependencies on object permissions. For example, if a permission set has the “Transfer Leads” permission,
it also has “Read” and “Create” on the leads object.

You can query from ObjectPermissions up to the parent PermissionSet object. For example:

```
   SELECT Parent.Name, Parent.PermissionsTransferAnyLead, PermissionsRead, PermissionsCreate

   FROM ObjectPermissions

   WHERE SobjectType = 'Lead'

```

Determining Object Access with “Modify All Data”

When using SOQL to query object permissions, be aware that some object permissions are enabled because a user permission requires
them.

The exception to this rule is when “Modify All Data” is enabled. While it enables all object permissions, it doesn’t physically store any
object permission records in the database. As a result, unlike object permissions that are required by a user permission—such as “View
All Data” or “Import Leads”—the query still returns permission sets with “Modify All Data,” but the object permission record will contain
an invalid ID that begins with “000”. This ID indicates that the object has full access due to “Modify All Data” and the object permission
record can’t be updated or deleted. To remove full access from these objects, disable “Modify All Data” and then delete the resulting
object permission record. This ensures that when using SOQL to find all the objects that have full access, it returns all objects that have
this access regardless of whether it’s due to “Modify All Data” or because an administrator set full access.

For example, the following will return all permission sets that have “Read” on the Merchandise__c object, regardless of whether it’s
explicitly defined on the object or implicitly defined through “Modify All Data.”

```
   SELECT Id, Parent.label, SobjectType, PermissionsRead,

     Parent.PermissionsModifyAllData, ParentId

   FROM ObjectPermissions

   WHERE PermissionsRead = true and SobjectType = 'Merchandise__c'

```

Nesting Object Permissions

You can nest ObjectPermissions in a PermissionSet query. For example, the following returns any permission sets where “Transfer Leads”
is true. Additionally, the result set will include the “Read” object permission on leads. This is done by nesting the SOQL with an object
permission query using the relationship name for object permissions: `ObjectPerms` .

```
   SELECT Id,Name,PermissionsTransferAnyLead,

   (SELECT Id, PermissionsRead from ObjectPerms where SobjectType='Lead')

   FROM PermissionSet

   WHERE PermissionsTransferAnyLead = true

```

As a result, it’s possible to traverse the relationship between the PermissionSet and any child-related objects (in this case, ObjectPermissions).
You can do this from the PermissionSet object by using the child relationship ( `ObjectPerms`, `FieldPerms`, and so on) or from
the child object by referencing the PermissionSet with `Parent.` _**`permission_set_attribute`**_ .

It’s important to consider when to use a conditional `WHERE` statement to restrict the result set. To query based on an attribute on the
permission set object, nest the SOQL with the child relationship. However, to query based on an attribute on the child object, you must
reference the permission set parent attribute in your query.


### Standard Objects ObjectRelatedUrl

The following two queries return the same columns with different results, based on whether you use the child relationship or parent
notation.

```
   SELECT Id, Name, PermissionsModifyAllData,

   (SELECT Id, SobjectType, PermissionsRead from Objectperms)

   FROM PermissionSet

   WHERE PermissionsModifyAllData=true

```

versus:

```
   SELECT Id, SObjectType, PermissionsRead, Parent.Id, Parent.Name,

   Parent.PermissionsModifyAllData

   FROM ObjectPermissions

   WHERE SObjectType='Merchandise__c'

```

SEE ALSO:

PermissionSet

FieldPermissions

### ObjectRelatedUrl

Represents a URL slug for a Product or Category page on a B2B Commerce or D2C Commerce LWR site, or a custom object, account, or
contact page on an enhanced LWR Experience Cloud site. This object is available in API version 57.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `undelete()`,
`update()`, `upsert()`

Special Access Rules

Your org must have B2B Commerce or D2C Commerce license enabled for commerce use cases. ObjectRelatedUrl is available for Product2
and ProductCategory records in Commerce, and on custom object, account and contact record pages in enhanced LWR sites.

Fields

**Field** **Details**

```
LanguageCode

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The combined language and locale ISO code, which controls the language of the
object-related URL. The maximum length is 8 characters.


Standard Objects ObjectRelatedUrl

**Field** **Details**

```
Name

ParentId

Scope

UniqueIndex

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the object-related URL. This field isn’t editable.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The ID of the parent record that the `UrlName` refers to. `ParentId` can point
only to Product2, ProductCategory, and custom object, account, and contact record pages.

This field is a polymorphic relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Product2, ProductCategory, account, contact, and custom objects

Availability in API versions:

**•** Product2 and ProductCategory in LWR Commerce stores (available in API version 58.0 and
later)

**•** Custom object pages on enhanced LWR sites (available in API version 60.0 and later)

**•** Account and contact pages on enhanced LWR sites (available in API version 61.0 and later)

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. Helps ensure uniqueness of the UrlName field across all records with the same
Scope and LanguageCode values. The maximum length is 18 characters.

**Type**
string

**Properties**
Filter, idLookup, Nillable, Sort


### Standard Objects ObjectTerritory2AssignmentRule

**Field** **Details**

**Description**
Ensures uniqueness for each record within your org and creates an index for lookup. This
field isn’t editable.

This field is a calculated field.

```
UrlName

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The URL slug for the record.

Note: When creating a query, for example, `SELECT UrlName From ObjectRelatedUrl WHERE Scope='01t'`,
the `WHERE` condition must use `Id`, `UniqueIndex`, `Scope`, or `ParentId` .

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ObjectRelatedUrlChangeEvent on page 68 (API version 62.0)**
Change events are available for the object.

### ObjectTerritory2AssignmentRule

Represents a territory assignment rule that’s associated with an object, such as Account. ObjectTerritory2AssignmentRuleItem can be
created or deleted if the BooleanFilter field on its corresponding ObjectTerritory2AssignmentRule is `null` . Available if Sales Territories
has been enabled.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Standard users can access this object. If a territory model is in `Active` state, any standard user can view that model, including its
territories, assignment rules, assigned records, and assigned users. Users cannot view territory models in other states (such as `Planning`
or `Archived` ).


Standard Objects ObjectTerritory2AssignmentRule

Fields

**Field Name** **Details**

```
BooleanFilter

DeveloperName

IsActive

Language

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Represents advanced filter conditions that were specified for the rule in the online
application. For example, “(1 AND 2) OR 3.”

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The unique name of the object in the API. This name can contain only
underscores and alphanumeric characters and must be unique in your
organization. It must begin with a letter, not include spaces, not end with an
underscore, and not contain two consecutive underscores. The field label in the
user interface is `Unique Name` .

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is
specified, performance slows down while Salesforce generates one for
each record.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the rule is active (true) or inactive (false). Via the API, active
rules run automatically when object records are created and edited. The exception
is when the value of the IsExcludedFromRealign field on an object record is `true`,
which prevents record assignment rules from evaluating that record.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


### Standard Objects ObjectTerritory2AssignmentRuleItem

**Field Name** **Details**

**Description**
The language of the label in the user interface.

```
MasterLabel

ObjectType

Territory2ModelId

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The user interface label for the territory type.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The object that the rule is defined for. For API version 31, Account only.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the territory model.

### ObjectTerritory2AssignmentRuleItem

A single row of selection criteria for an ObjectTerritory2AssignmentRule object. ObjectTerritory2AssignmentRuleItem can only be created
or deleted if the `BooleanFilter` field on its corresponding ObjectTerritory2AssignmentRule object is a `null` value. Available if
Sales Territories has been enabled.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Standard users can access this object. If a territory model is in `Active` state, any standard user can view that model, including its
territories and assignment rules. For territories in an active model, any standard user can view assigned records and assigned users subject
to your Salesforce sharing settings. Users cannot view territory models in other states (such as `Planning` or `Archived` ).


Standard Objects ObjectTerritory2AssignmentRuleItem

Fields

**Field Name** **Details**

```
Field

Operation

RuleId

SortOrder

Value

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The standard or custom object field that the rule item will operate on.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The criterion to apply for the rule item. For example: _`equals`_, _`notContain`_,
or _`startsWith`_ .

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the associated ObjectTerritory2AssignmentRule.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The order in which this row is evaluated in relation to other
ObjectTerritoryAssignmentRuleItem objects for the given
ObjectTerritoryAssignmentRule. This field is required for assignment rule items,
which are used in the Boolean conditions in assignment rule formulas.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The field value or values to evaluate. For example: if the field is `Billing`
`ZIP/Postal Code`, a value might be `94105` .


### Standard Objects ObjectTerritory2Association ObjectTerritory2Association

Represents an association (by assignment) between a territory and an object record such as an account or a lead.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Available after enabling Sales Territories.

Standard and partner users can access this object. If a territory model is in `Active` state, any standard or partner user can view that
model, including its territories and assignment rules. For territories in an active model, any standard or partner user can view assigned
records and assigned users subject to your sharing settings.

If you delete associations, you can query them for up to 12 hours. Keep in mind that deleted associations bypass the recycle bin.

Fields

**Field Name** **Details**

```
AssociationCause

ObjectId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The means by which the record was associated with the territory. User interface
field label is `Method` .

Possible values are:

**•** `Territory2AssignmentRule` —Territory assignment rule association

**•** `Territory2Manual` —Manual association

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the object assigned to the territory.


### Standard Objects ObjectUserTerritory2View

**Field Name** **Details**

This is a polymorphic relationship field.

**Relationship Name**
### Object

**Relationship Type**
Lookup

**Refers To**
Account

Lead

```
SobjectType

Territory2Id

### ObjectUserTerritory2View

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of the object.

Possible values are:

**•** `Account`

**•** `Lead`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the territory that the record is assigned to.

This is a relationship field.

**Relationship Name**
Territory2

**Relationship Type**
Lookup

**Refers To**
Territory2

Represents a user and object, such as an account or lead, assigned to a territory. This object is available in API version 58.0 and later.


Standard Objects ObjectUserTerritory2View

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

To see this object, enable Sales Territories.

Fields

**Field** **Details**

```
ObjectId

RoleInTerritory2

Territory2Id

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Required field for querying ObjectUserTerritory2View.

ID of the object that the territory user is assigned to.

This field is a polymorphic relationship field.

**Relationship Name**
Object

**Refers To**
Account, Lead

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
Role of the user assigned to the territory.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the territory to which the object and user are assigned.

This field is a relationship field.

**Relationship Name**
Territory2

**Refers To**
Territory2


### Standard Objects OmniSupervisorConfig

**Field** **Details**

```
UserId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the user assigned to the territory.

This field is a relationship field.

**Relationship Name**
User

**Refers To**
User

### OmniSupervisorConfig

Represents the Command Center for Service configuration for an assigned group of supervisors. This object is available in API version
41.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve() update()`, `upsert()`

Special Access Rules

[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

As of Spring ’20 and later, only authenticated internal and external users can access this object.

Fields

**Field** **Details**

```
DeveloperName

```

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.


Standard Objects OmniSupervisorConfig

**Field** **Details**

In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance slows down while
Salesforce generates one for each record.

```
IsTimelineHidden

Language

MasterLabel

SkillVisibility

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If set to `true`, hides the agent timeline from the supervisors assigned to this Command
Center for Service configuration. The default value is `false` .

This field is available in API version 53.0 and later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The language of this Command Center for Service configuration.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
A unique label name for this Command Center for Service configuration. The name must
begin with a letter. The name can contain alphanumeric characters and underscores. The
name can’t contain spaces, two consecutive underscores, or end with an underscore. The
name appears as Command Center for Service Configuration Name in the UI.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

Determines which work items based on skills are visible to the supervisors assigned to this
Command Center for Service configuration. Possible values are:

**•** `AllSkills`  - Show work items with all skill requirements selected in this Command
Center for Service configuration.


### Standard Objects OmniSupervisorConfigAction

**Field** **Details**

**•** `AnySkill`                   - Show work items with at least one skill requirement selected in this
Command Center for Service configuration.

This field is available in API version 53.0 and later.

### OmniSupervisorConfigAction

Represents the actions available to the supervisors of a Command Center for Service configuration. This object is available in API version
56.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

Only authenticated internal and external users can access this object.

Fields

**Field** **Details**

```
DisplayOrder

OmniSupervisorActionType

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The order in which the action is displayed.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
An action that a supervisor can perform.

Possible values are:

**•** `AgentDetails.CustomAction`

**•** `AllAgents.AWSDashboard` —All Agents - View Amazon Real-Time Metrics

**•** `AllAgents.AssignLearning`

**•** `AllAgents.ChangeQueues`


### Standard Objects OmniSupervisorConfigGroup

**Field** **Details**

**•** `AllAgents.ChangeSkills`

**•** `AllAgents.CustomAction`

**•** `AssignedWork.AWSDashboard` —Assigned Work - View Amazon Real-Time
Metrics

**•** `AssignedWork.CustomAction`

**•** `AssignedWorkDetails.CustomAction`

**•** `QueueDetails.CustomAction`

**•** `QueuesBacklog.AWSDashboard` —Queues Backlog - View Amazon Real-Time
Metrics

**•** `QueuesBacklog.CustomAction`

**•** `QueuesBacklog.ManageQueues` —Queues Backlog - Assign Agents to Queues

**•** `SkillDetails.CustomAction`

**•** `SkillsBacklog.AWSDashboard` —Skills Backlog - View Amazon Real-Time
Metrics

**•** `SkillsBacklog.CustomAction`

```
OmniSupervisorConfigId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
A unique identifier for the Command Center for Service configuration.

This field is a relationship field.

**Relationship Name**
### OmniSupervisorConfig

**Relationship Type**
Lookup

**Refers To**
### OmniSupervisorConfig

### OmniSupervisorConfigGroup

Represents the group of reps who are visible to the supervisors of a Command Center for Service configuration. The group, if visible,
appears in the Agents tab of Command Center for Service. This object is available in API version 41.0 and later.

Supported Calls

`create()`, `delete()`, `query()`, `update()`, `retrieve()`


### Standard Objects OmniSupervisorConfigProfile

Special Access Rules

[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

As of Spring ’20 and later, only authenticated internal and external users can access this object.

Fields

**Field** **Details**

```
GroupId

OmniSupervisorConfigId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
A unique identifier for the group of reps that’s made visible to the supervisors who are
assigned to the Command Center for Service configuration.

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
Create, Filter, Group, Sort

**Description**
A unique identifier for the Command Center for Service configuration.

This is a relationship field.

**Relationship Name**
### OmniSupervisorConfig

**Relationship Type**
Lookup

**Refers To**
### OmniSupervisorConfig

### OmniSupervisorConfigProfile

Represents the supervisor profiles to which a Command Center for Service configuration applies. User-level configurations override
profile-level configurations. This object is available in API version 41.0 and later.


Standard Objects OmniSupervisorConfigProfile

Supported Calls

`create()`, `delete()`, `query()`, `update()`, `retrieve()`

Special Access Rules

[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

As of Spring ’20 and later, only authenticated internal and external users can access this object.

Fields

**Field** **Details**

```
OmniSupervisorConfigId

ProfileId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
A unique identifier for the Command Center for Service configuration.

This is a relationship field.

**Relationship Name**
OmniSupervisorConfig

**Relationship Type**
Lookup

**Refers To**
OmniSupervisorConfig

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
A unique identifier for the profile that’s associated with this Command Center for Service
configuration. A profile can be associated with only one Command Center for Service
configuration. This field is unique within your org.

This is a relationship field.

**Relationship Name**
Profile

**Relationship Type**
Lookup

**Refers To**
Profile


### Standard Objects OmniSupervisorConfigQueue OmniSupervisorConfigQueue

Represents the queues that are visible to the supervisors of a Command Center for Service configuration. The queue, if visible, appears
in the Queues Backlog and Assigned Work tabs of Command Center for Service. This object is available in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

Only authenticated internal and external users can access this object.

Fields

**Field** **Details**

```
OmniSupervisorConfigId

QueueId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
om

A unique identifier for the Command Center for Service configuration.

This is a relationship field.

**Relationship Name**
### OmniSupervisorConfig

**Relationship Type**
Lookup

**Refers To**
### OmniSupervisorConfig

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
A unique identifier for the queue that’s made visible to the supervisors who are assigned to
the Command Center for Service configuration.

This is a relationship field.


### Standard Objects OmniSupervisorConfigSkill

**Field** **Details**

**Relationship Name**
Queue

**Relationship Type**
Lookup

**Refers To**
Group

### OmniSupervisorConfigSkill

Represents the skills that are visible to the supervisors of a Command Center for Service configuration. These skills, if visible, appear in
the Skills Backlog tab of Command Center for Service. This object is available in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

Only authenticated internal and external users can access this object.

Fields

**Field** **Details**

```
OmniSupervisorConfigId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
A unique identifier for the Command Center for Service configuration.

This is a relationship field.

**Relationship Name**
### OmniSupervisorConfig

**Relationship Type**
Lookup

**Refers To**
### OmniSupervisorConfig


### Standard Objects OmniSupervisorConfigTab

**Field** **Details**

```
SkillId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
A unique identifier for the skill that’s made visible to the supervisors who are assigned to the
Command Center for Service configuration.

This is a relationship field.

**Relationship Name**
Skill

**Relationship Type**
Lookup

**Refers To**
Skill

### OmniSupervisorConfigTab

Represents the visible tabs specified in a Command Center for Service configuration. This object is available in API version 60.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

Only authenticated internal and external users can access this object.

Fields

**Field** **Details**

```
DisplayOrder

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The order in which tabs are displayed in Command Center for Service.


### Standard Objects OmniSupervisorConfigUser

**Field** **Details**

```
OmniSupervisorConfigId

OmniSupervisorTabType

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
A unique identifier for the Command Center for Service configuration.

This is a relationship field.

**Relationship Name**
### OmniSupervisorConfig

**Relationship Type**
Lookup

**Refers To**
### OmniSupervisorConfig

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Tabs shown on the Command Center for Service page. Possible values are:

**•** `Agents`  - the Agents tab

**•** `AssignedWork`  - the Assigned Work tab

**•** `FlexiPageType`  - A custom tab created using Lightning App Builder, with the
`OmniSupervisorPageType` value of the `FlexiPage Type` field

**•** `QueuesBacklog`  - the Queues Backlog tab

**•** `SkillsBacklog`  - the Skills Backlog tab

**•** `Wallboard`  - the Wallboard tab

### OmniSupervisorConfigUser

Represents the users to whom a Command Center for Service configuration applies. User-level configurations override profile-level
configurations. This object is available in API version 41.0 and later.

Supported Calls

`create()`, `delete()`, `query()`, `update()`, `retrieve()`

Special Access Rules

[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)


### Standard Objects OpenActivity

As of Spring ’20 and later, only authenticated internal and external users can access this object.

Fields

**Field** **Details**

```
OmniSupervisorConfigId

UserId

### OpenActivity

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
A unique identifier for the Command Center for Service configuration.

This is a relationship field.

**Relationship Name**
OmniSupervisorConfig

**Relationship Type**
Lookup

**Refers To**
OmniSupervisorConfig

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
A unique identifier for the user associated with this Command Center for Service configuration.
A user can be associated with only one Command Center for Service configuration. This field
is unique within your org.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

This read-only object is displayed in a related list of open activities—future events and open tasks—related to an object. It includes
activities for all contacts related to the object. OpenActivity fields for phone calls are only available if your organization uses Salesforce
CRM Call Center.


Standard Objects OpenActivity

Supported Calls

```
   describeSObjects()

```

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

**•** The date of an event if `IsAllDayEvent` is set to `true`

This field has a time stamp that is always set to midnight in the Universal Time Coordinated
(UTC) time zone. The time stamp doesn’t represent the time of the activity; don’t attempt
to alter it to accommodate time zone differences. Label is `Date` .

**Type**
dateTime

**Properties**
Aggregate, Filter, Nillable, Sort


Standard Objects OpenActivity

**Field** **Details**

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

**Description**
The ID of a record the activity is related to which contains more details about the activity.
For example, an activity can be related to an EmailMessage record.


Standard Objects OpenActivity

**Field** **Details**

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

CompletedDateTime

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
Filter, Group,Nillable, Sort

**Description**

Name of a call center. Limit is 255 characters.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

The type of call being answered: Inbound, Internal, or Outbound.

**Type**
dateTime


Standard Objects OpenActivity

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The date and time the task was saved with a Closed status. This value is always null.

```
ConnectionReceivedId

ConnectionSentId

Description

DurationInMinutes

EndDateTime

```

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


Standard Objects OpenActivity

**Field** **Details**

**Description**
Indicates the end date and time of the event or task. Available in versions 27.0 and later. This
field is optional, depending on the following:

**•** If `IsAllDayEvent` is true, you can supply a value for either `DurationInMinutes`
or `EndDateTime` . Supplying values in both fields is allowed if the values add up to
the same amount of time. If both fields are `null`, the duration defaults to one day.

**•** If `IsAllDayEvent` is false, a value must be supplied for either
`DurationInMinutes` or `EndDateTime` . Supplying values in both fields is allowed
if the values add up to the same amount of time.

```
IsAllDayEvent

IsClosed

IsDeleted

IsHighPriority

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If the value of this field is set to `true`, then the activity is an event spanning a full day, and
the `ActivityDate` defines the date of the event. If the value of this field is set to `false`,
then the activity may be an event spanning less than a full day, or it may be a task. The default
value of this field is `false` . Label is `All-Day Event` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a task is closed ( `true` ) or not closed ( `false` ). The default value of this
field is `false` . This field is set indirectly by setting `Status` on the task—each picklist
value has a corresponding `IsClosed` value. Label is `Closed` .

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the activity has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is `Deleted` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects OpenActivity

**Field** **Details**

**Description**
Indicates a high-priority task. The default value of this field is `false` . This field is derived
from the `Priority` field.

```
IsReminderSet

IsTask

IsVisibleInSelfService

Location

OwnerId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a reminder is set for an activity ( `true` ) or not ( `false` ). The default value
of this field is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If the value of this field is set to `true`, then the activity is a task; if the value is set to `false`,
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
If the activity is an event, then this field represents the location of the event. If the activity is
a task, then the value is `null` .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the ID of the user or group who owns the activity.


Standard Objects OpenActivity

**Field** **Details**

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Calendar, Group, User

```
PrimaryAccountId

PrimaryWhoId

Priority

ReminderDateTime

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Contains the `AccountId` value from the activity record. Available in API versions 30.0 and
later to organizations that use Shared Activities.

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
Represents the time at which a reminder is scheduled to fire if `IsReminderSet` is set to
`true` . If `IsReminderSet` is set to `false`, then either the user has deselected the
reminder checkbox in the user interface or the reminder has already fired at the time indicated
by the value.


Standard Objects OpenActivity

**Field** **Details**

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
Indicates the current status of a task. The default value of this field is `Not Started` . Each
predefined status field sets a value for `IsClosed` . To obtain picklist values, query the
TaskStatus object.

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


Standard Objects OpenActivity

**Field** **Details**

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

This is a polymorphic relationship field.

**Relationship Name**
Who

**Relationship Type**
Lookup

**Refers To**
Contact, Lead


### Standard Objects OperatingHours

Usage

**Query activities that are related to an object**

**1.** Optionally, issue a describe call against the object whose activities you want to query, to get a suggestion of the correct SOQL
query to use.

**2.** Issue a SOQL relationship query with a main clause that references the object and an inner clause that references the activity
history. For example:

```
       SELECT

        (SELECT ActivityDate, Description

         FROM OpenActivities)

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

         FROM OpenActivities

         ORDER BY ActivityDate ASC NULLS LAST, LastModifiedDate DESC

         LIMIT 500)

       FROM Account

       WHERE Name = 'Acme'

       LIMIT 1

```

**•** In the inner clause of the query, you can’t use `WHERE` .

**•** In the inner clause of the query, you must specify a limit of 500 or fewer on the number of rows that are returned in the list.

**•** In the inner clause of the query, you must sort on `ActivityDate` in ascending order and `LastModifiedDate` in
descending order. You can optionally display nulls last. For example: `ORDER BY ActivityDate ASC NULLS LAST,`
`LastModifiedDate DESC` .

SEE ALSO:

Task

### OperatingHours

Represents the hours in which a service territory, service resource, or account is available for work. OperatingHours is used by Field
Service, Salesforce Scheduler, Salesforce Meetings, Sales Engagement, and Workforce Engagement. This object is available in API version
38.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects OperatingHours

Fields

**Field Name** **Details**

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
The description of the operating hours. Add any details that aren’t included in
the name.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the operating hours record was last modified. Its label in the user
interface is `Last Modified Date` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the operating hours record was last viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the operating hours. For example, _`Summer Hours`_, _`Winter`_
_`Hours`_, or _`Peak Season Hours`_ .

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the operating hours record.

This field is available in API version 59.0.

This field is a polymorphic relationship field.


### Standard Objects OperatingHoursHistory

**Field Name** **Details**

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

```
TimeZone

```

Usage

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The time zone that the operating hours fall within.

By default, only System Administrators can view, create, and assign operating hours.

Service territory members—which are service resources who can work in the territory—automatically use their service territory’s operating
hours. If a resource needs different operating hours than their territory, create separate operating hours for them from the Operating
Hours tab. Then, select the desired hours in the `Operating Hours` lookup field on the service territory member detail page.

To view a service resource’s operating hours for a particular territory, navigate to their Service Territories related list and click the Member
Number for the territory. You reach the service territory member detail page, which lists the member’s operating hours and dates during
which they belong to the territory.

Associated Objects

This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**[OperatingHoursChangeEvent (API version 54.0)](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/sforce_api_associated_objects_change_event.htm)**
Change events are available for the object.

### **OperatingHoursHistory (API version 62.0)**

History is available for tracked fields of the object.

### OperatingHoursHistory

Represents the history of changes made to tracked fields on an operating hours record. This object is available in API version 38.0 and
later.

Supported Calls

`getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)


Standard Objects OperatingHoursHistory

Special Access Rules

Field Service must be enabled in your organization, and field tracking for operating hours fields must be configured.

Fields

**Field Name** **Details**

```
DataType

Field

NewValue

OldValue

TimeSlotId

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
ID of the operating hours record being tracked. The history is displayed on the
detail page for this record.


### Standard Objects OperatingHoursHoliday OperatingHoursHoliday

Represents the day or hours for which a service territory and service resources exclusive to the service territory are unavailable in Salesforce
Scheduler. This object is available in API version 54.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `update()`, `upsert()`

Special Access Rules

Salesforce Scheduler must be enabled.

Fields

**Field** **Details**

```
DateAndTime

HolidayId

LastReferencedDate

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
(Read-Only) The date or time for the holiday.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the holiday that’s related to the operating hours indicated in the OperatingHoursId
field.

This is a relationship field.

**Relationship Name**
Holiday

**Relationship Type**
Lookup

**Refers To**
Holiday

**Type**
dateTime


### Standard Objects Opportunity

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the current user last viewed a record related to this object.

```
LastViewedDate

OperatingHoursHolidayNumber

OperatingHoursId

### Opportunity

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
(Read-Only) An auto-generated number identifying the operating hours holiday.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the operating hours that’s related to the holiday indicated in the HolidayId field.

This is a relationship field.

**Relationship Name**
OperatingHours

**Relationship Type**
Lookup

**Refers To**
OperatingHours

Represents an opportunity, which is a sale or pending deal.


Standard Objects Opportunity

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Field Type**

```
AccountId

ActivityMetricId

ActivityMetricRollupId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the account associated with this opportunity.

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

**Description**
When Einstein Activity Capture with Activity Metrics is enabled, the ID of the related activity
metric rollup.


Standard Objects Opportunity

**Field** **Field Type**

This field is a relationship field.

**Relationship Name**
ActivityMetricRollup

**Refers To**
ActivityMetricRollup

```
AgeInDays

Amount

CampaignId

```

**Type**
int

**Properties**
Aggregate, Filter, Group, Nillable, Sort

**Description**
The number of days since the opportunity was created, calculated by the current date minus
the `created_date` field. This field is available in API version 52.0 and later if you enabled
Pipeline Inspection.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Estimated total sale amount. For opportunities with products, the amount is the sum of the
related products. Any attempt to update this field, if the record has products, will be ignored.
The update call will not be rejected, and other fields will be updated as specified, but the
Amount will be unchanged.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of a related Campaign. This field is defined only for those organizations that have the
campaign feature Campaigns enabled. The User must have read access rights to the
cross-referenced Campaign object in order to create or update that campaign into this field
on the opportunity.

This is a relationship field.

**Relationship Name**
Campaign

**Relationship Type**
Lookup

**Refers To**
Campaign


Standard Objects Opportunity

**Field** **Field Type**

```
CloseDate

ConnectionReceivedId

ConnectionSentId

ContactId

ContractId

```

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. Date when the opportunity is expected to close.

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
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the contact associated with this opportunity, set as the primary contact. Read-only field
that is derived from the opportunity contact role, which is created at the same time the
opportunity is created. This field can only be populated when it’s created, and can’t be
updated. To update the value in this field, change the `IsPrimary` flag on the
OpportunityContactRole associated with this opportunity. Available in API version 46.0 and
later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects Opportunity

**Field** **Field Type**

**Description**
ID of the contract that’s associated with this opportunity.

This is a relationship field.

**Relationship Name**
Contract

**Relationship Type**
Lookup

**Refers To**
Contract

```
CurrencyIsoCode

Description

ExpectedRevenue

ExportStatus

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for organizations with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.

If the organization has multicurrency and a Pricebook2 is specified on the opportunity (that
is, the `Pricebook2Id` field is not blank), then the currency value of this field must match
the currency of the PricebookEntry records that are associated with any opportunity line
items it has.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Text description of the opportunity. Limit: 32,000 characters.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Read-only field that is equal to the product of the opportunity `Amount` field and the
`Probability` . You can’t directly set this field, but you can indirectly set it by setting the
`Amount` or `Probability` fields.

**Type**
picklist

**Properties**
Filter, Restricted picklist, Sort


Standard Objects Opportunity

**Field** **Field Type**

**Description**
Derived field for the record map for Partner Connect. The export status of this opportunity
to the partner’s connected org. To see this field, enable Partner Connect and add the Export
Vendor Records to an Authorized Partner Org user permission to the cosell export user. See
[Set Up Partner Connect as a Vendor in](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_vendor_parent.htm&type=5&language=en_US) _Salesforce Help_ . Available in API version 62.0 and later.

```
Fiscal

FiscalQuarter

FiscalYear

ForecastCategory

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If fiscal years are not enabled, the name of the fiscal quarter or period in which the opportunity
`CloseDate` falls. Use YYYY Q format, for example, '2006 1' for first quarter of 2006.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the fiscal quarter. Valid values are 1, 2, 3, or 4.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the fiscal year, for example, 2006.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Restricted picklist field. It is implied, but not directly controlled, by the `StageName` field.
You can override this field to a different value than is implied by the `StageName` value.
The values of this field are fixed enumerated values. The field labels are localized to the
language of the user performing the operation, if localized versions of those labels are
available for that language in the user interface.

In API version 12.0 and later, the value of this field is automatically set based on the value of
the `ForecastCategoryName` and can’t be updated any other way. The field properties
Create, Defaulted on create, Nillable, and Update are not available in version 12.0.

Possible values are:


Standard Objects Opportunity

**Field** **Field Type**

**•** `BestCase`

**•** `Closed`

**•** `Forecast`

**•** `MostLikely`

**•** `Omitted`

**•** `Pipeline`

```
ForecastCategoryName

HasOpenActivity

HasOpportunityLineItem

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The name of the forecast category. It is implied, but not directly controlled, by the
`StageName` field. You can override this field to a different value than is implied by the
`StageName` value. Available in API version 12.0 and later.

Possible values are:

**•** `Best Case`

**•** `Closed`

**•** `Commit`

**•** `Most Likely`

**•** `Omitted`

**•** `Pipeline`

**Type**
boolean

**Properties**
Defaulted on create, Group,

**Description**
Indicates whether an opportunity has an open event or task ( `true` ) or not ( `false` ). Available
in API version 35.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read-only field that indicates whether the opportunity has associated line items. A value of
`true` means that Opportunity line items have been created for the opportunity. An
opportunity can have opportunity line items only if the opportunity has a price book. The
opportunity line items must correspond to PricebookEntry objects that are listed in the
opportunity Pricebook2. However, you can insert opportunity line items on an opportunity


Standard Objects Opportunity

**Field** **Field Type**

that does not have an associated Pricebook2. For the first opportunity line item that you
insert on an opportunity without a Pricebook2, the API automatically sets the
`Pricebook2Id` field, if the opportunity line item corresponds to a PricebookEntry in an
active Pricebook2 that has a `CurrencyIsoCode` field that matches the
`CurrencyIsoCode` field of the opportunity. If the Pricebook2 is not active or the
`CurrencyIsoCode` fields do not match, then the API returns an error. You can’t update
the `Pricebook2Id` or `PricebookId` fields if opportunity line items exist on the
Opportunity. You must delete the line items before attempting to update the
`PricebookId` field.

```
HasOverdueTask

IqScore

IsClosed

IsDeleted

```

**Type**
boolean

**Properties**
Defaulted on create, Group,

**Description**
Indicates whether an opportunity has an overdue task ( `true` ) or not ( `false` ). Available in
API version 35.0 and later.

**Type**
int

**Properties**
Aggregate, Filter, Group, Nillable, Sort

**Description**
The likelihood, measured on a scale of 1 to 99, that an opportunity will be won. Einstein
Opportunity Scoring must be enabled. Available in API version 41.0 and later. Label is
**Opportunity Score** .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Directly controlled by `StageName` . You can query and filter on this field, but you can’t
directly set it in a create, upsert, or update request. It can only be set via `StageName` . Label
is **Closed** .

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is **Deleted** .


Standard Objects Opportunity

**Field** **Field Type**

```
IsExcludedFromTerritory2Filter

IsPriorityRecord

IsPrivate

IsSplit

IsWon

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Used for Filter-Based Opportunity Territory Assignment (Pilot in Spring ’15 / API version 33).
Indicates whether the opportunity is excluded ( _`True`_ ) or included ( _`False`_ ) each time the
APEX filter is executed.

**Type**
boolean

**Properties**
Defaulted on create, Group

**Description**
Shows whether the user has marked the opportunity as important ( _`True`_ ) or not ( _`False`_ ).
The default value is `false` . Available in API version 53.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If _`true`_, only the opportunity owner, users above that role in the hierarchy, and admins can
view the opportunity or query it via the API. When you mark opportunities as private,
opportunity teams, opportunity splits, and sharing are removed. Label is **Private** . The default
value is _`False`_ .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read-only field that indicates whether credit for the opportunity is split between opportunity
team members. Label is `IsSplit` . This field is available in versions 14.0 and later for
organizations that enabled Opportunity Splits during the pilot period.

This field should not be used. However, it’s documented for the benefit of pilot customers
who find references to `IsSplit` in code.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects Opportunity

**Field** **Field Type**

**Description**
Directly controlled by `StageName` . You can query and filter on this field, but you can’t
directly set the value. It can only be set via `StageName` . Label is **Won** .

```
LastActivityDate

LastActivityInDays

LastAmountChangedHistoryId

LastCloseDateChangedHistoryId

```

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Value is one of the following, whichever is the most recent:

**•** Due date of the most recent event logged against the record.

**•** Due date of the most recently closed task associated with the record.

**Type**
int

**Properties**
Aggregate, Filter, Group, Nillable, Sort

**Description**
The number of days since the last completed event or task for the record, calculated by the
current date minus the `last_activity` field. If the `last_activity` field is null,
this field is null. This field is available in API version 52.0 and later if you enabled Pipeline
Inspection.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the OpportunityHistory record that contains information about when the opportunity
Amount field was last updated in Winter ’21 or later. Information includes the date and time
of the change and the user who made the change. Available in API version 50.0 and later.

This is a relationship field.

**Relationship Name**
LastAmountChangedHistory

**Relationship Type**
Lookup

**Refers To**
OpportunityHistory

**Type**
reference


Standard Objects Opportunity

**Field** **Field Type**

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the OpportunityHistory record that contains information about when the opportunity
Close Date field was last updated in Winter ’21 or later. Information includes the date and
time of the change and the user who made the change. Available in API version 50.0 and
later.

This is a relationship field.

**Relationship Name**
LastCloseDateChangedHistory

**Relationship Type**
Lookup

**Refers To**
OpportunityHistory

```
LastReferencedDate

LastStageChangeDate

LastStageChangeInDays

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
Aggregate, Filter, Nillable, Sort

**Description**
The date of the last change made to the `Stage` field on this opportunity record. This field
is available in API version 52.0 and later.

**Type**
int

**Properties**
Aggregate, Filter, Group, Nillable, Sort

**Description**
The number of days since the last change was made to the `Stage` field on the opportunity
record, calculated by the current date minus the `last_stage_change_date` field. If
the `last_stage_change_date` is null, then this field contains the value for
`AgeInDays` . This field is available in API version 52.0 and later if you enabled Pipeline
Inspection.


Standard Objects Opportunity

**Field** **Field Type**

```
LastViewedDate

LeadSource

Name

NextStep

OwnerId

```

**Type**
datetime

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
Source of this opportunity, such as Advertisement or Trade Show.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. A name for this opportunity. Limit: 120 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of next task in closing opportunity. Limit: 255 characters.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the User who has been assigned to work this opportunity.

If you update this field, the previous owner's access becomes Read Only or the access specified
in your organization-wide default for opportunities, whichever is greater.

If you have set up opportunity teams in your organization, updating this field has different
consequences depending on your version of the API:


Standard Objects Opportunity

**Field** **Field Type**

**•** For API version 12.0 and later, sharing records are kept, as they are for all objects. (All
previous opportunity team members are kept on the opportunity team.)

**•** For API version before 12.0, sharing records are deleted. (All previous opportunity team
members are removed from the opportunity team.)

**•** For API version 16.0 and later, users must have the Transfer Record permission in order
to update (transfer) account ownership using this field.

This is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

```
PartnerAccountId

Pricebook2Id

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the partner account for the partner user that owns this opportunity. Available if Partner
Relationship Management is enabled or if digital experiences is enabled and you have partner
portal licenses.

If you are uploading opportunities using API version 15.0 or earlier, and one of the
opportunities in the batch has a partner user as the owner, the `Partner Account` field
on all opportunities in the batch is set to that partner user’s account regardless of whether
the partner user is the owner. In version 16.0, the `Partner Account` field is set to the
appropriate account for the partner user that owns the opportunity. If the owner of the
opportunity is not a partner user, this field remains empty.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
ID of a related Pricebook2 object. The `Pricebook2Id` field indicates which Pricebook2
applies to this opportunity. The `Pricebook2Id` field is defined only for those organizations
that have products enabled as a feature. You can specify values for only one field
( `Pricebook2Id` or `PricebookId` )—not both fields. For this reason, both fields are
declared nillable.

This is a relationship field.

**Relationship Name**
Pricebook2


Standard Objects Opportunity

**Field** **Field Type**

**Relationship Type**
Lookup

**Refers To**
Pricebook2

```
PricebookId

Probability

PushCount

RecordTypeId

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Nillable, Update

**Description**
Unavailable as of version 3.0. As of version 8.0, the Pricebook object is no longer available.
Use the `Pricebook2Id` field instead, specifying the ID of the Pricebook2 record.

**Type**
percent

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
Percentage of estimated confidence in closing the opportunity. It is implied, but not directly
controlled, by the `StageName` field. You can override this field to a different value than
what is implied by the `StageName` .

If you're changing the `Probability` field through the API using a partner WSDL call, or
an Apex `before` trigger, and the value may have several decimal places, we recommend
rounding the value to a whole number. For example, the following Apex in a `before`
trigger uses the `round` method to change the field value: `o.probability =`

```
  o.probability.round();

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times an opportunity’s close date has been pushed out by one calendar
month. For example, moving a close date from April to May counts as one push, but moving
from April 1 to April 30 doesn't count. The total is not decreased when the close date is
moved in. Available in API version 53.0 and later.

**Type**
reference

**Properties**
Create, Filter, Nillable, Update


Standard Objects Opportunity

**Field** **Field Type**

**Description**
ID of the record type assigned to this object.

```
StageName

SyncedQuoteID

Territory2Id

TotalOpportunityQuantity

```

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. Current stage of this record. The `StageName` field controls several other fields
on an opportunity. Each of the fields can be directly set or implied by changing the
`StageName` field. In addition, the `StageName` field is a picklist, so it has additional
members in the returned describeSObjectResult to indicate how it affects the other fields.
To obtain the stage name values in the picklist, query the OpportunityStage object. If the
`StageName` is updated, then the `ForecastCategoryName`, `IsClosed`, `IsWon`,
and `Probability` are automatically updated based on the stage-category mapping.

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
Read only in an Apex trigger. The ID of the Quote that syncs with the opportunity. Setting
this field lets you start and stop syncing between the opportunity and a quote. The ID has
to be for a quote that is a child of the opportunity.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the territory that is assigned to the opportunity. Available only if Enterprise Territory
Management has been enabled for your organization. Users who have full access to an
opportunity’s account can assign any territory from the active model to the opportunity.
Users who do _not_ can assign only a territory that is also assigned to the opportunity’s account.
The same restriction applies to territory assignments made via Apex in system mode.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Number of items included in this opportunity. Used in quantity-based forecasting.


Standard Objects Opportunity

**Field** **Field Type**

```
Type

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Type of opportunity. For example, Existing Business or New Business. Label is **Opportunity**
**Type** .

Note: When importing opportunity data, users need the Set Audit Fields upon Record Creation permission to assign values to
audit fields such as `CreatedDate` . Audit fields are automatically updated during API operations unless you set these fields
yourself.

Usage

Use the Opportunity object to manage information about a sale or pending deal. You can also sync this object with a child Quote. To
update an Opportunity, your client application needs Edit permission on opportunities. You can create, update, delete, and query
Attachment records associated with an opportunity via the API. To split credit for an opportunity among multiple opportunity team
members, use the OpportunitySplit object.

Client applications can also create or update opportunity objects by converting a Lead with `convertLead()` .

Note: On opportunities and opportunity products, the workflow rules, validation rules, and Apex triggers fire when an update to
a child opportunity product or schedule causes an update to the parent record. This means your custom application logic is
enforced when there are updates to the parent record, ensuring higher data quality and compliance with your organization’s
business policies.

Sample Code—Java

This code starts the sync between an object and a child quote.

```
public void startQuoteSync() {

      Opportunity opp = new Opportunity();

      opp.setId(new ID("006D000000CpOSy"));

      opp.setSyncedQuoteId(new ID("0Q0D000000002OZ"));

  // Invoke the update call and save the results

  try {

    SaveResult[] saveResults = binding.update(new SObject[] {opp});

    // check results and do more processing after the update call ...

  }

  catch (Exception ex) {

    System.out.println("An unexpected error has occurred." + ex.getMessage());

    return;

 }

}

```


Standard Objects Opportunity

This code stops the sync between an object and a child quote.

```
   public void stopQuoteSync() {

         Opportunity opp = new Opportunity();

         opp.setId(new ID("006D000000CpOSy"));

         opp.setFieldsToNull(new String[] {"SyncedQuoteId"} );

     // Invoke the update call and save the results

     try {

       SaveResult[] saveResults = binding.update(new SObject[] {opp});

       // check results and do more processing after the update call ...

     }

     catch (Exception ex) {

       System.out.println("An unexpected error has occurred." + ex.getMessage());

       return;

    }

   }

```

Associated Objects

This object has these associated objects. Unless noted, they are available in the same API version as this object.

**[OpportunityChangeEvent (API version 44.0)](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**
Change events are available for the object.

**[OpportunityFeed (API version 18.0)](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**
Feed tracking is available for the object.

**OpportunityHistory**

History is available for tracked fields of the object.

**OpportunityOwnerSharingRule**

Sharing rules are available for the object.

**OpportunityShare**

Sharing is available for the object.

Additional Considerations

If you are using `before` triggers to set `Stage` and `Forecast Category` for an opportunity record, the behavior is as follows:

**•** If you set `Stage` and `Forecast Category`, the opportunity record contains those exact values.

**•** If you set `Stage` but not `Forecast Category`, the `Forecast Category` value on the opportunity record defaults to
the one associated with trigger `Stage` .

**•** If you reset `Stage` to a value specified in an API call or incoming from the user interface, the `Forecast Category` value
should also come from the API call or user interface. If no value for `Forecast Category` is specified and the incoming `Stage`
is different than the trigger `Stage`, the `Forecast Category` defaults to the one associated with trigger `Stage` . If the trigger
`Stage` and incoming `Stage` are the same, the `Forecast Category` is not defaulted.

If you are cloning an opportunity with products, the following events occur in order:

Note: If errors occur on an opportunity product, you must return to the opportunity and fix the errors before cloning.

If any opportunity products contain unique custom fields, you must null them out before cloning the opportunity.

**•** [The parent opportunity is saved according to the order of execution.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_triggers_order_of_execution.htm)


### Standard Objects OpportunityCompetitor

**•** [The opportunity products are saved according to the order of execution.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_triggers_order_of_execution.htm)

SEE ALSO:

### OpportunityCompetitor

OpportunityHistory

OpportunityLineItem

OpportunityLineItemSchedule

OpportunityFieldHistory

Quote

QuoteLineItem

PartnerNetworkConnection

### OpportunityCompetitor

Represents a competitor on an Opportunity.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Fields

**Field** **Details**

```
CompetitorName

IsDeleted

OpportunityId

```

**Type**
combobox

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Name of the competitor.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is **Deleted** .

**Type**
reference


### Standard Objects OpportunityContactRole

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the associated Opportunity.

This is a relationship field.

**Relationship Name**
### Opportunity

**Relationship Type**
Lookup

**Refers To**
### Opportunity

```
 Strengths

 Weaknesses

```

Usage

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Description of the competitor’s strengths. Limit: 1,000 characters.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Description of the competitor’s weaknesses. Limit: 1,000 characters.

Use this object to manage competitors on an Opportunity, associating multiple competitors on a opportunity and specifying the strengths
and weaknesses of each competitor.

SEE ALSO:

### Opportunity OpportunityContactRole

Represents the role that a Contact plays on an Opportunity.


Standard Objects OpportunityContactRole

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ContactId

CurrencyIsoCode

Division

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of an associated Contact. The API applies user access rights to the associated Opportunity
for this object, but not to the associated Contact. The API may return rows from a query on
this object that include this field’s values for contacts to which the user does not have
sufficient access rights. It may also return values for this field for contacts that have been
deleted. In either case, the client must perform a query on the contact table for this field’s
value to determine whether the Contact is accessible to the user and has not been deleted.

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
Available only for orgs with the multicurrency feature enabled. Contains the ISO code for
any currency allowed by the org. This field is available in API version 47.0.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
A logical segment of your organization's data. For example, if your company is organized
into different business units, you could create a division for each business unit, such as “North


Standard Objects OpportunityContactRole

**Field** **Details**

America,” “Healthcare,” or “Consulting.” Available only if the organization has the Division
permission enabled.

```
IsDeleted

IsPrimary

OpportunityId

Role

```

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the record has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
The `IsDeleted` flag is usable only when the parent record is deleted to the recycle bin,
and not when the `OpportunityContactRole` record is deleted directly. Label is
**Deleted** .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the associated Contact plays the primary role on the Opportunity ( `true` )
or not ( `false` ). Each Opportunity has only one primary contact. Label is **Primary** .

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of an associated Opportunity. This field is non-nullable, and it cannot be updated.
You must provide a value for this field when creating new records. You can’t change it after
it has been created.

This is a relationship field.

**Relationship Name**
Opportunity

**Relationship Type**
Lookup

**Refers To**
Opportunity

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects OpportunityContactRoleSuggestionInsight

**Field** **Details**

**Description**
Name of the role played by the associated Contact on the Opportunity, such as Business
User or Decision Maker.

Usage

Use the Opportunity Contact Role object to manage information about contacts and roles related to opportunities. Records of this type
appear in the user interface in the Opportunity Contact Role related list and on the Opportunity detail page.

Although allowed, we do not recommend that you create multiple relationships between the same Opportunity and a Contact.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**OpportunityContactRoleChangeEvent (API version 45.0)**
Change events are available for the object.

SEE ALSO:

Overview of Salesforce Objects and Fields

### OpportunityContactRoleSuggestionInsight

Represents a suggestion for a new opportunity contact role. Available in API versions 45.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getDeleted()`, `query()`, `retrieve()`

Special Access Rules

To add or decline opportunity contact role suggestions, users need a Sales Cloud Einstein license, edit access on opportunities, and read
or edit access on contacts. As of the Spring ’20 release, Pardot and Sales Engagement users no longer have access to this object.

Fields

**Field Name** **Details**

```
ContactId

```

**Type**
reference

**Properties**
Filter, Group, Sort


Standard Objects OpportunityContactRoleSuggestionInsight

**Field Name** **Details**

**Description**
The ID of the related contact record.

```
CreatedRecordId

CurrencyIsoCode

Division

LastOperationUserId

LastReferencedDate

LastViewedDate

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the created opportunity contact role record.

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
The division of the suggested opportunity contact role.

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
The timestamp when the current user last interacted with this record, directly or
indirectly. Some sample scenarios are:

**Type**
dateTime


Standard Objects OpportunityContactRoleSuggestionInsight

**Field Name** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, it’s possible that the user only accessed this record or list view
( `LastReferencedDate` ), but not viewed it.

```
OpportunityId

RationaleLabel

Role

Status

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related opportunity.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The reason why this is a suggested opportunity contact role.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The role of the suggested opportunity contact role.

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


### Standard Objects OpportunityFieldHistory

Usage

This object is read-only and isn’t supported in workflows, triggers, or process builder.

### OpportunityFieldHistory

Represents the history of changes to the values in the fields of an opportunity. This object is available in versions 13.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Fields

**Field** **Details**

```
DataType

Field

IsDeleted

OpportunityId

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


### Standard Objects OpportunityHistory

**Field** **Details**

**Description**
ID of the Opportunity. Label is **Opportunity ID** .

This is a relationship field.

**Relationship Name**
### Opportunity

**Relationship Type**
Lookup

**Refers To**
### Opportunity

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

Use this object to identify changes to any fields on an Opportunity. The OpportunityHistory object represents the history of a change to
the `Amount`, `Probability`, `Stage`, or `Close Date` fields of an Opportunity.

This object respects field level security on the parent object.

SEE ALSO:

### Opportunity OpportunityHistory

Represents the stage history of an opportunity.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects OpportunityHistory

Fields

**Field** **Details**

```
Amount

CloseDate

ExpectedRevenue

ForecastCategory

IsDeleted

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Estimated total sale amount.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Date when the opportunity is expected to close.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Calculated revenue based on the `Amount` and `Probability` fields.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Category that determines the column in which an opportunity is totaled in a forecast. Label
is **To ForecastCategory** .

**•** `BestCase`

**•** `Closed`

**•** `Forecast`

**•** `MostLikely`

**•** `Omitted`

**•** `Pipeline`

**Type**
boolean

**Properties**
Defaulted on create, Filter


Standard Objects OpportunityHistory

**Field** **Details**

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is **Deleted** .

```
OpportunityId

PrevAmount

PrevCloseDate

Probability

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the associated Opportunity.

This is a relationship field.

**Relationship Name**
Opportunity

**Relationship Type**
Lookup

**Refers To**
Opportunity

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The value in the opportunity’s Amount field before the update of the opportunity. In
OpportunityHistory records created before Winter ’21, the value is null.Available in API version
50.0 and later.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The value in the opportunity’s Close Date field before the update of the opportunity. In
OpportunityHistory records created before Winter ’21, the value is null.Available in API version
50.0 and later.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
Percentage of estimated confidence in closing the opportunity.


### Standard Objects OpportunityInsight

**Field** **Details**

```
StageName

```

Usage

**Type**
picklist

**Properties**
Filter, Group, Sort

**Description**
Name of the current stage of the opportunity (for example, Prospect or Proposal).

This object represents the history of a change to the `Amount`, `Probability`, `Stage`, or `Close Date` fields of an Opportunity.
The OpportunityFieldHistory object represents the history of a change to any of the fields of an Opportunity. To obtain information about
how a particular opportunity is progressing, query the OpportunityHistory records associated with a given Opportunity. Please note that
if an opportunity's `Amount`, `Probability`, `Stage`, or `Close Date` fields have not changed, nothing will be returned in the
OpportunityHistory objects. In this case, query the OpportunityFieldHistory records associated with a given Opportunity to get more
information about changes to the opportunity.

This object is read-only. The system generates a new record whenever a user or client application changes the value of any of the above
fields; the then-current values of all of these major fields are saved in the newly-generated object.

This object respects field-level security on the parent object.

Note: The record is automatically deleted if its parent Opportunity is deleted.

SEE ALSO:

### Opportunity OpportunityInsight

Represents an individual insight (deal prediction, follow-up reminder, or key moment) related to an opportunity record.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `query()`, `retrieve()`

Special Access Rules

To see an insight related to a specific opportunity, users need a Sales Cloud Einstein license and access to the opportunity record. As of
the Spring ’20 release, Pardot and Sales Engagement users no longer have access to this object.


Standard Objects OpportunityInsight

Fields

**Field Name** **Details**

```
ActualHeardWithinDays

CloseDate

CompetitorName

ContactName

ContactTitle

CurrencyIsoCode

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of days it has been since a prospect has responded for insights of
type `Prospect has not responded` and `No communication` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The close date of the related opportunity for insights of type `Opportunity`
`is overdue` and `Opportunity is unlikely to close in`
`time` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field has been deprecated as of API version 45.0.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field is not in use as of API version 46.0.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field is not in use as of API version 46.0.

**Type**
picklist


Standard Objects OpportunityInsight

**Field Name** **Details**

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.

```
Division

ExpectedHeardWithinDays

LastHeard

LastReferencedDate

LastViewedDate

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The division of the related record.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The expected number of days it takes to hear back from a prospect for insights
of type `Prospect has not responded` and `No communication` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the related prospect was last heard from for insights of type
`Prospect has not responded` .

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


Standard Objects OpportunityInsight

**Field Name** **Details**

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, it’s possible that the user only accessed this record or list view
( `LastReferencedDate` ), but not viewed it.

```
OpportunityId

Rationale

Reason

TaskDue

Title

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related opportunity record.

**Type**
string

**Properties**
Filter, Group, Nillable

**Description**
The explanation for an insight, providing more background information and
details that are specific to the org.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The reason why a specific insight type is appearing. Relevant to the following
insights:

**•** Opportunity is unlikely to close in time

**•** Opportunity slowing

**•** Opportunity boosting

**•** Time-consuming opportunity

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that a task associated with the related opportunity record is due.

**Type**
string


Standard Objects OpportunityInsight

**Field Name** **Details**

**Properties**
Filter, Group, Nillable

**Description**
The title of the insight.

```
TrendType

Type

```

Usage

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The trend type of the insight. Possible values include:

**•** Negative

**•** Positive

**•** Informational

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of insight. Possible values include:

**•** Opportunity is unlikely to close in time

**•** Prospect has not responded

**•** Opportunity slowing

**•** Opportunity boosting

**•** Time-consuming opportunity

**•** No communication

**•** Re-engaged opportunity

**•** Opportunity has an overdue task

**•** Opportunity is overdue

**•** Opportunity has no open activity

**•** Unusual opportunity amount

This object is read-only and isn’t supported in workflows, triggers, or process builder.


### Standard Objects OpportunityLineItem OpportunityLineItem

Represents an opportunity line item, which is a member of the list of Product2 products associated with an Opportunity.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Special Access Rules

The user must have the “Edit” permission on Opportunity records to create or update opportunity line items on an opportunity.

Fields

**Field** **Details**

```
CanUseQuantitySchedule

CanUseRevenueSchedule

ConnectionReceivedId

ConnectionSentId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the opportunity product can have a quantity schedule ( `true` ) or not
( `false` ). This field is read-only.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the opportunity product can have a revenue schedule ( `true` ) or not
( `false` ). This field is read-only.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the PartnerNetworkConnection that shared this record with your organization. This
field is available if you enabled Salesforce to Salesforce.

**Type**
reference


Standard Objects OpportunityLineItem

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the PartnerNetworkConnection that you shared this record with. This field is available
if you enabled Salesforce to Salesforce. This field is supported using API versions earlier than
15.0. In all other API versions, this field’s value is null. You can use the new
PartnerNetworkRecordConnection object to forward records to connections.

```
CurrencyIsoCode

Description

Discount

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Available only for organizations with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.

If the organization has multicurrency enabled, and a Pricebook2 isn’tspecified on the parent
opportunity (that is, the `Pricebook2Id` field is blank on the opportunity referenced by
this object’s `OpportunityId` ), then the value of this field must match the currency of
the `CurrencyIsoCode` field on the PricebookEntry records that are associated with this
object.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Text description of the opportunity line item. Limit: 255 characters.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Discount for the product as a percentage.

When updating these records:

**•** If you specify `Discount` without specifying `TotalPrice`, the `TotalPrice` is
adjusted to accommodate the new `Discount` value, and the `UnitPrice` is held
constant.

**•** If you specify both `Discount` and `Quantity`, you must also specify either
`TotalPrice` or `UnitPrice` so the system knows which one to automatically
adjust.


Standard Objects OpportunityLineItem

**Field** **Details**

```
HasQuantitySchedule

HasRevenueSchedule

HasSchedule

LastReferencedDate

LastViewedDate

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read-only. Indicates whether a quantity schedule has been created for this object ( `true` )
or not ( `false` ).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a revenue schedule has been created for this object ( `true` ) or not
( `false` ).

If this object has a revenue schedule, the `Quantity` and `TotalPrice` fields can’t be
updated. In addition, the `Quantity` field can’t be updated if this object has a quantity
schedule. Update requests aren’t rejected but the updated values are ignored.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If either `HasQuantitySchedule` or `HasRevenueSchedule` is `true`, this field is
also `true` .

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record. Available
in API version 50.0 and later.

**Type**
datetime

**Properties**
Filter, Nillable, Sort


Standard Objects OpportunityLineItem

**Field** **Details**

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced (LastReferencedDate) and not viewed. Available in
API version 50.0 and later.

```
ListPrice

Name

OpportunityId

PricebookEntryId

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Corresponds to the `UnitPrice` on the PricebookEntry that is associated with this line
item, which can be in the standard price book or a custom price book. A client application
can use this information to show whether the unit price (or sales price) of the line item differs
from the price book entry list price.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The opportunity line item name (known as “Opportunity Product” in the user interface). This
read-only field is available in API version 30.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the associated Opportunity.

This is a relationship field.

**Relationship Name**
Opportunity

**Relationship Type**
Lookup

**Refers To**
Opportunity

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort


Standard Objects OpportunityLineItem

**Field** **Details**

**Description**
Required. ID of the associated PricebookEntry. Exists only for those organizations that have
Products enabled as a feature. In API versions 1.0 and 2.0, you can specify values for either
this field or `ProductId`, but not both. For this reason, both fields are declared nillable. In
API version 3.0 and later, you must specify values for this field instead of `ProductId` .

This is a relationship field.

**Relationship Name**
PricebookEntry

**Relationship Type**
Lookup

**Refers To**
PricebookEntry

```
ProductId

Product2Id

ProductCode

```

**Type**
reference

**Properties**
Create, Filter, Nillable

**Description**
ID of the related Product record. This field is unavailable as of version 3.0 and is only provided
for backward compatibility. The Product object is unavailable beginning with version 8.0.
Use the `PricebookEntryId` field instead, specifying the ID of the PricebookEntry record.

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
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the related Product2 record. This is a read-only field available in API version 30.0
and later.

Use the `PricebookEntryId` field instead, specifying the ID of the PricebookEntry record.

**Type**
string


Standard Objects OpportunityLineItem

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
This read-only field is available in API version 30.0 and later. It references the value in the
ProductCode field of the related Product2 record.

```
Quantity

RecalculateTotalPrice

ServiceDate

```

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
Read-only if this record has a quantity schedule, a revenue schedule, or both a quantity and
a revenue schedule.

When updating these records:

**•** If you specify `Quantity` without specifying the `UnitPrice`, the `UnitPrice`
value is adjusted to accommodate the new `Quantity` value, and the `TotalPrice`
is held constant.

**•** If you specify both `Discount` and Quantity, you must also specify either `TotalPrice`
or `UnitPrice` so the system can determine which one to automatically adjust.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Changes behavior of OpportunityLineItem calculations when a line item has child schedule
rows for the `Quantity` value. When enabled, if the rollup quantity changes, then the
quantity rollup value is multiplied against the sales price to change the total price. Product2
flag must be set to true.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Date when the product revenue will be recognized and the product quantity will be shipped.

**•** Opportunity Close Date— `ServiceDate` is ignored.

**•** Product Date— `ServiceDate` is used if not `null` .

**•** Schedule Date— `ServiceDate` is used if not `null` and there are no revenue
schedules present for this line item, that is, there are no OpportunityLineItemSchedule
records with a field `Type` value of Revenue that are children of this record.


Standard Objects OpportunityLineItem

**Field** **Details**

```
SortOrder

Subtotal

TotalPrice

UnitPrice

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number indicating the sort order selected by the user. Client applications can use this to
match the sort order in Salesforce.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Difference between standard and discounted pricing. Converted currency amounts when
the opportunity's currency is different from the user's currency.

**Type**
currency

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
This field is available only for backward compatibility. It represents the total price of the
OpportunityLineItem.

If you don’t specify `UnitPrice`, this field is required. If you specify `Discount` and
`Quantity`, this field or `UnitPrice` is required. When updating these records, you can
change either this value or the `UnitPrice`, but not both at the same time.

This field is nillable, but you can’t set both `TotalPrice` and `UnitPrice` to null in the
same update request. To insert the `TotalPrice` via the API (given only a unit price and
the quantity), calculate this field as the unit price multiplied by the quantity. This field is
read-only if the opportunity line item has a revenue schedule. If the opportunity line item
doesn’t have a schedule or only has a quantity schedule, this field can be updated.

**Type**
currency

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
The unit price for the opportunity line item. In the Salesforce user interface, this field’s value
is calculated by dividing the total price of the opportunity line item by the quantity listed for
that line item. Label is **Sales Price** .

This field or `TotalPrice` is required. You can’t specify both.

If you specify `Discount` and `Quantity`, this field or `TotalPrice` is required.


Standard Objects OpportunityLineItem

Usage

An Opportunity can have associated OpportunityLineItem records only if the Opportunity has a Pricebook2. An OpportunityLineItem
must correspond to a Product2 that is listed in the opportunity's Pricebook2. For information about inserting OpportunityLineItem for
an opportunity that doesn’t have an associated Pricebook2 or any existing line items, see Effects on Opportunities.

This object is defined only for orgs with products enabled as a feature. If the products feature isn’t enabled, this object doesn’t appear
in the `describeGlobal()` call, and you can’t use `describeSObjects()` or query the OpportunityLineItem object.

[For a visual diagram of the relationships between OpportunityLineItem and other objects, see the Product & Price Book diagram.](https://developer.salesforce.com/docs/platform/data-models/guide/product-price-book.html)

Note:

**•** If the multicurrency option is enabled, the `CurrencyIsoCode` field is present. It can’t be modified, and is always set to
the value of the `CurrencyIsoCode` of the parent Opportunity.

**•** If customizable product schedules are enabled, you can use custom fields in default schedules and customize their layout. But
if you’ve applied validation rules or Apex triggers, they’re bypassed when they’re first inserted.

Effects on Opportunities

Opportunities with associated OpportunityLineItem records are affected in the following ways:

**•** Creating an OpportunityLineItem increments the Opportunity `Amount` value by the `TotalPrice` of the OpportunityLineItem.
Additionally, inserting an OpportunityLineItem increments the `ExpectedRevenue` on the opportunity by the `TotalPrice`
times the opportunity `Probability` .

**•** The Opportunity `Amount` becomes a read-only field when the opportunity has line items. The API ignores any attempt to update
this field on an opportunity with line items. Update requests aren’t rejected, but the updated value is ignored.

**•** You can’t update the `PricebookId` field or the `CurrencyIsoCode` field on the opportunity if line items exist. The API rejects
any attempt to update these fields on an opportunity with line items.

**•** When you create or update an OpportunityLineItem, the API verifies that the line item corresponds to a PricebookEntry in the
Pricebook2 associated with the opportunity.

**–** If the opportunity has an associated active or inactive Pricebook2, the OpportunityLineItem is created or updated.

**–** If the opportunity doesn’t have an associated Pricebook2, but the OpportunityLineItem corresponds to a PricebookEntry in an
active Pricebook2 where the PricebookEntry has a `CurrencyIsoCode` value that matches the `CurrencyIsoCode`
value of the opportunity, the API automatically sets this PriceBook2 on the opportunity.

**–** If the opportunity doesn’t have an associated Pricebook2, but the line item corresponds to a PricebookEntry in a Pricebook2 that
isn’t active or that has a `CurrencyIsoCode` value that does not match the `CurrencyIsoCode` value of the opportunity,
an error is returned.

**•** The Opportunity `HasOpportunityLineItem` field is set to `true` when an OpportunityLineItem is inserted for that Opportunity.

**•** When OpportunityLineItem records are directly deleted, they aren’t sent to the recycle bin and can’t be undeleted. The
`getDeleted()` call shows deleted OpportunityLineItem records until they’re purged, which is usually within the same day or
the next day.

**•** In Lightning, the `ListPrice`, `Name`, and `ProductCode` fields aren’t populated before insert because their values are computed
after the OpportunityLineItem.Product2Id value is saved. To access a value from these fields, use an After Insert trigger.


### Standard Objects OpportunityLineItemSchedule

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[OpportunityLineItemChangeEvent (API version 60.0)](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**
Change events are available for the object.

SEE ALSO:

### OpportunityLineItemSchedule OpportunityLineItemSchedule Represents information about the quantity, revenue distribution, and delivery dates for a particular OpportunityLineItem .

In API version 38.0 and later, when an OpportunityLineItem record is created for a product with a previously established schedule, an
### OpportunityLineItemSchedule record is also created.

In API version 46.0 and later, this object supports custom fields, validation rules, and Apex triggers. Deleting a schedule now also invokes
delete triggers. If customizable product schedules are enabled, you can use custom fields in default schedules and customize their layout.
But if you’ve applied validation rules or Apex triggers, they’re bypassed when they’re first inserted.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Fields

**Field** **Details**

```
CurrencyIsoCode

Description

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Nillable, Restricted picklist, Update

**Description**
Available only for organizations with the multicurrency feature enabled.
Contains the ISO code for any currency allowed by the organization. This field
is available in version 10.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Text description of the opportunity line item schedule. Limit: 80 characters.
Label is **Comments** .


Standard Objects OpportunityLineItemSchedule

**Field** **Details**

```
OpportunityLineItemId

Quantity

Revenue

ScheduleDate

Type

```

**Type**
reference

**Properties**
Create, Filter

**Description**
Required. ID of the associated `OpportunityLineItem` .

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Required. The total number of units to be scheduled in a quantity schedule.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The revenue that should be recognized, or the quantity that should be
shipped, or both - depending upon the value of `Type` .

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The date the associated `OpportunityLineItem` is to be
scheduled for an event: delivery, shipping, or any other date you wish to track.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of the schedule. Required when inserting an
OpportunityLineItemSchedule. Valid values include `Quantity`, `Revenue`,
or `Both` .


Standard Objects OpportunityLineItemSchedule

Allowed Type Field Values

The allowed `Type` values for an `OpportunityLineItemSchedule` depend on the product-level schedule preferences and
whether the line item has any existing schedules. The following criteria must be met:

**•** The Product2 on which the `OpportunityLineItem` is based must have the appropriate `CanUseRevenueSchedule` or
`CanUseQuantitySchedule` fields (or both) set to `true` .

**•** When you create a schedule for a line item that does not have any existing schedules, you can specify any valid value.

**•** If you create a schedule for a line item that already has existing schedules, the new schedule must be consistent with the existing
schedules. The following matrix outlines the allowable values:

**Value of HasRevenueSchedule** **Value of HasQuantitySchedule** **Allowable Type Values**
**on line item** **on line item**

false false `Revenue`, `Quantity`, both

false true `Quantity`

true false `Revenue`

true true both

Allowed Quantity and Revenue Field Values

The allowable `Quantity` and `Revenue` field values depend on the value of the `Type` field:

**Type Value** **Allowable Quantity Value** **Allowable Revenue Value**

`Revenue` Null Non-null

`Quantity` Non-null Null

both Non-null Non-null

The `Quantity` and `Revenue` fields have the following restrictions when this object is updated:

**•** For a schedule of `Type Quantity`, you can’t update a null `Revenue` value to non-null. Likewise for a schedule of `Type`
`Revenue`, you can’t update a null `Quantity` value to non-null.

**•** You can’t null out the `Quantity` field for a schedule of `Type Quantity` . Likewise you can’t null out the `Revenue` field for
a schedule of `Type Revenue` .

**•** You can’t null out either the `Revenue` or `Quantity` fields for a schedule of type `Both` .

Usage

`OpportunityLineItemSchedule` supports two types of schedules:

**•** `Quantity` schedules

**•** `Revenue` schedules

The user must have edit access rights on the Opportunity in order to create or update line item schedules on that opportunity.


### Standard Objects OpportunityLineItemSplit

Products and Schedules Must Be Enabled

The `OpportunityLineItemSchedule` object is defined only for those organizations that have the products and schedules
features enabled. If the organization does not have the products and schedules features, the `OpportunityLineItemSchedule`
object is not returned in a describe, and you can't describe or query `OpportunityLineItemSchedule` records.

Effects on Opportunities and Opportunity Line Items

`OpportunityLineItemSchedule` records affect opportunities and opportunity line items in the following ways:

**•** Inserting an `OpportunityLineItemSchedule` of `Type` “Revenue” or “Quantity” increments the `TotalPrice` field on
### the OpportunityLineItem by the OpportunityLineItemSchedule Revenue amount. Inserting an

`OpportunityLineItemSchedule` of `Type Quantity` or `Both` increments the `Quantity` field on the
### OpportunityLineItem by the OpportunityLineItemSchedule Quantity amount.

**•** Creating an OpportunityLineItemSchedule record affects the original opportunity:

**1.** The Opportunity `Amount` is incremented the by `OpportunityLineItemSchedule` revenue amount

**2.** The Opportunity `ExpectedRevenue` is incremented by the line item schedule amount multiplied by the Opportunity

```
      Probability

### • Deleting an OpportunityLineItemSchedule has a similar effect on the related OpportunityLineItem and
```

Opportunity. Deleting an `OpportunityLineItemSchedule` decrements the `OpportunityLineItemTotalPrice`
by the deleted `OpportunityLineItemSchedule Quantity` or `Revenue` amount. The Opportunity `Amount` is also
decremented by the `OpportunityLineItemSchedule Quantity` or `Revenue` amount, and the Opportunity
`ExpectedRevenue` is reduced by `OpportunityLineItemSchedule Quantity` or `Revenue` amount multiplied
by the Opportunity `Probability` .

Deleting an Opportunity Line Item Schedule

Deleting the last remaining schedule will set the corresponding `HasQuantitySchedule` or `HasRevenueSchedule` flags (or
both) to `false` on the parent line item.

SEE ALSO:

### OpportunityLineItem

Product2

### OpportunityLineItemSplit

Represents information about an opportunity product split, including percentages, amounts, and owner. This object is available in API
version 58.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`


Standard Objects OpportunityLineItemSplit

Special Access Rules

Before creating OpportunityLineItemSplit records, enable Team Selling, set up opportunity splits, and enable product splits on at least
one opportunity split type in Setup.

Fields

**Field** **Details**

```
ArchivedTerritoryName

CurrencyIsoCode

OpportunityLineItemId

```

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the associated territory that’s on an archived territory model. If the
OpportunityLineItemSplit isn’t associated with a territory on an archived territory model, the
field value is null. This field is available in API version 62.0 and later.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Available only for organizations with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.

If the organization has multicurrency enabled, and a Pricebook2 is specified on the opportunity
(that is, the Pricebook2Id field isn’t blank on the opportunity referenced by this object’s
OpportunityId), then the value of this field must match the currency of the CurrencyIsoCode
field on the PricebookEntry records that are associated with this object.

Possible values are:

**•** `BRL` —Brazilian Real

**•** `CAD` —Canadian Dollar

**•** `EUR` —Euro

**•** `USD` —U.S. Dollar

The default value is `USD` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the associated parent OpportunityLineItem. This field is a relationship field.


Standard Objects OpportunityLineItemSplit

**Field** **Details**

**Relationship Name**
OpportunityLineItem

**Relationship Type**
Lookup

**Refers To**
OpportunityLineItem

```
Split

SplitAmount

SplitNote

SplitOwnerId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Read-only. Automatically generated number identifying the split within the opportunity.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The amount or value of the split.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Optional text about the split.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the user who is the owner of the split. This field is a relationship field.

**Relationship Name**
SplitOwner

**Relationship Type**
Lookup

**Refers To**
User


Standard Objects OpportunityLineItemSplit

**Field** **Details**

```
SplitPercentage

SplitTypeId

Territory2Id

```

Usage

**Type**
percent

**Properties**
Create, Filter, Sort, Update

**Description**
The percentage of the OpportunityLineItem's value that the split represents.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the associated OpptyLineItemSplitType. This field is a relationship field.

**Relationship Name**
SplitType

**Relationship Type**
Lookup

**Refers To**
OpptyLineItemSplitType

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the associated territory. This field is a relationship field, and is available in API version
62.0 and later.

**Relationship Name**
Territory2

**Relationship Type**
Lookup

**Refers To**
Territory2

Use the OpportunityLineItemSplit object to manage opportunity product splits for an opportunity.


### Standard Objects OpportunityOwnerSharingRule

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**OpportunityLineItemSplitHistory on page 63 (API version 59.0)**
History is available for tracked fields of the object.

### OpportunityOwnerSharingRule

Represents a rule for sharing an opportunity with users other than the owner.

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

```

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

This field is available in API version 24.0 and later.


Standard Objects OpportunityOwnerSharingRule

**Field** **Details**

When creating large sets of data, always specify a unique `DeveloperName` for
each record. If no `DeveloperName` is specified, performance slows down while
Salesforce generates one for each record.

```
GroupId

Name

OpportunityAccessLevel

UserOrGroupId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the source group. Opportunities owned by users in the source
group trigger the rule to give access.

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
A value that represents the type of sharing being allowed. The possible values are:

**•** `Read`

**•** `Edit`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the target user or group. The target user or group is being given
access.


### Standard Objects OpportunityPartner

Usage

Use this object to manage the sharing rules for opportunities. General sharing and Territory-related sharing use this object.

SEE ALSO:

Case

_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_sharingrules.htm)_ : SharingRules

### OpportunityPartner

This object represents a partner relationship between an Account and an Opportunity. An OpportunityPartner record is created
automatically when a Partner record is created for a partner relationship between an account and an opportunity.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Customer Portal users can't access this object.

Fields

**Field** **Details**

```
AccountToId

IsPrimary

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the partner Account in the partner relationship.

This is a relationship field.

**Relationship Name**
AccountTo

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort


Standard Objects OpportunityPartner

**Field** **Details**

**Description**
Indicates whether the account is the opportunity’s primary partner ( `true` ) or not ( `false` ).
Label is **Primary** .

```
OpportunityId

ReversePartnerId

Role

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the Opportunity that is in the partner relationship.

This is a relationship field.

**Relationship Name**
Opportunity

**Relationship Type**
Lookup

**Refers To**
Opportunity

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the reciprocal OpportunityPartner record in a partner relationship.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The UserRole that the Account has on the Opportunity. For example, `Reseller` or
`Manufacturer` .

Creating an Account-Opportunity Partner Relationship

When you create a partner relationship between an account and an opportunity (when you create a Partner record and specify the
`OpportunityId` field), the API automatically creates two OpportunityPartner records, one for the forward relationship and one for
the reverse.

**•** The value of the Partner field `AccountToId` maps to the value of the OpportunityPartner field `AccountToId` .

**•** The values of the `OpportunityId`, `Role`, and `IsPrimary` fields in both the Partner and OpportunityParnter records are the
same.


### Standard Objects OpportunityRelatedDeleteLog

**•** If you set the `IsPrimary` value to 1 ( `true` ) upon insert of a new OpportunityPartner, the `IsPrimary` value is automatically
set to 0 ( `false` ) for any existing primary partners for that opportunity.

This mapping allows the API to manage the records and their relationships efficiently.

SEE ALSO:

Partner

AccountPartner

### OpportunityRelatedDeleteLog

Represents an audit log of the deletion of opportunity-related child records, such as opportunity team members, product splits, or
opportunity splits. This object is available in API version 59.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
CurrencyIsoCode

DataType

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Available only when the multicurrency feature is enabled. Contains the ISO code for any
currency allowed by the organization.

When multicurrency is enabled, and a Pricebook2 is specified on the parent opportunity
(that is, the `Pricebook2Id` field isn’t blank on the opportunity record referenced by this
object’s `OpportunityId` ), then the value must match the currency of the
`CurrencyIsoCode` field on the PricebookEntry records that are associated with this
object.

Possible values are:

**•** `AED` —UAE Dirham

**•** `CAD` —Canadian Dollar

**•** `INR` —Indian Rupee

**•** `USD` —U.S. Dollar

The default value is `USD` .

**Type**
picklist


Standard Objects OpportunityRelatedDeleteLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Data type of the field that was deleted.

Possible values are:

**•** `Double`

**•** `DynamicEnum`

**•** `EntityId`

**•** `StaticEnum`

**•** `Text`

```
DeleteLog

FieldName

OpportunityId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The name of the field that was deleted.

Possible values are:

**•** `OpportunityLineItemSplit.SplitOwnerId`

**•** `OpportunityLineItemSplit.SplitPercentage`

**•** `OpportunityLineItemSplit.SplitTypeId`

**•** `OpportunitySplit.SplitOwnerId`

**•** `OpportunitySplit.SplitPercentage`

**•** `OpportunitySplit.SplitTypeId`

**•** `OpportunityTeamMember.TeamMemberRole`

**•** `OpportunityTeamMember.UserId`

**•** `Product2.Name`

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Required. ID of the associated opportunity.


### Standard Objects OpportunityShare

**Field** **Details**

This field is a relationship field.

**Relationship Name**
### Opportunity

**Relationship Type**
Lookup

**Refers To**
### Opportunity

```
Parent

SobjectType

Value

### OpportunityShare

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the record that was deleted. Records with the same Parent text indicate that the value
shown in the Value field came from the same record that was previously deleted. Refer to
the FieldName field to see which field is being tracked.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The object that’s being recorded for this row of data. Possible values are:

**•** `OpportunityLineItemSplit`

**•** `OpportunitySplit`

**•** `OpportunityTeamMember`

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The value of the field that was deleted.

Represents a sharing entry on an Opportunity.

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual` . Sharing entries
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.


Standard Objects OpportunityShare

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

Supported Calls

`describeSObjects()`, `create()`, `delete()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

As of Summer ’20 and later, only users with access to the Opportunity object can access this object.

Fields

The properties available for some fields depend on the default organization-wide sharing settings. The properties listed are true for the
default settings of such fields.

**Field** **Details**

```
IsDeleted

OpportunityAccessLevel

OpportunityId

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
Level of access that the user or group has to the opportunity. The possible values are:

**•** `Read`

**•** `Edit`

**•** `All` —This value is not valid when creating, updating, or deleting records.

This field must be set to an access level that’s higher than the org’s default access level for
opportunities.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


Standard Objects OpportunityShare

**Field** **Details**

**Description**
ID of the opportunity associated with this sharing entry. This field can’t be updated.

This is a relationship field.

**Relationship Name**
Opportunity

**Relationship Type**
Lookup

**Refers To**
Opportunity

```
RowCause

UserOrGroupId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only permitted
value is `Manual` . If no value is specified, the field defaults to `Manual` . All other `RowCause`
values are read-only. After the sharing entry is created, this field can’t be edited.

Valid values include:

**•** `Owner` —The User is the owner of the opportunity.

**•** `Manual` —The User or Group has access because a user with “All” access manually
shared the opportunity with the user or group.

**•** `Rule` —The User or Group has access via an opportunity sharing rule.

**•** `GuestRule` —The User or Group has access via an opportunity guest user sharing
rule.

**•** `ImplicitChild` —The User or Group has access to the opportunity on the account
associated with this opportunity. After faster account sharing recalculation is enabled,
sharing entries with this value aren’t returned in queries. Instead of storing implicit child
shares, record access is determined dynamically.

**•** `LpuImplicit` —The User has access to records owned by high-volume Experience
Cloud site users via a share group.

**•** `ARImplicit` —The User, who belongs to a partner or customer account, has access
to the opportunity via an account relationship data sharing rule.

**•** `Sales Team` —The User has access to the opportunity because the user is on the
opportunity sales team for the opportunity. The OpportunityTeamMember object sets
the access level. See OpportunityTeamMember for more information.

**•** `Territory` —The forecast manager has access because they are assigned to a territory
above the territory that is assigned the opportunity.

**Type**
reference


### Standard Objects OpportunitySplit

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the user or group that has been given access to the opportunity. This field can’t be
updated.

This is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Relationship Type**
Lookup

**Refers To**
Group, User

Usage

This object allows you to determine which users and groups can view or edit opportunities owned by other users.

Note: After faster account sharing recalculation is enabled for your org, we no longer store implicit share records between accounts
and their child opportunity records. Sharing entries that have a value of `ImplicitChild` in the `RowCause` field aren’t
returned when you query this object. Instead, the system dynamically determines whether users can access child opportunity
records when they try to access them. This change speeds up ownership and sharing recalculation for accounts.

[For more information, see the Faster Account Sharing Recalculation knowledge article.](https://help.salesforce.com/s/articleView?id=000394638&type=1&language=en_US)

If you attempt to create a record that matches an existing record, any modified fields are updated, the system returns the existing record.

If an opportunity is shared in multiple ways with a user, you don’t always see multiple sharing records. If a user has access to an opportunity
for one or more of the following RowCause values, the records in the OpportunityShare object are compressed into one record with the
highest level of access.

**•** `Manual`

**•** `Owner`

SEE ALSO:

Overview of Salesforce Objects and Fields

### OpportunitySplit OpportunitySplit credits one or more opportunity team members with a portion of the opportunity amount. This object is available in

API version 16.0 and later for pilot customers, and version 28.0 and later for others.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`


Standard Objects OpportunitySplit

Fields

**Field** **Details**

```
ArchivedTerritoryName

HasOpportunityLineItemSplit

OpportunityId

Split

```

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the associated territory that’s on an archived territory model. If the
OpportunityLineItemSplit isn’t associated with a territory on an archived territory
model, the field value is null. This field is available in API version 62.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read-only. Indicates whether the opportunity split has a split on the opportunity
line item level ( `true` ) or not ( `false` ).

The default value is `false` . This field is available in API version 58.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the opportunity for which the split is being created.

This field is a relationship field.

**Relationship Name**
Opportunity

**Relationship Type**
Lookup

**Refers To**
Opportunity

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Read-only. Automatically generated number identifying the split within the
opportunity.


Standard Objects OpportunitySplit

**Field** **Details**

```
SplitAmount

SplitNote

SplitOwnerId

SplitPercentage

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Monetary amount of the split.

Label is `Split Amount` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Enter any notes or comments about the split. The character limit is 255.

Label is `Split Note` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The opportunity owner.

This field is a relationship field.

**Relationship Name**
SplitOwner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
percent

**Properties**
Create, Filter, Sort, Update

**Description**
Split percentage that this team member receives. If the split type is validated to
a 100% total, this number can range from 0 to 100. If the total isn’t validated, this
number can range from 0 to 1,000.

Label is `Split (%)` .


Standard Objects OpportunitySplit

**Field** **Details**

```
SplitTypeId

Territory2Id

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Auto-generated, numeric ID for the split type defined by the OpportunitySplitType
object. This field is available in API version 28 and later.

If this field is blank, the system automatically specifies the default split type for
the opportunity amount, which is validated to 100%.

This field is a relationship field.

**Relationship Name**
SplitType

**Relationship Type**
Lookup

**Refers To**
OpportunitySplitType

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the associated territory. This field is a relationship field, and is available in
API version 62.0 and later.

**Relationship Name**
Territory2

**Relationship Type**
Lookup

**Refers To**
Territory2

Use the OpportunitySplit object to manage splits for an opportunity.

If you change the opportunity owner using the API, the old owner remains on the opportunity team with either Read-only access, or
the level of access specified in your organization-wide defaults.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


### Standard Objects OpportunitySplitType

**OpportunitySplitChangeEvent (API version 48.0)**
Change events are available for the object.

**OpportunitySplitHistory on page 63 (API version 59.0)**
History is available for tracked fields of the object.

### OpportunitySplitType OpportunitySplitType provides unique labels and behavior for each split type. This object is available in API version 28.0 and later.

There are two default split types: revenue splits, which must total 100%, and overlay splits, which can total any percentage.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`, `update()`

Fields

**Field Name** **Details**

```
Description

DeveloperName

IsActive

```

**Type**
textarea

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Describes the purpose of the split type, providing context to future developers.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The unique name of the object in the API. In managed packages, this
field prevents naming conflicts on package installations. With this field, a
developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is
specified, performance slows down while Salesforce generates one for
each record.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects OpportunitySplitType

**Field Name** **Details**

**Description**
Enables or disables the split type.

```
IsTotalValidated

Language

ManageableState

MasterLabel

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
If `true`, the split must total 100%. If `false`, the split can total any percentage.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates language of split labels in the user interface.

**Type**
ManageableState enumerated list

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the manageable state of the specified component that is contained in
a package:

**•** `beta`

**•** `deleted`

**•** `deprecated`

**•** `deprecatedEditable`

**•** `installed`

**•** `installedEditable`

**•** `released`

**•** `unmanaged`

This field is available in API version 38.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The user-interface label for the split type.


Standard Objects OpportunitySplitType

**Field Name** **Details**

```
NamespacePrefix

SplitEntity

SplitField

SplitDataStatus

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

This field can’t be accessed unless the logged-in user has the Customize
Application permission.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The containing record type, such as an opportunity. Available in API version 30
and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Indicates which currency field of the opportunity object is split. Available in API
version 30 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable,Restricted picklist, Sort,Update


### Standard Objects OpportunityStage

**Field Name** **Details**

**Description**
Indicates the status of the split type. Available in API version 30 and later.

### OpportunityStage

Represents the stage of an Opportunity in the sales pipeline, such as New Lead, Negotiating, Pending, Closed, and so on.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ApiName

DefaultProbability

Description

ForecastCategory

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Uniquely identifies a picklist value so it can be retrieved without using an id or master label.

**Type**
percent

**Properties**
Filter, Nillable, Sort,

**Description**
The default percentage estimate of the confidence in closing a specific opportunity for this
opportunity stage value. Label is **Probability (%)** .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Description of this opportunity stage value. Limit: 255 characters.

**Type**
picklist


Standard Objects OpportunityStage

**Field** **Details**

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The default forecast category for this opportunity stage value. The forecast category
automatically determines how opportunities are tracked and totaled in a forecast.

Possible values are:

**•** `BestCase`

**•** `Closed`

**•** `Forecast`

**•** `MostLikely`

**•** `Omitted`

**•** `Pipeline`

```
ForecastCategoryName

IsActive

IsClosed

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Available in API version 12.0 and later. The default forecast category value for this opportunity
stage value.

Possible values are:

**•** `Best Case`

**•** `Closed`

**•** `Commit`

**•** `Most Likely`

**•** `Omitted`

**•** `Pipeline`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this opportunity stage value is active ( `true` ) or not ( `false` ). Inactive
opportunity stage values are not available in the picklist and are retained for historical
purposes only.

**Type**
boolean


Standard Objects OpportunityStage

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this opportunity stage value represents a closed opportunity ( `true` ) or
not ( `false` ). Multiple opportunity stage values can represent a closed opportunity. Label
is **Closed** .

```
 IsWon

 MasterLabel

 SortOrder

```

Usage

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this opportunity stage value represents a won opportunity ( `true` ) or not
( `false` ). Multiple opportunity stage values can represent a won opportunity. Label is **Won** .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Master label for this opportunity stage value. This display value is the internal label that does
not get translated. Limit: 255 characters.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number used to sort this value in the opportunity stage picklist. These numbers are not
guaranteed to be sequential, as some previous opportunity stage values might have been
deleted.

This object represents a value in the opportunity stage picklist, which provides additional information about the stage of an Opportunity,
such as its probability or forecast category. Query this object to retrieve the set of values in the opportunity stage picklist, and then use
that information while processing Opportunity records to determine more information about a given opportunity. For example, the
application could test whether a given opportunity is won or not based on its `StageName` value and the value of the `IsWon` property
in the associated OpportunityStage object.


### Standard Objects OpportunityTag

This object is read-only via the API.

SEE ALSO:

Overview of Salesforce Objects and Fields

### OpportunityTag

Associates a word or short phrase with an Opportunity.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
ItemId

Name

TagDefinitionId

Type

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


### Standard Objects OpportunityTeamMember

**Field Name** **Details**

**Properties**
Create, Filter, Restricted picklist

**Description**
Defines the visibility of a tag.

Valid values:

**•** `Public` —The tag can be viewed and manipulated by all users in an organization.

**•** `Personal` —The tag can be viewed or manipulated only by a user with a matching
`OwnerId` .

Usage

OpportunityTag stores the relationship between its parent TagDefinition and the Opportunity being tagged. Tag objects act as metadata,
allowing users to describe and organize their data.

When a tag is deleted, its parent TagDefinition will also be deleted if the name is not being used; otherwise, the parent remains. Deleting
a TagDefinition sends it to the Recycle Bin, along with any associated tag entries.

### OpportunityTeamMember

Represents a User on the opportunity team of an Opportunity.

See also UserTeamMember, which represents a User who is on the default Opportunity team of another user.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
IsDeleted

```

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not
( `false` ). Label is **Deleted** .

Note: An OpportunityTeamMember that is deleted isn’t moved to the Recycle
Bin and can’t be undeleted, unless the record was cascade-deleted when deleting
a related Opportunity. For directly deleted OpportunityTeamMember records,


Standard Objects OpportunityTeamMember

**Field** **Details**

don't use the `isDeleted` field to detect deleted records in SOQL queries.
Instead, use `getDeleted()` .

```
Name

OpportunityAccessLevel

OpportunityId

PhotoURL

TeamMemberRole

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The team member name. This read-only field is available in API version 30.0 and later.

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
Opportunity access level for this team member. Valid values:

**•** `Read`

**•** `Edit`

**•** `All`

This field is supported in triggers, but not in workflows or validation rules. It’s editable
in API version 36.0 and later.

**Type**
reference

**Properties**
Create, Filter

**Description**
Required. ID of the Opportunity associated with this opportunity team. This field can’t
be updated.

**Type**
URL

**Properties**
Filter, Nillable, Sort, Group

**Description**
Read only. Retrieves the users Chatter photo URL. This field is available in API version
32.0 and later.

**Type**
picklist


Standard Objects OpportunityTeamMember

**Field** **Details**

**Properties**
Create, Filter, Nillable, Update

**Description**
Role that the team member has on the opportunity. The org’s admin sets the valid
values in the Opportunity Team Roles picklist. Label is **Team Role** .

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
Read only. Retrieves the user’s title. This field is available in API version 36.0 and later.

**Type**
reference

**Properties**
Create, Filter

**Description**
Required. ID of the User who is a member of the opportunity team. This field can’t
be updated.

If you create a record for this object and the `OpportunityId` and `UserId` combination matches an existing record, the system
updates any modified fields and returns the existing record.

In the user interface, users can set up an opportunity team for the opportunities they own. The opportunity team includes other users
that are working on the opportunity with them. This object is available only in organizations that have enabled team selling.

Note: The behavior for changing ownership of opportunities is different using the user interface when the previous owner is on
an opportunity team. For example, when you change the owner of an opportunity using the API, the previous owner's access
becomes Read Only or the access specified in your organization-wide default for opportunities, whichever is greater. However,
performing this same action in the user interface allows you to select the access level for the previous owner when the previous
owner is on an opportunity team.

Associated Objects

