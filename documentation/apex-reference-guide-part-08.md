error code is returned: `BCC_NOT_ALLOWED_IF_BCC_ COMPLIANCE_ENABLED` . Contact your Salesforce representative for
information on BCC compliance.

##### setCcAddresses(ccAddresses)

Optional. A list of carbon copy (CC) addresses or object IDs of the contacts, leads, and users you’re sending the email to. The maximum
size for this field is 4,000 bytes. The maximum total of `toAddresses`, `ccAddresses`, and `bccAddresses` per email is 150. All
recipients in these three fields count against the limit for email sent using Apex or the API.

Signature

```
   public Void setCcAddresses(String[] ccAddresses)

```

Parameters

```
   ccAddresses
```

Type: String[]

Return Value

Type: Void

Usage

All emails must have a recipient value in at least one of the following fields:

**•** `toAddresses`

**•** `ccAddresses`

**•** `bccAddresses`

**•** `targetObjectId`

##### setCharset(characterSet)

Optional. The character set for the email. If this value is null, the user's default value is used.

Signature

```
   public Void setCharset(String characterSet)

```

Parameters

```
   characterSet
```

Type: String

Return Value

Type: Void


Apex Reference Guide SingleEmailMessage Class

##### setDocumentAttachments(documentIds)

**(Deprecated. Use** `setEntityAttachments()` **instead.)** Optional. A list containing the ID of each document object you want
to attach to the email.

Signature

```
   public Void setDocumentAttachments(ID[] documentIds)

```

Parameters

```
   documentIds
```

Type: ID[]

Return Value

Type: Void

Usage

You can attach multiple documents as long as the total size of all attachments does not exceed 10 MB.

##### setEntityAttachments(ids)

[Optional. Array of IDs of Document, ContentVersion, or Attachment items to attach to the email.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_document.htm)

Signature

```
   public void setEntityAttachments(List<String> ids)

```

Parameters

```
   ids
```

Type: List<String>

Return Value

Type: void

##### setFileAttachments(fileNames)

Optional. A list containing the file names of the binary and text files you want to attach to the email.

Signature

```
   public Void setFileAttachments(EmailFileAttachment[] fileNames)

```

Parameters

```
   fileNames
```

Type: Messaging.EmailFileAttachment[]


Apex Reference Guide SingleEmailMessage Class

Return Value

Type: Void

Usage

You can attach multiple files as long as the total size of all attachments does not exceed 10 MB.

##### setHtmlBody(htmlBody)

Optional. The HTML version of the email, specified by the sender. The value is encoded according to the specification associated with
##### the organization. Specify a value for setTemplateId, setHtmlBody, or setPlainTextBody . Or, you can define both setHtmlBody and setPlainTextBody .

Signature

```
   public Void setHtmlBody(String htmlBody)

```

Parameters

```
   htmlBody
```

Type: String

Return Value

Type: Void

##### setInReplyTo(parentMessageIds)

Sets the optional In-Reply-To field of the outgoing email. This field identifies the email or emails to which this email is a reply (parent
emails).

Signature

```
   public Void setInReplyTo(String parentMessageIds)

```

Parameters

```
   parentMessageIds
```

Type: String

Contains one or more parent email message IDs.

Return Value

Type: Void


Apex Reference Guide SingleEmailMessage Class

##### **`setOneClickPost(oneClickPost)`**

Optional. If set to true, a List-Unsubscribe-Post header is added to an email with List-Unsubscribe=One-Click. Use this method to support
unsubscribe functionality in email sent via Salesforce. You can provide additional instructions on how to send unsubscribe requests by
using the header. This includes specifying the HTTP method and content type to use and provides a secure way to add more info to
unsubscribe requests. Default is `false` .

Signature

```
   public void setOneClickPost(Boolean oneClickPost)

```

Parameters

```
   oneClickPost
```

Type: Boolean

Return Value

Type: void

Usage

You can set the `oneClickPost` method to true only after invoking the `setUnsubscribeUrls` method. If set to true, pass at
least one HTTPS unsubscribe URL to unsubscribe.

Example

This example demonstrates how to send an email using Salesforce's `Messaging.SingleEmailMessage` class with enhanced
unsubscribe functionality. It creates an email message with a recipient, subject, and body, and includes an unsubscribe URL. It also
enables the `oneClickPost` feature, allowing for a simplified unsubscribe process. The email message is added to a list and sent
using the `Messaging.sendEmail` method.

```
   Messaging.SingleEmailMessage message = new Messaging.SingleEmailMessage();

   // Set the recipient's email address

   // Replace IDs with valid record IDs in your org.

   message.toAddresses = new String[] { '003D000000QDexS' };

   message.subject = 'Test Message';

   message.plainTextBody = 'This is the message body.';

   // Create a list to hold unsubscribe URLs

   List<String> unsubscribeUrls = new List<String>();

   unsubscribeUrls.add('https://example.com/unsubscribe.html?opaque=123456789');

   // Assign the unsubscribe URLs to the email message

   message.unsubscribeUrls = unsubscribeUrls;

   // Enable the one-click unsubscribe feature

   message.oneClickPost = true;

   Messaging.SingleEmailMessage[] messages =

```


Apex Reference Guide SingleEmailMessage Class

```
      new List<Messaging.SingleEmailMessage> {message};

   Messaging.SendEmailResult[] results = Messaging.sendEmail(messages);

   if (results[0].success) {

      System.debug('The email was sent successfully.');

   } else {

      System.debug('The email failed to send: '

         + results[0].errors[0].message);

   }

##### setOptOutPolicy(emailOptOutPolicy)

```

Optional. If you added recipients by ID instead of email address and the `Email Opt Out` option is set, this method determines the
behavior of the `sendEmail()` call. If you add recipients by their email addresses, the opt-out settings for those recipients aren’t
checked and those recipients always receive the email.

Signature

```
   public void setOptOutPolicy(String emailOptOutPolicy)

```

Parameters

```
   emailOptOutPolicy
```

Type: String

Possible values of the _`emailOptOutPolicy`_ parameter are:

**•** `SEND` (default)—The email is sent to all recipients. The recipients’ `Email Opt Out` setting is ignored. The setting Enforce
email privacy settings is ignored.

**•** `FILTER` —No email is sent to recipients that have the `Email Opt Out` option set. Emails are sent to the other recipients.
The setting Enforce email privacy settings is ignored.

**•** `REJECT` —If any of the recipients have the `Email Opt Out` option set, `sendEmail()` throws an error and no email is
sent. The setting Enforce email privacy settings is respected, as are the selections in the data privacy record based on the Individual
object. If any of the recipients have Don’t Market, Don’t Process, or Forget This Individual selected, `sendEmail()` throws an
error and no email is sent.

Return Value

Type: void

Example

This example shows how to send an email with the opt-out setting enforced. Recipients are specified by their IDs. The `FILTER` option
causes the email to be sent only to recipients that haven’t opted out from email. This example uses dot notation of the email properties,
which is equivalent to using the set methods.

```
   Messaging.SingleEmailMessage message = new Messaging.SingleEmailMessage();

   // Set recipients to two contact IDs.

   // Replace IDs with valid record IDs in your org.

   message.toAddresses = new String[] { '003D000000QDexS', '003D000000QDfW5' };

   message.optOutPolicy = 'FILTER';

```


Apex Reference Guide SingleEmailMessage Class

```
   message.subject = 'Opt Out Test Message';

   message.plainTextBody = 'This is the message body.';

   Messaging.SingleEmailMessage[] messages =

      new List<Messaging.SingleEmailMessage> {message};

         Messaging.SendEmailResult[] results = Messaging.sendEmail(messages);

   if (results[0].success) {

      System.debug('The email was sent successfully.');

   } else {

      System.debug('The email failed to send: '

         + results[0].errors[0].message);

   }

##### setPlainTextBody(plainTextBody)

```

Optional. The text version of the email, specified by the sender. Specify a value for `setTemplateId`, `setHtmlBody`, or
##### setPlainTextBody . Or, you can define both setHtmlBody and setPlainTextBody .

Signature

```
   public Void setPlainTextBody(String plainTextBody)

```

Parameters

```
   plainTextBody
```

Type: String

Return Value

Type: Void

##### setOrgWideEmailAddressId(emailAddressId)

Optional. The ID of the organization-wide email address associated with the outgoing email. If you’re using Apex to send emails from
the guest user, set the sender to the verified org-wide email address or the emails are blocked. The object's `DisplayName` field cannot
be set if the `setSenderDisplayName` field is already set.

Signature

```
   public Void setOrgWideEmailAddressId(ID emailAddressId)

```

Parameters

```
   emailAddressId
```

Type: ID

Usage

After you create an org-wide email address, you’re sent a confirmation email to verify it. Copy the Id from the URL and use
the _`setOrgWideEmailAddressId(Id)`_ method on your instance of _`Messaging.SingleEmailMessage`_ .


Apex Reference Guide SingleEmailMessage Class

To avoid hard-coding an ID, after creating your org-wide email address, you can query them.

```
   OrgWideEmailAddress[] owea = [select Id from OrgWideEmailAddress where Address =

   'doNotReply@<somedomain>.com'];

   Messaging.SingleEmailMessage mail = new Messaging.SingleEmailMessage();

   if ( owea.size() > 0 ) {

      mail.setOrgWideEmailAddressId(owea.get(0).Id);

   }

```

Return Value

Type: Void

##### setReferences(references)

Optional. The References field of the outgoing email. Identifies an email thread. Contains the parent emails' References and message
IDs, and possibly the In-Reply-To fields.

Signature

```
   public Void setReferences(String references)

```

Parameters

```
   references
```

Type: String

Return Value

Type: Void

##### setSubject(subject)

Optional. The email subject line. If you are using an email template, the subject line of the template overrides this value.

Signature

```
   public Void setSubject(String subject)

```

Parameters

```
   subject
```

Type: String

Return Value

Type: Void


Apex Reference Guide SingleEmailMessage Class

##### setTargetObjectId(targetObjectId)

Required if using a template, optional otherwise. The ID of the contact, lead, or user to which the email will be sent. The ID you specify
sets the context and ensures that merge fields in the template contain the correct data.

Signature

```
   public Void setTargetObjectId(ID targetObjectId)

```

Parameters

```
   targetObjectId
```

Type: ID

Return Value

Type: Void

Usage

Do not specify the IDs of records that have the `Email Opt Out` option selected.

All emails must have a recipient value in at least one of the following fields:

**•** `toAddresses`

**•** `ccAddresses`

**•** `bccAddresses`

**•** `targetObjectId`

##### setTemplateId(templateId)

Required if using a template, optional otherwise. The ID of the template used to create the email.

Signature

```
   public Void setTemplateId(ID templateId)

```

Parameters

```
   templateId
```

Type: ID

Return Value

Type: Void

##### setToAddresses(toAddresses)

Optional. A list of email addresses or object IDs of the contacts, leads, and users you’re sending the email to. The maximum size for this
field is 4,000 bytes. The maximum total of `toAddresses`, `ccAddresses`, and `bccAddresses` per email is 150. All recipients
in these three fields count against the limit for email sent using Apex or the API.


Apex Reference Guide SingleEmailMessage Class

Signature

```
   public Void setToAddresses(String[] toAddresses)

```

Parameters

```
   toAddresses
```

Type: String[]

Return Value

Type: Void

Usage

All emails must have a recipient value in at least one of the following fields:

**•** `toAddresses`

**•** `ccAddresses`

**•** `bccAddresses`

**•** `targetObjectId`

##### setTreatBodiesAsTemplate(treatAsTemplate)

Optional. If set to `true`, the subject, plain text, and HTML text bodies of the email are treated as template data. The merge fields are
resolved using the `renderEmailTemplate` method. Default is `false` .

Signature

```
   public void setTreatBodiesAsTemplate(Boolean treatAsTemplate)

```

Parameters

```
   treatAsTemplate
```

Type: Boolean

Return Value

Type: void

##### setTreatTargetObjectAsRecipient(treatAsRecipient)

Optional. If set to `true`, the `targetObjectId` (a contact, lead, or user) is the recipient of the email. If set to `false`, the
`targetObjectId` is supplied as the `WhoId` field for template rendering but isn’t a recipient of the email. The default is `true` .

Signature

```
   public void setTreatTargetObjectAsRecipient(Boolean treatAsRecipient)

```


Apex Reference Guide SingleEmailMessage Class

Parameters

```
   treatAsRecipient
```

Type: Boolean

Return Value

Type: void

Usage

Note: You can set TO, CC, and BCC addresses using the email messaging methods regardless of whether a template is used for
the email or the target object is a recipient.

##### **`setUnsubscribeComment(unsubscribeComment)`**

Optional. Sets a comment in the List-Unsubscribe email header. This comment is ignored by email clients and systems that parse the
header. The comments contain human-readable notes or context for developers, administrators, or other stakeholders managing the
email system.

Signature

```
   public void setUnsubscribeComment(String unsubscribeComment)

```

Parameters

```
   unsubscribeComment
```

Type: String

Return Value

Type: void

Usage

##### Invoke the setUnsubscribeUrls method before using setUnsubscribeComment .

Example

This example demonstrates how to send an email using Salesforce's `Messaging.SingleEmailMessage` class with an option
to include an unsubscribe link. It creates an email message with a recipient, subject, and body, and includes an unsubscribe URL that
directs the recipient to send an unsubscribe request via email. Additionally, it sets an `unsubscribeComment` to provide context
for the unsubscribe action.

```
   Messaging.SingleEmailMessage message = new Messaging.SingleEmailMessage();

   // Set the recipient's email address

   // Replace IDs with valid record IDs in your org

   message.toAddresses = new String[] { '003D000000QDexS' };

   message.subject = 'Test Message';

   message.plainTextBody = 'This is the message body.';

```


Apex Reference Guide SingleEmailMessage Class

```
   // Create a list to hold unsubscribe URLs

   List<String> unsubscribeUrls = new List<String>();

   unsubscribeUrls.add('mailto:listrequest@example.com?subject=unsubscribe');

   // Assign the unsubscribe URLs to the email message

   message.unsubscribeUrls = unsubscribeUrls;

   // Set an unsubscribe comment to provide context for the unsubscribe action

   message.unsubscribeComment = 'email unsubscribe support';

   Messaging.SingleEmailMessage[] messages =

      new List<Messaging.SingleEmailMessage> {message};

   Messaging.SendEmailResult[] results = Messaging.sendEmail(messages);

   if (results[0].success) {

      System.debug('The email was sent successfully.');

   } else {

      System.debug('The email failed to send: '

         + results[0].errors[0].message);

   }

##### **`setUnsubscribeUrls(UnsubscribeUrls)`**

```

Optional. Sets a `mailto` URI and HTTP URL of a mechanism for unsubscribing a recipient from an email list. A list of all unsubscribe
##### URLs passed through setUnsubscribeUrls is added to the List-Unsubscribe header. A minimum of one URL is required

to use this method.

Signature

```
   public void setUnsubscribeUrls(List<String> unsubscribeUrls)

```

Parameters

```
    UnsubscribeUrls

```

Type: List<String>

Return Value

Type: void

Usage

Provide a list of URLs that support unsubscribe functionality by offering recipients multiple ways to opt-out of future communications.
Each provided URL can use different protocols to allow for technical capacities of the recipient.

##### All setUnsubscribeUrls must have a value of one of these types:

**•** `Mailto` : Allows recipients to send an unsubscribe request via email.

**–** Example: `mailto:listrequest@example.com?subject=unsubscribe`


Apex Reference Guide SingleEmailMessage Class

**•** `HTTP` : Directs recipients to a web page where they can unsubscribe.

**–** Example: `http://example.com/unsubscribe.html?opaque=123456789`

**•** `HTTPS` : Directs recipients to a secure web page to unsubscribe.

**–** Example: `https://example.com/unsubscribe.html?opaque=123456789`

Example

This example demonstrates how to send an email using Salesforce's `Messaging.SingleEmailMessage` class that includes an
option to include an unsubscribe link for a user to click. It creates an email message, sets the recipient's email address, subject, and body,
and includes an unsubscribe URL. The email message is added to a list and sent using the `Messaging.sendEmail` method.

```
   Messaging.SingleEmailMessage message = new Messaging.SingleEmailMessage();

   // Set the recipient's email address

   // Replace IDs with valid record IDs in your org.

   message.toAddresses = new String[] { '003D000000QDexS' };

   message.subject = 'Test Message';

   message.plainTextBody = 'This is the message body.';

   // Create a list to hold unsubscribe URLs

   List<String> unsubscribeUrls = new List<String>();

   unsubscribeUrls.add('https://example.com/unsubscribe.html?opaque=123456789');

   // Assign the unsubscribe URLs to the email message

   message.unsubscribeUrls = unsubscribeUrls;

   Messaging.SingleEmailMessage[] messages =

      new List<Messaging.SingleEmailMessage> {message};

   Messaging.SendEmailResult[] results = Messaging.sendEmail(messages);

   if (results[0].success) {

      System.debug('The email was sent successfully.');

   } else {

      System.debug('The email failed to send: '

         + results[0].errors[0].message);

   }

##### setWhatId(whatId)

```

If you specify a contact for the `targetObjectId` field, you can specify an optional `whatId` as well. This helps to further ensure
that merge fields in the template contain the correct data.

Signature

```
   public Void setWhatId(ID whatId)

```


## Apex Reference Guide Metadata Namespace

Parameters

```
   whatId
```

Type: ID

Return Value

Type: Void

Usage

The value must be one of the following types:

**•** Account

**•** Asset

**•** Campaign

**•** Case

**•** Contract

**•** Opportunity

**•** Order

**•** Product

**•** Solution

**•** Custom

## Metadata Namespace The Metadata namespace provides classes and methods for working with custom metadata in Salesforce

Salesforce uses metadata types and components to represent org configuration and customization. Metadata is used for org settings
## that admins control or configuration information applied by installed apps and packages. Use the classes in the Metadata namespace

to access metadata from within Apex code.

Metadata access in Apex is available for Apex classes using API version 40.0 and later.

[For more information, see Metadata.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_metadata.htm)

## The following are the classes in the Metadata namespace.

IN THIS SECTION:

AnalyticsCloudComponentLayoutItem Class
Represents the settings for a Wave Analytics dashboard on a standard or custom page.

ConsoleComponent Class
Represents a custom console component on a section of a page layout.

Container Class
Represents a location and style in which to display more than one custom console component in the sidebars of the console.

CustomConsoleComponents Class
Represents custom console components (Visualforce pages, lookup fields, or related lists) on a page layout.


Apex Reference Guide Metadata Namespace

CustomMetadata Class
Represents records of custom metadata types.

CustomMetadataValue Class
Represents custom metadata values for a custom metadata component.

DeployCallback Interface
An interface for metadata deployment callback classes.

DeployCallbackContext Class
Represents context information for a deployment job.

DeployContainer Class
Represents a container for custom metadata components to be deployed.

DeployDetails Class
Contains detailed information on deployed components.

DeployMessage Class
Represents result information for the deployment of a metadata component.

DeployProblemType Enum
Describes the problem type for an unsuccessful component deploy.

DeployResult Class
Represents the results of a metadata deployment.

DeployStatus Enum
The result status of a deployment.

FeedItemTypeEnum Enum
The type of feed item in a feed-based page layout.

FeedLayout Class
Represents the values that define the feed view of a feed-based page layout. Feed-based layouts are available on Account, Case,
Contact, Lead, Opportunity, custom, and external objects. They include a feed view and a detail view.

FeedLayoutComponent Class
Represents a component in the feed view of a feed-based page layout.

FeedLayoutComponentType Enum
Indicates the type of feed layout component.

FeedLayoutFilter Class
Represents a feed filter option in the feed view of a feed-based page layout. A filter can have only `standardFilter` or
`feedItemType` set.

FeedLayoutFilterPosition Enum
Describes where the feed filters list is included in the layout.

FeedLayoutFilterType Enum
The type of feed layout filter.

Layout Class
Represents the metadata associated with a page layout.

LayoutColumn Class
Represents the items in a column within a layout section.


Apex Reference Guide Metadata Namespace

LayoutHeader Enum
Represents tagging types used for `Metadata.Layout.headers`

LayoutItem Class
Represents the valid values that define a layout item.

LayoutSection Class
Represents a section of a page layout, such as the Custom Links section.

LayoutSectionStyle Enum
Describes the possible styles for a layout section.

Metadata Class
An abstract base class that represents a custom metadata component.

MetadataType Enum
Represents the custom metadata components available in Apex.

MetadataValue Class
An abstract base class that represents a custom metadata component field.

MiniLayout Class
Represents a mini view of a record in the Console tab, hover details, and event overlays.

Operations Class
Represents a class to execute metadata operations, such as retrieving or deploying custom metadata.

PlatformActionList Class
Represents the list of actions, and their order, that display in the Salesforce mobile action bar for the layout.

PlatformActionListContextEnum Enum
Describes the different contexts of action lists.

PlatformActionListItem Class
Represents an action in the platform action list for a layout.

PlatformActionTypeEnum Enum
The type of action for a `PlatformActionListItem` .

PrimaryTabComponents Class
Represents custom console components on primary tabs in the Salesforce console.

QuickActionList Class
Represents the list of actions associated with the page layout.

QuickActionListItem Class
Represents an action in the `QuickActionList` .

RelatedContent Class
Represents the Mobile Cards section of the page layout.

RelatedContentItem Class
Represents an individual item in the `RelatedContent` list.

RelatedList Class
Represents related list custom components on the sidebars of the Salesforce console.

RelatedListItem Class
Represents an item in the related list in a page layout.


### Apex Reference Guide AnalyticsCloudComponentLayoutItem Class

ReportChartComponentLayoutItem Class
Represents the settings for a report chart on a standard or custom page.

ReportChartComponentSize Enum
Describes the size of the displayed report chart component.

SidebarComponent Class
Represents a specific custom console component to display in a container that hosts multiple components in one of the sidebars
of the Salesforce console.

SortOrder Enum
Describes the sort order of a related list.

StatusCode Enum
Describes the status code for an unsuccessful component deploy.

SubtabComponents Class
Represents custom console components on subtabs in the Salesforce console.

SummaryLayoutStyleEnum Enum
Describes the highlights panel style for a `SummaryLayout` .

SummaryLayout Class
Controls the appearance of the highlights panel, which summarizes key fields in a grid at the top of a page layout, when Case Feed
is enabled.

SummaryLayoutItem Class
Controls the appearance of an individual field and its column and row position within the highlights panel grid, when Case Feed is
enabled. You can have two fields per each grid in a highlights panel.

UiBehavior Enum
Describes the behavior for a layout item on a layout page.

### AnalyticsCloudComponentLayoutItem Class

Represents the settings for a Wave Analytics dashboard on a standard or custom page.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see
“AnalyticsCloudComponentLayoutItem” in the _[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

AnalyticsCloudComponentLayoutItem Properties

AnalyticsCloudComponentLayoutItem Methods


Apex Reference Guide AnalyticsCloudComponentLayoutItem Class

#### AnalyticsCloudComponentLayoutItem Properties The following are properties for AnalyticsCloudComponentLayoutItem .

IN THIS SECTION:

##### assetType

Specifies the type of Wave Analytics asset.

##### devName

Unique development name of the dashboard to add.

error
An error string that is populated only when an error occurred in the underlying dashboard.

filter
Dashboard filters for mapping data fields in the dashboard to the object’s fields.

height
Specifies the height of the dashboard, in pixels.

hideOnError
Controls whether users see a dashboard that has an error.

showHeader
If `true`, includes the dashboard’s header bar. If `false`, the dashboard appears without a header bar.

showSharing
If set to true, and the dashboard is shareable the dashboard shows the Share icon. If set to false, the dashboard doesn’t show the
Share icon.

showTitle
If true, includes the dashboard’s title above the dashboard. If false, the dashboard appears without a title.

width
Specifies the width of the dashboard, in pixels or percentage.

##### assetType

Specifies the type of Wave Analytics asset.

Signature

```
   public String assetType {get; set;}

```

Property Value

Type: String

##### devName

Unique development name of the dashboard to add.


Apex Reference Guide AnalyticsCloudComponentLayoutItem Class

Signature

```
   public String devName {get; set;}

```

Property Value

Type: String

##### error

An error string that is populated only when an error occurred in the underlying dashboard.

Signature

```
   public String error {get; set;}

```

Property Value

Type: String

##### filter

Dashboard filters for mapping data fields in the dashboard to the object’s fields.

Signature

```
   public String filter {get; set;}

```

Property Value

Type: String

##### height

Specifies the height of the dashboard, in pixels.

Signature

```
   public Integer height {get; set;}

```

Property Value

Type: Integer

##### hideOnError

Controls whether users see a dashboard that has an error.

Signature

```
   public Boolean hideOnError {get; set;}

```


Apex Reference Guide AnalyticsCloudComponentLayoutItem Class

Property Value

Type: Boolean

##### showHeader

If `true`, includes the dashboard’s header bar. If `false`, the dashboard appears without a header bar.

Signature

```
   public Boolean showHeader {get; set;}

```

Property Value

Type: Boolean

##### showSharing

If set to true, and the dashboard is shareable the dashboard shows the Share icon. If set to false, the dashboard doesn’t show the Share
icon.

Signature

```
   public Boolean showSharing {get; set;}

```

Property Value

Type: Boolean

##### showTitle

If true, includes the dashboard’s title above the dashboard. If false, the dashboard appears without a title.

Signature

```
   public Boolean showTitle {get; set;}

```

Property Value

Type: Boolean

##### width

Specifies the width of the dashboard, in pixels or percentage.

Signature

```
   public String width {get; set;}

```


### Apex Reference Guide ConsoleComponent Class

Property Value

Type: String

#### AnalyticsCloudComponentLayoutItem Methods The following are methods for AnalyticsCloudComponentLayoutItem .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.AnalyticsCloudComponentLayoutItem` .

##### clone()

Makes a duplicate copy of the `Metadata.AnalyticsCloudComponentLayoutItem` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### ConsoleComponent Class

Represents a custom console component on a section of a page layout.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “ConsoleComponent” in the
_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### ConsoleComponent Properties

ConsoleComponent Methods

#### ConsoleComponent Properties

### The following are properties for ConsoleComponent .


Apex Reference Guide ConsoleComponent Class

IN THIS SECTION:

##### height

The height of the custom console component in pixels.

##### location

The location of the custom console component on the page layout. Valid values are right, left, top, and bottom.

##### visualforcePage

The unique name of the custom console component.

##### width

The width of the custom console component in pixels.

##### height

The height of the custom console component in pixels.

Signature

```
   public Integer height {get; set;}

```

Property Value

Type: Integer

##### location

The location of the custom console component on the page layout. Valid values are right, left, top, and bottom.

Signature

```
   public String location {get; set;}

```

Property Value

Type: String

##### visualforcePage

The unique name of the custom console component.

Signature

```
   public String visualforcePage {get; set;}

```

Property Value

Type: String

##### width

The width of the custom console component in pixels.


### Apex Reference Guide Container Class

Signature

```
   public Integer width {get; set;}

```

Property Value

Type: Integer

#### ConsoleComponent Methods The following are methods for ConsoleComponent .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.ConsoleComponent` .

##### clone()

Makes a duplicate copy of the `Metadata.ConsoleComponent` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### Container Class

Represents a location and style in which to display more than one custom console component in the sidebars of the console.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “Container” in the _[Metadata](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_
_[API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

Container Properties

Container Methods


Apex Reference Guide Container Class

#### Container Properties The following are properties for Container .

IN THIS SECTION:

##### height

The height of the component’s container. The `unit` property determines the unit of measurement, in pixels or percent.

##### isContainerAutoSizeEnabled

If set to true, stacked console components in the sidebars autosize vertically.

##### region

The location of the component’s container (right, left, bottom, top).

sidebarComponents
Represents a specific custom console component to display in the components’ container.

style
The style of the container in which to display multiple components (stack, tab, accordion).

unit
The unit of measurement, in pixels or percent, for the height or width of the components’ container.

width
The width of the component’s container. The `unit` property determines the unit of measurement, in pixels or percent.

##### height

The height of the component’s container. The `unit` property determines the unit of measurement, in pixels or percent.

Signature

```
   public Integer height {get; set;}

```

Property Value

Type: Integer

##### isContainerAutoSizeEnabled

If set to true, stacked console components in the sidebars autosize vertically.

Signature

```
   public Boolean isContainerAutoSizeEnabled {get; set;}

```

Property Value

Type: Boolean

##### region

The location of the component’s container (right, left, bottom, top).


Apex Reference Guide Container Class

Signature

```
   public String region {get; set;}

```

Property Value

Type: String

##### sidebarComponents

Represents a specific custom console component to display in the components’ container.

Signature

```
   public List<Metadata.SidebarComponent> sidebarComponents {get; set;}

```

Property Value

Type: List<Metadata.SidebarComponent>

##### style

The style of the container in which to display multiple components (stack, tab, accordion).

Signature

```
   public String style {get; set;}

```

Property Value

Type: String

##### unit

The unit of measurement, in pixels or percent, for the height or width of the components’ container.

Signature

```
   public String unit {get; set;}

```

Property Value

Type: String

##### width The width of the component’s container. The unit property determines the unit of measurement, in pixels or percent.

Signature

```
   public Integer width {get; set;}

```


### Apex Reference Guide CustomConsoleComponents Class

Property Value

Type: Integer

#### Container Methods The following are methods for Container .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.Container` .

##### clone()

Makes a duplicate copy of the `Metadata.Container` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### CustomConsoleComponents Class

Represents custom console components (Visualforce pages, lookup fields, or related lists) on a page layout.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “CustomConsoleComponents”
in the _[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### CustomConsoleComponents Properties

CustomConsoleComponents Methods

#### CustomConsoleComponents Properties

### The following are properties for CustomConsoleComponents .


Apex Reference Guide CustomConsoleComponents Class

IN THIS SECTION:

##### primaryTabComponents

Represents custom console components on primary tabs in the Salesforce console.

##### subtabComponents

Represents custom console components on subtabs in the Salesforce console.

##### primaryTabComponents

Represents custom console components on primary tabs in the Salesforce console.

Signature

```
   public Metadata.PrimaryTabComponents primaryTabComponents {get; set;}

```

Property Value

Type: Metadata.PrimaryTabComponents

##### subtabComponents

Represents custom console components on subtabs in the Salesforce console.

Signature

```
   public Metadata.SubtabComponents subtabComponents {get; set;}

```

Property Value

Type: Metadata.SubtabComponents

#### CustomConsoleComponents Methods The following are methods for CustomConsoleComponents .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.CustomConsoleComponents` .

##### clone()

Makes a duplicate copy of the `Metadata.CustomConsoleComponents` .

Signature

```
   public Object clone()

```


### Apex Reference Guide CustomMetadata Class

Return Value

Type: Object

### CustomMetadata Class

Represents records of custom metadata types.

Warning: Protected custom metadata types behave like public custom metadata types when they are outside of a managed
package. Public custom metadata types are readable for all profiles, including the guest user. Do not store secrets, personally
identifying information, or any private data in these records. Use protected custom metadata types only in managed packages.
Outside of a managed package, use named credentials or encrypted custom fields to store secrets like OAuth tokens, passwords,
and other confidential material.

Namespace

Metadata

Usage

Use `Metadata.CustomMetadata` [to represent records of custom metadata types in Apex. For more information, see Custom](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_custommetadatatypes.htm)
[Metadata Types in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_custommetadatatypes.htm) _Metadata API Developer Guide_ .

Example

```
   // Set up custom metadata to be created in the subscriber org.

      Metadata.CustomMetadata customMetadata = new Metadata.CustomMetadata();

      customMetadata.fullName = 'ISVNamespace__MetadataTypeName.MetadataRecordName';

      Metadata.CustomMetadataValue customField = new Metadata.CustomMetadataValue();

      customField.field = 'customField__c';

      customField.value = 'New value';

      customMetadata.values.add(customField);

```

Note: When you assign namespaces to records, provide full, qualified record names to the app. If both the type and the record
are in _`Namespace`_, use something like: `customMetadata.fullName =`

```
     ' Namespace __MetadataTypeName. Namespace __MetadataRecordName'

```

IN THIS SECTION:

#### CustomMetadata Properties

CustomMetadata Methods

#### CustomMetadata Properties

### The following are properties for CustomMetadata .


Apex Reference Guide CustomMetadata Class

IN THIS SECTION:

##### description

The description of the custom metadata.

##### label

The label of the custom metadata record.

##### protected_x

Property that describes whether the custom metadata record is a protected component.

##### values

A list of custom metadata values, such as custom fields, for the custom metadata record.

##### description

The description of the custom metadata.

Signature

```
   public String description {get; set;}

```

Property Value

Type: String

##### label

The label of the custom metadata record.

Signature

```
   public String label {get; set;}

```

Property Value

Type: String

##### protected_x

Property that describes whether the custom metadata record is a protected component.

Signature

```
   public Boolean protected_x {get; set;}

```

Property Value

Type: Boolean

##### values

A list of custom metadata values, such as custom fields, for the custom metadata record.


### Apex Reference Guide CustomMetadataValue Class

Signature

```
   public List<Metadata.CustomMetadataValue> values {get; set;}

```

Property Value

Type: List<Metadata.CustomMetadataValue>

#### CustomMetadata Methods The following are methods for CustomMetadata .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.CustomMetadata` .

##### clone()

Makes a duplicate copy of the `Metadata.CustomMetadata` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### CustomMetadataValue Class

Represents custom metadata values for a custom metadata component.

Namespace

Metadata

Usage

Use `Metadata.CustomMetadataValue` to access values for custom fields of custom metadata records.

Supported Apex primitive types are:

**•** Boolean

**•** Date

**•** DateTime

**•** Decimal

**•** Double

**•** Integer

**•** Long


Apex Reference Guide CustomMetadataValue Class

**•** String

Example

```
   // Set a custom field value for a custom metadata record

   Metadata.CustomMetadataValue customField = new Metadata.CustomMetadataValue();

   customField.field = 'CustomField1__c';

   customField.value = 'New Value';

   customMetadata.values.add(customField);

```

IN THIS SECTION:

#### CustomMetadataValue Properties

CustomMetadataValue Methods

#### CustomMetadataValue Properties The following are properties for CustomMetadataValue .

IN THIS SECTION:

##### field

The field name for the custom metadata value.

##### value

The field value for the custom metadata value.

##### field

The field name for the custom metadata value.

Signature

```
   public String field {get; set;}

```

Property Value

Type: String

##### value

The field value for the custom metadata value.

Signature

```
   public Object value {get; set;}

```

Property Value

Type: Object


### Apex Reference Guide DeployCallback Interface

Supported Apex primitive types are:

**•** Boolean

**•** Date

**•** DateTime

**•** Decimal

**•** Double

**•** Integer

**•** Long

**•** String

When setting the value for relationship fields, use the qualified API name of the related metadata, not the ID.

[For more information, see Primitive Data Types.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/langCon_apex_primitives.htm)

#### CustomMetadataValue Methods The following are methods for CustomMetadataValue .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.CustomMetadataValue` .

##### clone()

Makes a duplicate copy of the `Metadata.CustomMetadataValue` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### DeployCallback Interface

An interface for metadata deployment callback classes.

Namespace

Metadata

Usage

You must provide a callback class for the asynchronous deployment of custom metadata through Apex. This class must implement the
`Metadata.DeployCallback` interface.


Apex Reference Guide DeployCallback Interface

Salesforce calls your `DeployCallback.handleResult()` method asynchronously once the queued deployment completes.
Because the callback is called as asynchronous Apex after deployment, there may be a brief period where the deploy has completed,
but your callback has not been called yet.

IN THIS SECTION:

#### DeployCallback Methods DeployCallback Example Implementation DeployCallback Methods The following are methods for DeployCallback .

IN THIS SECTION:

##### handleResult(var1, var2)

Method that is called when the asynchronous deployment of custom metadata completes.

##### handleResult(var1, var2)

Method that is called when the asynchronous deployment of custom metadata completes.

Signature

```
   public void handleResult(Metadata.DeployResult var1, Metadata.DeployCallbackContext

   var2)

```

Parameters

```
   var1
```

Type: Metadata.DeployResult

The results of the asynchronous deployment.

```
   var2
```

Type: Metadata.DeployCallbackContext

The context for the queued asynchronous deployment job.

Return Value

Type: void

#### DeployCallback Example Implementation

This is an example implementation of the `Metadata.DeployCallback` interface.

```
   public class MyCallback implements Metadata.DeployCallback {

      public void handleResult(Metadata.DeployResult result,

                     Metadata.DeployCallbackContext context) {

        if (result.status == Metadata.DeployStatus.Succeeded) {

           // Deployment was successful

```


### Apex Reference Guide DeployCallbackContext Class

```
        } else {

           // Deployment was not successful

        }

      }

   }

```

The following example uses this implementation for a deployment.

```
   // Setup callback and deploy

   MyCallback callback = new MyCallback();

   Metadata.Operations.enqueueDeployment(mdContainer, callback);

### DeployCallbackContext Class

```

Represents context information for a deployment job.

Namespace

Metadata

Usage

After an asynchronous metadata deployment finishes, Salesforce provides an instance of `Metadata.DeployCallbackContext`
in an asynchronous call to your implementation of `handleResult()` in your `Metadata.DeployCallback` class.

Example

```
   public void handleResult(Metadata.DeployResult result,

                  Metadata.DeployCallbackContext context) {

     // Check the callback job ID for the deployment

     Id jobId = context.getCallbackJobId();

     // ...process the results...

   }

```

IN THIS SECTION:

#### DeployCallbackContext Methods DeployCallbackContext Methods

### The following are methods for DeployCallbackContext .

IN THIS SECTION:

clone()
Makes a duplicate copy of the `Metadata.DeployCallbackContext` .

getCallbackJobId()
Gets the asynchronous Apex job ID for the callback job.


### Apex Reference Guide DeployContainer Class

##### clone()

Makes a duplicate copy of the `Metadata.DeployCallbackContext` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

##### getCallbackJobId()

Gets the asynchronous Apex job ID for the callback job.

Signature

```
   public Id getCallbackJobId()

```

Return Value

Type: Id

### DeployContainer Class

Represents a container for custom metadata components to be deployed.

Namespace

Metadata

Usage

Use `Metadata.DeployContainer` to manage custom metadata components for deployment. A container must have one or
more components before being deployed.

Example

```
   // Use DeployContainer for deployment

   Metadata.DeployContainer mdContainer = new Metadata.DeployContainer();

   mdContainer.addMetadata(customMetadata);

   ...

   // Enqueue deploy

   Metadata.Operations.enqueueDeployment(mdContainer, callback);

```


Apex Reference Guide DeployContainer Class

IN THIS SECTION:

#### DeployContainer Methods DeployContainer Methods The following are methods for DeployContainer .

IN THIS SECTION:

##### addMetadata(md)

Add a custom metadata component to the container.

##### clone()

Makes a duplicate copy of the `Metadata.DeployContainer` .

getMetadata()
Retrieves a list of custom metadata components from the container.

removeMetadata(md)
Removes a metadata component from the container.

removeMetadataByFullName(fullName)
Removes a metadata component from the container using the component’s full name.

##### addMetadata(md)

Add a custom metadata component to the container.

Signature

```
   public void addMetadata(Metadata.Metadata md)

```

Parameters

```
   md
```

Type: Metadata.Metadata

A custom metadata component class that derives from `Metadata.Metadata` . Avoid adding components to a
`Metadata.DeployContainer` that have the same `Metadata.Metadata.fullName` because it causes deployment
errors.

Return Value

Type: void

##### clone()

Makes a duplicate copy of the `Metadata.DeployContainer` .

Signature

```
   public Object clone()

```


Apex Reference Guide DeployContainer Class

Return Value

Type: Object

##### getMetadata()

Retrieves a list of custom metadata components from the container.

Signature

```
   public List<Metadata.Metadata> getMetadata()

```

Return Value

Type: List<Metadata.Metadata>

##### removeMetadata(md)

Removes a metadata component from the container.

Signature

```
   public Boolean removeMetadata(Metadata.Metadata md)

```

Parameters

```
   md
```

Type: Metadata.Metadata

Metadata component to remove.

Return Value

Type: Boolean

Returns `true` if the container changed as a result of the call.

##### removeMetadataByFullName(fullName)

Removes a metadata component from the container using the component’s full name.

Signature

```
   public Boolean removeMetadataByFullName(String fullName)

```

Parameters

```
   fullName
```

Type: String

Full name of the component to remove.


### Apex Reference Guide DeployDetails Class

Return Value

Type: Boolean

Returns `true` if the container changed as a result of the call.

### DeployDetails Class

Contains detailed information on deployed components.

Namespace

Metadata

Usage

Use this class to obtain a list of the successfully and unsuccessfully deployed components after a completed deployment by Salesforce
in your `Metadata.DeployCallback` results.

IN THIS SECTION:

#### DeployDetails Properties

DeployDetails Methods

#### DeployDetails Properties

### The following are properties for DeployDetails .

IN THIS SECTION:

##### componentFailures

Contains a list of information about components that failed to deploy.

##### componentSuccesses

Contains a list of information about components that deployed successfully.

##### componentFailures

Contains a list of information about components that failed to deploy.

Signature

```
   public List<Metadata.DeployMessage> componentFailures {get; set;}

```

Property Value

Type: List<Metadata.DeployMessage>

##### componentSuccesses

Contains a list of information about components that deployed successfully.


### Apex Reference Guide DeployMessage Class

Signature

```
   public List<Metadata.DeployMessage> componentSuccesses {get; set;}

```

Property Value

Type: List<Metadata.DeployMessage>

#### DeployDetails Methods The following are methods for DeployDetails .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.DeployDetails` .

##### clone()

Makes a duplicate copy of the `Metadata.DeployDetails` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### DeployMessage Class

Represents result information for the deployment of a metadata component.

Namespace

Metadata

Usage

### Use DeployMessage to access detailed information about component deployments. Salesforce provides a list of DeployMessages
#### for a completed deployment via the DeployDetails and DeployResults instances sent in the

`DeployCallback.handleResult()` callback.

IN THIS SECTION:

DeployMessage Properties

DeployMessage Methods


Apex Reference Guide DeployMessage Class

#### DeployMessage Properties The following are properties for DeployMessage .

IN THIS SECTION:

##### changed

Determines whether the component was changed after deployment. If true, the component was changed as a result of the deployment.
If false, the deployed component was the same as the corresponding component already in the org.

columnNumber
Each component is represented by a text file. If an error occurs during deployment, this property represents the column of the text
file where the error occurred.

componentType
The metadata type of the component in the deployment.

created
If true, the component was created as a result of the deployment. If false, the component was modified as a result of the deployment.

createdDate
The date and time when the component was created as a result of the deployment.

deleted
If true, the component was deleted as a result of the deployment. If false, the component was either new or modified as result of
the deployment.

fileName
The name of the file in the metadata archive used to deploy the component.

fullName
Full name for the custom metadata component.

id
ID of the component that was deployed.

lineNumber
Each component is represented by a text file. If an error occurs during deployment, this field represents the line number of the text
file where the error occurred.

problem
If an error or warning occurred, this field contains a description of the problem that caused the deployment to fail.

problemType
Indicates the problem type, for example, an error or warning.

success
Indicates whether the component was successfully deployed (true) or not (false).

##### changed

Determines whether the component was changed after deployment. If true, the component was changed as a result of the deployment.
If false, the deployed component was the same as the corresponding component already in the org.


Apex Reference Guide DeployMessage Class

Signature

```
   public Boolean changed {get; set;}

```

Property Value

Type: Boolean

##### columnNumber

Each component is represented by a text file. If an error occurs during deployment, this property represents the column of the text file
where the error occurred.

Signature

```
   public Integer columnNumber {get; set;}

```

Property Value

Type: Integer

##### componentType

The metadata type of the component in the deployment.

Signature

```
   public String componentType {get; set;}

```

Property Value

Type: String

##### created

If true, the component was created as a result of the deployment. If false, the component was modified as a result of the deployment.

Signature

```
   public Boolean created {get; set;}

```

Property Value

Type: Boolean

##### createdDate

The date and time when the component was created as a result of the deployment.


Apex Reference Guide DeployMessage Class

Signature

```
   public Datetime createdDate {get; set;}

```

Property Value

Type: Datetime

##### deleted

If true, the component was deleted as a result of the deployment. If false, the component was either new or modified as result of the
deployment.

Signature

```
   public Boolean deleted {get; set;}

```

Property Value

Type: Boolean

##### fileName

The name of the file in the metadata archive used to deploy the component.

Signature

```
   public String fileName {get; set;}

```

Property Value

Type: String

##### fullName

Full name for the custom metadata component.

Signature

```
   public String fullName {get; set;}

```

Property Value

Type: String

##### id

ID of the component that was deployed.


Apex Reference Guide DeployMessage Class

Signature

```
   public Id id {get; set;}

```

Property Value

Type: Id

##### lineNumber

Each component is represented by a text file. If an error occurs during deployment, this field represents the line number of the text file
where the error occurred.

Signature

```
   public Integer lineNumber {get; set;}

```

Property Value

Type: Integer

##### problem

If an error or warning occurred, this field contains a description of the problem that caused the deployment to fail.

Signature

```
   public String problem {get; set;}

```

Property Value

Type: String

##### problemType

Indicates the problem type, for example, an error or warning.

Signature

```
   public Metadata.DeployProblemType problemType {get; set;}

```

Property Value

Type: Metadata.DeployProblemType

##### success

Indicates whether the component was successfully deployed (true) or not (false).


### Apex Reference Guide DeployProblemType Enum

Signature

```
   public Boolean success {get; set;}

```

Property Value

Type: Boolean

#### DeployMessage Methods The following are methods for DeployMessage .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.DeployMessage` .

##### clone()

Makes a duplicate copy of the `Metadata.DeployMessage` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### DeployProblemType Enum

Describes the problem type for an unsuccessful component deploy.

Enum Values

The following are the values of the `Metadata.DeployProblemType` enum.

**Value** **Description**

`Error` The deploy problem is an error.

`Info` The deploy problem is of type “Info”.

`Warning` The deploy problem is a warning.

SEE ALSO:

StatusCode Enum


### Apex Reference Guide DeployResult Class DeployResult Class

Represents the results of a metadata deployment.

Namespace

Metadata

Usage

After an asynchronous metadata deployment finishes, Salesforce provides an instance of `Metadata.DeployResult` in a call to
your implementation of `handleResult()` in your `Metadata.DeployCallback` class.

Example

```
   public void handleResult(Metadata.DeployResult result,

                  Metadata.DeployCallbackContext context) {

      if (result.status == Metadata.DeployStatus.Succeeded) {

        // Deployment was successful

      } else {

        // Deployment was not successful

      }

   }

```

IN THIS SECTION:

#### DeployResult Properties

DeployResult Methods

#### DeployResult Properties

### The following are properties for DeployResult .

IN THIS SECTION:

canceledBy
ID of the user who canceled the queued deployment.

canceledByName
Full name of the user who canceled the queued deployment.

checkOnly
Indicates whether the deployment checked only the validity of the deployed files without making changes in the org. A check-only
deployment does not deploy components or change the org in any way.

completedDate
Date and time for when the deployment process ended.

createdBy
ID of the user who created the deployment job.


Apex Reference Guide DeployResult Class

createdByName
Full name of the user who created the deployment job.

createdDate
Date and time the deployment job was first queued.

details
Provides the details for components in a completed deployment.

done
Indicates whether Salesforce finished processing the deployment.

errorMessage
Message corresponding to the values in the `errorStatusCode` property, if any.

errorStatusCode
If an error occurs during deployment, a status code is returned. The message corresponding to the status code is returned in the
`errorMessagefield` property.

id
ID of the deployment job.

ignoreWarnings
Specifies whether a deployment continues, even if the deployment generates warnings.

lastModifiedDate
Date and time of the last update for the deployment process.

messages
A list of all the detail messages for a deployment.

numberComponentErrors
The number of components that generated errors during the deployment.

numberComponentsDeployed
The number of components deployed in the deployment process. Use this value with the `numberComponentsTotal` property
to get an estimate of the deployment’s progress.

numberComponentsTotal
The total number of components in the deployment. Use this value with the `numberComponentsDeployed` property to get
an estimate of the deployment’s progress.

rollbackOnError
Indicates whether any failure causes a complete rollback (true) or not (false) of the deployment.

startDate
Date and time the deployment process began.

stateDetail
Indicates which component is being deployed.

status
Indicates the current state of the deployment.

success
Indicates whether the deployment was successful (true) or not (false).


Apex Reference Guide DeployResult Class

##### canceledBy

ID of the user who canceled the queued deployment.

Signature

```
   public String canceledBy {get; set;}

```

Property Value

Type: String

##### canceledByName

Full name of the user who canceled the queued deployment.

Signature

```
   public String canceledByName {get; set;}

```

Property Value

Type: String

##### checkOnly

Indicates whether the deployment checked only the validity of the deployed files without making changes in the org. A check-only
deployment does not deploy components or change the org in any way.

Signature

```
   public Boolean checkOnly {get; set;}

```

Property Value

Type: Boolean

##### completedDate

Date and time for when the deployment process ended.

Signature

```
   public Datetime completedDate {get; set;}

```

Property Value

Type: Datetime


Apex Reference Guide DeployResult Class

##### createdBy

ID of the user who created the deployment job.

Signature

```
   public String createdBy {get; set;}

```

Property Value

Type: String

##### createdByName

Full name of the user who created the deployment job.

Signature

```
   public String createdByName {get; set;}

```

Property Value

Type: String

##### createdDate

Date and time the deployment job was first queued.

Signature

```
   public Datetime createdDate {get; set;}

```

Property Value

Type: Datetime

##### details

Provides the details for components in a completed deployment.

Signature

```
   public Metadata.DeployDetails details {get; set;}

```

Property Value

Type: Metadata.DeployDetails

##### done

Indicates whether Salesforce finished processing the deployment.


Apex Reference Guide DeployResult Class

Signature

```
   public Boolean done {get; set;}

```

Property Value

Type: Boolean

##### errorMessage Message corresponding to the values in the errorStatusCode property, if any.

Signature

```
   public String errorMessage {get; set;}

```

Property Value

Type: String

##### errorStatusCode

If an error occurs during deployment, a status code is returned. The message corresponding to the status code is returned in the
##### errorMessagefield property.

Signature

```
   public String errorStatusCode {get; set;}

```

Property Value

Type: String

[For a description of each status code value, see Core Data Types Used in API Calls in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/sforce_api_calls_concepts_core_data_objects.htm) _SOAP API Developer Guide_ .

##### id

ID of the deployment job.

Signature

```
   public Id id {get; set;}

```

Property Value

Type: Id

##### ignoreWarnings

Specifies whether a deployment continues, even if the deployment generates warnings.


Apex Reference Guide DeployResult Class

Signature

```
   public Boolean ignoreWarnings {get; set;}

```

Property Value

Type: Boolean

##### lastModifiedDate

Date and time of the last update for the deployment process.

Signature

```
   public Datetime lastModifiedDate {get; set;}

```

Property Value

Type: Datetime

##### messages

A list of all the detail messages for a deployment.

Note: Removed in API version 29.0 and later.

Signature

```
   public List<Metadata.DeployMessage> messages {get; set;}

```

Property Value

Type: List<Metadata.DeployMessage>

##### numberComponentErrors

The number of components that generated errors during the deployment.

Signature

```
   public Integer numberComponentErrors {get; set;}

```

Property Value

Type: Integer

##### numberComponentsDeployed

The number of components deployed in the deployment process. Use this value with the `numberComponentsTotal` property
to get an estimate of the deployment’s progress.


Apex Reference Guide DeployResult Class

Signature

```
   public Integer numberComponentsDeployed {get; set;}

```

Property Value

Type: Integer

##### numberComponentsTotal

The total number of components in the deployment. Use this value with the `numberComponentsDeployed` property to get an
estimate of the deployment’s progress.

Signature

```
   public Integer numberComponentsTotal {get; set;}

```

Property Value

Type: Integer

##### rollbackOnError

Indicates whether any failure causes a complete rollback (true) or not (false) of the deployment.

Signature

```
   public Boolean rollbackOnError {get; set;}

```

Property Value

Type: Boolean

##### startDate

Date and time the deployment process began.

Signature

```
   public Datetime startDate {get; set;}

```

Property Value

Type: Datetime

##### stateDetail

Indicates which component is being deployed.


Apex Reference Guide DeployResult Class

Signature

```
   public String stateDetail {get; set;}

```

Property Value

Type: String

##### status

Indicates the current state of the deployment.

Signature

```
   public Metadata.DeployStatus status {get; set;}

```

Property Value

Type: Metadata.DeployStatus

##### success

Indicates whether the deployment was successful (true) or not (false).

Signature

```
   public Boolean success {get; set;}

```

Property Value

Type: Boolean

#### DeployResult Methods The following are methods for DeployResult .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.DeployResult` .

##### clone()

Makes a duplicate copy of the `Metadata.DeployResult` .

Signature

```
   public Object clone()

```


### Apex Reference Guide DeployStatus Enum

Return Value

Type: Object

### DeployStatus Enum

The result status of a deployment.

Usage

`Metadata.DeployResult.status` uses this enum to describe the results of the deployment.

Enum Values

The following are the values of the `Metadata.DeployStatus` enum.

**Value** **Description**

`Canceled` The queued deployment was canceled.

`Canceling` The queued deployment is being canceled.

`Failed` The deployment failed.

`FinalizingDeploy` The deployment has started, and is in the finalizing state. Deployments in the state
can't be canceled.

`FinalizingDeployFailed` The deployment failed during the finalizing state.

`InProgress` The deployment has been started and is in progress.

`Pending` The deployment has been queued but not started.

`Succeeded` The deployment succeeded.

`SucceededPartial` The deployment succeeded, but some components might not have been successfully
deployed. Check `Metadata.DeployResult` for more details.

### FeedItemTypeEnum Enum

The type of feed item in a feed-based page layout.

Enum Values

The following are the values of the `Metadata.FeedItemTypeEnum` enum.

**Value** **Description**

`ActivityEvent` Activity on tasks and events associated with a case. Available only on Case layouts.

`AdvancedTextPost` Group announcements posted on a feed.

`AnnouncementPost` Not used.


Apex Reference Guide FeedItemTypeEnum Enum

**Value** **Description**

`ApprovalPost` Approvals submitted on a feed.

`AttachArticleEvent` Activity related to attaching articles to cases.

`BasicTemplateFeedItem` Activity from the Log a Call action. Available only on layouts for objects that support
Activities (tasks and events).

`CallLogPost` Activity from the Log a Call action. Available only on layouts for objects that support
Activities (tasks and events).

`CanvasPost` Posts a canvas app makes on a feed.

`CaseCommentPost` Activity from the Case Note action. Available only on Case layouts.

`ChangeStatusPost` Activity from the Change Status action. Available only on Case layouts.

`ChatTranscriptPost` Activity related to attaching Chat transcripts to cases. Available only on Case layouts.

`CollaborationGroupCreated` Creating a public group.

`CollaborationGroupUnarchived` Not used.

`ContentPost` Attaching a file to a post.

`CreateRecordEvent` Creating a record from the publisher.

`DashboardComponentAlert` Not used.

`DashboardComponentSnapshot` Posting a dashboard snapshot on a feed.

`EmailMessageEvent` Activity from the Email action. Available only on Case layouts.

`FacebookPost` Not used.

`LinkPost` Attaching a URL to a post.

`MilestoneEvent` Changing the milestone status on a case. Available only on Case layouts.

`PollPost` Posting a poll on a feed.

`ProfileSkillPost` Adding skills to a user’s Chatter profile.

`QuestionPost` Posting a question on a feed.

`ReplyPost` Activity from the Portal action. Available only on Case layouts.

`RypplePost` Creating a Thanks badge in WDC.

`SocialPost` Activity on Twitter from the Social Post action.

`TestItem` Creating a text post from the publisher.

`TextPost` Making a change or group of changes to a tracked field.

`TrackedChange` Not used.

`Undefined` Undefined feed item.

`UserStatus` Not used.


### Apex Reference Guide FeedLayout Class FeedLayout Class

Represents the values that define the feed view of a feed-based page layout. Feed-based layouts are available on Account, Case, Contact,
Lead, Opportunity, custom, and external objects. They include a feed view and a detail view.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “FeedLayout” in the _[Metadata](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_
_[API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### FeedLayout Properties

FeedLayout Methods

#### FeedLayout Properties

### The following are properties for FeedLayout .

IN THIS SECTION:

autocollapsePublisher
Specifies whether the publisher is collapsed when the page loads (true) or not (false).

compactFeed
Specifies whether the feed-based page layout uses a compact feed (true) or not (false). If set to true, feed items on the page are
collapsed by default, and the feed view has an updated design.

feedFilterPosition
Indicates where the feed filters list is included in the layout.

feedFilters
The individual filters displayed in the feed filters list.

fullWidthFeed
Specifies whether the feed expands horizontally to take up all available space on the page ( `true` ) or not ( `false` ).

hideSidebar
Specifies whether the sidebar is hidden ( `true` ) or not ( `false` ).

highlightExternalFeedItems
Controls whether to highlight external feed items (true) or not (false).

leftComponents
The individual components displayed in the left column of the feed view.

rightComponents
Lists the individual components displayed in the right column of the feed view.


Apex Reference Guide FeedLayout Class

useInlineFiltersInConsole
Indicates whether to use inline filters in the Salesforce console.

##### autocollapsePublisher

Specifies whether the publisher is collapsed when the page loads (true) or not (false).

Signature

```
   public Boolean autocollapsePublisher {get; set;}

```

Property Value

Type: Boolean

##### compactFeed

Specifies whether the feed-based page layout uses a compact feed (true) or not (false). If set to true, feed items on the page are collapsed
by default, and the feed view has an updated design.

Signature

```
   public Boolean compactFeed {get; set;}

```

Property Value

Type: Boolean

##### feedFilterPosition

Indicates where the feed filters list is included in the layout.

Signature

```
   public Metadata.FeedLayoutFilterPosition feedFilterPosition {get; set;}

```

Property Value

Type: FeedLayoutFilterPosition Enum

##### feedFilters

The individual filters displayed in the feed filters list.

Signature

```
   public List<Metadata.FeedLayoutFilter> feedFilters {get; set;}

```

Property Value

Type: List<FeedLayoutFilter Class>.


Apex Reference Guide FeedLayout Class

##### fullWidthFeed

Specifies whether the feed expands horizontally to take up all available space on the page ( `true` ) or not ( `false` ).

Signature

```
   public Boolean fullWidthFeed {get; set;}

```

Property Value

Type: Boolean

##### hideSidebar

Specifies whether the sidebar is hidden ( `true` ) or not ( `false` ).

Signature

```
   public Boolean hideSidebar {get; set;}

```

Property Value

Type: Boolean

##### highlightExternalFeedItems

Controls whether to highlight external feed items (true) or not (false).

Signature

```
   public Boolean highlightExternalFeedItems {get; set;}

```

Property Value

Type: Boolean

##### leftComponents

The individual components displayed in the left column of the feed view.

Signature

```
   public List<Metadata.FeedLayoutComponent> leftComponents {get; set;}

```

Property Value

Type: List<FeedLayoutComponent Class>

##### rightComponents

Lists the individual components displayed in the right column of the feed view.


### Apex Reference Guide FeedLayoutComponent Class

Signature

```
   public List<Metadata.FeedLayoutComponent> rightComponents {get; set;}

```

Property Value

Type: List<FeedLayoutComponent Class>

##### useInlineFiltersInConsole

Indicates whether to use inline filters in the Salesforce console.

Signature

```
   public Boolean useInlineFiltersInConsole {get; set;}

```

Property Value

Type: Boolean

#### FeedLayout Methods The following are methods for FeedLayout .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.FeedLayout` .

##### clone()

Makes a duplicate copy of the `Metadata.FeedLayout` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### FeedLayoutComponent Class

Represents a component in the feed view of a feed-based page layout.

Namespace

Metadata


Apex Reference Guide FeedLayoutComponent Class

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “FeedLayoutComponent” in
the _[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### FeedLayoutComponent Properties

FeedLayoutComponent Methods

#### FeedLayoutComponent Properties The following are properties for FeedLayoutComponent . See FeedLayoutComponent in the Metadata API Developer Guide

IN THIS SECTION:

##### componentType

Represents a component in the feed view of a feed-based page layout. The type of component is required.

##### height

The height, in pixels, of the component. Doesn’t apply to `standardComponents`

page_x
The name of the Visualforce page used as a custom component.

##### componentType

Represents a component in the feed view of a feed-based page layout. The type of component is required.

Signature

```
   public Metadata.FeedLayoutComponentType componentType {get; set;}

```

Property Value

Type: Metadata.FeedLayoutComponentType on page 3057

##### height

The height, in pixels, of the component. Doesn’t apply to `standardComponents`

Signature

```
   public Integer height {get; set;}

```

Property Value

Type: Integer


### Apex Reference Guide FeedLayoutComponentType Enum

##### page_x

The name of the Visualforce page used as a custom component.

Signature

```
   public String page_x {get; set;}

```

Property Value

Type: String

#### FeedLayoutComponent Methods The following are methods for FeedLayoutComponent .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.FeedLayoutComponent` .

##### clone()

Makes a duplicate copy of the `Metadata.FeedLayoutComponent` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### FeedLayoutComponentType Enum

Indicates the type of feed layout component.

Enum Values

The following are the values of the `Metadata.FeedLayoutComponentType` enum.

**Value** **Description**

`CaseExperts` List of case experts.

`CaseUnifiedFiles` List of all files attached to the case.

`CustomButtons` Custom button.

`CustomLinks` Custom link.

`Followers` List of followers.


### Apex Reference Guide FeedLayoutFilter Class

**Value** **Description**

```
Following

```

Icon that toggles between a Follow button (if the user viewing a record doesn’t
already follow it) and a Following indicator (if the user viewing a record does follow
it).

`HelpAndToolLinks` Icons that link to the help topic for the page, the page layout, and, the printable
view of the page. Available only on Case layouts.

`Milestones` Milestone tracker, which lets users see the status of a milestone on a case. Available
only on Case layouts.

`SimilarCases` List of similar cases.

`Topics` List of topics related to the record.

`Visualforce` Custom Visualforce component.

### FeedLayoutFilter Class

Represents a feed filter option in the feed view of a feed-based page layout. A filter can have only `standardFilter` or
`feedItemType` set.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “FeedLayoutFilter” in the
_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### FeedLayoutFilter Properties

FeedLayoutFilter Methods

#### FeedLayoutFilter Properties

### The following are properties for FeedLayoutFilter .

IN THIS SECTION:

feedFilterName
The name of a `CustomFeedFilter` component. Names are prefixed with the name of the parent object. For example,
`Case.MyCustomFeedFilter` .

feedFilterType
The type of filter.


Apex Reference Guide FeedLayoutFilter Class

##### feedItemType

The type of feed item to display.

##### feedFilterName

The name of a `CustomFeedFilter` component. Names are prefixed with the name of the parent object. For example,
`Case.MyCustomFeedFilter` .

Signature

```
   public String feedFilterName {get; set;}

```

Property Value

Type: String

##### feedFilterType

The type of filter.

Signature

```
   public Metadata.FeedLayoutFilterType feedFilterType {get; set;}

```

Property Value

Type: FeedLayoutFilterType Enum

##### feedItemType

The type of feed item to display.

Signature

```
   public Metadata.FeedItemTypeEnum feedItemType {get; set;}

```

Property Value

Type: FeedItemTypeEnum Enum

#### FeedLayoutFilter Methods The following are methods for FeedLayoutFilter .

IN THIS SECTION:

clone()
Makes a duplicate copy of the `Metadata.FeedLayoutFilter` .


### Apex Reference Guide FeedLayoutFilterPosition Enum

##### clone()

Makes a duplicate copy of the `Metadata.FeedLayoutFilter` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### FeedLayoutFilterPosition Enum

Describes where the feed filters list is included in the layout.

Enum Values

The following are the values of the `Metadata.FeedLayoutFilterPosition` enum.

**Value** **Description**

`CenterDropDown` As a drop-down list in the center column.

`LeftFixed` As a fixed list in the left column.

`LeftFloat` As a floating list in the left column.

### FeedLayoutFilterType Enum

The type of feed layout filter.

Enum Values

The following are the values of the `Metadata.FeedLayoutFilterType` enum.

**Value** **Description**

`AllUpdates` Shows all feed items on a record.

`Custom` Shows custom feed items.

`FeedItemType` Shows feed items only for a particular type of activity on the record.

### Layout Class

Represents the metadata associated with a page layout.


Apex Reference Guide Layout Class

Namespace

Metadata

Usage

[Use this class to access layout metadata components. For more information, see Layout in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_layouts.htm) _Metadata API Developer Guide_ .

IN THIS SECTION:

#### Layout Properties

Layout Methods

#### Layout Properties The following are properties for Layout .

IN THIS SECTION:

customButtons
The custom buttons for this layout.

customConsoleComponents
Represents custom console components (Visualforce pages, lookup fields, or related lists) on a page layout.

emailDefault
Default value for the email checkbox. Only relevant if the `showEmailCheckbox` property is set.

excludeButtons
List of standard buttons to exclude from this layout.

feedLayout
Represents the values that define the feed view of a feed-based page layout.

headers
Represents the layout headers used for tagging.

layoutSections
The main sections of the layout containing fields, s-controls, and custom links. The order here determines the layout order.

miniLayout
Represents a minilayout, which is used in the mini view of a record in the Console tab, hover details, and event overlays.

multilineLayoutFields
Fields for special multiline layout fields which appear in OpportunityProduct layouts.

platformActionList
The list of actions, and their order, that display in the Salesforce mobile action bar for the layout.

quickActionList
The list of quick actions that display in the full Salesforce site for the page layout.

relatedContent
The Related Content section of the page layout.


Apex Reference Guide Layout Class

relatedLists
The related lists for the layout, listed in the order they appear in the user interface.

relatedObjects
The list of related objects that appears in the mini view of the console.

runAssignmentRulesDefault
Default value for the “run assignment rules” checkbox. Only relevant if the `showRunAssignmentRulesCheckbox` property
is set.

showEmailCheckbox
Controls whether to show the email checkbox. Only allowed on Case, CaseClose, and Task layouts. The default state of checkbox is
controlled by the `emailDefault` property.

showHighlightsPanel
If set, the highlights panel displays on pages in the Salesforce console.

showInteractionLogPanel
If set, the interaction log displays on pages in the Salesforce console.

showKnowledgeComponent
Only allowed on Case layouts. If set, the Knowledge sidebar displays on cases in the Salesforce console.

showRunAssignmentRulesCheckbox
Controls whether to show the Run Assignment Rules checkbox. Only allowed on Lead and Case layouts. The default state of checkbox
is controlled by the `runAssignmentRulesDefault` property.

showSolutionSection
Only allowed on CaseClose layout. If set, the built-in solution information section shows up on the page.

showSubmitAndAttachButton
For Cast layouts only. If set, the Submit & Add Attachment button displays on case edit pages to portal users in the Customer Portal.

summaryLayout
The summary layout for this layout.

##### customButtons

The custom buttons for this layout.

Signature

```
   public List<String> customButtons {get; set;}

```

Property Value

Type: List<String>

##### customConsoleComponents

Represents custom console components (Visualforce pages, lookup fields, or related lists) on a page layout.

Signature

```
   public Metadata.CustomConsoleComponents customConsoleComponents {get; set;}

```


Apex Reference Guide Layout Class

Property Value

Type: CustomConsoleComponents Class

##### emailDefault

Default value for the email checkbox. Only relevant if the `showEmailCheckbox` property is set.

Signature

```
   public Boolean emailDefault {get; set;}

```

Property Value

Type: Boolean

##### excludeButtons

List of standard buttons to exclude from this layout.

Signature

```
   public List<String> excludeButtons {get; set;}

```

Property Value

Type: List<String>

##### feedLayout

Represents the values that define the feed view of a feed-based page layout.

Signature

```
   public Metadata.FeedLayout feedLayout {get; set;}

```

Property Value

Type: Metadata.FeedLayout

##### headers

Represents the layout headers used for tagging.

Signature

```
   public List<Metadata.LayoutHeader> headers {get; set;}

```

Property Value

Type: List<Metadata.LayoutHeader>


Apex Reference Guide Layout Class

##### layoutSections

The main sections of the layout containing fields, s-controls, and custom links. The order here determines the layout order.

Signature

```
   public List<Metadata.LayoutSection> layoutSections {get; set;}

```

Property Value

Type: List<Metadata.LayoutSection>

##### miniLayout

Represents a minilayout, which is used in the mini view of a record in the Console tab, hover details, and event overlays.

Signature

```
   public Metadata.MiniLayout miniLayout {get; set;}

```

Property Value

Type: Metadata.MiniLayout

##### multilineLayoutFields

Fields for special multiline layout fields which appear in OpportunityProduct layouts.

Signature

```
   public List<String> multilineLayoutFields {get; set;}

```

Property Value

Type: List<String>

##### platformActionList

The list of actions, and their order, that display in the Salesforce mobile action bar for the layout.

Signature

```
   public Metadata.PlatformActionList platformActionList {get; set;}

```

Property Value

Type: Metadata.PlatformActionList

##### quickActionList

The list of quick actions that display in the full Salesforce site for the page layout.


Apex Reference Guide Layout Class

Signature

```
   public Metadata.QuickActionList quickActionList {get; set;}

```

Property Value

Type: Meatadata.QuickActionL.

##### relatedContent

The Related Content section of the page layout.

Signature

```
   public Metadata.RelatedContent relatedContent {get; set;}

```

Property Value

Type: Metadata.RelatedContent

##### relatedLists

The related lists for the layout, listed in the order they appear in the user interface.

Signature

```
   public List<Metadata.RelatedListItem> relatedLists {get; set;}

```

Property Value

Type: List<Metadata.RelatedListItem>

##### relatedObjects

The list of related objects that appears in the mini view of the console.

Signature

```
   public List<String> relatedObjects {get; set;}

```

Property Value

Type: List<String>

##### runAssignmentRulesDefault

Default value for the “run assignment rules” checkbox. Only relevant if the `showRunAssignmentRulesCheckbox` property is
set.


Apex Reference Guide Layout Class

Signature

```
   public Boolean runAssignmentRulesDefault {get; set;}

```

Property Value

Type: Boolean

##### showEmailCheckbox

Controls whether to show the email checkbox. Only allowed on Case, CaseClose, and Task layouts. The default state of checkbox is
controlled by the `emailDefault` property.

Signature

```
   public Boolean showEmailCheckbox {get; set;}

```

Property Value

Type: Boolean

##### showHighlightsPanel

If set, the highlights panel displays on pages in the Salesforce console.

Signature

```
   public Boolean showHighlightsPanel {get; set;}

```

Property Value

Type: Boolean

##### showInteractionLogPanel

If set, the interaction log displays on pages in the Salesforce console.

Signature

```
   public Boolean showInteractionLogPanel {get; set;}

```

Property Value

Type: Boolean

##### showKnowledgeComponent

Only allowed on Case layouts. If set, the Knowledge sidebar displays on cases in the Salesforce console.


Apex Reference Guide Layout Class

Signature

```
   public Boolean showKnowledgeComponent {get; set;}

```

Property Value

Type: Boolean

##### showRunAssignmentRulesCheckbox

Controls whether to show the Run Assignment Rules checkbox. Only allowed on Lead and Case layouts. The default state of checkbox
is controlled by the `runAssignmentRulesDefault` property.

Signature

```
   public Boolean showRunAssignmentRulesCheckbox {get; set;}

```

Property Value

Type: Boolean

##### showSolutionSection

Only allowed on CaseClose layout. If set, the built-in solution information section shows up on the page.

Signature

```
   public Boolean showSolutionSection {get; set;}

```

Property Value

Type: Boolean

##### showSubmitAndAttachButton

For Cast layouts only. If set, the Submit & Add Attachment button displays on case edit pages to portal users in the Customer Portal.

Signature

```
   public Boolean showSubmitAndAttachButton {get; set;}

```

Property Value

Type: Boolean

##### summaryLayout

The summary layout for this layout.


### Apex Reference Guide LayoutColumn Class

Signature

```
   public Metadata.SummaryLayout summaryLayout {get; set;}

```

Property Value

Type: Metadata.SummaryLayout

#### Layout Methods The following are methods for Layout .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.Layout` .

##### clone()

Makes a duplicate copy of the `Metadata.Layout` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### LayoutColumn Class

Represents the items in a column within a layout section.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “LayoutColumn” in the _[Metadata](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_
_[API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

LayoutColumn Properties

LayoutColumn Methods


Apex Reference Guide LayoutColumn Class

#### LayoutColumn Properties The following are properties for LayoutColumn .

IN THIS SECTION:

##### layoutItems

The individual items within a column (ordered from top to bottom).

##### reserved

This field is reserved for Salesforce.

##### layoutItems

The individual items within a column (ordered from top to bottom).

Signature

```
   public List<Metadata.LayoutItem> layoutItems {get; set;}

```

Property Value

Type: List<Metadata.LayoutItem>

##### reserved

This field is reserved for Salesforce.

Signature

```
   public String reserved {get; set;}

```

Property Value

Type: String

#### LayoutColumn Methods The following are methods for LayoutColumn .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.LayoutColumn` .

##### clone()

Makes a duplicate copy of the `Metadata.LayoutColumn` .


### Apex Reference Guide LayoutHeader Enum

Signature

```
   public Object clone()

```

Return Value

Type: Object

### LayoutHeader Enum

Represents tagging types used for `Metadata.Layout.headers`

Enum Values

The following are the values of the `Metadata.LayoutHeader` enum.

**Value** **Description**

`PersonalTagging` Tag is set to private user.

`PublicTagging` Tag is viewable to any user who can access the record.

### LayoutItem Class

Represents the valid values that define a layout item.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “LayoutItem” in the _[Metadata](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_
_[API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### LayoutItem Properties

LayoutItem Methods

#### LayoutItem Properties

### The following are properties for LayoutItem .

IN THIS SECTION:

analyticsCloudComponent
A Wave Analytics dashboard component on a page.


Apex Reference Guide LayoutItem Class

##### behavior

Determines the field behavior.

canvas
References a canvas app.

component
References a component.

customLink
The custom link reference.

emptySpace
Controls if this layout item is a blank space.

field
The field name reference, relative to the layout, for example “Description” or “MyField__c”.

height
For s-controls and pages only, the height in pixels.

page_x
Reference to a Visualforce page.

reportChartComponent
Refers to a report chart that you can add to a standard or custom object page.

scontrol
Reference to an s-control.

showLabel
For s-control and pages only, whether to show the label.

showScrollbars
For s-control and pages only, whether to show scrollbars.

width
For s-control and pages only, the width in pixels or percent. Pixel values are simply the number of pixels, for example, 500. Percentage
values must include the percent sign, for example, 20%.

##### analyticsCloudComponent

A Wave Analytics dashboard component on a page.

Signature

```
   public Metadata.AnalyticsCloudComponentLayoutItem analyticsCloudComponent {get; set;}

```

Property Value

Type: Metadata.AnalyticsCloudComponentLayoutItem

##### behavior

Determines the field behavior.


Apex Reference Guide LayoutItem Class

Signature

```
   public Metadata.UiBehavior behavior {get; set;}

```

Property Value

Type: Metadata.UiBehavior

##### canvas

References a canvas app.

Signature

```
   public String canvas {get; set;}

```

Property Value

Type: String

##### component

References a component.

Signature

```
   public String component {get; set;}

```

Property Value

Type: String

##### customLink

The custom link reference.

Signature

```
   public String customLink {get; set;}

```

Property Value

Type: String

##### emptySpace

Controls if this layout item is a blank space.

Signature

```
   public Boolean emptySpace {get; set;}

```


Apex Reference Guide LayoutItem Class

Property Value

Type: Boolean

##### field

The field name reference, relative to the layout, for example “Description” or “MyField__c”.

Signature

```
   public String field {get; set;}

```

Property Value

Type: String

##### height

For s-controls and pages only, the height in pixels.

Signature

```
   public Integer height {get; set;}

```

Property Value

Type: Integer

##### page_x

Reference to a Visualforce page.

Signature

```
   public String page_x {get; set;}

```

Property Value

Type: String

##### reportChartComponent

Refers to a report chart that you can add to a standard or custom object page.

Signature

```
   public Metadata.ReportChartComponentLayoutItem reportChartComponent {get; set;}

```

Property Value

Type: Metadata.ReportChartComponentLayoutItem


Apex Reference Guide LayoutItem Class

##### scontrol

Reference to an s-control.

Signature

```
   public String scontrol {get; set;}

```

Property Value

Type: String

##### showLabel

For s-control and pages only, whether to show the label.

Signature

```
   public Boolean showLabel {get; set;}

```

Property Value

Type: Boolean

##### showScrollbars

For s-control and pages only, whether to show scrollbars.

Signature

```
   public Boolean showScrollbars {get; set;}

```

Property Value

Type: Boolean

##### width

For s-control and pages only, the width in pixels or percent. Pixel values are simply the number of pixels, for example, 500. Percentage
values must include the percent sign, for example, 20%.

Signature

```
   public String width {get; set;}

```

Property Value

Type: String


### Apex Reference Guide LayoutSection Class

#### LayoutItem Methods The following are methods for LayoutItem .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.LayoutItem` .

##### clone()

Makes a duplicate copy of the `Metadata.LayoutItem` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### LayoutSection Class

Represents a section of a page layout, such as the Custom Links section.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “LayoutSection” in the _[Metadata](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_
_[API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### LayoutSection Properties

LayoutSection Methods

#### LayoutSection Properties

### The following are properties for LayoutSection .

IN THIS SECTION:

customLabel
Indicates if this section's label is custom or standard (built-in).

detailHeading
Controls whether this heading appears on the detail page.


Apex Reference Guide LayoutSection Class

##### editHeading

Controls whether this heading appears on the edit page.

##### label

The label; either standard or custom, based on the customLabel property.

layoutColumns
Lists the layout columns. You can have one, two, or three columns, ordered left to right, are possible.

style
The style of the layout for this section.

##### customLabel

Indicates if this section's label is custom or standard (built-in).

Signature

```
   public Boolean customLabel {get; set;}

```

Property Value

Type: Boolean

##### **`detailHeading`**

Controls whether this heading appears on the detail page.

Signature

```
   public Boolean detailHeading {get; set;}

```

Property Value

Type: Boolean

##### **`editHeading`**

Controls whether this heading appears on the edit page.

Signature

```
   public Boolean editHeading {get; set;}

```

Property Value

Type: Boolean

##### label

The label; either standard or custom, based on the customLabel property.


Apex Reference Guide LayoutSection Class

Signature

```
   public String label {get; set;}

```

Property Value

Type: String

##### layoutColumns

Lists the layout columns. You can have one, two, or three columns, ordered left to right, are possible.

Signature

```
   public List<Metadata.LayoutColumn> layoutColumns {get; set;}

```

Property Value

Type: List<Metadata.LayoutColumn>

##### style

The style of the layout for this section.

Signature

```
   public Metadata.LayoutSectionStyle style {get; set;}

```

Property Value

Type: Metadata.LayoutSectionStyle

#### LayoutSection Methods The following are methods for LayoutSection .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.LayoutSection` .

##### clone()

Makes a duplicate copy of the `Metadata.LayoutSection` .

Signature

```
   public Object clone()

```


### Apex Reference Guide LayoutSectionStyle Enum

Return Value

Type: Object

### LayoutSectionStyle Enum

Describes the possible styles for a layout section.

Enum Values

The following are the values of the `Metadata.LayoutSectionStyle` enum.

**Value** **Description**

`CustomLinks` Contains custom links only

`OneColumn` One column

`TwoColumnsLeftToRight` Two columns, tab goes left to right

`TwoColumnsTopToBottom` Two columns, tab goes top to bottom

### Metadata Class

An abstract base class that represents a custom metadata component.

Namespace

### Metadata

Usage

You can’t create instances of this abstract class. Instead, create an instance of a specific custom metadata component class that derives
from `Metadata.Metadata`, such as `Metadata.CustomMetadata` [. For more information, see Metadata in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/metadata.htm) _Metadata API_
_Developer Guide_ .

IN THIS SECTION:

#### Metadata Properties

Metadata Methods

#### Metadata Properties

### The following are properties for Metadata .

IN THIS SECTION:

fullName
The full name of the custom metadata, which can include the namespace, type, and component name.


### Apex Reference Guide MetadataType Enum

##### fullName

The full name of the custom metadata, which can include the namespace, type, and component name.

Signature

```
   public String fullName {get; set;}

```

Property Value

Type: String

The format of the full name can include the namespace, metadata type, and metadata component name. If you’re updating components
in a namespace, you also need to qualify the namespace for the component in the full name. For example, the full name for a custom
metadata "MDType1__mdt" component named "Component1" that is contained in the "myPackage" namespace is
"myPackage__MDType1__mdt.myPackage__Component1". For more information on full name formats for different metadata types,
see reference documentation on the metadata types in the _[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

#### Metadata Methods The following are methods for Metadata .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.Metadata` .

##### clone()

Makes a duplicate copy of the `Metadata.Metadata` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### MetadataType Enum

Represents the custom metadata components available in Apex.

Enum Values

The following are the values of the `Metadata.MetadataType` enum.

**Value** **Description**

`CustomMetadata` Records of custom metadata types


### Apex Reference Guide MetadataValue Class

**Value** **Description**

`Layout` Layouts

### MetadataValue Class

An abstract base class that represents a custom metadata component field.

Namespace

### Metadata

Usage

You can’t create instances of this abstract class. Instead, create an instance of a specific custom metadata component value class that
derives from `Metadata.MetadataValue`, such as `Metadata.CustomMetadataValue` .

IN THIS SECTION:

#### MetadataValue Methods MetadataValue Methods

### The following are methods for MetadataValue .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.MetadataValue` .

##### clone()

Makes a duplicate copy of the `Metadata.MetadataValue` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### MiniLayout Class

Represents a mini view of a record in the Console tab, hover details, and event overlays.


Apex Reference Guide MiniLayout Class

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “MiniLayout” in the _[Metadata](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_
_[API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### MiniLayout Properties

MiniLayout Methods

#### MiniLayout Properties The following are properties for MiniLayout .

IN THIS SECTION:

##### fields

The fields for the mini-layout, listed in the order they appear in the UI. Fields that appear in the mini-layout must appear in the main
layout.

##### relatedLists

The mini related lists, listed in the order they appear in the UI. You cannot set sorting on mini related lists. Fields that appear in the
mini related lists must appear in the main layout.

##### fields

The fields for the mini-layout, listed in the order they appear in the UI. Fields that appear in the mini-layout must appear in the main
layout.

Signature

```
   public List<String> fields {get; set;}

```

Property Value

Type: List<String>

##### relatedLists

The mini related lists, listed in the order they appear in the UI. You cannot set sorting on mini related lists. Fields that appear in the mini
related lists must appear in the main layout.

Signature

```
   public List<Metadata.RelatedListItem> relatedLists {get; set;}

```


### Apex Reference Guide Operations Class

Property Value

Type: List<Metadata.RelatedListItem>

#### MiniLayout Methods The following are methods for MiniLayout .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.MiniLayout` .

##### clone()

Makes a duplicate copy of the `Metadata.MiniLayout` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### Operations Class

Represents a class to execute metadata operations, such as retrieving or deploying custom metadata.

Namespace

Metadata

Usage

Use the `Metadata.Operations` class to execute metadata operations. For more information on use cases and restrictions of
metadata operations in Apex, see Metadata.

Example: Retrieve Metadata

The following example retrieves the “MyTestCustomMDType” custom metadata record from the subscriber org, and inspects the custom
fields.

```
   public class ReadMetadata {

     public void retrieveMetadata () {

      // List fullnames of components we want to retrieve

      List<String> componentNameList =

   new List<String>{'ISVNamespace__TestCustomMDType.MyTestCustomMDType'};

      // Retrieve components that are records of custom metadata types

```


Apex Reference Guide Operations Class

```
      // based on name

      List<Metadata.Metadata> components = Metadata.Operations.retrieve(

   Metadata.MetadataType.CustomMetadata, componentNameList);

      Metadata.CustomMetadata customMetadataRecord = (Metadata.CustomMetadata)

   components.get(0);

      // Check fields of retrieved component

      List<Metadata.CustomMetadataValue> values = customMetadataRecord.values;

      for (integer i = 0; i < values.size(); i++) {

       if (values.get(i).field == 'testField__c' &&

         values.get(i).value == 'desired value') {

        // ...process accordingly...

       }

      }

     }

   }

```

Example: Deploy Metadata

The following example uses the Metadata API in Apex to update the customField custom field value of the MetadataRecordName custom
metadata record and deploy this change into the subscriber org. Because the deployment is asynchronous, you must provide a callback
class that implements the `Metadata.DeployCallback` interface, which is then used when the queued deployment completes.

```
   public class CreateMetadata{

     public void updateAndDeployMetadata() {

      // Setup custom metadata to be created in the subscriber org.

      Metadata.CustomMetadata customMetadata = new Metadata.CustomMetadata();

      customMetadata.fullName = 'ISVNamespace__MetadataTypeName.MetadataRecordName';

      Metadata.CustomMetadataValue customField = new Metadata.CustomMetadataValue();

      customField.field = 'customField__c';

      customField.value = 'New value';

      customMetadata.values.add(customField);

      Metadata.DeployContainer mdContainer = new Metadata.DeployContainer();

      mdContainer.addMetadata(customMetadata);

      // Setup deploy callback, MyDeployCallback implements

      // the Metadata.DeployCallback interface (code for

      // this class not shown in this example)

      MyDeployCallback callback = new MyDeployCallback();

      // Enqueue custom metadata deployment

      Id jobId = Metadata.Operations.enqueueDeployment(mdContainer, callback);

     }

   }

```

Example: Create Two Metadata Records Synchronously

Create a metadata record along with another one that references it in the same transaction. If the parent record was installed with a
namespace, prefix the developer name with _`recordNs__`_ .


Apex Reference Guide Operations Class

Note: No custom metadata relationship can relate records of the same type to each other.

```
   public class CreateMetadata {

      public Id doCreate(

        String parentRecDevName,

        String parentRecLabel,

        String childRecDevName,

        String childRecLabel) {

        Metadata.DeployContainer mdContainer = new Metadata.DeployContainer();

        Metadata.CustomMetadata parentRecord = new Metadata.CustomMetadata();

        parentRecord.fullName = 'ParentType.' + parentRecDevName;

        parentRecord.label = parentRecLabel;

        mdContainer.addMetadata(parentRecord);

        Metadata.CustomMetadata childRecord = new Metadata.CustomMetadata();

        childRecord.fullName = 'ChildType.' + childRecDevName;

        childRecord.label = childRecLabel;

        Metadata.CustomMetadataValue relValue = new Metadata.CustomMetadataValue();

        relValue.field = 'Parent__c';

        relValue.value = parentRecDevName;

        childRecord.values.add(relValue);

        mdContainer.addMetadata(childRecord);

        Id jobId = Metadata.Operations.enqueueDeployment(mdContainer, null);

        return jobId;

      }

   }

```

IN THIS SECTION:

#### Operations Methods Operations Methods The following are methods for Operations .

IN THIS SECTION:

clone()
Makes a duplicate copy of the `Metadata.Operations` .

enqueueDeployment(container, callback)
Deploys custom metadata components asynchronously.

retrieve(type, fullNames)
Retrieves a list of custom metadata components.


Apex Reference Guide Operations Class

##### clone()

Makes a duplicate copy of the `Metadata.Operations` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

##### enqueueDeployment(container, callback)

Deploys custom metadata components asynchronously.

Signature

To preserve service function, we limit the number of Metadata API deployments originating from Apex that can be enqueued at a time.
See Limit on Enqueued Deployments from Apex.

```
   public static Id enqueueDeployment(Metadata.DeployContainer container,

   Metadata.DeployCallback callback)

```

Parameters

```
   container
```

Type: Metadata.DeployContainer

Container that contains the set of metadata components to deploy.

```
   callback
```

Type: Metadata.DeployCallback

A class that implements the `Metadata.DeployCallback` interface. Used by Salesforce to return information about the
deployment results.

Return Value

Type: Id

ID of deployment request.

##### retrieve(type, fullNames)

Retrieves a list of custom metadata components.

Signature

```
   public static List<Metadata.Metadata> retrieve(Metadata.MetadataType type, List<String>

   fullNames)

```


### Apex Reference Guide PlatformActionList Class

Parameters

```
   type
```

Type: Metadata.MetadataType

The metadata component type.

```
   fullNames
```

Type: List<String>

A list of component names to retrieve. For information on component name formats, see Metadata.fullName().

Return Value

Type: List<Metadata.Metadata>

### PlatformActionList Class

Represents the list of actions, and their order, that display in the Salesforce mobile action bar for the layout.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “PlatformActionList” in the
_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### PlatformActionList Properties

PlatformActionList Methods

#### PlatformActionList Properties

### The following are properties for PlatformActionList .

IN THIS SECTION:

actionListContext
The context of the action list.

platformActionListItems
The actions in the platform action list.

relatedSourceEntity
When the `actionListContext` property is “RelatedList” or” “RelatedListRecord”, this field represents the API name of the
related list to which the action belongs.


Apex Reference Guide PlatformActionList Class

##### actionListContext

The context of the action list.

Signature

```
   public Metadata.PlatformActionListContextEnum actionListContext {get; set;}

```

Property Value

Type: Metadata.PlatformActionListContextEnum

##### platformActionListItems

The actions in the platform action list.

Signature

```
   public List<Metadata.PlatformActionListItem> platformActionListItems {get; set;}

```

Property Value

Type: List<Metadata.PlatformActionListItem>

##### relatedSourceEntity When the actionListContext property is “RelatedList” or” “RelatedListRecord”, this field represents the API name of the related

list to which the action belongs.

Signature

```
   public String relatedSourceEntity {get; set;}

```

Property Value

Type: String

#### PlatformActionList Methods The following are methods for PlatformActionList .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.PlatformActionList` .

##### clone()

Makes a duplicate copy of the `Metadata.PlatformActionList` .


### Apex Reference Guide PlatformActionListContextEnum Enum

Signature

```
   public Object clone()

```

Return Value

Type: Object

### PlatformActionListContextEnum Enum

Describes the different contexts of action lists.

Enum Values

The following are the values of the `Metadata.PlatformActionListContextEnum` enum.

**Value** **Description**

`ActionDefinition` Action definition context.

`Assistant` Assistant context.

`BannerPhoto` Banner photo context.

`Chatter` Chatter context.

`Dockable` Dockable context.

`FeedElement` Feed element context.

`Flexipage` Flexipage context.

`Global_x` Global context.

`ListView` Listview context.

`ListViewDefinition` Listview definition context.

`ListViewRecord` Listview record context.

`Lookup` Lookup context.

`MruList` MRU list context.

`MruRow` MRU row context.

`ObjectHomeChart` Object home chart context.

`Photo` Photo context

`Record` Record context.

`RecordEdit` Record edit context

`RelatedList` Related list context.

`RelatedListRecord` Related list record context.


### Apex Reference Guide PlatformActionListItem Class PlatformActionListItem Class

Represents an action in the platform action list for a layout.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “PlatformActionListItem” in the
_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### PlatformActionListItem Properties

PlatformActionListItem Methods

#### PlatformActionListItem Properties

### The following are properties for PlatformActionListItem .

IN THIS SECTION:

##### actionName

The API name for the action in the list.

##### actionType

The type of action.

sortOrder
The placement of the action in the list.

subtype
The subtype of the action.

##### actionName

The API name for the action in the list.

Signature

```
   public String actionName {get; set;}

```

Property Value

Type: String

##### actionType

The type of action.


Apex Reference Guide PlatformActionListItem Class

Signature

```
   public Metadata.PlatformActionTypeEnum actionType {get; set;}

```

Property Value

Type: Metadata.PlatformActionTypeEnum

##### sortOrder

The placement of the action in the list.

Signature

```
   public Integer sortOrder {get; set;}

```

Property Value

Type: Integer

##### subtype

The subtype of the action.

Signature

```
   public String subtype {get; set;}

```

Property Value

Type: String

#### PlatformActionListItem Methods The following are methods for PlatformActionListItem .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.PlatformActionListItem` .

##### clone()

Makes a duplicate copy of the `Metadata.PlatformActionListItem` .

Signature

```
   public Object clone()

```


### Apex Reference Guide PlatformActionTypeEnum Enum

Return Value

Type: Object

### PlatformActionTypeEnum Enum

The type of action for a `PlatformActionListItem` .

Enum Values

The following are the values of the `Metadata.PlatformActionTypeEnum` enum.

**Value** **Description**

`ActionLink` An indicator on a feed element that targets an API, a web page, or a file, represented
by a button in the Salesforce Chatter feed UI.

`CustomButton` When clicked, opens a URL or a Visualforce page in a window or executes JavaScript.

`InvocableAction` An invocable action such as posting to Chatter.

`ProductivityAction` Productivity actions are predefined by Salesforce and are attached to a limited set
of objects. You can’t edit or delete productivity actions.

`QuickAction` A global or object-specific action.

`StandardButton` A predefined Salesforce button such as New, Edit, and Delete.

### PrimaryTabComponents Class

Represents custom console components on primary tabs in the Salesforce console.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “PrimaryTabComponents” in
the _[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### PrimaryTabComponents Properties

PrimaryTabComponents Methods

#### PrimaryTabComponents Properties

### The following are properties for PrimaryTabComponents .


Apex Reference Guide PrimaryTabComponents Class

IN THIS SECTION:

##### component

Represents a custom console component (Visualforce page, lookup field, or related lists) on a section of a page layout.

##### containers

Represents a location and style in which to display more than one custom console component on the sidebars of the Salesforce
console.

##### component

Represents a custom console component (Visualforce page, lookup field, or related lists) on a section of a page layout.

Signature

```
   public List<Metadata.ConsoleComponent> component {get; set;}

```

Property Value

Type: List<Metadata.ConsoleComponent>

##### containers

Represents a location and style in which to display more than one custom console component on the sidebars of the Salesforce console.

Signature

```
   public List<Metadata.Container> containers {get; set;}

```

Property Value

Type: List<Metadata.Container>

#### PrimaryTabComponents Methods The following are methods for PrimaryTabComponents .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.PrimaryTabComponents` .

##### clone()

Makes a duplicate copy of the `Metadata.PrimaryTabComponents` .

Signature

```
   public Object clone()

```


### Apex Reference Guide QuickActionList Class

Return Value

Type: Object

### QuickActionList Class

Represents the list of actions associated with the page layout.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “QuickActionList” in the _[Metadata](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_
_[API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### QuickActionList Properties QuickActionList Methods QuickActionList Properties

### The following are properties for QuickActionList .

IN THIS SECTION:

##### quickActionListItems
### List of QuickActionList objects.

##### quickActionListItems

### List of QuickActionList objects.

Signature

```
   public List<Metadata.QuickActionListItem> quickActionListItems {get; set;}

```

Property Value

Type: List<Metadata.QuickActionListItem>

#### QuickActionList Methods

### The following are methods for QuickActionList .


### Apex Reference Guide QuickActionListItem Class

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.QuickActionList` .

##### clone()

Makes a duplicate copy of the `Metadata.QuickActionList` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### QuickActionListItem Class Represents an action in the QuickActionList .

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “QuickActionListItem” in the
_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### QuickActionListItem Properties

QuickActionListItem Methods

#### QuickActionListItem Properties

### The following are properties for QuickActionListItem .

IN THIS SECTION:

##### quickActionName

The API name of the action.

##### quickActionName

The API name of the action.


### Apex Reference Guide RelatedContent Class

Signature

```
   public String quickActionName {get; set;}

```

Property Value

Type: String

#### QuickActionListItem Methods The following are methods for QuickActionListItem .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.QuickActionListItem` .

##### clone()

Makes a duplicate copy of the `Metadata.QuickActionListItem` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### RelatedContent Class

Represents the Mobile Cards section of the page layout.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “RelatedContent” in the _[Metadata](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_
_[API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

RelatedContent Properties

RelatedContent Methods


### Apex Reference Guide RelatedContentItem Class

#### RelatedContent Properties The following are properties for RelatedContent .

IN THIS SECTION:

##### relatedContentItems

A list of layout items in the Mobile Cards section of the page layout.

##### relatedContentItems

A list of layout items in the Mobile Cards section of the page layout.

Signature

```
   public List<Metadata.RelatedContentItem> relatedContentItems {get; set;}

```

Property Value

Type: List<Metadata.RelatedContentItem>

#### RelatedContent Methods The following are methods for RelatedContent .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.RelatedContent` .

##### clone()

Makes a duplicate copy of the `Metadata.RelatedContent` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### RelatedContentItem Class

#### Represents an individual item in the RelatedContent list.

Namespace

Metadata


Apex Reference Guide RelatedContentItem Class

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “RelatedContentItem” in the
_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### RelatedContentItem Properties RelatedContentItem Methods RelatedContentItem Properties The following are properties for RelatedContentItem .

IN THIS SECTION:

##### layoutItem

An individual layout item in the Mobile Cards section.

##### layoutItem

An individual layout item in the Mobile Cards section.

Signature

```
   public Metadata.LayoutItem layoutItem {get; set;}

```

Property Value

Type: Metadata.LayoutItem

#### RelatedContentItem Methods The following are methods for RelatedContentItem .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.RelatedContentItem` .

##### clone()

Makes a duplicate copy of the `Metadata.RelatedContentItem` .

Signature

```
   public Object clone()

```


### Apex Reference Guide RelatedList Class

Return Value

Type: Object

### RelatedList Class

Represents related list custom components on the sidebars of the Salesforce console.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “RelatedList” in the _[Metadata](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_
_[API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### RelatedList Properties

RelatedList Methods

#### RelatedList Properties

### The following are properties for RelatedList .

IN THIS SECTION:

##### hideOnDetail

When set to true, the related list is hidden from detail pages where it appears as a component to prevent duplicate information from
showing.

name
The name of the component as it appears to console users.

##### hideOnDetail

When set to true, the related list is hidden from detail pages where it appears as a component to prevent duplicate information from
showing.

Signature

```
   public Boolean hideOnDetail {get; set;}

```

Property Value

Type: Boolean


### Apex Reference Guide RelatedListItem Class

##### name

The name of the component as it appears to console users.

Signature

```
   public String name {get; set;}

```

Property Value

Type: String

#### RelatedList Methods The following are methods for RelatedList .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.RelatedList` .

##### clone()

Makes a duplicate copy of the `Metadata.RelatedList` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### RelatedListItem Class

Represents an item in the related list in a page layout.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “RelatedListItem” in the _[Metadata](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_
_[API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

RelatedListItem Properties

RelatedListItem Methods


Apex Reference Guide RelatedListItem Class

#### RelatedListItem Properties The following are properties for RelatedListItem .

IN THIS SECTION:

##### customButtons

A list of custom buttons used in the related list.

##### excludeButtons

A list of excluded related-list buttons.

fields
A list of fields displayed in the related list. Uses aliases instead of field or API names.

quickActions
A list of quick actions used on the related list.

relatedList
The name of the related list.

sortField
The name of the field used for sorting.

sortOrder
When `sortField` is set, the `sortOrder` property determines the sort order.

##### customButtons

A list of custom buttons used in the related list.

Signature

```
   public List<String> customButtons {get; set;}

```

Property Value

Type: List<String>

For more information, see “Define Custom Buttons and Links” in the Salesforce online help.

##### excludeButtons

A list of excluded related-list buttons.

Signature

```
   public List<String> excludeButtons {get; set;}

```

Property Value

Type: List<String>


Apex Reference Guide RelatedListItem Class

##### fields

A list of fields displayed in the related list. Uses aliases instead of field or API names.

Signature

```
   public List<String> fields {get; set;}

```

Property Value

Type: List<String>

##### **`quickActions`**

A list of quick actions used on the related list.

Signature

```
   public List<String> quickActions {get; set;}

```

Property Value

Type: List<String>

##### relatedList

The name of the related list.

Signature

```
   public String relatedList {get; set;}

```

Property Value

Type: String

##### sortField

The name of the field used for sorting.

Signature

```
   public String sortField {get; set;}

```

Property Value

Type: String

##### sortOrder When sortField is set, the sortOrder property determines the sort order.


### Apex Reference Guide ReportChartComponentLayoutItem Class

Signature

```
   public Metadata.SortOrder sortOrder {get; set;}

```

Property Value

Type: Metadata.SortOrder

#### RelatedListItem Methods The following are methods for RelatedListItem .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.RelatedListItem` .

##### clone()

Makes a duplicate copy of the `Metadata.RelatedListItem` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### ReportChartComponentLayoutItem Class

Represents the settings for a report chart on a standard or custom page.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see
“ReportChartComponentLayoutItem” in the _[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

ReportChartComponentLayoutItem Properties

ReportChartComponentLayoutItem Methods


Apex Reference Guide ReportChartComponentLayoutItem Class

#### ReportChartComponentLayoutItem Properties The following are properties for ReportChartComponentLayoutItem .

IN THIS SECTION:

##### cacheData

Indicates whether to use cached data when displaying the chart. When the attribute is set to true, data is cached for 24 hours. When
the attribute is set to false, the report is run every time the page is refreshed.

##### contextFilterableField

Unique development name of the field by which a report chart is filtered to return data relevant to the page. If set, the ID field for
the parent object of the page or report type is the chart data filter. The parent object for the report type and the page must match
for a chart to return relevant data.

error
Error string that is populated only when an error occurs in the underlying report.

hideOnError
Controls whether users see a chart that has an error. When an error occurs and this attribute is not set, the chart doesn’t show any
data except the error. Set the attribute to true to hide the chart from a page on error.

includeContext
If true, filters the report chart to return data that’s relevant to the page.

reportName
Unique development name of a report that includes a chart.

showTitle
If true, applies the title from the report to the chart.

size
Size of the displayed chart. The default is medium.

##### cacheData

Indicates whether to use cached data when displaying the chart. When the attribute is set to true, data is cached for 24 hours. When
the attribute is set to false, the report is run every time the page is refreshed.

Signature

```
   public Boolean cacheData {get; set;}

```

Property Value

Type: Boolean

##### contextFilterableField

Unique development name of the field by which a report chart is filtered to return data relevant to the page. If set, the ID field for the
parent object of the page or report type is the chart data filter. The parent object for the report type and the page must match for a chart
to return relevant data.


Apex Reference Guide ReportChartComponentLayoutItem Class

Signature

```
   public String contextFilterableField {get; set;}

```

Property Value

Type: String

##### error

Error string that is populated only when an error occurs in the underlying report.

Signature

```
   public String error {get; set;}

```

Property Value

Type: String

##### hideOnError

Controls whether users see a chart that has an error. When an error occurs and this attribute is not set, the chart doesn’t show any data
except the error. Set the attribute to true to hide the chart from a page on error.

Signature

```
   public Boolean hideOnError {get; set;}

```

Property Value

Type: Boolean

##### includeContext

If true, filters the report chart to return data that’s relevant to the page.

Signature

```
   public Boolean includeContext {get; set;}

```

Property Value

Type: Boolean

##### reportName

Unique development name of a report that includes a chart.


Apex Reference Guide ReportChartComponentLayoutItem Class

Signature

```
   public String reportName {get; set;}

```

Property Value

Type: String

##### showTitle

If true, applies the title from the report to the chart.

Signature

```
   public Boolean showTitle {get; set;}

```

Property Value

Type: Boolean

##### size

Size of the displayed chart. The default is medium.

Signature

```
   public Metadata.ReportChartComponentSize size {get; set;}

```

Property Value

Type: Metadata.ReportChartComponentSize

#### ReportChartComponentLayoutItem Methods The following are methods for ReportChartComponentLayoutItem .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.ReportChartComponentLayoutItem` .

##### clone()

Makes a duplicate copy of the `Metadata.ReportChartComponentLayoutItem` .

Signature

```
   public Object clone()

```


### Apex Reference Guide ReportChartComponentSize Enum

Return Value

Type: Object

### ReportChartComponentSize Enum

Describes the size of the displayed report chart component.

Enum Values

The following are the values of the `Metadata.ReportChartComponentSize` enum.

**Value** **Description**

`LARGE` Large chart size.

`MEDIUM` Medium chart size.

`SMALL` Small chart size.

### SidebarComponent Class

Represents a specific custom console component to display in a container that hosts multiple components in one of the sidebars of the
Salesforce console.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “SidebarComponent” in the
_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### SidebarComponent Properties

SidebarComponent Methods

#### SidebarComponent Properties

### The following are properties for SidebarComponent .

IN THIS SECTION:

componentType
Specifies the component type. Valid values are “KnowledgeOne”, “Lookup”, “Milestones”, “RelatedList”, “Topics”, “Files”, and
“CaseExperts”.


Apex Reference Guide SidebarComponent Class

##### createAction

If the component is a lookup field, the name of the quick action used to create a record.

enableLinking
If the component is a lookup field, lets users associate a record with this field.

height
The height of the component in the container. The `unit` property determines the unit of measurement, in pixels or percent.

knowledgeOneEnable
Indicates if the component is enabled for Knowledge One.

label
The name of the component as it displays to console users. Available for components in a container with the style of tabs or accordion.

lookup
If the component is a lookup field, the name of the field.

page_x
If the component is a Visualforce page, the name of the Visualforce page.

relatedLists
If the component is a related list component, the list of related list names.

unit
The unit of measurement (pixels or percent) for the height and width of the component in the container.

updateAction
If the component is a lookup field, the name of the quick action used to update a record.

width
The width of the component in the container. The `unit` property determines the unit of measurement, in pixels or percent.

##### componentType

Specifies the component type. Valid values are “KnowledgeOne”, “Lookup”, “Milestones”, “RelatedList”, “Topics”, “Files”, and “CaseExperts”.

Signature

```
   public String componentType {get; set;}

```

Property Value

Type: String

##### createAction

If the component is a lookup field, the name of the quick action used to create a record.

Signature

```
   public String createAction {get; set;}

```


Apex Reference Guide SidebarComponent Class

Property Value

Type: String

##### enableLinking

If the component is a lookup field, lets users associate a record with this field.

Signature

```
   public Boolean enableLinking {get; set;}

```

Property Value

Type: Boolean

##### height

The height of the component in the container. The `unit` property determines the unit of measurement, in pixels or percent.

Signature

```
   public Integer height {get; set;}

```

Property Value

Type: Integer

##### knowledgeOneEnable

Indicates if the component is enabled for Knowledge One.

Signature

```
   public Boolean knowledgeOneEnable {get; set;}

```

Property Value

Type: Boolean

##### label

The name of the component as it displays to console users. Available for components in a container with the style of tabs or accordion.

Signature

```
   public String label {get; set;}

```

Property Value

Type: String


Apex Reference Guide SidebarComponent Class

##### lookup

If the component is a lookup field, the name of the field.

Signature

```
   public String lookup {get; set;}

```

Property Value

Type: String

##### page_x

If the component is a Visualforce page, the name of the Visualforce page.

Signature

```
   public String page_x {get; set;}

```

Property Value

Type: String

##### relatedLists

If the component is a related list component, the list of related list names.

Signature

```
   public List<Metadata.RelatedList> relatedLists {get; set;}

```

Property Value

Type: List<Metadata.RelatedList>

##### unit

The unit of measurement (pixels or percent) for the height and width of the component in the container.

Signature

```
   public String unit {get; set;}

```

Property Value

Type: String

##### updateAction

If the component is a lookup field, the name of the quick action used to update a record.


### Apex Reference Guide SortOrder Enum

Signature

```
   public String updateAction {get; set;}

```

Property Value

Type: String

##### width

The width of the component in the container. The `unit` property determines the unit of measurement, in pixels or percent.

Signature

```
   public Integer width {get; set;}

```

Property Value

Type: Integer

#### SidebarComponent Methods The following are methods for SidebarComponent .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.SidebarComponent` .

##### clone()

Makes a duplicate copy of the `Metadata.SidebarComponent` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### SortOrder Enum

Describes the sort order of a related list.

Enum Values

The following are the values of the `Metadata.SortOrder` enum.


### Apex Reference Guide StatusCode Enum

**Value** **Description**

`Asc_x` Sort in ascending order.

`Desc_x` Sort in descending order.

### StatusCode Enum

Describes the status code for an unsuccessful component deploy.

Enum Values

The following are the values of the `Metadata.StatusCode` enum.

**Value** **Description**

`INVALID_SCS_INBOUND_USER` Log in as the RunAs user configured in your SCS setup.

`REQUIRE_CONNECTED_APP_SCS` SCS Connected App is not installed.

`REQUIRE_CONNECTED_APP_SESSION_SCS` To use the SCS connected app, the user must be authenticated.

`REQUIRE_RUNAS_USER` A RunAs user must be configured in your org.

SEE ALSO:

DeployProblemType Enum

### SubtabComponents Class

Represents custom console components on subtabs in the Salesforce console.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “SubtabComponents” in the
_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### SubtabComponents Properties

SubtabComponents Methods

#### SubtabComponents Properties

### The following are properties for SubtabComponents .


Apex Reference Guide SubtabComponents Class

IN THIS SECTION:

##### component

Represents a custom console component (Visualforce page, lookup field, or related lists) on a section of a page layout.

##### containers

Represents a location and style in which to display more than one custom console component on the sidebars of the Salesforce
console.

##### component

Represents a custom console component (Visualforce page, lookup field, or related lists) on a section of a page layout.

Signature

```
   public List<Metadata.ConsoleComponent> component {get; set;}

```

Property Value

Type: List<Metadata.ConsoleComponent>

##### containers

Represents a location and style in which to display more than one custom console component on the sidebars of the Salesforce console.

Signature

```
   public List<Metadata.Container> containers {get; set;}

```

Property Value

Type: List<Metadata.Container>

#### SubtabComponents Methods The following are methods for SubtabComponents .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.SubtabComponents` .

##### clone()

Makes a duplicate copy of the `Metadata.SubtabComponents` .

Signature

```
   public Object clone()

```


### Apex Reference Guide SummaryLayoutStyleEnum Enum

Return Value

Type: Object

### SummaryLayoutStyleEnum Enum Describes the highlights panel style for a SummaryLayout .

Enum Values

The following are the values of the `Metadata.SummaryLayoutStyleEnum` enum.

**Value** **Description**

`CaseInteraction` Case interaction style.

`ChildServiceReportTemplateStyle` Child service report template style.

`DefaultQuoteTemplate` Default quote template style.

`DefaultServiceReportTemplate` Default service report style

`Default_x` Default style.

`PathAssistant` Path assisstant style.

`QuickActionLayoutLeftRight` Quick action left-right layout style.

`QuickActionLayoutTopDown` Quick action top-down layout style.

`QuoteTemplate` Quote template style.

`ServiceReportTemplate` Service report style.

### SummaryLayout Class

Controls the appearance of the highlights panel, which summarizes key fields in a grid at the top of a page layout, when Case Feed is
enabled.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “SummaryLayout” in the
_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

SummaryLayout Properties

SummaryLayout Methods


Apex Reference Guide SummaryLayout Class

#### SummaryLayout Properties The following are properties for SummaryLayout .

IN THIS SECTION:

##### masterLabel

The name of the layout label.

##### sizeX

Number of columns in the highlights pane, between 1 and 4 (inclusive).

sizeY
Number of rows in each column, either 1 or 2.

sizeZ
If provided, the setting is not visible to users.

summaryLayoutItems
Controls the appearance of an individual field and its column and row position within the highlights panel grid, when Case Feed is
enabled. At least one is required.

summaryLayoutStyle
Specifies the panel style.

##### masterLabel

The name of the layout label.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Signature

```
   public String masterLabel {get; set;}

```

Property Value

Type: String

##### sizeX

Number of columns in the highlights pane, between 1 and 4 (inclusive).

Signature

```
   public Integer sizeX {get; set;}

```

Property Value

Type: Integer


Apex Reference Guide SummaryLayout Class

##### sizeY

Number of rows in each column, either 1 or 2.

Signature

```
   public Integer sizeY {get; set;}

```

Property Value

Type: Integer

##### sizeZ

If provided, the setting is not visible to users.

Signature

```
   public Integer sizeZ {get; set;}

```

Property Value

Type: Integer

##### summaryLayoutItems

Controls the appearance of an individual field and its column and row position within the highlights panel grid, when Case Feed is
enabled. At least one is required.

Signature

```
   public List<Metadata.SummaryLayoutItem> summaryLayoutItems {get; set;}

```

Property Value

Type: List<Metadata.SummaryLayoutItem>

##### summaryLayoutStyle

Specifies the panel style.

Signature

```
   public Metadata.SummaryLayoutStyleEnum summaryLayoutStyle {get; set;}

```

Property Value

Type: Metadata.SummaryLayoutStyleEnum


### Apex Reference Guide SummaryLayoutItem Class

#### SummaryLayout Methods The following are methods for SummaryLayout .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.SummaryLayout` .

##### clone()

Makes a duplicate copy of the `Metadata.SummaryLayout` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### SummaryLayoutItem Class

Controls the appearance of an individual field and its column and row position within the highlights panel grid, when Case Feed is
enabled. You can have two fields per each grid in a highlights panel.

Namespace

Metadata

Usage

Use this class when accessing `Metadata.Layout` metadata components. For more information, see “SummaryLayoutItem” in the
_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_intro.htm)_ .

IN THIS SECTION:

#### SummaryLayoutItem Properties

SummaryLayoutItem Methods

#### SummaryLayoutItem Properties

### The following are properties for SummaryLayoutItem .

IN THIS SECTION:

customLink
The custom link reference.


Apex Reference Guide SummaryLayoutItem Class

##### field

The field name reference, relative to the page layout. Must be a standard or custom field that also exists on the detail page.

##### posX

The item's column position in the highlights panel grid. Must be within the range of `sizeX` .

##### posY

The item's row position in the highlights panel grid. Must be within the range of `sizeY` .

posZ
Reserved for future use. If provided, the setting is not visible to users.

##### customLink

The custom link reference.

Signature

```
   public String customLink {get; set;}

```

Property Value

Type: String

##### field

The field name reference, relative to the page layout. Must be a standard or custom field that also exists on the detail page.

Signature

```
   public String field {get; set;}

```

Property Value

Type: String

##### posX

The item's column position in the highlights panel grid. Must be within the range of `sizeX` .

Signature

```
   public Integer posX {get; set;}

```

Property Value

Type: Integer

##### posY

The item's row position in the highlights panel grid. Must be within the range of `sizeY` .


### Apex Reference Guide UiBehavior Enum

Signature

```
   public Integer posY {get; set;}

```

Property Value

Type: Integer

##### posZ

Reserved for future use. If provided, the setting is not visible to users.

Signature

```
   public Integer posZ {get; set;}

```

Property Value

Type: Integer

#### SummaryLayoutItem Methods The following are methods for SummaryLayoutItem .

IN THIS SECTION:

##### clone()

Makes a duplicate copy of the `Metadata.SummaryLayoutItem` .

##### clone()

Makes a duplicate copy of the `Metadata.SummaryLayoutItem` .

Signature

```
   public Object clone()

```

Return Value

Type: Object

### UiBehavior Enum

Describes the behavior for a layout item on a layout page.

Enum Values

The following are the values of the `Metadata.UiBehavior` enum.


## Apex Reference Guide PlaceQuote Namespace

**Value** **Description**

`Edit` The layout field can be edited but is not required.

`Readonly` The layout field is read-only.

`Required` The layout field can be edited and is required.

## PlaceQuote Namespace The PlaceQuote namespace provides classes and methods to create or update quotes with pricing preferences and configuration

options.

[See PlaceQuote namespace for more information about the available classes and methods.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_namespace_placequote.htm)

## Pref_center Namespace

The Pref_center namespace provides an interface, classes, and methods to create and retrieve data in forms in Preference Manager.
Preference Manager, previously called Preference Center, is a feature within the Privacy Center app.

## The following are the classes in the Pref_center namespace.

IN THIS SECTION:

### LoadFormData Class

Retrieve records related to the tokenized record id, and populate the values of a preference form.

LoadParameters Class
Contains methods to retrieve record Id information for parameters passed into the load-form handler.

PreferenceCenterApexHandler Interface
Pass data between your organization and a form in Preference Manager.

SubmitFormData Class
Contains methods to retrieve information on buttons and options selected in a preference form.

SubmitParameters Class
Retrieve record ID information to use with your submit-form handler.

TokenType Enum
Defines the types of values supported by the TokenUtility methods.

TokenUtility Class
Generate authentication tokens to access preference forms.

ValidationResult Class
This class is reserved for future use with Preference Manager.

### LoadFormData Class

Retrieve records related to the tokenized record id, and populate the values of a preference form.


Apex Reference Guide LoadFormData Class

Namespace

Pref_center

Example

#### Use methods in the LoadFormData class to set available and selected values in different form components:

```
   List<System.SelectOption> picklistOptions = new List<System.SelectOption>();

   picklistOptions.add(new System.SelectOption('optIn', 'Opt In'));

   picklistOptions.add(new System.SelectOption('optOut', 'Opt Out'));

   // Set the available options for the picklist

   loadFormData.setOptions('myPicklist', picklistOptions);

   // Add an option to the existing options for the picklist

   loadFormData.addOption('myPicklist', 'optOutAll', 'Opt Out All');

   // Select the 'optIn' option in the picklist

   loadFormData.setSelectedOption('myPicklist', 'optIn');

   List<System.SelectOption> checkboxOptions = new List<System.SelectOption>();

   checkboxOptions.add(new System.SelectOption('yes', 'Yes'));

   checkboxOptions.add(new System.SelectOption('no', 'No'));

   // Set available options for the checkbox group

   loadFormData.setOptions('myCheckbox', checkboxOptions);

   // Select the 'yes' option in the checkbox group

   loadFormData.addSelectedOption('myCheckbox', 'yes');

   // Also select the 'no' option in the checkbox group

   loadFormData.addSelectedOption('myCheckbox', 'no');

   // Another way to select both the 'yes' and 'no' options in the checkbox group

   loadFormData.setSelectedOptions('myCheckbox', new List<String>{'yes', 'no'});

   // Fill the value in the text input

   loadFormData.setTextValue('myTextInput', 'admin@salesforce.com');

   // Set the hint text for the text input

   loadFormData.setTextHint('myTextInput', 'Email Address');

   // Set the label for the button

   loadFormData.setButtonLabel('myButton', 'Save Preferences');

```

IN THIS SECTION:

#### LoadFormData Constructors

LoadFormData Methods

#### LoadFormData Constructors The following are constructors for LoadFormData .


Apex Reference Guide LoadFormData Class

IN THIS SECTION:

##### LoadFormData(data) Creates an instance of the LoadFormData class for running tests on any custom Apex classes you create for Preference Manager. **`LoadFormData(data)`** Creates an instance of the LoadFormData class for running tests on any custom Apex classes you create for Preference Manager.

Signature

```
   public LoadFormData(Map<String,pref_center.FieldProperties> data)

```

Parameters

```
   data
```

Type: Map<String,pref_center.FieldProperties>Map

Maps preference form data from the field ID to the field properties.

Usage

This constructor is available in API version 56.0 and later.

#### LoadFormData Methods

##### The following are methods for LoadFormData .

IN THIS SECTION:

addOption(fieldId, value, label)
Add an option for a checkbox, picklist, or radio button field in a preference form using the label and value.

addOption(fieldId, option)
Add a defined, selectable option for a checkbox, picklist, or radio button field in a preference form.

addSelectedOption(fieldId, option)
Add a selected option for a checkbox field in a preference form. This requires the field on the form to have a defined option with a
set value.

setButtonLabel(fieldId, label)
Set the label of a button added to the preference form.

setOptions(fieldId, options)
Add a list of selectable options for a field on a preference form.

setSelectedOption(fieldId, optionValue)
For a picklist or radio button field on a preference form that has defined values, set the value entered in the optionValue field as the
selected option.

setSelectedOptions(fieldId, options)
For an existing checkbox field on a preference form that has defined values, set the values entered in the options field as the selected
options. This requires the field on the form to have defined options with a set value.


Apex Reference Guide LoadFormData Class

setTextHint(fieldId, hintText)
Set the hint text inside a text input field. The hint text tells the user what type of information to enter, like an email address.

setTextValue(fieldId, value)
Set the value of a text field in a preference form.

##### **`addOption(fieldId, value, label)`**

Add an option for a checkbox, picklist, or radio button field in a preference form using the label and value.

Signature

```
   public void addOption(String fieldId, String value, String label)

```

Parameters

```
   fieldId
```

Type: String

Identifies a field in the preference form.

```
   value
```

Type: String

Represents the selection or text entered in a preference form field.

```
   label
```

Type: String

The label for the value of a field in a preference form.

Return Value

Type: void

##### **`addOption(fieldId, option)`**

Add a defined, selectable option for a checkbox, picklist, or radio button field in a preference form.

Signature

```
   public void addOption(String fieldId, System.SelectOption option)

```

Parameters

```
   fieldId
```

Type: String

Identifies a field in the preference form.

```
   option
```

Type: System.SelectOption

The option selected on a field in the preference form.


Apex Reference Guide LoadFormData Class

Return Value

Type: void

##### **`addSelectedOption(fieldId, option)`**

Add a selected option for a checkbox field in a preference form. This requires the field on the form to have a defined option with a set
value.

Signature

```
   public void addSelectedOption(String fieldId, String option)

```

Parameters

```
   fieldId
```

Type: String

Identifies a field in the preference form.

```
   option
```

Type: String

The selectable option being added.

Return Value

Type: void

##### **`setButtonLabel(fieldId, label)`**

Set the label of a button added to the preference form.

Signature

```
   public void setButtonLabel(String fieldId, String label)

```

Parameters

```
   fieldId
```

Type: String

Identifies a field in the preference form.

```
   label
```

Type: String

The label for a button added to the preference form.

Return Value

Type: void


Apex Reference Guide LoadFormData Class

##### **`setOptions(fieldId, options)`**

Add a list of selectable options for a field on a preference form.

Signature

```
   public void setOptions(String fieldId, List<System.SelectOption> options)

```

Parameters

```
   fieldId
```

Type: String

Identifies a field in the preference form.

```
   options
```

Type: List<System.SelectOption>

The selectable options for a field in the preference form.

Return Value

Type: void

##### **`setSelectedOption(fieldId, optionValue)`**

For a picklist or radio button field on a preference form that has defined values, set the value entered in the optionValue field as the
selected option.

Signature

```
   public void setSelectedOption(String fieldId, String optionValue)

```

Parameters

```
   fieldId
```

Type: String

Identifies a field in the preference form.

```
   optionValue
```

Type: String

The value for the selected option.

Return Value

Type: void

##### **`setSelectedOptions(fieldId, options)`**

For an existing checkbox field on a preference form that has defined values, set the values entered in the options field as the selected
options. This requires the field on the form to have defined options with a set value.


Apex Reference Guide LoadFormData Class

Signature

```
   public void setSelectedOptions(String fieldId, List<String> options)

```

Parameters

```
   fieldId
```

Type: String

Identifies the checkbox field in the preference form.

```
   options
```

Type: List<String>

The selected options for a field in the preference form.

Return Value

Type: void

##### **`setTextHint(fieldId, hintText)`**

Set the hint text inside a text input field. The hint text tells the user what type of information to enter, like an email address.

Signature

```
   public void setTextHint(String fieldId, String hintText)

```

Parameters

```
   fieldId
```

Type: String

The ID of the text input field in the preference form.

```
   hintText
```

Type: String

The hint text in the text input field.

Return Value

Type: void

##### **`setTextValue(fieldId, value)`**

Set the value of a text field in a preference form.

Signature

```
   public void setTextValue(String fieldId, String value)

```


### Apex Reference Guide LoadParameters Class

Parameters

```
   fieldId
```

Type: String

Identifies a field in the preference form.

```
   value
```

Type: String

Represents the value entered for the text field in a preference form.

Return Value

Type: void

### LoadParameters Class

Contains methods to retrieve record Id information for parameters passed into the load-form handler.

Namespace

Pref_center

Example

```
   String userId = loadParams.getRecordId();

   User user = [select id, AboutMe from User where id=:userId];

```

IN THIS SECTION:

#### LoadParameters Methods LoadParameters Methods

### The following are methods for LoadParameters .

IN THIS SECTION:

##### getRecordId()

Returns the untokenized version of the record Id.

##### **`getRecordId()`**

Returns the untokenized version of the record Id.

Signature

```
   public String getRecordId()

```


### Apex Reference Guide PreferenceCenterApexHandler Interface

Return Value

Type: String

### PreferenceCenterApexHandler Interface

Pass data between your organization and a form in Preference Manager.

Namespace

Pref_center

IN THIS SECTION:

#### PreferenceCenterApexHandler Methods PreferenceCenterApexHandler Methods

### The following are methods for PreferenceCenterApexHandler .

IN THIS SECTION:

##### load(loadParams, formData, validationResult)

Retrieve the record IDs and initial values from a preference form before it is edited and submitted.

submit(loadParams, formData, validationResult)
Updates the changed values of fields when the preference form is submitted.

##### **`load(loadParams, formData, validationResult)`**

Retrieve the record IDs and initial values from a preference form before it is edited and submitted.

Signature

```
   public pref_center.LoadFormData load(pref_center.LoadParameters loadParams,

   pref_center.LoadFormData formData, pref_center.ValidationResult validationResult)

```

Parameters

```
   loadParams
```

Type: pref_center.LoadParameters

Retrieve the tokenized record ID.

```
   formData
```

Type: pref_center.LoadFormData

Set the initial values of fields in a form before they are edited.

```
   validationResult
```

Type: pref_center.ValidationResult

Reserved for future use.


### Apex Reference Guide SubmitFormData Class

Return Value

Type: pref_center.LoadFormData

##### **`submit(loadParams, formData, validationResult)`**

Updates the changed values of fields when the preference form is submitted.

Signature

```
   public void submit(pref_center.SubmitParameters submitParams, pref_center.SubmitFormData

   formData, pref_center.ValidationResult validationResult)

```

Parameters

```
   submitParams
```

Type: pref_center.SubmitParameters

Retrieve the tokenized record Id.

```
   formData
```

Type: pref_center.SubmitFormData

Retrieve the values of fields in a submitted form.

```
   validationResult
```

Type: pref_center.ValidationResult

Reserved for future use.

Return Value

Type: void

### SubmitFormData Class

Contains methods to retrieve information on buttons and options selected in a preference form.

Namespace

Pref_center

Example

### Use methods in the SubmitFormData class to retrieve the selected values in different form components:

```
   String buttonClickedId = formData.getButtonClicked();

   if (buttonClickedId == 'submitButton') {

   // Handle form submit

   } else if (buttonClickedId == 'cancelButton') {

   // Handle form cancel

   }

   String picklistValueOld = formData.getOldSelectedValue('myPicklist');

```


Apex Reference Guide SubmitFormData Class

```
   String picklistValueNew = formData.getSelectedValue('myPicklist');

   if (picklistValueOld != picklistValueNew) {

   // Do something

   }

   List<String> checkboxValuesOld = formData.getOldSelectedValues('myCheckbox');

   List<String> checkboxValuesNew = formData.getSelectedValues('myCheckbox');

   if (checkboxValuesOld != null && checkboxValuesNew != null && (checkboxValuesOld.size()

   != checkboxValuesNew.size())) {

   // Do something

   }

   String textinputValueOld = formData.getOldStringValue('myTextinput');

   String textinputValueNew = formData.getStringValue('myTextinput');

   if (textinputValueOld != textinputValueNew) {

   // Do something

   }

```

IN THIS SECTION:

#### SubmitFormData Methods SubmitFormData Methods The following are methods for SubmitFormData .

IN THIS SECTION:

getButtonClicked()
Returns the field ID of the button that was clicked in the preference form. For example, use this method to determine if the clicked
#### button was Submit or Cancel .

getOldSelectedValue(fieldId)
Returns the value that was set for the specified field when the preference form was previously edited by the user. This method is
used for field types such as picklist or radio buttons.

getOldSelectedValues(fieldId)
Returns a list of the string values that were set on a checkbox field when the preference form was previously edited by the user.

getOldStringValue(fieldId)
Returns the string value that was set on a field when the preference form was loaded. This method is used for field types such as
text, and throws a TypeException if used with a field that can return more than one value, like a checkbox field.

getSelectedValue(fieldId)
Returns the string value that is currently selected for a picklist or radio button field in the preference form.

getSelectedValues(fieldId)
Returns a list of string values that are currently selected on a checkbox field in the preference form.

getStringValue(fieldId)
Returns the string value that was set on a field when the preference form was loaded. This method is used for field types such as
text.


Apex Reference Guide SubmitFormData Class

##### **`getButtonClicked()`**

Returns the field ID of the button that was clicked in the preference form. For example, use this method to determine if the clicked button
was **Submit** or **Cancel** .

Signature

```
   public String getButtonClicked()

```

Return Value

Type: String

##### **`getOldSelectedValue(fieldId)`**

Returns the value that was set for the specified field when the preference form was previously edited by the user. This method is used
for field types such as picklist or radio buttons.

Signature

```
   public String getOldSelectedValue(String fieldId)

```

Parameters

```
   fieldId
```

Type: String

Identifies a field in the preference form.

Return Value

Type: String

##### **`getOldSelectedValues(fieldId)`**

Returns a list of the string values that were set on a checkbox field when the preference form was previously edited by the user.

Signature

```
   public List<String> getOldSelectedValues(String fieldId)

```

Parameters

```
   fieldId
```

Type: String

Identifies a field in the preference form.

Return Value

Type: List<String>


Apex Reference Guide SubmitFormData Class

##### **`getOldStringValue(fieldId)`**

Returns the string value that was set on a field when the preference form was loaded. This method is used for field types such as text,
and throws a TypeException if used with a field that can return more than one value, like a checkbox field.

Signature

```
   public String getOldStringValue(String fieldId)

```

Parameters

```
   fieldId
```

Type: String

Identifies a field in the preference form.

Return Value

Type: String

##### **`getSelectedValue(fieldId)`**

Returns the string value that is currently selected for a picklist or radio button field in the preference form.

Signature

```
   public String getSelectedValue(String fieldId)

```

Parameters

```
   fieldId
```

Type: String

Identifies a field in the preference form.

Return Value

Type: String

##### **`getSelectedValues(fieldId)`**

Returns a list of string values that are currently selected on a checkbox field in the preference form.

Signature

```
   public List<String> getSelectedValues(String fieldId)

```

Parameters

```
   fieldId
```

Type: String

Identifies a field in the preference form.


### Apex Reference Guide SubmitParameters Class

Return Value

Type: List<String>

##### **`getStringValue(fieldId)`**

Returns the string value that was set on a field when the preference form was loaded. This method is used for field types such as text.

Signature

```
   public String getStringValue(String fieldId)

```

Parameters

```
   fieldId
```

Type: String

Identifies a field in the preference form.

Return Value

Type: String

### SubmitParameters Class

Retrieve record ID information to use with your submit-form handler.

Namespace

Pref_center

Example

```
   String userId = submitParams.getRecordId();

   User user = [select id, AboutMe from User where id=:userId];

```

IN THIS SECTION:

#### SubmitParameters Methods SubmitParameters Methods

### The following are methods for SubmitParameters .

IN THIS SECTION:

getRecordId()
Returns the untokenized version of the record ID.


### Apex Reference Guide TokenType Enum

##### **`getRecordId()`**

Returns the untokenized version of the record ID.

Signature

```
   public String getRecordId()

```

Return Value

Type: String

### TokenType Enum

Defines the types of values supported by the TokenUtility methods.

Enum Values

The following are the values of the `pref_center.TokenType` enum.

**Value** **Description**

`EMAIL` Identifies the token as an email address.

`STANDARD` Identifies the token as a Salesforce record ID. This is the default token type.

### TokenUtility Class

Generate authentication tokens to access preference forms.

Namespace

Pref_center

Example

Call the `generateToken()` method to generate a single token for a specified Salesforce record ID:

```
   Individual individual = [SELECT Id FROM Individual LIMIT 1];

   String token = pref_center.TokenUtility.generateToken(individual.Id);

   // Do something with the token

   System.debug(token)

```

Call the `generateTokens()` method to generate tokens in bulk when given a list of Salesforce record IDs:

```
   List<Id> individualIds = new List<Id>();

   // Get Ids of Individuals who have not opted out of tracking

   for (Individual individual : [SELECT Id FROM Individual WHERE HasOptedOutTracking = false])

    {

      individualIds.add(individual.Id);

   }

```


Apex Reference Guide TokenUtility Class

```
   // Generate tokens for the list of Individual record Ids

   Map<String, String> tokens = pref_center.TokenUtility.generateTokens(individualIds);

   String firstIndividualId = individualIds[0];

   // The returned Map has the input record Id as key and the corresponding token as value

   String tokenForFirstIndividual = tokens.get(firstIndividualId);

   // Do something with the token

   System.debug(tokenForFirstIndividual);

```

IN THIS SECTION:

#### TokenUtility Methods TokenUtility Methods The following are methods for TokenUtility .

IN THIS SECTION:

##### generateToken(tokenValue, tokenType)

Returns the authentication token for the specified token value using the given token type.

generateToken(tokenValue)
Returns the authentication token for the specified token value using the default `standard` token type.

generateTokens(tokenValues, tokenType)
Returns the authentication tokens in the form of a map, where the map key is the input value to be tokenized and the map value is
the corresponding token. The given token type is used to generate the tokens.

generateTokens(tokenValues)
Returns the generated tokens in the form of a map. This method uses the default standard token type to generate the tokens.

##### **`generateToken(tokenValue, tokenType)`**

Returns the authentication token for the specified token value using the given token type.

Signature

```
   public static String generateToken(String tokenValue, pref_center.TokenType tokenType)

```

Parameters

```
   tokenValue
```

Type: String

The value passed to `LoadParameters.getRecordId()` and `SubmitParameters.getRecordId()` . Identifies the
entity that the preference form is acting on.

```
   tokenType
```

Type: pref_center.TokenType

Specifies the type of the value to be encrypted with authentication tokens.


Apex Reference Guide TokenUtility Class

Return Value

Type: String

##### **`generateToken(tokenValue)`**

Returns the authentication token for the specified token value using the default `standard` token type.

Signature

```
   public static String generateToken(String tokenValue)

```

Parameters

```
   tokenValue
```

Type: String

Identifies the entity that the preference form is acting on. The value passed to `LoadParameters.getRecordId()` and
`SubmitParameters.getRecordId()` .

Return Value

Type: String

##### **`generateTokens(tokenValues, tokenType)`**

Returns the authentication tokens in the form of a map, where the map key is the input value to be tokenized and the map value is the
corresponding token. The given token type is used to generate the tokens.

Signature

```
   public static Map<String,String> generateTokens(List<String> tokenValues,

   pref_center.TokenType tokenType)

```

Parameters

```
   tokenValues
```

Type: List<String>

The values passed to `LoadParameters.getRecordId()` and `SubmitParameters.getRecordId()` . Identifies
the entity that the preference form is acting on. Contains multiple values to be encrypted with authentication tokens.

```
   tokenType
```

Type: pref_center.TokenType

Specifies the type of the value to be encrypted with authentication tokens.

Return Value

Type: Map<String,String>

##### **`generateTokens(tokenValues)`**

Returns the generated tokens in the form of a map. This method uses the default standard token type to generate the tokens.


### Apex Reference Guide ValidationResult Class

Signature

```
   public static Map<String,String> generateTokens(List<String> tokenValues)

```

Parameters

```
   tokenValues
```

Type: List<String>

The list of string values passed to `LoadParameters.getRecordId()` and `SubmitParameters.getRecordId().`
Contains multiple values to be encrypted with authentication tokens.

Return Value

Type: Map<String,String>, where the map key is the input value to be tokenized and the map value is the corresponding token.

### ValidationResult Class

This class is reserved for future use with Preference Manager.

Namespace

Pref_center

## Process Namespace The Process namespace provides an interface and classes for passing data between your organization and a flow. The following are the interfaces and classes in the Process namespace.

IN THIS SECTION:

Plugin Interface
Allows you to pass data between your organization and a specified flow.

PluginDescribeResult Class
Describes the input and output parameters for `Process.PluginResult` .

PluginDescribeResult.InputParameter Class
Describes the input parameter for `Process.PluginResult` .

PluginDescribeResult.OutputParameter Class
Describes the output parameter for `Process.PluginResult` .

PluginDescribeResult.ParameterType Enum
Specifies the data types of input and output parameters of the `Process.PluginDescribeResult` class.

PluginRequest Class
Passes input parameters from the class that implements the `Process.Plugin` interface to the flow.


### Apex Reference Guide Plugin Interface

PluginResult Class
Returns output parameters from the class that implements the `Process.Plugin` interface to the flow.

SEE ALSO:

_Apex Developer Guide_ [: Passing Data to a Flow Using the Process.Plugin Interface](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_process_plugin_using.htm)

### Plugin Interface

Allows you to pass data between your organization and a specified flow.

Namespace

Process

Tip: We recommend using the `@InvocableMethod` annotation instead of the `Process.Plugin` interface.

**•** The interface doesn’t support Blob, Collection, and sObject, data types, and it doesn’t support bulk operations. After you
implement the interface on a class, the class can be referenced only from flows.

**•** The annotation supports all data types and bulk operations. After you implement the annotation on a class, the class can be
referenced from flows, processes, and the Custom Invocable Actions REST API endpoint.

**•** Legacy Apex actions aren’t supported in auto-layout in Flow Builder. Legacy Apex actions are only available to be added in
free-form in Flow Builder. Existing actions can be edited in both auto-layout and free-form mode.

IN THIS SECTION:

#### Plugin Methods

Plugin Example Implementation

#### Plugin Methods

### The following are instance methods for Plugin .

IN THIS SECTION:

##### describe()

Returns a `Process.PluginDescribeResult` object that describes this method call.

invoke(request)
Primary method that the system invokes when the class that implements the interface is instantiated.

##### describe()

Returns a `Process.PluginDescribeResult` object that describes this method call.

Signature

```
   public Process.PluginDescribeResult describe()

```


Apex Reference Guide Plugin Interface

Return Value

Type: Process.PluginDescribeResult

##### invoke(request)

Primary method that the system invokes when the class that implements the interface is instantiated.

Signature

```
   public Process.PluginResult invoke(Process.PluginRequest request)

```

Parameters

```
   request
```

Type: Process.PluginRequest

Return Value

Type: Process.PluginResult

#### Plugin Example Implementation

```
   global class flowChat implements Process.Plugin {

   // The main method to be implemented. The Flow calls this at run time.

   global Process.PluginResult invoke(Process.PluginRequest request) {

        // Get the subject of the Chatter post from the flow

        String subject = (String) request.inputParameters.get('subject');

        // Use the Chatter APIs to post it to the current user's feed

        FeedItem fItem = new FeedItem();

        fItem.ParentId = UserInfo.getUserId();

        fItem.Body = 'Flow Update: ' + subject;

        insert fItem;

        // return to Flow

        Map<String,Object> result = new Map<String,Object>();

        return new Process.PluginResult(result);

      }

      // Returns the describe information for the interface

      global Process.PluginDescribeResult describe() {

        Process.PluginDescribeResult result = new Process.PluginDescribeResult();

        result.Name = 'flowchatplugin';

        result.Tag = 'chat';

        result.inputParameters = new

          List<Process.PluginDescribeResult.InputParameter>{

            new Process.PluginDescribeResult.InputParameter('subject',

            Process.PluginDescribeResult.ParameterType.STRING, true)

           };

        result.outputParameters = new

          List<Process.PluginDescribeResult.OutputParameter>{ };

```


### Apex Reference Guide PluginDescribeResult Class

```
        return result;

      }

   }

```

Test Class

The following is a test class for the above class.

```
   @isTest

   private class flowChatTest {

      static testmethod void flowChatTests() {

        flowChat plugin = new flowChat();

        Map<String,Object> inputParams = new Map<String,Object>();

        string feedSubject = 'Flow is alive';

        InputParams.put('subject', feedSubject);

        Process.PluginRequest request = new Process.PluginRequest(inputParams);

        plugin.invoke(request);

      }

   }

### PluginDescribeResult Class

```

Describes the input and output parameters for `Process.PluginResult` .

Namespace

Process

Tip: We recommend using the `@InvocableMethod` annotation instead of the `Process.Plugin` interface.

**•** The interface doesn’t support Blob, Collection, and sObject, data types, and it doesn’t support bulk operations. After you
implement the interface on a class, the class can be referenced only from flows.

**•** The annotation supports all data types and bulk operations. After you implement the annotation on a class, the class can be
referenced from flows, processes, and the Custom Invocable Actions REST API endpoint.

**•** Legacy Apex actions aren’t supported in auto-layout in Flow Builder. Legacy Apex actions are only available to be added in
free-form in Flow Builder. Existing actions can be edited in both auto-layout and free-form mode.

IN THIS SECTION:

PluginDescribeResult Constructors

PluginDescribeResult Properties


Apex Reference Guide PluginDescribeResult Class

#### PluginDescribeResult Constructors The following are constructors for PluginDescribeResult .

IN THIS SECTION:

##### PluginDescribeResult()

Creates a new instance of the `Process.PluginDescribeResult` class.

##### PluginDescribeResult()

Creates a new instance of the `Process.PluginDescribeResult` class.

Signature

```
   public PluginDescribeResult()

#### PluginDescribeResult Properties The following are properties for PluginDescribeResult .

```

IN THIS SECTION:

##### description

This optional field describes the purpose of the plug-in.

inputParameters
The input parameters passed by the `Process.PluginRequest` class from a flow to the class that implements the
`Process.Plugin` interface.

name
Unique name of the plug-in.

outputParameters
The output parameters passed by the `Process.PluginResult` class from the class that implements the `Process.Plugin`
interface to the flow.

##### description

This optional field describes the purpose of the plug-in.

Signature

```
   public String description {get; set;}

```

Property Value

Type: String

Usage

Size limit: 255 characters.


### Apex Reference Guide PluginDescribeResult.InputParameter Class

##### inputParameters

The input parameters passed by the `Process.PluginRequest` class from a flow to the class that implements the
`Process.Plugin` interface.

Signature

```
   public List<Process.PluginDescribeResult.InputParameter> inputParameters {get; set;}

```

Property Value

Type: List<Process.PluginDescribeResult.InputParameter>

##### name

Unique name of the plug-in.

Signature

```
   public String name {get; set;}

```

Property Value

Type: String

Usage

Size limit: 40 characters.

##### outputParameters

The output parameters passed by the `Process.PluginResult` class from the class that implements the `Process.Plugin`
interface to the flow.

Signature

```
   public List<Process.PluginDescribeResult.OutputParameter> outputParameters {get; set;}

```

Property Value

Type: List<Process.PluginDescribeResult.OutputParameter>

### PluginDescribeResult.InputParameter Class

Describes the input parameter for `Process.PluginResult` .

Namespace

Process


Apex Reference Guide PluginDescribeResult.InputParameter Class

Tip: We recommend using the `@InvocableMethod` annotation instead of the `Process.Plugin` interface.

**•** The interface doesn’t support Blob, Collection, and sObject, data types, and it doesn’t support bulk operations. After you
implement the interface on a class, the class can be referenced only from flows.

**•** The annotation supports all data types and bulk operations. After you implement the annotation on a class, the class can be
referenced from flows, processes, and the Custom Invocable Actions REST API endpoint.

**•** Legacy Apex actions aren’t supported in auto-layout in Flow Builder. Legacy Apex actions are only available to be added in
free-form in Flow Builder. Existing actions can be edited in both auto-layout and free-form mode.

IN THIS SECTION:

#### PluginDescribeResult.InputParameter Constructors

PluginDescribeResult.InputParameter Properties

#### PluginDescribeResult.InputParameter Constructors The following are constructors for PluginDescribeResult.InputParameter .

IN THIS SECTION:

##### PluginDescribeResult.InputParameter(name, description, parameterType, required)

Creates a new instance of the `Process.PluginDescribeResult.InputParameter` class using the specified name,
description, parameter type, and required option.

PluginDescribeResult.InputParameter(name, parameterType, required)
Creates a new instance of the `Process.PluginDescribeResult.InputParameter` class using the specified name,
parameter type, and required option.

##### PluginDescribeResult.InputParameter(name, description, parameterType, required)

Creates a new instance of the `Process.PluginDescribeResult.InputParameter` class using the specified name,
description, parameter type, and required option.

Signature

```
   public PluginDescribeResult.InputParameter(String name, String description,

   Process.PluginDescribeResult.ParameterType parameterType, Boolean required)

```

Parameters

```
   name
```

Type: String

Unique name of the plug-in.

```
   description
```

Type: String

Describes the purpose of the plug-in.

```
   parameterType
```

Type: Process.PluginDescribeResult.ParameterType


Apex Reference Guide PluginDescribeResult.InputParameter Class

The data type of the input parameter.

```
   required
```

Type: Boolean

Set to `true` for required and `false` otherwise.

##### PluginDescribeResult.InputParameter(name, parameterType, required)

Creates a new instance of the `Process.PluginDescribeResult.InputParameter` class using the specified name,
parameter type, and required option.

Signature

```
   public PluginDescribeResult.InputParameter(String name,

   Process.PluginDescribeResult.ParameterType parameterType, Boolean required)

```

Parameters

```
   name
```

Type: String

Unique name of the plug-in.

```
   parameterType
```

Type: Process.PluginDescribeResult.ParameterType

The data type of the input parameter.

```
   required
```

Type: Boolean

Set to `true` for required and `false` otherwise.

#### PluginDescribeResult.InputParameter Properties

##### The following are properties for PluginDescribeResult.InputParameter .

IN THIS SECTION:

##### Description

This optional field describes the purpose of the plug-in.

Name
Unique name of the plug-in.

ParameterType
The data type of the input parameter.

Required
Set to `true` for required and `false` otherwise.

##### Description

This optional field describes the purpose of the plug-in.


Apex Reference Guide PluginDescribeResult.InputParameter Class

Signature

```
   public String Description {get; set;}

```

Property Value

Type: String

Usage

Size limit: 255 characters.

##### Name

Unique name of the plug-in.

Signature

```
   public String Name {get; set;}

```

Property Value

Type: String

Usage

Size limit: 40 characters.

##### **`ParameterType`**

The data type of the input parameter.

Signature

```
   public Process.PluginDescribeResult.ParameterType ParameterType {get; set;}

```

Property Value

Type: Process.PluginDescribeResult.ParameterType

##### Required

Set to `true` for required and `false` otherwise.

Signature

```
   public Boolean Required {get; set;}

```

Property Value

Type: Boolean


### Apex Reference Guide PluginDescribeResult.OutputParameter Class PluginDescribeResult.OutputParameter Class

Describes the output parameter for `Process.PluginResult` .

Namespace

Process

Tip: We recommend using the `@InvocableMethod` annotation instead of the `Process.Plugin` interface.

**•** The interface doesn’t support Blob, Collection, and sObject, data types, and it doesn’t support bulk operations. After you
implement the interface on a class, the class can be referenced only from flows.

**•** The annotation supports all data types and bulk operations. After you implement the annotation on a class, the class can be
referenced from flows, processes, and the Custom Invocable Actions REST API endpoint.

**•** Legacy Apex actions aren’t supported in auto-layout in Flow Builder. Legacy Apex actions are only available to be added in
free-form in Flow Builder. Existing actions can be edited in both auto-layout and free-form mode.

IN THIS SECTION:

#### PluginDescribeResult.OutputParameter Constructors

PluginDescribeResult.OutputParameter Properties

#### PluginDescribeResult.OutputParameter Constructors

### The following are constructors for PluginDescribeResult.OutputParameter .

IN THIS SECTION:

##### PluginDescribeResult.OutputParameter(name, description, parameterType)

Creates a new instance of the `Process.PluginDescribeResult.OutputParameter` class using the specified name,
description, and parameter type.

PluginDescribeResult.OutputParameter(name, parameterType)
Creates a new instance of the `Process.PluginDescribeResult.OutputParameter` class using the specified name,
description, and parameter type.

##### PluginDescribeResult.OutputParameter(name, description, parameterType)

Creates a new instance of the `Process.PluginDescribeResult.OutputParameter` class using the specified name,
description, and parameter type.

Signature

```
   public PluginDescribeResult.OutputParameter(String name, String description,

   Process.PluginDescribeResult.ParameterType parameterType)

```

Parameters

```
   name
```

Type: String


Apex Reference Guide PluginDescribeResult.OutputParameter Class

Unique name of the plug-in.

```
   description
```

Type: String

Describes the purpose of the plug-in.

```
   parameterType
```

Type: Process.PluginDescribeResult.ParameterType

The data type of the input parameter.

##### PluginDescribeResult.OutputParameter(name, parameterType)

Creates a new instance of the `Process.PluginDescribeResult.OutputParameter` class using the specified name,
description, and parameter type.

Signature

```
   public PluginDescribeResult.OutputParameter(String name,

   Process.PluginDescribeResult.ParameterType parameterType)

```

Parameters

```
   name
```

Type: String

Unique name of the plug-in.

```
   parameterType
```

Type: Process.PluginDescribeResult.ParameterType

The data type of the input parameter.

#### PluginDescribeResult.OutputParameter Properties

##### The following are properties for PluginDescribeResult.OutputParameter .

IN THIS SECTION:

##### Description

This optional field describes the purpose of the plug-in.

Name
Unique name of the plug-in.

ParameterType
The data type of the output parameter.

##### Description

This optional field describes the purpose of the plug-in.


### Apex Reference Guide PluginDescribeResult.ParameterType Enum

Signature

```
   public String Description {get; set;}

```

Property Value

Type: String

Usage

Size limit: 255 characters.

##### Name

Unique name of the plug-in.

Signature

```
   public String Name {get; set;}

```

Property Value

Type: String

Usage

Size limit: 40 characters.

##### **`ParameterType`**

The data type of the output parameter.

Signature

```
   public Process.PluginDescribeResult.ParameterType ParameterType {get; set;}

```

Property Value

Type: Process.PluginDescribeResult.ParameterType

### PluginDescribeResult.ParameterType Enum

Specifies the data types of input and output parameters of the `Process.PluginDescribeResult` class.

Enum Values

The following are the values of the `Process.PluginDescribeResult.ParameterType` enum.

**Value** **Description**

`BOOLEAN` A value that can only be assigned `true`, `false`, or `null` .


### Apex Reference Guide PluginRequest Class

**Value** **Description**

`DATE` A value that indicates a particular day.

`DATETIME` A value that indicates a particular day and time, such as a timestamp.

`DECIMAL` A number that includes a decimal point. Decimal is an arbitrary precision number.

`DOUBLE` A 64-bit number that includes a decimal point.

`FLOAT` A floating point number.

`ID` Any valid 18-character Lightning Platform record identifier.

`INTEGER` A 32-bit number that doesn’t include a decimal point.

`LONG` A 64-bit number that doesn’t include a decimal point.

`STRING` Any set of characters surrounded by single quotes.

`TIME` A value that indicates a particular time.

### PluginRequest Class

Passes input parameters from the class that implements the `Process.Plugin` interface to the flow.

Namespace

Process

Tip: We recommend using the `@InvocableMethod` annotation instead of the `Process.Plugin` interface.

**•** The interface doesn’t support Blob, Collection, and sObject, data types, and it doesn’t support bulk operations. After you
implement the interface on a class, the class can be referenced only from flows.

**•** The annotation supports all data types and bulk operations. After you implement the annotation on a class, the class can be
referenced from flows, processes, and the Custom Invocable Actions REST API endpoint.

**•** Legacy Apex actions aren’t supported in auto-layout in Flow Builder. Legacy Apex actions are only available to be added in
free-form in Flow Builder. Existing actions can be edited in both auto-layout and free-form mode.

#### PluginRequest Properties

### The following are properties for PluginRequest .

IN THIS SECTION:

##### inputParameters

Input parameters that are passed from the class that implements the `Process.Plugin` interface to the flow.

##### inputParameters

Input parameters that are passed from the class that implements the `Process.Plugin` interface to the flow.


### Apex Reference Guide PluginResult Class

Signature

```
   public MAP<String,ANY> inputParameters {get; set;}

```

Property Value

Type: Map<String, Object>

### PluginResult Class

Returns output parameters from the class that implements the `Process.Plugin` interface to the flow.

Tip: We recommend using the `@InvocableMethod` annotation instead of the `Process.Plugin` interface.

**•** The interface doesn’t support Blob, Collection, and sObject, data types, and it doesn’t support bulk operations. After you
implement the interface on a class, the class can be referenced only from flows.

**•** The annotation supports all data types and bulk operations. After you implement the annotation on a class, the class can be
referenced from flows, processes, and the Custom Invocable Actions REST API endpoint.

**•** Legacy Apex actions aren’t supported in auto-layout in Flow Builder. Legacy Apex actions are only available to be added in
free-form in Flow Builder. Existing actions can be edited in both auto-layout and free-form mode.

Namespace

Process

#### PluginResult Properties

### The following are properties for PluginResult .

IN THIS SECTION:

##### outputParameters

Output parameters returned from the class that implements the interface to the flow.

##### outputParameters

Output parameters returned from the class that implements the interface to the flow.

Signature

```
   public MAP<String, ANY> outputParameters {get; set;}

```

Property Value

Type: Map<String, Object>

## QuickAction Namespace The QuickAction namespace provides classes and methods for quick actions.


### Apex Reference Guide DescribeAvailableQuickActionResult Class

The following are the classes in the `QuickAction` namespace.

IN THIS SECTION:

### DescribeAvailableQuickActionResult Class

Contains describe metadata information for a quick action that is available for a specified parent.

DescribeLayoutComponent Class
Represents the smallest unit in a layout—a field or a separator.

DescribeLayoutItem Class
Represents an individual item in a `QuickAction.DescribeLayoutRow` .

DescribeLayoutRow Class
Represents a row in a `QuickAction.DescribeLayoutSection` .

DescribeLayoutSection Class
Represents a section of a layout and consists of one or more columns and one or more rows (an array of
`QuickAction.DescribeLayoutRow` ).

DescribeQuickActionDefaultValue Class
Returns a default value for a quick action.

DescribeQuickActionParameter Class
Represents the parameters corresponding to a quick action.

DescribeQuickActionResult Class
Contains describe metadata information for a quick action.

QuickActionDefaults Class
Represents an abstract Apex class that provides the context for running the standard Email Action on Case Feed and the container
of the Email Message fields for the action payload. You can override the target fields before the standard Email Action is rendered.

QuickActionDefaultsHandler Interface
The `QuickAction.QuickActionDefaultsHandler` interface lets you specify the default values for the standard Email
and Send Email actions in the case feed. You can use this interface to specify the From address, CC address, BCC address, subject,
and email body for the Email action in the case feed. You can use the interface to pre-populate these fields based on the context
where the action is displayed, such as the case origin (for example, country) and subject.

QuickActionRequest Class
Use the `QuickAction.QuickActionRequest` class for providing action information for quick actions to be performed by
`QuickAction` class methods. Action information includes the action name, context record ID, and record.

QuickActionResult Class
After you initiate a quick action with the `QuickAction` class, use the `QuickActionResult` class for processing action
results.

SendEmailQuickActionDefaults Class
Represents an Apex class that provides: the From address list; the original email’s email message ID, provided that the reply action
was invoked on the email message feed item; and methods to specify related settings on templates. You can override these fields
before the standard Email Action is rendered.

### DescribeAvailableQuickActionResult Class

Contains describe metadata information for a quick action that is available for a specified parent.


Apex Reference Guide DescribeAvailableQuickActionResult Class

Namespace

QuickAction

Usage

The QuickAction `describeAvailableQuickActions` method returns an array of available quick action describe result objects
( `QuickAction.DescribeAvailableQuickActionResult` ).

#### DescribeAvailableQuickActionResult Methods The following are methods for DescribeAvailableQuickActionResult . All are instance methods.

IN THIS SECTION:

##### getActionEnumOrId()

Returns the unique ID for the action. If the action doesn’t have an ID, its API name is used.

##### getLabel()

The quick action label.

getName()
The quick action name.

getType()
The quick action type.

##### getActionEnumOrId()

Returns the unique ID for the action. If the action doesn’t have an ID, its API name is used.

Signature

```
   public String getActionEnumOrId()

```

Return Value

Type: String

##### getLabel()

The quick action label.

Signature

```
   public String getLabel()

```

Return Value

Type: String


### Apex Reference Guide DescribeLayoutComponent Class

##### getName()

The quick action name.

Signature

```
   public String getName()

```

Return Value

Type: String

##### getType()

The quick action type.

Signature

```
   public String getType()

```

Return Value

Type: String

### DescribeLayoutComponent Class

Represents the smallest unit in a layout—a field or a separator.

Namespace

QuickAction

#### DescribeLayoutComponent Methods

### The following are methods for DescribeLayoutComponent . All are instance methods.

IN THIS SECTION:

getDisplayLines()
Returns the vertical lines displayed for a field. Applies to `textarea` and multi-select picklist fields.

getTabOrder()
Returns the tab order for the item in the row.

##### getType()

Returns the name of the `QuickAction.DescribeLayoutComponent` type for this component.

getValue()
Returns the name of the field if the type for `QuickAction.DescribeLayoutComponent` is `textarea` .


### Apex Reference Guide DescribeLayoutItem Class

##### getDisplayLines()

Returns the vertical lines displayed for a field. Applies to `textarea` and multi-select picklist fields.

Signature

```
   public Integer getDisplayLines()

```

Return Value

Type: Integer

##### getTabOrder()

Returns the tab order for the item in the row.

Signature

```
   public Integer getTabOrder()

```

Return Value

Type: Integer

##### getType()

Returns the name of the `QuickAction.DescribeLayoutComponent` type for this component.

Signature

```
   public String getType()

```

Return Value

Type: String

##### getValue()

Returns the name of the field if the type for `QuickAction.DescribeLayoutComponent` is `textarea` .

Signature

```
   public String getValue()

```

Return Value

Type: String

### DescribeLayoutItem Class

Represents an individual item in a `QuickAction.DescribeLayoutRow` .


Apex Reference Guide DescribeLayoutItem Class

Namespace

QuickAction

Usage

For most fields on a layout, there is only one component per layout item. However, in a display-only view, the
`QuickAction.DescribeLayoutItem` might be a composite of the individual fields (for example, an address can consist of
street, city, state, country, and postal code data). On the corresponding edit view, each component of the address field would be split
up into separate `QuickAction.DescribeLayoutItem` s.

#### DescribeLayoutItem Methods The following are methods for DescribeLayoutItem . All are instance methods.

IN THIS SECTION:

##### getLabel()

Returns the label text for this item.

##### getLayoutComponents()

Returns a list of `QuickAction.DescribeLayoutComponents` for this item.

isEditableForNew()
Indicates whether this item can be edited for new ( `true` ) or not ( `false` ).

isEditableForUpdate()
Indicates whether this item can be edited for update( `true` ) or not ( `false` ).

isPlaceholder()
Indicates whether this item is a placeholder ( `true` ) or not ( `false` ). If `true`, then this item is blank.

isRequired()
Indicates whether this item is required ( `true` ) or not ( `false` ).

##### getLabel()

Returns the label text for this item.

Signature

```
   public String getLabel()

```

Return Value

Type: String

##### getLayoutComponents()

Returns a list of `QuickAction.DescribeLayoutComponents` for this item.


Apex Reference Guide DescribeLayoutItem Class

Signature

```
   public List<QuickAction.DescribeLayoutComponent> getLayoutComponents()

```

Return Value

Type: List<QuickAction.DescribeLayoutComponent>

##### isEditableForNew()

Indicates whether this item can be edited for new ( `true` ) or not ( `false` ).

Signature

```
   public Boolean isEditableForNew()

```

Return Value

Type: Boolean

##### isEditableForUpdate()

Indicates whether this item can be edited for update( `true` ) or not ( `false` ).

Signature

```
   public Boolean isEditableForUpdate()

```

Return Value

Type: Boolean

##### isPlaceholder()

Indicates whether this item is a placeholder ( `true` ) or not ( `false` ). If `true`, then this item is blank.

Signature

```
   public Boolean isPlaceholder()

```

Return Value

Type: Boolean

##### isRequired()

Indicates whether this item is required ( `true` ) or not ( `false` ).

Signature

```
   public Boolean isRequired()

```


### Apex Reference Guide DescribeLayoutRow Class

Return Value

Type: Boolean

Usage

This is useful if, for example, you want to render required fields in a contrasting color.

### DescribeLayoutRow Class

Represents a row in a `QuickAction.DescribeLayoutSection` .

Namespace

QuickAction

Usage

A `QuickAction.DescribeLayoutRow` consists of one or more `QuickAction.DescribeLayoutItem` objects. For
each `QuickAction.DescribeLayoutRow`, a `QuickAction.DescribeLayoutItem` refers either to a specific field or
to an “empty” `QuickAction.DescribeLayoutItem` (one that contains no `QuickAction.DescribeLayoutComponent`
objects). An empty `QuickAction.DescribeLayoutItem` can be returned when a given
`QuickAction.DescribeLayoutRow` is sparse (for example, containing more fields on the right column than on the left column).

#### DescribeLayoutRow Methods

### The following are methods for DescribeLayoutRow . All are instance methods.

IN THIS SECTION:

##### getLayoutItems()

Returns either a specific field or an empty `QuickAction.DescribeLayoutItem` (one that contains no
`QuickAction.DescribeLayoutComponent` objects).

getNumItems()
Returns the number of `QuickAction.DescribeLayoutItem` .

##### getLayoutItems()

Returns either a specific field or an empty `QuickAction.DescribeLayoutItem` (one that contains no
`QuickAction.DescribeLayoutComponent` objects).

Signature

```
   public List<QuickAction.DescribeLayoutItem> getLayoutItems()

```

Return Value

Type: List<QuickAction.DescribeLayoutItem>


### Apex Reference Guide DescribeLayoutSection Class

##### getNumItems()

Returns the number of `QuickAction.DescribeLayoutItem` .

Signature

```
   public Integer getNumItems()

```

Return Value

Type: Integer

### DescribeLayoutSection Class

Represents a section of a layout and consists of one or more columns and one or more rows (an array of
`QuickAction.DescribeLayoutRow` ).

Namespace

QuickAction

#### DescribeLayoutSection Properties

### The following are properties for DescribeLayoutSection .

##### collapsed

The current view of the record details section: collapsed ( `true` ) or expanded ( `false` ).

Signature

```
   public Boolean collapsed {get; set;}

```

Property Value

Type: Boolean

##### layoutsectionid

The unique ID of the record details section in the layout.

Signature

```
   public Id layoutsectionid {get; set;}

```

Property Value

Type: Id


Apex Reference Guide DescribeLayoutSection Class

#### DescribeLayoutSection Methods The following are methods for DescribeLayoutSection .

IN THIS SECTION:

##### getColumns()

Returns the number of columns in the `QuickAction.DescribeLayoutSection` .

##### getHeading()

The heading text (label) for the `QuickAction.DescribeLayoutSection` .

getLayoutRows()
Returns an array of one or more `QuickAction.DescribeLayoutRow` objects.

getLayoutSectionId()
Returns the ID of the record details section in the layout.

getParentLayoutId()
#### Returns the ID of the layout upon which this DescribeLayoutSection resides.

getRows()
Returns the number of rows in the `QuickAction.DescribeLayoutSection` .

isCollapsed()
Indicates whether the record details section is collapsed ( `true` ) or expanded ( `false` ). If you build your own app, you can use this
method to see whether the current user collapsed a section, and respect that preference in your own UI.

isUseCollapsibleSection()
Indicates whether the `QuickAction.DescribeLayoutSection` is a collapsible section ( `true` ) or not ( `false` ).

isUseHeading()
Indicates whether to use the `heading` ( `true` ) or not ( `false` ).

##### getColumns()

Returns the number of columns in the `QuickAction.DescribeLayoutSection` .

Signature

```
   public Integer getColumns()

```

Return Value

Type: Integer

##### getHeading()

The heading text (label) for the `QuickAction.DescribeLayoutSection` .

Signature

```
   public String getHeading()

```


Apex Reference Guide DescribeLayoutSection Class

Return Value

Type: String

##### getLayoutRows()

Returns an array of one or more `QuickAction.DescribeLayoutRow` objects.

Signature

```
   public List<QuickAction.DescribeLayoutRow> getLayoutRows()

```

Return Value

Type: List<QuickAction.DescribeLayoutRow>

##### getLayoutSectionId()

Returns the ID of the record details section in the layout.

Signature

```
   public Id getLayoutSectionId()

```

Return Value

Type: Id

##### getParentLayoutId()

Returns the ID of the layout upon which this `DescribeLayoutSection` resides.

Signature

```
   public Id getParentLayoutId()

```

Return Value

Type: Id

##### getRows()

Returns the number of rows in the `QuickAction.DescribeLayoutSection` .

Signature

```
   public Integer getRows()

```

Return Value

Type: Integer


### Apex Reference Guide DescribeQuickActionDefaultValue Class

##### isCollapsed()

Indicates whether the record details section is collapsed ( `true` ) or expanded ( `false` ). If you build your own app, you can use this
method to see whether the current user collapsed a section, and respect that preference in your own UI.

Signature

```
   public Boolean isCollapsed()

```

Return Value

Type: Boolean

##### isUseCollapsibleSection()

Indicates whether the `QuickAction.DescribeLayoutSection` is a collapsible section ( `true` ) or not ( `false` ).

Signature

```
   public Boolean isUseCollapsibleSection()

```

Return Value

Type: Boolean

##### isUseHeading()

Indicates whether to use the `heading` ( `true` ) or not ( `false` ).

Signature

```
   public Boolean isUseHeading()

```

Return Value

Type: Boolean

### DescribeQuickActionDefaultValue Class

Returns a default value for a quick action.

Namespace

QuickAction

Usage

Represents the default values of fields to use in default layouts.


### Apex Reference Guide DescribeQuickActionParameter Class

#### DescribeQuickActionDefaultValue Methods The following are methods for DescribeQuickActionDefaultValue . All are instance methods.

IN THIS SECTION:

##### getDefaultValue()

Returns the default value of the quick action.

##### getField()

Returns the field name of the action.

##### getDefaultValue()

Returns the default value of the quick action.

Signature

```
   public String getDefaultValue()

```

Return Value

Type: String

##### getField()

Returns the field name of the action.

Signature

```
   public String getField()

```

Return Value

Type: String

### DescribeQuickActionParameter Class

Represents the parameters corresponding to a quick action.

Namespace

QuickAction

IN THIS SECTION:

DescribeQuickActionParameter Properties
Learn more about the available properties with the `CalculateTaxRequest` class.

DescribeQuickActionParameter Methods


Apex Reference Guide DescribeQuickActionParameter Class

#### DescribeQuickActionParameter Properties

Learn more about the available properties with the `CalculateTaxRequest` class.

#### The following are properties for DescribeQuickActionParameter .The following are properties for DescribeQuickActionParameter .

IN THIS SECTION:

##### parametername

Describes the name of the parameter that can be associated with a specific quick action type. For example, User Utterance is a
parameter that is associated with agent quick actions.

##### parametertype

Describes the type of quick action. The type can either be Input or Output.

##### parametervalue

Describes the value of the parameter associated with the quick action.

##### **`parametername`**

Describes the name of the parameter that can be associated with a specific quick action type. For example, User Utterance is a parameter
that is associated with agent quick actions.

Signature

```
   public String parametername {get; set;}

```

Property Value

Type: String

##### **`parametertype`**

Describes the type of quick action. The type can either be Input or Output.

Signature

```
   public String parametertype {get; set;}

```

Property Value

Type: String

##### **`parametervalue`**

Describes the value of the parameter associated with the quick action.

Signature

```
   public String parametervalue {get; set;}

```


Apex Reference Guide DescribeQuickActionParameter Class

Property Value

Type: String

#### DescribeQuickActionParameter Methods The following are methods for DescribeQuickActionParameter .

IN THIS SECTION:

##### getParameterName()

Returns the name of the parameter associated with the quick action.

##### getParameterType()

Returns the type of the parameter associated with the quick action. This can either be Input or Output.

##### getParameterValue()

Returns the value of the parameter associated with the quick action.

##### **`getParameterName()`**

Returns the name of the parameter associated with the quick action.

Signature

```
   public String getParameterName()

```

Return Value

Type: String

##### **`getParameterType()`**

Returns the type of the parameter associated with the quick action. This can either be Input or Output.

Signature

```
   public String getParameterType()

```

Return Value

Type: String

##### **`getParameterValue()`**

Returns the value of the parameter associated with the quick action.

Signature

```
   public String getParameterValue()

```


### Apex Reference Guide DescribeQuickActionResult Class

Return Value

Type: String

### DescribeQuickActionResult Class

Contains describe metadata information for a quick action.

Namespace

QuickAction

Usage

The QuickAction `describeQuickActions` method returns an array of quick action describe result objects
( `QuickAction.DescribeQuickActionResult` ).

IN THIS SECTION:

#### DescribeQuickActionResult Properties

DescribeQuickActionResult Methods

#### DescribeQuickActionResult Properties

### The following are properties for DescribeQuickActionResult .

IN THIS SECTION:

canvasapplicationname
The name of the Canvas application invoked by the custom action.

colors
Array of color information. Each color is associated with a theme.

contextsobjecttype
The object used for the action. Was `getsourceSobjectType()` in API version 29.0 and earlier.

defaultvalues
The action’s default values.

flowdevname
If the custom action invokes a flow, the fully qualified name of the flow.

flowrecordidvar
If the custom action invokes a flow, the input variable that the custom action passes the record’s ID to.

height
The height in pixels of the action pane.

iconname
The name of the icon used for the action. If a custom icon is not used, this value isn’t set.


Apex Reference Guide DescribeQuickActionResult Class

icons
Array of icons. Each icon is associated with a theme.

iconurl
The URL of the icon used for the action. This icon URL corresponds to the 32x32 icon used for the current Salesforce theme, introduced
in Spring ’10, or the custom icon, if there is one.

layout
The section of the layout where the action resides.

lightningcomponentbundleid
If the custom action invokes an Aura component, the ID of the Aura component bundle to which the component belongs.

lightningcomponentbundlename
If the custom action invokes an Aura component, the name of the Aura component bundle to which the component belongs.

lightningcomponentqualifiedname
The fully qualified name of the Aura component invoked by the custom action.

lightningwebcomponentbundleid
If the custom action invokes a Lightning web component, the ID of the Lightning web component bundle to which the component
belongs.

lightningwebcomponentbundlename
If the custom action invokes a Lightning web component, the name of the Lightning web component bundle to which the component
belongs.

lightningwebcomponentqualifiedname
The fully qualified name of the Lightning web component invoked by the custom action.

miniiconurl
The icon’s URL. This icon URL corresponds to the 16x16 icon used for the current Salesforce theme, introduced in Spring ’10, or the
custom icon, if there is one.

showquickactionlcheader
Indicates whether the Lightning component quick action header and footer are shown. If `false`, then both the header containing
the quick action title and the footer containing the Save and Cancel buttons aren’t displayed.

showquickactionvfheader
Indicates whether the Visualforce quick action header and footer should be shown. If `false`, then both the header containing the
quick action title and the footer containing the Save and Cancel buttons aren’t displayed.

targetparentfield
The parent object type of the action. Links the target object to the parent object. For example, the value is Account if the target
object is Contact and the parent object is Account.

targetrecordtypeid
The record type of the target record.

targetsobjecttype
The action’s target object type.

visualforcepagename
The name of the Visualforce page associated with the custom action.

visualforcepageurl
The URL of the Visualforce page associated with the action.


Apex Reference Guide DescribeQuickActionResult Class

width
The width in pixels of the action pane, for custom actions that call Visualforce pages, Canvas apps, or Lightning components.

##### canvasapplicationname

The name of the Canvas application invoked by the custom action.

Signature

```
   public String canvasapplicationname {get; set;}

```

Property Value

Type: String

##### colors

Array of color information. Each color is associated with a theme.

Signature

```
   public List<Schema.DescribeColorResult> colors {get; set;}

```

Property Value

Type: List<Schema.DescribeColorResult> on page 3374

##### contextsobjecttype

The object used for the action. Was `getsourceSobjectType()` in API version 29.0 and earlier.

Signature

```
   public String contextsobjecttype {get; set;}

```

Property Value

Type: String

##### defaultvalues

The action’s default values.

Signature

```
   public List<QuickAction.DescribeQuickActionDefaultValue> defaultvalues {get; set;}

```

Property Value

Type: List<QuickAction.DescribeQuickActionDefaultValue>


Apex Reference Guide DescribeQuickActionResult Class

##### flowdevname

If the custom action invokes a flow, the fully qualified name of the flow.

Signature

```
   public String flowdevname {get; set;}

```

Property Value

Type: String

##### flowrecordidvar

If the custom action invokes a flow, the input variable that the custom action passes the record’s ID to.

Signature

```
   public String flowrecordidvar {get; set;}

```

Property Value

Type: String

Valid values are _`null`_ or _`recordId`_ .

##### height

The height in pixels of the action pane.

Signature

```
   public Integer height {get; set;}

```

Property Value

Type: Integer

##### iconname

The name of the icon used for the action. If a custom icon is not used, this value isn’t set.

Signature

```
   public String iconname {get; set;}

```

Property Value

Type: String


Apex Reference Guide DescribeQuickActionResult Class

##### icons

Array of icons. Each icon is associated with a theme.

Signature

```
   public List<Schema.DescribeIconResult> icons {get; set;}

```

Property Value

Type: List<Schema.DescribeIconResult on page 3397>

If no custom icon was associated with the quick action and the quick action creates a specific object, the icons will correspond to the
##### icons used for the created object. For example, if the quick action creates an Account, the icon array will contain the icons used for

Account.

If a custom icon was associated with the quick action, the array will contain that custom icon.

##### iconurl

The URL of the icon used for the action. This icon URL corresponds to the 32x32 icon used for the current Salesforce theme, introduced
in Spring ’10, or the custom icon, if there is one.

Signature

```
   public String iconurl {get; set;}

```

Property Value

Type: String

##### layout

The section of the layout where the action resides.

Signature

```
   public QuickAction.DescribeLayoutSection layout {get; set;}

```

Property Value

Type: QuickAction.DescribeLayoutSection on page 3157

##### lightningcomponentbundleid

If the custom action invokes an Aura component, the ID of the Aura component bundle to which the component belongs.

Signature

```
   public String lightningcomponentbundleid {get; set;}

```


Apex Reference Guide DescribeQuickActionResult Class

Property Value

Type: String

##### lightningcomponentbundlename

If the custom action invokes an Aura component, the name of the Aura component bundle to which the component belongs.

Signature

```
   public String lightningcomponentbundlename {get; set;}

```

Property Value

Type: String

##### lightningcomponentqualifiedname

The fully qualified name of the Aura component invoked by the custom action.

Signature

```
   public String lightningcomponentqualifiedname {get; set;}

```

Property Value

Type: String

##### **`lightningwebcomponentbundleid`**

If the custom action invokes a Lightning web component, the ID of the Lightning web component bundle to which the component
belongs.

Signature

```
   public String lightningwebcomponentbundleid {get; set;}

```

Property Value

Type: String

##### **`lightningwebcomponentbundlename`**

If the custom action invokes a Lightning web component, the name of the Lightning web component bundle to which the component
belongs.

Signature

```
   public String lightningwebcomponentbundlename {get; set;}

```


Apex Reference Guide DescribeQuickActionResult Class

Property Value

Type: String

##### **`lightningwebcomponentqualifiedname`**

The fully qualified name of the Lightning web component invoked by the custom action.

Signature

```
   public String lightningwebcomponentqualifiedname {get; set;}

```

Property Value

Type: String

##### miniiconurl

The icon’s URL. This icon URL corresponds to the 16x16 icon used for the current Salesforce theme, introduced in Spring ’10, or the
custom icon, if there is one.

Signature

```
   public String miniiconurl {get; set;}

```

Property Value

Type: String

##### showquickactionlcheader

Indicates whether the Lightning component quick action header and footer are shown. If `false`, then both the header containing the
quick action title and the footer containing the Save and Cancel buttons aren’t displayed.

Signature

```
   public Boolean showquickactionlcheader {get; set;}

```

Property Value

Type: Boolean

##### showquickactionvfheader

Indicates whether the Visualforce quick action header and footer should be shown. If `false`, then both the header containing the
quick action title and the footer containing the Save and Cancel buttons aren’t displayed.

Signature

```
   public Boolean showquickactionvfheader {get; set;}

```


Apex Reference Guide DescribeQuickActionResult Class

Property Value

Type: Boolean

##### targetparentfield

The parent object type of the action. Links the target object to the parent object. For example, the value is Account if the target object
is Contact and the parent object is Account.

Signature

```
   public String targetparentfield {get; set;}

```

Property Value

Type: String

##### targetrecordtypeid

The record type of the target record.

Signature

```
   public String targetrecordtypeid {get; set;}

```

Property Value

Type: String

##### targetsobjecttype

The action’s target object type.

Signature

```
   public String targetsobjecttype {get; set;}

```

Property Value

Type: String

##### visualforcepagename

The name of the Visualforce page associated with the custom action.

Signature

```
   public String visualforcepagename {get; set;}

```


Apex Reference Guide DescribeQuickActionResult Class

Property Value

Type: String

##### visualforcepageurl

The URL of the Visualforce page associated with the action.

Signature

```
   public String visualforcepageurl {get; set;}

```

Property Value

Type: String

##### width

The width in pixels of the action pane, for custom actions that call Visualforce pages, Canvas apps, or Lightning components.

Signature

```
   public Integer width {get; set;}

```

Property Value

Type: Integer

#### DescribeQuickActionResult Methods The following are methods for DescribeQuickActionResult . All are instance methods.

IN THIS SECTION:

getActionEnumOrId()
Returns the unique ID for the action. If the action doesn’t have an ID, its API name is used.

getCanvasApplicationName()
Returns the name of the Canvas application, if used.

getColors()
Returns an array of color information. Each color is associated with a theme.

getContextSobjectType()
Returns the object used for the action. Replaces `getsourceSobjectType()` in API version 30.0 and later.

getDefaultValues()
Returns the default values for a action.

getFlowDevName()
If the custom action invokes a flow, returns the fully qualified name of the flow invoked by the custom action.

getFlowRecordIdVar()
If the custom action invokes a flow, returns the input variable that the custom action passes the record’s ID to.


Apex Reference Guide DescribeQuickActionResult Class

getHeight()
Returns the height in pixels of the action pane.

getIconName()
Returns the actions’ icon name.

getIconUrl()
Returns the URL of the 32x32 icon used for the action.

getIcons()
Returns a list of `Schema.DescribeIconResult` objects that describe colors used in a tab.

getLabel()
Returns the action label.

getLayout()
Returns the layout sections that comprise an action.

getLightningComponentBundleId()
If the custom action invokes an Aura component, returns the ID of the Aura component bundle to which the component belongs.

getLightningComponentBundleName()
If the custom action invokes an Aura component, returns the name of the Aura component bundle to which the component belongs.

getLightningComponentQualifiedName()
If the custom action invokes an Aura component, returns the fully qualified name of the Aura component invoked by the custom
action.

getLightningWebComponentBundleId()
If the custom action invokes a Lightning web component, returns the ID of the Lightning web component bundle to which the
component belongs.

getLightningWebComponentBundleName()
If the custom action invokes a Lightning web component, returns the name of the Lightning web component bundle to which the
component belongs.

getLightningWebComponentQualifiedName()
If the custom action invokes a Lightning web component, returns the fully qualified name of the Lightning web component invoked
by the custom action.

getMiniIconUrl()
Returns the 16x16 icon URL.

getName()
Returns the action name.

getShowQuickActionLcHeader()
Returns an indication of whether the Lightning component quick action header and footer are shown.

getShowQuickActionVfHeader()
Returns an indication of whether the Visualforce quick action header and footer should be shown.

getSourceSobjectType()
Returns the object type used for the action.

getTargetParentField()
Returns the parent object’s type for the action.


Apex Reference Guide DescribeQuickActionResult Class

getTargetRecordTypeId()
Returns the record type of the targeted record.

getTargetSobjectType()
Returns the action’s target object type.

getType()
Returns a create or custom Visualforce action.

getVisualforcePageName()
If Visualforce is used, returns the name of the associated page for the action.

getVisualforcePageUrl()
Returns the URL of the Visualforce page associated with the action.

getWidth()
If a custom action is created, returns the width in pixels of the action pane.

##### getActionEnumOrId()

Returns the unique ID for the action. If the action doesn’t have an ID, its API name is used.

Signature

```
   public String getActionEnumOrId()

```

Return Value

Type: String

##### getCanvasApplicationName()

Returns the name of the Canvas application, if used.

Syntax

```
   public String getCanvasApplicationName()

```

Return Value

Type: String

##### getColors()

Returns an array of color information. Each color is associated with a theme.

Signature

```
   public List<Schema.DescribeColorResult> getColors()

```

Return Value

Type: List <Schema.DescribeColorResult>


Apex Reference Guide DescribeQuickActionResult Class

##### getContextSobjectType()

Returns the object used for the action. Replaces `getsourceSobjectType()` in API version 30.0 and later.

Signature

```
   public String getContextSobjectType()

```

Return Value

Type: String

##### getDefaultValues()

Returns the default values for a action.

Signature

```
   public List<QuickAction.DescribeQuickActionDefaultValue> getDefaultValues()

```

Return Value

Type: List<QuickAction.DescribeQuickActionDefaultValue>

##### getFlowDevName()

If the custom action invokes a flow, returns the fully qualified name of the flow invoked by the custom action.

Signature

```
   public String getFlowDevName()

```

Return Value

Type: String

##### getFlowRecordIdVar()

If the custom action invokes a flow, returns the input variable that the custom action passes the record’s ID to.

Signature

```
   public String getFlowRecordIdVar()

```

Return Value

Type: String

##### getHeight()

Returns the height in pixels of the action pane.


Apex Reference Guide DescribeQuickActionResult Class

Signature

```
   public Integer getHeight()

```

Return Value

Type: Integer

##### getIconName()

Returns the actions’ icon name.

Signature

```
   public String getIconName()

```

Return Value

Type: String

##### getIconUrl()

Returns the URL of the 32x32 icon used for the action.

Signature

```
   public String getIconUrl()

```

Return Value

Type: String

##### getIcons()

Returns a list of `Schema.DescribeIconResult` objects that describe colors used in a tab.

Signature

```
   public List<Schema.DescribeIconResult> getIcons()

```

Return Value

Type: List<Schema.DescribeIconResult>

##### getLabel()

Returns the action label.

Signature

```
   public String getLabel()

```


Apex Reference Guide DescribeQuickActionResult Class

Return Value

Type: String

##### getLayout()

Returns the layout sections that comprise an action.

Signature

```
   public QuickAction.DescribeLayoutSection getLayout()

```

Return Value

Type: QuickAction.DescribeLayoutSection

##### getLightningComponentBundleId()

If the custom action invokes an Aura component, returns the ID of the Aura component bundle to which the component belongs.

Signature

```
   public String getLightningComponentBundleId()

```

Return Value

Type: String

##### getLightningComponentBundleName()

If the custom action invokes an Aura component, returns the name of the Aura component bundle to which the component belongs.

Signature

```
   public String getLightningComponentBundleName()

```

Return Value

Type: String

##### getLightningComponentQualifiedName()

If the custom action invokes an Aura component, returns the fully qualified name of the Aura component invoked by the custom action.

Signature

```
   public String getLightningComponentQualifiedName()

```

Return Value

Type: String


Apex Reference Guide DescribeQuickActionResult Class

##### **`getLightningWebComponentBundleId()`**

If the custom action invokes a Lightning web component, returns the ID of the Lightning web component bundle to which the component
belongs.

Signature

```
   public String getLightningWebComponentBundleId()

```

Return Value

Type: String

##### **`getLightningWebComponentBundleName()`**

If the custom action invokes a Lightning web component, returns the name of the Lightning web component bundle to which the
component belongs.

Signature

```
   public String getLightningWebComponentBundleName()

```

Return Value

Type: String

##### **`getLightningWebComponentQualifiedName()`**

If the custom action invokes a Lightning web component, returns the fully qualified name of the Lightning web component invoked
by the custom action.

Signature

```
   public String getLightningWebComponentQualifiedName()

```

Return Value

Type: String

##### getMiniIconUrl()

Returns the 16x16 icon URL.

Signature

```
   public String getMiniIconUrl()

```

Return Value

Type: String


Apex Reference Guide DescribeQuickActionResult Class

##### getName()

Returns the action name.

Signature

```
   public String getName()

```

Return Value

Type: String

##### getShowQuickActionLcHeader()

Returns an indication of whether the Lightning component quick action header and footer are shown.

Signature

```
   public Boolean getShowQuickActionLcHeader()

```

Return Value

Type: Boolean

If `false`, then both the header containing the quick action title and the footer containing the Save and Cancel buttons aren’t displayed.

##### getShowQuickActionVfHeader()

Returns an indication of whether the Visualforce quick action header and footer should be shown.

Signature

```
   public Boolean getShowQuickActionVfHeader()

```

Return Value

Type: Boolean

If `false`, then both the header containing the quick action title and the footer containing the Save and Cancel buttons aren’t displayed.

##### getSourceSobjectType()

Returns the object type used for the action.

Signature

```
   public String getSourceSobjectType()

```

Return Value

Type: String


Apex Reference Guide DescribeQuickActionResult Class

##### getTargetParentField()

Returns the parent object’s type for the action.

Signature

```
   public String getTargetParentField()

```

Return Value

Type: String

##### getTargetRecordTypeId()

Returns the record type of the targeted record.

Signature

```
   public String getTargetRecordTypeId()

```

Return Value

Type: String

##### getTargetSobjectType()

Returns the action’s target object type.

Signature

```
   public String getTargetSobjectType()

```

Return Value

Type: String

##### getType()

Returns a create or custom Visualforce action.

Signature

```
   public String getType()

```

Return Value

Type: String

##### getVisualforcePageName()

If Visualforce is used, returns the name of the associated page for the action.


### Apex Reference Guide QuickActionDefaults Class

Signature

```
   public String getVisualforcePageName()

```

Return Value

Type: String

##### getVisualforcePageUrl()

Returns the URL of the Visualforce page associated with the action.

Signature

```
   public String getVisualforcePageUrl()

```

Return Value

Type: String

##### getWidth()

If a custom action is created, returns the width in pixels of the action pane.

Signature

```
   public Integer getWidth()

```

Return Value

Type: Integer

### QuickActionDefaults Class

Represents an abstract Apex class that provides the context for running the standard Email Action on Case Feed and the container of
the Email Message fields for the action payload. You can override the target fields before the standard Email Action is rendered.

Namespace

### QuickAction

Usage

Note: You cannot extend this abstract class. You can use the getter methods when using it in the context of
QuickAction.QuickActionDefaultsHandler. Salesforce provides a class that extends this class (See
QuickAction.SendEmailQuickActionDefaults.)

IN THIS SECTION:

QuickActionDefaults Methods


Apex Reference Guide QuickActionDefaults Class

#### QuickActionDefaults Methods The following are methods for QuickActionDefaults .

IN THIS SECTION:

##### getActionName()

Returns the name of the standard Email Action on Case Feed (Case.Email).

##### getActionType()

Returns the type of the standard Email Action on Case Feed (Email).

##### getContextId()

The ID of the context related to the standard Email Action on Case Feed (Case ID).

getTargetSObject()
The target object of the standard Email Action on Case Feed (EmailMessage).

##### getActionName()

Returns the name of the standard Email Action on Case Feed (Case.Email).

Signature

```
   public String getActionName()

```

Return Value

Type: String

##### getActionType()

Returns the type of the standard Email Action on Case Feed (Email).

Signature

```
   public String getActionType()

```

Return Value

Type: String

##### getContextId()

The ID of the context related to the standard Email Action on Case Feed (Case ID).

Signature

```
   public Id getContextId()

```


### Apex Reference Guide QuickActionDefaultsHandler Interface

Return Value

Type: Id

##### getTargetSObject()

The target object of the standard Email Action on Case Feed (EmailMessage).

Signature

```
   public SObject getTargetSObject()

```

Return Value

Type: SObject

### QuickActionDefaultsHandler Interface

The `QuickAction.QuickActionDefaultsHandler` interface lets you specify the default values for the standard Email and
Send Email actions in the case feed. You can use this interface to specify the From address, CC address, BCC address, subject, and email
body for the Email action in the case feed. You can use the interface to pre-populate these fields based on the context where the action
is displayed, such as the case origin (for example, country) and subject.

Namespace

### QuickAction

Usage

To specify default values for the standard Email action in the case feed, create a class that implements
`QuickAction.QuickActionDefaultsHandler` .

The `QuickAction.QuickActionDefaultsHandler` interface works in Salesforce Classic and Lightning Experience.

When working in Lightning Experience, keep the following things in mind:

**•** The interface overrides email values set up with predefined IDs.

**•** The interface works with the out-of-the-box Email action provided on cases. You can also use the interface with custom Email actions
for the case object.

**•** The interface in Lightning Experience doesn’t support:

**–** Email attachments

**–** Custom email fields

**–** Visualforce email templates, which are a type of email template available in Salesforce Classic

**•** The From field determines the from address picklist. While you can’t customize this picklist in Send Email action types via the
QuickActionDefaultsHandler interface, you can customize the From Address field. To customize this field, remove the From field
from the SendEmail quick action layout and add the From Address field instead. Then provide a valid and verified from address in
the QuickActionDefaultsHandler code. This address must be the current user’s address, an organization-wide email address that the
current user has access to, or an Email-to-Case routing address.

**•** If your Apex interface adds content to the email body, merge fields display as unresolved. During preview and send, the merge fields
resolve.


Apex Reference Guide QuickActionDefaultsHandler Interface

When you implement this interface, provide an empty parameterless constructor.

IN THIS SECTION:

#### QuickActionDefaultsHandler Methods QuickActionDefaultsHandler Example Implementations

These examples are implementations of the `QuickAction.QuickActionDefaultsHandler` interface.

#### QuickActionDefaultsHandler Methods The following are methods for QuickActionDefaultsHandler .

IN THIS SECTION:

##### onInitDefaults(actionDefaults)

Implement this method to provide default values for the standard Email action in the case feed.

##### onInitDefaults(actionDefaults)

Implement this method to provide default values for the standard Email action in the case feed.

Signature

```
   public void onInitDefaults(QuickAction.QuickActionDefaults[] actionDefaults)

```

Parameters

```
   actionDefaults
```

Type: QuickAction.QuickActionDefaults[]

This array contains only one item of type `QuickAction.SendEmailQuickActionDefaults` .

Return Value

Type: void

#### QuickActionDefaultsHandler Example Implementations

These examples are implementations of the `QuickAction.QuickActionDefaultsHandler` interface.

##### In this example, the onInitDefaults method checks whether the element passed in the array is for the standard Email action in

the case feed. Then, it performs a query to retrieve the case that corresponds to the context ID. Next, it sets the value of the BCC address
of the corresponding email message to a default value. The default value is based on the case reason. Finally, it sets the default values
##### of the email template properties. The onInitDefaults method determines the default values based on two criteria: first, whether

a reply action on an email message initiated the call to the method, and second, whether any previous emails attached to the case are
associated with the call.

```
   global class EmailPublisherLoader implements QuickAction.QuickActionDefaultsHandler {

      // Empty constructor

      global EmailPublisherLoader() {

      }

```


Apex Reference Guide QuickActionDefaultsHandler Interface

```
      // The main interface method

      global void onInitDefaults(QuickAction.QuickActionDefaults[] defaults) {

        QuickAction.SendEmailQuickActionDefaults sendEmailDefaults = null;

        // Check if the quick action is the standard case feed Email action

        for (Integer j = 0; j < defaults.size(); j++) {

           if (defaults.get(j) instanceof QuickAction.SendEmailQuickActionDefaults &&

            defaults.get(j).getTargetSObject().getSObjectType() ==

               EmailMessage.sObjectType &&

            defaults.get(j).getActionName().equals('Case.Email') &&

            defaults.get(j).getActionType().equals('Email')) {

               sendEmailDefaults =

                 (QuickAction.SendEmailQuickActionDefaults)defaults.get(j);

               break;

           }

        }

        if (sendEmailDefaults != null) {

           Case c = [SELECT Status, Reason FROM Case

                 WHERE Id=:sendEmailDefaults.getContextId()];

          EmailMessage emailMessage = (EmailMessage)sendEmailDefaults.getTargetSObject();

           // Set BCC address to make sure each email goes for audit

           emailMessage.BccAddress = getBccAddress(c.Reason);

           /*

           Set Template related fields

           when the In Reply To Id field is null we know the interface

           is called on page load. Here we check if

           there are any previous emails attached to the case and load

           the 'New_Case_Created' or 'Automatic_Response' template.

           When the In Reply To Id field is not null we know that

           the interface is called on click of reply/reply all

           of an email and we load the 'Default_reply_template' template

           */

           if (sendEmailDefaults.getInReplyToId() == null) {

             Integer emailCount = [SELECT count() FROM EmailMessage

                          WHERE ParentId=:sendEmailDefaults.getContextId()];

             if (emailCount!= null && emailCount > 0) {

               sendEmailDefaults.setTemplateId(

                  getTemplateIdHelper('Automatic_Response'));

             } else {

               sendEmailDefaults.setTemplateId(

                  getTemplateIdHelper('New_Case_Created'));

             }

             sendEmailDefaults.setInsertTemplateBody(false);

             sendEmailDefaults.setIgnoreTemplateSubject(false);

           } else {

             sendEmailDefaults.setTemplateId(

               getTemplateIdHelper('Default_reply_template'));

             sendEmailDefaults.setInsertTemplateBody(false);

```


Apex Reference Guide QuickActionDefaultsHandler Interface

```
             sendEmailDefaults.setIgnoreTemplateSubject(true);

           }

        }

      }

      private Id getTemplateIdHelper(String templateApiName) {

        Id templateId = null;

        try {

           templateId = [select id, name from EmailTemplate

                   where developername = : templateApiName].id;

        } catch (Exception e) {

           system.debug('Unble to locate EmailTemplate using name: ' +

             templateApiName + ' refer to Setup | Communications Templates '

               + templateApiName);

        }

        return templateId;

      }

   private String getBccAddress(String reason) {

        if (reason != null && reason.equals('Technical'))

           { return 'support_technical@mycompany.com'; }

        else if (reason != null && reason.equals('Billing'))

           { return 'support_billing@mycompany.com'; }

        else { return 'support@mycompany.com'; }

      }

   }

```

In this example, the `onInitDefaults` method checks whether the element passed in the array is for the standard Email action in
the case feed. Then it performs a query to determine if the case Priority is set to _`High`_ . If the Priority is set to _`High`_, the email address
_`managers@acme.com`_ is appended to the BCC field.

```
   global class EmailPublisherForHighPriorityCases implements

   QuickAction.QuickActionDefaultsHandler {

      // Empty constructor

      global EmailPublisherForHighPriorityCases() {

      }

      // The main interface method

      global void onInitDefaults(QuickAction.QuickActionDefaults[] defaults) {

        QuickAction.SendEmailQuickActionDefaults sendEmailDefaults =

   (QuickAction.SendEmailQuickActionDefaults)defaults.get(0);

        EmailMessage emailMessage = (EmailMessage)sendEmailDefaults.getTargetSObject();

        Case c = [SELECT CaseNumber, Priority FROM Case WHERE

   Id=:sendEmailDefaults.getContextId()];

        // If case severity is “High,” append “managers@acme.com” to the existing (and

   possibly blank) BCC field

        if (c.Priority != null && c.Priority.equals('High')) { // Priority is 'High'

           emailMessage.BccAddress = 'managers@acme.com';

        }

      }

   }

```


Apex Reference Guide QuickActionDefaultsHandler Interface

In this example, the `onInitDefaults` method checks whether the element passed in the array is for the standard Email action in
the case feed. Then it performs a query to determine if the case Type is set to _`Problem`_ . If the type is set to _`Problem`_, the _`First`_
_`Response`_ email template is inserted into the body of the email.

```
   global class EmailPublisherForCaseType implements QuickAction.QuickActionDefaultsHandler

   {

      // Empty constructor

      global EmailPublisherForCaseType() {

      }

      // The main interface method

      global void onInitDefaults(QuickAction.QuickActionDefaults[] defaults) {

      QuickAction.SendEmailQuickActionDefaults sendEmailDefaults =

   (QuickAction.SendEmailQuickActionDefaults)defaults.get(0);

      EmailMessage emailMessage = (EmailMessage)sendEmailDefaults.getTargetSObject();

     Case c = [SELECT CaseNumber, Type FROM Case WHERE Id=:sendEmailDefaults.getContextId()];

      // If case type is “Problem,” insert the “First Response” email template

      if (c.CaseNumber != null && c.Type.equals('Problem')) {

        sendEmailDefaults.setTemplateId('Insert Email Template ID Here'); // Set the

   template Id corresponding to First Response

        sendEmailDefaults.setInsertTemplateBody(true);

        sendEmailDefaults.setIgnoreTemplateSubject(false);

      }

   }

```

In this example, the `onInitDefaults` method checks whether the element passed in the array is for the standard Email action in
the case feed. Then it performs a query to determine if the email is a Reply or Reply All email. If the email is a Reply or Reply All email,
the corresponding email templates for these emails are inserted into the body of the email.

```
   global class EmailPublisherForReplyAndReplyAll implements

   QuickAction.QuickActionDefaultsHandler {

      // Empty constructor

      global EmailPublisherForReplyAndReplyAll() {

      }

      // The main interface method

      global void onInitDefaults(QuickAction.QuickActionDefaults[] defaults) {

      QuickAction.SendEmailQuickActionDefaults sendEmailDefaults =

   (QuickAction.SendEmailQuickActionDefaults)defaults.get(0);

      EmailMessage emailMessage = (EmailMessage)sendEmailDefaults.getTargetSObject();

      // If the email is a “Reply” email, insert the “Reply Email Template” to the email

   body

      if (sendEmailDefaults.getActionName().equals('EmailMessage._Reply')) {

        sendEmailDefaults.setTemplateId('Insert Reply Email Template ID Here');

        sendEmailDefaults.setInsertTemplateBody(true);

        sendEmailDefaults.setIgnoreTemplateSubject(false);

```


### Apex Reference Guide QuickActionRequest Class

```
      // If the email is a “Reply All” email, insert the “Reply All Email Template” to the

   email body

      } else if (sendEmailDefaults.getActionName().equals('EmailMessage._ReplyAll')) {

        sendEmailDefaults.setTemplateId('Insert Reply All Email Template ID Here');

        sendEmailDefaults.setInsertTemplateBody(true);

        sendEmailDefaults.setIgnoreTemplateSubject(false);

   }

### QuickActionRequest Class

```

Use the `QuickAction.QuickActionRequest` class for providing action information for quick actions to be performed by
### QuickAction class methods. Action information includes the action name, context record ID, and record.

Namespace

### QuickAction

Usage

For Apex saved using Salesforce API version 28.0, a parent ID is associated with the QuickActionRequest instead of the context ID.

The constructor of this class takes no arguments:

```
   QuickAction.QuickActionRequest qar = new QuickAction.QuickActionRequest();

```

Example

In this sample, a new quick action is created to create a contact and assign a record to it.

```
   QuickAction.QuickActionRequest req = new QuickAction.QuickActionRequest();

   // Some quick action name

   req.quickActionName = Schema.Account.QuickAction.AccountCreateContact;

   // Define a record for the quick action to create

   Contact c = new Contact();

   c.lastname = 'last name';

   req.record = c;

   // Provide the context ID (or parent ID). In this case, it is an Account record.

   req.contextid = '001xx000003DGcO';

   QuickAction.QuickActionResult res = QuickAction.performQuickAction(req);

```

IN THIS SECTION:

QuickActionRequest Constructors


Apex Reference Guide QuickActionRequest Class

#### QuickActionRequest Methods

SEE ALSO:

QuickAction Class

#### QuickActionRequest Constructors The following are constructors for QuickActionRequest .

IN THIS SECTION:

##### QuickActionRequest()

Creates a new instance of the `QuickAction.QuickActionRequest` class.

##### QuickActionRequest()

Creates a new instance of the `QuickAction.QuickActionRequest` class.

Signature

```
   public QuickActionRequest()

#### QuickActionRequest Methods The following are methods for QuickActionRequest . All are instance methods.

```

IN THIS SECTION:

##### getContextId()

Returns this QuickAction’s context record ID.

getQuickActionName()
Returns this QuickAction’s name.

getRecord()
Returns the QuickAction’s associated record.

setContextId(contextId)
##### Sets this QuickAction’s context ID. Returned by getContextId .

setQuickActionName(name)
Sets this QuickAction’s name. Returned by `getQuickActionName` .

setRecord(record)
Sets a record for this QuickAction. Returned by `getRecord` .

##### getContextId()

Returns this QuickAction’s context record ID.


Apex Reference Guide QuickActionRequest Class

Signature

```
   public Id getContextId()

```

Return Value

Type: ID

##### getQuickActionName()

Returns this QuickAction’s name.

Signature

```
   public String getQuickActionName()

```

Return Value

Type: String

##### getRecord()

Returns the QuickAction’s associated record.

Signature

```
   public SObject getRecord()

```

Return Value

Type: sObject

##### setContextId(contextId)

Sets this QuickAction’s context ID. Returned by `getContextId` .

Signature

```
   public Void setContextId(Id contextId)

```

Parameters

```
   contextId
```

Type: ID

Return Value

Type: Void

Usage

For Apex saved using Salesforce API version 28.0, sets this QuickAction’s parent ID and is returned by `getParentId` .


### Apex Reference Guide QuickActionResult Class

##### setQuickActionName(name)

Sets this QuickAction’s name. Returned by `getQuickActionName` .

Signature

```
   public Void setQuickActionName(String name)

```

Parameters

```
   name
```

Type: String

Return Value

Type: Void

##### setRecord(record)

Sets a record for this QuickAction. Returned by `getRecord` .

Signature

```
   public Void setRecord(SObject record)

```

Parameters

```
   record
```

Type: sObject

Return Value

Type: Void

### QuickActionResult Class After you initiate a quick action with the QuickAction class, use the QuickActionResult class for processing action results.

Namespace

### QuickAction

SEE ALSO:

QuickAction Class

#### QuickActionResult Methods

### The following are methods for QuickActionResult . All are instance methods.


Apex Reference Guide QuickActionResult Class

IN THIS SECTION:

##### getErrors()

If an error occurs, an array of one or more database error objects, along with error codes and descriptions, is returned.

##### getIds()

The IDs of the QuickActions being processed.

##### getSuccessMessage()

Returns the success message associated with the quick action.

isCreated()
Returns `true` if the action is created; otherwise, `false` .

isSuccess()
Returns `true` if the action completes successfully; otherwise, `false` .

##### getErrors()

If an error occurs, an array of one or more database error objects, along with error codes and descriptions, is returned.

Signature

```
   public List<Database.Error> getErrors()

```

Return Value

Type: List<Database.Error>

##### getIds()

The IDs of the QuickActions being processed.

Signature

```
   public List<Id> getIds()

```

Return Value

Type: List<Id>

##### getSuccessMessage()

Returns the success message associated with the quick action.

Signature

```
   public String getSuccessMessage()

```

Return Value

Type: String


### Apex Reference Guide SendEmailQuickActionDefaults Class

##### isCreated()

Returns `true` if the action is created; otherwise, `false` .

Signature

```
   public Boolean isCreated()

```

Return Value

Type: Boolean

##### isSuccess()

Returns `true` if the action completes successfully; otherwise, `false` .

Signature

```
   public Boolean isSuccess()

```

Return Value

Type: Boolean

### SendEmailQuickActionDefaults Class

Represents an Apex class that provides: the From address list; the original email’s email message ID, provided that the reply action was
invoked on the email message feed item; and methods to specify related settings on templates. You can override these fields before
the standard Email Action is rendered.

Namespace

QuickAction

Usage

Note: You cannot instantiate this class. One can use the getters/setters when using it in the context of
`QuickAction.QuickActionDefaultsHandler` .

IN THIS SECTION:

#### SendEmailQuickActionDefaults Methods SendEmailQuickActionDefaults Methods

### The following are methods for SendEmailQuickActionDefaults .


Apex Reference Guide SendEmailQuickActionDefaults Class

IN THIS SECTION:

##### getFromAddressList()

Returns a list of email addresses that are available in the From: address drop-down menu for the standard Email Action.

##### getInReplyToId()

Returns the email message ID of the email to which the reply/reply all action has been invoked.

##### setIgnoreTemplateSubject(useOriginalSubject)

Specifies whether the template subject should be ignored (true), thus using the original subject, or whether the template subject
should replace the original subject (false).

setInsertTemplateBody(keepOriginalBodyContent)
Specifies whether the template body should be inserted above the original body content (true) or whether it should replace the
entire content with the template body (false).

setTemplateId(templateId)
Sets the email template ID to load into the email body.

##### getFromAddressList()

Returns a list of email addresses that are available in the From: address drop-down menu for the standard Email Action.

Signature

```
   public List<String> getFromAddressList()

```

Return Value

Type: List<String>

##### getInReplyToId()

Returns the email message ID of the email to which the reply/reply all action has been invoked.

Signature

```
   public Id getInReplyToId()

```

Return Value

Type: Id

##### setIgnoreTemplateSubject(useOriginalSubject)

Specifies whether the template subject should be ignored (true), thus using the original subject, or whether the template subject should
replace the original subject (false).

Signature

```
   public void setIgnoreTemplateSubject(Boolean useOriginalSubject)

```


## Apex Reference Guide Reports Namespace

Parameters

```
   useOriginalSubject
```

Type: Boolean

Return Value

Type: void

##### setInsertTemplateBody(keepOriginalBodyContent)

Specifies whether the template body should be inserted above the original body content (true) or whether it should replace the entire
content with the template body (false).

Signature

```
   public void setInsertTemplateBody(Boolean keepOriginalBodyContent)

```

Parameters

```
   keepOriginalBodyContent
```

Type: Boolean

Return Value

Type: void

##### setTemplateId(templateId)

Sets the email template ID to load into the email body.

Signature

```
   public void setTemplateId(Id templateId)

```

Parameters

```
   templateId
```

Type: Id

The template ID.

Return Value

Type: void

## Reports Namespace The Reports namespace provides classes for accessing the same data as is available in the Salesforce Reports and Dashboards REST

API.

## The following are the classes in the Reports namespace.


Apex Reference Guide Reports Namespace

IN THIS SECTION:

AggregateColumn Class
Contains methods for describing summary fields such as Record Count, Sum, Average, Max, Min, and custom summary formulas.
Includes name, label, data type, and grouping context.

BucketField Class
Contains methods and constructors to work with information about a bucket field, including bucket type, name, and bucketed
values.

BucketFieldValue Class
Contains information about the report values included in a bucket field.

BucketType Enum
The types of values included in a bucket.

ColumnDataType Enum
The `Reports.ColumnDataType` enum describes the type of data in a column. It is returned by the `getDataType` method.

ColumnSortOrder Enum
The `Reports.ColumnSortOrder` enum describes the order that the grouping column uses to sort data.

CrossFilter Class
Contains methods and constructors used to work with information about a cross filter.

CsfGroupType Enum
The group level at which the custom summary format aggregate is displayed in a report.

DateGranularity Enum
The `Reports.DateGranularity` enum describes the date interval that is used for grouping.

DetailColumn Class
Contains methods for describing fields that contain detailed data. Detailed data fields are also listed in the report metadata.

Dimension Class
Contains information for each row or column grouping.

EvaluatedCondition Class
Contains the individual components of an evaluated condition for a report notification, such as the aggregate name and label, the
operator, and the value that the aggregate is compared to.

EvaluatedConditionOperator Enum
The `Reports.EvaluatedConditionOperator` enum describes the type of operator used to compare an aggregate to
a value. It is returned by the `getOperator` method.

FilterOperator Class
Contains information about a filter operator, such as display name and API name.

FilterValue Class
Contains information about a filter value, such as the display name and API name.

FormulaType Enum
The format of the numbers in a custom summary formula.

GroupingColumn Class
Contains methods for describing fields that are used for column grouping.

GroupingInfo Class
Contains methods for describing fields that are used for grouping.


Apex Reference Guide Reports Namespace

GroupingValue Class
Contains grouping values for a row or column, including the key, label, and value.

NotificationAction Interface
Implement this interface to trigger a custom Apex class when the conditions for a report notification are met.

NotificationActionContext Class
Contains information about the report instance and condition threshold for a report notification.

ReportCsf Class
Contains methods and constructors for working with information about a custom summary formula (CSF).

ReportCurrency Class
Contains information about a currency value, including the amount and currency code.

ReportDataCell Class
Contains the data for a cell in the report, including the display label and value.

ReportDescribeResult Class
Contains report, report type, and extended metadata for a tabular, summary, or matrix report.

ReportDetailRow Class
Contains data cells for a detail row of a report.

ReportDivisionInfo Class
Contains information about the divisions that can be used to filter a report.

ReportExtendedMetadata Class
Contains report extended metadata for a tabular, summary, or matrix report.

ReportFact Class
Contains the fact map for the report, which represents the report’s data values.

ReportFactWithDetails Class
Contains the detailed fact map for the report, which represents the report’s data values.

ReportFactWithSummaries Class
Contains the fact map for the report, which represents the report’s data values, and includes summarized fields.

ReportFilter Class
Contains information about a report filter, including column, operator, and value.

ReportFormat Enum
Contains the possible report format types.

ReportFilterType Enum
The types of values included in a report filter type.

ReportInstance Class
Returns an instance of a report that was run asynchronously. Retrieves the results for that instance.

ReportManager Class
Runs a report synchronously or asynchronously and with or without details.

ReportMetadata Class
Contains report metadata for a tabular, summary, or matrix report.

ReportResults Class
Contains the results of running a report.


Apex Reference Guide Reports Namespace

ReportScopeInfo Class
Contains information about possible scope values that you can choose. Scope values depend on the report type. For example, you
can set the scope for opportunity reports to `All opportunities`, `My team’s opportunities`, or `My`
`opportunities` .

ReportScopeValue Class
Contains information about a possible scope value. Scope values depend on the report type. For example, you can set the scope for
opportunity reports to `All opportunities`, `My team’s opportunities`, or `My opportunities` .

ReportType Class
Contains the unique API name and display name for the report type.

ReportTypeColumn Class
Contains detailed report type metadata about a field, including data type, display name, and filter values.

ReportTypeColumnCategory Class
Information about categories of fields in a report type.

ReportTypeMetadata Class
Contains report type metadata, which gives you information about the fields that are available in each section of the report type,
plus filter information for those fields.

SortColumn Class
Contains information about the sort column used in the report.

StandardDateFilter Class
Contains information about standard date filter available in the report—for example, the API name, start date, and end date of the
standard date filter duration as well as the API name of the date field on which the filter is placed.

StandardDateFilterDuration Class
Contains information about each standard date filter—also referred to as a relative date filter. It contains the API name and display
label of the standard date filter duration as well as the start and end dates.

StandardDateFilterDurationGroup Class
Contains information about the standard date filter groupings, such as the grouping display label and all standard date filters that
fall under the grouping. Groupings include `Calendar Year`, `Calendar Quarter`, `Calendar Month`, `Calendar`
`Week`, `Fiscal Year`, `Fiscal Quarter`, `Day`, and custom values based on user-defined date ranges.

StandardFilter Class
Contains information about the standard filter defined in the report, such as the filter field API name and filter value.

StandardFilterInfo Class
Is an abstract base class for an object that provides standard filter information.

StandardFilterInfoPicklist Class
Contains information about the standard filter picklist, such as the display name and type of the filter field, the default picklist value,
and a list of all possible picklist values.

StandardFilterType Enum
The `StandardFilterType` enum describes the type of standard filters in a report. The `getType()` method returns a
`Reports.StandardFilterType` enum value.

SummaryValue Class
Contains summary data for a cell of the report.

ThresholdInformation Class
Contains a list of evaluated conditions for a report notification.


### Apex Reference Guide AggregateColumn Class

TopRows Class
Contains methods and constructors for working with information about a row limit filter.

Reports Exceptions
The `Reports` namespace contains exception classes.

### AggregateColumn Class

Contains methods for describing summary fields such as Record Count, Sum, Average, Max, Min, and custom summary formulas. Includes
name, label, data type, and grouping context.

Namespace

Reports

#### AggregateColumn Methods

### The following are methods for AggregateColumn . All are instance methods.

IN THIS SECTION:

##### getName()

Returns the unique API name of the summary field.

##### getLabel()

Returns the localized display name for the summarized or custom summary formula field.

getDataType()
Returns the data type of the summarized or custom summary formula field.

getAcrossGroupingContext()
Returns the column grouping in the report where the summary field is displayed.

getDownGroupingContext()
Returns the row grouping in the report where the summary field is displayed.

##### getName()

Returns the unique API name of the summary field.

Syntax

```
   public String getName()

```

Return Value

Type: String

##### getLabel()

Returns the localized display name for the summarized or custom summary formula field.


### Apex Reference Guide BucketField Class

Syntax

```
   public String getLabel()

```

Return Value

Type: String

##### getDataType()

Returns the data type of the summarized or custom summary formula field.

Syntax

```
   public Reports.ColumnDataType getDataType()

```

Return Value

Type: Reports.ColumnDataType

##### getAcrossGroupingContext()

Returns the column grouping in the report where the summary field is displayed.

Syntax

```
   public String getAcrossGroupingContext()

```

Return Value

Type: String

##### getDownGroupingContext()

Returns the row grouping in the report where the summary field is displayed.

Syntax

```
   public String getDownGroupingContext()

```

Return Value

Type: String

### BucketField Class

Contains methods and constructors to work with information about a bucket field, including bucket type, name, and bucketed values.

Namespace

Reports


Apex Reference Guide BucketField Class

IN THIS SECTION:

#### BucketField Constructors

BucketField Methods

#### BucketField Constructors The following are constructors for BucketField .

IN THIS SECTION:

##### BucketField(bucketType, devloperName, label, nullTreatedAsZero, otherBucketLabel, sourceColumnName, values)

Creates an instance of the `Reports.BucketField` class using the specified parameters.

BucketField()
Creates an instance of the `Reports.BucketField` class. You can then set values by using the class’s `set` methods.

##### BucketField(bucketType, devloperName, label, nullTreatedAsZero, otherBucketLabel,

sourceColumnName, values)

Creates an instance of the `Reports.BucketField` class using the specified parameters.

Signature

```
   public BucketField(Reports.BucketType bucketType, String devloperName, String label,

   Boolean nullTreatedAsZero, String otherBucketLabel, String sourceColumnName,

   List<Reports.BucketFieldValue> values)

```

Parameters

```
   bucketType
```

Type: Reports.BucketType

The type of bucket.

```
   devloperName
```

Type: String

API name of the bucket.

```
   label
```

Type: String

User-facing name of the bucket.

```
   nullTreatedAsZero
```

Type: Boolean

Specifies whether null values are converted to zero ( `true` ) or not ( `false` ).

```
   otherBucketLabel
```

Type: String

Name of the fields grouped as `Other` (in buckets of `BucketType PICKLIST` ).

```
   sourceColumnName
```

Type: String


Apex Reference Guide BucketField Class

Name of the bucketed field.

```
   values
```

Type: List<Reports.BucketType>

Types of the values included in the bucket.

##### BucketField()

Creates an instance of the `Reports.BucketField` class. You can then set values by using the class’s `set` methods.

Signature

```
   public BucketField()

#### BucketField Methods

##### The following are methods for BucketField .

```

IN THIS SECTION:

getBucketType()
Returns the bucket type.

getDevloperName()
Returns the bucket’s API name.

getLabel()
Returns the user-facing name of the bucket.

getNullTreatedAsZero()
Returns `true` if null values are converted to the number zero, otherwise returns `false` .

getOtherBucketLabel()
Returns the name of fields grouped as `Other` in buckets of type `PICKLIST` .

getSourceColumnName()
Returns the API name of the bucketed field.

getValues()
Returns the report values grouped by the bucket field.

setBucketType(value)
Sets the `BucketType` of the bucket.

setBucketType(bucketType)
Sets the `BucketType` of the bucket.

setDevloperName(devloperName)
Sets the API name of the bucket.

setLabel(label)
Sets the user-facing name of the bucket.

setNullTreatedAsZero(nullTreatedAsZero)
Specifies whether null values in the bucket are converted to zero ( `true` ) or not ( `false` ).


Apex Reference Guide BucketField Class

setOtherBucketLabel(otherBucketLabel)
Sets the name of the fields grouped as `Other` (in buckets of `BucketType PICKLIST` ).

setSourceColumnName(sourceColumnName)
Specifies the name of the bucketed field.

setValues(values)
Specifies which type of values are included in the bucket.

toString()
Returns a string.

##### getBucketType()

Returns the bucket type.

Signature

```
   public Reports.BucketType getBucketType()

```

Return Value

Type: Reports.BucketType

##### getDevloperName()

Returns the bucket’s API name.

Signature

```
   public String getDevloperName()

```

Return Value

Type: String

##### getLabel()

Returns the user-facing name of the bucket.

Signature

```
   public String getLabel()

```

Return Value

Type: String

##### getNullTreatedAsZero()

Returns `true` if null values are converted to the number zero, otherwise returns `false` .


Apex Reference Guide BucketField Class

Signature

```
   public Boolean getNullTreatedAsZero()

```

Return Value

Type: Boolean

##### getOtherBucketLabel()

Returns the name of fields grouped as `Other` in buckets of type `PICKLIST` .

Signature

```
   public String getOtherBucketLabel()

```

Return Value

Type: String

##### getSourceColumnName()

Returns the API name of the bucketed field.

Signature

```
   public String getSourceColumnName()

```

Return Value

Type: String

##### getValues()

Returns the report values grouped by the bucket field.

Signature

```
   public List<Reports.BucketFieldValue> getValues()

```

Return Value

Type: List on page 3891<Reports.BucketFieldValue>

##### setBucketType(value)

Sets the `BucketType` of the bucket.

Signature

```
   public void setBucketType(String value)

```


Apex Reference Guide BucketField Class

Parameters

```
   value
```

Type: String

See the Reports.BucketType enum for valid values.

Return Value

Type: void

##### setBucketType(bucketType)

Sets the `BucketType` of the bucket.

Signature

```
   public void setBucketType(Reports.BucketType bucketType)

```

Parameters

```
   bucketType
```

Type: Reports.BucketType

Return Value

Type: void

##### setDevloperName(devloperName)

Sets the API name of the bucket.

Signature

```
   public void setDevloperName(String devloperName)

```

Parameters

```
   devloperName
```

Type: String

The API name to assign to the bucket.

Return Value

Type: void

##### setLabel(label)

Sets the user-facing name of the bucket.


Apex Reference Guide BucketField Class

Signature

```
   public void setLabel(String label)

```

Parameters

```
   label
```

Type: String

Return Value

Type: void

##### setNullTreatedAsZero(nullTreatedAsZero)

Specifies whether null values in the bucket are converted to zero ( `true` ) or not ( `false` ).

Signature

```
   public void setNullTreatedAsZero(Boolean nullTreatedAsZero)

```

Parameters

```
   nullTreatedAsZero
```

Type: Boolean

Return Value

Type: void

##### setOtherBucketLabel(otherBucketLabel)

Sets the name of the fields grouped as `Other` (in buckets of `BucketType PICKLIST` ).

Signature

```
   public void setOtherBucketLabel(String otherBucketLabel)

```

Parameters

```
   otherBucketLabel
```

Type: String

Return Value

Type: void

##### setSourceColumnName(sourceColumnName)

Specifies the name of the bucketed field.


### Apex Reference Guide BucketFieldValue Class

Signature

```
   public void setSourceColumnName(String sourceColumnName)

```

Parameters

```
   sourceColumnName
```

Type: String

Return Value

Type: void

##### setValues(values)

Specifies which type of values are included in the bucket.

Signature

```
   public void setValues(List<Reports.BucketFieldValue> values)

```

Parameters

```
   values
```

Type: List on page 3891<Reports.BucketFieldValue>

Return Value

Type: void

##### toString()

Returns a string.

Signature

```
   public String toString()

```

Return Value

Type: String

### BucketFieldValue Class

Contains information about the report values included in a bucket field.

Namespace

Reports


Apex Reference Guide BucketFieldValue Class

IN THIS SECTION:

#### BucketFieldValue Constructors BucketFieldValue Methods BucketFieldValue Constructors The following are constructors for BucketFieldValue .

IN THIS SECTION:

##### BucketFieldValue(label, sourceDimensionValues, rangeUpperBound)

Creates an instance of the `Reports.BucketFieldValue` class using the specified parameters.

##### BucketFieldValue()

Creates an instance of the `Reports.BucketFieldValue` class. You can then set values by using the class’s `set` methods.

##### BucketFieldValue(label, sourceDimensionValues, rangeUpperBound)

Creates an instance of the `Reports.BucketFieldValue` class using the specified parameters.

Signature

```
   public BucketFieldValue(String label, List<String> sourceDimensionValues, Double

   rangeUpperBound)

```

Parameters

```
   label
```

Type: String

The user-facing name of the bucket.

```
   sourceDimensionValues
```

Type: List on page 3891<String>

A list of the values from the source field included in this bucket category (in buckets of type `PICKLIST` and buckets of type `TEXT` ).

```
   rangeUpperBound
```

Type: Double

The greatest range limit under which values are included in this bucket category (in buckets of type `NUMBER` ).

##### BucketFieldValue()

Creates an instance of the `Reports.BucketFieldValue` class. You can then set values by using the class’s `set` methods.

Signature

```
   public BucketFieldValue()

#### BucketFieldValue Methods The following are methods for BucketFieldValue .

```


Apex Reference Guide BucketFieldValue Class

IN THIS SECTION:

##### getLabel()

Returns the user-facing name of the bucket category.

##### getRangeUpperBound()

Returns the greatest range limit under which values are included in this bucket category (in buckets of type `NUMBER` ).

##### getSourceDimensionValues()

Returns a list of the values from the source field included in this bucket category (in buckets of type `PICKLIST` and buckets of
type `TEXT` ).

setLabel(label)
Set the user-facing name of the bucket category.

setRangeUpperBound(rangeUpperBound)
Sets the greatest limit of a range under which values are included in this bucket category (in buckets of type `NUMBER` ).

setSourceDimensionValues(sourceDimensionValues)
Specifies the values from the source field included in this bucket category (in buckets of type `PICKLIST` and buckets of type
`TEXT` ).

toString()
Returns a string.

##### getLabel()

Returns the user-facing name of the bucket category.

Signature

```
   public String getLabel()

```

Return Value

Type: String

##### getRangeUpperBound()

Returns the greatest range limit under which values are included in this bucket category (in buckets of type `NUMBER` ).

Signature

```
   public Double getRangeUpperBound()

```

Return Value

Type: Double

##### getSourceDimensionValues()

Returns a list of the values from the source field included in this bucket category (in buckets of type `PICKLIST` and buckets of type
`TEXT` ).


Apex Reference Guide BucketFieldValue Class

Signature

```
   public List<String> getSourceDimensionValues()

```

Return Value

Type: List<String>

##### setLabel(label)

Set the user-facing name of the bucket category.

Signature

```
   public void setLabel(String label)

```

Parameters

```
   label
```

Type: String

Return Value

Type: void

##### setRangeUpperBound(rangeUpperBound)

Sets the greatest limit of a range under which values are included in this bucket category (in buckets of type `NUMBER` ).

Signature

```
   public void setRangeUpperBound(Double rangeUpperBound)

```

Parameters

```
   rangeUpperBound
```

Type: Double

Return Value

Type: void

##### setSourceDimensionValues(sourceDimensionValues)

Specifies the values from the source field included in this bucket category (in buckets of type `PICKLIST` and buckets of type `TEXT` ).

Signature

```
   public void setSourceDimensionValues(List<String> sourceDimensionValues)

```


### Apex Reference Guide BucketType Enum

Parameters

```
   sourceDimensionValues
```

Type: List<String>

Return Value

Type: void

##### toString()

Returns a string.

Signature

```
   public String toString()

```

Return Value

Type: String

### BucketType Enum

The types of values included in a bucket.

Enum Values

The following are the values of the `Reports.BucketType` enum.

**Value** **Description**

`NUMBER` Numeric values

`PICKLIST` Picklist values

`TEXT` String values

### ColumnDataType Enum

The `Reports.ColumnDataType` enum describes the type of data in a column. It is returned by the `getDataType` method.

Namespace

Reports

Enum Values

The following are the values of the `Reports.ColumnDataType` enum.


### Apex Reference Guide ColumnSortOrder Enum

**Value** **Description**

`BOOLEAN_DATA` Boolean ( `true` or `false` ) values

`COMBOBOX_DATA` Comboboxes, which provide a set of enumerated values and enable the user to
specify a value that is not in the list

`CURRENCY_DATA` Currency values

`DATETIME_DATA` DateTime values

`DATE_DATA` Date values

`DOUBLE_DATA` Double values

`EMAIL_DATA` Email addresses

`ID_DATA` An object’s Salesforce ID

`INT_DATA` Integer values

`MULTIPICKLIST_DATA` Multi-select picklists, which provide a set of enumerated values from which multiple
values can be selected

`PERCENT_DATA` Percent values

`PHONE_DATA` Phone numbers. Values can include alphabetic characters. Client applications are
responsible for phone number formatting.

`PICKLIST_DATA` Single-select picklists, which provide a set of enumerated values from which only
one value can be selected

`REFERENCE_DATA` Cross-references to another object, analogous to a foreign key field

`STRING_DATA` String values

`TEXTAREA_DATA` String values that are displayed as multiline text fields

`TIME_DATA` Time values

`URL_DATA` URL values that are displayed as hyperlinks

### ColumnSortOrder Enum

The `Reports.ColumnSortOrder` enum describes the order that the grouping column uses to sort data.

Namespace

Reports

Usage

The `GroupingInfo.getColumnSortOrder()` method returns a `Reports.ColumnSortOrder` enum value. The
`GroupingInfo.setColumnSortOrder()` method takes the enum value as an argument.


### Apex Reference Guide CrossFilter Class

Enum Values

The following are the values of the `Reports.ColumnSortOrder` enum.

**Value** **Description**

`ASCENDING` Sort data in ascending order (A–Z)

`DESCENDING` Sort data in descending order (Z–A)

### CrossFilter Class

Contains methods and constructors used to work with information about a cross filter.

Namespace

Reports

IN THIS SECTION:

#### CrossFilter Constructors

CrossFilter Methods

#### CrossFilter Constructors

### The following are constructors for CrossFilter .

IN THIS SECTION:

##### CrossFilter(criteria, includesObject, primaryEntityField, relatedEntity, relatedEntityJoinField)

Creates an instance of the `Reports.CrossFilter` class using the specified parameters.

CrossFilter()
Creates an instance of the `Reports.CrossFilter` class. You can then set values by using the class’s `set` methods.

##### CrossFilter(criteria, includesObject, primaryEntityField, relatedEntity, relatedEntityJoinField)

Creates an instance of the `Reports.CrossFilter` class using the specified parameters.

Signature

```
   public CrossFilter(List<Reports.ReportFilter> criteria, Boolean includesObject, String

   primaryEntityField, String relatedEntity, String relatedEntityJoinField)

```

Parameters

```
   criteria
```

Type: List<Reports.ReportFilter>

Information about how to filter the `relatedEntity` . Relates the primary entity with a subset of the `relatedEntity` .


Apex Reference Guide CrossFilter Class

```
   includesObject
```

Type: Boolean

Specifies whether objects returned have a relationship with the `relatedEntity` ( `true) or not (false).`

```
   primaryEntityField
```

Type: String

The name of the object on which the cross filter is evaluated.

```
   relatedEntity
```

Type: String

The name of the object that the `primaryEntityField` is evaluated against—the right-hand side of the cross filter.

```
   relatedEntityJoinField
```

Type: String

The name of the field used to join the `primaryEntityField` and `relatedEntity` .

##### CrossFilter()

Creates an instance of the `Reports.CrossFilter` class. You can then set values by using the class’s `set` methods.

Signature

```
   public CrossFilter()

#### CrossFilter Methods

##### The following are methods for CrossFilter .

```

IN THIS SECTION:

getCriteria()
Returns information about how to filter the `relatedEntity` . Describes the subset of the `relatedEntity` which the primary
entity is evaluated against.

getIncludesObject()
Returns `true` if primary object has a relationship with the `relatedEntity`, otherwise returns `false` .

getPrimaryEntityField()
Returns the name of the object on which the cross filter is evaluated.

getRelatedEntity()
Returns name of the object that the `primaryEntityField` is evaluated against—the right-hand side of the cross filter.

getRelatedEntityJoinField()
Returns the name of the field used to join the `primaryEntityField` and `relatedEntity` .

setCriteria(criteria)
Specifis how to filter the `relatedEntity` . Relates the primary entity with a subset of the `relatedEntity` .

setIncludesObject(includesObject)
Specifies whether objects returned have a relationship with the `relatedEntity` ( `true` ) or not ( `false` ).


Apex Reference Guide CrossFilter Class

setPrimaryEntityField(primaryEntityField)
Specifies the name of the object on which the cross filter is evaluated.

setRelatedEntity(relatedEntity)
Specifies the name of the object that the `primaryEntityField` is evaluated against—the right-hand side of the cross filter.

setRelatedEntityJoinField(relatedEntityJoinField)
Specifies the name of the field used to join the `primaryEntityField` and `relatedEntity` .

toString()
Returns a string.

##### getCriteria()

Returns information about how to filter the `relatedEntity` . Describes the subset of the `relatedEntity` which the primary
entity is evaluated against.

Signature

```
   public List<Reports.ReportFilter> getCriteria()

```

Return Value

Type: List<Reports.ReportFilter>

##### getIncludesObject()

Returns `true` if primary object has a relationship with the `relatedEntity`, otherwise returns `false` .

Signature

```
   public Boolean getIncludesObject()

```

Return Value

Type: Boolean

##### getPrimaryEntityField()

Returns the name of the object on which the cross filter is evaluated.

Signature

```
   public String getPrimaryEntityField()

```

Return Value

Type: String

##### getRelatedEntity()

Returns name of the object that the `primaryEntityField` is evaluated against—the right-hand side of the cross filter.


Apex Reference Guide CrossFilter Class

Signature

```
   public String getRelatedEntity()

```

Return Value

Type: String

##### getRelatedEntityJoinField()

Returns the name of the field used to join the `primaryEntityField` and `relatedEntity` .

Signature

```
   public String getRelatedEntityJoinField()

```

Return Value

Type: String

##### setCriteria(criteria)

Specifis how to filter the `relatedEntity` . Relates the primary entity with a subset of the `relatedEntity` .

Signature

```
   public void setCriteria(List<Reports.ReportFilter> criteria)

```

Parameters

```
   criteria
```

Type: List<Reports.ReportFilter>

Return Value

Type: void

##### setIncludesObject(includesObject)

Specifies whether objects returned have a relationship with the `relatedEntity` ( `true` ) or not ( `false` ).

Signature

```
   public void setIncludesObject(Boolean includesObject)

```

Parameters

```
   includesObject
```

Type: Boolean


Apex Reference Guide CrossFilter Class

Return Value

Type: void

##### setPrimaryEntityField(primaryEntityField)

Specifies the name of the object on which the cross filter is evaluated.

Signature

```
   public void setPrimaryEntityField(String primaryEntityField)

```

Parameters

```
   primaryEntityField
```

Type: String

Return Value

Type: void

##### setRelatedEntity(relatedEntity)

Specifies the name of the object that the `primaryEntityField` is evaluated against—the right-hand side of the cross filter.

Signature

```
   public void setRelatedEntity(String relatedEntity)

```

Parameters

```
   relatedEntity
```

Type: String

Return Value

Type: void

##### setRelatedEntityJoinField(relatedEntityJoinField)

Specifies the name of the field used to join the `primaryEntityField` and `relatedEntity` .

Signature

```
   public void setRelatedEntityJoinField(String relatedEntityJoinField)

```

Parameters

```
   relatedEntityJoinField
```

Type: String


### Apex Reference Guide CsfGroupType Enum

Return Value

Type: void

##### toString()

Returns a string.

Signature

```
   public String toString()

```

Return Value

Type: String

### CsfGroupType Enum

The group level at which the custom summary format aggregate is displayed in a report.

Enum Values

The following are the values of the `Reports.CsfGroupType` enum.

**Value** **Description**

`ALL` The aggregate is displayed at the end of every summary row.

`CUSTOM` The aggregate is displayed at specified grouping levels.

`GRAND_TOTAL` The aggregate is displayed only at the grand total level.

### DateGranularity Enum

The `Reports.DateGranularity` enum describes the date interval that is used for grouping.

Namespace

Reports

Usage

The `GroupingInfo.getDateGranularity` method returns a `Reports.DateGranularity` enum value. The
`GroupingInfo.setDateGranularity` method takes the enum value as an argument.

Enum Values

The following are the values of the `Reports.DateGranularity` enum.


### Apex Reference Guide DetailColumn Class

**Value** **Description**

`DAY` The day of the week (Monday–Sunday)

`DAY_IN_MONTH` The day of the month (1–31)

`FISCAL_PERIOD` The fiscal period

`FISCAL_QUARTER` The fiscal quarter

`FISCAL_WEEK` The fiscal week

`FISCAL_YEAR` The fiscal year

`MONTH` The month (January–December)

`MONTH_IN_YEAR` The month number (1–12)

`NONE` No date grouping

`QUARTER` The quarter number (1–4)

`WEEK` The week number (1–52)

`YEAR` The year number (####)

### DetailColumn Class

Contains methods for describing fields that contain detailed data. Detailed data fields are also listed in the report metadata.

Namespace

Reports

#### DetailColumn Instance Methods

### The following are instance methods for DetailColumn . All are instance methods.

IN THIS SECTION:

##### getName()

Returns the unique API name of the detail column field.

getLabel()
Returns the localized display name of a standard field, the ID of a custom field, or the API name of a bucket field that has detailed
data.

getDataType()
Returns the data type of a detail column field.

##### getName()

Returns the unique API name of the detail column field.


### Apex Reference Guide Dimension Class

Syntax

```
   public String getName()

```

Return Value

Type: String

##### getLabel()

Returns the localized display name of a standard field, the ID of a custom field, or the API name of a bucket field that has detailed data.

Syntax

```
   public String getLabel()

```

Return Value

Type: String

##### getDataType()

Returns the data type of a detail column field.

Syntax

```
   public Reports.ColumnDataType getDataType()

```

Return Value

Type: Reports.ColumnDataType

### Dimension Class

Contains information for each row or column grouping.

Namespace

Reports

#### Dimension Methods

### The following are methods for Dimension . All are instance methods.

IN THIS SECTION:

getGroupings()
Returns information for each row or column grouping as a list.


### Apex Reference Guide EvaluatedCondition Class

##### getGroupings()

Returns information for each row or column grouping as a list.

Syntax

```
   public List<Reports.GroupingValue> getGroupings()

```

Return Value

Type: List<Reports.GroupingValue>

### EvaluatedCondition Class

Contains the individual components of an evaluated condition for a report notification, such as the aggregate name and label, the
operator, and the value that the aggregate is compared to.

Namespace

Reports

IN THIS SECTION:

#### EvaluatedCondition Constructors

EvaluatedCondition Methods

#### EvaluatedCondition Constructors

### The following are constructors for EvaluatedCondition .

IN THIS SECTION:

##### EvaluatedCondition(aggregateName, aggregateLabel, compareToValue, aggregateValue, displayCompareTo, displayValue, operator)

Creates a new instance of the `Reports.EvaluatedConditions` class using the specified parameters.

##### EvaluatedCondition(aggregateName, aggregateLabel, compareToValue, aggregateValue,

displayCompareTo, displayValue, operator)

Creates a new instance of the `Reports.EvaluatedConditions` class using the specified parameters.

Signature

```
   public EvaluatedCondition(String aggregateName, String aggregateLabel, Double

   compareToValue, Double aggregateValue, String displayCompareTo, String displayValue,

   Reports.EvaluatedConditionOperator operator)

```

Parameters

```
   aggregateName
```

Type: String


Apex Reference Guide EvaluatedCondition Class

The unique API name of the aggregate.

```
   aggregateLabel
```

Type: String

The localized display name of the aggregate.

```
   compareToValue
```

Type: Double

The value that the aggregate is compared to in the condition.

```
   aggregateValue
```

Type: Double

The actual value of the aggregate when the report is run.

```
   displayCompareTo
```

Type: String

The value that the aggregate is compared to in the condition, formatted for display. For example, a display value for a currency is
$20.00 or USD20.00 instead of 20.00.

```
   displayValue
```

Type: String

The value of the aggregate when the report is run, formatted for display. For example, a display value for a currency is $20.00 or
USD20.00 instead of 20.00.

```
   operator
```

Type: Reports.EvaluatedConditionOperator

The operator used in the condition.

#### EvaluatedCondition Methods The following are methods for EvaluatedCondition .

IN THIS SECTION:

getAggregateLabel()
Returns the localized display name of the aggregate.

getAggregateName()
Returns the unique API name of the aggregate.

getCompareTo()
Returns the value that the aggregate is compared to in the condition.

getDisplayCompareTo()
Returns the value that the aggregate is compared to in the condition, formatted for display. For example, a display value for a currency
is $20.00 or USD20.00 instead of 20.00.

getDisplayValue()
Returns the value of the aggregate when the report is run, formatted for display. For example, a display value for a currency is $20.00
or USD20.00 instead of 20.00.

getOperator()
Returns the operator used in the condition.


Apex Reference Guide EvaluatedCondition Class

getValue()
Returns the actual value of the aggregate when the report is run.

##### getAggregateLabel()

Returns the localized display name of the aggregate.

Signature

```
   public String getAggregateLabel()

```

Return Value

Type: String

##### getAggregateName()

Returns the unique API name of the aggregate.

Signature

```
   public String getAggregateName()

```

Return Value

Type: String

##### getCompareTo()

Returns the value that the aggregate is compared to in the condition.

Signature

```
   public Double getCompareTo()

```

Return Value

Type: Double

##### getDisplayCompareTo()

Returns the value that the aggregate is compared to in the condition, formatted for display. For example, a display value for a currency
is $20.00 or USD20.00 instead of 20.00.

Signature

```
   public String getDisplayCompareTo()

```

Return Value

Type: String


### Apex Reference Guide EvaluatedConditionOperator Enum

##### getDisplayValue()

Returns the value of the aggregate when the report is run, formatted for display. For example, a display value for a currency is $20.00 or
USD20.00 instead of 20.00.

Signature

```
   public String getDisplayValue()

```

Return Value

Type: String

##### getOperator()

Returns the operator used in the condition.

Signature

```
   public Reports.EvaluatedConditionOperator getOperator()

```

Return Value

Type: Reports.EvaluatedConditionOperator

##### getValue()

Returns the actual value of the aggregate when the report is run.

Signature

```
   public Double getValue()

```

Return Value

Type: Double

### EvaluatedConditionOperator Enum

The `Reports.EvaluatedConditionOperator` enum describes the type of operator used to compare an aggregate to a
##### value. It is returned by the getOperator method.

Namespace

Reports

Enum Values

The following are the values of the `Reports.EvaluatedConditionOperator` enum.


### Apex Reference Guide FilterOperator Class

**Value** **Description**

`EQUAL` Equality operator.

`GREATER_THAN` Greater than operator.

`GREATER_THAN_EQUAL` Greater than or equal to operator.

`LESS_THAN` Less than operator.

`LESS_THAN_EQUAL` Less than or equal to operator.

`NOT_EQUAL` Inequality operator.

### FilterOperator Class

Contains information about a filter operator, such as display name and API name.

Namespace

Reports

#### FilterOperator Methods

### The following are methods for FilterOperator . All are instance methods.

IN THIS SECTION:

##### getLabel()

Returns the localized display name of the filter operator. Possible values for this name are restricted based on the data type of the
column being filtered.

getName()
Returns the unique API name of the filter operator. Possible values for this name are restricted based on the data type of the column
being filtered. For example `multipicklist` fields can use the following filter operators: “equals,” “not equal to,” “includes,” and
“excludes.” Bucket fields are considered to be of the `String` type.

##### getLabel()

Returns the localized display name of the filter operator. Possible values for this name are restricted based on the data type of the column
being filtered.

Syntax

```
   public String getLabel()

```

Return Value

Type: String


### Apex Reference Guide FilterValue Class

##### getName()

Returns the unique API name of the filter operator. Possible values for this name are restricted based on the data type of the column
being filtered. For example `multipicklist` fields can use the following filter operators: “equals,” “not equal to,” “includes,” and
“excludes.” Bucket fields are considered to be of the `String` type.

Syntax

```
   public String getName()

```

Return Value

Type: String

### FilterValue Class

Contains information about a filter value, such as the display name and API name.

Namespace

Reports

#### FilterValue Methods

### The following are methods for FilterValue . All are instance methods.

IN THIS SECTION:

##### getLabel()

Returns the localized display name of the filter value. Possible values for this name are restricted based on the data type of the column
being filtered.

##### getName()

Returns the unique API name of the filter value. Possible values for this name are restricted based on the data type of the column
being filtered.

##### getLabel()

Returns the localized display name of the filter value. Possible values for this name are restricted based on the data type of the column
being filtered.

Syntax

```
   public String getLabel()

```

Return Value

Type: String


### Apex Reference Guide FormulaType Enum

##### getName()

Returns the unique API name of the filter value. Possible values for this name are restricted based on the data type of the column being
filtered.

Syntax

```
   public String getName()

```

Return Value

Type: String

### FormulaType Enum

The format of the numbers in a custom summary formula.

Enum Values

The following are the values of the `Reports.FormulaType` enum.

**Value** **Description**

`CURRENCY` Formatted as currency. For example, $100.00.

`NUMBER` Formatted as numbers. For example, 100.

`PERCENT` Formatted as percentages. For example, 100%.

### GroupingColumn Class

Contains methods for describing fields that are used for column grouping.

Namespace

Reports

### The GroupingColumn class provides basic information about column grouping fields. The GroupingInfo class includes

additional methods for describing and updating grouping fields.

#### GroupingColumn Methods

### The following are methods for GroupingColumn . All are instance methods.

IN THIS SECTION:

##### getName()

Returns the unique API name of the field or bucket field that is used for column grouping.

getLabel()
Returns the localized display name of the field that is used for column grouping.


Apex Reference Guide GroupingColumn Class

##### getDataType()

Returns the data type of the field that is used for column grouping.

##### getGroupingLevel()

Returns the level of grouping for the column.

##### getName()

Returns the unique API name of the field or bucket field that is used for column grouping.

Syntax

```
   public String getName()

```

Return Value

Type: String

##### getLabel()

Returns the localized display name of the field that is used for column grouping.

Syntax

```
   public String getLabel()

```

Return Value

Type: String

##### getDataType()

Returns the data type of the field that is used for column grouping.

Syntax

```
   public Reports.ColumnDataType getDataType()

```

Return Value

Type: Reports.ColumnDataType

##### getGroupingLevel()

Returns the level of grouping for the column.

Syntax

```
   public Integer getGroupingLevel()

```


### Apex Reference Guide GroupingInfo Class

Return Value

Type: Integer

Usage

**•** In a summary report, 0, 1, or 2 indicates grouping at the first, second, or third row level.

**•** In a matrix report, 0 or 1 indicates grouping at the first or second row or column level.

### GroupingInfo Class

Contains methods for describing fields that are used for grouping.

Namespace

Reports

#### GroupingInfo Methods

### The following are methods for GroupingInfo . All are instance methods.

IN THIS SECTION:

##### getName()

Returns the unique API name of the field or bucket field that is used for row or column grouping.

##### getSortOrder()

Returns the order that is used to sort data in a row or column grouping ( `ASCENDING` or `DESCENDING` ).

getDateGranularity()
Returns the date interval that is used for row or column grouping.

getSortAggregate()
Returns the summary field that is used to sort data within a grouping in a summary report. The value is null when data within a
grouping is not sorted by a summary field.

##### getName()

Returns the unique API name of the field or bucket field that is used for row or column grouping.

Syntax

```
   public String getName()

```

Return Value

Type: String

##### getSortOrder()

Returns the order that is used to sort data in a row or column grouping ( `ASCENDING` or `DESCENDING` ).


### Apex Reference Guide GroupingValue Class

Syntax

```
   public Reports.ColumnSortOrder getSortOrder()

```

Return Value

Type: Reports.ColumnSortOrder

##### getDateGranularity()

Returns the date interval that is used for row or column grouping.

Syntax

```
   public Reports.DateGranularity getDateGranularity()

```

Return Value

Type: Reports.DateGranularity

##### getSortAggregate()

Returns the summary field that is used to sort data within a grouping in a summary report. The value is null when data within a grouping
is not sorted by a summary field.

Syntax

```
   public String getSortAggregate()

```

Return Value

Type: String

### GroupingValue Class

Contains grouping values for a row or column, including the key, label, and value.

Namespace

Reports

#### GroupingValue Methods

### The following are methods for GroupingValue . All are instance methods.

IN THIS SECTION:

getGroupings()
Returns a list of second- or third-level row or column groupings. If there are none, the value is an empty array.


Apex Reference Guide GroupingValue Class

##### getKey()

Returns the unique identifier for a row or column grouping. The identifier is used by the fact map to specify data values within each
grouping.

##### getLabel()

Returns the localized display name of a row or column grouping. For date and time fields, the label is the localized date or time.

##### getValue()

Returns the value of the field that is used as a row or column grouping.

##### getGroupings()

Returns a list of second- or third-level row or column groupings. If there are none, the value is an empty array.

Syntax

```
   public LIST<Reports.GroupingValue> getGroupings()

```

Return Value

Type: List<Reports.GroupingValue>

##### getKey()

Returns the unique identifier for a row or column grouping. The identifier is used by the fact map to specify data values within each
grouping.

Syntax

```
   public String getKey()

```

Return Value

Type: String

##### getLabel()

Returns the localized display name of a row or column grouping. For date and time fields, the label is the localized date or time.

Syntax

```
   public String getLabel()

```

Return Value

Type: String

##### getValue()

Returns the value of the field that is used as a row or column grouping.


### Apex Reference Guide NotificationAction Interface

Syntax

```
   public Object getValue()

```

Return Value

Type: Object

Usage

The value depends on the field’s data type.

**•** Currency fields:

**–** `amount` : Of type currency. A data cell’s value.

**–** `currency` : Of type picklist. The ISO 4217 currency code, if available; for example, USD for US dollars or CNY for Chinese yuan.
(If the grouping is on the converted currency, this value is the currency code for the report and not for the record.)

**•** Picklist fields: API name. For example, a custom picklist field— `Type of Business` with values 1, 2, and 3 for Consulting,
Services, and Add-On Business respectively—has `1`, `2`, or `3` as the grouping value.

**•** ID fields: API name.

**•** Record type fields: API name.

**•** Date and time fields: Date or time in ISO-8601 format.

**•** Lookup fields: Unique API name. For example, for the `Opportunity Owner` lookup field, the ID of each opportunity owner’s
Chatter profile page can be a grouping value.

### NotificationAction Interface

Implement this interface to trigger a custom Apex class when the conditions for a report notification are met.

Namespace

Reports

Usage

Report notifications for reports that users have subscribed to can trigger a custom Apex class, which must implement the
`Reports.NotificationAction` interface. The `execute` method in this interface receives a
`NotificationActionContext` object as a parameter, which contains information about the report instance and the conditions
that must be met for a notification to be triggered.

IN THIS SECTION:

#### NotificationAction Methods

NotificationAction Example Implementation

#### NotificationAction Methods

### The following are methods for NotificationAction .


### Apex Reference Guide NotificationActionContext Class

IN THIS SECTION:

##### execute(context)
### Executes the custom Apex action specified in the context parameter of the context object, NotificationActionContext .

The object contains information about the report instance and the conditions that must be met for a notification to be triggered.
The method executes whenever the specified conditions are met.

##### execute(context)

### Executes the custom Apex action specified in the context parameter of the context object, NotificationActionContext .

The object contains information about the report instance and the conditions that must be met for a notification to be triggered. The
method executes whenever the specified conditions are met.

Signature

```
   public void execute(Reports.NotificationActionContext context)

```

Parameters

```
   context
```

Type: Reports.NotificationActionContext

Return Value

Type: Void

#### NotificationAction Example Implementation

This is an example implementation of the `Reports.NotificationAction` interface.

```
   public class AlertOwners implements Reports.NotificationAction {

      public void execute(Reports.NotificationActionContext context) {

        Reports.ReportResults results = context.getReportInstance().getReportResults();

        for(Reports.GroupingValue g: results.getGroupingsDown().getGroupings()) {

           FeedItem t = new FeedItem();

           t.ParentId = (Id)g.getValue();

           t.Body = 'This record needs attention. Please view the report.';

           t.Title = 'Needs Attention: '+ results.getReportMetadata().getName();

           t.LinkUrl = '/' + results.getReportMetadata().getId();

           insert t;

        }

      }

   }

### NotificationActionContext Class

```

Contains information about the report instance and condition threshold for a report notification.


Apex Reference Guide NotificationActionContext Class

Namespace

Reports

IN THIS SECTION:

#### NotificationActionContext Constructors NotificationActionContext Methods NotificationActionContext Constructors The following are constructors for NotificationActionContext .

IN THIS SECTION:

##### NotificationActionContext(reportInstance, thresholdInformation)

Creates a new instance of the `Reports.NotificationActionContext` class using the specified parameters.

##### NotificationActionContext(reportInstance, thresholdInformation)

Creates a new instance of the `Reports.NotificationActionContext` class using the specified parameters.

Signature

```
   public NotificationActionContext(Reports.ReportInstance reportInstance,

   Reports.ThresholdInformation thresholdInformation)

```

Parameters

```
   reportInstance
```

Type: Reports.ReportInstance

An instance of a report.

```
   thresholdInformation
```

Type: Reports.ThresholdInformation

The evaluated conditions for the notification.

#### NotificationActionContext Methods The following are methods for NotificationActionContext .

IN THIS SECTION:

getReportInstance()
Returns the report instance associated with the notification.

getThresholdInformation()
Returns the threshold information associated with the notification.


### Apex Reference Guide ReportCsf Class

##### getReportInstance()

Returns the report instance associated with the notification.

Signature

```
   public Reports.ReportInstance getReportInstance()

```

Return Value

Type: Reports.ReportInstance

##### getThresholdInformation()

Returns the threshold information associated with the notification.

Signature

```
   public Reports.ThresholdInformation getThresholdInformation()

```

Return Value

Type: Reports.ThresholdInformation

### ReportCsf Class

Contains methods and constructors for working with information about a custom summary formula (CSF).

Namespace

Reports

IN THIS SECTION:

#### ReportCsf Constructors

ReportCsf Methods

#### ReportCsf Constructors

### The following are constructors for ReportCsf .

IN THIS SECTION:

ReportCsf(label, description, formulaType, decimalPlaces, downGroup, downGroupType, acrossGroup, acrossGroupType, formula)
Creates an instance of the `Reports.ReportCsf` class using the specified parameters.

ReportCsf()
Creates an instance of the `Reports.ReportCsf` class. You can then set values by using the class’s `set` methods.


Apex Reference Guide ReportCsf Class

##### ReportCsf(label, description, formulaType, decimalPlaces, downGroup, downGroupType,

acrossGroup, acrossGroupType, formula)

Creates an instance of the `Reports.ReportCsf` class using the specified parameters.

Signature

```
   public ReportCsf(String label, String description, Reports.FormulaType formulaType,

   Integer decimalPlaces, String downGroup, Reports.CsfGroupType downGroupType, String

   acrossGroup, Reports.CsfGroupType acrossGroupType, String formula)

```

Parameters

```
   label
```

Type: String

The user-facing name of the custom summary formula.

```
   description
```

Type: String

The user-facing description of the custom summary formula.

```
   formulaType
```

Type: Reports.FormulaType

The format of the numbers in the custom summary formula.

```
   decimalPlaces
```

Type: Integer

The number of decimal places to include in numbers.

```
   downGroup
```

Type: String

The name of a row grouping when the `downGroupType` is `CUSTOM` ; `null` otherwise.

```
   downGroupType
```

Type: Reports.CsfGroupType

Where to display the aggregate of the custom summary formula.

```
   acrossGroup
```

Type: String

The name of a column grouping when the `accrossGroupType` is `CUSTOM` ; `null` otherwise.

```
   acrossGroupType
```

Type: Reports.CsfGroupType

Where to display the aggregate of the custom summary formula.

```
   formula
```

Type: String

The operations performed on values in the custom summary formula.

##### ReportCsf()

Creates an instance of the `Reports.ReportCsf` class. You can then set values by using the class’s `set` methods.


Apex Reference Guide ReportCsf Class

Signature

```
   public ReportCsf()

#### ReportCsf Methods The following are methods for ReportCsf .

```

IN THIS SECTION:

getAcrossGroup()
Returns the name of a column grouping when the `acrossGroupType` is `CUSTOM` . Otherwise, returns `null` .

getAcrossGroupType()
Returns where to display the aggregate.

getDecimalPlaces()
Returns the number of decimal places that numbers in the custom summary formula have.

getDescription()
Returns the user-facing description of a custom summary formula.

getDownGroup()
Returns the name of a row grouping when the `downGroupType` is `CUSTOM` . Otherwise, returns `null` .

getDownGroupType()
Returns where to display the aggregate of the custom summary formula.

getFormula()
Returns the operations performed on values in the custom summary formula.

getFormulaType()
Returns the formula type.

getLabel()
Returns the user-facing name of the custom summary formula.

setAcrossGroup(acrossGroup)
Specifies the column for the across grouping.

setAcrossGroupType(value)
Sets where to display the aggregate.

setAcrossGroupType(acrossGroupType)
Sets where to display the aggregate.

setDecimalPlaces(decimalPlaces)
Sets the number of decimal places in numbers.

setDescription(description)
Sets the user-facing description of the custom summary formula.

setDownGroup(downGroup)
Sets the name of a row grouping when the `downGroupType` is `CUSTOM` .

setDownGroupType(value)
Sets where to display the aggregate.


Apex Reference Guide ReportCsf Class

setDownGroupType(downGroupType)
Sets where to display the aggregate.

setFormula(formula)
Sets the operations to perform on values in the custom summary formula.

setFormulaType(value)
Sets the format of the numbers in the custom summary formula.

setFormulaType(formulaType)
Sets the format of numbers used in the custom summary formula.

setLabel(label)
Sets the user-facing name of the custom summary formula.

toString()
Returns a string.

##### getAcrossGroup()

Returns the name of a column grouping when the `acrossGroupType` is `CUSTOM` . Otherwise, returns `null` .

Signature

```
   public String getAcrossGroup()

```

Return Value

Type: String

##### getAcrossGroupType()

Returns where to display the aggregate.

Signature

```
   public Reports.CsfGroupType getAcrossGroupType()

```

Return Value

Type: Reports.CsfGroupType

##### getDecimalPlaces()

Returns the number of decimal places that numbers in the custom summary formula have.

Signature

```
   public Integer getDecimalPlaces()

```

Return Value

Type: Integer


Apex Reference Guide ReportCsf Class

##### getDescription()

Returns the user-facing description of a custom summary formula.

Signature

```
   public String getDescription()

```

Return Value

Type: String

##### getDownGroup()

Returns the name of a row grouping when the `downGroupType` is `CUSTOM` . Otherwise, returns `null` .

Signature

```
   public String getDownGroup()

```

Return Value

Type: String

##### getDownGroupType()

Returns where to display the aggregate of the custom summary formula.

Signature

```
   public Reports.CsfGroupType getDownGroupType()

```

Return Value

Type: Reports.CsfGroupType

##### getFormula()

Returns the operations performed on values in the custom summary formula.

Signature

```
   public String getFormula()

```

Return Value

Type: String

##### getFormulaType()

Returns the formula type.


Apex Reference Guide ReportCsf Class

Signature

```
   public Reports.FormulaType getFormulaType()

```

Return Value

Type: Reports.FormulaType

##### getLabel()

Returns the user-facing name of the custom summary formula.

Signature

```
   public String getLabel()

```

Return Value

Type: String

##### setAcrossGroup(acrossGroup)

Specifies the column for the across grouping.

Signature

```
   public void setAcrossGroup(String acrossGroup)

```

Parameters

```
   acrossGroup
```

Type: String

Return Value

Type: void

##### setAcrossGroupType(value)

Sets where to display the aggregate.

Signature

```
   public void setAcrossGroupType(String value)

```

Parameters

```
   value
```

Type: String

For possible values, see Reports.CsfGroupType.


Apex Reference Guide ReportCsf Class

Return Value

Type: void

##### setAcrossGroupType(acrossGroupType)

Sets where to display the aggregate.

Signature

```
   public void setAcrossGroupType(Reports.CsfGroupType acrossGroupType)

```

Parameters

```
   acrossGroupType
```

Type: Reports.CsfGroupType

Return Value

Type: void

##### setDecimalPlaces(decimalPlaces)

Sets the number of decimal places in numbers.

Signature

```
   public void setDecimalPlaces(Integer decimalPlaces)

```

Parameters

```
   decimalPlaces
```

Type: Integer

Return Value

Type: void

##### setDescription(description)

Sets the user-facing description of the custom summary formula.

Signature

```
   public void setDescription(String description)

```

Parameters

```
   description
```

Type: String


Apex Reference Guide ReportCsf Class

Return Value

Type: void

##### setDownGroup(downGroup)

Sets the name of a row grouping when the `downGroupType` is `CUSTOM` .

Signature

```
   public void setDownGroup(String downGroup)

```

Parameters

```
   downGroup
```

Type: String

Return Value

Type: void

##### setDownGroupType(value)

Sets where to display the aggregate.

Signature

```
   public void setDownGroupType(String value)

```

Parameters

```
   value
```

Type: String

For valid values, see Reports.CsfGroupType.

Return Value

Type: void

##### setDownGroupType(downGroupType)

Sets where to display the aggregate.

Signature

```
   public void setDownGroupType(Reports.CsfGroupType downGroupType)

```

Parameters

```
   downGroupType
```

Type: Reports.CsfGroupType


Apex Reference Guide ReportCsf Class

Return Value

Type: void

##### setFormula(formula)

Sets the operations to perform on values in the custom summary formula.

Signature

```
   public void setFormula(String formula)

```

Parameters

```
   formula
```

Type: String

Return Value

Type: void

##### setFormulaType(value)

Sets the format of the numbers in the custom summary formula.

Signature

```
   public void setFormulaType(String value)

```

Parameters

```
   value
```

Type: String

For valid values, see Reports.FormulaType.

Return Value

Type: void

##### setFormulaType(formulaType)

Sets the format of numbers used in the custom summary formula.

Signature

```
   public void setFormulaType(Reports.FormulaType formulaType)

```

Parameters

```
   formulaType
```

Type: Reports.FormulaType


### Apex Reference Guide ReportCurrency Class

Return Value

Type: void

##### setLabel(label)

Sets the user-facing name of the custom summary formula.

Signature

```
   public void setLabel(String label)

```

Parameters

```
   label
```

Type: String

Return Value

Type: void

##### toString()

Returns a string.

Signature

```
   public String toString()

```

Return Value

Type: String

### ReportCurrency Class

Contains information about a currency value, including the amount and currency code.

Namespace

Reports

#### ReportCurrency Methods

### The following are methods for ReportCurrency . All are instance methods.

IN THIS SECTION:

getAmount()
Returns the amount of the currency value.


### Apex Reference Guide ReportDataCell Class

##### getCurrencyCode()

Returns the report currency code, such as USD, EUR, or GBP, for an organization that has multicurrency enabled. The value is `null`
if the organization does not have multicurrency enabled.

##### getAmount()

Returns the amount of the currency value.

Syntax

```
   public Decimal getAmount()

```

Return Value

Type: Decimal

##### getCurrencyCode()

Returns the report currency code, such as USD, EUR, or GBP, for an organization that has multicurrency enabled. The value is `null` if
the organization does not have multicurrency enabled.

Syntax

```
   public String getCurrencyCode()

```

Return Value

Type: String

### ReportDataCell Class

Contains the data for a cell in the report, including the display label and value.

Namespace

Reports

#### ReportDataCell Methods

### The following are methods for ReportDataCell . All are instance methods.

IN THIS SECTION:

getLabel()
Returns the localized display name of the value of a specified cell in the report.

getValue()
Returns the value of a specified cell of a detail row of a report.


### Apex Reference Guide ReportDescribeResult Class

##### getLabel()

Returns the localized display name of the value of a specified cell in the report.

Syntax

```
   public String getLabel()

```

Return Value

Type: String

##### getValue()

Returns the value of a specified cell of a detail row of a report.

Syntax

```
   public Object getValue()

```

Return Value

Type: Object

### ReportDescribeResult Class

Contains report, report type, and extended metadata for a tabular, summary, or matrix report.

Namespace

Reports

#### ReportDescribeResult Methods

### The following are methods for ReportDescribeResult . All are instance methods.

IN THIS SECTION:

##### getReportExtendedMetadata()

Returns additional information about grouping and summaries.

getReportMetadata()
Returns unique identifiers for groupings and summaries.

getReportTypeMetadata()
Returns the fields in each section of a report type, plus filtering information for those fields.

##### getReportExtendedMetadata()

Returns additional information about grouping and summaries.


### Apex Reference Guide ReportDetailRow Class

Syntax

```
   public Reports.ReportExtendedMetadata getReportExtendedMetadata()

```

Return Value

Type: Reports.ReportExtendedMetadata

##### getReportMetadata()

Returns unique identifiers for groupings and summaries.

Syntax

```
   public Reports.ReportMetadata getReportMetadata()

```

Return Value

Type: Reports.ReportMetadata

##### getReportTypeMetadata()

Returns the fields in each section of a report type, plus filtering information for those fields.

Syntax

```
   public Reports.ReportTypeMetadata getReportTypeMetadata()

```

Return Value

Type: Reports.ReportTypeMetadata

### ReportDetailRow Class

Contains data cells for a detail row of a report.

Namespace

Reports

#### ReportDetailRow Methods

### The following are methods for ReportDetailRow . All are instance methods.

IN THIS SECTION:

getDataCells()
Returns a list of data cells for a detail row.


### Apex Reference Guide ReportDivisionInfo Class

##### getDataCells()

Returns a list of data cells for a detail row.

Syntax

```
   public LIST<Reports.ReportDataCell> getDataCells()

```

Return Value

Type: List<Reports.ReportDataCell>

### ReportDivisionInfo Class

Contains information about the divisions that can be used to filter a report.

Available only if your organization uses divisions to segment data and you have the “Affected by Divisions” permission. If you do not
have the “Affected by Divisions” permission, your reports include records in all divisions.

Namespace

Reports

Usage

Use to filter records in the report based on a division, like West Coast and East Coast.

#### ReportDivisionInfo Methods

### The following are methods for ReportDivisionInfo .

##### getDefaultValue()

Returns the default division for the report.

Signature

```
   public String getDefaultValue()

```

Return Value

Type: String

##### getValues()

Returns a list of all possible divisions for the report.

Signature

```
   public List<Reports.FilterValue> getValues()

```


### Apex Reference Guide ReportExtendedMetadata Class

Return Value

Type: List<Reports.FilterValue>

### ReportExtendedMetadata Class

Contains report extended metadata for a tabular, summary, or matrix report.

Namespace

Reports

Report extended metadata provides additional, detailed metadata about summary and grouping fields, including data type and label
information.

#### ReportExtendedMetadata Methods

### The following are methods for ReportExtendedMetadata . All are instance methods.

IN THIS SECTION:

##### getAggregateColumnInfo()

Returns all report summaries such as `Record Count`, `Sum`, `Average`, `Max`, `Min`, and custom summary formulas. Contains
values for each summary that is listed in the report metadata.

##### getDetailColumnInfo()

Returns a map of two properties for each field that has detailed data identified by its unique API name. The detailed data fields are
also listed in the report metadata.

getGroupingColumnInfo()
Returns a map of each row or column grouping to its metadata. Contains values for each grouping that is identified in the
groupingsDown and groupingsAcross lists.

##### getAggregateColumnInfo()

Returns all report summaries such as `Record Count`, `Sum`, `Average`, `Max`, `Min`, and custom summary formulas. Contains values
for each summary that is listed in the report metadata.

Syntax

```
   public MAP<String,Reports.AggregateColumn> getAggregateColumnInfo()

```

Return Value

Type: Map<String,Reports.AggregateColumn>

##### getDetailColumnInfo()

Returns a map of two properties for each field that has detailed data identified by its unique API name. The detailed data fields are also
listed in the report metadata.


### Apex Reference Guide ReportFact Class

Syntax

```
   public MAP<String,Reports.DetailColumn> getDetailColumnInfo()

```

Return Value

Type: Map<String,Reports.DetailColumn>

##### getGroupingColumnInfo()

Returns a map of each row or column grouping to its metadata. Contains values for each grouping that is identified in the groupingsDown
and groupingsAcross lists.

Syntax

```
   public MAP<String,Reports.GroupingColumn> getGroupingColumnInfo()

```

Return Value

Type: Map<String,Reports.GroupingColumn>

### ReportFact Class

Contains the fact map for the report, which represents the report’s data values.

Namespace

Reports

Usage

### ReportFact is the parent class of ReportFactWithDetails and ReportFactWithSummaries . If includeDetails

is `true` when the report is run, the fact map is a `ReportFactWithDetails` object. If `includeDetails` is `false` when
the report is run, the fact map is a `ReportFactWithSummaries` object.

#### ReportFact Methods

### The following are methods for ReportFact . All are instance methods.

IN THIS SECTION:

getAggregates()
Returns summary-level data for a report, including the record count.

getKey()
Returns the unique identifier for a row or column grouping. This identifier can be used to index specific data values within each
grouping.


### Apex Reference Guide ReportFactWithDetails Class

##### getAggregates()

Returns summary-level data for a report, including the record count.

Syntax

```
   public LIST<Reports.SummaryValue> getAggregates()

```

Return Value

Type: List<Reports.SummaryValue>

##### getKey()

Returns the unique identifier for a row or column grouping. This identifier can be used to index specific data values within each grouping.

Syntax

```
   public String getKey()

```

Return Value

Type: String

### ReportFactWithDetails Class

Contains the detailed fact map for the report, which represents the report’s data values.

Namespace

Reports

Usage

### The ReportFactWithDetails class extends the ReportFact class. A ReportFactWithDetails object is returned if

`includeDetails` is set to `true` when the report is run. To access the detail values, you’ll need to cast the return value of the
### ReportResults.getFactMap method to a ReportFactWithDetails object.

#### ReportFactWithDetails Methods

### The following are methods for ReportFactWithDetails . All are instance methods.

IN THIS SECTION:

##### getAggregates()

Returns summary-level data for a report, including the record count.

##### getKey()

Returns the unique identifier for a row or column grouping. This identifier can be used to index specific data values within each
grouping.


### Apex Reference Guide ReportFactWithSummaries Class

##### getRows()

Returns a list of detailed report data in the order of the detail columns that are provided by the report metadata.

##### getAggregates()

Returns summary-level data for a report, including the record count.

Syntax

```
   public LIST<Reports.SummaryValue> getAggregates()

```

Return Value

Type: List<Reports.SummaryValue>

##### getKey()

Returns the unique identifier for a row or column grouping. This identifier can be used to index specific data values within each grouping.

Syntax

```
   public String getKey()

```

Return Value

Type: String

##### getRows()

Returns a list of detailed report data in the order of the detail columns that are provided by the report metadata.

Syntax

```
   public LIST<Reports.ReportDetailRow> getRows()

```

Return Value

Type: List<Reports.ReportDetailRow>

### ReportFactWithSummaries Class

Contains the fact map for the report, which represents the report’s data values, and includes summarized fields.

Namespace

Reports


Apex Reference Guide ReportFactWithSummaries Class

Usage

#### The ReportFactWithSummaries class extends the ReportFact class. A ReportFactWithSummaries object is

returned if `includeDetails` is set to `false` when the report is run.

#### ReportFactWithSummaries Methods The following are methods for ReportFactWithSummaries . All are instance methods.

IN THIS SECTION:

##### getAggregates()

Returns summary-level data for a report, including the record count.

##### getKey()

Returns the unique identifier for a row or column grouping. This identifier can be used to index specific data values within each
grouping.

##### toString()

Returns a string.

##### getAggregates()

Returns summary-level data for a report, including the record count.

Syntax

```
   public LIST<Reports.SummaryValue> getAggregates()

```

Return Value

Type: List<Reports.SummaryValue>

##### getKey()

Returns the unique identifier for a row or column grouping. This identifier can be used to index specific data values within each grouping.

Syntax

```
   public String getKey()

```

Return Value

Type: String

##### toString()

Returns a string.

Signature

```
   public String toString()

```


### Apex Reference Guide ReportFilter Class

Return Value

Type: String

### ReportFilter Class

Contains information about a report filter, including column, operator, and value.

Namespace

Reports

IN THIS SECTION:

#### ReportFilter Constructors

ReportFilter Methods

#### ReportFilter Constructors

### The following are constructors for ReportFilter .

IN THIS SECTION:

##### ReportFilter()

Creates a new instance of the `Reports.ReportFilter` class. You can then set values by using the “set” methods.

##### ReportFilter(column, operator, value)

Creates a new instance of the `Reports.ReportFilter` class by using the specified parameters.

ReportFilter(column, operator, value, filterType)
Creates a new instance of the `Reports.ReportFilter` class by using the specified parameters.

ReportFilter(column, operator, value, filterType, entityName)
Creates a new instance of the `Reports.ReportFilter` class by using the specified parameters.

##### ReportFilter()

Creates a new instance of the `Reports.ReportFilter` class. You can then set values by using the “set” methods.

Signature

```
   public ReportFilter()

##### ReportFilter(column, operator, value)

```

Creates a new instance of the `Reports.ReportFilter` class by using the specified parameters.

Signature

```
   public ReportFilter(String column, String operator, String value)

```


Apex Reference Guide ReportFilter Class

Parameters

```
   column
```

Type: String

```
   operator
```

Type: String

```
   value
```

Type: String

##### ReportFilter(column, operator, value, filterType)

Creates a new instance of the `Reports.ReportFilter` class by using the specified parameters.

Syntax

```
   public ReportFilterType(String column, String operator, String value,

   Reports.ReportFilterType filterType)

```

Parameters

```
   column
```

Type: String

```
   operator
```

Type: String

```
   value
```

Type: String

```
   filterType
```

Type: ReportFilterType Enum on page 3260

##### **`ReportFilter(column, operator, value, filterType, entityName)`**

Creates a new instance of the `Reports.ReportFilter` class by using the specified parameters.

Syntax

```
   public ReportFilterType(String column, String operator, String value,

   Reports.ReportFilterType filterType, String entityName)

```

Parameters

```
   column
```

Type: String

```
   operator
```

Type: String

```
   value
```

Type: String

```
   filterType
```

Type: ReportFilterType Enum on page 3260


Apex Reference Guide ReportFilter Class

```
   entityName
```

Type: String

#### ReportFilter Methods The following are methods for ReportFilter . All are instance methods.

IN THIS SECTION:

##### getColumn()

Returns the unique API name for the field that’s being filtered.

getEntityName()
Returns the entity name used in the report filter. Use the entity name to handle ambiguous field names across entities, specifically
when using cross filters.

getFilterType()
Returns the type of report filter.

getOperator()
Returns the unique API name for the condition that is used to filter a field, such as “greater than” or “not equal to.” Filter conditions
depend on the data type of the field.

getValue()
Returns the value that the field is being filtered by. For example, the field `Age` can be filtered by a numeric value.

setColumn(column)
Sets the unique API name for the field that’s being filtered.

setEntityName(entityName)
Sets the entity name to use in the report filter. Use the entity name to handle ambiguous field names across entities, specifically
when using cross filters.

setFilterType()
Sets the type of report filter.

setOperator(operator)
Sets the unique API name for the condition that is used to filter a field, such as “greater than” or “not equal to.” Filter conditions
depend on the data type of the field.

setValue(value)
Sets the value by which a field can be filtered. For example, the field `Age` can be filtered by a numeric value.

toString(column)
Returns a string representation of the filter.

##### getColumn()

Returns the unique API name for the field that’s being filtered.

Syntax

```
   public String getColumn()

```


Apex Reference Guide ReportFilter Class

Return Value

Type: String

##### **`getEntityName()`**

Returns the entity name used in the report filter. Use the entity name to handle ambiguous field names across entities, specifically when
using cross filters.

Syntax

```
   public String getEntityName()

```

Return Value

Type: String

##### getFilterType()

Returns the type of report filter.

Syntax

```
   public String getFilterType()

```

Return Value

Type: ReportFilterType Enum on page 3260

##### getOperator()

Returns the unique API name for the condition that is used to filter a field, such as “greater than” or “not equal to.” Filter conditions
depend on the data type of the field.

Syntax

```
   public String getOperator()

```

Return Value

Type: String

##### getValue()

Returns the value that the field is being filtered by. For example, the field `Age` can be filtered by a numeric value.

Syntax

```
   public String getValue()

```


Apex Reference Guide ReportFilter Class

Return Value

Type: String

##### setColumn(column)

Sets the unique API name for the field that’s being filtered.

Syntax

```
   public Void setColumn(String column)

```

Parameters

```
   column
```

Type: String

Return Value

Type: Void

##### **`setEntityName(entityName)`**

Sets the entity name to use in the report filter. Use the entity name to handle ambiguous field names across entities, specifically when
using cross filters.

Syntax

```
   public Void setEntityName(String entityName)

```

Parameters

```
   operator
```

Type: String

Return Value

Type: Void

##### setFilterType()

Sets the type of report filter.

Syntax

```
   public Void setFilterType(String column)

```

Parameters

```
   column
```

Type: String


Apex Reference Guide ReportFilter Class

Return Value

Type: Void

##### setOperator(operator)

Sets the unique API name for the condition that is used to filter a field, such as “greater than” or “not equal to.” Filter conditions depend
on the data type of the field.

Syntax

```
   public Void setOperator(String operator)

```

Parameters

```
   operator
```

Type: String

Return Value

Type: Void

##### setValue(value)

Sets the value by which a field can be filtered. For example, the field `Age` can be filtered by a numeric value.

Syntax

```
   public Void setValue(String value)

```

Parameters

```
   value
```

Type: String

Return Value

Type: Void

##### toString(column)

Returns a string representation of the filter.

Signature

```
   public String toString()

```

Return Value

Type: String


### Apex Reference Guide ReportFormat Enum ReportFormat Enum

Contains the possible report format types.

Namespace

Reports

Enum Values

The following are the values of the `Reports.ReportFormat` enum.

**Value** **Description**

`MATRIX` Matrix report format

`SUMMARY` Summary report format

`TABULAR` Tabular report format

### ReportFilterType Enum

The types of values included in a report filter type.

Enum Values

The following are the values of the `Reports.ReportFilterType` enum.

**Value** **Description**

`fieldToField` Field-to-field filter

`fieldValue` Field-to-value filter

### ReportInstance Class

Returns an instance of a report that was run asynchronously. Retrieves the results for that instance.

Namespace

Reports

#### ReportInstance Methods

### The following are methods for ReportInstance . All are instance methods.


Apex Reference Guide ReportInstance Class

IN THIS SECTION:

##### getCompletionDate()

Returns the date and time when the instance of the report finished running. The completion date is available only if the report
instance ran successfully or couldn’t be run because of an error. Date and time information is in ISO-8601 format.

##### getId()

Returns the unique ID for an instance of a report that was run asynchronously.

##### getOwnerId()

Returns the ID of the user who created the report instance.

getReportId()
Returns the unique ID of the report this instance is based on.

getReportResults()
Retrieves results for an instance of an asynchronous report. When you request your report, you can specify whether to summarize
data or include details.

getRequestDate()
Returns the date and time when an instance of the report was run. Date and time information is in ISO-8601 format.

getStatus()
Returns the status of a report.

##### getCompletionDate()

Returns the date and time when the instance of the report finished running. The completion date is available only if the report instance
ran successfully or couldn’t be run because of an error. Date and time information is in ISO-8601 format.

Syntax

```
   public Datetime getCompletionDate()

```

Return Value

Type: Datetime

##### getId()

Returns the unique ID for an instance of a report that was run asynchronously.

Syntax

```
   public Id getId()

```

Return Value

Type: Id

##### getOwnerId()

Returns the ID of the user who created the report instance.


Apex Reference Guide ReportInstance Class

Syntax

```
   public Id getOwnerId()

```

Return Value

Type: Id

##### getReportId()

Returns the unique ID of the report this instance is based on.

Syntax

```
   public Id getReportId()

```

Return Value

Type: Id

##### getReportResults()

Retrieves results for an instance of an asynchronous report. When you request your report, you can specify whether to summarize data
or include details.

Syntax

```
   public Reports.ReportResults getReportResults()

```

Return Value

Type: Reports.ReportResults

##### getRequestDate()

Returns the date and time when an instance of the report was run. Date and time information is in ISO-8601 format.

Syntax

```
   public Datetime getRequestDate()

```

Return Value

Type: Datetime

##### getStatus()

Returns the status of a report.


### Apex Reference Guide ReportManager Class

Syntax

```
   public String getStatus()

```

Return Value

Type: String

Usage

**•** `New` if the report run was recently triggered through a request.

**•** `Success` if the report ran.

**•** `Running` if the report is being run.

**•** `Error` if the report run failed. The instance of a report run can return an error if, for example, your permission to access the report
was removed after you requested the run.

### ReportManager Class

Runs a report synchronously or asynchronously and with or without details.

Namespace

Reports

Usage

Gets instances of reports and describes the metadata of Reports.

#### ReportManager Methods

### The following are methods for ReportManager . All methods are static.

IN THIS SECTION:

describeReport(reportId)
Retrieves report, report type, and extended metadata for a tabular, summary, or matrix report.

getDatatypeFilterOperatorMap()
Lists the field data types that you can use to filter the report.

getReportInstance(instanceId)
Retrieves results for an instance of a report that has been run asynchronously. The settings you use when you run your asynchronous
report determine whether you can retrieve summary data or detailed data.

getReportInstances(reportId)
Returns a list of instances for a report that was run asynchronously. Each item in the list represents a separate instance of the report,
with metadata for the time at which the report was run.

runAsyncReport(reportId, reportMetadata, includeDetails)
Runs a report asynchronously with the report ID. Includes details if _`includeDetails`_ is set to `true` . Filters the report based
on the report metadata in _`reportMetadata`_ .


Apex Reference Guide ReportManager Class

runAsyncReport(reportId, includeDetails)
Runs a report asynchronously with the report ID. Includes details if _`includeDetails`_ is set to `true` .

runAsyncReport(reportId, reportMetadata)
Runs a report asynchronously with the report ID. Filters the results based on the report metadata in _`reportMetadata`_ .

runAsyncReport(reportId)
Runs a report asynchronously with the report ID.

runReport(reportId, reportMetadata, includeDetails)
Runs a report immediately with the report ID. Includes details if _`includeDetails`_ is set to `true` . Filters the results based on
the report metadata in _`reportMetadata`_ .

runReport(reportId, includeDetails)
Runs a report immediately with the report ID. Includes details if _`includeDetails`_ is set to `true` .

runReport(reportId, reportMetadata)
Runs a report immediately with the report ID. Filters the results based on the report metadata in _`rmData`_ .

runReport(reportId)
Runs a report immediately with the report ID.

##### describeReport(reportId)

Retrieves report, report type, and extended metadata for a tabular, summary, or matrix report.

Syntax

```
   public static Reports.ReportDescribeResult describeReport(Id reportId)

```

Parameters

```
   reportId
```

Type: Id

Return Value

Type: Reports.ReportDescribeResult

##### getDatatypeFilterOperatorMap()

Lists the field data types that you can use to filter the report.

Syntax

```
   public static MAP<String,LIST<Reports.FilterOperator>> getDatatypeFilterOperatorMap()

```

Return Value

Type: Map<String, List<Reports.FilterOperator>>


Apex Reference Guide ReportManager Class

##### getReportInstance(instanceId)

Retrieves results for an instance of a report that has been run asynchronously. The settings you use when you run your asynchronous
report determine whether you can retrieve summary data or detailed data.

Syntax

```
   public static Reports.ReportInstance getReportInstance(Id instanceId)

```

Parameters

```
   instanceId
```

Type: Id

Return Value

Type: Reports.ReportInstance

##### getReportInstances(reportId)

Returns a list of instances for a report that was run asynchronously. Each item in the list represents a separate instance of the report, with
metadata for the time at which the report was run.

Syntax

```
   public static LIST<Reports.ReportInstance> getReportInstances(Id reportId)

```

Parameters

```
   reportId
```

Type: Id

Return Value

Type: List<Reports.ReportInstance>

##### runAsyncReport(reportId, reportMetadata, includeDetails)

Runs a report asynchronously with the report ID. Includes details if _`includeDetails`_ is set to `true` . Filters the report based on
the report metadata in _`reportMetadata`_ .

Syntax

```
   public static Reports.ReportInstance runAsyncReport(Id reportId, Reports.ReportMetadata

   reportMetadata, Boolean includeDetails)

```

Parameters

```
   reportId
```

Type: Id


Apex Reference Guide ReportManager Class

```
   reportMetadata
```

Type: Reports.ReportMetadata

```
   includeDetails
```

Type: Boolean

Return Value

Type: Reports.ReportInstance

##### runAsyncReport(reportId, includeDetails)

Runs a report asynchronously with the report ID. Includes details if _`includeDetails`_ is set to `true` .

Syntax

```
   public static Reports.ReportInstance runAsyncReport(Id reportId, Boolean includeDetails)

```

Parameters

```
   reportId
```

Type: Id

```
   includeDetails
```

Type: Boolean

Return Value

Type: Reports.ReportInstance

##### runAsyncReport(reportId, reportMetadata)

Runs a report asynchronously with the report ID. Filters the results based on the report metadata in _`reportMetadata`_ .

Syntax

```
   public static Reports.ReportInstance runAsyncReport(Id reportId, Reports.ReportMetadata

   reportMetadata)

```

Parameters

```
   reportId
```

Type: Id

```
   reportMetadata
```

Type: Reports.ReportMetadata

Return Value

Type: Reports.ReportInstance


Apex Reference Guide ReportManager Class

##### runAsyncReport(reportId)

Runs a report asynchronously with the report ID.

Syntax

```
   public static Reports.ReportInstance runAsyncReport(Id reportId)

```

Parameters

```
   reportId
```

Type: Id

Return Value

Type: Reports.ReportInstance

##### runReport(reportId, reportMetadata, includeDetails)

Runs a report immediately with the report ID. Includes details if _`includeDetails`_ is set to `true` . Filters the results based on the
report metadata in _`reportMetadata`_ .

Syntax

```
   public static Reports.ReportResults runReport(Id reportId, Reports.ReportMetadata

   reportMetadata, Boolean includeDetails)

```

Parameters

```
   reportId
```

Type: Id

```
   reportMetadata
```

Type: Reports.ReportMetadata

```
   includeDetails
```

Type: Boolean

Return Value

Type: Reports.ReportResults

##### runReport(reportId, includeDetails)

Runs a report immediately with the report ID. Includes details if _`includeDetails`_ is set to `true` .

Syntax

```
   public static Reports.ReportResults runReport(Id reportId, Boolean includeDetails)

```


Apex Reference Guide ReportManager Class

Parameters

```
   reportId
```

Type: Id

```
   includeDetails
```

Type: Boolean

Return Value

Type: Reports.ReportResults

##### runReport(reportId, reportMetadata)

Runs a report immediately with the report ID. Filters the results based on the report metadata in _`rmData`_ .

Syntax

```
   public static Reports.ReportResults runReport(Id reportId, Reports.ReportMetadata

   reportMetadata)

```

Parameters

```
   reportId
```

Type: Id

```
   reportMetadata
```

Type: Reports.ReportMetadata Reports.ReportMetadata

Return Value

Type: Reports.ReportResults

##### runReport(reportId)

Runs a report immediately with the report ID.

Syntax

```
   public static Reports.ReportResults runReport(Id reportId)

```

Parameters

```
   reportId
```

Type: Id

Return Value

Type: Reports.ReportResults


### Apex Reference Guide ReportMetadata Class ReportMetadata Class

Contains report metadata for a tabular, summary, or matrix report.

Namespace

Reports

Usage

Report metadata gives information about the report as a whole, such as the report type, format, summary fields, row or column groupings,
### and filters that are saved to the report. You can use the ReportMetadata class to retrieve report metadata and to set metadata

that can be used to filter a report.

#### ReportMetadata Methods

### The following are methods for ReportMetadata . All are instance methods.

IN THIS SECTION:

getAggregates()
Returns unique identifiers for summary or custom summary formula fields in the report.

getBuckets()
Returns a list of bucket fields in the report.

getCrossFilters()
Returns information about cross filters applied to a report.

getCurrencyCode()
Returns report currency, such as USD, EUR, or GBP, for an organization that has multicurrency enabled. The value is `null` if the
organization does not have multicurrency enabled.

getCustomSummaryFormula()
Returns information about custom summary formulas in a report.

getDescription()
Returns the description of the report.

getDetailColumns()
Returns unique API names (column names) for the fields that contain detailed data. For example, the method might return the
following values: “OPPORTUNITY_NAME, TYPE, LEAD_SOURCE, AMOUNT.”

getDeveloperName()
Returns the report API name. For example, the method might return the following value: “Closed_Sales_This_Quarter.”

getDivision()
Returns the division specified in the report.

getGroupingsAcross()
Returns column groupings in a report.

getGroupingsDown()
Returns row groupings for a report.


Apex Reference Guide ReportMetadata Class

getHasDetailRows()
Indicates whether the report has detail rows.

getHasRecordCount()
Indicates whether the report shows the total number of records.

getHistoricalSnapshotDates()
Returns a list of historical snapshot dates.

getId()
Returns the unique report ID.

getName()
Returns the report name.

getReportBooleanFilter()
Returns logic to parse custom field filters. The value is `null` when filter logic is not specified.

getReportFilters()
Returns a list of each custom filter in the report along with the field name, filter operator, and filter value.

getReportFormat()
Returns the format of the report.

getReportType()
Returns the unique API name and display name for the report type.

getScope()
Returns the API name for the scope defined for the report. Scope values depend on the report type.

getShowGrandTotal()
Indicates whether the report shows the grand total.

getShowSubtotals()
Indicates whether the report shows subtotals, such as column or row totals.

getSortBy()
Returns the list of columns on which the report is sorted. Currently, you can sort on only one column.

getStandardDateFilter()
Returns information about the standard date filter for the report, such as the start date, end date, date range, and date field API
name.

getStandardFilters()
Returns a list of standard filters for the report.

getTopRows()
Returns information about a row limit filter, including the number of rows returned and the sort order.

setAggregates(aggregates)
Sets unique identifiers for standard or custom summary formula fields in the report.

setBuckets(buckets)
Creates bucket fields in a report.

setCrossFilters(crossFilters)
Applies cross filters to a report.

setCurrencyCode(currencyCode)
Sets the currency, such as USD, EUR, or GBP, for report summary fields in an organization that has multicurrency enabled.


Apex Reference Guide ReportMetadata Class

setCustomSummaryFormula(customSummaryFormula)
Adds a custom summary formula to a report.

setDescription(description)
Sets the description of the report.

setDetailColumns(detailColumns)
Sets the unique API names for the fields that contain detailed data—for example, `OPPORTUNITY_NAME`, `TYPE`, `LEAD_SOURCE`,
or `AMOUNT` .

setDeveloperName(developerName)
Sets the report API name—for example, `Closed_Sales_This_Quarter` .

setDivision(division)
Sets the division of the report.

setGroupingsAcross(groupingInfo)
Sets column groupings in a report.

setGroupingsDown(groupingInfo)
Sets row groupings for a report.

setHasDetailRows(hasDetailRows)
Specifies whether the report has detail rows.

setHasRecordCount(hasRecordCount)
Specifies whether the report is configured to show the total number of records.

setHistoricalSnapshotDates(historicalSnapshot)
Sets a list of historical snapshot dates.

setId(id)
Sets the unique report ID.

setName(name)
Sets the report name.

setReportBooleanFilter(reportBooleanFilter)
Sets logic to parse custom field filters.

setReportFilters(reportFilters)
Sets a list of each custom filter in the report along with the field name, filter operator, and filter value.

setReportFormat(format)
Sets the format of the report.

setReportType(reportType)
Sets the unique API name and display name for the report type.

setScope(scopeName)
Sets the API name for the scope defined for the report. Scope values depend on the report type.

setShowGrandTotal(showGrandTotal)
Specifies whether the report shows the grand total.

setShowSubtotals(showSubtotals)
Specifies whether the report shows subtotals, such as column or row totals.

setSortBy(column)
Sets the list of columns on which the report is sorted. Currently, you can only sort on one column.


Apex Reference Guide ReportMetadata Class

setStandardDateFilter(dateFilter)
Sets the standard date filter—which includes the start date, end date, date range, and date field API name—for the report.

setStandardFilters(filters)
Sets one or more standard filters on the report.

setTopRows(topRows)
Applies a row limit filter to a report.

##### getAggregates()

Returns unique identifiers for summary or custom summary formula fields in the report.

Syntax

```
   public LIST<String> getAggregates()

```

Return Value

Type: List<String>

Usage

For example:

**•** `a!Amount` represents the average for the `Amount` column.

**•** `s!Amount` represents the sum of the `Amount` column.

**•** `m!Amount` represents the minimum value of the `Amount` column.

**•** `x!Amount` represents the maximum value of the `Amount` column.

**•** `s!` _`<customfieldID>`_ represents the sum of a custom field column. For custom fields and custom report types, the identifier
is a combination of the summary type and the field ID.

##### getBuckets()

Returns a list of bucket fields in the report.

Signature

```
   public List<Reports.BucketField> getBuckets()

```

Return Value

Type: List<Reports.BucketField>

##### getCrossFilters()

Returns information about cross filters applied to a report.

Signature

```
   public Reports.CrossFilter getCrossFilters()

```


Apex Reference Guide ReportMetadata Class

Return Value

Type: List<Reports.CrossFilter>

##### getCurrencyCode()

Returns report currency, such as USD, EUR, or GBP, for an organization that has multicurrency enabled. The value is `null` if the
organization does not have multicurrency enabled.

Syntax

```
   public String getCurrencyCode()

```

Return Value

Type: String

##### getCustomSummaryFormula()

Returns information about custom summary formulas in a report.

Signature

```
   public Map<String,Reports.ReportCsf> getCustomSummaryFormula()

```

Return Value

Type: Map<String,Reports.ReportCsf>

##### getDescription()

Returns the description of the report.

Signature

```
   public String getDescription()

```

Return Value

Type: String

##### getDetailColumns()

Returns unique API names (column names) for the fields that contain detailed data. For example, the method might return the following
values: “OPPORTUNITY_NAME, TYPE, LEAD_SOURCE, AMOUNT.”

Syntax

```
   public LIST<String> getDetailColumns()

```


Apex Reference Guide ReportMetadata Class

Return Value

Type: List<String>

##### getDeveloperName()

Returns the report API name. For example, the method might return the following value: “Closed_Sales_This_Quarter.”

Syntax

```
   public String getDeveloperName()

```

Return Value

Type: String

##### getDivision()

Returns the division specified in the report.

Note: Reports that use standard filters (such as My Cases or My Team’s Accounts) show records in all divisions. These reports can’t
be further limited to a specific division.

Signature

```
   public String getDivision()

```

Return Value

Type: String

##### getGroupingsAcross()

Returns column groupings in a report.

Syntax

```
   public LIST<Reports.GroupingInfo> getGroupingsAcross()

```

Return Value

Type: List<Reports.GroupingInfo>

Usage

The identifier is:

**•** An empty array for reports in summary format, because summary reports don't include column groupings

**•** `BucketField_(` _**`ID`**_ `)` for bucket fields

**•** The ID of a custom field when the custom field is used for a column grouping


Apex Reference Guide ReportMetadata Class

##### getGroupingsDown()

Returns row groupings for a report.

Syntax

```
   public LIST<Reports.GroupingInfo> getGroupingsDown()

```

Return Value

Type: List<Reports.GroupingInfo>

Usage

The identifier is:

**•** `BucketField_(` _**`ID`**_ `)` for bucket fields

**•** The ID of a custom field when the custom field is used for grouping

##### getHasDetailRows()

Indicates whether the report has detail rows.

Signature

```
   public Boolean getHasDetailRows()

```

Return Value

Type: Boolean

##### getHasRecordCount()

Indicates whether the report shows the total number of records.

Signature

```
   public Boolean getHasRecordCount()

```

Return Value

Type: Boolean

##### getHistoricalSnapshotDates()

Returns a list of historical snapshot dates.

Syntax

```
   public LIST<String> getHistoricalSnapshotDates()

```


Apex Reference Guide ReportMetadata Class

Return Value

Type: List<String>

##### getId()

Returns the unique report ID.

Syntax

```
   public Id getId()

```

Return Value

Type: Id

##### getName()

Returns the report name.

Syntax

```
   public String getName()

```

Return Value

Type: String

##### getReportBooleanFilter()

Returns logic to parse custom field filters. The value is `null` when filter logic is not specified.

Syntax

```
   public String getReportBooleanFilter()

```

Return Value

Type: String

##### getReportFilters()

Returns a list of each custom filter in the report along with the field name, filter operator, and filter value.

Syntax

```
   public LIST<Reports.ReportFilter> getReportFilters()

```

Return Value

Type: List<Reports.ReportFilter>


Apex Reference Guide ReportMetadata Class

##### getReportFormat()

Returns the format of the report.

Syntax

```
   public Reports.ReportFormat getReportFormat()

```

Return Value

Type: Reports.ReportFormat

Usage

This value can be:

**•** `TABULAR`

**•** `SUMMARY`

**•** `MATRIX`

##### getReportType()

Returns the unique API name and display name for the report type.

Syntax

```
   public Reports.ReportType getReportType()

```

Return Value

Type: Reports.ReportType

##### getScope()

Returns the API name for the scope defined for the report. Scope values depend on the report type.

Signature

```
   public String getScope()

```

Return Value

Type: String

##### getShowGrandTotal()

Indicates whether the report shows the grand total.

Signature

```
   public Boolean getShowGrandTotal()

```


Apex Reference Guide ReportMetadata Class

Return Value

Type: Boolean

##### getShowSubtotals()

Indicates whether the report shows subtotals, such as column or row totals.

Signature

```
   public Boolean getShowSubtotals()

```

Return Value

Type: Boolean

##### getSortBy()

Returns the list of columns on which the report is sorted. Currently, you can sort on only one column.

Signature

```
   public List<Reports.SortColumn> getSortBy()

```

Return Value

Type: List<Reports.SortColumn>

##### getStandardDateFilter()

Returns information about the standard date filter for the report, such as the start date, end date, date range, and date field API name.

Signature

```
   public Reports.StandardDateFilter getStandardDateFilter()

```

Return Value

Type: Reports.StandardDateFilter

##### getStandardFilters()

Returns a list of standard filters for the report.

Signature

```
   public List<Reports.StandardFilter> getStandardFilters()

```

Return Value

Type: List<Reports.StandardFilter>


Apex Reference Guide ReportMetadata Class

##### getTopRows()

Returns information about a row limit filter, including the number of rows returned and the sort order.

Signature

```
   public Reports.TopRows getTopRows()

```

Return Value

Type: Reports.TopRows

##### setAggregates(aggregates)

Sets unique identifiers for standard or custom summary formula fields in the report.

Signature

```
   public void setAggregates(List<String> aggregates)

```

Parameters

```
   aggregates
```

Type: List<String>

Return Value

Type: void

##### setBuckets(buckets)

Creates bucket fields in a report.

Signature

```
   public void setBuckets(List<Reports.BucketField> buckets)

```

Parameters

```
   buckets
```

Type: List<Reports.BucketField>

Return Value

Type: void

##### setCrossFilters(crossFilters)

Applies cross filters to a report.


Apex Reference Guide ReportMetadata Class

Signature

```
   public void setCrossFilters(List<Reports.CrossFilter> crossFilters)

```

Parameters

```
   crossFilter
```

Type: List<Reports.CrossFilter>

Return Value

Type: void

##### setCurrencyCode(currencyCode)

Sets the currency, such as USD, EUR, or GBP, for report summary fields in an organization that has multicurrency enabled.

Signature

```
   public void setCurrencyCode(String currencyCode)

```

Parameters

```
   currencyCode
```

Type: String

Return Value

Type: void

##### setCustomSummaryFormula(customSummaryFormula)

Adds a custom summary formula to a report.

Signature

```
   public void setCustomSummaryFormula(MAP<String,Reports.ReportCsf> customSummaryFormula)

```

Parameters

```
   customSummaryFormula
```

Type: Map<String, Reports.ReportCsf>

Return Value

Type: void

##### setDescription(description)

Sets the description of the report.


Apex Reference Guide ReportMetadata Class

Signature

```
   public void setDescription(String description)

```

Parameters

```
   description
```

Type: String

Return Value

Type: void

##### setDetailColumns(detailColumns)

Sets the unique API names for the fields that contain detailed data—for example, `OPPORTUNITY_NAME`, `TYPE`, `LEAD_SOURCE`,
or `AMOUNT` .

Signature

```
   public void setDetailColumns(List<String> detailColumns)

```

Parameters

```
   detailColumns
```

Type: List<String>

Return Value

Type: void

##### setDeveloperName(developerName)

Sets the report API name—for example, `Closed_Sales_This_Quarter` .

Signature

```
   public void setDeveloperName(String developerName)

```

Parameters

```
   developerName
```

Type: String

Return Value

Type: void

##### setDivision(division)

Sets the division of the report.


Apex Reference Guide ReportMetadata Class

Note: Reports that use standard filters (such as My Cases or My Team’s Accounts) show records in all divisions. These reports can’t
be further limited to a specific division.

Signature

```
   public void setDivision(String division)

```

Parameters

```
   division
```

Type: String

Return Value

Type: void

##### setGroupingsAcross(groupingInfo)

Sets column groupings in a report.

Signature

```
   public void setGroupingsAcross(List<Reports.GroupingInfo> groupingInfo)

```

Parameters

```
   groupingInfo
```

Type: List<Reports.GroupingInfo>

Return Value

Type: void

##### setGroupingsDown(groupingInfo)

Sets row groupings for a report.

Signature

```
   public void setGroupingsDown(List<Reports.GroupingInfo> groupingInfo)

```

Parameters

```
   groupingInfo
```

Type: List<Reports.GroupingInfo>

Return Value

Type: void


Apex Reference Guide ReportMetadata Class

##### setHasDetailRows(hasDetailRows)

Specifies whether the report has detail rows.

Signature

```
   public void setHasDetailRows(Boolean hasDetailRows)

```

Parameters

```
   hasDetailRows
```

Type: Boolean

Return Value

Type: void

##### setHasRecordCount(hasRecordCount)

Specifies whether the report is configured to show the total number of records.

Signature

```
   public void setHasRecordCount(Boolean hasRecordCount)

```

Parameters

```
   hasRecordCount
```

Type: Boolean

Return Value

Type: void

##### setHistoricalSnapshotDates(historicalSnapshot)

Sets a list of historical snapshot dates.

Syntax

```
   public Void setHistoricalSnapshotDates(LIST<String> historicalSnapshot)

```

Parameters

```
   historicalSnapshot
```

Type: List<String>

Return Value

Type: Void


Apex Reference Guide ReportMetadata Class

##### setId(id)

Sets the unique report ID.

Signature

```
   public void setId(Id id)

```

Parameters

```
   id
```

Type: Id

Return Value

Type: void

##### setName(name)

Sets the report name.

Signature

```
   public void setName(String name)

```

Parameters

```
   name
```

Type: String

Return Value

Type: void

##### setReportBooleanFilter(reportBooleanFilter)

Sets logic to parse custom field filters.

Syntax

```
   public Void setReportBooleanFilter(String reportBooleanFilter)

```

Parameters

```
   reportBooleanFilter
```

Type: String

Return Value

Type: Void


Apex Reference Guide ReportMetadata Class

##### setReportFilters(reportFilters)

Sets a list of each custom filter in the report along with the field name, filter operator, and filter value.

Syntax

```
   public Void setReportFilters(LIST<Reports.ReportFilter> reportFilters)

```

Parameters

```
   reportFilters
```

Type: List<Reports.ReportFilter>

Return Value

Type: Void

##### setReportFormat(format)

Sets the format of the report.

Signature

```
   public void setReportFormat(Reports.ReportFormat format)

```

Parameters

```
   format
```

Type: Reports.ReportFormat

Return Value

Type: void

##### setReportType(reportType)

Sets the unique API name and display name for the report type.

Signature

```
   public void setReportType(Reports.ReportType reportType)

```

Parameters

```
   reportType
```

Type: Reports.ReportType

Return Value

Type: void


Apex Reference Guide ReportMetadata Class

##### setScope(scopeName)

Sets the API name for the scope defined for the report. Scope values depend on the report type.

Signature

```
   public void setScope(String scopeName)

```

Parameters

```
   scopeName
```

Type: String

Return Value

Type: void

##### setShowGrandTotal(showGrandTotal)

Specifies whether the report shows the grand total.

Signature

```
   public void setShowGrandTotal(Boolean showGrandTotal)

```

Parameters

```
   showGrandTotal
```

Type: Boolean

Return Value

Type: void

##### setShowSubtotals(showSubtotals)

Specifies whether the report shows subtotals, such as column or row totals.

Signature

```
   public void setShowSubtotals(Boolean showSubtotals)

```

Parameters

```
   showSubtotals
```

Type: Boolean

Return Value

Type: void


Apex Reference Guide ReportMetadata Class

##### setSortBy(column)

Sets the list of columns on which the report is sorted. Currently, you can only sort on one column.

Signature

```
   public void setSortBy(List<Reports.SortColumn> column)

```

Parameters

```
   column
```

Type: List<Reports.SortColumn>

Return Value

Type: void

##### setStandardDateFilter(dateFilter)

Sets the standard date filter—which includes the start date, end date, date range, and date field API name—for the report.

Signature

```
   public void setStandardDateFilter(Reports.StandardDateFilter dateFilter)

```

Parameters

```
   dateFilter
```

Type: Reports.StandardDateFilter

Return Value

Type: void

##### setStandardFilters(filters)

Sets one or more standard filters on the report.

Signature

```
   public void setStandardFilters(List<Reports.StandardFilter> filters)

```

Parameters

```
   filters
```

Type: List<Reports.StandardFilter>

Return Value

Type: void


### Apex Reference Guide ReportResults Class

##### setTopRows(topRows)

Applies a row limit filter to a report.

Signature

```
   public Reports.TopRows setTopRows(Reports.TopRows topRows)

```

Parameters

```
   topRows
```

Type: Reports.TopRows

Return Value

Type: void

### ReportResults Class

Contains the results of running a report.

Namespace

Reports

#### ReportResults Methods

### The following are methods for ReportResults . All are instance methods.

IN THIS SECTION:

getAllData()
Returns all report data.

getFactMap()
Returns summary-level data or summary and detailed data for each row or column grouping. Detailed data is available if the
`includeDetails` parameter is set to `true` when the report is run.

getGroupingsAcross()
Returns a collection of column groupings, keys, and values.

getGroupingsDown()
Returns a collection of row groupings, keys, and values.

getHasDetailRows()
Returns information about whether the fact map has detail rows.

getReportExtendedMetadata()
Returns additional, detailed metadata about the report, including data type and label information for groupings and summaries.

getReportMetadata()
Returns metadata about the report, including grouping and summary information.


Apex Reference Guide ReportResults Class

##### getAllData()

Returns all report data.

Syntax

```
   public Boolean getAllData()

```

Return Value

Type: Boolean

Usage

When `true`, indicates that all report results are returned.

When `false`, indicates that results are returned for the same number of rows as in a report run in Salesforce.

Note: For reports that contain too many records, use filters to refine results.

##### getFactMap()

Returns summary-level data or summary and detailed data for each row or column grouping. Detailed data is available if the
`includeDetails` parameter is set to `true` when the report is run.

Syntax

```
   public MAP<String,Reports.ReportFact> getFactMap()

```

Return Value

Type: Map<String,Reports.ReportFact>

##### getGroupingsAcross()

Returns a collection of column groupings, keys, and values.

Syntax

```
   public Reports.Dimension getGroupingsAcross()

```

Return Value

Type: Reports.Dimension

##### getGroupingsDown()

Returns a collection of row groupings, keys, and values.

Syntax

```
   public Reports.Dimension getGroupingsDown()

```


### Apex Reference Guide ReportScopeInfo Class

Return Value

Type: Reports.Dimension

##### getHasDetailRows()

Returns information about whether the fact map has detail rows.

Syntax

```
   public Boolean getHasDetailRows()

```

Return Value

Type: Boolean

Usage

**•** When `true`, indicates that the fact map returns values for summary-level and record-level data.

**•** When `false`, indicates that the fact map returns summary values.

##### getReportExtendedMetadata()

Returns additional, detailed metadata about the report, including data type and label information for groupings and summaries.

Syntax

```
   public Reports.ReportExtendedMetadata getReportExtendedMetadata()

```

Return Value

Type: Reports.ReportExtendedMetadata

##### getReportMetadata()

Returns metadata about the report, including grouping and summary information.

Syntax

```
   public Reports.ReportMetadata getReportMetadata()

```

Return Value

Type: Reports.ReportMetadata

### ReportScopeInfo Class

Contains information about possible scope values that you can choose. Scope values depend on the report type. For example, you can
set the scope for opportunity reports to `All opportunities`, `My team’s opportunities`, or `My opportunities` .


### Apex Reference Guide ReportScopeValue Class

Namespace

Reports

IN THIS SECTION:

#### ReportScopeInfo Methods ReportScopeInfo Methods The following are methods for ReportScopeInfo .

IN THIS SECTION:

##### getDefaultValue()

Returns the default scope of the data to display in the report.

##### getValues()

Returns a list of scope values specified for the report.

##### getDefaultValue()

Returns the default scope of the data to display in the report.

Signature

```
   public String getDefaultValue()

```

Return Value

Type: String

##### getValues()

Returns a list of scope values specified for the report.

Signature

```
   public List<Reports.ReportScopeValue> getValues()

```

Return Value

Type: List<Reports.ReportScopeValue>

### ReportScopeValue Class

Contains information about a possible scope value. Scope values depend on the report type. For example, you can set the scope for
opportunity reports to `All opportunities`, `My team’s opportunities`, or `My opportunities` .


Apex Reference Guide ReportScopeValue Class

Namespace

Reports

IN THIS SECTION:

#### ReportScopeValue Methods ReportScopeValue Methods The following are methods for ReportScopeValue .

IN THIS SECTION:

##### getAllowsDivision()

Returns a boolean value that indicates whether you can segment the report by this scope.

##### getLabel()

Returns the display name of the scope of the report.

##### getValue()

Returns the scope value for the report.

##### getAllowsDivision()

Returns a boolean value that indicates whether you can segment the report by this scope.

Signature

```
   public Boolean getAllowsDivision()

```

Return Value

Type: Boolean

##### getLabel()

Returns the display name of the scope of the report.

Signature

```
   public String getLabel()

```

Return Value

Type: String

##### getValue()

Returns the scope value for the report.


### Apex Reference Guide ReportType Class

Signature

```
   public String getValue()

```

Return Value

Type: String

### ReportType Class

Contains the unique API name and display name for the report type.

Namespace

Reports

#### ReportType Methods

### The following are methods for ReportType . All are instance methods.

IN THIS SECTION:

##### getLabel()

Returns the localized display name of the report type.

##### getType()

Returns the unique identifier of the report type.

##### getLabel()

Returns the localized display name of the report type.

Syntax

```
   public String getLabel()

```

Return Value

Type: String

##### getType()

Returns the unique identifier of the report type.

Syntax

```
   public String getType()

```

Return Value

Type: String


### Apex Reference Guide ReportTypeColumn Class ReportTypeColumn Class

Contains detailed report type metadata about a field, including data type, display name, and filter values.

Namespace

Reports

#### ReportTypeColumn Methods

### The following are methods for ReportTypeColumn . All are instance methods.

IN THIS SECTION:

##### getDataType()

Returns the data type of the field.

##### getFilterValues()

If the field data type is picklist, multi-select picklist, boolean, or checkbox, returns all filter values for a field. For example, checkbox
fields always have a value of `true` or `false` . For fields of other data types, the filter value is an empty array, because their values
can’t be determined.

getFilterable()
If the field is of a type that can’t be filtered, returns `False` . For example, fields of the type `Encrypted Text` can’t be filtered.

getLabel()
Returns the localized display name of the field.

getName()
Returns the unique API name of the field.

##### getDataType()

Returns the data type of the field.

Syntax

```
   public Reports.ColumnDataType getDataType()

```

Return Value

Type: Reports.ColumnDataType

##### getFilterValues()

If the field data type is picklist, multi-select picklist, boolean, or checkbox, returns all filter values for a field. For example, checkbox fields
always have a value of `true` or `false` . For fields of other data types, the filter value is an empty array, because their values can’t be
determined.

Syntax

```
   public LIST<Reports.FilterValue> getFilterValues()

```


### Apex Reference Guide ReportTypeColumnCategory Class

Return Value

Type: List<Reports.FilterValue>

##### getFilterable()

If the field is of a type that can’t be filtered, returns `False` . For example, fields of the type `Encrypted Text` can’t be filtered.

Syntax

```
   public Boolean getFilterable()

```

Return Value

Type: Boolean

##### getLabel()

Returns the localized display name of the field.

Syntax

```
   public String getLabel()

```

Return Value

Type: String

##### getName()

Returns the unique API name of the field.

Syntax

```
   public String getName()

```

Return Value

Type: String

### ReportTypeColumnCategory Class

Information about categories of fields in a report type.

Namespace

Reports


Apex Reference Guide ReportTypeColumnCategory Class

Usage

A report type column category is a set of fields that the report type grants access to. For example, an opportunity report has categories
like _Opportunity Information_ and _Primary Contact_ . The Opportunity Information category has fields like _Amount_, _Probability_, and _Close_
_Date_ .

Get category information about a report by first getting the report metadata:

```
   // Get the report ID

   List <Report> reportList = [SELECT Id,DeveloperName FROM Report where DeveloperName =

   'Q1_Opportunities2'];

   String reportId = (String)reportList.get(0).get('Id');

   // Describe the report

   Reports.ReportDescribeResult describeResults =

   Reports.ReportManager.describeReport(reportId);

   // Get report type metadata

   Reports.ReportTypeMetadata reportTypeMetadata = describeResults.getReportTypeMetadata();

   // Get report type column categories

   List<Reports.ReportTypeColumnCategory> reportTypeColumnCategories =

   reportTypeMetadata.getCategories();

   System.debug('reportTypeColumnCategories: ' + reportTypeColumnCategories);

#### ReportTypeColumnCategory Methods The following are methods for ReportTypeColumnCategory . All are instance methods.

```

IN THIS SECTION:

##### getColumns()

Returns information for all fields in the report type. The information is organized by each section’s unique API name.

getLabel()
Returns the localized display name of a section in the report type under which fields are organized. For example, in an Accounts
with Contacts custom report type, `Account General` is the display name of the section that contains fields on general account
information.

##### getColumns()

Returns information for all fields in the report type. The information is organized by each section’s unique API name.

Syntax

```
   public MAP<String,Reports.ReportTypeColumn> getColumns()

```

Return Value

Type: Map<String,Reports.ReportTypeColumn>


### Apex Reference Guide ReportTypeMetadata Class

##### getLabel()

Returns the localized display name of a section in the report type under which fields are organized. For example, in an Accounts with
Contacts custom report type, `Account General` is the display name of the section that contains fields on general account information.

Syntax

```
   public String getLabel()

```

Return Value

Type: String

### ReportTypeMetadata Class

Contains report type metadata, which gives you information about the fields that are available in each section of the report type, plus
filter information for those fields.

Namespace

Reports

IN THIS SECTION:

#### ReportTypeMetadata Methods ReportTypeMetadata Methods

### The following are methods for ReportTypeMetadata . All are instance methods.

IN THIS SECTION:

##### getCategories()

Returns all fields in the report type. The fields are organized by section.

getDivisionInfo()
Returns the default division and a list of all possible divisions that can be applied to this type of report.

getScopeInfo()
Returns information about the scopes that can be applied to this type of report.

getStandardDateFilterDurationGroups()
Returns information about the standard date filter groupings that can be applied to this type of report. Standard date filter groupings
include Calendar Year, Calendar Quarter, Calendar Month, Calendar Week, Fiscal Year, Fiscal Quarter, Day and a custom value based
on a user-defined date range.

getStandardFilterInfos()
Returns information about standard date filters that can be applied to this type of report.

##### getCategories()

Returns all fields in the report type. The fields are organized by section.


Apex Reference Guide ReportTypeMetadata Class

Syntax

```
   public LIST<Reports.ReportTypeColumnCategory> getCategories()

```

Return Value

Type: List<Reports.ReportTypeColumnCategory>

##### getDivisionInfo()

Returns the default division and a list of all possible divisions that can be applied to this type of report.

Signature

```
   public Reports.ReportDivisionInfo getDivisionInfo()

```

Return Value

Type: Reports.ReportDivisionInfo

##### getScopeInfo()

Returns information about the scopes that can be applied to this type of report.

Signature

```
   public Reports.ReportScopeInfo getScopeInfo()

```

Return Value

Type: Reports.ReportScopeInfo

##### getStandardDateFilterDurationGroups()

Returns information about the standard date filter groupings that can be applied to this type of report. Standard date filter groupings
include Calendar Year, Calendar Quarter, Calendar Month, Calendar Week, Fiscal Year, Fiscal Quarter, Day and a custom value based on
a user-defined date range.

Signature

```
   public List<Reports.StandardDateFilterDurationGroup>

##### `getStandardDateFilterDurationGroups()`

```

Return Value

Type: List<Reports.StandardDateFilterDurationGroup>

##### getStandardFilterInfos()

Returns information about standard date filters that can be applied to this type of report.


### Apex Reference Guide SortColumn Class

Signature

```
   public Map<String,Reports.StandardFilterInfo> getStandardFilterInfos()

```

Return Value

Type: Map<String,Reports.StandardFilterInfo>

### SortColumn Class

Contains information about the sort column used in the report.

Namespace

Reports

IN THIS SECTION:

#### SortColumn Methods SortColumn Methods

### The following are methods for SortColumn .

IN THIS SECTION:

##### getSortColumn()

Returns the column used to sort the records in the report.

getSortOrder()
Returns the the sort order— ascending or descending—for the sort column.

setSortColumn(sortColumn)
Sets the column used to sort the records in the report.

setSortOrder(SortOrder)
Sets the sort order— ascending or descending—for the sort column.

##### getSortColumn()

Returns the column used to sort the records in the report.

Signature

```
   public String getSortColumn()

```

Return Value

Type: String


### Apex Reference Guide StandardDateFilter Class

##### getSortOrder()

Returns the the sort order— ascending or descending—for the sort column.

Signature

```
   public Reports.ColumnSortOrder getSortOrder()

```

Return Value

Type: Reports.ColumnSortOrder

##### setSortColumn(sortColumn)

Sets the column used to sort the records in the report.

Signature

```
   public void setSortColumn(String sortColumn)

```

Parameters

```
   sortColumn
```

Type: String

Return Value

Type: void

##### setSortOrder(SortOrder)

Sets the sort order— ascending or descending—for the sort column.

Signature

```
   public void setSortOrder(Reports.ColumnSortOrder sortOrder)

```

Parameters

```
   sortOrder
```

Type: Reports.ColumnSortOrder

Return Value

Type: void

### StandardDateFilter Class

Contains information about standard date filter available in the report—for example, the API name, start date, and end date of the
standard date filter duration as well as the API name of the date field on which the filter is placed.


Apex Reference Guide StandardDateFilter Class

Namespace

Reports

IN THIS SECTION:

#### StandardDateFilter Methods StandardDateFilter Methods The following are methods for StandardDateFilter .

IN THIS SECTION:

##### getColumn()

Returns the API name of the standard date filter column.

##### getDurationValue()

Returns duration information about a standard date filter, such as start date, end date, and display name and API name of the date
filter.

getEndDate()
Returns the end date of the standard date filter.

getStartDate()
Returns the start date for the standard date filter.

setColumn(standardDateFilterColumnName)
Sets the API name of the standard date filter column.

setDurationValue(durationName)
Sets the API name of the standard date filter.

setEndDate(endDate)
Sets the end date for the standard date filter.

setStartDate(startDate)
Sets the start date for the standard date filter.

##### getColumn()

Returns the API name of the standard date filter column.

Signature

```
   public String getColumn()

```

Return Value

Type: String

##### getDurationValue()

Returns duration information about a standard date filter, such as start date, end date, and display name and API name of the date filter.


Apex Reference Guide StandardDateFilter Class

Signature

```
   public String getDurationValue()

```

Return Value

Type: String

##### getEndDate()

Returns the end date of the standard date filter.

Signature

```
   public String getEndDate()

```

Return Value

Type: String

##### getStartDate()

Returns the start date for the standard date filter.

Signature

```
   public String getStartDate()

```

Return Value

Type: String

##### setColumn(standardDateFilterColumnName)

Sets the API name of the standard date filter column.

Signature

```
   public void setColumn(String standardDateFilterColumnName)

```

Parameters

```
   standardDateFilterColumnName
```

Type: String

Return Value

Type: void


Apex Reference Guide StandardDateFilter Class

##### setDurationValue(durationName)

Sets the API name of the standard date filter.

Signature

```
   public void setDurationValue(String durationName)

```

Parameters

```
   durationName
```

Type: String

Return Value

Type: void

##### setEndDate(endDate)

Sets the end date for the standard date filter.

Signature

```
   public void setEndDate(String endDate)

```

Parameters

```
   endDate
```

Type: String

Return Value

Type: void

##### setStartDate(startDate)

Sets the start date for the standard date filter.

Signature

```
   public void setStartDate(String startDate)

```

Parameters

```
   startDate
```

Type: String

Return Value

Type: void


### Apex Reference Guide StandardDateFilterDuration Class StandardDateFilterDuration Class

Contains information about each standard date filter—also referred to as a relative date filter. It contains the API name and display label
of the standard date filter duration as well as the start and end dates.

Namespace

Reports

IN THIS SECTION:

#### StandardDateFilterDuration Methods StandardDateFilterDuration Methods

### The following are methods for StandardDateFilterDuration .

IN THIS SECTION:

##### getEndDate()

Returns the end date of the date filter.

##### getLabel()

Returns the display name of the date filter. Possible values are relative date filters—like `Current FY` and `Current FQ` —and
custom date filters.

getStartDate()
Returns the start date of the date filter.

getValue()
Returns the API name of the date filter. Possible values are relative date filters—like `THIS_FISCAL_YEAR` and
`NEXT_FISCAL_QUARTER` —and custom date filters.

##### getEndDate()

Returns the end date of the date filter.

Signature

```
   public String getEndDate()

```

Return Value

Type: String

##### getLabel()

Returns the display name of the date filter. Possible values are relative date filters—like `Current FY` and `Current FQ` —and
custom date filters.


### Apex Reference Guide StandardDateFilterDurationGroup Class

Signature

```
   public String getLabel()

```

Return Value

Type: String

##### getStartDate()

Returns the start date of the date filter.

Signature

```
   public String getStartDate()

```

Return Value

Type: String

##### getValue()

Returns the API name of the date filter. Possible values are relative date filters—like `THIS_FISCAL_YEAR` and
`NEXT_FISCAL_QUARTER` —and custom date filters.

Signature

```
   public String getValue()

```

Return Value

Type: String

### StandardDateFilterDurationGroup Class

Contains information about the standard date filter groupings, such as the grouping display label and all standard date filters that fall
under the grouping. Groupings include `Calendar Year`, `Calendar Quarter`, `Calendar Month`, `Calendar Week`,
`Fiscal Year`, `Fiscal Quarter`, `Day`, and custom values based on user-defined date ranges.

Namespace

Reports

IN THIS SECTION:

#### StandardDateFilterDurationGroup Methods StandardDateFilterDurationGroup Methods

### The following are methods for StandardDateFilterDurationGroup .


### Apex Reference Guide StandardFilter Class

IN THIS SECTION:

##### getLabel()

Returns the display label for the standard date filter grouping.

##### getStandardDateFilterDurations()

Returns the standard date filter groupings.

##### getLabel()

Returns the display label for the standard date filter grouping.

Signature

```
   public String getLabel()

```

Return Value

Type: String

##### getStandardDateFilterDurations()

Returns the standard date filter groupings.

Signature

```
   public List<Reports.StandardDateFilterDuration> getStandardDateFilterDurations()

```

Return Value

Type: List<Reports.StandardDateFilterDuration>

For example, a standard filter date grouping might look like this:

```
   Reports.StandardDateFilterDuration[endDate=2015-12-31, label=Current FY,

   startDate=2015-01-01, value=THIS_FISCAL_YEAR],

   Reports.StandardDateFilterDuration[endDate=2014-12-31, label=Previous FY,

   startDate=2014-01-01, value=LAST_FISCAL_YEAR],

   Reports.StandardDateFilterDuration[endDate=2014-12-31, label=Previous 2 FY,

   startDate=2013-01-01, value=LAST_N_FISCAL_YEARS:2]

### StandardFilter Class

```

Contains information about the standard filter defined in the report, such as the filter field API name and filter value.

Namespace

Reports


Apex Reference Guide StandardFilter Class

Usage

Use to get or set standard filters on a report. Standard filters vary by report type. For example, standard filters for reports on the Opportunity
object are Show, Opportunity Status, and Probability.

IN THIS SECTION:

#### StandardFilter Methods StandardFilter Methods The following are methods for StandardFilter .

IN THIS SECTION:

##### getName()

Return the API name of the standard filter.

##### getValue()

Returns the standard filter value.

setName(name)
Sets the API name of the standard filter.

setValue(value)
Sets the standard filter value.

##### getName()

Return the API name of the standard filter.

Signature

```
   public String getName()

```

Return Value

Type: String

##### getValue()

Returns the standard filter value.

Signature

```
   public String getValue()

```

Return Value

Type: String


### Apex Reference Guide StandardFilterInfo Class

##### setName(name)

Sets the API name of the standard filter.

Signature

```
   public void setName(String name)

```

Parameters

```
   name
```

Type: String

Return Value

Type: void

##### setValue(value)

Sets the standard filter value.

Signature

```
   public void setValue(String value)

```

Parameters

```
   value
```

Type: String

Return Value

Type: void

### StandardFilterInfo Class

Is an abstract base class for an object that provides standard filter information.

Namespace

Reports

IN THIS SECTION:

#### StandardFilterInfo Methods StandardFilterInfo Methods

### The following are methods for StandardFilterInfo .


### Apex Reference Guide StandardFilterInfoPicklist Class

IN THIS SECTION:

##### getLabel()

Returns the display label of the standard filter.

##### getType()

Returns the type of standard filter.

##### getLabel()

Returns the display label of the standard filter.

Signature

```
   public String getLabel()

```

Return Value

Type: String

##### getType()

Returns the type of standard filter.

Signature

```
   public Reports.StandardFilterType getType()

```

Return Value

Type: Reports.StandardFilterType

### StandardFilterInfoPicklist Class

Contains information about the standard filter picklist, such as the display name and type of the filter field, the default picklist value, and
a list of all possible picklist values.

Namespace

Reports

IN THIS SECTION:

#### StandardFilterInfoPicklist Methods StandardFilterInfoPicklist Methods

### The following are methods for StandardFilterInfoPicklist .


Apex Reference Guide StandardFilterInfoPicklist Class

IN THIS SECTION:

##### getDefaultValue()

Returns the default value for the standard filter picklist.

##### getFilterValues()

Returns a list of standard filter picklist values.

##### getLabel()

Returns the display name of the standard filter picklist.

##### getType()

Returns the type of the standard filter picklist.

##### getDefaultValue()

Returns the default value for the standard filter picklist.

Signature

```
   public String getDefaultValue()

```

Return Value

Type: String

##### getFilterValues()

Returns a list of standard filter picklist values.

Signature

```
   public List<Reports.FilterValue> getFilterValues()

```

Return Value

Type: List<Reports.FilterValue>

##### getLabel()

Returns the display name of the standard filter picklist.

Signature

```
   public String getLabel()

```

Return Value

Type: String

##### getType()

Returns the type of the standard filter picklist.


### Apex Reference Guide StandardFilterType Enum

Signature

```
   public Reports.StandardFilterType getType()

```

Return Value

Type: Reports.StandardFilterType

### StandardFilterType Enum The StandardFilterType enum describes the type of standard filters in a report. The getType() method returns a

`Reports.StandardFilterType` enum value.

Namespace

Reports

Enum Values

The following are the values of the `Reports.StandardFilterType` enum.

**Value** **Description**

`PICKLIST` Values for the standard filter type.

`STRING` String values.

### SummaryValue Class

Contains summary data for a cell of the report.

Namespace

Reports

#### SummaryValue Methods

### The following are methods for SummaryValue . All are instance methods.

IN THIS SECTION:

##### getLabel()

Returns the formatted summary data for a specified cell.

getValue()
Returns the numeric value of the summary data for a specified cell.

##### getLabel()

Returns the formatted summary data for a specified cell.


### Apex Reference Guide ThresholdInformation Class

Syntax

```
   public String getLabel()

```

Return Value

Type: String

##### getValue()

Returns the numeric value of the summary data for a specified cell.

Syntax

```
   public Object getValue()

```

Return Value

Type: Object

### ThresholdInformation Class

Contains a list of evaluated conditions for a report notification.

Namespace

Reports

IN THIS SECTION:

#### ThresholdInformation Constructors

ThresholdInformation Methods

#### ThresholdInformation Constructors

### The following are constructors for ThresholdInformation .

IN THIS SECTION:

##### ThresholdInformation(evaluatedConditions)

Creates a new instance of the `Reports.EvaluatedCondition` class.

##### ThresholdInformation(evaluatedConditions)

Creates a new instance of the `Reports.EvaluatedCondition` class.

Signature

```
   public ThresholdInformation(List<Reports.EvaluatedCondition> evaluatedConditions)

```


### Apex Reference Guide TopRows Class

Parameters

```
   evaluatedConditions
```

Type: List<Reports.EvaluatedCondition>

A list of `Reports.EvaluatedCondition` objects.

#### ThresholdInformation Methods The following are methods for ThresholdInformation .

IN THIS SECTION:

##### getEvaluatedConditions()

Returns a list of evaluated conditions for a report notification.

##### getEvaluatedConditions()

Returns a list of evaluated conditions for a report notification.

Signature

```
   public List<Reports.EvaluatedCondition> getEvaluatedConditions()

```

Return Value

Type: List<Reports.EvaluatedCondition>

### TopRows Class

Contains methods and constructors for working with information about a row limit filter.

Namespace

Reports

IN THIS SECTION:

#### TopRows Constructors

TopRows Methods

#### TopRows Constructors

### The following are constructors for TopRows .

IN THIS SECTION:

TopRows(rowLimit, direction)
Creates an instance of the `Reports.TopRows` class using the specified parameters.


Apex Reference Guide TopRows Class

##### TopRows()

Creates an instance of the `Reports.TopRows` class. You can then set values by using the class’s `set` methods.

##### TopRows(rowLimit, direction)

Creates an instance of the `Reports.TopRows` class using the specified parameters.

Signature

```
   public TopRows(Integer rowLimit, Reports.ColumnSortOrder direction)

```

Parameters

```
   rowLimit
```

Type: Integer

The number of rows returned in the report.

```
   direction
```

Type: Reports.ColumnSortOrder

The sort order of the report rows.

##### TopRows()

Creates an instance of the `Reports.TopRows` class. You can then set values by using the class’s `set` methods.

Signature

```
   public TopRows()

#### TopRows Methods

##### The following are methods for TopRows .

```

IN THIS SECTION:

getDirection()
Returns the sort order of the report rows.

getRowLimit()
Returns the maximum number of rows shown in the report.

setDirection(value)
Sets the sort order of the report’s rows.

setDirection(direction)
Sets the sort order of the report’s rows.

setRowLimit(rowLimit)
Sets the maximum number of rows included in the report.

toString()
Returns a string.


Apex Reference Guide TopRows Class

##### getDirection()

Returns the sort order of the report rows.

Signature

```
   public Reports.ColumnSortOrder getDirection()

```

Return Value

Type: Reports.ColumnSortOrder

##### getRowLimit()

Returns the maximum number of rows shown in the report.

Signature

```
   public Integer getRowLimit()

```

Return Value

Type: Integer

##### setDirection(value)

Sets the sort order of the report’s rows.

Signature

```
   public void setDirection(String value)

```

Parameters

```
   value
```

Type: String

For possible values, see Reports.ColumnSortOrder.

Return Value

Type: void

##### setDirection(direction)

Sets the sort order of the report’s rows.

Signature

```
   public void setDirection(Reports.ColumnSortOrder direction)

```


### Apex Reference Guide Reports Exceptions

Parameters

```
   direction
```

Type: Reports.ColumnSortOrder

Return Value

Type: void

##### setRowLimit(rowLimit)

Sets the maximum number of rows included in the report.

Signature

```
   public void setRowLimit(Integer rowLimit)

```

Parameters

```
   rowLimit
```

Type: Integer

Return Value

Type: void

##### toString()

Returns a string.

Signature

```
   public String toString()

```

Return Value

Type: String

### Reports Exceptions The Reports namespace contains exception classes.

All exception classes support built-in methods for returning the error message and exception type. See Exception Class and Built-In
Exceptions on page 3784.

### The Reports namespace contains these exceptions:

**Exception** **Description** **Methods**

`Reports.FeatureNotSupportedException` Invalid report format

`Reports.InstanceAccessException` Unable to access report
instance


## Apex Reference Guide RevSignaling Namespace

**Exception** **Description** **Methods**

`Reports.InvalidFilterException` Filter validation error `List<String> getFilterErrors()` returns a list of
filter errors

`Reports.InvalidReportMetadataException` Missing metadata for `List<String> getReportMetadataErrors()`
filters returns a list of metadata errors

`Reports.InvalidSnapshotDateException` Invalid historical report `List<String> getSnapshotDateErrors()` returns
format a list of snapshot date errors

`Reports.MetadataException` No selected report
columns

`Reports.ReportRunException` Error running report

`Reports.UnsupportedOperationException` Missing permissions for
running reports

## RevSignaling Namespace The RevSignaling namespace provides classes to extend the standard procedure plan implementation through custom logic. A

procedure plan helps you set up your procedures, configure the procedure execution settings, and relate them to a context definition
in one centralized location based on your requirements.

## The RevSignaling namespace includes these classes and an interface.

**•** [ProcedurePlan Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RevSignaling_ProcedurePlan.htm)

**•** [SignalingApexProcessor Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_interface_RevSignaling_SignalingApexProcessor.htm)

**•** [TransactionRequest Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RevSignaling_TransactionRequest.htm)

**•** [TransactionResponse Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RevSignaling_TransactionResponse.htm)

## RevSalesTrxn Namespace The RevSalesTrxn namespace provides classes and methods to create a sales transaction, such as a quote or an order, with

integrated pricing and configuration.

## The RevSalesTrxn namespace includes these classes.

**•** [ConfigurationOptionsInput Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RevSalesTrxn_ConfigurationOptionsInput.htm)

**•** [GraphRequest Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RevSalesTrxn_GraphRequest.htm)

**•** [PlaceSalesTransactionException Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RevSalesTrxn_PlaceSalesTransactionException.htm)

**•** [PlaceSalesTransactionExecutor Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RevSalesTrxn_PlaceSalesTransactionExecutor.htm)

**•** [PlaceSalesTransactionResponse Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RevSalesTrxn_PlaceSalesTransactionResponse.htm)

**•** [RecordResource Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RevSalesTrxn_RecordResource.htm)

**•** [RecordWithReferenceRequest Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RevSalesTrxn_RecordWithReferenceRequest.htm)

SEE ALSO:

_Salesforce Help_ [: Build Your Procedure Plan Framework](https://help.salesforce.com/s/articleView?id=ind.pricing_procedure_plan_framework.htm&language=en_US)


## Apex Reference Guide RichMessaging Namespace RichMessaging Namespace

Provides objects and methods for handling content in enhanced Messaging channels.

## The following are the classes in the RichMessaging namespace.

IN THIS SECTION:

AbstractTiming Class
Parent class for other RichMessaging timing classes.

AddressableContact Class
Represents an addressable contact.

AuthRequestHandler Interface
Use this interface to handle authorization request responses.

AuthRequestResponse Class
This class contains authorization request response data.

AuthRequestResult Class
This class contains the result from handling the authorization request response.

AuthRequestResultStatus Enum
This enum describes the authentication result status.

DeferredTiming Class
Represents timing for a transaction that occurs in the future.

MessageDefinitionInputParameter Class
Represents a messaging component parameter value. This class is used to provide parameter payloads that can be translated to
structured content payloads in rich content messages.

PaymentItemStatus Enum
Represents the status of a payment item in payment requests sent in enhanced Messaging channels.

PaymentLineItem Class
Represents a payment line item in payment requests sent in enhanced Messaging channels.

PaymentMethod Class
Represents a payment method.

PostalAddress Class
Represents the postal address.

ProcessFormHandler Interface
Apex interface that processes the responses to forms submitted in a messaging session.

ProcessPaymentHandler Interface
Interface used to process payment requests.

ProcessPaymentRequest Class
Represents a request to process a payment.

ProcessPaymentResult Class
Represents the result of a payment processing operation.


### Apex Reference Guide AbstractTiming Class

ProcessPaymentResultStatus Enum
Represents the status of a payment processing result.

RecurringTiming Class
Represents a payment that occurs on a regular basis.

ShippingMethod Class
Represents a shipping method listed in payment requests sent in enhanced Messaging channels.

TimeSlotOption Class
Represents a complex time slot option type. This class is used to provide time option payloads that can be translated to structured
content payloads in rich content messages.

TimingIntervalUnit Enum
Represents an enumerated type that describes the timing interval.

TimingType Enum
Represents an enumerated type that describes the type of timing.

### AbstractTiming Class

Parent class for other RichMessaging timing classes.

Namespace

RichMessaging

SEE ALSO:

DeferredTiming Class

RecurringTiming Class

### AddressableContact Class

Represents an addressable contact.

Namespace

RichMessaging

IN THIS SECTION:

#### AddressableContact Constructors

AddressableContact Properties

#### AddressableContact Constructors

### The following are constructors for AddressableContact .


Apex Reference Guide AddressableContact Class

IN THIS SECTION:

##### AddressableContact(givenName, phoneticGivenName, familyName, phoneticFamilyName, emailAddress, phoneNumber, postalAddress)

Creates a new instance of the `RichMessaging.AddressableContact` class.

##### **`AddressableContact(givenName, phoneticGivenName, familyName,`**

```
  phoneticFamilyName, emailAddress, phoneNumber, postalAddress)

```

Creates a new instance of the `RichMessaging.AddressableContact` class.

Signature

```
   public AddressableContact(String givenName, String phoneticGivenName, String familyName,

   String phoneticFamilyName, String emailAddress, String phoneNumber,

   RichMessaging.PostalAddress postalAddress)

```

Parameters

```
   givenName
```

Type: String

The contact’s first name.

```
   phoneticGivenName
```

Type: String

The phonetic spelling of the contact’s first name.

```
   familyName
```

Type: String

The contact’s surname.

```
   phoneticFamilyName
```

Type: String

The phonetic spelling of the contact’s surname.

```
   emailAddress
```

Type: String

The contact’s email address.

```
   phoneNumber
```

Type: String

The contact’s phone number.

```
   postalAddress
```

Type: RichMessaging.PostalAddress

The contact’s postal address.

#### AddressableContact Properties

##### The following are properties for AddressableContact .


Apex Reference Guide AddressableContact Class

IN THIS SECTION:

##### emailAddress

The contact’s email address.

##### familyName

The contact’s surname.

##### givenName

The contact’s first name.

phoneNumber
The contact’s phone number.

phoneticFamilyName
The phonetic spelling of the contact’s surname.

phoneticGivenName
The phonetic spelling of the contact’s first name.

postalAddress
The contact’s postal address.

##### **`emailAddress`**

The contact’s email address.

Signature

```
   public String emailAddress {get; set;}

```

Property Value

Type: String

##### **`familyName`**

The contact’s surname.

Signature

```
   public String familyName {get; set;}

```

Property Value

Type: String

##### **`givenName`**

The contact’s first name.

Signature

```
   public String givenName {get; set;}

```


Apex Reference Guide AddressableContact Class

Property Value

Type: String

##### **`phoneNumber`**

The contact’s phone number.

Signature

```
   public String phoneNumber {get; set;}

```

Property Value

Type: String

##### **`phoneticFamilyName`**

The phonetic spelling of the contact’s surname.

Signature

```
   public String phoneticFamilyName {get; set;}

```

Property Value

Type: String

##### **`phoneticGivenName`**

The phonetic spelling of the contact’s first name.

Signature

```
   public String phoneticGivenName {get; set;}

```

Property Value

Type: String

##### **`postalAddress`**

The contact’s postal address.

Signature

```
   public RichMessaging.PostalAddress postalAddress {get; set;}

```

Property Value

Type: RichMessaging.PostalAddress


### Apex Reference Guide AuthRequestHandler Interface AuthRequestHandler Interface

Use this interface to handle authorization request responses.

Namespace

RichMessaging on page 3318

Usage

[When using this interface, the following limits are overridden. See Execution Governors and Limits in the Apex Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_gov_limits.htm)

**Table 1: Overridden Limits**

IN THIS SECTION:

#### AuthRequestHandler Methods

AuthRequestHandler Example Implementation

#### AuthRequestHandler Methods

### The following are methods for AuthRequestHandler .

IN THIS SECTION:

##### handleAuthRequest(var1)

Handles authorization request response.

##### **`handleAuthRequest(var1)`**

Handles authorization request response.

Signature

```
   public RichMessaging.AuthRequestResult

   handleAuthRequest(RichMessaging.AuthRequestResponse var1)

```


Apex Reference Guide AuthRequestHandler Interface

Parameters

```
   var1
```

Type: RichMessaging.AuthRequestResponse on page 3325

The authorization response.

Return Value

Type: RichMessaging.AuthRequestResult on page 3327

#### AuthRequestHandler Example Implementation

This is an example implementation of the `RichMessaging.AuthRequestHandler` interface.

```
   global class SampleAuthRequestHandler implements RichMessaging.AuthRequestHandler {

      global RichMessaging.AuthRequestResult

   handleAuthRequest(RichMessaging.AuthRequestResponse authReqResponse) {

        // Get contact email from messaging session

        String sessionId = authReqResponse.getContextRecordId();

        String contactEmail = [select MessagingSession.EndUserContact.Email from

   MessagingSession where id = :sessionId].EndUserContact.Email;

        RichMessaging.AuthRequestResultStatus authRequestStatus =

   RichMessaging.AuthRequestResultStatus.DECLINED;

        DateTime dt = DateTime.now();

        // Get user info if there's a valid contact email

        if (!String.isBlank(contactEmail)) {

           String userInfoUrl = 'https://api.MY_AUTH_DOMAIN.com/v1/';

           HttpRequest req = new HttpRequest();

           req.setEndpoint(userInfoUrl);

           req.setHeader('Content-Type','application/json');

           req.setMethod('GET');

           req.setHeader('Authorization', 'Bearer '+authReqResponse.getAccessToken());

           Http http = new Http();

           HTTPResponse res = http.send(req);

           String responseBody = res.getBody();

           UserWrapper userInfo = (UserWrapper)System.JSON.deserialize(responseBody,

   UserWrapper.class);

           if (userInfo.email == contactEmail) {

             authRequestStatus = RichMessaging.AuthRequestResultStatus.AUTHENTICATED;

             dt = dt.addHours(6);

           }

         }

        return new RichMessaging.AuthRequestResult(

           null,

```


### Apex Reference Guide AuthRequestResponse Class

```
           authRequestStatus,

           dt);

      }

      public class UserWrapper{

        public String href;

        public String display_name;

        public String type;

        public String country;

        public String product;

        public String email;

      }

   }

### AuthRequestResponse Class

```

This class contains authorization request response data.

Namespace

RichMessaging

IN THIS SECTION:

#### AuthRequestResponse Constructors

AuthRequestResponse Methods

#### AuthRequestResponse Constructors

### The following are constructors for AuthRequestResponse .

IN THIS SECTION:

##### AuthRequestResponse(accessToken, contextRecordId, authProviderName)

Creates a new instance of the `RichMessaging.AuthRequestResponse` class.

##### **`AuthRequestResponse(accessToken, contextRecordId, authProviderName)`**

Creates a new instance of the `RichMessaging.AuthRequestResponse` class.

Signature

```
   public AuthRequestResponse(String accessToken, String contextRecordId, String

   authProviderName)

```

Parameters

```
   accessToken
```

Type: String


Apex Reference Guide AuthRequestResponse Class

The authorization access token.

```
   contextRecordId
```

Type: String

The context record ID.

```
   authProviderName
```

Type: String

The provider name.

#### AuthRequestResponse Methods The following are methods for AuthRequestResponse .

IN THIS SECTION:

##### getAccessToken()

Gets the authorization access token.

##### getAuthProviderName()

Get the authorization provider name.

getContextRecordId()
Gets the context record ID.

##### **`getAccessToken()`**

Gets the authorization access token.

Signature

```
   public String getAccessToken()

```

Return Value

Type: String

The access token.

##### **`getAuthProviderName()`**

Get the authorization provider name.

Signature

```
   public String getAuthProviderName()

```

Return Value

Type: String

The authorization provider name.


### Apex Reference Guide AuthRequestResult Class

##### **`getContextRecordId()`**

Gets the context record ID.

Signature

```
   public String getContextRecordId()

```

Return Value

Type: String

The context record ID.

### AuthRequestResult Class

This class contains the result from handling the authorization request response.

Namespace

RichMessaging

IN THIS SECTION:

#### AuthRequestResult Constructors

AuthRequestResult Properties

#### AuthRequestResult Constructors

### The following are constructors for AuthRequestResult .

IN THIS SECTION:

##### AuthRequestResult(redirectPageReference, resultStatus, expirationDateTime)

Creates a new instance of the `RichMessaging.AuthRequestResult` class.

##### **`AuthRequestResult(redirectPageReference, resultStatus, expirationDateTime)`**

Creates a new instance of the `RichMessaging.AuthRequestResult` class.

Signature

```
   public AuthRequestResult(System.PageReference redirectPageReference,

   RichMessaging.AuthRequestResultStatus resultStatus, Datetime expirationDateTime)

```

Parameters

```
   redirectPageReference
```

Type: System.PageReference on page 3984

The reference to the redirect page.


Apex Reference Guide AuthRequestResult Class

##### _`resultStatus`_

Type: RichMessaging.AuthRequestResultStatus on page 3329

The result status value.

##### _`expirationDateTime`_

Type: Datetime

The expiration time.

#### AuthRequestResult Properties The following are properties for AuthRequestResult .

IN THIS SECTION:

##### expirationDateTime

The expiration date and time.

##### redirectPageReference

The reference to the redirect page.

##### resultStatus

The result status value.

##### **`expirationDateTime`**

The expiration date and time.

Signature

```
   public Datetime expirationDateTime {get; set;}

```

Property Value

Type: Datetime

##### **`redirectPageReference`**

The reference to the redirect page.

Signature

```
   public System.PageReference redirectPageReference {get; set;}

```

Property Value

Type: System.PageReference on page 3984

##### **`resultStatus`**

The result status value.


### Apex Reference Guide AuthRequestResultStatus Enum

Signature

```
   public RichMessaging.AuthRequestResultStatus resultStatus {get; set;}

```

Property Value

Type: RichMessaging.AuthRequestResultStatus on page 3329

### AuthRequestResultStatus Enum

This enum describes the authentication result status.

Enum Values

The following are the values of the `RichMessaging.AuthRequestResultStatus` enum.

**Value** **Description**

`AUTHENTICATED` Authenticated result.

`DECLINED` Declined result.

### DeferredTiming Class

Represents timing for a transaction that occurs in the future.

Namespace

RichMessaging

IN THIS SECTION:

#### DeferredTiming Constructors

DeferredTiming Properties

#### DeferredTiming Constructors

### The following are constructors for DeferredTiming .

IN THIS SECTION:

##### DeferredTiming(deferredDate)

Creates a new instance of the `RichMessaging.DeferredTiming` class.

DeferredTiming()
Creates a new instance of the `RichMessaging.DeferredTiming` class.

##### **`DeferredTiming(deferredDate)`**

Creates a new instance of the `RichMessaging.DeferredTiming` class.


Apex Reference Guide DeferredTiming Class

Signature

```
   public DeferredTiming(Datetime deferredDate)

```

Parameters

##### _`deferredDate`_

Type: Datetime

The deferred date.

##### **`DeferredTiming()`**

Creates a new instance of the `RichMessaging.DeferredTiming` class.

Signature

```
   public DeferredTiming()

#### DeferredTiming Properties

##### The following are properties for DeferredTiming .

```

IN THIS SECTION:

##### deferredDate

The deferred date. Invocable variable.

##### deferredDateValue

The deferred date. Enabled for Lightning components.

timingType
Always returns “DeferredTiming”.

##### **`deferredDate`**

The deferred date. Invocable variable.

Signature

```
   public Datetime deferredDate {get; set;}

```

Property Value

Type: Datetime

##### **`deferredDateValue`**

The deferred date. Enabled for Lightning components.


### Apex Reference Guide MessageDefinitionInputParameter Class

Signature

```
   public Datetime deferredDateValue {get; set;}

```

Property Value

Type: Datetime

##### **`timingType`**

Always returns “DeferredTiming”.

Signature

```
   public String timingType {get; set;}

```

Property Value

Type: String

### MessageDefinitionInputParameter Class

Represents a messaging component parameter value. This class is used to provide parameter payloads that can be translated to structured
content payloads in rich content messages.

Namespace

RichMessaging

IN THIS SECTION:

#### MessageDefinitionInputParameter Properties MessageDefinitionInputParameter Properties

### The following are properties for MessageDefinitionInputParameter .

IN THIS SECTION:

booleanValue
A boolean input parameter.

booleanValues
A list of boolean parameters.

dateTimeValue
A datetime input parameter.

dateTimeValues
A list of datetime input parameters.


Apex Reference Guide MessageDefinitionInputParameter Class

dateValue
A date input parameter.

dateValues
A list of date input parameters.

name
A name input parameter.

numberValue
A number input parameter.

numberValues
A list of number input parameters.

recordIdValue
A record ID input parameter.

recordIdValues
A list of record ID input parameters.

textValue
A text input parameter.

textValues
A list of text input parameters.

##### **`booleanValue`**

A boolean input parameter.

Signature

```
   public Boolean booleanValue {get; set;}

```

Property Value

Type: Boolean

##### **`booleanValues`**

A list of boolean parameters.

Signature

```
   public List<Boolean> booleanValues {get; set;}

```

Property Value

Type: List on page 3891<Boolean>

##### **`dateTimeValue`**

A datetime input parameter.


Apex Reference Guide MessageDefinitionInputParameter Class

Signature

```
   public Datetime dateTimeValue {get; set;}

```

Property Value

Type: Datetime

##### **`dateTimeValues`**

A list of datetime input parameters.

Signature

```
   public List<Datetime> dateTimeValues {get; set;}

```

Property Value

Type: List on page 3891<Datetime>

##### **`dateValue`**

A date input parameter.

Signature

```
   public Date dateValue {get; set;}

```

Property Value

Type: Date

##### **`dateValues`**

A list of date input parameters.

Signature

```
   public List<Date> dateValues {get; set;}

```

Property Value

Type: List on page 3891<Date>

##### **`name`**

A name input parameter.

Signature

```
   public String name {get; set;}

```


Apex Reference Guide MessageDefinitionInputParameter Class

Property Value

Type: String

##### **`numberValue`**

A number input parameter.

Signature

```
   public Double numberValue {get; set;}

```

Property Value

Type: Double

##### **`numberValues`**

A list of number input parameters.

Signature

```
   public List<Double> numberValues {get; set;}

```

Property Value

Type: List on page 3891<Double>

##### **`recordIdValue`**

A record ID input parameter.

Signature

```
   public String recordIdValue {get; set;}

```

Property Value

Type: String

##### **`recordIdValues`**

A list of record ID input parameters.

Signature

```
   public List<String> recordIdValues {get; set;}

```

Property Value

Type: List on page 3891<String>


### Apex Reference Guide PaymentItemStatus Enum

##### **`textValue`**

A text input parameter.

Signature

```
   public String textValue {get; set;}

```

Property Value

Type: String

##### **`textValues`**

A list of text input parameters.

Signature

```
   public List<String> textValues {get; set;}

```

Property Value

Type: List on page 3891<String>

### PaymentItemStatus Enum

Represents the status of a payment item in payment requests sent in enhanced Messaging channels.

Enum Values

The following are the values of the `RichMessaging.PaymentItemStatus` enum.

**Value** **Description**

`FinalCost` Indicates that the payment item's cost is final and has been determined.

`PendingCost` Indicates that the payment item's cost is pending and has not been determined
yet.

### PaymentLineItem Class

Represents a payment line item in payment requests sent in enhanced Messaging channels.

Namespace

RichMessaging


Apex Reference Guide PaymentLineItem Class

Example

```
   public with sharing class MessagingPaymentLineItems {

      @InvocableMethod

      public static List<List<RichMessaging.PaymentLineItem>> getLineItems() {

        Double amount = 0.25;

        List<List<RichMessaging.PaymentLineItem>> result = new

   List<List<RichMessaging.PaymentLineItem>>();

        RichMessaging.PaymentLineItem pizza = new RichMessaging.PaymentLineItem('pizza',

   amount);

        RichMessaging.PaymentLineItem pasta = new RichMessaging.PaymentLineItem('pasta',

   amount);

        pizza.statusValue = RichMessaging.PaymentItemStatus.FinalCost;

        pasta.statusValue = RichMessaging.PaymentItemStatus.FinalCost;

        List<RichMessaging.PaymentLineItem> options = new

   List<RichMessaging.PaymentLineItem>{

           pizza, pasta

        };

        result.add(options);

        return result;

      }

   }

```

IN THIS SECTION:

#### PaymentLineItem Constructors

PaymentLineItem Properties

PaymentLineItem Methods

#### PaymentLineItem Constructors The following are constructors for PaymentLineItem .

IN THIS SECTION:

##### PaymentLineItem(label, amount, timing)

Creates a new instance of the `RichMessaging.PaymentLineItem` class.

PaymentLineItem(label, amount)
Creates a new instance of the `RichMessaging.PaymentLineItem` class.

PaymentLineItem()
Creates a new instance of the `RichMessaging.PaymentLineItem` class.

##### **`PaymentLineItem(label, amount, timing)`**

Creates a new instance of the `RichMessaging.PaymentLineItem` class.


Apex Reference Guide PaymentLineItem Class

Signature

```
   public PaymentLineItem(String label, Double amount, RichMessaging.AbstractTiming timing)

```

Parameters

```
   label
```

Type: String

The label of the payment line item.

```
   amount
```

Type: Double

The amount of the payment line item.

```
   timing
```

Type: RichMessaging.AbstractTiming

The timing of the payment line item.

##### **`PaymentLineItem(label, amount)`**

Creates a new instance of the `RichMessaging.PaymentLineItem` class.

Signature

```
   public PaymentLineItem(String label, Double amount)

```

Parameters

```
   label
```

Type: String

The label of the payment line item.

```
   amount
```

Type: Double

The amount of the payment line item.

##### **`PaymentLineItem()`**

Creates a new instance of the `RichMessaging.PaymentLineItem` class.

Signature

```
   public PaymentLineItem()

#### PaymentLineItem Properties

##### The following are properties for PaymentLineItem .

```


Apex Reference Guide PaymentLineItem Class

IN THIS SECTION:

##### amount

The amount of the payment line item.

##### amountValue

The amount value of the payment line item.

automaticReloadPaymentThresholdAmount
The automatic reload payment threshold amount of the payment line item.

automaticReloadPaymentThresholdAmountValue
The automatic reload payment threshold amount value of the payment line item.

label
The label of the payment line item.

labelValue
The label value of the payment line item.

lineItemType
The line item type of the payment line item. Read-only variable.

status
The status of the payment line item.

statusValue
The status value of the payment line item.

timing
The timing of the payment line item.

timingValue
The timing value of the payment line item.

##### **`amount`**

The amount of the payment line item.

Signature

```
   public Double amount {get; set;}

```

Property Value

Type: Double

##### **`amountValue`**

The amount value of the payment line item.

Signature

```
   public Double amountValue {get; set;}

```


Apex Reference Guide PaymentLineItem Class

Property Value

Type: Double

##### **`automaticReloadPaymentThresholdAmount`**

The automatic reload payment threshold amount of the payment line item.

Signature

```
   public Double automaticReloadPaymentThresholdAmount {get; set;}

```

Property Value

Type: Double

##### **`automaticReloadPaymentThresholdAmountValue`**

The automatic reload payment threshold amount value of the payment line item.

Signature

```
   public Double automaticReloadPaymentThresholdAmountValue {get; set;}

```

Property Value

Type: Double

##### **`label`**

The label of the payment line item.

Signature

```
   public String label {get; set;}

```

Property Value

Type: String

##### **`labelValue`**

The label value of the payment line item.

Signature

```
   public String labelValue {get; set;}

```

Property Value

Type: String


Apex Reference Guide PaymentLineItem Class

##### **`lineItemType`**

The line item type of the payment line item. Read-only variable.

Signature

```
   public String lineItemType {get; set;}

```

Property Value

Type: String

##### **`status`**

The status of the payment line item.

Signature

```
   public String status {get; set;}

```

Property Value

Type: String

##### **`statusValue`**

The status value of the payment line item.

Signature

```
   public RichMessaging.PaymentItemStatus statusValue {get; set;}

```

Property Value

Type: RichMessaging.PaymentItemStatus

##### **`timing`**

The timing of the payment line item.

Signature

```
   public RichMessaging.AbstractTiming timing {get; set;}

```

Property Value

Type: RichMessaging.AbstractTiming

##### **`timingValue`**

The timing value of the payment line item.


### Apex Reference Guide PaymentMethod Class

Signature

```
   public RichMessaging.AbstractTiming timingValue {get; set;}

```

Property Value

Type: RichMessaging.AbstractTiming

#### PaymentLineItem Methods The following are methods for PaymentLineItem .

### PaymentMethod Class

Represents a payment method.

Namespace

RichMessaging

IN THIS SECTION:

#### PaymentMethod Constructors

PaymentMethod Properties

#### PaymentMethod Constructors

### The following are constructors for PaymentMethod .

IN THIS SECTION:

##### PaymentMethod(network, paymentType, displayName)

Creates a new instance of the `RichMessaging.PaymentMethod` class.

##### **`PaymentMethod(network, paymentType, displayName)`**

Creates a new instance of the `RichMessaging.PaymentMethod` class.

Signature

```
   public PaymentMethod(String network, String paymentType, String displayName)

```

Parameters

```
   network
```

Type: String

The network associated with the payment method.

```
   paymentType
```

Type: String


Apex Reference Guide PaymentMethod Class

The payment type of the payment method.

##### _`displayName`_

Type: String

The display name of the payment method.

#### PaymentMethod Properties The following are properties for PaymentMethod .

IN THIS SECTION:

##### displayName

The display name of the payment method.

##### network

The network associated with the payment method.

##### paymentType

The payment type of the payment method.

##### **`displayName`**

The display name of the payment method.

Signature

```
   public String displayName {get; set;}

```

Property Value

Type: String

##### **`network`**

The network associated with the payment method.

Signature

```
   public String network {get; set;}

```

Property Value

Type: String

##### **`paymentType`**

The payment type of the payment method.

Signature

```
   public String paymentType {get; set;}

```


### Apex Reference Guide PostalAddress Class

Property Value

Type: String

### PostalAddress Class

Represents the postal address.

Namespace

RichMessaging

IN THIS SECTION:

#### PostalAddress Constructors

PostalAddress Properties

#### PostalAddress Constructors

### The following are constructors for PostalAddress .

IN THIS SECTION:

##### PostalAddress(addressLines, subLocality, locality, postalCode, subAdministrativeArea, administrativeArea, country, countryCode)

Creates a new instance of the `RichMessaging.PostalAddress` class.

##### **`PostalAddress(addressLines, subLocality, locality, postalCode,`**

```
  subAdministrativeArea, administrativeArea, country, countryCode)

```

Creates a new instance of the `RichMessaging.PostalAddress` class.

Signature

```
   public PostalAddress(List<String> addressLines, String subLocality, String locality,

   String postalCode, String subAdministrativeArea, String administrativeArea, String

   country, String countryCode)

```

Parameters

```
   addressLines
```

Type: List<String>

The street address.

```
   subLocality
```

Type: String

The sub-locality of the address.

```
   locality
```

Type: String

The locality of the address.


Apex Reference Guide PostalAddress Class

```
   postalCode
```

Type: String

The postal code.

```
   subAdministrativeArea
```

Type: String

The sub-administrative area.

```
   administrativeArea
```

Type: String

The administrative area.

```
   country
```

Type: String

The country.

```
   countryCode
```

Type: String

The country code.

#### PostalAddress Properties The following are properties for PostalAddress .

IN THIS SECTION:

##### addressLines

The street address.

administrativeArea
The administrative area.

country
The country.

countryCode
The country code.

locality
The locality of the address.

postalCode
The postal code.

subAdministrativeArea
The sub-administrative area.

subLocality
The sub-locality of the address.

##### **`addressLines`**

The street address.


Apex Reference Guide PostalAddress Class

Signature

```
   public List<String> addressLines {get; set;}

```

Property Value

Type: List<String>

##### **`administrativeArea`**

The administrative area.

Signature

```
   public String administrativeArea {get; set;}

```

Property Value

Type: String

##### **`country`**

The country.

Signature

```
   public String country {get; set;}

```

Property Value

Type: String

##### **`countryCode`**

The country code.

Signature

```
   public String countryCode {get; set;}

```

Property Value

Type: String

##### **`locality`**

The locality of the address.

Signature

```
   public String locality {get; set;}

```


### Apex Reference Guide ProcessFormHandler Interface

Property Value

Type: String

##### **`postalCode`**

The postal code.

Signature

```
   public String postalCode {get; set;}

```

Property Value

Type: String

##### **`subAdministrativeArea`**

The sub-administrative area.

Signature

```
   public String subAdministrativeArea {get; set;}

```

Property Value

Type: String

##### **`subLocality`**

The sub-locality of the address.

Signature

```
   public String subLocality {get; set;}

```

Property Value

Type: String

### ProcessFormHandler Interface

Apex interface that processes the responses to forms submitted in a messaging session.

Namespace

RichMessaging

IN THIS SECTION:

ProcessFormHandler Methods


Apex Reference Guide ProcessFormHandler Interface

#### ProcessFormHandler Methods The following are methods for ProcessFormHandler .

IN THIS SECTION:

##### processFormRequest

Processes the form request and returns the ID of the record created during form processing.

##### **`processFormRequest`**

Processes the form request and returns the ID of the record created during form processing.

Signature

```
   ID processFormRequest(RichMessaging.ProcessFormResponse formResponse)

```

Parameters

```
   formResponse
```

Type: RichMessaging.ProcessFormResponse

The form response.

Return Value

```
   ID
```

Type: RichMessaging.ProcessFormResponse

ProcessFormHandler Example Implementation

The sample `ContactApexFormHandler` Apex class automatically captures the customer's submitted details, creates a Contact
record in Salesforce, and returns the Contact record ID.

This is an example implementation of the `RichMessaging.ProcessFormHandler` interface.

```
   global class ContactApexFormHandler implements Richmessaging.ProcessFormHandler{

      global ID

##### `processFormRequest(RichMessaging.ProcessFormResponse formResponse) {`

        // Create a new Contact object

           Contact newContact = new Contact(

           Phone = formResponse.formValues.get('Phone'),

           Salutation = formResponse.formValues.get('Salutation'),

           Email = formResponse.formValues.get('Email')

           );

      // Insert the new contact into the database

      insert newContact;

      // Return the ID of the newly created contact

      return newContact.Id;

```

[For more information, see "Create a Form Based on an Apex Class" in this help topic.](https://help.salesforce.com/s/articleView?id=service.messaging_components_forms.htm&language=en_US)


### Apex Reference Guide ProcessPaymentHandler Interface ProcessPaymentHandler Interface

Interface used to process payment requests.

Namespace

RichMessaging

IN THIS SECTION:

#### ProcessPaymentHandler Methods ProcessPaymentHandler Example Implementation ProcessPaymentHandler Methods

### The following are methods for ProcessPaymentHandler .

IN THIS SECTION:

##### processPaymentRequest(var1)

Processes a payment request.

##### **`processPaymentRequest(var1)`**

Processes a payment request.

Signature

```
   public RichMessaging.ProcessPaymentResult

   processPaymentRequest(RichMessaging.ProcessPaymentRequest var1)

```

Parameters

```
   var1
```

Type: RichMessaging.ProcessPaymentRequest

The payment request.

Return Value

Type: RichMessaging.ProcessPaymentResult

#### ProcessPaymentHandler Example Implementation

This is an example implementation of the `RichMessaging.ProcessPaymentHandler` interface.

```
   global class MyProcessPaymentHandler implements Richmessaging.ProcessPaymentHandler {

     global RichMessaging.ProcessPaymentResult

   processPaymentRequest(RichMessaging.ProcessPaymentRequest paymentRequest) {

```


### Apex Reference Guide ProcessPaymentRequest Class

```
        // TODO: Reach out to your payment processor here and return success or failure

   based on the result of that request

        return new

   RichMessaging.ProcessPaymentResult(RichMessaging.ProcessPaymentResultStatus.SUCCESS);

     }

   }

### ProcessPaymentRequest Class

```

Represents a request to process a payment.

Namespace

RichMessaging

IN THIS SECTION:

#### ProcessPaymentRequest Constructors

ProcessPaymentRequest Properties

#### ProcessPaymentRequest Constructors

### The following are constructors for ProcessPaymentRequest .

IN THIS SECTION:

##### ProcessPaymentRequest(transactionIdentifier, paymentData, billingContact, shippingContact, paymentMethod, shippingMethod,

contextRecordId)
Creates a new instance of the `RichMessaging.ProcessPaymentRequest` class.

##### **`ProcessPaymentRequest(transactionIdentifier, paymentData, billingContact,`**

```
  shippingContact, paymentMethod, shippingMethod, contextRecordId)

```

Creates a new instance of the `RichMessaging.ProcessPaymentRequest` class.

Signature

```
   public ProcessPaymentRequest(String transactionIdentifier, String paymentData,

   RichMessaging.AddressableContact billingContact, RichMessaging.AddressableContact

   shippingContact, RichMessaging.PaymentMethod paymentMethod, RichMessaging.ShippingMethod

   shippingMethod, String contextRecordId)

```

Parameters

```
   transactionIdentifier
```

Type: String

The transaction identifier associated with the payment request.


Apex Reference Guide ProcessPaymentRequest Class

```
   paymentData
```

Type: String

The encrypted payment data for the payment request.

```
   billingContact
```

Type: RichMessaging.AddressableContact

The billing contact information for the payment request.

```
   shippingContact
```

Type: RichMessaging.AddressableContact

The shipping contact information for the payment request.

```
   paymentMethod
```

Type: RichMessaging.PaymentMethod

The payment method for the payment request.

```
   shippingMethod
```

Type: RichMessaging.ShippingMethod

The shipping method for the payment request.

```
   contextRecordId
```

Type: String

The context record ID associated with the payment request.

#### ProcessPaymentRequest Properties The following are properties for ProcessPaymentRequest .

IN THIS SECTION:

billingContact
The billing contact information for the payment request.

contextRecordId
The context record ID associated with the payment request.

paymentData
The encrypted payment data for the payment request.

paymentMethod
The payment method for the payment request.

shippingContact
The shipping contact information for the payment request.

shippingMethod
The shipping method for the payment request.

transactionIdentifier
The transaction identifier associated with the payment request.


Apex Reference Guide ProcessPaymentRequest Class

##### **`billingContact`**

The billing contact information for the payment request.

Signature

```
   public RichMessaging.AddressableContact billingContact {get; set;}

```

Property Value

Type: RichMessaging.AddressableContact

##### **`contextRecordId`**

The context record ID associated with the payment request.

Signature

```
   public String contextRecordId {get; set;}

```

Property Value

Type: String

##### **`paymentData`**

The encrypted payment data for the payment request.

Signature

```
   public String paymentData {get; set;}

```

Property Value

Type: String

##### **`paymentMethod`**

The payment method for the payment request.

Signature

```
   public RichMessaging.PaymentMethod paymentMethod {get; set;}

```

Property Value

Type: RichMessaging.PaymentMethod

##### **`shippingContact`**

The shipping contact information for the payment request.


### Apex Reference Guide ProcessPaymentResult Class

Signature

```
   public RichMessaging.AddressableContact shippingContact {get; set;}

```

Property Value

Type: RichMessaging.AddressableContact

##### **`shippingMethod`**

The shipping method for the payment request.

Signature

```
   public RichMessaging.ShippingMethod shippingMethod {get; set;}

```

Property Value

Type: RichMessaging.ShippingMethod

##### **`transactionIdentifier`**

The transaction identifier associated with the payment request.

Signature

```
   public String transactionIdentifier {get; set;}

```

Property Value

Type: String

### ProcessPaymentResult Class

Represents the result of a payment processing operation.

Namespace

RichMessaging

IN THIS SECTION:

#### ProcessPaymentResult Constructors

ProcessPaymentResult Properties

#### ProcessPaymentResult Constructors

### The following are constructors for ProcessPaymentResult .


Apex Reference Guide ProcessPaymentResult Class

IN THIS SECTION:

##### ProcessPaymentResult(resultStatus, errorMessage)

Creates a new instance of the `RichMessaging.ProcessPaymentResult` class.

##### ProcessPaymentResult(resultStatus)

Creates a new instance of the `RichMessaging.ProcessPaymentResult` class.

##### **`ProcessPaymentResult(resultStatus, errorMessage)`**

Creates a new instance of the `RichMessaging.ProcessPaymentResult` class.

Signature

```
   public ProcessPaymentResult(RichMessaging.ProcessPaymentResultStatus resultStatus,

   String errorMessage)

```

Parameters

```
   resultStatus
```

Type: RichMessaging.ProcessPaymentResultStatus

The status of the payment processing result.

```
   errorMessage
```

Type: String

The error message associated with the payment processing result, if any.

##### **`ProcessPaymentResult(resultStatus)`**

Creates a new instance of the `RichMessaging.ProcessPaymentResult` class.

Signature

```
   public ProcessPaymentResult(RichMessaging.ProcessPaymentResultStatus resultStatus)

```

Parameters

```
   resultStatus
```

Type: RichMessaging.ProcessPaymentResultStatus

The status of the payment processing result.

#### ProcessPaymentResult Properties

##### The following are properties for ProcessPaymentResult .

IN THIS SECTION:

errorMessage
The error message associated with the payment processing result, if any.


### Apex Reference Guide ProcessPaymentResultStatus Enum

##### resultStatus

The status of the payment processing result.

##### **`errorMessage`**

The error message associated with the payment processing result, if any.

Signature

```
   public String errorMessage {get; set;}

```

Property Value

Type: String

##### **`resultStatus`**

The status of the payment processing result.

Signature

```
   public RichMessaging.ProcessPaymentResultStatus resultStatus {get; set;}

```

Property Value

Type: RichMessaging.ProcessPaymentResultStatus

### ProcessPaymentResultStatus Enum

Represents the status of a payment processing result.

Enum Values

The following are the values of the `RichMessaging.ProcessPaymentResultStatus` enum.

**Value** **Description**

`PROCESSOR_ERROR` Indicates an error occurred during payment processing at the processor level.

`SUCCESS` Indicates a successful payment processing result.

### RecurringTiming Class

Represents a payment that occurs on a regular basis.

Namespace

RichMessaging


Apex Reference Guide RecurringTiming Class

IN THIS SECTION:

#### RecurringTiming Constructors

RecurringTiming Properties

#### RecurringTiming Constructors The following are constructors for RecurringTiming .

IN THIS SECTION:

##### RecurringTiming(startDate, endDate, intervalCount, intervalUnit)

Creates a new instance of the `RichMessaging.RecurringTiming` class.

##### RecurringTiming()

Creates a new instance of the `RichMessaging.RecurringTiming` class.

##### **`RecurringTiming(startDate, endDate, intervalCount, intervalUnit)`**

Creates a new instance of the `RichMessaging.RecurringTiming` class.

Signature

```
   public RecurringTiming(Date startDate, Date endDate, Integer intervalCount,

   RichMessaging.TimingIntervalUnit intervalUnit)

```

Parameters

```
   startDate
```

Type: Date

The start date. Invocable variable.

```
   endDate
```

Type: Date

The end date. Invocable variable.

```
   intervalCount
```

Type: Integer

The number of interval units that make up the total payment interval. Invocable variable.

```
   intervalUnit
```

Type: RichMessaging.TimingIntervalUnit

The amount of time—in calendar units, such as day, month, or year—that represents a fraction of the total payment interval.
Invocable variable.

##### **`RecurringTiming()`**

Creates a new instance of the `RichMessaging.RecurringTiming` class.


Apex Reference Guide RecurringTiming Class

Signature

```
   public RecurringTiming()

#### RecurringTiming Properties The following are properties for RecurringTiming .

```

IN THIS SECTION:

##### endDate

The end date. Invocable variable.

##### endDateValue

The end date. Enabled for Lightning components.

intervalCount
The number of interval units that make up the total payment interval. Invocable variable.

intervalCountValue
The number of interval units that make up the total payment interval. Enabled for Lightning components.

intervalUnit
The amount of time—in calendar units, such as day, month, or year—that represents a fraction of the total payment interval.
Invocable variable.

intervalUnitValue
The amount of time—in calendar units, such as day, month, or year—that represents a fraction of the total payment interval. Enabled
for Lightning components.

startDate
The start date. Invocable variable.

startDateValue
The start date. Enabled for Lightning components.

timingType
Always returns “RecurringTiming”.

##### **`endDate`**

The end date. Invocable variable.

Signature

```
   public Date endDate {get; set;}

```

Property Value

Type: Date

##### **`endDateValue`**

The end date. Enabled for Lightning components.


Apex Reference Guide RecurringTiming Class

Signature

```
   public Date endDateValue {get; set;}

```

Property Value

Type: Date

##### **`intervalCount`**

The number of interval units that make up the total payment interval. Invocable variable.

Signature

```
   public Integer intervalCount {get; set;}

```

Property Value

Type: Integer

##### **`intervalCountValue`**

The number of interval units that make up the total payment interval. Enabled for Lightning components.

Signature

```
   public Integer intervalCountValue {get; set;}

```

Property Value

Type: Integer

##### **`intervalUnit`**

The amount of time—in calendar units, such as day, month, or year—that represents a fraction of the total payment interval. Invocable
variable.

Signature

```
   public String intervalUnit {get; set;}

```

Property Value

Type: String

##### **`intervalUnitValue`**

The amount of time—in calendar units, such as day, month, or year—that represents a fraction of the total payment interval. Enabled
for Lightning components.


### Apex Reference Guide ShippingMethod Class

Signature

```
   public RichMessaging.TimingIntervalUnit intervalUnitValue {get; set;}

```

Property Value

Type: RichMessaging.TimingIntervalUnit

##### **`startDate`**

The start date. Invocable variable.

Signature

```
   public Date startDate {get; set;}

```

Property Value

Type: Date

##### **`startDateValue`**

The start date. Enabled for Lightning components.

Signature

```
   public Date startDateValue {get; set;}

```

Property Value

Type: Date

##### **`timingType`**

Always returns “RecurringTiming”.

Signature

```
   public String timingType {get; set;}

```

Property Value

Type: String

### ShippingMethod Class

Represents a shipping method listed in payment requests sent in enhanced Messaging channels.

Namespace

RichMessaging


Apex Reference Guide ShippingMethod Class

Example

```
   public with sharing class MessagingShippingMethods {

      @InvocableMethod

      public static List<List<RichMessaging.ShippingMethod>> getShippingMethods(){

        Double amount = 0.25;

        List<List<RichMessaging.ShippingMethod>> result = new

   List<List<RichMessaging.ShippingMethod>>();

       List<RichMessaging.ShippingMethod> options = new List<RichMessaging.ShippingMethod>{

          new RichMessaging.ShippingMethod('doordash', amount, '1 hour delivery to your

    door', 'ddash'),

           new RichMessaging.ShippingMethod('UPS', amount, '2 days delivery', 'UPS')

        };

        result.add(options);

        return result;

      }

   }

```

IN THIS SECTION:

#### ShippingMethod Constructors

ShippingMethod Properties

#### ShippingMethod Constructors The following are constructors for ShippingMethod .

IN THIS SECTION:

##### ShippingMethod(label, amount, detail, identifier)

Creates a new instance of the `RichMessaging.ShippingMethod` class.

ShippingMethod()
Creates a new instance of the `RichMessaging.ShippingMethod` class.

##### **`ShippingMethod(label, amount, detail, identifier)`**

Creates a new instance of the `RichMessaging.ShippingMethod` class.

Signature

```
   public ShippingMethod(String label, Double amount, String detail, String identifier)

```

Parameters

```
   label
```

Type: String


Apex Reference Guide ShippingMethod Class

The label of the shipping method.

```
   amount
```

Type: Double

The amount of the shipping method.

```
   detail
```

Type: String

Details about the shipping method.

```
   identifier
```

Type: String

The identifier of the shipping method.

##### **`ShippingMethod()`**

Creates a new instance of the `RichMessaging.ShippingMethod` class.

Signature

```
   public ShippingMethod()

#### ShippingMethod Properties

##### The following are properties for ShippingMethod .

```

IN THIS SECTION:

amount
The amount of the shipping method.

amountValue
The amount value of the shipping method.

detail
Details about the shipping method.

detailValue
The detail value of the shipping method.

identifier
The identifier of the shipping method.

identifierValue
The identifier value of the shipping method.

label
The label of the shipping method.

labelValue
The label value of the shipping method.

shippingMethodType
The shipping method type. Read only.


Apex Reference Guide ShippingMethod Class

##### **`amount`**

The amount of the shipping method.

Signature

```
   public Double amount {get; set;}

```

Property Value

Type: Double

##### **`amountValue`**

The amount value of the shipping method.

Signature

```
   public Double amountValue {get; set;}

```

Property Value

Type: Double

##### **`detail`**

Details about the shipping method.

Signature

```
   public String detail {get; set;}

```

Property Value

Type: String

##### **`detailValue`**

The detail value of the shipping method.

Signature

```
   public String detailValue {get; set;}

```

Property Value

Type: String

##### **`identifier`**

The identifier of the shipping method.


Apex Reference Guide ShippingMethod Class

Signature

```
   public String identifier {get; set;}

```

Property Value

Type: String

##### **`identifierValue`**

The identifier value of the shipping method.

Signature

```
   public String identifierValue {get; set;}

```

Property Value

Type: String

##### **`label`**

The label of the shipping method.

Signature

```
   public String label {get; set;}

```

Property Value

Type: String

##### **`labelValue`**

The label value of the shipping method.

Signature

```
   public String labelValue {get; set;}

```

Property Value

Type: String

##### **`shippingMethodType`**

The shipping method type. Read only.

Signature

```
   public String shippingMethodType {get; set;}

```


### Apex Reference Guide TimeSlotOption Class

Property Value

Type: String

### TimeSlotOption Class

Represents a complex time slot option type. This class is used to provide time option payloads that can be translated to structured
content payloads in rich content messages.

Namespace

RichMessaging

IN THIS SECTION:

#### TimeSlotOption Constructors

TimeSlotOption Properties

#### TimeSlotOption Constructors

### The following are constructors for TimeSlotOption .

IN THIS SECTION:

##### TimeSlotOption(startTime, endTime)
### Creates a TimeSlotOption object with a start and end time.

TimeSlotOption(startTime, duration)
### Creates a TimeSlotOption object with a start time and a duration.

TimeSlotOption()
### Creates a TimeSlotOption object.

##### **`TimeSlotOption(startTime, endTime)`**

### Creates a TimeSlotOption object with a start and end time.

Signature

```
   public TimeSlotOption(Datetime startTime, Datetime endTime)

```

Parameters

```
   startTime
```

Type: Datetime

Start time.

```
   endTime
```

Type: Datetime

End time.


Apex Reference Guide TimeSlotOption Class

##### **`TimeSlotOption(startTime, duration)`** Creates a TimeSlotOption object with a start time and a duration.

Signature

```
   public TimeSlotOption(Datetime startTime, Integer duration)

```

Parameters

```
   startTime
```

Type: Datetime

Start time.

##### _`duration`_

Type: Integer

Duration in seconds.

##### **`TimeSlotOption()`** Creates a TimeSlotOption object.

Signature

```
   public TimeSlotOption()

#### TimeSlotOption Properties

##### The following are properties for TimeSlotOption .

```

IN THIS SECTION:

##### duration

The duration in seconds.

##### durationValue

The duration in seconds. Enabled for Lightning components.

endTimeValue
The end time. Enabled for Lightning components.

startTime
The start time.

startTimeValue
The start time. Enabled for Lightning components.

##### **`duration`**

The duration in seconds.


Apex Reference Guide TimeSlotOption Class

Signature

```
   public Integer duration {get; set;}

```

Property Value

Type: Integer

##### **`durationValue`**

The duration in seconds. Enabled for Lightning components.

Signature

```
   public Integer durationValue {get; set;}

```

Property Value

Type: Integer

##### **`endTimeValue`**

The end time. Enabled for Lightning components.

Signature

```
   public Datetime endTimeValue {get; set;}

```

Property Value

Type: Datetime

##### **`startTime`**

The start time.

Signature

```
   public Datetime startTime {get; set;}

```

Property Value

Type: Datetime

##### **`startTimeValue`**

The start time. Enabled for Lightning components.

Signature

```
   public Datetime startTimeValue {get; set;}

```


### Apex Reference Guide TimingIntervalUnit Enum

Property Value

Type: Datetime

### TimingIntervalUnit Enum

Represents an enumerated type that describes the timing interval.

Enum Values

The following are the values of the `RichMessaging.TimingIntervalUnit` enum.

**Value** **Description**

`Day` Day interval.

`Hour` Hour interval.

`Minute` Minute interval.

`Month` Month interval.

`Year` Year interval.

### TimingType Enum

Represents an enumerated type that describes the type of timing.

Enum Values

The following are the values of the `RichMessaging.TimingType` enum.

**Value** **Description**

`DeferredTiming` Indicates that the timing is deferred. See DeferredTiming Class.

`RecurringTiming` Indicates that the timing recurs. See RecurringTiming Class.

## RulesAppln Namespace

The RulesAppln namespace contains output classes that store details about a rules-based application of payments and credits.

[The rules are applied by using the applyPaymentsAndCreditsByRules invocable action. See Apply Payments and Credits by Rules Action](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/actions_obj_apply_rules.htm)
in the _Revenue Cloud Developer Guide_ .

## The RulesAppln namespace includes these classes.

**•** [RulesApplicationResponse Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RulesAppln_RulesApplicationResponse.htm)

**•** [RulesApplicationSummaryResponse Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RulesAppln_RulesApplicationSummaryResponse.htm)

**•** [RulesApplicationErrorResponse Class](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/apex_class_RulesAppln_RulesApplicationErrorResponse.htm)


## Apex Reference Guide runtime_industries_insurance Namespace runtime_industries_insurance Namespace The runtime_industries_insurance namespace provides options classes for insurance operations, such as creating and

updating insurance quotes, generating insurance clauses, and running insurance rating.

## The runtime_industries_insurance namespace includes these classes.

**•** [AddEligibleInsuranceClausesOptions](https://developer.salesforce.com/docs/atlas.en-us.260.0.insurance_developer_guide.meta/insurance_developer_guide/apex_class_runtime_industries_insurance_AddEligibleInsuranceClausesOptions.htm)

**•** [CreateInsuranceQuoteOptions](https://developer.salesforce.com/docs/atlas.en-us.260.0.insurance_developer_guide.meta/insurance_developer_guide/apex_class_runtime_industries_insurance_CreateInsuranceQuoteOptions.htm)

**•** [CreateInsuranceRatingOptions](https://developer.salesforce.com/docs/atlas.en-us.260.0.insurance_developer_guide.meta/insurance_developer_guide/apex_class_runtime_industries_insurance_CreateInsuranceRatingOptions.htm)

**•** [GenerateInsuranceClausesOptions](https://developer.salesforce.com/docs/atlas.en-us.260.0.insurance_developer_guide.meta/insurance_developer_guide/apex_class_runtime_industries_insurance_GenerateInsuranceClauseOptions.htm)

**•** [UpdateInsuranceQuoteOptions](https://developer.salesforce.com/docs/atlas.en-us.260.0.insurance_developer_guide.meta/insurance_developer_guide/apex_class_runtime_industries_insurance_UpdateInsuranceQuoteOptions.htm)

## Schema Namespace The Schema namespace provides classes and methods for schema metadata information. The following are the classes in the Schema namespace.

IN THIS SECTION:

ChildRelationship Class
Contains methods for accessing the child relationship as well as the child sObject for a parent sObject.

DataCategory Class
Represents the categories within a category group.

DataCategoryGroupSobjectTypePair Class
Specifies a category group and an associated object.

DescribeColorResult Class
Contains color metadata information for a tab.

DescribeDataCategoryGroupResult Class
Contains the list of the category groups associated with KnowledgeArticleVersion and Question.

DescribeDataCategoryGroupStructureResult Class
Contains the category groups and categories associated with KnowledgeArticleVersion and Question.

DescribeFieldResult Class
Contains methods for describing sObject fields.

DescribeIconResult Class
Contains icon metadata information for a tab.

DescribeSObjectResult Class
Contains methods for describing SObjects. None of the methods take an argument.

DescribeTabResult Class
Contains tab metadata information for a tab in a standard or custom app available in the Salesforce user interface.

DescribeTabSetResult Class
Contains metadata information about a Salesforce Classic standard or custom app available in the Salesforce user interface.


### Apex Reference Guide ChildRelationship Class

DisplayType Enum
A `Schema.DisplayType` enum value is returned by the field describe result's `getType` method.

FieldDescribeOptions Enum
A `Schema.FieldDescribeOptions` enum value is a parameter in the `SObjectType.getDescribe` method.

FieldSet Class
Contains methods for discovering and retrieving the details of field sets created on sObjects.

FieldSetMember Class
Contains methods for accessing the metadata for field set member fields.

PicklistEntry Class
Represents a picklist entry.

RecordTypeInfo Class
Contains methods for accessing record type information for an sObject with associated record types.

SOAPType Enum
A `Schema.SOAPType` enum value is returned by the field describe result `getSoapType` method.

SObjectDescribeOptions Enum
A `Schema.SObjectDescribeOptions` enum value is a parameter in the `SObjectType.getDescribe` method.

SObjectField Class
A `Schema.sObjectField` object is returned from the field describe result using the `getController` and
`getSObjectField` methods.

SObjectType Class
A `Schema.sObjectType` object is returned from the field describe result using the `getReferenceTo` method, or from
the sObject describe result using the `getSObjectType` method.

### ChildRelationship Class

Contains methods for accessing the child relationship as well as the child sObject for a parent sObject.

Namespace

Schema

Example

A ChildRelationship object is returned from the sObject describe result using the `getChildRelationship` method. For example:

```
   Schema.DescribeSObjectResult R = Account.SObjectType.getDescribe();

   List<Schema.ChildRelationship> C = R.getChildRelationships();

#### ChildRelationship Methods

### The following are methods for ChildRelationship . All are instance methods.

```


Apex Reference Guide ChildRelationship Class

IN THIS SECTION:

##### getChildSObject()

Returns the token of the child sObject on which there is a foreign key back to the parent sObject.

##### getField()

Returns the token of the field that has a foreign key back to the parent sObject.

##### getRelationshipName()

Returns the name of the relationship.

isCascadeDelete()
Returns `true` if the child object is deleted when the parent object is deleted, `false` otherwise.

isDeprecatedAndHidden()
Reserved for future use.

isRestrictedDelete()
Returns `true` if the parent object can't be deleted because it is referenced by a child object, `false` otherwise.

##### getChildSObject()

Returns the token of the child sObject on which there is a foreign key back to the parent sObject.

Signature

```
   public Schema.SObjectType getChildSObject()

```

Return Value

Type: Schema.SObjectType

##### getField()

Returns the token of the field that has a foreign key back to the parent sObject.

Signature

```
   public Schema.SObjectField getField()

```

Return Value

Type: Schema.SObjectField

##### getRelationshipName()

Returns the name of the relationship.

Signature

```
   public String getRelationshipName()

```


### Apex Reference Guide DataCategory Class

Return Value

Type: String

##### isCascadeDelete()

Returns `true` if the child object is deleted when the parent object is deleted, `false` otherwise.

Signature

```
   public Boolean isCascadeDelete()

```

Return Value

Type: Boolean

##### isDeprecatedAndHidden()

Reserved for future use.

Signature

```
   public Boolean isDeprecatedAndHidden()

```

Return Value

Type: Boolean

##### isRestrictedDelete()

Returns `true` if the parent object can't be deleted because it is referenced by a child object, `false` otherwise.

Signature

```
   public Boolean isRestrictedDelete()

```

Return Value

Type: Boolean

### DataCategory Class

Represents the categories within a category group.

Namespace

Schema


Apex Reference Guide DataCategory Class

Usage

The `Schema.DataCategory` object is returned by the `getTopCategories` method.

#### DataCategory Methods The following are methods for DataCategory . All are instance methods.

IN THIS SECTION:

##### getChildCategories()

Returns a recursive object that contains the visible sub categories in the data category.

##### getLabel()

Returns the label for the data category used in the Salesforce user interface.

##### getName()

Returns the unique name used by the API to access to the data category.

##### getChildCategories()

Returns a recursive object that contains the visible sub categories in the data category.

Signature

```
   public Schema.DataCategory getChildCategories()

```

Return Value

Type: List<Schema.DataCategory>

##### getLabel()

Returns the label for the data category used in the Salesforce user interface.

Signature

```
   public String getLabel()

```

Return Value

Type: String

##### getName()

Returns the unique name used by the API to access to the data category.

Signature

```
   public String getName()

```


### Apex Reference Guide DataCategoryGroupSobjectTypePair Class

Return Value

Type: String

### DataCategoryGroupSobjectTypePair Class

Specifies a category group and an associated object.

Namespace

Schema

Usage

Schema.DataCategoryGroupSobjectTypePair is used by the `describeDataCategory GroupStructures` method to return
the categories available to this object.

IN THIS SECTION:

#### DataCategoryGroupSobjectTypePair Constructors DataCategoryGroupSobjectTypePair Methods DataCategoryGroupSobjectTypePair Constructors

### The following are constructors for DataCategoryGroupSobjectTypePair .

IN THIS SECTION:

##### DataCategoryGroupSobjectTypePair()

Creates a new instance of the `Schema.DataCategoryGroupSobjectTypePair` class.

##### DataCategoryGroupSobjectTypePair()

Creates a new instance of the `Schema.DataCategoryGroupSobjectTypePair` class.

Signature

```
   public DataCategoryGroupSobjectTypePair()

#### DataCategoryGroupSobjectTypePair Methods

### The following are methods for DataCategoryGroupSobjectTypePair . All are instance methods.

```

IN THIS SECTION:

getDataCategoryGroupName()
Returns the unique name used by the API to access the data category group.

getSobject()
Returns the object name associated with the data category group.


Apex Reference Guide DataCategoryGroupSobjectTypePair Class

##### setDataCategoryGroupName(name)

Specifies the unique name used by the API to access the data category group.

##### setSobject(sObjectName)

Sets the sObject associated with the data category group.

##### getDataCategoryGroupName()

Returns the unique name used by the API to access the data category group.

Signature

```
   public String getDataCategoryGroupName()

```

Return Value

Type: String

##### getSobject()

Returns the object name associated with the data category group.

Signature

```
   public String getSobject()

```

Return Value

Type: String

##### setDataCategoryGroupName(name)

Specifies the unique name used by the API to access the data category group.

Signature

```
   public String setDataCategoryGroupName(String name)

```

Parameters

**name**
Type: String

Return Value

Type: Void

##### setSobject(sObjectName)

Sets the sObject associated with the data category group.


### Apex Reference Guide DescribeColorResult Class

Signature

```
   public Void setSobject(String sObjectName)

```

Parameters

```
   sObjectName
```

Type: String

The _`sObjectName`_ is the object name associated with the data category group. Valid values are:

**•** `KnowledgeArticleVersion` —for article types.

**•** `Question` —for questions from Answers.

Return Value

Type: Void

### DescribeColorResult Class

Contains color metadata information for a tab.

Namespace

Schema

Usage

The `getColors` method of the `Schema.DescribeTabResult` class returns a list of `Schema.DescribeColorResult`
objects that describe colors used in a tab.

The methods in the `Schema.DescribeColorResult` class can be called using their property counterparts. For each method
starting with `get`, you can omit the `get` prefix and the ending parentheses `()` to call the property counterpart. For example,
`colorResultObj.color` is equivalent to `colorResultObj.getColor()` .

Example

This sample shows how to get the color information in the Sales app for the first tab’s first color.

```
   // Get tab set describes for each app

   List<Schema.DescribeTabSetResult> tabSetDesc = Schema.DescribeTabs();

   // Iterate through each tab set describe for each app and display the info

   for(Schema.DescribeTabSetResult tsr : tabSetDesc) {

      // Display tab info for the Sales app

      if (tsr.getLabel() == 'Sales') {

        // Get color information for the first tab

        List<Schema.DescribeColorResult> colorDesc = tsr.getTabs()[0].getColors();

        // Display the icon color, theme, and context of the first color returned

        System.debug('Color: ' + colorDesc[0].getColor());

        System.debug('Theme: ' + colorDesc[0].getTheme());

        System.debug('Context: ' + colorDesc[0].getContext());

      }

```


Apex Reference Guide DescribeColorResult Class

```
   }

   // Example debug statement output

   // DEBUG|Color: 1797C0

   // DEBUG|Theme: theme4

   // DEBUG|Context: primary

#### DescribeColorResult Methods The following are methods for DescribeColorResult . All are instance methods.

```

IN THIS SECTION:

##### getColor()

Returns the Web RGB color code, such as `00FF00` .

##### getContext()

Returns the color context. The context determines whether the color is the main color for the tab or not.

##### getTheme()

Returns the color theme.

##### getColor()

Returns the Web RGB color code, such as `00FF00` .

Signature

```
   public String getColor()

```

Return Value

Type: String

##### getContext()

Returns the color context. The context determines whether the color is the main color for the tab or not.

Signature

```
   public String getContext()

```

Return Value

Type: String

##### getTheme()

Returns the color theme.


Apex Reference Guide DescribeDataCategoryGroupResult Class

Signature

```
   public String getTheme()

```

Return Value

Type: String

Possible theme values include `theme3`, `theme4`, and `custom` .

**•** `theme3` is the Salesforce theme introduced during Spring ‘10.

**•** `theme4` is the Salesforce theme introduced in Winter ‘14 for the mobile touchscreen version of Salesforce.

**•** `custom` is the theme name associated with a custom icon.

DescribeDataCategoryGroupResult Class

Contains the list of the category groups associated with KnowledgeArticleVersion and Question.

Namespace

Schema

Usage

The `describeDataCategoryGroups` method returns a `Schema.DescribeDataCategoryGroupResult` object
containing the list of the category groups associated with the specified object.

For additional information and code examples using `describeDataCategoryGroups` [, see Accessing All Data Categories](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_data_categories.htm)
[Associated with an sObject.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_data_categories.htm)

Example

The following is an example of how to instantiate a data category group describe result object:

```
   List <String> objType = new List<String>();

   objType.add('KnowledgeArticleVersion');

   objType.add('Question');

   List<Schema.DescribeDataCategoryGroupResult> describeCategoryResult =

     Schema.describeDataCategoryGroups(objType);

#### DescribeDataCategoryGroupResult Methods The following are methods for DescribeDataCategoryGroupResult . All are instance methods.

```

IN THIS SECTION:

getCategoryCount()
Returns the number of visible data categories in the data category group.

getDescription()
Returns the description of the data category group.


Apex Reference Guide DescribeDataCategoryGroupResult Class

##### getLabel()

Returns the label for the data category group used in the Salesforce user interface.

##### getName()

Returns the unique name used by the API to access to the data category group.

getSobject()
Returns the object name associated with the data category group.

##### getCategoryCount()

Returns the number of visible data categories in the data category group.

Signature

```
   public Integer getCategoryCount()

```

Return Value

Type: Integer

##### getDescription()

Returns the description of the data category group.

Signature

```
   public String getDescription()

```

Return Value

Type: String

##### getLabel()

Returns the label for the data category group used in the Salesforce user interface.

Signature

```
   public String getLabel()

```

Return Value

Type: String

##### getName()

Returns the unique name used by the API to access to the data category group.

Signature

```
   public String getName()

```


Apex Reference Guide DescribeDataCategoryGroupStructureResult Class

Return Value

Type: String

##### getSobject()

Returns the object name associated with the data category group.

Signature

```
   public String getSobject()

```

Return Value

Type: String

DescribeDataCategoryGroupStructureResult Class

Contains the category groups and categories associated with KnowledgeArticleVersion and Question.

Namespace

Schema

Usage

The `describeDataCategoryGroupStructures` method returns a list of `Schema.Describe`
`DataCategoryGroupStructureResult` objects containing the category groups and categories associated with the specified
object.

[For additional information and code examples, see Accessing All Data Categories Associated with an sObject.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_data_categories.htm)

Example

The following is an example of how to instantiate a data category group structure describe result object:

```
   List <DataCategoryGroupSobjectTypePair> pairs =

       new List<DataCategoryGroupSobjectTypePair>();

   DataCategoryGroupSobjectTypePair pair1 =

       new DataCategoryGroupSobjectTypePair();

   pair1.setSobject('KnowledgeArticleVersion');

   pair1.setDataCategoryGroupName('Regions');

   DataCategoryGroupSobjectTypePair pair2 =

       new DataCategoryGroupSobjectTypePair();

   pair2.setSobject('Questions');

   pair2.setDataCategoryGroupName('Regions');

   pairs.add(pair1);

   pairs.add(pair2);

```


Apex Reference Guide DescribeDataCategoryGroupStructureResult Class

```
   List<Schema.DescribeDataCategoryGroupStructureResult>results =

       Schema.describeDataCategoryGroupStructures(pairs, true);

#### DescribeDataCategoryGroupStructureResult Methods The following are methods for DescribeDataCategoryGroupStructureResult . All are instance methods.

```

IN THIS SECTION:

##### getDescription()

Returns the description of the data category group.

##### getLabel()

Returns the label for the data category group used in the Salesforce user interface.

##### getName()

Returns the unique name used by the API to access to the data category group.

getSobject()
Returns the name of object associated with the data category group.

getTopCategories()
Returns a `Schema.DataCategory` object, that contains the top categories visible depending on the user's data category group
visibility settings.

##### getDescription()

Returns the description of the data category group.

Signature

```
   public String getDescription()

```

Return Value

Type: String

##### getLabel()

Returns the label for the data category group used in the Salesforce user interface.

Signature

```
   public String getLabel()

```

Return Value

Type: String

##### getName()

Returns the unique name used by the API to access to the data category group.


### Apex Reference Guide DescribeFieldResult Class

Signature

```
   public String getName()

```

Return Value

Type: String

##### getSobject()

Returns the name of object associated with the data category group.

Signature

```
   public String getSobject()

```

Return Value

Type: String

##### getTopCategories()

Returns a `Schema.DataCategory` object, that contains the top categories visible depending on the user's data category group
visibility settings.

Signature

```
   public List<Schema.DataCategory> getTopCategories()

```

Return Value

Type: List<Schema.DataCategory>

Usage

For more information on data category group visibility, see “Data Category Visibility” in the Salesforce online help.

### DescribeFieldResult Class

Contains methods for describing sObject fields.

Namespace

Schema

Usage

### Instances of field describe results on the same DescribeFieldResult aren’t guaranteed to be equal because the state and

behavior of a describe object is determined by various factors including the API version used. To compare describe results, call the


Apex Reference Guide DescribeFieldResult Class

`getSObjectField()` method on the field describe results and use the equality operator ( `==` ) to compare the `SObjectField`
values.

Example

The following is an example of how to instantiate a field describe result object:

```
   Schema.DescribeFieldResult dfr = Account.Description.getDescribe();

#### DescribeFieldResult Methods The following are methods for DescribeFieldResult . All are instance methods.

```

IN THIS SECTION:

getByteLength()
For variable-length fields (including binary fields), returns the maximum size of the field, in bytes.

getCalculatedFormula()
Returns the formula specified for this field.

getController()
Returns the token of the controlling field.

getDefaultValue()
Returns the default value for this field.

getDefaultValueFormula()
Returns the default formula value that is specified for this formula field.

getDigits()
Returns the maximum number of digits specified for the field. This method is only valid with Integer fields.

getInlineHelpText()
Returns the content of the field-level help.

getLabel()
Returns the text label that is displayed next to the field in the Salesforce user interface. This label can be localized.

getLength()
Returns the maximum size of the field for the DescribeFieldResult object in Unicode characters (not bytes).

getLocalName()
Returns the name of the field, similar to the `getName` method. However, if the field is part of the current namespace, the namespace
portion of the name is omitted.

getName()
Returns the field name used in Apex.

getPicklistValues()
Returns a list of active PicklistEntry objects. A runtime error is returned if the field isn’t a picklist. Only active picklist values are returned.

getPrecision()
For fields of type Double, returns the maximum number of digits that can be stored, including all numbers to the left and to the
right of the decimal point (but excluding the decimal point character).


Apex Reference Guide DescribeFieldResult Class

getReferenceTargetField()
Returns the name of the custom field on the parent standard or custom object whose values are matched against the values of the
child external object's indirect lookup relationship field. The match is done to determine which records are related to each other.

getReferenceTo()
Returns a list of Schema.sObjectType objects for the parent objects of this field. If the `isNamePointing` method returns `true`,
there is more than one entry in the list, otherwise there is only one.

getRelationshipName()
Returns the name of the child-to-parent relationship.

getRelationshipOrder()
Returns 0 if the field is the primary relationship field or 1 if the field is the secondary relationship field.

getScale()
For fields of type Double, returns the number of digits to the right of the decimal point.

getSOAPType()
Returns one of the SoapType enum values, depending on the type of field.

getSObjectField()
Returns the token for this field.

getSObjectType()
Returns the Salesforce object type from which this field originates.

getType()
Returns one of the DisplayType enum values, depending on the type of field.

isAccessible()
Returns `true` if the current user can see this field, `false` otherwise.

isAiPredictionField() (Beta)
Returns `true` if the current field is enabled to display Einstein prediction data, `false` otherwise.

isAutoNumber()
Returns `true` if the field is an Auto Number field, `false` otherwise.

isCalculated()
Returns `true` if the field is a custom formula field, `false` otherwise. Note that custom formula fields are always read-only.

isCascadeDelete()
Returns `true` if the child object is deleted when the parent object is deleted, `false` otherwise.

isCaseSensitive()
Returns `true` if the field is case sensitive, `false` otherwise.

isCreateable()
Returns `true` if the field can be created by the current user, `false` otherwise.

isCustom()
Returns `true` if the field is a custom field, `false` if it is a standard field, such as `Name` .

isDefaultedOnCreate()
Returns `true` if the field receives a default value when created, `false` otherwise.

isDependentPicklist()
Returns `true` if the picklist is a dependent picklist, `false` otherwise.


Apex Reference Guide DescribeFieldResult Class

isDeprecatedAndHidden()
Reserved for future use.

isEncrypted()
Returns `true` if the field is encrypted with Shield Platform Encryption, `false` otherwise.

isExternalID()
Returns `true` if the field is used as an external ID, `false` otherwise.

isFilterable()
Returns `true` if the field can be used as part of the filter criteria of a `WHERE` statement, `false` otherwise.

isFormulaTreatNullNumberAsZero()
Returns `true` if `null` is treated as zero in a formula field, `false` otherwise.

isGroupable()
Returns `true` if the field can be included in the `GROUP BY` clause of a SOQL query, `false` otherwise. This method is only
available for Apex classes and triggers saved using API version 18.0 and higher.

isHtmlFormatted()
Returns `true` if the field has been formatted for HTML and should be encoded for display in HTML, `false` otherwise. One example
of a field that returns `true` for this method is a hyperlink custom formula field. Another example is a custom formula field that has
an `IMAGE` text function.

isIdLookup()
Returns `true` if the field can be used to specify a record in an `upsert` method, `false` otherwise.

isNameField()
Returns `true` if the field is a name field, `false` otherwise.

isNamePointing()
Returns `true` if the field can have multiple types of objects as parents. For example, a task can have both the `Contact/Lead`
`ID` ( `WhoId` ) field and the `Opportunity/Account ID` ( `WhatId` ) field return `true` for this method. because either of
those objects can be the parent of a particular task record. This method returns `false` otherwise.

isNillable()
Returns `true` if the field is nillable, `false` otherwise. A nillable field can have empty content. A non-nillable field must have a
value for the object to be created or saved.

isPermissionable()
Returns `true` if field permissions can be specified for the field, `false` otherwise.

isRestrictedDelete()
Returns `true` if the parent object can't be deleted because it is referenced by a child object, `false` otherwise.

isRestrictedPicklist()
Returns `true` if the field is a restricted picklist, `false` otherwise

isSearchPrefilterable()
Returns `true` if a foreign key can be included in prefiltering when used in a SOSL `WHERE` clause, `false` otherwise.

isSortable()
Returns `true` if a query can sort on the field, `false` otherwise

isUnique()
Returns `true` if the value for the field must be unique, `false` otherwise


Apex Reference Guide DescribeFieldResult Class

isUpdateable()
Returns `true` if the field can be edited by the current user, or child records in a master-detail relationship field on a custom object
can be reparented to different parent records; `false` otherwise.

isWriteRequiresMasterRead()
Returns `true` if writing to the detail object requires read sharing instead of read/write sharing of the parent.

##### getByteLength()

For variable-length fields (including binary fields), returns the maximum size of the field, in bytes.

Signature

```
   public Integer getByteLength()

```

Return Value

Type: Integer

##### getCalculatedFormula()

Returns the formula specified for this field.

Signature

```
   public String getCalculatedFormula()

```

Return Value

Type: String

##### getController()

Returns the token of the controlling field.

Signature

```
   public Schema.sObjectField getController()

```

Return Value

Type: Schema.SObjectField

##### getDefaultValue()

Returns the default value for this field.

Signature

```
   public Object getDefaultValue()

```


Apex Reference Guide DescribeFieldResult Class

Return Value

Type: Object

##### getDefaultValueFormula()

Returns the default formula value that is specified for this formula field.

Signature

```
   public String getDefaultValueFormula()

```

Return Value

Type: String

##### getDigits()

Returns the maximum number of digits specified for the field. This method is only valid with Integer fields.

Signature

```
   public Integer getDigits()

```

Return Value

Type: Integer

##### getInlineHelpText()

Returns the content of the field-level help.

Signature

```
   public String getInlineHelpText()

```

Return Value

Type: String

Usage

For more information, see “Define Field-Level Help” in the Salesforce online help.

##### getLabel()

Returns the text label that is displayed next to the field in the Salesforce user interface. This label can be localized.

Signature

```
   public String getLabel()

```


Apex Reference Guide DescribeFieldResult Class

Return Value

Type: String

Usage

Note: For the Type field on standard objects, `getLabel` returns a label different from the default label. It returns a label of the
form _`Object`_ `Type`, where _Object_ is the standard object label. For example, for the Type field on Account, `getLabel` returns

`Account Type` instead of the default label `Type` . If the Type label is renamed, `getLabel` returns the new label. You can
check or change the labels of all standard object fields from Setup by entering _`Rename Tabs and Labels`_ in the `Quick`
`Find box`, then selecting **Rename Tabs and Labels** .

##### getLength()

Returns the maximum size of the field for the DescribeFieldResult object in Unicode characters (not bytes).

Signature

```
   public Integer getLength()

```

Return Value

Type: Integer

##### getLocalName() Returns the name of the field, similar to the getName method. However, if the field is part of the current namespace, the namespace

portion of the name is omitted.

Signature

```
   public String getLocalName()

```

Return Value

Type: String

##### getName()

Returns the field name used in Apex.

Signature

```
   public String getName()

```

Return Value

Type: String


Apex Reference Guide DescribeFieldResult Class

##### getPicklistValues()

Returns a list of active PicklistEntry objects. A runtime error is returned if the field isn’t a picklist. Only active picklist values are returned.

Signature

```
   public List<Schema.PicklistEntry> getPicklistValues()

```

Return Value

Type: List<Schema.PicklistEntry>

##### getPrecision()

For fields of type Double, returns the maximum number of digits that can be stored, including all numbers to the left and to the right
of the decimal point (but excluding the decimal point character).

Signature

```
   public Integer getPrecision()

```

Return Value

Type: Integer

##### getReferenceTargetField()

Returns the name of the custom field on the parent standard or custom object whose values are matched against the values of the child
external object's indirect lookup relationship field. The match is done to determine which records are related to each other.

Signature

```
   public String getReferenceTargetField()

```

Return Value

Type: String

Usage

For information about indirect lookup relationships, see “Indirect Lookup Relationship Fields on External Objects” in the Salesforce Help.

##### getReferenceTo()

Returns a list of Schema.sObjectType objects for the parent objects of this field. If the `isNamePointing` method returns `true`,
there is more than one entry in the list, otherwise there is only one.

Signature

```
   public List <Schema.sObjectType> getReferenceTo()

```


Apex Reference Guide DescribeFieldResult Class

Return Value

Type: List<Schema.sObjectType>

Versioned Behavior Changes

In API version 51.0 and later, the `getReferenceTo()` method returns referenced objects that aren’t accessible to the context user.
If the context user has access to an object’s field that references another object, irrespective of the context user’s access to the
cross-referenced object, the method returns references. In API version 50.0 and earlier, if the context user doesn’t have access to the
cross-referenced object, the method returns an empty list.

##### getRelationshipName()

Returns the name of the child-to-parent relationship.

Signature

```
   public String getRelationshipName()

```

Return Value

Type: String

Usage

[For more information about relationships and relationship names, see Understanding Relationship Names in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_relationships_understanding.htm) _SOQL and SOSL Reference_ .

##### getRelationshipOrder()

Returns 0 if the field is the primary relationship field or 1 if the field is the secondary relationship field.

Signature

```
   public Integer getRelationshipOrder()

```

Return Value

Type: Integer

Usage

[For more information about primary and secondary relationships, see Considerations for Object Relationships. For more information](https://help.salesforce.com/s/articleView?id=sf.relationships_considerations.htm&language=en_US)
[about relationships and relationship names, see Understanding Relationship Names in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_relationships_understanding.htm) _SOQL and SOSL Reference_ .

##### getScale()

For fields of type Double, returns the number of digits to the right of the decimal point.

Signature

```
   public Integer getScale()

```


Apex Reference Guide DescribeFieldResult Class

Return Value

Type: Integer

##### getSOAPType()

Returns one of the SoapType enum values, depending on the type of field.

Signature

```
   public Schema.SOAPType getSOAPType()

```

Return Value

Type: Schema.SOAPType

##### getSObjectField()

Returns the token for this field.

Signature

```
   public Schema.sObjectField getSObjectField()

```

Return Value

Type: Schema.SObjectField

##### **`getSObjectType()`**

Returns the Salesforce object type from which this field originates.

Signature

```
   public Schema.SObjectType getSObjectType()

```

Return Value

Type: Schema.SObjectType

Example

```
   Schema.DescribeFieldResult f = Account.Industry.getDescribe();

   Schema.sObjectType sourceType = f.getSObjectType();

   Assert.areEqual(Account.sObjectType, sourceType);

##### getType()

```

Returns one of the DisplayType enum values, depending on the type of field.


Apex Reference Guide DescribeFieldResult Class

Signature

```
   public Schema.DisplayType getType()

```

Return Value

Type: Schema.DisplayType

##### isAccessible()

Returns `true` if the current user can see this field, `false` otherwise.

Signature

```
   public Boolean isAccessible()

```

Return Value

Type: Boolean

##### isAiPredictionField() (Beta)

Returns `true` if the current field is enabled to display Einstein prediction data, `false` otherwise.

Signature

```
   public Boolean isAiPredictionField()

```

Return Value

Type: Boolean

Usage

Custom number fields can be set to display Einstein prediction values. If you are participating in the Einstein Prediction Builder Beta
program, use Einstein Prediction Builder to set up the value to display. Use this method to find out if a field is enabled to display an
Einstein prediction value.

##### isAutoNumber()

Returns `true` if the field is an Auto Number field, `false` otherwise.

Signature

```
   public Boolean isAutoNumber()

```

Return Value

Type: Boolean


Apex Reference Guide DescribeFieldResult Class

Usage

Analogous to a SQL IDENTITY type, Auto Number fields are read-only, non-createable text fields with a maximum length of 30 characters.
Auto Number fields are used to provide a unique ID that is independent of the internal object ID (such as a purchase order number or
invoice number). Auto Number fields are configured entirely in the Salesforce user interface.

##### isCalculated()

Returns `true` if the field is a custom formula field, `false` otherwise. Note that custom formula fields are always read-only.

Signature

```
   public Boolean isCalculated()

```

Return Value

Type: Boolean

##### isCascadeDelete()

Returns `true` if the child object is deleted when the parent object is deleted, `false` otherwise.

Signature

```
   public Boolean isCascadeDelete()

```

Return Value

Type: Boolean

##### isCaseSensitive()

Returns `true` if the field is case sensitive, `false` otherwise.

Signature

```
   public Boolean isCaseSensitive()

```

Return Value

Type: Boolean

##### isCreateable()

Returns `true` if the field can be created by the current user, `false` otherwise.

Signature

```
   public Boolean isCreateable()

```


Apex Reference Guide DescribeFieldResult Class

Return Value

Type: Boolean

##### isCustom()

Returns `true` if the field is a custom field, `false` if it is a standard field, such as `Name` .

Signature

```
   public Boolean isCustom()

```

Return Value

Type: Boolean

##### isDefaultedOnCreate()

Returns `true` if the field receives a default value when created, `false` otherwise.

Signature

```
   public Boolean isDefaultedOnCreate()

```

Return Value

Type: Boolean

Usage

If this method returns `true`, Salesforce implicitly assigns a value for this field when the object is created, even if a value for this field is
not passed in on the create call. For example, in the Opportunity object, the Probability field has this attribute because its value is derived
from the Stage field. Similarly, the Owner has this attribute on most objects because its value is derived from the current user (if the
Owner field is not specified).

##### isDependentPicklist()

Returns `true` if the picklist is a dependent picklist, `false` otherwise.

Signature

```
   public Boolean isDependentPicklist()

```

Return Value

Type: Boolean

##### isDeprecatedAndHidden()

Reserved for future use.


Apex Reference Guide DescribeFieldResult Class

Signature

```
   public Boolean isDeprecatedAndHidden()

```

Return Value

Type: Boolean

##### isEncrypted()

Returns `true` if the field is encrypted with Shield Platform Encryption, `false` otherwise.

Signature

```
   public Boolean isEncrypted()

```

Return Value

Type: Boolean

##### isExternalID()

Returns `true` if the field is used as an external ID, `false` otherwise.

Signature

```
   public Boolean isExternalID()

```

Return Value

Type: Boolean

##### isFilterable()

Returns `true` if the field can be used as part of the filter criteria of a `WHERE` statement, `false` otherwise.

Signature

```
   public Boolean isFilterable()

```

Return Value

Type: Boolean

##### isFormulaTreatNullNumberAsZero()

Returns `true` if `null` is treated as zero in a formula field, `false` otherwise.

Signature

```
   public Boolean isFormulaTreatNullNumberAsZero()

```


Apex Reference Guide DescribeFieldResult Class

Return Value

Type: Boolean

##### isGroupable()

Returns `true` if the field can be included in the `GROUP BY` clause of a SOQL query, `false` otherwise. This method is only available
for Apex classes and triggers saved using API version 18.0 and higher.

Signature

```
   public Boolean isGroupable()

```

Return Value

Type: Boolean

##### isHtmlFormatted()

Returns `true` if the field has been formatted for HTML and should be encoded for display in HTML, `false` otherwise. One example
of a field that returns `true` for this method is a hyperlink custom formula field. Another example is a custom formula field that has an
`IMAGE` text function.

Signature

```
   public Boolean isHtmlFormatted()

```

Return Value

Type: Boolean

##### isIdLookup()

Returns `true` if the field can be used to specify a record in an `upsert` method, `false` otherwise.

Signature

```
   public Boolean isIdLookup()

```

Return Value

Type: Boolean

##### isNameField()

Returns `true` if the field is a name field, `false` otherwise.

Signature

```
   public Boolean isNameField()

```


Apex Reference Guide DescribeFieldResult Class

Return Value

Type: Boolean

Usage

This method is used to identify the name field for standard objects (such as `AccountName` for an Account object) and custom objects.
Objects can only have one name field, except where the `FirstName` and `LastName` fields are used instead (such as on the Contact
object).

If a compound name is present, for example, the `Name` field on a person account, `isNameField` is set to `true` for that record.

##### isNamePointing()

Returns `true` if the field can have multiple types of objects as parents. For example, a task can have both the `Contact/Lead ID`
( `WhoId` ) field and the `Opportunity/Account ID` ( `WhatId` ) field return `true` for this method. because either of those objects
can be the parent of a particular task record. This method returns `false` otherwise.

Signature

```
   public Boolean isNamePointing()

```

Return Value

Type: Boolean

##### isNillable()

Returns `true` if the field is nillable, `false` otherwise. A nillable field can have empty content. A non-nillable field must have a value
for the object to be created or saved.

Signature

```
   public Boolean isNillable()

```

Return Value

Type: Boolean

##### isPermissionable()

Returns `true` if field permissions can be specified for the field, `false` otherwise.

Signature

```
   public Boolean isPermissionable()

```

Return Value

Type: Boolean


Apex Reference Guide DescribeFieldResult Class

##### isRestrictedDelete()

Returns `true` if the parent object can't be deleted because it is referenced by a child object, `false` otherwise.

Signature

```
   public Boolean isRestrictedDelete()

```

Return Value

Type: Boolean

##### isRestrictedPicklist()

Returns `true` if the field is a restricted picklist, `false` otherwise

Signature

```
   public Boolean isRestrictedPicklist()

```

Return Value

Type: Boolean

##### isSearchPrefilterable()

Returns `true` if a foreign key can be included in prefiltering when used in a SOSL `WHERE` clause, `false` otherwise.

Signature

```
   public Boolean isSearchPrefilterable()

```

Return Value

Type: Boolean

Usage

_Prefiltering_ means to filter by a specific field value before executing the full search query. Prefiltering is supported only in `WHERE` clauses
with the equals ( `=` ) operator.

##### isSortable()

Returns `true` if a query can sort on the field, `false` otherwise

Signature

```
   public Boolean isSortable()

```


### Apex Reference Guide DescribeIconResult Class

Return Value

Type: Boolean

##### isUnique()

Returns `true` if the value for the field must be unique, `false` otherwise

Signature

```
   public Boolean isUnique()

```

Return Value

Type: Boolean

##### isUpdateable()

Returns `true` if the field can be edited by the current user, or child records in a master-detail relationship field on a custom object can
be reparented to different parent records; `false` otherwise.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Signature

```
   public Boolean isUpdateable()

```

Return Value

Type: Boolean

##### isWriteRequiresMasterRead()

Returns `true` if writing to the detail object requires read sharing instead of read/write sharing of the parent.

Signature

```
   public Boolean isWriteRequiresMasterRead()

```

Return Value

Type: Boolean

### DescribeIconResult Class

Contains icon metadata information for a tab.

Namespace

Schema


Apex Reference Guide DescribeIconResult Class

Usage

The `getIcons` method of the `Schema.DescribeTabResult` class returns a list of `Schema.DescribeIconResult`
objects that describe colors used in a tab.

The methods in the `Schema.DescribeIconResult` class can be called using their property counterparts. For each method
starting with `get`, you can omit the `get` prefix and the ending parentheses `()` to call the property counterpart. For example,
`iconResultObj.url` is equivalent to `iconResultObj.getUrl()` .

Example

This sample shows how to get the icon information in the Sales app for the first tab’s first icon.

```
   // Get tab set describes for each app

   List<Schema.DescribeTabSetResult> tabSetDesc = Schema.describeTabs();

   // Iterate through each tab set

   for(Schema.DescribeTabSetResult tsr : tabSetDesc) {

      // Get tab info for the Sales app

      if (tsr.getLabel() == 'Sales') {

        // Get icon information for the first tab

        List<Schema.DescribeIconResult> iconDesc = tsr.getTabs()[0].getIcons();

        // Display the icon height and width of the first icon

        System.debug('Height: ' + iconDesc[0].getHeight());

        System.debug('Width: ' + iconDesc[0].getWidth());

      }

   }

   // Example debug statement output

   // DEBUG|Height: 32

   // DEBUG|Width: 32

#### DescribeIconResult Methods The following are methods for DescribeIconResult . All are instance methods.

```

IN THIS SECTION:

getContentType()
Returns the tab icon’s content type, such as `image/png` .

getHeight()
Returns the tab icon’s height in pixels.

getTheme()
Returns the tab’s icon theme.

getUrl()
Returns the tab’s icon fully qualified URL.

getWidth()
Returns the tab’s icon width in pixels.


Apex Reference Guide DescribeIconResult Class

##### getContentType()

Returns the tab icon’s content type, such as `image/png` .

Signature

```
   public String getContentType()

```

Return Value

Type: String

##### getHeight()

Returns the tab icon’s height in pixels.

Signature

```
   public Integer getHeight()

```

Return Value

Type: Integer

Usage

Note: If the icon content type is SVG, the icon won’t have a size and its height is zero.

##### getTheme()

Returns the tab’s icon theme.

Signature

```
   public String getTheme()

```

Return Value

Type: String

Possible theme values include `theme3`, `theme4`, and `custom` .

**•** `theme3` is the Salesforce theme introduced during Spring ‘10.

**•** `theme4` is the Salesforce theme introduced in Winter ‘14 for the mobile touchscreen version of Salesforce.

**•** `custom` is the theme name associated with a custom icon.

##### getUrl()

Returns the tab’s icon fully qualified URL.


### Apex Reference Guide DescribeSObjectResult Class

Signature

```
   public String getUrl()

```

Return Value

Type: String

##### getWidth()

Returns the tab’s icon width in pixels.

Signature

```
   public Integer getWidth()

```

Return Value

Type: Integer

Usage

Note: If the icon content type is SVG, the icon won’t have a size and its width is zero.

### DescribeSObjectResult Class

Contains methods for describing SObjects. None of the methods take an argument.

Namespace

Schema

Usage

### Instances of describe results on the same DescribeSObjectResult aren’t guaranteed to be equal because the state and behavior

of a describe object is determined by various factors including the API version used. To compare describe results, call the
`getSObjectType()` method on the SObject describe results and use the equality operator ( `==` ) to compare the `SObjectType`
values.

#### DescribeSObjectResult Properties

### The following are properties for DescribeSObjectResult .

##### **`accessible`**

Indicates whether the current user has access to the SObject.


Apex Reference Guide DescribeSObjectResult Class

Signature

```
   public Boolean accessible {get; set;}

```

Property Value

Type: Boolean

##### **`associateentitytype`**

The type of associated object. For example, `History` or `Share` .

Signature

```
   public String associateentitytype {get; set;}

```

Property Value

Type: String

##### **`associateparententity`**

The parent object of an associated object.

Signature

```
   public String associateparententity {get; set;}

```

Property Value

Type: String

##### **`childrelationships`**

A list of child relationships, which is the name of the sObject that has a foreign key to the sObject being described.

Signature

```
   public List<Schema.ChildRelationship> childrelationships {get; set;}

```

Property Value

Type: List<Schema.ChildRelationship on page 3368>

##### **`createable`**

Indicates whether the SObject can be created by the current user.

Signature

```
   public Boolean createable {get; set;}

```


Apex Reference Guide DescribeSObjectResult Class

Property Value

Type: Boolean

##### **`custom`**

Indicates whether the SObject is a custom object.

Signature

```
   public Boolean custom {get; set;}

```

Property Value

Type: Boolean

##### **`customsetting`**

Indicates whether the SObject is a custom setting.

Signature

```
   public Boolean customsetting {get; set;}

```

Property Value

Type: Boolean

##### **`datatranslationenabled`**

Indicates whether data translation is enabled for the SObject. This property is available in API version 49.0 and later.

Signature

```
   public Boolean datatranslationenabled {get; set;}

```

Property Value

Type: Boolean

##### **`defaultimplementation`**

Reserved for future use.

Signature

```
   public String defaultimplementation {get; set;}

```

Property Value

Type: String


Apex Reference Guide DescribeSObjectResult Class

##### **`deletable`**

Indicates whether the SObject can be deleted by the current user.

Signature

```
   public Boolean deletable {get; set;}

```

Property Value

Type: Boolean

##### **`deprecatedandhidden`**

Reserved for future use.

Signature

```
   public Boolean deprecatedandhidden {get; set;}

```

Property Value

Type: Boolean

##### **`feedenabled`**

Indicates whether Chatter feeds are enabled for the SObject.

Signature

```
   public Boolean feedenabled {get; set;}

```

Property Value

Type: Boolean

##### fields

A list of fields associated with the SObject.

Signature

```
   public Schema.SObjectTypeFields fields {get; set;}

```

Property Value

Type: Schema.SObjectTypeFields

##### Follow fields with the getMap method.


Apex Reference Guide DescribeSObjectResult Class

Example

This sample code shows how to use `fields` . To get a custom field, specify the custom field name.

```
   Schema.DescribeFieldResult dfr = Schema.SObjectType.Account.fields.Name;

##### fieldSets

```

Represents field sets, which is a grouping of the SObject fields.

Signature

```
   public Schema.SObjectTypeFieldSets fieldsets {get; set;}

```

Property Value

Type: Schema.SObjectTypeFieldSets

##### Follow fieldSets with a field set name or with the getMap method.

Example

##### This sample code shows how to use fieldSet .

```
   Schema.DescribeSObjectResult d =

     Account.sObjectType.getDescribe();

   Map<String, Schema.FieldSet> FsMap =

     d.fieldSets.getMap();

##### **`hassubtypes`**

```

Reserved for future use.

Signature

```
   public Boolean hassubtypes {get; set;}

```

Property Value

Type: Boolean

##### **`implementedby`**

Reserved for future use.

Signature

```
   public String implementedby {get; set;}

```

Property Value

Type: String


Apex Reference Guide DescribeSObjectResult Class

##### **`implementsinterfaces`**

Reserved for future use.

Signature

```
   public String implementsinterfaces {get; set;}

```

Property Value

Type: String

##### **`isinterface`**

Reserved for future use.

Signature

```
   public Boolean isinterface {get; set;}

```

Property Value

Type: Boolean

##### **`keyprefix`**

The three-character prefix code in the SObject ID.

Signature

```
   public String keyprefix {get; set;}

```

Property Value

Type: String

##### **`label`**

The SObject's label, which may or may not match the object name. For example, an organization representing a medical vertical might
rename Account to Patient. Tabs and fields can be renamed in the Salesforce user interface.

Signature

```
   public String label {get; set;}

```

Property Value

Type: String


Apex Reference Guide DescribeSObjectResult Class

##### **`labelplural`**

The SObject's plural label, which may or may not match the object name. For example, Accounts.

Signature

```
   public String labelplural {get; set;}

```

Property Value

Type: String

##### **`localname`**

The name of the SObject. If the object is part of the current namespace, the namespace portion of the name is omitted.

Signature

```
   public String localname {get; set;}

```

Property Value

Type: String

##### **`mergeable`**

Indicates whether the SObject can be merged with other objects of its type by the current user. This is set to `true` for leads, contacts,
and accounts.

Signature

```
   public Boolean mergeable {get; set;}

```

Property Value

Type: Boolean

##### **`mruenabled`**

Indicates whether Most Recently Used (MRU) list functionality is enabled for the SObject.

Signature

```
   public Boolean mruenabled {get; set;}

```

Property Value

Type: Boolean


Apex Reference Guide DescribeSObjectResult Class

##### **`name`**

The name field of the SObject.

Signature

```
   public String name {get; set;}

```

Property Value

Type: String

##### **`queryable`**

Indicates whether the SObject can be queried by the current user.

Signature

```
   public Boolean queryable {get; set;}

```

Property Value

Type: Boolean

##### **`recordtypeinfos`**

A list of the record types supported by the SObject.

Signature

```
   public List<Schema.RecordTypeInfo> recordtypeinfos {get; set;}

```

Property Value

Type: List<Schema.RecordTypeInfo>

##### **`recordtypeinfosbydevelopername`**

A map that matches developer names to their associated record type.

Signature

```
   public Map<String,Schema.RecordTypeInfo> recordtypeinfosbydevelopername {get; set;}

```

Property Value

Type: Map<String, Schema.RecordTypeInfo>

##### **`recordtypeinfosbyid`**

A map that matches record IDs to their associated record types.


Apex Reference Guide DescribeSObjectResult Class

Signature

```
   public Map<Id,Schema.RecordTypeInfo> recordtypeinfosbyid {get; set;}

```

Property Value

Type: Map<ID, Schema.RecordTypeInfo>

##### **`recordtypeinfosbyname`**

A map that matches record labels to their associated record type.

Signature

```
   public Map<String,Schema.RecordTypeInfo> recordtypeinfosbyname {get; set;}

```

Property Value

Type: Map<String, Schema.RecordTypeInfo>

##### **`searchable`**

Indicates whether the SObject can be searched by the current user.

Signature

```
   public Boolean searchable {get; set;}

```

Property Value

Type: Boolean

##### **`sobjectdescribeoption`**

The effective describe option used by the system for the SObject.

Signature

```
   public Schema.SObjectDescribeOptions sobjectdescribeoption {get; set;}

```

Property Value

Type: SObjectDescribeOptions Enum

##### **`sobjecttype`**

The Schema.SObjectType object for the SObject.

Signature

```
   public Schema.SObjectType sobjecttype {get; set;}

```


Apex Reference Guide DescribeSObjectResult Class

Property Value

Type: Schema.SObjectType

##### **`undeletable`**

Indicates whether the SObject can be undeleted by the current user.

Signature

```
   public Boolean undeletable {get; set;}

```

Property Value

Type: Boolean

##### **`updateable`**

Indicates whether the SObject can be updated by the current user.

Signature

```
   public Boolean updateable {get; set;}

```

Property Value

Type: Boolean

#### DescribeSObjectResult Methods The following are methods for DescribeSObjectResult . All are instance methods.

IN THIS SECTION:

equals(obj)
Compares the SObject to the specified object and returns true if both are equal. Otherwise, returns false.

getAssociateEntityType()
Returns additional metadata for an associated object of a specified parent but only if it's a specific associated object type. Used in
combination with the `getAssociateParentEntity()` method to get the parent object. For example, invoking the method
on AccountHistory returns the parent object as `Account` and the type of associated object as `History` .

getAssociateParentEntity()
Returns additional metadata for an associated object but only if it's associated to a specific parent object. Used in combination with
the `getAssociateEntityType()` method to get the type of associated object. For example, invoking the method on
AccountHistory returns the parent object as `Account` and the type of associated object as `History` .

getChildRelationships()
Returns a list of child relationships, which are the names of the sObjects that have a foreign key to the sObject being described.

getDataTranslationEnabled()
Returns true if data translation is enabled for the SObject. Otherwise, returns false.


Apex Reference Guide DescribeSObjectResult Class

getDefaultImplementation()
Reserved for future use.

getFields()
Returns the fields that make up the SObject being described.

getFieldSets()
Returns field sets, which is a grouping of the SObject fields.

getHasSubtypes()
Reserved for future use.

getImplementedBy()
Reserved for future use.

getImplementsInterfaces()
Reserved for future use.

getIsInterface()
Reserved for future use.

getKeyPrefix()
Returns the three-character prefix code for the object. Record IDs are prefixed with three-character codes that specify the type of
the object (for example, accounts have a prefix of `001` and opportunities have a prefix of `006` ).

getLabel()
Returns the object's label, which may or may not match the object name.

getLabelPlural()
Returns the object's plural label, which may or may not match the object name.

getLocalName()
Returns the name of the object, similar to the `getName` method. However, if the object is part of the current namespace, the
namespace portion of the name is omitted.

getName()
Returns the name of the object.

getRecordTypeInfos()
Returns a list of the record types supported by this object. The current user is not required to have access to a record type to see it
in this list.

getRecordTypeInfosByDeveloperName()
Returns a map that matches developer names to their associated record type. The current user is not required to have access to a
record type to see it in this map.

getRecordTypeInfosById()
Returns a map that matches record IDs to their associated record types. The current user is not required to have access to a record
type to see it in this map.

getRecordTypeInfosByName()
Returns a map that matches record labels to their associated record type. The current user is not required to have access to a record
type to see it in this map.

getSObjectDescribeOption()
Returns the effective describe option used by the system for the SObject.


Apex Reference Guide DescribeSObjectResult Class

getSobjectType()
Returns the Schema.SObjectType object for the sObject. You can use this to create a similar sObject.

getHasSubtypes()
Reserved for future use.

hashCode()
Returns the hash code for the SObject.

isAccessible()
Returns `true` if the current user can see this object, `false` otherwise.

isCreateable()
Returns `true` if the object can be created by the current user, `false` otherwise.

isCustom()
Returns `true` if the object is a custom object, `false` if it is a standard object.

isCustomSetting()
Returns `true` if the object is a custom setting, `false` otherwise.

isDeletable()
Returns `true` if the object can be deleted by the current user, `false` otherwise.

isDeprecatedAndHidden()
Reserved for future use.

isFeedEnabled()
Returns `true` if Chatter feeds are enabled for the object, `false` otherwise. This method is only available for Apex classes and
triggers saved using SalesforceAPI version 19.0 and later.

isMergeable()
Returns `true` if the object can be merged with other objects of its type by the current user, `false` otherwise. `true` is returned
for leads, contacts, and accounts.

isMruEnabled()
Returns `true` if Most Recently Used (MRU) list functionality is enabled for the object, `false` otherwise.

isQueryable()
Returns `true` if the object can be queried by the current user, `false` otherwise

isSearchable()
Returns `true` if the object can be searched by the current user, `false` otherwise.

isUndeletable()
Returns `true` if the object can be undeleted by the current user, `false` otherwise.

isUpdateable()
Returns `true` if the object can be updated by the current user, `false` otherwise.

toString()
Returns a string that represents the SObject.

##### **`equals(obj)`**

Compares the SObject to the specified object and returns true if both are equal. Otherwise, returns false.


Apex Reference Guide DescribeSObjectResult Class

Signature

```
   public Boolean equals(Object obj)

```

Parameters

```
   obj
```

Type: Object

The object with which to compare.

Return Value

Type: Boolean

##### **`getAssociateEntityType()`**

Returns additional metadata for an associated object of a specified parent but only if it's a specific associated object type. Used in
##### combination with the getAssociateParentEntity() method to get the parent object. For example, invoking the method

on AccountHistory returns the parent object as `Account` and the type of associated object as `History` .

Signature

```
   public String associateentitytype {get; set;}

```

Return Value

Type: String

SEE ALSO:

DescribeSObjectResult Properties

##### **`getAssociateParentEntity()`**

Returns additional metadata for an associated object but only if it's associated to a specific parent object. Used in combination with the
##### getAssociateEntityType() method to get the type of associated object. For example, invoking the method on AccountHistory

returns the parent object as `Account` and the type of associated object as `History` .

Signature

```
   public String getAssociateParentEntity()

```

Return Value

Type: String

SEE ALSO:

DescribeSObjectResult Properties


Apex Reference Guide DescribeSObjectResult Class

##### getChildRelationships()

Returns a list of child relationships, which are the names of the sObjects that have a foreign key to the sObject being described.

Signature

```
   public Schema.ChildRelationship getChildRelationships()

```

Return Value

Type: List<Schema.ChildRelationship>

Example

For example, the Account object includes `Contacts` and `Opportunities` as child relationships.

##### **`getDataTranslationEnabled()`**

Returns true if data translation is enabled for the SObject. Otherwise, returns false.

Signature

```
   public Boolean getDataTranslationEnabled()

```

Return Value

Type: Boolean

##### getDefaultImplementation()

Reserved for future use.

Signature

```
   public String getDefaultImplementation()

```

Return Value

Type: String

##### **`getFields()`**

Returns the fields that make up the SObject being described.

Signature

```
   public Schema.SObjectTypeFields getFields()

```

Return Value

Type: Schema.SObjectTypeFields


Apex Reference Guide DescribeSObjectResult Class

The return value is a special data type. Call the `getMap()` method to get a map of Strings and SObjectFields.

Usage

When you describe SObjects and their fields from within an Apex class, custom fields of new field types are returned regardless of the
API version that the class is saved in. If a field type, such as the geolocation field type, is available only in a recent API version, components
of a geolocation field are returned even if the class is saved in an earlier API version.

SEE ALSO:

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_field_tokens.htm)_ : Using Field Tokens

_Apex Developer Guide_ [: Describing sObjects Using Schema Method](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_describeSObject.htm)

_Apex Developer Guide_ [: Understanding Apex Describe Information](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_describe_objects_understanding.htm)

##### **`getFieldSets()`**

Returns field sets, which is a grouping of the SObject fields.

Signature

```
   public Schema.SObjectTypeFieldSets getFieldSets()

```

Return Value

Type: Schema.SObjectTypeFieldSets

The return value is a special data type. Call the `getMap()` method to get a map of Strings and SObjectFieldSets.

SEE ALSO:

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_field_tokens.htm)_ : Using Field Tokens

_Apex Developer Guide_ [: Describing sObjects Using Schema Method](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_describeSObject.htm)

_Apex Developer Guide_ [: Understanding Apex Describe Information](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_describe_objects_understanding.htm)

##### getHasSubtypes()

Reserved for future use.

To check if Person Accounts are enabled for the current org, use this code snippet:

```
   Schema.SObjectType.Account.fields.getMap().containsKey( 'isPersonAccount' );

```

Signature

```
   public Boolean getHasSubtypes()

```

Return Value

Type: Boolean


Apex Reference Guide DescribeSObjectResult Class

##### getImplementedBy()

Reserved for future use.

Signature

```
   public String getImplementedBy()

```

Return Value

Type: String

##### getImplementsInterfaces()

Reserved for future use.

Signature

```
   public String getImplementsInterfaces()

```

Return Value

Type: String

##### getIsInterface()

Reserved for future use.

Signature

```
   public Boolean getIsInterface()

```

Return Value

Type: Boolean

##### getKeyPrefix()

Returns the three-character prefix code for the object. Record IDs are prefixed with three-character codes that specify the type of the
object (for example, accounts have a prefix of `001` and opportunities have a prefix of `006` ).

Signature

```
   public String getKeyPrefix()

```

Return Value

Type: String


Apex Reference Guide DescribeSObjectResult Class

Usage

The DescribeSobjectResult object returns a value for objects that have a stable prefix. For object types that do not have a stable or
predictable prefix, this field is blank. Client applications that rely on these codes can use this way of determining object type to ensure
forward compatibility.

##### getLabel()

Returns the object's label, which may or may not match the object name.

Signature

```
   public String getLabel()

```

Return Value

Type: String

Usage

The object's label might not always match the object name. For example, an organization in the medical industry might change the
label for Account to Patient. This label is then used in the Salesforce user interface. See the Salesforce online help for more information.

##### getLabelPlural()

Returns the object's plural label, which may or may not match the object name.

Signature

```
   public String getLabelPlural()

```

Return Value

Type: String

Usage

The object's plural label might not always match the object name. For example, an organization in the medical industry might change
the plural label for Account to Patients. This label is then used in the Salesforce user interface. See the Salesforce online help for more
information.

##### getLocalName()

Returns the name of the object, similar to the `getName` method. However, if the object is part of the current namespace, the namespace
portion of the name is omitted.

Signature

```
   public String getLocalName()

```


Apex Reference Guide DescribeSObjectResult Class

Return Value

Type: String

##### getName()

Returns the name of the object.

Signature

```
   public String getName()

```

Return Value

Type: String

##### getRecordTypeInfos()

Returns a list of the record types supported by this object. The current user is not required to have access to a record type to see it in
this list.

Signature

```
   public List<Schema.RecordTypeInfo> getRecordTypeInfos()

```

Return Value

Type: List<Schema.RecordTypeInfo>

##### getRecordTypeInfosByDeveloperName()

Returns a map that matches developer names to their associated record type. The current user is not required to have access to a record
type to see it in this map.

Signature

```
   public Map<String, Schema.RecordTypeInfo> getRecordTypeInfosByDeveloperName()

```

Return Value

Type: Map<String, Schema.RecordTypeInfo>

##### getRecordTypeInfosById()

Returns a map that matches record IDs to their associated record types. The current user is not required to have access to a record type
to see it in this map.

Signature

```
   public Schema.RecordTypeInfo getRecordTypeInfosById()

```


Apex Reference Guide DescribeSObjectResult Class

Return Value

Type: Map<ID, Schema.RecordTypeInfo>

##### getRecordTypeInfosByName()

Returns a map that matches record labels to their associated record type. The current user is not required to have access to a record type
to see it in this map.

Signature

```
   public Schema.RecordTypeInfo getRecordTypeInfosByName()

```

Return Value

Type: Map<String, Schema.RecordTypeInfo>

##### getSObjectDescribeOption()

Returns the effective describe option used by the system for the SObject.

Signature

```
   public Schema.SObjectDescribeOptions getSObjectDescribeOption()

```

Return Value

Type: Schema.SObjectDescribeOptions

Valid values are:

**•** `SObjectDescribeOptions.FULL` : Indicates eager-load all elements of the describe, including child relationships, up-front
at the time of method invocation.

**•** `SObjectDescribeOptions.DEFERRED` : Indicates lazy-load child relationships. This means that all child relationships will
not be loaded at the time of first invocation of the method.

##### getSobjectType()

Returns the Schema.SObjectType object for the sObject. You can use this to create a similar sObject.

Signature

```
   public Schema.SObjectType getSobjectType()

```

Return Value

Type: Schema.SObjectType

##### getHasSubtypes()

Reserved for future use.


Apex Reference Guide DescribeSObjectResult Class

To check if Person Accounts are enabled for the current org, use this code snippet:

```
   Schema.SObjectType.Account.fields.getMap().containsKey( 'isPersonAccount' );

```

Signature

```
   public Boolean getHasSubtypes()

```

Return Value

Type: Boolean

##### **`hashCode()`**

Returns the hash code for the SObject.

Signature

```
   public Integer hashCode()

```

Return Value

Type: Integer

##### isAccessible()

Returns `true` if the current user can see this object, `false` otherwise.

Signature

```
   public Boolean isAccessible()

```

Return Value

Type: Boolean

Versioned Behavior Changes

In API version 54.0 and later, for custom settings and custom metadata type objects,
`DescribeSObjectResult.isAccessible()` returns `false` if the user doesn’t have permissions to access the queried
objects. In API version 53.0 and earlier, the method returns `true` even if the user doesn't have the required permissions.

##### isCreateable()

Returns `true` if the object can be created by the current user, `false` otherwise.

Signature

```
   public Boolean isCreateable()

```


Apex Reference Guide DescribeSObjectResult Class

Return Value

Type: Boolean

##### isCustom()

Returns `true` if the object is a custom object, `false` if it is a standard object.

Signature

```
   public Boolean isCustom()

```

Return Value

Type: Boolean

##### isCustomSetting()

Returns `true` if the object is a custom setting, `false` otherwise.

Signature

```
   public Boolean isCustomSetting()

```

Return Value

Type: Boolean

##### isDeletable()

Returns `true` if the object can be deleted by the current user, `false` otherwise.

Signature

```
   public Boolean isDeletable()

```

Return Value

Type: Boolean

##### isDeprecatedAndHidden()

Reserved for future use.

Signature

```
   public Boolean isDeprecatedAndHidden()

```

Return Value

Type: Boolean


Apex Reference Guide DescribeSObjectResult Class

##### isFeedEnabled()

Returns `true` if Chatter feeds are enabled for the object, `false` otherwise. This method is only available for Apex classes and triggers
saved using SalesforceAPI version 19.0 and later.

Signature

```
   public Boolean isFeedEnabled()

```

Return Value

Type: Boolean

##### isMergeable()

Returns `true` if the object can be merged with other objects of its type by the current user, `false` otherwise. `true` is returned for
leads, contacts, and accounts.

Signature

```
   public Boolean isMergeable()

```

Return Value

Type: Boolean

##### isMruEnabled()

Returns `true` if Most Recently Used (MRU) list functionality is enabled for the object, `false` otherwise.

Signature

```
   public Boolean isMruEnabled()

```

Return Value

Type: Boolean

##### isQueryable()

Returns `true` if the object can be queried by the current user, `false` otherwise

Signature

```
   public Boolean isQueryable()

```

Return Value

Type: Boolean


### Apex Reference Guide DescribeTabResult Class

##### isSearchable()

Returns `true` if the object can be searched by the current user, `false` otherwise.

Signature

```
   public Boolean isSearchable()

```

Return Value

Type: Boolean

##### isUndeletable()

Returns `true` if the object can be undeleted by the current user, `false` otherwise.

Signature

```
   public Boolean isUndeletable()

```

Return Value

Type: Boolean

##### isUpdateable()

Returns `true` if the object can be updated by the current user, `false` otherwise.

Signature

```
   public Boolean isUpdateable()

```

Return Value

Type: Boolean

##### **`toString()`**

Returns a string that represents the SObject.

Signature

```
   public String toString()

```

Return Value

Type: String

### DescribeTabResult Class

Contains tab metadata information for a tab in a standard or custom app available in the Salesforce user interface.


Apex Reference Guide DescribeTabResult Class

Namespace

Schema

Usage

The `getTabs` method of the `Schema.DescribeTabSetResult` returns a list of `Schema.DescribeTabResult` objects
that describe the tabs of one app.

The methods in the `Schema.DescribeTabResult` class can be called using their property counterparts. For each method starting
##### with get, you can omit the get prefix and the ending parentheses () to call the property counterpart. For example,

`tabResultObj.label` is equivalent to `tabResultObj.getLabel()` . Similarly, for each method starting with `is`, omit
the `is` prefix and the ending parentheses `()` . For example, `tabResultObj.isCustom` is equivalent to
`tabResultObj.custom` .

#### DescribeTabResult Methods The following are methods for DescribeTabResult . All are instance methods.

IN THIS SECTION:

##### getColors()

Returns a list of color metadata information for all colors associated with this tab. Each color is associated with a theme and context.

getIconUrl()
Returns the URL for the main 32 x 32-pixel icon for a tab. This icon corresponds to the current theme (theme3) and appears next to
the heading at the top of most pages.

getIcons()
Returns a list of icon metadata information for all icons associated with this tab. Each icon is associated with a theme and context.

getLabel()
Returns the display label of this tab.

getMiniIconUrl()
Returns the URL for the 16 x 16-pixel icon that represents a tab. This icon corresponds to the current theme (theme3) and appears
in related lists and other locations.

getSobjectName()
Returns the name of the sObject that is primarily displayed on this tab (for tabs that display a particular SObject).

getUrl()
Returns a fully qualified URL for viewing this tab.

isCustom()
Returns `true` if this is a custom tab, or `false` if this is a standard tab.

##### getColors()

Returns a list of color metadata information for all colors associated with this tab. Each color is associated with a theme and context.

Signature

```
   public List<Schema.DescribeColorResult> getColors()

```


Apex Reference Guide DescribeTabResult Class

Return Value

Type: List<Schema.DescribeColorResult>

##### getIconUrl()

Returns the URL for the main 32 x 32-pixel icon for a tab. This icon corresponds to the current theme (theme3) and appears next to the
heading at the top of most pages.

Signature

```
   public String getIconUrl()

```

Return Value

Type: String

##### getIcons()

Returns a list of icon metadata information for all icons associated with this tab. Each icon is associated with a theme and context.

Signature

```
   public List<Schema.DescribeIconResult> getIcons()

```

Return Value

Type: List<Schema.DescribeIconResult>

##### getLabel()

Returns the display label of this tab.

Signature

```
   public String getLabel()

```

Return Value

Type: String

##### getMiniIconUrl()

Returns the URL for the 16 x 16-pixel icon that represents a tab. This icon corresponds to the current theme (theme3) and appears in
related lists and other locations.

Signature

```
   public String getMiniIconUrl()

```


### Apex Reference Guide DescribeTabSetResult Class

Return Value

Type: String

##### getSobjectName()

Returns the name of the sObject that is primarily displayed on this tab (for tabs that display a particular SObject).

Signature

```
   public String getSobjectName()

```

Return Value

Type: String

##### getUrl()

Returns a fully qualified URL for viewing this tab.

Signature

```
   public String getUrl()

```

Return Value

Type: String

##### isCustom()

Returns `true` if this is a custom tab, or `false` if this is a standard tab.

Signature

```
   public Boolean isCustom()

```

Return Value

Type: Boolean

### DescribeTabSetResult Class

Contains metadata information about a Salesforce Classic standard or custom app available in the Salesforce user interface.

Namespace

Schema


Apex Reference Guide DescribeTabSetResult Class

Usage

The `Schema.describeTabs` method returns a list of `Schema.DescribeTabSetResult` objects that describe Salesforce
Classic standard and custom apps.

The methods in the `Schema.DescribeTabSetResult` class can be called using their property counterparts. For each method
starting with `get`, you can omit the `get` prefix and the ending parentheses `()` to call the property counterpart. For example,
`tabSetResultObj.label` is equivalent to `tabSetResultObj.getLabel()` . Similarly, for each method starting with
`is`, omit the `is` prefix and the ending parentheses `()` . For example, `tabSetResultObj.isSelected` is equivalent to
`tabSetResultObj.selected` .

Example

This example shows how to call the `Schema.describeTabs` method to get describe information for all available Salesforce Classic
apps. This example iterates through each describe result and gets more metadata information for the Sales app.

```
   // App we're interested to get more info about

   String appName = 'Sales';

   // Get tab set describes for each app

   List<Schema.DescribeTabSetResult> tabSetDesc = Schema.describeTabs();

   // Iterate through each tab set describe for each app and display the info

   for(Schema.DescribeTabSetResult tsr : tabSetDesc) {

      // Get more information for the Sales app

      if (tsr.getLabel() == appName) {

        // Find out if the app is selected

        if (tsr.isSelected()) {

           System.debug('The ' + appName + ' app is selected. ');

        }

        // Get the app's Logo URL and namespace

        String logo = tsr.getLogoUrl();

        System.debug('Logo URL: ' + logo);

        String ns = tsr.getNamespace();

        if (ns == '') {

           System.debug('The ' + appName + ' app has no namespace defined.');

        }

        else {

           System.debug('Namespace: ' + ns);

        }

        // Get the number of tabs

        System.debug('The ' + appName + ' app has ' + tsr.getTabs().size() + ' tabs.');

      }

   }

   // Example debug statement output

   // DEBUG|The Sales app is selected.

   // DEBUG|Logo URL:

   https:// MyDomainName .my.salesforce.com/img/seasonLogos/2014_winter_aloha.png

   // DEBUG|The Sales app has no namespace defined.

   // DEBUG|The Sales app has 14 tabs.

```


Apex Reference Guide DescribeTabSetResult Class

#### DescribeTabSetResult Methods The following are methods for DescribeTabSetResult . All are instance methods.

IN THIS SECTION:

##### getDescription()

Returns the display description for the standard or custom app.

##### getLabel()

Returns the display label for the standard or custom app.

getLogoUrl()
Returns a fully qualified URL to the logo image associated with the standard or custom app.

getNamespace()
Returns the developer namespace prefix of a Salesforce AppExchange managed package.

getTabs()
Returns metadata information about the standard or custom app’s displayed tabs.

isSelected()
Returns `true` if this standard or custom app is the user’s currently selected app in Salesforce Classic. Otherwise, returns `false` .

##### getDescription()

Returns the display description for the standard or custom app.

Signature

```
   public String getDescription()

```

Return Value

Type: String

##### getLabel()

Returns the display label for the standard or custom app.

Signature

```
   public String getLabel()

```

Return Value

Type: String

Usage

The display label changes when tabs are renamed in the Salesforce user interface. See the Salesforce online help for more information.


Apex Reference Guide DescribeTabSetResult Class

##### getLogoUrl()

Returns a fully qualified URL to the logo image associated with the standard or custom app.

Signature

```
   public String getLogoUrl()

```

Return Value

Type: String

##### getNamespace()

Returns the developer namespace prefix of a Salesforce AppExchange managed package.

Signature

```
   public String getNamespace()

```

Return Value

Type: String

Usage

This namespace prefix corresponds to the namespace prefix of the Developer Edition organization that was enabled to allow publishing
a managed package. This method applies to a custom app containing a set of tabs and installed as part of a managed package.

##### getTabs()

Returns metadata information about the standard or custom app’s displayed tabs.

Signature

```
   public List<Schema.DescribeTabResult> getTabs()

```

Return Value

Type: List<Schema.DescribeTabResult>

##### **`isSelected()`**

Returns `true` if this standard or custom app is the user’s currently selected app in Salesforce Classic. Otherwise, returns `false` .

Signature

```
   public Boolean isSelected()

```


### Apex Reference Guide DisplayType Enum

Return Value

Type: Boolean

### DisplayType Enum

A `Schema.DisplayType` enum value is returned by the field describe result's `getType` method.

Namespace

Schema

**Type Field Value** **What the Field Object Contains**

`ADDRESS` Address values

`ANYTYPE` Any value of the following types: `String`, `Picklist`, `Boolean`, `Integer`, `Double`,
`Percent`, `ID`, `Date`, `DateTime`, `URL`, or `Email` .

`BASE64` Base64-encoded arbitrary binary data (of type base64Binary)

`BOOLEAN` Boolean ( `true` or `false` ) values

`COMBOBOX` Comboboxes, which provide a set of enumerated values and allow the user to specify a value
not in the list

`COMPLEXVALUE` Complex Value Type (CVT)

`CURRENCY` Currency values

`DATACATEGORYGROUPREFERENCE` Reference to a data category group or a category unique name

`DATE` Date values

`DATETIME` DateTime values

`DOUBLE` Double values

`EMAIL` Email addresses

`ENCRYPTEDSTRING` Encrypted string

`FLOATARRAY` Array of float values, reserved for future use.

`ID` Primary key field for an object

`INTEGER` Integer values

`JSON` JSON format

`LOCATION` Location values, including latitude and longitude.

`LONG` Long values

`MULTIPICKLIST` Multi-select picklists, which provide a set of enumerated values from which multiple values can
be selected

`PERCENT` Percent values


### Apex Reference Guide FieldDescribeOptions Enum

**Type Field Value** **What the Field Object Contains**

`PHONE` Phone numbers. Values can include alphabetic characters. Client applications are responsible for
phone number formatting.

`PICKLIST` Single-select picklists, which provide a set of enumerated values from which only one value can
be selected

`REFERENCE` Cross-references to a different object, analogous to a foreign key field

`SOBJECT` An sObject variable represents a row of data and can only be declared in Apex using the SOAP
API name of the object.

`STRING` String values

`TEXTAREA` String values that are displayed as multiline text fields

`TEXTARRAY` Array of text values, reserved for future use.

`TIME` Time values

`URL` URL values that are displayed as hyperlinks

Usage

[For more information, see Field Types in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/field_types.htm) _Object Reference for Salesforce_ . For more information about the methods shared by all enums,
see Enum Methods.

### FieldDescribeOptions Enum

A `Schema.FieldDescribeOptions` enum value is a parameter in the `SObjectType.getDescribe` method.

Usage

For more information about the method using this enum, see `getDescribe(options)` .

Enum Values

The following are the values of the `Schema.FieldDescribeOptions` enum.

**Value** **Description**

`DEFAULT` Compute context-specific, describe field results.

`FULL_DESCRIBE` Compute all aspects of describe field results.

### FieldSet Class

Contains methods for discovering and retrieving the details of field sets created on sObjects.


Apex Reference Guide FieldSet Class

Namespace

Schema

Usage

Use the methods in the `Schema.FieldSet` class to discover the fields contained within a field set, and get details about the field
set itself, such as the name, namespace, label, and so on. The following example shows how to get a collection of field set describe result
objects for an sObject. The key of the returned Map is the field set name, and the value is the corresponding field set describe result.

```
   Map<String, Schema.FieldSet> FsMap =

      Schema.SObjectType.Account.fieldSets.getMap();

```

Field sets are also available from sObject describe results. The following lines of code are equivalent to the prior sample:

```
   Schema.DescribeSObjectResult d =

     Account.sObjectType.getDescribe();

   Map<String, Schema.FieldSet> FsMap =

     d.fieldSets.getMap();

```

To work with an individual field set, you can access it via the map of field sets on an sObject or, when you know the name of the field
set in advance, using an explicit reference to the field set. The following two lines of code retrieve the same field set:

```
   Schema.FieldSet fs1 = Schema.SObjectType.Account.fieldSets.getMap().get('field_set_name');

   Schema.FieldSet fs2 = Schema.SObjectType.Account.fieldSets.field_set_name;

```

Example: Displaying a Field Set on a Visualforce Page

This sample uses `Schema.FieldSet` and `Schema.FieldSetMember` methods to dynamically get all the fields in the
Dimensions field set for the Merchandise custom object. The list of fields is then used to construct a SOQL query that ensures those fields
are available for display. The Visualforce page uses the `MerchandiseDetails` class as its controller.

```
   public class MerchandiseDetails {

      public Merchandise__c merch { get; set; }

      public MerchandiseDetails() {

        this.merch = getMerchandise();

      }

      public List<Schema.FieldSetMember> getFields() {

        return SObjectType.Merchandise__c.FieldSets.Dimensions.getFields();

      }

      private Merchandise__c getMerchandise() {

        String query = 'SELECT ';

        for(Schema.FieldSetMember f : this.getFields()) {

           query += f.getFieldPath() + ', ';

        }

        query += 'Id, Name FROM Merchandise__c LIMIT 1';

        return Database.query(query);

      }

   }

```


Apex Reference Guide FieldSet Class

The Visualforce page using the above controller is simple:

```
   <apex:page controller="MerchandiseDetails">

      <apex:form >

       <apex:pageBlock title="Product Details">

         <apex:pageBlockSection title="Product">

            <apex:inputField value="{!merch.Name}"/>

         </apex:pageBlockSection>

         <apex:pageBlockSection title="Dimensions">

            <apex:repeat value="{!fields}" var="f">

              <apex:inputField value="{!merch[f.fieldPath]}"

                 required="{!OR(f.required, f.dbrequired)}"/>

            </apex:repeat>

         </apex:pageBlockSection>

        </apex:pageBlock>

      </apex:form>

   </apex:page>

```

One thing to note about the above markup is the expression used to determine if a field on the form should be indicated as being a
required field. A field in a field set can be required by either the field set definition, or the field’s own definition. The expression handles
both cases.

#### FieldSet Methods The following are methods for FieldSet . All are instance methods.

IN THIS SECTION:

##### getDescription()

Returns the field set’s description.

getFields()
Returns a list of `Schema.FieldSetMember` objects for the fields making up the field set.

getLabel()
Returns the translation of the text label that is displayed next to the field in the Salesforce user interface.

getName()
Returns the field set’s name.

getNamespace()
Returns the field set’s namespace.

getSObjectType()
Returns the `Schema.sObjectType` of the sObject containing the field set definition.

##### getDescription()

Returns the field set’s description.


Apex Reference Guide FieldSet Class

Signature

```
   public String getDescription()

```

Return Value

Type: `String`

Usage

Description is a required field for a field set, intended to describe the context and content of the field set. It’s often intended for
administrators who might be configuring a field set defined in a managed package, rather than for end users.

##### getFields()

Returns a list of `Schema.FieldSetMember` objects for the fields making up the field set.

Signature

```
   public List<FieldSetMember> getFields()

```

Return Value

Type: List<Schema.FieldSetMember>

##### getLabel()

Returns the translation of the text label that is displayed next to the field in the Salesforce user interface.

Signature

```
   public String getLabel()

```

Return Value

Type: `String`

##### getName()

Returns the field set’s name.

Signature

```
   public String getName()

```

Return Value

Type: `String`


### Apex Reference Guide FieldSetMember Class

##### getNamespace()

Returns the field set’s namespace.

Signature

```
   public String getNamespace()

```

Return Value

Type: `String`

Usage

The returned namespace is an empty string if your organization hasn’t set a namespace, and the field set is defined in your organization.
Otherwise, it’s the namespace of your organization, or the namespace of the managed package containing the field set.

##### getSObjectType()

Returns the `Schema.sObjectType` of the sObject containing the field set definition.

Signature

```
   public Schema.SObjectType getSObjectType()

```

Return Value

Type: `Schema.SObjectType`

### FieldSetMember Class

Contains methods for accessing the metadata for field set member fields.

Namespace

Schema

Usage

Use the methods in the `Schema.FieldSetMember` class to get details about fields contained within a field set, such as the field
label, type, a dynamic SOQL-ready field path, and so on. The following example shows how to get a collection of field set member
describe result objects for a specific field set on an sObject:

```
   List<Schema.FieldSetMember> fields =

      Schema.SObjectType.Account.fieldSets.getMap().get('field_set_name').getFields();

```


Apex Reference Guide FieldSetMember Class

If you know the name of the field set in advance, you can access its fields more directly using an explicit reference to the field set:

```
   List<Schema.FieldSetMember> fields =

      Schema.SObjectType.Account.fieldSets.field_set_name.getFields();

```

SEE ALSO:

FieldSet Class

#### FieldSetMember Methods The following are methods for FieldSetMember . All are instance methods.

IN THIS SECTION:

##### getDBRequired()

Returns `true` if the field is required by the field’s definition in its sObject, otherwise, `false` .

##### getFieldPath()

Returns a field path string in a format ready to be used in a dynamic SOQL query.

getLabel()
Returns the text label that’s displayed next to the field in the Salesforce user interface.

getRequired()
Returns `true` if the field is required by the field set, otherwise, `false` .

getType()
Returns the field’s Apex data type.

getSObjectField()
Returns the token for this field.

##### getDBRequired()

Returns `true` if the field is required by the field’s definition in its sObject, otherwise, `false` .

Signature

```
   public Boolean getDBRequired()

```

Return Value

Type: `Boolean`

##### getFieldPath()

Returns a field path string in a format ready to be used in a dynamic SOQL query.

Signature

```
   public String getFieldPath()

```


Apex Reference Guide FieldSetMember Class

Return Value

Type: `String`

Example

See Displaying a Field Set on a Visualforce Page for an example of how to use this method.

##### getLabel()

Returns the text label that’s displayed next to the field in the Salesforce user interface.

Signature

```
   public String getLabel()

```

Return Value

Type: `String`

##### getRequired()

Returns `true` if the field is required by the field set, otherwise, `false` .

Signature

```
   public Boolean getRequired()

```

Return Value

Type: `Boolean`

##### getType()

Returns the field’s Apex data type.

Signature

```
   public Schema.DisplayType getType()

```

Return Value

Type: `Schema.DisplayType`

##### getSObjectField()

Returns the token for this field.

Signature

```
   public Schema.sObjectField getSObjectField()

```


### Apex Reference Guide PicklistEntry Class

Return Value

Type: Schema.SObjectField

### PicklistEntry Class

Represents a picklist entry.

Namespace

Schema

Usage

Picklist fields contain a list of one or more items from which a user chooses a single item. They display as drop-down lists in the Salesforce
user interface. One of the items can be configured as the default item.

A `Schema.PicklistEntry` object is returned from the field describe result using the `getPicklistValues` method. For
example:

```
   Schema.DescribeFieldResult F = Account.Industry.getDescribe();

   List<Schema.PicklistEntry> P = F.getPicklistValues();

#### PicklistEntry Methods

### The following are methods for PicklistEntry . All are instance methods.

```

IN THIS SECTION:

##### getLabel()

Returns the display name of this item in the picklist.

getValue()
Returns the value of this item in the picklist.

isActive()
Returns `true` if this item must be displayed in the drop-down list for the picklist field in the user interface, `false` otherwise.

isDefaultValue()
Returns `true` if this item is the default value for the picklist, `false` otherwise. Only one item in a picklist can be designated as
the default.

##### getLabel()

Returns the display name of this item in the picklist.

Signature

```
   public String getLabel()

```


### Apex Reference Guide RecordTypeInfo Class

Return Value

Type: String

##### getValue()

Returns the value of this item in the picklist.

Signature

```
   public String getValue()

```

Return Value

Type: String

##### isActive()

Returns `true` if this item must be displayed in the drop-down list for the picklist field in the user interface, `false` otherwise.

Signature

```
   public Boolean isActive()

```

Return Value

Type: Boolean

##### isDefaultValue()

Returns `true` if this item is the default value for the picklist, `false` otherwise. Only one item in a picklist can be designated as the
default.

Signature

```
   public Boolean isDefaultValue()

```

Return Value

Type: Boolean

### RecordTypeInfo Class

Contains methods for accessing record type information for an sObject with associated record types.

Namespace

Schema


Apex Reference Guide RecordTypeInfo Class

Usage

A RecordTypeInfo object is returned from the sObject describe result using the `getRecordTypeInfos` method. For example:

```
   Schema.DescribeSObjectResult R = Account.SObjectType.getDescribe();

   List<Schema.RecordTypeInfo> RT = R.getRecordTypeInfos();

```

In addition to the `getRecordTypeInfos` method, you can use the `getRecordTypeInfosById` and the
`getRecordTypeInfosByName` methods. These methods return maps that associate RecordTypeInfo with record IDs and record
labels, respectively.

Example

The following example assumes at least one record type has been created for the Account object:

```
   RecordType rt = [SELECT Id,Name FROM RecordType WHERE SobjectType='Account' LIMIT 1];

   Schema.DescribeSObjectResult d = Schema.SObjectType.Account;

   Map<Id,Schema.RecordTypeInfo> rtMapById = d.getRecordTypeInfosById();

   Schema.RecordTypeInfo rtById = rtMapById.get(rt.id);

   Map<String,Schema.RecordTypeInfo> rtMapByName = d.getRecordTypeInfosByName();

   Schema.RecordTypeInfo rtByName = rtMapByName.get(rt.name);

   System.assertEquals(rtById,rtByName);

#### RecordTypeInfo Methods The following are methods for RecordTypeInfo . All are instance methods.

```

IN THIS SECTION:

getDeveloperName()
Returns the developer name for this record type.

getName()
Returns the UI label of this record type. The label can be translated into any language that Salesforce supports.

getRecordTypeId()
Returns the ID of this record type.

isActive()
Returns `true` if this record type is active, `false` otherwise.

isAvailable()
Returns `true` if this record type is available to the current user, `false` otherwise. Use this method to display a list of available
record types to the user when he or she is creating a new record.

isDefaultRecordTypeMapping()
Returns `true` if this is the default record type for the user, `false` otherwise.

isMaster()
Returns `true` if this is the master record type and `false` otherwise. The master record type is the default record type that’s used
when a record has no custom record type associated with it.


Apex Reference Guide RecordTypeInfo Class

##### getDeveloperName()

Returns the developer name for this record type.

Signature

```
   public String getDeveloperName()

```

Return Value

Type: String

##### getName()

Returns the UI label of this record type. The label can be translated into any language that Salesforce supports.

Signature

```
   public String getName()

```

Return Value

Type: String

##### getRecordTypeId()

Returns the ID of this record type.

Signature

```
   public ID getRecordTypeId()

```

Return Value

Type: ID

##### isActive()

Returns `true` if this record type is active, `false` otherwise.

Signature

```
   public Boolean isActive()

```

Return Value

Type: Boolean


### Apex Reference Guide SOAPType Enum

##### isAvailable()

Returns `true` if this record type is available to the current user, `false` otherwise. Use this method to display a list of available record
types to the user when he or she is creating a new record.

Signature

```
   public Boolean isAvailable()

```

Return Value

Type: Boolean

##### isDefaultRecordTypeMapping()

Returns `true` if this is the default record type for the user, `false` otherwise.

Signature

```
   public Boolean isDefaultRecordTypeMapping()

```

Return Value

Type: Boolean

##### isMaster()

Returns `true` if this is the master record type and `false` otherwise. The master record type is the default record type that’s used
when a record has no custom record type associated with it.

Signature

```
   public Boolean isMaster()

```

Return Value

Type: Boolean

### SOAPType Enum

A `Schema.SOAPType` enum value is returned by the field describe result `getSoapType` method.

Namespace

Schema

**Type Field Value** **What the Field Object Contains**

`anytype` Any value of the following types: `String`, `Boolean`, `Integer`, `Double`, `ID`, `Date` or
`DateTime` .


### Apex Reference Guide SObjectDescribeOptions Enum

**Type Field Value** **What the Field Object Contains**

`base64binary` Base64-encoded arbitrary binary data (of type base64Binary)

`Boolean` Boolean ( `true` or `false` ) values

`Date` Date values

`DateTime` DateTime values

`Double` Double values

`ID` Primary key field for an object

`Integer` Integer values

`String` String values

`Time` Time values

Usage

To programmatically retrieve the list of valid SOAPType enum values, use this code sample.

```
   system.debug(SoapType.values().size()); //Gets the number of supported values

   for (SoapType st : SoapType.values()) system.debug(st);

```

[For more information, see SOAPTypes in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/sforce_api_calls_describesobjects_describesobjectresult.htm#soaptype_topic) _SOAP API Developer Guide_ . For more information about the methods shared by all enums,
see Enum Methods.

### SObjectDescribeOptions Enum

A `Schema.SObjectDescribeOptions` enum value is a parameter in the `SObjectType.getDescribe` method.

Usage

For more information about the method using this enum, see `getDescribe(options)` .

Enum Values

The following are the values of the `Schema.SObjectDescribeOptions` enum.

**Value** **Description**

`DEFAULT` Either eager-load or lazy-load depending on the API version.

`DEFERRED` Lazy-load child relationships; do not load all child relationships at the time of first
invocation of the method.

`FULL` Eager-load all elements of the describe, including child relationships, up-front at
the time of method invocation.

See `getDescribe(options)` .


### Apex Reference Guide SObjectField Class SObjectField Class

A `Schema.sObjectField` object is returned from the field describe result using the `getController` and `getSObjectField`
methods.

Namespace

Schema

Example

```
   Schema.DescribeFieldResult F = Account.Industry.getDescribe();

   Schema.sObjectField T = F.getSObjectField();

#### sObjectField Methods The following are instance methods for sObjectField .

```

IN THIS SECTION:

##### getDescribe()

Returns the describe field result for this field.

##### getDescribe(options)

Returns the describe field result for this field. This method also provides an option to get all the describe field results for an object.

##### getDescribe()

Returns the describe field result for this field.

Signature

```
   public Schema.DescribeFieldResult getDescribe()

```

Return Value

Type: Schema.DescribeFieldResult

##### getDescribe(options)

Returns the describe field result for this field. This method also provides an option to get all the describe field results for an object.

Signature

```
   public Schema.DescribeFieldResult getDescribe(Object options)

```

Parameters

```
   options
```

Type: Object


### Apex Reference Guide SObjectType Class

Use this parameter to pass `FieldDescribeOptions.FULL_DESCRIBE` when a subset of system objects could have
different results for picklist values based on the context they're invoked in. This parameter computes all aspects of describe field
results.

For example, `AIConversationContext.PersonType` field is a picklist that contains a list of accessible object types.

Return Value

Type: Schema.DescribeFieldResult

### SObjectType Class

A `Schema.sObjectType` object is returned from the field describe result using the `getReferenceTo` method, or from the
sObject describe result using the `getSObjectType` method.

Namespace

Schema

Usage

```
   Schema.DescribeFieldResult F = Account.Industry.getDescribe();

   List<Schema.sObjectType> P = F.getReferenceTo();

#### SObjectType Methods

### The following are methods for SObjectType . All are instance methods.

```

IN THIS SECTION:

##### getDescribe()

Returns the describe sObject result for this field.

getDescribe(options)
Returns the describe sObject result for this field; the parameter value determines whether all child relationships are loaded up-front,
or not.

newSObject()
Constructs a new sObject of this type.

newSObject(id)
Constructs a new sObject of this type, with the specified ID.

newSObject(recordTypeId, loadDefaults)
Constructs a new sObject of this type, and optionally, of the specified record type ID and with default custom field values.

##### getDescribe()

Returns the describe sObject result for this field.


Apex Reference Guide SObjectType Class

Signature

```
   public Schema.DescribeSObjectResult getDescribe()

```

Return Value

Type: Schema.DescribeSObjectResult

##### getDescribe(options)

Returns the describe sObject result for this field; the parameter value determines whether all child relationships are loaded up-front, or
not.

Signature

```
   public Schema.DescribeSObjectResult getDescribe(Object options)

```

Parameters

```
   options
```

Type: Object

The parameter values determine how the elements of the describe operation are loaded.

**•** Use `SObjectDescribeOptions.FULL` to eager-load all elements of the describe, including child relationships, up-front
at the time of method invocation. This describe guarantees fully coherent results, even if the describe object is passed to another
namespace, API version, or other Apex context that may have different results when generating describe attributes.

**•** Use `SObjectDescribeOptions.DEFERRED` to enable lazy initialization of describe attributes on first use. This means
that all child relationships will not be loaded at the time of first invocation of the method.

**•** Use `SObjectDescribeOptions.DEFAULT` to default to either eager-load or lazy-load depending on the API version.

The type of describe operation, as determined by the parameter value is depicted in this table.

**Table 2: Type of Load for SObjectType.getDescribe()**

Return Value

Type: Schema.DescribeSObjectResult

##### newSObject()

Constructs a new sObject of this type.

Signature

```
   public sObject newSObject()

```


Apex Reference Guide SObjectType Class

Return Value

Type: sObject

Example

[For an example, see Dynamic DML.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_dml.htm)

##### newSObject(id)

Constructs a new sObject of this type, with the specified ID.

Signature

```
   public sObject newSObject(ID id)

```

Parameters

```
   id
```

Type: ID

Return Value

Type: sObject

Usage

For the argument, pass the ID of an existing record in the database.

After you create a new sObject, the sObject returned has all fields set to `null` . You can set any updateable field to desired values and
then update the record in the database. Only the fields you set new values for are updated and all other fields which are not system
fields are preserved.

##### newSObject(recordTypeId, loadDefaults)

Constructs a new sObject of this type, and optionally, of the specified record type ID and with default custom field values.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Signature

```
   public sObject newSObject(ID recordTypeId, Boolean loadDefaults)

```

Parameters

```
   recordTypeId
```

Type: ID

Specifies the record type ID of the sObject to create. If no record type exists for this sObject, use `null` . If the sObject has record
types and you specify `null`, the default record type is used.


Apex Reference Guide SObjectType Class

```
   loadDefaults
```

Type: Boolean

Specifies whether to populate custom fields with their predefined default values ( `true` ) or not ( `false` ).

Return Value

Type: sObject

Usage

**•** For required fields that have no default values, make sure to provide a value before inserting the new sObject. Otherwise, the insertion
results in an error. An example is the Account Name field or a master-detail relationship field.

**•** Since picklists and multi-select picklists can have default values specified per record type, this method populates the default value
corresponding to the record type specified.

**•** If fields have no predefined default values and the _`loadDefaults`_ argument is `true`, this method creates the sObject with field
values of `null` .

**•** If the _`loadDefaults`_ argument is `false`, this method creates the sObject with field values of `null` .

**•** This method populates read-only custom fields of the new sObject with default values. You can then insert the new sObject with
the read-only fields, even though these fields cannot be edited after they’re inserted.

**•** If a custom field is marked as unique and also provides a default value, inserting more than one new sObject will cause a run-time
exception because of duplicate field values.

To learn more about default field values, see “Default Field Values” in the Salesforce online help.

Note: You can also use this method to create a platform event with a prepopulated `EventUuid` field value for Apex publish
[callbacks. For more information, see Get the Result of Asynchronous Platform Event Publishing with Apex Publish Callbacks in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_publish_callbacks.htm)
_Platform Events Developer Guide_ .

Example: Creating New sObject with Default Values

This sample creates an account with any default values populated for its custom fields, if any, using the `newSObject` method. It also
creates a second account for a specific record type. For both accounts, the sample sets the Name field, which is a required field that
doesn’t have a default value, before inserting the new accounts.

```
   // Create an account with predefined default values

   Account acct = (Account)Account.sObjectType.newSObject(null, true);

   // Provide a value for Name

   acct.Name = 'Acme';

   // Insert new account

   insert acct;

   // This is for record type RT1 of Account

   ID rtId = [SELECT Id FROM RecordType WHERE sObjectType='Account' AND Name='RT1'].Id;

   Account acct2 = (Account)Account.sObjectType.newSObject(rtId, true);

   // Provide a value for Name

   acct2.Name = 'Acme2';

   // Insert new account

   insert acct2;

```


## Apex Reference Guide Search Namespace Search Namespace The Search namespace provides classes for getting search results and suggestion results. The following are the classes in the Search namespace.

IN THIS SECTION:

### KnowledgeSuggestionFilter Class

Filter settings that narrow the results from a call to `System.Search.suggest(searchQuery, sObjectType,`
`options)` when the SOSL search query contains a KnowledgeArticleVersion object.

QuestionSuggestionFilter Class
The `Search.QuestionSuggestionFilter` class filters results from a call to
`System.Search.suggest(searchQuery, sObjectType, options)` when the SOSL `searchQuery` contains
a `FeedItem` object.

SearchResult Class
A wrapper object that contains an sObject and search metadata.

SearchResults Class
Wraps the results returned by the `Search.find(String)` method.

SuggestionOption Class
Options that narrow record and article suggestion results returned from a call to `System.Search.suggest(String,`

`String, Search.SuggestionOption)` .

SuggestionResult Class
A wrapper object that contains an sObject.

SuggestionResults Class
Wraps the results returned by the `Search.suggest(String, String, Search.SuggestionOption)` method.

SEE ALSO:

find(searchQuery)

suggest(searchQuery, sObjectType, suggestions)

### KnowledgeSuggestionFilter Class

Filter settings that narrow the results from a call to `System.Search.suggest(searchQuery, sObjectType, options)`
when the SOSL search query contains a KnowledgeArticleVersion object.

Namespace

## Search

#### KnowledgeSuggestionFilter Methods

### The following are methods for KnowledgeSuggestionFilter .


Apex Reference Guide KnowledgeSuggestionFilter Class

IN THIS SECTION:

##### addArticleType(articleType)

Adds a filter that narrows suggestion results to display the specified article type. This filter is optional.

##### addDataCategory(dataCategoryGroupName, dataCategoryName)

Adds a filter that narrows suggestion results to display articles in the specified data category. This filter is optional.

addTopic(topic)
Specifies the article topic to return. This filter is optional.

setChannel(channelName)
Sets a channel to narrow the suggestion results to articles in the specified channel. This filter is optional.

setDataCategories(dataCategoryFilters)
Adds filters that narrow suggestion results to display articles in the specified data categories. Use this method to set multiple data
category group and name pairs in one call. This filter is optional.

setLanguage(localeCode)
Sets a language to narrow the suggestion results to display articles in that language. This filter value is required in calls to
`System.Search.suggest(String, String, Search.SuggestionOption)` .

setPublishStatus(publishStatus)
Sets a publish status to narrow the suggestion results to display articles with that status. This filter value is required in calls to
`System.Search.suggest(String, String, Search.SuggestionOption)` .

setValidationStatus(validationStatus)
Sets a validation status to narrow the suggestion results to display articles with that status. This filter is optional.

##### addArticleType(articleType)

Adds a filter that narrows suggestion results to display the specified article type. This filter is optional.

Signature

```
   public void addArticleType(String articleType)

```

Parameters

```
   articleType
```

Type: String

A three-character ID prefix indicating the desired article type.

Return Value

Type: void

Usage

To add more than 1 article type, call the method multiple times.

##### addDataCategory(dataCategoryGroupName, dataCategoryName)

Adds a filter that narrows suggestion results to display articles in the specified data category. This filter is optional.


Apex Reference Guide KnowledgeSuggestionFilter Class

Signature

```
   public void addDataCategory(String dataCategoryGroupName, String dataCategoryName)

```

Parameters

```
   dataCategoryGroupName
```

Type: String

The name of the data category group

```
   dataCategoryName
```

Type: String

The name of the data category.

Return Value

Type: void

Usage

To set multiple data categories, call the method multiple times. The name of the data category group and name of the data category
for desired articles, expressed as a mapping, for example,
`Search.KnowledgeSuggestionFilter.addDataCategory('Regions', 'Asia')` .

##### addTopic(topic)

Specifies the article topic to return. This filter is optional.

Signature

```
   public void addTopic(String topic)

```

Parameters

##### _`addTopic`_

Type: String

The name of the article topic.

Return Value

Type: void

Usage

To add more than 1 article topic, call the method multiple times.

##### setChannel(channelName)

Sets a channel to narrow the suggestion results to articles in the specified channel. This filter is optional.


Apex Reference Guide KnowledgeSuggestionFilter Class

Signature

```
   public void setChannel(String channelName)

```

Parameters

```
   channelName
```

Type: String

The name of a channel. Valid values are:

**•** `AllChannels` –Visible in all channels the user has access to

**•** `App` –Visible in the internal Salesforce Knowledge application

**•** `Pkb` –Visible in the public knowledge base

**•** `Csp` –Visible in the Customer Portal

**•** `Prm` –Visible in the Partner Portal

If `channel` isn’t specified, the default value is determined by the type of user.

**•** `Pkb` for a guest user

**•** `Csp` for a Customer Portal user

**•** `Prm` for a Partner Portal user

**•** `App` for any other type of user

If `channel` is specified, the specified value may not be the actual value requested, because of certain requirements.

**•** For guest, Customer Portal, and Partner Portal users, the specified value must match the default value for each user type. If the
values don’t match or `AllChannels` is specified, then `App` replaces the specified value.

**•** For all users other than guest, Customer Portal, and Partner Portal users:

**–** If `Pkb`, `Csp`, `Prm`, or `App` are specified, then the specified value is used.

**–** If `AllChannels` is specified, then `App` replaces the specified value.

Return Value

Type: void

##### setDataCategories(dataCategoryFilters)

Adds filters that narrow suggestion results to display articles in the specified data categories. Use this method to set multiple data category
group and name pairs in one call. This filter is optional.

Signature

```
   public void setDataCategories(Map dataCategoryFilters)

```

Parameters

```
   dataCategoryFilters
```

Type: Map

A map of data category group and data category name pairs.


Apex Reference Guide KnowledgeSuggestionFilter Class

Return Value

Type: void

##### setLanguage(localeCode)

Sets a language to narrow the suggestion results to display articles in that language. This filter value is required in calls to
`System.Search.suggest(String, String, Search.SuggestionOption)` .

Signature

```
   public void setLanguage(String localeCode)

```

Parameters

```
   localeCode
```

Type: String

A locale code. For example, `'en_US'` (English–United States), or `'es'` (Spanish).

Return Value

Type: void

SEE ALSO:

[Supported Locales](https://help.salesforce.com/HTViewHelpDoc?id=admin_supported_locales.htm&language=en_US)

##### setPublishStatus(publishStatus)

Sets a publish status to narrow the suggestion results to display articles with that status. This filter value is required in calls to
`System.Search.suggest(String, String, Search.SuggestionOption)` .

Signature

```
   public void setPublishStatus(String publishStatus)

```

Parameters

```
   publishStatus
```

Type: String

A publish status. Valid values are:

**•** `Draft` –Articles aren’t published in Salesforce Knowledge.

**•** `Online` –Articles are published in Salesforce Knowledge.

**•** `Archived` –Articles aren’t published and are available in Archived Articles view.

##### setValidationStatus(validationStatus)

Sets a validation status to narrow the suggestion results to display articles with that status. This filter is optional.


### Apex Reference Guide QuestionSuggestionFilter Class

Signature

```
   public void setValidationStatus(String validationStatus)

```

Parameters

```
   validationStatus
```

Type: String

An article validation status. These values are available in the `ValidationStatus` field on the KnowledgeArticleVersion object.

Return Value

Type: void

### QuestionSuggestionFilter Class

The `Search.QuestionSuggestionFilter` class filters results from a call to `System.Search.suggest(searchQuery,`
`sObjectType, options)` when the SOSL `searchQuery` contains a `FeedItem` object.

Namespace

Search

IN THIS SECTION:

#### QuestionSuggestionFilter Methods QuestionSuggestionFilter Methods

### The following are methods for QuestionSuggestionFilter .

IN THIS SECTION:

addGroupId(groupId)
Adds a filter to display questions associated with the single specified group whose ID is passed in as an argument. This filter is
optional.

addNetworkId(networkId)
Adds a filter to display questions associated with the single specified network whose ID is passed in as an argument. This filter is
optional.

addUserId(userId)
Adds a filter to display questions belonging to the single specified user whose ID is passed in as an argument. This filter is optional.

setGroupIds(groupIds)
Sets a new list of groups to replace the current list of groups where the group IDs are passed in as an argument. This filter is optional.

setNetworkIds(networkIds)
Sets a new list of networks to replace the current list of networks where the network IDs are passed in as an argument. This filter is
optional.


Apex Reference Guide QuestionSuggestionFilter Class

setTopicId(topicId)
Sets a filter to display questions associated with the single specified topic whose ID is passed in as an argument. This filter is optional.

setUserIds(userIds)
Sets a new list of users to replace the current list of users where the users IDs are passed in as an argument. This filter is optional.

##### addGroupId(groupId)

Adds a filter to display questions associated with the single specified group whose ID is passed in as an argument. This filter is optional.

Signature

```
   public void addGroupId(String groupId)

```

Parameters

```
   groupId
```

Type: String

The ID for a group.

Return Value

Type: void

Usage

To add more than one group, call the method multiple times.

##### addNetworkId(networkId)

Adds a filter to display questions associated with the single specified network whose ID is passed in as an argument. This filter is optional.

Signature

```
   public void addNetworkId(String networkId)

```

Parameters

```
   networkId
```

Type: String

The ID of the Experience Cloud site about which you’re retrieving this information.

Return Value

Type: void

Usage

To add more than one network, call the method multiple times.


Apex Reference Guide QuestionSuggestionFilter Class

##### addUserId(userId)

Adds a filter to display questions belonging to the single specified user whose ID is passed in as an argument. This filter is optional.

Signature

```
   public void addUserId(String userId)

```

Parameters

```
   userId
```

Type: String

The ID for the user.

Return Value

Type: void

Usage

To add more than one user, call the method multiple times.

##### setGroupIds(groupIds)

Sets a new list of groups to replace the current list of groups where the group IDs are passed in as an argument. This filter is optional.

Signature

```
   public void setGroupIds(List<String> groupIds)

```

Parameters

```
   groupIds
```

Type: List<String>

A list of group IDs.

Return Value

Type: void

##### setNetworkIds(networkIds)

Sets a new list of networks to replace the current list of networks where the network IDs are passed in as an argument. This filter is
optional.

Signature

```
   public void setNetworkIds(List<String> networkIds)

```


### Apex Reference Guide SearchResult Class

Parameters

```
   networkIds
```

Type: List<String>

A list of network IDs.

Return Value

Type: void

##### setTopicId(topicId)

Sets a filter to display questions associated with the single specified topic whose ID is passed in as an argument. This filter is optional.

Signature

```
   public void setTopicId(String topicId)

```

Parameters

```
   topicId
```

Type: String

The ID for a topic.

Return Value

Type: void

##### setUserIds(userIds)

Sets a new list of users to replace the current list of users where the users IDs are passed in as an argument. This filter is optional.

Signature

```
   public void setUserIds(List<String> userIds)

```

Parameters

```
   userIds
```

Type: List<String>

A list of user IDs.

Return Value

Type: void

### SearchResult Class

A wrapper object that contains an sObject and search metadata.


Apex Reference Guide SearchResult Class

Namespace

#### Search SearchResult Methods The following are methods for SearchResult .

IN THIS SECTION:

##### getSObject()

Returns an sObject from a SearchResult object.

##### getSnippet(fieldName)

Returns a snippet from a Case, Feed, or Knowledge Article SearchResult object based on the specified field name.

getSnippet()
Returns a snippet from a SearchResult object based on the default field.

##### getSObject()

Returns an sObject from a SearchResult object.

Signature

```
   public SObject getSObject()

```

Return Value

Type: SObject

SEE ALSO:

find(searchQuery)

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_sosl.htm)_ : Dynamic SOSL

##### getSnippet(fieldName)

Returns a snippet from a Case, Feed, or Knowledge Article SearchResult object based on the specified field name.

Signature

```
   public String getSnippet(String fieldName)

```

Parameters

```
   fieldName
```

Type: String

The field name to use for creating the snippet.

Valid values: `Case.Casenumber`, `FeedPost.Title`, `KnowledgeArticleVersion.Title`


### Apex Reference Guide SearchResults Class

Return Value

Type: String

SEE ALSO:

find(searchQuery)

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_sosl.htm)_ : Dynamic SOSL

##### getSnippet()

Returns a snippet from a SearchResult object based on the default field.

Signature

```
   public String getSnippet()

```

Return Value

Type: String

SEE ALSO:

find(searchQuery)

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_sosl.htm)_ : Dynamic SOSL

### SearchResults Class

Wraps the results returned by the `Search.find(String)` method.

Namespace

### Search

#### SearchResults Methods

### The following are methods for SearchResults .

IN THIS SECTION:

##### get(sObjectType)

Returns a list of `Search.SearchResult` objects that contain an sObject of the specified type.

##### get(sObjectType)

Returns a list of `Search.SearchResult` objects that contain an sObject of the specified type.

Signature

```
   public List<Search.SearchResult> get(String sObjectType)

```


### Apex Reference Guide SuggestionOption Class

Parameters

```
   sObjectType
```

Type: String

The name of an sObject in the dynamic SOSL query passed to the `Search.find(String)` method.

Return Value

Type: List<Search.SearchResult>

Usage

SOSL queries passed to the `Search.find(String)` method can return results for multiple objects. For example, the query
`Search.find('FIND \'map\' IN ALL FIELDS RETURNING Account, Contact, Opportunity')` includes
results for 3 objects. You can call `get(string)` to retrieve search results for 1 object at a time. For example, to get results for the
Account object, call `Search.SearchResults.get('Account')` .

SEE ALSO:

find(searchQuery)

SearchResult Methods

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dynamic_sosl.htm)_ : Dynamic SOSL

### SuggestionOption Class

Options that narrow record and article suggestion results returned from a call to `System.Search.suggest(String, String,`
`Search.SuggestionOption)` .

Namespace

Search

#### SuggestionOption Methods

### The following are methods for SuggestionOption .

IN THIS SECTION:

##### setFilter(knowledgeSuggestionFilter)

Set filters that narrow Salesforce Knowledge article results in a call to `System.Search.suggest(String, String,`
`Search.SuggestionOption)` .

setLimit(limit)
The maximum number of record or article suggestions to retrieve.

##### setFilter(knowledgeSuggestionFilter)

Set filters that narrow Salesforce Knowledge article results in a call to `System.Search.suggest(String, String,`
`Search.SuggestionOption)` .


Apex Reference Guide SuggestionOption Class

Signature

```
   public void setFilter(Search.KnowledegeSuggestionFilter knowledgeSuggestionFilter)

```

Parameters

```
   knowledgeSuggestionFilter
```

Type: KnowledgeSuggestionFilter

An object containing filters that narrow the search results.

Return Value

Type: void

Usage

```
   Search.KnowledgeSuggestionFilter filters = new Search.KnowledgeSuggestionFilter();

   filters.setLanguage('en_US');

   filters.setPublishStatus('Online');

   filters.setChannel('app');

   Search.SuggestionOption options = new Search.SuggestionOption();

   options.setFilter(filters);

   Search.SuggestionResults suggestionResults = Search.suggest('all', 'KnowledgeArticleVersion',

    options);

   for (Search.SuggestionResult searchResult : suggestionResults.getSuggestionResults()) {

     KnowledgeArticleVersion article = (KnowledgeArticleVersion)searchResult.getSObject();

     System.debug(article.title);

   }

##### setLimit(limit)

```

The maximum number of record or article suggestions to retrieve.

Signature

```
   public void setLimit(Integer limit)

```

Parameters

```
   limit
```

Type: Integer

The maximum number of record or article suggestions to retrieve.

Return Value

Type: void


### Apex Reference Guide SuggestionResult Class

Usage

By default, the `System.Search.suggest(String, String, Search.SuggestionOption)` method returns the
5 most relevant results. However, if your query is broad, it could match more than 5 results. If
`Search.SuggestionResults.hasMoreResults()` returns `true`, there are more than 5 results. To retrieve them, call
`setLimit(Integer)` to increase the number of suggestions results.

```
   Search.SuggestionOption option = new Search.SuggestionOption();

   option.setLimit(10);

   Search.suggest('my query', 'mySObjectType', option);

### SuggestionResult Class

```

A wrapper object that contains an sObject.

Namespace

Search

#### SuggestionResult Methods

### The following are methods for SuggestionResult .

IN THIS SECTION:

##### getSObject()

Returns the sObject from a SuggestionResult object.

##### getSObject()

Returns the sObject from a SuggestionResult object.

Signature

```
   public SObject getSObject()

```

Return Value

Type: SObject

### SuggestionResults Class

Wraps the results returned by the `Search.suggest(String, String, Search.SuggestionOption)` method.

Namespace

Search


## Apex Reference Guide setup_flow_performance Namespace

#### SuggestionResults Methods The following are methods for SuggestionResults .

IN THIS SECTION:

##### getSuggestionResults()

Returns a list of SuggestionResult objects from the response to a call to `Search.suggest(String, String,`
`Search.SuggestionOption)` .

##### hasMoreResults() Indicates whether a call to System.Search.suggest(String, String, Search.SuggestionOption) has

more results available than were returned.

##### getSuggestionResults()

Returns a list of SuggestionResult objects from the response to a call to `Search.suggest(String, String,`
`Search.SuggestionOption)` .

Signature

```
   public List<Search.SuggestionResult> getSuggestionResults()

```

Return Value

Type: List<SuggestionResult>

##### hasMoreResults()

Indicates whether a call to `System.Search.suggest(String, String, Search.SuggestionOption)` has more
results available than were returned.

Signature

```
   public Boolean hasMoreResults()

```

Return Value

Type: Boolean

Usage

If a limit isn’t specified, 5 records are returned in calls to `System.Search.suggest(String, String,`
##### Search.SuggestionOption) . If there are more suggested records than the limit specified, a call to hasMoreResults()

returns `true` .

## setup_flow_performance Namespace

The class and methods in this namespace are for internal use only.

## The following are the classes in the setup_flow_performance namespace.


### Apex Reference Guide FlowPerformanceSetupDetails Class

IN THIS SECTION:

### FlowPerformanceSetupDetails Class

The methods and properties in this class are for internal use only.

### FlowPerformanceSetupDetails Class

The methods and properties in this class are for internal use only.

Namespace

setup_flow_performance

## Sfc Namespace

The Sfc namespace contains classes used in Salesforce Files.

## The following are the classes in the Sfc namespace.

IN THIS SECTION:

### ContentDownloadContext Enum

This enum specifies the download context.

ContentDownloadHandler Class
Use ContentDownloadHandler to define a custom download handler that controls how content is downloaded.

ContentDownloadHandlerFactory Interface
Use this interface to provide a class factory that Salesforce can call to create instances of your custom ContentDownloadHandler.

### ContentDownloadContext Enum

This enum specifies the download context.

Usage

If the operationContext is `CONTENT`, `CHATTER`, `DELIVERY`, `S1`, or `MOBILE`, it can be used in a shepherd servlet as a query
parameter. It’s possible for a user to change the query parameters. If a user enters a value other than `CONTENT`, `CHATTER`, `DELIVERY`,
`S1`, or `MOBILE`, the value is treated as the default value `CONTENT` .

Users can’t set query parameters to `REST_API`, `SOQL`, or `RETRIEVE`, so these values can be assumed to be accurate.

Enum Values

The Sfc.ContentDownloadContext enum value identifies the content download context. The enum value is provided as a query parameter
in the file download servlet. The following are the values of the `Sfc.ContentDownloadContext` enum.

**Value** **Description**

`CHATTER` Download from Chatter.


### Apex Reference Guide ContentDownloadHandler Class

**Value** **Description**

`CONTENT` Default value. Downloads from the Salesforce CRM Content product.

`DELIVERY` Download of a content delivery.

`REST_API` Download from the Connect API ( `/connect/files/${fileId}/content`
endpoint). Used in both Android and iOS apps.

`RETRIEVE` Retrieve VersionData from SObject API.

`S1` Download from Lightning Experience.

`SOQL` Select VersionData from SOQL.

### ContentDownloadHandler Class

Use ContentDownloadHandler to define a custom download handler that controls how content is downloaded.

Namespace

Sfc on page 3463

IN THIS SECTION:

#### ContentDownloadHandler Properties ContentDownloadHandler Properties

### The following are properties for ContentDownloadHandler .

IN THIS SECTION:

##### downloadErrorMessage

A customized error message explaining why the download isn’t allowed.

isDownloadAllowed
Indicates whether or not download is allowed.

redirectUrl
The URL the user is redirected to when the download action isn't available, for applying Information Rights Management (IRM)
control, virus scanning, or other behavior.

##### downloadErrorMessage

A customized error message explaining why the download isn’t allowed.

Signature

```
   public String downloadErrorMessage {get; set;}

```


### Apex Reference Guide ContentDownloadHandlerFactory Interface

Property Value

Type: String

##### This message is used if a redirectUrl is not provided. If the download is not allowed, Salesforce will throw a

`ContentCustomizedDownloadException` exception that contains the `downloadErrorMessage` .

##### isDownloadAllowed

Indicates whether or not download is allowed.

Signature

```
   public Boolean isDownloadAllowed {get; set;}

```

Property Value

Type: Boolean

##### redirectUrl

The URL the user is redirected to when the download action isn't available, for applying Information Rights Management (IRM) control,
virus scanning, or other behavior.

Signature

```
   public String redirectUrl {get; set;}

```

Property Value

Type: String

The URL must be a valid relative URL. For example, the redirect can be a custom Visualforce page such as “/apex/IRMControl”. URLs with
no path, such as “www.domain.com”, results in an `InvalidParameterValueException` .

### ContentDownloadHandlerFactory Interface

Use this interface to provide a class factory that Salesforce can call to create instances of your custom ContentDownloadHandler.

Namespace

Sfc on page 3463

Usage

ContentDownloadHandler getContentDownloadHandler(List<ID> ids, ContentDownloadContext context);

IN THIS SECTION:

ContentDownloadHandlerFactory Methods

ContentDownloadHandlerFactory Example Implementation


Apex Reference Guide ContentDownloadHandlerFactory Interface

#### ContentDownloadHandlerFactory Methods The following are methods for ContentDownloadHandlerFactory .

IN THIS SECTION:

##### getContentDownloadHandler(var1, var2)

Returns a ContentDownloadHandler for a given list of content IDs and a download context.

##### getContentDownloadHandler(var1, var2)

Returns a ContentDownloadHandler for a given list of content IDs and a download context.

Signature

```
   public Sfc.ContentDownloadHandler getContentDownloadHandler(List<Id> var1,

   Sfc.ContentDownloadContext var2)

```

Parameters

```
   var1
```

Type: List<Id>

```
   var2
```

Type: Sfc.ContentDownloadContext on page 3463

Return Value

Type: Sfc.ContentDownloadHandler on page 3464

#### ContentDownloadHandlerFactory Example Implementation

This example creates a class that implements the `Sfc.ContentDownloadHandlerFactory` interface and returns a download
handler that blocks downloading content to mobile devices.

```
   // Allow customization of the content Download experience

   public class ContentDownloadHandlerFactoryImpl implements Sfc.ContentDownloadHandlerFactory

    {

     public Sfc.ContentDownloadHandler getContentDownloadHandler(List<ID> ids,

   Sfc.ContentDownloadContext context) {

      Sfc.ContentDownloadHandler contentDownloadHandler = new Sfc.ContentDownloadHandler();

      if(context == Sfc.ContentDownloadContext.MOBILE) {

       contentDownloadHandler.isDownloadAllowed = false;

       contentDownloadHandler.downloadErrorMessage = 'Downloading a file from a mobile

   device is not allowed.';

       return contentDownloadHandler;

      }

      contentDownloadHandler.isDownloadAllowed = true;

      return contentDownloadHandler;

```


## Apex Reference Guide Sfdc_Checkout Namespace

```
     }

   }

## Sfdc_Checkout Namespace

```

The Sfdc_Checkout namespace provides an interface and classes for B2B Commerce apps in Salesforce.

## The following are the classes in the Sfdc_Checkout namespace.

IN THIS SECTION:

### AsyncCartProcessor Interface

Use this interface to implement asynchronous integrations in B2B Commerce.

B2BCheckoutController Class
Communicate with simple checkout Apex methods to work with data related to B2B Commerce checkout.

IntegrationInfo Class
Provides the values that B2B Commerce Checkout uses to map requests to responses, necessary metadata, and context.

IntegrationStatus Class
Supports synchronous execution of Apex integrations for B2B Commerce. The implementation must return the status of the execution.

IntegrationStatus.Status Enum
The IntegrationStatus.Status enum describes the status of the current integration.

### AsyncCartProcessor Interface

Use this interface to implement asynchronous integrations in B2B Commerce.

Namespace

## Sfdc_Checkout

IN THIS SECTION:

#### AsyncCartProcessor Methods

AsyncCartProcessor Example Implementation

#### AsyncCartProcessor Methods

### The following are methods for AsyncCartProcessor .

IN THIS SECTION:

startCartProcessAsync(integrationInfo, cartId)
The startCartProcessAsync method is called asynchronously by the integration framework. Calling this method begins cart processing
for Commerce checkout.


### Apex Reference Guide B2BCheckoutController Class

##### startCartProcessAsync(integrationInfo, cartId)

The startCartProcessAsync method is called asynchronously by the integration framework. Calling this method begins cart processing
for Commerce checkout.

Signature

```
   public sfdc_checkout.IntegrationStatus

   startCartProcessAsync(sfdc_checkout.IntegrationInfo integrationInfo, Id cartId)

```

Parameters

```
   integrationInfo
```

Type: IntegrationInfo

Provides values that B2B Commerce checkout APIs use to map requests to responses, necessary metadata, and context.

```
   cartId
```

Type: Id

ID of the WebCart object.

Return Value

Type: IntegrationStatus

Status of the current integration. Possible values are `SUCCESS` and `FAILED` .

#### AsyncCartProcessor Example Implementation

This is an example implementation of the `sfdc_checkout.AsyncCartProcessor` interface.

```
   global interface checkout_AsyncCartProcessor {

     //Integration for async processing

     IntegrationStatus startCartProcessAsync(

       IntegrationInfo integrationInfo,

       Id cartId);

   }

```

AsyncCartProcessor is a base interface. There are four interfaces that extend it, including CartInventoryValidation, CartPriceCalculations,
CartShippingCharges, and CartTaxCalculations. For more information about these interfaces, including code examples and test classes,
[see Checkout Integrations.](https://github.com/forcedotcom/b2b-commerce-on-lightning-quickstart/tree/master/examples/checkout/integrations)

### B2BCheckoutController Class

Communicate with simple checkout Apex methods to work with data related to B2B Commerce checkout.

Namespace

sfdc_checkout


### Apex Reference Guide IntegrationInfo Class

Usage

You must specify the `sfdc_checkout` namespace when creating an instance of this class.

IN THIS SECTION:

#### B2BCheckoutController Methods B2BCheckoutController Methods The following are methods for B2BCheckoutController .

IN THIS SECTION:

##### licenseCompliance(cartId, orderId)

If you implement your own cart-to-order process without invoking the Cart to Order flow core action, you must invoke this method
to correctly track your orders for GMV (Gross Merchandise Value) recognition.

##### licenseCompliance(cartId, orderId)

If you implement your own cart-to-order process without invoking the Cart to Order flow core action, you must invoke this method to
correctly track your orders for GMV (Gross Merchandise Value) recognition.

Signature

```
   public static void licenseCompliance(String cartId, String orderId)

```

Parameters

```
   cartId
```

Type: String

The `cartId` of a web cart from which an order is created.

```
   orderId
```

Type: String

The `orderId` of the order you created from the cart.

Return Value

Type: Void

### IntegrationInfo Class

Provides the values that B2B Commerce Checkout uses to map requests to responses, necessary metadata, and context.

Namespace

sfdc_checkout on page 3467


Apex Reference Guide IntegrationInfo Class

Usage

This class provides information about a B2B Commerce integration. An instance of this class is passed as a parameter into the integration
interface.

IN THIS SECTION:

#### IntegrationInfo Properties IntegrationInfo Properties The following are properties for IntegrationInfo .

IN THIS SECTION:

##### integrationId

The unique ID of a B2B Commerce integration.

##### jobId

The ID of the job, specific to the Salesforce Background Operation framework.

##### siteLanguage

Site language to be used by third party services.

##### integrationId

The unique ID of a B2B Commerce integration.

Signature

```
   public String integrationId {get; set;}

```

Property Value

Type: String

##### jobId

The ID of the job, specific to the Salesforce Background Operation framework.

Signature

```
   public String jobId {get; set;}

```

Property Value

Type: String

##### siteLanguage

Site language to be used by third party services.


### Apex Reference Guide IntegrationStatus Class

Signature

```
   public String siteLanguage {get; set;}

```

Property Value

Type: String

### IntegrationStatus Class

Supports synchronous execution of Apex integrations for B2B Commerce. The implementation must return the status of the execution.

Namespace

sfdc_checkout

Usage

You must specify the `sfdc_checkout` namespace when creating an instance of this class.

IN THIS SECTION:

#### IntegrationStatus Properties IntegrationStatus Properties

### The following are properties for IntegrationStatus .

IN THIS SECTION:

##### status

Indicates the status of the integration process and whether or not it completed successfully.

##### status

Indicates the status of the integration process and whether or not it completed successfully.

Signature

```
   public sfdc_checkout.IntegrationStatus.Status status {get; set;}

```

Property Value

Type: sfdc_checkout.IntegrationStatus.Status on page 3471

### IntegrationStatus.Status Enum

The IntegrationStatus.Status enum describes the status of the current integration.


## Apex Reference Guide Sfdc_Enablement Namespace

Enum Values

The following are the values of the `sfdc_checkout.IntegrationStatus.Status` enum.

**Value** **Description**

`FAILED` Indicates transient, unknown error, managed by the implementor. The buyer can
retry this action.

`SUCCESS` Indicates the integration executed successfully.

## Sfdc_Enablement Namespace

The `sfdc_enablement` namespace provides classes for creating custom learning items to implement custom exercise types in
Enablement programs. Lightning web components are used to render the custom exercises on Program Builder.

The following are the classes in the `sfdc_enablement` namespace.

IN THIS SECTION:

### LearningEvaluation Class

Contains methods to retrieve and update details that are required to evaluate a learning item.

LearningEvaluationResult Class
Represents a user’s progress and progress status of a custom exercise in an Enablement program.

LearningItemEvaluationHandler Class
Contains methods to customize the evaluation process of a learning item.

LearningItemProgressStatus Enum
Represents the status of a user’s progress for a learning item in an Enablement program.

LearningItemSerializeDeserializer Class
Serializes and deserializes the content associated with a custom exercise when migrating an Enablement program from one org to
another.

### LearningEvaluation Class

Contains methods to retrieve and update details that are required to evaluate a learning item.

Namespace

sfdc_enablement

Usage

Pass this class as input to the sfdc_enablement.LearningEvaluationResult class.

Example

See example code in sfdc_enablement.LearningItemEvaluationHandler on page 3476.


Apex Reference Guide LearningEvaluation Class

IN THIS SECTION:

#### LearningEvaluation Methods LearningEvaluation Methods The following are methods for LearningEvaluation .

IN THIS SECTION:

##### getDetails()

Retrieves the details associated with the learning evaluation instance.

##### getLearningItemId()

Retrieves the record ID of the learning item that's associated with this learning evaluation instance.

##### setDetails(details)

Sets or updates the details of the learning item record for this learning evaluation instance.

setLearningItemId(learningItemId)
Sets or updates the learning item record ID for this learning evaluation instance.

##### **`getDetails()`**

Retrieves the details associated with the learning evaluation instance.

Signature

```
   public Map<String,Object> getDetails()

```

Return Value

Type: Map on page 3911<String,Object on page 3978>

##### **`getLearningItemId()`**

Retrieves the record ID of the learning item that's associated with this learning evaluation instance.

Signature

```
   public String getLearningItemId()

```

Return Value

Type: String

##### **`setDetails(details)`**

Sets or updates the details of the learning item record for this learning evaluation instance.


### Apex Reference Guide LearningEvaluationResult Class

Signature

```
   public void setDetails(Map<String,Object> details)

```

Parameters

```
   details
```

Type: Map<String,Object>

[The details of the learning item record that you get by calling evaluateLearningItem API.](https://developer.salesforce.com/docs/platform/lwc/guide/reference-evaluate-learning-item.html)

Return Value

Type: void

##### **`setLearningItemId(learningItemId)`**

Sets or updates the learning item record ID for this learning evaluation instance.

Signature

```
   public void setLearningItemId(String learningItemId)

```

Parameters

```
   learningItemId
```

Type: String

Return Value

Type: void

### LearningEvaluationResult Class

Represents a user’s progress and progress status of a custom exercise in an Enablement program.

Namespace

sfdc_enablement

Usage

To calculate the user’s progress through an exercise as a percentage and return the progress status, use the
`sfdc_enablement.LearningEvaluationResult` class inside the sfdc_enablement.LearningItemEvaluationHandler. In
your custom code, set the percentages to correspond to these sfdc_enablement.LearningItemProgressStatus on page 3478 enum values.

**•** `NotStarted` is equal to 0.00

**•** `InProgress` is from 0.01 through 99.99

**•** `Completed` is equal to 100.00


Apex Reference Guide LearningEvaluationResult Class

Example

See example code in sfdc_enablement.LearningItemEvaluationHandler on page 3476.

IN THIS SECTION:

#### LearningEvaluationResult Methods LearningEvaluationResult Methods The following are methods for LearningEvaluationResult .

IN THIS SECTION:

##### getLearningItemProgress()

Returns the progress percentage of the learning item.

##### getLearningItemProgressStatus()

Retrieves the progress status of the learning item.

setLearningItemProgress(learningItemProgress)
Sets the progress percentage of the learning item.

setLearningItemProgressStatus(learningItemProgressStatus)
Sets the progress status of the learning item.

##### **`getLearningItemProgress()`**

Returns the progress percentage of the learning item.

Signature

```
   public Double getLearningItemProgress()

```

Return Value

Type: Double

The progress percentage is formatted to two decimal places.

##### **`getLearningItemProgressStatus()`**

Retrieves the progress status of the learning item.

Signature

```
   public sfdc_enablement.LearningItemProgressStatus getLearningItemProgressStatus()

```

Return Value

Type: sfdc_enablement.LearningItemProgressStatus on page 3478


### Apex Reference Guide LearningItemEvaluationHandler Class

##### **`setLearningItemProgress(learningItemProgress)`**

Sets the progress percentage of the learning item.

Signature

```
   public void setLearningItemProgress(Double learningItemProgress)

```

Parameters

```
   learningItemProgress
```

Type: Double

The progress in percentage formatted to two decimal places.

Return Value

Type: void

##### **`setLearningItemProgressStatus(learningItemProgressStatus)`**

Sets the progress status of the learning item.

Signature

```
   public void setLearningItemProgressStatus(sfdc_enablement.LearningItemProgressStatus

   learningItemProgressStatus)

```

Parameters

```
   learningItemProgressStatus
```

Type: Sfdc_enablement.LearningItemProgressStatus on page 3478

Return Value

Type: void

### LearningItemEvaluationHandler Class

Contains methods to customize the evaluation process of a learning item.

Namespace

sfdc_enablement

Usage

[Extend this class and implement your custom progress evaluation method. Then link this class to a LearningItemType metadata record](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_learningitemtype.htm)
by passing the Apex class name to the `ApexEvaluationHandler` field.


Apex Reference Guide LearningItemEvaluationHandler Class

Example

This code updates a user’s progress when they take a custom screen flow exercise in an Enablement program. The code updates the
progress by checking the number of screens the user has navigated, calculating the progress percentage, and returning the progress
[status. See Track a User's Progress in a Custom Exercise from](https://developer.salesforce.com/docs/sales/enablement/guide/custom-exercise-track-progress.html) _Salesforce Developer Guide_ : Sales Programs and Partner Tracks with Enablement.

```
   global class ScreenFlowEvaluationHandler extends

   sfdc_enablement.LearningItemEvaluationHandler {

      global override sfdc_enablement.LearningEvaluationResult

   evaluate(sfdc_enablement.LearningEvaluation learningEvaluation) {

        sfdc_enablement.LearningEvaluationResult result = new

   sfdc_enablement.LearningEvaluationResult();

        Double percentage = 100.0d;

        Map<String, Object> details = learningEvaluation.getDetails();

        String currentScreen = (String) details.get('currentScreen');

        String allScreensString = (String) details.get('allScreens');

        List<String> allScreens = allScreensString.split(',');

        String status = (String) details.get('status');

        if (status == 'FINISHED') {

           percentage = 100;

        } else {

           Integer index = 0;

           for (Integer i = 0; i < allScreens.size(); i++) {

             if (allScreens.get(i).equals(currentScreen)) {

               index = i + 1;

               break;

             }

           }

           if (index == allScreens.size()) {

             percentage = 99.0d;

           } else {

             percentage = (Double.valueOf(index) / Double.valueOf(allScreens.size()))

   * 100.0d;

           }

        }

        result.setLearningItemProgress(percentage);

        if (percentage == 100.0d) {

   result.setLearningItemProgressStatus(sfdc_enablement.LearningItemProgressStatus.Completed);

        } else if (percentage == 0.0d) {

   result.setLearningItemProgressStatus(sfdc_enablement.LearningItemProgressStatus.NotStarted);

        } else {

   result.setLearningItemProgressStatus(sfdc_enablement.LearningItemProgressStatus.InProgress);

```


### Apex Reference Guide LearningItemProgressStatus Enum

```
        }

        return result;

      }

   }

```

IN THIS SECTION:

#### LearningItemEvaluationHandler Methods LearningItemEvaluationHandler Methods The following are methods for LearningItemEvaluationHandler .

IN THIS SECTION:

##### evaluate(learningEvaluation)

Contains the custom logic for evaluating a learning item.

##### **`evaluate(learningEvaluation)`**

Contains the custom logic for evaluating a learning item.

Signature

```
   public Sfdc_enablement.LearningEvaluationResult

   evaluate(Sfdc_enablement.LearningEvaluation learningEvaluation)

```

Parameters

```
   learningEvaluation
```

Type: Sfdc_enablement.LearningEvaluation on page 3472

The details of the learning item record to be evaluated.

Return Value

Type: Sfdc_enablement.LearningEvaluationResult on page 3474

The result of the evaluation, including progress and status details.

### LearningItemProgressStatus Enum

Represents the status of a user’s progress for a learning item in an Enablement program.

Usage

To set the progress status in the sfdc_enablement.LearningEvaluationResult on page 3474 class, use this enum.


### Apex Reference Guide LearningItemSerializeDeserializer Class

Enum Values

The following are the values for the `sfdc_enablement.LearningItemProgressStatus` enum.

**Value** **Description**

`NotStarted` The user hasn't started the custom exercise.

`InProgress` The user's custom exercise is in progress.

`Completed` The user completed the custom exercise.

### LearningItemSerializeDeserializer Class

Serializes and deserializes the content associated with a custom exercise when migrating an Enablement program from one org to
another.

Namespace

sfdc_enablement

Usage

The class contains methods to serialize and deserialize custom exercise content between orgs when an Enablement program that
includes a custom exercise is migrated from one org to another through change sets or packaging.

Extend the `sfdc_enablement.LearningItemSerializeDeserializer` Apex abstract class and add the class name
to the `ApexSerializerDeserializer` [field of the LearningItemType metadata record. If you don’t add the class name to the](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_learningitemtype.htm)
LearningItemType metadata record, the `customContent` property for the custom exercise is empty in the destination org and no
[corresponding LearningItem record is created for the exercise’s EnblProgramTaskDefinition record.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_enblprogramtaskdefinition.htm)

The serialize on page 3481 method serializes the custom content of the learning item from the source org. This method is called when
you retrieve custom content from the source org.

The deserialize on page 3481 method is called during the deployment of a program. This method takes the serialized custom content,
recreates the custom object record in the target org, and returns a new learning item record ID.

Example

The sample code serializes and deserializes the custom content for a given learning item of a custom screen flow exercise in an Enablement
program. For this example to work, make sure the screen flow exists in the target org.

```
   global class ScreenFlowSerializerDeserializer extends

   Sfdc_enablement.LearningItemSerializeDeserializer {

      // The serialize method returns the serialized output of the

      // learning item’s custom content.

      global override String serialize(String learningItemId) {

        // Get the screen flow record ID associated with the learning item.

        LearningItem learningItem = [SELECT ScreenFlow_Field__c from LearningItem where

   Id =: learningItemId LIMIT 1];

        String screenFlowRecordId = learningItem.ScreenFlow_Field__c;

        // Get the flow version ID associated with that screen flow.

```


Apex Reference Guide LearningItemSerializeDeserializer Class

```
        ScreenFlow_Object__c screenFlowRecord = [SELECT FlowVersionId__c from

   ScreenFlow_Object__c where Id =: screenFlowRecordId LIMIT 1];

        String flowVersionId = screenFlowRecord.FlowVersionId__c;

        // Query the flow definition associated with that flow version.

        // Get the information you need to recreate the custom object

        // record in the destination org.

        // In this example, we're only getting the API name of the

        // flow version.

        FlowDefinitionView flowDefinitionView = [SELECT ApiName from FlowDefinitionView

   where ActiveVersionId =: flowVersionId LIMIT 1];

        // Return the serialized string.

        // In this example, we're only returning the API name of the flow

        // definition in the string.

        return flowDefinitionView.ApiName;

      }

      // The deserialize method deserializes the string containing the custom

      // content. In the method, you recreate the custom object record

      // for the destination org and populate it with the custom content.

      // Then insert the record in the destination org and return the new

      // custom object record ID.

      global override String deserialize(String serializedOutput) {

        // Find the flow active version ID of the same screen flow in the

        // destination org.

        FlowDefinitionView flowDefinitionView = [SELECT ActiveVersionId from

   FlowDefinitionView where ApiName =: serializedOutput LIMIT 1];

        String flowActiveVersionId = flowDefinitionView.ActiveVersionId;

        // Create the screen flow custom object record using the

        // information you passed to the string in the serialize method.

        // In this example, we only passed the API name of the screen flow

        // to the string.

        ScreenFlow_Object__c screenFlowRecord = new ScreenFlow_Object__c();

        screenFlowRecord.Name = serializedOutput;

        screenFlowRecord.FlowVersionId__c = flowActiveVersionId;

        // Insert the custom object record into the destination org.

        insert screenFlowRecord;

        // Return the new screen flow record ID for the new learning item

        // in the destination org.

        return screenFlowRecord.Id;

      }

   }

```

IN THIS SECTION:

LearningItemSerializeDeserializer Methods


Apex Reference Guide LearningItemSerializeDeserializer Class

#### LearningItemSerializeDeserializer Methods The following are methods for LearningItemSerializeDeserializer .

IN THIS SECTION:

##### deserialize(serializedOutput)

Deserializes the provided custom content string and returns the record ID of the learning item.

##### serialize(learningItemId)

Serializes the custom content associated with the specified learning item. The serialized string represents the metadata of the custom
content and is used to recreate the custom content in the target Salesforce org during deployment.

##### **`deserialize(serializedOutput)`**

Deserializes the provided custom content string and returns the record ID of the learning item.

Signature

```
   public String deserialize(String serializedOutput)

```

Parameters

```
   serializedOutput
```

Type: String

The serialized information of custom content associated with a learning item The serialize(learningItemId) on page 3481 method
returns this information as a string that is less than or equal to 250 characters.

Return Value

Type: String

The ID of the learning item created for the target org.

##### **`serialize(learningItemId)`**

Serializes the custom content associated with the specified learning item. The serialized string represents the metadata of the custom
content and is used to recreate the custom content in the target Salesforce org during deployment.

Signature

```
   public String serialize(String learningItemId)

```

Parameters

```
   learningItemId
```

Type: String

The ID of the learning item associated with the custom content to be serialized.


## Apex Reference Guide sfdc_surveys Namespace

Return Value

Type: String

The serialized information of the custom content of the specified learning item. The format is a string that’s less than or equal to 250
characters long.

## sfdc_surveys Namespace The sfdc_surveys namespace provides an interface for shortening survey invitations. The following are the classes in the sfdc_surveys namespace.

IN THIS SECTION:

### SurveyInvitationLinkShortener Interface

Use this interface to provide a class factory that Salesforce can call to create instances of your custom
### SurveyInvitationLinkShortener .

Example Implementation to Associate SurveySubjects with SurveyInvitation and SurveyResponses
If no survey responses are populated, create a custom code to associate SurveySubjects with SurveyInvitation and SurveyResponses.

### SurveyInvitationLinkShortener Interface

Use this interface to provide a class factory that Salesforce can call to create instances of your custom
### SurveyInvitationLinkShortener .

Namespace

## sfdc_surveys

Usage

### Implement an instance of the SurveyInvitationLinkShortener interface to shorten the survey invitation that can be

distributed as short URLs over customer engaged channels, such as SMS, WhatsApp, or Facebook Messenger.

Special access rules

To implement this interface, you must have the Salesforce Feedback Management license enabled in your Salesforce organization.

IN THIS SECTION:

#### SurveyInvitationLinkShortener Methods

SurveyInvitationLinkShortener Example Implementation

#### SurveyInvitationLinkShortener Methods

### The following are methods for SurveyInvitationLinkShortener .


Apex Reference Guide SurveyInvitationLinkShortener Interface

IN THIS SECTION:

##### getShortenedURL(var1)

Returns a shortened URL for a given survey invitation.

##### **`getShortenedURL(var1)`**

Returns a shortened URL for a given survey invitation.

Signature

```
   public String getShortenedURL(String var1)

```

Parameters

```
   var1
```

Type: String

Return Value

Type: String

#### SurveyInvitationLinkShortener Example Implementation

This is an example implementation of the `sfdc_surveys.SurveyInvitationLinkShortener` interface.

[This sample code uses Named Credentials for authentication. For more information on Named Credentials, see Named Credentials as](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_callouts_named_credentials.htm)
[Callout Endpoints.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_callouts_named_credentials.htm)

```
   public class SurveyInvitationLinkShortenerImpl implements

   sfdc_surveys.SurveyInvitationLinkShortener {

     public String getShortenedURL(String invitationURL) {

       return shortenUrlUsingBitlyService(invitationURL);

     }

     public String shortenUrlUsingBitlyService(String invitationURL) {

       HttpRequest request = new HttpRequest();

       request.setEndpoint('callout:bitly/v4/shorten');

       request.setMethod('POST');

       request.setHeader('Authorization', 'Bearer {!$Credential.Password}');

       request.setHeader('Accept', 'application/json');

       request.setHeader('Content-Type', 'application/json');

       request.setBody(JSON.serialize(new Map<String, Object>{

       'group_guid' => '{!$Credential.UserName}',

       'long_url' => invitationURL

       }));

       Http http = new Http();

       HttpResponse res = http.send(request);

       Object result = JSON.deserializeUntyped(res.getBody());

       if (result instanceof Map<String, Object>) {

         Map<String, Object> resultMap = (Map<String, Object>) result;

```


### Apex Reference Guide Example Implementation to Associate SurveySubjects with

SurveyInvitation and SurveyResponses

```
         Object shortenedLinkVal = resultMap.get('link');

         if(shortenedLinkVal != null && shortenedLinkVal instanceof String) {

           return (String) shortenedLinkVal;

         }

       }

       return invitationURL;

     }

   }

### Example Implementation to Associate SurveySubjects with SurveyInvitation
```

and SurveyResponses

If no survey responses are populated, create a custom code to associate SurveySubjects with SurveyInvitation and SurveyResponses.

This example shows how to associate SurveySubjects with SurveyInvitation and SurveyResponses.

```
   public class CreateEntriesInSurveyInvitationRespRL {

      // Utility to create SurveyInvitation and SurveySubject record

      public static void addEntry(String associatedRecordId, String surveyId, String

   participantId) {

        String invitationId = createSurveyInvitation(surveyId, participantId);

        createSurveySubject(invitationId, associatedRecordId);

      }

      // Create an unauthenticated invitation by setting the surveyId and participantId

      private static String createSurveyInvitation(String surveyId, String participantId) {

        SurveyInvitation surveyInv = new SurveyInvitation();

        surveyInv.Name = 'SurveyInvitationForCase'; // add your survey invitation name

   here

        surveyInv.ParticipantId = participantId;

        surveyInv.CommunityId = '0DBRM0000004n4y'; //add your community id here

        surveyInv.OptionsAllowGuestUserResponse = true;

        surveyInv.SurveyId = surveyId;

        // Insert the SurveyInvitation Record

        insert surveyInv;

        return surveyInv.Id;

      }

      // Associate the above invitation to the required record (eg: Case, Opportunity...)

     private static void createSurveySubject(String invitationId, String associatedRecordId)

    {

        SurveySubject subj = new SurveySubject();

        subj.Name = 'Sur_Subject_for_invitation';

       subj.ParentId = invitationId; // similary you can use survey response id to associate

    survey subject to a response record.

        subj.SubjectId = associatedRecordId;

        // Insert the SurveySubject Record

        insert subj;

```


## Apex Reference Guide Site Namespace

```
      }

   }

   //Use this trigger to create a survey subject record associated to

   //the Survey Response record

   trigger SurveyResponseForCaseTrigger on SurveyResponse (after insert) {

      System.debug('Inside Survey response trigger ');

      for(SurveyResponse sr: Trigger.New)

      {

       SurveySubject subj = new SurveySubject();

        subj.Name = 'Sur_Subject_for_response';

        subj.ParentId = sr.id; //Associating survey response id

        //Get the associatedRecordId recordId (like Case, Opportunity etc) using the

   SurveyInvitation Id and

        //assigning it to SubjectId, assuming we inserted SurveySubject record for the

   associated invitation

        //using the previous code

        List<SurveySubject> SurSubj=[select subjectid from SurveySubject where parentid =

   :sr.invitationId];

        for(SurveySubject sub:SurSubj){

           String ids=String.valueOf(sub.subjectid).substring(0,3);

           if('500'.equals(ids)){

             subj.SubjectId =sub.subjectid;

        // Insert the SurveySubject Record

           insert subj;

             break;

           }

   }

## Site Namespace The Site namespace provides an interface for rewriting Sites URLs. The following is the interface in the Site namespace.

```

IN THIS SECTION:

UrlRewriter Interface
Enables rewriting Sites URLs.

Site Exceptions
## The Site namespace contains an exception class.


### Apex Reference Guide UrlRewriter Interface UrlRewriter Interface

Enables rewriting Sites URLs.

Namespace

Site

Usage

Sites provides built-in logic that helps you display user-friendly URLs and links to site visitors. Create rules to rewrite URL requests typed
into the address bar, launched from bookmarks, or linked from external websites. You can also create rules to rewrite the URLs for links
within site pages. URL rewriting not only makes URLs more descriptive and intuitive for users, it allows search engines to better index
your site pages.

For example, let's say that you have a blog site. Without URL rewriting, a blog entry's URL might look like this:

```
   https://myblog.my.salesforce-sites.com/posts?id=003D000000Q0PcN

```

To rewrite URLs for a site, create an Apex class that maps the original URLs to user-friendly URLs, and then add the Apex class to your
site.

#### UrlRewriter Methods

### The following are methods for UrlRewriter . All are instance methods.

IN THIS SECTION:

##### generateUrlFor(salesforceUrls)

Maps a list of Salesforce URLs to a list of user-friendly URLs.

mapRequestUrl(userFriendlyUrl)
Maps a user-friendly URL to a Salesforce URL.

##### generateUrlFor(salesforceUrls)

Maps a list of Salesforce URLs to a list of user-friendly URLs.

Signature

```
   public System.PageReference[] generateUrlFor(System.PageReference[] salesforceUrls)

```

Parameters

```
   salesforceUrls
```

Type: System.PageReference[]

Return Value

Type: System.PageReference[]


### Apex Reference Guide Site Exceptions

Usage

You can use `List<PageReference>` instead of `PageReference[]`, if you prefer.

Important: The size and order of the input list of Salesforce URLs must exactly correspond to the size and order of the generated
list of user-friendly URLs. The `generateUrlFor` method maps input URLs to output URLs based on the order in the lists.

##### mapRequestUrl(userFriendlyUrl)

Maps a user-friendly URL to a Salesforce URL.

Signature

```
   public System.PageReference mapRequestUrl(System.PageReference userFriendlyUrl)

```

Parameters

```
   userFriendlyUrl
```

Type: System.PageReference

Return Value

Type: System.PageReference

### Site Exceptions The Site namespace contains an exception class.

All exception classes support built-in methods for returning the error message and exception type. See Exception Class and Built-In
Exceptions.

### The Site namespace contains this exception:

**Exception** **Description** **Methods**

`Site.ExternalUserCreateException` Unable to create
external user

## Slack Namespace

Use the `String getMessage()` to get the error message
and write it to debug log.

Use `List<String> getDisplayMessages()` to get
a list of errors displayed to the end user.

This exception can’t be subclassed or thrown in code.

## The Slack Namespace provides tools designed to accelerate and ease the process of developing Slack apps on the Salesforce platform. The following are the classes in the Slack namespace.

[App Class](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_client_access.html)

[Action Class](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_dispatchers.html)

[AppClient](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_client.html)


Apex Reference Guide Slack Namespace

[AppRequest Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_apprequest.html)

[Apps Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_apps.html)

[Auth Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_auth.html)

[BotClient Class](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_client_bot.html)

[BotsInfo Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_bot.html)

[Call Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_calls.html)

[Channel Class](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_channels.html)

[Chat Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_chat.html)

[Conversation Class](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_conversations.html)

[Dnd Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_dnd.html)

[Emoji CLasses](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_emojis.html)

[Event Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_events.html)

[Field Class](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_fields.html)

[File Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_files.html)

[Latest Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_latest.html)

[Message Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_messages.html)

[MigrationExchange Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_migrationexc.html)

[Modals Class](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_modal.html)

[Options Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_options.html)

[Paging Class](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_paging.html)

[Pin Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_pins.html)

[Purpose Class](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_purpose.html)

[Reaction Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_reactions.html)

[Reminder Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_reminders.html)

[RequestContext Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_requestcontext.html)

[ResponseMetadata Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_response_metadata.html)

[RunnableHandler Interface](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_runnablehandler.html)

[Search Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_search.html)

[Shortcut Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_shortcut.html)

[SlackCommand Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_slashcommand.html)

[Star Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_stars.html)

[Team Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_teams.html)

[TestHarness Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_testharness.html)

[Topic Class](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_topics.html)

[User Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_users.html)

[UserClient Class](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_client_user.html)

[Usergroup Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_usergroups.html)


## Apex Reference Guide Support Namespace

[UserMapping Service Class](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_usermapping_service.html)

[Views Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_views.html)

[Workflow Classes](https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref_workflows.html)

## Support Namespace The Support namespace provides an interface used for Case Feed. The following is the interface in the Support namespace.

IN THIS SECTION:

### EmailTemplateSelector Interface

The `Support.EmailTemplateSelector` interface enables providing default email templates in Case Feed. With default
email templates, specified email templates are preloaded for cases based on criteria such as case origin or subject.

MilestoneTriggerTimeCalculator Interface
The `Support.MilestoneTriggerTimeCalculator` interface calculates the time trigger for a milestone.

### EmailTemplateSelector Interface

The `Support.EmailTemplateSelector` interface enables providing default email templates in Case Feed. With default email
templates, specified email templates are preloaded for cases based on criteria such as case origin or subject.

`Support.EmailTemplateSelector` works only in Salesforce Classic, not in Lightning Experience. Lightning Experience users
can specify default values for emails using the `QuickActionDefaultsHandler` interface.

Namespace

## Support

To specify default templates, you must create a class that implements `Support.EmailTemplateSelector` .

When you implement this interface, provide an empty parameterless constructor.

IN THIS SECTION:

#### EmailTemplateSelector Methods

EmailTemplateSelector Example Implementation

#### EmailTemplateSelector Methods

### The following are methods for EmailTemplateSelector .

IN THIS SECTION:

getDefaultTemplateId(caseId)
Returns the ID of the email template to preload for the case currently being viewed in the case feed using the specified case ID.


Apex Reference Guide EmailTemplateSelector Interface

##### getDefaultTemplateId(caseId)

Returns the ID of the email template to preload for the case currently being viewed in the case feed using the specified case ID.

Signature

```
   public ID getDefaultTemplateId(ID caseId)

```

Parameters

```
   caseId
```

Type: ID

Return Value

Type: ID

#### EmailTemplateSelector Example Implementation

This is an example implementation of the `Support.EmailTemplateSelector` interface.

The `getDefaultEmailTemplateId` method implementation retrieves the subject and description of the case corresponding
to the specified case ID. Next, it selects an email template based on the case subject and returns the email template ID.

```
   global class MyCaseTemplateChooser implements Support.EmailTemplateSelector {

      // Empty constructor

      global MyCaseTemplateChooser() { }

      // The main interface method

      global ID getDefaultEmailTemplateId(ID caseId) {

        // Select the case we're interested in, choosing any fields that are relevant to

   our decision

        Case c = [SELECT Subject, Description FROM Case WHERE Id=:caseId];

        EmailTemplate et;

        if (c.subject.contains('LX-1150')) {

           et = [SELECT id FROM EmailTemplate WHERE DeveloperName = 'LX1150_template'];

        } else if(c.subject.contains('LX-1220')) {

           et = [SELECT id FROM EmailTemplate WHERE DeveloperName = 'LX1220_template'];

        }

        // Return the ID of the template selected

        return et.id;

      }

   }

```

The following example tests the above code:

```
   @isTest

   private class MyCaseTemplateChooserTest {

      static testMethod void testChooseTemplate() {

```


### Apex Reference Guide MilestoneTriggerTimeCalculator Interface

```
        MyCaseTemplateChooser chooser = new MyCaseTemplateChooser();

        // Create a simulated case to test with

        Case c = new Case();

        c.Subject = 'I\'m having trouble with my LX-1150';

        Database.insert(c);

        // Make sure the proper template is chosen for this subject

        Id actualTemplateId = chooser.getDefaultEmailTemplateId(c.Id);

        EmailTemplate expectedTemplate =

         [SELECT id FROM EmailTemplate WHERE DeveloperName = 'LX1150_template'];

        Id expectedTemplateId = expectedTemplate.Id;

        System.assertEquals(actualTemplateId, expectedTemplateId);

        // Change the case properties to match a different template

        c.Subject = 'My LX1220 is overheating';

        Database.update(c);

        // Make sure the correct template is chosen in this case

        actualTemplateId = chooser.getDefaultEmailTemplateId(c.Id);

        expectedTemplate =

         [SELECT id FROM EmailTemplate WHERE DeveloperName = 'LX1220_template'];

        expectedTemplateId = expectedTemplate.Id;

        System.assertEquals(actualTemplateId, expectedTemplateId);

      }

   }

### MilestoneTriggerTimeCalculator Interface

```

The `Support.MilestoneTriggerTimeCalculator` interface calculates the time trigger for a milestone.

Namespace

Support

Implement the `Support.MilestoneTriggerTimeCalculator` interface to calculate a dynamic time trigger for a milestone
based on the milestone type, the properties of the case, and case-related objects. To implement the
`Support.MilestoneTriggerTimeCalculator` interface, you must first declare a class with the `implements` keyword
as follows:

```
   global class Employee implements Support.MilestoneTriggerTimeCalculator {

```

Next, your class must provide an implementation for the following method:

```
   global Integer calculateMilestoneTriggerTime(String caseId, String milestoneTypeId)

```

The implemented method must be declared as `global` or `public` .

IN THIS SECTION:

MilestoneTriggerTimeCalculator Methods

MilestoneTriggerTimeCalculator Example Implementation


Apex Reference Guide MilestoneTriggerTimeCalculator Interface

#### MilestoneTriggerTimeCalculator Methods The following are instance methods for MilestoneTriggerTimeCalculator .

IN THIS SECTION:

##### calculateMilestoneTriggerTime(caseId, milestoneTypeId)

Calculates the milestone trigger time based on the specified case and milestone type and returns the time in minutes.

##### calculateMilestoneTriggerTime(caseId, milestoneTypeId)

Calculates the milestone trigger time based on the specified case and milestone type and returns the time in minutes.

Syntax

```
   public Integer calculateMilestoneTriggerTime(String caseId, String milestoneTypeId)

```

Parameters

```
   caseId
```

Type: String

ID of the case the milestone is applied to.

```
   milestoneTypeId
```

Type: String

ID of the milestone type.

Return Value

Type: Integer

The calculated trigger time in minutes.

#### MilestoneTriggerTimeCalculator Example Implementation

This sample class demonstrates the implementation of the `Support.MilestoneTriggerTimeCalculator` interface. In this
sample, the case’s priority and the milestone `m1` determine that the time trigger is 18 minutes.

```
   global class myMilestoneTimeCalculator implements Support.MilestoneTriggerTimeCalculator

   {

      global Integer calculateMilestoneTriggerTime(String caseId, String milestoneTypeId){

        Case c = [SELECT Priority FROM Case WHERE Id=:caseId];

        MilestoneType mt = [SELECT Name FROM MilestoneType WHERE Id=:milestoneTypeId];

        if (c.Priority != null && c.Priority.equals('High')){

            if (mt.Name != null && mt.Name.equals('m1')) { return 7;}

            else { return 5; }

        }

        else {

           return 18;

        }

```


## Apex Reference Guide System Namespace

```
      }

   }

```

This test class can be used to test the implementation of `Support.MilestoneTriggerTimeCalculator` .

```
   @isTest

   private class MilestoneTimeCalculatorTest {

      static testMethod void testMilestoneTimeCalculator() {

        // Select an existing milestone type to test with

        MilestoneType[] mtLst = [SELECT Id, Name FROM MilestoneType LIMIT 1];

        if(mtLst.size() == 0) { return; }

        MilestoneType mt = mtLst[0];

        // Create case data.

        // Typically, the milestone type is related to the case,

        // but for simplicity, the case is created separately for this test.

        Case c = new Case(priority = 'High');

        insert c;

        myMilestoneTimeCalculator calculator = new myMilestoneTimeCalculator();

        Integer actualTriggerTime = calculator.calculateMilestoneTriggerTime(c.Id, mt.Id);

        if(mt.name != null && mt.Name.equals('m1')) {

           System.assertEquals(actualTriggerTime, 7);

        }

        else {

           System.assertEquals(actualTriggerTime, 5);

        }

        c.priority = 'Low';

        update c;

        actualTriggerTime = calculator.calculateMilestoneTriggerTime(c.Id, mt.Id);

        System.assertEquals(actualTriggerTime, 18);

      }

   }

## System Namespace The System namespace provides classes and methods for core Apex functionality. The following are the classes in the System namespace.

```

IN THIS SECTION:

AccessLevel Class
Defines the different modes, such as system or user mode, that Apex database operations execute in.

AccessType Enum
Specifies the access check type for the fields of an sObject.

Address Class
Contains methods for accessing the component fields of address compound fields.


Apex Reference Guide System Namespace

Answers Class
Represents zone answers.

ApexPages Class
Use `ApexPages` to add and check for messages associated with the current page, as well as to reference the current page.

Approval Class
Contains methods for processing approval requests and setting approval-process locks and unlocks on records.

Assert Class
Contains methods to assert various conditions with test methods, such as whether two values are the same, a condition is true, or
a variable is null.

AsyncInfo Class
Provides methods to get the current stack depth, maximum stack depth, and the minimum queueable delay for Queueable
transactions, and to determine if maximum stack depth is set.

AsyncOptions Class
Contains maximum stack depths for queueable transactions and the minimum queueable delay in minutes. Passed as parameter
to the `System.enqueueJob()` method to define a unique queueable job signature, the maximum stack depth for queueable
transactions and the minimum queueable delay in minutes.

Blob Class
Contains methods for the Blob primitive data type.

Boolean Class
Contains methods for the Boolean primitive data type.

BusinessHours Class
Use the `BusinessHours` methods to set the business hours at which your customer support team operates.

CallbackStatus Enum
Specifies the status of asynchronous requests to an external system.

Callable Interface
Enables developers to use a common interface to build loosely coupled integrations between Apex classes or triggers, even for code
in separate packages. Agreeing upon a common interface enables developers from different companies or different departments
to build upon one another’s solutions. Implement this interface to enable the broader community, which might have different
solutions than the ones you had in mind, to extend your code’s functionality.

Cases Class
Use the `Cases` class to interact with case records.

Collator Class
Contains methods to get locale-specific instances that can be used for comparisons and sorting. Use the `getInstance()`
method to obtain the Collator instance for a given locale and pass the Collator as the Comparator parameter to the `list.sort()`
method.

Comparable Interface
Adds sorting support for Lists that contain non-primitive types, that is, Lists of user-defined types. Your implementation must explicitly
handle null inputs in the `compareTo()` method to avoid a null pointer exception.

Comparator Interface
Implement different sort orders with the Comparator interface’s `compare()` method, and pass the Comparator as a parameter
to `List.sort()` . Your implementation must explicitly handle null inputs in the `compare()` method to avoid a null pointer
exception.


Apex Reference Guide System Namespace

Continuation Class
Use the `Continuation` class to make callouts asynchronously to a SOAP or REST Web service.

Cookie Class
The `Cookie` class lets you access cookies for your Salesforce site using Apex.

Crypto Class
Provides methods for creating digests, message authentication codes, and signatures, as well as encrypting and decrypting information.

Custom Metadata Type Methods
Custom metadata types are customizable, deployable, packageable, and upgradeable application metadata. All custom metadata
is exposed in the application cache, which allows access without repeated queries to the database. The metadata is then available
for formula fields, validation rules, flows, Apex, and SOAP API. All methods are static.

Custom Settings Methods
Custom settings are similar to custom objects and enable application developers to create custom sets of data, as well as create and
associate custom data for an organization, profile, or specific user. All custom settings data is exposed in the application cache, which
enables efficient access without the cost of repeated queries to the database. This data is then available for formula fields, validation
rules, flows, Apex, and the SOAP API.

Database Class
Contains methods for creating and manipulating data.

Date Class
Contains methods for the Date primitive data type.

Datetime Class
Contains methods for the Datetime primitive data type.

Decimal Class
Contains methods for the Decimal primitive data type.

Domain Class
Represents an existing domain hosted by Salesforce that serves the org or its content. Contains methods to obtain information about
these domains, such as the domain type, My Domain name, and sandbox name.

DomainCreator Class
Use the DomainCreator class to return a hostname specific to the org. For example, get the org’s Visualforce hostname. Values are
returned as a hostname, such as _**`MyDomainName`**_ `.lightning.force.com` .

DomainParser Class
Use the DomainParser class to parse a domain that Salesforce hosts for the org and extract information about the domain.

DomainType Enum
Specifies the domain type for a System.Domain.

Double Class
Contains methods for the Double primitive data type.

EmailMessages Class
Use the methods in the `EmailMessages` class to interact with emails and email threading.

EncodingUtil Class
Use the methods in the `EncodingUtil` class to encode and decode URL strings, and convert strings to hexadecimal format.

Enum Methods
An enum is an abstract data type with values that each take on exactly one of a finite set of identifiers that you specify. Apex provides
built-in enums, such as `LoggingLevel`, and you can define your own enum.


Apex Reference Guide System Namespace

EventBus Class
Contains methods for publishing platform events.

Exception Class and Built-In Exceptions
An exception denotes an error that disrupts the normal flow of code execution. You can use Apex built-in exceptions or create
custom exceptions. All exceptions have common methods.

ExternalServiceTest Class
Provides methods to test an external service's asynchronous callouts, enables sending a mock request, asserts the expected request
payload, then triggers the mocked external service’s asynchronous callback response.

FlexQueue Class
Contains methods that reorder batch jobs in the Apex flex queue.

FeatureManagement Class
Use the methods in the `System.FeatureManagement` class to check and modify the values of feature parameters, and to
show or hide custom objects and custom permissions in your subscribers’ orgs.

Formula Class
Contains methods to get a builder for creating a formula instance and to update all formula fields on the input SObjects.

FormulaRecalcFieldError Class
The return type of the `FormulaRecalcResult.getErrors` method.

FormulaRecalcResult Class
The return type of the `Formula.recalculateFormulas` method.

Http Class
Use the `Http` class to initiate an HTTP request and response.

HttpCalloutMock Interface
Enables sending fake responses when testing HTTP callouts.

HttpRequest Class
Use the `HttpRequest` class to programmatically create HTTP requests like GET, POST, PATCH, PUT, and DELETE.

HttpResponse Class
Use the `HttpResponse` class to handle the HTTP response returned by the `Http` class.

Id Class
Contains methods for the ID primitive data type.

Ideas Class
Represents zone ideas.

InstallHandler Interface
Enables custom code to run after a managed package installation or upgrade.

Integer Class
Contains methods for the Integer primitive data type.

JSON Class
Contains methods for serializing Apex objects into JSON format and deserializing JSON content that was serialized using the
`serialize` method in this class.

JSONGenerator Class
Contains methods used to serialize objects into JSON content using the standard JSON encoding.


Apex Reference Guide System Namespace

JSONParser Class
Represents a parser for JSON-encoded content.

JSONToken Enum
Contains all token values used for parsing JSON content.

Label Class
Provides methods to retrieve a custom label or to check if translation exists for a label in a specific language and namespace. Label
names are dynamically resolved at run time, overriding the user’s current language if a translation exists for the requested language.
You can’t access labels that are protected in a different namespace.

Limits Class
Contains methods that return limit information for specific resources.

List Class
Contains methods for the List collection type.

Location Class
Contains methods for accessing the component fields of geolocation compound fields.

LoggingLevel Enum
Specifies the logging level for the `System.debug` method.

Long Class
Contains methods for the Long primitive data type.

Map Class
Contains methods for the Map collection type.

Matcher Class
Matchers use Patterns to perform match operations on a character string.

Math Class
Contains methods for mathematical operations.

Messaging Class
Contains messaging methods used when sending a single or mass email.

MultiStaticResourceCalloutMock Class
Utility class used to specify a fake response using multiple resources for testing HTTP callouts.

Network Class
Manage Experience Cloud sites.

Object Class
Contains methods that are implemented by all Apex types.

OrgLimit Class
Contains methods that provide the name, maximum value, and current value of an org limit.

OrgLimits Class
Contains methods that provide a list or map of all OrgLimit instances for Salesforce your org, such as SOAP API requests, Bulk API
requests, and Streaming API limits.

PageReference Class
A PageReference is a reference to an instantiation of a page. Among other attributes, PageReferences consist of a URL and a set of
query parameter names and values.


Apex Reference Guide System Namespace

Packaging Class
Contains a method for obtaining information about managed and unlocked packages.

Pattern Class
Represents a compiled representation of a regular expression.

Queueable Interface
Enables the asynchronous execution of Apex jobs that can be monitored.

QueueableContext Interface
Represents the parameter type of the `execute()` method in a class that implements the `Queueable` interface and contains
the job ID. This interface is implemented internally by Apex.

QueueableDuplicateSignature Class
Used in the `AsyncOptions` class to store the queueable job signature in the `DuplicateSignature` property.

QueueableDuplicateSignature.Builder Class
Build a unique signature for your queueable job using this inner builder class. The `build()` class method builds a
`QueueableDuplicateSignature` object, with input from the `addId()`, `addInteger()`, and `addString()`
methods. Use the `DuplicateSignature` property in the `AsyncOptions` class to store the queueable job signature.
Enqueue your job by using the `System.enqueueJob()` with the `AsyncOptions` parameter.

QuickAction Class
Use Apex to request and process actions on objects that allow custom fields, on objects that appear in a Chatter feed, or on objects
that are available globally.

Quiddity Enum
Specifies a Quiddity value used by the methods in the System.Request class

RemoteObjectController
Use `RemoteObjectController` to access the standard Visualforce Remote Objects operations in your Remote Objects
override methods.

Request Class
Contains methods to obtain the request ID and Quiddity value of the current Salesforce request.

ResetPasswordResult Class
Represents the result of a password reset.

RestContext Class
Contains the `RestRequest` and `RestResponse` objects.

RestRequest Class
Use the `System.RestRequest` class to access and pass request data in a RESTful Apex method.

RestResponse Class
Represents an object used to pass data from an Apex RESTful Web service method to an HTTP response.

SandboxPostCopy Interface
To make your sandbox environment business ready, automate data manipulation or business logic tasks. Extend this interface and
add methods to perform post-copy tasks, then specify the class during sandbox creation.

Schedulable Interface
The class that implements this interface can be scheduled to run at different intervals.

SchedulableContext Interface
Represents the parameter type of a method in a class that implements the `Schedulable` interface and contains the scheduled
job ID. This interface is implemented internally by Apex.


Apex Reference Guide System Namespace

Schema Class
Contains methods for obtaining schema describe information.

Search Class
Use the methods of the Search class to perform dynamic SOSL queries.

Security Class
Contains methods to securely implement Apex applications.

SelectOption Class
A `SelectOption` object specifies one of the possible values for a Visualforce `selectCheckboxes`, `selectList`, or
`selectRadio` component.

Set Class
Represents a collection of unique elements with no duplicate values.

Site Class
Use the `Site` Class to manage your sites. Change, reset, validate, and check the expiration of passwords. Create site users, person
accounts, and portal users. Get the admin email and ID. Get various URLs, the path prefix, the ID, the template, and the type of the
site. Log in to the site.

SObject Class
Contains methods for the sObject data type.

SObjectAccessDecision Class
Contains the results of a call to the Security.stripInaccessible method and methods to retrieve those results.

SoqlStubProvider Class
Contains a method to create a mock test class for handling SOQL query responses for Data Cloud data model objects (DMOs).

StaticResourceCalloutMock Class
Utility class used to specify a fake response for testing HTTP callouts.

String Class
Contains methods for the String primitive data type.

StubProvider Interface

`StubProvider` is a callback interface that you can use as part of the Apex stub API to implement a mocking framework. Use this
interface with the `Test.createStub()` method to create stubbed Apex objects for testing.

System Class
Contains methods for system operations, such as writing debug messages and scheduling jobs.

Test Class
Contains methods related to Apex tests.

Time Class
Contains methods for the Time primitive data type.

TimeZone Class
Represents a time zone. Contains methods for creating a new time zone and obtaining time zone properties, such as the time zone
ID, offset, and display name.

Trigger Class
Use the `Trigger` class to access run-time context information in a trigger, such as the type of trigger or the list of sObject records
that the trigger operates on.


### Apex Reference Guide AccessLevel Class

TriggerOperation Enum
System.TriggerOperation enum values are associated with trigger events.

Type Class
Contains methods for getting the Apex type that corresponds to an Apex class and for instantiating new types.

UninstallHandler Interface
Enables custom code to run after a managed package is uninstalled.

URL Class
Represents a uniform resource locator (URL) and provides access to parts of the URL. Enables access to the base URL used to access
your Salesforce org.

UserInfo Class
Contains methods for obtaining information about the context user.

UserManagement Class
Contains methods to manage end users, for example, to register their verification methods, verify their identity, or remove their
personal information.

UUID Class
Contains methods to randomly generate a version 4 universally unique identifier (UUID), compare UUIDs, and convert UUID instance
to a string.

Version Class
Use the Version methods to get the version of a first-generation managed package (1GP) or a migrated second-generation managed
package (2GP), and to compare package versions.

WebServiceCallout Class
Enables making callouts to SOAP operations on an external Web service. This class is used in the Apex stub class that is auto-generated
from a WSDL.

WebServiceMock Interface
Enables sending fake responses when testing Web service callouts of a class auto-generated from a WSDL.

XmlStreamReader Class Class
The `XmlStreamReader` class provides methods for forward, read-only access to XML data. You can pull data from XML or skip
unwanted events. You can parse nested XML content that’s up to 50 nodes deep.

XmlStreamWriter Class
The `XmlStreamWriter` class provides methods for writing XML data.

### AccessLevel Class

Defines the different modes, such as system or user mode, that Apex database operations execute in.

Namespace

System


Apex Reference Guide AccessLevel Class

Usage

By default, Apex code runs in system mode, which means that it runs with substantially elevated permissions over the user running the
code. In system mode, the object and field-level permissions of the current user are ignored, and the record sharing rules are controlled
[by the class sharing keywords. In user mode, the current user's object permissions, field-level security, and sharing rules are enforced.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)

Many of the DML methods of the `System.Database` and `System.Search` classes include an `accessLevel` parameter to
specify the execution mode.

Avoid specifying an `accessLevel` parameter in the same query as a `WITH SECURITY_ENFORCED` clause. Salesforce recommends
that you specify either system mode or user mode, and remove any redundant `WITH SECURITY_ENFORCED` clauses.

Example

If the user running this Apex code doesn't have write access to the Account object, the `Database.insert()` method returns an
error.

```
   List<Account> toInsert = new List<Account>{new Account(Name = 'Exciting New Account')};

   List<Database.SaveResult> sr = Database.insert(toInsert, AccessLevel.USER_MODE);

```

In contrast, this example shows the method running in system mode. The success of the insert doesn't depend on whether the user
running the Apex code has create access to the Account object.

```
   List<Account> toInsert = new List<Account>{new Account(Name = 'Exciting New Account')};

   List<Database.SaveResult> sr = Database.insert(toInsert, AccessLevel.SYSTEM_MODE);

```

IN THIS SECTION:

#### AccessLevel Methods

AccessLevel Properties

#### AccessLevel Methods The following are methods for AccessLevel .

IN THIS SECTION:

##### withPermissionSetId(permissionSetId)(Developer Preview)

Supports database and search operations to be run with permissions specified in a permission set. Apex enforces field-level security
(FLS) and object permissions as per the specified permission set, in addition to the running user’s permissions.

##### **`withPermissionSetId(permissionSetId)(Developer Preview)`**

Supports database and search operations to be run with permissions specified in a permission set. Apex enforces field-level security
(FLS) and object permissions as per the specified permission set, in addition to the running user’s permissions.

Note: Feature is available as a developer preview. Feature isn’t generally available unless or until Salesforce announces its general
availability in documentation or in press releases or public statements. All commands, parameters, and other features are subject
to change or deprecation at any time, with or without notice. Don’t implement functionality developed with these commands or


Apex Reference Guide AccessLevel Class

tools in a production environment. You can provide feedback and suggestions for the “Permission Sets with User Mode” feature
[in the Trailblazer Community.](https://trailhead.salesforce.com/trailblazer-community/groups/0F94S000000GvrW)

This feature is available in scratch orgs where the `ApexUserModeWithPermset` feature is enabled. If the feature isn’t enabled,
Apex code with this feature can be compiled but not executed.

Signature

```
   public System.AccessLevel withPermissionSetId(String permissionSetId)

```

Parameters

```
   permissionSetId
```

Type: String

Permissions in the specified permission set are enforced while running user-mode DML operations, in addition to the running user’s
permissions.

Return Value

Type: Access Level Class

Example: This example runs the `AccessLevel.withPermissionSetId()` method with the specified permission set
and inserts a custom object.

```
      @isTest

      public with sharing class ElevateUserModeOperations_Test {

        @isTest

        static void objectCreatePermViaPermissionSet() {

          Profile p = [SELECT Id FROM Profile WHERE Name='Minimum Access - Salesforce'];

           User u = new User(Alias = 'standt', Email='standarduser@testorg.com',

             EmailEncodingKey='UTF-8', LastName='Testing', LanguageLocaleKey='en_US',

             LocaleSidKey='en_US', ProfileId = p.Id,

             TimeZoneSidKey='America/Los_Angeles',

             UserName='standarduser' + DateTime.now().getTime() + '@testorg.com');

           System.runAs(u) {

             try {

               Database.insert(new Account(name='foo'), AccessLevel.User_mode);

               Assert.fail();

             } catch (SecurityException ex) {

               Assert.isTrue(ex.getMessage().contains('Account'));

             }

             //Get ID of previously created permission set named 'AllowCreateToAccount'

             Id permissionSetId = [Select Id from PermissionSet

               where Name = 'AllowCreateToAccount' limit 1].Id;

```


Apex Reference Guide AccessLevel Class

```
             Database.insert(new Account(name='foo'),

      AccessLevel.User_mode.withPermissionSetId(permissionSetId));

             // The elevated access level in not persisted to subsequent operations

             try {

               Database.insert(new Account(name='foo2'), AccessLevel.User_mode);

               Assert.fail();

             } catch (SecurityException ex) {

               Assert.isTrue(ex.getMessage().contains('Account'));

             }

           }

        }

      }

#### AccessLevel Properties The following are properties for AccessLevel .

```

IN THIS SECTION:

##### SYSTEM_MODE

Execution mode in which the the object and field-level permissions of the current user are ignored, and the record sharing rules are
[controlled by the class sharing keywords.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)

##### USER_MODE

Execution mode in which the object permissions, field-level security, and sharing rules of the current user are enforced.

##### **`SYSTEM_MODE`**

Execution mode in which the the object and field-level permissions of the current user are ignored, and the record sharing rules are
[controlled by the class sharing keywords.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)

Signature

```
   public System.AccessLevel SYSTEM_MODE {get;}

```

Property Value

Type: System.AccessLevel

##### **`USER_MODE`**

Execution mode in which the object permissions, field-level security, and sharing rules of the current user are enforced.

Signature

```
   public System.AccessLevel USER_MODE {get;}

```


### Apex Reference Guide AccessType Enum

Property Value

Type: System.AccessLevel

### AccessType Enum

Specifies the access check type for the fields of an sObject.

Usage

Use these enum values for the `accessCheckType` parameter of the stripInaccessible method.

Enum Values

The following are the values of the `System.AccessType` enum.

**Value** **Description**

`CREATABLE` Check the fields of an sObject for create access.

`READABLE` Check the fields of an sObject for read access.

`UPDATABLE` Check the fields of an sObject for update access.

`UPSERTABLE` Check the fields of an sObject for both insert and update access.

### Address Class

Contains methods for accessing the component fields of address compound fields.

Namespace

System

Usage

Each of these methods is also equivalent to a read-only property. For each getter method, you can access the property using dot notation.
For example, `myAddress.getCity()` is equivalent to `myAddress.city` .

You can’t use dot notation to access compound fields’ subfields directly on the parent field. Instead, assign the parent field to a variable
### of type Address, and then access its components. For example, to access the City field in myAccount.BillingAddress,

do the following:

```
   Address addr = myAccount.BillingAddress;

   String acctCity = addr.City;

```

Important: “Address” in Salesforce can also refer to the Address standard object. When referencing the Address object in your
### Apex code, always use Schema.Address instead of Address to prevent confusion with the standard Address compound

field. If referencing both the Address object and the Address standard field in the same snippet, you can differentiate between the
two by using `System.Address` for the field and `Schema.Address` for the object.


Apex Reference Guide Address Class

Example

```
   // Select and access Address fields.

   // Call the getDistance() method in different ways.

   Account[] records = [SELECT id, BillingAddress FROM Account LIMIT 10];

   for(Account acct : records) {

     Address addr = acct.BillingAddress;

     Double lat = addr.latitude;

     Double lon = addr.longitude;

     Location loc1 = Location.newInstance(30.1944,-97.6682);

     Double apexDist1 = addr.getDistance(loc1, 'mi');

     Double apexDist2 = loc1.getDistance(addr, 'mi');

     System.assertEquals(apexDist1, apexDist2);

     Double apexDist3 = Location.getDistance(addr, loc1, 'mi');

     System.assertEquals(apexDist2, apexDist3);

   }

```

IN THIS SECTION:

#### Address Methods Address Methods The following are methods for Address .

IN THIS SECTION:

getCity()
Returns the city field of this address.

getCountry()
Returns the text-only country/territory name component of this address.

getCountryCode()
Returns the country/territory code of this address if state and country/territory picklists are enabled in your organization. Otherwise,
returns `null` .

getDistance(toLocation, unit)
Returns the distance from this location to the specified location using the specified unit.

getGeocodeAccuracy()
When using geolocation data for a given address, this method gives you relative location information based on latitude and longitude
values. For example, you can find out if the latitude and longitude values point to the middle of the street, instead of the exact
address.

getLatitude()
Returns the latitude field of this address.

getLongitude()
Returns the longitude field of this address.

getPostalCode()
Returns the postal code of this address.


Apex Reference Guide Address Class

getState()
Returns the text-only state name component of this address.

getStateCode()
Returns the state code of this address if state and country/territory picklists are enabled in your organization. Otherwise, returns

`null` .

getStreet()
Returns the street field of this address.

##### getCity()

Returns the city field of this address.

Signature

```
   public String getCity()

```

Return Value

Type: String

##### getCountry()

Returns the text-only country/territory name component of this address.

Signature

```
   public String getCountry()

```

Return Value

Type: String

##### getCountryCode()

Returns the country/territory code of this address if state and country/territory picklists are enabled in your organization. Otherwise,
returns `null` .

Signature

```
   public String getCountryCode()

```

Return Value

Type: String

##### getDistance(toLocation, unit)

Returns the distance from this location to the specified location using the specified unit.


Apex Reference Guide Address Class

Signature

```
   public Double getDistance(Location toLocation, String unit)

```

Parameters

```
   toLocation
```

Type: Location

The `Location` to which you want to calculate the distance from the current `Location` .

```
   unit
```

Type: String

The distance unit you want to use: `mi` or `km` .

Return Value

Type: Double

##### getGeocodeAccuracy()

When using geolocation data for a given address, this method gives you relative location information based on latitude and longitude
values. For example, you can find out if the latitude and longitude values point to the middle of the street, instead of the exact address.

Signature

```
   public String getGeocodeAccuracy()

```

Return Value

Type: String

##### The getGeocodeAccuracy() return value tells you more about the location at a latitude and longitude for a given address. For

example, `Zip` means the latitude and longitude point to the center of the zip code area, in case a match for an exact street address
can’t be found.


Apex Reference Guide Address Class

Geocodes are added only for some standard addresses.

**•** `Billing Address` on accounts

**•** `Shipping Address` on accounts

**•** `Mailing Address` on contacts

**•** `Address` on leads

Person accounts are not supported.

Note: For `getGeocodeAccuracy()` to work, set up and activate the geocode data integration rules for the related address
fields.

##### getLatitude()

Returns the latitude field of this address.

Signature

```
   public Double getLatitude()

```

Return Value

Type: Double

##### getLongitude()

Returns the longitude field of this address.

Signature

```
   public Double getLongitude()

```

Return Value

Type: Double

##### getPostalCode()

Returns the postal code of this address.

Signature

```
   public String getPostalCode()

```


### Apex Reference Guide Answers Class

Return Value

Type: String

##### getState()

Returns the text-only state name component of this address.

Signature

```
   public String getState()

```

Return Value

Type: String

##### getStateCode()

Returns the state code of this address if state and country/territory picklists are enabled in your organization. Otherwise, returns `null` .

Signature

```
   public String getStateCode()

```

Return Value

Type: String

##### getStreet()

Returns the street field of this address.

Signature

```
   public String getStreet()

```

Return Value

Type: String

### Answers Class

Represents zone answers.

Namespace

System


Apex Reference Guide Answers Class

Usage

Answers is a feature that enables users to ask questions and have zone members post replies. Members can then vote on the helpfulness
of each reply, and the person who asked the question can mark one reply as the best answer.

For more information on answers, see “Answers Overview” in the Salesforce online help.

Example

The following example finds questions in an internal zone that have similar titles as a new question:

```
   public class FindSimilarQuestionController {

     public static void test() {

     // Instantiate a new question

     Question question = new Question ();

     // Specify a title for the new question

     question.title = 'How much vacation time do full-time employees get?';

     // Specify the communityID (INTERNAL_COMMUNITY) in which to find similar questions.

     Community community = [ SELECT Id FROM Community WHERE Name = 'INTERNAL_COMMUNITY' ];

     question.communityId = community.id;

     ID[] results = Answers.findSimilar(question);

     }

   }

```

The following example marks a reply as the best reply:

```
   ID questionId = [SELECT Id FROM Question WHERE Title = 'Testing setBestReplyId' LIMIT

   1].Id;

   ID replyID = [SELECT Id FROM Reply WHERE QuestionId = :questionId LIMIT 1].Id;

   Answers.setBestReply(questionId,replyId);

#### Answers Methods The following are methods for Answers . All methods are static.

```

IN THIS SECTION:

##### findSimilar(yourQuestion)

Returns a list of similar questions based on the title of the specified question.

setBestReply(questionId, replyId)
Sets the specified reply for the specified question as the best reply. Because a question can have multiple replies, setting the best
reply helps users quickly identify the reply that contains the most helpful information.

##### findSimilar(yourQuestion)

Returns a list of similar questions based on the title of the specified question.


### Apex Reference Guide ApexPages Class

Signature

```
   public static ID[] findSimilar(Question yourQuestion)

```

Parameters

```
   yourQuestion
```

Type: Question

Return Value

Type: ID[]

Usage

Each `findSimilar` call counts against the SOSL statements governor limit allowed for the process.

##### setBestReply(questionId, replyId)

Sets the specified reply for the specified question as the best reply. Because a question can have multiple replies, setting the best reply
helps users quickly identify the reply that contains the most helpful information.

Signature

```
   public static Void setBestReply(String questionId, String replyId)

```

Parameters

```
   questionId
```

Type: String

```
   replyId
```

Type: String

Return Value

Type: Void

### ApexPages Class Use ApexPages to add and check for messages associated with the current page, as well as to reference the current page.

Namespace

System

Usage

### In addition, ApexPages is used as a namespace for the PageReference Class and the Message Class.


Apex Reference Guide ApexPages Class

#### ApexPages Methods The following are methods for ApexPages . All are instance methods.

IN THIS SECTION:

##### addMessage(message)

Add a message to the current page context.

##### addMessages(exceptionThrown)

Adds a list of messages to the current page context based on a thrown exception.

currentPage()
Returns the current page's PageReference.

getMessages()
Returns a list of the messages associated with the current context.

hasMessages()
Returns `true` if there are messages associated with the current context, `false` otherwise.

hasMessages(severity)
Returns `true` if messages of the specified severity exist, `false` otherwise.

##### addMessage(message)

Add a message to the current page context.

Signature

```
   public Void addMessage(ApexPages.Message message)

```

Parameters

**message**
Type: ApexPages.Message

Return Value

Type: Void

##### addMessages(exceptionThrown)

Adds a list of messages to the current page context based on a thrown exception.

Signature

```
   public Void addMessages(Exception exceptionThrown)

```

Parameters

```
   exceptionThrown
```

Type: Exception


Apex Reference Guide ApexPages Class

Return Value

Type: Void

##### currentPage()

Returns the current page's PageReference.

Signature

```
   public System.PageReference currentPage()

```

Return Value

Type: System.PageReference

Example

This code segment returns the id parameter of the current page.

```
   public MyController() {

      account = [

        SELECT Id, Name, Site

        FROM Account

        WHERE Id =

           :ApexPages.currentPage().

           getParameters().

           get('id')

      ];

   }

##### getMessages()

```

Returns a list of the messages associated with the current context.

Signature

```
   public ApexPages.Message[] getMessages()

```

Return Value

Type: ApexPages.Message[]

##### hasMessages()

Returns `true` if there are messages associated with the current context, `false` otherwise.

Signature

```
   public Boolean hasMessages()

```


### Apex Reference Guide Approval Class

Return Value

Type: Boolean

##### hasMessages(severity)

Returns `true` if messages of the specified severity exist, `false` otherwise.

Signature

```
   public Boolean hasMessages(ApexPages.Severity severity)

```

Parameters

```
   sev
```

Type: ApexPages.Severity

Return Value

Type: Boolean

### Approval Class

Contains methods for processing approval requests and setting approval-process locks and unlocks on records.

Namespace

System

Usage

Salesforce admins can edit locked records. Depending on your approval process configuration settings, an assigned approver can also
edit locked records. Locks and unlocks that are set programmatically use the same record editability settings as other approval-process
locks and unlocks.

Record locks and unlocks are treated as DML. They’re blocked before a callout, they count toward your DML limits, and if a failure occurs,
they’re rolled back along with the rest of your transaction. To change this rollback behavior, use an `allOrNone` parameter.

Approval is also used as a namespace for the `ProcessRequest` and `ProcessResult` classes.

SEE ALSO:

[Approval Process Considerations](https://help.salesforce.com/HTViewHelpDoc?id=approvals_considerations.htm&language=en_US)

#### Approval Methods

### The following are methods for Approval . All methods are static.

IN THIS SECTION:

isLocked(id)
Returns `true` if the record with the ID `id` is locked, or `false` if it’s not.


Apex Reference Guide Approval Class

isLocked(ids)
Returns a map of record IDs and their lock statuses. If the record is locked the status is `true` . If the record is not locked the status
is `false` .

isLocked(sobject)
Returns `true` if the `sobject` record is locked, or `false` if it’s not.

isLocked(sobjects)
Returns a map of record IDs to lock statuses. If the record is locked the status is `true` . If the record is not locked the status is `false` .

lock(recordId)
Locks an object, and returns the lock results.

lock(recordIds)
Locks a set of objects, and returns the lock results, including failures.

lock(recordToLock)
Locks an object, and returns the lock results.

lock(recordsToLock)
Locks a set of objects, and returns the lock results, including failures.

lock(recordId, allOrNothing)
Locks an object, with the option for partial success, and returns the lock result.

lock(recordIds, allOrNothing)
Locks a set of objects, with the option for partial success. It returns the lock results, including failures.

lock(recordToLock, allOrNothing)
Locks an object, with the option for partial success, and returns the lock result.

lock(recordsToLock, allOrNothing)
Locks a set of objects, with the option for partial success. It returns the lock results, including failures.

process(approvalRequest)
Submits a new approval request and approves or rejects existing approval requests.

process(approvalRequest, allOrNone)
Submits a new approval request and approves or rejects existing approval requests.

process(approvalRequests)
Submits a list of new approval requests, and approves or rejects existing approval requests.

process(approvalRequests, allOrNone)
Submits a list of new approval requests, and approves or rejects existing approval requests.

unlock(recordId)
Unlocks an object, and returns the unlock results.

unlock(recordIds)
Unlocks a set of objects, and returns the unlock results, including failures.

unlock(recordToUnlock)
Unlocks an object, and returns the unlock results.

unlock(recordsToUnlock)
Unlocks a set of objects, and returns the unlock results, including failures.

unlock(recordId, allOrNothing)
Unlocks an object, with the option for partial success, and returns the unlock result.


Apex Reference Guide Approval Class

unlock(recordIds, allOrNothing)
Unlocks a set of objects, with the option for partial success. It returns the unlock results, including failures.

unlock(recordToUnlock, allOrNothing)
Unlocks an object, with the option for partial success, and returns the unlock result.

unlock(recordsToUnlock, allOrNothing)
Unlocks a set of objects, with the option for partial success. It returns the unlock results, including failures.

##### isLocked(id)

Returns `true` if the record with the ID `id` is locked, or `false` if it’s not.

Signature

```
   public static Boolean isLocked(Id id)

```

Parameters

```
   id
```

Type: Id

The ID of the record whose lock or unlock status is in question.

Return Value

Type: Boolean

##### isLocked(ids)

Returns a map of record IDs and their lock statuses. If the record is locked the status is `true` . If the record is not locked the status is

`false` .

Signature

```
   public static Map<Id,Boolean> isLocked(List<Id> ids)

```

Parameters

```
   ids
```

Type: List<Id>

The IDs of the records whose lock or unlock statuses are in question.

Return Value

Type: Map<Id,Boolean>

##### isLocked(sobject)

Returns `true` if the `sobject` record is locked, or `false` if it’s not.


Apex Reference Guide Approval Class

Signature

```
   public static Boolean isLocked(SObject sobject)

```

Parameters

```
   sobject
```

Type: SObject

The record whose lock or unlock status is in question.

Return Value

Type: Boolean

##### isLocked(sobjects)

Returns a map of record IDs to lock statuses. If the record is locked the status is `true` . If the record is not locked the status is `false` .

Signature

```
   public static Map<Id,Boolean> isLocked(List<SObject> sobjects)

```

Parameters

```
   sobjects
```

Type: List<SObject>

The records whose lock or unlock statuses are in question.

Return Value

Type: Map<Id,Boolean>

##### lock(recordId)

Locks an object, and returns the lock results.

Signature

```
   public static Approval.LockResult lock(Id recordId)

```

Parameters

```
   recordId
```

Type: Id

ID of the object to lock.

Return Value

Type: Approval.LockResult


Apex Reference Guide Approval Class

##### lock(recordIds)

Locks a set of objects, and returns the lock results, including failures.

Signature

```
   public static List<Approval.LockResult> lock(List<Id> ids)

```

Parameters

```
   ids
```

Type: List<Id>

IDs of the objects to lock.

Return Value

Type: List<Approval.LockResult>

##### lock(recordToLock)

Locks an object, and returns the lock results.

Signature

```
   public static Approval.LockResult lock(SObject recordToLock)

```

Parameters

```
   recordToLock
```

Type: SObject

Return Value

Type: Approval.LockResult

##### lock(recordsToLock)

Locks a set of objects, and returns the lock results, including failures.

Signature

```
   public static List<Approval.LockResult> lock(List<SObject> recordsToLock)

```

Parameters

```
   recordsToLock
```

Type: List<SObject>

Return Value

Type: List<Approval.LockResult>


Apex Reference Guide Approval Class

##### lock(recordId, allOrNothing)

Locks an object, with the option for partial success, and returns the lock result.

Signature

```
   public static Approval.LockResult lock(Id recordId, Boolean allOrNothing)

```

Parameters

```
   recordId
```

Type: Id

ID of the object to lock.

```
   allOrNothing
```

Type: Boolean

Specifies whether this operation allows partial success. If you specify `false` and a record fails, the remainder of the DML operation
can still succeed. This method returns a result object that you can use to verify which records succeeded, which failed, and why.

Return Value

Type: Approval.LockResult

##### lock(recordIds, allOrNothing)

Locks a set of objects, with the option for partial success. It returns the lock results, including failures.

Signature

```
   public static List<Approval.LockResult> lock(List<Id> recordIds, Boolean allOrNothing)

```

Parameters

```
   recordIds
```

Type: List<Id>

IDs of the objects to lock.

```
   allOrNothing
```

Type: Boolean

Specifies whether this operation allows partial success. If you specify `false` and a record fails, the remainder of the DML operation
can still succeed. This method returns a result object that you can use to verify which records succeeded, which failed, and why.

Return Value

Type: List<Approval.LockResult>

##### lock(recordToLock, allOrNothing)

Locks an object, with the option for partial success, and returns the lock result.


Apex Reference Guide Approval Class

Signature

```
   public static Approval.LockResult lock(SObject recordToLock, Boolean allOrNothing)

```

Parameters

```
   recordToLock
```

Type: SObject

```
   allOrNothing
```

Type: Boolean

Specifies whether this operation allows partial success. If you specify `false` and a record fails, the remainder of the DML operation
can still succeed. This method returns a result object that you can use to verify which records succeeded, which failed, and why.

Return Value

Type: Approval.LockResult

##### lock(recordsToLock, allOrNothing)

Locks a set of objects, with the option for partial success. It returns the lock results, including failures.

Signature

```
   public static List<Approval.LockResult> lock(List<SObject> recordsToLock, Boolean

   allOrNothing)

```

Parameters

```
   recordsToLock
```

Type: List<SObject>

```
   allOrNothing
```

Type: Boolean

Specifies whether this operation allows partial success. If you specify `false` and a record fails, the remainder of the DML operation
can still succeed. This method returns a result object that you can use to verify which records succeeded, which failed, and why.

Return Value

Type: List<Approval.LockResult>

##### process(approvalRequest)

Submits a new approval request and approves or rejects existing approval requests.

Signature

```
   public static Approval.ProcessResult process(Approval.ProcessRequest approvalRequest)

```


Apex Reference Guide Approval Class

Parameters

```
   approvalRequest
```

Type: Approval.ProcessRequest

Return Value

Type: Approval.ProcessResult

Example

```
   // Insert an account

   Account a = new Account(Name='Test',

                annualRevenue=100.0);

   insert a;

   // Create an approval request for the account

   Approval.ProcessSubmitRequest req1 =

       new Approval.ProcessSubmitRequest();

   req1.setObjectId(a.id);

   // Submit the approval request for the account

   Approval.ProcessResult result =

               Approval.process(req1);

##### process(approvalRequest, allOrNone)

```

Submits a new approval request and approves or rejects existing approval requests.

Signature

```
   public static Approval.ProcessResult process(Approval.ProcessRequest approvalRequest,

   Boolean allOrNone)

```

Parameters

```
   approvalRequest
```

Approval.ProcessRequest

```
   allOrNone
```

Type: Boolean

The optional _`allOrNone`_ parameter specifies whether the operation allows for partial success. If you specify `false` for this
parameter and an approval fails, the remainder of the approval processes can still succeed.

Return Value

Approval.ProcessResult


Apex Reference Guide Approval Class

##### process(approvalRequests)

Submits a list of new approval requests, and approves or rejects existing approval requests.

Signature

```
   public static Approval.ProcessResult [] process(Approval.ProcessRequest[]

   approvalRequests)

```

Parameters

```
   approvalRequests
```

Approval.ProcessRequest []

Return Value

Approval.ProcessResult []

##### process(approvalRequests, allOrNone)

Submits a list of new approval requests, and approves or rejects existing approval requests.

Signature

```
   public static Approval.ProcessResult [] process(Approval.ProcessRequest[]

   approvalRequests, Boolean allOrNone)

```

Parameters

```
   approvalRequests
```

Approval.ProcessRequest []

```
   allOrNone
```

Type: Boolean

The optional _`allOrNone`_ parameter specifies whether the operation allows for partial success. If you specify `false` for this
parameter and an approval fails, the remainder of the approval processes can still succeed.

Return Value

Approval.ProcessResult []

##### unlock(recordId)

Unlocks an object, and returns the unlock results.

Signature

```
   public static Approval.UnlockResult unlock(Id recordId)

```


Apex Reference Guide Approval Class

Parameters

```
   recordId
```

Type: Id

ID of the object to unlock.

Return Value

Type: Approval.UnlockResult

##### unlock(recordIds)

Unlocks a set of objects, and returns the unlock results, including failures.

Signature

```
   public static List<Approval.UnlockResult> unlock(List<Id> recordIds)

```

Parameters

```
   recordIds
```

Type: List<Id>

IDs of the objects to unlock.

Return Value

Type: List<Approval.UnlockResult>

##### unlock(recordToUnlock)

Unlocks an object, and returns the unlock results.

Signature

```
   public static Approval.UnlockResult unlock(SObject recordToUnlock)

```

Parameters

```
   recordToUnlock
```

Type: SObject

Return Value

Type: Approval.UnlockResult

##### unlock(recordsToUnlock)

Unlocks a set of objects, and returns the unlock results, including failures.


Apex Reference Guide Approval Class

Signature

```
   public static List<Approval.UnlockResult> unlock(List<SObject> recordsToUnlock)

```

Parameters

```
   recordsToUnlock
```

Type: List<SObject>

Return Value

Type: List<Approval.UnlockResult>

##### unlock(recordId, allOrNothing)

Unlocks an object, with the option for partial success, and returns the unlock result.

Signature

```
   public static Approval.UnlockResult unlock(Id recordId, Boolean allOrNothing)

```

Parameters

```
   recordId
```

Type: Id

ID of the object to lock.

```
   allOrNothing
```

Type: Boolean

Specifies whether this operation allows partial success. If you specify `false` and a record fails, the remainder of the DML operation
can still succeed. This method returns a result object that you can use to verify which records succeeded, which failed, and why.

Return Value

Type: Approval.UnlockResult

##### unlock(recordIds, allOrNothing)

Unlocks a set of objects, with the option for partial success. It returns the unlock results, including failures.

Signature

```
   public static List<Approval.UnlockResult> unlock(List<Id> recordIds, Boolean

   allOrNothing)

```

Parameters

```
   recordIds
```

Type: List<Id>

IDs of the objects to unlock.


Apex Reference Guide Approval Class

```
   allOrNothing
```

Type: Boolean

Specifies whether this operation allows partial success. If you specify `false` and a record fails, the remainder of the DML operation
can still succeed. This method returns a result object that you can use to verify which records succeeded, which failed, and why.

Return Value

Type: List<Approval.UnlockResult>

##### unlock(recordToUnlock, allOrNothing)

Unlocks an object, with the option for partial success, and returns the unlock result.

Signature

```
   public static Approval.UnlockResult unlock(SObject recordToUnlock, Boolean allOrNothing)

```

Parameters

```
   recordToUnlock
```

Type: SObject

```
   allOrNothing
```

Type: Boolean

Specifies whether this operation allows partial success. If you specify `false` and a record fails, the remainder of the DML operation
can still succeed. This method returns a result object that you can use to verify which records succeeded, which failed, and why.

Return Value

Type: Approval.UnlockResult

##### unlock(recordsToUnlock, allOrNothing)

Unlocks a set of objects, with the option for partial success. It returns the unlock results, including failures.

Signature

```
   public static List<Approval.UnlockResult> unlock(List<SObject> recordsToUnlock, Boolean

   allOrNothing)

```

Parameters

```
   recordsToUnlock
```

Type: List<SObject>

```
   allOrNothing
```

Type: Boolean

Specifies whether this operation allows partial success. If you specify `false` and a record fails, the remainder of the DML operation
can still succeed. This method returns a result object that you can use to verify which records succeeded, which failed, and why.


### Apex Reference Guide Assert Class

Return Value

Type: List<Approval.UnlockResult>

### Assert Class

Contains methods to assert various conditions with test methods, such as whether two values are the same, a condition is true, or a
variable is null.

Namespace

System

#### Assert Methods

### The following are methods for Assert .

IN THIS SECTION:

areEqual(expected, actual, msg)
Asserts that the first two arguments are the same.

areEqual(expected, actual)
Asserts that the two arguments are the same.

areNotEqual(notExpected, actual, msg)
Asserts that the first two arguments aren’t the same.

areNotEqual(notExpected, actual)
Asserts that the two arguments aren’t the same.

fail(msg)
Immediately return a fatal error that causes code execution to halt.

fail()
Immediately return a fatal error that causes code execution to halt.

isFalse(condition, msg)
Asserts that the specified condition is `false` .

isFalse(condition)
Asserts that the specified condition is `false` .

isInstanceOfType(instance, expectedType, msg)
Asserts that the instance is of the specified type.

isInstanceOfType(instance, expectedType)
Asserts that the instance is of the specified type.

isNotInstanceOfType(instance, notExpectedType, msg)
Asserts that the instance isn’t of the specified type.

isNotInstanceOfType(instance, notExpectedType)
Asserts that the instance isn’t of the specified type.


Apex Reference Guide Assert Class

isNotNull(value, msg)
Asserts that the value isn’t null.

isNotNull(value)
Asserts that the value isn’t null.

isNull(value, msg)
Asserts that the value is null.

isNull(value)
Asserts that the value is null.

isTrue(condition, msg)
Asserts that the specified condition is `true` .

isTrue(condition)
Asserts that the specified condition is `true` .

##### areEqual(expected, actual, msg)

Asserts that the first two arguments are the same.

Signature

```
   public static void areEqual(Object expected, Object actual, String msg)

```

Parameters

```
   expected
```

Type: Object

Expected value.

```
   actual
```

Type: Object

Actual value.

```
   msg
```

Type: String

(Optional) Custom message returned as part of the error message.

Return Value

Type: void

Usage

If the first two arguments aren't the same, a fatal error is returned that causes code execution to halt.

You can’t catch an assertion failure using a try/catch block even though it’s logged as an exception.


Apex Reference Guide Assert Class

Example

```
   String sub = 'abcde'.substring(2);

   Assert.areEqual('cde', sub, 'Expected characters after first two'); // Succeeds

##### areEqual(expected, actual)

```

Asserts that the two arguments are the same.

Signature

```
   public static void areEqual(Object expected, Object actual)

```

Parameters

```
   expected
```

Type: Object

Expected value.

```
   actual
```

Type: Object

Actual value.

Return Value

Type: void

Usage

If the two arguments aren't the same, a fatal error is returned that causes code execution to halt.

You can’t catch an assertion failure using a try/catch block even though it’s logged as an exception.

Example

```
   String sub = 'abcde'.substring(2);

   Assert.areEqual('cde', sub); // Succeeds

##### areNotEqual(notExpected, actual, msg)

```

Asserts that the first two arguments aren’t the same.

Signature

```
   public static void areNotEqual(Object notExpected, Object actual, String msg)

```

Parameters

```
   notExpected
```

Type: Object

Value that’s not expected.


Apex Reference Guide Assert Class

```
   actual
```

Type: Object

Actual value.

```
   msg
```

Type: String

(Optional) Custom message returned as part of the error message.

Return Value

Type: void

Usage

If the first two arguments are the same, a fatal error is returned that causes code execution to halt.

You can’t catch an assertion failure using a try/catch block even though it’s logged as an exception.

Example

```
   String sub = 'abcde'.substring(2);

   Assert.areNotEqual('xyz', sub, 'Characters not expected after first two'); // Succeeds

##### areNotEqual(notExpected, actual)

```

Asserts that the two arguments aren’t the same.

Signature

```
   public static void areNotEqual(Object notExpected, Object actual)

```

Parameters

```
   notExpected
```

Type: Object

Value that’s not expected.

```
   actual
```

Type: Object

Actual value.

Return Value

Type: void

Usage

If the two arguments are the same, a fatal error is returned that causes code execution to halt.

You can’t catch an assertion failure using a try/catch block even though it’s logged as an exception.


Apex Reference Guide Assert Class

Example

```
   String sub = 'abcde'.substring(2);

   Assert.areNotEqual('xyz', sub); // Succeeds

##### fail(msg)

```

Immediately return a fatal error that causes code execution to halt.

Signature

```
   public static void fail(String msg)

```

Parameters

```
   msg
```

Type: String

(Optional) Custom message returned as part of the error message.

Return Value

Type: void

Usage

Commonly used in a try/catch block test case where an exception is expected to be thrown. You can’t, however, catch the assertion
failure in the try/catch block even though it’s logged as an exception.

Example

```
   // test case where exception is expected

   try {

      SomeClass.methodUnderTest();

      Assert.fail('DmlException Expected');

   } catch (DmlException ex) {

      // Add assertions here about the expected exception

   }

##### fail()

```

Immediately return a fatal error that causes code execution to halt.

Signature

```
   public static void fail()

```

Return Value

Type: void


Apex Reference Guide Assert Class

Usage

Commonly used in a try/catch block test case where an exception is expected to be thrown. You can’t, however, catch the assertion
failure in the try/catch block even though it’s logged as an exception.

Example

```
   // test case where exception is expected

   try {

      SomeClass.methodUnderTest();

      Assert.fail();

   } catch (DmlException ex) {

      // Add assertions here about the expected exception

   }

##### isFalse(condition, msg)

```

Asserts that the specified condition is `false` .

Signature

```
   public static void isFalse(Boolean condition, String msg)

```

Parameters

```
   condition
```

Type: Boolean

Condition you’re checking to determine if it’s `false` .

```
   msg
```

Type: String

(Optional) Custom message returned as part of the error message.

Return Value

Type: void

Usage

If the condition is `true`, a fatal error is returned that causes code execution to halt.

You can’t catch an assertion failure using a try/catch block even though it’s logged as an exception.

Example

```
   Boolean containsCode = 'Salesforce'.contains('code');

   Assert.isFalse(containsCode, 'No code'); // Assertion succeeds

##### isFalse(condition)

```

Asserts that the specified condition is `false` .


Apex Reference Guide Assert Class

Signature

```
   public static void isFalse(Boolean condition)

```

Parameters

```
   condition
```

Type: Boolean

Condition you’re checking to determine if it’s `false` .

Return Value

Type: void

Usage

If the condition is `true`, a fatal error is returned that causes code execution to halt.

You can’t catch an assertion failure using a try/catch block even though it’s logged as an exception.

Example

```
   Boolean containsCode = 'Salesforce'.contains('code');

   Assert.isFalse(containsCode); // Assertion succeeds

##### isInstanceOfType(instance, expectedType, msg)

```

Asserts that the instance is of the specified type.

Signature

```
   public static void isInstanceOfType(Object instance, System.Type expectedType, String

   msg)

```

Parameters

```
   instance
```

Type: Object

Instance whose type you're checking.

```
   expectedType
```

Type: System.Type on page 4260

Expected type.

```
   msg
```

Type: String

(Optional) Custom message returned as part of the error message.

Return Value

Type: void


Apex Reference Guide Assert Class

Usage

If the instance isn't of the specified type, a fatal error is returned that causes code execution to halt.

You can’t catch an assertion failure using a try/catch block even though it’s logged as an exception.

Example

```
   Account o = new Account();

   Assert.isInstanceOfType(o, Account.class); // Succeeds

##### isInstanceOfType(instance, expectedType)

```

Asserts that the instance is of the specified type.

Signature

```
   public static void isInstanceOfType(Object instance, System.Type expectedType)

```

Parameters

```
   instance
```

Type: Object

Instance whose type you're checking.

```
   expectedType
```

Type: System.Type on page 4260

Expected type.

Return Value

Type: void

Usage

If the instance isn't of the specified type, a fatal error is returned that causes code execution to halt.

You can’t catch an assertion failure using a try/catch block even though it’s logged as an exception.

Example

```
   Account o = new Account();

   Assert.isInstanceOfType(o, Account.class); // Succeeds

   Account o = new Account();

   Assert.isInstanceOfType(o, Account.class, 'Expected type.'); // Succeeds

##### isNotInstanceOfType(instance, notExpectedType, msg)

```

Asserts that the instance isn’t of the specified type.


Apex Reference Guide Assert Class

Signature

```
   public static void isNotInstanceOfType(Object instance, System.Type notExpectedType,

   String msg)

```

Parameters

```
   instance
```

Type: Object

Instance whose type you're checking.

```
   notExpectedType
```

Type: System.Type on page 4260

Type that's not expected.

```
   msg
```

Type: String

(Optional) Custom message returned as part of the error message.

Return Value

Type: void

Usage

If the instance is of the specified type, a fatal error is returned that causes code execution to halt.

You can’t catch an assertion failure using a try/catch block even though it’s logged as an exception.

Example

```
   Contact con = new Contact();

   Assert.isNotInstanceOfType(con, Account.class, 'Not expected type'); // Succeeds

##### isNotInstanceOfType(instance, notExpectedType)

```

Asserts that the instance isn’t of the specified type.

Signature

```
   public static void isNotInstanceOfType(Object instance, System.Type notExpectedType)

```

Parameters

```
   instance
```

Type: Object

Instance whose type you're checking.

```
   notExpectedType
```

Type: System.Type on page 4260

Type that's not expected.


Apex Reference Guide Assert Class

Return Value

Type: void

Usage

If the instance is of the specified type, a fatal error is returned that causes code execution to halt.

You can’t catch an assertion failure using a try/catch block even though it’s logged as an exception.

Example

```
   Contact con = new Contact();

   Assert.isNotInstanceOfType(con, Account.class); // Succeeds

##### isNotNull(value, msg)

```

Asserts that the value isn’t null.

Signature

```
   public static void isNotNull(Object value, String msg)

```

Parameters

```
   value
```

Type: Object

Value you’re checking to determine if it’s not null.

```
   msg
```

Type: String

(Optional) Custom message returned as part of the error message.

Return Value

Type: void

Usage

If the value is null, a fatal error is returned that causes code execution to halt.

You can’t catch an assertion failure using a try/catch block even though it’s logged as an exception.

Example

```
   String myString = 'value';

   Assert.isNotNull(myString, 'myString should not be null'); // Succeeds

##### isNotNull(value)

```

Asserts that the value isn’t null.


Apex Reference Guide Assert Class

Signature

```
   public static void isNotNull(Object value)

```

Parameters

```
   value
```

Type: Object

Value you’re checking to determine if it’s not null.

Return Value

Type: void

Usage

If the value is null, a fatal error is returned that causes code execution to halt.

You can’t catch an assertion failure using a try/catch block even though it’s logged as an exception.

Example

```
   String myString = 'value';

   Assert.isNotNull(myString); // Succeeds

##### isNull(value, msg)

```

Asserts that the value is null.

Signature

```
   public static void isNull(Object value, String msg)

```

Parameters

```
   value
```

Type: Object

Value you’re checking to determine if it’s null.

```
   msg
```

Type: String

(Optional) Custom message returned as part of the error message.

Return Value

Type: void

Usage

If the value isn't null, a fatal error is returned that causes code execution to halt.

You can’t catch an assertion failure using a try/catch block even though it’s logged as an exception.


Apex Reference Guide Assert Class

Example

```
   String myString = null;

   Assert.isNull(myString, 'String should be null'); // Succeeds

##### isNull(value)

```

Asserts that the value is null.

Signature

```
   public static void isNull(Object value)

```

Parameters

```
   value
```

Type: Object

Value you’re checking to determine if it’s null.

Return Value

Type: void

Usage

If the value isn't null, a fatal error is returned that causes code execution to halt.

You can’t catch an assertion failure using a try/catch block even though it’s logged as an exception.

Example

```
   String myString = null;

   Assert.isNull(myString); // Succeeds

##### isTrue(condition, msg)

```

Asserts that the specified condition is `true` .

Signature

```
   public static void isTrue(Boolean condition, String msg)

```

Parameters

```
   condition
```

Type: Boolean

Condition you’re checking to determine if it’s `true` .

```
   msg
```

Type: String

(Optional) Custom message returned as part of the error message.


### Apex Reference Guide AsyncInfo Class

Return Value

Type: void

Usage

If the specified condition is `false`, a fatal error is returned that causes code execution to halt.

You can’t catch an assertion failure using a try/catch block even though it’s logged as an exception.

Example

```
   Boolean containsForce = 'Salesforce'.contains('force');

   Assert.isTrue(containsForce, 'Contains force'); // Assertion succeeds

##### isTrue(condition)

```

Asserts that the specified condition is `true` .

Signature

```
   public static void isTrue(Boolean condition)

```

Parameters

```
   condition
```

Type: Boolean

Condition you’re checking to determine if it’s `true` .

Return Value

Type: void

Usage

If the specified condition is `false`, a fatal error is returned that causes code execution to halt.

You can’t catch an assertion failure using a try/catch block even though it’s logged as an exception.

Example

```
   Boolean containsForce = 'Salesforce'.contains('force');

   Assert.isTrue(containsForce); // Assertion succeeds

### AsyncInfo Class

```

Provides methods to get the current stack depth, maximum stack depth, and the minimum queueable delay for Queueable transactions,
and to determine if maximum stack depth is set.


Apex Reference Guide AsyncInfo Class

Namespace

System

IN THIS SECTION:

#### AsyncInfo Methods AsyncInfo Methods The following are methods for AsyncInfo .

IN THIS SECTION:

##### getCurrentQueueableStackDepth()

Get the current queueable stack depth for queueable transactions.

##### getMaximumQueueableStackDepth()

Get the maximum queueable stack depth for queueable transactions.

getMinimumQueueableDelayInMinutes()
Get the minimum queueable delay for queueable transactions (in minutes).

hasMaxStackDepth()
Determine if maximum stack depth is set for your queueable requests.

##### **`getCurrentQueueableStackDepth()`**

Get the current queueable stack depth for queueable transactions.

Signature

```
   public static Integer getCurrentQueueableStackDepth()

```

Return Value

Type: Integer

##### **`getMaximumQueueableStackDepth()`**

Get the maximum queueable stack depth for queueable transactions.

Signature

```
   public static Integer getMaximumQueueableStackDepth()

```

Return Value

Type: Integer


### Apex Reference Guide AsyncOptions Class

##### **`getMinimumQueueableDelayInMinutes()`**

