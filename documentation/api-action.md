# Api action

> Source: https://resources.docs.salesforce.com/258/latest/en-us/sfdc/pdf/api_action.pdf
> Fetched: 2025-12-19T11:11:09Z
Actions Developer Guide
Developer Guide

Version 65.0, Winter ’26

Last updated: December 12, 2025

© Copyright 2000–2025 Salesforce, Inc. All rights reserved. Salesforce is a registered trademark of Salesforce, Inc., as are other
names and marks. Other marks appearing herein may be trademarks of their respective owners.

CONTENTS

**Chapter 1:** Introducing Actions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1**

Overview **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1**
Invoking Actions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2**
Available Actions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3**

**Chapter 2:** Action Objects **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7**

Apex Actions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7**
Assign Enablement Program **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9**
Apply Case Classification Recommendations **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10**
B2B and D2C Commerce Actions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11**

Commerce Checkout Flow Actions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11**
Create Subscription Records Action **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12**
Process First Payment Billing for Subscriptions Action **. . . . . . . . . . . . . . . . . . . . . . . . . . 14**
Record Tax Reversal Action **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16**
Record Tax Transaction Action **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18**
Commerce Checkout Flow Actions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20**
Create Service Document Actions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20**
Create Service Report Actions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23**
Custom Notification Actions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24**
Deploy Data Kit Components Action **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27**
Email Alert Actions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32**
Einstein Bots Actions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33**

Get Data Category Details **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33**
Get Data Category Groups **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34**
Search Knowledge Articles **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35**
Explore Conversation Actions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36**
Flow Actions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39**
Generate Order Summary Action **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40**
Generate Work Orders Actions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41**
Get Assessment Response Summary **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42**
Get Conversation Intelligence Action **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45**
Get Conversation Transcript Action **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50**
Get Data Graph Data By Lookup **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55**
Get Data Graph Metadata **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57**
Knowledge Actions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58**
Lead Action **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69**
Live Message Notification Actions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71**
Omni-Channel Action **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74**
Apply Payment Action **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75**

**Contents**

Payment Sale Action **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77**
Perform Survey Sentiment Analysis **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79**
PlatformAction **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81**
Post to Chatter Actions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89**
Preview Cart to Exchange Order **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90**
Prompt Template Actions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92**
Quick Actions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93**
Refresh Metric Actions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94**
Sales Engagement Actions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95**
Salesforce Omnichannel Inventory Actions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104**
Salesforce Order Management Actions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105**
Send Conversation Messages Actions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106**
Send Notification Actions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109**
Session-Based Permission Set Actions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111**
Simple Email Actions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112**
Submit Exchange Order **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117**
Submit for Approval Actions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119**
Survey Invitation Actions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122**

Dynamic Send Survey Invitation Actions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122**
Send Survey Invitation Actions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125**
Work Plan and Work Step Actions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127**

# CHAPTER 1 Introducing Actions

Use actions to add more functionality to your applications. Choose from standard actions, such as posting to Chatter or sending email,
or create actions based on your company’s needs.

For example, you can:

**•** Add features and functionality to your existing Lightning Platform tools.

**•** Build dynamic modules for Lightning Platform development into your enterprise integration tools.

**•** Build specialized development tools for a specific application or service.

You can batch actions to improve performance in API version 35.0 and later.

## Overview

Actions allow you to build custom development tools for Lightning Platform applications.

Actions are about “getting things done” in Salesforce. They encapsulate a piece of logic that allows a user to perform some work, such
as sending email. When an action runs, it saves changes in your organization by updating the database.

Actions are easy to discover and use, and also easy to understand and implement. Every button and link in Salesforce can be considered
an action. A consistent Actions API and framework support the creation and distributed use of actions throughout Salesforce. Actions
are available in the REST API.

The types of actions are:

**Type** **Description**

InvocableAction

Invocable actions can be invoked from a common endpoint in the REST API. They provide “describe”
support – a programmatic mechanism to learn about all invocable actions on the platform.

There are two types of invocable actions.

**Standard action**
A standard action is ready to use right away. The work it performs is predefined, along with its
inputs and outputs, and they’re available in every organization.

**Custom action**
You create custom actions because these actions require a definition. For example, to use an
Apex action, create the Apex class method for the action.

QuickAction Quick Actions, formerly known as Publisher Actions, use page layouts to make it easy for administrators
to configure an action to create or update a record. The API always works with an sObject.

StandardButton Standard buttons are URLs allowing users to either go to another page (for example, the Edit page)
or accomplish some task (for example, lead conversion).

CustomButton Custom buttons are URLs that an administrator can specify and when included on a page and clicked,
will redirect a user to that URL.

To call an action from a flow, use `FlowActionCall`, as described in the _[Metadata API Developer’s Guide.](https://developer.salesforce.com/docs/atlas.en-us.258.0.api_meta.meta/api_meta/)_

1

## Introducing Actions Invoking Actions

The `If-Modified-Since` header can be used with actions, with a date format of `EEE, dd MMM yyyy HH:mm:ss z` .
When this header is used, if the action metadata has not changed since the provided date, a `304 Not Modified` status code is
returned, with no response body.

SEE ALSO:

_[REST API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.258.0.api_rest.meta/api_rest/resources_actions_invocable.htm)_ : Invocable Actions

## Invoking Actions

Most actions are invoked using the same JSON body format. The top-level JSON key name must be `inputs` .

Note: Invoke Salesforce Order Management actions with the corresponding Connect REST API resources or Apex ConnectApi
methods, not the standard endpoints.

The following example request shows two Chatter posts made with a single Post to Chatter action.

```
   POST /services/data/v XX.X /actions/standard/chatterPost

   { "inputs" :

     [

     {

      "subjectNameOrId" : "jsmith@salesforce.com",

      "type" : "user",

      "text" : "first chatter post!"

     },

     {

      "subjectNameOrId" : "hsmith@salesforce.com",

      "type" : "user",

      "text" : "second chatter post!"

     }

     ]

   }

```

Here is the response.

```
   [ {

     "actionName" : "chatterPost",

     "errors" : null,

     "isSuccess" : true,

     "outputValues" : {

      "feedItemId" : "0D5D0000000kynqKBA"

     }

   }, {

     "actionName" : "chatterPost",

     "errors" : null,

     "isSuccess" : true,

     "outputValues" : {

      "feedItemId" : "0D5D0000000kynrKBz"

     }

   } ]

```

Standard actions return their name in `actionName` . The value of `actionName` varies for custom actions.

2

## Introducing Actions Available Actions

SEE ALSO:

_[REST API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.258.0.api_rest.meta/api_rest/resources_actions_invocable.htm)_ : Invocable Actions

## Available Actions

The available actions are:

**Action** **Description**

Apex Actions Invoke Apex methods annotated with `@InvocableMethod` and include
custom parameters with `@InvocableVariable` .

Apply Payment Action Applies a payment record to an invoice header by creating a PaymentLineInvoice
record with a type of Applied.

Apply Case Classification Recommendations Applies Einstein’s recommended values for fields on a given case record, and
returns the updated case record.

[Assign Candidates to Research Study Group Action](https://developer.salesforce.com/docs/atlas.en-us.258.0.life_sciences_dev_guide.meta/life_sciences_dev_guide/actions_obj_assign_candidate_to_research_study_group.htm) Randomly assign candidates, enrolled in the clinical trials, to research study
comparison groups.

[Asset Lifecycle Actions](https://developer.salesforce.com/docs/atlas.en-us.258.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/asset_lifecycle_invocable_actions_parent.htm) Create or update an asset from an order or order item. Additionally, initiate the
amendment, cancellation, or renewal of an asset.

Assign Enablement Program Automatically assign a user to an Enablement program.

[Batch Management Actions](https://developer.salesforce.com/docs/atlas.en-us.258.0.loyalty.meta/loyalty/batch_mgt_actions_parent.htm) Manage your Batch Management jobs by using invocable actions.

[Billing Actions](https://developer.salesforce.com/docs/atlas.en-us.258.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/billing_invocable_actions_parent.htm) Manage billing operations by using invocable actions.

B2B and D2C Commerce Actions

Manage B2B Commerce integrations and store checkout flow. Record and reverse
tax transactions in external systems like Stripe based on order changes, and create
subscription records for orders with subscription products.

Commerce Checkout Flow Actions Manage Commerce integrations and store checkout flow.

[Context Service Actions](https://developer.salesforce.com/docs/atlas.en-us.258.0.industries_reference.meta/industries_reference/context_service_invocable_actions_parent.htm) Work with context data using invocable actions.

3

Introducing Actions Available Actions

**Action** **Description**

Create Service Report Actions Creates a service report for a service appointment, work order, or work order line
item.

Custom Notification Actions Send custom notifications to recipients via desktop or mobile channels.

[Decision Table Actions](https://developer.salesforce.com/docs/atlas.en-us.258.0.loyalty.meta/loyalty/dt_actions_parent.htm) Invokes a decision table or refreshes business rules for an active decision table.

[Data Processing Engine Actions](https://developer.salesforce.com/docs/atlas.en-us.258.0.loyalty.meta/loyalty/dpe_actions_parent.htm) Runs an active Data Processing Engine definition.

Deploy Data Kit Components Action Deploys data kit components of a package to a target org via a flow action.

[Dynamic Revenue Orchestrator Actions](https://developer.salesforce.com/docs/atlas.en-us.258.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/dynamic_revenue_orchestrator_invocable_actions_parent.htm) Submit an order or a sales transaction to Dynamic Revenue Orchestrator (DRO)
for fulfillment.

[Dynamic Revenue Orchestrator Actions](https://developer.salesforce.com/docs/atlas.en-us.258.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/dynamic_revenue_orchestrator_invocable_actions_parent.htm) Run rules for a specific quote or order based on a context ID or transaction ID, and
process other steps that are part of the configuration directly within a Flow.

Email Alert Actions Send emails from flows by reusing already-configured workflow email alerts.

Einstein Bots Actions Search for knowledge articles based on data category and data category groups.

[Einstein Visit Recommendation Action](https://developer.salesforce.com/docs/atlas.en-us.258.0.retail_api.meta/retail_api/einstein_visit_recommendation_actions_parent.htm) Save visit and task recommendation decisions.

Explore Conversation on page 36 Answer a user's questions about a voice or video call based on the contents of the
call transcript.

[Financial Services Cloud Actions](https://developer.salesforce.com/docs/atlas.en-us.258.0.financial_services_cloud_object_reference.meta/financial_services_cloud_object_reference/fsc_actions_parent.htm) Create person accounts, financial accounts, and related records from a residential
loan application for Financial Services Cloud.

Flow Actions Invoke an active autolaunched flow or active invocable process that exists in the
current org.

[Fundraising for Nonprofit Cloud Actions](https://developer.salesforce.com/docs/atlas.en-us.258.0.nonprofit_cloud.meta/nonprofit_cloud/fundraising_actions_parent.htm) Manage gift commitments, gift commitment schedules, gift default schedules,
gift transaction designations, and gift entries for Fundraising.

Generate Order Summary Action Generate a URL so that authenticated and guest users can access order details.

[Generate Research Study Block Action](https://developer.salesforce.com/docs/atlas.en-us.258.0.life_sciences_dev_guide.meta/life_sciences_dev_guide/actions_obj_generate_research_study_blocks.htm) Generate research study randomization block records to link each block with a
specific research study comparison group by using the randomization process.

Generate Work Orders Actions Generates work orders from a maintenance plan.

Get Conversation Intelligence Gets intelligence information about a voice or video call, including any insights
and a conversation summary.

Get Conversation Transcript Gets a transcript for a voice or video call.

Get Data Graph Data By Lookup Get data of a data graph by data graph API name, data space name, and lookup
key.

Get Data Graph Data By Lookup Get metadata of a data graph by data graph API name and data space name.

[Get Personalization Decisions](https://developer.salesforce.com/docs/marketing/einstein-personalization/guide/get-personalization-decision-invocable-action-reference.html) Get personalized decisions from Salesforce Personalization for the specified context
and personalization point.

[Health Cloud Actions](https://developer.salesforce.com/docs/atlas.en-us.258.0.health_cloud_object_reference.meta/health_cloud_object_reference/hc_actions_parent.htm) Automate healthcare-related tasks using invocable actions.

4

Introducing Actions Available Actions

**Action** **Description**

[Initiate Natural Language Processing Action](https://developer.salesforce.com/docs/atlas.en-us.258.0.industries_reference.meta/industries_reference/actions_obj_initiate_nlp.htm) Create a record for the AI natural language processing result and initiate text
processing by using the service specified in the related record.

[Insurance Brokerage Actions](https://developer.salesforce.com/docs/atlas.en-us.258.0.insurance_developer_guide.meta/insurance_developer_guide/insurance_brokerage_invocable_actions_parent.htm) Use the invocable actions to streamline operations and deliver personalized
experiences for all Insurance Brokerage lines of business.

[Insurance Claims Actions](https://developer.salesforce.com/docs/atlas.en-us.258.0.insurance_developer_guide.meta/insurance_developer_guide/insurance_claim_invocable_actions_parent.htm) Use the Insurance Claims invocable actions to manage insurance claims journey.

[Insurance Group Benefits Actions](https://developer.salesforce.com/docs/atlas.en-us.258.0.insurance_developer_guide.meta/insurance_developer_guide/insurance_group_benefits_invocable_actions_parent.htm) Use the invocable actions to effectively manage the insurance plans offered to
groups, such as employees and their dependents.

[Insurance Policy Actions](https://developer.salesforce.com/docs/atlas.en-us.258.0.insurance_developer_guide.meta/insurance_developer_guide/insurance_policy_invocable_actions_parent.htm) Manage the insurance policy lifecycle by using the invocable actions.

[Insurance Quoting Actions](https://developer.salesforce.com/docs/atlas.en-us.258.0.insurance_developer_guide.meta/insurance_developer_guide/quote_invocable_actions_parent.htm) Manage the insurance quoting journey by using the invocable actions.

Knowledge Actions Manage your Knowledge articles by using invocable actions.

Live Message Notification Actions

Use messaging templates to send notifications to users over communication
channels, such as SMS, WhatsApp, and Facebook Messenger, when certain
conditions are met.

[Loyalty Management Actions](https://developer.salesforce.com/docs/atlas.en-us.258.0.loyalty.meta/loyalty/loyalty_mgt_actions_parent.htm) Create and manage loyalty programs for your organization by using the standard
and custom invocable actions.

[Manufacturing Cloud Actions](https://developer.salesforce.com/docs/atlas.en-us.258.0.mfg_api_devguide.meta/mfg_api_devguide/mfg_actions_parent.htm) Automate business processes related to account forecast, sales agreements, and
account manager target values.

[Media Integration Procedure Action](https://developer.salesforce.com/docs/atlas.en-us.258.0.media_developer_guide.meta/media_developer_guide/media_industries_dev_guide/actions_obj_media_integration_procedure.htm) Call an Integration Procedure from a Salesforce Flow to process media content.

[Net Zero Cloud Actions](https://developer.salesforce.com/docs/atlas.en-us.258.0.netzero_cloud_dev_guide.meta/netzero_cloud_dev_guide/net_zero_cloud_invocable_actions_parent.htm) Track and manage environmental impact for precise calculation and analysis of
carbon emissions.

Omni-Channel Action Create a `PendingServiceRouting` record used for Omni-Channel
skills-based routing.

Payment Sale Action Capture a payment without any prior authorization and create a payment record.
The payment sale transaction consists of an authorize request and a capture request

made to the payment gateway at the same time. This way, the merchant can
request funds to be transferred to the merchant account in a single command,
with no further action required.

PlatformAction

PlatformAction is a virtual read-only object. It enables you to query for actions
displayed in the UI, given a user, a context, device format, and a record ID. Examples
include standard and custom buttons, quick actions, and productivity actions.

Post to Chatter Actions Post a message to a specified feed, such as to a Chatter group or a case record.
The message can contain mentions and topics, but only text posts are supported.

Preview Cart to Exchange Order Generate preview details of an exchange order for specified order summary,
exchange cart ID, and reference record ID.

[Product Discovery Standard Invocable Actions](https://developer.salesforce.com/docs/atlas.en-us.258.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/product_discovery_invocable_actions_parent.htm) Find and retrieve product, category, and catalog details. Additionally, execute a
qualification procedure, and search products with guided selection.

5

Introducing Actions Available Actions

**Action** **Description**

Prompt Template Actions Generate a response based on the large language model (LLM) response for the
specified prompt template and inputs.

Process Compliance Navigator Actions Use the invocable actions to evaluate the compliance validation procedures and
get the job details.

[Public Sector Solutions Actions](https://developer.salesforce.com/docs/atlas.en-us.258.0.psc_api.meta/psc_api/psc_standard_invocable_action_api_parent.htm) Create a benefit disbursement for an eligible benefit assignment or run a Data
Processing Engine definition to process an asynchronous batch job.

Quick Actions Use a quick action to create a task or a case. Invoke existing quick actions, both
global and object-specific, to create records, update records, or log calls.

[Quote and Order Capture Actions](https://developer.salesforce.com/docs/atlas.en-us.258.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/qoc_invocable_actions_parent.htm) Create an order from a quote record.

[Rebate Management Actions](https://developer.salesforce.com/docs/atlas.en-us.258.0.rebates_api_devguide.meta/rebates_api_devguide/rebate_actions_parent.htm) Create and manage rebate programs and manage payouts and transactions by
using the Rebate Management invocable actions.

[Referral Marketing Actions](https://developer.salesforce.com/docs/atlas.en-us.258.0.referral_marketing.meta/referral_marketing/referral_actions_parent.htm) Create and manage referral programs for your organization.

Refresh Metric Actions Update a metric’s Current Value field if it’s linked to a summary field in a Salesforce
report. The refresh runs as the metric owner.

Sales Engagement Actions Manage cadence targets by using invocable actions.

Salesforce Omnichannel Inventory Actions Manage inventory availability and provide omnichannel commerce experiences
in flows with Salesforce Omnichannel Inventory.

Salesforce Order Management Actions Manage, fulfill, and service orders in flows with Salesforce Order Management.

[Salesforce Pricing Actions](https://developer.salesforce.com/docs/atlas.en-us.258.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/pricing_invocable_actions_parent.htm)

Invoke the Pricing Connect API by providing the context, pricing procedure, and
price waterfall details. Additionally, you can also specify the pricing data and details
of a context to invoke the Pricing Connect API.

Send Notification Actions Call a notification type to send. Each Send Notification action corresponds to an
available notification type.

Session-Based Permission Set Actions Activate or deactivate a session-based permission set for the current user’s API
session.

Simple Email Actions Send an email where you specify the subject, body, and recipients.

Submit for Approval Actions Submit a Salesforce record for approval if an approval process is defined for the
current entity.

Submit Exchange Order Submits an exchange order based on the specified information.

Survey Invitation Actions

Send email survey invitations to leads, contacts, and users in your org based on
an action. Also, send customized notifications to users about important events or
updates to the records that they’re working on.

[Usage Management Actions](https://developer.salesforce.com/docs/atlas.en-us.258.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/usage_management_invocable_actions_parent.htm) Manage consumption of usage-based products by using the invocable actions.

Search Contract Document Action Search the latest contract document version based on the user's query.

6

# CHAPTER 2 Action Objects

This is the reference for quick actions and dynamic actions. Invocable actions are also known as dynamic actions.

## Apex Actions

Invoke Apex methods annotated with `@InvocableMethod` and include custom parameters with `@InvocableVariable` .

This object is available in API version 33.0 and later.

Supported REST HTTP Methods

**URI**
Get a list of available Apex actions:

```
  /services/data/v XX.X /actions/custom/apex

```

Get information about a specific Apex action:

```
  /services/data/v XX.X /actions/custom/apex/ action_name

```

**Formats**
JSON, XML

**HTTP Methods**
GET, HEAD, POST

**Authentication**

```
  Authorization: Bearer token

```

**Parameters**
None

**Example**
This example invokes the Apex action called `ActionTestWithSObject`, which takes a list of Accounts, increases the employee
count for each account by one, and returns an updated list of account IDs. The top-level key name in the JSON request body must
be `inputs` .

7

Action Objects Apex Actions

```
       "objects": {

       "attributes" : {

        "type" : "Account"

       },

       "Name": "Global Media"

       }

      }

      ]

     }

```

Here’s the Apex code.

```
     public class ActionTestWithSObject {

     @InvocableMethod(label='Action Test With sObject' description='Given a list of sObjects

      (Accounts), increase employee count by one and return account ID' category='Account')

      public static List<String> getAccountNames(List<Account> objects) {

      List<String> accountIds = new List<String>();

      Map<Id, Account> accountsMap = new Map<Id, Account>(objects);

      Map<Id, Account> retrievedAccountMap = new Map<Id, Account>([SELECT Id,

     NumberOfEmployees FROM Account WHERE Id in :accountsMap.keySet()]);

      for (Account a : objects) {

       Account ra = retrievedAccountMap.get(a.Id);

       ra.NumberOfEmployees = ra.NumberOfEmployees == null ? 1 : ra.NumberOfEmployees + 1;

       accountIds.add(ra.Id);

      }

      update retrievedAccountMap.values();

      return accountIds;

      }

     }

```

Note: The resource is the name of the Apex class, not the Apex method. In this example, the resource is
`/ActionTestWithSObject`, not `/getAccountNames` .

**Notes**

**•** Describe and invoke for an Apex action respect the profile access for the Apex class. If you don’t have access, an error is issued.

**•** Describe for an Apex action returns only one level of fields for Apex-defined inputs or outputs. You can access top-level fields,
but not the fields of any nested Apex-defined objects.

**•** If you add an Apex action to a flow, and then remove the `@InvocableMethod` annotation from the Apex class, you get a
runtime error in the flow.

**•** If an Apex action is used in a flow, packageable components that reference these elements aren’t automatically included in the
package. To deploy the package successfully, manually add those referenced components to the package.

**•** An Apex invocable action can be declared `public` or `global` in a managed package. However, that action doesn’t appear
in Flow Builder’s list of available Apex actions. Flows within the same managed package can still refer to these invocable actions.
Global Apex invocable actions in a managed package can be used in flows outside the managed package, anywhere in the
organization, and appear in Flow Builder’s list of available Apex actions.

Inputs

Supply input values that correspond to the Apex action.

8

## Action Objects Assign Enablement Program

**•** A POST request body must use the JSON format specified in Invoking Actions.

**•** Apex methods annotated with `@InvocableMethod` must take a List as an input and return a List or `Null` . For more information,
see `[@InvocableMethod](https://developer.salesforce.com/docs/atlas.en-us.258.0.apexcode.meta/apexcode/apex_classes_annotation_InvocableMethod.htm)` Annotation in the _Apex Developer Guide_ .

**•** Only the following primitive types are supported as inputs in a POST request body:

**–** `Blob`

**–** `Boolean`

**–** `Date`

**–** `Datetime`

**–** `Decimal`

**–** `Double`

**–** `ID`

**–** `Integer`

**–** `Long`

**–** `String`

**–** `Time`

**•** Concrete types inherited from the sObject. In the previous example, the inherited concrete type is Account.

**•** A user-defined type, containing variables of the supported types and with the `InvocableVariable` annotation. To implement
your data type, create a custom global or public Apex class. The class must contain at least one member variable with the invocable
variable annotation.

Outputs

The Apex InvocableMethod determines the output values.

SEE ALSO:

Flow Actions

_Apex Developer Guide_ [: InvocableMethod Annotation](https://developer.salesforce.com/docs/atlas.en-us.258.0.apexcode.meta/apexcode/apex_classes_annotation_InvocableMethod.htm)

_[REST API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.258.0.api_rest.meta/api_rest/resources_actions_invocable.htm)_ : Invocable Actions

## Assign Enablement Program

Automatically assign a user to an Enablement program based on your determined criteria.

To assign users to an Enablement program, enable the Design and Deliver Enablement Programs user permission.

This object is available in API version 58.0 and later.

Supported REST HTTP Methods

**URI**

```
    /services/data/v58.0/actions/standard/assignEnablementProgram

```

**Formats**
JSON

9

## Action Objects Apply Case Classification Recommendations

**HTTP Methods**
POST

**Authentication**

```
    Authorization: Bearer token

```

Inputs

**Input** **Details**

```
assigneeId

notificationUserId

programId

startDate

```

Outputs

None

SEE ALSO:

**Type**
ID

**Description**
Required. The ID of the Enablement user to assign to the program.

**Type**
ID

**Description**
Required. The ID of another Salesforce user to notify when the program assignment is complete.

By default, a notification is sent to the user who runs this invocable action. Use
`notificationUserId` to specify another user that you want to notify.

**Type**
ID

**Description**
Required. The ID of the program being assigned.

**Type**
ID

**Description**
Required. The date that assignees can access the program. Dates for Saturdays and Sundays are
automatically set to the following Monday.

_Salesforce Help_ [: Automating Enablement Program Assignment](https://help.salesforce.com/s/articleView?id=sf.automated_program_assignment.htm&language=en_US)

## Apply Case Classification Recommendations

Recommends values for fields on a given case record. Requires an active Einstein Case Classification model.

10

## Action Objects B2B and D2C Commerce Actions

These actions are available in API version 55.0 and later.

Supported REST HTTP Methods

**URI**
Get a case SObject with recommended values for fields:

```
    /services/data/v XX.X /actions/standard/applyCaseClassificationRecommendations

```

**Formats**
JSON, XML

**HTTP Methods**
GET, HEAD, POST

**Authentication**

```
    Authorization: Bearer token

```

Inputs

**Input** **Details**

```
caseId

```

Outputs

**Type**
ID

**Description**
Required. The ID of a case.

**Input** **Details**

```
caseSObject

```

**Type**
SObject

**Description**
A case SObject with recommendations applied.

## B2B and D2C Commerce Actions

Manage B2B Commerce integrations and store checkout flow. Record and reverse tax transactions in external systems like Stripe based
on order changes, and create subscription records for orders with subscription products. For more information on standard invocable
actions, see **[REST API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.258.0.api_rest.meta/api_rest/resources_actions_invocable_standard.htm)** and **[Actions Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.258.0.api_action.meta/api_action/actions_intro.htm)** .

### Commerce Checkout Flow Actions

Manage your B2B Commerce integrations and create a custom checkout with Checkout Flow actions.

11

### Action Objects Create Subscription Records Action

[For more information about using Commerce Checkout Flow actions in flows, see B2B Commerce Checkout Flow Core Actions in](https://help.salesforce.com/HTViewHelpDoc?id=flow_ref_elements_b2b_comm_actions_list.htm&language=en_US)
Salesforce Help.

These actions are available in API version 50.0 and later.

Your org must have B2B Commerce enabled.

Supported REST HTTP Methods

**URI**
Get a specific B2B Commerce Checkout Flow action:

```
    /services/data/v XX.X /actions/standard/ checkout_flow_action_name

```

**Formats**
JSON, XML

**HTTP Methods**
GET

**Authentication**

```
    Authorization: Bearer token

```

**Notes**
[You can also call the corresponding Connect REST API endpoints or Apex ConnectApi methods. For more information, see B2B and](https://developer.salesforce.com/docs/atlas.en-us.258.0.chatterapi.meta/chatterapi/connect_resources_commerce.htm)
[B2B2C Commerce Resources in the](https://developer.salesforce.com/docs/atlas.en-us.258.0.chatterapi.meta/chatterapi/connect_resources_commerce.htm) _Connect REST API Developer Guide_ [and ConnectApi Namespace in the](https://developer.salesforce.com/docs/atlas.en-us.258.0.apexcode.meta/apexcode/apex_classes_connect_api.htm) _Apex Developer Guide_ .

### Create Subscription Records Action

Creates subscription records for orders containing subscription products. It accepts either the order summary ID or the order item
summary IDs as input, filters the subscription products, and creates records to manage them effectively.

Special Access Rules

This action is available in API version 63.0 and later for users with system administrator access or the Assetize Order permission set
assigned, along with any of the following licenses enabled:

**•** B2B Commerce, or D2C Commerce and Revenue Cloud Subscription Management. When this license is enabled in your org, both
`orderSummaryId` and `orderItemSummaryIds` are supported.

**•** B2B Commerce, or D2C Commerce and Revenue Lifecycle Management. When this license is enabled in your org, only
`orderSummaryId` is supported.

Supported REST HTTP Methods

**URI**

```
    /services/data/v XX.X /actions/standard/createSubscriptionRecords

```

**Formats**
JSON, XML

**HTTP Methods**
POST

**Authentication**

```
    Authorization: Bearer token

```

12

Action Objects Create Subscription Records Action

Inputs

**Input** **Details**

```
webStoreId

orderSummaryId

orderItemSummaryIds

```

Outputs

**Type**
String

**Description**
Required.

The ID of the web store associated with the order.

**Type**
String

**Description**
The ID of the order summary record.

This field is optional if `orderItemSummaryIds` is specified.

**Type**
String

**Description**
The list of the order item summary IDs.

This field is optional if `orderSummaryId` is specified.

**Output** **Details**

```
Subscription

ProcessedItems

```

Example

**Sample Request**

**Type**
STRING

**Description**
An array of order item summary IDs that are processed and have an associated subscription
record created.

Here’s a sample request with `orderSummaryID` and `webStoreID` :

```
{

  "inputs": [

   {

    "createSubscriptionRecords": {

     "orderSummaryId": "1OsJ3000000Gmd3KAC",

     "webStoreId": "0ZE5i000000PbfKGAS"

    }

```

13

### Action Objects Process First Payment Billing for Subscriptions Action

```
      }

     ]

   }

```

Here’s a sample request with `orderItemSummaryIDs` and `webStoreID` :

```
   {

     "inputs": [

      {

       "createSubscriptionRecords": {

        "orderItemSummaryIds": [

         "10uJ3000000GmczIAC", "10uJ3000000GmcyIAC"

        ],

        "webStoreId": "0ZE5i000000PbfKGAS"

       }

      }

     ]

   }

```

**Sample Response**

```
   [

     {

      "actionName": "createSubscriptionRecords",

      "errors": null,

      "isSuccess": true,

      "outputValues": {

       "SubscriptionProcessedItems": [

        "10uJ3000000GmczIAC",

        "10uJ3000000GmcyIAC"

       ]

      }

     }

   ]

### Process First Payment Billing for Subscriptions Action

```

Creates invoices for orders containing subscription products. When an order containing subscription products is placed in a B2B or D2C
store, the first term payment for subscription products is captured, but an invoice isn’t generated. This action uses Revenue Cloud’s
billing system to generate and settle a subscripition order’s first-term invoice and create a billing schedule for the subscription order.

Special Access Rules

This action is available in API version 63.0 and later for users with system administrator access or the BillingTransactionToBSApiUser,
InvoiceOrErrorRecoveryAPI, and RLMBilliingAccess users permissions assigned, along with any of these licenses enabled:

**•** B2B Commerce or D2C Commerce and Salesforce Payments

**•** Revenue Lifecycle Management and Salesforce Pricing

Supported REST HTTP Methods

**URI**

```
    /services/data/v XX.X /actions/standard/processFirstPaymentBilling

```

14

Action Objects Process First Payment Billing for Subscriptions Action

**Formats**
JSON, XML

**HTTP Methods**
GET, HEAD, POST

**Authentication**

```
    Authorization: Bearer token

```

Inputs

**Input** **Details**

```
correlationId

orderSummaryId

```

Outputs

**Type**
String

**Description**
The request correlation ID used for tracking the request.

**Type**
String

**Description**
The ID of the order summary record.

**Output** **Details**

```
correlationId

requestId

```

Example

**Sample Request**

**Type**
STRING

**Description**
The request correlationID used for tracking the request.

**Type**
STRING

**Description**
The ID of the request.

Here’s a sample request with `correlationId` and `orderSummaryId` :

```
{

  "inputs": [

   {

```

15

### Action Objects Record Tax Reversal Action

```
       "orderSummaryId": "1OsLT0000098gcu0AA",

       "correlationId": "4869bd78-3af4-40ff-8475-899d711b5db4"

      }

     ]

   }

```

**Sample Response**

```
   [

     {

      "actionName": "processFirstPaymentBilling",

      "errors": null,

      "invocationId": null,

      "isSuccess": true,

      "outcome": null,

      "outputValues": {

       "requestId": "fcec4cff-3f26-45fd-8193-0a599dbb7d03",

       "correlationId": "4869bd78-3af4-40ff-8475-899d711b5db4"

      },

      "sortOrder": -1,

      "version": 1

     }

   ]

### Record Tax Reversal Action

```

Reverses the recorded tax transactions in an external system, such as Stripe, after an order is returned or canceled.

This action is available in API version 62.0 and later for users with these licenses:

**•** B2B Commerce, or D2C Commerce

**•** Salesforce Order Management

Only store administrators can access this action.

Supported REST HTTP Methods

**URI**

```
    /services/data/v XX.X /actions/standard/recordTaxReversal

```

**Formats**
JSON, XML

**HTTP Methods**
POST

**Authentication**

```
    Authorization: Bearer token

```

16

Action Objects Record Tax Reversal Action

Inputs

**Input** **Details**

```
taxReversalInfos

```

Outputs

**Type**
Apex-defined

**Description**
Required.

A list of Apex `commercestoretax__TaxReversalInfo` records containing details
about the tax transactions for the order that was returned or canceled.

**Output** **Details**

```
taxReversalResult

```

Example

**Sample Request**

**Type**
Apex-defined

**Description**
An Apex `commercestoretax__TaxReversalResult` record containing details about
each tax transaction in the reversal request. The details include whether each reversal was
successful and, if not, any error messages returned.

```
{

  "inputs": [

    {

      "taxReversalInfos": {

        "taxReversalInfoList": [

         {

           "orderItemSummaryId": "10uxx0000004EdmAAE",

           "quantity": 1,

           "amount": -10,

           "taxAmount": 1.0

         }

        ]

      }

    }

  ]

}

```

**Sample Response**

```
[

  {

    "actionName": "RECORD_TAX_REVERSAL",

```

17

### Action Objects Record Tax Transaction Action

```
       "errors": null,

       "invocationId": null,

       "isSuccess": true,

       "outputValues": {

         "taxReversalResult": {

           "success": true,

           "resultItems": [

            {

              "transactionReferenceNumber": "tax_1PcknrITDqIkouLURfR4pNAM",

              "success": true,

              "orderItemSummaryId": "10uxx0000004EicAAE",

              "lineItemReference": tax_li_QZM99en1lXKf9s,

              "errorMessage": null

            }

           ],

           "errorMessage": null

         }

       },

       "sortOrder": -1,

       "version": 1

     }

   ]

### Record Tax Transaction Action

```

Records tax transactions from an order summary to an external system such as Stripe.

This action is available in API version 62.0 and later with these licenses:

**•** B2B Commerce, or D2C Commerce

**•** Salesforce Order Management

Only store administrators can access this action.

Supported REST HTTP Methods

**URI**

```
    /services/data/v XX.X /actions/standard/recordTaxTransaction

```

**Formats**
JSON, XML

**HTTP Methods**
POST

**Authentication**

```
    Authorization: Bearer token

```

18

Action Objects Record Tax Transaction Action

Inputs

**Input** **Details**

```
orderSummaryId

```

Outputs

**Type**
string

**Description**
Required.

The ID of the order summary to record tax transaction for.

**Output** **Details**

```
taxTransactionResult

```

Example

**Sample Request**

**Type**
Apex-defined

**Description**
An `Apex commercestoretax__TaxTransactionResult` record that contains
details about the tax transactions recorded.

```
{

  "inputs": [

    {

      "orderSummaryId": "1Osxx0000004CVcCAM"

    }

  ]

}

```

**Sample Response**

```
[

  {

   "actionName": "RECORD_TAX_TRANSACTION",

   "errors": null,

   "invocationId": null,

   "isSuccess": true,

   "outputValues": {

    "taxTransactionResult": {

     "success": true,

     "resultItems": [

      {

        "transactionReferenceNumber": "tax_1PcknrITDqIkouLURfR4pNAM",

        "success": true,

        "orderItemSummaryId": "10uxx0000004EicAAE",

```

19

## Action Objects Commerce Checkout Flow Actions

```
           "errorMessage": null,

           "calculationReferenceNumber": null

         },

         {

           "transactionReferenceNumber": "tax_1PcknrITDqIkouLURfR4pNAM",

           "success": true,

           "oderItemSummaryId": "10uxx0000004EibAAE",

           "errorMessage": null,

           "calculationReferenceNumber": null

         }

        ],

        "orderSummaryId": "1Osxx0000004CVc",

        "errorMessage": null

       }

      },

      "sortOrder": -1,

      "version": 1

     }

   ]

## Commerce Checkout Flow Actions

```

Manage your Commerce integrations and create a custom checkout with Checkout Flow actions.

[For more information about using Commerce Checkout Flow actions in flows, see Commerce Checkout Flow Core Actions in Salesforce](https://help.salesforce.com/HTViewHelpDoc?id=flow_ref_elements_comm_actions_list.htm&language=en_US)
Help.

These actions are available in API version 55.0 and later.

Supported REST HTTP Methods

**URI**
Get a specific Commerce Checkout Flow action:

```
    /services/data/v XX.X /actions/standard/ flow_action_name

```

**Formats**
JSON, XML

**HTTP Methods**
GET

**Authentication**

```
    Authorization: Bearer token

```

**Notes**
[You can also call the corresponding Connect REST API endpoints or Apex ConnectApi methods. For more information, see B2B and](https://developer.salesforce.com/docs/atlas.en-us.258.0.chatterapi.meta/chatterapi/connect_resources_commerce.htm)
[B2B2C Commerce Resources in the](https://developer.salesforce.com/docs/atlas.en-us.258.0.chatterapi.meta/chatterapi/connect_resources_commerce.htm) _Connect REST API Developer Guide_ [and ConnectApi Namespace in the](https://developer.salesforce.com/docs/atlas.en-us.258.0.apexcode.meta/apexcode/apex_classes_connect_api.htm) _Apex Developer Guide_ .

## Create Service Document Actions

Create service documents from work orders, work order line items, or service appointments.

This object is available in API version 60.0 and later.

20

Action Objects Create Service Document Actions

Supported REST HTTP Methods

**URI**

```
    /services/data/v 60.0 /actions/standard/createServiceDocument

```

**Formats**
JSON

**HTTP Methods**
POST

**Authentication**

```
    Authorization: Bearer token

```

Inputs

**Input** **Details**

```
recordId

templateId

locale

title

documentType

```

**Type**
string

**Description**
Required. The record ID of a work order, work order line item, or service appointment used to
generate the service document. Create a Lightning web component to use a Custom Property
Editor (CPE) to validate the `recordId` to avoid deployment issues.

**Type**
string

**Description**
Required, if the `recordId` is a work order, work order line item, or service appointment. The
ID of the service document template to use when generating the document.

**Type**
string

**Description**
Optional. Specifies the language for service document localization. The default is the user’s
language. Used when generating a document in a different language from the user’s language.
[See a list of supported languages in Supported Languages.](https://help.salesforce.com/s/articleView?id=sf.faq_getstart_what_languages_does.htm&type=5&language=en_US)

You can only input language for locale. For example, use `es` for Spanish. Using language and
country, for example `es_ES` for Spanish associated with Spain, results in error.

**Type**
string

**Description**
Optional. The value used to populate the `Label` field in the generated service report.

**Type**
string

21

Action Objects Create Service Document Actions

**Input** **Details**

**Description**
Optional. Value that allows users to generate different types of documents by using the service.
Valid values are:

**•** `SERVICE_DOCUMENT` —Type of service document, such as service agreement or service
contract.

**•** `QUOTE_DOCUMENT` —Type of quote document, such as sales quote or service quote.

**•** `SFS_QUOTE_DOCUMENT` —Type of quote document for Salesforce Field Service (SFS),
suitable for mobile use. This document is stored in the QuoteDocument object, and is
generated through flow-based processes that link to related service documents.

The default value is `ServiceDocument` .

```
pdfReportId

```

Outputs

**Type**
string

**Description**
Optional value corresponding to `recordId` and `templateId` . However, the value is required
if you aren’t generating the document from the default `pdfRecord` record. For the Document
Builder feature, this is a service report ID for a report that is in progress, queued, or failed. It must
be used to generate a service document from failed state.

**Inputs** **Details**

```
pdfReportId

```

Usage

**Sample Input**

**Type**
string

**Description**
Required. The report’s record ID that holds the generated PDF. For service documents, the
`pdfReportId` is a service report, and the record is created if the work order, work order line
item, or service appointment is passed as the `recordId` .

This sample generates a PDF of a service document with a specific `recordId` and `templateId` .

```
{

  "inputs": [

   {

    "recordId": "08pOG00000023anYAA",

    "templateId": "0M0OG0000005Na40AE",

    "locale": "en_US",

    "title": "Sample PDF"

```

22

## Action Objects Create Service Report Actions

```
       }

      ]

     }

## Create Service Report Actions

```

Creates a service report for a service appointment, work order, or work order line item.

This object is available in API version 39.0 and later.

Supported REST HTTP Methods

**URI**

```
    /services/data/v XX.X /actions/standard/createServiceReport

```

**Formats**
JSON

**HTTP Methods**
POST

**Authentication**

```
    Authorization: Bearer token

```

Inputs

**Input** **Details**

```
entityId

signatures

```

**Type**
reference

**Description**
Required. The ID of the service appointment, work order, or work order line item that the service
report is created for.

**Type**
string

**Description**
Optional. A list of JSON definitions for a digital signature.

**•** data—(Required) The base64 code for an image.

**•** contentType—(Required)The file type of the signature.

**•** signatureType—(Required) The role of the person signing; for example, “Customer.” Salesforce
admin defines Signature Type picklist values ahead of time. Each signature block must use
a different signature type, and the signature types you define in your call must match the
service report template’s signature types.

**•** name—The signature block title. This value appears on the generated service report.

**•** place—The place of signing. This value appears on the generated service report.

23

## Action Objects Custom Notification Actions

**Input** **Details**

**•** signedBy—The name of the person signing. This value appears on the generated service
report.

**•** signedDate—The date of signing. This value appears on the generated service report.

```
templateId

```

Usage

**Sample Input**

**Type**
reference

**Description**
Required. The ID of the standard or custom service report template that is used to create the
service report.

The following code sample creates a service report with two signatures by making an Apex callout to the _`createServiceReport`_
action REST API resource.

```
    {

      "inputs" : [ {

        "entityId" : "0WOxx000000001E",

          "signatures" : [

               {"data": "Base64 code for the captured signature image",

               "contentType":"image/png",

               "name":"Customer Signature",

               "signatureType":"Customer",

               "place":"San Francisco",

               "signedBy":"John Doe",

               "signedDate":"Thu Jul 13 22:34:43 GMT 2017"

               },

               {"data": "Base64 code for the captured signature image",

               "contentType":"image/png",

               "name":"Technician Signature",

               "signatureType":"Technician"

               }],

          "templateId" : "0SLR00000004DBFOA2"

      } ]

    }

## Custom Notification Actions

```

Send custom notifications to recipients via desktop or mobile channels.

Before you send a custom notification, you must first create a notification type.

24

Action Objects Custom Notification Actions

Important: In orgs created in Winter ’21 or later, the Send Custom Notifications user permission is required to trigger the Send
[Custom Notification action in flows that run in user context, REST API calls, and Apex callouts.](https://help.salesforce.com/articleView?id=flow_distribute_context.htm&type=5&language=en_US)

The Send Custom Notifications user permission isn’t required to trigger the Send Custom Notification action in processes or flows
that run in system context.

This object is available in API version 46.0 and later.

Supported REST HTTP Methods

**URI**

```
    /services/data/v XX.X /actions/standard/customNotificationAction

```

**Formats**
JSON, XML

**HTTP Methods**
GET, HEAD, POST

**Authentication**

```
    Authorization: Bearer token

```

Inputs

**Input** **Details**

```
customNotifTypeId

recipientIds

```

**Type**
reference

**Description**
Required. The ID of the Custom Notification Type being used for the notification.

**Type**
reference

**Description**
Required. The ID of the recipient or recipient type of the notification. Valid recipient or recipient
type values are:

**•** `UserId`  - The notification is sent to this user, if this user is active.

**•** `AccountId`  - The notification is sent to all active users who are members of this account’s
Account Team.

This recipient type is valid if account teams are enabled for your org.

**•** `OpportunityId`  - The notification is sent to all active users who are members of this
opportunity’s Opportunity Team.

This recipient type is valid if team selling is enabled for your org.

**•** `GroupId`  - The notification is sent to all active users who are members of this group.

**•** `QueueId`  - The notification is sent to all active users who are members of this queue.

Values can be combined in a list up to the maximum of 500 values.

25

Action Objects Custom Notification Actions

**Input** **Details**

```
senderId

title

body

targetId

targetPageRef

```

Usage

GET

**Type**
reference

**Description**
Optional. The User ID of the sender of the notification.

**Type**
string

**Description**
Required. The title of the notification, as seen by recipients. Maximum characters: 250.

The content of mobile push notifications depends on the content push notification setting.

**Type**
string

**Description**
Required. The body of the notification, as seen by recipients. Maximum characters: 750.

The content of mobile push notifications depends on the content push notification setting..

**Type**
reference

**Description**
Optional. The Record ID for the target record of the notification.

You must specify either a `targetID` or a `targetPageRef` .

**Type**
string

**Description**
Optional. The `PageReference` for the navigation target of the notification.

[To see how to specify the target using JSON, see pageReference.](https://developer.salesforce.com/docs/atlas.en-us.258.0.lightning.meta/lightning/components_navigation_page_definitions.htm)

You must specify either a `targetID` or a `targetPageRef` .

The following example shows how to get information about the custom notification action type:

```
curl --include --request GET \

--header "Authorization: Authorization: Bearer 00DR...xyz" \

--header "Content-Type: application/json" \

"https://instance.salesforce.com/services/data/v46.0/actions/standard/customNotificationAction"

```

POST

26

## Action Objects Deploy Data Kit Components Action

The following example shows how to create a custom notification action:

```
   curl --include --request POST \

   --header "Authorization: Authorization: Bearer 00DR...xyz" \

   --header "Content-Type: application/json" \

   --data '{ "inputs" :

     [

     {

      "customNotifTypeId" : "0MLR0000000008eOAA",

      "recipientIds" : ["005R0000000LSqtIAG"],

      "title" : "Custom Notification",

      "body" : "This is a custom notification.",

      "targetId" : "001R0000003fSUDIA2"

     }

     ]

   }' \

   "https://instance.salesforce.com/services/data/v46.0/actions/standard/customNotificationAction"

```

The response is:

```
   [

     {

       "actionName" : "customNotificationAction",

       "errors" : null,

       "isSuccess" : true,

       "outputValues" : {

         "SuccessMessage" : "Your custom notification is processed successfully."

       }

     }

   ]

## Deploy Data Kit Components Action

```

Deploy data kit components sequentially in a subscriber org. The `deployDataKitComponents` invocable action is used in the
## Deploy Data Kit Component flow to invoke the deployment of each data kit component. This action is available for flows in

API version 61.0 and later.

Inputs

**Input** **Details**

```
dataKitComponentDeployInput

dataKitName

```

**Type**
Apex-defined sfdatakit__DeployComponentInput

**Description**
Required. An Apex `sfdatakit__DeployComponentInput` payload that contains details
about the components to deploy and their metadata.

**Type**
text

27

Action Objects Deploy Data Kit Components Action

**Input** **Details**

**Description**
Required. The data kit name that contains the components to get the status for.

```
dataSpaceName

```

Outputs

None.

Example

**Type**
text

**Description**
The name of the data space to deploy the data kit to. If a data space isn't defined, the system
deploys the components in the default data space.

The following example shows a sample input payload for the different data kit components.

**Input** **Details**

```
sfdatakit__DeployComponentInput.bundleConfig

```

**Type**
Apex-defined

**Input Payload**

```
  {

    "inputs": [

       {

         "dataKitComponentsInput": [

            {

              "componentType": "DataStreamBundle",

              "bundleConfig": {

                "connectorType": "CRM",

                "bundleName": "hello", #full Qualified

   Bundle Name with namespace in datakit

                "forceNoRefresh": true,

                "bundleCRMConfig": {

                   "orgId": "org123" #Data Org Id

                }

              }

            }

         ],

         "dataKitNameInput": "datakit1",

         "dataKitDataSpaceInput" : "default"

       }

    ]

  }

```

28

Action Objects Deploy Data Kit Components Action

**Input** **Details**

```
sfdatakit__DeployComponentBundleConfig.bundleConnectorFrameworkConfig

sfdatakit__DeployComponentBundleConfig.bundleIngestApiConfig

```

**Type**
Apex-defined

**Input Payload**

```
  {

    "inputs": [

       {

         "dataKitComponentsInput": [

            {

              "componentType": "DataStreamBundle",

              "bundleConfig": {

                "connectorType": "MORECONNECTORS",

                "bundleName": "hello", #full Qualified

   Bundle Name with namespace in datakit

                "forceNoRefresh": true,

                "bundleConnectorFrameworkConfig": {

                   "connectionName": "name"

                }

              }

            }

         ],

         "dataKitNameInput": "datakit1",

         "dataKitDataSpaceInput" : "default"

       }

    ]

  }

```

**Type**
Apex-defined

**Input Payload**

29

Action Objects Deploy Data Kit Components Action

**Input** **Details**

```
                          "dataKitDataSpaceInput" : "default"

                        }

                     ]

                   }

```

```
sfdatakit__DeployComponentBundleConfig.bundleStreamingAppConfig

sfdatakit__DeployComponentInput.calculatedInsightsConfig

```

**Type**
Apex-defined

**Input Payload**

```
  {

    "inputs": [

       {

         "dataKitComponentsInput": [

            {

              "componentType": "DataStreamBundle",

              "bundleConfig": {

                "connectorType": "STREAMINGAPP",

                "bundleName": "hello", #full Qualified

   Bundle Name with namespace in datakit

                "forceNoRefresh": true,

                "bundleStreamingAppConfig": {

                  "connectorName": "name", #Streaming

   app connector name

                   "streamingAppDataConnectorType":

  "MobileApp" #MobileApp,WebApp

                }

              }

            }

         ],

         "dataKitNameInput": "datakit1",

         "dataKitDataSpaceInput" : "default"

       }

    ]

  }

```

**Type**
Apex-defined

**Input Payload**

30

Action Objects Deploy Data Kit Components Action

**Input** **Details**

```
                                 "label": "lab", #label of CI to be

                   created on org

                                 "publishInterval":"NotScheduled"

                   #NotScheduled,One,Six,Twelve,TwentyFour

                               }

                            }

                          ],

                          "dataKitNameInput": "datakit1",

                          "dataKitDataSpaceInput" : "default"

                        }

                     ]

                   }

```

```
sfdatakit__DeployComponentInput.dloConfig

sfdatakit__DeployComponentInput.dataTransformConfig

```

**Type**
Apex-defined

**Input Payload**

```
  {

    "inputs": [

       {

         "dataKitComponentsInput": [

            {

              "componentType": "DataLakeObject",

              "dloConfig": {

                "dataSourceObjectDevName": "crm",#full

   Qualified DLO Name with namespace in datakit

                "apiName": "hello",#api name of DLO to

   be created on org

               "label": "lab"#label of DLO to be created

   on org

              }

            }

         ],

         "dataKitNameInput": "datakit1",

         "dataKitDataSpaceInput" : "default"

       }

    ]

  }

```

**Type**
Apex-defined

**Input Payload**

```
  {

    "inputs": [

       {

         "dataKitComponentsInput": [

            {

              "componentType": "DataTransform",

              "dataTransformConfig": {

```

31

## Action Objects Email Alert Actions

**Input** **Details**

```
                               "dataTransformType": "BATCH",

                   #STREAMING,BATCH

                               "dataTransformDevName":

                   "BatchTransformAccount",#full Qualified Transform Name with

                   namespace in datakit

                              "apiName":"BatchTransformAccount",#api name

                   of Transform to be created on org

                               "label" : "BatchTransformAccount"#label of

                   Transform to be created on org

                               }

                            }

                          ],

                          "dataKitNameInput": "datakit1",

                          "dataKitDataSpaceInput" : "default"

                        }

                     ]

                   }

## Email Alert Actions

```

Send emails from flows by reusing already-configured workflow email alerts.

The email alert is already configured with the email’s contents, recipients, and sender, so the flow only has to provide the record ID.
[Email alerts are entity-specific. For more information about creating email alerts, see Creating Email Alerts for Workflow, Approvals, or](https://help.salesforce.com/apex/HTViewHelpDoc?id=creating_workflow_alerts.htm&language=en_US)
[Milestones in Salesforce Help. Make sure to review the daily limits for emails sent from email alerts.](https://help.salesforce.com/apex/HTViewHelpDoc?id=creating_workflow_alerts.htm&language=en_US)

This object is available in API version 32.0 and later.

Supported REST HTTP Methods

**URI**
Get a list of available email alert actions:

```
    /services/data/v XX.X /actions/custom/emailAlert

```

Get information about a specific email alert action:

```
    /services/data/v XX.X /actions/custom/emailAlert/ entity_name / action_name

```

**Formats**
JSON, XML

**HTTP Methods**
GET, HEAD, POST

**Authentication**

```
    Authorization: Bearer token

```

32

## Action Objects Einstein Bots Actions

Inputs

The email alert action uses the record specified by `SObjectRowId` to get the information it needs. For example, if a Case was specified
for the action, the action could retrieve the email address and recipient’s name from the Case object’s _`SuppliedEmail`_ and
_`SuppliedName`_ fields, respectively.

**Input** **Details**

```
SObjectRowId

```

Outputs

None.

**Type**
ID

**Description**
Required. The ID of a record such as an Account.

## Einstein Bots Actions

Search for knowledge articles based on data category and data category groups. To use these actions, you must enable Einstein Bots
and Lightning Knowledge.

### Get Data Category Details

Gets the labels and API names for a specified data category associated with the Knowledge object and its child categories.

This object is available in API version 56.0 and later.

Supported REST HTTP Methods

**URI**

```
  /services/data/56.0/actions/standard/getDataCategoryDetails

```

**Formats**
JSON, XML

**HTTP Methods**
GET, HEAD, POST

**Authentication**

```
  Authorization: Bearer token

```

Inputs

**Input** **Details**

```
dataCategoryGroupName

```

**Type**
string

33

### Action Objects Get Data Category Groups

**Input** **Details**

**Description**
The API name of the data category group.

```
dataCategoryName

```

Outputs

**Type**
string

**Description**
The API name of the data category.

**Output** **Details**

```
dataCategoryDetailsOutput

```

**Type**
Apex

**Description**
An Apex knowledge_bot__DataCategoryDetailsOutput record that contains the labels and API
names for the data category and its child categories.

### Get Data Category Groups

Gets the labels and API names of the active data category groups associated with the Knowledge object that are visible to the current
user.

This object is available in API version 56.0 and later.

Supported REST HTTP Methods

**URI**

```
  /services/data/v56.0/actions/standard/getDataCategoryGroups

```

**Formats**
JSON, XML

**HTTP Methods**
GET, HEAD, POST

**Authentication**

```
  Authorization: Bearer token

```

Inputs

None

34

### Action Objects Search Knowledge Articles

Outputs

**Output** **Details**

```
dataCategoryGroupInfo

```

**Type**
Apex

**Description**
An Apex knowledge_bot__DataCategoryGroupInfo record that contains the labels and API
names of the data category groups visible to the current user.

### Search Knowledge Articles

Searches for knowledge articles with specified search terms, language, data category group, and data category.

This object is available in API version 56.0 and later.

Supported REST HTTP Methods

**URI**

```
  /services/data/v56.0/actions/standard/searchKnowledgeArticles

```

**Formats**
JSON, XML

**HTTP Methods**
GET, HEAD, POST

**Authentication**

```
  Authorization: Bearer token

```

Inputs

**Input** **Details**

```
searchText

languageCode

dataCategoryGroupName

```

**Type**
string

**Description**
Search terms to be used in the knowledge article search.

**Type**
string

**Description**
The language code to be used in a knowledge article search. Valid values are language codes
for fully supported languages.

**Type**
string

35

## Action Objects Explore Conversation Actions

**Input** **Details**

**Description**
The API name of the data category group to be used in the knowledge article search.

```
dataCategoryName

resultsLimit

```

Outputs

**Type**
string

**Description**
The API name of the data category to be used in the knowledge article search.

**Type**
integer

**Description**
Optional. The maximum number of knowledge articles to return. Valid values are from 1 through
2000. By default, the maximum is 2000.

**Output** **Details**

```
knoweldgeArticlesList

```

**Type**
Apex

**Description**
An Apex knowledge_bot__ArticlesList record that contains information about the knowledge
articles that were returned.

## Explore Conversation Actions

Answer a user's questions about a voice or video call based on the contents of the call transcript.

This action is available in API version 60.0 and later.

On invocation, this action takes a natural language question about a voice or video call and uses an LLM to return an answer in rich text
based on the call transcript.

Typical use cases include:

**•** Answering questions about call sentiment

**•** Determining whether a deal is likely to close based on a call transcript

**•** Identifying customer blockers or challenges in a call

The user calling the action must have the Einstein Sales Call Explorer permission set and Read access to the voice or video call. This action
does not respect flows that try to override this privilege, so flows in the system context still need to use a user with Read access to the
call.

36

Action Objects Explore Conversation Actions

Supported REST HTTP Methods

**URI**

```
    /services/data/v XX.X /actions/standard/exploreConversation

```

**Formats**
JSON, XML

**HTTP Methods**
GET, HEAD, POST

**Authentication**

```
    Authorization: Bearer token

```

Inputs

**Input** **Details**

```
recordId

question

promptVersion

```

Outputs

**Type**
string

**Description**
Required. The ID of the related voice or video call record to answer a question for.

**Type**
string

**Description**
Required. The question asked about the voice or video call.

**Type**
string

**Description**
The prompt used when answering a voice or video call.

**Input** **Details**

```
answer

type

```

**Type**
string

**Description**
The answer to the call question in rich text format.

**Type**
string

**Description**
The format of the answer, such as rich text.

37

Action Objects Explore Conversation Actions

**Input** **Details**

```
responseId

requestId

```

Usage

**Sample Input**

```
  {

   "inputs": [{

```

**Type**
string

**Description**
The response ID from the LLM, used for gathering feedback data.

**Type**
string

**Description**
The request ID from the LLM, used for gathering feedback data.

```
      "recordId":"0LQSG000000gNTF4A2",

      "question":"What is the call about?"

   }]

  }

```

**Sample Output**

```
  [

   {

    "actionName":"exploreConversation",

    "errors":null,

    "invocationId":null,

    "isSuccess":true,

    "outcome":null,

    "outputValues":{

   "answer":"The call is about discussing the next steps for moving forward with an

  intermediate subscription for 25 user licenses. The salesperson, Sam Rhodes, is trying

   to coordinate with Jon Amos and Dale to finalize the purchase, considering the

  possibility of upgrading to an Advanced subscription if the budget allows.",

  "requestId":"chatcmpl-BCxbhgFVv2CwHZVsAHYYX1PHfNwRc",

  "type":"richtext",

  "responseId":"dee515cc-4493-4bfe-a3ec-be07d993f020"

    }

   "sortOrder":-1,

   "version":1

   }

  ]

```

[For more information about this action, see Flow Core Actions: Explore Conversation and Explore Conversation Invocable Action in](https://help.salesforce.com/s/articleView?id=platform.flow_ref_elements_actions_explore_conversation.htm&language=en_US)
Salesforce Help.

38

## Action Objects Flow Actions Flow Actions

Invoke an active autolaunched flow that exists in the current org.

[For more information about creating flows, see Build a Flow in Salesforce Help.](https://help.salesforce.com/HTViewHelpDoc?id=flow_build.htm&language=en_US)

This object is available for autolaunched flows in API version 32.0 and later.

Supported REST HTTP Methods

**URI**
Get a list of available flow actions:

```
    /services/data/v XX.X /actions/custom/flow

```

Invokes the `LargeOrder` flow:

```
    /services/data/v XX.X /actions/custom/flow/LargeOrder

```

**Formats**
JSON, XML

**HTTP Methods**
GET, HEAD, POST

**Authentication**

```
    Authorization: Bearer token

```

Inputs

Input values vary according to the input variables specified for each flow. For autolaunched flows, the input values vary according to
the input variables in that flow.

Outputs

The Response to an invocation will include `Flow__InterviewStatus` and any output variables defined in the flow. For more
[information, see Flow Resource: Variable in Salesforce Help.](https://help.salesforce.com/s/articleView?id=platform.flow_ref_resources_variable.htm&type=5&language=en_US)

**Output** **Details**

```
Flow__InterviewStatus

```

**Type**
picklist

**Description**
The status of the flow interview. Valid values are:

**•** Created

**•** Started

**•** Finished

**•** Error

**•** Waiting

39

## Action Objects Generate Order Summary Action

Legacy Support for Process Builder

[Processes created with type ‘Invocable’ in Process Builder can also be invoked via REST, using the endpoint listed above. See Create a](https://help.salesforce.com/apex/HTViewHelpDoc?id=process_create.htm&language=en_US)
[Process in Salesforce Help. This object is available for invocable processes in API version 38.0 and later.](https://help.salesforce.com/apex/HTViewHelpDoc?id=process_create.htm&language=en_US)

Invocable processes always require one of these input parameters:

**•** sObject: The sObject itself that you want the process to execute on. The sObject must be of the same object type as the one on
which the process is defined.

**•** sObjectId: The Id of the sObject record that you want the process to execute on. The record must be of the same object type as the
one on which the process is defined.

Invocable processes don’t have outputs.

SEE ALSO:

_Apex Developer Guide_ [: InvocableMethod Annotation](https://developer.salesforce.com/docs/atlas.en-us.258.0.apexcode.meta/apexcode/apex_classes_annotation_InvocableMethod.htm)

_[REST API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.258.0.api_rest.meta/api_rest/resources_actions_invocable.htm)_ : Invocable Actions

## Generate Order Summary Action

Generates a URL so that authenticated and guest users can access order details.

To access, you need these permissions.

**•** Salesforce Order Management License or Salesforce B2B Commerce License

This object is available in API version 59.0 and later.

Supported REST HTTP Methods

**URI**

```
    /services/data/v59.0/actions/standard/generateOrderSummaryUrl

```

**Formats**
JSON

**HTTP Methods**
POST

Inputs

**Input** **Details**

```
orderSummaryId

orderNumber

```

**Type**
ID

**Description**
Optional. The ID of the order summary to generate a URL for.

**Type**
string

40

## Action Objects Generate Work Orders Actions

**Input** **Details**

**Description**
Optional. The ID of the Salesforce payment gateway record that represents the external payment
gateway used for processing the sale request.

```
webStoreId

```

Outputs

**Type**
ID

**Description**
Required. The order number of the order summary to generate a URL for.

**Output** **Details**

```
url

```

**Type**
string

**Description**
The URL generated by the action that links to the order summary.

## Generate Work Orders Actions

Generates work orders from a maintenance plan. This object supports manual work order generation only. Before using this object, make
sure that Auto-Generate Work Orders isn’t selected on the maintenance plan.

This object is available in API version 40.0 and later.

Supported REST HTTP Methods

**URI**

```
  /services/data/v XX.X /actions/standard/generateWorkOrders

```

**Formats**
JSON, XML

**HTTP Methods**
POST

**Authentication**

```
  Authorization: Bearer token

```

41

## Action Objects Get Assessment Response Summary

Inputs

**Input** **Details**

```
recordId

```

**Type**
reference

**Description**
The ID of the maintenance plan from which you want to generate work orders.

## Get Assessment Response Summary Get Assessment Response Summary makes it easy to use a flow to trigger server-side document generation using Docgen.

In Discovery Framework, the responses from an assessment are stored in the AssessmentQuestionResponse object and the form metadata
stays in OmniScript. You can use this invocable action to pass assessment summary data to the downstream processes. This invocable
action provides a summary JSON that can be consumed in Docgen workflows to generate documents.

The Get Assessment Response Summary invocable action takes assessment ID as the input to get the OmniProcess ID, which is used to
retrieve the OmniProcess elements. The assessment ID also retrieves the assessment response and merges the response with the
OmniProcess elements to create an assessment summary response in JSON.

This object is available in API version 56.0 and later.

Supported REST HTTP Methods

**URI**

```
  /services/data/v56.0/actions/standard/getAssessmentResponseSummary

```

**Formats**
JSON

**HTTP Methods**
POST

**Authentication**

```
  Authorization: Bearer token

```

Inputs

**Input** **Details**

```
assessmentId

```

**Type**
ID

**Description**
Required. The ID of the assessment record for which to summarize responses.

42

Action Objects Get Assessment Response Summary

Outputs

**Output** **Details**

```
assessmentResponseSummary

```

Usage

**Sample Input**

**Type**
string

**Description**
A JSON string containing the summary assessment question texts and responses for the specified
assessment record. The response summary structure follows the structure of the OmniScript.

When exposing the Get Assessment Response Summary invocable action in a REST API, you can use the following format to pass
input, which includes the assessmentId and its value.

```
  {

   "inputs" : [ {"assessmentId" : "0U3RO00000005FN0AY"} ]

  }

```

**Sample Output**

In this example, the first line indicates the OmniScript type, subtype, and language. For each step, there are multiple questions that
appear in the OmniScript. You can use this information in a downstream process, such as generation of PDF document using Docgen
capability.

```
   "KYC_Individual_English": {

    "Step1": {

      "label": "Identity Details",

      "value": {

       "LC_Survey_Question_2": {

        "label": "Full Name",

        "value": "Joe Smith"

       },

       "DateofBirth_m": {

        "label": "Date of Birth",

        "value": "Thu Jul 27 00:00:00 GMT 2000"

       },

       "Gender_m": {

        "label": "Gender",

        "value": "Female"

       },

       "EmailAddress_m": {

        "label": "Email Address",

        "value": "Joe.Smith@company.com"

       },

       "PAN": {

        "label": "PAN",

        "value": "QWEASDZXC"

       }

      }

```

43

Action Objects Get Assessment Response Summary

```
       },

       "Step2": {

         "label": "Address Details",

         "value": {

          "Address_CorrespondenceAdd_Corporate": {

           "label": "Address of Correspondence",

           "value": "100 Some St, San Francisco, CA 12345, United States"

          },

          "Address_ContactDetails_Corporate": {

           "label": "Telephone/Mobile",

           "value": "1616111233"

          },

          "Alternate_Contact": {

           "label": "Alternate Mobile Number",

           "value": "1911212123"

          }

         }

       },

       "Step3": {

         "label": "Account Declaration",

         "value": {

          "Account_declaration": {

           "label": "I declare that I have following deposit accounts with your/

     other bank's branches :",

           "value": [

            {

             "Bank": {

               "label": "Bank",

               "value": "Acme1"

             },

             "Branch": {

               "label": "Branch",

               "value": "Mission St"

             },

             "Type_of_Account": {

               "label": "Type of Account",

               "value": "Checking"

             },

             "Account_Number": {

               "label": "Account Number",

               "value": "12345678"

             }

            },

            {

             "Bank": {

               "label": "Bank",

               "value": "Acme2"

             },

             "Branch": {

               "label": "Branch",

               "value": "Mission St"

             },

             "Type_of_Account": {

               "label": "Type of Account",

```

44

## Action Objects Get Conversation Intelligence Action

```
               "value": "Savings"

             },

             "Account_Number": {

               "label": "Account Number",

               "value": "1234567890"

             }

            }

           ]

          }

         }

       },

       "Step4": {

         "label": "Declaration",

         "value": {

          "Declaration_m": {

           "label": "The customer declares and certifies that the information in this

     form is true and correct. Any pre-filled sections of this form must be reviewed prior

      to signing and submitting, to ensure the information accurately conveys the new

     account details.",

           "value": "true"

          }

         }

       }

      }

     }

## Get Conversation Intelligence Action

```

Gets intelligence information about a voice or video call, including any insights and a conversation summary.

This action is available in API version 65.0 and later.

On invocation, this action gets a list of insights related to a call, and a call summary if one is available.

The user calling the action must have access to the related voice or video call records.

Supported REST HTTP Methods

**URI**

```
    /services/data/v XX.X /actions/standard/getConversationIntelligence

```

**Formats**
JSON, XML

**HTTP Methods**
GET, HEAD, POST

**Authentication**

```
    Authorization: Bearer token

```

45

Action Objects Get Conversation Intelligence Action

Inputs

**Input** **Details**

```
recordId

```

Outputs

**Type**
string

**Description**
Required. The ID of the related voice or video call record to answer a question for.

**OUTput** **Details**

```
conversationInsights

conversationIntelligence

momentInsights

```

Usage

**Sample Input**

```
  {

    "inputs": [

       {

```

**Type**
Apex collection

**Description**
The list of insights related to the content of the call as a whole, such as generative conversation
insights.

**Type**
Apex

**Description**
Other intelligence information related to the call, including a summary of the call if one was
generated.

**Type**
Apex collection

**Description**
The list of insights related to conversation moments, such as pricing insights or mentions of
relevant keywords about products or competitors. The list is empty if no insights are found.

```
       "recordId": "6qrAAC000000BGPYB2",

     }

  ]

}

```

46

Action Objects Get Conversation Intelligence Action

**Sample Output**

```
     {

       "conversationInsights": [],

       "conversationIntelligence": {

          "callSummary": "&lt;p&gt;&lt;strong&gt; Customer

     Impression&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;Sam, the customer, expressed a need for more

      features than their current service, Genius Solutions, offers. They appreciated the

     flexibility in adding licenses and were concerned about pricing due to a tight

     budget.&lt;/p&gt;&lt;p&gt;&lt;br&gt;&lt;/p&gt;&lt;p&gt;&lt;strong&gt; Call

     Summary&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;Sam, the customer, has been using Genius

     Solutions for several years but feels it lacks some features they need. They are exploring

      other options and are particularly interested in the flexibility of adding licenses,

     which is a significant pain point for them. Sam is also concerned about pricing and

     needs to stay within a budget of $1,600 per month. They are considering the intermediate

      subscription, which seems to fit their current needs. Sam plans to discuss the pricing

      and options with their partner, John, and their boss, who has significant influence

     over the decision. They are also interested in a demo of the intermediate subscription

      to prove the concept.&lt;/p&gt;&lt;p&gt;&lt;br&gt;&lt;/p&gt;&lt;p&gt;&lt;strong&gt;

     Next Steps&lt;/strong&gt;&lt;/p&gt;&lt;ol&gt;&lt;li&gt;Seller to put together a quote

     and email it to Sam.&lt;/li&gt;&lt;li&gt;Sam to discuss the quote with their partner,

     John, and their boss.&lt;/li&gt;&lt;li&gt;Schedule a demo of the intermediate subscription

     for next week.&lt;/li&gt;&lt;li&gt;Sam to confirm the best time for the demo with their

      team.&lt;/li&gt;&lt;/ol&gt;&lt;p&gt;&lt;br&gt;&lt;/p&gt;"

       },

       "momentInsights": [

          {

            "category": "Question",

            "insightTypeId": "00000000-0000-0000-0000-000000001010",

            "keyword": "Question",

            "momentTimes": [

               {

                 "action": null,

                 "endOffset": 39.18000030517578,

                 "entries": [

                   "Long you been with Solutions?"

                 ],

                 "isFollowup": false,

                 "mentionId": 0,

                 "momentOffset": 32.720001220703125,

                 "needsAttention": false,

                 "sequences": [

                   7

                 ],

                 "speakerId": "Speaker 2",

                 "speakerRole": null,

                 "startOffset": 27.719999313354492

               },

               {

                 "action": null,

                 "endOffset": 75.08999633789062,

                 "entries": [

                   "I&#39;m you&#39;ve had a kind comb through our as extensively,

      a think one missing is need be boss how this going are terms?"

```

47

Action Objects Get Conversation Intelligence Action

```
                 ],

                 "isFollowup": false,

                 "mentionId": 1,

                 "momentOffset": 56.099998474121094,

                 "needsAttention": false,

                 "sequences": [

                   11

                 ],

                 "speakerId": "Speaker 2",

                 "speakerRole": null,

                 "startOffset": 51.099998474121094

               },

               {

                 "action": null,

                 "endOffset": 103.44999694824219,

                 "entries": [

                   "Many off, how licenses are you looking at?"

                 ],

                 "isFollowup": false,

                 "mentionId": 2,

                 "momentOffset": 94.66999816894531,

                 "needsAttention": false,

                 "sequences": [

                   17

                 ],

                 "speakerId": "Speaker 1",

                 "speakerRole": null,

                 "startOffset": 89.66999816894531

               },

               {

                 "action": null,

                 "endOffset": 175.7100067138672,

                 "entries": [

                   "You said 16 licenses, correct?"

                 ],

                 "isFollowup": false,

                 "mentionId": 3,

                 "momentOffset": 167.88999938964844,

                 "needsAttention": false,

                 "sequences": [

                   28

                 ],

                 "speakerId": "Speaker 1",

                 "speakerRole": null,

                 "startOffset": 162.88999938964844

               },

               {

                 "action": null,

                 "endOffset": 179.5800018310547,

                 "entries": [

                   "Like how pay, can you break me?"

                 ],

                 "isFollowup": false,

                 "mentionId": 4,

```

48

Action Objects Get Conversation Intelligence Action

```
                 "momentOffset": 172.08999633789062,

                 "needsAttention": false,

                 "sequences": [

                   29

                 ],

                 "speakerId": "Speaker 1",

                 "speakerRole": null,

                 "startOffset": 167.08999633789062

               },

               {

                 "action": null,

                 "endOffset": 182.6199951171875,

                 "entries": [

                   "Like monthly it quarterly or annual?"

                 ],

                 "isFollowup": false,

                 "mentionId": 5,

                 "momentOffset": 174.82000732421875,

                 "needsAttention": false,

                 "sequences": [

                   30

                 ],

                 "speakerId": "Speaker 1",

                 "speakerRole": null,

                 "startOffset": 169.82000732421875

               }

            ]

          },

          {

            "category": "Pricing",

            "insightTypeId": "00000000-0000-0000-0000-000000001001",

            "keyword": "Pricing",

            "momentTimes": [

               {

                 "action": null,

                 "endOffset": 196.5399932861328,

                 "entries": [

                   "It&#39;s monthly can access it via once customer. intermediate

      subscription about $1,200 a month. the premium, an additional $55 per you include

     looking at about 20."

                 ],

                 "isFollowup": false,

                 "mentionId": 0,

                 "momentOffset": 191.17999267578125,

                 "needsAttention": false,

                 "sequences": [

                   31

                 ],

                 "speakerId": "Speaker 1",

                 "speakerRole": null,

                 "startOffset": 186.17999267578125

               }

            ]

          },

```

49

## Action Objects Get Conversation Transcript Action

```
          {

            "category": "Next Step",

            "insightTypeId": "00000000-0000-0000-0000-000000001000",

            "keyword": "Next Step",

            "momentTimes": [

               {

                 "action": null,

                 "endOffset": 272.57000732421875,

                 "entries": [

                   "Like to subscription. available next be great just to prove

     out concept little me work on that with my Linda, that she can be on it have a large

     deal of influence."

                 ],

                 "isFollowup": false,

                 "mentionId": 0,

                 "momentOffset": 267.04998779296875,

                 "needsAttention": false,

                 "sequences": [

                   48

                 ],

                 "speakerId": "Speaker 1",

                 "speakerRole": null,

                 "startOffset": 262.04998779296875

               },

               {

                 "action": null,

                 "endOffset": 299.4653015136719,

                 "entries": [

                   "Talk soon."

                 ],

                 "isFollowup": false,

                 "mentionId": 1,

                 "momentOffset": 294.9100036621094,

                 "needsAttention": false,

                 "sequences": [

                   53

                 ],

                 "speakerId": "Speaker 2",

                 "speakerRole": null,

                 "startOffset": 289.9100036621094

               }

            ]

          }

       ]

     }

```

[For more information about this action, see Flow Core Actions: Get Conversation Intelligence and Get Conversation Intelligence Invocable](https://help.salesforce.com/s/articleView?id=platform.flow_ref_elements_actions_get_conversation_intelligence.htm&language=en_US)
[Action in Salesforce Help.](https://help.salesforce.com/s/articleView?id=sales.ci_ia_get_conv_intel.htm&language=en_US)

## Get Conversation Transcript Action

Gets a transcript for a voice or video call.

This action is available in API version 63.0 and later.

50

Action Objects Get Conversation Transcript Action

On invocation, this action gets the transcript for a voice or video call record.

Typical use cases include:

**•** Ground a customer-defined prompt template with a conversation transcript

**•** Automate updates to relevant records based on conversation data

Some considerations include:

**•** The transcript must be available in order to retrieve it.

**•** The user calling the action must have Read access to the voice or video call.

**•** Video calls can retrieve the initial raw vendor transcript, but voice calls can retrieve the processed transcript only.

Supported REST HTTP Methods

**URI**

```
    /services/data/v XX.X /actions/standard/getConversationTranscript

```

**Formats**
JSON, XML

**HTTP Methods**
GET, HEAD, POST

**Authentication**

```
    Authorization: Bearer token

```

Inputs

**Input** **Details**

```
recordId

transcriptType

```

Outputs

**Type**
string

**Description**
Required. The ID of the related voice or video call record to get the transcript for.

**Type**
picklist

**Description**
The type of transcript. The Raw type includes the plain text transcript, while the Processed type
contains the full conversation transcript. The Raw transcript type is limited to video calls only.

**output** **Details**

```
structuredTranscript

```

**Type**
Apex

51

Action Objects Get Conversation Transcript Action

**output** **Details**

**Description**
An Apex ConversationTranscript record that contains the full conversation transcript. This is
available for Processed transcript types only.

```
unformattedTextTranscript

```

Usage

**Sample Input**

```
  {

    "inputs": [

       {

```

**Type**
string

**Description**
The conversation transcript in plain text format. For Processed transcript types, the speaker and
conversation content are shown. For Raw transcript types, whatever is present from the vendor
is shown.

```
         "recordId": "6qrAAC000000BGPYB2",

         "transcriptType": "PROCESSED". // Values: RAW, PROCESSED. Optional

       }

    ]

  }

```

**Sample Output**

```
  {"structuredTranscript":{"entries":[{"endDateTime":"2025-02-20T00:01:13.426Z","entry":"Hey,

   good morning, hi, nice to meet you and thanks for jumping on me, how&#39;re you doing

  today.","sequence":0,"speakerId":"1afSG000000yOsHYAU","startDateTime":"2025-02-20T00:01:07.546Z"},{"endDateTime":"2025-02-20T00:01:43.906Z","entry":"Good

   morning, Sam, Yeah, thanks so much for getting back to me and for setting this up I

  didn&#39;t think I did hear back from someone so quickly I&#39;m doing well and yourself,

   I&#39;m doing great, I&#39;m, and I&#39;m glad we able to find the time that works so

   quickly and your you&#39;re just said that you want to hear a bit more about your are

  you guys and company was currently are you looking to get started with the service like

   ours so we are currently using Genius Solutions, But we&#39;re looking to switch over

   to something

  else","sequence":1,"speakerId":"1afSG000000yOttYAE","startDateTime":"2025-02-20T00:01:14.236Z"},{"endDateTime":"2025-02-20T00:01:48.346Z","entry":"Alright,

   then, how long you been with Genius

  Solutions?","sequence":2,"speakerId":"1afSG000000yOsHYAU","startDateTime":"2025-02-20T00:01:45.046Z"},{"endDateTime":"2025-02-20T00:02:17.086Z","entry":"We&#39;ve

   been using Genius Solutions for 2 years now it works, but I feel like we&#39;re still

   missing some key features, the, the other companies have at least I&#39;ve been doing

  a bit of research and I&#39;m also taking a look at total tax, I haven&#39;t had a call

   with Total Attack or anything, but, from, what I see on their website they look like

  they&#39;re similar to you guys gotcha, okay, 2 years with Genius

  Solutions.","sequence":3,"speakerId":"1afSG000000yOttYAE","startDateTime":"2025-02-20T00:01:49.156Z"},{"endDateTime":"2025-02-20T00:02:19.936Z","entry":"Have

   you had a chance to go through our website as

  well?","sequence":4,"speakerId":"1afSG000000yOsHYAU","startDateTime":"2025-02-20T00:02:17.746Z"},{"endDateTime":"2025-02-20T00:02:33.256Z","entry":"Yes,

   extensively, the one thing I am missing is the pricing, I need to be able to tell my

```

52

Action Objects Get Conversation Transcript Action

```
     boss, how much is going to Cost us, you know, we can&#39;t go outside the

     Budget.","sequence":5,"speakerId":"1afSG000000yOttYAE","startDateTime":"2025-02-20T00:02:20.716Z"},{"endDateTime":"2025-02-20T00:02:47.956Z","entry":"Completely

      understand and we&#39;ll work to make sure to stay within a Budget, so the reason we

     don&#39;t have any pricing listed on the website is because, we customize each package

     based on which features functionality is the number of the user licenses that you would

     need","sequence":6,"speakerId":"1afSG000000yOsHYAU","startDateTime":"2025-02-20T00:02:33.946Z"},{"endDateTime":"2025-02-20T00:02:49.876Z","entry":"Okay

      that makes

     sense","sequence":7,"speakerId":"1afSG000000yOttYAE","startDateTime":"2025-02-20T00:02:48.826Z"},{"endDateTime":"2025-02-20T00:02:59.356Z","entry":"So,

      how many licenses would you be looking at in which I&#39;ve visited group and Wisdom

     does subscriptions, years Ah, seems interesting or a good to

     you.","sequence":8,"speakerId":"1afSG000000yOsHYAU","startDateTime":"2025-02-20T00:02:50.836Z"},{"endDateTime":"2025-02-20T00:03:22.186Z","entry":"So

      we wouldn&#39;t need 16 user licenses right now, but if we need more can be added to

     it at any time, you can always adjust the number of licenses based on a higher teeny

     grows that it&#39;s not a problem. Okay that&#39;s good to know, Genius Solutions is

     not making it as smooth processed purchase more user licenses, which is also one of the

      reasons that we are looking to

     switch","sequence":9,"speakerId":"1afSG000000yOttYAE","startDateTime":"2025-02-20T00:03:00.526Z"},{"endDateTime":"2025-02-20T00:03:35.596Z","entry":"No

      that&#39;s an easy, which, even if you want to move a few licenses we can do that just

      didn&#39;t really it just takes 24 hours for the account reset and then you&#39;ll be

      good to

     go","sequence":10,"speakerId":"1afSG000000yOsHYAU","startDateTime":"2025-02-20T00:03:23.596Z"},{"endDateTime":"2025-02-20T00:03:56.826Z","entry":"Okay,

      that&#39;s great, it&#39;s not something we&#39;d be changing often But, ah good to

     know that it&#39;s not an issue if and, when it is I did exactly, and which subscription

      here were you interested in I was taking a look at Intermediate and potentially the

     Premium Add On as

     well.","sequence":11,"speakerId":"1afSG000000yOttYAE","startDateTime":"2025-02-20T00:03:36.806Z"},{"endDateTime":"2025-02-20T00:04:02.616Z","entry":"Alright

      gotcha, I dive right in and, and he said, you need a 16 years or licenses,

     right","sequence":12,"speakerId":"1afSG000000yOsHYAU","startDateTime":"2025-02-20T00:03:57.596Z"},{"endDateTime":"2025-02-20T00:04:07.806Z","entry":"Correct,

      and, how do we pay is this a monthly Cost or

     annual","sequence":13,"speakerId":"1afSG000000yOttYAE","startDateTime":"2025-02-20T00:04:03.216Z"},{"endDateTime":"2025-02-20T00:04:28.496Z","entry":"Monthly

      and via our portal app so for 16 user licenses with the Intermediate Subscription that

      would Cost to a total of $1200 a month the Premium Add On it and it is an additional

     $55 per license. So if you wanted to include that as well, you&#39;d be looking at $2080

     monthly.","sequence":14,"speakerId":"1afSG000000yOsHYAU","startDateTime":"2025-02-20T00:04:08.966Z"},{"endDateTime":"2025-02-20T00:04:45.876Z","entry":"Alright

      it looks like the Premium Add On is outside our Budget can&#39;t go any higher than

     1600 monthly, but just the Intermediate Subscription, fits and we can also request more

      from corporate in the future

     hopefully.","sequence":15,"speakerId":"1afSG000000yOttYAE","startDateTime":"2025-02-20T00:04:29.456Z"},{"endDateTime":"2025-02-20T00:05:02.676Z","entry":"I

     can do all this together in a price quote, and email it over to you that would be great

      could you add my partner John too distance wall chirping I have your email from their

      request, confirming it work, you know, at Gmail Dot Com and can you get any

     junk?","sequence":16,"speakerId":"1afSG000000yOsHYAU","startDateTime":"2025-02-20T00:04:46.896Z"},{"endDateTime":"2025-02-20T00:05:09.116Z","entry":"Yeah

      that&#39;s my email, and John&#39;s email is John email at gmail dot

     Com.","sequence":17,"speakerId":"1afSG000000yOttYAE","startDateTime":"2025-02-20T00:05:03.426Z"},{"endDateTime":"2025-02-20T00:05:14.366Z","entry":"Okay

      great, so once we get off this call I&#39;ll put all that together and send it

     over.","sequence":18,"speakerId":"1afSG000000yOsHYAU","startDateTime":"2025-02-20T00:05:09.866Z"},{"endDateTime":"2025-02-20T00:05:22.586Z","entry":"Perfect

      once we have that we can bring into corporate for discussion they have the authority

     to approve the final purchase

     request.","sequence":19,"speakerId":"1afSG000000yOttYAE","startDateTime":"2025-02-20T00:05:15.086Z"},{"endDateTime":"2025-02-20T00:05:28.956Z","entry":"Would

      you like to run through a full demo of the Intermediate Subscription I am available at

      the end of next

     week?","sequence":20,"speakerId":"1afSG000000yOsHYAU","startDateTime":"2025-02-20T00:05:23.996Z"},{"endDateTime":"2025-02-20T00:05:37.266Z","entry":"Actually

```

53

Action Objects Get Conversation Transcript Action

```
      that would be great, let me can solve that, with my boss Linda, she will want to be on

      this call his

     wall","sequence":21,"speakerId":"1afSG000000yOttYAE","startDateTime":"2025-02-20T00:05:30.656Z"},{"endDateTime":"2025-02-20T00:05:45.456Z","entry":"Okay,

      awesome so in the meantime also send over a few potential time slots for demos next

     week and you can let me know which works best for you

     guys","sequence":22,"speakerId":"1afSG000000yOsHYAU","startDateTime":"2025-02-20T00:05:37.976Z"},{"endDateTime":"2025-02-20T00:05:49.926Z","entry":"Wonderful

      thank you so much and I look forward to speaking more

     soon.","sequence":23,"speakerId":"1afSG000000yOttYAE","startDateTime":"2025-02-20T00:05:46.176Z"},{"endDateTime":"2025-02-20T00:05:54.146Z","entry":"Great,

      we&#39;ll talk soon, thanks so much bye

     bye.","sequence":24,"speakerId":"1afSG000000yOsHYAU","startDateTime":"2025-02-20T00:05:50.606Z"}],"participants":[{"relatedWhoId":"005SG00000DuJJqYAN","speakerId":"1afSG000000yOsHYAU","speakerName":"Sam

     Rhodes","speakerRole":"Agent"},{"relatedWhoId":"003SG00000Ay9h1YAB","speakerId":"1afSG000000yOttYAE","speakerName":"Jon

     Amos","speakerRole":"EndUser"}],"transcribedLanguage":"en","transcriptionDateTime":"2025-02-21T00:06:06.131Z"},

     "unformattedTextTranscript":"Sam Rhodes: Hey, good morning, hi, nice to meet you and

     thanks for jumping on me, how're you doing today.\nJon Amos: Good morning, Sam, Yeah,

     thanks so much for getting back to me and for setting this up I didn't think I did hear

      back from someone so quickly I'm doing well and yourself, I'm doing great, I'm, and

     I'm glad we able to find the time that works so quickly and your you're just said that

      you want to hear a bit more about your are you guys and company was currently are you

      looking to get started with the service like ours so we are currently using Genius

     Solutions, But we're looking to switch over to something else\nSam Rhodes: Alright,

     then, how long you been with Genius Solutions?\nJon Amos: We've been using Genius

     Solutions for 2 years now it works, but I feel like we're still missing some key features,

      the, the other companies have at least I've been doing a bit of research and I'm also

      taking a look at total tax, I haven't had a call with Total Attack or anything, but,

     from, what I see on their website they look like they're similar to you guys gotcha,

     okay, 2 years with Genius Solutions.\nSam Rhodes: Have you had a chance to go through

     our website as well?\nJon Amos: Yes, extensively, the one thing I am missing is the

     pricing, I need to be able to tell my boss, how much is going to Cost us, you know, we

     can't go outside the Budget.\nSam Rhodes: Completely understand and we'll work to make

      sure to stay within a Budget, so the reason we don't have any pricing listed on the

     website is because, we customize each package based on which features functionality is

     the number of the user licenses that you would need\nJon Amos: Okay that makes sense\nSam

      Rhodes: So, how many licenses would you be looking at in which I've visited group and

      Wisdom does subscriptions, years Ah, seems interesting or a good to you.\nJon Amos: So

      we wouldn't need 16 user licenses right now, but if we need more can be added to it at

      any time, you can always adjust the number of licenses based on a higher teeny grows

     that it's not a problem. Okay that's good to know, Genius Solutions is not making it as

      smooth processed purchase more user licenses, which is also one of the reasons that we

      are looking to switch\nSam Rhodes: No that's an easy, which, even if you want to move

     a few licenses we can do that just didn't really it just takes 24 hours for the account

      reset and then you'll be good to go\nJon Amos: Okay, that's great, it's not something

      we'd be changing often But, ah good to know that it's not an issue if and, when it is

      I did exactly, and which subscription here were you interested in I was taking a look

     at Intermediate and potentially the Premium Add On as well.\nSam Rhodes: Alright gotcha,

      I dive right in and, and he said, you need a 16 years or licenses, right\nJon Amos:

     Correct, and, how do we pay is this a monthly Cost or annual\nSam Rhodes: Monthly and

     via our portal app so for 16 user licenses with the Intermediate Subscription that would

      Cost to a total of $1200 a month the Premium Add On it and it is an additional $55 per

      license. So if you wanted to include that as well, you'd be looking at $2080

     monthly.\nJon Amos: Alright it looks like the Premium Add On is outside our Budget can't

      go any higher than 1600 monthly, but just the Intermediate Subscription, fits and we

```

54

## Action Objects Get Data Graph Data By Lookup

```
     can also request more from corporate in the future hopefully.\nSam Rhodes: I can do all

      this together in a price quote, and email it over to you that would be great could you

      add my partner John too distance wall chirping I have your email from their request,

     confirming it work, you know, at Gmail Dot Com and can you get any junk?\nJon Amos: Yeah

      that's my email, and John's email is John email at gmail dot Com.\nSam Rhodes: Okay

     great, so once we get off this call I'll put all that together and send it over.\nJon

     Amos: Perfect once we have that we can bring into corporate for discussion they have

     the authority to approve the final purchase request.\nSam Rhodes: Would you like to run

      through a full demo of the Intermediate Subscription I am available at the end of next

      week?\nJon Amos: Actually that would be great, let me can solve that, with my boss

     Linda, she will want to be on this call his wall\nSam Rhodes: Okay, awesome so in the

     meantime also send over a few potential time slots for demos next week and you can let

     me know which works best for you guys\nJon Amos: Wonderful thank you so much and I look

      forward to speaking more soon.\nSam Rhodes: Great, we'll talk soon, thanks so much bye

      bye."}

```

[For more information about this action, see Flow Core Actions: Get Conversation Transcript and Get Conversation Transcript Invocable](https://help.salesforce.com/s/articleView?id=platform.flow_ref_elements_actions_get_conversation_transcript.htm&language=en_US)
[Action in Salesforce Help.](https://help.salesforce.com/s/articleView?id=sales.ci_ia_get_conv_transcript.htm&language=en_US)

## Get Data Graph Data By Lookup

Get data of a data graph in Data Cloud by data graph API name, data space name, and lookup key.

This resource is available in API version 63.0 and later.

Supported REST HTTP Methods

**URI**

[/services/data/v63.0/actions/standard/cdpGetDataGraphByLookup]

**Formats**
JSON, XML

**HTTP Methods**
POST

**Authentication**

```
    Authorization: Bearer token

```

Request Parameters

**Input** **Details**

dataGraphApiName

```
lookupKey

```

**Type**
string

**Description**
API name of the data graph to query.

**Type**
string

55

Action Objects Get Data Graph Data By Lookup

**Input** **Details**

**Description**
The lookup key used to query the data graph.

dataSpaceApiName

Example

**Example Request Body**

**Type**
string

**Description**
API name of the data space.

```
  {

    {

   "inputs": [

    {

      "dataspaceApiName": "default",

      "dataGraphApiName": "DGTest”,

      "lookupKey": "ssot__ContactPointAddress__dlm.ssot__Id__c=003SB000001a3GtYAI"

    }

   ]

  }

```

**Example Response Body**

```
  {

    [

   {

    "actionName": "cdpGetDataGraphByLookup",

    "errors": null,

    "invocationId": null,

    "isSuccess": true,

    "outcome": null,

    "outputValues": {

      "data": [

  "{\"ssot__Id__c\":\"1008703904\",\"ssot__BirthDate__c\":\"2021-12-20T07:53:46.832Z\",

  ...}]}",

  "{\"ssot__Id__c\":\"1008703907\",\"ssot__BirthDate__c\":\"2021-12-20T07:53:46.832Z\",

  ...}]}"

      ]

    },

    "sortOrder": -1,

    "version": 1

   }

  ]

```

56

## Action Objects Get Data Graph Metadata Get Data Graph Metadata

Get metadata of a data graph in Data Cloud by data graph API name and data space name. If the data space name isn't provided, the
API uses the default value.

This resource is available in API version 64.0 and later.

Supported REST HTTP Methods

**URI**

[/services/data/v64.0/actions/standard/cdpGetDataGraphMetadata]

**Formats**
JSON, XML

**HTTP Methods**
POST

**Authentication**

```
    Authorization: Bearer token

```

Request Parameters

**Input** **Details**

dataGraphApiName

dataSpaceApiName

Example

**Example Request Body**

**Type**
string

**Description**
API name of the data graph to query.

**Type**
string

**Description**
API name of the data space.

```
{

  {

 "inputs": [

  {

    "dataspaceApiName": "default",

    "dataGraphApiName": "DGTest”

  }

 ]

}

```

57

## Action Objects Knowledge Actions

**Example Response Body**

```
     [

      {

       "actionName": "cdpGetDataGraphMetadata",

       "errors": null,

       "invocationId": null,

       "isSuccess": true,

       "outcome": null,

       "outputValues": {

         "dataGraphMetadata": [

          "{\"createdBy\":\"005SB000000wYK5YAM\",\"createdDate\":\"Fri Apr 04 06:55:04

     GMT

     2025\",\"dataspaceName\":\"AMER\",\"description\":null,\"id\":\"0g7SB000000Ku2rYAC\",\"label\":\"Data

      Graph

     Demo\",\"modifiedBy\":null,\"modifiedDate\":null,\"name\":\"Data_Graph_Demo\",\"cacheDurationInDays\":null,\"dayZeroMappingDevName\":null,\"dayZeroTransformDevName\":null,...}"

         ]

       },

       "sortOrder": -1,

       "version": 1

      }

     ]

## Knowledge Actions

```

Manage your Knowledge articles using invocable actions.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

The Assign and Publish actions are available in API version 44.0 and later. All the other actions are available in API version 45.0 and later.

Lightning Knowledge must be set up in your org. The user must have permissions to manage articles.

You can use multiple inputs to an invocable action. This technique is useful for actions that don’t take lists, such as
`restoreKnowledgeArticleVersion` .

Supported REST HTTP Methods

**URIs**

Archive Knowledge articles:

```
    /services/data/v XX.X /actions/standard/archiveKnowledgeArticles

```

Assign Knowledge articles:

```
    /services/data/v XX.X /actions/standard/assignKnowledgeArticles

```

Create draft from online Knowledge articles:

```
    /services/data/v XX.X /actions/standard/createDraftFromOnlineKnowledgeArticle

```

Delete Knowledge articles:

```
    /services/data/v XX.X /actions/standard/deleteKnowledgeArticles

```

58

Action Objects Knowledge Actions

Publish Knowledge articles:

```
    /services/data/v XX.X /actions/standard/publishKnowledgeArticles

```

Restore Knowledge article version:

```
    /services/data/v XX.X /actions/standard/restoreKnowledgeArticleVersion

```

Retrieve Smart Link URL:

```
    /services/data/v XX.X /actions/standard/getArticleSmartLinkUrl

```

Submit Knowledge article for translation:

```
    /services/data/v XX.X /actions/standard/submitKnowledgeArticleForTranslation

```

**Formats**
JSON, XML

**HTTP Methods**
GET, HEAD, POST

**Authentication**

```
    Authorization: Bearer token

```

**Other Information**

Error Response Types on page 69

Archive Knowledge Articles

URI: `/services/data/v` _**`XX.X`**_ `/actions/standard/archiveKnowledgeArticles`

**Table 1: Inputs**

**Input** **Details**

```
articleVersionIdList

```

**Sample Input**

**Type**
string

**Description**
Required. Comma-separated article version ID list.

The following code sample archives two articles:

```
  {

   "inputs" : [

    {

      "articleVersionIdList" : [ "ka0RM00000004VeYAI", "ka0RM00000003doYAA" ]

    }

   ]

  }

```

**Sample Output**

The following code sample illustrates a response after a successful request.

```
  [ {

   "actionName" : "archiveKnowledgeArticles",

```

59

Action Objects Knowledge Actions

```
      "errors" : null,

      "isSuccess" : true,

      "outputValues" : {

       "ka0RM00000004Ve" : "Success",

       "ka0RM00000003do" : "Success"

      }

     } ]

```

The following code sample illustrates a response with one success and one failure:

```
     [ {

      "actionName" : "archiveKnowledgeArticles",

      "errors" : null,

      "isSuccess" : false,

      "outputValues" : {

       "ka0RM00000004Ve" : "You can't perform this action. Be sure the action is valid for

      the current state of the article, and that you have permission to perform it.",

       "ka0RM00000003do" : "Success"

      }

     } ]

```

Assign Knowledge Articles

URI: `/services/data/v` _**`XX.X`**_ `/actions/standard/assignKnowledgeArticles`

**Table 2: Inputs**

**Input** **Details**

```
articleVersionIdList

assigneeId

assignAction

dueDate

```

**Type**
string

**Description**
Required. Comma-separated article version ID list.

**Type**
ID

**Description**
Required. ID of the assigned user.

**Type**
string

**Description**
Required. Assign action. Valid actions are:

**•** ASSIGN_DRAFT_MASTER

**•** ASSIGN_DRAFT_TRANSLATION

**Type**
string

60

Action Objects Knowledge Actions

**Input** **Details**

**Description**
Optional. Assigned due date.

```
instruction

sendEmailNotification

```

**Sample Input**

**Type**
string

**Description**
Optional. Instructions for the assignee.

**Type**
boolean

**Description**
Optional. Indicates whether to send an email notification. Defaults to `false` .

The following code sample assigns two articles for translation:

```
  {

   "inputs" : [

    {

      "articleVersionIdList" : [ "ka0RM00000004VeYAI", "ka0RM00000003doYAA" ]

      "assigneeId" : "005RM00000AAAAAYA4",

      "assignAction" : "ASSIGN_DRAFT_TRANSLATION"

    }

   ]

  }

```

**Sample Output**

The following code sample illustrates a response after a successful request.

```
  [ {

   "actionName" : "assignKnowledgeArticles",

   "errors" : null,

   "isSuccess" : true,

   "outputValues" : {

    "ka0RM00000004Ve" : "Success",

    "ka0RM00000003do" : "Success"

   }

  } ]

```

Create Draft from Online Knowledge Article

URI: `/services/data/v` _**`XX.X`**_ `/actions/standard/createDraftFromOnlineKnowledgeArticle`

61

Action Objects Knowledge Actions

**Table 3: Inputs**

**Input** **Details**

```
action

unpublish

articleVersionId

articleId

```

**Sample Input**

**Type**
string

**Description**
Required. Edit action for primary language or translation articles. Valid actions are:

**•** EDIT_AS_DRAFT_ARTICLE

**•** EDIT_AS_DRAFT_TRANSLATION

**Type**
boolean

**Description**
Required. Indicates whether to keep the article published ( `false` ) or archive the published
article ( `true` ). Use `false` to keep the current article version online and create a draft. Use
`true` to archive the current online version, which removes it from the knowledge base, and
creates a draft.

**Type**
string

**Description**
Article version ID. Required to create a draft from an online (published) translation. Optional to
create a draft from the online primary article if the Article ID is provided.

**Type**
string

**Description**
Article ID. Required when creating a draft from the online (published) primary article if the Article
Version ID isn’t provided.

The following code sample creates a draft from a primary article and archives the original article:

```
{

  "inputs" : [

   {

    "action" : "EDIT_AS_DRAFT_ARTICLE",

    "unpublish" : true,

    "articleId" : "kA0RM00000004pP0AQ"

   }

  ]

}

```

62

Action Objects Knowledge Actions

**Sample Output**

The following code sample illustrates a response after a successful request.

```
     [ {

      "actionName" : "createDraftFromOnlineKnowledgeArticle",

      "errors" : null,

      "isSuccess" : true,

      "outputValues" : {

       "kA0RM00000004pP0AQ" : "Success"

      }

     } ]

```

Delete Knowledge Articles

URI: `/services/data/v` _**`XX.X`**_ `/actions/standard/deleteKnowledgeArticles`

**Table 4: Inputs**

**Input** **Details**

```
articleVersionIdList

```

**Sample Input**

**Type**
string

**Description**
Required. Comma-separated article version ID list.

The following code sample deletes two articles:

```
  {

   "inputs" : [

    {

      "articleVersionIdList" : [ "ka0RM00000004VeYAI", "ka0RM00000003doYAA" ]

    }

   ]

  }

```

**Sample Output**

The following code sample illustrates a response after a successful request.

```
  [ {

   "actionName" : "deleteKnowledgeArticles",

   "errors" : null,

   "isSuccess" : true,

   "outputValues" : {

    "ka0RM00000004Ve" : "Success",

    "ka0RM00000003do" : "Success"

   }

  } ]

```

63

Action Objects Knowledge Actions

Publish Knowledge Articles

URI: `/services/data/v` _**`XX.X`**_ `/actions/standard/publishKnowledgeArticles`

**Table 5: Inputs**

**Input** **Details**

```
articleVersionIdList

pubAction

pubDate

```

**Sample Input**

**Type**
string

**Description**
Required. Comma-separated article version ID list.

**Type**
string

**Description**
Required. Publish action. Valid actions are:

**•** PUBLISH_ARTICLE (which replaces the latest version)

**•** PUBLISH_ARTICLE_NEW_VERSION (which creates a new version)

**•** SCHEDULE_ARTICLE_FOR_PUBLICATION

**•** PUBLISH_TRANSLATION

**Type**
string

**Description**
Optional. Scheduled publish date in ISO 8601 format `yyyy-MM-dd\'T\'HH:mm:ss.SSSZ` .
For example, for February 8, 2023, 1:40 pm UTC+01:00 use
`2023-02-08T13:40:00.000+0100` .

The following code sample publishes two articles:

```
  {

   "inputs" : [

    {

      "articleVersionIdList" : [ "ka0RM00000004VeYAI", "ka0RM00000003doYAA" ],

      "pubAction" : "PUBLISH_ARTICLE"

    }

   ]

  }

```

**Sample Output**

The following code sample illustrates a response after a successful request.

```
  [ {

   "actionName" : "publishKnowledgeArticles",

   "errors" : null,

   "isSuccess" : true,

```

64

Action Objects Knowledge Actions

```
      "outputValues" : {

       "ka0RM00000004Ve" : "Success",

       "ka0RM00000003do" : "Success"

      }

     } ]

```

Restore Knowledge Article Version

URI: `/services/data/v` _**`XX.X`**_ `/actions/standard/restoreKnowledgeArticleVersion`

**Table 6: Inputs**

**Input** **Details**

```
action

articleId

versionNumber

```

**Sample Input**

**Type**
string

**Description**
Required. The only valid action is: RESTORE_KNOWLEDGE_ARTICLE_VERSION

**Type**
string

**Description**
Required. Article ID.

**Type**
integer

**Description**
Optional. Version number of the archived article version to restore. Default is the latest archived
version.

The following code restores the latest archived version:

```
{

  "inputs" : [

   {

    "action" : "RESTORE_KNOWLEDGE_ARTICLE_VERSION",

    "articleId" : "kA0RM00000004pP0AQ"

   }

  ]

}

```

The following code restores a past archived version of a published article:

```
{

  "inputs" : [

   {

    "action" : "RESTORE_KNOWLEDGE_ARTICLE_VERSION",

    "versionNumber":3,

```

65

Action Objects Knowledge Actions

```
         "articleId" : "kA0RM00000004pP0AQ"

       }

      ]

     }

```

The following code restores two archived articles:

```
     {

      "inputs" : [

       {

         "action" : "RESTORE_KNOWLEDGE_ARTICLE_VERSION",

         "articleId" : "kA0RM00000004pP0AQ"

       },

       {

         "action" : "RESTORE_KNOWLEDGE_ARTICLE_VERSION",

         "articleId" : "kA0RM00000004pP0AB"

       }

      ]

     }

```

**Sample Output**

The following code sample illustrates a response after a successful request.

```
     [ {

      "actionName" : "restoreKnowledgeArticleVersion",

      "errors" : null,

      "isSuccess" : true,

      "outputValues" : {

       "kA0RM00000004pP0AQ" : "Success"

      }

     } ]

```

Retrieve Smart Link URL

URI: `/services/data/v` _**`XX.X`**_ `/actions/standard/getArticleSmartLinkUrl`

**Table 7: Inputs**

**Input** **Details**

```
articleVersionId

```

**Sample Input**

**Type**
string

**Description**
Required. The ID of the Knowledge article version.

The following code sample retrieves the SmartLink URL of a Knowledge article version:

```
{

  "inputs":[

    {

      "articleVersionId":"ka0xx00000000cjAAA"

```

66

Action Objects Knowledge Actions

```
         }

       ]

     }

```

**Sample Output**

The following code sample illustrates a response after a successful request.

```
     [

       {

         "actionName":"getArticleSmartLinkUrl",

         "errors":null,

         "isSuccess":true,

         "outputValues":{

     "articleSmartLinkUrl":"https://example.lightning.force.com/lightning/articles/Knowledge/Test-Redirection-1"

         }

       }

     ]

```

Submit Knowledge Article for Translation

URI: `/services/data/v` _**`XX.X`**_ `/actions/standard/submitKnowledgeArticleForTranslation`

**Table 8: Inputs**

**Input** **Details**

```
articleId

language

assigneeId

dueDate

```

**Type**
string

**Description**
Required. Article ID.

**Type**
string

**Description**
Required. Language code for the translation.

**Type**
ID

**Description**
Required. ID of the assigned user.

**Type**
string

**Description**
Optional. Assigned due date.

67

Action Objects Knowledge Actions

**Input** **Details**

```
sendEmailNotification

```

**Type**
boolean

**Description**
Optional. Indicates whether to send an email notification. Defaults to `false` .

**Table 9: Outputs**

**Output** **Details**

```
articleId

language

```

**Sample Input**

**Type**
ID

**Description**
Article ID.

**Type**
string

**Description**
Language code for the translation.

The following code sample submits one article for translation into Spanish:

```
  {

   "inputs" : [

    {

      "articleId" : "kA0RM00000004pP0AQ",

      "language" : "es",

      "assigneeId" : "005RM00000AAAAAYA4"

    }

   ]

  }

```

**Sample Output**

The following code sample illustrates a response after a successful request.

```
  [ {

   "actionName" : "submitKnowledgeArticleForTranslation",

   "errors" : null,

   "isSuccess" : true,

   "outputValues" : {

    "articleId" : "kA0RM00000004pP0AQ",

    "language" : "es"

   }

  } ]

```

68

## Action Objects Lead Action

Error Response Types

Knowledge actions can respond with two types of error responses: action-scoped errors and item-scoped errors.

Action-scoped errors describe an error about the overall action that you’re trying to invoke. Action-scoped errors have a `statusCode`
in addition to a `message` . This example illustrates an action-scoped error caused by sending invalid input values.

```
   [ {

         "actionName" : "restoreKnowledgeArticleVersion",

         "errors" : [ {

         "statusCode" : "INVALID_API_INPUT",

         "message" : "You can't perform this action. Be sure the action is valid for the

   current state of the article, and that you have permission to perform it.",

         "fields" : [ ]

         } ],

         "isSuccess" : false,

         "outputValues" : null

         } ]

```

Item-scoped errors describe a problem with a specific article or article version within the action. For example, this code illustrates an
archiveKnowledgeArticles action response with one failed item and one successful item.

```
   [ {

         "actionName" : "archiveKnowledgeArticles",

         "errors" : null,

         "isSuccess" : false,

         "outputValues" : {

         "ka0RM00000004Ve" : "You can't perform this action. Be sure the action is valid

   for the current state of the article, and that you have permission to perform it.",

         "ka0RM00000003do" : "Success"

         }

         } ]

```

If any type of error occurs with an action, the `isSuccess` field is `false` .

## Lead Action

Manage your leads using the invocable action.

Leads must be enabled in your org. The user must have read and edit permissions for leads.

Supported REST HTTP Methods

**URIs**

Apply Lead Assignment Rules:

```
    /services/data/v XX.X /actions/standard/invocableApplyLeadAssignmentRules

```

**Formats**
JSON, XML

**HTTP Methods**
GET, HEAD, POST

**Authentication**

```
    Authorization: Bearer token

```

69

Action Objects Lead Action

**Other Information**

Error Response Types on page 70

Apply Lead Assignment Rules

Run lead assignment rules on a collection of leads.

Available in API version 54.0.

URI: `/services/data/v` _**`XX.X`**_ `/actions/standard/invocableApplyLeadAssignmentRules`

**Table 10: Inputs**

**Input** **Details**

```
LeadIds

```

**Sample Input**

**Type**
String Collection

**Description**
Required. A collection of lead IDs to run lead assignment rules for.

The following code runs lead assignment rules for two leads:

```
  {"inputs": [ {

      "leadId" : "00QR00000006LE8OAM"

    },

    {

       "leadId" : "00QR00000006LEDOA2"

    }]

  }

```

**Sample Output**

The following code sample illustrates a response when the action succeeds.

```
  [ {

       "actionName" : "invocableApplyLeadAssignmentRules",

       "isSuccess" : true

       } ]

```

Error Response Types

Sales Engagement actions can respond with success or errors.

If any type of error occurs with an action, the `isSuccess` field is `false` .

This example illustrates an error caused when the user has insufficient access to leads when calling the Apply Lead Assignment Rules
action.

```
[ {

  "actionName" : "invocableApplyLeadAssignmentRules",

  "errors" : [ {

   "statusCode" : "INSUFFICIENT_ACCESS_OR_READONLY",

```

70

## Action Objects Live Message Notification Actions

```
      "message" : "Looks like you don't have access to this record. Your Salesforce admin

   can help with that.",

      "fields" : [ ]

     } ],

     "isSuccess" : false,

     "outputValues" : null

   } ]

```

This example illustrates an error caused when the lead IDs passed to the Apply Lead Assignment Rules action are invalid.

```
   [ {

     "actionName" : "invocableApplyLeadAssignmentRules",

     "errors" : [ {

      "statusCode" : "UNKNOWN_EXCEPTION",

      "message" : "Something's not right with one or more the specified LeadIds. Check the

   IDs and try again.",

      "fields" : [ ]

     } ],

     "isSuccess" : false,

     "outputValues" : null

   } ]

```

This example illustrates an error caused when one of the leads passed to the Apply Lead Assignment Rules action has been deleted.

```
   [ {

     "actionName" : "invocableApplyLeadAssignmentRules",

     "errors" : [ {

      "statusCode" : "ENTITY_IS_DELETED",

      "message" : "One or more of the specified LeadIds were deleted. Check the IDs and try

    again.",

      "fields" : [ ]

     } ],

     "isSuccess" : false,

     "outputValues" : null

   } ]

## Live Message Notification Actions

```

Use messaging templates to send notifications to users over communication channels, such as SMS, WhatsApp, and Facebook Messenger,
when certain conditions are met.

This action is available in API version 43.0 and later.

[For more information about using Live Message Notification actions in flows, see Create Flows to Send Automatic Message Notifications](https://help.salesforce.com/HTViewHelpDoc?id=sf.livemessage_automatic_notifications_flows.htm&language=en_US)
in Salesforce Help.

Special Access Rules

To access Live Message Notification action for Surveys, you must have the Feedback Management Starter or Growth license and Salesforce
org enabled with a default community.

71

Action Objects Live Message Notification Actions

Supported REST HTTP Methods

**URI**

```
    /services/data/v 43.0 /actions/standard/liveMessageNotification

```

**Formats**
JSON, XML

**HTTP Methods**
GET, HEAD, POST

**Authentication**

```
    Authorization: Bearer token

```

Inputs

**Input** **Details**

```
channelDeveloperName

contextRecordId

conversationBroadcastId

recipientPhone

recipientRecordId

```

**Type**
string

**Description**
Required. The unique name of the messaging channel that’s used to send the messaging
notification.

**Type**
ID

**Description**
The entity ID of the sObject that’s used as the context for the merge field in a messaging template.

To resolve a merge field, the `contextRecordId` input property is required.

**Type**
ID

**Description**
The entity ID of the sObject that links all the messages within a broadcast.

**Type**
string

**Description**
The destination phone number that the message is sent to. If the messaging channel type is
SMS and the `recipientRecordId` input property isn’t a messaging user, then the
`recipientPhone` input property is required.

**Type**
ID

**Description**
Required. The `MessagingEndUserId` property or the Record ID associated with a recipient
phone number, to send the message notification.

72

Action Objects Live Message Notification Actions

**Input** **Details**

```
surveyDeveloperName

templateDeveloperName

triggeredOutboundTypeEnum

```

Outputs

None.

Example

**GET**

**Type**
string

**Description**
The API name of the survey that’s sent in the message. Available in API version 57.0 and later.

This input property is applicable to Surveys only.

**Type**
string

**Description**
Required. The unique name of the messaging template that’s used to generate the message.

**Type**
picklist

**Description**
The type of triggered outbound message. Possible values are:

**•** `Standard`

**•** `Broadcast`

The following example shows how to get information about the Live Message Notification action type:

```
  curl --include --request GET \

  --header "Authorization: Authorization: Bearer 00DR...xyz" \

  --header "Content-Type: application/json" \

  "https://instance.salesforce.com/services/data/v43.0/actions/standard/liveMessageNotification"

```

**POST**

Here’s an example request for the Live Message Notification action:

```
  {

    "inputs":[{

      "templateDeveloperName":"MessageQ3Template",

      "channelDeveloperName":"MessageQ3Template",

      "contextRecordId":"003RO00000480RvYAM",

      "recipientRecordId":"0PARM000000GJzo4AG"

    }]

  }

```

73

## Action Objects Omni-Channel Action

Here’s an example response for the Live Message Notification action:

```
     [

       {

         "actionName" : "liveMessageNotification",

         "errors" : null,

         "isSuccess" : true,

         "outputValues" : null

       }

     ]

## Omni-Channel Action

```

Create a `PendingServiceRouting` record used for Omni-Channel skills-based routing.

[For more information about skills-based routing, see Skills-Based Routing for Omni-Channel in Salesforce Help.](https://help.salesforce.com/articleView?id=omnichannel_skills_based_routing.htm&language=en_US)

This object is available in API version 44.0 and later.

Supported REST HTTP Methods

**URI**

```
    /services/data/v XX.X /actions/standard/skillsBasedRouting

```

**Formats**
JSON, XML

**HTTP Methods**
POST

**Authentication**

```
    Authorization: Bearer token

```

Inputs

**Input** **Details**

```
recordId

routingConfigId

skillIdList

```

**Type**
ID

**Description**
Required. ID of the Salesforce record to be routed by Omni-Channel.

**Type**
ID

**Description**
Required. ID of the `[QueueRoutingConfig](https://developer.salesforce.com/docs/atlas.en-us.258.0.object_reference.meta/object_reference/sforce_api_objects_queueroutingconfig.htm)` record to be used by Omni-Channel.

**Type**
string

74

## Action Objects Apply Payment Action

**Input** **Details**

**Description**
Optional. Comma-separated list of `[Skill](https://developer.salesforce.com/docs/atlas.en-us.258.0.object_reference.meta/object_reference/sforce_api_objects_skill.htm)` IDs. Maximum number of skills is 25.

Outputs

**Output** **Details**

```
pendingServiceRoutingId

```

Usage

**Sample Input**

**Type**
ID

**Description**
ID of the new `[PendingServiceRouting](https://developer.salesforce.com/docs/atlas.en-us.258.0.omni_channel_dev.meta/omni_channel_dev/sforce_api_objects_pendingservicerouting.htm)` record, if the request was successful.

The following code sample attempts to create a `PendingServiceRouting` record using a work record ( `recordId` ), the
routing configuration ( `routingConfigId` ), and two skills ( `skillIdList` ).

```
  {

   "inputs": [{

      "recordId":"400B0000004GGUUIA4",

      "routingConfigId":"0K8B0000000CbgZKAS",

      "skillIdList":"0C4B00000008QImKAM,0C4B0000000CcR1KAK"

   }]

  }

```

**Sample Output**

The following code sample illustrates a response after a successful request.

```
  [

   {

    "actionName":"skillsBasedRouting",

    "errors":null,

    "isSuccess":true,

    "outputValues":{

      "pendingServiceRoutingId":"0JRB0000000TWA2"

    }

   }

  ]

## Apply Payment Action

```

Applies a payment record to an invoice header by creating a PaymentLineInvoice record with a type of Applied.

To access Commerce Payments resources, you need the following permissions.

75

Action Objects Apply Payment Action

**•** Salesforce Order Management License or Salesforce B2B Commerce License

**•** PaymentsAPIUser user permission. This permission is available with the Salesforce Order Management or B2B Commerce License.
Your Salesforce admin assigns it to your user profile.

This object is available in API version 54.0 and later.

Supported REST HTTP Methods

**URI**

```
    /services/data/v54.0/actions/standard/applyPayment

```

**Formats**
JSON

**HTTP Methods**
POST

**Authentication**

```
    Authorization: Bearer token

```

Inputs

**Input** **Details**

```
amount

appliedToId

associatedAccountId

comments

effectiveDate

```

**Type**
number

**Description**
Required. The amount to be applied to the invoice header.

**Type**
ID

**Description**
Required. The ID of the invoice that receives the payment.

**Type**
ID

**Description**
Optional. The ID of the account that contains the invoice.

**Type**
String

**Description**
Optional comments for more information about the payment application.

**Type**
datetime

76

## Action Objects Payment Sale Action

**Input** **Details**

**Description**
Optional. The date that the payment takes effect on the invoice.

```
paymentId

```

Outputs

**Type**
string

**Description**
Required. The payment that's applied to the invoice. The application is represented by the
PaymentLineInvoice created for a successful action.

**Output** **Details**

```
appliedDate

paymentLineInvoiceId

```

**Type**
datetime

**Description**
The date that the payment was applied to the invoice header.

**Type**
ID

**Description**
Represents the application of the payment's amount to the invoice. Created after a successful
action.

## Payment Sale Action

Capture a payment without any prior authorization and create a payment record. The payment sale transaction consists of an authorize
request and a capture request made to the payment gateway at the same time. This way, the merchant can request funds to be transferred
to the merchant account in a single command, with no further action required.

To access Commerce Payments resources, you need the following permissions.

**•** Salesforce Order Management License or Salesforce B2B Commerce License

**•** PaymentsAPIUser user permission. This permission is available with the Salesforce Order Management or B2B Commerce License.
Your Salesforce admin assigns it to your user profile.

The payment sale API handles only one payment at a time. Bulk requests aren't supported.

This object is available in API version 54.0 and later.

Supported REST HTTP Methods

**URI**

```
  /services/data/v54.0/actions/standard/paymentSale

```

77

Action Objects Payment Sale Action

**Formats**
JSON

**HTTP Methods**
POST

**Authentication**

```
    Authorization: Bearer token

```

Inputs

**Input** **Details**

```
amount

paymentGatewayId

paymentMethodId

currencyIsoCode

idempotencyKey

```

**Type**
number

**Description**
Required. The amount of the payment sale request.

**Type**
ID

**Description**
Required. The ID of the Salesforce payment gateway record that represents the external payment
gateway used for processing the sale request.

**Type**
ID

**Description**
Required. The ID of the Salesforce payment method that contains customer payment information.

**Type**
string

**Description**
Required for multicurrency orgs. Three-letter ISO 4217 currency code associated with the payment
output.

**Type**
string

**Description**
Optional. Key used to ensure idempotency and avoid duplicate payments.

78

## Action Objects Perform Survey Sentiment Analysis

Outputs

**Output** **Details**

```
actionName

errors

isSuccess

outputValues

```

**Type**
string

**Description**
The name of the action performed. Becomes `paymentSale` following a Payment Sale action.

**Type**
string

**Description**
Following a `400` error response, the error objects show information about the error that occurred.
Contains a status code, message, and list of fields.

**Type**
boolean

**Description**
Shows whether the payment sale request was successful.

**Type**
ID

**Description**
The ID of the new payment request record.

## Perform Survey Sentiment Analysis

Create or update the AI Sentiment Result records. You can get insights into the sentiments underlying survey responses and save the
sentiment analysis in the SentimentAnalysisResult object.

This action is available in API version 55.0 and later.

Special Access Rules

To access the Perform Survey Sentiment Analysis action, you must have the Feedback Management - Starter and Feedback Management

- Growth licenses.

Supported REST HTTP Methods

**URI**

```
  /services/data/v 55.0 /actions/standard/performSurveySentimentAnalysis

```

**Formats**
JSON

79

Action Objects Perform Survey Sentiment Analysis

**HTTP Methods**
POST

**Authentication**

```
    Authorization: Bearer token

```

Inputs

**Input** **Details**

```
surveyId

surveyQuestionIds

startDate

endDate

typeOfOperation

```

**Type**
ID

**Description**
Required. The ID of the survey containing the questions for whose responses you want to get
sentiment insights.

**Type**
ID

**Description**
Required. The IDs of the questions for whose responses you want to get sentiment insights.

**Type**
Datetime

**Description**
Required. The date from when participant responses are processed to get sentiment insights.

**Type**
Datetime

**Description**
Required. The date until when participant responses are processed to get sentiment insights.

**Type**
String

**Description**
Required. The type of operation to be performed on the survey responses.

Possible values are:

**•** `create` —Bulk process survey responses. After the processing is completed, the AI Sentiment
Result records are created with the Submitted status.

**•** `update` —Bulk process survey responses that have associated AI Sentiment Result records
in the Draft status. After the processing is completed, the AI Sentiment Result records are
updated and their status is changed to Submitted.

You can only update a sentiment analysis result record with the Draft status.

80

## Action Objects PlatformAction

Outputs

None.

Example

**Sample Request**

Here’s an example POST request to create or update the AI Sentiment Result records:

```
     {

       "inputs":[{

         "surveyId":"0Kdx00000000GYeCAM",

         "surveyQuestionIds":["0Kux00000000xDgCAI","0Kux00000000xDiCAI"],

         "startDate":"1-07-2022",

         "endDate":"12-07-2022",

         "typeOfOperation":"create"

       }]

     }

```

SEE ALSO:

_Salesforce Help_ [: Automate Your Business Process: Perform Survey Sentiment Analysis](https://help.salesforce.com/s/articleView?id=sf.flow_ref_elements_actions_surveys_perform_survey_sentiment_analysis.htm&language=en_US)

## PlatformAction PlatformAction is a virtual read-only object. It enables you to query for actions displayed in the UI, given a user, a context, device format,

and a record ID. Examples include standard and custom buttons, quick actions, and productivity actions.

Supported Calls

`describeSObjects()`, `query()`

Fields

**Field** **Details**

```
ActionListContext

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Required. The list context this action applies to. Valid values are:

**•** `Assistant`

**•** `BannerPhoto`

**•** `Chatter`

**•** `Dockable`

81

Action Objects PlatformAction

**Field** **Details**

**•** `FeedElement`

**•** `Flexipage`

**•** `Global`

**•** `ListView`

**•** `ListViewDefinition`

**•** `ListViewRecord`

**•** `Lookup`

**•** `MruList`

**•** `MruRow`

**•** `ObjectHomeChart`

**•** `Photo`

**•** `Record`

**•** `RecordEdit`

**•** `RelatedList`

**•** `RelatedListRecord`

```
ActionTarget

ActionTargetType

ActionTargetUrl

```

**Type**
textarea

**Properties**
Nillable

**Description**
The URL to invoke or describe the action when the action is invoked. If the action is a standard
button overridden by a Visualforce page, the ActionTarget returns the URL of the Visualforce
page, such as `/apex/` _`pagename`_ .

This field is available in API version 35.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of the target when this action is triggered. Valid values are:

**•** `Describe` —applies to actions with a user interface, such as quick actions

**•** `Invoke` —applies to actions with no user interface, such as action links or invocable
actions

**•** `Visualforce` —applies to standard buttons overridden by a Visualforce page

**Type**
string

82

Action Objects PlatformAction

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
URL to invoke or describe the action when the action is invoked. This field is deprecated in
API version 35.0 and later. Use `ActionTarget` instead.

```
Category

ConfirmationMessage

DeviceFormat

ExternalId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Applies only to action links. Denotes whether the action link shows up in the feed item list
of actions or the overflow list of actions. Valid values are:

**•** `Primary`

**•** `Overflow`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Applies only to action links. The message to display before the action is invoked. Field is null
if no confirmation is required before invoking the action.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies which action icon the PlatformAction query returns. If this field isn’t specified, it
defaults to Phone. Valid values are:

**•** `Aloha`

**•** `Desktop`

**•** `Phone`

**•** `Tablet`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

83

Action Objects PlatformAction

**Field** **Details**

**Description**
The unique ID for the PlatformAction. If the action doesn’t have an ID, its API name is used.

```
GroupId

IconContentType

IconHeight

IconUrl

IconWidth

InvocationStatus

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a group of action links.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The content type—such as .jpg, .gif, or .png—of the icon for this action. Applies to both
custom and standard icons assigned to actions.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The height of the icon for this action. Applies only to standard icons.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URL of the icon for this action.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The width of the icon for this action. Applies only to standard icons.

**Type**
picklist

84

Action Objects PlatformAction

**Field** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of the action within the feed item. Applies to action links only. Valid values are:

**•** `Failed`

**•** `New`

**•** `Pending`

**•** `Successful`

```
InvokedByUserId

IsGroupDefault

IsMassAction

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who most recently invoked this action within the current feed item. Applies
to action links only.

This is a relationship field.

**Relationship Name**
InvokedByUser

**Relationship Type**
Lookup

**Refers To**
User

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Denotes whether this action is the default in an action link group. False for other action types.
Applies to action links only.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the action can be performed on multiple records.

This field is available in API version 38.0 and later.

85

Action Objects PlatformAction

**Field** **Details**

```
Label

PrimaryColor

RelatedListRecordId

RelatedSourceEntity

Section

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The label to display for this action.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The primary color of the icon for this action.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the ID of a record in an object’s related list.

This field is available in API version 38.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
When the `ActionListContext` is RelatedList or RelatedListRecord, this field represents
the API name of the related list to which the action belongs.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The section of the user interface the action resides in. Applicable only to Lightning Experience.
Valid values are:

**•** ActivityComposer

**•** CollaborateComposer

**•** NotesComposer

**•** Page

86

Action Objects PlatformAction

**Field** **Details**

**•** SingleActionLinks

This field is available in API version 35.0 and later.

```
SourceEntity

Subtype

TargetObject

TargetUrl

Type

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Required. The object or record with which this action is associated.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The subtype of the action. For quick actions, the subtype is `QuickActionType` . For
custom buttons, the subtype is `WebLinkTypeEnum` . For action links, subtypes are `Api`,
`ApiAsync`, `Download`, and `Ui` . Standard buttons and productivity actions have no
subtype.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of object record the action creates, such as a contact or opportunity.

This field is available in API version 41.0 and later.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The URL that a custom button or link points to.

This field is available in API version 41.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

87

Action Objects PlatformAction

**Field** **Details**

**Description**
The type of the action. Valid values are:

**•** `ActionLink` —An indicator on a feed element that targets an API, a web page, or a
file, represented by a button in the Salesforce Chatter feed UI.

**•** `CustomButton` —When clicked, opens a URL or a Visualforce page in a window or
executes JavaScript.

**•** `InvocableAction`

**•** `ProductivityAction` —Productivity actions are predefined and attached to a
limited set of objects. Productivity actions include Send Email, Call, Map, View Website,
and Read News. Except for the Call action, you can’t edit productivity actions.

**•** `QuickAction` —A global or object-specific action.

**•** `StandardButton` —A predefined Salesforce button such as New, Edit, and Delete.

Usage

PlatformAction can be described using describeSObject().

You can directly query for PlatformAction. For example, this query returns all fields for actions associated with each of the records of the
listed objects:

```
   SELECT ExternalId, ActionTargetType, ActionTargetUrl, ApiName, Category,

       ConfirmationMessage, ExternalId, GroupId, UiTheme, IconUrl, IconContentType,

       IconHeight, IconWidth, PrimaryColor, InvocationStatus, InvokedByUserId,

       IsGroupDefault, Label, LastModifiedDate, Subtype, SourceEntity, Type

   FROM PlatformAction

   WHERE SourceEntity IN ('001xx000003DGsH', '001xx000003DHBq', ‘Task’) AND

       ActionListContext = ‘Record’;

```

Note: To query PlatformAction, provide the `ActionListContext` and `SourceEntity` . If you query for
`ActionListContext` with a value of `RelatedList`, and don't specify a `RelatedSourceEntity`, the query returns
the API name of the related list. In API v43.0 and before, `SourceEntity = '` _**`Object API Name`**_ `' and`
`ActionListContext = 'ListView'` is an invalid combination to fetch quick actions in a SOQL query. Use
`SourceEntity = '` _**`Object ID`**_ `' and ActionListContext = 'ListView'` instead.

This query uses multiple `ActionListContext` values in its `WHERE` clause to return all actions in the Lightning Experience user
interface ( `DeviceFormat = 'Desktop'` ) for the specified object:

```
   SELECT ActionListContext, Label, Type, Subtype, Section, SourceEntity,

      RelatedSourceEntity, ActionTarget, ActionTargetType, ApiName, Category,

      ConfirmationMessage, DeviceFormat, ExternalId, GroupId, IconContentType,

      IconHeight, IconUrl, IconWidth, Id, InvocationStatus, InvokedByUserId,

      IsGroupDefault, LastModifiedDate, PrimaryColor

   FROM PlatformAction

   WHERE ActionListContext IN ('Record','Chatter','RelatedList') AND

       SourceEntity = '001xx000003DlvX' AND

       DeviceFormat = 'Desktop'

```

88

## Action Objects Post to Chatter Actions Post to Chatter Actions

Post to the feed for a specific record, user, or Chatter group.

Use a Post to Chatter action to post a message at run time to a specified feed. Post to Chatter supports @mentions and topics, but only
text posts are supported.

This object is available in API version 32.0 and later.

Supported REST HTTP Methods

**URI**
Get a list of available post to Chatter actions:

```
    /services/data/v XX.X /actions/standard/chatterPost

```

**Formats**
JSON, XML

**HTTP Methods**
GET, HEAD, POST

**Authentication**

```
    Authorization: Bearer token

```

Inputs

**Input** **Details**

```
communityId

subjectNameOrId

text

```

**Type**
reference

**Description**
Optional. Specifies the ID of an Experience Cloud site to post to. Valid only if Digital Experiences
is enabled. Required if posting to a user or Chatter group that belongs to an Experience Cloud
site. This value is available in API version 35.0 and later.

**Type**
string

**Description**
Required. Reference to the user, Chatter group, or record whose feed you want to post to.

**•** To post to a user’s feed, enter the user’s `ID` or `Username` . For example:

```
   jsmith@salesforce.com

```

**•** To post to a Chatter group, enter the group’s `Name` or `ID` . For example: _`Entire`_

```
   Organization

```

**•** To post to a record, enter the record’s `ID` . For example: _`001D000000JWBDx`_

**Type**
string

89

## Action Objects Preview Cart to Exchange Order

**Input** **Details**

**Description**
Required. The text that you want to post. Must be a string of no more than 10,000 characters.

To mention a user or group, enter @[ `reference` ], where `reference` is the ID for the user
or group that you want to mention. The reference can be a literal value, a merge field, or a flow
resource.

To add a topic, enter #[ `string` ], where `string` is the topic that you want to add.

For example, the string `Hi @[005000000000001] check this out`
`#[some_topic].` is stored appropriately as `Hi @Joe, check this out`
`#some_topic.` where “@Joe” and “#some_topic” are links to the user and topic, respectively.

```
type

visibility

```

Outputs

**Type**
picklist

**Description**
Required only if `subjectNameOrId` is set to a username or a Chatter group name. The type
of feed that you want to post to.

**•** _`User`_ —Enter this value if `subjectNameOrId` is set to a user’s `Username` .

**•** _`Group`_ —Enter this value if `subjectNameOrId` is set to a Chatter group’s `Name` .

**Type**
picklist

**Description**
Optional. Valid only if Digital Experiences is enabled. Specifies whether this feed item is available
to all users or internal users only. Valid values are:

**•** _`allUsers`_

**•** _`internalUsers`_

This value is available in API version 35.0 and later.

**Output** **Details**

```
feedItemId

```

**Type**
reference

**Description**
The ID of the new Chatter feed item.

## Preview Cart to Exchange Order

Generate preview details of an exchange order for specified order summary, exchange cart ID, and reference record ID.

90

Action Objects Preview Cart to Exchange Order

To access, you need the following permissions.

**•** Salesforce Order Management License or Salesforce B2B Commerce License

This object is available in API version 60.0 and later.

Supported REST HTTP Methods

**URI**

```
    /services/data/v59.0/actions/standard/previewCartToExchangeOrder

```

**Formats**
JSON, XML

**HTTP Methods**
GET, HEAD, POST

**Authentication**
Authorization: Bearer token

Inputs

**Input** **Details**

```
orderSummaryId

exchangeCartId

referenceId

```

Outputs

**Type**
ID

**Description**
Required. The ID of the order summary record associated with the list of exchanges.

**Type**
ID

**Description**
Required. The ID of the cart record containing the items for the exchange order.

**Type**
ID

**Description**
Required. The ID of the record that's related to the specified order summary. Only IDs from a
return order record are supported.

**Output** **Details**

```
changeBalances

```

**Type**
string

91

## Action Objects Prompt Template Actions

**Output** **Details**

**Description**
A string that contains the calculated amounts resulting from the exchange order.

```
errors

isSuccess

orderSummaryID

```

**Type**
string

**Description**
Following a `400` error response, the error objects show information about the error that occurred.
Contains a status code, message, and list of fields.

**Type**
boolean

**Description**
Shows whether the payment sale request was successful.

**Type**
ID

**Description**
The ID of the order summary record associated with the list of exchanges.

## Prompt Template Actions

Creates a response based on the large language model (LLM) response for the specified prompt template and inputs.

This object is available in API version 60.0 and later.

This action is available only if you enable Prompt Builder and the user who runs the flow has the Prompt Template User permission.

The API name for each action is prefixed with `generatePromptResponse` .

Supported REST HTTP Methods

**URI**
Get a list of available Prompt Template actions:

```
  /services/data/vXX.X/actions/custom/generatePromptResponse

```

Get information about a specific Prompt Template action:

```
  /services/data/vXX.X/actions/custom/generatePromptResponse/ template_API_name

```

**Formats**
JSON, XML

**HTTP Methods**
GET, HEAD, POST

**Authentication**

```
  Authorization: Bearer token

```

92

## Action Objects Quick Actions

Inputs

**Input** **Details**

```
citation

promptResponse

```

**Type**

```
  Picklist

```

**Description**
Specifies how citations are returned:

**•** `post_generation` : Return citations after generation

**•** `off` : Don’t return citations

**Type**
string

**Description**
The prompt response generated by the action based on the specified prompt template and
input.

Additional input values vary according to the input variables specified for the prompt template.

Outputs

**Output** **Details**

```
citation

promptResponse

## Quick Actions

```

**Type**

```
  AiCopilot.GenAiCitationOutput

```

**Description**
Information about the citations associated with this response.

**Type**
string

**Description**
The prompt response generated by the action based on the specified prompt template and
input.

Use a quick action to create a task or a case. Invoke existing quick actions, both global and object-specific, to create records, update
records, or log calls.

[For more information about creating global quick actions, see Create Global Quick Actions, and for more information on object-specific](https://help.salesforce.com/HTViewHelpDoc?id=creating_global_actions.htm&language=en_US)
[quick actions, see Create Object-Specific Quick Actions, in Salesforce Help.](https://help.salesforce.com/HTViewHelpDoc?id=creating_object_specific_actions.htm&language=en_US)

This object is available in API version 32.0 and later.

93

## Action Objects Refresh Metric Actions

Supported REST HTTP Methods

**URI**
Get a list of quick actions:

```
    /services/data/v XX.X /actions/custom/quickAction

```

Get a specific quick action:

```
    /services/data/v XX.X /actions/custom/quickAction/ quick_action_name

```

**Formats**
JSON, XML

**HTTP Methods**
GET, HEAD, POST

**Authentication**

```
    Authorization: Bearer token

```

**Notes**
The only type of quick actions that can be invoked are create, update, and logACall.

Inputs

All quick actions have the `contextId` input parameter. It’s a reference to the related record for the quick action. Other inputs vary
according to the layout of the quick action. To determine inputs for a specific quick action, use the describe feature. For example, perform
a GET with `/services/data/vXX.X/actions/custom/quickAction/Task/deferTask` to see the inputs for the
quick action `deferTask` .

## Refresh Metric Actions

Update a metric’s Current Value field if it’s linked to a summary field in a Salesforce report. The refresh runs as the metric owner.

This object is available in API version 34.0 and later.

Supported REST HTTP Methods

**URI**
Get a list of metric refresh actions:

```
    /services/data/v XX.X /actions/standard/metricRefresh

```

**Formats**
JSON, XML

**HTTP Methods**
GET, HEAD, POST

**Authentication**

```
    Authorization: Bearer token

```

94

## Action Objects Sales Engagement Actions

Inputs

**Input** **Details**

```
metricId

```

Outputs

**Type**
string

**Description**
Required. The metric linked to a Salesforce report.

**Output** **Details**

```
resultingMessage

```

**Type**
string

**Description**
The message that indicates the results of the metric refresh.

## Sales Engagement Actions

Manage your Sales Engagement cadences using invocable actions.

Sales Engagement must be set up in your org. The user must have permissions to use cadences.

Supported REST HTTP Methods

**URIs**

Assign Target To Cadence:

```
  /services/data/v XX.X /actions/standard/assignTargetToSalesCadence

```

Remove Target From Cadence:

```
  /services/data/v XX.X /actions/standard/removeTargetFromSalesCadence

```

Pause Cadence Tracker:

```
  /services/data/v XX.X /actions/standard/pauseSalesCadenceTracker

```

Resume Cadence Tracker:

```
  /services/data/v XX.X /actions/standard/resumeSalesCadenceTracker

```

Change Cadence Target Assignee:

```
  /services/data/v XX.X /actions/standard/changeSalesCadenceTargetAssignee

```

Modify Cadence Tracker Attributes:

```
  /services/data/v XX.X /actions/standard/modifyCadenceTrackerAttributes

```

Send Cadence Event:

95

Action Objects Sales Engagement Actions

```
    /services/data/v XX.X /actions/standard/sendSalesCadenceEvent

```

Select Template For Cadence Step Tracker:

```
    /services/data/v XX.X /actions/standard/selectTemplateForSalesCadenceStepTracker

```

**Formats**
JSON, XML

**HTTP Methods**
GET, HEAD, POST

**Authentication**

```
    Authorization: Bearer token

```

**Other Information**

Error Response Types on page 104

Assign Target to Cadence

Available in API version 45.0.

URI: `/services/data/v` _**`XX.X`**_ `/actions/standard/assignTargetToSalesCadence`

**Table 11: Inputs**

**Input** **Details**

```
salesCadenceNameOrId

startStepNameOrId

targetId

userId

relatedToId

```

**Type**
string

**Description**
Required. The name or ID of the cadence.

**Type**
string

**Description**
The name or ID of the cadence step where the target starts in the cadence.

**Type**
ID

**Description**
Required. The ID of the contact, a lead, or person account to add to the cadence.

**Type**
ID

**Description**
The ID of the user designated as the target assignee. The target assignee is the sales rep who
performs the cadence steps for the target.

**Type**
ID

96

Action Objects Sales Engagement Actions

**Input** **Details**

**Description**
The ID of the target’s related opportunity or invoice. This field is only available when Relate
Opportunities to Cadences or Use Cadences for Collections is turned on in Sales Engagement
Setup.

**Sample Input**

The following code sample adds a target to a cadence:

```
     {

      "inputs" : [ {

       "salesCadenceNameOrId" : "77Cxx0000004CXEEA2",

       "targetId" : "00Qxx000002TRI2EAO"

       }]

     }

```

Remove Target from Cadence

Available in API version 45.0.

URI: `/services/data/v` _**`XX.X`**_ `/actions/standard/removeTargetFromSalesCadence`

**Table 12: Inputs**

**Input** **Details**

```
targetId

actionCadenceTrackerId

completionReasonCode

completionDisposition

```

**Type**
ID

**Description**
Required if `actionCadenceTrackerId` is null. The ID of the contact, a lead, or person
account to remove from the cadence.

**Type**
ID

**Description**
Required if `targetId` is null. The ID of the action cadence tracker to remove from the cadence.

**Type**
string

**Description**
Required. The completion reason code indicates how the target competed the cadence. Valid
value is:

**•** ManuallyRemoved

**Type**
string

97

Action Objects Sales Engagement Actions

**Input** **Details**

**Description**
The disposition of the completed cadence tracker. Valid values are:

**•** Success

**•** Customer Engaged

**•** Customer Connected

**•** Contact Later

**•** No Response

**•** Not Interested

**•** Disqualified

**•** Bad Data

**•** Duplicate

```
relatedToId

relatedToAttributionType

shouldApplyUserContext

```

**Sample Input**

**Type**
ID

**Description**
The ID of the target’s related opportunity or invoice. This field is only available when Relate
Opportunities to Cadences or Use Cadences for Collections is turned on in Sales Engagement
Setup.

**Type**
string

**Description**
The attribution type of the target’s related opportunity or invoice. This field is only available when
Relate Opportunities to Cadences or Use Cadences for Collections is turned on in Sales
Engagement Setup. Valid values are:

**•** Activation (Valid for both opportunities and invoices.)

**•** Maturation (Valid for opportunities.)

**•** Collected (Valid for invoices.)

**Type**
boolean

**Description**
Indicates whether to remove only action cadence trackers owned by the running user ( `true` )
or not ( `false` ).

The following code sample removes a target from a cadence:

```
{

  "inputs" : [ {

   "completionReasonCode" : "ManuallyRemoved",

```

98

Action Objects Sales Engagement Actions

```
       "targetId" : "00Qxx000002TRI2EAO"

       }]

     }

```

Pause Cadence Tracker

Pause a target in its cadence. Available in API version 50.0.

URI: `/services/data/v` _**`XX.X`**_ `/actions/standard/pauseSalesCadenceTracker`

**Table 13: Inputs**

**Input** **Details**

```
targetId

resumeTime

```

**Sample Input**

**Type**
ID

**Description**
Required. The ID of the contact, a lead, or person account to pause.

**Type**
String

**Description**
Optional. The scheduled end time for the pause.

The following code sample pauses a target in its cadence:

```
  {

   "inputs" : [ {

    "targetId" : "00Qxx000002TRI2EAO", "resumeTime" : "2021-06-15T05:30:00:521917Z"

    }]

  }

```

Resume Cadence Tracker

Resume a target in its cadence. Available in API version 50.0.

URI: `/services/data/v` _**`XX.X`**_ `/actions/standard/resumeSalesCadenceTracker`

**Table 14: Inputs**

**Input** **Details**

```
targetId

```

**Type**
ID

**Description**
Required. The ID of the contact, a lead, or person account to pause.

99

Action Objects Sales Engagement Actions

**Sample Input**

The following code sample resumes a target in its cadence:

```
     {

      "inputs" : [ {

       "targetId" : "00Qxx000002TRI2EAO"

       }]

     }

```

Change Cadence Target Assignee

Available in API version 50.0.

URI: `/services/data/v` _**`XX.X`**_ `/actions/standard/changeSalesCadenceTargetAssignee`

**Table 15: Inputs**

**Input** **Details**

```
targetId

userId

```

**Sample Input**

**Type**
ID

**Description**
Required. The ID of the contact, a lead, or person account to pause.

**Type**
ID

**Description**
The ID of the user designated as the target assignee. The target assignee is the sales rep who
performs the cadence steps for the target.

The following code changes a target’s assignee:

```
  {

   "inputs" : [ {

    "targetId" : "00Qxx000002TRI2EAO",

    "userId" : "005R0000000eg3zIAA",

    }]

  }

```

Modify Cadence Tracker Attributes

Available in API version 51.0.

URI: `/services/data/v` _**`XX.X`**_ `/actions/standard/modifyCadenceTrackerAttributes`

100

Action Objects Sales Engagement Actions

**Table 16: Inputs**

**Input** **Details**

```
actionCadenceTrackerId

completionDisposition

relatedToId

relatedToAttributionType

```

**Type**
ID

**Description**
Required. The ID of the cadence tracker to modify.

**Type**
string

**Description**
The disposition of the completed cadence tracker. Valid values are:

**•** Success

**•** Customer Engaged

**•** Customer Connected

**•** Contact Later

**•** No Response

**•** Not Interested

**•** Disqualified

**•** Bad Data

**•** Duplicate

**Type**
ID

**Description**
The ID of the target’s related opportunity or invoice. This field is only available when Relate
Opportunities to Cadences or Use Cadences for Collections is turned on in Sales Engagement
Setup.

**Type**
string

**Description**
The attribution type of the target’s related opportunity or invoice. This field is only available when
Relate Opportunities to Cadences or Use Cadences for Collections is turned on in Sales
Engagement Setup. Valid values are:

**•** Activation (Valid for both opportunities and invoices.)

**•** Maturation (Valid for opportunities.)

**•** Collected (Valid for invoices.)

101

Action Objects Sales Engagement Actions

**Sample Input**

The following code modifies a cadence tracker with a Completion Disposition of “Customer Engaged”, a related opportunity, and
an Attribution Type of “Activation”:

```
     {

      "inputs" : [ {

       "actionCadenceTrackerId" : "0qBR00000005CXvMAM",

       "completionDisposition" : "Customer Engaged",

       "relatedToId" : "006R0000003DNpJIAW",

       "relatedToAttributionType" : "Activation"

       }]

     }

```

Send Cadence Event

Available in API version 52.0.

Send an event to a cadence, such as skipping or manually completing a step.

URI: `/services/data/v` _**`XX.X`**_ `/actions/standard/sendSalesCadenceEvent`

**Table 17: Inputs**

**Input** **Details**

```
recordId

eventType

```

**Sample Input**

**Type**
ID

**Description**
Required. The ID of the cadence step tracker to send the event to.

**Type**
string

**Description**
Required. The type of event to send. Valid values are:

**•** Skip

**•** ManualComplete

The following code sends a Manual Complete event to a cadence step tracker:

```
{

  "inputs" : [ {

   "recordId" : "8HFR00000005WyqOAE",

   "eventType" : "Manual Complete"

   }]

}

```

102

Action Objects Sales Engagement Actions

Select Template for Cadence Step Tracker

Retrieve the email template or call script from a cadence step or cadence step variant (if variant testing) to be used while executing a
step for a particular target. Available in API version 53.0.

URI: `/services/data/v` _**`XX.X`**_ `/actions/standard/selectTemplateForSalesCadenceStepTracker`

**Table 18: Inputs**

**Input** **Details**

```
stepTrackerId

```

**Type**
ID

**Description**
Required. The ID of the cadence step tracker.

**Table 19: Outputs**

**Output** **Details**

```
output

error

```

**Sample Input**

**Type**
JSON

**Description**
The email template or call script ID and its related split percentage.

**Type**
string

**Description**
The error message returned when the action fails.

The following code retrieves the email template or call script for two cadence steps:

```
  {"inputs": [ {

       "stepTrackerId" : "8HFR00000006LE8OAM"

    },

    {

       "stepTrackerId" : "8HFR00000006LEDOA2"

    }]

  }

```

**Sample Output**

The following code sample illustrates a response after one success and one failure.

```
  [ {

   "actionName" : "selectTemplateForSalesCadenceStepTracker",

   "errors" : null,

   "isSuccess" : true,

   "outputValues" : {

```

103

## Action Objects Salesforce Omnichannel Inventory Actions

```
       "output" : {

         "SplitPercentage" : 10.0,

         "TemplateId" : "00XR0000000UOtZMAW"

       }

      }

     }, {

      "actionName" : "selectTemplateForSalesCadenceStepTracker",

      "errors" : [ {

       "statusCode" : "UNKNOWN_EXCEPTION",

       "message" : "No template was found.",

       "fields" : [ ]

      } ],

      "isSuccess" : false,

      "outputValues" : {

       "error" : "No template was found."

      }

     } ]

```

Error Response Types

Sales Engagement actions can respond with success or errors.

If any type of error occurs with an action, the `isSuccess` field is `false` .

This example illustrates a success response for the Assign Target To Cadence action.

```
   [ {

         "actionName" : "assignTargetToSalesCadence",

         "isSuccess" : true

         } ]

```

This example illustrates an error caused by sending invalid input values to the Assign Target To Cadence action.

```
   [ {

         "actionName" : "assignTargetToSalesCadence",

         "errors" : [ {

         "statusCode" : "UNKNOWN_EXCEPTION",

         "message" : "The object needs to be a valid cadence entity.",

         "fields" : [ ]

         } ],

         "isSuccess" : false,

         "outputValues" : {

         "error" : "The object needs to be a valid cadence entity."

         }

         } ]

## Salesforce Omnichannel Inventory Actions

```

Manage inventory availability and provide omnichannel commerce experiences in flows with Salesforce Omnichannel Inventory.

[For more information about using Omnichannel Inventory actions in flows, see Salesforce Omnichannel Inventory Flow Core Actions in](https://help.salesforce.com/HTViewHelpDoc?id=flow_ref_elements_oci_actions_list.htm&language=en_US)
Salesforce Help.

These actions are available in API version 51.0 and later.

104

## Action Objects Salesforce Order Management Actions

Your org must have Salesforce Omnichannel Inventory enabled.

Supported REST HTTP Methods

**URI**
Get a specific Omnichannel Inventory action:

```
    /services/data/v XX.X /actions/standard/ oci_action_name

```

**Formats**
JSON, XML

**HTTP Methods**
GET

**Authentication**

```
    Authorization: Bearer token

```

**Notes**
[You can also call the corresponding Connect REST API endpoints or Apex ConnectApi methods. For more information, see Omnichannel](https://developer.salesforce.com/docs/atlas.en-us.258.0.chatterapi.meta/chatterapi/connect_resources_omnichannel_inventory_resources.htm)
[Inventory Resources in the](https://developer.salesforce.com/docs/atlas.en-us.258.0.chatterapi.meta/chatterapi/connect_resources_omnichannel_inventory_resources.htm) _Connect REST API Developer Guide_ [and ConnectApi Namespace in the](https://developer.salesforce.com/docs/atlas.en-us.258.0.apexcode.meta/apexcode/apex_classes_connect_api.htm) _Apex Developer Guide_ .

In flows, Omnichannel Inventory action inputs and outputs use Apex-defined variables that map to input and output classes in the
ConnectApi namespace.

## Salesforce Order Management Actions

Manage, fulfill, and service orders in flows with Salesforce Order Management.

[For more information about using Order Management actions in flows, see Salesforce Order Management Flow Core Actions in Salesforce](https://help.salesforce.com/HTViewHelpDoc?id=flow_ref_elements_om_actions_list.htm&language=en_US)
Help.

These actions are available in API version 48.0 and later.

Your org must have a Salesforce Order Management license.

Supported REST HTTP Methods

**URI**
Get a specific Order Management action:

```
    /services/data/v XX.X /actions/standard/ om_action_name

```

**Formats**
JSON, XML

**HTTP Methods**
GET

**Authentication**

```
    Authorization: Bearer token

```

**Notes**
[You can also call the corresponding Connect REST API endpoints or Apex ConnectApi methods. For more information, see Order](https://developer.salesforce.com/docs/atlas.en-us.258.0.chatterapi.meta/chatterapi/connect_resources_order_management_resources.htm)
[Management Resources in the](https://developer.salesforce.com/docs/atlas.en-us.258.0.chatterapi.meta/chatterapi/connect_resources_order_management_resources.htm) _Connect REST API Developer Guide_ [and ConnectApi Namespace in the](https://developer.salesforce.com/docs/atlas.en-us.258.0.apexcode.meta/apexcode/apex_classes_connect_api.htm) _Apex Developer Guide_ .

105

## Action Objects Send Conversation Messages Actions

In flows, Order Management action inputs and outputs use Apex-defined variables that map to input and output classes in the
ConnectApi namespace.

## Send Conversation Messages Actions

Send a messaging component to users in enhanced WhatsApp, enhanced Apple Messages for Business, enhanced SMS, or Messaging
for In-App when the targeted channel has bandwidth. Each Send Conversation Messages action corresponds to a supported messaging
component.

This object is available in API version 59.0 and later.

On invocation, this action inserts and enqueues a message for handling the request and sending out the messages async. The request
record can be used to track the progress.

Typical use cases include:

**•** Confirmation of a purchase or booking

**•** Shipping or delivery updates

**•** Password reset requests

**•** Account verification messages

**•** Payment reminders

**•** Abandoned cart reminders

Messages are sent immediately as long as the following conditions are met. If these conditions aren’t met, messages can be queued for
sending, resulting in a slight delay.

**•** The invocation of the Send Conversation Messages action includes 5 or fewer messages. If it includes more, the additional messages
are queued.

**•** No more than 200 invocations of the Send Conversation Messages action are in progress. If this limit is reached, additional requests
are queued and sent when the number of in-progress requests falls below 200. For queued requests, the messaging session owner
for automated messages is the Platform Integration User. Otherwise, it’s the user triggering the action.

**•** The conversation platform has capacity available to send the message. Messages in active conversations are always prioritized over
automated outbound messages.

Supported REST HTTP Methods

**URI**

```
    /services/data/v 59.0 /actions/standard/sendConversationMessages

```

**Formats**
JSON, XML

**HTTP Methods**
GET, HEAD, POST

**Authentication**

```
    Authorization: Bearer token

```

106

Action Objects Send Conversation Messages Actions

Inputs

**Input** **Details**

```
allowedSessionStatus

channelConsentType

communicationSubscriptionId

isEnforceMessagingChannelConsent

messageDefinitionName

```

**Type**
string

**Description**
Limits the time when the message can be sent. Valid values are:

**•** `Any` —Send the message whether the messaging user is engaged in a messaging session
with the business or not.

**•** `NonActive` —Send the message unless the messaging user is engaged in a messaging
session with a status of Active. The message is sent after the session’s status changes.

**•** `Closed` —Send the message unless the messaging user is engaged in a messaging session.
The message is sent after the session is closed.

**Type**
string

**Description**
How to apply consent preferences when determining which messaging users receive the message.
Valid values are:

**•** `MessagingEndUser` —Apply messaging users' consent settings for a channel. This is
the most common approach.

**•** `CommunicationSubscription`  - Send the message only to messaging end users
who have opted into a particular subscription. When selected, a
`communicationSubscriptionId` must also be provided. This option is visible only
if you have a unified channel that supports marketing interactions.

**•** `Custom` —Apply custom consent preferences. Used if
`isEnforceMessagingChannelConsent` is set to `false` .

**Type**
string

**Description**
(Available if `channelConsentType` is set to `CommunicationSubscription` ) The
subscription that controls which messaging users the message is sent to. The subscription must
be tied to the channel where the message is sent, and the message is sent only to users who
opted in to the subscription.

**Type**
boolean

**Description**
Indicates whether messaging consent must be verified after messages are queued for sending.

**Type**
string

107

Action Objects Send Conversation Messages Actions

**Input** **Details**

**Description**
The API name of a ConversationMessageDefinition (messaging component) record that's used
to render the messages.

```
messagingDefinitionInputParameters

messagingEndUserIds

requestType

```

Outputs

**Type**
list

**Description**
Optional. A collection of Apex
`richmessaging__MessageDefinitionInputParameter` records that contain
messaging component details to use when rendering messages.

**Type**
list

**Description**
A collection of up to 100 messaging end user record IDs to use as recipients of the messages. To
send more than 100 messages, divide your end user recipients into batches of 100 or fewer and
repeat the action invocation for each batch.

**Type**
string

**Description**
Specifies the type of the request. Valid values are: `SendNotificationMessages` .

**Input** **Details**

```
requestId

messageIdentifiers

```

**Type**
string

**Description**
The ID of the ConvMessageSendActionRequest record created by the request that's used to track
the message progress.

**Type**
list

**Description**
A collection of generated message UUIDs with one entry for each recipient specified in
messagingUserIds.

108

## Action Objects Send Notification Actions

Usage

**Sample Input**

The following sample input attempts to create a ConvMessageSendRequest record using a Messaging Component
( `messageDefinitionName` ), the request for the type of component being sent ( `requestType` ), the consent preferences
( `isEnforceMessagingChannelConsent` ), the consent type ( `channelConsentType` ), when the message can be sent
( `allowedSessionStatus` ), and the message recipients ( `messagingEndUserIds` ). Additionally, the request contains a
list of custom parameters ( `messagingDefinitionInputParameters` ). These parameters are mapped to parameters
configured in the messaging component, which can be optional. Applicable data types for parameters are `textValue`,
`recordIdValue`, `dateValue`, `dateTimeValue`, `numberValue`, and `booleanValue` .

```
     {

      "inputs": [{

         "messageDefinitionName":"Notification",

         "requestType":"SendNotificationMessages",

         "isEnforceMessagingChannelConsent":true,

         "channelConsentType":"MessagingEndUser",

         "allowedSessionStatus":"Any",

         "messagingEndUserIds":"0PARM000000Lc3I,0PARM000000MZ3p",

     "messagingDefinitionInputParameters":[{"name":"custom_parameter_name","textValue":"custom

      parameter value"}]

      }]

     }

```

**Sample Output**

The following sample output illustrates a response after a successful request.

```
     [

      {

       "actionName":"sendConversationMessages",

       "errors":null,

       "isSuccess":true,

       "outputValues":{

     "messageIdentifiers":"c581098c-5db6-4ed8-915f-c9aaa016c671,d8e1990e-5d67-414c-9713-180107d7d1bb",

     "requestId":"1srM000000000p"

       }

      }

     ]

```

[For more information about this action, see Flow Core Actions: Send Conversation Messages and Send Automated Messages in Enhanced](https://help.salesforce.com/s/articleView?id=sf.flow_ref_elements_actions_sendconversationmessages.htm&language=en_US)
[Messaging Channels in Salesforce Help.](https://help.salesforce.com/s/articleView?id=sf.messaging_automated_enhanced.htm&language=en_US)

## Send Notification Actions

Call a notification type to send. Each Send Notification action corresponds to a supported notification type. This object is available in API
version 54.0 and later. Send Notification actions are available only for Slack-enabled custom notification types and certain Slack-enabled
standard notification types.

Note: [To send notifications for Slack, enable Salesforce for Slack Integrations.](https://help.salesforce.com/s/articleView?id=sf.slack_apps_enable.htm&language=en_US)

[To create a custom Slack notification type supported by a Send Notification action, see Create and Send Custom Slack Notifications.](https://help.salesforce.com/s/articleView?id=sf.notif_builder_create_send_slack.htm&language=en_US)

109

Action Objects Send Notification Actions

To trigger Send Notification actions using REST API calls, you need the Send Custom Notifications user permission.

Supported REST HTTP Methods

**URI**
Get a list of available Send Notification actions.

```
    /services/data/v XX.X /actions/custom/sendNotification

```

Get information about a specific Send Notification action:

```
    /services/data/v XX.X /actions/custom/sendNotification/ notification_type_name

```

**Formats**
JSON, XML

**HTTP Methods**
GET, HEAD, POST

**Authentication**

```
    Authorization: Bearer token

```

Inputs

**Input** **Details**

```
recipientIds

recordId

```

**Type**
ID

**Description**
Required. The IDs of the notification recipients or recipient types. Valid recipient or recipient type
values are UserId or CollaborationRoomId values.

**Type**
ID

**Description**

Required. The ID of the record that the notifications are about. The record ID must be associated
with the specific EntityType of the notification type. For example, enter the record ID for an
opportunity when configuring a notification type associated with the Opportunity object.

For custom notification types, you can find the related object by viewing the notification type's
settings from Custom Notifications in Setup. For supported standard notification types, refer to
the Standard Notification Types and Related Objects table.

Standard Notification Types and Related Objects

Use this table to identify which object applies to each standard notification type supported by a Send Notification action. The object
determines the value that you enter for `recordId` .

110

## Action Objects Session-Based Permission Set Actions

**Standard Notification Type** **Related Salesforce Object**

`amount_updated` Opportunity

`close_date_reminder` Opportunity

`close_date_updated` Opportunity

`deal_won` Opportunity

`deals_to_watch` Opportunity

`hc_allergy_intolerance_alert` Allergy Intolerance

`hc_care_determinant_alert` Care Determinant

`hc_care_plan_alert` Case

`hc_care_plan_task_alert` Task

`hc_health_condition_alert` Health Condition

`high_priority_case` Case

`new_child_opportunity` Opportunity

`next_step_reminder` Opportunity

`stage_reminder` Opportunity

`stage_updated` Opportunity

SEE ALSO:

_[Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.258.0.object_reference.meta/object_reference/sforce_api_objects_collaborationroom.htm)_ : CollaborationRoom

_[Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.258.0.object_reference.meta/object_reference/sforce_api_objects_swarm.htm)_ : Swarm

## Session-Based Permission Set Actions

Activate or deactivate a session-based permission set for the current user’s API session.

This object is available in API version 40.0 and later.

This action activates or deactivates the provided permission set for the current user’s API session. The activation or deactivation doesn’t
affect other sessions. The permission set must already be assigned to the current user.

111

## Action Objects Simple Email Actions

Supported REST HTTP Methods

**URI**
Activate session-based permission set:

```
    /services/data/v XX.X /actions/standard/activateSessionPermSet

```

Deactivate session-based permission set:

```
    /services/data/v XX.X /actions/standard/deactivateSessionPermSet

```

**Formats**
JSON, XML

**HTTP Methods**
GET, HEAD, POST

**Authentication**

```
    Authorization: Bearer token

```

Inputs

**Input** **Details**

```
PermSetName

PermSetNamespace

```

Outputs

None.

**Type**
string

**Description**
Required. Specifies the developer name of the permission set.

**Type**
string

**Description**
Optional. Specifies the namespace of the permission set.

## Simple Email Actions

Send an email where you specify the subject, body, and recipients. Available in API version 32.0 and later.

**Email Sending Limits**
If you’re using `logEmailOnSend` or `emailTemplateId`, the daily email-sending limit is based on the single email limit. See
[General Email Limits.](https://help.salesforce.com/s/articleView?id=000381534&type=1&language=en_US)

If you’re not using `logEmailOnSend` or `emailTemplateId`, the daily email-sending limit is based on the daily workflow
[email limit. See Proactive Alert Monitoring: Daily Workflow Email Limit.](https://help.salesforce.com/s/articleView?id=000382442&type=1&language=en_US)

112

Action Objects Simple Email Actions

Supported REST HTTP Methods

**URI**
Get a list of available simple email actions:

```
    /services/data/v XX.X /actions/standard/emailSimple

```

**Formats**
JSON, XML

**HTTP Methods**
GET, HEAD, POST

**Authentication**

```
    Authorization: Bearer token

```

Inputs

**Configure Recipient Details**

113

Action Objects Simple Email Actions

**Configure Sender Details**

**Configure Email Content**

To configure the email content in your email flow, use the following input parameters. You can create your email content or use an
existing email template.

114

Action Objects Simple Email Actions

115

Action Objects Simple Email Actions

116

## Action Objects Submit Exchange Order

Outputs

None.

## Submit Exchange Order

Submits an exchange order based on the specified information.

To access, you need the following permissions.

**•** Salesforce Order Management License or Salesforce B2B Commerce License

This object is available in API version 60.0 and later.

Supported REST HTTP Methods

**URI**

```
  /services/data/v59.0/actions/standard/previewCartToExchangeOrder

```

**Formats**
JSON, XML

**HTTP Methods**
GET, HEAD, POST

**Authentication**
Authorization: Bearer token

117

Action Objects Submit Exchange Order

Inputs

**Input** **Details**

```
exchangeCartId

orderNumber

orderSummaryId

paymentInfoInputs

referenceId

sequenceList

```

**Type**
ID

**Description**
Required. The ID of the cart record containing the items in the exchange order.

**Type**
ID

**Description**
Optional. Order number for the created exchange order summary.

**Type**
ID

**Description**
Required. The ID of the order summary record associated with the list of exchanges.

**Type**
Collection

**Description**
Optional. A collection of Apex ConnectApi.PaymentInfoInputRepresentation records, each
containing payment details when the exchange order amount is greater than the original order
amount.

**Type**
ID

**Description**
Required. The ID of the record that's related to the specified order summary. Only IDs from a
return order record are supported.

**Type**
Collection

**Description**
Optional. A collection of Apex ConnectApi.SequenceOrderPaymentSummaryInputRepresentation
records to reserve a balance from. Each record contains an order summary payment ID and an
amount.

118

## Action Objects Submit for Approval Actions

Outputs

**Output** **Details**

```
changeBalances

errors

exchangeOrderSummaryId

isSuccess

orderSummaryID

```

**Type**
string

**Description**
A string that contains the calculated amounts resulting from the exchange order.

**Type**
string

**Description**
Following a `400` error response, the error objects show information about the error that occurred.
Contains a status code, message, and list of fields.

**Type**
ID

**Description**
The ID of the order summary record associated with the list of exchanges.

**Type**
boolean

**Description**
The ID of the order summary record created for the exchanges.

**Type**
ID

**Description**
The ID of the order summary record associated with the list of exchanges.

## Submit for Approval Actions

Submit a Salesforce record for approval if an approval process is defined for the current entity.

[For more information about creating submit for approval actions, see Creating Approval Actions, and to learn more about approval](https://help.salesforce.com/HTViewHelpDoc?id=approvals_creating_approval_actions.htm&language=en_US)
[processes, see Approval Process Overview, in Salesforce Help.](https://help.salesforce.com/apex/HTViewHelpDoc?id=what_are_approvals.htm&language=en_US)

This object is available in API version 32.0 and later.

Supported REST HTTP Methods

**URI**
Get a list of actions:

```
  /services/data/v XX.X /actions/standard/submit

```

119

Action Objects Submit for Approval Actions

**Formats**
JSON, XML

**HTTP Methods**
GET, HEAD, POST

**Authentication**

```
    Authorization: Bearer token

```

Inputs

**Input** **Details**

```
comment

nextApproverIds

objectId

processDefinitionNameOrId

skipEntryCriteria

submitterId

```

**Type**
string

**Description**
Optional. Comments that accompany the Approval submission.

**Type**
reference

**Description**
Optional. An array of one ID of the next approver, which can be a user or a group. This input is
optional because some approval processes have the next approver specified in the approval
process definition. You can’t specify more than 2,000 approvers.

**Type**
reference

**Description**
Required. The ID of the record being submitted for approval.

**Type**
string

**Description**
Optional. The ID or name of the approval process to run against the record. If none is specified,
the first approval process whose entry criteria the record satisfies is used. Names can’t be longer
than 120 characters.

**Type**
boolean

**Description**
Optional. A Boolean value controlling whether the entry criteria for the specified approval process
must be evaluated for the record ( `true` ) or not ( `false` ). If set to true, also specify
`processDefinitionNameOrId` .

**Type**
string

120

Action Objects Submit for Approval Actions

**Input** **Details**

**Description**
Optional. The ID of the user submitting the record for approval. If none is specified, the submitter
is the current user.

Outputs

**Output** **Details**

```
actorIds

entityId

instanceId

instanceStatus

newWorkItemIds

```

**Type**
reference

**Description**
An array of the IDs of the next approvers.

**Type**
reference

**Description**
The ID of the record submitted for approval.

**Type**
reference

**Description**
The ID of the approval process instance.

**Type**
string

**Description**
The status of the approval. The valid values are

**•** Approved

**•** Pending

**•** Rejected

**•** Removed

**Type**
reference

**Description**
An array of the IDs of the work items created for the next step in this approval process.

121

## Action Objects Survey Invitation Actions Survey Invitation Actions

Send email survey invitations to leads, contacts, and users in your org based on an action. Also, send customized notifications to users
about important events or updates to the records that they’re working on.

### Dynamic Send Survey Invitation Actions

Send customized notifications to users about important events or updates to the records that they’re working on. For example, notify
account owners when a case is created.

This action is available in API version 51.0 and later.

Special Access Rules

To access the Dynamic Send Survey Invitation action, you must have the Feedback Management Survey Response Pack and the Salesforce
org enabled with Surveys.

Supported REST HTTP Methods

**URI**

Get the list of invocable actions for each available survey.

```
    /services/data/v 51.0 /actions/custom/dynamicSendSurveyInvitation

```

Send survey invitation by email by using the invocable action.

```
    /services/data/v 51.0 /actions/custom/dynamicSendSurveyInvitation/ {surveyName}

```

**Formats**
JSON, XML

**HTTP Methods**
GET, HEAD, POST

**Authentication**

```
    Authorization: Bearer token

```

Inputs

**Input** **Details**

```
anonymousResponse

autoExpiryDays

```

**Type**
boolean

**Description**
Indicates whether the participant’s name is recorded in the response record ( `true` ) or not
( `false` ).

**Type**
integer

122

Action Objects Dynamic Send Survey Invitation Actions

**Input** **Details**

**Description**
Number of days remaining for the survey invitation to expire.

```
emailTemplateName

isUnauthenticatedResponse

personalInvitation

recipient

recipientType

surveyQuestionName

surveySubjectEntity

```

Outputs

None.

**Type**
string

**Description**
Developer name of the template that contains either the question or the survey link.

**Type**
boolean

**Description**
Indicates whether the participant is required to authenticate before starting the survey ( `true` )
or not ( `false` ).

**Type**
boolean

**Description**
Indicates whether the invitation is specific to the recipient ( `true` ) or not ( `false` ).

**Type**
reference

**Description**
Required. Salesforce ID of the record that the survey invitation is sent to.

**Type**
string

**Description**
Type of the survey recipient.

**Type**
string

**Description**
Developer name of the question that’s sent by using the invitation.

**Type**
reference

**Description**
ID of the record that associates the invitation record with another record.

123

Action Objects Dynamic Send Survey Invitation Actions

Example

**GET**

This example shows how to get information about the Dynamic Send Survey Invitation action type.

```
     curl --include --request GET \

     --header "Authorization: Authorization: Bearer 00DR...xyz" \

     --header "Content-Type: application/json" \

     "https://instance.salesforce.com/services/data/v51.0/actions/custom/dynamicSendSurveyInvitation"

```

Here’s a response that returns the list of invocable actions for each survey.

```
     {

      "actions" : [ {

       "label" : "flowsend",

       "name" : "flowsend",

       "type" : "SEND_SURVEY_DYNAMIC_INVOCABLE_ACTION",

       "url" : "/services/data/v51.0/actions/custom/dynamicSendSurveyInvitation/flowsend"

      }, {

       "label" : "survey2",

       "name" : "survey2",

       "type" : "SEND_SURVEY_DYNAMIC_INVOCABLE_ACTION",

       "url" : "/services/data/v51.0/actions/custom/dynamicSendSurveyInvitation/survey2"

      }, {

       "label" : "survey",

       "name" : "survey",

       "type" : "SEND_SURVEY_DYNAMIC_INVOCABLE_ACTION",

       "url" : "/services/data/v51.0/actions/custom/dynamicSendSurveyInvitation/survey"

      } ]

     }

```

**POST**

Here’s a request for the Dynamic Send Survey Invitation action.

```
     {

       "inputs":[{

         "recipient" : "003xx000004WpemAAC",

         “isUnauthenticatedResponse” : false,

         "autoExpiryDays" : 6

       }]

     }

```

Here’s a response for the Dynamic Send Survey Invitation action.

```
     [

       {

         "actionName" : "survey",

         "errors" : null,

         "isSuccess" : true,

         "outputValues" : null

```

124

### Action Objects Send Survey Invitation Actions

```
       }

     ]

```

SEE ALSO:

_Salesforce Help_ [: Send Survey Invitations Using Flows](https://help.salesforce.com/s/articleView?id=sf.concept_send_invitation_flow_builder.htm&language=en_US)

### Send Survey Invitation Actions

Send email survey invitations to leads, contacts, and users in your org based on an action. For example, send a survey invitation when
a customer support case closes.

This action is available in API version 47.0 and later.

Special Access Rules

To access the Send Survey Invitation action, you must have the Feedback Management Survey Response Pack and the Salesforce org
enabled with Surveys.

Supported REST HTTP Methods

**URI**

```
    /services/data/v 47.0 /actions/standard/sendSurveyInvitation

```

**Formats**
JSON, XML

**HTTP Methods**
GET, HEAD, POST

**Authentication**

```
    Authorization: Bearer token

```

Inputs

**Input** **Details**

```
anonymousResponse

autoExpiryDays

```

**Type**
boolean

**Description**
Indicates whether the participant’s name is recorded in the response record ( `true` ) or not
( `false` ).

**Type**
integer

**Description**
Number of days remaining for the survey invitation to expire.

125

Action Objects Send Survey Invitation Actions

**Input** **Details**

```
emailTemplateName

isUnauthenticatedResponse

personalInvitation

recipient

surveyName

surveyQuestionName

surveySubjectEntity

```

Outputs

None.

**Type**
string

**Description**
Developer name of the template that contains either the question or the survey link.

**Type**
boolean

**Description**
Indicates whether the participant is required to authenticate before starting the survey ( `true` )
or not ( `false` ).

**Type**
boolean

**Description**
Indicates whether the invitation is specific to the recipient ( `true` ) or not ( `false` ).

**Type**
reference

**Description**
Required. Salesforce ID of the record that the survey invitation is sent to. The record can be a
user (internal invitation) or a contact or a lead (external invitation via community).

**Type**
string

**Description**
Required. Developer name of the survey that the invitation is sent for.

**Type**
string

**Description**
Developer name of the question that’s sent using the invitation.

**Type**
reference

**Description**
ID of the record that associates the invitation record with another record.

126

## Action Objects Work Plan and Work Step Actions

Example

**GET**

This example shows how to get information about the Send Survey Invitation action type.

```
     curl --include --request GET \

     --header "Authorization: Authorization: Bearer 00DR...xyz" \

     --header "Content-Type: application/json" \

     "https://instance.salesforce.com/services/data/v47.0/actions/standard/sendSurveyInvitation"

```

**POST**

Here’s a request for the send survey invitation action.

```
     {

       "inputs":[{

         "surveyName" : "FlowActionSend",

         "recipient" : "003RO0000037IRvYAM",

         "autoExpiryDays" : 6

       }]

     }

```

Here’s a response for the send survey invitation action.

```
     [

       {

         "actionName" : "sendSurveyInvitation",

         "errors" : null,

         "isSuccess" : true,

         "outputValues" : null

       }

     ]

```

SEE ALSO:

_Salesforce Help_ [: Send Survey Invitations Using Process Builder](https://help.salesforce.com/s/articleView?id=sf.process_action_send_survey_invite.htm&language=en_US)

## Work Plan and Work Step Actions

Manage work plans and work steps using actions.

[For more information about Field Service, see the Field Service Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.258.0.field_service_dev.meta/field_service_dev/)

These actions are available in API version 52.0 and later. They require Field Service to be enabled.

**Add Work Plans Limits**
You can generate work plans linked to work orders via the `addWorkPlans` flow, but, by default, users can only generate 100
work plans per work order.

Supported REST HTTP Methods

**URIs**

Add work plans: `/services/data/v` _**`XX.X`**_ `/actions/standard/addWorkPlans`

Add work steps: `/services/data/v` _**`XX.X`**_ `/actions/standard/addWorkSteps`

127

Action Objects Work Plan and Work Step Actions

Generate work plans: `/services/data/v` _**`XX.X`**_ `/actions/standard/generateWorkPlans`

Delete work plans: `/services/data/v` _**`XX.X`**_ `/actions/standard/deleteWorkPlans`

**Formats**
JSON, XML

**HTTP Methods**
GET, HEAD, POST

**Authentication**

```
    Authorization: Bearer token

```

Add Work Plans

URI: `/services/data/v` _**`XX.X`**_ `/actions/standard/addWorkPlans`

This action creates work plan records from the work plan library.

**Table 20: Inputs**

**Input** **Details**

```
recordId

workPlanTemplateIdList

```

**Type**
string

**Description**
Required. The ID of the work order or work order line item to add the work plans to.

**Type**
array of strings

**Description**
Required. The IDs of the work plan templates used to instantiate the work plans.

**Table 21: Outputs**

**Output** **Details**

```
recordId

workPlanIdList

```

**Type**
string

**Description**
The ID of the work order or work order line item.

**Type**
array of strings

**Description**
The list of work plan IDs.

128

Action Objects Work Plan and Work Step Actions

**Sample Input**

The following code sample adds work plans:

```
     {

       "inputs" : [ {

          "recordId" : "0WOxx00000007j3",

          "workPlanTemplateIdList" : ["7Iyxx0000004LSS", "7Iyxx0000004LTT"]

       }]

     }

```

**Sample Output**

The following code sample illustrates a response after a successful request.

```
     [ {

       "actionName" : "addWorkPlans",

       "errors" : null,

       "isSuccess" : true,

       "outputValues" : {

          "recordId" : "0WOxx00000007j3",

          "workPlanIdList" : ["0gqxx0000000Adh", "0gqxx0000000Adi"]

       }

     } ]

```

Add Work Steps

URI: `/services/data/v` _**`XX.X`**_ `/actions/standard/addWorkSteps`

This action creates work step records from the work plan library.

**Table 22: Inputs**

**Input** **Details**

```
recordId

workStepTemplateIdList

```

**Type**
string

**Description**
Required. The ID of the work plan to add the work steps to.

**Type**
array of strings

**Description**
Required. The IDs of the work step templates used to instantiate the work steps.

**Table 23: Outputs**

**Output** **Details**

```
recordId

```

**Type**
string

129

Action Objects Work Plan and Work Step Actions

**Output** **Details**

**Description**
The ID of the work order or work order line item.

```
workStepIdList

```

**Sample Input**

**Type**
array of strings

**Description**
The list of work step IDs.

The following code sample adds work steps:

```
  {

    "inputs" : [ {

       "recordId" : "0gqRM0000004DxoYAE",

       "workStepTemplateIdList" : ["4L0xx0000004FJoCAM", "4L0xx0000004FJoNAC"]

    }]

  }

```

**Sample Output**

The following code sample illustrates a response after a successful request.

```
  [ {

    "actionName" : "addWorkSteps",

    "errors" : null,

    "isSuccess" : true,

    "outputValues" : {

      "recordId" : "0gqRM0000004DxoYAE",

      "workstepIdList" : ["0hFxx00000007uLEAQ", "0hFxx00000007uRAUW"]

    }

  } ]

```

Generate Work Plans

URI: `/services/data/v` _**`XX.X`**_ `/actions/standard/generateWorkPlans`

This action generates work plans based off rules defined in the work plan library.

**Table 24: Inputs**

**Input** **Details**

```
recordId

```

**Type**
string

**Description**
Required. The ID of the work order or work order line item to generate work plans for.

130

Action Objects Work Plan and Work Step Actions

**Table 25: Outputs**

**Output** **Details**

```
recordId

workPlanIdList

```

**Sample Input**

**Type**
string

**Description**
The ID of the work order or work order line item.

**Type**
array of strings

**Description**
The list of work plan IDs.

The following code sample generates a work plan:

```
  {

    "inputs" : [ {

       "recordId" : "0WOxx00000007j3"

    }]

  }

```

**Sample Output**

The following code sample illustrates a response after a successful request.

```
  [ {

    "actionName" : "generateWorkPlans",

    "errors" : null,

    "isSuccess" : true,

    "outputValues" : {

       "recordId" : "0WOxx00000007j3",

       "workPlanIdList" : ["0gqxx0000000Adh", "0gqxx0000000Adi"]

    }

  } ]

```

Delete Work Plans

URI: `/services/data/v` _**`XX.X`**_ `/actions/standard/deleteWorkPlans`

This action deletes all the work plans (and its child work steps) associated with a WorkOrder or WorkOrderLineItem.

**Table 26: Inputs**

**Input** **Details**

```
recordId

```

**Type**
string

**Description**
Required. The ID of the work order or work order line item.

131

Action Objects Work Plan and Work Step Actions

**Table 27: Outputs**

**Output** **Details**

```
recordId

workPlanIdList

```

**Sample Input**

**Type**
string

**Description**
The ID of the work order or work order line item.

**Type**
array of strings

**Description**
The ID list for the work plans that were deleted.

The following code deletes a work plan:

```
  {

    "inputs" : [ {

       "recordId" : "OWOxxxxxxxxxxxx"

    }]

  }

```

**Sample Output**

The following code sample illustrates a response after a successful request.

```
  [ {

    "actionName" : "deleteWorkPlans",

    "errors" : null,

    "isSuccess" : true,

    "outputValues" : {

       "recordId" : "0WORM000000621X",

       "workPlanIdList" : [ "0gqRM0000004CRS" ]

     }

  } ]

```

132
