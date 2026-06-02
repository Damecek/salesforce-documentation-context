appear in the Assigned Resources related list on service appointments. This object is available in API version 38.0 and later.

AssignmentRule
Represents an assignment rule associated with a Case or Lead.

AssociatedLocation
Represents a link between an account and a location in Field Service. You can associate multiple accounts with one location. For
example, a shopping center location may have multiple customer accounts.

AsyncApexJob
Represents an individual Apex sharing recalculation job, a batch Apex job, a method with the `future` annotation, or a job that
implements `Queueable` or `Schedulable` . Use this object to query Apex batch jobs in your organization.

AsyncOperationLog
Represents an async operations log containing progress and status information about external synchronizations to the Omnichannel
Inventory service. This object is available in API version 51.0 and later.

AsyncOperationTracker
Represents the status of an asynchronous request initiated from the Quote, Order, and CreditMemo objects. This object is available
in API version 61.0 and later.

AsyncOpSyndicationFeedFile
Represents the sync status of file-related information shared with external channels such as Facebook and Instagram. This object is
available in API version 64.0 and later.

AttachedContentDocument
This read-only object contains all `ContentDocument` objects associated with an object.

AttachedContentNote
This read-only object contains all ContentNote objects associated with an object.This object is available in API version 35.0 and later.

Attachment
Represents a file that a User has uploaded and attached to a parent object.

AttachmentEventLog
Attachment event logs contain information about attachments. This object is available in API version 65.0 and later.

AttribModel
Represents an attribution model used with Personalization, Attribution, and Campaign Influence, including model weights and
touch type. This object is available in API version 62.0 and later.

AttribModelStage
Represents a funnel stage that’s used in a predefined or custom attribution configuration. Available in API version 62.0 and later.

AttribModelStageMetric
Represents the engagement signal metrics that you select when you configure a funnel stage for an attribution configuration.
Available in API version 63.0 and later.

AttributeDefinition
Represents a product, asset, or object attribute, for example, a hardward specification or software detail. This object is available in
API version 57.0 and later.


Standard Objects

AttributePicklist
Represents a custom picklist for an asset attribute. This object is available in API version 57.0 and later.

AttributePicklistValue
Represents the values of an asset attribute picklist. This object is available in API version 57.0 and later.

AsyncReportRunEventLog
Async Report Run Event Log is used for reporting scheduled requests. This category includes dashboard refreshes, asynchronous
reports, schedule reports, and analytics snapshots. This object is available in API version 61.0 and later.

Audience
Represents an audience that is defined by criteria and can be assigned and used for targeting in an Experience Cloud site. This object
is available in API version 44.0 and later.

AuraDefinition
Represents an Aura component definition, such as component markup, a client-side controller, or an event. This object is available
in API version 32.0 and later.

AuraDefinitionBundle
Represents a Lightning Aura component definition bundle, such as a component or application bundle. A bundle contains a Lightning
Aura component definition and all its related resources. This object is available in API version 32.0 and later.

AuraDefinitionBundleInfo
For internal use only.

AuraDefinitionInfo
For internal use only.

AuraRequestEventLog
Aura Request Event Log contains details of requests to Apex methods from Aura and Lightning web components. This object is
available in API version 61.0 and later.

AuthConfig
Represents authentication options for My Domain and Experience Cloud site login pages. This object is available in API version 32.0
and later.

AuthConfigProviders
Represents an authentication provider that’s configured in an organization. AuthConfigProviders is a child of the AuthConfig object.
This object is available in API version 32.0 and later.

AuthorizationForm
Represents the specific version and effective dates of a form that is associated with consent, such as a privacy policy or terms and
conditions. This object is available in API version 46.0 and later.

AuthorizationFormConsent
Represents the date and way in which a user consented to an authorization form. This object is available in API version 46.0 and
later.

AuthorizationFormDataUse
Represents the data use consented to in an authorization form. This object is available in API version 46.0 and later.

AuthorizationFormText
Represents an authorization form’s text and language settings. This object is available in API version 46.0 and later.

AuthProvider
Represents an authentication provider (auth provider). An auth provider lets users log in to your Salesforce org from an external
service provider, such as Facebook, Google, or GitHub. This object is available in API version 27.0 and later.


Standard Objects

AuthProvParamFwdAllowlist
Represents an allowlisted URL parameter that can be forwarded from authentication provider client configuration URLs to the
authorization URL. Use this type to add custom functionality to authentication providers. For example, allowlist a `ui_locales`
parameter and use it to send a user's language preference from Salesforce to the third-party provider's login page. This object is
available in API version 62..0 and later.

AuthSession
The AuthSession object represents an individual user session in your organization. This object is available in versions 29.0 and later.

AutomatedAction
Represents the configuration of an automated action, such as a workflow rule. This object is available in API version 57.0 and later.

AutomatedActionCondition
Represents the logical operator details for evaluating conditions in an automated action. This object is available in API version 57.0
and later.

AutomatedActionOverride
Represents a modified attribute of a shared automated action. For example, the modified attribute can contain customizations for
your business. This object is available in API version 58.0 and later.

AutomatedActionParameter
Represents the values or field references evaluated by the automated action. This object is available in API version 57.0 and later.

AutomatedActionReminder
Represents a reminder to the end user to take an action in the future. This object is available in API version 58.0 and later.

BackgroundOperation
Represents a background operation in an asynchronous job queue. This object is available in API version 35.0 and later.

BackgroundOperationResult
Stores error messages generated when or importing data into big objects using Bulk API. This is a big object, available in API version
37.0 and later.

BatchApexErrorEvent
[The documentation has moved to BatchApexErrorEvent in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/sforce_api_objects_batchapexerrorevent.htm) _Platform Events Developer Guide_ .

BillingBatchScheduler
Represents a scheduled processing job that triggers recurring invoice batch runs and payment batch runs in Subscription Management.
This object is available in API version 55.0 and later.

BillingPeriodItem
Represents one payment period for a subscription. The billing period item is used to pass billing information to an invoice line item
in Subscription Management. This object is available in API version 55.0 and later.

BillingPolicy
Represents a group of billing treatments, which define the rules for how to invoice a customer for an order item. This object is
available in API version 55.0 and later.

BillingSchedule
Stores the order item information used in the invoicing process. This object is available in API version 55.0 and later.

BillingScheduleGroup
Represents a consolidated view of all billing schedules related to the order items generated from one asset, including new orders
and amendment orders. This object is available in API version 55.0 and later.


Standard Objects

BillingTreatment
Defines how Subscription Management bills an order item. The Exclude From Billing field controls whether the order item is invoiced.
Child billing treatment items control how much of the order item's balance is invoiced for each invoice across the subscription's
lifecycle. Billing treatments are assigned to order items based on the parent billing policy's Billing Treatment Selection field. This
object is available in API version 55.0 and later.

BillingTreatmentItem
A billing treatment item defines how the order item's total amount is distributed into billing schedules over the course of the order
item's lifecycle. In the Subscription Management pilot, billing treatments must have only one billing treatment item, so that the
billing treatment item covers 100% of the order item's total value. This object is available in API version 55.0 and later.

BlockedRedirectEventLog
Blocked Redirect events capture information about blocked redirections from Salesforce to untrusted and malformed URLs. This
object is available in API version 65.0 and later.

Bookmark
Represents a link between opportunities that share common information.

BotDefinition
Represents a top level object for Einstein Bots or Agentforce Agents. This object is available in API version 60.0 and later.

BotVersion
Represents a version of a bot or agent defined by a BotDefinition record. This object is available in API version 63.0 and later.

BrandingSet
Represents the definition of a set of branding properties for an Experience Builder site, as defined in the Theme panel in Experience
Builder. This object is available in API version 40.0 and later.

BrandTemplate
Letterhead for HTML EmailTemplate.

Brief
Represents a marketing brief. A brief contains information that’s used for positioning and grounding a marketing campaign. Agentforce
can help you create a campaign that best fits the goals and requirements in your brief. This object is available in API version 61.0
and later.

BriefcaseAssignment
Represents the assignment of a briefcase definition to selected users and user groups. This object is available in API version 50.0 and
later.

BriefcaseDefinition
Represents a briefcase definition. A briefcase makes selected records available for users to view when they’re offline in the Salesforce
Field Service mobile app for iOS and Android. This object is available in API version 50.0 and later.

BriefcaseRule
Represents a rule that specifies records for a briefcase definition. This object is available in API version 50.0 and later.

BriefcaseRuleFilter
Represents a filter criteria for a briefcase rule. This object is available in API version 50.0 and later.

BroadcastCommAudience
Represents the audience that the broadcast communication is sent to. This object is available in API version 56.0 and later.

BroadcastCommunication
Represents a broadcast communication related to an incident. This object is available in API version 56.0 and later.


Standard Objects

BroadcastTopic
Represents a definition of a broadcast topic. A broadcast topic is associated with a list of Experience Cloud network sites for Service
Cloud and collaboration rooms for Sales Cloud. The topic is created for a specific user role. Collaboration rooms are linked to Slack
channels. This object is available in API version 55.0 and later.

BroadcastTopicGroup
Represents a junction object that relates a group to an alert type broadcast topic. The broadcast sends the alert to this group. This
object is available in API version 57.0 and later.

BroadcastTopicNetwork
Represents a link between a broadcast topic and the Experience Cloud network site for Service Cloud. This object is available in API
version 56.0 and later.

BrowserPolicyViolation
Represents a violation that occurred within the last seven days related to the Trusted URLs and Trusted URLs for External Redirects
allowlists. These violations include blocked resource requests based on your content security policy (CSP) and blocked redirections.
This object is available in API version 61.0 and later.

BulkApi2EventLog
Bulk API 2 event logs contain details about Bulk API 2.0 requests. This object is available in API version 61.0 and later.

BulkApiEventLog
Bulk API event logs contain details about Bulk API requests. This object is available in API version 61.0 and later.

BulkApiRequestEventLog
The Bulk API request event captures when Bulk API requests are received to create a job, update a job, create a batch, update a batch,
and when a job completes. This object is available in API version 65.0 and later.

BusinessBrand
Represents a unique brand for a business that belongs to a parent entity. This object is available in API version 53.0 and later.

BusinessAlert
Represents information about insight notifications that Einstein Relationship Insights explores, such as news mentions, job updates,
and relationships. This object is available in API version 57.0 and later.

BusinessAlertStatus
Represents information about the read status of an insight alert. This object is available in API version 57.0 and later.

BusinessHours
Specifies the business hours of your support organization. Escalation rules are run only during these hours.

Business Process
Represents a business process. Business Processes track separate sales, lead, support, and solution lifecycles by displaying different
picklist values according to each user’s profile.

BusinessProcessDefinition
Setup object that stores information about stages in a customer lifecycle map. The stages are associated with surveys and questions
created using Salesforce Surveys. This object is reserved for internal use, and is available in API version 49.0 and later.

BusinessProcessFeedback
Setup object that stores information about the survey and the question associated with each stage in a customer lifecycle map.
Customer lifecycle maps are used to track the scores provided by customers across their lifecycle using Salesforce Surveys. This object
is reserved for internal use, and is available in API version 49.0 and later.


Standard Objects

BusinessProcessGroup
Setup object that stores information about customer lifecycle maps. Customer lifecycle maps are used to track the scores provided
by customers across their lifecycle using Salesforce Surveys. This object is reserved for internal use, and is available in API version
49.0 and later.

BuyerAccount
Represents an account that is enabled as a buyer for Lightning B2B Commerce. This object is available in API version 48.0 and later.

BuyerCriteria
Represents the buyer context qualifier of locale for any buyer groups of type Market This object is available in API version 58.0 and
later.

BuyerGroup
Associates group qualifiers (entitlements, price books, promotions, and shipping methods) with buyer members based on buyer
account ID or on the localized language and currency of the market browsed in a webstore. This object is available in API version
57.0; amended to support Market in version 58.0 and later.

BuyerGroupBuyerCriteria
Associates a buyer group that is enabled for webstores supporting multiple languages and currencies with BuyerCriteria that define
those languages and currencies. This object is available in API version 58.0 and later.

BuyerGroupMember
Represents a member of a buyer group. This object is available in API version 55.0 and later.

BuyerGroupPricebook
Represents a buyer group price book used in Lightning B2B Commerce. This object is available in API version 48.0 and later.

BuyerGroupRelatedObject
Used to associate currencies and supported ship-to countries with a buyer group and its price books, promotions, and entitlements.
Supports buyer experience when buyer group members shop in stores enabled for multiple locales. This object is available in API
version 58.0 and later.

CalcProcStepRelationship
Defines a parent-child relationship between two Expression Set Steps in an Expression Set Version. The label for this object is
Expression Set Step Relationship. This object is available in API version 53.0 and later.

CalculatedInsightRangeBound
Stores the information required to calculate a range-bound data insight. This object is available in API version 59.0 and later.

CalculationMatrix
Matches input values to a table row and returns the row's output values. The label for this object is Decision Matrix. This object is
available in API version 53.0 and later.

CalculationMatrixColumn
Defines a column in a Decision Matrix. The label for this object is Decision Matrix Column. This object is available in API version 53.0
and later.

CalculationMatrixRow
Defines a row in a Decision Matrix. The label for this object is Decision Matrix Row. This object is available in API version 53.0 and
later.

CalculationMatrixVersion
Defines a version of a Decision Matrix. The label for this object is Decision Matrix Version. This object is available in API version 53.0
and later.


Standard Objects

CalculationProcedure
Performs a series of calculations using matrix lookups and user-defined variables and constants. The label for this object is Expression
Set. This object is available in API version 53.0 and later.

CalculationProcedureStep
Defines a step in an Expression Set. The label for this object is Expression Set Step. This object is available in API version 53.0 and
later.

CalculationProcedureVariable
Defines a variable in an Expression Set. The label for this object is Expression Set Variable. This object is available in API version 53.0
and later.

CalculationProcedureVersion
Defines a version of an Expression Set. The label for this object is Expression Set Version. This object is available in API version 53.0
and later.

Calendar
Represents a calendar. This can be a default user calendar, public calendar, resource calendar, or holiday calendar. This object is
available in API version 45.0 and later.

CalendarView
These calendars can be created and assigned to users other than the creator. Available calendars include object, shared, public,
resource, and user list calendars. Object calendars represent a calendar based on a Salesforce object, either standard or custom. This
object is available in API version 51.0 and later.

CallCenter
Represents a call center, which is a logical representation of a single computer-telephony integration (CTI) system instance in an
organization.

CallCenterRoutingMap
Stores a mapping between a user or queue in a Salesforce org to a user or queue in an external system’s call center. This object is
available in API version 53.0 and later.

CallCoachingMediaProvider
Represents the media provider for call recordings. This object is available in API version 49.0 and later.

CallCtrAgentFavTrfrDest
Represents a transfer destination that has been marked (starred) as a favorite in the Omni-Channel softphone by a contact center
agent for voice call transfers. This object is available in API version 55.0 and later.

CallCtrAgentFavTrfrDestShare
Represents a sharing entry on a favorite transfer destination in the Omni-Channel softphone for voice call transfers. This object is
available in API version 55.0 and later.

CallDisposition
Represents a call result value that sales reps select when logging a call. This object is available in API version 47.0 and later.

CallDispositionCategory
Represents the call outcome of a phone call that is used in reports and branching criteria for cadences. This object is available in API
version 47.0 and later.

CallTemplate
Represents a call script for users to read when making calls.

Campaign
Represents and tracks a marketing campaign, such as a direct mail promotion, webinar, or trade show.


Standard Objects

CampaignInfluence
Represents the association between a campaign and an opportunity in Customizable Campaign Influence. This object is available
in API version 37.0 and later.

CampaignInfluenceModel
This read-only object represents a campaign influence model in Customizable Campaign Influence. Use campaign influence models
to group `CampaignInfluence` records created by a specific set of triggers and workflows that you define. The Primary Campaign
Source influence model is the default model. This object is available in API version 37.0 and later.

CampaignMember
The CampaignMember object represents the relationship between a campaign and either a lead or a contact. If the Accounts as
Campaign Members setting is enabled in an org, CampaignMember can also represent the relationship between a campaign and
an account.

CampaignMemberStatus
One or more member status values defined for a campaign.

CampaignOwnerSharingRule
Represents the rules for sharing a campaign with User records other than the owner or anyone above the owner in the role hierarchy.

CampaignShare
Represents a sharing entry on a Campaign.

CampaignTag
Associates a word or short phrase with a Campaign.

CardPaymentMethod
Represents a credit card or debit card payment method, which implements the PaymentMethod object. This object is available in
API version 48.0 and later.

CartCheckoutSession
Represents a checkout session used in Lightning B2B Commerce checkout. This object is available in API version 48.0 and later.

CartDeliveryGroup
Represents shipping information for the delivery of items in an order against a store built with B2B Commerce or D2C Commerce.
This object is available in API version 49.0 and later.

CartDeliveryGroupMethod
Represents the selected delivery method for a cart delivery group used in Lightning B2B Commerce checkout. This object is available
in API version 49.0 and later.

CartDeliveryGroupMethodAdj
Represents the shipping promotion discount for a shipping method. This object is available in API version 60.0 and later.

CartItem
Represents an item in a `WebCart` that’s active in a store built with B2B. Cart item can be of type `Product` or `Charge` . This
object is available in API version 49.0 and later.

CartItemAttribute
Represents the attributes associated with a cart item, stored as key-value pairs. These attributes are derived from the product and
carried forward to the order during checkout. This object is available in API version 66.0 and later.

CartItemPriceAdjustment
Price adjustment for a cart item. This object is available in API version 52.0 and later.


Standard Objects

CartTax
Represents taxes for a line item in a `WebCart` that’s active in a store built with B2B Commerce or D2C Commerce. This object is
available in API version 49.0 and later.

CartValidationOutput
Associate errors to cart entities, such as cart line items, delivery groups, and the like, in a store built with B2B Commerce or D2C
Commerce. An example error is “Out of stock.” Available in API version 49.0 and later.

Case
Represents a case, which is a customer issue or problem.

CaseArticle
Represents the association between a Case and a KnowledgeArticle. This object is available in API version 20.0 and later.

CaseComment
Represents a comment that provides additional information about the associated Case.

CaseContactRole
Represents the role that a given Contact plays on a Case.

CaseHistory
Represents historical information about changes that have been made to the associated Case.

CaseHistory2
Represents historical information about owner and status changes that have been made to the associated Case. This object is available
in API version 59.0 and later.

CaseMilestone
Represents a milestone (required step in a customer support process) on a Case. This object is available in API version 18.0 and later.

CaseOwnerSharingRule
Represents the rules for sharing a case with users other than the owner.

CaseParticipant
Represents a junction between a case, and an account or a contact. This object stores the details of the participant associated with
a case. This participant could be the applicant, co-applicant, a household, or even a business account. This object is available in API
version 54.0 and later.

CaseRelatedIssue
This object acts as a junction between a customer issue (Case) and the Incident or Problem that represents an associated service
failure. This object is available in API version 53.0 and later.

CaseShare
Represents a sharing entry on a Case.

CaseSolution
Represents the association between a Case and a Solution.

CaseStatus
Represents the status of a Case, such as New, On Hold, or In Process.

CaseSubjectParticle
Represents the Social Business Rules custom format for the **Case Subject** field on cases created from inbound social posts. This
object is available in API version 41.0 and later.

CaseTag
Associates a word or short phrase with a Case


Standard Objects

CaseTeamMember
Represents a case team member, who works with a team of other users to help resolve a case.

CaseTeamRole
Represents a case team role. Every case team member has a role on a case, such as “Customer Contact” or “Case Manager.”

CaseTeamTemplate
Represents a predefined case team, which is a group of users that helps resolve a case.

CaseTeamTemplateMember
Represents a member on a predefined case team, which is a group of users that helps resolve cases.

CaseTeamTemplateRecord
The CaseTeamTemplateRecord object is a linking object between the Case and CaseTeamTemplate objects. To assign a predefined
case team to a case (customer inquiry), create a CaseTeamTemplateRecord record and point the `ParentId` to the case and the
`TeamTemplateId` to the predefined case team.

CategoryData
Represents a logical grouping of Solution records.

CategoryNode
Represents a tree of Solution categories.

CategoryNodeLocalization
When the Translation Workbench is enabled for your organization, the CategoryNodeLocalization object provides the translation of
the label of a solution category.

ChangeRequest
Represents a decision to implement a formal request for a change (RFC). This object is available in API version 53.0 and later.

ChangeRequestRelatedIssue
Represents a junction object that relates a ChangeRequest to an Incident or Problem due to a service failure. This object is available
in API version 53.0 and later.

ChangeRequestRelatedItem
Represents a junction object that relates a ChangeRequest to an Asset. This object is available in API version 53.0 and later.

ChangeSetOperationEventLog
Change Set Operation events contain information from change set migrations. This object is available in API version 65.0 and later.

ChannelObjectLinkingRule
Represents a rule for linking a channel interaction with an object (such as Lead or Contact). This object is available in API version
47.0 and later.

ChannelProgram
Represents a channel program that vendors use to market and sell their products through channel partners. This object is available
in API version 41.0 and later.

ChannelProgramLevel
Represents a level, based on member experience, in a channel program. This object is available in API version 41.0 and later.

ChannelProgramMember
Represents a partner who is a member of a channel program. This object is available in API version 41.0 and later.

ChatterActivity
ChatterActivity represents the number of posts and comments made by a user and the number of comments and likes on posts
and comments received by the same user. This object is available in API version 23.0 and later.


Standard Objects

ChatterAnswersActivity
Represents the reputation of a User in Chatter Answers zones.This object is available in API version 25.0 and later.

ChatterAnswersReputationLevel
Represents a reputation level within a Chatter Answers zone. This object is available in API version 26.0 and later.

ChatterConversation
Represents a private conversation in Chatter, consisting of messages that conversation members have sent or received. This object
is available in API version 23.0 and later.

ChatterConversationMember
Represents a member of a private conversation in Chatter. A member has either sent messages to or received messages from other
conversation participants. This object is available in API version 23.0 and later.

ChatterExtension
Represents a Rich Publisher App that’s integrated with the Chatter publisher. This object is available in API version 41.0 and later.

ChatterExtensionConfig
Configuration for the Chatter extension for Experience Cloud sites. This object is available in API version 41.0 and later.

ChatterMessage
Represents a message sent as part of a private conversation in Chatter. This object is available in API version 23.0 and later.

ClientBrowser
Represents a cookie added to the browser upon login, and also includes information about the browser application where the cookie
was inserted. This object is available in version 28.0 and later.

CollaborationGroup
Represents a Chatter group. This object is available in API version 19.0 and later.

CollaborationGroupMember
Represents a member of a Chatter group. This object is available in API version 19.0 and later.

CollaborationGroupMemberRequest
Represents a request to join a private Chatter group. This object is available in API version 21.0 and later.

CollaborationGroupRecord
Represents the records associated with Chatter groups.

CollaborationInvitation
Represents an invitation to join Chatter, either directly or through a group. This object is available in API version 21.0 and later.

CollaborationRoom
Represents a collaboration room, which links Salesforce to a Slack channel used by applications with specific use cases, such as
swarming or reporting. This object is available in API version 55.0 and later.

CollabDocumentMetric
Represents the engagement metrics for a Quip thread (document or spreadsheet) that’s linked to a Salesforce record. This object is
available in API version 50.0 and later.

CollabDocumentMetricRecord
Represents an association between a CollabDocumentMetric and a Salesforce record.It tracks which Salesforce record, such as an
Account or Contact, is linked to a Quip thread for which metrics were gathered using CollabDocumentMetric.
CollabDocumentMetricRecord is available in API version 50.0 and later.

CollabTemplateMetric
Represents the engagement metrics for a Quip template.This object is available in API version 50.0 and later.


Standard Objects

CollabTemplateMetricRecord
Represents an association between a CollabTemplateMetric and a Salesforce record.It tracks which Salesforce record, such as an
Account or Contact, is linked to a Quip template for which metrics were gathered using CollabTemplateMetric.
CollabTemplateMetricRecord is available in API version 50.0 and later.

CollabUserEngagementMetric
Represents the user engagement metrics for a Quip thread in a Quip template or document. This object is available in API version
50.0 and later.

CollabUserEngmtRecordLink
Represents an association between a CollabUserEngagementMetric and a Salesforce record. It tracks which Salesforce record, such
as an Account or Contact, is associated with the user engagement metric. This object is available in API version 50.0 and later.

ColorDefinition
Represents the color-related metadata for a custom tab. This object is available in API version 43.0 and later.

ContCalloutSummaryEventLog
Continuation Callout Summary events contain information about all of the asynchronous callouts performed during a transaction,
their response status codes, execution times, and URL endpoint destinations. This object is available in API version 65.0 and later.

CombinedAttachment
This read-only object contains all notes, attachments, Google Docs, documents uploaded to libraries in Salesforce CRM content, and
files added to Chatter that are associated with a record.

CommerceEntitlementBuyerGroup
Represents the entitlement policy for a buyer group. This object is available in API version 49.0 and later.

CommerceEntitlementPolicy
Represents an entitlement policy, which determines what products and prices a user can see. This object is available in API version
49.0 and later.

CommerceEntitlementPolicyShare
Represents the entitlement rule for sharing products and prices with users other than the owner. This object is available in API version
49.0 and later.

CommerceEntitlementProduct
Represents the entitlement policy for a product. This object is available in API version 49.0 and later.

CommissionSchedule
Represents a commission calculation and rate definition. Calculates commission values for a commissionable event.

CommissionScheduleAssignment
Represents the commission calculation applicable to a specific product or producer for one or multiple commissionable events.

CommSubscription
Represents the subscription options for a specific communication. This object is available in API version 48.0 and later.

CommSubscriptionChannelType
Represents the engagement channel through which you can reach a customer for a communication subscription. This object is
available in API version 48.0 and later.

CommSubscriptionConsent
Represents a customer’s consent to a communication subscription. This object is available in API version 48.0 and later.

CommSubscriptionTiming
Represents a customer's timing preferences for receiving a communication subscription. This object is available in API version 48.0
and later.


Standard Objects

Community (Zone)
Represents a zone that contains Idea or Question objects.

ConcurApexLimitEventLog
Concurrent Apex Limit event logs contain information about long-running concurrent Apex requests in your org that Salesforce
terminated after reaching your org’s concurrency limit. Requests with an established Apex context that execute for 5 seconds are
counted towards your org’s limit of concurrent long-running requests. (Asynchronous requests don’t count towards the limit.) When
the long-running requests exceed the org default limit, additional long-running requests are denied. This object is available in API
version 61.0 and later.

ConnectedApplication
Represents a connected app and its details; all fields are read-only.

ConferenceNumber
Holds the telephone number for an external event shown in the Salesforce Today feature in the Salesforce mobile app. This object
is available in API version 35.0 and later.

Consumption Rate
Consumption rates describe the billing rate for a range of usage within a consumption schedule. All consumption schedules require
at least one consumption rate in order to rate usage on a usage product. This object is available in API version 45.0 and later.

Consumption Schedule
A consumption schedule organizes a set of consumption rates by which usage-based products are quoted and billed. This object
is available in API version 45.0 and later.

Contact
Represents a contact, which is a person associated with an account.

ContactCenterChannel
Represents a junction object that relates a Bring Your Own Channel for Contact Center as a Service (CCaaS) messaging channel to
a CallCenter object for Bring Your Own Channel for CCaaS. This object also represents the routing details for a voicemail configuration
and routing information for callback requests. This object is available in API version 56.0 and later.

ContactCleanInfo
Stores the metadata Data.com Clean uses to determine a contact record’s clean status. Helps you automate the cleaning or related
processing of contact records. ContactCleanInfo includes a number of bit vector fields. This object is removed in API version 67.0

ContactDailyMetric
Represents the daily engagement metrics for a contact. This object is available in API version 52.0 and later.

ContactMonthlyMetric
Represents the monthly engagement metrics for a contact. This object is available in API version 52.0 and later.

ContactPointAddress
Represents a contact’s billing or shipping address, which is associated with an individual or person account. This object is available
in API version 49.0 and later.

ContactPointConsent
Represents a customer's consent to be contacted via a specific contact point, such as an email address or phone number. This object
is available in API version 48.0 and later.

ContactPointEmail
Represents a contact’s email, which is associated with an individual or person account. This object is available in API version 48.0
and later.


Standard Objects

ContactPointPhone
Represents a contact’s phone number, which is associated with an individual or person account. This object is available in API version
48.0 and later.

ContactPointTypeConsent
Represents consent for a contact point type, such as email or phone. This object is available in API version 45.0 and later.

ContactOwnerSharingRule
Represents the rules for sharing a contact with a User other than the owner.

ContactRequest
Represents a customer’s request for support to get back to them about an issue. This object is available in API version 45.0 and later.

ContactRequestShare
Represents a list of access levels to a ContactRequest with an explanation of the access level. This object is available in API version
45.0 and later.

ContactShare
Represents a list of access levels to a Contact along with an explanation of the access level. For example, if you have access to a
record because you own it, the `ContactAccessLevel` is `All` and `RowCause` is Owner.

ContactSuggestionInsight
Represents a suggestion for a new contact record. Available in API versions 45.0 and later.

ContactTag
Associates a word or short phrase with a Contact.

ContentAsset
Represents a Salesforce file that has been converted to an asset file in a custom app in Lightning Experience. Use asset files for org
setup and configuration. Asset files can be packaged and referenced by other components. This object is available in API version
38.0 and later.

ContentBody
Represents the body of a file in Salesforce CRM Content or Salesforce Files. This object is available in API version 40.0 and later.

ContentDistribution
Represents information about sharing a document externally. This object is available in API version 32.0 and later.

ContentDistributionEventLog
Content Distribution events contain information about content distributions and deliveries to users. This object is available in API
version 65.0 and later.

ContentDistributionView
Represents information about views of a shared document. This read-only object is available in API version 32.0 and later.

ContentDocument
Represents a document that was uploaded to a library in Salesforce Files or Salesforce CRM content. This object is available in versions
17.0 and later for Salesforce CRM.This object is available in API version 21.0 and later for Salesforce Files.

ContentDocumentHistory
Represents the history of a document. This object is available in versions 17.0 and later.

ContentDocumentLink
Represents the link between a Salesforce CRM Content document, Salesforce file, or ContentNote and where it's shared. A file can
be shared with other users, groups, records, and Salesforce CRM Content libraries. This object is available in versions 21.0 and later
for Salesforce CRM Content documents and Salesforce Files.


Standard Objects

ContentDocumentListViewMapping
Represents an association between a ListView and a Quip ContentDocument. Applies to Quip file types only. Maintains the mapping
between a list view and Quip document when the list view is exported to a newly created Quip document. This object is available
in API version 44.0 and later.

ContentDocumentSubscription
Represents a subscription for a user following or commenting on a file in a library. This object is available in API version 42.0 and
later.

ContentDocLinkEventLog
Content Document Link events contain sharing information for content documents. This object is available in API version 65.0 and
later.

ContentFolder
Represents a folder in a content library for adding files. This object is available in API version 34.0 and later.

ContentFolderItem
Represents a file (ContentDocument) or folder (ContentFolder) that resides in a ContentFolder in a ContentWorkspace. This object
is available in API version 35.0 and later.

ContentFolderLink
Defines the association between a library and its root folder. This object is available in API version 34.0 and later.

ContentFolderMember
Defines the association between a file and a folder. This object is available in API version 34.0 and later.

ContentHubItem
Represents a file or folder in a Files Connect external data source, such as Microsoft SharePoint or OneDrive for Business. This object
is available in API version 33.0 and later.

ContentHubRepository
Represents a Files Connect external data source such as Microsoft SharePoint or OneDrive for Business. This object is available in API
version 33.0 and later.

ContentNote
Represents a note created with the enhanced note-taking tool, released in Winter ’16. This object is available in API version 32.0 and
later.

ContentNotification
Represents a notification for a file. This object is available in API version 42.0 and later.

ContentTagSubscription
Represents a subscription for a user following a tag on a file. This object is available in API version 42.0 and later.

ContentTaxonomy
Represents a content taxonomy, which is used to classify and organize Salesforce CMS content. To create a hierarchy of terms in a
content taxonomy, use this object in addition to the ContentTaxonomyTerm, ContentTaxonomyRelatedTerm, and
ContentTaxonomyTermRelatedTerm objects. This object is available in API version 63.0 and later.

ContentTaxonomyRelatedTerm
Represents the relationship between a term and the content taxonomy to which the term belongs. This object is available in API
version 63.0 and later.

ContentTaxonomyTerm
Represents a term in a content taxonomy. Terms describe what content is or how it's used, and they’re organized in parent-child
relationships in the taxonomy hierarchy. This object is available in API version 63.0 and later.


Standard Objects

ContentTaxonomyTermRelatedTerm
Represents the relationship between two terms in a content taxonomy. This object is available in API version 63.0 and later.

ContentTaxonomyTermRelationshipType
Represents the type of relationship between two terms in a content taxonomy. This object is available in API version 63.0 and later.

ContentTransferEventLog
ContentTransferEventLog stores information about content transfer events, such as downloads, uploads, and previews. This information
includes events performed on files and attachments to records. This object is available in API version 62.0 and later.

ContentUserSubscription
Represents a subscription for a user following another user. This object is available in API version 42.0 and later.

ContentVersion
Represents a specific version of a document in Salesforce CRM content or Salesforce Files. This object is available in versions 17.0
and later for Salesforce CRM content documents. This object is available in versions 20.0 and later for Salesforce Files.

ContentVersionComment
Represents a comment on a version of a file. This object is available in API version 42.0 and later.

ContentVersionHistory
Represents the history of a specific version of a document. This object is available in version 17.0 and later.

ContentVersionRating
Represents a rating on a version of a file. This object is available in API version 42.0 and later.

ContentWorkspace
Represents a content library. This object is available in versions 17.0 and later.

ContentWorkspaceDoc
Represents a link between a document and a public library in Salesforce CRM Content. This object is available in versions 17.0 and
later.

ContentWorkspaceMember
Represents a member of a content library. This object is available in API version 40.0 and later.

ContentWorkspacePermission
Represents a library permission. This object is available in API version 40.0 and later.

ContentWorkspaceSubscription
Represents a subscription for a user following a library. This object is available in API version 42.0 and later.

ContextParamMap
Represents optional context data for a Conversation or a ConversationParticipant. This object is available in API version 57.0 and
later.

Contract
Represents a contract (a business agreement) associated with an Account.

ContractContactRole
Represents the role that a Contact plays on a Contract.

ContractLineItem
Represents a product covered by a service contract (customer support agreement). This object is available in API version 18.0 and
later.


Standard Objects

ContractLineOutcome
Represents information on a contract line outcome’s captured data and other related parameters that are used when capturing data.
This object is available in API version 58.0 and later.

ContractLineOutcomeData
Represents the contract line outcome’s captured data. It stores the data that was captured between the contract line outcome’s
start date and end date. This object is available in API version 58.0 and later.

ContractStatus
Represents the status of a Contract, such as Draft, InApproval, Activated, Terminated, or Expired.

ContractTag
Associates a word or short phrase with a Contract.

ConvAnalysisSummary
Represents the information stored for each run or refresh of Sales Signals. This object is available in API version 63.0 and later.

ConvAnalysisTopic
Represents a topic generated from the Sales Signals refresh or run. For example, a product experiencing issues due to high pricing
could be a topic identified through the analysis of multiple calls. This object is available in API version 63.0 and later.

ConvAnalysisTopicEntry
Represents a single entry under the ConvAnalysisTopic object. An entry represents a segment of a video or voice call that is associated
with a conversation analysis topic. This object is available in API version 63.0 and later.

Conversation
Represents a conversation between an end user and an agent. Available in API version 49.0 and later.

ConversationApiLog
Logs of an API operation on a specific conversation object done using the Conversation Service API. This object is available in API
version 63.0 and later.

ConversationContextEntry
Represents the context of a message or an event in the chat history between an agent and a messaging user. This object is available
in API version 47.0 and later.

ConversationChannelDefinition
Represents a configurable definition of a conversation channel that’s implemented for Interaction Service for Bring Your Own Channel
for Messaging and Bring Your Own Channel for CCaaS messaging channels. This object is available in API version 60.0 and later.

ConversationEntry
Represents a message or event in a voice call or messaging session. The schema on this page only applies to conversation entries
[for legacy chat. Refer to the ConversationEntry (Off-Core) schema in the Messaging Object Model guide to see the ConversationEntry](https://developer.salesforce.com/docs/service/messaging-object-model/guide/overview.html)
schema for Enhanced Channels. This object is available in API version 43.0 and later.

ConversationParticipant
Represents an active participant in a conversation. A new ConversationParticipant record is created each time a participant joins a
conversation. This object is available in API version 49.0 and later.

ConvIntelligenceSignalRule
Represents a conversation intelligence signal rule. The rule triggers actions based on real-time intelligence signals from your telephony
system or keywords mentioned by support reps or customers. The rule contains a set of conditions (subrules) and the filter logic
used to evaluate those conditions to determine whether to trigger actions. This object is available in API version 62.0 and later.

ConvIntelligenceSignalSubRule
Represents a condition (subrule) within a conversation intelligence signal rule. This object is available in API version 62.0 and later.


Standard Objects

ConvMessageSendRequest
Represents a request to send a template-based messaging component to a series of messaging users in an enhanced messaging
channel or Messaging for In-App. This object is available in API version 60.0 and later.

ConversationVendorInfo
This setup object connects the partner vendor system to the Service Cloud feature. For example, for Salesforce Voice with Telephony
Providers, this object contains information about the partner telephony or Contact Center as a Service (CCaaS) partner system. For
Bring Your Own Channel for Messaging this object contains information about the partner messaging system, and for Bring Your
Own Channel for CCaaS, this object contains information about the CCaaS partner system. This object is available in API version 52.0
and later.

CorsWhitelistEntry
Represents an entry in the cross-origin resource sharing (CORS) allowlist. Origins included in the allowlist can request REST resources
from that Salesforce org.

Coupon
A coupon associated with a promotion. This object is available in API version 54.0 and later.

CouponCodeRedemption
Tracks each coupon code redemption. This object is available in API version 58.0 and later.

CreditMemo
Represents a document that is used to reduce the amount that a buyer owes a seller under the terms of an earlier invoice. This object
is available in API version 48.0 and later.

CreditMemoAddressGroup
Stores the buyer's address information, which is used to determine the amount of tax to credit to a buyer when a credit memo is
issued. This object is available in API version 55.0 and later.

CreditMemoInvApplication
Represents an amount applied from a credit memo to an invoice. This object is available in API version 48.0 and later.

CreditMemoLine
Represents product, service, adjustment, or tax line items that were included in a credit memo. This object is available in API version
48.0 and later.

Crisis
Represents a major crisis event that affects an Employee in an InternalOrganizationUnit. This object is available in API version 48.0
and later. In API version 49.0 and later, this object supports reports, criteria-based sharing rules, and history tracking, plus you can
exclude individual fields from custom page layouts.

CronJobDetail
Contains details about the associated scheduled job, such as the job’s name and type. This object is available in API version 29.0 and
later.

CronTrigger
Contains schedule information for a scheduled job. CronTrigger is similar to a cron job on UNIX systems. This object is available in
API version 17.0 and later.

CryptoProdCatgWalletGroup
Specifies if CryptoWalletGroup is in the allowlist or airdrop for the ProductCategory. A custom object between ProductCategory and
CryptoWalletGroup adding the CryptoWalletGroup to allowlist or airdrop. This object is available in API version 58.0 and later.


Standard Objects

CspTrustedSite
Represents a trusted URL. For each CspTrustedSite, you can specify Content Security Policy (CSP) directives and permissions policy
directives. Each CSP directive allows Lightning components, third-party APIs, and WebSocket connections to access a resource type
from the trusted URL. If the Permissions-Policy HTTP header is enabled, each permissions policy directive grants the trusted URL
access to a browser feature. In API version 58.0 and earlier, CspTrustedSite included only CSP directives and was referred to as CSP
Trusted Sites in Salesforce Setup. Available in API version 39.0 and later.

CspViolationEventLog
CSP violation events capture details about blocked resource requests from Lightning Experience pages based on your content
security policy (CSP). This object is available in API version 63.0 and later.

CurrencyType
Represents the currencies used by an organization for which the multicurrency feature is enabled.

CustExpIntlTransfSetup
Stores information for different data sources that are processed for customer insights. This object is available in API version 65.0 and
later.

CustomBrand
Represents a custom branding and color scheme. This object is available in API version 28.0 and later.

CustomBrandAsset
Represents a branding element in a custom branding scheme. For example, a color, logo image, header image, or footer text. A
CustomBrandAsset can apply to an Experience Cloud site or to an org using the Salesforce mobile app. This object is available in API
version 28.0 and later.

CustomFieldDisplayValue
Stores variation details for the product attribute item view. This object is available in API version 63.0 and later.

CustomHelpMenuItem
Represents the items within a section of the Lightning Experience help menu that the admin added to display custom, org-specific
help resources. This object is available in API version 44.0 and later.

CustomHelpMenuSection
Represents a section of the Lightning Experience help menu that the admin added to display custom, org-specific help resources.
This object is available in API version 44.0 and later.

CustomHttpHeader
Represents a custom HTTP header that provides context information from Salesforce such as region, org details, or the role of the
person viewing the external object. This object is available in API version 43.0 and later.

CustomMsgChannel
Represents a custom conversation channel and stores event-driven Messaging settings. Custom conversation channels are
implemented for Bring Your Own Channel for Messaging and Bring Your Own Channel for CCaaS Messaging channels. This object
is available in API version 63.0 and later.

CustomNotificationType
Stores information about custom notification types. This object is available in API version 47.0 and later.

CustomPermission
Represents a permission created to control access to a custom process or app, such as sending email. This object is available in API
version 31.0 and later.

CustomPermissionDependency
Represents the dependency between two custom permissions when one custom permission requires that you enable another
custom permission. This object is available in API version 32.0 and later.


Standard Objects

Customer
Represents the customer role of an individual with respect to a particular company or organization. This object is available in API
version 53.0 and later.

DandBCompany
Represents a Dun & Bradstreet [®] company record, which is associated with an account added from Data.com. This object is available
in API version 25.0 and later.

Dashboard
Represents a dashboard, which shows data from custom reports as visual components. Access is read-only. This object is available
in API version 20.0 and later.

DashboardComponent
Represents a dashboard component, which can be a chart, metric, table, or gauge on a dashboard. Access is read-only. This object
is available in API version 21.0 and later.

DashboardTag
Associates a word or short phrase with a Dashboard. This object is available in API version 20.0 and later.

DataAssessmentFieldMetric
Represents summary statistics for matched, blank, and differing fields in account records of an org compared to records in Data.com.
This object is available in API version 37.0 and later.

DataAssessmentMetric
Represents a summary of statistics for fields matched and unmatched in your account records with Data.com account records. This
object is available in API version 37.0 and later.

DataAssessmentValueMetric
Summarizes the number of fields matched for your account records with Data.com account records.This object is available in API
version 37.0 and later.

DatabaseSaveEventLog
Database Save events track when records are created,updated, or deleted This object is available in API version 64.0 and later.

DatacloudCompany
Represents the fields for Data.com company records. This object is available in API version 30.0 or later.

DatacloudContact
The fields and properties for Data.com contact records. This object is available in API version 30.0 or later.

DatacloudDandBCompany
Represents a set of read-only fields that are used to return D&B company data from Data.com API calls. This object is available in API
version 30.0 or later.

DatacloudOwnedEntity
Represents fields in the DatacloudOwnedEntity object. The DatacloudOwnedEntity object tracks user-purchased records. This object
is available in API version 30.0 or later.

DatacloudPurchaseUsage
Represents an object used to identify and track Data.com record purchases. This object is available in API version 30.0 or later.

DataDetectJobObjectSession
For internal use only. This object is available in API version 63.0 and later.

DataDetectJobSession
Represents a run of a DataDetect scan policy that's triggered manually. This object is available in API version 63.0 and later.


Standard Objects

DataDetectJobSessSummary
For internal use only. This object is available in API version 66.0 and later.

DataDetectPolicy
Represents a set of parameters that specifies the types of sensitive data for search with in a data scan. DataDetect scan policies can
also apply filters to a data scan, along with specific objects and fields for scanning. This object is available in API version 60.0 and
later.

DataDetectPolicyObject
Represents an object of the DataDetect scan policy to be scanned. This object is available in API version 62.0 and later.

DataDetectScanResult
Represents the results of a DataDetect data policy scan. This object is available in API version 63.0 and later.

DataDetectPolicyObjField
Represents an object field of the DataDetect scan policy object to be scanned. This object is available in API version 64.0 and later.

DataDetectPolicySnapshot
For internal use only. This object is available in API version 64.0 and later.

DataDetPlcyDataSrchExps
Represents data search expressions for scanning DataDetect scan policies based on Java regex. This object is available in API version
64.0 and later.

DataDetPlcyMdatScanCrit
Represents inclusion and exclusion criteria that filter what DataDetect scan policy object fields are to be scanned based on metadata
tags. This object is available in API version 64.0 and later.

DataDetPlcySstvDataCatg
Represents the sensitive data categories that the DataDetect scan policy is required to scan. This object is available in API version
64.0 and later.

DataEncryptionKey
The DataEncryptionKey object is part of the Bring Your Own Key (BYOK) feature, which allows users to upload a data encryption key
(DEK) using a public key generated by the Salesforce Shield Key Management Service (KMS). Customers create their own DEKs and
upload them to Salesforce. Users access this entity via the API to list DEK keys for auditing purposes. They can also programmatically
use this object to create the certificate and to upload key material. This object is available in API version 63.0 and later.

DataIntegrationRecordPurchasePermission
Indicates Lightning Data purchase credits that a Salesforce admin has granted to users.

DataKitDeployEvent
Represents a data kit deployment event that notifies subscribers of the status of the data kit component deployment. This object is
available in API version 61.0 or later.

DataKitDeploymentLog
Represents the log details of a data kit component deployment. This object is available in API version 61.0 or later.

DatasetExport
Represents a dataset exported from CRM Analytics. When a dataset is exported, the data is converted into a .csv file and the schema
is stored in a separate JSON file. These files are stored in two objects: DatasetExport and DatasetExportPart. DatasetExport acts as
the header and includes the JSON schema.

DatasetExportPart
Represents a dataset exported from CRM Analytics. When a dataset is exported, the data is converted into a .csv file and the schema
is stored in a separate JSON file. These files are stored in two objects: DatasetExport and DatasetExportPart. DatasetExportPart contains
parts of the .csv file.


Standard Objects

DataMaskCustomValueLibrary
Represents a set of user-inputted values in a custom library in Data Mask. This object is available in API version 64.0 and later.

DataStatistics
For internal use only.

DataUseLegalBasis
Represents the legal basis for contacting a customer, such as billing or contract. This object is available in API version 45.0 and later.

DataUsePurpose
Represents the reason for contacting a prospect or customer, such as for billing, marketing, or surveys. This object is available in API
version 45.0 and later.

DataWeaveResource
Represents the DataWeaveScriptResource class that is generated for all DataWeave scripts. This object is available in API version 58.0
and later.

DatedConversionRate
Represents the dated exchange rates used by an organization for which the multicurrency and the effective dated currency features
are enabled.

DealIndirectPartner
Represents an indirect partner’s involvement in a deal. This object is available in API version 63.0 and later.

DeclinedEventRelation
Represents event participants (invitees or attendees) with the status `Declined` for a given event. This object is available in API
versions 29.0 and later.

DelegatedAccount
Represents the external managed account. This object is available in API version 49.0 and later.

DeleteEvent
Represents a record that has been soft deleted. Search on this object was available in API version 48.0, then removed in API version
50.0.

DeliveryEstimationSetup
Shows the configuration options for the commerce delivery service offered through a web store or sales channel. Includes settings
such as delivery location group, channel, fulfillment types, and default fulfillment time. This object is available in API version 61.0
and later.

DigitalSignature
Represents a signature captured on a service report in field service.

DigitalWallet
Represents a customer’s digital wallet service. Salesforce Payments can use a digital wallet as a payment source when processing
payments through a payment gateway. This object is available in API version 48.0 and later.

DirectMessage
Represents a direct message conversation between multiple users in Chatter. This object is available in API version 38.0 and later.

Division
A logical segment of your organization's data. For example, if your company is organized into different business units, you could
create a division for each business unit, such as “North America,” “Healthcare,” or “Consulting.” Available only if the organization has
the Division permission enabled.


Standard Objects

DivisionLocalization
When the Translation Workbench is enabled for your organization, the DivisionLocalization object provides the translation of the
label for a division.

DocAtchDownloadEventLog
Document Attachment Downloads events contain details of document and attachment downloads. This object is available in API
version 65.0 and later.

Document
Represents a file that a user has uploaded. Unlike Attachment records, documents are not attached to a parent object.

DocumentAttachmentMap
Maps the relationship between an EmailTemplate and its attachment, which is stored as a Document.

DocumentRecipient
Connects a Service Report to a Digital Signature. This object is available in API version 55.0 and later.

DocumentTag
Associates a word or short phrase with a Document.

Domain
Read-only object that represents a custom Web address assigned to a site in your organization. This object is available in API version
26.0 and later.

DomainSite
Read-only junction object that joins the Site and Domain objects. This object is available in API version 26.0 and later.

DsarPolicy
Represents a Data Subject Access Request (DSAR) policy created in the Privacy Center managed package. DSAR policies anonymize
or transfer personal data from your org at your customer’s request. This object is available in API version 50.0 and later.

DsarPolicyLog
Represents the history of Data Subject Access Request (DSAR) policy execution requests. This log records the status and results of
executed DSAR policies for a customer. This object is available in API version 50.0 and later.

DuplicateJob
Represents an instance of a job that identifies duplicates among existing records in the system.

DuplicateJobDefinition
Setup object defining a job that identifies duplicate record items globally.

DuplicateJobMatchingRule
Represents a MatchingRule to be used with a DuplicateJob sharing the corresponding DuplicateJobMatchingRuleDefinition.

DuplicateJobMatchingRuleDefinition
Setup object specifying a MatchingRule to use with DuplicateJob instances that share a DuplicateJobDefinition.

DuplicateRecordItem
Represents a record that’s been identified as a duplicate. DuplicateRecordItems are included in a DuplicateRecordSet, which are
processed in duplicate jobs. Use this object to create custom report types for duplicates.

DuplicateRecordSet
Represents a group of records that have been identified as duplicates. Each duplicate record set contains one or more duplicate
record items. Use this object to create custom report types and view the results of duplicate jobs.

DuplicateRule
Represents a duplicate rule for detecting duplicate records.


Standard Objects

DynamicDataCapture
DynamicDataCapture is a junction object that adds a Form tab to Work Order Overview, and to the related list of a work order, work
order line item, or service appointment in the Field Service mobile app. This object is available in API version 62.0 and later.

ElectronicMediaGroup
Represents the type of media that you can associate with a product or category.This object is available in API version 49.0 and later.

ElectronicMediaUse
Represents the usage of media. This object is available in API version 49.0 and later.

EmailContent
Represents a marketing email asset for use with Account Engagement. This object is available in API version 50.0 and later.

EmailDomainFilter
Represents a filter that determines whether an email relay is restricted to a specific list of domains. This object is available in API
version 43.0 and later.

EmailDomainKey
Represents a domain key for an organization’s domain, used to authenticate outbound email that Salesforce sends on the organization’s
behalf. This object is available in API version 28.0 and later.

EmailInsight
Represents an insight generated from an email interaction. EmailInsights acts as a central place to store various types of insights
related to email messages. The insights stored include status, type, and time of generation. Only certain types of insights can be
created based on a pre-configured list of insight types. This object is available in API version 63.0 and later.

EmailInsightAction
Represents the actions that have been taken, or could be taken, in relation to email insights. It logs different types of actions and
associated metadata, helping to track and manage the activities and decisions made based on email insights. This object is available
in API version 63.0 and later.

EmailMessage
Represents an email in Salesforce.

EmailMessageMigration
For internal use only.

EmailMessageRelation
Represents the relationship between an email and contacts, leads, and users. This object is available in API version 37.0 and later.

EmailRelay
Represents the configuration for sending an email relay. An email relay routes email sent from Salesforce through your company’s
email servers. This object is available in API version 43.0 and later.

EmailRoutingAddress
An email address used for Email-to-Case. Email routing addresses store a unique email services address provided by Salesforce and
configuration options for emails received by this address.

EmailServicesAddress
An email service address.

EmailServicesFunction
An email service.

EmailStatus
Represents the status of email sent.


Standard Objects

EmailTemplate
Represents a template for an email, mass email, list email, or Sales Engagement email. Supported in first-generation managed
packages only.

EmailTemplateMonthlyMetric
Represents the monthly engagement metrics for an email template. This object is available in API version 53.0 and later.

EmbeddedServiceDetail
Represents a metadata catalog object that exposes fields from the underlying Embedded Service setup objects defined in each
EmbeddedServiceConfig deployment for guest users. Guest users don’t have direct access to the Embedded Service setup objects.
Available in API version 39.0 and later.

EmbeddedServiceLabel
Represents a customized label in Embedded Chat or embedded Appointment Management.This object is available in API version
44.0 and later.

Employee
Represents an employee within a company or organization. This object is available in API version 48.0 and later. In API version 49.0
and later, this object supports reports, criteria-based sharing rules, and history tracking, plus you can exclude individual fields from
custom page layouts.

Employee2
Represents an employee within a company or an organization. This object is available in API version 62.0 and later.

EmployeeCrisisAssessment
Represents a crisis assessment of an Employee. This object is available in API version 48.0 and later. In API version 49.0 and later, this
object supports reports, criteria-based sharing rules, and history tracking, plus you can exclude individual fields from custom page
layouts.

EmpUserProvisioningProcess
Represents an employee-user provisioning process. This object is available in API version 52.0 and later.

EmpUserProvisionProcessErr
Represents an employee-user provisioning process error. This object is available in API version 52.0 and later.

EnablementMeasureDefinition
Represents an Enablement measure, which specifies the job-related activity that a user performs to complete a milestone or outcome
in an Enablement program. A measure identifies a source object and optional related objects, with optional field filters and filter
logic, for tracking the activity. This object also represents Enablement measure information in Metadata API. This object is available
in API version 56.0 and later.

EnablementProgram
Represents an Enablement program, which includes exercises and measurable milestones to help users such as sales reps achieve
specific outcomes related to your company’s revenue goals. This object is available in API version 56.0 and later.

EnablementProgramDefinition
Represents Enablement program information in Metadata API. This object is available in API version 61.0 and later.

EnblMeasureObjectDefinition
Represents the criteria for an object that tracks the job-related activity for an Enablement measure in an Enablement program. A
separate EnblMeasureObjectDefinition is used for a measure's source object and each optional related object. This object is available
in API version 56.0 and later.

EnblPgmTaskMeasureProgress
Represents a user’s progress through the object and field requirements that an Enablement measure defines for an outcome or
milestone in an Enablement program. This object is available in API version 61.0 and later.


Standard Objects

EnblProgramSection
Represents an optional section in an Enablement program. A section can include other program items, such as milestones and
exercises. This object is available in API version 60.0 and later.

EnblProgramTaskDefinition
Represents an outcome, a milestone, or an exercise in an Enablement program. A program task is also known as a program item.
This object is available in API version 60.0 and later.

EnblProgramTaskMeasure
Represents the connection between an Enablement measure and a specific milestone or outcome in an Enablement program. This
object is available in API version 61.0 and later.

EnblProgramTaskProgress
Represents a user’s progress towards completing an outcome, a milestone, or an exercise in an Enablement program. This object is
available in API version 60.0 and later.

EnblProgramTaskSubCategory
Represents a custom exercise type that an Enablement admin adds to an Enablement program in Program Builder. A custom exercise
type also requires a corresponding EnblProgramTaskDefinition record for Program Builder and corresponding LearningItem and
LearningItemType records for when users take the exercise in the Guidance Center. This object is available in API version 62.0 and
later.

EngagementChannelType
Represents a channel through which a customer can be reached for communication. This object is available in API version 48.0 and
later.

EngagementSignal
Represents data about an individual’s engagement action, such as a web click, an email response, or a PDF download. This object
is available in API version 62.0 and later.

EngagementSignalCmpndMetric
Represents a rate metric that measures the ratio between two engagement signal metrics, such as product orders and product views
to calculate a conversion rate, or email clicks and email opens to determine a click-through rate. Use this object to create complex
measurements for A/B testing and web experimentation. This object is available in API version 62.0 and later.

EngagementSignalMetric
Represents a measurable quantity that’s derived from an engagement signal, such as the sum of revenue or a count of clicks. Use
this object to track user engagement for A/B tests, machine learning model training, and attribution configurations. This object is
available in API version 62.0 and later.

EnhancedLetterhead
Represents an enhanced letterhead that can be associated with a Lightning email template that doesn’t use the Salesforce Merge
Language (SML). This object is available in API version 46.0 and later.

Entitlement
Represents the customer support an account or contact is eligible to receive. This object is available in API version 18.0 and later.
Entitlements may be based on an asset, product, or service contract.

EntitlementContact
Represents a Contact eligible to receive customer support via an Entitlement. This object is available in API version 18.0 and later.

EntitlementTemplate
Represents predefined terms of customer support for a product (Product2). This object is available in API version 18.0 and later.


Standard Objects

EntityHistory
Represents historical information about an object’s changed field values. This object is only available to users with the “View All Data”
[permission. This object is unavailable beginning with API version 8.0. Use the object-specific Historyobjects instead.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.xml)

EntityMilestone
Represents a required step in a customer support process on a work order. The Salesforce user interface uses the term “object
milestone. This object is available in API version 37.0 and later.

EntitySubscription
Represents a subscription for a user following a record or another user. This object is available in API version 34.0 and later.

EnvironmentHubMember
Represents a member organization in the Environment Hub. This object is available in API version 29.0 and later.

Event
Represents an event in the calendar. In the user interface, event and task records are collectively referred to as activities.

EventLogFile
Represents event log files for event monitoring. The event monitoring product gathers information about your Salesforce org’s
operational events, which you can use to analyze usage trends and user behavior. This object is available in API version 32.0 and
later. The `Interval` and `Sequence` fields are available only in API version 37.0 and later.

EventRelation
Represents a person (a user, lead, or contact) or a resource (such as a conference room) invited to an event. This object lets you add
or remove invitees from an event and use the API to manage invitees’ responses to invitations. If Shared Activities is enabled,
EventRelation can also represent other objects that are related to an event. EventRelation does not support triggers, workflow, or
data validation rules.

EventBusSubscriber
Represents a trigger, process, or flow that’s subscribed to a platform event or a change data capture event. Doesn’t include CometD
or Pub/Sub API subscribers.

EventRelayConfig
Represents the configuration of an event relay, which relays platform events and change data capture events from Salesforce to
Amazon EventBridge. This object is available in API version 56.0 and later.

EventRelayFeedback
Represents execution state information about an event relay from Salesforce to Amazon EventBridge for platform events and change
data capture events. Query this object to get information such as the event relay status and any error message. This object is available
in API version 56.0 and later.

EventStagedInviteeEmail
Represents the relationship between an event and an email address invited to the event that doesn’t match to a user, contact, or
lead record. Data about the unmatched email address is represented in StagedInviteeEmail. This object represents event-related
details, such as the invitee's attendance response to the event. This object is available in API version 66.0 and later.

EventTag
Associates a word or short phrase with an Event.

EventWhoRelation
Represents the relationship between an event and a lead or contacts. This derived object is a filtered version of the EventRelation
on page 2454 object; that is, IsParent is _`true`_ and IsWhat is _`false`_ . It doesn’t represent relationships to invitees or to accounts,
opportunities, or other objects. This object is available in API versions 29.0 and later.


Standard Objects

Expense
Represents an expense linked to a work order. Service resource technicians can log expenses, such as tools or travel costs. This object
is available in API version 49.0 and later.

ExpenseReport
Represents a report that summarizes expenses. This object is available in API version 50.0 and later.

ExpenseReportEntry
Represents an entry in an expense report. This object is available in API version 50.0 and later.

ExpressionFilter
Represents a logical expression that’s used to control the execution of macro instructions. This object is available in API version 46.0
and later.

ExpressionFilterCriteria
Represents a condition in an expression that’s used to control the execution of macro instructions. This object is available in API
version 46.0 and later.

ExpressionSetConstraintObj
Represents the association between a Product object and the constraint model tags defined in a given constraint model. This object
is available in API version 63.0 and later.

ExtConvParticipantIntegDef
Represents the integration configuration for external conversation participants, used for communication between Salesforce and
external messaging platforms. This object is available in API version 66.0 and later.

ExtDataShare
Represents a data share, which is a collection of Data Cloud objects that can be shared with other Data Cloud orgs or third-party
partners. This object is available in API version 56.0 and later.

ExternalAccountHierarchy
Represents the external account hierarchy, which works like a role-based hierarchy. Use ExternalAccountHierarchy to allow partner
and customer users to share data with other external accounts in their hierarchy.This object is available in API version 49.0 and later.

ExternalAccountHierarchyHistory
Represents the history of changes to values in the fields of an external account hierarchy. This object is available in API version 50.0
and later.

ExternalClientApplication
For internal use only.

ExternalDataSource
Represents an external data source, which defines connection details for integration with data and content that are stored outside
the Salesforce org. This object is available in API version 27.0 and later.

ExternalDataUserAuth
Stores authentication settings for a Salesforce user to access an external system. The external system must be defined in an external
data source or a named credential that’s configured to use per-user authentication. This object is available in API version 27.0 and
later.

ExternalEncryptionRootKey
Represents metadata about root keys stored in third-party key stores that are used to generate and secure keys that encrypt Salesforce
data. This object is available in API version 58.0 and later.

ExternalEvent
Holds native iOS or Android calendar event details for the Salesforce Today feature in the Salesforce mobile app. This object is available
in API version 35.0 and later.


Standard Objects

ExternalEventMapping
Holds native iOS or Android calendar event details for the Salesforce Today feature in the Salesforce mobile app. This object is available
in API version 35.0 and later.

ExternalSocialAccount
Represents a managed social media account on a social network such as Facebook or Twitter. This object is available in API version
29.0 and later.

ExtKnowledgeConnector
Represents a connector to a third-party knowledge source for Unified Knowledge. This object is available in API version 60.0 and
later.

ExtlClntAppOauthPlcyCnfg
For internal use only.

ExtlClntAppOauthSettings
For internal use only.

ExtlClntAppPlcyCnfg
For internal use only.

ExtlIntrIdMapping
Represents a mapping between a Salesforce record and its corresponding record in an external system, such as Workday. This object
is available in API version 66.0 and later.

ExtlRecShrCnct
Represents authentication data to make outbound calls to and inbound calls from an external system to publish events for Partner
Connect. This object is available in API version 62.0 and later.

ExtlRecShrCnctAccnt
Represents an association between an account and an external record share connection for Partner Connect. This object is available
in API version 62.0 and later.

ExtlRecShrField
Represents an imported, exported, or updated external record share field for Partner Connect. This object is available in API version
63.0 and later.

ExtlRecShrFieldMap
Represents the external record share field mapping between the sender and receiver for Partner Connect. This object is available in
API version 62.0 and later.

ExtlRecShrLead
Represents the Lead record of a vendor org if you’re a partner. If you’re a vendor for Partner Connect, this object represents a partner
org. This object is available in API version 62.0 and later.

ExtlRecShrObject
Represents a shared object for Partner Connect. This object is available in API version 62.0 and later.

ExtlRecShrOpportunity
Represents the opportunity for Partner Connect in the vendor org if you’re a partner and the partner org if you’re the vendor. This
object is available in API version 62.0 and later.

ExtlRecShrPcklstOptn
Represents a picklist option of an external record share picklist field shared between a partner and vendor for Partner Connect. This
object is available in API version 62.0 and later.


Standard Objects

ExtlRecShrPicklistMap
Represents the external record share picklist field mapping between the partner and vendor system for Partner Connect. This object
is available in API version 62.0 and later.

ExtlRecShrRecordMap
Represents the lead or opportunity being mapped between a partner and vendor for Partner Connect. This object is available in API
version 62.0 and later.

FeedAttachment
Represents an attachment to a feed item, such as a file attachment or a link. Use FeedAttachment to add various attachments to
one feed item. This object is available in API version 36.0 and later.

FeedComment
Represents a comment added to a feed by a user. This object is available in API version 18.0 and later.

FeedItem
FeedItem represents an entry in the feed, such as changes in a record feed, including text posts, link posts, and content posts. This
object is available in API version 21.0 and later. This object replaces FeedPost.

FeedLike
Indicates that a user has liked a feed item. This object is available in API version 21.0 and later.

FeedPollChoice
Shows the choices for a poll posted in the feed. This object is available in API version 29.0 and later.

FeedPollVote
Shows how users voted on a poll posted in the feed. This object is available in API version 29.0 and later.

FeedPost
FeedPost represents the following types of changes in a record feed, such as AccountFeed: text posts, link posts, and content posts.
This object is available in API version 18.0 through 21.0. FeedPost is no longer available in later versions. Starting with API version
21.0, use FeedItem to represent text posts, link posts, and content posts in feeds.

FeedRevision
Holds the revision history of a specific feed item or comment, including a list of attributes that changed for each revision. This object
is available in API version 34.0 and later.

feedSignal
Attach feed signals, like `UpDownVote`, `UserVerified`, and `Verified`, to a feed post or comment. This object is available
in API version 41.0 and later.

FeedTrackedChange
Represents an individual field change or set of field changes. A FeedTrackedChange is a child object of a record feed, such as
AccountFeed. This object is available in API version 18.0 and later.

FieldHistoryArchive
Represents field history values for all objects that retain field history. `FieldHistoryArchive` is a big object, available only to
users with the “Retain Field History” permission. This object is available in API version 29.0 and later.

FieldChangeSnapshot
Use this virtual object to learn which opportunities' close dates changed during the specified time period. This object is available in
API version 52.0 and later.

FieldPermissions
Represents the enabled field permissions for the parent PermissionSet. This object is available in API version 24.0 and later.


Standard Objects

FieldSecurityClassification
Represents a field’s data sensitivity value selected from the SecurityClassification picklist. This object is available in API version 46.0
and later.

FieldServiceMobileSettings
Represents a configuration of settings that control the Field Service iOS and Android mobile app experience. This object is available
in API version 38.0 and later.

FieldServiceOrgSettings
Represents the org settings for Field Service, such as Appointment Assistant settings. If Field Service is enabled, the org contains one
read-only record of this object. This object is available in API version 51.0 and later.

FileSearchActivity
Represents search activity on a file. This object is available in API version 38.0 and later.

FiscalYearSettings
Settings to define a custom or standard fiscal year for your organization. This object has a parent-child relationship with the Period
object.

FldSvcObjChg
Represents a change made to one of a service appointment’s tracked fields. This object is available in API version 63.0 and later.

FldSvcObjChgDtl
Represents the details of a change made to one of a service appointment’s tracked fields. This object is available in API version 63.0
and later.

FlexQueueItem
Represents an asynchronous Apex job in the Apex flex queue. Provides information about the job type and flex queue position of
the AsyncApexJob. This object is available in API version 36.0 and later.

FlowDefinitionView
Represents the description of a flow definition. This object is available in API version 46.0 and later.

FlowInterview
Represents a flow interview. A _flow interview_ is a running instance of a flow. This object is available in API version 32.0 and later.

FlowInterviewLog
Represents the logs of a screen flow interview. An _interview_ is an instance of a running or previously run flow.This object is available
in API version 49.0 and later.

FlowInterviewLogEntry
Represents the log of a specific element that’s executed by a screen flow interview. An _interview_ is an instance of a running or
previously run flow. This object is available in API version 49.0 and later.

FlowInterviewLogOwnerSharingRule
Represents the rules for sharing a FlowInterviewLog with users other than the owner.This object is available in API version 49.0 and
later.

FlowInterviewOwnerSharingRule
Represents the rules for sharing a FlowInterview with users other than the owner. This object is available in API version 33.0 and
later.

FlowInterviewShare
Represents a sharing entry on a FlowInterview. This object is available in API version 33.0 and later.


Standard Objects

FlowNavMetricEventLog
Flow Navigation Metric event logs contain metric data for flow interviews such as total execution time, number of interviews, and
number of errors. This object is available in API version 61.0 and later.

FlowOrchestration
Represents the details of an orchestration definition. This object is available in API version 62.0 and later.

FlowOrchestrationInstance
Represents a run-time instance of an orchestration. This object is available in API version 53.0 and later.

FlowOrchestrationLog
Represents logging data for a FlowOrchestrationInstance. This object is available in API version 54.0 and later.

FlowOrchestrationStageInstance
Represents a run-time instance of a stage in a run-time instance of an orchestration. This read-only object is available in API version
53.0 and later.

FlowOrchestrationStepInstance
Represents a run-time instance of a step in a run-time instance of a stage of a run-time instance of an orchestration. This read-only
object is available in API version 53.0 and later.

FlowOrchestrationVersion
Represents the version of an orchestration. This object is available in API version 62.0 and later.

FlowOrchestrationWorkItem
Represents a work item associated with a run-time instance of an interactive step in a run-time instance of an orchestration. This
object is available in API version 54.0 and later.

FlowRecord
Represents the details of a flow. This object is available in API version 58.0 and later.

FlowRecordElement
Represents a single element within a flow version. This object is available in API version 58.0 and later.

FlowRecordElementOccurrence
Represents the execution metrics for a single element within a flow version. This object is available in API version 62.0 and later.

FlowRecordRelation
Represents a relationship between a record and a flow interview. When a flow interview is paused, Salesforce uses the
$Flow.CurrentRecord global variable in the flow to associate the interview with a record. Available in API version 42.0 and later.

FlowRecordVersion
Represents the version of a flow. This object is available in API version 58.0 and later.

FlowRecordVersionOccurrence
Represents an instance of a recurring flow that runs on a schedule. For example, a flow that runs weekly on Wednesdays creates an
occurrence each time it runs. This object is available in API version 60.0 and later.

FlowTestResult
Represents the results for a flow test associated with a flow version. This object is available in API version 55.0 and later.

FlowTestView
Represents the description of a flow test associated with a flow definition. This object is available in API version 55.0 and later.

FlowStageRelation
Represents a relationship between a paused flow interview and its stages. When a flow interview is paused, Salesforce creates a
FlowStageRelation record for each stage that’s set to the `$Flow.CurrentStage` or `$Flow.ActiveStages` global variable.
Available in API version 43.0 and later.


Standard Objects

FlowVariableView
Represents a variable within the flow version. This object is available in API version 46.0 and later.

FlowVersionView
Represents the version of a flow definition. This object is available in API version 46.0 and later.

Folder
Represents a repository for a Dashboard, Document, EmailTemplate, Macro, QuickText, or Report. Only one type of item can be
contained in a folder.

FolderedContentDocument
Represents the relationship between a parent and child ContentFolderItem in a ContentWorkspace.

ForecastingAdjustment
This object represents an individual forecast manager’s adjustment for a subordinate’s or child territory’s forecast via a ForecastingItem.
Available in API versions 26.0 and later. This object is different from the ForecastingOwnerAdjustment object, which represents
forecast users’ adjustments of their _own_ forecasts, including territory forecasts they own.

ForecastingColumnDefinition
Represents a custom calculated column or a custom reference data column in a forecast type. This object is available in API version
56.0 and later.

ForecastingColumnDefinitionLocalization
Represents the translated value of a custom calculated column or custom reference data column label when the Translation
Workbench is enabled for your organization. This object is available in API version 56.0 and later.

ForecastingCustomCategory
Represents a custom forecasting category used for forecast rollups. This object is available in API version 62.0 and later.

ForecastingCustomData
Represents forecast data from external sources to display in the forecasts page. For example, risk or last year’s revenue. This object
is available in API version 58.0 and later.

ForecastingDisplayedFamily
Represents the table in Forecasts Settings where an admin selects the product families that users can forecast on in Lightning
Experience. This object is available in API version 40.0 and later.

ForecastingFact
This object is read-only and links a ForecastingItem with its opportunities, such as opportunities that share the same owner or forecast
category and have a closing date within the period of the forecasting item. Available in API versions 26 and greater.

ForecastingFilter
Represents the custom filter for including or excluding data from opportunity forecasts. This object is available in API version 54.0
and later.

ForecastingFilterCondition
Represents the custom filter condition logic for including or excluding data from opportunity forecasts. This object is available in
API version 54.0 and later.

ForecastingGroup
Represents groups used to roll up forecast totals on the forecasts page. For example, group forecasts by industry or sales type. This
object is available in API version 60.0 and later.

ForecastingGroupItem
Represents the value within the picklist that is specified as the forecasting group for a forecast type. For example, if you have a
forecasting group that identifies the industry an opportunity is part of, this object represents the value in the the industry picklist
that’s chosen to be part of the group. This object is available in API version 60.0 and later.


Standard Objects

ForecastingItem
This object is read-only used for individual forecast amounts. Users see amounts based on their perspectives and forecast roles. The
amounts users see include one of these values when forecasting in revenue: `AmountWithoutAdjustments`,
`AmountWithoutManagerAdjustment`, `ForecastAmount`, `OwnerOnlyAmount` . The amounts users see include
one of these values when forecasting in quantity: `QuantityWithoutAdjustments`,
`QuantityWithoutManagerAdjustment`, `ForecastQuantity`, `OwnerOnlyQuantity` . Available in API version
26.0 and later.

ForecastingOwnerAdjustment
This object represents an individual forecast user’s adjustment of their _own_ forecast, including territory forecasts they own, via a
ForecastingItem. Available in API versions 33.0 and later. This object is different from the ForecastingAdjustment object, which
represents managers’ adjustments of _subordinates’_ and child territories’ forecasts.

ForecastingQuota
This object represents an individual user’s or territory’s quota for a specified time period. The Managed Quotas user permission is
required for creating, updating, or deleting quotas. (Users can only edit their subordinates’ or child territories’ quotas, not their own.)
The View All Forecasts permission is required to view any user's forecast, regardless of the forecast hierarchy. Available in API versions
25.0 and later. Forecast managers can view the forecasts of subordinates and territories below them in the forecast hierarchy.

ForecastingShare
Represents forecasts shared between a forecast manager and a user. Available in API version 44.0 and later.

ForecastingSourceDefinition
Represents the object, measure, date type, and hierarchy that a forecast uses to project sales. This object is available in API version
52.0 and later.

ForecastingSrcRecJudgment
Represents forecast managers’ judgment of whether they consider an opportunity-related deal to be certain to close. This object is
available in API version 59.0 and later.

ForecastingSubmission
Represents a submitted forecast. This object is available in API version 62.0 and later.

ForecastingSubmissionItem
Represents the values for each forecast category in a submitted forecast. This object is available in API version 62.0 and later.

ForecastingType
Used to identify the forecast type associated with `ForecastingAdjustment`, `ForecastingOwnerAdjustment`,
`ForecastingQuota`, `ForecastingFact`, and `ForecastingItem` objects. Available in API version 30.0 and greater.

ForecastingTypeSource
Maps a forecasting source definition to a forecast type. This object is available in API version 52.0 and later.

ForecastingUserPreference
Represents the forecasting selections that a user has made, such as display options, date range, forecasting type, and currency.

FormulaFunction
Represents a function used when building a formula, including examples and uses. This object is available in API version 47.0 and
later.

FormulaFunctionAllowedType
Represents the functions that are supported in the given formula context. This object is available in API version 48.0 and later.

FormulaFunctionCategory
Represents the category to which a formula belongs when building a formula. This object is available in API version 47.0 and later.


Standard Objects

FrcstCustmCatgRampRateSrc
Represents the total contract value used for custom bulk adjustments. This object is available in API version 63.0 and later.

FrcstCustmzAdjustment
Represents an individual forecast manager’s adjustment of a subordinate’s consumption forecast. Available in API version 63.0 and
later. This object is different from the ForecastingAdjustment object, which represents managers’ adjustments of subordinates’
pipeline forecasts.

FrcstCustmzOwnerAdjustment
Represents an individual forecast user’s adjustment of their own consumption forecast. Available in API version 63.0 and later. This
object is different from the ForecastingOwnerAdjustment object, which represents users’ adjustments of their pipeline forecasts.

FulfillmentOrder
Represents a group of products, fees, and delivery charges on a single order that share the same fulfillment location, delivery method,
and recipient. The FulfillmentOrderLineItems belonging to a FulfillmentOrder are associated with OrderItemSummary objects
belonging to a single OrderSummary. This object is available in API version 48.0 and later.

FulfillmentOrderItemAdjustment
Represents a price adjustment on a FulfillmentOrderLineItem. Corresponds to an OrderItemAdjustmentLineSummary associated
with the corresponding OrderItemSummary. This object is available in API version 48.0 and later.

FulfillmentOrderItemTax
Represents the tax on a FulfillmentOrderLineItem or FulfillmentOrderItemAdjustment. Corresponds to an
OrderItemTaxLineItemSummary. This object is available in API version 48.0 and later.

FulfillmentOrderLineItem
Represents a product or delivery charge belonging to a FulfillmentOrder. Corresponds to an OrderItemSummary. This object is
available in API version 48.0 and later.

FunctionConnection
Represents a connection between an org and Salesforce Functions. This object is available in API version 52.0 and later.

FunctionInvocationRequest
Represents invocation information for a Salesforce Function. This object is available in API version 51.0 and later.

FunctionReference
Represents a deployed Salesforce Function associated with an org. This object is available in API version 52.0 and later.

GenAIConversationSummary
Represents a generated summary of a voice or video call. This object is available in API version 60.0 and later.

GenAiFunctionDefinition
Represents an agent action. This object is available in API version 60.0 and later.

GenAiPlannerDefinition
Represents an agent planner service that uses a large language model (LLM) and a reasoning strategy to decompose a given task
into smaller subtasks, identify the most suitable actions for each subtask, and invoke them. This object is available in API version 60.0
and later.

GenAiPlannerFunctionDef
Represents a relationship between the agent planner service and agent actions. This object is available in API version 60.0 and later.

GenAiPluginDefinition
Represents an agent topic, which is a category of actions related to a particular job to be done by AI agents. This object is available
in API version 62.0 and later.


Standard Objects

GenOpPlanRequest
Represents a request to generate a service plan. This object is available in API version 67.0 and later.

GeoCountry
Represents a country. This object is available in API version 56.0 and later.

GeolocationBasedAction
Represents a geolocation-based action, which is an action that’s triggered when a user enters, exits, or is within the area of the
associated object. Available in API version 61.0 and later.

GeoState
Represents a state. This object is available in API version 57.0 and later.

GtwyProvPaymentMethodType
The gateway provider payment method type allows integrators and payment providers to choose an active payment to receive an
order's payment data rather than allowing the Salesforce Order Management platform to select a default payment method. This
object is available in API version 50.0 and later.

Goal
The Goal object represents the components of a goal such as its name, description, and status.

GoalLink
Represents the relationship between two goals. This is a many-to-many relationship, meaning that each goal can link to many other
goals.

GoogleDoc
Represents a link to a Google Document. This object is available in API version 14.0 and later.

Group
A set of User records.

GroupMember
Represents a User or Group that is a member of a public group.

GroupMembershipEventLog
Group Membership events capture details about changes to public group and queue membership, such as when members are
added to or removed from the public group or queue. This object is available in API version 64.0 and later.

GuestBuyerProfile
Represents a store's guest buyer profile, which allows unauthenticated buyers to browse the store. This object is available in API
version 51.0 and later.

HashtagDefinition
HashtagDefinition represents hashtag (#) topics in public Chatter posts and comments. Public posts and comments include those
on profiles and in public groups, but not those on records or in private groups. This object is available in API version 26.0 and later.

HealthCareDiagnosis
Represents information related to industry-standard healthcare diagnosis codes. Before the Spring ’21 release, the Healthcare
Procedure and Healthcare Diagnosis objects stored codes specifically related to procedures and diagnoses. These codes were used
for prior-authorization requests and approval processes. Since the Spring’21 release, Health Cloud uses the Code Set and Code Set
Bundle objects for this purpose instead.

HealthCareProcedure
Represents information related to industry-standard healthcare procedure codes. Before the Spring ’21 release, the Healthcare
Procedure and Healthcare Diagnosis objects stored codes specifically related to procedures and diagnoses. These codes were used
for prior-authorization requests and approval processes. Since the Spring’21 release, Health Cloud uses the Code Set and Code Set
Bundle objects for this purpose instead.


Standard Objects

Holiday
Represents a period of time during which your customer support team is unavailable. Business hours and escalation rules associated
with business hours are suspended during any holidays with which they are affiliated.

IconDefinition
Represents the icon-related metadata for a custom tab. This object is available in API version 43.0 and later.

Idea
Represents an idea on which users are allowed to comment and vote, for example, a suggestion for an enhancement to an existing
product or process. This object is available in API version 12 and later.

IdeaComment
Represents a comment that a user has submitted in response to an idea.

IdeaReputation
Represents a collection of statistics and scores derived from a user’s activity within an Ideas zone or internal organization. This object
is available in API version 28.0 and later.

IdeaReputationLevel
Represents a reputation level within an Ideas zone or internal organization and is used by the system to calculate reputation. You
can create up to 25 levels per zone or internal organization. This object is available in API version 28.0 and later.

IdeaTheme
Represents an invitation to zone members to submit ideas that are focused on a specific topic. This object is available in API version
26 and later.

IdpEventLog
Represents the Identity Provider Event Log. This log records both problems and successes with inbound SAML or OpenID Connect
authentication requests from another app provider. It also records outbound SAML responses when Salesforce is acting as an identity
provider. This object is available in API version 39.0 and later.

IframeWhiteListUrl
Represents a list of trusted external domains that you allow to frame your Embedded Service, Surveys, and Visualforce pages. This
object is available in API version 45.0 and later.

Image
Represents the details of an image. This object is available in API version 47.0 and later.

Incident
An Incident is any unplanned business interruption that has wide-sweeping impacts and requires an urgent fix. This object contains
the details of the incident, documenting the history of the incident from registration to closure. This object is available in API version
53.0 and later.

IncidentRelatedItem
Represents a junction object that relates an Incident to an Asset or Product. This object is available in API version 53.0 and later.

Individual
Represents a customer’s data privacy and protection preferences. Data privacy records based on the Individual object store your
customers’ preferences. Data privacy records are associated with related leads, contacts, person accounts, and users. This object is
available in API version 42.0 and later.

IndividualApplicationItem
Captures individual application input data that is used during run-time. This object is available in API version 58.0 and later.

IndividualHistory
Represents the history of changes to values in the fields of a data privacy record, based on the Individual object. This object is available
in versions 42.0 and later.


Standard Objects

IndividualShare
Represents a list of access levels to a data privacy record along with an explanation of the access level. For example, if you have
access to a record because you own it, the `IndividualAccessLevel` is `All` and `RowCause` is Owner. This object is
available in API version 42.0 and later.

InsufficientAccessEventLog
Insufficient Access event logs contain details about errors relating to insufficient account, case, contact, and opportunity record
access. This object is available in API version 61.0 and later.

InternalOrganizationUnit
Represents an organization that an Employee belongs to. This object is available in API version 48.0 and later. In API version 49.0 and
later, this object supports reports, criteria-based sharing rules, and history tracking, plus you can exclude individual fields from custom
page layouts.

InventoryItemReservation
Used to store inventory item reservation information for a specific product and location. This object is available in API version 60.0
and later.

InventoryReservation
Stores information about the status of cart inventory reservations in B2B and D2C Commerce. This object is available in API version
60.0 and later.

InvocableActionEventLog
Invocable Action events capture the calls to Salesforce Invocable Actions. This is particularly useful to monitor actions invoked during
Agentforce flows. This object is available in API version 64.0 and later.

Invoice
Represents a financial document describing the total amount a buyer must pay for goods or services provided. This object is available
in API version 48.0 and later.

InvoiceAddressGroup
Stores the buyer's address information. This object is available in API version 50.0 and later.

InvoiceBatchRun
Represents a batch processing job in Subscription Management or Billing (Revenue Cloud). During an invoice batch run, all billing
schedules that meet the specified criteria are processed, resulting in the generation of invoices. This object is available in API version
55.0 and later.

InvoiceBatchRunCriteria
Represents a batch processing job and its required criteria in Subscription Management. During an invoice batch run, all billing
schedules that meet the specified criteria are processed, resulting in the generation of invoices. This object is available in API version
55.0 and later.

InvoiceBatchRunRecovery
Provides information about an invoice batch run recovery procedure. This object is available in API version 57.0 and later.

InvoiceDocument
Tracks and displays the status of documents generated for invoices. Invoice documents are available in the related lists of invoice
entity records. This object is available in API version 61.0 and later.

InvoiceLine
Represents the amount that a buyer must pay for a product, service, or fee. Invoice lines are created based on the amount of an
order line. This object is available in API version 48.0 and later.

JobProfile
Represents a job profile used for shift scheduling. This object is available in API versions 47.0 and later.


Standard Objects

JobProfileQueueGroup
JobProfileQueueGroup defines the mapping between Queue and JobProfile and configurations for capacity plans in Workforce
Engagement. This object is available in API version 53.0 and later.

Knowledge__Feed
Represents the feed for a knowledge article. This object is available in API version 39.0 and later.

Knowledge__ka
Provides access to the concrete object that represents a Knowledge article, the parent object for article versions. This object is
available in API version 39.0 and later.

Knowledge__kav
Provides access to the concrete object that represents a Knowledge article version. This object is available in API version 39.0 and
later.

Knowledge__DataCategorySelection
Represents a data category that classifies an article. This object is available in API version 39.0 and later.

KnowledgeableUser
Represents a user identified as knowledgeable about a specific topic, and ranks them relative to other knowledgeable users. This
object is available in API version 31.0 and later.

KnowledgeArticle
Provides read-only access to an article and the ability to delete the primary article. This object is available in API version 19.0 and
later.

KnowledgeArticleEventLog
Knowledge Article View event logs contain user activity with your knowledge base. This object is available in API version 61.0 and
later.

KnowledgeArticleFeedback
Represents information about feedback from users on Knowledge articles and details about assignment of feedback to the article
owner or team to take action. This object is available in API version 64.0 and later.

KnowledgeArticleVersion
Provides a global view of standard article fields across all types of articles depending on their version. This object is available in API
version 18.0 and later.

KnowledgeArticleVersionHistory
Enables read-only access to the full history of an article. This object is available in API version 25.0 and later.

KnowledgeArticleViewStat
Provides certain statistics related to the number of views for the specified article across all article types. The view count statistics are
for published and archived articles only. View counts for draft articles aren’t tracked. This object is read-only and available in API
version 20.0 and later.

KnowledgeArticleVoteStat
Provides the weighted rating for the specified article on a scale of 1 to 5 across all article types. This object is read-only and available
in API version 20.0 and later.

LandingPage
Represents an Account Engagement landing page. A landing page is a web page that a visitor reaches after clicking a link or
advertisement. Landing pages can be created in Account Engagement and synced to Salesforce or created on the Landing Page
object in Account Engagement Lightning App. This object is available in API version 42.0 and later.

Lead
Represents a prospect or lead.


Standard Objects

LeadCleanInfo
Stores the metadata Data.com Clean uses to determine a lead record’s clean status. Helps you automate the cleaning or related
processing of lead records.

LeadDailyMetric
Represents the daily engagement metrics for a lead. This object is available in API version 52.0 and later.

LeadMonthlyMetric
Represents the monthly engagement metrics for a lead. This object is available in API version 52.0 and later.

LeadOwnerSharingRule
Represents the rules for sharing a lead with users other than the owner.

LeadShare
Represents a sharing entry on a Lead.

LeadStatus
Represents the status of a Lead record, such as Open, Qualified, or Converted.

LeadTag
Associates a word or short phrase with a Lead.

LearningContent
Represents a Trailhead or enablement site (myTrailhead) module assigned to a user in Workforce Engagement or Learning Paths.
This object also represents a Trailhead module or video in an Enablement program exercise. This object is available in API version
54.0 and later.

LearningItem
Represents an item that requires users to take action, including a Learning Paths entry, an Enablement program, or an exercise with
linked content in an Enablement program. For Learning Paths, users are assigned a learning item to complete. For Enablement
programs and exercises, users are assigned a program or can self-enroll in shared programs. This object is available in API version
58.0 and later.

LearningItemAssignment
Represents the assignment of a Learning Paths entry to users or groups or the enrollment of an Enablement program for a specific
user. This object is available in API version 58.0 and later.

LearningItemProgress
Represents the progress that a user has made towards completing an assigned learning item, such as a Learning Paths entry or
Enablement program. This object is available in API version 60.0 and later.

LearningItemSubmission
Represents a link to a resource, such as a video recording, that a user submits as part of a Feedback Request exercise in an Enablement
program. For peer and manager feedback, this resource can be a recording of a user’s sales patch. For Einstein Coach feedback, this
resource can be a video call, and Einstein generates feedback from the call’s transcription. This object is available in API version 59.0
and later, but Einstein Coach is available only in API version 61.0 and later.

LearningItemType
Represents a custom exercise type that an Enablement user takes in an Enablement program in the Guidance Center. A custom
exercise type also requires a corresponding LearningItem record for the Guidance Center and corresponding EnblProgramTaskDefinition
and EnblProgramTaskSubCategory records for when admins create a program in Program Builder. This object is available in API
version 62.0 and later.


Standard Objects

LearningPractice
Represents a Feedback Request exercise in an Enablement program. Users can submit a sample of their work and request feedback
from their peers and managers. Or, users can submit a video call and Einstein Coach generates feedback from the call’s transcription.
This object is available in API version 59.0 and later, but Einstein Coach feedback is available only in API version 61.0 and later.

LegalEntity
Represents the way an organization is structured. An organization can be a single legal entity or it can comprise more than one legal
entity. This object is available in API version 48.0 and later.

LicenseDefinitionCustomPermission (Developer Preview)
Represents a licensed custom permission that controls access to a license's features when included in a custom permission set license
definition. This object is available in API version 54.0 and later.

LightningErrorEventLog
Lightning Error events represent errors that occurred during user interactions with Lightning Experience and the Salesforce mobile
app. This object is available in API version 64.0 and later.

LightningExperienceTheme
Represents information for a theme in Lightning Experience. This object is available in API Version 42.0 and later.

LightningLoggerEventLog
Lightning Logger Event Log provides information from observed Lightning component logs. This object is available in API version
61.0 and later.

LightningOnboardingConfig
Represents the feedback provided when users switch from Lightning Experience to Salesforce Classic. Admins can customize the
question, how frequently the form appears, and where the feedback is stored in Chatter from the Adoption Assistance page in
Lightning Experience Setup. Available in API version 47.0 and later.

LightningPageViewEventLog
Lightning Page View event logs represent information about the page on which the event occurred in Lightning Experience and
the Salesforce mobile app. A Lightning Page View event log tracks the page a user visited, how long the user spent on the page,
and the load time for the page. This object is available in API version 61.0 and later.

LightningPrfmEventLog
Lightning Performance events track trends in Lightning Experience and Salesforce mobile app performance. This object is available
in API version 65.0 and later.

LightningToggleMetrics
Represents users who switched from Lightning Experience back to Salesforce Classic. This object is available in API version 43.0 and
later.

LightningUsageByAppTypeMetrics
Represents number of users on Lightning Experience and Salesforce Mobile. This object is available in API version 43.0 and later.

LightningUsageByBrowserMetrics
Represents Lightning Experience usage grouped by user’s browser. This object is available in API version 43.0 and later.

LightningUsageByPageMetrics
Represents standard pages users viewed most frequently in Lightning Experience. This object is available in API version 43.0 and
later.

LightningUsageByFlexiPageMetrics
Represents custom pages users viewed most frequently in Lightning Experience. This object is available in API version 43.0 and later.


Standard Objects

LightningExitByPageMetrics
Represents frequency metrics about the standard pages within which users switched from Lightning Experience to Salesforce Classic.
This object is available in API version 44.0 and later.

LinkedArticle
Represents a knowledge article that is attached to a work order, work order line item, or work type. This object is available in API
version 37.0 and later.

LinkedArticleFeed
Represents the comment feed on a linked article. This object is available in API version 39.0 and later.

LinkedArticleHistory
Represents the history of changes made to tracked fields on a linked article. This object is available in API version 37.0 and later.

ListEmail
Represents a list email sent from Salesforce, or sent from Account Engagement and synced to Salesforce. When the list email is sent,
the recipients are generated by combining recipients in ListEmailIndividualRecipients and ListEmailRecipientSource. Duplicate and
other invalid recipients are removed. The result is the recipients sent any given list email. ListEmail has a one-to-many relationship
with ListEmailRecipientSource and ListEmailIndividualRecipient. This object is available in API version 41.0 and later.

ListEmailIndividualRecipient
For a list email in Salesforce, represents a recipient. Each record represents a link from a list email to exactly one recipient for that list
email. Recipients can be contacts, leads, or campaign members. Has a one-to-many relationship with ListEmail. This object is available
in API version 44.0 and later.

ListEmailSentResult
Represents the results of a list email sent from Salesforce, or sent from Account Engagement and synced to Salesforce. It contains
transport headers and information specific to the associated send action. This object is available in API version 67.0 and later.

ListEmailMonthlyMetric
Represents the monthly engagement metrics for a single list email. This object is available in API version 49.0 and later.

ListEmailRecipientSource
For a list email in Salesforce, represents the dynamically defined sources of recipient email addresses. Each record represents a link
to a single list view or campaign that is examined when the list email is sent. Has a one-to-many relationship with ListEmail. This
object is available in API version 41.0 and later.

ListView
Represents a list view. A list view shows a set of records for an object, based on specific criteria. This object is available in API version
32.0 and later.

ListViewChart
Represents a graphical chart that’s displayed on Salesforce for Android, iOS, and mobile web list views. The chart aggregates data
that is filtered based on the list view that’s currently displayed. This object is available in API version 33.0 and later and is accessible
by portal users.

ListViewChartInstance
Retrieves metadata for all standard and custom charts for a given entity in context of a given list view. This object is available in API
versions 34.0 and later.

LiveAgentSession
This object is automatically created for each Chat session and stores information about the session. This object is available in API
versions 28.0 and later.


Standard Objects

LiveAgentSessionHistory
This object is automatically created for each Chat session and stores information about changes made to the session. This object is
available in API versions 28.0 and later.

LiveAgentSessionShare
This object is automatically created for each Chat session and stores information about the session. This object is available in API
versions 28.0 and later.

LiveChatBlockingRule
Represents a rule for blocking chat visitors’ IP addresses from starting new chats with agents. This object is available in API version
34.0 and later.

LiveChatObjectAccessConfig
Represents the action you can perform on a specified object by the Chat API. This object is available in API version 53.0 and later.

LiveChatObjectAccessDefinition
Represents the parent record for one or more LiveChatObjectAccessConfig objects. This object is available in API version 53.0 and
later.

LiveChatButton
Represents a button that allows visitors to request chats with Chat users. This object is available in API version 24.0 and later.

LiveChatButtonDeployment
Associates an automated chat invitation with a specific deployment. This object is available in API versions 28.0 and later.

LiveChatButtonSkill
Represents all the skills available to a LiveChatButton except the one currently assigned. To retrieve the skill currently assigned, query
LiveChatButton. This object is available in API version 25.0 and later.

LiveChatDeployment
Represents the general settings for deploying Live Agent on a website. This object is available in API version 24.0 and later.

LiveChatSensitiveDataRule
Represents a rule for masking or deleting data of a specified pattern. Written as a regular expression (regex). This object is available
in API version 35.0 and later.

LiveChatTranscript
This object is automatically created for each Live Agent chat session and stores information about the session. This object is available
in API version 24.0 and later.

LiveChatTranscriptEvent
Captures specific events that occur over the lifetime of a chat. This object is available in API version 24.0 and later.

LiveChatTranscriptShare
Represents a sharing entry on a LiveChatTranscript object. This object is available in API version 24.0 and later.

LiveChatTranscriptSkill
Represents a join between LiveChatTranscript and Skill. This object is available in API version 25.0 and later.

LiveChatUserConfig
Represents a setting that controls the console settings for Chat users. This object is available in API version 24.0 and later.

LiveChatUserConfigProfile
Represents a join between LiveChatUserConfig and Profile. This object is available in API version 24.0 and later.

LiveChatUserConfigUser
Represents a join between Live Chat User Config and User. This object is available in API version 24.0 and later.


Standard Objects

LiveChatVisitor
Represents a website visitor who has started or tried to start a chat session. This object is available in API version 24.0 and later.

Location
Represents a warehouse, service vehicle, work site, or other element of the region where your team performs field service work. In
API version 49.0 and later, you can associate activities with specific locations. Activities, such as the tasks and events related to a
location, appear in the activities timeline when you view the location detail page. Also in API version 49.0 and later, Work.com users
can view Employees as a related list on Location records. In API version 51.0 and later, this object is available for Omnichannel
Inventory and represents physical locations where inventory is available for fulfilling orders.

LocationGroup
Represents a group of Omnichannel Inventory locations, providing an aggregate view of inventory availability across those locations.
Omnichannel Inventory can create an inventory reservation for an order at the location group level, then assign the reservation to
one or more locations in the group as needed. This object is available in API version 51.0 and later.

LocationGroupAssignment
Represents the assignment of a location to a location group. This object is available in API version 51.0 and later.

LocationShippingCarrierMethod
The available shipping carrier services associated with a location or location group. Allows the assignment of different shipping
methods to a specific location and enables flexibility and customization in the shipping process. This object is available in API version
61.0 and later.

LocationTrustMeasure
Represents the COVID safety protocols that your business follows. For example, enforcement of masks, social distancing, cleanliness,
and capacity limits. This object is available in API version 50.0 and later.

LocWaitlistMsgTemplate
Represents a junction object connecting LocationWaitlist to MessagingTemplate. This object is available in API version 50.0 and later.

LocationWaitlist
Represents a queue created for a specific location. Multiple queues can be created for a single location. For example, you can have
a queue for each sales agent or a standard queue and a queue for vulnerable groups. The specific party of people in a queue is
represented by LocationWaitlistedParty. This object is available in API version 50.0 and later.

LocationWaitlistedParty
Represents a specific party of people waiting in a queue. This object is available in API version 50.0 and later.

LoginAsEventLog
LoginAsEventLog contains details about when a user logs in as another user in your org. This object is available in API version 61.0
and later.

LoginEvent
[The documentation has moved to LoginEvent in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/sforce_api_objects_loginevent.htm) _Platform Events Developer Guide_ .

LoginEventLog
Login event logs contain details about your Salesforce org's user login history. This object is available in API version 61.0 and later.

LoginGeo
Represents the geographic location of the user’s IP address for a login event. Due to the nature of geolocation technology, the
accuracy of geolocation fields (for example, country, city, postal code) may vary. This object is available in API version 34.0 and later.

LoginHistory
Represents the login history for all successful and failed login attempts for organizations and enabled portals. This object is available
in API version 21.0 and later.


Standard Objects

LoginIp
Represents a validated IP address. This object is available in version 28.0 and later.

LogoutEventLog
Contains details of user sessions ending or being revoked. This object is available in API version 65.0 and later.

LogoutEventStream
[The documentation has moved to LogoutEventStream in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/sforce_api_objects_logouteventstream.htm) _Platform Events Developer Guide_ .

LookedUpFromActivity
This read-only object is displayed as a related list on an activity record (an event or a task); the list contains records that have custom
lookup relationships from the activity to another object. This object is not queryable.

Macro
Represents a macro, which is a set of instructions that tells the system to perform one or more tasks. This object is available in API
version 32.0 and later.

MacroInstruction
Represents an instruction in a macro. An instruction can specify the object that the macro interacts with, the context or publisher
that the macro works within, the operation or action that the macro performs, and the target of the macro’s actions.

MacroUsage
Represents macro usage on a record, including which macro was used, who used it, and how they used it. This object is available
in API version 47.0 and later.

MailmergeTemplate
Represents a mail merge template (a Microsoft Word document) used for performing mail merges for your organization.

MaintenanceAsset
Represents an asset covered by a maintenance plan in field service. Assets can be associated with multiple maintenance plans.

MaintenancePlan
Represents a preventive maintenance schedule for one or more assets in field service.

MaintenanceWorkRule
Represents the recurrence pattern for a maintenance record. This object is available in API version 49.0 and later.

ManagedContent
Represents managed content in a Salesforce CMS workspace for use in an Experience Cloud site or a channel. The ManagedContent
object represents the complete instance of a managed content record. It provides a consistent identifier for the managed content
so that variants of the content item can be created over time. This object is available in API version 56.0 and later.

ManagedContentChannel
Represents the details of a CMS channel. CMS channels correspond to managed content publishing endpoints. They deliver published
content from your Salesforce CMS workspaces to an audience. This object is available in API version 55.0 and later.

ManagedContentInfo
Allows the creation of relationship to Product using ProductMedia. This object is available in API version 49.0 to 57.0. In API version
58.0 and later, use the ManagedContent object.

ManagedContentSpace
Represents the complete instance of a Salesforce CMS workspace that stores managed content. Users and groups with designated
permissions can access and manage the content in a CMS workspace. This object is available in API version 56.0 and later.

ManagedContentVariant
Represents a variant of a managed content item. This object is available in API version 56.0 and later.


Standard Objects

MarketingForm
Represents an Account Engagement marketing form that has been synched to Salesforce. Use forms on your website and landing
pages to collect information about visitors and turn anonymous visitors into identified prospects. This object is available in API version
42.0 and later.

MarketingLink
Represents an Account Engagement marketing link record, either a custom redirect or a file, that has been synced to Salesforce. This
object is available in API version 42.0 and later.

MatchingRule
Represents a matching rule that is used to identify duplicate records. This object is available in API version 33.0 and later.

MatchingRuleItem
Represents criteria used by a matching rule to identify duplicate records. This object is available in API version 33.0 and later.

MerchAccPaymentMethodSet
Defines an ordered list of payment methods that are available to a merchant's cudstomer during checkout. You can configure
multiple payment method sets, each designated for a specific locale, payment region, or sale channel. This object is available in API
version 58.0 and later.

MerchAccPaymentMethodType
Refers to a payment method that is in a payment method set, which is defined by the `MerchAccPaymentMethodSet` object.
This object is available in API version 58.0 and later.

MerchantAccount
A type of bank account that lets a merchant accept payments from a variety of payment methods, including credit or debit cards,
or digital wallets. A Salesforce Payments merchant account is linked to an underlying payment gateway to process payments This
object is available in API version 56.0 and later.

MerchantAccountEvent
Represents a merchant account platform event. Subscribe to these events so you can listen and respond to them when they’re
published. For example, create a Salesforce Flow that is triggered when one of these events is published. This object is available in
API version 59.0 and later.

MessagingChannel
Represents a communication channel that an end user can use to send a message to an agent. A communication channel can be
an SMS number, a Facebook page, or another supported messaging channel. This object is available in API version 40.0 and later.

MessagingChannelSkill
Junction object that represents an association between MessagingChannel and Skill. This object is available in API version 45.0 and
later.

MessagingChannelUsage
Represents the status of an enhanced Messaging channel or of an application in a Unified Messaging channel. This object is available
in API version 60.0 and later.

MessagingConfiguration
Represents the details for a Messaging configuration. This object is available in API version 47.0 and later.

MessagingDeliveryError
Represents a log of triggered outbound failures to verify when a triggered outbound has failed. This object is available in API version
44.0 and later.

MessagingEndUser
Represents a single address—such as a phone number or Facebook page—communicating with a single Messaging channel. This
object is available in API version 40.0 and later.


Standard Objects

MessagingLink
Represents the link between a Messaging Channel and where it's shared. This object is available in API version 47.0 and later.

MessagingSession
Represents a session on a Messaging channel. This object is available in API version 47.0 and later.

MessagingSessionMetrics
Represents a metric gathered about a specific enhanced messaging session, such as average agent response time. This object is
available starting in October 2024 in API version 62.0 and later.

MessagingTemplate
Represents a Messaging template used to send pre-formatted messages. This object is available in API version 47.0 and later.

MetadataApiOpEventLog
MetadataApiOpEventLog stores details of Metadata API retrieval and deployment requests. This object is available in API version
62.0 and later.

MetadataPackage
Represents a package that has been developed in the org you’re logged in to. Applies to unlocked, unmanaged, first-generation,
and second-generation managed packages.

MetadataPackageVersion
Represents a package version (managed or unmanaged) that has been uploaded from the org you’re logged in to.

Metric
The Metric object represents the components of a goal metric such as its name, metric type, and current value.

MetricDataLink
The link between the metric and the data source, such as a report.

MigratedEmail
For internal use only.

MilestoneType
Represents a milestone (required step in a customer support process). This object is available in API version 18.0 and later.

MktJourneyDcsnSetup
Represents a collection of Marketing Cloud Engagement journeys that you can interact with by using Salesforce Flow in Marketing
Cloud. This object is available in API version 65.0 and later.

MLField
Represents a single field in a data definition. This object is available in API version 50.0 and later.

MlIntentUtteranceSuggestion
Represents a customer input, used for training purposes in the feedback loop process of a conversation. Admins can add these inputs
to the intent training model. This object is available in API version 51.0 and later.

MLPredictionDefinition
Represents a prediction definition that specifies details about the prediction. This object is available in API version 50.0 and later.

MLModel
Represents an AI model that can be used in Einstein Prediction Builder, Einstein Recommendation Builder, and other Einstein features.
This object is available in API version 53.0 and later.

MLModelFactor
Represents a field value that has a positive or negative effect on the model’s score. This object is available in API version 53.0 and
later.


Standard Objects

MLModelFactorComponent
Represents information about the related MLModelFactor. For example, this object can represent a field value or a field range such
as “Title = CEO” or “Annual Revenue >10000000”. This object is available in API version 53.0 and later.

MLModelMetric
Represents a metric or statistic about the related model, such as accuracy, precision, or RSquared. Use a model’s metrics to learn
about its performance and to compare it with other models. This object is available in API version 53.0 and later.

MLRecommendationDefinition
For internal use only.

MobileDeviceAppRegistration
Represents the details provided in a mobile device registration event from an app that uses the Engagement Mobile SDK. This object
is available in API version 65.0 and later.

MobileSecurityAssignment
Represents the assignment of mobile security policies to a profile. The policies apply to the Salesforce mobile app with Enhanced
Mobile App Security enabled. This object is available in API version 54.0 and later.

MobileSecurityPolicy
Enables mobile security policies on the Salesforce mobile app with Enhanced Mobile Security. This object is available in API version
50.0 and later.

MobileSecurityUserMetric
Represents the metrics for users who have Enhanced Mobile Security policies enforced. This object is available in API version 51.0
and later.

MobileSettingsAssignment
Represents the assignment of a particular field service mobile settings configuration to a user profile. This object is available in API
version 41.0 and later.

MobSecurityCertPinConfig
Configuration of mobile security certificate pinning on the Salesforce mobile app with Enhanced Mobile Security. This object is
available in API version 53.0 and later.

MobSecurityCertPinEvent
The event of mobile security certificate pinning on the Salesforce mobile app with Enhanced Mobile Security. This object is available
in API version 53.0 and later.

MsgChannelLanguageKeyword
Represents the consent configuration for a Messaging channel. This object is available in API version 48.0 and later.

MsgChannelUsageExternalOrg
Represents the Enterprise ID (EID) and Business Unit (MID) for Marketing Cloud connections in a Unified Messaging channel. This
object is available in API version 60.0 and later.

MyDomainDiscoverableLogin
Represents configuration settings when the My Domain login page type is Discovery. Login Discovery provides an identity-first login
experience, where the login page contains the identifier field only. Based on the identifier entered, a handler determines how to
authenticate the user. This object is available in API version 45.0 and later.

MutingPermissionSet
Represents a set of disabled permissions and is used in conjunction with PermissionSetGroup. This object is available in API version
46.0 and later.

Name
Non-queryable object that provides information about foreign key traversals when the foreign key has more than one parent.


Standard Objects

NamedCredential
Represents a named credential, which specifies the URL of a callout endpoint and its required authentication parameters in one
definition. A named credential can be specified as an endpoint to simplify the setup of authenticated callouts. This object is available
in API version 33.0 and later.

NamedCredentialEventLog
The Named Credential event type captures information about Apex callouts that use named credentials as their endpoints. Use this
event type to audit the installed managed packages that use named credentials. If you don’t recognize the package namespace in
the named credential event log file, then you can investigate whether a security breach has occurred. This object is available in API
version 65.0 and later.

NamespaceRegistry
Represents a namespace that you can link to scratch orgs that were created from your org’s Dev Hub. You use the namespace when
developing, packaging, and releasing an app. You can’t create this object with the API. Use the **Link Namespace** action in the Dev
Hub graphical interface to insert a `NamespaceRegistry` record. This object is available in API version 41.0 and later.

NavigationLinkSet
Represents the navigation menu in an Experience Cloud site. A navigation menu consists of items that users can click to go to other
parts of the site. This object is available in API version 35.0 and later.

NavigationMenuItem
Represents a single menu item in a NavigationLinkSet. Use this object to create, delete, or update menu items in your Experience
Cloud site’s navigation menu. This object is available in API version 35.0 and later.

NavigationMenuItemLocalization
Represents the translated value of a navigation menu item in an Experience Cloud site. This object is available in API version 36.0
and later.

Network
Represents an Experience Cloud site. Salesforce Experience Cloud lets you create branded spaces for your employees, customers,
and partners. You can customize and create experiences, whether they’re communities, sites, or portals, to meet your business needs,
then transition seamlessly between them. Experience Cloud sites let you share information, records, and files with coworkers and
stakeholders all in one place. This object is available in API version 26.0 and later.

NetworkActivityAudit
Represents an audit trail of moderation actions in Experience Cloud sites. This object is available in API version 30.0 and later.

NetworkAffinity
Represents a junction object that associates a user profile with a Network object, that is, with an Experience Cloud site. Use
NetworkAffinity to assign a default Experience Cloud site to a user profile. This object is available in API version 41.0 and later.

NetworkAuthApiSettings
Represents the settings that control enablement, access, and security for the Headless Registration Flow, Headless Forgot Password
Flow, Headless Passwordless Login Flow, and their associated APIs. This object is available in API version 58.0 and later.

NetworkDataCategory
Represents data categories in Lightning Web Runtime (LWR) Experience Cloud Sites. This object is available in API version 59.0 and
later.

NetworkDiscoverableLogin
Represents the Login Discoverable page from where customers and partners log in to an Experience Cloud site. Customers and
partners are users with an External Identity license or any communities license for Experience Cloud. This object is available in API
version 44.0 and later.


Standard Objects

NetworkEmailTmplAllowlist
Represents an allowlist for the one-time password (OTP) email templates that are sent to end users during the Headless Registration
Flow, the Headless Passwordless Login Flow, and the Headless Forgot Password Flow. This object is available in API version 60.0 and
later.

NetworkFeedResponseMetric
Represents an object that stores the date and time values of question posts. It captures information for question creation, answer
creation, and when an answer is marked as best answer This object is available in API version 51.0 and later.

NetworkMember
Represents a member of an Experience Cloud site. Members can be either users in your company or external users with portal profiles.
This object is available in API version 26.0 and later.

NetworkMemberGroup
Represents a group of members in an Experience Cloud site. Members can be either users in your internal org or external users
assigned portal profiles. An administrator adds members to an Experience Cloud site by adding a profile or a permission set, and
any user with the profile or permission set becomes a member of the site. This object is available in API version 26.0 and later.

NetworkModeration
Represents a flag on an item in a community. This object is available in API version 30.0 and later.

NetworkPageOverride
Represents information about custom pages used to override the default pages in Experience Cloud sites. You can create Experience
Builder or Visualforce pages and override the default pages in a site. Using custom pages allows you to create a more personalized
experience for your users. This object is available in API version 34.0 and later.

NetworkSelfRegistration
Represents the account that self-registering Experience Cloud users are associated with by default. Self-registering users in an
Experience Cloud site are required to be associated with an account, which the admin must specify while setting up self-registration
for the site. If an account isn’t specified, Salesforce creates person accounts (when enabled) for self-registering users. This object is
available in API version 34.0 and later.

NetworkUserHistoryRecent
Represents an Experience Cloud site user’s history of accessed records. This object is available in API version 42.0 and later.

Note
Represents a note, which is text associated with a custom object or a standard object, such as a Contact, Contract, or Opportunity.

NoteAndAttachment
This read-only object contains all notes and attachments associated with an object.

NoteTag
Associates a word or short phrase with a Note.

OauthCustomScope
Represents a permission defining the protected data that a connected app can access from an external entity when Salesforce is
the OAuth authorization provider.

OauthCustomScopeApp
Represents the name of the connected app to which the custom scope is assigned. This object is available in API version 49.0 and
later.

OauthToken
Represents an OAuth access token for connected app authentication. Use this object to create a user interface for token management.
This object is available in API version 32.0 and later.


Standard Objects

OauthTokenExchangeHandler
Represents a token exchange handler. The token exchange handler also consists of an Apex class. During the OAuth 2.0 token
exchange flow, the token exchange handler is used to validate tokens from an external identity provider and to map users to
Salesforce. This object is available in API version 60.0 and later.

OauthTokenExchHandlerApp
Represents the enablement settings for a specific Salesforce connected app or external client app that’s enabled for the token
exchange handler. A handler can be enabled for multiple apps. This object is available in API version 60.0 and later.

ObjectDataImport
Represents the data import status of one or more object records. This object is available in API version 57.0 and later.

ObjectDataImportReference
Represents the relationships to the associated reference objects showing the source from which the data is imported. This object is
available in API version 57.0 and later.

ObjectMetadataTag
Represents a meta tag for a store page. Meta tags in HTML documents provide structured data used by search engines for ranking
and to show content in search results. This object is available in API version 60.0 and later.

ObjectPermissions
Represents the enabled object permissions for the parent PermissionSet. This object is available in API version 24.0 and later.

ObjectRelatedUrl
Represents a URL slug for a Product or Category page on a B2B Commerce or D2C Commerce LWR site, or a custom object, account,
or contact page on an enhanced LWR Experience Cloud site. This object is available in API version 57.0 and later.

ObjectTerritory2AssignmentRule
Represents a territory assignment rule that’s associated with an object, such as Account. ObjectTerritory2AssignmentRuleItem can
be created or deleted if the BooleanFilter field on its corresponding ObjectTerritory2AssignmentRule is `null` . Available if Sales
Territories has been enabled.

ObjectTerritory2AssignmentRuleItem
A single row of selection criteria for an ObjectTerritory2AssignmentRule object. ObjectTerritory2AssignmentRuleItem can only be
created or deleted if the `BooleanFilter` field on its corresponding ObjectTerritory2AssignmentRule object is a `null` value.
Available if Sales Territories has been enabled.

ObjectTerritory2Association
Represents an association (by assignment) between a territory and an object record such as an account or a lead.

ObjectUserTerritory2View
Represents a user and object, such as an account or lead, assigned to a territory. This object is available in API version 58.0 and later.

OmniSupervisorConfig
Represents the Command Center for Service configuration for an assigned group of supervisors. This object is available in API version
41.0 and later.

OmniSupervisorConfigAction
Represents the actions available to the supervisors of a Command Center for Service configuration. This object is available in API
version 56.0 and later.

OmniSupervisorConfigGroup
Represents the group of reps who are visible to the supervisors of a Command Center for Service configuration. The group, if visible,
appears in the Agents tab of Command Center for Service. This object is available in API version 41.0 and later.


Standard Objects

OmniSupervisorConfigProfile
Represents the supervisor profiles to which a Command Center for Service configuration applies. User-level configurations override
profile-level configurations. This object is available in API version 41.0 and later.

OmniSupervisorConfigQueue
Represents the queues that are visible to the supervisors of a Command Center for Service configuration. The queue, if visible, appears
in the Queues Backlog and Assigned Work tabs of Command Center for Service. This object is available in API version 53.0 and later.

OmniSupervisorConfigSkill
Represents the skills that are visible to the supervisors of a Command Center for Service configuration. These skills, if visible, appear
in the Skills Backlog tab of Command Center for Service. This object is available in API version 53.0 and later.

OmniSupervisorConfigTab
Represents the visible tabs specified in a Command Center for Service configuration. This object is available in API version 60.0 and
later.

OmniSupervisorConfigUser
Represents the users to whom a Command Center for Service configuration applies. User-level configurations override profile-level
configurations. This object is available in API version 41.0 and later.

OpenActivity
This read-only object is displayed in a related list of open activities—future events and open tasks—related to an object. It includes
activities for all contacts related to the object. OpenActivity fields for phone calls are only available if your organization uses Salesforce
CRM Call Center.

OperatingHours
Represents the hours in which a service territory, service resource, or account is available for work. OperatingHours is used by Field
Service, Salesforce Scheduler, Salesforce Meetings, Sales Engagement, and Workforce Engagement. This object is available in API
version 38.0 and later.

OperatingHoursHistory
Represents the history of changes made to tracked fields on an operating hours record. This object is available in API version 38.0
and later.

OperatingHoursHoliday
Represents the day or hours for which a service territory and service resources exclusive to the service territory are unavailable in
Salesforce Scheduler. This object is available in API version 54.0 and later.

Opportunity
Represents an opportunity, which is a sale or pending deal.

OpportunityCompetitor
Represents a competitor on an Opportunity.

OpportunityContactRole
Represents the role that a Contact plays on an Opportunity.

OpportunityContactRoleSuggestionInsight
Represents a suggestion for a new opportunity contact role. Available in API versions 45.0 and later.

OpportunityFieldHistory
Represents the history of changes to the values in the fields of an opportunity. This object is available in versions 13.0 and later.

OpportunityHistory
Represents the stage history of an opportunity.


Standard Objects

OpportunityInsight
Represents an individual insight (deal prediction, follow-up reminder, or key moment) related to an opportunity record.

OpportunityLineItem
Represents an opportunity line item, which is a member of the list of Product2 products associated with an Opportunity.

OpportunityLineItemSchedule
Represents information about the quantity, revenue distribution, and delivery dates for a particular `OpportunityLineItem` .

OpportunityLineItemSplit
Represents information about an opportunity product split, including percentages, amounts, and owner. This object is available in
API version 58.0 and later.

OpportunityOwnerSharingRule
Represents a rule for sharing an opportunity with users other than the owner.

OpportunityPartner
This object represents a partner relationship between an Account and an Opportunity. An OpportunityPartner record is created
automatically when a Partner record is created for a partner relationship between an account and an opportunity.

OpportunityRelatedDeleteLog
Represents an audit log of the deletion of opportunity-related child records, such as opportunity team members, product splits, or
opportunity splits. This object is available in API version 59.0 and later.

OpportunityShare
Represents a sharing entry on an Opportunity.

OpportunitySplit
OpportunitySplit credits one or more opportunity team members with a portion of the opportunity amount. This object is available
in API version 16.0 and later for pilot customers, and version 28.0 and later for others.

OpportunitySplitType
OpportunitySplitType provides unique labels and behavior for each split type. This object is available in API version 28.0 and later.

OpportunityStage
Represents the stage of an Opportunity in the sales pipeline, such as New Lead, Negotiating, Pending, Closed, and so on.

OpportunityTag
Associates a word or short phrase with an Opportunity.

OpportunityTeamMember
Represents a User on the opportunity team of an Opportunity.

OpptyLineItemSplitType
Represents an opportunity product split type. This object is available in API version 58.0 and later.

Order
Represents an order associated with a contract or an account.

OrderAction
Indicates the type of order, such as a new sale or a cancellation. This object is available in API version 55.0 and later.

OrderAdjustmentGroup
Group containing a set of adjustments applied to an order. This object is available in API version 48.0 and later.


Standard Objects

OrderAdjustmentGroupSummary
Represents the current properties and state of a group of related price adjustments. Associated with a set of
OrderItemAdjustmentLineSummaries that apply to OrderItemSummaries belonging to one OrderSummary. Corresponds to one or
more order adjustment group objects, consisting of an original object and any change objects applicable to it. This object is available
in API version 48.0 and later.

OrderChangeLog
Represents a log record of all change requests made to an order post activation. A log record is always one-to-one to change an
order request. This object is available in API version 48.0 and later.

OrderChgReasonCategMap
The mapping between an order change reason and a service flow category. This object is available in API version 65.0 and later.

OrderDeliveryGroup
A group of order items that share a delivery method and address. The delivery method and address are used during the fulfillment
process, such as shipping as a gift, downloading, picking up in store, or shipping to a standard address This object is available in API
version 48.0 and later.

OrderDeliveryGroupSummary
Represents the current properties and state of a group of OrderItemSummaries, belonging to one OrderSummary, to be fulfilled
using the same delivery method and delivered to the same address. A single shipment can include them all, but that isn’t guaranteed.
Corresponds to one or more order delivery group objects, consisting of an original object and any change objects applicable to it.
This object is available in API version 48.0 and later.

OrderDeliveryMethod
Shows the customizations and options that a buyer selected for their delivery method. This object is available in API version 48.0
and later.

OrderHistory
Represents historical information about changes that have been made to the standard fields of the associated order, or to any custom
fields with history tracking enabled.

OrderItem
Represents an order product that your organization sells.

OrderItemAdjustmentLineItem
An adjustment that has been made to an order item. This object is available in API version 48.0 and later.

OrderItemAdjustmentLineSummary
Represents the current properties and state of price adjustments on an OrderItemSummary. Corresponds to one or more order item
adjustment line item objects, consisting of an original object and any change objects applicable to it. This object is available in API
version 48.0 and later.

OrderItemGroup
Stores the group information for line items in an order. It also stores the aggregated line field information (subtotal). It contains a
parent-child relationship to order. This object is available in API version 62.0 and later.

OrderItemRecipient
Represents a site, employee, or other entity for which services are being ordered. This includes essential details such as the recipient's
name, contact information, and the specific site or location where the services will be provided. This object is available in API version
62.0 and later.

OrderItemRelationship
Describes a relationship between order products. This object is available in API version 58.0 and later.


Standard Objects

OrderItemSummary
Represents the current properties and state of a product or charge on an OrderSummary. Corresponds to one or more order item
objects, consisting of an original object and any change objects applicable to it. This object is available in API version 48.0 and later.

OrderItemSummaryChange
Represents a change to an OrderItemSummary, usually a reduction in quantity due to a cancel or return. Corresponds to a change
order item. This object is available in API version 48.0 and later.

OrderItemSummaryRelationship
Junction object used to track how an original order summary (created before any exchanges have occurred) relates to other order
summary objects in a chain of exchange orders. This object is available in API version 60.0 and later. An exchange order is an
OrderSummary object whose SourceProcess property is set to Exchange. An original order summary can have an exchange order,
which in turn can have yet another exchange order, and so on. The OrderSummaryRelationship object maintains this relationship
between OrderSummary objects.

OrderItemTaxLineItem
The tax amount that has been applied to an order item. This object is available in API version 48.0 and later.

OrderItemTaxLineItemSummary
Represents the current tax on an OrderItemSummary or OrderItemAdjustmentLineSummary. Corresponds to one or more order
item tax line items, consisting of an original object and any change objects applicable to it. This object is available in API version 48.0
and later.

OrderItemType
Shows whether the order product is a product line or charge line. This object is available in API version 48.0 and later.

OrderOwnerSharingRule
Represents a rule which determines order sharing access for the order’s owners.

OrderPaymentSummary
Represents the current properties and state of payments using a single payment method that are applied to one OrderSummary.
This object is available in API version 48.0 and later.

OrderPaymentSummaryReference
OrderPaymentSummaryReference is a junction object that allows an order payment summary to be shared with another order
summary. This object is available in API version 60.0 and later.

OrderShare
Represents a sharing entry on an Order. This object is available in API version 48.0 and later.

OrderStatus
Represents the status of the order entity. This object is available in API version 48.0 and later.

OrderSummary
Represents the current properties and state of an order. Corresponds to one or more order objects, consisting of an original object
and any change objects applicable to it. This object is available in API version 48.0 and later.

OrderSummaryAdditionalInfo
Stores information related to OrderSummary including context around the order, such as inventory reservation details, order
origination, and other values that Einstein uses to perform order analysis. Only reservation details can be stored in this object. This
object is available in API version 58.0 and later.

OrderSummaryRelationship
Junction object used to track how an original order summary (created before any exchanges have occurred) relates to other order
summary objects in a chain of exchange orders. This object is available in API version 60.0 and later.


Standard Objects

OrderSummaryRoutingSchedule
Represents an attempt to route an order summary to one or more inventory locations for fulfillment. You can use it to schedule
future attempts and to record completed attempts. This object is available in API version 51.0 and later.

Organization
Represents key configuration information for an organization.

OrgDeleteRequest
Represents a request to delete a developer edition (DE) org. This object is available in API version 42.0 and later. It is available only
in Developer and Database.com editions.

OrgEmailAddressSecurity
Defines the assignment of a user profile to an org-wide email address. This object is available in API version 58.0 and later.

OrgMetric
Represents a feature or metric that Salesforce Optimizer evaluates. This object is available in API version 47.0 and later.

OrgMetricScanResult
Represents data or an item associated with a feature’s results in a Salesforce Optimizer evaluation. For example, for the Custom Field
Limit feature, an OrgMetricScanResult object represents an object flagged for approaching the custom field limit. This object is
available in API version 47.0 and later.

OrgMetricScanSummary
Represents the results summary for a specific feature in a Salesforce Optimizer evaluation. This object is available in API version 47.0
and later.

OrgSnapshot
Represents a snapshot of a scratch org. Snapshots capture the state of a scratch org so that you can use it to quickly spin up new
scratch orgs using its configuration. This object is available in API version 61.0 and later.

OrgWideEmailAddress
Represents an organization-wide email address for user profiles.

OSAsyncChgCompletedEvent
An event that allows the processing of the credit memo, invoices, and other entities after a bulk action has successfully completed.
The event provides all of the values that would exist on the synchronous APIs. This object is available in API version 63.0 and later.

OutOfOffice
Represents a user-set value on a profile that shows when the user intends to be out of the office. This object is available in API version
41.0 and later.

OutgoingEmail
For internal use only.

OutgoingEmailRelation
For internal use only.

OwnedContentDocument
Represents a file owned by a user. This object is available in version 30.0 and later.

OwnerChangeOptionInfo
Represents default and optional actions that can be performed when a record’s owner is changed. Available in API version 35.0 and
later, but to query for change owner metadata, use the OwnerChangeOptionInfo object in Tooling API instead. For more information,
[see OwnerChangeOptionInfo in the Tooling API.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_tooling.meta/api_tooling/tooling_api_objects_ownerchangeoptioninfo.htm)


Standard Objects

PackageInstallEventLog
PackageInstallEventLog stores details about package installation in the organization. This object is available in API version 62.0 and
later.

PackageLicense
Represents a license for an installed managed package. This object is available in API version 31.0 and later.

PackagePushError
Represents an error encountered during a push request. The number of PackagePushError records created depends on the number
of push jobs in the request that result in an error.

PackagePushJob
Represents an individual push job for upgrading a package in an org from one version to another version. There can be multiple
push jobs created for one push request. For example, if you want to upgrade five orgs as part of one push, you have one
PackagePushRequest record and five PackagePushJob records.

PackagePushRequest
Represents the push request for upgrading a package in one or many orgs from one version to another version.

PackageSubscriber
Represents an installation of a package in an org. This object contains installation information for managed or unlocked packages
developed in the org you’re logged in to.

Participant
Represents a participant in a ConversationParticipant. An existing or new Participant is referenced each time a new
ConversationParticipant is created. This object is available in API version 57.0 and later.

Partner
Represents a partner relationship between two Account records or between an Opportunity record and an Account record.

PartnerFundAllocation
Represents allocated funds from a partner marketing budget for channel partners. This object is available in API version 41.0 and
later.

PartnerFundClaim
Represents a claim of funds from the partner marketing budget by a channel partner. This object is available in API version 41.0 and
later.

PartnerFundRequest
Represents a request for funds from the partner marketing budget by a channel partner. This object is available in API version 41.0
and later.

PartnerMarketingBudget
Represents a budget that provides funds to channel partners for selling and marketing products and services. This object is available
in API version 41.0 and later.

PartnerNetworkConnection
Represents a Salesforce to Salesforce connection between Salesforce organizations.

PartnerNetworkRecordConnection
Represents a record shared between Salesforce organizations using Salesforce to Salesforce.

PartnerNetworkSyncLog
Represents the Org Sync Log tab in Salesforce, where Salesforce administrators can track the replication of record inserts and updates
being performed in Organization Sync. The Connection Detail page for the replication connection also displays the Org Sync Log’s
twenty most recent entries, and provides a link to the log.


Standard Objects

PartnerRole
Represents a role for an account Partner, such as consultant, supplier, and so on.

PartyConsent
Represents consent preferences for an individual. This object is available in API version 48.0 and later.

Payment
Represents a single event when a shopper makes a payment. For credit cards, this event is a payment capture or payment sale, but
it doesn't appear on the shopper's credit card statement. This object is available in API version 48.0 and later.

PaymentAuthAdjustment
Shows information about an adjustment made to an authorized transaction. This object is available in API version 51.0 and later.

PaymentAuthorization
Represents a single payment authorization event where users can capture or reverse a payment against a reserve of funds. This
object is available in API version 48.0 and later.

PaymentCredit
Tracks the amount of money returned to the customer. The return can be a store credit, a gift card, or another type of credit. It's
linked to the original payment record and includes the total credit amount issued. This object is available in API version 65.0 and
later.

PaymentCreditLinePayment
A payment credit line payment. This object is available in API version 65.0 and later.

PaymentCreditTransaction
A payment credit transaction. This object is available in API version 65.0 and later.

PaymentGateway
Platform object that represents the connection to an external payment gateway. This object is available in API version 48.0 and later.

PaymentGatewayLog
Stores information exchanged between the Salesforce payments platform and external payment gateways. Gateway logs can also
record payloads from external payment entities. This object is available in API version 48.0 and later.

PaymentGatewayProvider
Setup entity for payment gateways. Defines the connection to a payment gateway Apex adapter. This object is available in API
version 48.0 and later.

PaymentGroup
Top-level object that groups all payment transactions that are processed for an order or invoice. PaymentGroup is a standalone
object, so it isn’t required for users to execute payment transactions (authorizations, captures, refunds, and sales). This object is
available in API version 48.0 and later.

PaymentInitiationSource
Represents the originating source of a payment. This information helps other Salesforce products integrate with Salesforce Payments.
This object is available in API version 63.0 and later.

PaymentIntent
Represents data temporarily stored during a transaction’s lifecycle that can identify the buyer, the merchant, and the amount the
buyer is sending to the merchant. Data such as timestamp and amount returned can also be stored in PaymentIntent. This object
is available in API version 58.0 and later.

PaymentIntentEvent
Represents a payment intent platform event. Subscribe to these events so you can listen and respond to them when they’re published.
For example, create a Salesforce Flow that is triggered when one of these events is published. This object is available in API version
59.0 and later.


Standard Objects

PaymentLineInvoice
Represents a payment allocated to or unallocated from an invoice. This object is available in API version 48.0 and later.

PaymentLink
A link that a merchant can share with customers to collect payments for products and services. The payment link, which you can
embed into a Salesforce app or send directly to a customer, directs the customer to a Pay Now payment page. The page can show
a total amount owed or an itemized list or products, shipping and tax charges, and a total amount owed. The customer enters their
contact and payment details, and submits their payment. The amounts are shown in the store's currency. This object is available in
API version 58.0 and later.

PaymentLinkEvent
Represents a payment link platform event. Subscribe to these events so you can listen and respond to them when they’re published.
For example, create a Salesforce Flow that is triggered when one of these events is published. This object is available in API version
59.0 and later.

PaymentMethod
Represents the method that a buyer uses to compensate the seller of a good or service. Common payment methods include cash,
checks, credit or debit cards, money orders, bank transfers, and online payment services. This object is available in API version 48.0
and later.

PymtSchdDistributionMethod
Indicates how the total payment is divided into partial payments. This object is available in API version 56.0 and later.

PaymentScheduleTreatmentDtl
Contains configuration information for the payment schedule treatment detail. This object is available in API version 56.0 and later.

PaymentTerm
Defines your company's method and expectations for receiving payment. This object is available in API version 55.0 and later.

PaymentTermItem
Defines the attributes of a payment term that your company uses. The PaymentTermItem is used to determine the due date on
invoices. This object is available in API version 55.0 and later.

PaymentSchedule
The payment schedule represents a collection of payments that a customer wants to collect at different times for a certain record.
A schedule contains one or more payment schedule items, where each item represents one payment to be processed. Each of a
schedule’s items can have different payment configuration fields, such as payment methods, payment dates, and payment accounts.
When a payment scheduler launches a payment run, the run evaluates active payment schedule items, and picks them up for
payment processing if they align with the scheduler’s payment criteria. This object is available in API version 55.0 and later.

PaymentScheduleItem
A payment schedule contains one or more payment schedule items, where each item represents one payment to be processed.
Each of a schedule’s items can have different payment configuration fields, such as payment methods, payment dates, and payment
accounts. When a payment scheduler launches a payment run, the run evaluates active payment schedule items, and picks them
up for payment processing if they align with the scheduler’s payment criteria. This object is available in API version 55.0 and later.

PaymentSchedulePolicy
Contains configuration information for the payment schedule policy. This object is available in API version 56.0 and later.

PaymentScheduleTreatment
Contains configuration information for the payment schedule. This object is available in API version 56.0 and later.

PendingOrderSummary
Object representing a B2C Commerce order ingested via High Scale Orders before an OrderSummary is created for it. Optimized for
online transaction processing (OLTP). This object is available in API version 55.0 and later.


Standard Objects

PendingServiceRouting
Represents the routing details of a work item that’s waiting to be routed or assigned. This object is available in API version 40.0 and
later.

PendingServiceRoutingInteractionInfo
Represents PendingServiceRouting interaction information that’s used when work is routed to an agent. For a screen pop, it specifies
which records to open when work is routed to an agent from a specific channel. PendingServiceRoutingInteractionInfo is read-only.
This object is available in API version 53.0 and later.

Period
Represents a fiscal period defined in FiscalYearSettings.

PermissionSet
Represents a set of permissions that’s used to grant more access to one or more users without changing their profile or reassigning
profiles. This object is available in API version 22.0 and later.

PermissionSetAssignment
Represents a user’s assignment to a permission set or permission set group. This object is available in API version 22.0 and later.

PermissionSetGroup
Represents a group of permission sets and the permissions within them. Use permission set groups to organize permissions based
on job functions or tasks. Then, you can package the groups as needed. This object is available in API version 45.0 and later.

PermissionSetGroupComponent
A junction object that relates the PermissionSetGroup and PermissionSet objects via their respective IDs; enables permission set
group recalculation to determine the aggregated permissions for the group. This object is available in API version 45.0 and later.

PermissionSetLicense
Represents a license that’s used to enable one or more users to receive a specified permission without changing their profile or
reassigning profiles. You can use permission set licenses to grant access, but not to deny access. This object is available in API version
29.0 and later.

PermissionSetLicenseAssign
Represents the association between a User and a PermissionSetLicense. This object is available in API version 29.0 and later.

PermissionSetLicenseDefinition (Developer Preview)
Represents the definition of a custom permission set license, which entitles specified features in a package. This object is available
in API version 54.0 and later.

PermissionSetTabSetting
Represents a permission set tab setting. Requires the View Setup permission. Use this object to query all tab settings of the permission
set. This object is available in API version 45.0 and later.

PersnlBatchDecision
Represents a batch personalization that delivers personalization decisions (content or recommendations) to a customer segment.
Available in API version 64.0 and later.

PersonAccountOwnerPowerUser
Represents a user who can own more than 50,000 customer or partner portal accounts. Person account owner power users can own
a large number of either customer or partner users. Their role can’t be changed and they must be at the root of the role hierarchy.
Person account owner power user objects can't be created if deferred sharing is turned on for your org. Person account owner power
user objects can be created while deferred sharing is turned off for an org. Deferred sharing can be turned back on after person
account owner power user objects have been created. This object is available in API version 57.0 and later.

PersonalOrgInfo
Represents the information for a Tableau Next personal org. This object is available in API version 64.0 and later.


Standard Objects

PersonalizationDecision
Represents a set of targeting rules within a personalization point that determine an individual's eligibility to receive personalized
content and the content to deliver. Available in API version 62.0 and later.

PersonalizationObjective
Represents a specific business outcome that you want to achieve when creating a recommender. Available in API version 62.0 and
later.

PersonalizationPoint
Represents a specific touch point in an experience where a personalization decision can be made. It connects a data space, profile
data graph, personalization type, and response template to deliver personalized content at that time in a customer journey. Available
in API version 62.0 and later.

PersonalizationSchema
Represents a personalization response template that’s used when you build a personalization decision. Available in API version 62.0
and later.

PersonalizationTargetInfo
Represents a target for an audience. This object is available in API version 47.0 and later.

PermissionUpdateEventLog
Permission update events represent changes to object, field, and user permissions and setup entity access that occur in profiles and
permission sets. The event type also tracks if you clone profiles or change whether session activation is required in permission sets
or permission set groups. This object is available in API version 65.0 and later.

PersonTraining
Represents an assignment of a learning module in Workforce Engagement. This object is available in API version 54.0 and later.

PicklistValueInfo
Represents the active picklist values for a given picklist field. This object is available in API version 40.0 and later.

PickTicket
A PickTicket represents quantities of one or more products to be picked for fulfillment at a location. It can include products belonging
to one or more fulfillment orders. This object is available in API version 57.0 and later.

PickTicketAssignment
Represents the association of a FulfillmentOrder with a PickTicket. A PickTicket has one PickTicketAssignment for each FulfillmentOrder
containing products to be picked as part of that PickTicket. This object is available in API version 57.0 and later.

PickTicketProduct
Represents a quantity of a product to be picked as part of a PickTicket. It can include quantities for multiple FulfillmentOrders. This
object is available in API version 57.0 and later.

PipelineInspectionListView
Represents a pipeline view, an intelligence view, or a saved filter. A pipeline view shows a set of opportunity records, based on specific
criteria. An intelligence view shows a set of account, lead, or contact records, based on specific criteria. This object is available in API
version 53.0 and later.

PipelineInspectionSumField
Use this object to learn which field from the opportunity object is used to aggregate Pipeline Inspection metrics on a pipeline view.
This object is available in API version 56.0 and later.

PipelineInspMetricConfig
Represents the configuration of a forecast category metric that appears in the Pipeline Inspection view. This object is available in
API version 55.0 and later.


Standard Objects

PipelineInspMetricConfigLocalization
Represents the translated label of a Pipeline Inspection metric. This object is available in API version 55.0 and later.

PlatformAction
PlatformAction is a virtual read-only object. It enables you to query for actions displayed in the UI, given a user, a context, device
format, and a record ID. Examples include standard and custom buttons, quick actions, and productivity actions.

PlatformEventUsageMetric
Contains usage data for event publishing and delivery to CometD and Pub/Sub API clients, `empApi` Lightning components, and
event relays. If Enhanced Usage Metrics isn't enabled, usage data is available for the last 24 hours, ending at the last hour, and for
historical daily usage. In API 58.0 and later, you can enable Enhanced Usage Metrics to get usage data by event name and client for
granular time intervals. PlatformEventUsageMetric contains separate usage metrics for platform events and change data capture
events. This object is available in API version 50.0 and later.

PlatformStatusAlertEvent
[The documentation has moved to PlatformStatusAlertEvent in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/sforce_api_objects_platformstatusalertevent.htm) _Platform Events Developer Guide_ .

PortalDelegablePermissionSet
PortalDelegablePermissionSet is a base platform object used to store permission sets that can be assigned by a delegated
portal/external user admin (DPUA) to portal users. This object is available in API version 47.0 and later.

PplnInspListViewCalcClmn
Represents a column configuration for a pipeline inspection list view. Determines which calculated columns appear in a pipeline or
intelligence view and their display order. This object is available in API version 66.0 and later.

PresenceConfigDeclineReason
Represents the settings for a decline reason that a presence user provides when declining work. This object is available in API version
37.0 and later.

PresenceDeclineReason
Represents an Omni-Channel decline reason that agents can select when declining work requests. This object is available in API
version 37.0 and later.

PresenceUserConfig
Represents a configuration that determines a presence user’s settings. This object is available in API version 32.0 and later.

PresenceUserConfigProfile
Represents a configuration that determines the settings that are assigned to presence users who are assigned to a specific profile.
User-level configurations override profile-level configurations. This object is available in API version 32.0 and later.

PresenceUserConfigUser
Represents a configuration that determines the settings that are assigned to a presence user. These user-level configurations override
profile-level configurations. This object is available in API version 32.0 and later.

PriceAdjustmentGroupShape
Defines the business logic for a top-level price adjustment, for example, a discount applied to an entire order. This object is available
in API version 57.0 and later.

PriceAdjustmentItemShape
Defines the business logic for an item-level price adjustment, for example, a discount on an order item. This object is available in API
version 57.0 and later.

PriceAdjustmentSchedule
Represents a series of discounts offered depending on your product's configuration, quantity, and when they’re purchased in
combination with other products. This object is available in API version 47.0 and later.


Standard Objects

PriceAdjustmentTier
Represents a discount tier in a price adjustment schedule. This object is available in API version 47.0 and later.

Pricebook2
Represents a price book that contains the list of products that your org sells.

Pricebook2History
Represents historical information about changes that have been made to the standard fields of the associated Pricebook2, or to any
custom fields with history tracking enabled. This object is available in API version 66.0 and later.

PricebookEntry
Represents a product entry (an association between a Pricebook2 and Product2) in a price book.

PricebookEntryAdjustment
Read-only junction object created when you associate a price adjustment schedule with a price book entry. This object is available
in API version 47.0 and later.

PriceProtectionExecution
Represents an instance of running the price protection process, capturing execution time, status, and the effective date of price
changes. This object is available in API version 63.0 and later.

PriceProtectExecLineItem
Represents a line item created as part of a Price Protection Execution. This object is available in API version 63.0 and later.

PriceProtectionTerm
Represents a configuration record that defines the rules, types, and eligible conditions for price protection. This object is available
in API version 63.0 and later.

PrivacyHold
Represents a Privacy Hold that indicates that a record should be preserved from masking or deletion by Data Management policies
in Privacy Center. This object is available in API version 59.0 and later.

PrivacyHoldReason
Represents the business or legal purpose for why a record has a Privacy Hold. This object is available in API version 59.0 and later.

PrivacyJobSession
Represents the status of past, ongoing, and scheduled policy jobs in Privacy Center. This object is available in API version 59.0 and
later.

PrivacyObjectSession
Represents the status of each object being processed in past, ongoing, and scheduled policy jobs in Privacy Center. This object is
available in API version 59.0 and later.

PrivacyRequest
See details and monitor the status of Data Subject Access Requests made in Privacy Center. This object is available in API version
54.0 and later.

PrivacyRTBFRequest
Represents a Right to Be Forgotten Request made in Privacy Center. This object is available in API version 59.0 and later.

PrivacySessionRecordFailure
Represents error messages encountered during policy job executions in Privacy Center. This object is available in API version 59.0
and later.

Problem
Problems represent the root cause data of one or more incidents. This object contains all the details of a problem, documenting the
history of the problem from detection to closure. This object is available in API version 53.0 and later.


Standard Objects

ProblemIncident
Represents a junction object that relates a Problem to an Incident. This object is available in API version 53.0 and later.

ProblemRelatedItem
Represents a junction object that relates a Problem to an Asset. This object is available in API version 53.0 and later.

ProcessDefinition
Represents the definition of a single approval process.

ProcessException
Represents a business exception, such as a processing failure on an order summary. A separate process is required to resolve the
failure that caused the process exception before processing can continue. This object is available in API version 50.0 and later.

ProcessFlowMigration
Represents a process's migrated criteria and the resulting migrated flow. This object is available in API version 58.0 and later.

ProcessInstance
Represents an instance of a single, end-to-end approval process. Use this and the node, step, and workitem process instance objects
to create approval history reports.

ProcessInstanceHistory
This read-only object shows all steps and pending approval requests associated with an approval process (ProcessInstance).

ProcessInstanceNode
Represents a step in an instance of an approval process. Compare to ProcessNode, which describes the step in a process definition.
Use this object to retrieve approval history.

ProcessInstanceStep
Represents one work item in an approval process (ProcessInstance).

ProcessInstanceWorkitem
Represents a user’s pending approval request.

ProcessNode
Describes a step in a process definition. Compare to ProcessInstanceNode, which describes a step in a running process. This object
is available in API version 31.0 and later.

ProducerCommission
Represents a producer's commission for an insurance policy. The commission can be calculated from the commissionable transactions
or can be populated from an external system. This object is available in API version 51.0 and later.

Product2
Represents a product that your company sells.

Product2DataTranslation
Represents the translated values of the data stored within a Product2 record’s fields. This object is available in API version 45.0 and
later.

ProductAttribute
Represents the attributes that can be associated with a product. This object is available in API version 50.0 and later.

ProductAttributeSet
Represents a group of attributes that can be associated with a product. This object is available in API version 50.0 and later.

ProductAttributeSetItem
Represents a set of attributes that can be associated with a product. This object is available in API version 50.0 and later.


Standard Objects

ProductAttributeSetProduct
Represents the product associated with a set of attributes. This object is available in API version 50.0 and later.

ProductCatalog
The container that holds a Product Category hierarchy. This object is available in API version 55.0 and later.

ProductCategory
Represents the category that products are organized in.This object is available in API version 49.0 and later.

ProductCategoryProduct
Holds the relation between product and product category to assign products to a category. This object is available in API version
55.0 and later.

ProductCategoryDataTranslation
Represents the translated values for the data stored within a ProductCategory record’s fields. This object is available in API version
46.0 and later.

ProductComponentGroup
Represents the logical grouping of associated products in a bundle and the products’ arrangement policy (group cardinality). This
object is available in API version 58.0 and later.

ProductConsumed
Represents an item from your inventory that was used to complete a work order or work order line item in field service.

ProductDetectedPriceChange
Represents a detected change in price for a product associated with a partner account. This object is available in API version 63.0
and later.

ProductEntitlementTemplate
Represents predefined terms of customer support (Entitlement) that users can add to products (Product2).

ProductFeaturedProduct
Represents the user-defined collection of featured products that are meant to cross-sell or upsell with your product. This object is
available in API version 64.0 and later.

ProductItem
Represents the stock of a particular product at a particular location in field service, such as all bolts stored in your main warehouse.

ProductItemTransaction
Represents an action taken on a product item in field service. Product item transactions are auto-generated records that help you
track when a product item is replenished, consumed, or adjusted.

ProductMedia
Represents the rich media, including images and attachments, that can be added to products.This object is available in API version
49.0 and later.

ProgramProduct
Represents a junction between Program and Product2. This will hold Product2 values related to a Program. This object is available
in API version 58.0 and later.

ProductQuantityRule
Represents the relationship between a quantity rule and a product. This object assigns quantity rules to a product. This object is
available in API version 51.0 and later.

ProductRelatedComponent
Represents a product that is included in a product bundle, a set, or a product and an add-on. This object is available in API version
57.0 and later.


Standard Objects

ProductRelationshipType
Defines the relationship between two sales transaction items. For example, defines a relationship between a bundle and a bundle
component. This object is available in API version 57.0 and later.

ProductRequest
Represents an order for a part or parts in field service.

ProductRequestLineItem
Represents a request for a part in field service. Product request line items are components of product requests.

ProductRequired
Represents a product that is needed to complete a work order or work order line item in field service.

ProductSellingModel
Defines one method by which a product can be sold; for example, as a one-time sale, an evergreen subscription, or a term-defined
subscription. If the product is sold on subscription, this object defines the subscription’s term. A product can have multiple product
selling models. This object is available in API version 55.0 and later.

ProductSellingModelOption
A junction object between Product Selling Model and Product2. This object is available in API version 55.0 and later.

ProductServiceCampaign
Represents a set of activities to be performed on a product service campaign asset, such as a product recall for safety issues or product
defects. This object is available in API version 51.0 and later.

ProductServiceCampaignItem
Represents a product service campaign's asset. This object is available in API version 51.0 and later.

ProductServiceCampaignItemStatus
Represents a status for a product service campaign item in field service. This object is available in API version 51.0 and later.

ProductServiceCampaignStatus
Represents a status for a product service campaign in field service. This object is available in API version 51.0 and later.

ProductTransfer
Represents the transfer of inventory between locations in field service.

ProductWarrantyTerm
Defines the relationship between a product or product family and warranty term. This object is available in API version 50.0 and
later.

Profile
Represents a profile, which defines a set of permissions to perform different operations. Operations can include creating a custom
profile or querying, adding, updating, or deleting information.

ProfileSkill
Represents a profile skill, which describes a user’s professional knowledge. This is a global record for the organization, and users are
associated through the ProfileSkillUser object.

ProfileSkillEndorsement
Represents a detail relationship of ProfileSkillUser. An endorsement of a profile skill shows approval and support of another user’s
publicly declared skill.

ProfileSkillShare
Represents a sharing entry on a ProfileSkill.

ProfileSkillUser
Represents a detail relationship of User. The object connects profile skills with users.


Standard Objects

ProgramRebateType
Represents a rebate structure associated with a Rebate Program. This object is available in API version 63.0 and later.

Promotion
Represents a promotion for B2B or D2C stores. This object is available in API version 52.0 and later.

PromotionLineItemRule
Lists compound conditions about a promotion. This object is available in API version 59.0 and later.

PromotionMarketSegment
Represents a market segment within B2B Commerce that promotions can be assigned to. This object is available in API version 52.0
and later.

PromotionQualifier
Represents the product, product category, or order that you want to target with your promotion qualifier in a B2B or D2C store. This
object is available in API version 52.0 and later.

PromotionSegment
Represents a promotion segment, which you can assign to different stores or buyer groups, allowing them to access the promotion.
This object is available in API version 52.0 and later.

PromotionSegmentBuyerGroup
Represents a promotion segment, associated with a buyer group, and used for B2B Commerce. This object is available in API version
52.0 and later.

PromotionSegmentSalesStore
Represents a promotion segment, associated with a store, and used for B2B Commerce. This object is available in API version 52.0
and later.

PromotionTarget
Represents the product, product category, or order that you want to target with your promotion in a B2B Store or D2C store. This
object is available in API version 52.0 and later.

PromotionTier
Represents a tier of a promotion that includes multiple tiers. A promotion can have up to 10 tiers. This object is available in API
version 57.0 and later.

Prompt
Represents record details about an in-app guidance prompt or walkthrough. Available in API version 46.0 and later.

PromptAction
Represents how the user interacted with the in-app guidance prompt or walkthrough. Available in API version 46.0 and later.

PromptError
Represents the error or warning associated with the PromptAction. Available in API version 52.0 and later.

PromptActionOwnerSharingRule
Represents a rule which determines `PromptAction` sharing access for the owners. Available in API version 46.0 and later.

PromptActionShare
Represents a sharing entry on a prompt action record. Available in API version 46.0 and later.

PromptLocalization
Represents the translated value of a label for record details about in-app guidance when the Translation Workbench is enabled for
your org. Available in API version 48.0 and later.

PromptVersion
Represents an in-app guidance prompt or walkthrough. Available in API version 46.0 and later.


Standard Objects

PromptVersionLocalization
Represents the translated value of a label for-app guidance when the Translation Workbench is enabled for your org. Available in
API version 48.0 and later.

Prospect
Represents a prospect. A prospect is an individual who has shared contact information, but isn't yet qualified. This object is available
in API version 63.0 and later.

ProspectingAgentDataSource
For internal use only.

ProspectingAgentRcmdTarget
Represents prospecting information suggested by generative AI. This object is available in API version 66.0 and later.

ProspectingAgentSpec
For internal use only.

ProspectingAgentSpecParm
For internal use only.

ProspectingAgentUserSpec
For internal use only.

ProrationPolicy
Defines how the price of a subscription is divided into time periods and how the price is calculated for each time period. This object
is available in API version 55.0 and later.

PublicComplaint
Represents the complaints submitted by public users. This object is available in API version 49.0 and later.

PurchaseQuantityRule
Represents a rule that restricts the quantity of a product that can be purchased. The rule can be an increment, minimum, or maximum
rule. This object is available in API version 52.0 and later.

PushTopic
Represents a query that is the basis for notifying Streaming API clients of changes to records in an org. This object is available in API
version 21.0 and later.

PushUpgradeCustomization
Customized push upgrades allow a package subscriber to block push upgrades to their org. Package developers control which
subscribers can opt into customized push upgrades. Each push upgrade customization maps to a specific package and to a specific
subscriber org. This object is available in API version 60.0 and later.

QueuedExecutionEventLog
Queued Execution events contain details about queued executions—for example, batch Apex. This object is available in API version
65.0 and later.

QueueRoutingConfig
Represents the settings that determine how work items are routed to agents. This object is available in API version 32.0 and later.

Question
Represents a question in a zone that users can view and reply to.

QuestionDataCategorySelection
A data category selection represents a data category that classifies a question.

QuestionReportAbuse
Represents a user-reported abuse on a Question in a Chatter Answers zone. This object is available in API version 24.0 and later.


Standard Objects

QuestionSubscription
Represents a subscription for a user following a Question. This object is available in API version 24.0 and later.

QueueSobject
Represents the mapping between a queue Group and the types associated with the queue, including custom objects.

QuickText
This object stores a snippet of text that allows users to send a quick response to a customer. Use quick text to create greetings,
answers to common questions, short notes, and more. This object is available in API version 24.0 and later.

QuickTextUsage
Represents the usage of quick text on a record, including which quick text was used, who used it, and how they used it. Quick text
is a snippet of text that allows users to send a quick response to a customer. This object is available in API version 47.0 and later.

Quote
Represents a quote, which is a record showing proposed prices for products and services. Available in API version 18.0 and later.

QuoteAction
Indicates the type of sales transaction that’s being quoted; for example, a renewal sale. This object is available in API version 59.0
and later.

QuoteAdjustmentGroup
Group containing a set of adjustments applied to a quote. This object is available in API version 58.0 and later.

QuoteDocument
Represents a quote in document format. Available in API version 18.0 and later.

QuoteLineGroup
Stores the group information for line items in a quote. It also stores the aggregated line field information (subtotal). It contains a
parent-child relationship to quote. This object is available in API version 61.0 and later.

QuoteLineItem
Represents a quote line item, which is a member of the list of Product2 products associated with a quote, along with other information
about those line items on that quote. Available in API version 18.0 and later.

QuoteLineItemRecipient
Represents a site, employee, or other entity for which services are being quoted. This could include details such as the recipient's
name, contact information, associated site or location, and any specific requirements or preferences for the quoted services. This
object is available in API version 62.0 and later.

QuoteLinePriceAdjustment
Indicates the calculated price adjustment that is applied to the quote line, for example, a calculated volume discount or the prorated
value of a manual discount. Use the quote line price adjustment to inform potential customers about the type, value, and total
amount of their discounts. This object is available in API version 56.0 and later.

QuoteLineRelationship
Describes the relationship between quote line items, such as items in a bundle. When you create a QuoteLineRelationship object,
it’s immutable: it can’t be edited or removed. This object is available in API version 58.0 and later.

QuoteItemTaxItem
The tax that is applied to a quote line item. This object is available in API version 55.0 and later.

QuoteLineWorkSource
Represents an association between a quote and work sources, such as assets, quote line items, order products, or work type groups.
This object is available in API version 63.0 and later.


Standard Objects

QuoteRecipientGroup
Represents a recipient group for which offers or products with the same configuration are being added. This also includes reusing
these groups to add or remove recipients. This object is available in API version 64.0 and later.

QuoteRecipientGroupMember
Represents a junction between a quote line item recipient and a quote recipient group. This object is available in API version 64.0
and later.

RecentFieldChange
Use this virtual object to see how an opportunity has changed in the past seven days. Learn the previous value of a field, who made
the change, and when the change was made. This object is available in API version 52.0 and later.

RecentlyViewed
Represents records or list views that the current user has recently viewed or referenced (by viewing a related record). List views are
available in API version 29.0 and later.

Recommendation
Represents the recommendations surfaced as offers and actions for Einstein Next Best Action. This object is available in API version
45.0 and later.

RecommendationResponse
Represents the user responses to a presented offer or recommendation for Einstein Next Best Action. This object is available in API
version 51.0 and later.

RecordAction
Represents a relationship between a record and an action, such as a flow. Create a RecordAction for every action that you want to
associate with a particular record. Available in API version 42.0 and later.

RecordActionHistory
Represents the lifecycle of a RecordAction as it goes through different states. Available in API version 44.0 and later.

RecordsetFilterCriteria
Represents a set of filters that can be used to match service appointments or assets based on your criteria fields. For example, you
can create recordset filter criteria so that only service appointments that satisfy the filter criteria are matched to the filtered shifts,
and likewise only maintenance work rules that satisfy your criteria are matched to assets. This object is available in API version 50.0
and later. Assets and maintenance work rules are available in API version 52.0 and later.

RecordsetFilterCriteriaRule
Represents a rule using fields from the designated source object to create filters on the filtered, or target, object.
RecordsetFilterCriteriaRule is associated with the RecordsetFilterCriteria object. This object is available in API version 50.0 and later.

RecordsetFltrCritMonitor
Monitors whether the value of an asset attribute is within the threshold of a recordset filter criteria (RFC). You can monitor one or
more RFCs for an Asset. This object is available in API version 57.0 and later.

RecordType
Represents a record type.

RecordTypeLocalization
Represents the translated value of a label for a record type when the Translation Workbench is enabled for your organization.

RecordVisibility (Pilot)
Represents the visibility attributes that determine a record’s read access. This object is read only and is available in API version 46.0
and later.


Standard Objects

RedirectWhitelistUrl
Represents a trusted URL for external user redirections. Redirections to a different Salesforce org, including its publicly served pages
and content, are allowed from your Salesforce org only when the URL is a RedirectWhitelistUrl. For non-Salesforce URLs, a session
setting controls whether redirections from pages and components built in Salesforce Classic are restricted to RedirectWhitelistUrl
objects. Except for cross-org redirections, you can’t restrict redirections that originate from pages and components built with Lightning
Experience. This object is available in API version 48.0 and later.

Refund
Represents a refund made against a payment. This object is available in API version 48.0 and later.

RefundLinePayment
A refund line that has been applied to a payment. This object is available in API version 48.0 and later.

RegisteredExternalService
Represents a registered external service used for checkout integrations by data integrators. This object is available in API version 49.0
and later.

RelatedListColumnDefinition
Represents information about a column in a related list. A related list specifies a set of records for a related object, based on specific
criteria. This object is available in API version 55.0 and later.

RelatedListDefinition
Represents information about a related list. A related list specifies a set of records for a related object, based on specific criteria. This
object is available in API version 55.0 and later.

RemoteKeyCalloutEvent
[The documentation has moved to RemoteKeyCalloutEvent in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/sforce_api_objects_remotekeycalloutevent.htm) _Platform Events Developer Guide_ .

Reply
Represents a reply that a user has submitted to a question in an answers zone.

ReplyEmailSettings
Represents a reply mail management configuration, which is used to configure emails that are received by an email sending domain.
This object is available in API version 62.0 and later.

ReplyReportAbuse
Represents a user-reported abuse on a Reply in a Chatter Answers zone. This object is available in API version 24.0 and later.

ReplyText
A text reply generated by Einstein Reply Recommendations that is based on closed chat transcripts. Admins review replies and
publish them to quick text, editing them as needed. Einstein recommends relevant published replies to support agents in the
Lightning Service Console, and agents can insert replies into chats or messaging sessions. This object is available in API version 49.0
and later.

Report
Represents a report, a set of data that meets certain criteria, displayed in an organized way. Access is read-only. This object is available
in API version 20.0 and later.

ReportEventLog
Report event logs contain information about what happened when a user ran a report. This event type includes all activity that's in
the Report Export event type, and additional information. For example, it has user activity for reports exported as both Formatted
Report and Details Only output. This object is available in API version 61.0 and later.


Standard Objects

ReportExportEventLog
Report Export events contain details about reports that a user exported. For example, this event type captures when a user exports
a report as Details Only output. But it doesn’t capture reports that users export as Formatted Report or XLSX Detail output. For that
data, see the Report event type. This object is available in API version 65.0 and later.

ReportTag
Associates a word or short phrase with a Report. This object is available in API version 20.0 and later.

ReputationLevel
Represents a reputation level defined for an Experience Cloud site. This object is available in API version 32.0 and later.

ReputationLevelLocalization
Represents the translated value of a reputation level. Reputation level localization only applies for reputation levels in Experience
Cloud sites. This object is available in API version 35.0 and later.

ReputationPointsRule
Represents the reputation point rules for an Experience Cloud site. Each rule specifies an action that members can earn points from
and the points associated with those actions in a particular site. This object is available in API version 32.0 and later.

ResourceAbsence
Represents a time period in which a service resource is unavailable to work in Field Service, Salesforce Scheduler, or Workforce
Engagement. This object is available in API version 38.0 and later.

ResourcePreference
Represents an account’s preference for a specified service resource on field service work.

RestApiEventLog
REST API event logs contain details about REST-specific requests. This object is available in API version 61.0 and later.

RetentionStoreUsage
Represents the total usage of the org's retention store measured at specific points in time. This object is available in API version 66.0
and later.

ReturnOrder
Represents the return or repair of inventory or products in Field Service, or the return of order products in Order Management. This
object is available in API version 42.0 and later.

ReturnOrderItemAdjustment
Represents a price adjustment on a return order line item. This object is available in API version 50.0 and later.

ReturnOrderItemTax
Represents the tax on a return order line item or return order item adjustment. This object is available in API version 50.0 and later.

ReturnOrderLineItem
Represents a specific product that is returned or repaired as part of a return order in Field service, or a specific order item that is
returned as part of a return order in Order Management. This object is available in API version 42.0 and later.

ReturnOrderOwnerSharingRule
Represents the rules for sharing a return order with user records other than the owner or anyone above the owner in the role hierarchy.
This object is available in API version 42.0 and later.

RevenueAsyncOperation
Represents the status of an asynchronous process initiated by a REST request in Subscription Management. This object is available
in API versions 57.0 to 59.0. Use AsyncOperationTracker instead of RevenueSyncOperation in API version 59.0 and later.


Standard Objects

RevenueTransactionErrorLog
Contains information about errors that occurred while processing a request. The error record persists until another error with the
same category, primary record, and (optionally) related record occurs. This object is available in API version 55.0 and later.

RpaFlowResultEvent
Reserved for future use.

RpaRobot
Reserved for future use.

RpaRobotAsgnMaintWindow
Reserved for future use.

RpaRobotAsgnSessionInf
Reserved for future use.

RpaRobotDefinition
Reserved for future use.

RpaRobotMaintWindow
Reserved for future use.

RpaRobotMaintWindowDef
Reserved for future use.

RpaRobotPool
Reserved for future use.

RpaRobotPoolAsgnRobot
Reserved for future use.

RpaRobotPoolDefinition
Reserved for future use.

RpaRobotPoolFlowAsgn
Reserved for future use.

RpaRobotSessionInfo
Reserved for future use.

RpaRobotSessionInfoDef
Reserved for future use.

RuleTerritory2Association
Represents a record-assignment rule and its association to an object, such as Account. Available if Sales Territories has been enabled.

SalesAIScoreCycle
Represents the cycle type and ID used to score records. This object is available in API version 47.0 and later.

SalesAIScoreModelFactor
Represents the factors that Sales Cloud Einstein uses to build a scoring model. Scoring models are used by features, such as Opportunity
Scoring, to score individual records. This object is available in API version 47.0 and later.

SalesforceLoginAsEventLog
Salesforce LoginAs Event provides details about the Salesforce User's login into Customer Org as Customer's authorized user. This
object is available in API version 65.0 and later.


Standard Objects

SalesChannel
Represents the origin of an order. For example, a web storefront, physical store, marketplace, or mobile app. If you integrate Salesforce
Order Management with Salesforce B2C Commerce, set up a SalesChannel corresponding to each Site in your B2C Commerce
implementation. This object is available in API version 48.0 and later.

SalesforceContract
Read-only virtual object used in the Your Account App. Represents contract information related to your organization’s Salesforce
subscription.

SalesforceInvoice
Read-only virtual object used in the Your Account App. Represents information about your organization’s invoices with Salesforce.

SalesforcePayment
Read-only virtual object used in the Your Account App. Represents information about payments related to your organization’s
Salesforce invoice.

SalesforceQuote
Read-only virtual object used in the Your Account App. Represents information about your organization’s quotes with Salesforce.

SalesStoreCatalog
Represents the catalog associated with a store. This object is available in API version 49.0 and later.

SalesTransactionItemShape
Defines the business logic for a sales transaction shape item, for example, an item in an order. This object is available in API version
57.0 and later.

SalesTransactionShape
Defines the business logic for a sales transaction; for example, an order, a quote, or a cart. This object is available in API version 57.0
and later.

SalesTransactionType
Represents the type of sales transaction, such as an initial, renewal, or amendment sale, and its related pricing configuration.. This
object is available in API version 61.0 and later.

SalesTrxnItemRelationShape
Describes the relationship between sales transaction shape items; for example, a bundle or set. This object is available in API version
57.0 and later.

SalesWorkQueueSettings
Represents settings used to customize work queue options for third-party scoring. Third-party scoring enables custom number fields
on person accounts, contacts, and leads. You must be a Sales Engagement customer to update this object. Previously, you could
only use the Einstein Intelligence Score for third-party scoring. Available starting in Version 47.0.

SandboxStatusEventLog
SandboxStatusEventLog stores details about Sandbox copies. This object is available in API version 62.0 and later.

SamlSsoConfig
Represents a SAML Single Sign-On configuration.This object is available in API version 32.0 and later.

SavedPaymentMethod
Represents a payment method saved by an authenticated customer. This object is available in API version 58.0 and later

SavedPaymentMethodEvent
Represents a saved payment method platform event. Subscribe to these events so you can listen and respond to them when they’re
published. For example, create a Salesforce Flow that is triggered when one of these events is published. This object is available in
API version 59.0 and later.


Standard Objects

SchedulingAdherenceDetail
Represents the breakdown of daily shift adherence data by agent status. This object is available in API version 54.0 and later.

SchedulingAdherenceSummary
Represents daily shift adherence data for a service resource in a service territory and job profile on a specific date. This object is
available in API version 54.0 and later.

SchedulingConstraint
Represents scheduling constraints on each service resource. This object is available in API version 50.0 and later.

SchedulingObjective
Represents business goals that the scheduling tools consider. This object is available in API version 53.0 and later.

SchedulingRule
Represents scheduling rules that are hard constraints in the scheduling logic engine. This object is available in API version 52.0 and
later.

SchedulingRuleParameter
Represents scheduling rule parameters associated with a scheduling rule. This object is available in API version 52.0 and later.

Scontrol
A custom s-control, which is custom content that is hosted by the system but executed by the client application.

ScontrolLocalization
The translated value of the field label for an s-control.

Scorecard
Use scorecards to measure partner performance and establish benchmarks for channel programs within Experience Cloud. Display
any report summary results that your channel account manager or executive team wants to see. This object is available in API version
40.0 and later.

ScorecardAssociation
Represents a connection between a specific scorecard and the associated account, channel program, or channel program level. This
object is available in API version 41.0 and later.

ScorecardMetric
Stores information about a Salesforce report that is run and summarized to get a single value. The stored value is added as a metric
to the related Scorecard object. This object is available in API version 40.0 and later.

ScoreIntelligence
For internal use only.

ScratchOrgInfo
Represents a scratch org and its audit log. Use this object to create a scratch org and keep a log of its creation and deletion. This
object is available in API version 41.0 and later.

SearchActivity
Represents search activity on a Knowledge article. Also known as KnowledgeSearchActivity. This object is available in API version
38.0 and later.

SearchClickEventLog
Search Click Event Log contains details about the user’s interaction with the search results. This object is available in API version 61.0
and later.

SearchEventLog
Search Event Log provides details about the user’s search query. This object is available in API version 61.0 and later.


Standard Objects

SearchLayout
Represents a search layout defined for an object. This object is available in API version 35.0 and later.

SearchPromotionRule
Represents a promoted search term, which is one or more keywords that you associate with a Salesforce Knowledge article. When
a user’s search query includes these keywords, the associated article is returned first in search results. This object is available in API
version 31.0 and later.

SecurityCustomBaseline
Provides the ability to read, create, and delete user-defined custom security baselines, which define an org’s security standards. This
object is available in API version 39.0 and later.

SelfServiceUser
Represents a Contact who has been enabled to use your organization’s Self-Service portal, where he or she can obtain online support.

Seller
Represents the seller role of an individual with respect to a particular company or organization. This object is available in API version
53.0 and later.

SenderEmailAddress
Represents a From address in a marketing email. This object is available in API version 63.0 and later.

ServiceAppointment
Represents an appointment to complete work for a customer in Field Service, Lightning Scheduler,Intelligent Appointment
Management, and Virtual Care.This object is available in API version 38.0 and later.

ServiceAppointmentStatus
Represents a possible status of a service appointment in field service.

ServiceChannel
Represents a channel of work items that are received from your organization—for example, cases, chats, or leads. This object is
available in API version 32.0 and later.

ServiceChannelFieldPriority
Represents a secondary routing priority field-value mapping. This object is available in API version 47.0 and later.

ServiceChannelStatus
Represents the status that’s associated with a specific service channel. This object is available in API version 32.0 and later.

ServiceChannelStatusField
Represents the values that you use to indicate completed and in-progress work item status for the status field in the Status-Based
Capacity routing model. This object is available in API version 49.0 and later.

ServiceContract
Represents a customer support contract (business agreement). This object is available in API version 18.0 and later.

ServiceContractOwnerSharingRule
Represents the rules for sharing a ServiceContract (customer service agreement) with users other than the owner. This object is
available in API version 18.0 and later.

ServiceCrew
Represents a group of service resources who can be assigned to service appointments as a unit.

ServiceCrewMember
Represents a technician service resource that belongs to a service crew.


Standard Objects

ServiceCrewOwnerSharingRule
Represents the rules for sharing a service crew with user records other than the owner or anyone above the owner in the role
hierarchy.

ServicePresenceStatus
Represents a presence status that can be assigned to a service channel. This object is available in API version 32.0 and later.

ServiceReport
Represents a report that summarizes a work order, work order line item, or service appointment.

ServiceReportLayout
Represents a service report template in field service.

ServiceRequest
Represents a formal request from a user for something to be provided, such as access, information, hardware, or software. This object
manages the lifecycle of these tasks, which are typically low-risk, and can be fulfilled through a defined, repeatable process. For
example, a Service Request can be created for an employee requesting a new laptop or a student needing a transcript. This object
is available in API version 66.0 and later.

ServiceResource
Represents a service technician or service crew in Field Service and Salesforce Scheduler, or an agent in Workforce Engagement. This
object is available in API version 38.0 and later.

ServiceResourceCapacity
Represents the maximum number of scheduled hours or number of service appointments that a capacity-based service resource
can complete within a specific time period. This object is available in API version 38.0 and later.

ServiceResourceCapacityHistory
Represents the history of changes made to tracked fields on a service resource capacity record. This object is available in API version
38.0 and later.

ServiceResourceDataTranslation
Represents the translated values of the data stored within a ServiceResource record’s fields. This object is available in API version
54.0 and later.

ServiceResourceOwnerSharingRule
Represents the rules for sharing a service resource with user records other than the owner or anyone above the owner in the role
hierarchy. This object is available in API version 38.0 and later.

ServiceResourcePreference
Represents the service resource scheduling preferences that are considered as a business objective in the scheduling logic engine.
This object is available in API version 52.0 and later.

ServiceResourceSkill
Represents a skill that a service resource possesses in Field Service and Lightning Scheduler. This object is available in API version
38.0 and later.

ServiceSetupProvisioning
Represents a task completed by the Service Setup Assistant. This object is available in API version 52.0 and later.

ServiceTerritory
Represents a geographic or functional region in which work can be performed in Field Service, Salesforce Scheduler, or Workforce
Engagement. This object is available in API version 38.0 and later.

ServiceTerritoryDataTranslation
Represents the translated values of the data stored within a ServiceTerritory record’s fields. This object is available in API version 54.0
and later.


Standard Objects

ServiceTerritoryLocation
Represents a location associated with a particular service territory in field service.

ServiceTerritoryMember
Represents a service resource who can be assigned in a service territory in Field Service, Salesforce Scheduler, or Workforce Engagement.
This object is available in API version 38.0 and later.

ServiceTerritoryWorkType
Represents the relationship between a ServiceTerritory object and a WorkType object for Salesforce Scheduler appointments. This
object is available in API version 45.0 and later.

SessionPermSetActivation
The SessionPermSetActivation object represents a permission set assignment activated during an individual user session. When a
SessionPermSetActivation object is inserted into a permission set, an activation event fires, allowing the permission settings to apply
to the user’s specific session. This object is available in API versions 37.0 and later.

SetupAssistantStep
For internal use only.

SetupAuditTrail
Represents changes you or other admins made in your org’s Setup area for at least the last 180 days. This object is available in API
version 15.0 and later.

SetupEntityAccess
Represents the enabled setup entity access settings (such as for Apex classes) for the parent PermissionSet. This object is available
in API version 25.0 and later.

ShapeRepresentation
Contains information about the shape of an org. The shape of an org includes licenses and limits information. You can easily create
scratch orgs based on a source org’s shape. This object is available in API version 50.0 and later.

SharingRecordCollection
Represents a collection of records. This object is available in API version 51.0 and later.

SharingRecordCollectionItem
Represents a single record in a collection of records. This object is available in API version 51.0 and later.

SharingRecordCollectionMember
Represents a user with access to a collection of records. This object is available in API version 51.0 and later.

Shift
Represents a shift for service resource scheduling. Available in API versions 46.0 and later.

ShiftHistory
Represents the history of changes made to tracked fields on a time sheet. Available in API versions 46.0 and later.

ShiftOwnerSharingRule
Represents the rules for sharing a shift with user records other than the owner or anyone above the owner in the role hierarchy.
Available in API versions 46.0 and later.

ShiftPattern
Represents a pattern of templates for creating shifts. This object is available in API version 51.0 and later.

ShiftPatternEntry
ShiftPatternEntry links a shift template to a shift pattern. This object is available in API version 51.0 and later.

ShiftSegment
Represents a scheduled activity within a shift. This object is available in API version 55.0 and later.


Standard Objects

ShiftSegmentType
Represents a type of activity scheduled within a shift. This object is available in API version 55.0 and later.

ShiftShare
Represents a sharing entry on a field service shift. Available in API versions 46.0 and later.

ShiftStatus
Represents a shift, such as Tentative, Published, or Confirmed. Available in API versions 46.0 and later.

ShiftTemplate
Represents a template for creating shifts. This object is available in API version 51.0 and later.

Shipment
Represents the transport of inventory in field service or a shipment of order items in Order Management.

ShipmentItem
Represents an order item included in a shipment. This object is available in API version 51.0 and later.

ShippingCarrier
Shipping company or carrier responsible for transporting goods or packages. Examples include UPS, FedEx, and USPS. This object is
available in API version 61.0 and later.

ShippingCarrierMethod
Shipping service provided by a shipping carrier. Examples include Ground, 2Day, and NextDay. Service depends on the range of
transit times available for each carrier. This object is available in API version 61.0 and later.

ShippingConfigurationSet
Shipping configuration for a set of products in a store. This object is available in API version 59.0 and later.

ShippingConfigSetProduct
Represents a product associated with a shipping configuration. This object is available in API version 64.0 and later.

ShippingRateArea
A designated geographical area that’s available for shipping. This object is available in API version 59.0 and later.

ShippingRateGroup
Available shipping rates based on shipping destination. This object is available in API version 59.0 and later.

SignupRequest
Represents a request for a new sign-up. SignupRequest isn’t supported in sandbox instances and will result in an error. This object
is available in API version 27.0 and later.

Site
Represents a public website that is integrated with an org. This object is available in API version 16.0 and later.

SiteDetail
Represents the details of a Salesforce site or Experience Cloud site. Available in API Version 38.0 and later.

SiteDomain
SiteDomain is a read-only object, and a one-to-many replacement for the Site.TopLevelDomain field. This object is available in API
version 21.0, and has been deprecated as of API version 26.0. In API version 26.0 and later, use the Domain and DomainSite objects
instead.

SiteEventLog
SiteEventLog stores details of Site.com requests. Requests can originate from the browser (UI). This object is available in API version
62.0 and later.


Standard Objects

SiteHistory
Represents the history of changes to the values in the fields of a site. This object is generally available in API version 18.0 and later.

SiteIframeWhitelistUrl
Represents a list of external domains that you allow to frame your Salesforce site or Experience Cloud site pages. This object is
available in API version 44.0 and later.

SiteRedirectMapping
Represents a site redirect from an external site to an Experience Cloud site. This object is available in API version 52.0 and later.

Skill
Represents a category or group of Chat users or service resources in Field Service or Workforce Engagement. This object is available
in API version 24.0 and later.

SkillLevelDefinition
Represents a skill which can be acquired by completing enablement site (myTrailhead) modules. This object is available in API version
51.0 and later.

SkillLevelProgress
Represents training progress for a given user. This object is available in API version 51.0 and later.

SkillProfile
Represents a join between Skill and Profile. This object is available in API version 24.0 and later.

SkillRequirement
Represents a skill that is required to complete a particular task in Field Service, Omni-Channel, Salesforce Scheduler, or Workforce
Engagement. Skill requirements can be added to pending service routing objects in Omni-Channel. They can be added to work
types, work orders, and work order line items in Field Service and Lightning Scheduler. And they can be added to job profiles in
Workforce Engagement. This object is available in API version 38.0 and later. You also can add skill requirements to work items in
Omni-Channel skills-based routing using API version 42.0 and later.

SkillUser
Represents a join between Skill and User. This object is available in API version 24.0 and later.

SlackChannelRelatedRecord
Represents the related record mapping between a Slack channel and a Salesforce record that’s made when you create a Salesforce
channel. This object is available in API version 65.0 and later.

SlaProcess
Represents an entitlement process associated with an Entitlement. This object is available in API version 19.0 and later.

Snippet
Represents a snippet, which is a container for rich text that can be reused across Account Engagement emails and email templates.
This object is available in API version 47.0 and later.

SnippetAssignment
Represents a relationship between a snippet and a campaign. Assignments are required to use snippet content in Account Engagement
emails and email templates. A snippet can be assigned to more than one campaign. This object is available in API version 47.0 and
later.

SoapApiEventLog
SOAP API events contain details about your org's SOAP API request activity. This object is available in API version 61.0 and later.

SocialPersona
Represents a snapshot of a contact's profile on a social network such as Facebook or Twitter. This object is available in API version
22.0 and later.


Standard Objects

SocialPost
Represents a snapshot of a post on a social network such as a Facebook or Twitter. This object is available in API version 23.0 and
later.

Solution
Represents a detailed description of a customer issue and the resolution of that issue.

SolutionStatus
Represents the status of a Solution, such as Draft, Reviewed, and so on.

SolutionTag
Associates a word or short phrase with a Solution.

SOSDeployment
Represents the general settings for deploying SOS video call capability in a native mobile application. This object is available in API
version 34.0 and later.

SOSSession
This object is automatically created for each SOS session and stores information about the session. This object is available in API
versions 34.0 and later.

SOSSessionActivity
Captures information about specific events that occur during an SOS video call, such as when an SOS call begins or ends. This object
is available in API version 34.0 and later.

StagedEmail
For internal use only.

StagedInviteeEmail
Represents an email address that is included on a calendar event but that doesn’t match an existing user, contact, or lead record.
This object is available in API version 66.0 and later.

StagedUnmtchdEmailAddr
Represents data about an email address identified by Einstein Activity Capture that doesn’t match to an existing user, contact, or
lead record. These addresses are only stored temporarily. Related to StagedUnmtchdEmailAddrRela, which represents data about
the email message or calendar event activity associated with an unmatched email. This object is available in API version 66.0 and
later.

StagedUnmtchdEmailAddrRela
Represents data about the message or event activity associated with an email address that Einstein Activity Capture can’t match
with an existing user, contact, or lead record. Related to StagedUnmtchdEmailAddr, which represents data about the unmatched
email address. This object is available in API version 66.0 and later.

Stamp
Represents a User Specialty. This object is available in API version 39.0 and later.

StampAssignment
Represents assignment of a User Specialty to a user. This object is available in API version 39.0 and later.

StandardInvocableActionType
Represents a collection of fields to set up granular user permissions for access to a standard invocable action in Flow Builder. This
object is available in API version 60.0 and later.

StandardShippingRate
Standard shipping rate for a store. This object is available in API version 59.0 and later.


Standard Objects

StaticResource
Represents a static resource that can be used in Visualforce markup.

StoreIntegratedService
Represents an association between an integration and a store. This object is available in API version 49.0 and later.

StreamingChannel
Represents a channel that is the basis for notifying listeners of generic Streaming API events. This object is available in API version
29.0 and later.

Salesforce Surveys Object Model
Learn about how Salesforce Surveys objects relate to one another in Salesforce.

Survey
Represents a survey.

SurveyEmailBranding
Represents the configuration settings for invitation emails sent to survey participants for a particular survey.

SurveyEngagementContext
Represents the context based on which a survey invitation was sent or a survey response was received. This object is available in API
version 49.0 and later.

SurveyInvitation
Represents the invitation sent to a participant to complete the survey.

SurveyPage
Represents a page, such as the title page or a question page, in a survey.

SurveyQuestion
Represents a question in a survey.

SurveyQuestionChoice
Represents an answer choice that a participant can select for a survey question.

SurveyQuestionResponse
Represents a participant’s answer to a specific question.

SurveyQuestionScore
Represents the aggregate of responses for the following question types: date, multiple choice, picklist, radio, ranking, rating, scoring,
[slider, and Net Promoter Score](https://www.salesforce.com/content/dam/web/en_us/www/documents/legal/Agreements/product-specific-terms/net-promoter-and-nps.pdf) [®] (NPS [®] ).

SurveyResponse
Represents information about a participant’s response to a survey, such as the status of the response, the participant’s location, and
when the survey was completed.

SurveySubject
Represents a relationship between a survey and another object, such as an account or a case.

SurveyVersion
Represents a version of a survey.

SurveyVersionAddlInfo
Represents additional information about a survey version. This information defines the default settings of a survey version. This object
is available in API version 49.0 and later.

SvcCatalogCategory
Represents a group of Service Catalog items by functional area. This object is available in API version 58.0 and later.


Standard Objects

SvcCatalogCategoryItem
Represents an association between a Service Catalog item and category. Service catalog items can be grouped into categories. This
object is available in API version 58.0 and later.

SvcCatalogFilterCriteria
Represents an eligibility rule that determines if a Service Catalog user has access to a catalog item. This object is available in API
version 60.0 and later.

SvcCatalogItemDef
Represents a service catalog item that can be requested by a service catalog user. This object is available in API version 53.0 and
later.

SvcCatalogRequest
Represents a request made by a user using the Service Catalog. Catalog builders use this object to report on Service Catalog activity.
This object is available in API version 53.0 and later.

SvcCatalogReqRelatedItem
Represents an item related to a Service Catalog Request. This object is available in API version 53.0 and later.

Swarm
Represents a team of agents, Salesforce users, or Slack users in a Slack channel or thread dedicated to solving a problem. This problem
can be related to a support case, incident, sales opportunity, or change request. This object is available in API version 55.0 and later.

SwarmMember
Represents a Salesforce member, such as an agent, of a swarm. This object is available in API version 55.0 and later.

TabDefinition
Represents a custom tab. Returns only the tabs that the current user has access to. This object is available in API version 43.0 and
later.

TagDefinition
Defines the attributes of child Tag objects.

Task
Represents a business activity such as making a phone call or other to-do items. In the user interface, Task and Event records are
collectively referred to as activities.

TaskPriority
Represents the importance or urgency of a task, such as High, Normal, or Low.

TaskRelation
Represents the relationship between a task and a lead, contacts, and other objects related to the task. If Shared Activities is enabled,
this object doesn’t support triggers, workflow, or data validation rules. This object is available in API version 24.0 and later.

TaskStatus
Represents the status of a task, such as Not Started, Completed, or Closed.

TaskTag
Associates a word or short phrase with a task .

TaskWhoRelation
Represents the relationship between a task and a lead or contacts. This object is available in API version 29.0 and later.


Standard Objects

TaxEngine
A tax engine represents both an instance of a tax engine provider as well as the merchant credentials for that specific instance. When
Subscription Management calculates tax on an order item, it sends a request through Subscription Management Tax Calculation
API to an external tax engine. The Salesforce tax engine record contains information passed to the external tax engine, such as This
object is available in API version 55.0 and later.

TaxEngineInteractionLog
A record of a communication with an external tax engine following a tax calculation request. This object is available in API version
55.0 and later.

TaxEngineProvider
Represents general information about a service that manages a tax engine, such as the ID of the tax adapter Apex class in Salesforce,
and the engine’s namespace prefix. Tax engine providers have a one-to-many relationship with tax engines, where the tax engine
record represents a specific configuration of a tax engine that can be assigned to multiple order items. This object is available in API
version 55.0 and later.

TaxGeoConfig
Represents a tax configuration associated with a GeoCountry. This object is available in API version 57.0 and later.

TaxPolicy
A tax policy contains a group of tax treatments, where each treatment represents parameters to determine how a particular product
is taxed for a transaction line item. Tax policies are related to products, which pass the policy on to the resulting order items. When
you activate an order, Subscription Management assigns a tax treatment to each order item based on the tax policy's
DefaultTaxTreatmentId, then uses the tax treatment to calculate tax. This object is available in API version 55.0 and later.

TaxRate
Represents a tax rate for a tax code and country. This object is available in API version 56.0 and later.

TaxTreatment
A tax treatment contains details about how Salesforce and external engines calculate taxes, and the tax engine to use for tax
calculation. The IsTaxable field determines whether tax is calculated for the product in the transaction. The tax code, tax engine, and
product code are sent via API to the external tax calculation service. When you invoice an order item that has a tax treatment, the
invoice line inherits the tax treatment from the order item’s related billing schedule. The invoice line’s TaxCode field is populated
based on the code that the tax engine used for calculation. This object is available in API version 55.0 and later.

TenantConsumptionAlert
Stores a record each time a utilization signal is reached for your org's consumption-based products. Each record captures the signal
type, the resource that triggered it, and the condition that was met. This object is available in API version 67.0 and later.

TenantScrAIPrmptInjection
Stores generative AI prompt injection data. This object is available in API version 65.0 and later.

TenantSecret
This object stores an encrypted organization-specific key fragment that’s used with the primary secret (KDF seed) to produce
org-specific data encryption keys. This object is available in API version 34.0 and later.

TenantSecurityAIGtwyUsage
Stores Einstein generative AI gateway usage data. This object is available in API version 65.0 and later.

TenantSecurityAlertRuleSelectedTenant
Stores information about a Security Center alert rule for tenants. This object is available for Security Center subscribers in API version
55.0 and later.

TenantSecurityApiAnomaly
[Stores detected anomalies in how users typically make API calls. Fore more information, see Threat Detection. This object is available](https://help.salesforce.com/s/articleView?language=en_US&type=5&id=sf.real_time_em_threat_detection.htm)
to Security Center subscribers in API version 53.0 and later.


Standard Objects

TenantSecurityCertificate
Stores metric details related to public key certificate information. The certificate binds the public key to the identity of an entity. This
object is available in API version 63.0 and later.

TenantSecurityConnectedApp
Stores the details for a connected app that was added to or removed from a Security Center tenant. This object is available to Security
Center subscribers in API version 53.0 and later.

TenantSecurityConfigAgent
Stores metric details related to implemented Agentforce Agents This object is available in API version 65.0 and later.

TenantSecurityCredentialStuffing
[Stores when a user successfully logs in to Salesforce during an identified credential stuffing attack. For more information, see Threat](https://help.salesforce.com/s/articleView?language=en_US&type=5&id=sf.real_time_em_threat_detection.htm)
[Detection. This object is available to Security Center subscribers in API version 53.0 and later.](https://help.salesforce.com/s/articleView?language=en_US&type=5&id=sf.real_time_em_threat_detection.htm)

TenantSecurityCustomMetricSetup
Represents the configuration for a custom metric within Security Center. This object is available in API version 61.0 and later.

TenantSecurityCustomMetricDetail
Stores TenantSecurityCustomMetricStat drill down details. This object is available in API version 62.0 and later.

TenantSecurityCustomMetricStat
Represents custom metric data within Security Center. This object is available in API version 61.0 and later.

TenantSecurityEncryptedField
Represents fields encrypted under your Shield Platform Encryption policy. This object is available in API version 61.0 and later.

TenantSecurityGuestUserAnomaly
Represents metric details for guest user anomaly events detected by Threat Detection. This object is available in API version 60.0
and later.

TenantSecurityEncryptionPolicy
Stores tenant encryption policy status. This object is available in API version 58.0 and later.

TenantSecurityFeature
Stores org features across all tenants in Security Center. This object is available in API version 57.0 and later.

TenantSecurityHealthCheckBaselineTrend
Stores metric details related to Health Check baseline settings. The Health Check detail page in Security Center displays scores and
settings for all your tenants in one place. Use this object to get details about which metrics are collected and for which tenants, and
changes made to the Health Check baseline. This object is available to Security Center subscribers in API version 54.0 and later.

TenantSecurityHealthCheckDetail
Stores the details of Health Check scores for a connected tenant. The Health Check detail page in Security Center displays scores and
settings for all your tenants in one place. Use this object to get settings and risks per tenant on a selected date. This object is available
to Security Center subscribers in API version 53.0 and later.

TenantSecurityHealthCheckTrend
Stores the history of Security Health Check scores for a connected tenant within Security Center. Health Check in Security Center
displays Health Check scores and the average risk settings for all your tenants in one place. This object belongs to the parent tenant
and stores Health Check data pushed from child tenants. This object is available for Security Center subscribers in API version 53.0
and later.

TenantSecurityLicense
Stores license usage information within Security Center. This object is available in API version 59.0 and later.


Standard Objects

TenantSecurityLogin
Stores the login details of a single user to a tenant, grouped by date and type. You can query this object to find out how many times
the user logged in to a specific tenant using a specific login type (for example, username/password or SSO). This object is available
to Security Center subscribers in API version 53.0 and later.

TenantSecurityLoginIpRangeTrend
Stores details of changes related to login IP ranges in Security Center. This object is available in API version 59.0 and later.

TenantSecurityMobilePolicyTrend
Stores metrics related to changes in mobile security policies across all tenants in Security Center. This object is available to Security
Center subscribers in API version 54.0 and later.

TenantSecurityMonitorMetric
Stores the daily count and daily count change for a metric within Security Center. This object is available to Security Center subscribers
in API version 53.0 and later.

TenantSecurityNotification
Stores information about notifications that were triggered in Security Center as a function of the Alerts feature. For more information,
[see Create Alerts for Security Changes. This object is available to Security Center subscribers in API version 54.0 and later.](https://help.salesforce.com/s/articleView?id=xcloud.security_center_create_alerts.htm&type=5&language=en_US)

TenantSecurityNotificationRule
Stores an alert configured in the Security Center Alerts feature to notify recipients of changes made to security settings. For more
[information, see Create Alerts for Security Changes. This object is available to Security Center subscribers in API version 53.0 and](https://help.salesforce.com/s/articleView?id=xcloud.security_center_create_alerts.htm&type=5&language=en_US)
later.

TenantSecurityMetricDetailLink
Represents the link between the metric count and metric drill down. This object is available in API version 48.0 and later.

TenantSecurityPackage
Stores details about managed and unmanaged packages that are added, updated, or removed from a tenant in Security Center. Use
this object to identify whether new packages are installed, upgraded, or uninstalled from your connected tenants. This object is
available to Security Center subscribers in API version 53.0 and later.

TenantSecurityPolicy
[Stores security policies created and deployed in Security Center. For more information, see Define and Deploy Security Policies. This](https://help.salesforce.com/s/articleView?id=xcloud.security_center_deploy_policies.htm&type=5&language=en_US)
object is available to Security Center subscribers in API version 54.0 and later.

TenantSecurityPolicyDeployment
[Stores the status of deployments of a Security Center policy on a tenant. For more information, see Define and Deploy Security](https://help.salesforce.com/s/articleView?id=xcloud.security_center_deploy_policies.htm&type=5&language=en_US)
[Policies. This object is available to Security Center subscribers in API version 54.0 and later.](https://help.salesforce.com/s/articleView?id=xcloud.security_center_deploy_policies.htm&type=5&language=en_US)

TenantSecurityPolicySelectedTenant
[Stores the list of tenants selected for a Security Center policy. For more information, see Define and Deploy Security Policies. This](https://help.salesforce.com/s/articleView?id=xcloud.security_center_deploy_policies.htm&type=5&language=en_US)
object is available to Security Center subscribers in API version 54.0 and later.

TenantSecurityReportAnomaly
Stores anomalies in how users run or export reports, including unsaved reports, as detected by Threat Detection. For more information,
[see Threat Detection. This object is available to Security Center subscribers in API version 53.0 and later.](https://help.salesforce.com/s/articleView?language=en_US&type=5&id=sf.real_time_em_threat_detection.htm)

TenantSecuritySessionHijacking
Stores information about session hijacking events as detected by Threat Detection within connected tenants in Security Center. For
[more information, see Threat Detection. This object is available for Security Center subscribers in API version 53.0 and later.](https://help.salesforce.com/s/articleView?language=en_US&type=5&id=sf.real_time_em_threat_detection.htm)

TenantSecurityTenantInfo
Stores information on changes related to the tenant history. This object is available in API version 56.0 and later.


Standard Objects

TenantSecurityTransactionPolicyTrend
Stores changes to the count of Transaction Security Policies for a connected tenant within Security Center. This object is available
for Security Center subscribers in API version 55.0 and later.

TenantSecurityTrigTransactionSecurityPol
Stores metric details related to Transaction Security Policy triggering events. This object is available in API version 63.0 and later.

TenantSecurityTrustedIpRangeTrend
Stores details of changes related to trusted IP ranges in Security Center.This object is available for Security Center subscribers in API
version 54.0 and later.

TenantSecurityUserActivity
Stores details related to how a user interacts with a tenant. Use this object to determine whether to reevaluate a user’s access to
your org for security purposes. You can check whether a user has never logged in, hasn’t been active for 90 days, has a frozen account,
or isn’t using multi-factor authentication. This object is available to Security Center subscribers in API version 53.0 and later.

TenantSecurityUserPerm
Stores information on permissions assigned to a user. Use this object to see which tenants a user is assigned to. This object is available
to Security Center subscribers in API version 53.0 and later.

TenantUsageEntitlement
Represents a data structure that contains information about the features or functionalities that a Salesforce org has access to. This
object is available in API version 28.0 and later.

Territory
Represents a flexible collection of accounts and users where the users have at least read access to the accounts, regardless of who
owns the accounts. Available if Sales Territories has been enabled. This object is available in API versions 7.0 to 52.0. Use Territory2
instead of Territory in API version 52.0 and later.

TerritoryMgmtObjectConfig
Represents territory management settings and defaults for a particular object. This object is available in API version 56.0 and later.

Territory2
Represents a sales territory. Available if Sales Territories has been enabled.

Territory2AlignmentLog
Represents the start and end status of a territory assignment rule run job. This object is available in API version 54.0 and later.

Territory2Model
Represents a territory model. Available if Sales Territories has been enabled.

Territory2ModelHistory
Represents the history of changes to the values in the fields on a territory model. Available if Sales Territories has been enabled.

Territory2ObjectExclusion
Represents the objects that aren’t included in territory assignment rule runs, even when they meet assignment rule criteria. This
object is available in API version 54.0 and later.

Territory2ObjSharingConfig
Represents the sharing access level of objects assigned to a particular territory. This object is available in API version 56.0 and later.

Territory2Type
Represents a category for territories (Territory2). Every Territory2 must have a Territory2Type. Available only if Sales Territories has
been enabled for your organization.


Standard Objects

TerritoryAdminAssignment
Represents designated team members who can administer specific territories and their descendants. This object is available in API
version 63.0 and later.

TestSuiteMembership
Associates an Apex class with an ApexTestSuite. This object is available in API version 36.0 and later.

ThirdPartyAccountLink
Represents the list of external users who authenticated using an authentication provider. This object is available in API version 32.0
and later.

ThreatDetectionFeedback
Represents feedback provided by a user about a Threat Detection event that occurred in your org. The feedback specifies whether
the event was malicious, suspicious, not a threat, or unknown. Each ThreatDetectionFeedback object is associated with one of these
Threat Detection storage events: ApiAnomalyEventStore, CredentialStuffingEventStore, ReportAnomalyEventStore, or
SessionHijackingEventStore. This object is available in API version 49.0 and later.

TimeSheet
Represents a schedule of a service resource’s time in Field Service or Workforce Engagement. This object is available in API v47.0 and
later.

TimeSheetEntry
Represents a span of time that a service resource spends on a field service task. This object is available in API version 47.0 and later.

TimeSlot
Represents a period of time on a specified day of the week during which work can be performed in Field Service, Salesforce Scheduler,
or Workforce Engagement. Operating hours consist of one or more time slots. This object is available in API version 38.0 and later.

TimeSlotHistory
Represents the history of changes made to tracked fields on a time slot. This object is available in API version 38.0 and later.

TodayGoal
Sets the quarterly sales goal on the performance chart. This object is available in API version 35.0 and later.

Topic
Represents a topic on a Chatter post or record. This object is available in API version 28.0 and later.

TopicAssignment
Represents the assignment of a topic to a specific feed item, record, or file. This object is available in API version 28.0 and later.

TopicLocalization
Represents the translated version of a topic name. Topic localization applies only to navigational and featured topics in Experience
Cloud sites. This object is available in API version 33.0 and later.

TopicUserEvent
Represents an action (such as comment, post, like, or share) made by a user on a topic. This object is available in API version 42.0
and later.

TopInsight
For internal use only.

TransactionSecurityPolicy
Represents a transaction security policy definition.

TransactionSecurityEventLog
Transaction Security event logs contain details about policy execution. Legacy transaction security policy details are supported in
API version 38.0 and later. Enhanced transaction security policy details are supported in API version 61.0 and later.


Standard Objects

Translation
The Translation object represents the languages enabled for translation in your Salesforce org. This object is available in API version
47.0 and later.

TravelMode
Represents a travel mode used for travel time calculations. The records include information about the type of transportation (such
as Car or Walking), whether a vehicle can take toll roads, and whether a vehicle is transporting hazardous materials. This object is
available in API version 54.0 and later.

TwoFactorInfo
Stores a user’s secret for multi-factor operations. Use this object when customizing multi-factor authentication in your organization.
(Note that multi-factor authentication was formerly called two-factor authentication.) This object is available in API version 32.0 and
later.

TwoFactorMethodsInfo
Stores information about which identity verification methods a user has registered. This object is available in API version 37.0 and
later.

TwoFactorTempCode
Stores information about a user’s temporary verification code for confirming their identity when logging in. This object is available
in API version 37.0 and later.

UiAgentInteractionEventLog
This log tracks client side interactions and events with the Agentforce panel. It is limited to Salesforce Lightning Experience, Salesforce
Mobile, and Conversation Preview within Agentforce Builder. This object is available in API version 65.0 and later.

UiFormulaCriterion
Represents a filter that helps define component visibility on a Lightning page. This object is available in API version 47.0 and later.

UiFormulaRule
Represents a set of one or more filters that define the conditions under which a component displays on a Lightning page. This object
is available in API version 47.0 and later.

UiTelemetryNavTmEventLog
UI Telemetry Navigation Timing events capture network performance metrics related to page navigation. The event extends from
[the UI Telemetry Resource Timing Event on page 2414 and includes requests initiated with either the Fetch API or the XMLHttpRequest](https://fetch.spec.whatwg.org/)
[API. This object is available in API version 64.0 and later.](https://xhr.spec.whatwg.org/)

UiTelemetryRsrcTmEventLog
UI Telemetry Resource Timing events capture network performance metrics related to loading an application’s resources. The event
[includes requests initiated with either the Fetch API or the XMLHttpRequest API. This object is available in API version 64.0 and later.](https://fetch.spec.whatwg.org/)

UndecidedEventRelation
Represents event participants (invitees or attendees) with the status `Not Responded` for a given event. This object is available
in API versions 29.0 and later.

UnifiedActivity
Represents an activity that is automatically captured from Einstein Activity Capture (EAC) or other activity data, such as calls, manually
logged tasks, and emails. This object consists of fields common to all types of activity-related objects such as Event, Task, EmailMessage,
VoiceCall, VideoCall, and so on. This object is available for reports and dashboards in the Winter ’24 release and later.

UnifiedActivityInsight
Represents an insight related to a unified activity. This object is available for reports and dashboards in the Winter ’24 release and
later.


Standard Objects

UnifiedActivityParticipant
Represents a participant in an activity. For example, a participant in a voice call is someone who initiated the call or someone who
received the call.This object is available for reports and dashboards in the Winter ’24 release and later.

UnifiedActivityRelation
Represents a relationship between an activity and a related record that’s a target or topic of the activity. For example, a related record
can be an opportunity, account, and so on. This object is available for reports and dashboards in the Winter ’24 release and later.

UnifiedActvtyInsightKeyword
Represents a keyword in a communication that triggered the activity insight. This object is available for reports and dashboards in
the Winter ’24 release and later.

UnifiedEmail
Represents an email that was captured or synced from an EmailMessage or Task record. This object is available for reports and
dashboards in the Winter ’24 release and later.

UnifiedEmailParticipant
Represents a participant in an email. This object is available for reports and dashboards in the Winter ’24 release and later.

UnifiedMeeting
Represents a meeting that was captured or synced from an Event record. This object is available for reports and dashboards in the
Winter ’24 release and later.

UnifiedMeetingParticipant
Represents a participant in a meeting. This object is available for reports and dashboards in the Winter ’24 release and later.

UnifiedTask
Represents a business activity such as a to-do item. This object is available for reports and dashboards in the Winter ’24 release and
later.

UnifiedTaskParticipant
Represents a participant in a task. This object is available for reports and dashboards in the Winter ’24 release and later.

UnifiedVideoCall
Represents a video call that is captured or synced from the VideoCall or Task record. This object is available for reports and dashboards
in the Winter ’24 release and later.

UnifiedVideoCallParticipant
Represents a participant in a video call. This object is available for reports and dashboards in the Winter ’24 release and later.

UnifiedVoiceCall
Represents a voice call that is captured or synced from a VoiceCall or Task record. This object is available for reports and dashboards
in the Winter ’24 release and later.

UnifiedVoiceCallParticipant
Represents a participant in a voice call. This object is available for reports and dashboards in the Winter ’24 release and later.

UnitOfMeasure
Defines the units and systems of units used to express and account for quantities. This object is available in API version 61.0 and
later.

UriEventLog
URI events contain details about user interaction with the web browser UI. This object is available in API version 61.0 and later.

UsageImpactFactor
Represents a collection of fields to set up the Usage Impact Factors used across jurisdictions and programs.This object is available
in API version 58.0 and later.


Standard Objects

UsageImpactGroup
Represents a collection of fields to set up the Usage Impact Groups used across jurisdictions and programs. This object is available
in API version 58.0 and later.

UsageImpactGroupFactor
Represents a junction between an Usage Impact Group version and Usage Impact Factor. This object is available in API version 58.0
and later.

UsageImpactGroupPgmMeasure
Represents a junction between the program, product, and Usage Impact Group version. This object is available in API version 58.0
and later.

UsageImpactGroupVersion
Represents a collection of fields to set up the versions of Usage Impact Groups. This object is available in API version 58.0 and later.

User
Represents a user in your organization.

UserAccessChange
Represents a change related to user access. This object is available in API version 57.0 and later.

UserAccessPolicy
Represents a user access policy. This object is available in API version 57.0 and later.

UserAccountTeamMember
Represents a User on the default account team of another User.

UserAppInfo
Stores the last Lightning app logged in to. If the user hasn’t logged into Salesforce or if the user lost access to the last accessed app,
the UserAppInfo object stores a Null value. This object is available in API version 38.0 and later.

UserAppMenuCustomization
Represents an individual user’s settings for items in the app menu or App Launcher. This object is available in API version 35.0 and
later.

UserAppMenuItem
Represents the organization-wide settings for items in the app menu or App Launcher that the requesting user has access to in
Setup. This object is available in API version 35.0 and later.

UserAuthCertificate
Represents a user authentication certificate in your org. A user certificate is a unique PEM-encoded X.509 digital certificate to
authenticate individual users to your org. This object is available in API version 45.0 and later.

UserConfigTransferButton
Represents the association between a Chat configuration and a live chat button. This association allows users associated with a
specific configuration to transfer chats to a button queue.

UserConfigTransferSkill
Represents the association between a Chat configuration and a skill. This association allows users associated with a specific configuration
to transfer chats to agents who have that skill.

UserCustomBadge
Represents a custom badge for a user. This object is available in API version 38.0 and later.

UserCustomBadgeLocalization
Represents the translated version of a custom badge for a user. This object is available in API version 38.0 and later.


Standard Objects

UserDailyMetric
Represents the daily engagement metrics for a user. This object is available in API version 52.0 and later.

UserDailyMetricOwnerSharingRule
Represents the rules for sharing the user daily metric with users other than the owner.

UserDefinedLabel
Represents a label created by a user to help organize, track, and find records. This object is available in API version 61.0 and later.

UserDefinedLabelAssignment
Represents a relationship between a record label and the item the user assigned it to. This object is available in API version 61.0 and
later.

UserDevice
Represents information unique to a device. Available in API version 43.0 and later.

UserDeviceApplication
Represents information on applications installed on a device that is accessing Salesforce. Available in API version 43.0 and later.

UserDeviceHistory
Represents tracking information on the UserDevice sObject. This object is available in API version 50.0 and later.

UserEmailCalendarSync
Represents the user assignments of an Einstein Activity Capture configuration. This object is available in API version 49.0 and later.

UserEmailPreferredPerson
Represents a mapping for a user’s preferred record for an email address when multiple records match an email field.This object is
available in API version 44.0 and later.

UserEmailPreferredPersonShare
Represents a sharing entry on a UserEmailPreferredPerson object. Sharing is not customizable for UserEmailPreferredPerson records.This
object is available in API version 44.0 and later.

UserLicense
Represents a user license in your organization. A user license entitles a user to specific functionality and determines the profiles and
permission sets available to the user.

UserListView
Represents the customizations a user made to a list view. This object is available in API version 32.0 and later.

UserListViewCriterion
Represents the criterion for a user’s customized list view. The criterion consists of the filters or sort order a user added to a list view
for the Salesforce Mobile app. This object is available in API version 32.0 and later.

UserLocationAssignment
Represents the assignment between a location and a user. This object is available in API version 57.0 and later.

UserLogin
Represents the settings that affect a user’s ability to log into an organization. To access this object, you need the
`UserPermissions.ManageUsers` permission. This object is available in API version 29.0 and later.

UserMembershipSharingRule
Represents the rules for sharing user records from a source group to a target group. A user record contains details about a user. Users
who are members of the source group can be shared with members of the target group. The source and target groups can be based
on roles, portal roles, public groups, or territories. This object is available in API version 26.0 and later.

UserMonthlyMetric
Represents the monthly engagement metrics for a user. This object is available in API version 52.0 and later.


Standard Objects

UserMonthlyMetricOwnerSharingRule
Represents the rules for sharing the user monthly metric with users other than the owner.

UserPackageLicense
Represents a license for an installed managed package, assigned to a specific user. This object is available in API version 31.0 and
later.

UserPermissionAccess
Represents the permissions accessibility for a current user. Available in API version 41.0 and later.

UserPrioritizedRecord
Represents records that Pipeline Inspection, Account Intelligence, Contact Intelligence, and Lead Intelligence users flag as important
for tracking in pipeline and intelligence views and filters. This object is available in API version 53.0 and later.

UserPreference
Represents a functional preference for a specific user in your organization.

UserProfile
Represents a Chatter user profile.

UserProvAccount
Represents information that links a Salesforce user account with an account in a third-party (target) system, such as Google, for users
of connected apps with Salesforce user provisioning enabled. This object is available in API version 33.0 and later.

UserProvAccountStaging
Temporarily stores user account information while a user completes the User Provisioning Wizard. This information that is stored in
the UserProvAccount object when you click the button to collect and analyze accounts on the target system.

UserProvMockTarget
Represents an entity for testing user data before committing the data to a third-party system for user provisioning.

UserProvisioningConfig
Represents information for a flow to use during a user provisioning request process, such as the attributes for an update. This object
is available in API version 34.0 and later.

UserProvisioningLog
Represents messages generated during the process of provisioning users for third-party applications. This object is available in API
version 33.0 and later.

UserProvisioningRequest
Represents an individual provisioning request to create, update, or delete a single user account in a third-party service system (or
another Salesforce organization). This object is available in API version 33.0 and later.

UserRecordAccess
Represents a user’s access to a set of records. This object is read only and is available in API version 24.0 and later. This object doesn’t
consider whether a user’s access is blocked by a restriction rule.

UserRelatedRecordContent
Represents the link between a managed content record, an account, event, or opportunity record, and a user record. This object is
reserved for future use.

UserRole
Represents a user role in your organization.

UserServicePresence
Represents a presence user’s real-time presence status. This object is available in API version 32.0 and later.


Standard Objects

UserSetupEntityAccess
Represents the enabled custom permissions of the running user. This object is available in API version 48.0 and later.

UserShare
Represents a sharing entry on a user record. This object is available in API version 26.0 and later.

UserSharedFeature
For internal use only.

UserTeamMember
Represents a single User on the default opportunity team of another User.

UserTerritory
Represents a User who has been assigned to a Territory.

UniqueQueryEventLog
Unique Query events capture specific search queries (SOQL), filter IDs, and report IDs that are processed, along with the underlying
database queries (SQL). This object is available in API version 65.0 and later.

UserTerritory2Association
Represents an association (by assignment) between a territory and a user record. Available only if Sales Territories has been enabled.

UserTerritory2AssocLog
Represents a log of when a user is assigned and unassigned from a territory. This object is available in API version 57.0 and later.

UserUIPreference
Represents user preferences for Salesforce components. This object is available in API version 63.0 and later.

UserWorkList
Represents a list of work items in the My List tab for Sales Engagement users.

UserWorkListItem
Represents an individual work item in the My List tab for Sales Engagement users.

VendorCallCenterStatusMap
Stores a mapping between a call center vendor agent status and a Salesforce presence status for an associated call center. This object
is available in API version 54.0 and later.

VerificationHistory
Represents the past six months of your org users’ attempts to verify their identity. This object is available in API version 36.0 and later.

VisualforceAccessMetrics
Represents summary statistics for Visualforce pages.

VisualforceRequestEventLog
Visualforce Request events contain details of Visualforce requests. Requests can originate from the browser (UI). This object is available
in API version 61.0 and later.

VideoCall
Represents a video call. One `VideoCall` record can be related to several `VideoCallRecording` records — for example, a
video call can have several video recordings and a transcript. As well, one video call record can be associated with several video call
participant records. This object is available in API version 51.0 and later.

VideoCallInsight
Represents the video call insight data associated with a video call. Each record represents the call insight of a specific recording or
transcript within a call. This object is available in API version 66.0 and later.


Standard Objects

VideoCallInsightAction
Represents a suggested follow-up action derived from a video call insight. VideoCallInsightAction manages recommended steps—such
as sending an email, creating a task, or scheduling a meeting—that address specific moments, including competitor mentions,
pricing discussions, or objections. This object is available in API version 66.0 and later.

VideoCallInsightReason
Represents the video call insight reason that contains the insight keyword, insight moments associated with a keyword, and the
number of keyword occurrences. This object is available in API version 66.0 and later.

VideoCallParticipant
Represents a participant in a video call. Participant information can come from the video call provider (for example, Zoom), or
Salesforce. This object is available in API version 51.0 and later.

VideoCallRecording
Represents a recording from a video call, such as a video recording, a voice recording, or a transcript. Video call recordings aren’t
saved in Salesforce. This object is available in API version 51.0 and later.

VideoCallRecordingStructure
Represents the structure of a video call recording, having relation to a video call participant, speaking order, start offset, and end
offset. This object is available in API version 65.0 and later.

VoiceCall
Represents a call in Salesforce Voice, Sales Dialer, or other supported voice connectors. For Salesforce Voice, this can be a phone or
Voice over Internet Protocol (VoIP) call. This object is available in API version 40.0 and later.

VoiceCallInsight
Represents the voice call insight data associated with a voice call. Each record represents the call insight of a specific recording or
transcript within a call. This object is available in API version 66.0 and later.

VoiceCallInsightAction
Represents a suggested follow-up action derived from a voice call insight. VoiceCallInsightAction manages recommended steps—such
as sending an email, creating a task, or scheduling a meeting—that address specific moments, including competitor mentions,
pricing discussions, or objections. This object is available in API version 66.0 and later.

VoiceCallInsightReason
Represents the voice call insight reason that contains the insight keyword, insight moments associated with a keyword, and the
number of keyword occurrences. This object is available in API version 66.0 and later.

VoiceCallMetrics
Represents metrics for a VoiceCall lifecycle event, aggregated daily. This object is available in API version 56.0 and later.

VoiceCallList
Represents a prioritized list of numbers to call.

VoiceCallListItem
Represents a single phone number in a prioritized call list.

VoiceCallQualityFeedback
Represents feedback given by a Sales Dialer user about the quality of a VoiceCall .

VoiceCallRecording
Represents a call recording in Salesforce Voice and Sales Dialer. Call recordings for Salesforce Voice with Amazon Connect and for
Salesforce Voice with Partner Telephony from Amazon Connect are stored in S3 buckets on your Amazon Web Services (AWS)
account and can be accessed via AWS. Call recordings for Sales Dialer are saved as files in Salesforce.

VoiceCoaching
Represents a call that is using call monitoring.


Standard Objects

VoiceLocalPresenceNumber
Represents a phone number with the same area code as the person who’s being called.

VoiceMailContent
Represents a voicemail message left by a caller to the context user.

VoiceMailGreeting
Represents a custom greeting message that plays upon reaching a user’s voicemail. This object is available in API version 41.0 and
later.

VoiceMailGreeting2
Represents information about a voicemail message that reps can drop during outbound customer calls, or set to play when they're
unable to take calls from customers. This object is available in API version 67.0 and later.

VoiceMailGreeting2Rep
Represents information about the voicemail message and its associated service rep. This object is available in API version 67.0 and
later.

VoiceMailMessage
Represents a prerecorded voicemail message.

VoiceOrgSetting
Represents the org's customized voice settings. This object is available in API version 46.0 and later.

VoiceUserLine
Represents a user’s forwarding phone number.

VoiceUserPreferences
Represents the number the user displays when making outbound calls. This object is available in API version 41.0 and later.

VoiceVendorInfo
Represents information about the Salesforce Voice or Sales Dialer provider’s vendor.

VoiceVendorLine
Represents a user’s phone number reserved with the vendor.

Vote
Represents a vote that a user has made on a Knowledge Article, Idea, or Reply.

WarrantyTerm
Represents warranty terms defining the labor, parts, and expenses covered, along with any exchange options, provided to rectify
issues with products. This object is available in API version 50.0 and later.

WaveAutoInstallRequest
Provides access to the concrete object that represents a CRM Analytics auto-install request. The auto-install request tracks the progress
of CRM Analytics applications created from CRM Analytics templates by the automated process user. This object is available in API
version 38.0 and later.

WebCart
Represents an online shopping cart for a store built with B2B Commerce or D2C Commerce, with total amounts for products, shipping
and handling, and taxes. This object is available in API version 49.0 and later.

WebCartAdjustmentBasis
Coupons that trigger promotions for the cart. When a customer tries to add a coupon to the cart, the store looks for promotions
associated with the coupon. If a promotion results in a price adjustment, a WebCartAdjusmentBasis record is created. This object is
available in API version 54.0 and later.


Standard Objects

WebCartAdjustmentGroup
Group of price adjustments for a cart. This object is available in API version 52.0 and later.

WebCartHistory
WebCartHistory represents the history of changes to the values in the fields of the `WebCart` object.

WebLink
Represents a custom link to a URL or Scontrol.

WebLinkLocalization
Represents the translated value of the field label for a custom link to a URL or s-control when the Translation Workbench is enabled
for your organization.

WebStore
Represents a B2B or D2C store. This object is available in API version 49.0 and later.

WebstoreBuyerGroup
Associates a webstore with a buyer group. Supports dynamically changing locales when buyers shop in orgs that are enabled for
multiple languages and currencies. This object is available in API version 58.0 and later.

WebStoreCatalog
Represents the collection of products associated with a store. This object is available in API version 49.0 and later.

WebStoreInventorySource
Used to configure the inventory source for a webstore. This object is available in API version 57.0 and later.

WebStoreMessageContent
Represents the assocation of a managed content message record in CMS to a web store, along with other attributes that specify the
application and intent of the message content. This object is available in API version 61.0 and later.

WebStoreNetwork
Represents the relationship between a web store and an experience site. This object is available in API version 49.0 and later.

WebStorePricebook
Represents a store price book used in Lightning B2B Commerce. This object is available in API version 48.0 and later.

WebStoreSearchProdSettings
Search settings for a WebStore product search. This object is available in API version 47.0 and later.

WebStoreShare
Represents a sharing entry on a B2B or D2C store. This object is available in API version 45.0 and later.

Wishlist
Represents a buyer-created list of `WishlistItem` s in a store that’s built with B2B Commerce on Lightning. Available in API version
49.0 and later.

WishlistItem
Represents an item on a `Wishlist` in a store built with B2B Commerce for Lightning. Available in API version 49.0 and later.

WorkAccess
Used to grant or restrict user access to give badge definitions. Each badge definition record must have one WorkAccess record.

WorkAccessShare
Used to control Givers of WorkBadgeDefinition records.

WorkBadge
Represents information about who the badge was given to and which badge was given. A WorkBadge record is created for each
recipient of a WorkBadgeDefinition.


Standard Objects

WorkBadgeDefinition
Represents the attributes of a badge including the badge name, description, and image. Each WorkBadge record must have a lookup
to a WorkBadgeDefinition since badge attributes (like badge name) are derived from the WorkBadgeDefinition object.

WorkCapacityAvailability
Represents the available work capacity for a specific time and service territory. This object is available in API version 59.0 and later.

WorkCapacityLimit
Represents the capacity limit in a specific service territory for a workstream or for the whole service territory in a given period. This
object is available in API version 59.0 and later.

WorkCapacityUsage
Represents the capacity usage in a specific service territory for a workstream or for the whole service territory in a given period. This
object is available in API version 59.0 and later.

WorkCoaching
Represents a single coaching relationship between two users. One of the users is defined as the coach and the other is defined as a
coachee. WorkCoaching is feed-enabled so there is a private feed available to the coach and coachee.

WorkDemographic
Represents the field values used to specify slices in the workload forecasting and capacity planning. This object is available in API
version 49.0 and later.

WorkFeedback
Represents the answer to a question that a person was asked via a feedback request. Also used to store offered feedback without
linking it to a particular question.

WorkFeedbackQuestion
Represents a free-form text type or multiple choice question within a set of questions.

WorkFeedbackQuestionSet
Represents a set of questions being asked. The question set is used to link all the individual requests where different recipients were
asked the same set of questions on the same subject.

WorkFeedbackRequest
Represents a single feedback request on a subject or topic (question) to a single recipient in the feedback application. In the case of
offered feedback, WorkFeedbackRequest represents feedback that is offered about a subject. In the performance application,
WorkFeedbackRequest represents a request for feedback on a set of questions from a question set, on a subject—for the recipient
to complete and submit.

WorkforceCapacity
Represents the time series for actual or forecasted workforce allocation. This object is available in API version 51.0 and later.

WorkforceCapacityUnit
Represents the number of resources allocated or needed for a specific set of work items at a timestamp within a specific duration.
This object is available in API version 51.0 and later.

WorkGoal
Represents the components of a goal, such as its description and associated metrics. This object has been deprecated as of API
version 35.0. Use the Goal object to query information about WDC goals.

WorkGoalCollaborator
Represents collaborators on a WorkGoal object. This doesn’t include WorkGoal followers, which is handled by Chatter Feed Follow
functionality. This object has been deprecated as of API version 35.0. Use the Goal object to query information about WDC goals.

WorkGoalCollaboratorHistory
Represents the history of changes to the values in the fields in a WorkGoalCollaborator object. Access is read-only.


Standard Objects

WorkGoalHistory
Represents the history of changes to the values in the fields of a WorkGoal. Access is read-only. This object has been deprecated as
of API version 35.0. Use the GoalHistory object to query historical information for WDC goals.

WorkGoalLink
Represents the relationship between two goals (many to many relationship). This object has been deprecated as of API version 35.0.
Use the GoalLink object to query information about the relationship between two WDC goals.

WorkGoalShare
Represents a sharing entry on a WorkGoal object. This object has been deprecated as of API version 35.0. Use the GoalShare object
to query information about sharing for WDC goals.

Workload
Represents the time series for work item volume and average handle time from aggregation and forecasting processes. This object
is available in API version 49.0 and later.

WorkloadUnit
Represents the number of work items and average handle time in a specific time interval. This object is available in API version 49.0
and later.

WorkOrder
Represents field service work to be performed for a customer. This object is available in API version 36.0 and later.

WorkOrderHistory
Represents the history of changes made to tracked fields on a work order. This object is available in API version 36.0 and later.

WorkOrderLineItem
Represents a subtask on a work order in field service. This object is available in API version 36.0 and later.

WorkOrderLineItemHistory
Represents the history of changes made to tracked fields on a work order line item. This object is available in API version 36.0 and
later.

WorkOrderLineItemStatus
Represents a possible status of a work order line item in field service.

WorkOrderShare
Represents a sharing entry on a work order. This object is available in API version 36.0 and later.

WorkOrderStatus
Represents a possible status of a work order in field service.

WorkPerformanceCycle
Represents feedback that is gathered to assess the performance of a specific set of employees.

WorkPlan
Represents a work plan for a work order or work order line item. This object is available in API version 52.0 and later.

WorkPlanSelectionRule
Represents a rule that selects a work plan for a work order or work order line item. This object is available in API version 52.0 and
later.

WorkPlanTemplate
Represents a template for a work plan. This object is available in API version 52.0 and later.

WorkPlanTemplateEntry
Represents an object that associates a work step template with a work plan template. This object is available in API version 52.0 and
later.


### Standard Objects AbnExperiment

WorkReward
Used to store reward codes tied to a Reward Fund. Reward Funds must have at least one WorkReward record.

WorkRewardFund
Represents a Reward Fund and describes the Reward Fund attributes.

WorkRewardFundType
Represents the type of WorkRewardFund object.

WorkStep
Represents a work step in a work plan. This object is available in API version 52.0 and later.

WorkStepStatus
Represents a picklist for a status category on a work step. This object is available in API version 52.0 and later.

WorkStepTemplate
Represents a template for a work step. This object is available in API version 52.0 and later.

WorkThanks
Represents the source and message of a thanks post.

WorkType
Represents a type of work to be performed in Field Service and Lightning Scheduler. Work types are templates that can be applied
to work order or work order line items. This object is available in API version 38.0 and later.

WorkTypeGroup
Represents a grouping of work types used to categorize types of appointments available in Lightning Scheduler, or to define
scheduling limits in Field Service. This object is available in API version 45.0 and later.

WorkTypeGroupMember
Represents the relationship between a work type and the work type group it belongs to. This object is available in API version 45.0
and later.

### AbnExperiment

Represents an A/B/n experiment that's used with Marketing Cloud Next content, Experience Cloud websites, and platform automations.
This object is available in API version 63.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
DataSpaceId

```

**Type**
reference

**Properties**
Filter, Group, Sort


Standard Objects AbnExperiment

**Field** **Details**

**Description**
Unique identifier that refers to the data space where an experiment's resources originate.
Required.

This field is a relationship field.

**Relationship Name**
DataSpace

**Refers To**
DataSpace

```
Description

DeveloperName

LastAnalyzed

LastReferencedDate

LastViewedDate

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Text description of the experiment. Optional.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
System or user-generated API name for the experiment. Required.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Time and date of last analysis.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp that indicates the last time an experiment was referenced by another resource.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects AbnExperiment

**Field** **Details**

**Description**
Timestamp that indicates the last time a user viewed the experiment.

```
Name

PersonalizationSchemaEnum

PersonalizationSchemaId

PrimaryMetricId

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Text label that identifies the experiment. Required.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Picklist value that indicates the type of personalization schema, which is related to where a
personalization decision is created.

Possible values are:

**•** `DecisionDefined`

**•** `ExperienceVariation`

**•** `FlowPath`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier that refers to the schema that’s related to the experiment.

This field is a relationship field.

**Relationship Name**
PersonalizationSchema

**Refers To**
PersonalizationSchema

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier that refers to engagement signal metrics, which are used to measure an
experiment.


Standard Objects AbnExperiment

**Field** **Details**

This field is a polymorphic relationship field.

**Relationship Name**
PrimaryMetric

**Refers To**
EngagementSignalCmpndMetric, EngagementSignalMetric

```
ProfileDataGraphId

ScheduleFrequencyInMinutes

Source

SourceRecordId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier that refers to the profile data graph that’s used.

This field is a relationship field.

**Relationship Name**
ProfileDataGraph

**Refers To**
DataGraph

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of minutes that defines when personalized content can be made available.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates where the experiment was created.

Possible values are:

**•** `BlockBuilder` —CMS content editors

**•** `ExperienceBuilder` —Experience Site Builder

**•** `FlowBuilder`

**•** `PersonalizationApp`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects AbnExperiment

**Field** **Details**

**Description**
Unique identifier that refers to the specific record that contains the experiment.

This field is a polymorphic relationship field.

**Relationship Name**
SourceRecord

**Refers To**
FlowRecordElement, ManagedContent

```
StartedDate

State

Status

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp that indicates when the experiment began or is scheduled to begin.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Picklist value that indicates the current state of the experiment.

Possible values are:

**•** `Archived`

**•** `Created`

**•** `Started`

**•** `Stopped`

The default value is `Created` .

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Picklist value that indicates the current status of the experiment while an action is being
performed.

Possible values are:

**•** `Active`

**•** `CreateError`

**•** `DeleteError`

**•** `Deleting`


### Standard Objects AbnExperimentCohort

**Field** **Details**

**•** `EditError`

**•** `Processing`

The default value is `Processing` .

```
StoppedDate

WinnerSelectionMode

```

Associated Objects

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp that indicates when the experiment ended or is scheduled to end.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Possible values are:

**•** `Automatic`

**•** `Manual`

The default value is `Manual` .

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AbnExperimentChangeEvent on page 68**
Change events are available for the object.

**AbnExperimentFeed on page 55**
Feed tracking is available for the object.

**AbnExperimentHistory on page 63**
History is available for tracked fields of the object.

**AbnExperimentOwnerSharingRule on page 65**
Sharing rules are available for the object.

**AbnExperimentShare on page 67**
Sharing is available for the object.

### AbnExperimentCohort

Represents the specified audience that's participating in an A/B/n experiment. This object is available in API version 63.0 and later.


Standard Objects AbnExperimentCohort

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
AbnExperimentId

AllocationWeight

CurrencyIsoCode

DataSpaceId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Unique identifier that refers to a related experiment.

This field is a relationship field.

**Relationship Name**
AbnExperiment

**Relationship Type**
Parent-detail

**Refers To**
AbnExperiment (the parent object)

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Percentage of an audience to experience the selected part of the experiment.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Three letter ISO currency codes for supported currencies. Optional.

Possible values are:

**•** `USD` —U.S. Dollar

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects AbnExperimentCohort

**Field** **Details**

**Description**
Unique identifier that refers to the data space where an experiment cohort's resources
originate. Required.

This field is a relationship field.

**Relationship Name**
DataSpace

**Refers To**
DataSpace

```
Description

DeveloperName

IsControl

IsFallThrough

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Text description of the experiment.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
System or user-generated API name for the experiment. Required.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Whether the cohort is used as the control group that performance is checked against.

The default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this cohort captures users who don't meet the criteria for other cohorts
in the experiment. When `true`, this cohort serves as the fallback option. When `false`,
users must explicitly qualify for this cohort. The default value is `false` .


Standard Objects AbnExperimentCohort

**Field** **Details**

```
Name

PersonalizerId

```

Usage

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Text label that identifies the experiment cohort. Required.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier that refers to the personalizer that’s related to the experiment cohort.

This field is a relationship field.

**Relationship Name**
Personalizer

**Refers To**
PersonalizationRecommender

Use this object to describe experiment cohorts or to change allocation weights.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AbnExperimentCohortChangeEvent on page 68**
Change events are available for the object.

**AbnExperimentCohortFeed on page 55**
Feed tracking is available for the object.

**AbnExperimentCohortHistory on page 63**
History is available for tracked fields of the object.

**AbnExperimentCohortOwnerSharingRule on page 65**
Sharing rules are available for the object.

**AbnExperimentCohortShare on page 67**
Sharing is available for the object.


### Standard Objects AcceptedEventRelation AcceptedEventRelation Represents event participants (invitees or attendees) with the status Accepted for a given event.

This object is available in API versions 29.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
EventId

RelationId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the ID of the event.

This is a relationship field.

**Relationship Name**
Event

**Relationship Type**
Lookup

**Refers To**
Event

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the ID of the invitee.

This is a polymorphic relationship field.

**Relationship Name**
Relation

**Relationship Type**
Lookup

**Refers To**
Calendar, Contact, Lead, User


### Standard Objects Account

**Field Name** **Details**

```
RespondedDate

Response

Type

```

Usage

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Indicates the most recent date and time when the invitee accepted an invitation
to the event.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the content of the response field. Label is `Comment` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates whether the invitee is a user, lead or contact, or resource.

**Query invitees who have accepted an invitation to an event**

```
  SELECT eventId, type, response FROM AcceptedEventRelation WHERE eventid='00UTD000000ZH5LA'

```

SEE ALSO:

DeclinedEventRelation

UndecidedEventRelation

### Account

Represents an individual account, which is an organization or person involved with your business (such as customers, competitors, and
partners).

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `merge()`,
`query()`, `retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects Account

Special Access Rules

Experience Cloud site or Customer Portal users can access their own accounts and any account shared with them.

Fields

**Field Name** **Details**

```
AccountNumber

AccountSource

ActivityMetricId

ActivityMetricRollupId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Account number assigned to this account (not the unique, system-generated ID assigned
during creation). Maximum size is 40 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The source of the account record. For example, _`Advertisement`_ or _`Trade Show`_ .
The source is selected from a picklist of available values, which are set by an administrator.
Each picklist value can have up to 40 characters.

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


Standard Objects Account

**Field Name** **Details**

**Description**
When Einstein Activity Capture with Activity Metrics is enabled, the ID of the related activity
metric rollup.

This field is a relationship field.

**Relationship Name**
ActivityMetricRollup

**Refers To**
ActivityMetricRollup

```
AnnualRevenue

BillingAddress

BillingCity

BillingCountry

BillingCountryCode

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Estimated annual revenue of the account.

**Type**
address

**Properties**
Filter, Nillable

**Description**
The compound form of the billing address. Read-only. For details on compound address
fields, see Address Compound Fields.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the billing address of this account. Maximum size is 40 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the billing address of this account. Maximum size is 80 characters.

**Type**
picklist


Standard Objects Account

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO country code for the account’s billing address.

```
BillingGeocodeAccuracy

BillingLatitude

BillingLongitude

BillingPostalCode

BillingState

```

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

**Description**
Used with `BillingLatitude` to specify the precise geolocation of a billing address.
Acceptable values are numbers between –180 and 180 with up to 15 decimal places. See
Compound Field Considerations and Limitations for details on geolocation compound fields.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the billing address of this account. Maximum size is 20 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects Account

**Field Name** **Details**

**Description**
Details for the billing address of this account. Maximum size is 80 characters.

```
BillingStateCode

BillingStreet

ChannelProgramLevelName

ChannelProgramName

CleanStatus

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO state code for the account’s billing address.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Street address for the billing address of this account.

**Type**
string

**Properties**
Group, Nillable

**Description**
Read only. Name of the channel program level the account has enrolled. If this account has
enrolled more than one channel program level, the oldest channel program name is displayed.

**Type**
string

**Properties**
Group, Nillable

**Description**
Read only. Name of the channel program the account has enrolled. If this account has enrolled
more than one channel program, the oldest channel program name is displayed.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the record’s clean status as compared with Data.com..

Possible values are:

**•** `Acknowledged` The label on the account record detail page is `Reviewed` .


Standard Objects Account

**Field Name** **Details**

**•** `Different`

**•** `Inactive`

**•** `Matched` —The label on the account record detail page is `In Sync` .

**•** `NotFound`

**•** `Pending` The label on the account record detail page is `Not Compared` .

**•** `SelectMatch`

**•** `Skipped`

```
CommerceCustomerReference

CommerceGroupReference

CommerceOrganizationReference

ConnectionReceivedId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The external Commerce ID of the individual. To update or create field values, you need the
Manage Shopper Profile Sync System Fields user permission. Available in API version 67.0
and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The external name of the Commerce customer group. To update or create field values, you
need the Manage Shopper Profile Sync System Fields user permission. Available in API version
67.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The external organization ID of the Commerce instance. To update or create field values, you
need the Manage Shopper Profile Sync System Fields user permission. Available in API version
67.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the PartnerNetworkConnection that shared this record with your organization. This
field is available if you enabled Salesforce to Salesforce.


Standard Objects Account

**Field Name** **Details**

```
ConnectionSentId

Description

DunsNumber

Fax

Industry

```

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
textarea

**Properties**
Create, Nillable, Update

**Description**
Text description of the account. Limited to 32,000 KB.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Data Universal Numbering System (D-U-N-S) number is a unique, nine-digit number
assigned to every business location in the Dun & Bradstreet database that has a unique,
separate, and distinct operation. D-U-N-S numbers are used by industries and organizations
around the world as a global standard for business identification and tracking. Maximum
size is 9 characters. This field is available on business accounts, not person accounts.

Note: This field is only available to organizations that use Data.com Prospector or
Data.com Clean.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Fax number for the account.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects Account

**Field Name** **Details**

**Description**
An industry associated with this account. For example, `Biotechnology` . Maximum size
is 40 characters.

```
IsBuyer

IsCustomerPortal

IsPartner

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates that the account is enabled as a buyer for Lightning B2B Commerce. The default
value is `false` . This field is available in API version 48.0 and later.

Note: This field is only available to organizations that have the B2B Commerce license
enabled.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the account has at least one contact enabled to use the org's Experience
Cloud site or Customer Portal ( `true` ) or not ( `false` ). This field is available if Customer
Portal is enabled OR digital experiences is enabled.

If your org is enabled to use Content Security Policy (CSP) features, then this field is visible
on the Account object even if those features are later disabled.

If you change this field's value from `true` to `false`, you can disable up to 100 Experience
Cloud site or Customer Portal users associated with the account and permanently delete all
of the account's site roles and groups. You can't restore deleted site roles and groups.

Exclude this field when merging accounts.

This field can be updated in API version 16.0 and later.

Tip: We recommend that you update up to 50 contacts simultaneously when
changing the accounts on contacts enabled for an Experience Cloud site. We also
recommend that you make this update after business hours.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the account has at least one contact enabled to use the org's partner
portal ( `true` ) or not ( `false` ). This field is available if partner relationship management


Standard Objects Account

**Field Name** **Details**

(partner portal) is enabled OR digital experiences is enabled and you have partner portal
licenses.

If you change this field's value from `true` to `false`, you can disable up to 15 partner
portal users associated with the account and permanently delete all of the account's partner
portal roles and groups. You can't restore deleted partner portal roles and groups.

Disabling a partner portal user in the Salesforce user interface or the API doesn’t change this
field's value from `true` to `false` .

Even if this field's value is `false`, you can enable a contact on an account as a partner
portal user via the API.

Exclude this field when merging accounts.

This field can be updated in API version 16.0 and later.

Tip: We recommend that you update up to 50 contacts simultaneously when
changing the accounts on contacts enabled for an Experience Cloud site. We also
recommend that you make this update after business hours.

```
IsPersonAccount

IsPriorityRecord

Jigsaw

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read only. Label is **Is Person Account** . Indicates whether this account has a record type of
Person Account ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Defaulted on create, Group

**Description**
Shows whether the user has marked the account as important ( _`True`_ ) or not ( _`False`_ ). The
default value is `false` . Available in API version 60.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
References the ID of a company in Data.com. If an account has a value in this field, it means
that the account was imported from Data.com. If the field value is `null`, the account was
not imported from Data.com. Maximum size is 20 characters. Available in API version 22.0
and later. Label is **Data.com Key** . This field is available on business accounts, not person
accounts.


Standard Objects Account

**Field Name** **Details**

Important: The `Jigsaw` field is exposed in the API to support troubleshooting for
import errors and reimporting of corrected data. Do not modify the value in the
`Jigsaw` field.

```
JigsawCompanyId

LastActivityDate

LastReferencedDate

LastViewedDate

MasterRecordId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the company in reference to `Jigsaw` .

Important: The `Jigsaw` field is exposed in the API to support troubleshooting for
import errors and reimporting of corrected data. Don’t modify the value in the
`Jigsaw` field.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Value is one of the following, whichever is the most recent:

**•** Due date of the most recent event logged against the record.

**•** Due date of the most recently closed task associated with the record.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for example,
through a list view or related record.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view ( `LastReferencedDate` ), but
not viewed it.

**Type**
reference


Standard Objects Account

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
If this object was deleted as the result of a merge, this field contains the ID of the record that
was kept. If this object was deleted for any other reason, or has not been deleted, the value
is `null` .

This is a relationship field.

**Relationship Name**
MasterRecord

**Relationship Type**
Lookup

**Refers To**
Account

```
NaicsCode

NaicsDesc

Name

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The six-digit North American Industry Classification System (NAICS) code is the standard
used by business and government to classify business establishments into industries,
according to their economic activity for the purpose of collecting, analyzing, and publishing
statistical data related to the U.S. business economy. Maximum size is 8 characters. This field
is available on business accounts, not person accounts.

Note: This field is only available to organizations that use Data.com Prospector or
Data.com Clean.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an org’s line of business, based on its NAICS code. Maximum size is 120
characters. This field is available on business accounts, not person accounts.

Note: This field is only available to organizations that use Data.com Prospector or
Data.com Clean.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects Account

**Field Name** **Details**

**Description**
Required. Label is **Account Name** . Name of the account. Maximum size is 255 characters.
If the account has a record type of Person Account:

**•** This value is the concatenation of the `FirstName`, `MiddleName`, `LastName`, and
`Suffix` of the associated person contact.

**•** You can't modify this value.

```
NumberOfEmployees

OperatingHoursId

OwnerId

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Label is **Employees** . Number of employees working at the company represented by this
account. Maximum size is eight digits.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The operating hours associated with the account. Available only if Field Service is enabled.

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
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who currently owns this account. Default value is the user logged in to
the API to perform the create.

If you have set up account teams in your org, updating this field has different consequences
depending on your version of the API:

**•** For API version 12.0 and later, sharing records are kept, as they are for all objects.

**•** For API version before 12.0, sharing records are deleted.


Standard Objects Account

**Field Name** **Details**

**•** For API version 16.0 and later, users must have the “Transfer Record” permission in order
to update (transfer) account ownership using this field.

This is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

```
Ownership

ParentId

PersonActionCadenceAssigneeId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Ownership type for the account, for example Private, Public, or Subsidiary.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the parent object, if any.

This is a relationship field.

**Relationship Name**
Parent

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
field is available in API version 47.0 and later when the Sales Engagement license is enabled.
To see this field, the user also needs the Sales Engagement User or Sales Engagement Quick
Cadence Creator user permission set.

This field is a polymorphic relationship field.


Standard Objects Account

**Field Name** **Details**

**Relationship Name**
PersonActionCadenceAssignee

**Refers To**
Group, User

```
PersonActionCadenceId

PersonActionCadenceState

PersonIndividualId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the lead’s assigned cadence. This field is available in API version 46.0 and later when
the Sales Engagement license is enabled. To see this field, the user also needs the Sales
Engagement User or Sales Engagement Quick Cadence Creator user permission set.

This is a relationship field.

**Relationship Name**
PersonActionCadence

**Refers To**
ActionCadence

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
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects Account

**Field Name** **Details**

**Description**
ID of the data privacy record associated with this person’s account. This field is available if
you enabled Data Protection and Privacy in Setup.

Available in API version 42.0 and later.

```
PersonScheduledResumeDateTime

Phone

PhotoUrl

Rating

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the action cadence tracker is going to resume after it’s paused or
on a wait step. This field is available in API version 54.0 and later when the Sales Engagement
license is enabled. To see this field, the user also needs the Sales Engagement User or Sales
Engagement Quick Cadence Creator user permission set.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Phone number for this account. Maximum size is 40 characters.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**

Path to be combined with the URL of a Salesforce instance (for example,
https:// _`yourInstance`_ .salesforce.com/) to generate a URL to request the social network
profile image associated with the account. Generated URL returns an HTTP redirect (code
302) to the social network profile image for the account.

Blank if Social Accounts and Contacts isn't enabled for the org or if Social Accounts and
Contacts is disabled for the requesting user.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The account’s prospect rating, for example Hot, Warm, or Cold.


Standard Objects Account

**Field Name** **Details**

```
RecordTypeId

Salutation

ShippingAddress

ShippingCity

ShippingCountry

ShippingCountryCode

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the record type assigned to this object.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Honorific added to the name for use in letters, etc. This field is available on person accounts.

**Type**
address

**Properties**
Filter, Nillable

**Description**
The compound form of the shipping address. Read-only. See Address Compound Fields for
details on compound address fields.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details of the shipping address for this account. City maximum size is 40 characters

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details of the shipping address for this account. Country maximum size is 80 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects Account

**Field Name** **Details**

**Description**
The ISO country code for the account’s shipping address.

```
ShippingGeocodeAccuracy

ShippingLatitude

ShippingLongitude

ShippingPostalCode

ShippingState

```

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

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details of the shipping address for this account. Postal code maximum size is 20 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details of the shipping address for this account. State maximum size is 80 characters.


Standard Objects Account

**Field Name** **Details**

```
ShippingStateCode

ShippingStreet

Sic

SicDesc

Site

TickerSymbol

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO state code for the account’s shipping address.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street address of the shipping address for this account. Maximum of 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Standard Industrial Classification code of the company’s main business categorization, for
example, 57340 for Electronics. Maximum of 20 characters. This field is available on business
accounts, not person accounts.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an org’s line of business, based on its SIC code. Maximum length is 80
characters. This field is available on business accounts, not person accounts.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Name of the account’s location, for example `Headquarters` or `London` . Label is
**Account Site** . Maximum of 80 characters.

**Type**
string


Standard Objects Account

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The stock market symbol for this account. Maximum of 20 characters. This field is available
on business accounts, not person accounts.

```
Tradestyle

Type

Website

YearStarted

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A name, different from its legal name, that an org may use for conducting business. Similar
to “Doing business as” or “DBA”. Maximum length is 255 characters. This field is available on
business accounts, not person accounts.

Note: This field is only available to organizations that use Data.com Prospector or
Data.com Clean.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Type of account, for example, Customer, Competitor, or Partner.

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The website of this account. Maximum of 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when an org was legally established. Maximum length is 4 characters. This field is
available on business accounts, not person accounts.

Note: This field is only available to organizations that use Data.com Prospector or
Data.com Clean.


Standard Objects Account

IsPersonAccount Fields

These fields are the subset of person account fields that are contained in the child person contact record of each person account. If the
`IsPersonAccount` field has the value `false`, the following fields have a null value and can't be modified. If `true`, the fields can
be modified.

Person account fields only show when person accounts are enabled. Person accounts are disabled by default.

**Field Name** **Details**

```
FirstName

LastName

MiddleName

PersonAssistantName

PersonAssistantPhone

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
First name of the person for a person account. Maximum size is 40 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Last name of the person for a person account. Required if the record type is a person account
record type. Maximum size is 80 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Middle name of the person for a person account. Maximum size is 40 characters.

**Type**
string

**Properties**
Create, Filter, Nillable, Update

**Description**
The person account’s assistant name. Label is **Assistant** . Maximum size is 40 characters.

**Type**
phone

**Properties**
Create, Filter, Nillable, Update

**Description**
The person account’s assistant phone. Label is **Asst. Phone** . Maximum size is 40 characters.


Standard Objects Account

**Field Name** **Details**

```
PersonBirthDate

PersonContactId

PersonDepartment

PersonEmail

PersonEmailBouncedDate

```

**Type**
date

**Properties**
Create, Filter, Nillable, Update

**Description**
The birthday of the contact associated with this person account. Label is **Birthdate** . The year
portion of the `PersonBirthDate` field is ignored in filter criteria, including report filters,
list view filters, and SOQL queries. For example, the following SOQL query returns person
accounts with birthdays later in the year than today:

```
  SELECT FirstName, LastName, PersonBirthDate

  FROM Account

  WHERE Birthdate > TODAY

```

**Type**
reference

**Properties**
Filter, Nillable, Update

**Description**
The ID for the contact associated with this person account. Label is **Contact ID** .

**Type**
string

**Properties**
Create, Filter, Nillable, Update

**Description**
The department. Label is **Department** . Maximum size is 80 characters.

**Type**
email

**Properties**
Create, Filter, Nillable, Update

**Description**
Email address for this person account. Label is **Email** .

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Update

**Description**
If bounce management is activated and an email sent to the person account bounces, the
date and time the bounce occurred.


Standard Objects Account

**Field Name** **Details**

```
PersonEmailBouncedReason

PersonGenderIdentity

PersonHasOptedOutOfEmail

PersonHomePhone

PersonLeadSource

PersonMailingAddress

```

**Type**
string

**Properties**
Create, Filter, Nillable, Update

**Description**
If bounce management is activated and an email sent to the person account bounces, the
reason the bounce occurred

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The person’s internal experience of their gender, which may or may not correspond to the
person’s designated sex at birth. Label is **Gender Identity** .

**Type**
boolean

**Properties**
Create, Filter, Nillable, Update

**Description**
Indicates whether the person account has opted out of email ( `true` ) or not ( `false` ). Label
is **Email Opt Out** .

**Type**
phone

**Properties**
Create, Filter, Nillable, Update

**Description**
The home phone number for this person account. Label is **Home Phone** .

**Type**
picklist

**Properties**
Create, Filter, Nillable, Update

**Description**
The person account’s lead source. Label is **Lead Source** .

**Type**
address

**Properties**
Filter, Nillable


Standard Objects Account

**Field Name** **Details**

**Description**
The compound form of the person account mailing address. Read-only. For details on
compound address fields, see Address Compound Fields.

**•** `PersonMailingCity` **Type**
string

**•** `PersonMailingCountry`

**•** `PersonMailingPostalCode` **Properties**
Create, Filter, Nillable, Update

**•** `PersonMailingState`
**Description**
Details about the mailing address for this person account. Labels are **Mailing City**, **Mailing**
**Country**, **Postal Code**, and **State** . Maximum size for city and country is 40 characters.
Maximum size for postal code and state is 20 characters.

**•** `PersonMailingCountryCode` **Type**

**•** `PersonMailingStateCode` picklist
**Properties**
Create, Filter, Group, Nillable, Sort, Update

```
PersonMailingGeocodeAccuracy

PersonMailingLatitude

PersonMailingLongitude

```

**Description**
The ISO country or state code for the mailing address of the person account.

**Type**
picklist

**Properties**
Retrieve, Query, Restricted picklist, Nillable

**Description**
Accuracy level of the geocode for the person’s mailing address. For details on geolocation
compound fields, see Compound Field Considerations and Limitations.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `PersonMailingLongitude` to specify the precise geolocation of a person
account’s mailing address. Acceptable values are numbers between –90 and 90 with up to
15 decimal places. For details on geolocation compound fields, see Compound Field
Considerations and Limitations.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects Account

**Field Name** **Details**

**Description**
Used with `PersonMailingLatitude` to specify the precise geolocation of a person
account’s mailing address. Acceptable values are numbers between –180 and 180 with up
to 15 decimal places. For details on geolocation compound fields, see Compound Field
Considerations and Limitations on page 19.

```
PersonMailingStreet

PersonMobilePhone

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Update

**Description**
The mailing street address for this person account. Label is **Mailing Street** . Maximum size
is 255 characters.

**Type**
phone

**Properties**
Create, Filter, Nillable, Update

**Description**
The mobile phone number for this person account. Label is **Mobile** .

**•** `PersonOtherCity` **Type**
string

**•** `PersonOtherCountry`

**•** `PersonOtherPostalCode` **Properties**
Create, Filter, Nillable, Update

**•** `PersonOtherState`
**Description**
Details about the alternate address for this person account. Labels are **Other City**, **Other**
**Country**, **Other Zip/Postal Code**, and **Other State** .

**•** `PersonOtherCountryCode` **Type**

**•** `PersonOtherStateCode` picklist
**Properties**
Create, Filter, Group, Nillable, Sort, Update

```
PersonOtherLatitude

```

**Description**
The ISO country or state code for the alternate address of the person account.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects Account

**Field Name** **Details**

**Description**
Used with `PersonOtherLongitude` to specify the precise geolocation of a person
account’s alternate address. Acceptable values are numbers between –90 and 90 with up
to 15 decimal places. For details on geolocation compound fields, see Compound Field
Considerations and Limitations.

```
PersonOtherLongitude

PersonOtherPhone

PersonOtherStreet

PersonPronouns

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `PersonOtherLatitude` to specify the precise geolocation of a person
account’s alternate address. Acceptable values are numbers between –180 and 180 with up
to 15 decimal places. For details on geolocation compound fields, see Compound Field
Considerations and Limitations.

**Type**
phone

**Properties**
Create, Filter, Nillable, Update

**Description**
The alternate phone number for this person account. Label is **Other Phone** .

**Type**
textarea

**Properties**
Create, Filter, Nillable, Update

**Description**
The person account’s alternate street address. Label is **Other Street** .

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The individual’s personal pronouns, reflecting their gender identity. Others can use these
pronouns to refer to the individual in the third person. The entry is selected from a picklist
of available values, which the administrator sets. Maximum 40 characters. Label is **Pronouns** .

Possible values are:

**•** `He/Him`

**•** `He/They`

**•** `Not Listed`


Standard Objects Account

**Field Name** **Details**

**•** `She/Her`

**•** `She/They`

**•** `They/Them`

```
PersonReportsToId

PersonTitle

Suffix

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort Update

**Description**
ID of the person account or contact that this person account reports to.

This field doesn't appear if `enableReportsToOnPersonAccount` in the
AccountSettings metadata type is `false` .

Available in API version 62.0 and later.

This is a relationship field.

**Relationship Name**
PersonReportsTo

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
string

**Properties**
Create, Filter, Nillable, Update

**Description**
The person account’s title. Label is **Title** . Maximum size is 80 characters. When converting a
lead to a person account, the conversion fails if the lead’s Title field contains more than 80
characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Name suffix of the person for a person account. Maximum size is 40 characters.

Note: When importing account data, users need the Set Audit Fields upon Record Creation permission to assign values to audit
fields such as `CreatedDate` . Audit fields are automatically updated during API operations unless you set these fields yourself.


### Standard Objects AccountBrand

Usage

Use this object to query and manage accounts in your org. Client applications can create, update, delete, or query Attachment records
associated with an account via the API.

Client applications can also create or update account objects by converting a Lead via the `convertLead()` call.

If the values in the IsPersonAccount Fields are not null, you can't change `IsPersonAccount` to `false` or an error occurs.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[AccountChangeEvent (API version 44.0)](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**
Change events are available for the object.

**[AccountFeed (API version 18.0)](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**
Feed tracking is available for the object.

**[AccountHistory (API version 11.0)](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**
History is available for tracked fields of the object.

**[AccountOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_accountownersharingrule.htm)**

Sharing rules are available for the object.

**[AccountShare](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_accountshare.htm)**

Sharing is available for the object.

SEE ALSO:

AccountShare

AccountTeamMember

_SOAP API Developer Guide_ [: Person Account Record Types](https://developer.salesforce.com/docs/atlas.en-us.262.0.api.meta/api/sforce_api_guidelines_personaccounts.htm)

### AccountBrand

Represents the brand details of a Partner Account. This object is available in API version 43.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated() query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available only if digital experiences is enabled in your org and it has a Partner Community or Customer Community Plus
license.


Standard Objects AccountBrand

Fields

**Field** **Details**

```
AccountId

Address

City

CompanyName

Country

Email

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the Account. This number is unique within your organization.

**Type**
address

**Properties**
Filter, Nillable

**Description**
The street address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the company associated with the account brand.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country where the account is physically located.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects AccountBrand

**Field** **Details**

**Description**
Email address associated with the account.

```
GeocodeAccuracy

LastReferencedDate

LastViewedDate

Latitude

LogoId

LogoUrl

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist Sort, Update

**Description**
Stores data for accurate geocoded location.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Most recent date referenced.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Most recent date viewed.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used along with `Longitude` to specify the precise geolocation of an address.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the logo.

**Type**
url

**Properties**
Nillable,


Standard Objects AccountBrand

**Field** **Details**

**Description**
URL of the logo. This field is available in API version 44.0 and later.

```
Longitude

Name

OwnerId

Phone

PostalCode

State

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `Latitude` to specify the precise geolocation of an address.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Required. Name of the account.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Required. ID of the Owner.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Phone number.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code where the user’s IP address is physically located.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects AccountContactRelation

**Field** **Details**

**Description**
The address state.

```
Street

Website

```

Associated Objects

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The address street.

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Website for the Account Brand.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**AccountBrandOwnerSharingRule**

Sharing rules are available for the object.

**AccountBrandShare**

Sharing is available for the object.

### AccountContactRelation

Represents a relationship between a contact and one or more accounts.

This object is available in API version 37.0. The AccountContactRelation object supports person accounts. That means that a person
account can be either a related contact on a business account or a related account on a contact. A person account can also be related
to another person account as either a related contact or related account.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`


Standard Objects AccountContactRelation

Fields

**Field Name** **Details**

```
AccountContactRelationshipCurrency

AccountId

ContactId

EndDate

IsActive

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for organizations with the multicurrency feature enabled. Contains
the ISO code for any currency allowed by the organization.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the account that is related to the contact. Field can't be modified when
updating existing account-contact relationship records.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the contact that is related to the account. Field can't be modified when
updating existing account-contact relationship records.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date a relationship between a contact and account ended. Use with the
`Start Date` to keep a history of the relationship.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether relationship is active ( `true` ) or not ( `false` ).


Standard Objects AccountContactRelation

**Field Name** **Details**

```
IsDirect

Roles

StartDate

```

Usage

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the account associated with the contact is the contact's primary
account ( `true` ) or not ( `false` ).

**Type**
multipicklist

**Properties**
Create, Filter, Nillable, Update

**Description**
The contact’s participating role in the account. Values are `Business User`,
`Decision Maker`, `Economic Buyer`, `Economic Decision Maker`,
`Evaluator`, `Executive Sponsor`, `Influencer`, `Technical`
`Buyer`, and `Other` .

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date a relationship between a contact and account began. Use with the `End`
`Date` to keep a history of the relationship.

Use this object to associate a single contact record to multiple account records so you can easily track the relationships between the
people and businesses they work with.

When you insert a non-private contact in your org that associates a contact to multiple accounts, an AccountContactRelation is created
and its validation rules, database insertion, and triggers are executed immediately after the contact is saved to the database. When you
change a contact's primary account, an AccountContactRelation may be created or edited, and the AccountContactRelation validation
[rules, database changes, and triggers are executed immediately after the contact is saved to the database. See Order of Execution.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_triggers_order_of_execution.htm)

Associated Objects

This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**AccountContactRelationChangeEvent on page 68 (API version 59.0)**
Change events are available for the object.


### Standard Objects AccountCleanInfo AccountCleanInfo

Stores the metadata Data.com Clean uses to determine an account record’s clean status. AccountCleanInfo helps you automate the
cleaning or related processing of account records. This object is removed in API version 67.0

Note: When your Data.com Prospector or Data.com Clean contract expires, Data.com features, objects, and fields will be removed
from your org.

To support customers’ needs around compliance and to remain a leader in trust and privacy, Salesforce removed all contact data
from the Data.com service on February 1, 2021.

[For more information, see Data.com Prospector and Clean Retirement.](https://help.salesforce.com/articleView?id=000270376&language=en_US&type=1)

Account Clean Info provides a snapshot of the data in your Salesforce account record and its matched Data.com record at the time the
Salesforce record was cleaned.

Account Clean Info includes a number of bit vector fields, whose component fields each correspond to individual object fields and
provide related data or status information about those fields. For example, the bit vector field `IsDifferent` has an
`IsDifferentState` field. If the `IsDifferentState` field’s value is `False`, that means the `State` field value is _the same_
on the Salesforce account record and its matched Data.com record.

### AccountCleanInfo bit vector fields include:

**•** `CleanedBy` indicates who (a user) or what (a Clean job) cleaned the account record.

**•** `IsDifferent` indicates whether or not a field on the account record has a value that differs from the corresponding field on the
matched Data.com record.

**•** `IsFlaggedWrong` indicates whether or not a field on the account record has a value that is flagged as wrong to Data.com.

**•** `IsReviewed` indicates whether or not a field on the account record is in a `Reviewed` state, which means that the value was
reviewed but not accepted.

Their individual bits are defined here.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`

Fields

**Field Name** **Details**

```
AccountId

AccountSite

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The unique, system-generated ID assigned when the account record was created.

**Type**
string


Standard Objects AccountCleanInfo

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Information about the account’s location, such as single location, headquarters,
or branch.

```
Address

AnnualRevenue

City

CleanedByJob

CleanedByUser

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
Estimated annual revenue of the account.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address of the account.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the account record was cleaned by a Data.com Clean job
( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter


Standard Objects AccountCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the account record was cleaned by a Salesforce user ( `true` )
or not ( `false` ).

```
CompanyName

CompanyStatusDataDotCom

Country

DandBCompanyDunsNumber

DataDotComId

```

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

**Description**
The status of the company per Data.com. Values are: `Company is In`
`Business per Data.com` or `Company is Out of Business`

```
  per Data.com.

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address of the account.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The D-U-N-S Number on the D&B Company record (if any) that is linked to the
account.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID Data.com maintains for the company.


Standard Objects AccountCleanInfo

**Field Name** **Details**

```
Description

DunsNumber

DunsRightMatchConfidence

DunsRightMatchGrade

Fax

Industry

```

**Type**
textarea

**Properties**
Nillable

**Description**
A description of the account.

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
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The account’s DUNSRight confidence code.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The account’s DUNSRight match grade.

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
The account’s fax number.

**Type**
picklist


Standard Objects AccountCleanInfo

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The industry the account belongs to.

```
IsDifferentAccountSite

IsDifferentAnnualRevenue

IsDifferentCity

IsDifferentCompanyName

IsDifferentCountry

```

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the account’s `AccountSite` field value is different from
the corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the account’s `AnnualRevenue` field value is different from
the corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the account’s `City` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the account’s `AccountName` field value is different from
the corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter


Standard Objects AccountCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the account’s `Country` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

```
IsDifferentCountryCode

IsDifferentDandBCompanyDunsNumber

IsDifferentDescription

IsDifferentDunsNumber

IsDifferentFax

```

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
Indicates whether the account’s `DandBCompanyID` field value is different
from the corresponding value on its matched Data.com record ( `true` ) or not
( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the account’s `Description` field value is different from
the corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the account’s `DunsNumber` field value is different from the
D-U-N-S Number on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter


Standard Objects AccountCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the account’s `Fax` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

```
IsDifferentIndustry

IsDifferentNaicsCode

IsDifferentNaicsDescription

IsDifferentNumberOfEmployees

IsDifferentOwnership

```

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the account’s `Industry` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the account’s `NaicsCode` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the account’s `NaicsDescription` field value is different
from the corresponding value on its matched Data.com record ( `true` ) or not
( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the account’s `NumberOf Employees` field value is
different from the corresponding value on its matched Data.com record ( `true` )
or not ( `false` ).

**Type**
boolean

**Properties**
Filter


Standard Objects AccountCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the account’s `Ownership` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

```
IsDifferentPhone

IsDifferentPostalCode

IsDifferentSic

IsDifferentSicDescription

IsDifferentState

```

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the account’s `Phone` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the account’s `PostalCode` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the account’s `Sic` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the account’s `SicDescription` field value is different
from the corresponding value on its matched Data.com record ( `true` ) or not
( `false` ).

**Type**
boolean

**Properties**
Filter


Standard Objects AccountCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the account’s `State` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

```
IsDifferentStateCode

IsDifferentStreet

IsDifferentTickerSymbol

IsDifferentTradestyle

IsDifferentWebsite

```

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
Indicates whether the account’s `State` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the account’s `TickerSymbol` field value is different from
the corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the account’s `Tradestyle` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter


Standard Objects AccountCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the account’s `Website` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

```
IsDifferentYearStarted

IsFlaggedWrongAccountSite

IsFlaggedWrongAddress

IsFlaggedWrongAnnualRevenue

IsFlaggedWrongCompanyName

```

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the account’s `YearStarted` field value is different from
the corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `AccountSite` field value is flagged as wrong
to Data.com ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `Address` field value is flagged as wrong to
Data.com ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `AnnualRevenue` field value is flagged as
wrong to Data.com ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update


Standard Objects AccountCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the account’s `CompanyName` field value is flagged as wrong
to Data.com ( `true` ) or not ( `false` ).

```
IsFlaggedWrongDescription

IsFlaggedWrongDunsNumber

IsFlaggedWrongFax

IsFlaggedWrongIndustry

IsFlaggedWrongNaicsCode

```

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `Description` field value is flagged as wrong
to Data.com ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `DunsNumber` field value is flagged as wrong
to Data.com ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `Fax` field value is flagged as wrong to Data.com
( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `Industry` field value is flagged as wrong to
Data.com ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update


Standard Objects AccountCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the account’s `NaicsCode` field value is flagged as wrong
to Data.com ( `true` ) or not ( `false` ).

```
IsFlaggedWrongNaicsDescription

IsFlaggedWrongNumberOfEmployees

IsFlaggedWrongOwnership

IsFlaggedWrongPhone

IsFlaggedWrongSic

```

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `NaicsDescription` field value is flagged
as wrong to Data.com ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `NumberOfEmployees` field value is flagged
as wrong to Data.com ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `Ownership` field value is flagged as wrong
to Data.com ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `Phone` field value is flagged as wrong to
Data.com ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update


Standard Objects AccountCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the account’s `Sic` field value is flagged as wrong to Data.com
( `true` ) or not ( `false` ).

```
IsFlaggedWrongSicDescription

IsFlaggedWrongTickerSymbol

IsFlaggedWrongTradestyle

IsFlaggedWrongWebsite

IsFlaggedWrongYearStarted

```

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `SicDescription` field value is flagged as
wrong to Data.com ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `TickerSymbol` field value is flagged as
wrong to Data.com ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `Tradestyle` field value is flagged as wrong
to Data.com ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `Website` field value is flagged as wrong to
Data.com ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update


Standard Objects AccountCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the account’s `YearStarted` field value is flagged as wrong
to Data.com ( `true` ) or not ( `false` ).

```
IsInactive

IsReviewedAccountSite

IsReviewedAddress

IsReviewedAnnualRevenue

IsReviewedCompanyName

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the account has been reported to Data.com as _`Inactive`_
( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `AccountSite` field value is in a `Reviewed`
state ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `Address` field value is in a `Reviewed` state
( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `AnnualRevenue` field value is in a
`Reviewed` state ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update


Standard Objects AccountCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the account’s `CompanyName` field value is in a `Reviewed`
state ( `true` ) or not ( `false` ).

```
IsReviewedDandBCompanyDunsNumber

IsReviewedDescription

IsReviewedDunsNumber

IsReviewedFax

IsReviewedIndustry

```

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `DandBCompanyID` field value is in a
`Reviewed` state ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `Description` field value is in a `Reviewed`
state ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `DunsNumber` field value is in a `Reviewed`
state ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `Fax` field value is in a `Reviewed` state ( `true` )
or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update


Standard Objects AccountCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the account’s `Industry` field value is in a `Reviewed`
state ( `true` ) or not ( `false` ).

```
IsReviewedNaicsCode

IsReviewedNaicsDescription

IsReviewedNumberOfEmployees

IsReviewedOwnership

IsReviewedPhone

```

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `NaicsCode` field value is in a `Reviewed`
state ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `NaicsDescription` field value is in a
`Reviewed` state ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `NumberOfEmployees` field value is in a
`Reviewed` state ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `Ownership` field value is in a `Reviewed`
state ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update


Standard Objects AccountCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the account’s `Phone` field value is in a `Reviewed` state
( `true` ) or not ( `false` ).

```
IsReviewedSic

IsReviewedSicDescription

IsReviewedTickerSymbol

IsReviewedTradestyle

IsReviewedWebsite

```

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `Sic` field value is in a `Reviewed` state ( `true` )
or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `SicDescription` field value is in a
`Reviewed` state ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `TickerSymbol` field value is in a `Reviewed`
state ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `Tradestyle` field value is in a `Reviewed`
state ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update


Standard Objects AccountCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the account’s `Website` field value is in a `Reviewed` state
( `true` ) or not ( `false` ).

```
IsReviewedYearStarted

LastMatchedDate

LastStatusChangedById

LastStatusChangedDate

Latitude

```

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the account’s `YearStarted` field value is in a `Reviewed`
state ( `true` ) or not ( `false` ).

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date the account record was last matched and linked to a Data.com record.

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


Standard Objects AccountCleanInfo

**Field Name** **Details**

```
Longitude

NaicsCode

NaicsDescription

Name

NumberOfEmployees

Ownership

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
Filter, Group, Nillable, Sort

**Description**
The six-digit North American Industry Classification System (NAICS) code is the
standard used by business and government to classify business establishments
into industries, according to their economic activity for the purpose of collecting,
analyzing, and publishing statistical data related to the U.S. business economy.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A brief description of an organization’s line of business, based on its NAICS code.

**Type**
string

**Properties**
Filter, Group, Sort, Update

**Description**
Field label is **Account Clean Info Name** . The name of the account. Maximum
size is 255 characters.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of employees working at the account.

**Type**
picklist


Standard Objects AccountCleanInfo

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Ownership type for the account, for example Private, Public, or Subsidiary.

```
Phone

PostalCode

Sic

SicDescription

State

```

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
The phone number for the account.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address of the account.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Standard Industrial Classification code of the company’s main business
categorization, for example, 57340 for Electronics.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A brief description of an organization’s line of business, based on its SIC code.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address of the account.


Standard Objects AccountCleanInfo

**Field Name** **Details**

```
Street

TickerSymbol

Tradestyle

Website

YearStarted

```

Usage

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address of the account.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The stock market symbol for the account.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A name, different from its legal name, that an organization can use for conducting
business. Similar to “Doing business as” (DBA).

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**
The website of the account.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The year the company was established or the year when current ownership or
management assumed control of the company.

Administrators can modify a limited set of AccountCleanInfo fields from the Account Clean Info page.


### Standard Objects AccountContactRole

Developers can create triggers that read the Account Clean Info fields to help automate the cleaning or related processing of account
records. For example, you might create a trigger that reads the `Clean Status` field on the Account object. If an account record’s
`Clean Status` field value is `Different` but the record has no `Billing Street` value, the trigger could update the record’s
status to `Not Compared` .

Create triggers that read AccountCleanInfo fields to help automate the cleaning or related processing of account records. For example:

**•** Keep account records’ status `InSync` if the only difference from matched records is the `Phone` format (for example, _`(415)`_
_`353-8000`_ on the account record versus _`415 353 8000`_ on the matched Data.com record).

```
     trigger AccountPhoneTrigger on Account (before update) {

       for (Account account: Trigger.new) {

         Account oldAccount = Trigger.oldMap.get(account.ID);

         if (account.CleanStatus == 'Different') {

            List <AccountCleanInfo> cleanInfo = [Select Id, IsDifferentPhone,

     IsReviewedPhone, Phone from AccountCleanInfo where AccountId = :account.Id];

            if (cleanInfo.size() > 0 && cleanInfo[0].IsDifferentPhone &&

     cleanInfo[0].Phone.StartsWith('+')) {

              // if Data.com phone number is marked Different but starts with ‘+’,

     ignore this

              // and set the status to “Reviewed”

              AccountCleanInfo cleanInfoToUpdate = new AccountCleanInfo();

              cleanInfoToUpdate.Id = cleanInfo[0].Id;

              cleanInfoToUpdate.IsReviewedPhone = true;

              update cleanInfoToUpdate;

              account.CleanStatus = 'Reviewed';

            }

         }

       }

     }

```

**•** Create a customized set of `Industry` field values for accounts. Use triggers to map values from fields on imported or cleaned
records onto a standard set of values.

**•** Read the `CleanStatus` field value on the Account object. If that value is `Different`, but a Salesforce record has no street
address value, update the record’s status to `Not Compared` .

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AccountCleanInfoChangeEvent (API version 62.0)**
Change events are available for the object.

### AccountContactRole

Represents the role that a Contact plays on an Account.


Standard Objects AccountContactRole

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
AccountId

ContactId

IsDeleted

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the Account.

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
Create, Filter, Group, Sort, Update

**Description**
Required. ID of the Contact associated with this account.

This is a relationship field.

**Relationship Name**
Contact

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
boolean


Standard Objects AccountContactRole

**Field** **Details**

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is **Deleted** .

```
 IsPrimary

 Role

```

Usage

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether the Contact plays the primary role on the Account ( `true` ) or not ( `false` ).
Note that each account has only one primary contact role. Label is **Primary** . Default value
is `false` .

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Name of the role played by the Contact on this Account, such as Decision Maker, Approver,
Buyer, and so on. Must be unique—there can't be multiple records in which the
`AccountId`, `ContactId`, and `Role` values are identical. Different contacts can play
the same role on the same account. A contact can play different roles on the same account.

Use this object to define the role that a Contact plays on a given Account within the context of a specific Opportunity.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AccountContactRoleChangeEvent (API version 44.0)**
Change events are available for the object.

SEE ALSO:

Account

Contact


### Standard Objects AccountInsight AccountInsight

Represents an individual insight (a key business development) related to an account record.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

To see an insight related to a specific account, users need a Sales Cloud Einstein license and access to the account record. As of the
Spring ’20 release, Pardot and Sales Engagement users no longer have access to this object.

Fields

**Field Name** **Details**

```
AccountId

ActualHeardWithinDays

CompetitorName

ContactName

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the related account record.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reserved for future use.

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


Standard Objects AccountInsight

**Field Name** **Details**

**Description**
This field is not in use as of API version 46.0.

```
ContactTitle

CurrencyIsoCode

Division

ExpectedHeardWithinDays

LastHeard

LastReferencedDate

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field is not in use as of API version 46.0.

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
The division of the related record.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reserved for future use.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Reserved for future use.

**Type**
dateTime


Standard Objects AccountInsight

**Field Name** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related
to this record, or a list view.

```
LastViewedDate

NumberOfNewsArticles

Rationale

Title

TrendType

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
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of news articles related to insights of type `M&A activity`
`detected`, `Company is expanding`, and `Leadership changes` .

**Type**
string

**Properties**
Filter, Group, Nillable

**Description**
The explanation for an insight, providing more background information and
details that are specific to the org.

**Type**
string

**Properties**
Filter, Group, Nillable

**Description**
The title of the insight.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort


### Standard Objects AccountOwnerSharingRule

**Field Name** **Details**

**Description**
The trend type of the insight. Possible values include:

**•** Negative

**•** Positive

**•** Informational

```
Type

```

Usage

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of insight. Possible values include:

**•** M&A activity detected

**•** Company is expanding

**•** Leadership changes

This object is read-only and isn’t supported with workflows, triggers, or process builder.

### AccountOwnerSharingRule

Represents the rules for sharing an account with a User other than the owner.

Note: To programmatically update owner sharing rules, we recommend that you use Metadata API. Contact Salesforce customer
support to enable access to this object for your org.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
upsert()

```

Special Access Rules

Customer Portal users can't access this object.


Standard Objects AccountOwnerSharingRule

Fields

**Field** **Details**

```
AccountAccessLevel

CaseAccessLevel

ContactAccessLevel

Description

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Update

**Description**
A value that represents the type of sharing being allowed. The possible values are:

**•** `Read`

**•** `Edit`

**•** `All` (This value isn’t valid for creating or updating.)

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A value that represents the type of access granted to the target Group for all child cases. The
possible values are:

**•** `None`

**•** `Read`

**•** `Edit`

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
A value that represents the type of access granted to the target Group, UserRole, or User for
any associated contacts. The possible values are:

**•** `None`

**•** `Read`

**•** `Edit`

Note: When `DefaultContactAccess` is set to `Controlled by Parent`,
you can’t create or update this field.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects AccountOwnerSharingRule

**Field** **Details**

**Description**
A description of the sharing rule. Maximum size is 1000 characters. This field is available in
API version 29.0 and later.

```
DeveloperName

GroupId

OpportunityAccessLevel

Name

```

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

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the source group. An Account owned by a User in the source Group
triggers the rule to give access.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A value that represents the type of access granted to the target Group for any associated
Opportunity. The possible values are:

**•** `None`

**•** `Read`

**•** `Edit`

**Type**
string


### Standard Objects AccountPartner

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
The ID representing the User or Group being granted access.

Use this object to manage the sharing rules for accounts. General sharing and territory management-related sharing use this object. For
example, the following code creates an account owner sharing rule between two public groups, which can also contain portal users.

```
AccountOwnerSharingRule rule = new AccountOwnerSharingRule();

rule.setName("RuleName"); // Set the sharing rule name

rule.setDeveloperName("RuleDeveloperName"); // Set the sharing rule developer name

rule.setGroupId("00Gx00000000000"); // Set the group of users to share records from

rule.setUserOrGroupId("00Gx00000000001"); // Set the group of users to share records to

rule.setAccountAccessLevel("Edit");

rule.setOpportunityAccessLevel("Read");

rule.setCaseAccessLevel("None");

connection.create(rule);

```

[Note: The original territory management feature is now unavailable. For more information, see The Original Territory Management](https://help.salesforce.com/articleView?id=The-original-Territory-Management-module-will-be-retired-in-the-Summer-20-release&language=en_US&type=1)
[Module Will Be Retired in the Summer ’21 Release. The information in this topic applies to the original territory management](https://help.salesforce.com/articleView?id=The-original-Territory-Management-module-will-be-retired-in-the-Summer-20-release&language=en_US&type=1)
feature only, and not to Enterprise Territory Management.

SEE ALSO:

### Account

AccountShare

_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_sharingrules.htm)_ : SharingRules

### AccountPartner

This object represents a partner relationship between two Account records. An AccountPartner record is created automatically when a
Partner record is created for a partner relationship between two accounts. An AccountPartner record is also created automatically
between an account and an opportunity’s account when a Partner record is created between an account and an opportunity.

Note: This object is completely distinct from and independent of Account records that have been enabled for the partner portal.


Standard Objects AccountPartner

Supported Calls

`create()`, `delete()`, `describeLayout()describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Customer Portal users can't access this object.

Fields

**Field** **Details**

```
AccountFromId

AccountToId

IsPrimary

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the main Account in the partner relationship.

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


Standard Objects AccountPartner

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the AccountPartner is the primary partner of an opportunity ( `true` ).
When there are no corresponding Opportunity Partner records, the value is `false` .

```
OpportunityId

ReversePartnerId

Role

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the opportunity in a partner relationship.

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
ID of the reciprocal AccountPartner record in a partner relationship.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The UserRole that the partner Account has on the main Account. For example, `Consultant`
or `Distributor` .

Creating an Account-Account Partner Relationship

When you create a partner relationship between two accounts (when you create a Partner record and specify the `AccountFromId` ),
the API automatically creates two AccountPartner records, one for the forward relationship and one for the reverse. For example, if you
create a Partner relationship with “Acme, Inc.” as the `AccountFromId` and “Acme Consulting” as the `AccountToId`, the API
automatically creates two AccountPartner records:


### Standard Objects AccountPlan

**•** The forward relationship AccountPartner with “Acme, Inc.” as the `AccountFromId` and “Acme Consulting” as the `AccountToId` .

**•** The reverse relationship AccountPartner with “Acme Consulting” as the `AccountFromId` and “Acme, Inc.” as the `AccountToId` .

**•** The value of the Role field in the reverse relationship AccountPartner is set to the PartnerRole record `ReverseRole` value associated
with the value of the `Role` field in the forward relationship AccountPartner.

This mapping allows the API to manage the records and their relationships efficiently.

SEE ALSO:

Partner

OpportunityPartner

### AccountPlan

Represents customer information with measurable objectives and executable steps to proactively manage and grow customer relationships.
This object is available in API version 62.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `update()`, `upsert()`

Special Access Rules

This object is available if sales account plans are turned on.

Fields

**Field** **Details**

```
AccountChallenges

AccountCmptvWeaknesses

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The key obstacles to the growth of the account.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The shortcomings that hinder the account’s ability to outperform competitors in the market.


Standard Objects AccountPlan

**Field** **Details**

```
AccountCompetitiveStrengths

AccountCompetitors

AccountId

AccountIndustryTrends

AccountInternalRiskRating

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The abilities of the account to outperform their competitors in the market.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The businesses or companies that offer similar products or services and compete for the
same target market as the account.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Account record.

This field is a relationship field.

**Relationship Name**
Account

**Refers To**
Account

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The shifts in the pattern of the industry that are specific to the account.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The rating that’s assigned to assess the risk level of the account. To access this field, you must
have an FSC Sales or a Financial Services Cloud Extension license.


Standard Objects AccountPlan

**Field** **Details**

```
AccountPrfmIndicators

AccountStrategicPriorities

AccountVision

CallingStrategy

CallingStrategyNotes

EndDate

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The key performance indicators used by the account to measure the success and effectiveness
of a product or service.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The key priorities of the account.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The long-term value statement of the account.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
How frequently the relationship team meets with the account. To access this field, you must
have an FSC Sales or a Financial Services Cloud Extension license.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The outline of the format and organization of account meetings. To access this field, you
must have an FSC Sales or a Financial Services Cloud Extension license.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects AccountPlan

**Field** **Details**

**Description**
The end date of the account plan.

```
FlexCard

LastReferencedDate

LastViewedDate

Name

Notes

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Omnistudio FlexCard. To access this field, you must have an FSC Sales or a Financial
Services Cloud Extension license.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly. For example,
accessed through a list view or related record.

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
The name of the account plan.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The notes or observations for the account plan.


Standard Objects AccountPlan

**Field** **Details**

```
OwnerId

RelationshipOpportunities

RelationshipStrengths

RelationshipSummary

RelationshipThreats

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the account plan.

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
The list of sales or potential deal opportunities in the relationship with the account.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The strengths in the relationship with the account.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A concise overview of the relationship dynamics with the account. To access this field, you
must have an FSC Sales or a Financial Services Cloud Extension license.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The possible concerns in the relationship with the account.


Standard Objects AccountPlan

**Field** **Details**

```
RelationshipWeaknesses

StartDate

Status

```

Associated Objects

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The shortcomings in the relationship with the account.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The start date of the account plan.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the status of the account plan.

Possible values are:

**•** `Active`

**•** `Inactive`

**•** `Not Started`

The default value is `Not Started` .

This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**[AccountPlanChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[AccountPlanHistory](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[AccountPlanOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_accountownersharingrule.htm)**

Sharing rules are available for the object.

**[AccountPlanShare](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_accountshare.htm)**

Sharing is available for the object.


### Standard Objects AccountPlanObjective AccountPlanObjective

Represents strategic objectives or initiatives pursued by a relationship team with a customer to enhance customer engagement and
satisfaction. This object is available in API version 62.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available if sales account plans are turned on.

Fields

**Field** **Details**

```
AccountPlanId

AccountPlanObjCategoryId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The account plan associated with the objective.

This field is a relationship field.

**Relationship Name**
### AccountPlan

**Relationship Type**
Master-detail

**Refers To**
### AccountPlan

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The category associated with the account plan objective. To access this field, you must have
an FSC Sales or a Financial Services Cloud Extension license.

This field is a relationship field.

**Relationship Name**
AccountPlanObjCategory


Standard Objects AccountPlanObjective

**Field** **Details**

**Refers To**
AccountPlanObjectiveCategory

```
Description

EndDate

ExternalStakeholderId

LastInteractionSumGenDate

LastReferencedDate

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the account plan objective.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The end date of the account plan objective.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The customer stakeholder contact associated with the account plan objective. The relationship
team collaborates with the customer stakeholder to achieve a specific objective. To access
this field, you must have an FSC Sales or a Financial Services Cloud Extension license.

This field is a relationship field.

**Relationship Name**
ExternalStakeholder

**Refers To**
Contact

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date when the most recent interaction summary was generated using Einstein Generative
AI. To access this field, you must have an FSC Sales or a Financial Services Cloud Extension
license.

**Type**
dateTime


Standard Objects AccountPlanObjective

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

```
LastViewedDate

Name

ObjectiveInteractionSummary

ObjectiveOwnerId

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
The name of the account plan objective.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The summary of interactions that occur with the account in relation to the account plan
objective. To access this field, you must have an FSC Sales or a Financial Services Cloud
Extension license.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The owner user associated with the objective.

This field is a relationship field.

**Relationship Name**
ObjectiveOwner

**Refers To**
User


Standard Objects AccountPlanObjective

**Field** **Details**

```
OwnerId

Priority

StartDate

Status

```

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

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the level of importance placed on achieving the objective associated with the
account plan. To access this field, you must have an FSC Sales or a Financial Services Cloud
Extension license.

Possible values are:

**•** `High`

**•** `Low`

**•** `Medium`

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The start date of the account plan objective.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the status of the account plan objective.

Possible values are:

**•** `Closed`


### Standard Objects AccountPlanObjectiveMeasure

**Field** **Details**

**•** `In Progress`

**•** `New`

Associated Objects

This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**AccountPlanObjectiveChangeEvent on page 68**
Change events are available for the object.

**AccountPlanObjectiveHistory on page 63**
History is available for tracked fields of the object.

**AccountPlanObjectiveOwnerSharingRule on page 65**
Sharing rules are available for the object.

**AccountPlanObjectiveShare on page 67**
Sharing is available for the object.

### AccountPlanObjectiveMeasure

Represents the performance of target metrics for an objective associated with the account plan. This object is available in API version
62.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available if sales account plans are turned on.

Fields

**Field** **Details**

AccountPlanObjMeasCalcDefId

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The account plan objective calculation definition associated with the measure.

This field is a relationship field. Available in API version 63.0 and later.


Standard Objects AccountPlanObjectiveMeasure

**Field** **Details**

**Relationship Name**
AccountPlanObjMeasCalcDef

**Refers To**
AccountPlanObjMeasCalcDef

```
AccountPlanObjectiveId

CurrentCurrencyValue

CurrentNumberValue

CurrentPercentValue

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The account plan objective associated with the measure.

This field is a relationship field.

**Relationship Name**
AccountPlanObjective

**Relationship Type**
Master-detail

**Refers To**
AccountPlanObjective

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The current value in currency for a measure associated with the account plan objective.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The current numerical value for a measure associated with the account plan objective.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The current value in percentage for a measure associated with the account plan objective.


Standard Objects AccountPlanObjectiveMeasure

**Field** **Details**

```
CurrentValue

```

CurrentValueTimestamp

```
LastReferencedDate

LastViewedDate

Name

TargetCurrencyValue

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The current value for a measure associated with the account plan objective.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the current value was last updated. This field is available in API version
63.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record. If this value is null, it’s possible
that this record was referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the account plan objective measure.

**Type**
currency

**Properties**
Filter, Nillable, Sort


Standard Objects AccountPlanObjectiveMeasure

**Field** **Details**

**Description**
The target value in currency for a measure associated with the account plan objective.

```
TargetNumberValue

TargetPercentValue

TargetValue

ValueType

```

Associated Objects

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The target numerical value for a measure associated with the account plan objective.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The target value in percentage for a measure associated with the account plan objective.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The target value for a measure associated with the account plan objective.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the type of value that's measured.

Possible values are:

**•** `Currency`

**•** `Number`

**•** `Percent`

This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.


### Standard Objects AccountPlanObjMeasCalcCond

**AccountPlanObjectiveMeasureChangeEvent on page 68**
Change events are available for the object.

**AccountPlanObjectiveMeasureHistory on page 63**
History is available for tracked fields of the object.

### AccountPlanObjMeasCalcCond

Represents a field and value combination for filtering records to include in the calculation of a sales account plan objective measure’s
current value. This object is available in API version 63.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

This object is available if sales account plans are turned on.

Fields

**Field** **Details**

```
AccountPlanObjMeasCalcDefId

FieldName

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The account plan objective measure calculation definition where this criteria is used.

This field is a relationship field.

**Relationship Name**
AccountPlanObjMeasCalcDef

**Relationship Type**
Master-detail

**Refers To**
AccountPlanObjMeasCalcDef

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A field on the calculation definition’s `TargetObject` that you want to filter by. Fields on
the Campaign, Case, Contact, or Opportunity objects are supported.


### Standard Objects AccountPlanObjMeasCalcDef

**Field** **Details**

```
Operation

Value

```

Usage

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The logical operator for matching records with the specified field value.

Possible values are:

**•** `Contains`

**•** `Equals`

**•** `GreaterOrEqual`

**•** `GreaterThan`

**•** `LessOrEqual`

**•** `LessThan`

**•** `NotContain`

**•** `NotEqual`

**•** `StartsWith`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The value to match for the specified field.

Let’s say that a calculation definition tracks the currency amount on Closed Won opportunities. The calculation definition’s
`TargetObject` is `Opportunity`, and the condition further specifies these values.

**•** `FieldName` is `StageName` .

**•** `Operation` is `Equals` .

**•** `Value` is `ClosedWon` .

### AccountPlanObjMeasCalcDef

Represents the definition of a target object, rollup field, and logic for calculating the current value of a sales account plan objective
measure. This object is available in API version 63.0 and later.


Standard Objects AccountPlanObjMeasCalcDef

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

This object is available if sales account plans are turned on.

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
Create, Filter, Group, Nillable, Sort, Update

**Description**
A summary of the calculation definition that’s visible to users when they select the definition
for an account plan objective measure.

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

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The combined language and locale ISO code, which controls the language of the calculation
definition.

**Type**
string


Standard Objects AccountPlanObjMeasCalcDef

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label for this calculation definition. This display value is the internal label that doesn't get
translated.

```
NamespacePrefix

RollupType

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

The namespace prefix can have one of these values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that aren’t Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The method for calculating the account plan objective measure’s current value from records
that match the calculation definition and any optional conditions.

Possible values are:

**•** `Count`

**•** `Max`

**•** `Min`

**•** `Sum`

In Setup, this field’s label is Calculation Type.

**Type**
picklist


Standard Objects AccountPlanObjMeasCalcDef

**Field** **Details**

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Possible values are:

**•** `Active`

**•** `Draft`

**•** `Inactive`

Only active calculation definitions are available for users to select when they specify an
account plan objective measure.

```
TargetField

TargetObject

ValueType

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The field on `TargetObject` to use for calculating the account plan objective measure’s
current value. Rollup fields on the Campaign, Case, Contact, or Opportunity object are
supported.

In Setup, this field’s label is Rollup Field.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The object to use for calculating the account plan objective measure’s current value.

Possible values are:

**•** `Campaign`

**•** `Case`

**•** `Contact`

**•** `Opportunity`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The data type for calculating the account plan objective measure’s current value.

Possible values are:

**•** `Currency`


### Standard Objects AccountPlanObjMeasCalcDefLocalization

**Field** **Details**

**•** `Number`

**•** `Percent`

Usage

Let’s say that a calculation definition tracks the currency amount on opportunities. The calculation definition’s `TargetObject` is
`Opportunity`, `TargetField` is `Amount`, and `RollupType` is `Sum` .

### AccountPlanObjMeasCalcDefLocalization

Represents the translated value of the definition of a target object, rollup field, and logic for calculating the current value of a sales
account plan objective measure. This object is available in API version 63.0 and later when the Translation Workbench is enabled.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()getUpdated()query()`, `retrieve()`, `update()`,

```
   upsert()

```

Special Access Rules

**•** Your organization must be using Lightning Experience with Sales Cloud in Enterprise, Performance, Unlimited, and Einstein 1 Sales
Edition editions.

**•** Translation Workbench must be enabled for your org.

**•** Sales account plans must be turned on.

**•** Users with the Customize Application or Manage Translation permission can create or update AccountPlanObjMeasCalcDef translations.

Fields

**Field** **Details**

Language

```
NamespacePrefix

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The language the AccountPlanObjMeasCalcDef is translated into.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects AccountPlanObjMeasRela

**Field** **Details**

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can
refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

The namespace prefix can have one of these values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that aren’t Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

```
 ParentId

Value

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the related account plan objective measure calculation definition. This field is a
relationship field.

**Type**
textarea

**Properties**
Create, Filter, Sort, update

**Description**
The translated label of the account plan objective measure calculation definition.

Translate the labels of your account plan objective measure calculation definitions for supported languages .

### AccountPlanObjMeasRela

Represents a junction between an account plan objective measure and the related objects. This object is available in API version 62.0
and later.


Standard Objects AccountPlanObjMeasRela

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AccountPlanObjectiveMeasureId

LastReferencedDate

LastViewedDate

Name

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The account plan objective measure associated with the record.

This field is a relationship field.

**Relationship Name**
AccountPlanObjectiveMeasure

**Relationship Type**
Master-detail

**Refers To**
AccountPlanObjectiveMeasure (the master object)

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
Autonumber, Defaulted on create, Filter, idLookup, Sort


### Standard Objects AccountRelationship

**Field** **Details**

**Description**
The name of the account plan objective measure relation record.

```
ReferenceRecordId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The record of the object associated with the account plan objective measure.

This field is a polymorphic relationship field.

**Relationship Name**
ReferenceRecord

**Refers To**
Case, FinancialDeal, Opportunity

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AccountPlanObjMeasRelaChangeEvent on page 68**
Change events are available for the object.

**AccountPlanObjMeasRelaHistory on page 63**
History is available for tracked fields of the object.

### AccountRelationship

Represents a relationship of a given type between two accounts. This object is available in API version 45.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Special Access Rules

In Digital Experience Settings, turn on the Enable Account Relationships org preference, which is off by default.


Standard Objects AccountRelationship

Fields

**Field** **Details**

```
AccountFromID

AccountToId

LastReferencedDate

LastViewedDate

Name

OwnerId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort,

**Description**
ID of the account that gains access to data from `AccountTo` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the account sharing data with `AccountFrom` .

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
the user accessed this record or list view ( `LastReferencedDate` ) but didn’t viewed it.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the account relationship.

**Type**
reference


Standard Objects AccountRelationship

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the user who created the account relationship.

```
Type

```

Associated Objects

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The relationship type. All account relationship sharing rules of that type are to this account
relationship.

Standard values are:

**•** System Integrator

**•** Agency

**•** Advertiser

**•** Reseller

**•** Distributor

**•** Developer

**•** Broker

**•** Lender

**•** Institution

**•** Contractor

**•** Dealer

**•** Consultant

**•** Client

**•** Vendor

**•** Agent

**•** Retailer

**•** SubContractor

**•** Supplier

Picklist items can be updated with your own values.

This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**AccountRelationshipFeed**

Feed tracking is available for the object.


### Standard Objects AccountRelationshipShareRule

**AccountRelationshipHistory**

History is available for tracked fields of the object.

**AccountRelationshipOwnerSharingRule**

Sharing rules are available for the object.

### **AccountRelationshipShare**

Sharing is available for the object.

### AccountRelationshipShareRule

Represents the rule that determines which object records are shared, how they are shared, the account relationship type that shares the
records, and the level of access granted to the records. This object is available in API version 45.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()` . `describeSObjects()`, `query()`, `retrieve()`, `update()` . `upsert()`

Fields

**Field** **Details**

```
AccessLevel

AccountToCriteriaField

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Type of access granted by the share rule. Valid values are:

**•** `Read` (Read Only)

**•** `Edit` (Read/Write)

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Criteria that must be met for the data to be shared.

Possible values are:

**•** `Account.OwnerId`

**•** `Account.ParentId`

**•** `Campaign.OwnerId`

**•** `Case.AccountId`

**•** `Case.OwnerId`

**•** `Contact.AccountId`


Standard Objects AccountRelationshipShareRule

**Field** **Details**

**•** `Contact.OwnerId`

**•** `Lead.ConvertedAccountId`

**•** `Lead.OwnerId`

**•** `Lead.PartnerAccountId`

**•** `Opportunity.PartnerAccountId`

**•** `Order.AccountId`

**•** `Order.ActivatedById`

**•** `Order.CompanyAuthorizedById`

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

```
Description

DeveloperName

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


Standard Objects AccountRelationshipShareRule

**Field** **Details**

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance may slow while
Salesforce generates one for each record.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

```
EntityType

Language

MasterLabel

NamespacePrefix

```

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


### Standard Objects AccountShare

**Field** **Details**

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

```
StaticFormulaCriteria

Type

### AccountShare

```

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A way to further filter what data gets shared. This must be a deterministic formula and
spanning is not allowed.

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


Standard Objects AccountShare

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

AccountId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Level of access that the User or Group has to the Account. The possible values are:

**•** `Read`

**•** `Edit`

**•** `All` (This value isn't valid for create or update calls.)

This field must be set to an access level that is at least equal to the organization’s default
Account access level. In addition, either this field, the `OpportunityAccessLevel`
field, or the `CaseAccessLevel` field must be set higher than the organization’s default
access level.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the Account associated with this sharing entry. This field can't be updated.

This is a relationship field.

**Relationship Name**
Account


Standard Objects AccountShare

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Account

```
CaseAccessLevel

ContactAccessLevel

OpportunityAccessLevel

```

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

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update


Standard Objects AccountShare

**Field** **Details**

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

```
RowCause

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

**•** `Manual` —The User or Group has access because a User with “All” access manually
shared the Account with the user or group.

**•** `Owner` —The User is the owner of the Account

**•** `Team` —The User or Group has team access (is an AccountTeamMember).

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


Standard Objects AccountShare

**Field** **Details**

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

Usage

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

```


### Standard Objects AccountTag

```
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


### Standard Objects AccountTeamMember

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

AccountTag stores the relationship between its parent TagDefinition and the Account being tagged. Tag objects act as metadata,
allowing users to describe and organize their data.

When a tag is deleted, its parent TagDefinition will also be deleted if the name is not being used; otherwise, the parent remains. Deleting
a TagDefinition sends it to the Recycle Bin, along with any associated tag entries.

### AccountTeamMember

Represents a User who is a member of an Account team.

See also UserAccountTeamMember, which represents a User who is on the default account team of another user.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`


Standard Objects AccountTeamMember

Special Access Rules

**•** This object is available only for Enterprise, Unlimited, and Performance Edition users who have enabled the account team functionality.

**•** Customer Portal users can't access this object.

Fields

**Field Name** **Details**

```
AccountAccessLevel

AccountId

CaseAccessLevel

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


Standard Objects AccountTeamMember

**Field Name** **Details**

`ContactAccessLevel`, `OpportunityAccessLevel`, or `CaseAccessLevel`
field must be set higher than the organization’s default access level. This field is available in
API version 37.0 and later.

```
ContactAccessLevel

CurrencyIsoCode

IsDeleted

```

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


Standard Objects AccountTeamMember

**Field Name** **Details**

The `getDeleted()` call also doesn’t show deleted account team members unless
the record was deleted from an account related list or the Developer Console.

```
OpportunityAccessLevel

PhotoURL

TeamMemberRole

Title

```

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

**Properties**
Create, Filter, Nillable, Update

**Description**
Role associated with this team member. One of the valid team member roles defined for
your organization. Label is **Team Role** .

**Type**
string

**Properties**
Filter, Nillable, Sort, Group

**Description**
Read only. Retrieves the user’s title. This field is available in API version 37.0 and later.


### Standard Objects AccountTerritoryAssignmentRule

**Field Name** **Details**

```
 UserId

```

Usage

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

[If you use SOQL statements to query all records in an organization, the ALL ROWS keywords don’t query deleted account team member](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/langCon_apex_SOQL_query_all_rows.htm)
records.

Associated Objects

This object has the following associated objects. If the API version isn't specified, they're available in the same API versions as this object.

**[AccountTeamMemberChangeEvent (API version 66.0)](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**
Change events are available for the object.

SEE ALSO:

### Account AccountTerritoryAssignmentRule

An account assignment rule that assigns accounts to territories based on account fields. Available if Sales Territories has been enabled.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
upsert()

```

Special Access Rules

Users with the View Setup and Configuration permission can access this object. Users with the Manage Territories permission can edit
this object.


Standard Objects AccountTerritoryAssignmentRule

Fields

**Field** **Details**

```
BooleanFilter

IsActive

IsInherited

Name

TerritoryId

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

**Type**
reference

**Properties**
Create, Filter, Update

**Description**
ID of the territory where accounts that satisfy this rule are assigned.


### Standard Objects AccountTerritoryAssignmentRuleItem

Usage

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

Operation

```

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The standard or custom account field to use as a criteria.

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The criteria to apply, such as “equals” or “starts with.”


### Standard Objects AccountTerritorySharingRule

**Field** **Details**

```
 RuleID

 SortOrder

 Value

```

Usage

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

**•** A territory will not have any accounts (with the exception of manually assigned accounts) unless at least one account assignment
rule is active for the territory.

SEE ALSO:

AccountTerritoryAssignmentRule

Territory

UserTerritory

### AccountTerritorySharingRule

Represents the rules for sharing an Account within a territory.


Standard Objects AccountTerritorySharingRule

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

ContactAccessLevel

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

**•** `Read`

**•** `Edit`

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
A value that represents the type of access granted to the target group for all related contacts
on the account. The possible values are:

**•** `None`

**•** `Read`


Standard Objects AccountTerritorySharingRule

**Field** **Details**

**•** `Edit`

Note: This field is read only.

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

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the source group. Accounts owned by users in the source territory trigger
the rule to give access.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label of the sharing rule as it appears in the user interface. Limited to 80 characters.
Corresponds to **Label** on the user interface.


### Standard Objects AccountUserTerritory2View

**Field** **Details**

```
OpportunityAccessLevel

UserOrGroupId

```

Usage

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

### Account

AccountShare

### AccountUserTerritory2View

Represents the view of the Users in Assigned Territories related list in Lightning Experience for Sales Territories. Available in API version
42.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Standard and partner users can access this object.


### Standard Objects ActionCadence

Fields

**Field Name** **Details**

```
AccountId

RoleInTerritory2

Territory2Id

UserId

```

Usage

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

**Description**
Unique identifier for each user in the Users in Assigned Territories related list.

Use this object to show the users who are assigned to the territories assigned to an account.

A filter criterion with one `AccountId` is required when you execute a SOQL query on this object.

### ActionCadence

Represents the definition of a cadence. This object is available in API version 45.0 and later.

Use ActionCadence and its related objects to learn about an action cadence, including:


Standard Objects ActionCadence

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

ActiveTargets

```

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date that the user activated the action cadence. ActionCadence objects are created in
a draft state and must be manually activated before they’re used.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of active targets that are currently assigned with this cadence. Available
in API version 58.0 and later.


Standard Objects ActionCadence

**Field** **Details**

```
Description

ErrorMessage

FolderId

FolderName

IsWaitAllowedBeforeDaisyChain

```

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


Standard Objects ActionCadence

**Field** **Details**

**Description**
Whether the cadence is allowed to have a wait step before a daisy chain step ( `true` ) or not
( `false` ).

The default value is `false` .

```
LastEditedDateTime

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

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of this action cadence. Every action cadence in an org must have a unique name.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the action cadence (typically the user who created it).

Note: To change the owner of an action cadence, the new owner must have read
access to action cadences enabled in their user profile.


Standard Objects ActionCadence

**Field** **Details**

This field is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

```
State

SuccessfulCompletions

```

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

An error occurred while trying to activate the action cadence.

**•** `Inactive`

The user deactivated the action cadence. New targets can’t be added to the action
cadence. Existing targets continue in the action cadence until completion.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of successful dispositions this cadence has upon completion. For example,
customer engaged or customer connected. Available in API version 58.0 and later.


Standard Objects ActionCadence

**Field** **Details**

```
TotalSteps

TotalTargets

Type

```

Usage

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

Quick cadences can contain only one step, are built by reps for their personal use, and
don't require the Cadence Builder.

**•** `SDR`

SDR cadences are built for Sales Development Representative workflows.

Use ActionCadence to learn how many action cadences are currently active:

```
select COUNT() from ActionCadence where State="Active"

```

Retrieve all ActionCadence records that have "West Coast" in their name:

```
SELECT ActionCadenceId FROM ActionCadence WHERE NAME LIKE '[West Coast Cadence]%'

```


### Standard Objects ActionCadenceRule

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

Fields

**Field** **Details**

```
ActionCadenceStepId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ActionCadenceStep that this rule is associated with.

This field is a relationship field.


Standard Objects ActionCadenceRule

**Field** **Details**

**Relationship Name**
ActionCadenceStep

**Relationship Type**
Lookup

**Refers To**
ActionCadenceStep

```
ConditionLogic

GlobalEventType

GraphState

```

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

**•** `CallLeftVoicemail`

**•** `CallCallBackLater`

This field is available in API version 49.0 and later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects ActionCadenceRule

**Field** **Details**

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

```
OutcomeNextStepName

ParentRuleName

RuleName

RuleType

```

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

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name given to the rule. Every rule in an action cadence must have a unique name.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update


### Standard Objects ActionCadenceRuleCondition

**Field** **Details**

**Description**
