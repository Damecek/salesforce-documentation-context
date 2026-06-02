# Second generation managed packaging developer guide

> Source: https://resources.docs.salesforce.com/latest/latest/en-us/sfdc/pdf/pkg2_dev.pdf
> Fetched: 2026-06-02T08:15:32Z
Second-Generation Managed
Packaging Developer Guide

Version 67.0, Summer ’26

Last updated: May 26, 2026

© Copyright 2000–2026 Salesforce, Inc. All rights reserved. Salesforce is a registered trademark of Salesforce, Inc., as are other
names and marks. Other marks appearing herein may be trademarks of their respective owners.

CONTENTS

**Chapter 1:** Second-Generation Managed Packages **. . . . . . . . . . . . . . . . . . . . . . . . . . . 1**

What’s a Second-Generation Managed Package? **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3**

Why Switch to Second-Generation Managed Packaging? **. . . . . . . . . . . . . . . . . . . . . . . 3**
Comparison of First- and Second-Generation Managed Packages **. . . . . . . . . . . . . . . . . 5**
Set Up Your Development Environment **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6**

Enable Dev Hub and Second-Generation Managed Packaging **. . . . . . . . . . . . . . . . . . . 6**
Limited Access License for Package Developers **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7**
Add a Limited Access User to Your Dev Hub Org **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8**
Assign Second-Generation Managed Packaging User Permissions **. . . . . . . . . . . . . . . . 8**
Before You Create Second-Generation Managed Packages **. . . . . . . . . . . . . . . . . . . . . . . . . 9**

Know Your Orgs for Second-Generation Managed Packages **. . . . . . . . . . . . . . . . . . . . 9**
Link a Namespace to a Dev Hub Org **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10**
Namespaces for Second-Generation Managed Packages **. . . . . . . . . . . . . . . . . . . . . . 11**
Create and Register Your Namespace for Second-Generation Managed Packages **. . . . . 11**
Key Concepts in Second-Generation Managed Packaging **. . . . . . . . . . . . . . . . . . . . . . 12**
How Manageability Rules and Ancestry Impact Upgrades for Second-Generation Managed
Packages **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13**
Which Package Types Can Your Package Depend On? **. . . . . . . . . . . . . . . . . . . . . . . . 14**
Scratch Orgs and Package Development **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15**

How Scratch Orgs Fit in the Package Development Workflow **. . . . . . . . . . . . . . . . . . . . 16**
Scratch Org Definition Files vs Org Shape in Package Development **. . . . . . . . . . . . . . . . 17**
When to Use Scratch Org Snapshots in Package Development **. . . . . . . . . . . . . . . . . . . 18**
Create a Package Version Based on a Scratch Org Snapshot **. . . . . . . . . . . . . . . . . . . . 19**
Get Access to Scratch Orgs That Have Agentforce **. . . . . . . . . . . . . . . . . . . . . . . . . . . 20**
Scratch Org Allocations for Salesforce Partners **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22**
Manage Scratch Orgs from the Dev Hub Org **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22**
Supported Scratch Org Editions for Partners **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23**
Workflow for Second-Generation Managed Packages **. . . . . . . . . . . . . . . . . . . . . . . . . . . . 23**
Components Available in Second-Generation Managed Packages **. . . . . . . . . . . . . . . . . . . 25**

Account Plan Objective Measure Calculation Definition **. . . . . . . . . . . . . . . . . . . . . . . . 41**
Account Relationship Share Rule **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42**
Action Link Group Template **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43**
Action Plan Template **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44**
Actionable List Definition **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45**
Actionable List Key Performance Indicator Definition **. . . . . . . . . . . . . . . . . . . . . . . . . . 46**
Activation Platform **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47**
AffinityScoreDefinition **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49**
Agent Action **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50**
Agent Topic **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51**

**Contents**

AI Application **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52**
AI Application Config **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53**
AIUsecaseDefinition **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55**
Analytics **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56**
Analytics Visualization **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56**
Analytics Workspace **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57**
Apex Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58**
Apex Sharing Reason **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60**
Apex Trigger **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61**
App Framework Template Bundle **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62**
Application Subtype Definition **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63**
AssessmentConfiguration **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64**
AssessmentQuestion **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64**
AssessmentQuestionSet **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65**
Aura Component **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66**
Batch Calc Job Definition **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67**
Batch Process Job Definition **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68**
Benefit Action **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69**
Bot Template **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70**
Branding Set **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72**
Briefcase Definition **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73**
Building Energy Intensity Record Type Configuration **. . . . . . . . . . . . . . . . . . . . . . . . . . 74**
Business Process **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75**
Business Process Group **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76**
Business Process Type Definition **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77**
Care Benefit Verify Settings **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77**
Care Limit Type **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79**
Care Request Configuration **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80**
Care System Field Mapping **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81**
Channel Layout **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82**
Chatter Extension **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83**
Claim Financial Settings **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83**
CommunicationChannelType **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84**
Community Template Definition **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85**
Community Theme Definition **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86**
Compact Layout **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87**
Conditional Formatting Ruleset **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88**
Connected App **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89**
Context Definition **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91**
Contract Type **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92**
Conversation Channel Definition **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93**
Conversation Vendor Info **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94**
CORS Allowlist **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95**
CSP Trusted Site **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96**

**Contents**

Custom Application **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98**
Custom Button or Link **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99**
Custom Console Components **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100**
Custom Field on Standard or Custom Object **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101**
Custom Field on Custom Metadata Type **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102**
Custom Field Display **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103**
Custom Help Menu Section **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104**
Custom Index **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104**
Custom Label **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105**
Custom Metadata Type Records **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106**
Custom Metadata Type **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107**
Custom Notification Type **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107**
Custom Object **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109**
Custom Object Translation **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110**
Custom Permission **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111**
Custom Tab **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112**
Dashboard **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114**
DataCalcInsightTemplate **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115**
Data Connector Ingest API **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116**
Data Connector S3 **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117**
Data Kit Object Dependency **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118**
Data Kit Object Template **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119**
DataObjectBuildOrgTemplate **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120**
Data Package Kit Definition **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121**
Data Package Kit Object **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123**
Data Source **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124**
Data Source Bundle Definition **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125**
Data Source Object **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126**
Data Src Data Model Field Map **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127**
Data Stream Definition **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128**
Data Stream Template **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130**
DataWeaveResource **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131**
Decision Matrix Definition **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132**
Decision Matrix Definition Version **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133**
Decision Table **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134**
Decision Table Dataset Link **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135**
Digital Experience **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136**
Digital Experience Bundle **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137**
Decision Table **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139**
Disclosure Definition **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140**
Disclosure Definition Version **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141**
Disclosure Type **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142**
Discovery AI Model **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143**
Discovery Goal **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 144**

**Contents**

Discovery Story **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145**
Document **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 146**
Document Generation Setting **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 146**
Eclair GeoData **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147**
Email Template (Classic) **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 148**
Email Template (Lightning) **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 149**
Embedded Service Config **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 150**
Embedded Service Menu Settings **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 151**
Enablement Measure Definition **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 152**
Enablement Program Definition **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 153**
Enablement Program Task Subcategory **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 155**
Entitlement Template **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 156**
ESignature Config **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157**
ESignature Envelope Config **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158**
Event Relay **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159**
Explainability Action Definition **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 160**
Explainability Action Version **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 161**
Explainability Message Template **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 161**
Expression Set Definition **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 162**
Expression Set Definition Version **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 164**
Expression Set Object Alias **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 165**
Expression Set Message Token **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 166**
External Auth Identity Provider **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 167**
External Client App Canvas Settings **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 168**
External Client App Header **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 170**
External Client App Notification Settings **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 171**
External Client App OAuth Settings **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 172**
External Client App Push Settings **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 173**
External Credential **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 174**
External Data Connector **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 176**
External Data Source **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 177**
External Data Transport Field Template **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 178**
External Data Transport Field **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 179**
External Data Transport Object Template **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 181**
External Data Transport Object **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 182**
External Document Storage Configuration **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 183**
External Services **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 184**
Feature Parameter Boolean **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 185**
Feature Parameter Date **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 186**
Feature Parameter Integer **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 188**
FieldMappingConfig **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 189**
Field Set **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 192**
Field Source Target Relationship **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 193**
Flow **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 194**

**Contents**

Flow Category **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 196**
Flow Definition **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 197**
Flow Test **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 198**
Folder **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 199**
Fuel Type **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 201**
Fuel Type Sustainability Unit of Measure **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 202**
Fundraising Config **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 203**
Gateway Provider Payment Method Type **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 204**
Gen Ai Planner Bundle **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 205**
Generative AI Prompt Template **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 206**
Global Picklist **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 207**
Home Page Component **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 208**
Home Page Layout **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 209**
Identity Verification Proc Def **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 210**
Inbound Network Connection **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 211**
IndustriesEinsteinFeatureSettings **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 212**
IntegrationProviderDef **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 213**
Invocable Action Extension **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 214**
LearningAchievementConfig **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 215**
Learning Item Type **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 216**
Letterhead **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 217**
Life Science Config Category **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 218**
Life Science Config Record **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 219**
Lightning Bolt **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 220**
Lightning Message Channel **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 221**
Lightning Page **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 222**
Lightning Type **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 223**
Lightning Web Component **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 224**
List View **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 225**
Live Chat Sensitive Data Rule **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 227**
Loyalty Program Setup **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 228**
Managed Content Type **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 229**
Marketing App Extension **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 230**
Marketing App Extension Activity **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 231**
Market Segment Definition **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 232**
MktCalculatedInsightsObjectDef **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 233**
MktDataConnection **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 234**
MktDataTranObject **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 236**
Named Credential **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 237**
Object Source Target Map **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 239**
Object Integration Provider Definition Mapping **. . . . . . . . . . . . . . . . . . . . . . . . . . . . 240**
OcrSampleDocument **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 241**
OcrTemplate **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 242**
Outbound Network Connection **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 243**

**Contents**

Page Layout **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 244**
Path Assistant **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 246**
Payment Gateway Provider **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 246**
Permission Set **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 247**
Permission Set Groups **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 248**
Platform Cache **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 249**
Platform Event Channel **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 250**
Platform Event Channel Member **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 251**
Platform Event Subscriber Configuration **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 252**
Pricing Action Parameters **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 253**
Pricing Recipe **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 254**
Procedure Output Resolution **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 255**
Process **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 256**
Process Flow Migration **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 256**
Product Attribute Set **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 257**
Product Specification Type **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 258**
Product Specification Record Type **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 259**
Prompts (In-App Guidance) **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 260**
Quick Action **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 260**
Recommendation Strategy **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 261**
Record Action Deployment **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 262**
Record Alert Data Source Expression Set Definition **. . . . . . . . . . . . . . . . . . . . . . . . . . 263**
Record Type **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 264**
RedirectWhitelistUrl **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 266**
Referenced Dashboard **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 267**
Registered External Service **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 268**
RelationshipGraphDefinition **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 269**
Remote Site Setting **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 270**
Report **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 271**
Report Type **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 272**
ServiceProcess **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 273**
Slack App (Beta) **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 274**
Service Catalog Category **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 275**
Service Catalog Filter Criteria **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 276**
Service Catalog Item Definition **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 277**
Service Catalog Fulfillment Flow **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 278**
Stationary Asset Environmental Source Record Type Configuration **. . . . . . . . . . . . . . . 279**
Static Resource **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 280**
Streaming App Data Connector **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 281**
Sustainability UOM **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 282**
Sustainability UOM Conversion **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 283**
Timeline Object Definition **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 284**
Timesheet Template **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 285**
Transaction Processing Type **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 286**

**Contents**

Translation **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 287**
UI Object Relation Config **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 288**
User Access Policy **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 289**
Validation Rule **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 290**
Vehicle Asset Emissions Source Record Type Configuration **. . . . . . . . . . . . . . . . . . . . 291**
View Definition (Beta) **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 292**
Virtual Visit Config **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 294**
Visualforce Component **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 295**
Visualforce Page **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 296**
Wave Analytic Asset Collection **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 297**
Wave Application **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 298**
Wave Component **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 299**
Wave Dataflow **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 300**
Wave Dashboard **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 301**
Wave Dataset **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 302**
Wave Lens **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 303**
Wave Recipe **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 304**
Wave Template Bundle **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 305**
Wave Xmd **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 306**
Web Store Template **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 307**
Workflow Alert **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 308**
Workflow Field Update **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 309**
Workflow Knowledge Publish **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 310**
Workflow Outbound Message **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 311**
Workflow Rule **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 312**
Workflow Task **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 313**
Behavior of Specific Metadata in Second-Generation Managed Packages **. . . . . . . . . . . . . . 314**

Package Agentforce Metadata Components **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 316**
Develop and Package Agent Templates Using Scratch Orgs **. . . . . . . . . . . . . . . . . . . . 316**
MCP for Agentforce Metadata in Managed Packages **. . . . . . . . . . . . . . . . . . . . . . . . 320**
Package Data Cloud Metadata Components **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 324**
Protected Components in Managed Packages **. . . . . . . . . . . . . . . . . . . . . . . . . . . . 325**
Set Up a Platform Cache Partition with Provider Free Capacity **. . . . . . . . . . . . . . . . . . 326**
Metadata Access in Apex Code **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 327**
Permission Sets and Profile Settings in Packages **. . . . . . . . . . . . . . . . . . . . . . . . . . . 327**
Protecting Your Intellectual Property **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 332**
Call Salesforce URLs Within a Package **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 333**
Namespace-Based Visibility for Apex Classes in Second-Generation Managed
Packages **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 334**
Work with Services Outside of Salesforce **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 335**
Package Connected Apps in Second-Generation Managed Packaging **. . . . . . . . . . . 336**
Test and Respond to the New Order Save Behavior **. . . . . . . . . . . . . . . . . . . . . . . . . 337**
Develop Second-Generation Managed Packages **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 339**

Create a Second-Generation Managed Package **. . . . . . . . . . . . . . . . . . . . . . . . . . . 339**

**Contents**

View Package Details for a Second-Generation Managed Package **. . . . . . . . . . . . . . 340**
Create Versions of a Second-Generation Managed Package **. . . . . . . . . . . . . . . . . . 340**
Guidance for Package Version Numbering **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 343**
View Details about a Second-Generation Managed Package Version **. . . . . . . . . . . . . 344**
Project Configuration File for a Second-Generation Managed Package **. . . . . . . . . . . . 346**
Get Ready to Promote and Release a Second-Generation Managed Package Version **. . 350**
Specify a Package Ancestor in the Project File for a Second-Generation Managed
Package **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 351**
Install and Uninstall Second-Generation Managed Packages **. . . . . . . . . . . . . . . . . . . . . . 353**

Use the CLI to Install a Second-Generation Managed Package **. . . . . . . . . . . . . . . . . . 354**
Use a URL to Install a Second-Generation Managed Package **. . . . . . . . . . . . . . . . . . 355**
Install Notifications for Unauthorized Managed Packages **. . . . . . . . . . . . . . . . . . . . . 356**
Upgrade a Second-Generation Managed Package Version **. . . . . . . . . . . . . . . . . . . . 356**
Resolve Apex Test Failures **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 357**
Run Apex on Package Install/Upgrade **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 357**
Customize Second-Generation Managed Package Installs and Uninstalls Using Scripts
**. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 361**
Sample Script for Installing Second-Generation Managed Packages with
Dependencies **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 362**
Uninstall a Second-Generation Managed Package **. . . . . . . . . . . . . . . . . . . . . . . . . 364**
Prepare to Distribute Your Second-Generation Managed Package **. . . . . . . . . . . . . . . . . . . 365**

Code Coverage for Second-Generation Managed Packages **. . . . . . . . . . . . . . . . . . . 365**
Package Installation Key for Second-Generation Managed Packages **. . . . . . . . . . . . . 366**
Release a Second-Generation Managed Package **. . . . . . . . . . . . . . . . . . . . . . . . . . 366**
Share Release Notes and Post-Install Instructions for Second-Generation Managed
Packages **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 367**
Publishing Your App on AppExchange **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 368**
Recommend a Specific Package Version to Your Subscribers **. . . . . . . . . . . . . . . . . . . 368**
Push a Package Upgrade for Second-Generation Managed Packages **. . . . . . . . . . . . . . . . 369**

Schedule a Push Upgrade Using CLI **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 370**
Schedule a Push Upgrade Using SOAP API for First- and Second-Generation Managed
Packages **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 373**
Enable a Package Subscriber to Restrict Push Upgrades **. . . . . . . . . . . . . . . . . . . . . . 374**
Assign Access to New and Changed Features in First- and Second-Generation Managed
Packages **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 375**
Sample Post Install Script for a Push Upgrade for First- and Second-Generation Managed
Packages **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 376**
Push Upgrade Best Practices **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 377**
Advanced Features for Second-Generation Managed Packages **. . . . . . . . . . . . . . . . . . . . 378**

Package Ancestors for Second-Generation Managed Packages **. . . . . . . . . . . . . . . . 380**
Patch Versions for Second-Generation Managed Packages **. . . . . . . . . . . . . . . . . . . . 384**
Create Dependencies Between Second-Generation Managed Packages **. . . . . . . . . . . 385**
Considerations for Promoting Packages with Dependencies **. . . . . . . . . . . . . . . . . . . 389**

**Contents**

Advanced Project Configuration Parameters for Second-Generation Managed
Packages **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 390**
Second-Generation Managed Packaging Keywords **. . . . . . . . . . . . . . . . . . . . . . . . . 394**
Target a Specific Release for Your Second-Generation Managed Packages During
Salesforce Release Transitions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 395**
Use Branches in Second-Generation Managed Packaging **. . . . . . . . . . . . . . . . . . . . 396**
Specify Unpackaged Metadata or Apex Access for Package Version Creation Tests for
Second-Generation Managed Packages **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 397**
Package IDs and Aliases for Second-Generation Managed Packages **. . . . . . . . . . . . . 398**
Avoid Namespace Collisions in Second-Generation Managed Packages **. . . . . . . . . . . 399**
Remove Metadata Components from Second-Generation Managed Packages **. . . . . . . 401**
Delete a Second-Generation Managed Package or Package Version **. . . . . . . . . . . . . 405**
Frequently Used Packaging Operations for Second-Generation Managed Packages **. . . 406**
Transfer a Second-Generation Managed Package to a Different Dev Hub **. . . . . . . . . . 406**
Contact Salesforce Partner Support to Enable Specific Packaging Features **. . . . . . . . . . . 411**
Best Practices for Second-Generation Managed Packages **. . . . . . . . . . . . . . . . . . . . . . . . 412**
Manage Licenses for Managed Packages **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 412**

Get Started with the License Management App **. . . . . . . . . . . . . . . . . . . . . . . . . . . . 413**
Lead and License Records in the License Management App **. . . . . . . . . . . . . . . . . . . . 417**
Modify a License Record **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 417**
Refresh Licenses for a Managed Package **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 418**
Extending the License Management App **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 418**
Move the License Management App to Another Salesforce Org **. . . . . . . . . . . . . . . . . 421**
Troubleshoot the License Management App **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 422**
Best Practices for the License Management App **. . . . . . . . . . . . . . . . . . . . . . . . . . . 423**
Troubleshoot Subscriber Issues **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 423**
Manage Features in Second-Generation Managed Packages **. . . . . . . . . . . . . . . . . . . . . . 426**

Feature Parameter Metadata Types and Custom Objects **. . . . . . . . . . . . . . . . . . . . . 427**
Set Up Feature Parameters **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 428**
Use LMO-to-Subscriber Feature Parameters to Enable and Disable Features **. . . . . . . . 430**
Track Preferences and Activation Metrics with Subscriber-to-LMO Feature Parameters **. . 431**
Hide Custom Objects and Custom Permissions in Your Subscribers’ Orgs **. . . . . . . . . . . 431**
Best Practices for Feature Management **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 432**
Considerations for Feature Management **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 432**
Get Started with AppExchange App Analytics **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 433**

App Analytics Use Cases **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 434**
Enable App Analytics on Your Second-Generation Managed Package **. . . . . . . . . . . . . 437**
Download Package Usage Logs, Package Usage Summaries, and Subscriber
Snapshots **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 437**
Considerations for Custom Interactions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 438**
AppExchange App Analytics Best Practices **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 443**
Package Usage Summaries **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 460**
Package Usage Logs **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 462**
Subscriber Snapshots **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 487**

**Contents**

Test Custom Integrations **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 489**
AppExchange App Analytics Developer Cookbook **. . . . . . . . . . . . . . . . . . . . . . . . . . 490**
Gaps Between First-Generation and Second-Generation Managed Packaging **. . . . . . . . . . . 510**

# CHAPTER 1 Second-Generation Managed Packages

In this chapter ...

**•** What’s a
# Second-Generation

Managed Package?

Second-generation managed packaging (managed 2GP) ushers in a new way for AppExchange partners
to develop, distribute, and manage their apps and metadata. You can use managed 2GP packaging to
organize your source, build small modular packages, integrate with your version control system, and
better utilize your custom Apex code. With version control being the source of truth, there are no
packaging or patch orgs. You can execute all packaging operations via Salesforce CLI, or automate them
using scripts. Submit second-generation managed packages for security review, and list them on
AppExchange.

**•** Set Up Your using scripts. Submit second-generation managed packages for security review, and list them on
Development AppExchange.
Environment
Use managed 2GP to create new managed packages. You can’t currently migrate a first-generation

**•** Before You Create
managed package to a second-generation managed package.
# Second-Generation

Managed Packages Another great way to learn about second-generation managed packages, is by taking the
# Second-Generation Managed Packages Trailhead module.

**•** Scratch Orgs and
Package

Note: Second-generation managed packaging addresses the specific needs of AppExchange

Development

Note: Second-generation managed packaging addresses the specific needs of AppExchange

Development

partners. If you’re a customer or system integrator and you don’t plan to distribute a package to

**•** Workflow for multiple customers, unlocked packaging is the preferred tool. You can use unlocked packages to
# Second-Generation organize your existing metadata, package an app or extension, or package new metadata. See

Managed Packages

multiple customers, unlocked packaging is the preferred tool. You can use unlocked packages to
# Second-Generation organize your existing metadata, package an app or extension, or package new metadata. See

Managed Packages

[Unlocked Packages for more information.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_unlocked_pkg_intro.htm)

**•** Components
Available in
# Second-Generation

Managed Packages

**•** Behavior of Specific
Metadata in
# Second-Generation

Managed Packages

**•** Develop
# Second-Generation

Managed Packages

**•** Install and Uninstall
# Second-Generation

Managed Packages

**•** Prepare to Distribute
Your
# Second-Generation

Managed Package

**•** Push a Package
Upgrade for
# Second-Generation

Managed Packages

**•** Advanced Features
for
# Second-Generation

Managed Packages


Second-Generation Managed Packages

**•** Best Practices for
Second-Generation
Managed Packages

**•** Manage Licenses for
Managed Packages

**•** Manage Features in
Second-Generation
Managed Packages

**•** Get Started with
AppExchange App
Analytics

**•** Gaps Between
First-Generation and
Second-Generation
Managed Packaging


## Second-Generation Managed Packages What’s a Second-Generation Managed Package? What’s a Second-Generation Managed Package?

If your goal is to build an app and distribute it on AppExchange, you’ll use managed packages to do both. Packaging is the container
that you fill with metadata, and it holds the set of related features, customizations, and schema that make up your app. A package can
include many different metadata components, and you can package a single component, an app, or library.

Each second-generation managed package follows a distinct lifecycle. As you develop your app, you add metadata to a package, and
create a new package version. While the package is continually evolving, each package version is an immutable artifact.

A package version contains the set of metadata and features associated with the package version at the moment it was created. As you
iterate on your package, and add, remove, or change the packaged metadata, you're likely to create many package versions along the
way.

You can install a package version in a scratch, sandbox, trial, developer edition, or production org. Your customers can install the package
into their org and when you release a new package version, your customers can upgrade to the latest version.

You can repeat the package development cycle any number of times. You can change metadata, create a package version, test the
package version, and distribute it to your customers via AppExchange.

### Why Switch to Second-Generation Managed Packaging?

You’ve been using first-generation managed packages to develop your apps, so you’re probably pretty familiar with what works
well, and what’s a bit more painful than you’d like. And no doubt, you’re aware that second-generation managed packages is our
newer technology, but maybe you aren’t so sure why switching to second-generation managed packaging (managed 2GP) will
improve your package development experience. So let’s talk about that.

Comparison of First- and Second-Generation Managed Packages
If you’re familiar with first-generation managed packages (managed 1GP) and wonder how it’s different from second-generation
managed packages (managed 2GP), here are some key distinctions.

### Why Switch to Second-Generation Managed Packaging?

You’ve been using first-generation managed packages to develop your apps, so you’re probably pretty familiar with what works well,
and what’s a bit more painful than you’d like. And no doubt, you’re aware that second-generation managed packages is our newer
technology, but maybe you aren’t so sure why switching to second-generation managed packaging (managed 2GP) will improve your
package development experience. So let’s talk about that.

Source-Driven Development

The source-driven development model used in managed 2GP is a big shift from the org-based development used in managed 1GP. Say
goodbye to packaging orgs as your source of truth. Instead, your source of truth with managed 2GP is the package metadata in your
version control system. And as you develop your managed 2GP package, you create and update your package metadata in a version
control system, not in an org.

Minimal Interaction with Salesforce Orgs

As you probably know well, with managed 1GP development, every package and patch version requires a unique Salesforce org, so it’s
not uncommon for you to own 100s of Salesforce orgs in which your package metadata is deployed. Managing these orgs and their
credentials can become a nightmare.

Managed 2GP takes away the hassle of managing orgs, and instead you use a single org, the Dev Hub org, to manage all your packages.
And even when you do need to connect to your Dev Hub org you’ll use Salesforce CLI (Command Line Interface) or a script to log in.


Second-Generation Managed Packages Why Switch to Second-Generation Managed Packaging?

By eliminating the need to manually log in and keep track of hundreds of packaging and patch orgs (and their login credentials), managed
2GP simplifies package development and promotes modern, programmatic Application Lifecycle Management (ALM).

API- and CLI-first Model

Unlike managed 1GP, which has only partial API coverage, you can perform every managed 2GP packaging operation using an API or
CLI command. You can completely automate packaging operations and be more productive. Repeatable, scriptable, and track-able ALM
is truly possible with managed 2GP.

Flexible Versioning

Managed 1GP packaging follows a linear versioning model that requires you to build upon the previous package version. This approach
is very restrictive, and for metadata that can’t be removed from a package, you’re stuck with that metadata in your managed 1GP.

Enter managed 2GP and flexible versioning. If you create a managed-released package version that you haven’t yet distributed to a
customer, you can abandon that package version and select a previous package version as the ancestor you want to build upon. Flexible
versioning also allows you to use branches and do parallel package development. You can iterate fast, learn from, and move on from
any mistakes.

One Namespace Shared Across Multiple Packages

Managed 1GP packages require each package to have a unique namespace. This restriction can lead to a proliferation of global Apex
because sharing code among packages is only possible by declaring Apex classes and methods as global.

Managed 2GP changes the game by allowing multiple packages to share the same namespace. The `@namespaceAccessible`
annotation then lets you share public Apex classes and methods across all packages in the same namespace. By using public Apex, you
don’t increase your global Apex footprint by exposing a global API.

Declarative Dependencies

In managed 2GP packaging, you specify dependencies among packages declaratively in a `.json` file. Which as you know, is a more
developer-friendly approach than how managed 1GP dependencies are declared.

Simplified Patch Versioning

Creating a patch version of a managed 2GP is as easy as creating a new major or minor package version. You use a Salesforce CLI command
and specify a non-zero number for the patch version number. And that’s it!

Because your version control system is the source of truth for managed 2GP, creating patch versions is straightforward. We promise you
won’t miss the laborious and error-prone patch org process of managed 1GP.

Avoid Having to Migrate Customers in the Future

As you may be aware, we’re developing capabilities to migrate your managed 1GP packages to managed 2GP. However, when we
launch that capability, there’s work that you have to do to migrate your managed 1GP packages and customers from 1GP to 2GP. By
adopting managed 2GP today for your new packages, you avoid the hassle of migration in the future.


### Second-Generation Managed Packages Comparison of First- and Second-Generation Managed

Packages

### Comparison of First- and Second-Generation Managed Packages

If you’re familiar with first-generation managed packages (managed 1GP) and wonder how it’s different from second-generation managed
packages (managed 2GP), here are some key distinctions.

Despite these distinctions, managed 1GP and 2GP packages have many things in common. They share the key packaging concept of
associating metadata with a package. And they both allow you to iterate and create package and patch versions, which can be installed
and uninstalled in subscriber orgs. Both managed package types enable you to submit a package for AppExchange security review, and
list your package on AppExchange. And both managed package types can use the License Management App, Subscriber Support
Console, and Feature Management App.


## Second-Generation Managed Packages Set Up Your Development Environment Set Up Your Development Environment

Second-generation managed packaging uses Salesforce DX developer tools. Ensure that you have the required tools and orgs installed
and enabled.

You use these tools for managed 2GP package development.

**•** [Salesforce CLI, a rich set of commands to execute different packaging operations like package creation and package install](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_setup.meta/sfdx_setup/sfdx_setup_intro.htm)

**•** A source control system of your choosing

**•** A Dev Hub org

**•** [Salesforce Extension for Visual Studio Code (optional), an IDE designed to facilitate the development of Salesforce components](https://developer.salesforce.com/tools/vscode/en/vscode-desktop/install)

Use the Dev Hub to Keep Track of Package Development

Your Dev Hub is the designated place to find and manage all your managed 2GP packages, scratch orgs, and namespaces. After you
enable the Dev Hub setting on a Salesforce org, that Dev Hub becomes the owner of every managed 2GP package you create.

All Salesforce ISV and OEM partners should designate their Partner Business Org as their Dev Hub org. A Partner Business Org (PBO) is
the production org where Salesforce Partners run their business.

### Enable Dev Hub and Second-Generation Managed Packaging

The Dev Hub lets you create and manage second-generation managed packages and scratch orgs. Your Dev Hub is the designated
place to find and manage all your managed 2GP packages, scratch orgs, and namespaces.

Limited Access License for Package Developers
The Salesforce Limited Access - Free is designed for users whose role is to build customizations or applications. This license provides
access to the Dev Hub, development tools, and environments. In the production org, this license restricts access to standard and
custom objects. Partner Business Orgs (PBO) include 100 Salesforce Limited Access - Free user licenses.

Add a Limited Access User to Your Dev Hub Org
Provide your developers access to the Dev Hub and Salesforce DX development tools by adding a user with Salesforce Limited Access

      - Free license and the Limited Access user profile in your Dev Hub org. Then create and assign them a permission set to the required
Dev Hub objects.

Assign Second-Generation Managed Packaging User Permissions
To create second-generation managed packages and scratch orgs, developers require access to the Dev Hub org. We recommend
enabling the Dev Hub in your Partner Business Org (PBO). A Salesforce admin can create a permission set to grant appropriate
permissions to the required Dev Hub objects and system permission.

### Enable Dev Hub and Second-Generation Managed Packaging

The Dev Hub lets you create and manage second-generation managed packages and scratch orgs.
Your Dev Hub is the designated place to find and manage all your managed 2GP packages, scratch
orgs, and namespaces.

After you enable the Dev Hub setting on a Salesforce org, that Dev Hub becomes the owner of
every managed 2GP package you create. All Salesforce ISV and OEM partners should designate their
Partner Business Org (PBO) as their Dev Hub org.

To enable Dev Hub:

**1.** Log in to your Partner Business Org.


EDITIONS

Available in: Salesforce
Classic and Lightning
Experience

Dev Hub available in:
**Developer**, **Enterprise**,
**Performance**, and
**Unlimited** Editions

### Second-Generation Managed Packages Limited Access License for Package Developers

**2.** From Setup, enter _`Dev Hub`_ in the Quick Find box and select **Dev Hub** . If you don't see Dev Hub in the Setup menu, make sure
that your org is one of the supported editions.

**3.** Select **Enable Dev Hub** . After you enable Dev Hub, you can’t disable it.

**4.** Select **Enable Unlocked Packages and Second-Generation Managed Packages** . After you enable this setting, you can’t disable
it.

If you choose to use a trial or Developer Edition org as your Dev Hub, consider these factors.

**•** When a trial or Developer Edition org expires, you lose access to all packages associated with that Dev Hub org.

**•** You’re limited to creating up to six scratch orgs and package versions per day, with a maximum of three active scratch orgs.

**•** Trial orgs expire on their expiration date.

**•** Developer Edition orgs can expire due to inactivity.

**•** If a package is associated with a non-production Dev Hub org, and that org expires or becomes inactive, the installed package can't
be updated, and new attempts to install the package may fail.

**•** If you plan to create package versions or run continuous integration jobs, it’s better to use your PBO as your Dev Hub because of
higher scratch org and package version limits.

The Dev Hub org instance determines where scratch orgs are created.

**•** Scratch orgs created from a Dev Hub org in Government Cloud are created on a Government Cloud instance.

**•** Scratch orgs created from a Dev Hub org in Public Cloud are created on a Public Cloud instance.

Note: You can’t enable Dev Hub in a sandbox.

### Limited Access License for Package Developers

The Salesforce Limited Access - Free is designed for users whose role is to build customizations or applications. This license provides
access to the Dev Hub, development tools, and environments. In the production org, this license restricts access to standard and custom
objects. Partner Business Orgs (PBO) include 100 Salesforce Limited Access - Free user licenses.

[If the Salesforce Limited Access - Free license isn’t already enabled in your PBO, log a case with Salesforce Partner Support to request up](https://partners.salesforce.com)
to 100 licenses. A Salesforce admin can upgrade a Salesforce Limited Access - Free license to a standard Salesforce license at any time.

Certain developer features aren’t available with the Salesforce Limited Access - Free license.

**•** To provide the ability to create and manage org shapes, assign the Salesforce user license. The Salesforce Limited Access - Free
license isn’t supported at this time.

**•** Users with the Salesforce Limited Access - Free license and View All Records permissions can create scratch orgs using an existing
org shape.

**•** Users with the Salesforce Limited Access - Free license and View All Records permissions can view scratch org snapshots created by
users other than themselves.

**•** The Salesforce Limited Access - Free license doesn’t provide access to some Salesforce CLI commands, such as `sf limits api`
`display` .

**•** Contact your Salesforce admin for API limits information.

[If your developers need broader access, consider assigning the Salesforce license. For details, see Standard User Licenses in](https://help.salesforce.com/s/articleView?id=platform.users_license_types_available.htm&type=5&language=en_US) _Salesforce_
_Help_ .


### Second-Generation Managed Packages Add a Limited Access User to Your Dev Hub Org Add a Limited Access User to Your Dev Hub Org

Provide your developers access to the Dev Hub and Salesforce DX development tools by adding a user with Salesforce Limited Access

    - Free license and the Limited Access user profile in your Dev Hub org. Then create and assign them a permission set to the required
Dev Hub objects.

The Salesforce Limited Access - Free is designed for users whose role is to build customizations or applications. This license provides
access to the Dev Hub, development tools, and environments. In the production org, this license restricts access to standard and custom
objects.

**1.** Create a user in your Dev Hub org.

**a.** In Setup, enter _`Users`_ in the Quick Find box, then select **Users** .

**b.** Click **New User** .

**c.** Fill out the form.

**d.** Select **Salesforce Limited Access - Free** for User License, and then **Limited Access User** for Profile.

**e.** After filling out the remaining information, click **Save** .

**2.** [Create a permission set that provides your developer users with access to the required Dev Hub objects. For details, see Create and](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_setup_permission_set.htm)
[Assign a Permission Set for Developer Users or Assign Second-Generation Managed Packaging User Permissions.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_setup_permission_set.htm)

### Assign Second-Generation Managed Packaging User Permissions

To create second-generation managed packages and scratch orgs, developers require access to the Dev Hub org. We recommend
enabling the Dev Hub in your Partner Business Org (PBO). A Salesforce admin can create a permission set to grant appropriate permissions
to the required Dev Hub objects and system permission.

To give developers access to the Dev Hub org, create a permission set that contains these required permissions:

**•** Object Settings > Scratch Org Info > Read, Create, and Delete

**•** Object Settings > Active Scratch Org > Read and Delete

**•** Object Settings > Namespace Registry > Read (to use a linked namespace in a scratch org)

To provide users with the ability to create second-generation managed packages and package versions, the permission set must also
contain:

**•** System Permissions > Create and Update Second-Generation Packages

This permission provides access to:

If you choose to test your package in a scratch org, the Create and Update Second-Generation Packages permission is also required
when creating the scratch org if you specified an ancestor version in the `sfdx-project.json` file. Alternatively, use the
`--noancestors` flag with the `sf org create` command when you create the scratch org.


## Second-Generation Managed Packages Before You Create Second-Generation Managed Packages Before You Create Second-Generation Managed Packages

When you use second-generation managed packaging, to be sure that you set it up correctly, verify the following.

Did you?

**•** [Enable Dev Hub and Second-Generation Managed Packaging in your Partner Business Org (PBO)](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_pkg_enable_devhub.htm)

**•** [Install Salesforce CLI](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_setup.meta/sfdx_setup/sfdx_setup_intro.htm)

**•** [Create and Register Your Namespace for Second-Generation Managed Packages](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_create_namespace.htm)

Developers who work with managed 2GP packages need a user license and permission set that provides access to the Dev Hub org. See
[Limited Access License for Package Developers and Assign Second-Generation Managed Packaging User Permissions.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_pkg_slalf_pkg_dev.htm)

### Know Your Orgs for Second-Generation Managed Packages

Some of the orgs that you use with second-generation managed packaging (managed 2GP) have a unique purpose.

Link a Namespace to a Dev Hub Org
To use a namespace with a scratch org, you must link the Developer Edition org where the namespace is registered to a Dev Hub
org.

Namespaces for Second-Generation Managed Packages
A namespace is a 1–15 character alphanumeric identifier that distinguishes your package and its contents from other packages in
your customer’s org. A namespace is assigned to a second-generation managed package (managed 2GP) at the time that it’s created,
and can’t be changed.

Create and Register Your Namespace for Second-Generation Managed Packages
With second-generation managed packaging (managed 2GP), you can share a single namespace with multiple packages. Since
sharing of code is much easier if your package shares the same namespace, we recommend that you use a single namespace for all
of your managed 2GP packages.

Key Concepts in Second-Generation Managed Packaging
Let’s look at some key high-level concepts in second-generation managed packaging (managed 2GP).

How Manageability Rules and Ancestry Impact Upgrades for Second-Generation Managed Packages
Before you dive in and create your first second-generation managed package (managed 2GP), it’s important to understand these
concepts, and how they affect each other.

Which Package Types Can Your Package Depend On?
Both second-generation managed packaging (managed 2GP) and unlocked packaging let you easily develop small interdependent
packages and share logic between them. If you design your app to rely on small modular packages, both package creation and
package installation are faster, and you’re less likely to hit limits.

### Know Your Orgs for Second-Generation Managed Packages

Some of the orgs that you use with second-generation managed packaging (managed 2GP) have a unique purpose.

Choose Your Dev Hub Org

Use the Dev Hub org for these purposes.

**•** As owner of all second-generation managed packages

**•** To link your namespaces

**•** To authorize and run your `sf package` Salesforce CLI commands


### Second-Generation Managed Packages Link a Namespace to a Dev Hub Org

We recommend that your Partner Business Org is also your Dev Hub org. For important considerations about your Dev Hub org, see
Enable Dev Hub and Second-Generation Managed Packaging on page 6.

Note: The Dev Hub org against which you run the `sf package create` command becomes the owner of the package.

If the Dev Hub org expires or is deleted, packages owned by that Dev Hub:

**•** Can’t be transferred to a different Dev Hub

**•** Stop working and new package versions can’t be created

Namespace Org

The primary purpose of the namespace org is to acquire a namespace for your managed 2GP package.

After you create a namespace org and specify the namespace in it, open the Dev Hub org and link the namespace org to the Dev Hub
org.

Other Orgs

When you work with managed 2GP packages, you also use these orgs:

**•** Scratch orgs to develop and test your packages.

**•** A target or installation org in which you install the package.

SEE ALSO:

### Link a Namespace to a Dev Hub Org

[Scratch Org Allocations for Partners](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/isv_partner_scratch_org_allocations.htm)

_[Salesforce DX Developer Guide:](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_scratch_orgs.htm)_ Scratch Orgs

### Link a Namespace to a Dev Hub Org

To use a namespace with a scratch org, you must link the Developer Edition org where the namespace is registered to a Dev Hub org.

Complete these tasks before you link a namespace.

**•** If you don’t have an org with a registered namespace, create a Developer Edition org that is separate from the Dev Hub or scratch
orgs. If you already have an org with a registered namespace, you’re good to go.

**•** In the Developer Edition org, create and register the namespace.

Important: Choose namespaces carefully. If you’re trying out this feature or need a namespace for testing purposes, choose
a disposable namespace. Don’t choose a namespace that you want to use in the future for a production org or some other
real use case. After you associate a namespace with an org, you can't change it or reuse it.

**1.** Log in to your Dev Hub org as the System Administrator or as a user with the Salesforce DX Namespace Registry permissions.

Tip: Make sure your browser allows pop-ups from your Dev Hub org.

**a.** From the App Launcher menu, select **Namespace Registries** .

**b.** Click **Link Namespace** .

**2.** In the window that pops up, log in to the Developer Edition org in which your namespace is registered using the org's System
Administrator's credentials.


### Second-Generation Managed Packages Namespaces for Second-Generation Managed Packages

You can’t link orgs without a namespace: sandboxes, scratch orgs, patch orgs, and branch orgs require a namespace to be linked to
the Namespace Registry.

To view all the namespaces linked to the Namespace Registry, select the **All Namespace Registries** list view.

### Namespaces for Second-Generation Managed Packages

A namespace is a 1–15 character alphanumeric identifier that distinguishes your package and its contents from other packages in your
customer’s org. A namespace is assigned to a second-generation managed package (managed 2GP) at the time that it’s created, and
can’t be changed.

When you specify a package namespace, every component added to a package has the namespace prefixed to the component API
name. Let’s say you have a custom object called Insurance_Agent with the API name, `Insurance_Agent__c` . If you add this
component to a package associated with the Acme namespace, the API name becomes `Acme__Insurance_Agent__c` .

Important: When creating a namespace, use something that’s useful and informative to users. However, don’t name a namespace
after a person (for example, by using a person's name, nickname, or private information).

When you work with namespaces, keep these considerations in mind.

**•** You can develop more than one managed 2GP package and associate the packages with the same namespace. But a single managed
2GP package can't be associated with more than one namespace.

**•** If you work with more than one namespace, we recommend that you set up one project for each namespace.

**•** It's beneficial for managed 2GP packages to share the same namespace, but it's not required. Carefully consider your package and
namespace strategy. After a namespace is associated with a managed 2GP, the association can't be changed.

**•** There are scenarios where you may prefer to keep a managed 2GP package isolated from other managed 2GP packages you're
developing. For example, if you’re developing a product that you intend to sell or spin off, having a unique namespace for that
package enables you to transfer the namespace with the package.

SEE ALSO:

### Create and Register Your Namespace for Second-Generation Managed Packages

[Link a Namespace to a Dev Hub Org](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_reg_namespace.htm.htm)

[Avoid Namespace Collisions in Second-Generation Managed Packages](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_namespace_collisions.htm)

### Create and Register Your Namespace for Second-Generation Managed

Packages

With second-generation managed packaging (managed 2GP), you can share a single namespace with multiple packages. Since sharing
of code is much easier if your package shares the same namespace, we recommend that you use a single namespace for all of your
managed 2GP packages.

To create a namespace:

**1.** Sign up for a new Developer Edition org.

**2.** In Setup, enter _`Package Manager`_ in the Quick Find box, and select **Package Manager** .

**3.** In Namespace Settings, click **Edit** .

**4.** Enter a namespace and select **Check Availability** .

**5.** (Optional) Select a package to associate with this namespace, or select **None**, then click **Review** .

**6.** Review your selections, and then click **Save** .


### Second-Generation Managed Packages Key Concepts in Second-Generation Managed Packaging

To register a namespace:

**1.** [To link the namespace that you created with your Dev Hub, use Namespace Registry. See Link a Namespace to a Dev Hub Org for](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_reg_namespace.htm)
details.

**2.** In the `sfdx-project.json` file, specify your namespace using the namespace attribute. When you create a new 2GP package,
the package is associated with the namespace specified in the `sfdx-project.json` file.

SEE ALSO:

[Namespaces for Second-Generation Managed Packages](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_plan_namespaces.htm)

[Link a Namespace to a Dev Hub Org](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_reg_namespace.htm)

[Avoid Namespace Collisions in Second-Generation Managed Packages](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_namespace_collisions.htm)

### Key Concepts in Second-Generation Managed Packaging

Let’s look at some key high-level concepts in second-generation managed packaging (managed 2GP).


### Second-Generation Managed Packages How Manageability Rules and Ancestry Impact Upgrades

for Second-Generation Managed Packages

### How Manageability Rules and Ancestry Impact Upgrades for

Second-Generation Managed Packages

Before you dive in and create your first second-generation managed package (managed 2GP), it’s important to understand these concepts,
and how they affect each other.

**•** Manageability Rules

**•** Package Ancestry

**•** Package Upgrades

**Manageability Rules**
Each metadata component that you include in a managed 2GP package has certain rules that determine its behavior in a subscriber
org. Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is
installed in a subscriber’s org.

Manageability rules apply at both the component level and at the component attribute level. For example, manageability rules
determine whether you or the subscriber can delete a custom field, and more specifically whether either of you can edit the Field
Label, Default Value, or other attributes of the custom field. For all first- and second-generation managed packages, we enforce
manageability rules during package version creation. If you attempt to make a change that would break a manageability rule for
one of the metadata components in your package, your package version creation fails.

**Package Ancestry**
Second-generation managed packaging offers a flexible linear package versioning model by letting you break your linear versioning
and abandon a package version you no longer want to build upon. We call these versioning decisions package ancestry. When you
create a package version, you must also specify which package version is the ancestor.

[In this quick glance at a package ancestry tree, version 1.2 and 1.5 have been abandoned. To dig deeper into this topic, see Package](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_package_ancestor_intro.htm)
[Ancestors.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_package_ancestor_intro.htm)


### Second-Generation Managed Packages Which Package Types Can Your Package Depend On?

**How Manageability Rules and Ancestry Impact Package Upgrades**
Both manageability rules and package ancestry impact package upgrades. During package upgrade we enforce the manageability
rule for each new and changed component in your package version. Depending on what you changed when you created the new
package version, some metadata is added to the org during package upgrade, other metadata is modified or deleted, and some
changes aren’t applied at all.

For example, page layouts don’t get updated during package upgrade, so if you change a page layout, only new customers receive
your modified page layout. When existing subscribers upgrade their package, they won’t receive that change. Conversely, changes
to Apex code or the formula in a formula field are updated during a package upgrade.

Package ancestry determines the package upgrade path. This is a complex topic, and we have topics that go deeper into this subject.
At a high level the package version you designate as the ancestor determines whether a subscriber can upgrade to that version.
[Subscribers can upgrade from one package version to another only if the ancestry tree is followed. To learn more, see Understanding](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_config_upgrades.htm)
[Package Upgrades with Ancestry.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_config_upgrades.htm)

SEE ALSO:

[Package Ancestors for Second-Generation Managed Packages](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_package_ancestor_intro.htm)

[Understanding Package Upgrades with Ancestry](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_config_upgrades.htm)

### Which Package Types Can Your Package Depend On?

Both second-generation managed packaging (managed 2GP) and unlocked packaging let you easily develop small interdependent
packages and share logic between them. If you design your app to rely on small modular packages, both package creation and package
installation are faster, and you’re less likely to hit limits.

To develop small, modular packages, you create dependencies between your packages. A package dependency is when metadata
contained in one package depends on metadata contained in another package. These dependencies allow you to extend the functionality
of the base package with components and metadata in a separate extension package.

When working with packaging, only certain combinations of packages are supported.


## Second-Generation Managed Packages Scratch Orgs and Package Development

1This dependency isn’t supported, and we block the installation of managed 2GP packages in managed 1GP packaging orgs. We can
[override this behavior on an individual basis. To share your scenario and request an override, log a case with Salesforce Partner Support.](https://partners.salesforce.com)
We’re investigating how to support this dependency scenario more broadly.

SEE ALSO:

[Create Dependencies Between Second-Generation Managed Packages](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_create_dependencies.htm)

[Considerations for Promoting Packages with Dependencies](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/dev2gp_considerations_pkg_dependency.htm)

## Scratch Orgs and Package Development

Scratch orgs are temporary Salesforce orgs intended for development and automation. They enable
source-driven deployments of Salesforce code and metadata. A scratch org is fully configurable,
allowing developers to emulate different Salesforce editions with various features and preferences.

You can use a scratch org to develop the app you want to package, and you can also create scratch
orgs to test out your package. Scratch orgs also help with continuous integration (CI) processes to
automate package development steps. For example, you could write a script that creates a package
version, creates a scratch org, installs the package version into the scratch org, runs Apex tests, and
emails the test results to the release manager.

Enable Data Cloud for Scratch Orgs

EDITIONS

Available in: Lightning
Experience

Available in: **Developer**,
**Enterprise**, **Performance**,
and **Unlimited** Editions

To use Data Cloud components in scratch orgs or to add these components to a package, Data Cloud for Scratch Orgs must be enabled.
[Log a case with Salesforce Partner Support and request that Data Cloud for Scratch Orgs be enabled on your Partner Business Org. Data](https://partners.salesforce.com/)
Cloud for Scratch Orgs is only available to scratch orgs associated with the Dev Hub in your Partner Business Org.

How Scratch Orgs Fit in the Package Development Workflow
Scratch orgs are an essential tool in both developing and testing the app you want to package. Scratch orgs also help with continuous
integration (CI) processes to automate package development steps. For example, you could write a script that creates a package
version, creates a scratch org, installs the package version into the scratch org, runs Apex tests, and emails the test results to the
release manager.

Scratch Org Definition Files vs Org Shape in Package Development
The scratch org definition file is used when you create scratch orgs, and also when you create new package versions. The scratch
org definition file is a blueprint for your scratch org and defines the shape of the org you want for your package development work.


### Second-Generation Managed Packages How Scratch Orgs Fit in the Package Development Workflow

When to Use Scratch Org Snapshots in Package Development
If the managed 2GP or unlocked package that you’re building depends on one or more large packages, it can take a long time for
the package version creation CLI command to complete. Let’s talk about why that occurs, and how scratch org snapshots can
dramatically reduce how long it takes to create a new package version.

Create a Package Version Based on a Scratch Org Snapshot
If the dependent package your base package requires is stable, you can reduce the end-to-end package version creation time by
creating a scratch org snapshot.

Get Access to Scratch Orgs That Have Agentforce
Agentforce is a set of tools to create and customize AI agents that are deeply and securely integrated with customers' data and apps.
Agentforce brings together humans with agents to transform the way work gets done. Start your journey with Agentforce by testing
it in a scratch org.

Scratch Org Allocations for Salesforce Partners
To ensure optimal performance, Salesforce partners are allocated a set number of scratch orgs in their Partner Business Org (PBO).
These allocations determine how many scratch orgs you can create daily, and how many can be active at a given point.

Manage Scratch Orgs from the Dev Hub Org
You can view and delete your scratch orgs and their associated requests from the Dev Hub org.

Supported Scratch Org Editions for Partners
Create partner edition scratch orgs from a Dev Hub partner business org.

### How Scratch Orgs Fit in the Package Development Workflow

Scratch orgs are an essential tool in both developing and testing the app you want to package. Scratch orgs also help with continuous
integration (CI) processes to automate package development steps. For example, you could write a script that creates a package version,
creates a scratch org, installs the package version into the scratch org, runs Apex tests, and emails the test results to the release manager.

Develop Your Package in a Scratch Org

When developing a package, it’s preferable to use a namespaced scratch org. A namespaced scratch org prepends scratch org metadata
with the package namespace. This is true for both metadata you create in the scratch org, and any metadata you deploy to the scratch
org.

To create a namespaced scratch org, use your Dev Hub org to create the scratch org. Before you create the scratch org:

**•** [Ensure that the namespace you plan to use is already associated with your Dev Hub org.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_reg_namespace.htm)

**•** Specify the namespace in your `sfdx-project.json` file.

**•** [Create a scratch org definition file and include any features, settings, or limits that your org needs.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_scratch_orgs_def_file.htm)

When you create a scratch org both the namespace and ancestry information listed in `sfdx-project.json` file are pulled into
the scratch org. The ancestry information, specified as `ancestorId` or `ancestorVersion` in your `sfdx-project.json`
file, seeds the scratch org with manageability rules, and later warns you if you attempt to change metadata in a way that's incompatible
with the specified ancestor version. This way, you learn of issues during development instead of during the creation of the next package
version.

To create a namespaced scratch org that includes ancestor information in the scratch org, run this CLI command.

```
   sf org create scratch --target-dev-hub MyHub --definition-file

   config/project-scratch-def.json

```


### Second-Generation Managed Packages Scratch Org Definition Files vs Org Shape in Package

Development

If you don’t want the ancestor and manageability rules seeded into the scratch org, include the `--no-ancestors` flag when you
create the scratch org.

[When you are ready to create a new package version, see Create Versions of a Second-Generation Managed Package.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_create_pkg_ver.htm)

Test Your Package in a Scratch Org

When testing your package, create a scratch org that doesn’t have a namespace. Use the `--no-namespace` parameter when you
create the scratch org.

```
   sf org create scratch --definition-file config/project-scratch-def.json --no-namespace

   --no-ancestors

```

[After you create the scratch org, install the package into the scratch org, and begin testing.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_install_pkg_cli.htm)

Enable Data Cloud for Scratch Orgs

To use Data Cloud components in scratch orgs or to add these components to a package, Data Cloud for Scratch Orgs must be enabled.
[Log a case with Salesforce Partner Support and request that Data Cloud for Scratch Orgs be enabled on your Partner Business Org. Data](https://partners.salesforce.com/)
Cloud for Scratch Orgs is only available to scratch orgs associated with the Dev Hub in your Partner Business Org.

SEE ALSO:

_[Salesforce DX Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_scratch_orgs_create.htm)_ : Create Scratch Orgs

_[Salesforce CLI Command Reference](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_org_commands_unified.htm#cli_reference_org_create_scratch_unified)_ : org create scratch

_Salesforce DX Developer Guide_ [: Select the Salesforce Release for a Scratch Org](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_scratch_orgs_version_selection.htm)

### Scratch Org Definition Files vs Org Shape in Package Development

The scratch org definition file is used when you create scratch orgs, and also when you create new package versions. The scratch org
definition file is a blueprint for your scratch org and defines the shape of the org you want for your package development work.

Build Your Own Scratch Definition File

If you read How Scratch Orgs Fit in the Package Development Workflow on page 16 you might recall that the CLI command for creating
scratch orgs includes a flag called `--definition-file` .

```
   sf org create scratch --target-dev-hub MyHub --definition-file

   config/project-scratch-def.json

```

In this example, `project-scratch-def.json` is the scratch org definition file. To learn more about what can be specified in
[this definition file, see Build Your Own Scratch Org Definition File in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_scratch_orgs_def_file.htm) _Salesforce DX Developer Guide_ .

Similarly the CLI `--definition-file` flag can be used when creating a new package version.

```
   sf package version create --package "Expenser App"

   --definition-file config/project-scratch-def.json --code-coverage

```

When used in the `package version create` command, the scratch org definition file is used to specify the features, settings,
or limits that your package requires.


### Second-Generation Managed Packages When to Use Scratch Org Snapshots in Package Development

When to Use Org Shape

If you're developing managed packages to distribute on AppExchange, we expect that you know what features and settings your
packages depends on, and expect you to specify these requirements in a scratch org definition file. But there are scenarios like unlocked
[packages, or if you're moving from 1GP to 2GP package development, where using Org Shape for Scratch Orgs can be useful.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_shape_intro.htm)

During org shape creation, we capture the features, settings, edition, licenses, and limits of the specified source org. By using org shape
you don’t have to manually list these items in the scratch org definition file.

Note: The source org you use for org shape can’t be a sandbox or scratch org.

Later when you create a package version, specify the org ID for the source org in the scratch org definition file.

```
   {

     "orgName": "Acme",

     "sourceOrg": "00DB1230400Ifx5"

   }

```

[For more detailed instructions on enabling and creating org shape, review Create a Scratch Org Based on an Org Shape in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_shape_intro.htm) _Salesforce_
_DX Developer Guide._

If you’re moving from managed 1GP package development to 2GP package development, creating an org shape of your 1GP packaging
org could be useful as you begin 2GP package development. Creating an org shape of your 1GP packaging org ensures that the features
required for your package metadata are specified.

SEE ALSO:

How Scratch Orgs Fit in the Package Development Workflow

_Salesforce DX Developer Guide_ [: Build Your Own Scratch Org Definition File](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_scratch_orgs_def_file.htm)

_Salesforce DX Developer Guide_ [: Create a Scratch Org Based on an Org Shape](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_shape_intro.htm)

_Salesforce DX Developer Guide_ [: Create a Scratch Org Based on an Org Shape](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_shape_intro.htm)

### When to Use Scratch Org Snapshots in Package Development

If the managed 2GP or unlocked package that you’re building depends on one or more large packages, it can take a long time for the
package version creation CLI command to complete. Let’s talk about why that occurs, and how scratch org snapshots can dramatically
reduce how long it takes to create a new package version.

When you run the `package version create` CLI command, we create a scratch org behind the scenes. That scratch org serves
as a build org where we build your package. In the build org we install the dependent packages you specified, and deploy the package
metadata for the package version you're creating. If your dependent packages are large, the package install time for those dependent
packages extends the overall package creation time.

If the dependent packages that your base package requires are stable, you can reduce the end-to-end package version creation time
by creating a scratch org snapshot, and using that scratch org snapshot during package version creation.

[A scratch org snapshot captures the state of a scratch org’s configuration so that you can use the snapshot to create scratch org replicas.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_snapshots_intro.htm)
A snapshot is a point-in-time copy of a scratch org that includes installed packages, features, limits, licenses, metadata, and data. If you
install your dependent packages in the scratch org before you create the snapshot, and you specify the snapshot when you create a
new package version, the package build process bypasses these steps. Meaning, we don't install the dependent packages into the build
org, we use the snapshot instead. By not installing the dependent packages during package version creation, your package version
builds in a fraction of the time.


### Second-Generation Managed Packages Create a Package Version Based on a Scratch Org Snapshot

Keep in mind, the intention of scratch org snapshots in the package development cycle is to shorten the package creation time during
development. When you are ready to promote and release a package, you must create a new package version that doesn’t rely on a
scratch org snapshot. Package versions created using scratch org snapshots can’t be promoted to the released state.

[Note: You can promote an unlocked package based on a snapshot. Only managed packages based on snapshots can’t be](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_unlocked_pkg_intro.htm)
promoted to the released state.

SEE ALSO:

### Create a Package Version Based on a Scratch Org Snapshot

_[Salesforce DX Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_snapshots_intro.htm)_ : Scratch Org Snapshots

### Create a Package Version Based on a Scratch Org Snapshot

If the dependent package your base package requires is stable, you can reduce the end-to-end package version creation time by creating
a scratch org snapshot.

If you haven’t reviewed When to Use Scratch Org Snapshots in Package Development on page 18, review that topic before continuing.

There’s more than one workflow you can follow when creating a package version based on a scratch org snapshot. You can start by
creating a scratch org, you can build your own scratch org definition file, or you can choose to use org shape to create a new scratch
org. Whichever path you choose, after the scratch org is created, you install all the dependent packages into it, and then take a snapshot
of the scratch org.

Sample Workflow

This workflow uses an org shape to create the initial scratch org where you’ll install the stable dependent packages, and then create a
scratch org snapshot to create a package version.

**1.** Create the org shape.

```
     sf org create shape --target-org source-org1

```

**2.** Create a scratch org definition file that indicates the shape’s source org.

```
     {

      "orgName": "Salesforce",

      "sourceOrg": "00DB1230400Ifx5"

     }

```

**3.** Create a scratch org using the org shape.

```
     sf org create scratch --duration-days 30 --no-namespace --no-ancestors --definition-file

      config/scratch-def-with-shape-id.json --alias dev1-with-shape

```

If your default Dev Hub org isn’t the one that owns the org shape, indicate it on the command line.

**4.** Install the dependent packages.

```
     sf package install --package 04txx --target-org dev1-with-shape

```

**5.** Create a snapshot of the scratch org.

```
     sf org create snapshot --name dhsnapshot --source-org dev1-with-shape --target-dev-hub

      dev-hub

```


### Second-Generation Managed Packages Get Access to Scratch Orgs That Have Agentforce

**6.** Create a new scratch org definition file and specify the snapshot name, then save the file.

```
     {

      "orgName": "Salesforce",

      "snapshot": "dhsnapshot"

     }

```

**7.** Create a package version using the org snapshot. This command is specifying the scratch org definition file that contains the snapshot
information in it.

```
     sf package version create --package hc-ext1 --code-coverage --installation-key-bypass

     --async-validation --definition-file

     scratch-def-with-snapshot-id.json

```

SEE ALSO:

When to Use Scratch Org Snapshots in Package Development

_[Salesforce DX Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_scratch_orgs_create.htm)_ : Create Org Shapes

### Get Access to Scratch Orgs That Have Agentforce

Agentforce is a set of tools to create and customize AI agents that are deeply and securely integrated with customers' data and apps.
Agentforce brings together humans with agents to transform the way work gets done. Start your journey with Agentforce by testing it
in a scratch org.

[If you don’t already have a Partner Business Org (PBO), join the Salesforce Partner Community and request a PBO.](https://developer.salesforce.com/docs/atlas.en-us.262.0.packagingGuide.meta/packagingGuide/appexchange_partner_join.htm)

If you’re new to creating scratch orgs, follow these steps to complete the one-time Dev Hub setup in your PBO. The Dev Hub is a feature
within an org that lets you create and manage scratch orgs, second-generation managed packages (2GP), and namespaces.

**•** [Enable the Dev Hub and 2GP](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_pkg_enable_devhub.htm)

**•** [Create a Developer Edition org using Environment Hub](https://developer.salesforce.com/docs/atlas.en-us.262.0.packagingGuide.meta/packagingGuide/environment_hub_manage_create_org.htm)

**•** [Create a namespace in the Developer Edition org](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_create_namespace.htm)

**•** [Link that namespace from your PBO. Linking the namespace lets you create 2GP packages that use that namespace.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_reg_namespace.htm)

**•** [Authorize the Dev Hub org.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_auth_web_flow.htm)

**•** [Create a Salesforce DX Project.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_ws_create_new.htm)

To create a scratch org with Agentforce and Prompt Builder enabled, use this sample `project-scratch-def.json` file (or
simply add the feature and setting shown in this sample to your existing scratch org definition file).

```
   {

     "orgName": "GenAI Scratch Org",

     "edition": "Partner Developer",

     "features": ["Einstein1AIPlatform"],

     "settings": {

      "einsteinGptSettings" : {

       "enableEinsteinGptPlatform" : true

      }

     }

   }

```

To create a scratch org with the Einstein1AIPlatform feature, the scratch org you create can be a Partner Developer, Partner Enterprise,
Developer, or Enterprise edition.


Second-Generation Managed Packages Get Access to Scratch Orgs That Have Agentforce

To create a scratch org, run this Salesforce CLI command. Update the definition-file name, alias, and target-dev-hub alias as needed.

```
   sf org create scratch --definition-file config/my-agentforce-project-scratch-def.json

   --alias MyNamespacedScratchOrg --set-default --target-dev-hub MyDevHubOrg

```

Scratch Orgs with both Agentforce and Data Cloud

For some use cases such as prompt templates that use RAG, Retrievers, or BYO LLM, a scratch org that has both GenAI and Data Cloud
functionality enabled is required.

Only include Data Cloud if it’s required. Specifying Data Cloud in a scratch org significantly increases the time it takes for a scratch org
creation to complete.

Note: Including Data Cloud in a scratch org has a prerequisite. You must first open a case in the Salesforce Partner Community
to request for your PBO Dev Hub org to be granted permission to create Data Cloud scratch orgs. This request is only granted to
PBO orgs.

```
   {

     "orgName": "GenAI & Data Cloud Scratch Org",

     "edition": "Partner Developer",

     "features": ["CustomerDataPlatform", "CustomerDataPlatformLite","Einstein1AIPlatform"],

     "settings": {

      "einsteinGptSettings" : {

       "enableEinsteinGptPlatform" : true

      },

      "customerDataPlatformSettings": {

       "enableCustomerDataPlatform": true

      }

     }

   }

```

Set up Agentforce in your Scratch Org

After your scratch org is created, follow these steps to start developing with Agentforce.

**•** [Create Agents manually in the scratch org.](https://help.salesforce.com/s/articleView?id=sf.copilot_setup_enable.htm&language=en_US)

**•** [To use prompt templates with your Agent Actions, assign prompt template permissions.](https://help.salesforce.com/s/articleView?id=ai.prompt_builder_enable.htm&type=5&language=en_US)

SEE ALSO:

[Packageable Agentforce Metadata](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/dev2gp_packageable_agentforce_md.htm)

_Trailhead_ [: Quick Start: Build Your First Agent with Agentforce](https://trailhead.salesforce.com/content/learn/projects/quick-start-build-your-first-agent-with-agentforce)

_Salesforce Help_ [: Agentforce: Agents](https://help.salesforce.com/s/articleView?id=ai.copilot_intro.htm&type=5&language=en_US)

_[Agentforce Developer Guide](https://developer.salesforce.com/docs/einstein/genai/guide/get-started.html)_

_Salesforce Help_ [: The Building Blocks of Agents](https://help.salesforce.com/s/articleView?id=ai.copilot_building_blocks.htm&type=5&language=en_US)

_Salesforce Help_ [: Customize Your Agents with Topics and Actions](https://help.salesforce.com/s/articleView?id=ai.copilot_topics_actions.htm&type=5&language=en_US)

_Salesforce Help_ [: Considerations for Agents](https://help.salesforce.com/s/articleView?id=ai.copilot_considerations.htm&type=5&language=en_US)

_Salesforce Help_ [: AI Project Success](https://help.salesforce.com/s/articleView?id=ai.generative_ai_plan_project.htm&type=5&language=en_US)


### Second-Generation Managed Packages Scratch Org Allocations for Salesforce Partners Scratch Org Allocations for Salesforce Partners

To ensure optimal performance, Salesforce partners are allocated a set number of scratch orgs in their Partner Business Org (PBO). These
allocations determine how many scratch orgs you can create daily, and how many can be active at a given point.

By default, Salesforce deletes scratch orgs and their associated ActiveScratchOrg records from your Dev Hub when a scratch org expires.
All partners get 100 Salesforce Limited Access - Free user licenses.

Active PBOs

**•** 150 active

**•** 300 daily

Trial PBOs

**•** 20 active

**•** 40 daily

Scratch Org Snapshot Allocations

The number of snapshots you can create (active and daily) is the same as the active scratch org allocation.

Package Version Creation Limits

The maximum number of package versions you can create per day is equal to the daily allocated scratch orgs. For example, if you’re
allocated 300 daily scratch orgs, you’re also allowed to create 300 package versions per day.

If you specify `--skipvalidation` when creating a package version, the maximum number of package versions you can create
[using skip validation is 500 per day.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_skip_validation.htm)

### Manage Scratch Orgs from the Dev Hub Org

You can view and delete your scratch orgs and their associated requests from the Dev Hub org.

In the Dev Hub org, the ActiveScratchOrg standard object represents the scratch orgs that are currently in use. The ScratchOrgInfo
standard object represents the requests that were used to create scratch orgs and provides historical context.

**1.** Log in to the Dev Hub org as the System Administrator or as a user with the Salesforce DX permissions.

**2.** From the App Launcher, select **Active Scratch Orgs** to see a list of all active scratch orgs.

To view more details about a scratch org, click the link in the Number column.

**3.** To delete an active scratch org from the Active Scratch Orgs list view, choose **Delete** from the dropdown.

Deleting an active scratch org doesn’t delete the request (ScratchOrgInfo) that created it, but it does free up a scratch org so that it
doesn’t count against your allocations.

**4.** To view the requests that created the scratch orgs, select **Scratch Org Infos** from the App Launcher.

To view more details about a request, click the link in the Number column. The details of a scratch org request include whether it's
active, expired, or deleted.

**5.** To delete the request that was used to create a scratch org, choose **Delete** from the dropdown.


### Second-Generation Managed Packages Supported Scratch Org Editions for Partners

Deleting the request (ScratchOrgInfo) also deletes the active scratch org.

### Supported Scratch Org Editions for Partners

Create partner edition scratch orgs from a Dev Hub partner business org.

Supported partner scratch org editions include:

**•** Partner Developer

**•** Partner Enterprise

**•** Partner Group

**•** Partner Professional

Indicate the partner edition in the scratch org definition file.

```
   "edition": "Partner Enterprise",

```

If you attempt to create a partner scratch org and see this error, confirm that you’re using an active partner business org. Contact the
[Partner Community for further assistance.](https://partners.salesforce.com/)

```
   ERROR: You don't have permission to create Partner Edition organizations.

   To enable this functionality, please log a case in the Partner Community.

```

[License limits for partner scratch orgs are similar to partner edition orgs created in Environment Hub. Get the details on the Partner](https://partners.salesforce.com/s/education/general/Partner_Orgs)
[Community.](https://partners.salesforce.com/s/education/general/Partner_Orgs)

## Workflow for Second-Generation Managed Packages

You can create and install a second-generation managed package (managed 2GP) directly from the command line.

Review and complete the steps in Before You Create Second-Generation Managed Packages before starting this workflow.

The basic managed 2GP workflow includes these steps. See specific topics for details about each step.

**1.** Create a DX project.

```
     sf project generate --output-dir expense-manager-workspace --name expenser-app

```

**2.** Authorize the Dev Hub org.

```
     sf org login web --set-default-dev-hub

```

When you perform this step, include the `---set-default-dev-hub` option. You can then omit the Dev Hub username when
running subsequent Salesforce CLI commands.

Tip: If you define an alias for each org you work with, it’s easy to switch between different orgs from the command line. You
can authorize different orgs as you iterate through the package development cycle.

**3.** Create a scratch org and develop the app you want to package. You can use VS Code and the Setup UI in the scratch org to build
and retrieve the pieces you want to include in your package. Navigate to the expenser-app directory, and then run this command.

```
     sf org create scratch --definition-file config/project-scratch-def.json

```

**4.** Verify that all package components are in the project directory where you want to create a package. If you’re trying out the exact
steps and commands in this workflow, you must add at least one piece of metadata before you continue to the next step.


Second-Generation Managed Packages Workflow for Second-Generation Managed Packages

**5.** In the `sfdx-project.json` file, specify a namespace using the namespace attribute. For example: “namespace”: “exp-mgr”

If you specified a namespace when you created a Salesforce DX project in step one, you can skip this step. Before adding a namespace,
make sure that you’ve linked the namespace to your Dev Hub org.

**6.** From the Salesforce DX project directory, create the package.

```
     sf package create --name "Expense Manager" --path force-app --package-type Managed

```

Your new managed 2GP package has the namespace you specified in the `sfdx-project.json` file.

Important: After you create a package, you can’t change or add a namespace, or change the Dev Hub the package is associated
with.

**7.** Review your `sfdx-project.json` file. The CLI automatically updates the project file to include the package directory and
creates an alias based on the package name.

```
     {

       "packageDirectories": [

         {

          "path": "force-app",

          "default": true,

          "package": "Expense Manager",

          "versionName": "ver 0.1",

          "versionNumber": "0.1.0.NEXT"

         }

       ],

       "namespace": "exp-mgr",

       "sfdcLoginUrl": "https://login.salesforce.com",

       "sourceApiVersion": "51.0",

       "packageAliases": {

         "Expense Manager": "0Hoxxx"

       }

     }

```

Notice the placeholder values for `versionName` and `versionNumber` . You can update these values, or indicate base packages
that this package depends on. Your project file displays the `namespace` you created.

Specify the features and org settings required for the metadata in your package using an external `.json` file, such as the scratch
org definition file. You can specify using the `--definition-file` flag with the `sf package version create`
command, or list the definition file in your `sfdx-project.json` file. See: Project Configuration File for a Second-Generation
Managed Package

**8.** Create a package version. This example assumes the package metadata is in the `force-app` directory.

```
     sf package version create --package "Expense Manager" --code-coverage --installation-key

      test1234 --wait 10

```

**9.** Install and test the package version in a scratch org. Use a different scratch org from the one you used in step three.

```
     sf package install --package "Expense Manager@0.1.0-1" --target-org MyTestOrg1

     --installation-key test1234 --wait 10 --publish-wait 10

```

**10.** After the package is installed, open the scratch org to view the package.

```
     sf org open --target-org MyTestOrg1

```


## Second-Generation Managed Packages Components Available in Second-Generation Managed

Packages

Package versions are beta until you promote them to a managed-released state. See: Release a Second-Generation Managed Package.

SEE ALSO:

[Before You Create Second-Generation Managed Packages](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_before.htm)

[Create and Register Your Namespace for Second-Generation Managed Packages](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_create_namespace.htm)

[Project Configuration File for a Second-Generation Managed Package](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev2gp_config_file.htm)

[Release a Second-Generation Managed Package](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_create_pkg_ver_promote.htm)

## Components Available in Second-Generation Managed Packages

Each metadata component that you include in a second-generation managed package has certain rules that determine its behavior in
a subscriber org. Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version
is created and installed.

Before you review the details about the metadata components that can be included in a managed package, be sure you understand
the meaning of each manageability rule.

**Table 1: Manageability Rules**


Second-Generation Managed Packages Components Available in Second-Generation Managed
Packages

Editable Properties After Package Promotion or Installation

Certain properties on metadata components are editable after the managed package is installed.

**•** Only Package Developer Can Edit: The package developer can edit specific component properties. These properties are locked in
the subscriber’s org. During package upgrade, the changes made by the package developer are applied in the subscriber org. For
example, when you update the code in an Apex class or the custom permissions in a permission set, subscribers receive those
updates during their package upgrade.

**•** Both Subscriber and Package Developer Can Edit: Both the subscriber and package developer can edit these component properties,
but developer changes are only applied to new subscriber installs. This approach prevents a package upgrade from overwriting
changes made by the subscriber. For example, the help text on a custom field, and the page layout of a custom object are editable
by both the subscriber and package developer. The subscriber can modify the page layout or help text, and trust that their changes
won’t be overwritten by a future package upgrade.

**•** Neither Subscriber or Package Developer Can Edit: After a package is promoted and released, these component properties are locked
and can’t be edited by the package developer or the subscriber. For example, the API names of packaged components are locked
and can’t be edited after the package version is promoted and released.

Supported Components in Second-Generation Managed Packages

Account Plan Objective Measure Calculation Definition
Represents the definition of a target object, rollup field, and logic for calculating the current value of a sales account plan objective
measure.

Account Relationship Share Rule
Determines which object records are shared, how they’re shared, the account relationship type that shares the records, and the level
of access granted to the records.

Action Link Group Template
Represents the action link group template. Action link templates let you reuse action link definitions and package and distribute
action links.

Action Plan Template
Represents an instance of an action plan template.

Actionable List Definition
Represents the data source definition details associated with an actionable list.

Actionable List Key Performance Indicator Definition
Represents the custom key performance indicators that are defined for a specific field in an object.


Second-Generation Managed Packages Components Available in Second-Generation Managed
Packages

Activation Platform
Represents the ActivationPlatform configuration, such as platform name, delivery schedule, output format, and destination folder.

AffinityScoreDefinition
Represents the affinity information used in calculations to analyze and categorize contacts for marketing purposes.

Agent Action
Represents an action, for use in Agentforce.

Agent Topic
Represents a topic, for use in Agentforce.

AI Application
Represents an instance of an AI application. For example, Einstein Prediction Builder.

AI Application Config
Represents additional prediction information related to an AI application.

AIUsecaseDefinition
Represents a collection of fields in a Salesforce org used to define a machine learning use case and get real-time predictions.

Analytics
Analytics components include analytics applications, dashboards, dataflows, datasets, lenses, recipes, and user XMD.

Analytics Visualization
Represents a Tableau Next visualization.

Analytics Workspace
Represents a Tableau Next workspace.

Apex Class
Represents an Apex Class. An Apex class is a template or blueprint from which Apex objects are created. Classes consist of other
classes, user-defined methods, variables, exception types, and static initialization code.

Apex Sharing Reason
Represents an Apex sharing reason, which is used to indicate why sharing was implemented for a custom object.

Apex Trigger
Represents an Apex trigger. A trigger is Apex code that executes before or after specific data manipulation language (DML) events
occur, such as before object records are inserted into the database, or after records have been deleted.

App Framework Template Bundle
Represents the app framework template bundle. Use these templates for Data Cloud and Tableau Next assets.

Application Subtype Definition
Represents a subtype of an application within an application domain.

AssessmentConfiguration
Represents a configuration for Assessment component. An AssessmentConfiguration entry indicates configuration for user flows
such as sending out emails or reminder actions on assessments initiated by the patient.

AssessmentQuestion
Represents the container object that stores the questions required for an assessment.

AssessmentQuestionSet
Represents the container object for Assessment Questions.


Second-Generation Managed Packages Components Available in Second-Generation Managed
Packages

Aura Component
Represents an Aura definition bundle. A bundle contains an Aura definition, such as an Aura component, and its related resources,
such as a JavaScript controller. The definition can be a component, application, event, interface, or a tokens collection.

Batch Calc Job Definition
Represents a Data Processing Engine definition.

Batch Process Job Definition
Represents the details of a Batch Management job definition.

Benefit Action
Represents details of an action that can be triggered for a benefit.

Bot Template
Represents the configuration details for a specific Einstein Bot template, including dialogs and variables.

Branding Set
Represents the definition of a set of branding properties for an Experience Builder site, as defined in the Theme panel in Experience
Builder.

Briefcase Definition
Represents a briefcase definition. A briefcase makes selected records available for specific users and groups to view when they’re
offline in the Salesforce Field Service mobile app for iOS and Android.

Building Energy Intensity Record Type Configuration
Represents the setup object that contains the mapping between the Building Energy Intensity Record record type and internal
enums. You can primarily use this object for calculations across different record types.

Business Process
The BusinessProcess metadata type enables you to display different picklist values for users based on their profile.

Business Process Group
Represents the surveys used to track customers’ experiences across different stages in their lifecycle.

Business Process Type Definition
Define the types of business processes that are applied to a rule.

Care Benefit Verify Settings
Represents the configuration settings for benefit verification requests.

Care Limit Type
Defines the characteristics of limits on benefit provision.

Care Request Configuration
Represents the details for a record type such as service request, drug request, or admission request. One or more record types can
be associated with a care request.

Care System Field Mapping
Represents a mapping from source system fields to Salesforce target entities and attributes.

Channel Layout
Represents the metadata associated with a communication channel layout.

Chatter Extension
Represents the metadata used to describe a Rich Publisher App that’s integrated with the Chatter publisher.

Claim Financial Settings
Represents the configuration settings for Insurance Claim Financial Services.


Second-Generation Managed Packages Components Available in Second-Generation Managed
Packages

CommunicationChannelType
Represents the type of communication channel, such as WhatsApp and SMS, to use for referral promotions.

Community Template Definition
Represents the definition of an Experience Builder site template.

Community Theme Definition
Represents the definition of a theme for an Experience Builder site.

Compact Layout
Represents the metadata associated with a compact layout.

Conditional Formatting Ruleset
Represents a set of rules that define the style and visibility of conditional field formatting on Dynamic Forms-enabled Lightning page
field instances.

Connected App
Represents a connected app configuration. A connected app enables an external application to integrate with Salesforce using APIs
and standard protocols, such as SAML, OAuth, and OpenID Connect.

Context Definition
A context definition defines the relationship between the nodes and the attributes within each node. For efficient data access, users
can use nodes and attributes to easily access the relevant data from the mapped data source. Various Salesforce products offer
predefined context definitions based on their use case.

Contract Type
A contract type is used to group contracts so that they exhibit similar characteristics. For example, the lifecycle states, the people
who access, the templates and clauses used.

Conversation Channel Definition
Represents the conversation channel definition that’s implemented for Interaction Service for Bring Your Own Channel and Bring
Your Own Channel for CCaaS messaging channels.

Conversation Vendor Info
This setup object connects the partner vendor system to the Service Cloud feature.

CORS Allowlist
Represents an origin in the CORS allowlist.

CSP Trusted Site
Represents a trusted URL. For each CspTrustedSite component, you can specify Content Security Policy (CSP) directives and permissions
policy directives.

Custom Application
Represents a custom application.

Custom Button or Link
Represents a custom link defined in a home page component.

Custom Console Components
Represents a custom console component (Visualforce page) assigned to a CustomApplication that is marked as a Salesforce console.
Custom console components extend the capabilities of Salesforce console apps.

Custom Field on Standard or Custom Object
Represents the metadata associated with a field. Use this metadata type to create, update, or delete custom field definitions on
standard or custom objects.


Second-Generation Managed Packages Components Available in Second-Generation Managed
Packages

Custom Field on Custom Metadata Type
Represents a custom fields on the custom metadata type.

Custom Field Display
Represents the CustomFieldDisplay view type assigned to product attribute custom fields.

Custom Help Menu Section
Represents the section of the Lightning Experience help menu that the admin added to display custom, org-specific help resources
for the org. The custom section contains help resources added by the admin.

Custom Index
Represents an index used to increase the speed of queries.

Custom Label
The CustomLabels metadata type allows you to create custom labels that can be localized for use in different languages, countries,
and currencies.

Custom Metadata Type Records
Represents a record of a custom metadata type.

Custom Metadata Type
Represents a record of a custom metadata type.

Custom Notification Type
Represents the metadata associated with a custom notification type.

Custom Object
Represents a custom object that stores data unique to an org or an external object that maps to data stored outside an org.

Custom Object Translation
This metadata type allows you to translate custom objects for a variety of languages.

Custom Permission
Represents a permission that grants access to a custom feature.

Custom Tab
Represents a custom tab. Custom tabs let you display custom object data or other web content in Salesforce.

Dashboard
Represents a dashboard. Dashboards are visual representations of data that allow you to see key metrics and performance at a glance.

DataCalcInsightTemplate
Represents the object template for data calculations and insights of Data Cloud objects in DataCalcInsightTemplate. These objects
are added inside the data kit.

Data Connector Ingest API
Represents the connection information specific to Ingestion API.

Data Connector S3
Represents the connection information specific to Amazon S3.

Data Kit Object Dependency
Represent the object dependencies and relationships between different objects in Data Kit Object Dependency. These objects are
added inside the data kit.

Data Kit Object Template
Represents the object in Data Kit Object Template. This object template is added inside the data kit.


Second-Generation Managed Packages Components Available in Second-Generation Managed
Packages

DataObjectBuildOrgTemplate
Represents the output objects of the components the user includes in a data kit.

Data Package Kit Definition
Represents the top-level Data Kit container definition. Content objects can be added after the Data Kit is defined.

Data Package Kit Object
Represents the object in Data Kit Content Object. These objects are added inside the data kit.

Data Source
Used to represent the system where the data was sourced.

Data Source Bundle Definition
Represents the bundle of streams that a user adds to a data kit.

Data Source Object
Represents the object from where the data was sourced.

Data Src Data Model Field Map
Represents the entity that’s used to store the design-time bundle-level mappings for the data source fields and data model fields.

Data Stream Definition
Contains Data Ingestion information such as Connection, API and File retrieval settings.

Data Stream Template
Represents the data stream that a user adds to a data kit.

DataWeaveResource
Represents the DataWeaveScriptResource class that is generated for all DataWeave scripts. DataWeave scripts can be directly invoked
from Apex.

Decision Matrix Definition
Represents a definition of a decision matrix.

Decision Matrix Definition Version
Represents a definition of a decision matrix version.

Decision Table
Represents the information about a decision table.

Decision Table Dataset Link
Represents the information about a dataset link associated with a decision table. In a dataset link, select an object for whose records,
the decision table must provide an outcome.

Digital Experience
Represents a text-based code structure of your organization’s workspaces, organized by workspace type, and each workspace’s
content items.

Digital Experience Bundle
Represents a text-based code structure of your organization’s workspaces, organized by workspace type, and each workspace’s
content items.

Decision Table
Represents the information about a decision table.

Disclosure Definition
Represents information that defines a disclosure type, such as details of the publisher or vendor who created or implemented the
report.


Second-Generation Managed Packages Components Available in Second-Generation Managed
Packages

Disclosure Definition Version
Represents the version information about the disclosure definition.

Disclosure Type
Represents the types of disclosures that are done by an individual or an organization and the associated metadata.

Discovery AI Model
Represents the metadata associated with a model used in Einstein Discovery.

Discovery Goal
Represents the metadata associated with an Einstein Discovery prediction definition.

Discovery Story
Represents the metadata associated with a story used in Einstein Discovery.

Document
Represents a Document. All documents must be in a document folder, such as sampleFolder/TestDocument.

Document Generation Setting
Represents an org's settings for automatic document generation from templates.

Eclair GeoData
Represents an Analytics custom map chart. Custom maps are user-defined maps that are uploaded to Analytics and are used just
as standard maps are. Custom maps are accessed in Analytics from the list of maps available with the map chart type.

Email Template (Classic)
Use email templates to increase productivity and ensure consistent messaging. Email templates with merge fields let you quickly
send emails that include field data from Salesforce records.

Email Template (Lightning)
Represents a template for an email, mass email, list email, or Sales Engagement email.

Embedded Service Config
Represents a setup node for creating an Embedded Service for Web deployment.

Embedded Service Menu Settings
Represents a setup node for creating a channel menu deployment. Channel menus list the ways in which customers can contact
your business.

Enablement Measure Definition
Represents an Enablement measure, which specifies the job-related activity that a user performs to complete a milestone or outcome
in an Enablement program. A measure identifies a source object and optional related objects, with optional field filters and filter
logic, for tracking the activity.

Enablement Program Definition
Represents an Enablement program, which includes exercises and measurable milestones to help users such as sales reps achieve
specific outcomes related to your company’s revenue goals.

Enablement Program Task Subcategory
Represents a custom exercise type that an Enablement admin adds to an Enablement program in Program Builder. A custom exercise
type also requires a corresponding EnblProgramTaskDefinition record for Program Builder and corresponding LearningItem and
LearningItemType records for when users take the exercise in the Guidance Center.

Entitlement Template
Represents an entitlement template. Entitlement templates are predefined terms of customer support that you can quickly add to
products.


Second-Generation Managed Packages Components Available in Second-Generation Managed
Packages

ESignature Config
Using the Electronic Signature Configuration setup, the system admin must define the required configurations to support the
e-signature APIs and UI.

ESignature Envelope Config
Using the Electronic Signature Envelope Config the system admin can define the default reminders and expiry for the envelopes
submitted for eSignature.

Event Relay
Represents an event relay that you can use to send platform events and change data capture events from Salesforce to Amazon
EventBridge.

Explainability Action Definition
Define where the metadata for your Decision Explainer business rules are stored in Public Sector Solutions.

Explainability Action Version
Define and store versions of the explainability actions used by your Decision Explainer business rules in Public Sector Solutions.

Explainability Message Template
Represents information about the template that contains the decision explanation message for a specified expression set step type.

Expression Set Definition
Represents an expression set definition.

Expression Set Definition Version
Represents a definition of an expression set version.

Expression Set Object Alias
Represents information about the alias of the source object that’s used in an expression set.

Expression Set Message Token
Represents a token that's used in an explainability message template. The token can be replaced with an expression set version
resource that the template is used in. This object is available in API version 59.0 and later.

External Auth Identity Provider
Represents the external auth identity provider that obtains OAuth tokens for callouts that use named credentials.

External Client App Canvas Settings
Represents an external client app's canvas app settings.

External Client App Header
Represents the header file for an external client application configuration.

External Client App Notification Settings
Represents the settings configuration for the external client app’s notifications plugin.

External Client App OAuth Settings
Represents the settings configuration for the external client app’s OAuth plugin.

External Client App Push Settings
Represents the settings configuration for the external client app’s push notification plugin.

External Credential
Represents the details of how Salesforce authenticates to the external system.

External Data Connector
Used to represent the object where the data was sourced.


Second-Generation Managed Packages Components Available in Second-Generation Managed
Packages

External Data Source
Represents the metadata associated with an external data source. Create external data sources to manage connection details for
integration with data and content that are stored outside your Salesforce org.

External Data Transport Field Template
Represents the definition of a Data Cloud schema field.

External Data Transport Field
Use ExternalDataTranField to add a field to the ExternalDataTranObject in your managed packages. ExternalDataTranObject is a Data
Cloud schema object.

External Data Transport Object Template
Represents the definition of a Data Cloud schema object.

External Data Transport Object
To include a Data Cloud schema object in your managed packages, add ExternalDataTranObject.

External Document Storage Configuration
Represents configuration, which admin makes in setup to specify the drive, path, and named credential to be used for storing
documents on external drives.

External Services
Represents the External Service configuration for an org.

Feature Parameter Boolean
Represents a boolean feature parameter in the Feature Management App (FMA). Feature parameters let you drive app behavior and
track activation metrics in subscriber orgs that install your package.

Feature Parameter Date
Represents a date feature parameter in the Feature Management App (FMA). Feature parameters let you drive app behavior and
track activation metrics in subscriber orgs that install your package.

Feature Parameter Integer
Represents an integer feature parameter in the Feature Management App (FMA). Feature parameters let you drive app behavior and
track activation metrics in subscriber orgs that install your package.

FieldMappingConfig
Represents the configuration for fields mapped between a source object and one or more destination objects and fields. This object
is available in API version 63.0 and later.

Field Set
Represents a field set. A field set is a grouping of fields. For example, you could have a field set that contains fields describing a user's
first name, middle name, last name, and business title.

Field Source Target Relationship
Stores the relationships between a data model object (DMO) and its fields. For example, the Individual.Id field has a one-to-many
relationship (1:M) with the ContactPointEmail.PartyId field.

Flow
Represents the metadata associated with a flow. With Flow, you can create an application that navigates users through a series of
pages to query and update records in the database. You can also execute logic and provide branching capability based on user input
to build dynamic applications.

Flow Category
Represents a list of flows that are grouped by category.


Second-Generation Managed Packages Components Available in Second-Generation Managed
Packages

Flow Definition
Represents the flow definition’s description and active flow version number.

Flow Test
Represents the metadata associated with a flow test. Before you activate a record-triggered flow, you can test it to verify its expected
results and identify flow run-time failures.

Folder
Represents a folder.

Fuel Type
Represents a custom fuel type in an org.

Fuel Type Sustainability Unit of Measure
Represents a mapping between the custom fuel types and their corresponding unit of measure (UOM) values defined by a customer
in an org.

Fundraising Config
Represents a collection of settings to configure the fundraising product.

Gateway Provider Payment Method Type
Represents an entity that allows integrators and payment providers to choose an active payment to receive an order's payment data
rather than allowing the Salesforce Order Management platform to select a default payment method.

Gen Ai Planner Bundle
Represents a planner for an agent or agent template. It’s a container for all the topics and actions used to interact with a large
language model (LLM).

Generative AI Prompt Template
Represents a generative AI prompt template, for use in Agentforce.

Global Picklist
Represents the metadata for a global picklist value set, which is the set of shared values that custom picklist fields can use. A global
value set isn’t a field itself. In contrast, the custom picklist fields that are based on a global picklist are of type ValueSet.

Home Page Component
Represents the metadata associated with a home page component. You can customize the Home tab in Salesforce Classic to include
components such as sidebar links, a company logo, a dashboard snapshot, or custom components that you create. Use to create,
update, or delete home page component definitions.

Home Page Layout
Represents the metadata associated with a home page layout. You can customize home page layouts and assign the layouts to
users based on their user profile.

Identity Verification Proc Def
Represents the definition of the identity verification process.

Inbound Network Connection
Represents a private connection between a third-party data service and a Salesforce org. The connection is inbound because the
callouts are coming into Salesforce.

IndustriesEinsteinFeatureSettings
Represents the settings for enabling the Industries Einstein feature.

IntegrationProviderDef
Represents an integration definition associated with a service process. Stores data for the Industries: Send Apex Async Request and
Industries: Send External Async Request invocable actions.


Second-Generation Managed Packages Components Available in Second-Generation Managed
Packages

Invocable Action Extension
Represents extended metadata for Apex classes that are used as invocable actions or data types. This allows developers to specify
how to present the action's inputs without writing custom code.

LearningAchievementConfig
Represents the mapping details between a Learning Achievement type and a Learning Achievement record type.

Learning Item Type
Represents a custom exercise type that an Enablement user takes in an Enablement program in the Guidance Center. A custom
exercise type also requires a corresponding LearningItem record for the Guidance Center and corresponding EnblProgramTaskDefinition
and EnblProgramTaskSubCategory records for when admins create a program in Program Builder.

Letterhead
Represents formatting options for the letterhead in an email template. A letterhead defines the logo, page color, and text settings
for your HTML email templates. Use letterheads to ensure a consistent look and feel in your company’s emails.

Life Science Config Category
Represents the category that a Life Sciences configuration record is organized into.

Life Science Config Record
Represents a configuration record for Life Sciences. This object is a child of Life Science Config Category.

Lightning Bolt
Represents the definition of a Lightning Bolt Solution, which can include custom apps, flow categories, and Experience Builder
templates.

Lightning Message Channel
Represents the metadata associated with a Lightning Message Channel. A Lightning Message Channel represents a secure channel
to communicate across UI technologies, such as Lightning Web Components, Aura Components, and Visualforce.

Lightning Page
Represents the metadata associated with a Lightning page. A Lightning page represents a customizable screen made up of regions
containing Lightning components.

Lightning Type
Represents a custom Lightning type. Use this type to override the default user interface to create a customized appearance based
on your business requirements. Deploy this bundle to your organization to implement the overrides.

Lightning Web Component
Represents a Lightning web component bundle. A bundle contains Lightning web component resources.

List View
ListView allows you to see a filtered list of records, such as contacts, accounts, or custom objects.

Live Chat Sensitive Data Rule
Represents a rule for masking or deleting data of a specified pattern. Written as a regular expression (regex). Use this object to mask
or delete data of specified patterns, such as credit card, social security, or phone and account numbers.

Loyalty Program Setup
Represents the configuration of a loyalty program process including its parameters and rules. Program processes determine how
new transaction journals are processed. When new transaction journals meet the criteria and conditions for a program process,
actions that are set up in the process are triggered for the transaction journals.

Managed Content Type
Represents the definition of custom content types for use with Salesforce CMS. Custom content types are displayed as forms with
defined fields.


Second-Generation Managed Packages Components Available in Second-Generation Managed
Packages

Marketing App Extension
Represents an integration with a third-party app or service that generates prospect external activity.

Marketing App Extension Activity
Represents an Activity Type, which is a prospect activity that occurs in a third-party app and can be used in Account Engagement
automations.

Market Segment Definition
Represents the field values for MarketSegmentDefinition. MarketSegmentDefinition is used to store the exportable metadata of a
segment, such as segment criteria and other attributes. Developers can create segment definition packages, pass segment definition
in the form of data build tool (DBT), and publish it on AppExchange for subscriber organizations to install and instantiate these
segments.

MktCalculatedInsightsObjectDef
Represents Calculated Insight definition such as expression.

MktDataConnection
Represents the connection information of an external connector that can ingest data to Data Cloud, read data from the source, or
write data to the source in Data Cloud.

MktDataTranObject
An entity that is used to deliver (aka transport) information from the source to a target (target will be called a landing entity).This
can be the schema of a file, API, Event, or other means of transporting data, such as SubscriberFile1.csv, or SubscriberCDCEvent.

Named Credential
Represents a named credential, which specifies the URL of a callout endpoint and its required authentication parameters in one
definition. A named credential can be specified as an endpoint to simplify the setup of authenticated callouts.

Object Source Target Map
Contains the object-level mappings between the source and the target objects. The source and target objects can be an
MktDataLakeObject or an MktDataModelObject. For example, an Email source object can be mapped to the ContactPointEmail
object.

Object Integration Provider Definition Mapping
Maps structured, logical data nodes in a context definition to actual Salesforce object fields or external data sources

OcrSampleDocument
Represents the details of a sample document or a document type that's used as a reference while extracting and mapping information
from a customer form.

OcrTemplate
Represents the details of the mapping between a form and a Salesforce object using Intelligent Form Reader.

Outbound Network Connection
Represents a private connection between a Salesforce org and a third-party data service. The connection is outbound because the
callouts are going out of Salesforce.

Page Layout
Represents the metadata associated with a page layout.

Path Assistant
Represents Path records.

Payment Gateway Provider
Represents the metadata associated with a payment gateway provider.


Second-Generation Managed Packages Components Available in Second-Generation Managed
Packages

Permission Set
Represents a set of permissions that's used to grant more access to one or more users without changing their profile or reassigning
profiles. You can use permission sets to grant access but not to deny access.

Permission Set Groups
Represents a group of permission sets and the permissions within them. Use permission set groups to organize permissions based
on job functions or tasks. Then, you can package the groups as needed.

Platform Cache
Represents a partition in the Platform Cache.

Platform Event Channel
Represents a channel that you can subscribe to in order to receive a stream of events.

Platform Event Channel Member
Represents an entity selected for Change Data Capture notifications on a standard or custom channel, or a platform event selected
on a custom channel.

Platform Event Subscriber Configuration
Represents configuration settings for a platform event Apex trigger, including the batch size, the trigger’s running user, and parallel
subscription settings.

Pricing Action Parameters
Represents a pricing action associated to a context definition and a pricing procedure.

Pricing Recipe
Represents one out of various data models or sets of entities of a particular cloud that'll be consumed by the pricing data store during
design and run time.

Procedure Output Resolution
Represents the pricing resolution for an pricing element determined using strategy name and formula.

Process
Use Flow instead.

Process Flow Migration
Represents a process's migrated criteria and the resulting migrated flow.

Product Attribute Set
Represents the ProductAttribute information being used as and attribute such as color_c, size_c .

Product Specification Type
Represents the type of product specification provided by the user to make the product terminology unique to an industry. A product
specification type is associated with a product specification record type.

Product Specification Record Type
Represents the relationship between industry-specific product specifications and the product record type.

Prompts (In-App Guidance)
Represents the metadata related to in-app guidance, which includes prompts and walkthroughs.

Quick Action
Represents a specified create or update quick action for an object that then becomes available in the Chatter publisher.

Recommendation Strategy
Represents a recommendation strategy. Recommendation strategies are applications, similar to data flows, that determine a set of
recommendations to be delivered to the client through data retrieval, branching, and logic operations.


Second-Generation Managed Packages Components Available in Second-Generation Managed
Packages

Record Action Deployment
Represents configuration settings for the Actions & Recommendations, Action Launcher, and Bulk Action Panel components.

Record Alert Data Source Expression Set Definition
Represents information about the data source for a record alert and the association with an expression set definition.

Record Type
Represents the metadata associated with a record type. Record types let you offer different business processes, picklist values, and
page layouts to different users. Use this metadata type to create, update, or delete record type definitions for a custom object.

RedirectWhitelistUrl
Represents a trusted URL that’s excluded from redirection restrictions when the redirectionWarning or redirectBlockModeEnabled
field on the SessionSettings Metadata type is set to true.

Referenced Dashboard
Represents the ReferencedDashboard object in CRM Analytics. A referenced dashboard stores information about an externally
referenced dashboard.

Registered External Service
Represents a registered external service, which provides an extension or integration.

RelationshipGraphDefinition
Represents a definition of a graph that you can configure in your organization to traverse object hierarchies and record details, giving
you a glimpse of how your business works.

Remote Site Setting
Represents a remote site setting.

Report
Represents a custom report.

Report Type
Represents the metadata associated with a custom report type. Custom report types allow you to build a framework from which
users can create and customize reports.

ServiceProcess
Represents a process created in Service Process Studio and its associated attributes.

Slack App (Beta)
Represents a Slack app.

Service Catalog Category
Represents the grouping of individual catalog items in Service Catalog.

Service Catalog Filter Criteria
Represents an eligibility rule that determines if a Service Catalog user has access to a catalog item.

Service Catalog Item Definition
Represents the entity associated with a specific, individual service available in the Service Catalog.

Service Catalog Fulfillment Flow
Represents the flow associated with a specific catalog item in the Service Catalog.

Stationary Asset Environmental Source Record Type Configuration
Represents the setup object that contains the mapping between the Stationary Asset Environmental Source record type and internal
enums. You can primarily use this object for calculations across different record types.


Second-Generation Managed Packages Components Available in Second-Generation Managed
Packages

Static Resource
Represents a static resource file, often a code library in a ZIP file.

Streaming App Data Connector
Represents the connection information specific to Web and Mobile Connectors.

Sustainability UOM
Represents information about the additional unit of measure values defined by a customer.

Sustainability UOM Conversion
Represents information about the unit of measure conversion for the additional fuel types defined by a customer.

Timeline Object Definition
Represents the container that stores the details of a timeline configuration. You can use this resource with Salesforce objects to see
their records' related events in a linear time-sorted view.

Timesheet Template
Represents a template for creating time sheets in Field Service.

Transaction Processing Type
Represents the processing constraint settings for a transaction processing request.

Translation
Add translations to your managed packages.

UI Object Relation Config
Represents the admin-created configuration of the object relation UI component.

User Access Policy
Represents a user access policy.

Validation Rule
Represents a validation rule, which is used to verify that the data a user enters in a record is valid and can be saved.

Vehicle Asset Emissions Source Record Type Configuration
Represents the setup object that contains the mapping between the Vehicle Asset Emissions Source record type and internal enums.
You can primarily use this object for calculations across different record types.

View Definition (Beta)
Represents a view definition on a Slack app.

Virtual Visit Config
Represents an external video provider configuration, which relays events from Salesforce to the provider.

Visualforce Component
Represents a Visualforce component.

Visualforce Page
Represents a Visualforce page.

Wave Analytic Asset Collection
A collection of CRM Analytics assets.

Wave Application
A CRM Analytics application.

Wave Component
A CRM Analytics dashboard component.


### Second-Generation Managed Packages Account Plan Objective Measure Calculation Definition

Wave Dataflow
A CRM Analytics data prep dataflow.

Wave Dashboard
A CRM Analytics dashboard.

Wave Dataset
A CRM Analytics dataset.

Wave Lens
A CRM Analytics lens.

Wave Recipe
A CRM Analytics data prep recipe.

Wave Template Bundle
A CRM Analytics template bundle.

Wave Xmd
The extended metadata for CRM Analytics dataset fields and their formatting for dashboards and lenses.

Web Store Template
Represents a configuration for creating commerce stores.

Workflow Alert
WorkflowAlert represents an email alert associated with a workflow rule.

Workflow Field Update
WorkflowFieldUpdate represents a workflow field update.

Workflow Knowledge Publish
WorkflowKnowledgePublish represents Salesforce Knowledge article publishing actions and information.

Workflow Outbound Message
WorkflowOutboundMessage represents an outbound message associated with a workflow rule.

Workflow Rule
This metadata type represents a workflow rule.

Workflow Task
This metadata type references an assigned workflow task.

### Account Plan Objective Measure Calculation Definition

Represents the definition of a target object, rollup field, and logic for calculating the current value of a sales account plan objective
measure.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes


### Second-Generation Managed Packages Account Relationship Share Rule

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** None

Both Package Developer and Subscriber Can Edit

**•** Description, DeveloperName, MasterLabel, RollupType, Status, TargetField, TargetObject

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: AccountPlanObjMeasCalcDef

Component Type in 1GP Package Manager UI: Account Plan Objective Measure Calculation Definition

**Documentation**

[Sales Account Plan Objectives, Measures, and Calculation Definitions](https://help.salesforce.com/s/articleView?id=sales.account_plans_objective_measures.htm&type=5&language=en_US)

### Account Relationship Share Rule

Determines which object records are shared, how they’re shared, the account relationship type that shares the records, and the level of
access granted to the records.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit


### Second-Generation Managed Packages Action Link Group Template

**•** Name

**•** Developer Name

**•** Description

**•** Account Relationship Type

**•** Access Level

**•** Object Type

**•** Account to Criteria Field

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: AccountRelationshipShareRule

**Use Case**
To share data between external accounts.

**License Requirements**
Orgs with Digital Experiences enabled can use this package.

**Documentation**
_Salesforce Help:_ [Account Relationships and Account Relationship Data Sharing Rules](https://help.salesforce.com/s/articleView?id=platform.networks_partner_account_relationships_and_sharing.htm&type=5&language=en_US)

### Action Link Group Template

Represents the action link group template. Action link templates let you reuse action link definitions and package and distribute action
links.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes. Supported in both 1GP and 2GP packages.

Component Has IP Protection No


### Second-Generation Managed Packages Action Plan Template

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** None

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: ActionLinkGroupTemplate

Component Type in 1GP Package Manager UI: Action Link Group Template

**Documentation**
_Salesforce Help:_ [Action Link Templates](https://help.salesforce.com/s/articleView?id=platform.action_link_group_template.htm&type=5&language=en_US)

### Action Plan Template

Represents an instance of an action plan template.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: First-Generation Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)


### Second-Generation Managed Packages Actionable List Definition

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** All attributes

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: ActionPlanTemplate

**Documentation**
_Salesforce Help:_ [Action Plans](https://help.salesforce.com/s/articleView?id=ind.fsc_action_plans.htm&type=5&language=en_US)

### Actionable List Definition

Represents the data source definition details associated with an actionable list.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes. Supported in both 1GP and 2GP packages.

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** All attributes

Both Package Developer and Subscriber Can Edit


### Second-Generation Managed Packages Actionable List Key Performance Indicator Definition

**•** None

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: ActionableListDefinition

Component Type in 1GP Package Manager UI: ActionableListDefinition

**Documentation**
_Salesforce Help:_ [Actionable Segmentation](https://help.salesforce.com/s/articleView?id=ind.actionable_segmentation.htm&type=5&language=en_US)

### Actionable List Key Performance Indicator Definition

Represents the custom key performance indicators that are defined for a specific field in an object.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org Yes

Package Developer Can Remove Component From Package Yes, Supported in both 1GP and 2GP packages.

Component Has IP Protection No

[To confirm whether this component is available in managed 1GP, managed 2GP, or both package types, see Metadata Coverage Report.](https://developer.salesforce.com/docs/success/metadata-coverage-report/references/coverage-report/metadata-coverage-report.html)

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** All attributes

Both Package Developer and Subscriber Can Edit

**•** All attributes

Neither Package Developer or Subscriber Can Edit


### Second-Generation Managed Packages Activation Platform

**•** None

More Information

**Feature Name**
Metadata Name: ActnblListKeyPrfmIndDef

Component Type in 1GP Package Manager UI: ActnblListKeyPrfmIndDef

**License Requirements**
Actionable Segmentation

**Documentation**
_Salesforce Help:_ [Create Custom Key Performance Indicators](https://help.salesforce.com/s/articleView?id=ind.create_custom_kpis.htm&type=5&language=en_US)

_Salesforce Help:_ [ActnblListKeyPrfmIndDef](https://developer.salesforce.com/docs/atlas.en-us.262.0.industries_reference.meta/industries_reference/sforce_api_objects_actnbllistkeyprfminddef.htm)

### Activation Platform

Represents the ActivationPlatform configuration, such as platform name, delivery schedule, output format, and destination folder.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: First-Generation Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** DataConnector

**•** Description

**•** LogoUrl

**•** MasterLabel

**•** OutputFormat

**•** RefreshMode


Second-Generation Managed Packages Activation Platform

**•** Type

Both Package Developer and Subscriber Can Edit

**•** Enabled (only subscriber editable)

**•** IncludeSegmentNames (only subscriber editable)

Neither Package Developer or Subscriber Can Edit

**•** ID

**•** OutputGrouping

**•** PeriodicRefreshFrequency

**•** RefreshFrequency

More Information

**Feature Name**
Metadata Name: ActivationPlatform

Component Type in 1GP Package Manager UI: ActivationPlatform

**Use Case**
Allows ISVs to specify capabilities of their Activation Platform integrations and publish it on AppExchange for subscriber organizations
to install and instantiate instances of the platform as a disparate activation target.

**Considerations When Packaging**
Some upgrade scenarios are not support:

**•** Adding a new required field

**•** Removing a previously supported ID type

**•** Removing a previously supported optional field or required field

**•** Changing a previously supported field property from optional to required

Some update scenarios are supported and don't automatically cascade to Activation Target or Activations created before the upgrade
installations:

**•** Adding a new ID type

**•** Adding of a new optional field

**•** Adding a new hidden field

**•** Value change on a previously supported hidden field

To apply updates to future Activation run jobs, the user must edit and resave all Activation Targets created before the upgrade.
Developers provide post-install instructions informing the subscriber of this required action anytime a change is made in a new
version release.

**License Requirements**
Data Cloud enabled orgs can access this package.

**Post Install Steps**
An admin from the subscriber org enables the activation platform to start using this platform in Activation creations.

**Documentation**
_Metadata API Developer Guide:_ [ActivationPlatform](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_activationplatform.htm)


### Second-Generation Managed Packages AffinityScoreDefinition AffinityScoreDefinition

Represents the affinity information used in calculations to analyze and categorize contacts for marketing purposes.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** AffinityScoreType

**•** NumberOfMonths

**•** NumberOfRanges

**•** SourceFieldApiNameList

**•** TargetFieldApiNameList

**•** ScoreRangeList

Both Package Developer and Subscriber Can Editv

**•** None

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: AffinityScoreDefinition

**Documentation**

**•** _Fundraising Metadata API Types_ [: AffinityScoreDefinitions](https://developer.salesforce.com/docs/atlas.en-us.262.0.nonprofit_cloud.meta/nonprofit_cloud/fundraising_affinityscoredefinition_metadata_api.htm)


### Second-Generation Managed Packages Agent Action

**•** _Salesforce Help_ [: Set Up RRM Scoring](https://help.salesforce.com/s/articleView?id=sfdo.npc_fr_set_up_configure_fundraising.htm&language=en_US)

**•** _Salesforce Help_ [: Scoring Frameworks Help Increase Fundraising Success](https://help.salesforce.com/s/articleView?id=sfdo.npc_fr_scoring_frameworks_help_increase_fundraising_success.htm&language=en_US)

### Agent Action

Represents an action, for use in Agentforce.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes

Component Has IP Protection No (However, actions can incorporate flows or Apex code that do
have IP protection.)

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** Description

**•** IsConfirmationRequired

**•** MasterLabel

Action Input Fields:

**•** CopilotAction.IsUserInput

**•** Description

**•** IsPII

**•** Properties (Inherited from invocationTarget like flows or Apex code.)

**•** Title (Inherited from invocationTarget like flows or Apex code.)

**•** Required

**•** Lightning.Type

Action Output Fields:

**•** Description


### Second-Generation Managed Packages Agent Topic

**•** CopilotAction.IsDisplayable

**•** IsPII

**•** CopilotAction.IsUsedByPlanner

**•** Properties (Inherited from invocationTarget like flows or Apex code.)

**•** Title (Inherited from invocationTarget like flows or Apex code.)

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** DeveloperName

**•** InvocationTarget

**•** InvocationTargetType

More Information

**Feature Name**
[Metadata Name: GenAiFunction](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_genaifunction.htm)

Component Type in 1GP Package Manager UI: Generative AI Function Definition

**Use Case**
Provide actions that customers can add to their own topics and agents.

**Considerations When Packaging**

When creating an Agent Action of type Apex, the Apex class, invocable Apex method, and any invocable Apex variables must all be
marked as `global` . If any of these are public or private, the Apex method won't appear in the list of options to add to the Agent
Action, and won't be invoked by an Agent at runtime.

**Documentation**
_Salesforce Help:_ [Agentforce Agents](https://help.salesforce.com/s/articleView?id=ai.copilot_intro.htm&type=5&language=en_US)

_Salesforce Help:_ [Agentforce Actions](https://help.salesforce.com/s/articleView?id=ai.copilot_actions.htm&language=en_US)

_Metadata API Developer Guide:_ [GenAiFunction](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_genaifunction.htm)

### Agent Topic

Represents a topic, for use in Agentforce.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes


### Second-Generation Managed Packages AI Application

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** Description

**•** MasterLabel

**•** Scope

**•** AiPluginUtterances

**•** GenAiFunctions

**•** GenAiPluginInstructions

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** DeveloperName

**•** PluginType

More Information

**Feature Name**
[Metadata Name: GenAiPlugin](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_genaiplugin.htm)

Component Type in 1GP Package Manager UI: Generative AI Plugin Definition

**Use Case**
Provide topics that customers can add to their own agents. Actions can be added to topics.

**Considerations When Packaging**

Subscribers can't edit which actions are associated with a managed-installed topic. Instead, subscribers must manually create a copy
of the topic and then assign actions to their copy of the topic. We're working to improve this experience.

**Documentation**
_Salesforce Help:_ [Agentforce Agents](https://help.salesforce.com/s/articleView?id=ai.copilot_intro.htm&type=5&language=en_US)

_Salesforce Help:_ [Agentforce Topics](https://help.salesforce.com/s/articleView?id=ai.copilot_topics.htm&language=en_US)

### AI Application

Represents an instance of an AI application. For example, Einstein Prediction Builder.


### Second-Generation Managed Packages AI Application Config

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** Type

Both Package Developer and Subscriber Can Edit

**•** Status

**•** ExternalId

**•** MlExternalId

Neither Package Developer or Subscriber Can Edit

**•** Name

More Information

**Feature Name**
Metadata Name: AIApplication

**Considerations When Packaging**

AIApplication is the parent entity for all Einstein configuration entities. Packaging of Einstein features must always begin with the
selection of one or more AIApplications. To create a package with ML Prediction Definition, select the parent AIApplication (Type =
PredictionBuilder). To create a package with ML Recommendation Definition, select the parent AIApplication (Type =
RecommendationBuilder). Packaging automatically analyzes the relationships and includes the associated MLPredictionDefinitions,
MLRecommendationDefinitions, and MLDataDefinitions necessary to fully define the Einstein configuration.

**Documentation**
_Metadata API Developer Guide:_ [AIApplication](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_aiapplication.htm)

_Salesforce Help:_ [Einstein Prediction Builder](https://help.salesforce.com/s/articleView?id=sales.custom_ai_prediction_builder_lm.htm&type=5&language=en_US)

_Salesforce Help:_ [Einstein Recommendation Builder](https://help.salesforce.com/s/articleView?id=sales.custom_ai_recommendation_builder.htm&type=5&language=en_US)

### AI Application Config

Represents additional prediction information related to an AI application.


Second-Generation Managed Packages AI Application Config

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** AIApplicationId

Both Package Developer and Subscriber Can Edit

**•** Rank

**•** IsInsightReasonEnabled

**•** IsInsightReasonEnabled

**•** AIScoringMode

**•** ExternalId

Neither Package Developer or Subscriber Can Edit

**•** Name

More Information

**Feature Name**
Metadata Name: AIApplicationConfig

**Considerations When Packaging**

AIApplicationConfig is always associated with an AIApplication. Packaging of Einstein features must always begin with the selection
of one or more AIApplications. To create a package with AI Application Config, select the parent AIApplication. Packaging automatically
analyzes the relationships and includes the associated MLApplicationConfig, MLPredictionDefinition, MLRecommendationDefinitions,
and MLDataDefinitions necessary to fully define the Einstein configuration.

**Documentation**
_Metadata API Developer Guide:_ [AIApplicationConfig](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_aiapplicationconfig.htm)

_Salesforce Help:_ [Einstein Prediction Builder](https://help.salesforce.com/s/articleView?id=sales.custom_ai_prediction_builder_lm.htm&type=5&language=en_US)

_Salesforce Help:_ [Einstein Recommendation Builder](https://help.salesforce.com/s/articleView?id=sales.custom_ai_recommendation_builder.htm&type=5&language=en_US)


### Second-Generation Managed Packages AIUsecaseDefinition AIUsecaseDefinition

Represents a collection of fields in a Salesforce org used to define a machine learning use case and get real-time predictions.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** All the AIUsecaseDefinition fields

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: AIUsecaseDefinition

Component Type in 1GP Package Manager UI: AIUsecaseDefinition

**Use Case**
AI Usecase Definition lets you ship data that can be used to set up use cases for which you want to generate real-time predictions.
This data includes machine learning models and feature extractors required to generate the real-time predictions.

**License Requirements**
This feature is available with the CRM Plus license and the use case-related product’s CRM license.

**Documentation**
_Industries Common Resources Developer Guide_ [: AI Accelerator](https://developer.salesforce.com/docs/atlas.en-us.262.0.industries_reference.meta/industries_reference/ai_accelerator.htm)


### Second-Generation Managed Packages Analytics

_Salesforce Help_ [: AI Accelerator](https://help.salesforce.com/s/articleView?id=ind.ai_accelerator.htm&type=5&language=en_US)

### Analytics Analytics components include analytics applications, dashboards, dataflows, datasets, lenses, recipes, and user XMD.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade

Yes (Analytics Dataflow only).

All other analytics components can’t be updated.

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package

Yes (Analytic snapshot only). Supported in managed 2GP packages
only.

All other analytics components can’t be removed.

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

[For more details on 2GP component removal, see Remove Metadata Components from Second-Generation Managed Packages.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_remove_md_components.htm)

More Information

[To include analytics components in a managed 2GP package, include EinsteinAnalyticsPlus in your scratch org definition file.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_scratch_orgs_def_file_config_values.htm#so_einsteinanalyticsplus)

[To enable analytics in a 1GP packaging org, see Basic CRM Analytics Platform Setup in Salesforce Help.](https://help.salesforce.com/s/articleView?id=analytics.bi_help_setup_basic.htm&type=5&language=en_US)

[For more details, see CRM Analytics Packaging Considerations.](https://help.salesforce.com/s/articleView?id=analytics.bi_packaging_considerations.htm&type=5&language=en_US)

### Analytics Visualization

Represents a Tableau Next visualization.

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: First-Generation Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes


### Second-Generation Managed Packages Analytics Workspace

Subscriber Can Delete Component From Org Yes

Package Developer Can Remove Component From Package Yes

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** Label

Both Package Developer and Subscriber Can Edit

**•** Description

Neither Package Developer or Subscriber Can Edit

**•** Full Name

**•** Is Original

**•** Version

More Information

**Feature Name**
Metadata Name: AnalyticsVisualization

Component Type in 1GP Package Manager UI: Analytics Visualization

**License Requirements**
Tableau Next Admin or Tableau Next Analyst permission sets

**Documentation**
[For more information on Tableau Next visualizations, see Build Insightful Visualizations in Tableau Next in](https://help.salesforce.com/s/articleView?id=analytics.tua_create_viz.htm&language=en_US) _Salesforce Help_ .

### Analytics Workspace

Represents a Tableau Next workspace.

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: First-Generation Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org Yes

Package Developer Can Remove Component From Package Yes

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit


### Second-Generation Managed Packages Apex Class

**•** Label

Both Package Developer and Subscriber Can Edit

**•** Description

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: AnalyticsWorkspace

Component Type in 1GP Package Manager UI: Analytics Workspace

**License Requirements**
Tableau Next Admin or Tableau Next Analyst permission sets

**Documentation**
[For more information on Tableau Next workspaces, see Tableau Next Workspaces in](https://help.salesforce.com/s/articleView?id=analytics.tua_workspace.htm&language=en_US) _Salesforce Help_ .

### Apex Class

Represents an Apex Class. An Apex class is a template or blueprint from which Apex objects are created. Classes consist of other classes,
user-defined methods, variables, exception types, and static initialization code.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package

Yes (if not set to `global` access).

Supported in both 1GP and 2GP packages.

Component Has IP Protection Yes

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

[For more details on 2GP component removal, see Remove Metadata Components from Second-Generation Managed Packages.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_remove_md_components.htm)


Second-Generation Managed Packages Apex Class

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** API Version

**•** Code

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** Name

More Information

**Feature Name**
Metadata Name: ApexClass

Component Type in 1GP Package Manager UI: Apex Class

**Considerations When Packaging**

**•** Any Apex that is included as part of a package must have at least 75% cumulative test coverage. Each trigger must also have
some test coverage. When you upload your package to AppExchange, all tests are run to ensure that they run without errors. In
addition, all tests are run when the package is installed in the installer’s org. If any test fails, the installer can decide whether to
install the package.

**•** Managed packages receive a unique namespace. This namespace is prepended to your class names, methods, variables, and so
on, which helps prevent duplicate names in the installer’s org.

**•** In a single transaction, you can only reference 10 unique namespaces. For example, suppose that you have an object that executes
a class in a managed package when the object is updated. Then that class updates a second object, which in turn executes a
different class in a different package. Even though the first package didn’t access the second package directly, the access occurs
in the same transaction. It’s therefore included in the number of namespaces accessed in a single transaction.

**•** If you’re exposing any methods as Web services, include detailed documentation so that subscribers can write external code
that calls your Web service.

**•** If an Apex class references a custom label and that label has translations, explicitly package the individual languages desired to
include those translations in the package.

**•** If you reference a custom object’s sharing object (such as MyCustomObject__share) in Apex, you add a sharing model dependency
to your package. Set the default org-wide access level for the custom object to Private so other orgs can install your package
successfully.

**•** The code contained in an Apex class, trigger, or Visualforce component that’s part of a managed package is obfuscated and
can’t be viewed in an installing org. The only exceptions are methods declared as global. You can view global method signatures
in an installing org. In addition, License Management Org users with the View and Debug Managed Apex permission can view
their packages’ obfuscated Apex classes when logged in to subscriber orgs via the Subscriber Support Console.

**•** You can use the `deprecated` annotation in Apex to identify `global` methods, classes, exceptions, enums, interfaces, and
variables that can’t be referenced in later releases of a managed package. So you can refactor code in managed packages as the
requirements evolve. After you create another package version as Managed - Released, new subscribers that install the latest
package version can’t see the deprecated elements, while the elements continue to function for existing subscribers and API
integrations.

**•** Apex code that refers to Data Categories can’t be uploaded.


### Second-Generation Managed Packages Apex Sharing Reason

**•** Before deleting Visualforce pages or global Visualforce components from your package, remove all references to public Apex
classes and public Visualforce components. After removing the references, upgrade your subscribers to an interim package
version before you delete the page or global component.

**Usage Limits**
[The maximum number of class and trigger code units in a deployment of Apex is 7500. For more information, see Execution Governors](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_gov_limits.htm)
[and Limits in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_gov_limits.htm) _Apex Developer Guide_ .

**Documentation**
_Second-Generation Managed Packaging Developer Guide:_ [Namespace-Based Visibility for Apex Classes in Second-Generation Managed](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_namespace_visibility.htm)
[Packages](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_namespace_visibility.htm)

_First-Generation Managed Packaging Developer Guide:_ [About API and Dynamic Apex Access in Packages](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/about_client_security_profile.htm)

_First-Generation Managed Packaging Developer Guide:_ [Using Apex in Group and Professional Editions](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/dev_packages_apex_ge_pe.htm)

### Apex Sharing Reason

Represents an Apex sharing reason, which is used to indicate why sharing was implemented for a custom object.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** Reason Label

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** Reason Name

More Information

**Feature Name**
Metadata Name: SharingReason

Component Type in 1GP Package Manager UI: Apex Sharing Reason


### Second-Generation Managed Packages Apex Trigger

**Considerations When Packaging**
Apex sharing reasons can be added directly to a package, but are only available for custom objects.

**Documentation**
_Metadata API Developer Guide_ [: SharingReason](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_apexsharingreason.htm)

### Apex Trigger

Represents an Apex trigger. A trigger is Apex code that executes before or after specific data manipulation language (DML) events occur,
such as before object records are inserted into the database, or after records have been deleted.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes. Supported in both 1GP and 2GP packages.

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

[For more details on 2GP component removal, see Remove Metadata Components from Second-Generation Managed Packages.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_remove_md_components.htm)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** API Version

**•** Code

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** Name

More Information

**Feature Name**
Metadata Name: ApexTrigger


### Second-Generation Managed Packages App Framework Template Bundle

Component Type in 1GP Package Manager UI: Apex Trigger

**Documentation**
_Apex Developer Guide:_ [Triggers](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_triggers.htm)

### App Framework Template Bundle

Represents the app framework template bundle. Use these templates for Data Cloud and Tableau Next assets.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org Yes

Package Developer Can Remove Component From Package Yes

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** Label

**•** MaxAppCount

Both Package Developer and Subscriber Can Edit

**•** Description

**•** TemplateBadgeIcon

Neither Package Developer or Subscriber Can Edit

**•** AssetVerion

**•** TemplateType

More Information

**Feature Name**
Metadata Name: AppFrameworkTemplateBundle

Component Type in 1GP Package Manager UI: App Framework Template Bundle

**Considerations When Packaging**
Data Cloud and Tableau Next assets are installed in subscriber orgs via templates using the AppFrameworkTemplateBundle. The
template framework supports the data sync and orchestration needed for visualization assets, along with customizations for each
org.


### Second-Generation Managed Packages Application Subtype Definition

**License Requirements**
Tableau Included App Manager permission set

### Application Subtype Definition

Represents a subtype of an application within an application domain.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade No

Subscriber Can Delete Component From Org Yes

Package Developer Can Remove Component From Package Yes

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** None

Both Package Developer and Subscriber Can Edit

**•** Label

**•** Developer Name

**•** Description

**•** Application Usage Type

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: ApplicationSubtypeDefinition

**Documentation**
_Industries Common Resources Developer Guide:_ **[AssessmentSubtypeDefinition](https://developer.salesforce.com/docs/atlas.en-us.262.0.industries_reference.meta/industries_reference/tooling_api_objects_applicationsubtypedefinition.htm)**


### Second-Generation Managed Packages AssessmentConfiguration AssessmentConfiguration

Represents a configuration for Assessment component. An AssessmentConfiguration entry indicates configuration for user flows such
as sending out emails or reminder actions on assessments initiated by the patient.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes. Supported in managed 1GP packages only.

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** All but DeveloperName

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** DeveloperName

More Information

**Feature Name**
Metadata Name: AssessmentConfiguration

Component Type in 1GP Package Manager UI: AssessmentConfiguration

**Documentation**
### Health Cloud Developer Guide:  AssessmentConfiguration AssessmentQuestion

Represents the container object that stores the questions required for an assessment.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.


### Second-Generation Managed Packages AssessmentQuestionSet

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** All except DeveloperName

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** DeveloperName

More Information

**Feature Name**
Metadata Name: AssessmentQuestion

**Documentation**
### Industries Common Resources Developer Guide: AssessmentQuestion AssessmentQuestionSet

Represents the container object for Assessment Questions.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No


### Second-Generation Managed Packages Aura Component

Package Developer Can Remove Component From Package Yes

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** All except DeveloperName

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** DeveloperName

More Information

**Feature Name**
Metadata Name: AssessmentQuestionSet

**Documentation**
_Industries Common Resources Developer Guide:_ **[AssessmentQuestionSet](https://developer.salesforce.com/docs/atlas.en-us.262.0.industries_reference.meta/industries_reference/meta_assessmentquestionset.htm)**

### Aura Component

Represents an Aura definition bundle. A bundle contains an Aura definition, such as an Aura component, and its related resources, such
as a JavaScript controller. The definition can be a component, application, event, interface, or a tokens collection.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

You can build Lightning components using two programming models: the Lightning Web Components model, and the original Aura
Components model.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes. Supported in both 1GP and 2GP packages.


### Second-Generation Managed Packages Batch Calc Job Definition

Component Has IP Protection No

When a package developer removes an Aura or Lightning web component from a package, the component remains in a subscriber’s
org after they install the upgraded package. The administrator of the subscriber’s org can delete the component, if desired. This behavior
is the same for a Lightning web component or an Aura component with a `public` or `global` access value.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** API Version

**•** Description

**•** Label

**•** Markup

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** Name

More Information

**Aura Component**
Metadata Name: AuraDefinitionBundle

Component Type in 1GP Package Manager UI: Aura Component Bundle

**Documentation**

[Lightning Aura Components Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.lightning.meta/lightning/)

### Batch Calc Job Definition

Represents a Data Processing Engine definition.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No


### Second-Generation Managed Packages Batch Process Job Definition

Component Has IP Protection Yes, except templates

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** Entire Data Processing Engine definition

Both Package Developer and Subscriber Can Edit

**•** Label

**•** Description

**•** Status

Neither Package Developer or Subscriber Can Edit

**•** API Name

**•** URL

More Information

**Feature Name**
Metadata Name: BatchCalcJobDefinition

Component Type in 1GP Package Manager UI: Batch Calculation Job Definition

**Use Case**
Data Processing Engine helps you transform data that's available in your Salesforce org and write back the transformation results as
new or updated records. You can transform the data for standard and custom objects using Data Processing Engine definitions.

**License Requirements**
Either Financial Services Cloud, Manufacturing Cloud, Loyalty Management, Net Zero Cloud, or Rebate Management

Data Pipelines

**Documentation**
_Salesforce Help:_ [Data Processing Engine](https://help.salesforce.com/s/articleView?id=ind.dpe_intro.htm&type=5&language=en_US)

### Batch Process Job Definition

Represents the details of a Batch Management job definition.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No


### Second-Generation Managed Packages Benefit Action

Package Developer Can Remove Component From Package No

Component Has IP Protection Yes, except templates

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** Entire Batch Management job

Both Package Developer and Subscriber Can Edit

**•** Label

**•** Description

**•** Status

Neither Package Developer or Subscriber Can Edit

**•** API Name

**•** URL

More Information

**Feature Name**
Metadata Name: BatchProcessJobDefinition

Component Type in 1GP Package Manager UI: Batch Process Job Definition

**Use Case**
Automate the processing of records in scheduled flows with Batch Management. With Batch Management, you can process a high
volume of standard and custom object records.

**License Requirements**
Either Loyalty Management, Manufacturing Cloud, or Rebate Management

System Administrator Profile

**Documentation**
_Salesforce Help:_ [Batch Management](https://help.salesforce.com/s/articleView?id=ind.concept_batch_management.htm&type=5&language=en_US)

### Benefit Action

Represents details of an action that can be triggered for a benefit.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes


### Second-Generation Managed Packages Bot Template

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection Yes, except templates

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** Entire Benefit Action record

Both Package Developer and Subscriber Can Edit

**•** Label

**•** Description

**•** Status

Neither Package Developer or Subscriber Can Edit

**•** API Name

**•** URL

More Information

**Feature Name**
Metadata Name: BenefitAction

Component Type in 1GP Package Manager UI: Benefit Action

**Use Case**
Benefit Actions are actions that can be triggered for a loyalty program benefit.

**License Requirements**
Loyalty Management permission set license

**Documentation**
_Salesforce Help:_ [Benefit Action](https://help.salesforce.com/s/articleView?id=xcloud.benefit_actions.htm&type=5&language=en_US)

### Bot Template

Represents the configuration details for a specific Einstein Bot template, including dialogs and variables.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org Yes


Second-Generation Managed Packages Bot Template

Package Developer Can Remove Component From Package Yes

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** Bot Dialog Groups

**•** Bot Dialogs

**•** Conversation Context Variables

**•** Conversation Languages

**•** Conversation Definition Goals

**•** Conversation System Dialogs

**•** Conversation Variables

**•** Description

**•** Entry Dialog

**•** Icon

**•** Main Menu Dialog

**•** Label

**•** MlDomain

**•** Rich Content Enabled

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: BotTemplate

Component Type in 1GP Package Manager UI: Bot Template

**Documentation**

[Salesforce Help: Create an Einstein Bot Template](https://help.salesforce.com/s/articleView?id=service.bots_service_create_new_template.htm&type=5&language=en_US)

[Salesforce Help: Create a Template from an Einstein Bot](https://help.salesforce.com/s/articleView?id=service.bots_service_create_template_bot.htm&type=5&language=en_US)

[Salesforce Help: Package an Einstein Bot Template](https://help.salesforce.com/s/articleView?id=service.bots_service_create_package_template.htm&type=5&language=en_US)

[Metadata API Developer Guide: BotTemplate](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_bottemplate.htm)


### Second-Generation Managed Packages Branding Set Branding Set

Represents the definition of a set of branding properties for an Experience Builder site, as defined in the Theme panel in Experience
Builder.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Note: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain terms
to avoid any effect on customer implementations.

Only Package Developer Can Edit

**•** brandingSetProperty

**•** description

**•** masterLabel

**•** type

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: BrandingSet

**Relationship to Other Components**
BrandingSet can’t be added to a package by itself. BrandingSet is included automatically in a package if it’s referenced by another
object in the package, such as CommunityThemeDefinition, LightningExperienceTheme, or EmbeddedServiceMenuSettings.

**Documentation**
_Salesforce Help_ [: Use Branding Sets in Experience Builder](https://help.salesforce.com/s/articleView?id=experience.community_designer_brandsets.htm&type=5&language=en_US)


### Second-Generation Managed Packages Briefcase Definition Briefcase Definition

Represents a briefcase definition. A briefcase makes selected records available for specific users and groups to view when they’re offline
in the Salesforce Field Service mobile app for iOS and Android.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** Entire briefcase

Both Package Developer and Subscriber Can Edit

**•** Active

Neither Package Developer or Subscriber Can Edit

**•** Full Name

More Information

**Feature Name**
Metadata Name: BriefcaseDefinition

Component Type in 1GP Package Manager UI: Briefcase Definition

**Considerations When Packaging**
As a best practice, package Briefcase Definition with IsActive set to false. If you package Briefcase Definition with IsActive set to true,
the package installation fails if installing the package exceeds any limits.

**Usage Limits**
[All Briefcase Builder limits apply to a Briefcase Definition package.](https://help.salesforce.com/s/articleView?id=xcloud.briefcase_builder_limits_considerations.htm&type=5&language=en_US)

**Relationship to Other Components**

After you install the package, assign the briefcase to the application that the briefcase's data is for.

**Documentation**
_Salesforce Help:_ [Briefcase Builder](https://help.salesforce.com/s/articleView?id=xcloud.briefcase_builder_overview.htm&type=5&language=en_US)


### Second-Generation Managed Packages Building Energy Intensity Record Type Configuration Building Energy Intensity Record Type Configuration

Represents the setup object that contains the mapping between the Building Energy Intensity Record record type and internal enums.
You can primarily use this object for calculations across different record types.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** All attributes

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: BldgEnrgyIntensityCnfg

Component Type in 1GP Package Manager UI: Building Energy Intensity Record Type Configuration

**Use Case**
You can use this component to build on top of the current Net Zero Cloud data model and carbon accounting capability to create
new stationary asset types for end users.

**License Requirements**

**•** Net Zero Cloud Growth license or Net Zero Cloud Starter license

**•** Net Zero Cloud Manager permissions set

**Post Install Steps**
Enable these org settings:

**•** Net Zero Cloud

**•** Manage Carbon Accounting

**•** Manage Building Energy Intensity


### Second-Generation Managed Packages Business Process

**Documentation**

**•** _Salesforce Help:_ [Set Up Record Types for Net Zero Cloud](https://help.salesforce.com/s/articleView?id=ind.netzero_setup_record_types.htm&type=5&language=en_US)

**•** _Salesforce Help:_ [Benchmark Building Energy Intensity Data](https://help.salesforce.com/s/articleView?id=ind.netzero_manager_manage_bei.htm&type=5&language=en_US)

### Business Process

The BusinessProcess metadata type enables you to display different picklist values for users based on their profile.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

Editable Properties After Package Promotion or Installation

**•** Only Package Developer Can EditNone

**•** Both Package Developer and Subscriber Can EditAll attributes

**•** Neither Package Developer or Subscriber Can EditNone

More Information

**Feature Name**
Metadata Name: BusinessProcess

**Use Case**
You can use this component to define different picklist values that you associate with record types.

**Relationship to Other Components**
Record types of corresponding entities.

**Documentation**
_Salesforce Help:_ [Tailor Business Processes to Different Users Using Record Types](https://help.salesforce.com/s/articleView?id=platform.customize_recordtype.htm&type=5&language=en_US)


### Second-Generation Managed Packages Business Process Group Business Process Group

Represents the surveys used to track customers’ experiences across different stages in their lifecycle.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** All Business Process Group fields including Business Process Definition and Business Process Feedback.

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** Developer Name

**•** Customer Satisfaction Metric

More Information

**Feature Name**
Metadata Name: BusinessProcessGroup

Component Type in 1GP Package Manager UI: Business Process Group

**Use Case**
### Business Process Group lets you ship groupings relevant to survey metrics that are captured as part of any purchase or product

lifecycle. For a specific business process group, you can define different stages and associate relevant questions from one or more
surveys for reporting purposes.

**License Requirements**
This feature is available with the Feedback Management - Growth license.

**Relationship to Other Components**
This feature can be used in conjunction with Surveys and Survey Invitation Rules Flow types, and their corresponding dependencies.

**Documentation**
_Metadata API Developer Guide_ [: BusinessProcessGroup](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_businessprocessgroup.htm)

_Salesforce Help_ [: Track Satisfaction Across a Customer's Lifecycle](https://help.salesforce.com/s/articleView?id=xcloud.task_customer_lifecycle_maps.htm&type=5&language=en_US)


### Second-Generation Managed Packages Business Process Type Definition Business Process Type Definition

Define the types of business processes that are applied to a rule.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade No

Subscriber Can Delete Component From Org Yes

Package Developer Can Remove Component From Package Yes

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** None

Both Package Developer and Subscriber Can Edit

**•** Label

**•** Developer Name

**•** Description

**•** Application Usage Type

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: BusinessProcessTypeDefinition

### Care Benefit Verify Settings

Represents the configuration settings for benefit verification requests.


Second-Generation Managed Packages Care Benefit Verify Settings

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** MasterLabel

**•** ServiceApexClass

**•** ServiceNamedCredential

**•** UriPath

**•** isDefault

**•** GeneralPlanServiceTypeCode

**•** ServiceTypeSourceSystem

**•** OrganizationName

**•** DefaultNpi

**•** CodeSetType

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** Name

More Information

**Feature Name**
Metadata Name: CareBenefitVerifySettings

Component Type in 1GP Package Manager UI: Care Benefit Verification Settings

**Use Case**
Provides out-of-the-box configuration settings for benefit verification requests in Health Cloud.

**License Requirements**
Industries Health Cloud

**Relationship to Other Components**
CareBenefitVerifySettings can contain ApexClass as well as NamedCredentials.


### Second-Generation Managed Packages Care Limit Type

**Documentation**
_Health Cloud Developer Guide_ [: CareBenefitVerifySettings](https://developer.salesforce.com/docs/atlas.en-us.262.0.health_cloud_object_reference.meta/health_cloud_object_reference/tooling_api_objects_carebenefitverifysettings.htm)

### Care Limit Type

Defines the characteristics of limits on benefit provision.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** LimitType

**•** MetricType

**•** MasterLabel

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** Name

More Information

**Feature Name**
Metadata Name: CareLimitType

Component Type in 1GP Package Manager UI: Care Limit Type

**Use Case**
Provide the characteristics of limits on benefit provision in Health Cloud.

**License Requirements**
Industries Health Cloud Add On or an org with a Health Cloud Financial Data Platform license

**Documentation**
_Health Cloud Developer Guide_ [: CareLimitType](https://developer.salesforce.com/docs/atlas.en-us.262.0.health_cloud_object_reference.meta/health_cloud_object_reference/tooling_api_objects_carelimittype.htm)


### Second-Generation Managed Packages Care Request Configuration Care Request Configuration

Represents the details for a record type such as service request, drug request, or admission request. One or more record types can be
associated with a care request.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** MasterLabel

**•** CareRequestType

**•** CareRequestRecordType

**•** CareRequestRecords

**•** IsDefaultRecordType

Both Package Developer and Subscriber Can Edit

**•** IsActive

Neither Package Developer or Subscriber Can Edit

**•** Name

More Information

**Feature Name**
Metadata Name: CareRequestConfiguration

Component Type in 1GP Package Manager UI: Care Request Configuration

**Use Case**
Provides the details for a record type such as a service request, drug request, or admission request in Health Cloud.

**License Requirements**
Industries Health Cloud Add On an org with a Health Cloud Utilization Mgmt Platform license

**Relationship to Other Components**
Ensure that the record type specified in the Case Record Type field in CareRequestConfiguration is available in the subscriber org.
Otherwise, the package must include the record type.


### Second-Generation Managed Packages Care System Field Mapping

**Documentation**
_Health Cloud Developer Guide_ [: CareRequestConfiguration](https://developer.salesforce.com/docs/atlas.en-us.262.0.health_cloud_object_reference.meta/health_cloud_object_reference/tooling_api_objects_carerequestconfiguration.htm)

### Care System Field Mapping

Represents a mapping from source system fields to Salesforce target entities and attributes.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** External ID Field

**•** Is Active

**•** Label

**•** Source System

**•** Target Object

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** Name

More Information

**Feature Name**
Metadata Name: CareSystemFieldMapping

Component Type in 1GP Package Manager UI: Care System Field Mapping

**Use Case**
Provides an out-of-the-box mapping for an external system to Salesforce for the Care Program Enrollment or Remote Monitoring
features in Health Cloud.

**License Requirements**
Industries Health Cloud


### Second-Generation Managed Packages Channel Layout

**Documentation**
_Health Cloud Developer Guide_ [: CareSystemFieldMapping](https://developer.salesforce.com/docs/atlas.en-us.262.0.health_cloud_object_reference.meta/health_cloud_object_reference/sforce_api_objects_caresystemfieldmapping.htm)

### Channel Layout

Represents the metadata associated with a communication channel layout.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: First-Generation Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** All attributes

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: ChannelLayout

Component Type in 1GP Package Manager UI: Communication Channel Layout

**Considerations When Packaging**
ChannelLayout can only be installed in Salesforce Classic orgs with Knowledge enabled.

ChannelLayout includes the article type `*__kav`, which is not supported by Lightning Knowledge.

If you try to install ChannelLayout into an org with Lightning Knowledge enabled, this message is displayed: “When Lightning
Knowledge is enabled, you can’t add an article type”.

**License Requirements**
Enable Knowledge in Salesforce Classic orgs.

**Documentation**

[Salesforce Knowledge Developer Guide: ChannelLayout](https://developer.salesforce.com/docs/atlas.en-us.262.0.knowledge_dev.meta/knowledge_dev/meta_articletype_channellayout.htm)


### Second-Generation Managed Packages Chatter Extension Chatter Extension

Represents the metadata used to describe a Rich Publisher App that’s integrated with the Chatter publisher.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: First-Generation Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection Yes

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** Description

**•** Header Text

**•** Hover Text

**•** Icon

**•** Name

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** Composition CMP

**•** Render CMP

**•** Type

More Information

**Feature Name**
Metadata Name: ChatterExtension

**Documentation**
_Metadata API Developer Guide:_ [ChatterExtension](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_chatterextensions.htm)

_Object Reference for the Salesforce Platform:_ [ChatterExtension](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_chatterextension.htm)

### Claim Financial Settings

Represents the configuration settings for Insurance Claim Financial Services.


### Second-Generation Managed Packages CommunicationChannelType

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** Label

Both Package Developer and Subscriber Can Edit

**•** Claim Coverage Pending Authority Status

**•** Claim Coverage Payment Detail Pending Authority Status

**•** Claim Pending Authority Status

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: ClaimFinancialSettings

**Documentation**
_Salesforce Help:_ [Claim Financial Settings](https://help.salesforce.com/s/articleView?id=ind.insurance_finauth_claim_financial_settings.htm&language=en_US)

### CommunicationChannelType

Represents the type of communication channel, such as WhatsApp and SMS, to use for referral promotions.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No


### Second-Generation Managed Packages Community Template Definition

Package Developer Can Remove Component From Package No

Component Has IP Protection Yes

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** None

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** API Name

More Information

**Feature Name**
Metadata Name: CommunicationChannelType

**Use Case**
Use WhatsApp as a communication channel for referral promotions.

**License Requirements**
Referral Marketing permission set license

**Documentation**
_Salesforce Help:_ [Communication Assets](https://help.salesforce.com/s/articleView?id=mktg.referral_promotion_wizard_step_content.htm&type=5&language=en_US)

### Community Template Definition

Represents the definition of an Experience Builder site template.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No


### Second-Generation Managed Packages Community Theme Definition

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** All

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: CommunityTemplateDefinition

Component Type in 1GP Package Manager UI: Lightning Community Template

**Use Case**
Share or distribute your Experience Builder site templates.

**License Requirements**
Customize Application user permission

Create and Set Up Experiences user permission

View Setup and Configuration user permission

**Relationship to Other Components**
If you add CommunityTemplateDefinition to a package, you must also add CommunityThemeDefinition to the package.

**Documentation**
_Salesforce Help:_ [Export a Customized Experience Builder Template for a Lightning Bolt Solution](https://help.salesforce.com/s/articleView?id=experience.community_builder_export_template.htm&type=5&language=en_US)

_Salesforce Help:_ [Package and Distribute a Lightning Bolt Solution](https://help.salesforce.com/s/articleView?id=experience.community_builder_export_package.htm&type=5&language=en_US)

### Community Theme Definition

Represents the definition of a theme for an Experience Builder site.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No


### Second-Generation Managed Packages Compact Layout

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** All

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: CommunityThemeDefinition

Component Type in 1GP Package Manager UI: Lightning Community Theme

**Use Case**
Share or distribute your Experience Builder site themes.

**License Requirements**
Customize Application user permission

Create and Set Up Experiences user permission

View Setup and Configuration user permission

**Relationship to Other Components**
CommunityThemeDefinition must contain a BrandingSet.

CommunityThemeDefinition can be added to a package without a CommunityTemplateDefinition, but CommunityTemplateDefinition
must contain a CommunityThemeDefinition to be added to a package.

**Documentation**
_Salesforce Help:_ [Export a Customized Experience Builder Theme for a Lightning Bolt Solution](https://help.salesforce.com/s/articleView?id=experience.community_builder_export_theme.htm&type=5&language=en_US)

_Salesforce Help:_ [Package and Distribute a Lightning Bolt Solution](https://help.salesforce.com/s/articleView?id=experience.community_builder_export_package.htm&type=5&language=en_US)

### Compact Layout

Represents the metadata associated with a compact layout.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes. Supported in 2GP packages only.


### Second-Generation Managed Packages Conditional Formatting Ruleset

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

[For more details on 2GP component removal, see Remove Metadata Components from Second-Generation Managed Packages.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_remove_md_components.htm)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** None

Both Package Developer and Subscriber Can Edit

**•** All attributes

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: CompactLayout

Component Type in 1GP Package Manager UI: Compact Layout

**Documentation**
_Metadata API Developer Guide:_ [CompactLayout](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_compactlayout.htm)

### Conditional Formatting Ruleset

Represents a set of rules that define the style and visibility of conditional field formatting on Dynamic Forms-enabled Lightning page
field instances.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No


### Second-Generation Managed Packages Connected App

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** Conditional formatting ruleset

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: UiFormatSpecificationSet

Component Type in 1GP Package Manager UI: UI Format Specification Set

**Relationship to Other Components**
You can only assign a conditional formatting ruleset to a field on a Dynamic Forms-enabled Lightning page.

**Documentation**
_Salesforce Help:_ [Conditional Field Formatting in Lightning App Builder](https://help.salesforce.com/s/articleView?id=platform.conditional_formatting_overview.htm&type=5&language=en_US)

_Metadata API Developer Guide:_ [UiFormatSpecificationSet](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_uiformatspecificationset.htm)

### Connected App

Represents a connected app configuration. A connected app enables an external application to integrate with Salesforce using APIs and
standard protocols, such as SAML, OAuth, and OpenID Connect.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes. Supported in 1GP packages only.

Component Has IP Protection No

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)


Second-Generation Managed Packages Connected App

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** Access Method

**•** Canvas App URL

**•** Callback URL

**•** Connected App Name

**•** Contact Email

**•** Contact Phone

**•** Description

**•** Icon URL

**•** Info URL

**•** Trusted IP Range

**•** Locations

**•** Logo Image URL

**•** OAuth Scopes

Both Package Developer and Subscriber Can Edit

**•** ACS URL

**•** Entity ID

**•** IP Relaxation

**•** Mobile Start URL

**•** Permitted Users

**•** Refresh Token Policy

**•** SAML Attributes

**•** Service Provider Certificate

**•** Start URL

**•** Subject Type

Neither Package Developer or Subscriber Can Edit

**•** API Name

**•** Created Date/By

**•** Consumer Key

**•** Consumer Secret

**•** Installed By

**•** Installed Date

**•** Last Modified Date/By

**•** Version

More Information

[For details on packaging a connected app in 2GP managed packages, see Package Connected Apps in Second-Generation Managed](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_connected_app.htm)
[Packaging in the](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_connected_app.htm) _Second-Generation Managed Packaging Developer Guide_ .


### Second-Generation Managed Packages Context Definition

**•** Subscribers or installers of a package can’t delete a connected app by itself, they can only uninstall the package. When a developer
deletes a connected app from a package, the connected app is deleted in the subscriber’s org during a package upgrade.

**•** To publish updates for a connected app that’s part of a managed package, you typically push a new managed package version
and upgrade subscriber orgs to the new version. But if you update a connected app’s PIN Protect settings, it’s not necessary to
push a new managed package upgrade. After saving changes to PIN Protect settings, these updates are automatically published
to subscriber orgs.

**•** The following connected app settings can’t be updated with managed package patches.

**–** Mobile App settings

**–** Push messaging, including Apple, Android, and Windows push notifications

**–** Canvas App settings

**–** SAML settings

To update these settings, publish a new package version.

**•** If you push upgrade a package containing a connected app whose OAuth scope or IP ranges have changed from the previous
version, the upgrade fails. This security feature blocks unauthorized users from gaining broad access to a customer org by
upgrading an installed package. A customer can still perform a pull upgrade of the same package. This upgrade is allowed
because it’s with the customer’s knowledge and consent.

**•** For connected apps created before Summer ’13, the existing install URL is valid until you package and upload a new version.
After you upload a new version of the package with an updated connected app, the install URL no longer works.

SEE ALSO:

[Package Connected Apps in Second-Generation Managed Packaging](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_dev2gp_connected_app.htm)

### Context Definition

A context definition defines the relationship between the nodes and the attributes within each node. For efficient data access, users can
use nodes and attributes to easily access the relevant data from the mapped data source. Various Salesforce products offer predefined
context definitions based on their use case.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: First-Generation Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes. Only if the component doesn’t contain any active context
definitions.

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit


### Second-Generation Managed Packages Contract Type

**•** None

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** Standard Context Definitions

More Information

**Feature Name**
Metadata Name: ContextDefinition

Component Type in 1GP Package Manager UI: Context Definition

**Documentation**
_Industries Common Resources Developer Guide:_ [Context Definition](https://developer.salesforce.com/docs/atlas.en-us.262.0.industries_reference.meta/industries_reference/meta_contextdefinition.htm)

_Salesforce Help:_ [Context Service](https://help.salesforce.com/s/articleView?id=ind.context_service_context_definitions.htm&type=5&language=en_US)

### Contract Type

A contract type is used to group contracts so that they exhibit similar characteristics. For example, the lifecycle states, the people who
access, the templates and clauses used.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade No

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Both Package Developer and Subscriber Can Edit

**•** Is Default

**•** Sub Types

Neither Package Developer or Subscriber Can Edit

**•** Name


### Second-Generation Managed Packages Conversation Channel Definition

More Information

**Feature Name**
Metadata Name: ContractType

**Use Case**
Allows admin users to modify Contract Type properties.

**License Requirements**
CLM Admin Permission Set (CLM User PSL).

**Documentation**
_Salesforce Contracts Developer Guide:_ [ContractType](https://developer.salesforce.com/docs/atlas.en-us.262.0.clm_developer_guide.meta/clm_developer_guide/meta_contracttype.htm)

### Conversation Channel Definition

Represents the conversation channel definition that’s implemented for Interaction Service for Bring Your Own Channel and Bring Your
Own Channel for CCaaS messaging channels.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** Connected App

**•** Description

**•** Label

**•** Name

Both Package Developer and Subscriber Can Edit

**•** None


### Second-Generation Managed Packages Conversation Vendor Info

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: ConversationChannelDefinition

Component Type in 1GP Package Manager UI: ConversationChannelDefinition

**Use Case**
To enable and set up Bring Your Own Channel, integrating third-party messaging services with Salesforce.

To enable and set up Bring Your Own Channel for Contact Center as a Service (CCaaS), integrating a third party CCaaS provider with
Salesforce.

**License Requirements**
Service Cloud license with Digital Engagement add-on license

**Post Install Steps**
Set up and enable Bring Your Own Channel or Bring Your Own Channel for CCaaS.

**Relationship to Other Components**
Linked to ConversationVendorInfo.

**Documentation**
_Salesforce Developer Documentation:_ [Bring Your Own Channel](https://developer.salesforce.com/docs/service/messaging-partner/overview)

_Salesforce Developer Documentation:_ [Bring Your Own Channel for CCaaS](https://developer.salesforce.com/docs/service/messaging-byoc-ccaas/overview)

_Salesforce Help:_ [Set Up Bring Your Own Channel](https://help.salesforce.com/s/articleView?id=service.partner_messaging_intro.htm&type=5&language=en_US)

_Salesforce Help:_ [Set Up Bring Your Own Channel for CCaaS](https://help.salesforce.com/s/articleView?id=service.byoc_ccaas_setup.htm&type=5&language=en_US)

### Conversation Vendor Info

This setup object connects the partner vendor system to the Service Cloud feature.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection Yes


### Second-Generation Managed Packages CORS Allowlist

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** None

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: ConversationVendorInfo

Component Type in 1GP Package Manager UI: ConversationVendorInfo

**Use Case**
Include information about a Service Cloud Voice implementation.

**License Requirements**
Enable Service Cloud Voice in your org.

**Documentation**
_Service Cloud Voice for Partner Telephony Developer Guide:_ [ConversationVendorInfo](https://developer.salesforce.com/docs/atlas.en-us.262.0.voice_pt_developer_guide.meta/voice_pt_developer_guide/sforce_api_objects_conversationvendorinfo.htm)

_Object Reference for the Salesforce Platform:_ [ConversationVendorInfo](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_conversationvendorinfo.htm)

### CORS Allowlist

Represents an origin in the CORS allowlist.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)


### Second-Generation Managed Packages CSP Trusted Site

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** Url pattern

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: CorsWhitelistOrigin

Component Type in 1GP Package Manager UI: CORS Allowed Origin List

**Use Case**
Customers can add a URL pattern that includes an HTTPS protocol and a domain name. Including a port number is optional. The
wildcard character (*) is supported only for the second-level domain name, for example, `https://*.example.com` .

**Documentation**
_Salesforce Help:_ [Enable CORS for OAuth Endpoints](https://help.salesforce.com/s/articleView?id=xcloud.remoteaccess_oauth_endpoints_cors.htm&type=5&language=en_US)

_Salesforce Help:_ [Configure Salesforce CORS Allowlist](https://help.salesforce.com/s/articleView?id=xcloud.extend_code_cors.htm&type=5&language=en_US)

### CSP Trusted Site

Represents a trusted URL. For each CspTrustedSite component, you can specify Content Security Policy (CSP) directives and permissions
policy directives.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org Yes

Package Developer Can Remove Component From Package No

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** None


Second-Generation Managed Packages CSP Trusted Site

Both Package Developer and Subscriber Can Edit

**•** context

**•** description

**•** endpointUrl

**•** isActive

**•** isApplicableToConnectSrc

**•** isApplicableToFontSrc

**•** isApplicableToFrameSrc

**•** isApplicableToImgSrc

**•** isApplicableToMediaSrc

**•** isApplicableToStyleSrc

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: CspTrustedSite

Component Type in 1GP Package Manager UI: CspTrustedSite

**Use Case**
[The Lightning Component framework uses Content Security Policy (CSP) to impose restrictions on content. The main objective of](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP)
[CSP is to help prevent cross-site scripting (XSS) and other code injection attacks. If your package includes sites or pages that load](https://www.owasp.org/index.php/Cross-site_Scripting_(XSS))
content from an external (non-Salesforce) server or via a WebSocket connection, add the external server as a CSP trusted site. Each
CSP trusted site can apply to Experience Cloud sites, Lightning Experience pages, custom Visualforce pages, or all three.

**Considerations When Packaging**
When you include the CspTrustedSite component in a package, the permissions for the third-party APIs and Websocket connections
apply to sites and pages across the org. Because this component modifies security, we don’t recommend including CspTrustedSite
components in packages. Instead, we recommend that you instruct customers to use the CSP Trusted Sites Setup page or the
CSPTrustedSites metadata API type to add the URLs to their allowlist as part of activating your package. If you choose to include
CspTrustedSite components in your package, disclose this change prominently in your package documentation to ensure that your
customers are aware of the security modification.

You can’t load JavaScript resources from a third-party site, even if it’s a CSP Trusted Site. To use a JavaScript library from a third-party
site, add it to a static resource, and then add the static resource to your component. After the library is loaded from the static resource,
you can use it as normal.

[CSP isn’t enforced by all browsers. For a list of browsers that enforce CSP, see caniuse.com.](https://caniuse.com)

**Usage Limits**
CspTrustedSite components are available in API version 39.0 and later. Multiple properties and enumeration values are available in
later API versions. For details, see CspTrustedSite in the _Metadata API Developer Guide_ .

For Experience Builder sites, if the HTTP header size is greater than 8 KB, the directives are moved from the CSP header to the `<meta>`
tag. To avoid errors from infrastructure limits, ensure that the HTTP header size doesn’t exceed 3 KB per context.

**Relationship to Other Components**
This component can be used only in conjunction with an Aura or Lightning Web Runtime (LWR) page for an Experience Cloud site,
a Lightning Page, or a Visualforce page.


### Second-Generation Managed Packages Custom Application

**Documentation**
_Salesforce Help:_ [Manage CSP Trusted Sites](https://help.salesforce.com/s/articleView?id=xcloud.security_trusted_urls_manage.htm&type=5&language=en_US)

_Metadata API Developer Guide_ [: CspTrustedSites](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_csptrustedsite.htm)

### Custom Application

Represents a custom application.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes. Supported in 2GP packages only.

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** Show in Lightning Experience (Salesforce Classic only)

**•** Selected Items (Lightning Experience only)

**•** Utility Bar (Lightning Experience only)

Both Package Developer and Subscriber Can Edit

**•** All attributes, except App Name and Show in Lightning Experience (Salesforce Classic only)

**•** All attributes, except Developer Name, Selected Items, and Utility Bar (Lightning Experience only)

Neither Package Developer or Subscriber Can Edit

**•** App Name (Salesforce Classic only)

**•** Developer Name (Lightning Experience only)


### Second-Generation Managed Packages Custom Button or Link

More Information

**Feature Name**
Metadata Name: CustomApplication

**Documentation**
_Metadata API Developer Guide:_ [CustomApplication](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_customapplication.htm)

### Custom Button or Link

Represents a custom link defined in a home page component.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes. Supported in both 1GP and 2GP packages.

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

[For more details on 2GP component removal, see Remove Metadata Components from Second-Generation Managed Packages.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_remove_md_components.htm)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** Behavior

**•** Button or Link URL

**•** Content Source

**•** Description

**•** Display Checkboxes

**•** Label

**•** Link Encoding

Both Package Developer and Subscriber Can Edit

**•** Height

**•** Resizeable


### Second-Generation Managed Packages Custom Console Components

**•** Show Address Bar

**•** Show Menu Bar

**•** Show Scrollbars

**•** Show Status Bar

**•** Show Toolbars

**•** Width

**•** Window Position

Neither Package Developer or Subscriber Can Edit

**•** Display Type

**•** Name

More Information

**Feature Name**
Metadata Name: WebLink, CustomPageWebLink

**Documentation**
_Salesforce Help:_ [Custom Buttons and Links](https://help.salesforce.com/s/articleView?id=platform.customize_enterprise.htm&type=5&language=en_US)

### Custom Console Components

Represents a custom console component (Visualforce page) assigned to a CustomApplication that is marked as a Salesforce console.
Custom console components extend the capabilities of Salesforce console apps.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

A package that has a custom console component can only be installed in an org with the Service Cloud license or Sales Console permission
enabled.

Packageable In: Second-Generation Managed Packages (2GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes. Supported in 1GP packages only.

Component Has IP Protection No

[To confirm whether this component is available in managed 1GP, managed 2GP, or both package types, see Metadata Coverage Report.](https://developer.salesforce.com/docs/success/metadata-coverage-report/references/coverage-report/metadata-coverage-report.html)

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)


### Second-Generation Managed Packages Custom Field on Standard or Custom Object

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** None

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: CustomApplicationComponent

Component Type in 1GP Package Manager UI: Custom Console Component

**Documentation**
_Metadata API Developer Guide:_ [CustomApplicationComponent](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_customapplicationcomponent.htm)

_Salesforce Help:_ [Create Console Components in Salesforce Classic](https://help.salesforce.com/s/articleView?id=service.console2_components_create_overview.htm&type=5&language=en_US)

### Custom Field on Standard or Custom Object

Represents the metadata associated with a field. Use this metadata type to create, update, or delete custom field definitions on standard
or custom objects.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes. Supported in both 1GP and 2GP packages.

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

[For more details on 2GP component removal, see Remove Metadata Components from Second-Generation Managed Packages.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_remove_md_components.htm)


### Second-Generation Managed Packages Custom Field on Custom Metadata Type

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** Auto-Number Display Format

**•** Decimal Places

**•** Description

**•** Default Value

**•** Field Label

**•** Formula

**•** Length

**•** Lookup Filter

**•** Related List Label

**•** Required

**•** Roll-Up Summary Filter Criteria

Both Package Developer and Subscriber Can Edit

**•** Chatter Feed Tracking

**•** Help Text

**•** Mask Type

**•** Mask Character

**•** Sharing Setting

**•** Sort Picklist Values

**•** Track Field History

Neither Package Developer or Subscriber Can Edit

**•** Child Relationship Name

**•** Data Type

**•** External ID

**•** Field Name

**•** Roll-Up Summary Field

**•** Roll-Up Summary Object

**•** Roll-Up Summary Type

**•** Unique

More Information

**•** Developers can add required and universally required custom fields to managed packages as long as they have default values.

**•** Auto-number type fields and required fields can’t be added after the object is included in a Managed - Released package.

**•** Subscriber orgs can’t install roll-up summary fields that summarize detail fields set to _protected_ .

### Custom Field on Custom Metadata Type

Represents a custom fields on the custom metadata type.


### Second-Generation Managed Packages Custom Field Display

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No

### Custom Field Display

Represents the CustomFieldDisplay view type assigned to product attribute custom fields.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** None

Both Package Developer and Subscriber Can Edit

**•** Description

**•** Master Label

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: CustomFieldDisplay


### Second-Generation Managed Packages Custom Help Menu Section

**License Requirements**
A B2B Commerce or D2C Commerce license and access to Commerce objects is required.

**Documentation**
_Salesforce Help:_ [Create Attributes for Product Variations in Commerce Cloud](https://help.salesforce.com/s/articleView?id=commerce.comm_config_att_set.htm&language=en_US)

### Custom Help Menu Section

Represents the section of the Lightning Experience help menu that the admin added to display custom, org-specific help resources for
the org. The custom section contains help resources added by the admin.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: First-Generation Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No

More Information

**Feature Name**
Metadata Name: CustomHelpMenuSection

**Documentation**
_Metadata API Developer Guide:_ [CustomHelpMenuSection](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_customhelpmenusection.htm)

### Custom Index

Represents an index used to increase the speed of queries.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade No

Subscriber Can Delete Component From Org No


### Second-Generation Managed Packages Custom Label

Package Developer Can Remove Component From Package No. It can only be removed if the associated custom field is
removed.

Component Has IP Protection No

More Information

**Feature Name**
Metadata Name: CustomIndex

Component Type in 1GP Package Manager UI: Custom Index

**Considerations When Packaging**
Subscribers can remove the custom index using Metadata API only.

**Documentation**
_Best Practices for Deployments with Large Data Volumes:_ [Indexes](https://developer.salesforce.com/docs/atlas.en-us.262.0.salesforce_large_data_volumes_bp.meta/salesforce_large_data_volumes_bp/ldv_deployments_infrastructure_indexes.htm)

### Custom Label

The CustomLabels metadata type allows you to create custom labels that can be localized for use in different languages, countries, and
currencies.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes. Supported in 2GP packages only.

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

[For more details on 2GP component removal, see Remove Metadata Components from Second-Generation Managed Packages.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_remove_md_components.htm)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** Category

**•** Short Description


### Second-Generation Managed Packages Custom Metadata Type Records

**•** Value

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** Name

More Information

**Feature Name**
Metadata Name: CustomLabels

**Considerations When Packaging**
If a label is translated, the language must be explicitly included in the package for the translations to be included in the package.
Subscribers can override the default translation for a custom label.

[This component can be marked as protected. For more details, see Protected Components in the](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/packaging_protected_components.htm) _First-Generation Managed Packaging_
_Developer Guide_ .

**Documentation**
_Metadata API Developer Guide:_ [CustomLabels](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_customlabels.htm)

### Custom Metadata Type Records

Represents a record of a custom metadata type.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes. Supported in managed 1GP if protected, and managed 2GP
whether protected or not.

Component Has IP Protection Yes

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)


### Second-Generation Managed Packages Custom Metadata Type

More Information

**Feature Name**
Metadata Name: CustomObject

[This component can be marked as protected. For more details, see Protected Components in the](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/packaging_protected_components.htm) _First-Generation Managed Packaging_
_Developer Guide_ .

**Usage Limits**
Deprecated custom metadata type records count against the subscriber’s org limit. When removing custom metadata type records
from a second-generation managed package, encourage subscribers to delete the deprecated records from their org. If the subscriber
org reaches their org limit for custom metadata type records, package upgrades that include new custom metadata type records
[fail. For details see Custom Metadata and Allocations and Usage Calculations in](https://help.salesforce.com/s/articleView?id=platform.custommetadatatypes_limits.htm&type=5&language=en_US) _Salesforce Help_ .

**Documentation**
_Salesforce Help:_ [Package Custom Metadata Types and Records](https://help.salesforce.com/s/articleView?id=platform.custommetadatatypes_package_install.htm&type=5&language=en_US)

### Custom Metadata Type

Represents a record of a custom metadata type.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection Yes

More Information

Second-generation managed packages (2GP) include the fields and records for custom metadata types that you add. You can’t add
fields directly to an existing package after the package version is promoted. If you create multiple packages that share a namespace,
then layouts and records can be in separate packages. Custom fields on the custom metadata type must be in the same package.

You can add fields to a custom metadata type by publishing an extension to the existing package, creating an entity relationship field,
[and mapping the field to the custom metadata type in your extension. See Add Custom Metadata Type Fields to Existing Packages.](https://help.salesforce.com/s/articleView?id=platform.custommetadatatypes_add_fields_packages.htm&type=5&language=en_US)

[This component can be marked as protected. For more details, see Protected Components in the](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/packaging_protected_components.htm) _First-Generation Managed Packaging_
_Developer Guide_ .

### Custom Notification Type

Represents the metadata associated with a custom notification type.


Second-Generation Managed Packages Custom Notification Type

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** Desktop, Mobile

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: CustomNotificationType

Component Type in 1GP Package Manager UI: Custom Notification Type

**License Requirements**
Database.com editions don’t have permission to access this component.

**Usage Limits**
You can package up to 500 custom notification types, but keep in mind that subscriber orgs are limited to a total of 500 custom
notification types. The subscriber org limit is shared across namespaces.

A subscriber org can execute up to 10,000 notification actions per hour.

**Documentation**
_Salesforce Help:_ [Create and Send Custom Desktop or Mobile Notifications](https://help.salesforce.com/s/articleView?id=platform.notif_builder_custom.htm&type=5&language=en_US)

_Salesforce Help:_ [Considerations for Processes that Send Custom Notifications](https://help.salesforce.com/s/articleView?id=platform.process_limits_customnotification.htm&type=5&language=en_US)


### Second-Generation Managed Packages Custom Object Custom Object

Represents a custom object that stores data unique to an org or an external object that maps to data stored outside an org.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes. Supported in both 1GP and 2GP packages.

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

[For more details on 2GP component removal, see Remove Metadata Components from Second-Generation Managed Packages.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_remove_md_components.htm)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** Description

**•** Label

**•** Plural Label

**•** Record Name

**•** Record Name Display Format

**•** Starts with a Vowel Sound

Both Package Developer and Subscriber Can Edit

**•** Allow Activities

**•** Allow Reports

**•** Available for Customer Portal

**•** Context-Sensitive Help Setting

**•** Default Sharing Model

**•** Development Status

**•** Enable Divisions

**•** Enhanced Lookup

**•** Grant Access Using Hierarchy


### Second-Generation Managed Packages Custom Object Translation

**•** Search Layouts

**•** Track Field History

Neither Package Developer or Subscriber Can Edit

**•** Object Name

**•** Record Name Data Type

More Information

**Feature Name**
Metadata Name: CustomObject

Component Type in 1GP Package Manager UI: Custom Object

**Considerations When Packaging**

If a developer enables the `Allow Reports` or `Allow Activities` attributes on a packaged custom object, the subscriber’s
org also has these features enabled during a package upgrade. After it’s enabled in a Managed - Released package, the developer
and the subscriber can’t disable these attributes.

Standard button and link overrides are also packageable.

In your extension package, if you want to access history information for custom objects contained in the base package, work with
the base package owner to:

**1.** Enable history tracking in the release org of the base package.

**2.** Create a new version of the base package.

**3.** Install the new version of the base package in the release org of the extension package to access the history tracking info.

As a best practice, don’t enable history tracking for custom objects contained in the base package directly in the extension package’s
release org. Doing so can result in an error when you install the package and when you create patch orgs for the extension package.

[This component can be marked as protected. For more details, see Protected Components and Hide Custom Objects and Custom](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/packaging_protected_components.htm)
[Permissions in Your Subscribers’ Orgs in the](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/fma_hide_custom_objects_permissions.htm) _First-Generation Managed Packaging Developer Guide_ .

**Documentation**
_Metadata API Developer Guide:_ [CustomObject](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/customobject.htm)

### Custom Object Translation

This metadata type allows you to translate custom objects for a variety of languages.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No


### Second-Generation Managed Packages Custom Permission

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** All attributes except Description of WorkflowTask, Help of CustomField, PicklistValueTranslation, and MasterLabel of LayoutSection.

Both Package Developer and Subscriber Can Edit

**•** Description of WorkflowTask

**•** Help of CustomField

**•** PicklistValueTranslation

**•** MasterLabel of LayoutSection

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: CustomObjectTranslation

**Relationship to Other Components**
When you create a first-generation managed package and add the Translation component, the Custom Object Translation component
is automatically added to your package.

When you create a second-generation managed package, you must add Custom Object Translation to your package, even if you've
already added the Translation component.

**Documentation**
_Metadata API Developer Guide:_ [CustomObjectTranslation](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_customobjecttranslation.htm)

### Custom Permission

Represents a permission that grants access to a custom feature.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes. Supported in 2GP packages only.

Component Has IP Protection No


### Second-Generation Managed Packages Custom Tab

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

[For more details on 2GP component removal, see Remove Metadata Components from Second-Generation Managed Packages.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_remove_md_components.htm)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** Connected App

**•** Description

**•** Label

**•** Name

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: CustomPermission

Component Type in 1GP Package Manager UI: Custom Permission

**Considerations When Packaging**
If you deploy a change set with a custom permission that includes a connected app, the connected app must already be installed
in the destination org.

[This component can be marked as protected. For more details, see Protected Components and Hide Custom Objects and Custom](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/packaging_protected_components.htm)
[Permissions in Your Subscribers’ Orgs in the](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/fma_hide_custom_objects_permissions.htm) _First-Generation Managed Packaging Developer Guide_ .

**Documentation**
_Metadata API Developer Guide:_ [CustomPermission](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_custompermission.htm)

### Custom Tab

Represents a custom tab. Custom tabs let you display custom object data or other web content in Salesforce.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes


Second-Generation Managed Packages Custom Tab

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes. Supported in both 1GP and 2GP packages.

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

[For more details on 2GP component removal, see Remove Metadata Components from Second-Generation Managed Packages.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_remove_md_components.htm)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** Description

**•** Encoding

**•** Has Sidebar

**•** Height

**•** Label

**•** S-control

**•** Splash Page Custom Link

**•** Type

**•** URL

**•** Width

Both Package Developer and Subscriber Can Edit

**•** Tab Style

Neither Package Developer or Subscriber Can Edit

**•** Tab Name

More Information

**Feature Name**
Metadata Name: CustomTab

**Considerations When Packaging**

**•** The tab style for a custom tab must be unique within your app. However, it doesn’t have to be unique within the org where it’s
installed. A custom tab style doesn’t conflict with an existing custom tab in the installer’s environment.

**•** To provide custom tab names in different languages, from Setup, in the Quick Find box, enter _`Rename Tabs and Labels`_,
then select **Rename Tabs and Labels** .

**Documentation**
_Metadata API Developer Guide:_ [CustomTab](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_tab.htm)


### Second-Generation Managed Packages Dashboard Dashboard

Represents a dashboard. Dashboards are visual representations of data that allow you to see key metrics and performance at a glance.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade No

Subscriber Can Delete Component From Org Yes

Package Developer Can Remove Component From Package Yes. Supported in both 1GP and 2GP packages.

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

[For more details on 2GP component removal, see Remove Metadata Components from Second-Generation Managed Packages.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_remove_md_components.htm)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** None

Both Package Developer and Subscriber Can Edit

**•** All attributes except Dashboard Unique Name

Neither Package Developer or Subscriber Can Edit

### • Dashboard Unique Name

More Information

**Feature Name**
Metadata Name: Dashboard

Type in 1GP Package Manager UI: Dashboard

**Considerations When Packaging**
Developers of managed packages must consider the implications of introducing dashboard components that reference reports
released in a previous version of the package. If the subscriber deleted the report or moved the report to a personal folder, the
dashboard component referencing the report is dropped during the installation. Also, if the subscriber has modified the report, the
report results can impact what displays in the dashboard component. As a best practice, release a dashboard and the related reports
in the same version.


### Second-Generation Managed Packages DataCalcInsightTemplate

**Documentation**
_Metadata API Developer Guide:_ [Dashboard](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_dashboard.htm)

### DataCalcInsightTemplate

Represents the object template for data calculations and insights of Data Cloud objects in DataCalcInsightTemplate. These objects are
added inside the data kit.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes. Supported in 1GP packages only.

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes. Supported in 1GP packages only.

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** None

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: DataCalcInsightTemplate

Component Type in 1GP Package Manager UI: Calculated Insight Template

**Use Case**
### DataCalcInsightTemplate represents the data calculations and insights for objects of a Data Cloud schema field the user includes in

a data kit.


### Second-Generation Managed Packages Data Connector Ingest API

**Considerations When Packaging**
A Data Cloud feature is always packaged via a data kit. A calculated insight template is added to a package when you add a data
calculation and insight into a data kit, and package that data kit. You can’t directly add this component to a package.

**License Requirements**
[For more information, see Data Cloud Standard Permission Sets in Salesforce Help.](https://help.salesforce.com/s/articleView?id=data.c360_a_userpermissions.htm&type=5&language=en_US)

**Post Install Steps**
After you install a package that contains a data kit, you must manually deploy the features from the installed data kit.

**Documentation**
_Data Cloud Developer Guide:_ [Packages and Data Kits](https://developer.salesforce.com/docs/platform/data-cloud-dev/guide/packages-data-kits.html)

_Salesforce Help:_ [Packaging in Data Cloud](https://help.salesforce.com/s/articleView?id=data.c360_a_packaging_in_customer_360_audiences.htm&type=5&language=en_US)

### Data Connector Ingest API

Represents the connection information specific to Ingestion API.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** None

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** DeveloperName

More Information

**Feature Name**
Metadata Name: DataConnectorIngestApi

Component Type in 1GP Package Manager UI: Adding DataStreamDefinition brings in DataConnectorIngestApi for Ingestion API
DataStreams.


### Second-Generation Managed Packages Data Connector S3

**Use Case**
This component is part of the Ingestion API Data stream metadata that is packaged and installed in subscriber.

**License Requirements**
You need Customer 360 Audiences Corporate (cdpPsl) licenses on both package developer org and subscriber org.

**Post Install Steps**
User has to create DataStream via ui-api or using the Data Cloud App.

**Documentation**
_Salesforce Help:_ [Ingestion API](https://developer.salesforce.com/docs/data/data-cloud-int/guide/c360-a-ingestion-api.html)

### Data Connector S3

Represents the connection information specific to Amazon S3.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** None

Both Package Developer and Subscriber Can Edit

**•** Delimiter

**•** FileNameWildCard

**•** ImportFromDirectory

**•** S3AccessKey

**•** S3BucketName

**•** S3SecretKey

Neither Package Developer or Subscriber Can Edit

**•** DeveloperName


### Second-Generation Managed Packages Data Kit Object Dependency

More Information

**Feature Name**
Metadata Name: DataConnectorS3

**Use Case**
This includes the bucket details for the S3 connector in Data Cloud.

**Considerations When Packaging**
[To package this component, first add it to a data kit. For more information about data kits, see Data Kits in](https://help.salesforce.com/s/articleView?id=data.c360_a_data_package_kits.htm&type=5&language=en_US) _Salesforce Help_ .

Credentials are encrypted and need “IsDevInternal” permission for the encryption service.

**License Requirements**
You need Customer 360 Audiences Corporate (cdpPsl) licenses on both package developer org and subscriber org.

**Post Install Steps**
User has to create DataStream via ui-api or using the Data Cloud App.

**Documentation**
_Salesforce Help:_ [Data Connector S3](https://developer.salesforce.com/docs/data/data-cloud-int/guide/c360-a-gcs-connector.html)

### Data Kit Object Dependency

Represent the object dependencies and relationships between different objects in Data Kit Object Dependency. These objects are added
inside the data kit.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes. Supported in 1GP packages only.

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes. Supported in 1GP packages only.

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** None


### Second-Generation Managed Packages Data Kit Object Template

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: DataKitObjectDependency

Component Type in 1GP Package Manager UI: Data Kit Object Dependency

**Use Case**
DataKitObjectDependency represents the relationship of objects of a Data Cloud schema field the user includes in a data kit.

**Considerations When Packaging**
A Data Cloud feature is always packaged via a data kit. You add the external data transport field template to a data kit and then add
that data kit to a package. You can’t directly add this component to a package.

**License Requirements**
[For more information, see Data Cloud Standard Permission Sets in Salesforce Help.](https://help.salesforce.com/s/articleView?id=data.c360_a_userpermissions.htm&type=5&language=en_US)

**Post Install Steps**
After you install a package that contains a data kit, you must manually deploy the features from the installed data kit.

**Documentation**
_Data Cloud Developer Guide:_ [Packages and Data Kits](https://developer.salesforce.com/docs/platform/data-cloud-dev/guide/packages-data-kits.html)

_Salesforce Help:_ [Packaging in Data Cloud](https://help.salesforce.com/s/articleView?id=data.c360_a_packaging_in_customer_360_audiences.htm&type=5&language=en_US)

### Data Kit Object Template

Represents the object in Data Kit Object Template. This object template is added inside the data kit.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes. Supported in 1GP packages only.

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes. Supported in 1GP packages only.

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.


### Second-Generation Managed Packages DataObjectBuildOrgTemplate

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** None

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: DataKitObjectTemplate

Component Type in 1GP Package Manager UI: Data Kit Object Dependency

**Use Case**
DataKitObjectTemplate represents the objects the user includes in a data kit.

**Considerations When Packaging**
A Data Cloud feature is always packaged via a data kit. You add the external data transport field template to a data kit, and then add
that data kit to a package. You can’t directly add this component to a package.

**License Requirements**
[For more information, see Data Cloud Standard Permission Sets in Salesforce Help.](https://help.salesforce.com/s/articleView?id=data.c360_a_userpermissions.htm&type=5&language=en_US)

**Post Install Steps**
After you install a package that contains a data kit, you must manually deploy the features from the installed data kit.

**Documentation**
_Data Cloud Developer Guide:_ [Packages and Data Kits](https://developer.salesforce.com/docs/platform/data-cloud-dev/guide/packages-data-kits.html)

_Salesforce Help:_ [Packaging in Data Cloud](https://help.salesforce.com/s/articleView?id=data.c360_a_packaging_in_customer_360_audiences.htm&type=5&language=en_US)

### DataObjectBuildOrgTemplate

Represents the output objects of the components the user includes in a data kit.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes. Supported in 1GP packages only.

Subscriber Can Delete Component From Org No


### Second-Generation Managed Packages Data Package Kit Definition

Package Developer Can Remove Component From Package Yes. Supported in 1GP packages only.

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** None

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: DataObjectBuildOrgTemplate

Component Type in 1GP Package Manager UI: DataObjectBuildOrgTemplate

**Use Case**

Supports extension packages that reference the output of any object.

**Considerations When Packaging**
A Data Cloud feature is always packaged via a data kit. You add the data object build org template to a data kit, and then add that
data kit to a package. You can’t directly add this component to a package.

**License Requirements**

[For more information, see Data Cloud Standard Permission Sets in Salesforce Help.](https://help.salesforce.com/s/articleView?id=data.c360_a_userpermissions.htm&type=5&language=en_US)

**Post Install Steps**

After you install a package that contains a data kit, you must manually deploy the features from the installed data kit.

**Documentation**
_Data Cloud Developer Guide:_ [Packages and Data Kits](https://developer.salesforce.com/docs/platform/data-cloud-dev/guide/packages-data-kits.html)

_Salesforce Help:_ [Packaging in Data Cloud](https://help.salesforce.com/s/articleView?id=data.c360_a_packaging_in_customer_360_audiences.htm&type=5&language=en_US)

### Data Package Kit Definition

Represents the top-level Data Kit container definition. Content objects can be added after the Data Kit is defined.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)


Second-Generation Managed Packages Data Package Kit Definition

Component Is Updated During Package Upgrade Yes. Supported in 1GP packages only.

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes. Supported in 1GP packages only.

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** description

**•** developerName

**•** isDeployed

**•** isEnabled

**•** masterLabel

**•** versionNumber

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: DataPackageKitDefinition

Component Type in 1GP Package Manager UI: Data Package Kit Definition

**Use Case**
Represents the top-level data kit container definition. Content objects can be added after the data kit is defined.

**License Requirements**
[For more information, see Data Cloud Standard Permission Sets in Salesforce Help.](https://help.salesforce.com/s/articleView?id=data.c360_a_userpermissions.htm&type=5&language=en_US)

**Post Install Steps**
After you install a package that contains a data kit, you must manually deploy features from the installed data kit.

**Documentation**
_Metadata API Developer Guide:_ [DataPackageKitDefinition](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_datapackagekitdefinition.htm)

_Data Cloud Developer Guide:_ [Packages and Data Kits](https://developer.salesforce.com/docs/platform/data-cloud-dev/guide/packages-data-kits.html)

_Salesforce Help:_ [Packaging in Data Cloud](https://help.salesforce.com/s/articleView?id=data.c360_a_packaging_in_customer_360_audiences.htm&type=5&language=en_US)


### Second-Generation Managed Packages Data Package Kit Object Data Package Kit Object

Represents the object in Data Kit Content Object. These objects are added inside the data kit.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes (supported only in 1GP packages)

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes (supported only in 1GP packages)

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** parentDataPackageKitDefinitionName

**•** referenceObjectName

**•** referenceObjectType

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: DataPackageKitObject

Component Type in 1GP Package Manager UI: Data Package Kit Object

**Use Case**
Represents an object in a data kit.

**License Requirements**
[For more information, see Data Cloud Standard Permission Sets in Salesforce Help.](https://help.salesforce.com/s/articleView?id=data.c360_a_userpermissions.htm&type=5&language=en_US)


### Second-Generation Managed Packages Data Source

**Post Install Steps**
After you install a package that contains a data kit, you must manually deploy features from the installed data kit.

**Documentation**
_Metadata API Developer Guide:_ [DataPackageKitObject](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_datapackagekitobject.htm)

_Data Cloud Developer Guide:_ [Packages and Data Kits](https://developer.salesforce.com/docs/platform/data-cloud-dev/guide/packages-data-kits.html)

_Salesforce Help:_ [Packaging in Data Cloud](https://help.salesforce.com/s/articleView?id=data.c360_a_packaging_in_customer_360_audiences.htm&type=5&language=en_US)

### Data Source

Used to represent the system where the data was sourced.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP)

Component Is Updated During Package Upgrade No

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** None

Both Package Developer and Subscriber Can Edit

**•** DataSourceStatus

**•** ExternalRecordIdentifier

**•** LastDataChangeStatusDateTime

**•** LastDataChangeStatusErrorCode

Neither Package Developer or Subscriber Can Edit

**•** DeveloperName

More Information

**Feature Name**
Metadata Name: DataSource

**Use Case**
DataSource gives the lineage information of the datastream.


### Second-Generation Managed Packages Data Source Bundle Definition

**License Requirements**
You need Customer 360 Audiences Corporate (cdpPsl) licenses on both package developer org and subscriber org.

**Post Install Steps**
Create DataStream using ui-api or the Data Cloud App.

**Relationship to Other Components**
This isn't a top-level entity. AddDataStreamDefinition or DataKitDefinition to pick up DataSource.

**Documentation**
_Salesforce Help:_ [Connection Tasks in Data Cloud](https://help.salesforce.com/s/articleView?id=data.c360_a_connection_tasks.htm&type=5&language=en_US)

### Data Source Bundle Definition

Represents the bundle of streams that a user adds to a data kit.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes (supported only in 1GP packages)

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes (supported only in 1GP packages)

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** dataPlatform

**•** isMultiDeploymentSupported

**•** masterLabel

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** None


### Second-Generation Managed Packages Data Source Object

More Information

**Feature Name**
Metadata Name: DataSourceBundleDefinition

Component Type in 1GP Package Manager UI: Data Source Bundle Definition

**Use Case**
Represents the data stream data sources that a user adds to a data kit.

**Considerations When Packaging**
Any Data Cloud feature is always packaged via a data kit. A data source bundle definition is added to a package when you add a
data stream to a data kit and package that data kit. You can’t directly add this component to a package.

**License Requirements**
[For more information, see Data Cloud Standard Permission Sets in Salesforce Help.](https://help.salesforce.com/s/articleView?id=data.c360_a_userpermissions.htm&type=5&language=en_US)

**Post Install Steps**
After you install a package that contains a data kit, you must manually deploy features from the installed data kit.

**Documentation**
_Metadata API Developer Guide:_ [DataSourceBundleDefinition](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_datasourcebundledefinition.htm)

_Data Cloud Developer Guide:_ [Packages and Data Kits](https://developer.salesforce.com/docs/platform/data-cloud-dev/guide/packages-data-kits.html)

_Salesforce Help:_ [Packaging in Data Cloud](https://help.salesforce.com/s/articleView?id=data.c360_a_packaging_in_customer_360_audiences.htm&type=5&language=en_US)

### Data Source Object

Represents the object from where the data was sourced.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP)

Component Is Updated During Package Upgrade No

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** None

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** DataObjectType


### Second-Generation Managed Packages Data Src Data Model Field Map

**•** DataSource

**•** ExternalRecordId

More Information

**Feature Name**
Metadata Name: DataSourceObject

**Use Case**
DataSourceObject contains specific information about the source of the data like filename, table names.

**Considerations When Packaging**
DataSourceObject pulls in child DataSourceField entity records when packaged with DataKitDefinition.

**License Requirements**
Customer 360 Audiences Corporate (cdpPsl) licenses must be available on both package developer org and subscriber org.

**Post Install Steps**
Create a DataStream via ui-api or using the Data Cloud App.

**Relationship to Other Components**
This isn’t a top-level entity. Add DataStreamDefinition or DataKitDefinition to pick up DataSourceObject.

**Documentation**
_Salesforce Help:_ [Connection Tasks in Data Cloud](https://help.salesforce.com/s/articleView?id=data.c360_a_connection_tasks.htm&type=5&language=en_US)

### Data Src Data Model Field Map

Represents the entity that’s used to store the design-time bundle-level mappings for the data source fields and data model fields.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes (supported only in 1GP packages)

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes (supported only in 1GP packages)

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)


### Second-Generation Managed Packages Data Stream Definition

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** masterLabel

**•** sourceField

**•** targetField

**•** versionNumber

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: DataSrcDataModelFieldMap

Component Type in 1GP Package Manager UI: Data Source Data Model Field Mapping

**Use Case**
Represents the entity that contains design-time bundle-level mappings for the data source fields and data model fields.

**Considerations When Packaging**
Any Data Cloud feature is always packaged via a data kit. Data model field mappings are added to a package when you add a data
stream and any associated mappings to a data kit and package that data kit. You can’t directly add this component to a package.

**License Requirements**
[For more information, see Data Cloud Standard Permission Sets in Salesforce Help.](https://help.salesforce.com/s/articleView?id=data.c360_a_userpermissions.htm&type=5&language=en_US)

**Post Install Steps**
After you install a package that contains a data kit, you must manually deploy features from the installed data kit.

**Documentation**
_Metadata API Developer Guide:_ [DataSrcDataModelFieldMap](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_datasrcdatamodelfieldmap.htm)

_Data Cloud Developer Guide:_ [Packages and Data Kits](https://developer.salesforce.com/docs/platform/data-cloud-dev/guide/packages-data-kits.html)

_Salesforce Help:_ [Packaging in Data Cloud](https://help.salesforce.com/s/articleView?id=data.c360_a_packaging_in_customer_360_audiences.htm&type=5&language=en_US)

### Data Stream Definition

Contains Data Ingestion information such as Connection, API and File retrieval settings.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes


Second-Generation Managed Packages Data Stream Definition

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** AreHeadersIncludedInTheFiles

**•** BulkIngest

**•** Description

**•** IsLimitedToNewFiles

**•** IsMissingFileFailure

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** DataConnectionGCS

**•** DataConnectorType

**•** DataExtractField

**•** DataExtractMethod

**•** DataExtractField

**•** DataPlatformDataSetBundle

**•** FileNameWildcard

**•** MktDataLakeObject

**•** MktDataTranObject

More Information

**Feature Name**
Metadata Name: DataStreamDefinition

Component Type in 1GP Package Manager UI: DataStreamDefinition

**Use Case**

DataStreamDefinition is the starting point for packaging a Datastream and its mappings.

**Considerations When Packaging**
Data Cloud admin user can install or upgrade the package. Admin User or Data Aware Specialist User can create Datastreams out of
the installed package.

**License Requirements**
Customer 360 Audiences Corporate (cdpPsl) licenses must be available on both package developer org and subscriber org. CDP
Admin User can install,upgrade, or uninstall the package.

**Post Install Steps**

Create the DataStream via ui-api or using the Data Cloud App.


### Second-Generation Managed Packages Data Stream Template

**Documentation**
_Metadata API Developer Guide:_ [DataStreamDefinition](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_datastreamdefinition.htm)

### Data Stream Template

Represents the data stream that a user adds to a data kit.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes (supported only in 1GP packages)

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes (supported only in 1GP packages)

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** dataImportRefreshFrequency

**•** dataSourceBundleDefinition

**•** dataSourceObject

**•** objectCategory

**•** refreshFrequency

**•** refreshHours

**•** refreshMode

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** None


### Second-Generation Managed Packages DataWeaveResource

More Information

**Feature Name**
Metadata Name: DataStreamTemplate

Component Type in 1GP Package Manager UI: Data Stream Template

**Use Case**
Represents the data stream that a user adds to a data kit.

**Considerations When Packaging**
Any Data Cloud feature is always packaged via a data kit. A data stream template is added to a package when you add a data stream
to a data kit and package that data kit. You can’t directly add this component to a package.

**License Requirements**
[For more information, see Data Cloud Standard Permission Sets in Salesforce Help.](https://help.salesforce.com/s/articleView?id=data.c360_a_userpermissions.htm&type=5&language=en_US)

**Post Install Steps**
After you install a package that contains a data kit, you must manually deploy features from the installed data kit.

**Documentation**
_Metadata API Developer Guide:_ [DataStreamTemplate](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_datastreamtemplate.htm)

_Data Cloud Developer Guide:_ [Packages and Data Kits](https://developer.salesforce.com/docs/platform/data-cloud-dev/guide/packages-data-kits.html)

_Salesforce Help:_ [Packaging in Data Cloud](https://help.salesforce.com/s/articleView?id=data.c360_a_packaging_in_customer_360_audiences.htm&type=5&language=en_US)

### DataWeaveResource

Represents the DataWeaveScriptResource class that is generated for all DataWeave scripts. DataWeave scripts can be directly invoked
from Apex.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes (if not set to `global` access).

Component Has IP Protection Yes

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)


### Second-Generation Managed Packages Decision Matrix Definition

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** API Version

**•** DataWeave Script

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: DataWeaveResource

Component Type in 1GP Package Manager UI: DataWeaveResource

**Use Case**
Include MuleSoft DataWeave scripts to read and parse data from one format, transform it, and export it in a different format directly
from Apex.

**Considerations When Packaging**
There’s a maximum of 50 DataWeave scripts per org.

**Documentation**
_Apex Developer Guide:_ [DataWeave in Apex.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/DataWeaveInApex.htm)

### Decision Matrix Definition

Represents a definition of a decision matrix.

Note: 2GP support for Business Rules Engine Components is a pilot or beta service that is subject to the Beta Services Terms at
[Agreements - Salesforce.com](https://www.salesforce.com/company/legal/agreements/) or a written Unified Pilot Agreement if executed by Customer, and applicable terms in the [Product](https://ptd.salesforce.com/)
[Terms Directory. Use of this pilot or beta service is at the Customer's sole discretion.](https://ptd.salesforce.com/)

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes. Only if the component is inactive.

Subscriber Can Delete Component From Org Yes. Only if the component is inactive.

Package Developer Can Remove Component From Package Yes

Component Has IP Protection No


### Second-Generation Managed Packages Decision Matrix Definition Version

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** Type

**•** GroupKey

**•** SubGroupKey

Both Package Developer and Subscriber Can Edit

**•** versions

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: DecisionMatrixDefinition

Component Type in 1GP Package Manager UI: Decision Matrix Definition

**Use Case**
Decision matrices are lookup tables that match input values to a matrix row and return the row’s output values. Expression sets and
various digital procedures can call decision matrices. Decision matrices accept JSON input from, and return JSON output to the digital
processes that call the matrices. Decision matrices are useful for implementing complex rules in a systematic, readable manner.

**Documentation**
### Industries Common Resources Developer Guide: Decision Matrix Definition

_Salesforce Help:_ [Decision Matrices](https://help.salesforce.com/s/articleView?id=ind.decision_matrices.htm&type=5&language=en_US)

_Salesforce Help:_ [Decision Matrix Migration Considerations](https://help.salesforce.com/s/articleView?id=ind.decision_matrix_migration_considerations.htm&type=5&language=en_US)

### Decision Matrix Definition Version

Represents a definition of a decision matrix version.

Note: 2GP support for Business Rules Engine Components is a pilot or beta service that is subject to the Beta Services Terms at
[Agreements - Salesforce.com](https://www.salesforce.com/company/legal/agreements/) or a written Unified Pilot Agreement if executed by Customer, and applicable terms in the [Product](https://ptd.salesforce.com/)
[Terms Directory. Use of this pilot or beta service is at the Customer's sole discretion.](https://ptd.salesforce.com/)

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.


### Second-Generation Managed Packages Decision Table

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes. Only if the component is inactive.

Subscriber Can Delete Component From Org Yes. Only if the component is inactive.

Package Developer Can Remove Component From Package Yes

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** None

Both Package Developer and Subscriber Can Edit

**•** columns

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: DecisionMatrixDefinitionVersion

Component Type in 1GP Package Manager UI: Decision Matrix Definition Version

**Post Install Steps**
After migrating a decision matrix version, upload the row data to the active version manually. The row data isn’t migrated as part of
the migration.

**Relationship to Other Components**
A DecisionMatrixDefinitionVersion is a child of DecisionMatrixDefinition, and can’t exist without the parent DecisionMatrixDefinition.

**Documentation**
_Industries Common Resources Developer Guide:_ [Decision Matrix Definition](https://developer.salesforce.com/docs/atlas.en-us.262.0.industries_reference.meta/industries_reference/meta_decisionmatrixdefinition.htm)

_Salesforce Help:_ [Decision Matrices](https://help.salesforce.com/s/articleView?id=ind.decision_matrices.htm&type=5&language=en_US)

_Salesforce Help:_ [Decision Matrix Migration Considerations](https://help.salesforce.com/s/articleView?id=ind.decision_matrix_migration_considerations.htm&type=5&language=en_US)

### Decision Table

Represents the information about a decision table.


### Second-Generation Managed Packages Decision Table Dataset Link

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection Yes, except templates

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

### • Decision Table

Both Package Developer and Subscriber Can Edit

**•** Label

**•** Description

**•** Status

Neither Package Developer or Subscriber Can Edit

**•** API Name

**•** URL

More Information

**Feature Name**
Metadata Name: DecisionTable

Component Type in 1GP Package Manager UI: Decision Table

**Use Case**
Decision tables read business rules and decide the outcome for records in your Salesforce org or for the values that you specify.

**License Requirements**
Either Loyalty Management or Rebate Management

**Documentation**
_Salesforce Help:_ [Decision Tables](https://help.salesforce.com/s/articleView?id=ind.concept_decision_table.htm&type=5&language=en_US)

### Decision Table Dataset Link

Represents the information about a dataset link associated with a decision table. In a dataset link, select an object for whose records,
the decision table must provide an outcome.


### Second-Generation Managed Packages Digital Experience

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection Yes, except templates

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** Dataset Link record

Both Package Developer and Subscriber Can Edit

**•** Label

**•** Description

**•** Status

Neither Package Developer or Subscriber Can Edit

**•** API Name

**•** URL

More Information

**Feature Name**
Metadata Name: DecisionTableDatasetLink

**Use Case**
In a dataset link, you can map the decision table’s input fields with fields of different standard or custom objects.

**License Requirements**
Either Loyalty Management or Rebate Management

**Documentation**
_Salesforce Help:_ [Add Dataset Links to a Decision Table](https://help.salesforce.com/s/articleView?id=ind.task_decision_table_dataset_link.htm&type=5&language=en_US)

### Digital Experience

Represents a text-based code structure of your organization’s workspaces, organized by workspace type, and each workspace’s content
items.


### Second-Generation Managed Packages Digital Experience Bundle

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** Content Title

**•** Content Body

**•** Content Folder

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: DigitalExperience

**Use Case**
To move Digital Experience metadata Content from one org to another

**Post Install Steps**
After the package is installed, publish the site to make it available to customers.

**Documentation**
_Salesforce Help:_ [CMS Content](https://help.salesforce.com/s/articleView?id=xcloud.community_managed_content_content_creation.htm&type=5&language=en_US)

### Digital Experience Bundle

Represents a text-based code structure of your organization’s workspaces, organized by workspace type, and each workspace’s content
items.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.


Second-Generation Managed Packages Digital Experience Bundle

Packageable In: Second-Generation Managed Packages (2GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** Labels

**•** Description

**•** Content

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: DigitalExperienceBundle

**Use Case**
Share or distribute the content of an enhanced workspace in Salesforce CMS, including images, documents, and news articles. In
Marketing Cloud, you can package the content of general and marketing workspaces, including landing pages, forms, and emails
(and their associated images and branding).

**Considerations When Packaging**

Enhanced LWR sites are unsupported.

In marketing workspaces, the default data graph, personalization recommenders, personalization points, and decisions aren't included
in the bundle. If the workspace includes emails with personalized content that’s based on these objects, then:

**•** Any merge field or repeater that uses the default data graph or a personalization recommender from the source org is broken
in the target org.

**•** Any dynamic content variations of email components are removed and only the default variations appear in the email.

**Post Install Steps**
After the package is installed, publish the workspace content to make it available to customers.

**Documentation**
_Salesforce Help:_ [Salesforce CMS](https://help.salesforce.com/s/articleView?id=xcloud.community_managed_content_overview.htm&language=en_US)

_Salesforce Help:_ [Marketing Cloud](https://help.salesforce.com/s/articleView?id=products.mktg_main.htm&type=5&language=en_US)

_Metadata API Developer Guide:_ [DigitalExperienceBundle](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_digitalexperiencebundle.htm)


### Second-Generation Managed Packages Decision Table Decision Table

Represents the information about a decision table.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection Yes, except templates

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

### • Decision Table

Both Package Developer and Subscriber Can Edit

**•** Label

**•** Description

**•** Status

Neither Package Developer or Subscriber Can Edit

**•** API Name

**•** URL

More Information

**Feature Name**
Metadata Name: DecisionTable

Component Type in 1GP Package Manager UI: Decision Table

**Use Case**
Decision tables read business rules and decide the outcome for records in your Salesforce org or for the values that you specify.

**License Requirements**
Either Loyalty Management or Rebate Management

**Documentation**
### Salesforce Help: Decision Tables


### Second-Generation Managed Packages Disclosure Definition Disclosure Definition

Represents information that defines a disclosure type, such as details of the publisher or vendor who created or implemented the report.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** All attributes

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: DisclosureDefinition

Component Type in 1GP Package Manager UI: Disclosure Definition

**Use Case**
You can use this component to define a disclosure type, such as details of the publisher or vendor who created or implemented the
report.

**License Requirements**

**•** Net Zero Cloud Growth license

**•** Disclosure and Compliance Hub permission set license

**•** Disclosure and Compliance Hub User permission set

**Post Install Steps**
Enable these org settings:

**•** Manage Disclosure and Compliance Hub


### Second-Generation Managed Packages Disclosure Definition Version

**Documentation**

**•** _Salesforce Help:_ [Disclosure and Compliance Hub](https://help.salesforce.com/articleView?id=ind.netzero_setup_disclosure_and_compliance_hub.htm&type=5&language=en_US)

**•** _Salesforce Help:_ [Generate Disclosures Using Disclosure and Compliance Hub](https://help.salesforce.com/articleView?id=ind.netzero_manager_generate_disclosures_using_disclosure_compliance_hub.htm&type=5&language=en_US)

**•** _Metadata API Developer Guide:_ [DisclosureDefinition](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_disclosuredefinition.htm)

### Disclosure Definition Version

Represents the version information about the disclosure definition.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** DisclosureDefinition

**•** Description

**•** IsActive

**•** VersionNumber

**•** OmniScriptCnfgApiName

**•** IsCurrentVersion

**•** DisclosureDefCurrVer

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: DisclosureDefinitionVersion

Component Type in 1GP Package Manager UI: Disclosure Definition Version


### Second-Generation Managed Packages Disclosure Type

**Use Case**
You can use this component to define the version information about the disclosure definition.

**License Requirements**

**•** Net Zero Cloud Growth license

**•** Disclosure and Compliance Hub permission set license

**•** Disclosure and Compliance Hub User permission set

**Post Install Steps**
Enable these org settings:

**•** Manage Disclosure and Compliance Hub

**Documentation**

**•** _Salesforce Help:_ [Disclosure and Compliance Hub](https://help.salesforce.com/articleView?id=ind.netzero_setup_disclosure_and_compliance_hub.htm&type=5&language=en_US)

**•** _Salesforce Help:_ [Generate Disclosures Using Disclosure and Compliance Hub](https://help.salesforce.com/articleView?id=ind.netzero_manager_generate_disclosures_using_disclosure_compliance_hub.htm&type=5&language=en_US)

**•** _Metadata API Developer Guide:_ [DisclosureDefinitionVersion](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_disclosuredefinitionversion.htm)

### Disclosure Type

Represents the types of disclosures that are done by an individual or an organization and the associated metadata.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** All attributes

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** None


### Second-Generation Managed Packages Discovery AI Model

More Information

**Feature Name**
Metadata Name: DisclosureType

Component Type in 1GP Package Manager UI: Disclosure Type

**Use Case**
You can use this component to create types of disclosures that are done by an individual or an organization.

**License Requirements**

**•** Net Zero Cloud Growth license

**•** Disclosure and Compliance Hub permission set license

**•** Disclosure and Compliance Hub User permission set

**Post Install Steps**
Enable these org settings:

**•** Manage Disclosure and Compliance Hub

**Documentation**

**•** _Salesforce Help:_ [Disclosure and Compliance Hub](https://help.salesforce.com/articleView?id=ind.netzero_setup_disclosure_and_compliance_hub.htm&type=5&language=en_US)

**•** _Salesforce Help:_ [Generate Disclosures Using Disclosure and Compliance Hub](https://help.salesforce.com/articleView?id=ind.netzero_manager_generate_disclosures_using_disclosure_compliance_hub.htm&type=5&language=en_US)

**•** _Metadata API Developer Guide:_ [DisclosureType](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_disclosuretype.htm)

### Discovery AI Model

Represents the metadata associated with a model used in Einstein Discovery.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade No

Subscriber Can Delete Component From Org Yes

Package Developer Can Remove Component From Package Yes

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

[For more details on 2GP component removal, see Remove Metadata Components from Second-Generation Managed Packages.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_remove_md_components.htm)


### Second-Generation Managed Packages Discovery Goal

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** None

Both Package Developer and Subscriber Can Edit

**•** All attributes except Discovery AI Model Unique Name

Neither Package Developer or Subscriber Can Edit

**•** Discovery AI Model Unique Name

More Information

**Feature Name**
Metadata Name: DiscoveryAIModel

**Documentation**
_Metadata API Developer Guide:_ [DiscoveryAIModel](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_discoveryaimodel.htm)

### Discovery Goal

Represents the metadata associated with an Einstein Discovery prediction definition.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade No

Subscriber Can Delete Component From Org Yes

Package Developer Can Remove Component From Package Yes

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

[For more details on 2GP component removal, see Remove Metadata Components from Second-Generation Managed Packages.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_remove_md_components.htm)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** None


### Second-Generation Managed Packages Discovery Story

Both Package Developer and Subscriber Can Edit

**•** All attributes except Discovery Goal Unique Name

Neither Package Developer or Subscriber Can Edit

**•** Discovery Goal Unique Name

More Information

**Feature Name**
Metadata Name: DiscoveryGoal

**Documentation**
_Metadata API Developer Guide:_ [DiscoveryGoal](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_discoverygoal.htm)

### Discovery Story

Represents the metadata associated with a story used in Einstein Discovery.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade No

Subscriber Can Delete Component From Org Yes

Package Developer Can Remove Component From Package Yes

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

[For more details on 2GP component removal, see Remove Metadata Components from Second-Generation Managed Packages.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_remove_md_components.htm)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** None

Both Package Developer and Subscriber Can Edit

**•** All attributes except Discovery Story Unique Name

Neither Package Developer or Subscriber Can Edit


### Second-Generation Managed Packages Document

**•** Discovery Story Unique Name

More Information

**Feature Name**
Metadata Name: DiscoveryStory

### **Documentation**

_Metadata API Developer Guide:_ [DiscoveryStory](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_discoverystory.htm)

### Document

Represents a Document. All documents must be in a document folder, such as sampleFolder/TestDocument.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade No

Subscriber Can Delete Component From Org Yes

Package Developer Can Remove Component From Package Yes. Supported in both 1GP and 2GP packages.

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

[For more details on 2GP component removal, see Remove Metadata Components from Second-Generation Managed Packages.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_remove_md_components.htm)

More Information

**Feature Name**
Metadata Name: Document

Component Type in 1GP Package Manager UI: Document

### **Documentation** Metadata API Developer Guide: Document Document Generation Setting

Represents an org's settings for automatic document generation from templates.


### Second-Generation Managed Packages Eclair GeoData

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade No

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Both Package Developer and Subscriber Can Edit

**•** Document Template Library Name

**•** Generation Mechanism

**•** Guest Access Named Credential

**•** Label

**•** Preview Type

Neither Package Developer or Subscriber Can Edit

**•** API Name

More Information

**Feature Name**
Metadata Name: DocumentGenerationSetting

**Use Case**
Allows admin users to modify document generation properties.

**License Requirements**
DocGen Designer (Permission Set License)

**Documentation**
_Metadata API Developer Guide:_ [DocumentGenerationSetting](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_documentgenerationsetting.htm)

### Eclair GeoData

Represents an Analytics custom map chart. Custom maps are user-defined maps that are uploaded to Analytics and are used just as
standard maps are. Custom maps are accessed in Analytics from the list of maps available with the map chart type.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.


### Second-Generation Managed Packages Email Template (Classic)

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade No

Subscriber Can Delete Component From Org Yes

Package Developer Can Remove Component From Package Yes

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** None

Both Package Developer and Subscriber Can Edit

**•** All attributes except Eclair GeoData Unique Name

Neither Package Developer or Subscriber Can Edit

**•** Eclair GeoData Unique Name

More Information

**Feature Name**
Metadata Name: EclairGeoData

**Documentation**
_Metadata API Developer Guide:_ [EclairGeoData](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_eclairgeodata.htm)

### Email Template (Classic)

Use email templates to increase productivity and ensure consistent messaging. Email templates with merge fields let you quickly send
emails that include field data from Salesforce records.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade No


### Second-Generation Managed Packages Email Template (Lightning)

Subscriber Can Delete Component From Org Yes

Package Developer Can Remove Component From Package Yes. Supported in 1GP packages only.

Component Has IP Protection No

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** None

Both Package Developer and Subscriber Can Edit

**•** All attributes except Email Template Name

Neither Package Developer or Subscriber Can Edit

**•** Email Template Name

### Email Template (Lightning)

Represents a template for an email, mass email, list email, or Sales Engagement email.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: First-Generation Managed Packages (1GP)

Component Is Updated During Package Upgrade No

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes. Supported in 1GP packages only. However, 1GP packages
created in Email Template Builder can't be removed.

Component Has IP Protection No

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** None

Both Package Developer and Subscriber Can Edit


### Second-Generation Managed Packages Embedded Service Config

**•** None

Neither Package Developer or Subscriber Can Edit

**•** All attributes

More Information

These packaging considerations apply to Lightning email templates, including email templates created in Email Template Builder.

**•** For email templates created in Email Template Builder before the Spring ’21 release, attachments aren’t automatically added to the
package. Open and resave these templates to turn the attachments into content assets, which are then automatically added to the
package.

**•** Enhanced email template folders have these behaviors:

**–** If a package includes an enhanced email template folder, the target organization must have enhanced folders enabled for the
deploy to succeed.

**–** If an email template is in a subfolder, adding the root folder to a package doesn’t automatically add the email template to the
package. If the email template is in the root folder, it’s automatically added to the package.

**–** You can’t package an email template in the default public and private folders.

**•** For merge fields based on custom fields that are used in the Recipients prefix (for leads and contacts), we add references to those
merge fields. If the custom field is renamed, the reference in the template isn’t updated. Edit the custom merge field to use the new
field name and update the reference.

Note: An email template created in Email Template Builder can’t be edited after it’s downloaded. To edit the template, clone it.

When upgrading a package that has Email Template Builder email templates, only the associated FlexiPage is updated. After
downloading the new version of the template, clone it to see the changes.

### Embedded Service Config

Represents a setup node for creating an Embedded Service for Web deployment.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: First-Generation Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit


### Second-Generation Managed Packages Embedded Service Menu Settings

**•** None

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: EmbeddedServiceConfig

**Documentation**
_Metadata API Developer Guide:_ [EmbeddedServiceConfig](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_embeddedserviceconfig.htm)

_Salesforce Help:_ [Embedded Chat](https://help.salesforce.com/s/articleView?id=service.snapins_chat_overview.htm&type=5&language=en_US)

### Embedded Service Menu Settings

Represents a setup node for creating a channel menu deployment. Channel menus list the ways in which customers can contact your
business.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: First-Generation Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** None

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** None


### Second-Generation Managed Packages Enablement Measure Definition

More Information

**Feature Name**
Metadata Name: EmbeddedServiceMenuSettings

**Documentation**
_Metadata API Developer Guide:_ [EmbeddedServiceMenuSettings](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_embeddedservicemenusettings.htm)

_Salesforce Help:_ [Channel Menu Setup](https://help.salesforce.com/s/articleView?id=service.embedded_chat_channel_menu.htm&type=5&language=en_US)

### Enablement Measure Definition

Represents an Enablement measure, which specifies the job-related activity that a user performs to complete a milestone or outcome
in an Enablement program. A measure identifies a source object and optional related objects, with optional field filters and filter logic,
for tracking the activity.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** All but Status and DeveloperName

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** DeveloperName


### Second-Generation Managed Packages Enablement Program Definition

More Information

**Feature Name**
Metadata Name: EnablementMeasureDefinition

**Use Case**

Include this component in a package with a program if the program has outcomes or milestones.

**Considerations When Packaging**
[See Considerations for Packaging Enablement Programs and Dependencies.](https://developer.salesforce.com/docs/sales/enablement/guide/enablement-package-considerations.html)

**License Requirements**
Enablement add-on license and the Enablement permission set license are required. For Partner Enablement programs in supported
[Experience Cloud sites, a supported Partner Relationship Management (PRM) add-on license is also required.](https://help.salesforce.com/s/articleView?id=slack.prm_support_license_template.htm&type=5&language=en_US)

**Usage Limits**
[See Enablement Limits.](https://help.salesforce.com/s/articleView?id=sales.enablement_limits.htm&type=5&language=en_US)

**Relationship to Other Components**
An Enablement measure is used within an Enablement program. Package the Enablement Measure Definition component with the
### Enablement Program Definition component. Or, package the Enablement Measure Definition component separately. Each measure

references a source object and optional related objects.

**Documentation**

**•** _Salesforce Help_ [: Sales Programs and Partner Tracks with Enablement](https://help.salesforce.com/s/articleView?id=sales.enablement.htm&type=5&language=en_US)

**•** _Metadata API Developer Guide_ [: EnablementMeasureDefinition](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_enablementmeasuredefinition.htm)

**•** _Sales Programs and Partner Tracks with Enablement Developer Guide_ [: Create a Managed Package for Enablement Programs,](https://developer.salesforce.com/docs/sales/enablement/guide/enablement-package.html)
[Measures, and Content](https://developer.salesforce.com/docs/sales/enablement/guide/enablement-package.html)

### Enablement Program Definition

Represents an Enablement program, which includes exercises and measurable milestones to help users such as sales reps achieve specific
outcomes related to your company’s revenue goals.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP)

Component Is Updated During Package Upgrade No

Subscriber Can Delete Component From Org Yes

Package Developer Can Remove Component From Package Yes

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.


Second-Generation Managed Packages Enablement Program Definition

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** None

Both Package Developer and Subscriber Can Edit

**•** All but DeveloperName

Neither Package Developer or Subscriber Can Edit

**•** DeveloperName

More Information

**Feature Name**
Metadata Name: EnablementProgramDefinition

**Use Case**

Include this component in a package when you want to move a program from one org to another.

**Considerations When Packaging**
[See Considerations for Packaging Enablement Programs and Dependencies.](https://developer.salesforce.com/docs/sales/enablement/guide/enablement-package-considerations.html)

**License Requirements**
Enablement add-on license and the Enablement permission set license are required. For Partner Enablement programs in supported
[Experience Cloud sites, a supported Partner Relationship Management (PRM) add-on license is also required.](https://help.salesforce.com/s/articleView?id=slack.prm_support_license_template.htm&type=5&language=en_US)

**Usage Limits**
[See Enablement Limits.](https://help.salesforce.com/s/articleView?id=sales.enablement_limits.htm&type=5&language=en_US)

**Relationship to Other Components**
An Enablement program can contain other items that are related to other packageable components. Package the Enablement
Program Definition component with other appropriate components.

**•** Exercises that reference Digital Experiences content. Package the Digital Experience component.

**•** Exercises that reference assessment surveys. Package the Flow component.

**•** Custom exercise types that reference user-defined content. Package the Learning Item Type and Enablement Program Task
Subcategory components.

**•** Measures that track job-related activity using specific objects. Package the Enablement Measure Definition component.

**Documentation**

**•** _Salesforce Help_ [: Sales Programs and Partner Tracks with Enablement](https://help.salesforce.com/s/articleView?id=sales.enablement.htm&type=5&language=en_US)

**•** _Metadata API Developer Guide_ [: EnablementMeasureDefinition](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_enablementmeasuredefinition.htm)

**•** _Sales Programs and Partner Tracks with Enablement Developer Guide_ [: Create a Managed Package for Enablement Programs,](https://developer.salesforce.com/docs/sales/enablement/guide/enablement-package.html)
[Measures, and Content](https://developer.salesforce.com/docs/sales/enablement/guide/enablement-package.html)


### Second-Generation Managed Packages Enablement Program Task Subcategory Enablement Program Task Subcategory

Represents a custom exercise type that an Enablement admin adds to an Enablement program in Program Builder. A custom exercise
type also requires a corresponding EnblProgramTaskDefinition record for Program Builder and corresponding LearningItem and
LearningItemType records for when users take the exercise in the Guidance Center.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** All but DeveloperName

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** DeveloperName

More Information

**Feature Name**
Metadata Name: EnblProgramTaskSubCategory

**Use Case**

Include this component in a package with a program if the program has a custom exercise type.

**Considerations When Packaging**
[See Considerations for Packaging Enablement Programs and Dependencies.](https://developer.salesforce.com/docs/sales/enablement/guide/enablement-package-considerations.html)

**License Requirements**
Enablement add-on license and the Enablement permission set license are required.


### Second-Generation Managed Packages Entitlement Template

Important: Custom exercises aren’t compatible with Partner Enablement programs.

**Usage Limits**
[See Enablement Limits.](https://help.salesforce.com/s/articleView?id=sales.enablement_limits.htm&type=5&language=en_US)

**Relationship to Other Components**
The Enablement Program Task Subcategory component requires a corresponding Learning Item Type component. Both components
are used with custom exercise types in Enablement programs. Package both of these components with an Enablement Program
Definition component.

**Documentation**

**•** _Salesforce Help_ [: Sales Programs and Partner Tracks with Enablement](https://help.salesforce.com/s/articleView?id=sales.enablement.htm&type=5&language=en_US)

**•** _Metadata API Developer Guide_ [: EnblProgramTaskSubCategory](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_enblprogramtasksubcategory.htm)

**•** _Metadata API Developer Guide_ [: LearningItemType](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_learningitemtype.htm)

**•** _Object Reference for the Salesforce Platform_ [: EnblProgramTaskDefinition](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_enblprogramtaskdefinition.htm)

**•** _Object Reference for the Salesforce Platform_ [: LearningItem](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_learningitem.htm)

**•** _Sales Programs and Partner Tracks with Enablement Developer Guide_ [: Create a Managed Package for Enablement Programs,](https://developer.salesforce.com/docs/sales/enablement/guide/enablement-package.html)
[Measures, and Content](https://developer.salesforce.com/docs/sales/enablement/guide/enablement-package.html)

**•** _Sales Programs and Partner Tracks with Enablement Developer Guide_ [: Implement Custom Exercise Types for Enablement Programs](https://developer.salesforce.com/docs/sales/enablement/guide/enablement-custom-exercises-intro.html)

### Entitlement Template

Represents an entitlement template. Entitlement templates are predefined terms of customer support that you can quickly add to
products.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: First-Generation Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** None

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** None


### Second-Generation Managed Packages ESignature Config

More Information

**Feature Name**
Metadata Name: EntitlementTemplate

**Documentation**
_Metadata API Developer Guide:_ [EntitlementTemplate](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_entitlementtemplate.htm)

_Salesforce Help:_ [Set Up an Entitlement Template](https://help.salesforce.com/s/articleView?id=service.entitlements_setting_up_templates.htm&type=5&language=en_US)

### ESignature Config

Using the Electronic Signature Configuration setup, the system admin must define the required configurations to support the e-signature
APIs and UI.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade No

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Both Package Developer and Subscriber Can Edit

**•** Config Type

**•** Config Value

**•** Description

**•** Group Type

**•** Vendor

Neither Package Developer or Subscriber Can Edit

**•** DeveloperName

**•** MasterLabel

More Information

**Feature Name**
Metadata Name: ESignatureConfig

**Use Case**
Allows users to get the electronic signatures on their documents.


### Second-Generation Managed Packages ESignature Envelope Config

**License Requirements**
DocGen Designer (Permission Set License)

### ESignature Envelope Config

Using the Electronic Signature Envelope Config the system admin can define the default reminders and expiry for the envelopes submitted
for eSignature.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade No

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Both Package Developer and Subscriber Can Edit

**•** Expiration Enabled

**•** Expiration Period

**•** Expiration Warning Period

**•** First Reminder Period

**•** Reminder Enabled

**•** Reminder Interval Period

**•** Target Object Name

**•** Vendor

**•** Vendor Account Identifier

**•** Vendor Default Notification Enabled

Neither Package Developer or Subscriber Can Edit

**•** DeveloperName

**•** MasterLabel

More Information

**Feature Name**
Metadata Name: ESignatureEnvelopeConfig


### Second-Generation Managed Packages Event Relay

**Use Case**
Allows users to get the electronic signatures and notifications on their documents.

**License Requirements**
DocGen Designer (Permission Set License)

**Documentation**
_Metadata API Developer Guide:_ [ESignatureEnvelopeConfig](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_esignatureenvelopeconfig.htm)

### Event Relay

Represents an event relay that you can use to send platform events and change data capture events from Salesforce to Amazon
EventBridge.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** None

Both Package Developer and Subscriber Can Edit

**•** `Label`

**•** `RelayOption`

**•** `State`

Neither Package Developer or Subscriber Can Edit

**•** `DestinationResourceName`

**•** `EventChannel`

**•** `UsageType`

More Information

**Feature Name**
Metadata Name: EventRelayConfig

Component Type in 1GP Package Manager UI: Event Relay


### Second-Generation Managed Packages Explainability Action Definition

**Documentation**
_Metadata API Developer Guide:_ [EventRelayConfig](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_eventrelayconfig.htm)

### Explainability Action Definition

Define where the metadata for your Decision Explainer business rules are stored in Public Sector Solutions.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade No

Subscriber Can Delete Component From Org Yes

Package Developer Can Remove Component From Package Yes

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** None

Both Package Developer and Subscriber Can Edit

**•** Label

**•** Description

**•** Developer Name

**•** Business Process Type

**•** Application Type

**•** Action Log Schema Type

**•** Application Subtype

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: ExplainabilityActionDefinition


### Second-Generation Managed Packages Explainability Action Version Explainability Action Version

Define and store versions of the explainability actions used by your Decision Explainer business rules in Public Sector Solutions.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade No

Subscriber Can Delete Component From Org Yes

Package Developer Can Remove Component From Package Yes

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** None

Both Package Developer and Subscriber Can Edit

**•** Label

**•** Active

**•** Description

**•** Explainability Action Definition

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: ExplainabilityActionVersion

### Explainability Message Template

Represents information about the template that contains the decision explanation message for a specified expression set step type.


### Second-Generation Managed Packages Expression Set Definition

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade No

Subscriber Can Delete Component From Org Yes

Package Developer Can Remove Component From Package Yes

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** None

Both Package Developer and Subscriber Can Edit

**•** Label

**•** Message

**•** Name

**•** Result Type

**•** Default

**•** Expression Set Step Type

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: ExplainabilityMsgTemplate

**Documentation**
_Industries Common Resources Developer Guide:_ [ExplainabilityMsgTemplate](https://developer.salesforce.com/docs/atlas.en-us.262.0.industries_reference.meta/industries_reference/meta_explainabilitymsgtemplate.htm)

_Salesforce Help:_ [Create Explainability Message Templates](https://help.salesforce.com/s/articleView?id=ind.create_explainability_message_templates.htm&type=5&language=en_US)

### Expression Set Definition

Represents an expression set definition.


Second-Generation Managed Packages Expression Set Definition

Note: 2GP support for Business Rules Engine Components is a pilot or beta service that is subject to the Beta Services Terms at
[Agreements - Salesforce.com](https://www.salesforce.com/company/legal/agreements/) or a written Unified Pilot Agreement if executed by Customer, and applicable terms in the [Product](https://ptd.salesforce.com/)
[Terms Directory. Use of this pilot or beta service is at the Customer's sole discretion.](https://ptd.salesforce.com/)

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes. Only if the component doesn’t contain any active versions.

Subscriber Can Delete Component From Org Yes. Only if the component doesn’t contain any active versions.

Package Developer Can Remove Component From Package Yes. Only if the component doesn’t contain any active versions.

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** None

Both Package Developer and Subscriber Can Edit

**•** versions

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: ExpressionSetDefinition

Component Type in 1GP Package Manager UI: ExpressionSet Definition

**Relationship to Other Components**
To use this component, any expression set version dependencies such as decision matrices, decision tables, object field aliases, and
subexpressions must be present in the target org.

**Documentation**
_Industries Common Resources Developer Guide:_ [Expression Set Definition](https://developer.salesforce.com/docs/atlas.en-us.262.0.industries_reference.meta/industries_reference/meta_expressionsetdefinition.htm)

_Salesforce Help:_ [Expression Set Migration Considerations](https://help.salesforce.com/s/articleView?id=sf.expression_set_migration_considerations.htm&type=5&language=en_US)


### Second-Generation Managed Packages Expression Set Definition Version Expression Set Definition Version

Represents a definition of an expression set version.

Note: 2GP support for Business Rules Engine Components is a pilot or beta service that is subject to the Beta Services Terms at
[Agreements - Salesforce.com](https://www.salesforce.com/company/legal/agreements/) or a written Unified Pilot Agreement if executed by Customer, and applicable terms in the [Product](https://ptd.salesforce.com/)
[Terms Directory. Use of this pilot or beta service is at the Customer's sole discretion.](https://ptd.salesforce.com/)

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes. Only if the component is in an inactive state.

Subscriber Can Delete Component From Org Yes. Only if the component is in an inactive state.

Package Developer Can Remove Component From Package No

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** None

Both Package Developer and Subscriber Can Edit

**•** variables

**•** steps

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: ExpressionSetDefinitionVersion

Component Type in 1GP Package Manager UI: Expression Set Definition Version

**Relationship to Other Components**
This component can be used only if the ExpressionSetDefinition to which this ExpressionSetDefinitionVersion component belongs
is present in the target org.


### Second-Generation Managed Packages Expression Set Object Alias

To use this component, any expression set version dependencies such as decision matrices, decision tables, object field aliases, and
subexpressions must be present in the target org.

**Documentation**
_Industries Common Resources Developer Guide:_ [Expression Set Definition Version](https://developer.salesforce.com/docs/atlas.en-us.262.0.industries_reference.meta/industries_reference/meta_expressionsetdefinition.htm)

_Salesforce Help:_ [Expression Set Migration Considerations](https://help.salesforce.com/s/articleView?id=sf.expression_set_migration_considerations.htm&type=5&language=en_US)

### Expression Set Object Alias

Represents information about the alias of the source object that’s used in an expression set.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** mappings.sourceFieldName

**•** mappings.fieldAlias

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** objectApiName

**•** usageType

**•** dataType

More Information

**Feature Name**
Metadata Name: ExpressionSetObjectAlias

Component Type: Expression Set Object Alias

**Use Case**
Expression set object aliases allow you to use object fields as variables in expression sets. Aliases are relevant and user-friendly names
that are created for underlying source object fields. Field aliases are grouped under an object alias.


### Second-Generation Managed Packages Expression Set Message Token

**Documentation**
_Industries Common Resources Developer Guide:_ [ExpressionSetObjectAlias](https://developer.salesforce.com/docs/atlas.en-us.262.0.industries_reference.meta/industries_reference/meta_expressionsetobjectalias.htm)

_Salesforce Help:_ [Object Variables in Expression Sets](https://help.salesforce.com/s/articleView?id=ind.object_variables_in_expression_sets.htm&type=5&language=en_US)

### Expression Set Message Token

Represents a token that's used in an explainability message template. The token can be replaced with an expression set version resource
that the template is used in. This object is available in API version 59.0 and later.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade No

Subscriber Can Delete Component From Org Yes

Package Developer Can Remove Component From Package Yes

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** None

Both Package Developer and Subscriber Can Edit

**•** Master Label

**•** Developer Name

**•** Description

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: ExpressionSetMessageToken


### Second-Generation Managed Packages External Auth Identity Provider

Component Type in 1GP Package Manager UI: ExpressionSetMessageToken

**Documentation**
_Industries Common Resources Developer Guide:_ [ExpressionSetMessageToken](https://developer.salesforce.com/docs/atlas.en-us.250.0.industries_reference.meta/industries_reference/tooling_api_objects_expressionsetmessagetoken.htm)

_Salesforce Help:_ [Create Expression Set Message Tokens](https://help.salesforce.com/s/articleView?id=ind.task_create_expression_set_message_tokens.htm&type=5&language=en_US)

### External Auth Identity Provider

Represents the external auth identity provider that obtains OAuth tokens for callouts that use named credentials.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes. Supported in 2GP packages only.

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

Editable Properties After Package Promotion or Installation

Note: In addition to these properties, the Description, ParameterName, ParameterType, ParameterValue, and SequenceNumber
properties have the same editability as the ExternalAuthIdentityProviderParameters they’re included in.

Only Package Developer Can Edit

**•** AuthenticationFlow

**•** AuthenticationProtocol

**•** Description

**•** Label

Both Package Developer and Subscriber Can Edit

**•** ExternalAuthIdentityProviderParameter

**–** AuthorizeUrl

**–** ClientAuthentication

**–** Description

**–** IdentityProviderOptions


### Second-Generation Managed Packages External Client App Canvas Settings

**–** ParameterName

**–** ParameterType

**–** ParameterValue

**–** RefreshRequestBodyParameter

**–** RefreshRequestHttpHeader

**–** RefreshRequestQueryParameter

**–** SequenceNumber

**–** StandardExternalIdentityProvider

**–** TokenRequestBodyParameter

**–** TokenRequestHttpHeader

**–** TokenRequestQueryParameter

**–** TokenUrl

**–** UserInfoUrl

Neither Package Developer or Subscriber Can Edit

**•** FullName

More Information

**Feature Name**
Metadata Name: ExternalAuthIdentityProvider

Component Type in 1GP Package Manager UI: External Auth Identity Provider

**Considerations When Packaging**
Though external auth identity providers are represented by metadata, the standard Metadata API can’t fully expose and render
sensitive information like tokens in plain text. This means that sensitive values such as client secrets aren’t included in packages.

Package upgrades delete any additional custom request parameters that subscribers add after installing the package. Alert subscribers
that they must recreate custom parameters.

Package developers can only create parameters and delete existing parameters. After package installation, subscribers don’t receive
updated parameter values from package upgrades.

**Relationship to Other Components**
A callout to an external system references a named credential, which in turn links to an external credential. For external credentials
that use OAuth 2.0 authentication, external auth identity providers obtain the OAuth tokens necessary for outbound callouts.

**Documentation**
_Salesforce Help:_ [Named Credentials](https://help.salesforce.com/s/articleView?id=xcloud.named_credentials_about.htm&type=5&language=en_US)

_Named Credentials Developer Guide:_ [Named Credentials Packaging Guide](https://developer.salesforce.com/docs/platform/named-credentials/guide/nc-packaging-dev-guide.html)

_Metadata API Developer Guide:_ [ExternalAuthIdentityProvider](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_externalauthidentityprovider.htm)

### External Client App Canvas Settings

Represents an external client app's canvas app settings.


Second-Generation Managed Packages External Client App Canvas Settings

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** All properties

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: ExtlClntAppCanvasSettings

**Considerations When Packaging**
Unlike most metadata, External Client Apps can’t be created via the Setup menu in a scratch org. ISVs who intend to package External
Client Apps in a managed 2GP should instead define the External Client App in their PBO (Partner Business Org) Dev Hub. The External
Client App can then be retrieved via Salesforce CLI and deployed into a scratch org, or packaged and installed into a scratch org for
[testing. See Configure Packageable External Client Apps for more information.](https://help.salesforce.com/s/articleView?id=xcloud.configure_packageable_external_client_apps.htm&type=5&language=en_US)

**Relationship to Other Components**
External Client App plugins like the canvas plugin include two types of configurations: settings and policies. All settings are determined
by the external client app developer and can’t be edited by the admin for the subscriber org. Admin-controlled configurations are
called policies. ExtlClntAppCanvasSettings contains all of the packageable configurations for the External Client Apps canvas plugin.

**Documentation**
_Salesforce Help:_ [External Client Apps](https://help.salesforce.com/s/articleView?id=xcloud.external_client_apps.htm&type=5&language=en_US)

_Metadata API Developer Guide:_ [ExtlClntAppCanvasSettings](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_extlclntappcanvassettings.htm)

_Canvas Developer Guide:_ [Introducing Canvas](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_connect.meta/platform_connect/canvas_framework_intro.htm)


### Second-Generation Managed Packages External Client App Header External Client App Header

Represents the header file for an external client application configuration.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org Yes

Package Developer Can Remove Component From Package No

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** All properties

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: ExternalClientApplication

**Considerations When Packaging**
Unlike most metadata, External Client Apps can’t be created via the Setup menu in a scratch org. ISVs who intend to package External
Client Apps in a managed 2GP should instead define the External Client App in their PBO (Partner Business Org) Dev Hub. The External
Client App can then be retrieved via Salesforce CLI and deployed into a scratch org, or packaged and installed into a scratch org for
[testing. See Configure Packageable External Client Apps for more information.](https://help.salesforce.com/s/articleView?id=xcloud.configure_packageable_external_client_apps.htm&type=5&language=en_US)

**Relationship to Other Components**
ExternalClientApplication is the header file for an external client app. This defines the basic configurations of the external client app,
including whether the external client app can be packaged or if it is developed for local use only.

ExtlClntAppGlobalOauthSettings includes sensitive information for the External Client Apps OAuth plugin, like OAuth consumer
credentials that can’t be packaged or added to source control. ExtlClntAppOauthSettings includes packageable configurations. All
settings are determined by the developer and can’t be edited by the admin. Admin-controlled configurations are called policies and
are included in ExtlClntAppOauthConfigurablePolicies.

**Documentation**
_Salesforce Help:_ [External Client Apps](https://help.salesforce.com/s/articleView?id=xcloud.external_client_apps.htm&type=5&language=en_US)

_Salesforce Help:_ [Configure Packageable External Client Apps](https://help.salesforce.com/s/articleView?id=xcloud.configure_packageable_external_client_apps.htm&type=5&language=en_US)


### Second-Generation Managed Packages External Client App Notification Settings External Client App Notification Settings

Represents the settings configuration for the external client app’s notifications plugin.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** All properties

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: ExtlClntAppNotificationSettings

**Considerations When Packaging**
Unlike most metadata, External Client Apps can’t be created via the Setup menu in a scratch org. ISVs who intend to package External
Client Apps in a managed 2GP should instead define the External Client App in their PBO (Partner Business Org) Dev Hub. The External
Client App can then be retrieved via Salesforce CLI and deployed into a scratch org, or packaged and installed into a scratch org for
[testing. See Configure Packageable External Client Apps for more information.](https://help.salesforce.com/s/articleView?id=xcloud.configure_packageable_external_client_apps.htm&type=5&language=en_US)

**Relationship to Other Components**
ExtlClntAppNotificationSettings contains all of the packageable configurations for the External Client Apps notifications plugin.

**Documentation**
_Salesforce Help:_ [External Client Apps](https://help.salesforce.com/s/articleView?id=xcloud.external_client_apps.htm&type=5&language=en_US)

[ExtlClntAppNotificationSettings](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_extlclntappnotificationsettings.htm)


### Second-Generation Managed Packages External Client App OAuth Settings External Client App OAuth Settings

Represents the settings configuration for the external client app’s OAuth plugin.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** All properties

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: ExtlClntAppOauthSettings

**Considerations When Packaging**
Unlike most metadata, External Client Apps can’t be created via the Setup menu in a scratch org. ISVs who intend to package External
Client Apps in a managed 2GP should instead define the External Client App in their PBO (Partner Business Org) Dev Hub. The External
Client App can then be retrieved via Salesforce CLI and deployed into a scratch org, or packaged and installed into a scratch org for
[testing. See Configure Packageable External Client Apps for more information.](https://help.salesforce.com/s/articleView?id=xcloud.configure_packageable_external_client_apps.htm&type=5&language=en_US)

**Relationship to Other Components**
External Client App plugins like the OAuth plugin include two types of configurations: settings and policies. All settings are determined
by the external client app developer and can’t be edited by the admin for the subscriber org. Admin-controlled configurations are
called policies.

ExtlClntAppOauthSettings contains all of the packageable configurations for the External Client Apps OAuth plugin. Sensitive
information, like OAuth consumer credentials that can’t be packaged or added to source control, are stored in the


### Second-Generation Managed Packages External Client App Push Settings

ExtlClntAppGlobalOauthSettings. Policies are saved in ExtlClntAppOauthConfigurablePolicies, which is not packaged but is generated
with default values at runtime.

**Documentation**
_Salesforce Help:_ [External Client Apps](https://help.salesforce.com/s/articleView?id=xcloud.external_client_apps.htm&type=5&language=en_US)

### External Client App Push Settings

Represents the settings configuration for the external client app’s push notification plugin.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** All properties

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: ExtlClntAppPushSettings

**Considerations When Packaging**

Unlike most metadata, External Client Apps can’t be created via the Setup menu in a scratch org. ISVs who intend to package External
Client Apps in a managed 2GP should instead define the External Client App in their PBO (Partner Business Org) Dev Hub. The External
Client App can then be retrieved via Salesforce CLI and deployed into a scratch org, or packaged and installed into a scratch org for
[testing. See Configure Packageable External Client Apps for more information.](https://help.salesforce.com/s/articleView?id=xcloud.configure_packageable_external_client_apps.htm&type=5&language=en_US)


### Second-Generation Managed Packages External Credential

To deploy ExtlClntAppPushSettings retrieved from the Dev Hub org, delete androidPushConfig or applePushConfig from the metadata
file.

**Relationship to Other Components**

External Client App plugins like the push notification plugin include two types of configurations: settings and policies. All settings
are determined by the external client app developer and can’t be edited by the admin for the subscriber org. Admin-controlled
configurations are called policies.

ExtlClntAppPushSettings contains all of the packageable configurations for the External Client Apps push notifcation plugin. Sensitive
information, like APNS or Firebase consumer credentials that can’t be packaged or added to source control, are stored in the
ExtlClntAppApplePushConfig and ExtlClntAppAndroidPushConfig, respectively. Policies are saved in
ExtlClntAppSamlConfigurablePolicies, which is not packaged but is generated with default values at runtime.

**Documentation**
_Salesforce Help:_ [External Client Apps](https://help.salesforce.com/s/articleView?id=xcloud.external_client_apps.htm&type=5&language=en_US)

[ExtlClntAppPushSettings](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_extlclntapppushsettings.htm)

### External Credential

Represents the details of how Salesforce authenticates to the external system.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes. Supported in 2GP packages only.

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

Editable Properties After Package Promotion or Installation

Note: In addition to these properties, the Description, ParameterGroup, ParameterName, ParameterValue, and SequenceNumber
properties have the same editability as the ExternalCredentialParameters they’re included in.

Only Package Developer Can Edit

**•** Label

**•** AuthenticationProtocol


Second-Generation Managed Packages External Credential

**•** ExternalCredentialParameters

**–** AuthProtocolVariant

Both Package Developer and Subscriber Can Edit

**•** Description

**•** ExternalCredentialParameters

**–** AuthHeader

**–** AuthProvider (only subscriber editable in 2GP)

**–** AuthProviderUrl

**–** AuthProviderUrlQueryParameter

**–** AuthParameter

**–** AwsStsPrincipal (only for external credentials that use AWS Signature v4 authentication with STS)

**–** Description

**–** JwtBodyClaim

**–** JwtHeaderClaim

**–** NamedPrincipal

**–** PerUserPrincipal

**–** SequenceNumber

**–** SigningCertificate (only subscriber editable in 2GP)

Neither Package Developer or Subscriber Can Edit

**•** FullName

More Information

**Feature Name**
Metadata Name: `ExternalCredential`

**Considerations When Packaging**
Though named and external credentials are represented by metadata, the standard Metadata API can’t fully expose the definition
of a credential and render sensitive information like tokens in plain text. This means that packaged named credentials don’t include
the access tokens or certificates that are needed to perform authenticated callouts. You can create the external credential’s principal
or populate its tokens or certificates in the UI or via the Connect API.

In managed 1GP packages, external credentials that use the OAuth 2.0 authentication protocol must reference an authentication
provider to capture the details of the authorization endpoint. If you add an external credential that references an authentication
[provider, the authentication provider is added to the package. See Authentication Providers for information on which elements of](https://help.salesforce.com/s/articleView?id=experience.sso_authentication_providers.htm&type=5&language=en_US)
an authentication provider are and aren’t packageable.

In managed 2GP packages, if an external credential uses an authentication provider to capture the details of the authorization
endpoint, you can’t include the reference to the authentication provider in the package. If the external credential references an
authentication provider, you must recreate the authentication provider in the subscriber org and add it to the external credential.

**Post Install Steps**
After installing an external credential from a managed or unmanaged package, you must:

**•** Create the external credential’s principal or populate its tokens or certificates in the UI or via the Connect API.

**•** Give permission sets and profiles access to the principals of the external credential. See Enable External Credential Principals.


### Second-Generation Managed Packages External Data Connector

**•** Reauthenticate to the external system.

**–** For a Named Principal, the admin must go to **Setup > Named Credential > External Credential** to authenticate.

**–** For a Per User Principal, each user must go to **My Personal Information > External Credential** to authenticate.

**Relationship to Other Components**
ExternalCredential can be added to a package without a NamedCredential, but NamedCredential must be packaged with an
ExternalCredential.

The named credential defines a callout endpoint and an HTTP transport protocol, while the external credential represents the details
of how Salesforce authenticates to an external system via an authentication protocol. Each named credential must be mapped to
at least one external credential.

**Documentation**
_Salesforce Help:_ [Named Credentials](https://help.salesforce.com/s/articleView?id=xcloud.named_credentials_about.htm&type=5&language=en_US)

_Named Credentials Developer Guide:_ [Named Credentials Packaging Guide](https://developer.salesforce.com/docs/platform/named-credentials/guide/nc-packaging-dev-guide.html)

_Metadata API Developer Guide:_ [ExternalCredential](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_externalcredential.htm)

### External Data Connector

Used to represent the object where the data was sourced.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP)

Component Is Updated During Package Upgrade No

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** None

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** DataConConfiguration

**•** DataConnectionStatus

**•** DataConnectorType

**•** DataPlatform


### Second-Generation Managed Packages External Data Source

**•** ExternalRecordId

More Information

**Feature Name**
Metadata Name: ExternalDataConnector

Component Type in 1GP Package Manager UI: Adding DataStreamDefinition or DataKitDefinition brings ExternalDataConnector for
S3 data streams.

**Use Case**
This component holds reference to Source Data Connector Metadata.

**License Requirements**
You need Customer 360 Audiences Corporate (cdpPsl) licenses on both package developer org and subscriber org.

**Post Install Steps**
User has to create DataStream via ui-api or using the Data Cloud App.

**Relationship to Other Components**

This isn’t a top-level entity. Add DataStreamDefinition or DataKitDefinition to pick up this entity.

### External Data Source

Represents the metadata associated with an external data source. Create external data sources to manage connection details for
integration with data and content that are stored outside your Salesforce org.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** Type

Both Package Developer and Subscriber Can Edit

**•** Auth Provider

**•** Certificate

**•** Custom Configuration


### Second-Generation Managed Packages External Data Transport Field Template

**•** Endpoint

**•** Identity Type

**•** OAuth Scope

**•** Password

**•** Protocol

**•** Username

Neither Package Developer or Subscriber Can Edit

**•** Name

More Information

**Feature Name**
Metadata Name: ExternalDataSource

Component Type in 1GP Package Manager UI: External Data Source

**Considerations When Packaging**

**•** After installing an external data source from a managed or unmanaged package, the subscriber must reauthenticate to the
external system.

**–** For password authentication, the subscriber must reenter the password in the external data source definition.

**–** For OAuth, the subscriber must update the callback URL in the client configuration for the authentication provider, then
reauthenticate by selecting `Start Authentication Flow on Save` on the external data source.

**•** Certificates aren’t packageable. If you package an external data source that specifies a certificate, make sure that the subscriber
org has a valid certificate with the same name.

**Documentation**
_Metadata API Developer Guide:_ [ExternalDataSource](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_externaldatasource.htm)

### External Data Transport Field Template

Represents the definition of a Data Cloud schema field.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes (supported only in 1GP packages)

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes (supported only in 1GP packages)

Component Has IP Protection No


### Second-Generation Managed Packages External Data Transport Field

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** DataSourceField

**•** ExternalDataTranField

**•** ExternalName

**•** IsDataRequired

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: ExtDataTranFieldTemplate

Component Type in 1GP Package Manager UI: External Data Transport Field Template

**Use Case**
ExtDataTranFieldTemplate represents the definition of a Data Cloud schema field the user includes in a data kit.

**Considerations When Packaging**
A Data Cloud feature is always packaged via a data kit. You add the external data transport field template to a data kit and then add
that data kit to a package. You can’t directly add this component to a package.

**License Requirements**
[For more information, see Data Cloud Standard Permission Sets in Salesforce Help.](https://help.salesforce.com/s/articleView?id=data.c360_a_userpermissions.htm&type=5&language=en_US)

**Post Install Steps**
After you install a package that contains a data kit, you must manually deploy the features from the installed data kit.

**Documentation**
_Data Cloud Developer Guide:_ [Packages and Data Kits](https://developer.salesforce.com/docs/platform/data-cloud-dev/guide/packages-data-kits.html)

_Salesforce Help:_ [Packaging in Data Cloud](https://help.salesforce.com/s/articleView?id=data.c360_a_packaging_in_customer_360_audiences.htm&type=5&language=en_US)

### External Data Transport Field

Use ExternalDataTranField to add a field to the ExternalDataTranObject in your managed packages. ExternalDataTranObject is a Data
Cloud schema object.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP)

Component Is Updated During Package Upgrade No

Subscriber Can Delete Component From Org Yes


Second-Generation Managed Packages External Data Transport Field

Package Developer Can Remove Component From Package No

Component Has IP Protection Yes

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** Length

**•** Precision

**•** Scale

**•** IsDataRequired

**•** ExternalName

**•** PrimaryIndexOrder

**•** DateFormat

**•** CreationType

**•** MktDataTranField

**•** Sequence

**•** IsImplicitFilteringRequired

**•** ExtDataTranFieldTemplate

**•** IsCurrencyIsoCode

Both Package Developer and Subscriber Can Edit

**•** CustomFieldDatatypes

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: ExternalDataTranField

**Use Case**
This component holds reference to ExternalDataTranObject metadata and represents the fields in the ExternalDataTranObject.

**License Requirements**
Data Cloud must be provisioned.

**Post Install Steps**
You must to create a data stream via ui-api or by using the Data Cloud App.

**Relationship to Other Components**
This isn’t a top-level entity. Add DataStreamDefinition to pick up this entity. This entity’s parent is ExternalDataTranObject.

**Documentation**
_Metadata API Developer Guide:_ [ExternalDataTranField](https://developer.salesforce.com/docs/atlas.en-us.254.0.api_meta.meta/api_meta/meta_externaldatatranobject.htm#subtype_ExternalDataTranField)


### Second-Generation Managed Packages External Data Transport Object Template External Data Transport Object Template

Represents the definition of a Data Cloud schema object.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes (supported only in 1GP packages)

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes (supported only in 1GP packages)

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** DataSourceObject

**•** ExternalDataTranObject

**•** ExternalName

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: ExtDataTranObjectTemplate

Component Type in 1GP Package Manager UI: External Data Transport Object Template

**Use Case**
ExtDataTranObjectTemplate represents the definition of a Data Cloud schema object the user includes in a data kit.

**Considerations When Packaging**
A Data Cloud feature is always packaged via a data kit. You add the external data transport object template to a data kit and then
add that data kit to a package. You can’t directly add this component to a package.

**License Requirements**
[For more information, see Data Cloud Standard Permission Sets in Salesforce Help.](https://help.salesforce.com/s/articleView?id=data.c360_a_userpermissions.htm&type=5&language=en_US)

**Post Install Steps**
After you install a package that contains a data kit, you must manually deploy the features from the installed data kit.


### Second-Generation Managed Packages External Data Transport Object

**Documentation**
_Data Cloud Developer Guide:_ [Packages and Data Kits](https://developer.salesforce.com/docs/platform/data-cloud-dev/guide/packages-data-kits.html)

_Salesforce Help:_ [Packaging in Data Cloud](https://help.salesforce.com/s/articleView?id=data.c360_a_packaging_in_customer_360_audiences.htm&type=5&language=en_US)

### External Data Transport Object

To include a Data Cloud schema object in your managed packages, add ExternalDataTranObject.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP)

Component Is Updated During Package Upgrade No

Subscriber Can Delete Component From Org Yes

Package Developer Can Remove Component From Package No

Component Has IP Protection Yes

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** AvailabilityStatus

**•** CreationType

**•** MktDataTranObject

**•** ObjectCategory

**•** ExtDataTranObjectTemplate

Both Package Developer and Subscriber Can Edit

**•** None

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: ExternalDataTranObject

**Use Case**
ExternalDataTranObject contains specific schema event information that is used to describe events for ingestion via Data Cloud
Ingestion API, Web, and Mobile connectors. This object is related to many child schema fields, ExternalDataTranField.

**License Requirements**
Data Cloud must be provisioned.


### Second-Generation Managed Packages External Document Storage Configuration

**Post Install Steps**
You must create a data stream via ui-api or by using the Data Cloud App.

**Relationship to Other Components**
This isn’t a top-level entity. Add DataStreamDefinition to pick up this entity. This entity’s parent is ExternalDataConnector.

**Documentation**
_Data Cloud Integration Guide:_ [Mobile and Web SDK Schema Quick Guide for Data Cloud](https://developer.salesforce.com/docs/data/data-cloud-int/guide/c360-a-mobile-web-sdk-schema-quick-guide.html)

_Data Cloud Integration Guide:_ [Requirements for Ingestion API Schema File](https://developer.salesforce.com/docs/data/data-cloud-int/guide/c360-a-ingestion-api-schema-req.html)

_Metadata API Developer Guide:_ [ExternalDataTranObject](https://developer.salesforce.com/docs/atlas.en-us.254.0.api_meta.meta/api_meta/meta_externaldatatranobject.htm)

### External Document Storage Configuration

Represents configuration, which admin makes in setup to specify the drive, path, and named credential to be used for storing documents
on external drives.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade No

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** None

Both Package Developer and Subscriber Can Edit

**•** Target Object

**•** Record Type

**•** External Document Storage Identifier

**•** Document Path

**•** Named Credential

**•** Storage Drive Type

Neither Package Developer or Subscriber Can Edit

**•** DeveloperName

**•** MasterLabel


### Second-Generation Managed Packages External Services

More Information

**Feature Name**
Metadata Name: ExternalDocStorageConfig

**Use Case**
Represents the configuration that the admin makes in Setup to specify the drive, path, and named credential to be used for storing
the documents on external drives.

**License Requirements**
Microsoft Word 365

**Documentation**
_Salesforce Help:_ [Configure External Document Storage for Contracts](https://help.salesforce.com/s/articleView?id=ind.sf_contracts_Configure_External_Document_Storage_for_Contracts.htm&type=5&language=en_US)

### External Services

Represents the External Service configuration for an org.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org Yes (If there are no dependencies on the External Services
registration and its actions from flows or other features)

Package Developer Can Remove Component From Package Yes. Supported in both 1GP and 2GP packages.

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** Description

**•** Label

**•** Schema

**•** Schema URL

Both Package Developer and Subscriber Can Edit


### Second-Generation Managed Packages Feature Parameter Boolean

**•** Named Credential

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: ExternalServiceRegistration

Component Type in 1GP Package Manager UI: ExternalServiceRegistration

**Considerations When Packaging**
Package developers must add named credential components to the External Services registration package. A subscriber can also
create a named credential in Salesforce. However, the subscriber must use the same name as the named credential specified in the
External Services registration that references it.

Create named credentials manually or with Apex. Be sure to add the named credential to a package so that subscriber orgs can
install it. When a subscriber org installs a named credential, it can use the Apex callouts generated by the External Services registration
process.

**Usage Limits**
_Salesforce Help:_ [External Services System Limits](https://help.salesforce.com/s/articleView?id=platform.external_services_schema_def_limits.htm&type=5&language=en_US)

**Documentation**
_Metadata API Developer Guide:_ [ExternalServiceRegistration](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_externalserviceregistration.htm)

_Salesforce Help:_ [External Services](https://help.salesforce.com/s/articleView?id=platform.external_services.htm&type=5&language=en_US)

### Feature Parameter Boolean

Represents a boolean feature parameter in the Feature Management App (FMA). Feature parameters let you drive app behavior and
track activation metrics in subscriber orgs that install your package.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade No. See note.

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No

Note: Feature parameters with a data flow direction set as LMO-to-Subscriber, can be updated in the LMO (License Management Org).
Feature parameters with a data flow direction set as Subscriber-to-LMO can be updated using Apex in the subscriber org. Neither of
these changes require a package upgrade.


### Second-Generation Managed Packages Feature Parameter Date

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** Master Label

**•** Value (When Data Flow Direction is set to `LMO to Subscriber` )

Both Package Developer and Subscriber Can Edit

**•** Value (When Data Flow Direction is set to `Subscriber to LMO` )

Neither Package Developer or Subscriber Can Edit

**•** Full Name

**•** Data Type

**•** Data Flow Direction

More Information

**Feature Name**
Metadata Name: FeatureParameterBoolean

Component Type in 1GP Package Manager UI: Feature Parameter Boolean

**Use Case**
Use LMO-to-Subscriber feature parameters to enable and disable your app’s features, or use Subscriber-to-LMO feature parameters
to track customer preferences and activation metrics.

**Considerations When Packaging**
Feature parameters are an extension of the License Management App (LMA), and because beta package versions can’t be registered
with the LMA, there are aspects of feature parameters that can’t be tested using a beta package version. If you use the default value,
you can test LMO-to-Subscriber values in beta package versions. You can’t test any Subscriber-to-LMO feature parameter values in
a beta managed package version.

**Usage Limits**
A package can include up to 200 feature parameters.

**Documentation**
_Metadata API Developer Guide:_ [FeatureParameterBoolean](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_featureparameterboolean.htm)

[Create Feature Parameters for Your Second-Generation Managed Package](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_dev2gp_fma_create_feature_parameters.htm)

[Create Feature Parameters in Your First-Generation Packaging Org](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/fma_create_feature_parameters.htm)

_Apex Reference Guide:_ [FeatureManagement Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_System_FeatureManagement.htm)

### Feature Parameter Date

Represents a date feature parameter in the Feature Management App (FMA). Feature parameters let you drive app behavior and track
activation metrics in subscriber orgs that install your package.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.


Second-Generation Managed Packages Feature Parameter Date

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade No. See note.

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No

Note: Feature parameters with a data flow direction set as LMO-to-Subscriber, can be updated in the LMO (License Management Org).
Feature parameters with a data flow direction set as Subscriber-to-LMO can be updated using Apex in the subscriber org. Neither of
these changes require a package upgrade.

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** Master Label

**•** Value (When Data Flow Direction is set to `LMO to Subscriber` )

Both Package Developer and Subscriber Can Edit

**•** Value (When Data Flow Direction is set to `Subscriber to LMO` )

Neither Package Developer or Subscriber Can Edit

**•** Full Name

**•** Data Type

**•** Data Flow Direction

More Information

**Feature Name**
Metadata Name: FeatureParameterDate

Component Type in 1GP Package Manager UI: Feature Parameter Date

**Use Case**
Use LMO-to-Subscriber feature parameters to enable and disable your app’s features, or use Subscriber-to-LMO feature parameters
to track customer preferences and activation metrics.

**Considerations When Packaging**
Feature parameters are an extension of the License Management App (LMA), and because beta package versions can’t be registered
with the LMA, there are aspects of feature parameters that can’t be tested using a beta package version. If you use the default value,
you can test LMO-to-Subscriber values in beta package versions. You can’t test any Subscriber-to-LMO feature parameter values in
a beta managed package version.

**Usage Limits**
A package can include up to 200 feature parameters.

**Documentation**
_Metadata API Developer Guide:_ [FeatureParameterDate](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_featureparameterdate.htm)

[Create Feature Parameters for Your Second-Generation Managed Package](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_dev2gp_fma_create_feature_parameters.htm)


### Second-Generation Managed Packages Feature Parameter Integer

[Create Feature Parameters in Your First-Generation Packaging Org](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/fma_create_feature_parameters.htm)

_Apex Reference Guide:_ [FeatureManagement Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_System_FeatureManagement.htm)

### Feature Parameter Integer

Represents an integer feature parameter in the Feature Management App (FMA). Feature parameters let you drive app behavior and
track activation metrics in subscriber orgs that install your package.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade No. See note.

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package No

Component Has IP Protection No

Note: Feature parameters with a data flow direction set as LMO-to-Subscriber, can be updated in the LMO (License Management Org).
Feature parameters with a data flow direction set as Subscriber-to-LMO can be updated using Apex in the subscriber org. Neither of
these changes require a package upgrade.

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** Master Label

**•** Value (When Data Flow Direction is set to `LMO to Subscriber` )

Both Package Developer and Subscriber Can Edit

**•** Value (When Data Flow Direction is set to `Subscriber to LMO` )

Neither Package Developer or Subscriber Can Edit

**•** Full Name

**•** Data Type

**•** Data Flow Direction

More Information

**Feature Name**
Metadata Name: FeatureParameterInteger

Component Type in 1GP Package Manager UI: Feature Parameter Integer


### Second-Generation Managed Packages FieldMappingConfig

**Use Case**
Use LMO-to-Subscriber feature parameters to enable and disable your app’s features, or use Subscriber-to-LMO feature parameters
to track customer preferences and activation metrics.

**Considerations When Packaging**
Feature parameters are an extension of the License Management App (LMA), and because beta package versions can’t be registered
with the LMA, there are aspects of feature parameters that can’t be tested using a beta package version. If you use the default value,
you can test LMO-to-Subscriber values in beta package versions. You can’t test any Subscriber-to-LMO feature parameter values in
a beta managed package version.

**Usage Limits**
A package can include up to 200 feature parameters.

**Documentation**
_Metadata API Developer Guide:_ [FeatureParameterInteger](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_featureparameterinteger.htm)

[Create Feature Parameters for Your Second-Generation Managed Package](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_dev2gp_fma_create_feature_parameters.htm)

[Create Feature Parameters in Your First-Generation Packaging Org](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/fma_create_feature_parameters.htm)

_Apex Reference Guide:_ [FeatureManagement Class](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_System_FeatureManagement.htm)

### FieldMappingConfig

Represents the configuration for fields mapped between a source object and one or more destination objects and fields. This object is
available in API version 63.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

This object is available only if the Fundraising Access license is enabled and the Fundraising User system permission is assigned to users.

Fields

### **Field Details**

```
Description

DeveloperName

```

**Type**
textarea

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the field mapping configuration.

**Type**
string


Second-Generation Managed Packages FieldMappingConfig

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unqiue name for FieldMappingConfig.

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
The language of the FieldMappingConfig.

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
Label for the FieldMappingConfig.

**Type**
string


Second-Generation Managed Packages FieldMappingConfig

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix associated with this object. Each Developer Edition organization that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can
refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

The namespace prefix can have one of the following values:

**•** In Developer Edition organizations, the namespace prefix is set to the namespace prefix
of the organization for all objects that support it. There is an exception if an object is in
an installed managed package. In that case, the object has the namespace prefix of the
installed managed package. This field’s value is the namespace prefix of the Developer
Edition organization of the package developer.

**•** In organizations that are not Developer Edition organizations, `NamespacePrefix`
is only set for objects that are part of an installed managed package. There is no
namespace prefix for all other objects.

```
ProcessType

SourceObjectId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the type of process that the field mapping configuration supports.

Possible values are:

**•** `ChangeRequest`

**•** `GiftEntry`

**•** `Incident`

**•** `Problem`

The default value is `GiftEntry` .

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The ID of the source object for all of the fields mapped in the configuration.

Possible values are:

**•** `GiftEntry`


### Second-Generation Managed Packages Field Set Field Set

Represents a field set. A field set is a grouping of fields. For example, you could have a field set that contains fields describing a user's
first name, middle name, last name, and business title.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes. Supported in both 1GP and 2GP packages.

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

[For more details on 2GP component removal, see Remove Metadata Components from Second-Generation Managed Packages.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_remove_md_components.htm)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** Description

**•** Label

**•** Available fields

Both Package Developer and Subscriber Can Edit

**•** Selected fields (only subscriber editable)

Neither Package Developer or Subscriber Can Edit

**•** Name

More Information

**Feature Name**
Metadata Name: FieldSet

Component Type in 1GP Package Manager UI: Field Set

**Considerations When Packaging**
Field sets in installed packages perform different merge behaviors during a package upgrade:


### Second-Generation Managed Packages Field Source Target Relationship

**If a package developer:** **Then in the package upgrade:**

Changes a field from **Unavailable** to **Available for the Field** The modified field is placed at the end of the upgraded field set
**Set** or **In the Field Set** in whichever column it was added to.

Adds a field The new field is placed at the end of the upgraded field set in
whichever column it was added to.

Changes a field from **Available for the Field Set** or **In the Field** The field is removed from the upgraded field set.
**Set** to **Unavailable**

Changes a field from **In the Field Set** to **Available for the Field** The change isn’t reflected in the upgraded field set.
**Set** (or vice versa)

Note: Subscribers aren’t notified of changes to their installed field sets. The developer must notify users of changes to released
field sets through the package release notes or other documentation. Merging has the potential to remove fields in your field
set.

When a field set is installed, a subscriber can add or remove any field.

**Documentation**
_Metadata API Developer Guide:_ [FieldSet](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_fieldset.htm)

### Field Source Target Relationship

Stores the relationships between a data model object (DMO) and its fields. For example, the Individual.Id field has a one-to-many
relationship (1:M) with the ContactPointEmail.PartyId field.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes

Component Has IP Protection No

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)


### Second-Generation Managed Packages Flow

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** CreationType

**•** DeveloperName

**•** MasterLabel

**•** RelationshipCardinality

**•** SourceField

**•** TargetField

Both Package Developer and Subscriber Can Edit

**•** LastDataChangeStatusDateTime

**•** LastDataChangeStatusErrorCode

**•** Status

Neither Package Developer or Subscriber Can Edit

**•** None

More Information

**Feature Name**
Metadata Name: FieldSrcTrgtRelationship

Component Type in 1GP Package Manager UI: Field Source Target Relationship

**License Requirements**
Data Cloud must be provisioned.

**Documentation**
_Metadata API Developer Guide:_ [FieldSrcTrgtRelationship](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_fieldsrctrgtrelationship.htm)

### Flow

Represents the metadata associated with a flow. With Flow, you can create an application that navigates users through a series of pages
to query and update records in the database. You can also execute logic and provide branching capability based on user input to build
dynamic applications.

Component Manageability Rules

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.

Packageable In: Second-Generation Managed Packages (2GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org Yes

Package Developer Can Remove Component From Package Yes. Supported in 2GP packages only.

Component Has IP Protection Yes, except a flow that is a template or overridable.


Second-Generation Managed Packages Flow

Note: When a package developer removes this component from a package, the component remains in a subscriber’s org after
they install the upgraded package. The admin of the subscriber’s org can then delete the component, if desired.

Removing components from managed 1GP or 2GP packages requires approval from Salesforce. To request access to the component
[removal feature, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/partnerSupport)

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** Entire flow

Both Package Developer and Subscriber Can Edit

**•** Flow Label

**•** Description

**•** Status

Neither Package Developer or Subscriber Can Edit

**•** Flow API Name

**•** URL

More Information

**Feature Name**
Metadata Name: Flow

**Use Case**
To repeat a business process automatically such as creating an account when some criteria are met or sending an email every week,
build a flow to save time and resources

**Considerations When Packaging**

**•** When you upload a package or package version, the active flow version is included. If the flow has no active version, the latest
version is packaged.

**•** To update a managed package with a different flow version, activate that version and upload the package again. Or deactivate
all versions of the flow, make sure the latest flow version is the one to distribute, and then upload the package.

**•** In a packaging org, you can’t delete a flow after you upload it to a released or beta first-generation managed package. You can
only delete a flow version from a packaging org after you upload it to a released or beta first-generation managed package, if:

**–** Salesforce Customer Support activated the Managed Component Deletion permission.

**–** The flow version is not the most recently packaged version of the flow.

**–** The flow version is not active.

**–** The flow version is not the only version.

**•** You can’t delete a flow from an installed package. To remove a packaged flow from your org, deactivate it and then uninstall
the package.

**•** If you have multiple versions of a flow installed from multiple unmanaged packages, you can’t remove only one version by
uninstalling its package. Uninstalling a package—managed or unmanaged—that contains a single version of the flow removes
the entire flow, including all versions.

**•** You can’t include flows in package patches.


### Second-Generation Managed Packages Flow Category

**•** An active flow in a package is active after it’s installed. The previous active version of the flow in the destination org is deactivated
