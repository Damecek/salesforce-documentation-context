Represents a technician service resource that belongs to a service crew.

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


Standard Objects

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


Standard Objects

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


Standard Objects

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


Standard Objects

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


Standard Objects

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


Standard Objects

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


Standard Objects

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

TenantScrAIPrmptInjection
Stores generative AI prompt injection data. This object is available in API version 65.0 and later.


Standard Objects

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


Standard Objects

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


Standard Objects

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
owns the accounts. Available if Sales Territories has been enabled.

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


Standard Objects

Territory2ObjectExclusion
Represents the objects that aren’t included in territory assignment rule runs, even when they meet assignment rule criteria. This
object is available in API version 54.0 and later.

Territory2ObjSharingConfig
Represents the sharing access level of objects assigned to a particular territory. This object is available in API version 56.0 and later.

Territory2Type
Represents a category for territories (Territory2). Every Territory2 must have a Territory2Type. Available only if Sales Territories has
been enabled for your organization.

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


Standard Objects

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
[the UI Telemetry Resource Timing Event on page 2413 and includes requests initiated with either the Fetch API or the XMLHttpRequest](https://fetch.spec.whatwg.org/)
[API. This object is available in API version 64.0 and later.](https://xhr.spec.whatwg.org/)

UiTelemetryRsrcTmEventLog
UI Telemetry Resource Timing events capture network performance metrics related to loading an application’s resources. The event
[includes requests initiated with either the Fetch API or the XMLHttpRequest API. This object is available in API version 64.0 and later.](https://fetch.spec.whatwg.org/)


Standard Objects

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


Standard Objects

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


Standard Objects

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


Standard Objects

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


Standard Objects

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


Standard Objects

VisualforceRequestEventLog
Visualforce Request events contain details of Visualforce requests. Requests can originate from the browser (UI). This object is available
in API version 61.0 and later.

VideoCall
Represents a video call.

VideoCallInsight
Represents the video call insight data associated with a video call. Each record represents the call insight of a specific recording or
transcript within a call. This object is available in API version 66.0 and later.

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
Represents a call in Service Cloud Voice, Sales Dialer, or other supported voice connectors. For Service Cloud Voice, this can be a
phone or Voice over Internet Protocol (VoIP) call. This object is available in API version 40.0 and later.

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


Standard Objects

VoiceCallQualityFeedback
Represents feedback given by a Sales Dialer user about the quality of a VoiceCall .

VoiceCallRecording
Represents a call recording in Service Cloud Voice and Sales Dialer. Call recordings for Service Cloud Voice with Amazon Connect
and for Service Cloud Voice with Partner Telephony from Amazon Connect are stored in S3 buckets on your Amazon Web Services
(AWS) account and can be accessed via AWS. Call recordings for Sales Dialer are saved as files in Salesforce.

VoiceCoaching
Represents a call that is using call monitoring.

VoiceLocalPresenceNumber
Represents a phone number with the same area code as the person who’s being called.

VoiceMailContent
Represents a voicemail message left by a caller to the context user.

VoiceMailGreeting
Represents a custom greeting message that plays upon reaching a user’s voicemail. This object is available in API version 41.0 and
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
Represents information about the Service Cloud Voice or Sales Dialer provider’s vendor.

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


Standard Objects

WebCartAdjustmentBasis
Coupons that trigger promotions for the cart. When a customer tries to add a coupon to the cart, the store looks for promotions
associated with the coupon. If a promotion results in a price adjustment, a WebCartAdjusmentBasis record is created. This object is
available in API version 54.0 and later.

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


Standard Objects

WorkAccessShare
Used to control Givers of WorkBadgeDefinition records.

WorkBadge
Represents information about who the badge was given to and which badge was given. A WorkBadge record is created for each
recipient of a WorkBadgeDefinition.

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


Standard Objects

WorkGoalCollaborator
Represents collaborators on a WorkGoal object. This doesn’t include WorkGoal followers, which is handled by Chatter Feed Follow
functionality. This object has been deprecated as of API version 35.0. Use the Goal object to query information about WDC goals.

WorkGoalCollaboratorHistory
Represents the history of changes to the values in the fields in a WorkGoalCollaborator object. Access is read-only.

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


### Standard Objects AbnExperiment

WorkPlanTemplate
Represents a template for a work plan. This object is available in API version 52.0 and later.

WorkPlanTemplateEntry
Represents an object that associates a work step template with a work plan template. This object is available in API version 52.0 and
later.

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


Standard Objects AbnExperiment

Fields

**Field** **Details**

```
DataSpaceId

Description

DeveloperName

LastAnalyzed

LastReferencedDate

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Unique identifier that refers to the data space where an experiment's resources originate.
Required.

This field is a relationship field.

**Relationship Name**
DataSpace

**Refers To**
DataSpace

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


Standard Objects AbnExperiment

**Field** **Details**

**Description**
Timestamp that indicates the last time an experiment was referenced by another resource.

```
LastViewedDate

Name

PersonalizationSchemaEnum

PersonalizationSchemaId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp that indicates the last time a user viewed the experiment.

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


Standard Objects AbnExperiment

**Field** **Details**

```
PrimaryMetricId

ProfileDataGraphId

ScheduleFrequencyInMinutes

Source

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier that refers to engagement signal metrics, which are used to measure an
experiment.

This field is a polymorphic relationship field.

**Relationship Name**
PrimaryMetric

**Refers To**
EngagementSignalCmpndMetric, EngagementSignalMetric

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


Standard Objects AbnExperiment

**Field** **Details**

**•** `ExperienceBuilder` —Experience Site Builder

**•** `FlowBuilder`

**•** `PersonalizationApp`

```
SourceRecordId

StartedDate

State

Status

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier that refers to the specific record that contains the experiment.

This field is a polymorphic relationship field.

**Relationship Name**
SourceRecord

**Refers To**
FlowRecordElement, ManagedContent

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


Standard Objects AbnExperiment

**Field** **Details**

**Description**
Picklist value that indicates the current status of the experiment while an action is being
performed.

Possible values are:

**•** `Active`

**•** `CreateError`

**•** `DeleteError`

**•** `Deleting`

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


### Standard Objects AbnExperimentCohort

**AbnExperimentOwnerSharingRule on page 65**
Sharing rules are available for the object.

**AbnExperimentShare on page 67**
Sharing is available for the object.

### AbnExperimentCohort

Represents the specified audience that's participating in an A/B/n experiment. This object is available in API version 63.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
AbnExperimentId

AllocationWeight

CurrencyIsoCode

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Unique identifier that refers to a related experiment.

This field is a relationship field.

**Relationship Name**
### AbnExperiment

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


Standard Objects AbnExperimentCohort

**Field** **Details**

**Description**
Three letter ISO currency codes for supported currencies. Optional.

Possible values are:

**•** `USD` —U.S. Dollar

```
DataSpaceId

Description

DeveloperName

IsControl

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Unique identifier that refers to the data space where an experiment cohort's resources
originate. Required.

This field is a relationship field.

**Relationship Name**
DataSpace

**Refers To**
DataSpace

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
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Whether the cohort is used as the control group that performance is checked against.

The default value is `false` .


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
ConnectionReceivedId

ConnectionSentId

Description

DunsNumber

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


Standard Objects Account

**Field Name** **Details**

around the world as a global standard for business identification and tracking. Maximum
size is 9 characters. This field is available on business accounts, not person accounts.

Note: This field is only available to organizations that use Data.com Prospector or
Data.com Clean.

```
Fax

Industry

IsBuyer

IsCustomerPortal

```

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

**Description**
An industry associated with this account. For example, `Biotechnology` . Maximum size
is 40 characters.

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


Standard Objects Account

**Field Name** **Details**

If you change this field's value from `true` to `false`, you can disable up to 100 Experience
Cloud site or Customer Portal users associated with the account and permanently delete all
of the account's site roles and groups. You can't restore deleted site roles and groups.

Exclude this field when merging accounts.

This field can be updated in API version 16.0 and later.

Tip: We recommend that you update up to 50 contacts simultaneously when
changing the accounts on contacts enabled for an Experience Cloud site. We also
recommend that you make this update after business hours.

```
IsPartner

IsPersonAccount

IsPriorityRecord

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the account has at least one contact enabled to use the org's partner
portal ( `true` ) or not ( `false` ). This field is available if partner relationship management
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

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read only. Label is **Is Person Account** . Indicates whether this account has a record type of
Person Account ( `true` ) or not ( `false` ).

**Type**
boolean


Standard Objects Account

**Field Name** **Details**

**Properties**
Defaulted on create, Group

**Description**
Shows whether the user has marked the account as important ( _`True`_ ) or not ( _`False`_ ). The
default value is `false` . Available in API version 60.0 and later.

```
Jigsaw

JigsawCompanyId

LastActivityDate

LastReferencedDate

```

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

Important: The `Jigsaw` field is exposed in the API to support troubleshooting for
import errors and reimporting of corrected data. Do not modify the value in the
`Jigsaw` field.

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


Standard Objects Account

**Field Name** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for example,
through a list view or related record.

```
LastViewedDate

MasterRecordId

NaicsCode

```

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


Standard Objects Account

**Field Name** **Details**

Note: This field is only available to organizations that use Data.com Prospector or
Data.com Clean.

```
NaicsDesc

Name

NumberOfEmployees

OperatingHoursId

```

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

**Description**
Required. Label is **Account Name** . Name of the account. Maximum size is 255 characters.
If the account has a record type of Person Account:

**•** This value is the concatenation of the `FirstName`, `MiddleName`, `LastName`, and
`Suffix` of the associated person contact.

**•** You can't modify this value.

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


Standard Objects Account

**Field Name** **Details**

**Relationship Type**
Lookup

**Refers To**
OperatingHours

```
OwnerId

Ownership

ParentId

```

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

**•** For API version 16.0 and later, users must have the “Transfer Record” permission in order
to update (transfer) account ownership using this field.

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


Standard Objects Account

**Field Name** **Details**

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Account

```
PersonActionCadenceAssigneeId

PersonActionCadenceId

PersonActionCadenceState

```

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

**Relationship Name**
PersonActionCadenceAssignee

**Refers To**
Group, User

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


Standard Objects Account

**Field Name** **Details**

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

```
PersonIndividualId

PersonScheduledResumeDateTime

Phone

PhotoUrl

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the data privacy record associated with this person’s account. This field is available if
you enabled Data Protection and Privacy in Setup.

Available in API version 42.0 and later.

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


Standard Objects Account

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**

Path to be combined with the URL of a Salesforce instance (for example,
https:// _`yourInstance`_ .salesforce.com/) to generate a URL to request the social network
profile image associated with the account. Generated URL returns an HTTP redirect (code
302) to the social network profile image for the account.

Blank if Social Accounts and Contacts isn't enabled for the org or if Social Accounts and
Contacts is disabled for the requesting user.

```
Rating

RecordTypeId

Salutation

ShippingAddress

ShippingCity

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The account’s prospect rating, for example Hot, Warm, or Cold.

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


Standard Objects Account

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details of the shipping address for this account. City maximum size is 40 characters

```
ShippingCountry

ShippingCountryCode

ShippingGeocodeAccuracy

ShippingLatitude

ShippingLongitude

```

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

**Description**
The ISO country code for the account’s shipping address.

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


Standard Objects Account

**Field Name** **Details**

**Description**
Used with `ShippingLatitude` to specify the precise geolocation of an address.
Acceptable values are numbers between –180 and 180 with up to 15 decimal places. For
details on geolocation compound fields, see Compound Field Considerations and Limitations.

```
ShippingPostalCode

ShippingState

ShippingStateCode

ShippingStreet

Sic

```

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


Standard Objects Account

**Field Name** **Details**

```
SicDesc

Site

TickerSymbol

Tradestyle

Type

```

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

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The stock market symbol for this account. Maximum of 20 characters. This field is available
on business accounts, not person accounts.

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


Standard Objects Account

**Field Name** **Details**

```
Website

YearStarted

```

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

IsPersonAccount Fields

These fields are the subset of person account fields that are contained in the child person contact record of each person account. If the
`IsPersonAccount` field has the value `false`, the following fields have a null value and can't be modified. If `true`, the fields can
be modified.

Person account fields only show when person accounts are enabled. Person accounts are disabled by default.

**Field Name** **Details**

```
FirstName

LastName

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


Standard Objects Account

**Field Name** **Details**

```
MiddleName

PersonAssistantName

PersonAssistantPhone

PersonBirthDate

PersonContactId

```

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


Standard Objects Account

**Field Name** **Details**

```
PersonDepartment

PersonEmail

PersonEmailBouncedDate

PersonEmailBouncedReason

PersonGenderIdentity

PersonHasOptedOutOfEmail

```

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


Standard Objects Account

**Field Name** **Details**

**Description**
Indicates whether the person account has opted out of email ( `true` ) or not ( `false` ). Label
is **Email Opt Out** .

```
PersonHomePhone

PersonLeadSource

PersonMailingAddress

```

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

**Description**
The ISO country or state code for the mailing address of the person account.


Standard Objects Account

**Field Name** **Details**

```
PersonMailingGeocodeAccuracy

PersonMailingLatitude

PersonMailingLongitude

PersonMailingStreet

PersonMobilePhone

```

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

**Description**
Used with `PersonMailingLatitude` to specify the precise geolocation of a person
account’s mailing address. Acceptable values are numbers between –180 and 180 with up
to 15 decimal places. For details on geolocation compound fields, see Compound Field
Considerations and Limitations on page 19.

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


Standard Objects Account

**Field Name** **Details**

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

PersonOtherLongitude

PersonOtherPhone

```

**Description**
The ISO country or state code for the alternate address of the person account.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `PersonOtherLongitude` to specify the precise geolocation of a person
account’s alternate address. Acceptable values are numbers between –90 and 90 with up
to 15 decimal places. For details on geolocation compound fields, see Compound Field
Considerations and Limitations.

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


Standard Objects Account

**Field Name** **Details**

```
PersonOtherStreet

PersonPronouns

PersonReportsToId

```

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

**•** `She/Her`

**•** `She/They`

**•** `They/Them`

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


Standard Objects Account

**Field Name** **Details**

```
PersonTitle

Suffix

```

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

Usage

Use this object to query and manage accounts in your org. Client applications can create, update, delete, or query Attachment records
associated with an account via the API.

Client applications can also create or update account objects by converting a Lead via the `convertLead()` call.

If the values in the IsPersonAccount Fields are not null, you can't change `IsPersonAccount` to `false` or an error occurs.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[AccountChangeEvent (API version 44.0)](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**
Change events are available for the object.

**[AccountFeed (API version 18.0)](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**
Feed tracking is available for the object.

**[AccountHistory (API version 11.0)](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**
History is available for tracked fields of the object.

**[AccountOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_accountownersharingrule.htm)**

Sharing rules are available for the object.


### Standard Objects AccountBrand

**[AccountShare](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_accountshare.htm)**

Sharing is available for the object.

SEE ALSO:

AccountShare

AccountTeamMember

_SOAP API Developer Guide_ [: Person Account Record Types](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/sforce_api_guidelines_personaccounts.htm)

### AccountBrand

Represents the brand details of a Partner Account. This object is available in API version 43.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated() query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available only if digital experiences is enabled in your org and it has a Partner Community or Customer Community Plus
license.

Fields

**Field** **Details**

```
AccountId

Address

City

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


Standard Objects AccountBrand

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city.

```
CompanyName

Country

Email

GeocodeAccuracy

LastReferencedDate

LastViewedDate

```

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

**Description**
Email address associated with the account.

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


Standard Objects AccountBrand

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
Most recent date viewed.

```
Latitude

LogoId

LogoUrl

Longitude

Name

OwnerId

```

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

**Description**
URL of the logo. This field is available in API version 44.0 and later.

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


Standard Objects AccountBrand

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Required. ID of the Owner.

```
Phone

PostalCode

State

Street

Website

```

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

**Description**
The address state.

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


### Standard Objects AccountContactRelation

Associated Objects

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

Fields

**Field Name** **Details**

### `AccountContactRelationshipCurrency`

```
AccountId

ContactId

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


Standard Objects AccountContactRelation

**Field Name** **Details**

**Description**
ID of the contact that is related to the account. Field can't be modified when
updating existing account-contact relationship records.

```
EndDate

IsActive

IsDirect

Roles

StartDate

```

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


### Standard Objects AccountCleanInfo

**Field Name** **Details**

**Description**
The date a relationship between a contact and account began. Use with the `End`
`Date` to keep a history of the relationship.

Usage

Use this object to associate a single contact record to multiple account records so you can easily track the relationships between the
people and businesses they work with.

When you insert a non-private contact in your org that associates a contact to multiple accounts, an AccountContactRelation is created
and its validation rules, database insertion, and triggers are executed immediately after the contact is saved to the database. When you
change a contact's primary account, an AccountContactRelation may be created or edited, and the AccountContactRelation validation
[rules, database changes, and triggers are executed immediately after the contact is saved to the database. See Order of Execution.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_triggers_order_of_execution.htm)

Associated Objects

This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**AccountContactRelationChangeEvent on page 68 (API version 59.0)**
Change events are available for the object.

### AccountCleanInfo

Stores the metadata Data.com Clean uses to determine an account record’s clean status. AccountCleanInfo helps you automate the
cleaning or related processing of account records.

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


Standard Objects AccountCleanInfo

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

Address

AnnualRevenue

City

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The unique, system-generated ID assigned when the account record was created.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Information about the account’s location, such as single location, headquarters,
or branch.

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


Standard Objects AccountCleanInfo

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Details for the billing address of the account.

```
CleanedByJob

CleanedByUser

CompanyName

CompanyStatusDataDotCom

Country

```

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

**Description**
Indicates whether the account record was cleaned by a Salesforce user ( `true` )
or not ( `false` ).

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


Standard Objects AccountCleanInfo

**Field Name** **Details**

**Description**
Details for the billing address of the account.

```
DandBCompanyDunsNumber

DataDotComId

Description

DunsNumber

DunsRightMatchConfidence

```

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


Standard Objects AccountCleanInfo

**Field Name** **Details**

```
DunsRightMatchGrade

Fax

Industry

IsDifferentAccountSite

IsDifferentAnnualRevenue

IsDifferentCity

```

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

**Properties**
Filter, Group, Nillable, Sort

**Description**
The industry the account belongs to.

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


Standard Objects AccountCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the account’s `City` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

```
IsDifferentCompanyName

IsDifferentCountry

IsDifferentCountryCode

IsDifferentDandBCompanyDunsNumber

IsDifferentDescription

```

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

**Description**
Indicates whether the account’s `Country` field value is different from the
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
Indicates whether the account’s `DandBCompanyID` field value is different
from the corresponding value on its matched Data.com record ( `true` ) or not
( `false` ).

**Type**
boolean

**Properties**
Filter


Standard Objects AccountCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the account’s `Description` field value is different from
the corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

```
IsDifferentDunsNumber

IsDifferentFax

IsDifferentIndustry

IsDifferentNaicsCode

IsDifferentNaicsDescription

```

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

**Description**
Indicates whether the account’s `Fax` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

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


Standard Objects AccountCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the account’s `NaicsDescription` field value is different
from the corresponding value on its matched Data.com record ( `true` ) or not
( `false` ).

```
IsDifferentNumberOfEmployees

IsDifferentOwnership

IsDifferentPhone

IsDifferentPostalCode

IsDifferentSic

```

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

**Description**
Indicates whether the account’s `Ownership` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

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


Standard Objects AccountCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the account’s `Sic` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

```
IsDifferentSicDescription

IsDifferentState

IsDifferentStateCode

IsDifferentStreet

IsDifferentTickerSymbol

```

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

**Description**
Indicates whether the account’s `State` field value is different from the
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
Indicates whether the account’s `State` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter


Standard Objects AccountCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the account’s `TickerSymbol` field value is different from
the corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

```
IsDifferentTradestyle

IsDifferentWebsite

IsDifferentYearStarted

IsFlaggedWrongAccountSite

IsFlaggedWrongAddress

```

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

**Description**
Indicates whether the account’s `Website` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

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


Standard Objects AccountCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the account’s `Address` field value is flagged as wrong to
Data.com ( `true` ) or not ( `false` ).

```
IsFlaggedWrongAnnualRevenue

IsFlaggedWrongCompanyName

IsFlaggedWrongDescription

IsFlaggedWrongDunsNumber

IsFlaggedWrongFax

```

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

**Description**
Indicates whether the account’s `CompanyName` field value is flagged as wrong
to Data.com ( `true` ) or not ( `false` ).

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


Standard Objects AccountCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the account’s `Fax` field value is flagged as wrong to Data.com
( `true` ) or not ( `false` ).

```
IsFlaggedWrongIndustry

IsFlaggedWrongNaicsCode

IsFlaggedWrongNaicsDescription

IsFlaggedWrongNumberOfEmployees

IsFlaggedWrongOwnership

```

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

**Description**
Indicates whether the account’s `NaicsCode` field value is flagged as wrong
to Data.com ( `true` ) or not ( `false` ).

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


Standard Objects AccountCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the account’s `Ownership` field value is flagged as wrong
to Data.com ( `true` ) or not ( `false` ).

```
IsFlaggedWrongPhone

IsFlaggedWrongSic

IsFlaggedWrongSicDescription

IsFlaggedWrongTickerSymbol

IsFlaggedWrongTradestyle

```

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

**Description**
Indicates whether the account’s `Sic` field value is flagged as wrong to Data.com
( `true` ) or not ( `false` ).

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


Standard Objects AccountCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the account’s `Tradestyle` field value is flagged as wrong
to Data.com ( `true` ) or not ( `false` ).

```
IsFlaggedWrongWebsite

IsFlaggedWrongYearStarted

IsInactive

IsReviewedAccountSite

IsReviewedAddress

```

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

**Description**
Indicates whether the account’s `YearStarted` field value is flagged as wrong
to Data.com ( `true` ) or not ( `false` ).

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


Standard Objects AccountCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the account’s `Address` field value is in a `Reviewed` state
( `true` ) or not ( `false` ).

```
IsReviewedAnnualRevenue

IsReviewedCompanyName

IsReviewedDandBCompanyDunsNumber

IsReviewedDescription

IsReviewedDunsNumber

```

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

**Description**
Indicates whether the account’s `CompanyName` field value is in a `Reviewed`
state ( `true` ) or not ( `false` ).

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


Standard Objects AccountCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the account’s `DunsNumber` field value is in a `Reviewed`
state ( `true` ) or not ( `false` ).

```
IsReviewedFax

IsReviewedIndustry

IsReviewedNaicsCode

IsReviewedNaicsDescription

IsReviewedNumberOfEmployees

```

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

**Description**
Indicates whether the account’s `Industry` field value is in a `Reviewed`
state ( `true` ) or not ( `false` ).

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


Standard Objects AccountCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the account’s `NumberOfEmployees` field value is in a
`Reviewed` state ( `true` ) or not ( `false` ).

```
IsReviewedOwnership

IsReviewedPhone

IsReviewedSic

IsReviewedSicDescription

IsReviewedTickerSymbol

```

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

**Description**
Indicates whether the account’s `Phone` field value is in a `Reviewed` state
( `true` ) or not ( `false` ).

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


Standard Objects AccountCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the account’s `TickerSymbol` field value is in a `Reviewed`
state ( `true` ) or not ( `false` ).

```
IsReviewedTradestyle

IsReviewedWebsite

IsReviewedYearStarted

LastMatchedDate

LastStatusChangedById

```

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

**Description**
Indicates whether the account’s `Website` field value is in a `Reviewed` state
( `true` ) or not ( `false` ).

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


Standard Objects AccountCleanInfo

**Field Name** **Details**

```
LastStatusChangedDate

Latitude

Longitude

NaicsCode

NaicsDescription

Name

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


Standard Objects AccountCleanInfo

**Field Name** **Details**

**Properties**
Filter, Group, Sort, Update

**Description**
Field label is **Account Clean Info Name** . The name of the account. Maximum
size is 255 characters.

```
NumberOfEmployees

Ownership

Phone

PostalCode

Sic

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of employees working at the account.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
Ownership type for the account, for example Private, Public, or Subsidiary.

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


Standard Objects AccountCleanInfo

**Field Name** **Details**

```
SicDescription

State

Street

TickerSymbol

Tradestyle

Website

```

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


Standard Objects AccountCleanInfo

**Field Name** **Details**

**Description**
The website of the account.

```
YearStarted

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The year the company was established or the year when current ownership or
management assumed control of the company.

Administrators can modify a limited set of AccountCleanInfo fields from the Account Clean Info page.

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


### Standard Objects AccountContactRole

**•** Read the `CleanStatus` field value on the Account object. If that value is `Different`, but a Salesforce record has no street
address value, update the record’s status to `Not Compared` .

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AccountCleanInfoChangeEvent (API version 62.0)**
Change events are available for the object.

### AccountContactRole

Represents the role that a Contact plays on an Account.

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

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the Account.

This is a relationship field.

**Relationship Name**
### Account

**Relationship Type**
Lookup

**Refers To**
### Account

**Type**
reference


Standard Objects AccountContactRole

**Field** **Details**

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

```
IsDeleted

IsPrimary

Role

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


### Standard Objects AccountInsight

Usage

Use this object to define the role that a Contact plays on a given Account within the context of a specific Opportunity.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**AccountContactRoleChangeEvent (API version 44.0)**
Change events are available for the object.

SEE ALSO:

### Account

Contact

### AccountInsight

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


Standard Objects AccountInsight

**Field Name** **Details**

**Description**
Reserved for future use.

```
CompetitorName

ContactName

ContactTitle

CurrencyIsoCode

Division

ExpectedHeardWithinDays

```

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


Standard Objects AccountInsight

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reserved for future use.

```
LastHeard

LastReferencedDate

LastViewedDate

NumberOfNewsArticles

Rationale

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Reserved for future use.

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


### Standard Objects AccountOwnerSharingRule

**Field Name** **Details**

**Description**
The explanation for an insight, providing more background information and
details that are specific to the org.

```
Title

TrendType

Type

```

Usage

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

**•** M&A activity detected

**•** Company is expanding

**•** Leadership changes

This object is read-only and isn’t supported with workflows, triggers, or process builder.

### AccountOwnerSharingRule

Represents the rules for sharing an account with a User other than the owner.

Note: To programmatically update owner sharing rules, we recommend that you use Metadata API. Contact Salesforce customer
support to enable access to this object for your org.


Standard Objects AccountOwnerSharingRule

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
AccountAccessLevel

CaseAccessLevel

ContactAccessLevel

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


Standard Objects AccountOwnerSharingRule

**Field** **Details**

**•** `Edit`

Note: When `DefaultContactAccess` is set to `Controlled by Parent`,
you can’t create or update this field.

```
Description

DeveloperName

GroupId

OpportunityAccessLevel

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
The ID representing the source group. An Account owned by a User in the source Group
triggers the rule to give access.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


Standard Objects AccountOwnerSharingRule

**Field** **Details**

**Description**
A value that represents the type of access granted to the target Group for any associated
Opportunity. The possible values are:

**•** `None`

**•** `Read`

**•** `Edit`

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


### Standard Objects AccountPartner

[Note: The original territory management feature is now unavailable. For more information, see The Original Territory Management](https://help.salesforce.com/articleView?id=The-original-Territory-Management-module-will-be-retired-in-the-Summer-20-release&language=en_US&type=1)
[Module Will Be Retired in the Summer ’21 Release. The information in this topic applies to the original territory management](https://help.salesforce.com/articleView?id=The-original-Territory-Management-module-will-be-retired-in-the-Summer-20-release&language=en_US&type=1)
feature only, and not to Enterprise Territory Management.

SEE ALSO:

### Account

AccountShare

_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_sharingrules.htm)_ : SharingRules

### AccountPartner

This object represents a partner relationship between two Account records. An AccountPartner record is created automatically when a
Partner record is created for a partner relationship between two accounts. An AccountPartner record is also created automatically
between an account and an opportunity’s account when a Partner record is created between an account and an opportunity.

Note: This object is completely distinct from and independent of Account records that have been enabled for the partner portal.

Supported Calls

`create()`, `delete()`, `describeLayout()describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Customer Portal users can't access this object.

Fields

**Field** **Details**

```
AccountFromId

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
### Account


Standard Objects AccountPartner

**Field** **Details**

```
AccountToId

IsPrimary

OpportunityId

ReversePartnerId

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

**Description**
Indicates whether the AccountPartner is the primary partner of an opportunity ( `true` ).
When there are no corresponding Opportunity Partner records, the value is `false` .

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


### Standard Objects AccountPlan

**Field** **Details**

**Description**
ID of the reciprocal AccountPartner record in a partner relationship.

```
Role

```

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


Standard Objects AccountPlan

Fields

**Field** **Details**

```
AccountChallenges

AccountCmptvWeaknesses

AccountCompetitiveStrengths

AccountCompetitors

AccountId

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


Standard Objects AccountPlan

**Field** **Details**

**Refers To**
Account

```
AccountIndustryTrends

AccountInternalRiskRating

AccountPrfmIndicators

AccountStrategicPriorities

AccountVision

CallingStrategy

```

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


Standard Objects AccountPlan

**Field** **Details**

**Properties**
Create, Nillable, Update

**Description**
How frequently the relationship team meets with the account. To access this field, you must
have an FSC Sales or a Financial Services Cloud Extension license.

```
CallingStrategyNotes

EndDate

FlexCard

LastReferencedDate

LastViewedDate

```

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

**Description**
The end date of the account plan.

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


Standard Objects AccountPlan

**Field** **Details**

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
and `LastReferenceDate` isn’t null, the user accessed this record or list view indirectly.

```
Name

Notes

OwnerId

RelationshipOpportunities

RelationshipStrengths

```

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


Standard Objects AccountPlan

**Field** **Details**

**Description**
The strengths in the relationship with the account.

```
RelationshipSummary

RelationshipThreats

RelationshipWeaknesses

StartDate

Status

```

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


### Standard Objects AccountPlanObjective

**Field** **Details**

**•** `Not Started`

The default value is `Not Started` .

Associated Objects

This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**[AccountPlanChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[AccountPlanHistory](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[AccountPlanOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_accountownersharingrule.htm)**

Sharing rules are available for the object.

**[AccountPlanShare](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_accountshare.htm)**

Sharing is available for the object.

### AccountPlanObjective

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

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The account plan associated with the objective.

This field is a relationship field.


Standard Objects AccountPlanObjective

**Field** **Details**

**Relationship Name**
AccountPlan

**Relationship Type**
Master-detail

**Refers To**
AccountPlan

```
AccountPlanObjCategoryId

Description

EndDate

ExternalStakeholderId

```

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

**Refers To**
AccountPlanObjectiveCategory

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


Standard Objects AccountPlanObjective

**Field** **Details**

**Description**
The customer stakeholder contact associated with the account plan objective. The relationship
team collaborates with the customer stakeholder to achieve a specific objective. To access
this field, you must have an FSC Sales or a Financial Services Cloud Extension license.

This field is a relationship field.

**Relationship Name**
ExternalStakeholder

**Refers To**
Contact

```
LastInteractionSumGenDate

LastReferencedDate

LastViewedDate

Name

```

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
The name of the account plan objective.


Standard Objects AccountPlanObjective

**Field** **Details**

```
ObjectiveInteractionSummary

ObjectiveOwnerId

OwnerId

Priority

```

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


### Standard Objects AccountPlanObjectiveMeasure

**Field** **Details**

Possible values are:

**•** `High`

**•** `Low`

**•** `Medium`

```
StartDate

Status

```

Associated Objects

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

**•** `In Progress`

**•** `New`

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


Standard Objects AccountPlanObjectiveMeasure

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available if sales account plans are turned on.

Fields

**Field** **Details**

AccountPlanObjMeasCalcDefId

```
AccountPlanObjectiveId

CurrentCurrencyValue

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The account plan objective calculation definition associated with the measure.

This field is a relationship field. Available in API version 63.0 and later.

**Relationship Name**
AccountPlanObjMeasCalcDef

**Refers To**
AccountPlanObjMeasCalcDef

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


Standard Objects AccountPlanObjectiveMeasure

**Field** **Details**

**Description**
The current value in currency for a measure associated with the account plan objective.

```
CurrentNumberValue

CurrentPercentValue

CurrentValue

```

CurrentValueTimestamp

```
LastReferencedDate

LastViewedDate

```

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


Standard Objects AccountPlanObjectiveMeasure

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record. If this value is null, it’s possible
that this record was referenced (LastReferencedDate) and not viewed.

```
Name

TargetCurrencyValue

TargetNumberValue

TargetPercentValue

TargetValue

```

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

**Description**
The target value in currency for a measure associated with the account plan objective.

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


### Standard Objects AccountPlanObjMeasCalcCond

**Field** **Details**

```
ValueType

```

Associated Objects

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

```

**Type**
reference


Standard Objects AccountPlanObjMeasCalcCond

**Field** **Details**

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

```
FieldName

Operation

Value

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A field on the calculation definition’s `TargetObject` that you want to filter by. Fields on
the Campaign, Case, Contact, or Opportunity objects are supported.

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


### Standard Objects AccountPlanObjMeasCalcDef

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The value to match for the specified field.

Usage

Let’s say that a calculation definition tracks the currency amount on Closed Won opportunities. The calculation definition’s
`TargetObject` is `Opportunity`, and the condition further specifies these values.

**•** `FieldName` is `StageName` .

**•** `Operation` is `Equals` .

**•** `Value` is `ClosedWon` .

### AccountPlanObjMeasCalcDef

Represents the definition of a target object, rollup field, and logic for calculating the current value of a sales account plan objective
measure. This object is available in API version 63.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

This object is available if sales account plans are turned on.

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
A summary of the calculation definition that’s visible to users when they select the definition
for an account plan objective measure.

**Type**
string


Standard Objects AccountPlanObjMeasCalcDef

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
The combined language and locale ISO code, which controls the language of the calculation
definition.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label for this calculation definition. This display value is the internal label that doesn't get
translated.

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


Standard Objects AccountPlanObjMeasCalcDef

**Field** **Details**

field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that aren’t Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

```
RollupType

Status

TargetField

```

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

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Possible values are:

**•** `Active`

**•** `Draft`

**•** `Inactive`

Only active calculation definitions are available for users to select when they specify an
account plan objective measure.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The field on `TargetObject` to use for calculating the account plan objective measure’s
current value. Rollup fields on the Campaign, Case, Contact, or Opportunity object are
supported.

In Setup, this field’s label is Rollup Field.


### Standard Objects AccountPlanObjMeasCalcDefLocalization

**Field** **Details**

```
TargetObject

ValueType

```

Usage

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

**•** `Number`

**•** `Percent`

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


Standard Objects AccountPlanObjMeasCalcDefLocalization

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

ParentId

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
reference

**Properties**
Create, Filter, Group, Sort


### Standard Objects AccountPlanObjMeasRela

**Field** **Details**

**Description**
The ID of the related account plan objective measure calculation definition. This field is a
relationship field.

```
Value

```

Usage

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

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AccountPlanObjectiveMeasureId

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


Standard Objects AccountPlanObjMeasRela

**Field** **Details**

**Refers To**
AccountPlanObjectiveMeasure (the master object)

```
LastReferencedDate

LastViewedDate

Name

ReferenceRecordId

```

Associated Objects

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

**Description**
The name of the account plan objective measure relation record.

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


### Standard Objects AccountRelationship

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

Fields

**Field** **Details**

```
AccountFromID

AccountToId

LastReferencedDate

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


Standard Objects AccountRelationship

**Field** **Details**

```
LastViewedDate

Name

OwnerId

Type

```

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

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the user who created the account relationship.

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


### Standard Objects AccountRelationshipShareRule

**Field** **Details**

**•** Dealer

**•** Consultant

**•** Client

**•** Vendor

**•** Agent

**•** Retailer

**•** SubContractor

**•** Supplier

Picklist items can be updated with your own values.

Associated Objects

This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**AccountRelationshipFeed**

Feed tracking is available for the object.

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

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


Standard Objects AccountRelationshipShareRule

**Field** **Details**

**Description**
Type of access granted by the share rule. Valid values are:

**•** `Read` (Read Only)

**•** `Edit` (Read/Write)

```
AccountToCriteriaField

```

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
