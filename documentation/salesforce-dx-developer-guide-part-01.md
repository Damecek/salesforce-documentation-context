# Salesforce DX Developer Guide

> Source: https://resources.docs.salesforce.com/latest/latest/en-us/sfdc/pdf/sfdx_dev.pdf
> Fetched: 2026-06-02T08:10:56Z
Salesforce DX Developer Guide

Version 67.0, Summer ’26

Last updated: May 22, 2026

© Copyright 2000–2026 Salesforce, Inc. All rights reserved. Salesforce is a registered trademark of Salesforce, Inc., as are other
names and marks. Other marks appearing herein may be trademarks of their respective owners.

CONTENTS

**Chapter 1:** How Salesforce Developer Experience (DX) Tooling Changes the Way You
Work **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1**

Get Started by Using a Sample Repo **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3**
Get Started by Creating a New DX Project **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4**

Get an Org to Play With and Set It as Your Dev Hub **. . . . . . . . . . . . . . . . . . . . . . . . . . . 5**
Install the Salesforce Platform Development Tools **. . . . . . . . . . . . . . . . . . . . . . . . . . . . 5**
Create a Salesforce DX Project **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6**
Authorize Your Dev Hub and Create a Scratch Org **. . . . . . . . . . . . . . . . . . . . . . . . . . . . 7**
Make a Change in Your Scratch Org And Retrieve It to Your Project **. . . . . . . . . . . . . . . . . 8**
Create an Apex Class and Deploy it To the Scratch Org **. . . . . . . . . . . . . . . . . . . . . . . . 10**
Create a Lightning Web Component and Deploy it to the Scratch Org **. . . . . . . . . . . . . . . 11**
Deploy All Customizations To a Sandbox **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11**
Add Project Files to Your VCS **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13**
Next Steps **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13**
Create an Application **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13**
Migrate or Import Existing Source **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14**
Release Notes **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14**

**Chapter 2:** Provide Developers Access to Salesforce DX Tools **. . . . . . . . . . . . . . . . . . 15**

Select and Enable a Dev Hub Org **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16**

Enable Unlocked Packaging **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17**
Enable Einstein Chatbot Features in Scratch Orgs **. . . . . . . . . . . . . . . . . . . . . . . . . . . . 17**
Enable Language Extension Packages (Beta) **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17**
Enable Source Tracking in Sandboxes **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17**

Enable Source Tracking for All Developer and Developer Pro Sandboxes **. . . . . . . . . . . . 18**
Enable Source Tracking in a Specific Sandbox **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19**
Add Salesforce DX Users **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19**

Determine Which License to Assign to Dev Hub Users **. . . . . . . . . . . . . . . . . . . . . . . . . 20**
Add a System Administrator or Standard User to Your Dev Hub Org **. . . . . . . . . . . . . . . 21**
Add a Developer User to Your Dev Hub Org **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22**
Add a Limited Access User to Your Dev Hub Org **. . . . . . . . . . . . . . . . . . . . . . . . . . . . 22**
Create and Assign a Permission Set to Developer Users **. . . . . . . . . . . . . . . . . . . . . . . 22**

**Chapter 3:** Project Setup **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24**

Sample Repository on GitHub **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25**
Create a Salesforce DX Project **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25**
Salesforce DX Project Structure and Source Format **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26**

Decomposed Metadata Types **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30**
How to Exclude Source When Syncing **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36**

**Contents**

Create a Salesforce DX Project from Existing Source **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40**
Convert Files in Metadata Format to Source Format **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42**
Salesforce DX Usernames and Orgs **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42**
Link a Namespace to a Dev Hub Org **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45**
Salesforce DX Project Configuration **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46**
Multiple Package Directories **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49**
Replace Strings in Code Before Deploying or Packaging **. . . . . . . . . . . . . . . . . . . . . . . . . . . 52**

Test String Replacements **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56**

**Chapter 4:** Authorization **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57**

Authorize an Org Using a Browser **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58**
Authorize an Org Using the JWT Flow **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59**

Authorize a Scratch Org Using the JWT Flow **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60**
Create a Private Key and Self-Signed Digital Certificate **. . . . . . . . . . . . . . . . . . . . . . . . . . . . 61**
Create an External Client App in Your Org **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62**

Get and Use the Consumer Key and Secret **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64**
Create a Connected App in Your Org **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64**
Use the Default Connected App Securely **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66**
Use an Existing Access Token **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67**
Authorize an Org Using Its SFDX Authorization URL **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68**
Authorization Information for an Org **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68**
View Org Authentication Secrets **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69**
Log Out of an Org **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70**

**Chapter 5:** Metadata Coverage **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71**

**Chapter 6:** Scratch Orgs **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72**

Supported Scratch Org Editions and Allocations **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75**
Build Your Own Scratch Org Definition File **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76**

Scratch Org Features **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81**
Scratch Org Settings **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 169**
Create a Scratch Org Based on an Org Shape **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 170**

Enable Org Shape for Scratch Orgs **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 171**
Org Shape Permissions **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 172**
Create and Manage Org Shapes **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 173**
Scratch Org Definition for Org Shape **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 174**
Troubleshoot Org Shape **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 175**
Create Scratch Orgs **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 178**
Scratch Org Snapshots **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 180**

Get Started with Scratch Org Snapshots **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 182**
Salesforce CLI Snapshot Commands **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 183**
Create a Scratch Org Snapshot **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 183**
Create a Snapshot for Use with Namespaced Scratch Orgs **. . . . . . . . . . . . . . . . . . . . 184**
Create a Scratch Org Based on a Snapshot **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 185**
Create a Package Version Based on a Snapshot **. . . . . . . . . . . . . . . . . . . . . . . . . . . . 187**

**Contents**

Manage and Maintain Your Snapshots **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 188**
Select the Salesforce Release for a Scratch Org **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 188**
Deploy Source From Your Project to the Scratch Org **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 191**
Retrieve Source from the Scratch Org to Your Project **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 193**
Scratch Org Users **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 195**

Create a Scratch Org User **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 196**
User Definition File for Customizing a Scratch Org User **. . . . . . . . . . . . . . . . . . . . . . . 198**
Generate or Change a Password for a Scratch Org User **. . . . . . . . . . . . . . . . . . . . . . 199**
Manage Scratch Orgs from the Dev Hub Org **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 201**
Scratch Org Error Codes **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 201**

**Chapter 7:** Sandboxes **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 203**

Authorize Your Production Org **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 204**
Create a Sandbox Definition File **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 204**
Create, Clone, or Refresh a Sandbox **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 207**

**Chapter 8:** Track Changes Between Your Project and Org **. . . . . . . . . . . . . . . . . . . . . 211**

Manage Source Tracking for Your org **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 212**
Preview Changes Identified by Source Tracking **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 213**
Deploy and Retrieve Changes Identified by Source Tracking **. . . . . . . . . . . . . . . . . . . . . . . . 214**

Retrieve Changes to Profiles with Source Tracking **. . . . . . . . . . . . . . . . . . . . . . . . . . . 217**
Resolve Conflicts Between Your Local Project and Org **. . . . . . . . . . . . . . . . . . . . . . . . . . . . 218**
Best Practices **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 219**
Performance Considerations of Source Tracking **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 220**

**Chapter 9:** Work with Data **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 221**

Work With Small Datasets **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 222**
Work With Large Datasets **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 224**
Work With Individual Records **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 228**
Run a SOQL or SOSL Query **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 230**
Upload a File to Your Org **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 231**

**Chapter 10:** Salesforce DX MCP Server and Tools (Beta) **. . . . . . . . . . . . . . . . . . . . . . 232**

Quick Start Using the VS Code With Copilot MCP Client (Beta) **. . . . . . . . . . . . . . . . . . . . . . . 235**
Install and Configure the Salesforce DX MCP Server (Beta) **. . . . . . . . . . . . . . . . . . . . . . . . 236**

Add the Salesforce DX MCP Server to Your MCP Client (Beta) **. . . . . . . . . . . . . . . . . . . 236**
Configure the Salesforce DX MCP Server for Your Environment (Beta) **. . . . . . . . . . . . . . 237**
Manage the Salesforce DX MCP Server (Beta) **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 242**
Use the Core Salesforce DX MCP Tools (Beta) **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 243**

**Chapter 11:** Development **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 246**

Develop Against Any Org **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 248**
Assign a Permission Set **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 251**
Create Lightning Apps and Aura Components **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 252**
Create Lightning Web Components **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 252**

**Contents**

Create an Apex Class **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 253**
Create an Apex Trigger **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 254**
Create a Custom Object **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 254**
Execute Anonymous Apex **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 255**
Run Apex Tests **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 256**

Debug Apex **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 259**
Generate and View Apex Debug Logs **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 260**

**Chapter 12:** Build and Release Your App **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 262**

Build and Release Your App with Metadata API **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 264**

Develop and Test Changes Locally **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 266**
Build and Test the Release Artifact **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 267**
Test the Release Artifact in a Staging Environment **. . . . . . . . . . . . . . . . . . . . . . . . . . 267**
Release Your App to Production **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 268**
Cancel a Metadata Deployment **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 268**

**Chapter 13:** Unlocked Packages **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 269**

What’s an Unlocked Package? **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 270**
Package-Based Development Model **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 270**
Before You Create Unlocked Packages **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 271**
Know Your Orgs **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 271**
Create Org-Dependent Unlocked Packages **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 272**
Workflow for Unlocked Packages **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 273**
Configure Unlocked Packages **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 274**

Project Configuration File for Unlocked Packages **. . . . . . . . . . . . . . . . . . . . . . . . . . . 275**
Unlocked Packaging Keywords **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 281**
Package Installation Key **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 282**
Extract Dependency Information from Unlocked Packages **. . . . . . . . . . . . . . . . . . . . . 283**
Understanding Namespaces **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 284**
Share Release Notes and Post-Install Instructions **. . . . . . . . . . . . . . . . . . . . . . . . . . . 288**
Specify Unpackaged Metadata or Apex Access for Apex Tests (Unlocked Packages) **. . . 289**
Best Practices for Unlocked Packages **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 290**
Package IDs and Aliases for Unlocked Packages **. . . . . . . . . . . . . . . . . . . . . . . . . . . 290**
Frequently Used Unlocked Packaging Operations **. . . . . . . . . . . . . . . . . . . . . . . . . . . 291**
How We Handle Profile Settings in Unlocked Packages **. . . . . . . . . . . . . . . . . . . . . . . . . . 292**
Develop Unlocked Packages **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 293**

Create and Update an Unlocked Package **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 294**
Create New Versions of an Unlocked Package **. . . . . . . . . . . . . . . . . . . . . . . . . . . . 295**
Guidance for Package Version Numbering **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 300**
Code Coverage for Unlocked Packages **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 301**
Considerations for Promoting Packages with Dependencies **. . . . . . . . . . . . . . . . . . . 302**
Release an Unlocked Package **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 303**
Update an Unlocked Package Version **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 304**
Hard-Deleted Components in Unlocked Packages **. . . . . . . . . . . . . . . . . . . . . . . . . . 304**

**Contents**

Delete an Unlocked Package or Package Version **. . . . . . . . . . . . . . . . . . . . . . . . . . 309**
View Package Details **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 310**
Push a Package Upgrade for Unlocked Packages **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 311**

Schedule a Push Upgrade Using CLI **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 311**
Install an Unlocked Package **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 314**

Install Packages with the CLI **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 315**
Install Unlocked Packages from a URL **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 316**
Upgrade a Version of an Unlocked Package **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 316**
Sample Script for Installing Unlocked Packages with Dependencies **. . . . . . . . . . . . . . . 317**
Migrate Deprecated Metadata from Unlocked Packages **. . . . . . . . . . . . . . . . . . . . . . . . . 320**
Uninstall an Unlocked Package **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 320**
Transfer an Unlocked Package to a Different Dev Hub **. . . . . . . . . . . . . . . . . . . . . . . . . . . 321**

Take Ownership of an Unlocked Package Transferred from a Different Dev Hub **. . . . . . 323**

**Chapter 14:** Continuous Integration **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 326**

Continuous Integration Using CircleCI **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 327**

Configure Your Environment for CircleCI **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 327**
Connect CircleCI to Your DevHub **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 328**
Continuous Integration Using Jenkins **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 329**

Configure Your Environment for Jenkins **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 330**
Jenkinsfile Walkthrough **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 331**
Sample Jenkinsfile **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 337**
Continuous Integration with Travis CI **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 342**
Sample CI Repos for Org Development Model **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 342**
Sample CI Repos for Package Development Model **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 342**

**Chapter 15:** Troubleshoot Salesforce DX **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 344**

Resolve Common Authorization Errors **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 345**

org login web Errors **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 345**
org login jwt Errors **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 348**
Error: No default dev hub found **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 351**
Unable to Work After Failed Org Authorization **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 351**
Error: The consumer key is already taken **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 352**
CLI Version Information **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 353**

**Chapter 16:** Limitations for Salesforce DX **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 354**

# CHAPTER 1 How Salesforce Developer Experience (DX) Tooling

Changes the Way You Work

In this chapter ...

**•** Get Started by Using
a Sample Repo

Salesforce DX tooling provides modern experience to manage and develop apps on the platform across
their entire lifecycle. It brings together source-driven development, team collaboration with governance,
and new levels of agility for custom app development on Salesforce based on modern best practices.

Highlights include:

**•** Get Started by
Creating a New DX **•**
Project **•**

**•** Your tools, your way. You use the developer tools you already know.

Project **•** The ability to apply best practices to software development. Source code and metadata exist outside

**•** Create an of the org and provide more agility to develop Salesforce apps in a team environment. Instead of
Application the org, your version control system is the source of truth.

**•** Migrate or Import
Existing Source

**•** Salesforce DX
Release Notes

**•** A powerful command-line interface (CLI) removes the complexity of working with your Salesforce
org for development, continuous integration, and delivery.

**•** Flexible and configurable scratch orgs that you build for development and automated environments.
This new type of org makes it easier to build your apps and packages.

**•** You can use any IDE or text editor you want with the CLI and externalized source.

Note: Salesforce DX tooling requires the API Enabled system permission, which provides
programmatic access to your org's information.

Are You Ready to Begin?

Here’s the basic order for doing your work using Salesforce DX. These workflows include the most
common CLI commands. For all commands, see the _Salesforce CLI Command Reference_ .

**•** [Install Salesforce CLI](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_setup.meta/sfdx_setup/sfdx_setup_intro.htm)

**•** Enable Dev Hub

**•** Use a Sample Repo to Get Started

**•** Create an Application

**•** Migrate or Import Existing Source

Optionally, install:

**•** [Salesforce Extensions for VS Code](https://developer.salesforce.com/docs/platform/sfvscode-extensions/guide/vscode-overview.html)

**•** [Agentforce Vibes IDE](https://developer.salesforce.com/docs/platform/code-builder/guide/codebuilder-overview.html)


How Salesforce Developer Experience (DX) Tooling Changes
the Way You Work

**•** [DevOps Center](https://help.salesforce.com/s/articleView?id=platform.devops_center_setup.htm&type=5&language=en_US)

SEE ALSO:

[Developer Experience (DX) Developer Center](https://developer.salesforce.com/developer-centers/developer-experience)

_[Salesforce CLI Command Reference](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_cli_reference.meta/sfdx_cli_reference)_


## How Salesforce Developer Experience (DX) Tooling Changes Get Started by Using a Sample Repo

the Way You Work

## Get Started by Using a Sample Repo

The quickest way to get going with Salesforce DX tooling is to clone the `dreamhouse-lwc` GitHub repo. Use its configuration files
and Salesforce application to try some commonly used Salesforce CLI commands. In addition to source code for the application, the
repo includes sample data and Apex tests.

[This task assumes you have a Dev Hub org. See Select and Enable a Dev Hub Org for more information.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_setup_enable_devhub.htm)

**1.** [If you haven't already, install Salesforce CLI on your computer.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_setup.meta/sfdx_setup/sfdx_setup_install_cli.htm)

**2.** Open a terminal or command prompt window, and clone the `[dreamhouse-lwc](https://www.sfdc.co/sfdx-sample-repo)` GitHub sample repo using HTTPS or SSH.
HTTPS:

```
     git clone https://github.com/trailheadapps/dreamhouse-lwc.git

```

SSH:

```
     git clone git@github.com:trailheadapps/dreamhouse-lwc.git

```

**3.** Change to the `dreamhouse-lwc` project directory.

```
     cd dreamhouse-lwc

```

**4.** Authorize your Dev Hub org by logging into it, set it as your default, and assign it an alias.

```
     sf org login web --set-default-dev-hub --alias DevHub

```

Enter your Dev Hub org credentials in the browser that opens. After you log in successfully, you can close the browser.

**5.** Create a scratch org using the `config/project-scratch-def.json` file, set the org as your default, and assign it an alias.

```
     sf org create scratch --definition-file config/project-scratch-def.json --set-default

     --alias my-scratch-org

```

The command uses the default Dev Hub you set with the `sf org login web` command in a previous step.

**6.** View the orgs that you've either created or logged into.

```
     sf org list

```

The table displays the Dev Hub you logged into and the scratch org you created. The right-most column indicates the default scratch
org and Dev Hub org; in the real-life output you see cute emojis, but in the output below we use `(S)` and `(D)`, respectively. The
Alias column displays the aliases you assigned each org. Here’s some sample output.

```
        Type Alias Username Org ID

     Status Expires

      ── ─────────────────────────────────────────────────────────────────────────────

     ───────────────────────────────

      (D) DevHub DevHub jules@sf.com 00Daj0AUXXXXXXXXXX

     Connected

        Sandbox jules@sf.com.jssandtwo 00D02000EAMXXXXXXX

     Connected

      (S) Scratch my-scratch-org test-loo73bj6givn@example.com 00D7xOjgTEASXXXXXX

     Active 2024-05-16

     Legend: (D)=DevHub, (S)=Default Org Use --all to see expired and deleted scratch

      orgs

```


## How Salesforce Developer Experience (DX) Tooling Changes Get Started by Creating a New DX Project

the Way You Work

**7.** Deploy the Dreamforce app, whose source is in the `force-app` directory, to the scratch org.

```
     sf project deploy start --source-dir force-app

```

**8.** Assign the `dreamhouse` permission set to the default scratch org user ( `test-ibnpzayw@example.com` ).

```
     sf org assign permset --name dreamhouse

```

**9.** Import sample data from three objects (Contact, Property, and Broker) into the scratch org using the specified plan definition file.

```
     sf data import tree --plan data/sample-data-plan.json

```

**10.** Run Apex tests.

```
     sf apex run test --result-format human --wait 1

```

Apex tests run asynchronously by default. If the tests finish before the `--wait` value, the results are displayed. Otherwise, use the
displayed command to get the results using a job ID.

**11.** Open the scratch org and view the deployed metadata under Most Recently Used.

```
     sf org open

```

**12.** In App Launcher, find and open the Dreamhouse application.

Congrats! You just deployed an application to a new scratch org.

SEE ALSO:

Sample Repository on GitHub

Authorization

Create Scratch Orgs

Deploy Source From Your Project to the Scratch Org

Run Apex Tests

## Get Started by Creating a New DX Project

Let's say you're a Salesforce developer who creates awesome org customizations using declarative tools and builders, such as Flow and
Lightning App Builder. You've heard about source-driven development, and want to move in that direction. You therefore need to
extract your customizations from your org and store them in a source control system, such as GitHub, which then becomes your new
source of truth. But you're not quite sure how it all works and would like to get some hands on practice using simple use cases. Keep
reading!

This tutorial starts completely from scratch and shows you how to create simple artifacts, such as Apex classes and LWC components,
and then how to sync them between your org and your local project on your laptop. Another tutorial to help you learn about source-driven
development is Get Started by Using a Sample Repo on page 3, which is also hands-on but provides a ready-made application that's
already in a GitHub repo. Both tutorials are a lot of fun.

Note: We highly recommend that you use a Developer Edition org to simulate your production org, and scratch orgs for your
development work. This tutorial shows you how to get set up. This way, you don’t mess up your developer sandbox with artifacts
you’re just playing with.


### How Salesforce Developer Experience (DX) Tooling Changes Get an Org to Play With and Set It as Your Dev Hub

the Way You Work

### Get an Org to Play With and Set It as Your Dev Hub

Before you do anything, you need a Salesforce org to play with and designate as your Dev Hub, which is required when working with
Salesforce DX. We don’t recommend using your production org.

If you don’t currently have an org in which you can play in, here are some options:

**•** [Sign up for a free Developer Edition org here. Remember your username and password!](https://developer.salesforce.com/signup)

**•** [Create a free Trailhead playground (also referred to as a Hands-on Org), which is just a Developer Edition org that’s linked to your](https://trailhead.salesforce.com/content/learn/modules/trailhead_playground_management)
[Trailhead account. Be sure you follow these instructions to get the username and password of your org.](https://trailhead.salesforce.com/content/learn/modules/trailhead_playground_management/get-your-trailhead-playground-username-and-password)

Then follow these steps.

**1.** Log in to your org from your browser by navigating to [login.salesforce.com](http://login.salesforce.com) and enter your username and password.

**2.** In the top-right corner, click the gear icon and then **Setup** .

**3.** In the Quick Find box on the left, enter _`Dev Hub`_, then click **Dev Hub** .

**4.** Click **Enable Dev Hub** .

**Read more about it:**

**•** [Select and Enable a Dev Hub Org](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_setup_enable_devhub.htm)

### Install the Salesforce Platform Development Tools

Now set up your local computer so you can start using the Platform development tools, Salesforce CLI and Salesforce Extensions for
Visual Studio Code (VS Code).

If you’re not allowed to install tools on your computer, you can use Agentforce Vibes IDE which contains all these tools in a Web browser.
In this document we show only Salesforce CLI and VS Code though.

**1.** Install Salesforce CLI on your computer.
**Windows:**

**a.** [Download the .exe file to your computer.](https://developer.salesforce.com/tools/salesforcecli)

**b.** Open Windows explorer and execute the downloaded `*.exe` file by double-clicking it and answering all the prompts.

**macOS:**


### How Salesforce Developer Experience (DX) Tooling Changes Create a Salesforce DX Project

the Way You Work

**a.** [Download the *.pkg file to your computer.](https://developer.salesforce.com/tools/salesforcecli)

**b.** Open Finder and execute the downloaded `*.pkg` file file by double-clicking it and answering all the prompts.

**2.** Open a command prompt (Windows) or terminal (macOS), and then run this CLI command to make sure Salesforce CLI is installed
correctly:

```
     sf version

```

You see something like `@salesforce/cli/2.98.6 darwin-arm64 node-v22.17.0.`

**3.** [Install Visual Studio Code on your computer.](https://code.visualstudio.com/)

**4.** [Install the Salesforce Extensions into VS Code.](https://marketplace.visualstudio.com/items?itemName=salesforce.salesforcedx-vscode)

Tip: If Node.js is installed on your computer and you prefer using `npm` to install applications, run this command to install Salesforce
CLI

```
      npm install -g @salesforce/cli

```

**Read more about it:**

**•** [Agentforce Vibes IDE Overview](https://developer.salesforce.com/tools/vscode/en/codebuilder/about)

**•** [Salesforce CLI: Quick Start](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_setup.meta/sfdx_setup/sfdx_setup_intro.htm)

**•** [Salesforce Extensions for Visual Studio Code](https://developer.salesforce.com/docs/platform/sfvscode-extensions/guide)

### Create a Salesforce DX Project

Salesforce DX projects provide a structure for your org’s metadata (such as Apex code and org configuration), org templates, sample
data, and all your team’s tests. To bring consistency to your team’s development processes, store project metadata in a source control
system (SCS), such as GitHub. Let’s create a project and take a brief look at the default new files.

**1.** In your command prompt (Windows) or terminal (macOS), change to a directory on your computer where you want to create the
DX project. For example, on macOS:

```
     cd /Users/juliet/sfdx

```

**2.** Create a Salesforce DX project called `mydxproject` by running this command:

```
     sf project generate --name mydxproject

```

**3.** Change to the directory that was created.

```
     cd mydxproject

```

Here’s some information about the most interesting files and subdirectories in your new DX project:

**•** `sfdx-project.json` : Main configuration file for your Salesforce DX project.

**•** `config/project-scratch-def.json` : Definition file for creating scratch orgs.

**•** `.forceignore` : File that specifies the source files you want to exclude when synchronizing metadata between your local project
and org. If you’re familiar with Git, you can see that the file is very similar to the .gitignore file.

**•** `force-app` : Directory that contains source files that represent metadata from your org. The directory doesn’t yet contain any files,
but we’ll add some later!

**Read more about it:**

### • Create a Salesforce DX Project


### How Salesforce Developer Experience (DX) Tooling Changes Authorize Your Dev Hub and Create a Scratch Org

the Way You Work

**•** [Salesforce DX Project Configuration](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_ws_config.htm)

### Authorize Your Dev Hub and Create a Scratch Org

Remember when you previously created a Dev Edition or Trailhead Playground org to play with and set it as your Dev Hub? You now
authorize it locally so you can use it with your Salesforce DX project. And then you can create a scratch org, which you use for development.

**1.** From your command prompt or terminal window, run this CLI command:

```
     sf org login web --set-default-dev-hub --alias DevHub

```

The `--set-default-dev-hub` and `--alias` flags declare this Dev Hub org as your default Dev Hub org and give it an
alias. Later you see how specifying these flags now makes other CLI commands easier to use.

**2.** Log in to the org using your username and password in the window that pops up, just like you log into any Salesforce org.
But wait, didn’t you already log into this org? Yes, you did! But this time you’re logging into it via the `org login web` CLI
command, which authorizes the org to be used by your local DX project. After you’re connected, you don’t have to keep logging
into the org when you run subsequent CLI commands.

**3.** Click Allow in the browser window that opens and asks if you allow access to the org.

You can close the browser window because you’re all done with it.

Back in your command prompt or terminal, you should see output like this, which confirms that you successfully authorized the org:

`Successfully authorized joe@creative-fox-gw7irx.com with org ID 00Daj123457MzBEAU` .

**4.** In your command prompt or terminal, run this command to see the org you just authorized, along with additional information about
it, such as its org ID and Connected status.

```
     sf org list

```

The little tree emoji ( ) to the left indicates that it’s your default Dev Hub org.

**5.** Run this command to create a scratch org using the default definition file that was created in the Salesforce DX project:

```
     sf org create scratch --definition-file config/project-scratch-def.json --set-default

     --alias myscratch

```

Be sure you run the command from your main DX project directory, which in our example is
`/Users/juliet/sfdx/mydxproject` .

As the command runs, the output tells you what’s happening in the background as Salesforce creates the scratch org.

Similar to when you authorized the Dev Hub org, the `--set-default` and `--alias` flags set the scratch org as your default
org and give it an alias. The scratch org creation process requires a Dev Hub, but because you previously set the one you authorized
as your default, you don’t need to specify it to the org create scratch command. Otherwise you must use the `--target-dev-hub`
flag.


### How Salesforce Developer Experience (DX) Tooling Changes Make a Change in Your Scratch Org And Retrieve It to Your

the Way You Work Project

You see this message when the scratch org creation is finished:

```
     Your scratch org is ready.

```

**6.** Run this command again to see the new scratch org listed in the list of authorized orgs:

```
     sf org list

```

The little leaf emoji ( ) to the left indicates that it’s your default org. Run this command to see details about your new org:

```
     sf org display

```

Good job! You’re now ready to do some development work using your new scratch org.

**Read more about it:**

**•** [Authorize an Org Using a Browser](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_auth_web_flow.htm)

**•** [Authorization Information for an Org](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_auth_view_info.htm)

**•** [Reference documentation for the “org” CLI commands](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_org_commands_unified.htm)

**•** [Create Scratch Orgs](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_scratch_orgs_create.htm)

### Make a Change in Your Scratch Org And Retrieve It to Your Project

If you’re a Salesforce admin, you’re probably familiar with customizing an org using tools such as Setup and Object Manager. You’re now
going to use these familiar tools to make a simple change in your new scratch org: add a custom field to the existing Account object.
The details don’t matter, you simply want to make any change so you can then retrieve its associated metadata into your project.

We’re also going to give VS Code a whirl. Most developers prefer using an integrated development environment (IDE) and VS Code is
optimized for working on the Salesforce Platform.

[We don’t go into details about how to use VS Code, which can do all kinds of amazing things. Check out this Trailhead module for more](https://trailhead.salesforce.com/content/learn/projects/quickstart-vscode-salesforce)
information. But we show you a few basics.

**1.** From your open command prompt or terminal, run this command to open your scratch org in a browser:

```
     sf org open

```

Hold on, how did the CLI command know which org to open? Easy: when you created the scratch org, you specified that it’s your
default org. If you want to open a different org, or be explicit about the default org, you use the `--target-org` flag and pass it
a username or alias. For example:

```
     sf org open --target-org myscratch

```

**2.** In the browser that opens, use Object Manager to create a custom field with label **Account Status** on the Account object. Choose
any properties about the field that you want, it doesn’t matter for the purposes of this exercise.
[Never done this task before? Follow this Trailhead Quick Look for details.](https://trailhead.salesforce.com/content/learn/modules/custom-fields-quick-look)

When you’re finished, you see something like this:


How Salesforce Developer Experience (DX) Tooling Changes Make a Change in Your Scratch Org And Retrieve It to Your
the Way You Work Project

**3.** Open VS Code. An easy way is to run this command from your open command prompt or terminal; the application opens right up:

```
     code

```

**4.** Click **File -> Open Folder ...**, navigate to your Salesforce DX project folder (which is `/Users/juliet/sfdx/mydxproject`
in our example), and click **Open** .

**5.** On the left, under **MYDXPROJECT**, click the `.forceignore` file, which is in the root of your Salesforce DX project directory. The
contents of the file appears in a tab on the right. You see something like this:

You use the `.forceignore` file to ignore files or directories when you run the CLI commands to deploy or retrieve source.

**6.** Click inside the `.forceignore` tab and add these two lines at the end of the file after `**/__tests__/**` :

```
     # Exclude Profiles

     **/profiles/**

```

The reason we’re excluding Profiles from the source that’s deployed and retrieved is that they can be finicky and it’s easier for now
to just not worry about them. You also get some practice using the `.forceignore` file!

**7.** Click **File -> Save** .

**8.** In the VS Code terminal, run this command to retrieve the customization you just made:

```
     sf project retrieve start

```

If you don’t have a terminal window open in VS Code, click **View -> Terminal** .

The retrieve might take a minute or two. But when it’s finished, you see something like this:

Similar to when you previously opened the scratch org, this CLI command knows to retrieve changed or new metadata from the
scratch org because you set it as your default org.

The command output shows the metadata that it retrieved. You should see your new Account Status custom field. You probably
also see other retrieved metadata, such as Layouts. That’s normal.

The Path column shows where the new metadata files are located in your project. Take a look at them if you want!


### How Salesforce Developer Experience (DX) Tooling Changes Create an Apex Class and Deploy it To the Scratch Org

the Way You Work

What you just did was pretty amazing; you used the Object Manager UI to customize the scratch org and then retrieved that customization
(as metadata source files) to your DX project as local source files.

**Read more about it:**

**•** [Develop with Ease with Salesforce Extensions for VS Code](https://developer.salesforce.com/tools/vscode)

**•** [How to Exclude Source When Syncing](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_exclude_source.htm)

**•** [Retrieve Metadata from Your Scratch Org](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_pull_md_from_scratch_org.htm)

**•** [Reference Documentation for the](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_project_commands_unified.htm) `project` CLI Commands

### Create an Apex Class and Deploy it To the Scratch Org

But wait, there’s more! Let’s say you want to create an Apex class in your scratch org. You can use Setup in the Salesforce UI to create
Apex classes, but the tool is limited, so let’s instead use VS Code, which we introduced in the previous section.

**1.** From VS Code, click **View -> Command Palette** and run **SFDX:Create Apex Class** .
Enter `MyApexClass` for the Apex class name and store it in the default local source directory
( `force-app/main/default/classes` ).

A new tab opens on the right with initial code for `MyApexClass`, which is stored in a file called `MyApexClass.cls` . The
command also created another file: `MyApexClass.cls-meta.xml` .

**2.** (Optional) If you’re familiar with the Apex programming language, add some code to the new class. But you can also leave it empty
for now; all we need for this exercise are the metadata files that correspond to the Apex class.

**3.** Click **File -> Save** to save the new Apex class.

**4.** From the command palette, run **SFDX: Push Source to Default Org** . (Deploying is sometimes also called pushing.)
You should see a notification like this when it’s complete:

Also check your output window (click **View -> Output** if you don’t see it). You see information about the deploy, including the files
that were actually deployed:

```
     === Pushed Source

     STATE FULL NAME TYPE PROJECT PATH

     ─────── ─────────── ─────────

     ────────────────────────────────────────────────────────────────────────

     Created MyApexClass ApexClass

     ../mydxproject/force-app/main/default/classes/MyApexClass.cls

     Created MyApexClass ApexClass

     ../mydxproject/force-app/main/default/classes/MyApexClass.cls-meta.xml

```

**5.** Go back to the browser window that’s open to your scratch org. If you closed the browser window, you can run this command again
from the VS Code terminal:

```
     sf org open

```

**6.** In the Setup Quick Find box, enter _`Apex`_, then click **Apex Classes** . You should see the `MyApexClass` Apex class you just created,
but now it’s also in your scratch org. Pretty cool, huh!


### How Salesforce Developer Experience (DX) Tooling Changes Create a Lightning Web Component and Deploy it to the

the Way You Work Scratch Org

**7.** For fun, let’s do one last thing: edit the Apex class in Setup. For example, add this comment to the top of the file:

```
     // This is a very exciting Apex class

     Be sure to save!

```

**8.** In VS Code, go to the command palette and run **SFDX: Pull Source from Default Org** .

**9.** When the retrieve (also sometimes called a pull) finishes, refresh the `MyApexClass` Apex class in VS Code if necessary; you should
see the new comment that you made in Setup.

This section gave you just a taste of using VS Code to develop Apex classes.

**Read more about it:**

**•** [Apex Quick Start](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_qs_HelloWorld.htm)

**•** [Develop with Ease with Salesforce Extensions for VS Code](https://developer.salesforce.com/tools/vscode)

### Create a Lightning Web Component and Deploy it to the Scratch Org

Writing an Apex class was fun, so let’s use VS Code to create a Lightning Web Component (LWC) in your DX project and then deploy it
to your scratch org.

**1.** From VS Code, click **View -> Command Palette** and run **SFDX:Create Lightning Web Component** .
Enter _`helloworld`_ for the filename and store it in the default directory ( `force-app/main/default/lwc` ).

A new tab opens on the right with initial code for the new LWC component, which is stored in a file called `helloworld.js.`
The command also creats two other associated files ( `helloworld.html` and `helloworld.js-meta.xml` ) and a test.

**2.** (Optional) If you’re familiar with creating Lightning Web Components, add some code to any of the `helloworld` files. But you
can also leave them empty for now; all we need for this exercise are metadata files associated with the LWC component.

**3.** Click **File -> Save** to save the new LWC component.

**4.** From the command palette, run **SFDX: Push Source to Default Org** . Similar to when you deployed the Apex class, you see a
notification and information in the Output window.

Optionally run through the same steps described in the Apex section, such as opening your scratch org, viewing your new `helloworld`
component in Setup (search for **Lightning Components** in the Quick Find box), making a change, and then retrieving the change back
to your project.

**Read more about it:**

**•** [Get Started with Lightning Web Components](https://developer.salesforce.com/docs/platform/lwc/guide/get-started-introduction.html)

**•** [Develop with Ease with Salesforce Extensions for VS Code](https://developer.salesforce.com/tools/vscode)

### Deploy All Customizations To a Sandbox

You just completed all this development work in a scratch org, but at some point you probably want to deploy everything to a sandbox
for further testing, and then eventually deploy to your production org.

Let’s simulate some of this process by deploying the changes you made (a new custom field, a new Apex class, and a new LWC component)
to your Dev Hub org, which we’ll pretend is the sandbox that you use for testing changes. This time we run CLI commands from a
command prompt or terminal, rather than use the VS Code commands.

Important: There’s a lot more involved in rigorous DevOps. This Getting Started doc simply gives you a taste of what you can do
with Salesforce CLI and VS Code extensions around org metadata and scratch orgs.


How Salesforce Developer Experience (DX) Tooling Changes Deploy All Customizations To a Sandbox
the Way You Work

**1.** From the command prompt (Windows) or terminal (macOS) that’s open in your Salesforce DX project, run this command to deploy
your changes to your Dev Hub.

```
     sf project deploy start --source-dir force-app --target-org DevHub

```

The `--source-dir` flag specifies exactly what you want to deploy, which is all the metadata that’s in the `force-app` package
directory.

You see something like this:

```
     ───────────────Deploying Metadata ───────────────

      Deploying v64.0 metadata to joe@resilient-fox-4z9oop.com using the v64.0 SOAP API.

      � Preparing 205ms

      � Waiting for the org to respond - Skipped

      � Deploying Metadata 2.88s

       � Components: 7/7 (100%)

      � Running Tests - Skipped

      � Updating Source Tracking - Skipped

      � Done 0ms

      Status: Succeeded

      Deploy ID: 0Affj0000017DPlCAM

      Target Org: joe@resilient-fox-4z9oop.com

      Elapsed Time: 3.09s

     Deployed Source

     ┌─────────┬────────────────────────────────────────┬──────────────────────────┬───────────────────────────────────────────────────────────────────────────────────────┐

     │State │Name │Type │Path

                                                     │

     ├─────────┼────────────────────────────────────────┼──────────────────────────┼───────────────────────────────────────────────────────────────────────────────────────┤

     │Created │MyApexClass │ApexClass │

     force-app/main/default/classes/MyApexClass.cls

     │

     │Created │MyApexClass │ApexClass │

     force-app/main/default/classes/MyApexClass.cls-meta.xml

     │

     │Created │Account.Account_Status__c │CustomField │

     force-app/main/default/objects/Account/fields/Account_Status__c.field-meta.xml

     │

     │Changed │Account-Account %28Marketing%29 Layout │Layout │

     force-app/main/default/layouts/Account-Account %28Marketing%29 Layout.layout-meta.xml

     │

     │Changed │Account-Account %28Sales%29 Layout │Layout │

     force-app/main/default/layouts/Account-Account %28Sales%29 Layout.layout-meta.xml

     │

     │Changed │Account-Account %28Support%29 Layout │Layout │

     force-app/main/default/layouts/Account-Account %28Support%29 Layout.layout-meta.xml

     │

     │Changed │Account-Account Layout │Layout │

     force-app/main/default/layouts/Account-Account Layout.layout-meta.xml

     │

     │Created │helloworld │LightningComponentBundle │

     force-app/main/default/lwc/helloworld/helloworld.html

     │

```


### How Salesforce Developer Experience (DX) Tooling Changes Add Project Files to Your VCS

the Way You Work

```
     │Created │helloworld │LightningComponentBundle │

     force-app/main/default/lwc/helloworld/helloworld.js

     │

     │Created │helloworld │LightningComponentBundle │

     force-app/main/default/lwc/helloworld/helloworld.js-meta.xml

     │

     └─────────┴────────────────────────────────────────┴──────────────────────────┴───────────────────────────────────────────────────────────────────────────────────────┘

```

**2.** Open the Dev Hub org in a browser window:

```
     sf org open --target-org DevHub

```

Use Object Manager and Setup to check that the new custom field ( `Account.Account_Status` ), Apex class ( `MyApexClass` ),
and LWC component ( `helloworld` ) exist in the org.

Wow, you just created and moved lots of metadata around! Awesome sauce.

**Read more about it:**

**•** [Deploy Source From Your Project to the Scratch Org](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_push_md_to_)

**•** [Reference Documentation for the](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_project_commands_unified.htm) `project` CLI Commands

### Add Project Files to Your VCS

A typical next step is to add your Salesforce DX project's local files, which represent Salesforce customizations, to a version control system
like GitHub. You can then share the DX project, use it to create a scratch org that mirrors your production org's customizations, version
your code updates, test updates using a continuous integration (CI) system, and generally adhere to modern development practices.

[However, that step is beyond the scope of this topic, but check out the Git and GitHub Basics Trailhead module for more information.](https://trailhead.salesforce.com/content/learn/modules/git-and-git-hub-basics)

### Next Steps

We hope this document gets you started using Salesforce DX. Here are a few more links to help you as you embark on this exciting
journey.

**•** [Get Started by Using a Sample Repo](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_intro_sample_repo.htm)

**•** [Salesforce Developers Sample Apps](https://github.com/trailheadapps/)

## Create an Application

Follow the basic workflow when you are starting from scratch to create and develop an app that runs on the Lightning Platform.

**1.** Set up your project.

**2.** Authorize the Developer Hub org for the project.

**3.** Configure your local project.

**4.** Create a scratch org.

**5.** Push the source from your project to the scratch org.

**6.** Develop the app.

**7.** Pull the source to keep your project and scratch org in sync.


## How Salesforce Developer Experience (DX) Tooling Changes Migrate or Import Existing Source

the Way You Work

**8.** Run tests.

**9.** Add, commit, and push changes. Create a pull request.

Deploy your app using one of the following methods:

**•** Build and release your app with managed packages

**•** Build and release your app using the Metadata API

## Migrate or Import Existing Source

Use the Metadata API to retrieve the code, and then convert your source for use in a Salesforce DX project.

Tip: If your current repo follows the directory structure that is created from a Metadata API retrieve, you can skip the retrieve step
and go directly to converting the source.

**1.** Set up your project.

**2.** Retrieve your metadata.

**3.** Convert the metadata formatted source you just retrieved to source format.

**4.** Authorize the Developer Hub org for the project.

**5.** Configure your local project.

**6.** Create a scratch org.

**7.** Push the source from your project to the scratch org.

**8.** Develop the app.

**9.** Pull the source to sync your project and scratch org.

**10.** Run tests.

**11.** Add, commit, and push changes. Create a pull request.

Deploy your app using one of the following methods:

**•** Build and release your app with managed packages

**•** Build and release your app using the Metadata API

Salesforce DX Release Notes

Use the Salesforce Release Notes to learn about the most recent updates and changes to development environments, packaging, platform
development tools, and Salesforce APIs.

For the latest changes, visit:

**•** [Salesforce Extensions for Visual Studio Code Release Notes](https://marketplace.visualstudio.com/items/salesforce.salesforcedx-vscode/changelog)

**•** [Salesforce CLI Release Notes](https://github.com/forcedotcom/cli/blob/main/releasenotes/README.md)

**•** [Development Environments Release Notes (Includes Developer Edition orgs, sandboxes, and scratch orgs)](https://help.salesforce.com/s/articleView?id=release-notes.rn_dev_environments.htm&language=en_US)

**•** [Packaging Release Notes](https://help.salesforce.com/s/articleView?id=release-notes.rn_development.htm&language=en_US)

**•** [New and Changed Items for Developers (Includes Apex, standard objects, Metadata API, and more)](https://help.salesforce.com/s/articleView?id=release-notes.rn_development_new_changed.htm&language=en_US)


# CHAPTER 2 Provide Developers Access to Salesforce DX Tools

In this chapter ... Prepare your development team with the license, user access, and user permissions they need. Determine
which org to use as your Dev Hub org, and enable the Dev Hub setting in that org.

**•** Select and Enable a
Dev Hub Org

**•** Enable Source
Tracking in
Sandboxes

**•** Add Salesforce DX
Users


## Provide Developers Access to Salesforce DX Tools Select and Enable a Dev Hub Org Select and Enable a Dev Hub Org

The Dev Hub lets you create scratch orgs, unlocked packages, and second-generation managed
packages. Your Dev Hub is also the designated place to manage all your scratch orgs, packages,
and namespaces.

Determine which org to use as your Dev Hub org, then enable the Dev Hub setting in that org. Dev
Hub comprises objects with permissions that allow admins to control the level of access available
to a user and an org. If you’re developing an unlocked package that you intend to deploy to other
orgs, enable the Dev Hub setting in one of your active production orgs. This ensures that your
package is owned by an active org.

All Salesforce ISV and OEM partners should designate their Partner Business Org (PBO) as their Dev
[Hub org, see Enable Dev Hub and Second-Generation Managed Packaging for more details.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_pkg_enable_devhub.htm)

To enable Dev Hub in an org:

**1.** Log in as System Administrator to your production, Developer Edition, or trial org.

**2.** From Setup, enter _`Dev Hub`_ in the Quick Find box and select **Dev Hub** .

If you don't see Dev Hub in the Setup menu, make sure that your org is one of the supported
editions.

**3.** To enable Dev Hub, click **Enable** .

After you enable Dev Hub, you can’t disable it.

Note: You can’t enable Dev Hub in a sandbox.

The Dev Hub org instance determines where scratch orgs are created.

EDITIONS

Available in: Salesforce
Classic and Lightning
Experience

Dev Hub available in:
**Developer**, **Enterprise**,
**Performance**, and
**Unlimited** Editions

Scratch orgs available in:
**Developer**, **Enterprise**,
**Group**, and **Professional**
Editions

**•** Scratch orgs created from a Dev Hub org in Government Cloud are created on a Government Cloud instance.

**•** Scratch orgs created from a Dev Hub org in Hyperforce are created on a Hyperforce instance.

Consider these factors if you select a trial or Developer Edition org as your Dev Hub.

**•** You can create up to six scratch orgs and package versions per day, with a maximum of three active scratch orgs.

**•** Trial orgs expire on their expiration date.

**•** Developer Edition orgs can expire due to inactivity.

**•** Package versions are associated with your Dev Hub org. When a trial or Developer Edition org expires, you lose access to the package
versions.

Enable Unlocked Packaging
Enable packaging in your org so you can develop unlocked packages. You can work with the packages in scratch orgs and sandboxes.

Enable Einstein Chatbot Features in Scratch Orgs
Turn on Einstein Features in your Dev Hub to eliminate the manual steps for enabling the Chatbot feature in scratch orgs. When you
accept the Terms of Service for Einstein, a separate acceptance is not required in each scratch org created from this Dev Hub org. If
you previously accepted the Terms of Service for Einstein to turn on an Einstein-related feature, this setting is already enabled.

Enable Language Extension Packages (Beta)
Enable Language Extension Packages in Dev Hub to create language extension packages that contain translations of components
in other packages. This feature is available in unlocked and first- and second-generation managed packages.


### Provide Developers Access to Salesforce DX Tools Enable Unlocked Packaging Enable Unlocked Packaging

Enable packaging in your org so you can develop unlocked packages. You can work with the packages in scratch orgs and sandboxes.

Before you begin, enable Dev Hub in your org.

**1.** Log in to the org where you’ve enabled Dev Hub.

**2.** From Setup, enter _`Dev Hub`_ in the Quick Find box and select **Dev Hub** .

**3.** Select **Enable Unlocked Packages and Second-Generation Managed Packages** .

After you enable this setting, you can’t disable it.

[To get started with creating unlocked packages, see Unlocked Packages. For information on second-generation managed packages, see](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_unlocked_pkg_intro.htm)
[the Second-Generation Managed Packages Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp.htm)

### Enable Einstein Chatbot Features in Scratch Orgs

Turn on Einstein Features in your Dev Hub to eliminate the manual steps for enabling the Chatbot feature in scratch orgs. When you
accept the Terms of Service for Einstein, a separate acceptance is not required in each scratch org created from this Dev Hub org. If you
previously accepted the Terms of Service for Einstein to turn on an Einstein-related feature, this setting is already enabled.

Complete this task before attempting to create a scratch org with the Chatbot feature.

**1.** Log in to your Dev Hub org.

**2.** From Setup, enter _`Dev Hub`_ in the Quick Find box and select **Dev Hub** .

**3.** On the Dev Hub Setup page, turn on **Enable Einstein Features** .

### Enable Language Extension Packages (Beta)

Enable Language Extension Packages in Dev Hub to create language extension packages that contain translations of components in
other packages. This feature is available in unlocked and first- and second-generation managed packages.

Note: This feature is a Beta Service. Customer may opt to try such Beta Service in its sole discretion. Any use of the Beta Service
[is subject to the applicable Beta Services Terms provided at Agreements and Terms.](https://www.salesforce.com/company/legal/agreements/)

Language extension packages can only contain Translations and CustomObjectTranslations. If a base package includes components
that can’t be translated, those components aren’t included when you create a language extension package.

**1.** In Dev Hub, from Setup, in the Quick Find box, enter _`Dev Hub`_, and then select **Dev Hub** .

### 2. On the Dev Hub Setup page, turn on Enable Language Extension Packages .

## Enable Source Tracking in Sandboxes

By enabling source tracking in Developer and Developer Pro sandboxes, Salesforce DX tooling can automatically track new, changed,
and deleted metadata components. You can then select and determine which changes to move forward in the development cycle and
release. For DX tooling that uses a Salesforce DX project or source control repository, source tracking can aid in conflict detection and
resolution. And best of all, because source tracking identifies which metadata components changed, you no longer have to manually
keep track of changes.

You can enable source tracking in Developer and Developer Pro sandboxes in two ways: in your production org for all sandboxes created
from it, or for a specific sandbox. After you turn on source tracking, you can disable it at any time.


### Provide Developers Access to Salesforce DX Tools Enable Source Tracking for All Developer and Developer Pro

Sandboxes

**•** For all Developer and Developer Pro sandboxes—when you enable the feature in your production org, all newly created and refreshed
sandboxes use source tracking. Existing sandboxes don’t have source tracking enabled until you refresh them.

**•** For a specific Developer or Developer Pro sandbox—if you don’t want to enable source tracking in all sandboxes, or want to enable
source tracking without refreshing the sandbox, you can enable it directly in the sandbox from the Sandbox Settings Setup page.

Note: Source tracking isn’t supported and can’t be enabled for Partial Copy sandboxes, Full sandboxes, or Developer Edition orgs.
Source tracking can result in metadata deployments taking longer to complete.

SEE ALSO:

_Salesforce Help_ [: Refresh Your Sandbox](https://help.salesforce.com/s/articleView?id=platform.data_sandbox_refresh.htm&language=en_US)

### Enable Source Tracking for All Developer and Developer Pro Sandboxes

Enable source tracking for all Developer and Developer Pro sandboxes in your production org from
the Dev Hub Setup page.

**1.** Log in to the source (production) org.

**2.** From Setup, find and select **Dev Hub** .

If you don't see Dev Hub in the Setup menu, make sure that the source org is one of the
supported editions.

**3.** Select **Enable Source Tracking in Developer and Developer Pro Sandboxes** .

**4.** Refresh any existing Developer or Developer Pro sandboxes to enable this feature.

Source tracking is automatically enabled for any newly created or refreshed Developer or
Developer Pro sandboxes.

You can disable this feature at any time by clicking the toggle. When the sandbox is refreshed, all
source tracking information is deleted.


EDITIONS

Available in: **Enterprise**,
**Performance**, and
**Unlimited** Editions. For
**Professional** and
**Database.com** Editions, you
can only enable source
tracking directly in the
sandbox.

USER PERMISSIONS

To view a sandbox:

**•** View Setup and
Configuration AND
Customize Applications

To create, refresh, activate,
and delete a sandbox:

**•** Manage Dev Sandboxes
(Developer or Developer
Pro only) or Manage
Sandboxes (all sandbox
types)

### Provide Developers Access to Salesforce DX Tools Enable Source Tracking in a Specific Sandbox Enable Source Tracking in a Specific Sandbox

Enable source tracking for a specific Developer or Developer Pro sandbox in its Settings Setup page.
If you refresh a sandbox, you must re-enable this feature.

**1.** Log in to the Developer or Developer Pro sandbox.

**2.** From Setup, find and select **Sandbox Settings** .

**3.** Click **Enable Source Tracking in This Sandbox** .

Metadata changes from this point forward are tracked, but existing metadata changes made before
you enabled this feature aren’t tracked. When the sandbox is refreshed, all source tracking information
is deleted. If you haven’t enabled source tracking in the production org for all Developer and
Developer Pro sandboxes, and you want the refreshed sandbox to use source tracking, you must
re-enable the feature in the Sandbox Settings page.

If you disable source tracking, it can take several days to clean up the source tracking records. The
process isn’t instantaneous. You can re-enable source tracking after the cleanup process is finished.

## Add Salesforce DX Users

System administrators can access the Dev Hub org by default. You can enable more users to access
the Dev Hub org so that they can create scratch orgs and use other developer-specific features.

EDITIONS

Available in: Lightning
Experience in Developer and
Developer Pro sandboxes

USER PERMISSIONS

To view a sandbox:

**•** View Setup and
Configuration AND
Customize Applications

To create, refresh, activate,
and delete a sandbox:

**•** Manage Dev Sandboxes
(Developer or Developer
Pro only) or Manage
Sandboxes (all sandbox
types)

Your developer users can use Salesforce DX with the Salesforce, and Salesforce Platform standard
user license, or you can assign them the Developer license, or the Salesforce Limited Access - Free license instead.

If your org has Developer licenses, you can add users with the Developer profile and assign them the provided Developer permission
set. Alternatively, you can add users with the Standard User or System Administrator profiles. For a standard user, you must create a
permission set with the required Dev Hub permissions. We recommend that you avoid adding users as system administrators unless
their work requires that level of authority and not just Dev Hub org access.

Determine Which License to Assign to Dev Hub Users
Which license type you assign to developer users depends on how much access they require in the Dev Hub org. If they require full
administrative access, you can assign the Salesforce or Salesforce Platform standard user license. If you want to limit access to only
specific features, Salesforce provides two developer license options

Add a System Administrator or Standard User to Your Dev Hub Org
Add system administrator users only if their work requires that level of authority. Otherwise, add standard users and create a permission
set with the required Salesforce DX permissions.

Add a Developer User to Your Dev Hub Org
Using a Developer license, add a user with the Developer profile and assign them the Developer permission set.

Add a Limited Access User to Your Dev Hub Org
If your users only require access to the Dev Hub, the Salesforce Limited Access - Free license is a good approach. The Salesforce
Limited Access - Free license is available by request. After this license is provisioned add a user with this license and the Limited
Access user profile, and then create and assign them a permission set to the required Dev Hub objects.


### Provide Developers Access to Salesforce DX Tools Determine Which License to Assign to Dev Hub Users

Create and Assign a Permission Set to Developer Users
To give full access to the Dev Hub org, create and assign a custom permission set that grants access to required Dev Hub objects.
Or if you have the Developer license, assign the Developer permission set.

SEE ALSO:

Org Shape Permissions

### Determine Which License to Assign to Dev Hub Users

Which license type you assign to developer users depends on how much access they require in the Dev Hub org. If they require full
administrative access, you can assign the Salesforce or Salesforce Platform standard user license. If you want to limit access to only
specific features, Salesforce provides two developer license options

Salesforce or Salesforce Platform License

The Salesforce license is for users who require full access to standard CRM and AppExchange apps. Users with this user license are entitled
to access any standard or custom app.

The Salesforce Platform license is designed for users who need access to custom apps but not to standard CRM functionality. Users with
this user license are entitled to use custom apps developed in your organization or installed from AppExchange.

Developer License

The Developer license is designed for users whose role is to build customizations or applications. This license provides access to
development tools and environments. It comes with one Developer sandbox, one scratch org, and access to the Dev Hub. In the
production org, this license restricts access to standard and custom objects. For example, users can’t access the Account object within
the Sales app. And because of the restriction to custom objects, users can’t be assigned access to custom apps or AppExchange apps.

The development environments provide access to Salesforce features. With a Developer sandbox, you can use all the features that exist
in the production org. The org administrator can create the Developer sandbox that was provisioned with the Developer license. A
scratch org, which can be configured to your specifications using a scratch org definition file, gives you access to features on a trial basis.
For example, you can use a scratch org to work with Financial Services Cloud or to play with Sales Cloud Einstein features. The Developer
license provides access to the Dev Hub, enabling users to create scratch orgs on a self-service basis.

Free Limited Access License

The Salesforce Limited Access - Free license provides accounts to non-admin users in your production org, when these users require
access to only a specific app, feature, or setting. Standard Salesforce objects such as Accounts, Contacts, and Opportunities aren’t
accessible with this license. The Salesforce Limited Access - Free license isn’t available in Developer Edition orgs.

The edition of the Dev Hub org determines the maximum number of the Limited Access licenses you can request.

**•** Enterprise Edition orgs can request up to 20 licenses.

**•** Unlimited Edition orgs can request up to 50 licenses.

To request this license, contact your Salesforce account executive. A Salesforce admin can upgrade a Salesforce Limited Access - Free
license to a standard Salesforce license at any time.

The Salesforce Limited Access - Free license doesn’t support certain features.

**•** To provide the ability to create and manage org shapes, assign the Salesforce user license. The Salesforce Limited Access - Free
license isn’t supported at this time.


### Provide Developers Access to Salesforce DX Tools Add a System Administrator or Standard User to Your Dev

Hub Org

**•** Users with the Salesforce Limited Access - Free license and View All Records permissions can create scratch orgs using an existing
org shape.

**•** Users with the Salesforce Limited Access - Free license and View All Records permissions can view scratch org snapshots created by
users other than themselves.

**•** The Salesforce Limited Access - Free license doesn’t provide access to some Salesforce CLI commands, such as `sf limits api`
`display` .

**•** Contact your Salesforce admin for API limits information.

SEE ALSO:

_[Add Salesforce DX Users](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_setup_add_users.htm)_

_[Permission Set for Salesforce DX Users](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_setup_add_users.htm#sfdx_setup_permission_set.xml)_

### Add a System Administrator or Standard User to Your Dev Hub Org

Add system administrator users only if their work requires that level of authority. Otherwise, add standard users and create a permission
set with the required Salesforce DX permissions.

**1.** Create a user in your Dev Hub org, if necessary.

**a.** In Setup, enter _`Users`_ in the Quick Find box, then select **Users** .

**b.** Click **New User** .

**c.** Fill out the form, and assign the System Administrator or Standard User profile.

**d.** Click **Save** .

If you’re adding a System Administrator user, you can stop here.

**2.** If you’re adding a Standard User, create a permission set for Salesforce DX users if you don’t have one.

**a.** From Setup, enter _`Permission Sets`_ in the Quick Find box, then select **Permission Sets** .

**b.** Click **New** .

**c.** Enter a label, API name, and description. The API name is a unique name used by the API and managed packages.

**d.** Select a user license option. If you plan to assign this permission set to multiple users with different licenses, select **None** .

**e.** Click **Save** . The permission set overview page appears. From here, you can navigate to the permissions you want to add or
change for Salesforce DX. For the required permissions, see Create and Assign a Permission Set to Developer Users.

**3.** Apply the Salesforce DX permission set to the Standard User.

**a.** From Setup, enter _`Permission Sets`_ in the Quick Find box, then select **Permission Sets** .

**b.** Select the Salesforce DX permission set.

**c.** In the permission set toolbar, click **Manage Assignments** .

**d.** Click **Add Assignments** .

**e.** Select the user to assign the permission set to.

**f.** Click **Assign** .

**g.** Click **Done** .

You can limit a user’s access by modifying the permissions.


### Provide Developers Access to Salesforce DX Tools Add a Developer User to Your Dev Hub Org Add a Developer User to Your Dev Hub Org

Using a Developer license, add a user with the Developer profile and assign them the Developer permission set.

The Developer license is a paid license that is designed for users whose role is to build customizations or applications. This license provides
access to development tools and environments. It comes with one Developer sandbox, one scratch org, and access to the Dev Hub. In
the production org, this license restricts access to standard and custom objects.

**1.** Create a user in your Dev Hub org.

**a.** In Setup, enter _`Users`_ in the Quick Find box, then select **Users** .

**b.** Click **New User** .

**c.** Fill out the form.

**d.** Select **Developer** for User License, and then **Developer** for Profile.

**e.** After filling out the remaining information, click **Save** .

**2.** Assign the built-in Developer permission set to the user.

**a.** On the user's detail page, in the Permission Set Assignments related list, click **Edit Assignments** .

**b.** In the Available Permission Sets, add the Developer permission set and click **Save** .

The Developer permission set grants access to Dev Hub features and second-generation packages. For details, see Create and Assign a
Permission Set to Developer Users.

### Add a Limited Access User to Your Dev Hub Org

If your users only require access to the Dev Hub, the Salesforce Limited Access - Free license is a good approach. The Salesforce Limited
Access - Free license is available by request. After this license is provisioned add a user with this license and the Limited Access user
profile, and then create and assign them a permission set to the required Dev Hub objects.

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

### Create and Assign a Permission Set to Developer Users

To give full access to the Dev Hub org, create and assign a custom permission set that grants access to required Dev Hub objects. Or if
you have the Developer license, assign the Developer permission set.


Provide Developers Access to Salesforce DX Tools Create and Assign a Permission Set to Developer Users

Standard Developer Permission Set

If you're providing access to the Dev Hub org using the standard Developer license, it also includes a built-in Developer permission set.
This permission set provides the required permissions for scratch orgs, and unlocked and second-generation managed packaging. You
can use the provided Developer permission set or create your own.

Create a Permission Set

[Follow the steps to create a permission set, then add the required scratch org and packaging permissions.](https://help.salesforce.com/s/articleView?id=platform.perm_sets_create.htm&language=en_US)

Required Permissions for Scratch Orgs

**•** Object Settings > Scratch Org Infos > Read, Create, Edit, and Delete

**•** Object Settings > Active Scratch Orgs > Read, Edit, and Delete

Required Permissions for Unlocked Packaging and Second-Generation Managed
Packaging

To work with unlocked or second-generation managed packages in the Dev Hub org, the permission set must contain the scratch org
permissions and:

**•** Object Settings > Namespace Registries > Read

**•** System Permissions > Create and Update Second-Generation Packages

The system permission provides access to:

Assign Permission Set to Users

[To assign one or more users to a permission set, or to remove a user from a permission set, see Manage Permission Set Assignments in](https://help.salesforce.com/s/articleView?id=platform.perm_sets_manage_assignments.htm&language=en_US)
_Salesforce Help_ .


# CHAPTER 3 Project Setup

In this chapter ...

**•** Sample Repository
on GitHub

A Salesforce DX project provides a project structure for your org’s metadata (code and configuration),
org templates, sample data, and all your team’s tests. To bring consistency to your team’s development
processes, store these items in a source control system (SCS). Retrieve the contents of your team’s
repository when you’re ready to develop a new feature.

**•** Create a Salesforce
What makes a project a Salesforce DX project? It includes an `sfdx-project.json` file, which
DX Project
defines the project’s configuration. This `.json` file includes connected app information for Salesforce

**•** Salesforce DX Project

CLI, in which directories project files are located, packaging directory structure for 2GP packages, and

Structure and Source

which API version you want to use, if not the latest.

Format

You have different options to create a Salesforce DX project depending on how you want to begin. You

**•** How to Exclude
can use your preferred SCS. Most of our examples use Git.
Source When Syncing

**•** Create a Salesforce
DX Project from
Existing Source

Source Format

**•** Salesforce DX
Usernames and Orgs

**•** Link a Namespace to
a Dev Hub Org

**•** Salesforce DX Project
Configuration

**•** Multiple Package
Directories

**•** Replace Strings in
Code Before
Deploying or
Packaging


## Project Setup Sample Repository on GitHub Sample Repository on GitHub

To get started quickly, see the `dreamhouse-lwc` GitHub repo. This standalone application contains an example DX project with
multiple Apex classes, Aura components, custom objects, sample data, and Apex tests.

Cloning this repo creates the directory `dreamhouse-lwc` . See the repo’s Readme for more information.

Assuming that you’ve already set up Git, use the `git clone` command to clone the main branch of the repo from the command
line.

To use HTTPS:

```
   git clone https://github.com/trailheadapps/dreamhouse-lwc

```

To use SSH:

```
   git clone git@github.com:trailheadapps/dreamhouse-lwc.git

```

If you don’t want to use Git, download a .zip file of the repository’s source using Clone, or download on the GitHub website. Unpack the
source anywhere on your local file system.

See Get Started by Using a Sample Repo for the next steps.

Tip: [Check out more complex examples in the Sample Gallery.](https://developer.salesforce.com/code-samples-and-sdks)

The Sample Gallery contains sample apps that show what you can build on the Salesforce platform. They’re continuously updated
to incorporate the latest features and best practices.

## Create a Salesforce DX Project

A Salesforce DX project has a specific structure and a configuration file that identifies the directory as a Salesforce DX project.

**1.** Change to the directory where you want the DX project located.

**2.** Create the DX project.

```
     sf project generate --name MyProject

```

If you don’t specify an output directory with the `--output-dir` flag, the project directory is created in the current location. You
can also use the `--default-package-dir` flag to specify the default package directory to target when syncing source to
and from the org. If you don’t indicate a default package directory, this command creates a default package directory, `force-app` .

Use the `--template` flag to specify what your project initially looks like. Each template provides a complete directory structure
that takes the guesswork out of where to put your source. If you choose `--template empty`, your project contains these
sample configuration files to get you started.

**•** `.forceignore`

**•** `config/project-scratch-def.json`

**•** `sfdx-project.json`

**•** `package.json`

If you choose `--template standard`, your project also contains these files that are especially helpful when using Salesforce
Extensions for VS Code. If you don’t specify the `--template` flag, the `project generate` command uses the standard
template.

**•** `.gitignore` : Makes it easier to start using Git for version control.


## Project Setup Salesforce DX Project Structure and Source Format

**•** `.prettierrc` and `.prettierignore` : Make it easier to start using Prettier to format your Aura components.

**•** `.vscode/extensions.json` : Causes Visual Studio Code, when launched, to prompt you to install the recommended
extensions for your project.

**•** `.vscode/launch.json` : Configures Replay Debugger, making it more discoverable and easier to use.

**•** `.vscode/settings.json` : By default, this file has one setting for excluding certain files and folders in searches and quick
open. You can change this value or add other settings.

If you choose `--template analytics`, you get all the helpful basic and VS Code files. But the default package directory
contains fewer directories, such as for storing Analytics template bundles. `/force-app/main/default/waveTemplates` )
and a few other metadata types, such as Apex classes and LWC components.

Example:

```
      sf project generate --name mywork --template standard

      sf project generate --name mywork --default-package-dir myapp-source

```

Next steps:

**•** (Optional) Register the namespace with the Dev Hub org.

**•** Configure the project ( `sfdx-project.json` ). If you use a namespace, update this file to include it.

**•** Create a scratch org definition that produces scratch orgs with the features you need for your project. The `config` directory of
your new project contains a sample scratch org definition file ( `project-scratch-def.json` ).

SEE ALSO:

Create a Salesforce DX Project from Existing Source

Salesforce DX Project Configuration

Link a Namespace to a Dev Hub Org

Build Your Own Scratch Org Definition File

How to Exclude Source When Syncing

_VS Code Command_ [: SFDX: Create Project, SFDX: Create Project with Manifest](https://developer.salesforce.com/docs/platform/sfvscode-extensions/guide/create-project.html)

## Salesforce DX Project Structure and Source Format

A Salesforce DX project has a specific project structure and source format. Source format uses a different set of files and file extensions
from what Metadata API uses. When you retrieve metadata from the org with the `project retrieve start` command, Salesforce
CLI stores it in source format in your project. When you deploy metadata, Salesforce CLI converts it into the format that Metadata API
requires.

Source Transformation

It’s not uncommon for metadata formatted source to be very large, making it difficult to find what you want. If you work on a team with
other developers who update the same metadata at the same time, you have to deal with merging multiple updates to the file. If you’re
thinking that there has to be a better way, you’re right.

Before, all custom objects and object translations were stored in one large metadata file.


Project Setup Salesforce DX Project Structure and Source Format

We solve this problem by providing a new source shape that breaks down, or _decomposes_, these large source files to make them more
digestible and easier to manage with a version control system. It’s called source format. Source format makes it much easier to find what
you want to change or update. And you're less likely to overwrite a team member's change if it's decomposed.

A Salesforce DX project decomposes custom objects and custom object translations into intuitive subdirectories by default. If you want,
you can also specify that other metadata types, such as permission sets and custom labels, are decomposed.

See Decomposed Metadata Types for details on how we decompose custom objects and custom object translations and how to configure
more metadata types to be similarly decomposed.

Static Resources

Static resources must reside in the `/main/default/staticresources` directory. The `project deploy` and `project`
`retrieve` commands support auto-expanding or compressing archive MIME types within your project. These behaviors support
both the `.zip` and `.jar` MIME types. This way, the source files are more easily integrated in your Salesforce DX project and version
control system.

For example, if you upload a static resource archive through the scratch org’s Setup UI, the `project retrieve start` command
expands it into its directory structure within the project. To mimic this process from the file system, add the directory structure to compress
directly into the static resources directory root, then create the associated `.resource-meta.xml` file. If an archive exists as a single
file in your project, it’s always treated as a single file and not expanded.


Project Setup Salesforce DX Project Structure and Source Format

This example illustrates how different types of static resources are stored in your local project. You can see an expanded `.zip` archive
called `expandedzippedresource` and its related `.resource-meta.xml` file. You also see a couple `.jpg` files being stored
with their MIME type, and a single file being stored with the legacy `.resource` extension

[See Salefsorce Help: Static Resources for more information.](https://help.salesforce.com/s/articleView?id=platform.pages_static_resources.htm&type=5&language=en_US)

File Extensions

When you convert existing metadata format to source format, we create an XML file for each bit. All files that contain XML markup now
have an `.xml` extension so that your XML editor recognizes them as XML files and you can look at them. To sync your local projects
and scratch orgs, Salesforce DX projects use a particular directory structure for custom objects, custom object translations, Lightning
web components, Aura components, and documents.

For example, if you had an object called Case, source format provides an XML version called `Case.object-meta.xml` . If you have
an app called DreamHouse, we create a file called `DreamHouse.app-meta.xml` . You get the idea.

Traditionally, static resources are stored on the file system as binary objects with a `.resource` extension. Source format handles static
resources differently by supporting content MIME types. For example, `.gif` files are stored as a `.gif` instead of `.resource` . By
storing files with their MIME extensions, you can manage and edit your files using the associated editor on your system.

You can have a combination of existing static resources with their `.resource` extension, and newly created static resources with
their MIME content extensions. Existing static resources with `.resource` extensions keep that extension, but any new static resources
show up in your project with their MIME type extensions. We allow `.resource` files to support the transition for existing customers.
Although you get this additional flexibility, we recommend storing your files with their MIME extensions.


Project Setup Salesforce DX Project Structure and Source Format

Aura Components

Aura bundles and components must reside in a directory named `aura` under the _`<package directory>`_ directory.

Lightning Web Components

Lightning web components must reside in a directory named `lwc` under the _`<package directory>`_ directory.


### Project Setup Decomposed Metadata Types

ExperienceBundle and DigitalExperienceBundle for Experience Cloud Sites

The ExperienceBundle metadata type represents an Aura or an LWR site, and must reside in a directory named `experiences` under
the _`<package directory>`_ directory. The `experiences` directory contains a folder for each Aura or LWR site in your org.

The DigitalExperiencBundle metadata type represents an enhanced LWR site, and must reside in a directory named
`digitalExperiences` under the _`<package directory>`_ directory. The `digitalExperiences/site` directory
contains a folder for each enhanced LWR site in your org.

Documents

Documents must be inside the directories of their parent document folder. The parent document folder must be in a directory called
`documents` . Each document has a corresponding metadata XML file that you can view with an XML editor.

### Decomposed Metadata Types

Decomposition refers to splitting a single, often large, metadata XML file into smaller XML files based on its subtypes. The result is referred
to as source format. By default, a Salesforce DX project always decomposes custom objects and custom object translations. You can also
optionally specify that other metadata types, such as permission sets and custom labels, be decomposed.


Project Setup Decomposed Metadata Types

Start Decomposing the Optional Metadata Types (Beta)

The Salesforce DX project file ( `sfdx-project.json` ) determines which of the optional metadata types are decomposed. But don't
update it manually. Rather, run the `project convert source-behavior` Salesforce CLI command which updates the project
file for you, and also breaks up the associated metadata file XML into smaller files.

Note: Decomposition of permission sets, custom labels, sharing rules, and workflows is a pilot or beta service that is subject to
[the Beta Services Terms at Agreements - Salesforce.com or a written Unified Pilot Agreement if executed by Customer, and](https://www.salesforce.com/company/legal/agreements/)
[applicable terms in the Product Terms Directory. Use of this pilot or beta service is at the Customer's sole discretion.](https://ptd.salesforce.com/?_ga=2.247987783.1372150065.1709219475-629000709.1639001992)

Before you begin, commit all your DX project source files to your version control system. Committing the files ensures that you can easily
see what changed in your project. You can also revert the changes if necessary.

**1.** Open a terminal or command prompt and change to your Salesforce DX project directory.

**2.** Optionally execute a dry run of the CLI command to display what it does before it actually changes your DX project. For example,
to dry run the decomposition of permission sets, run this command:

```
     sf project convert source-behavior --behavior decomposePermissionSetBeta2 --dry-run

```

See this table for the `--behavior` values for the other metadata types you can optionally decompose.

**3.** When you're ready to update your DX project, run the same command but without the `--dry-run` flag:

```
     sf project convert source-behavior --behavior decomposePermissionSetBeta2

```

If your default org is enabled for source tracking, the CLI command returns an error. This error is expected, because decomposing
your local metadata causes the source tracking system to get out of sync with the org. Follow the directions in the error message
and try again.

**4.** If you deleted your default org, recreate it and deploy your local source.

When the `project convert source-behavior` command finishes, your `sfdx-project.json` file is updated to always
decompose permission sets, or whatever type you specified. The existing source files in your local package directories are converted
into the new decomposed format. You can now deploy and retrieve your metadata as usual.

If you change your mind and don't want to decompose the optional types, revert the changes made by the `project convert`
`source-behavior` and recreate your source-tracking orgs.

This table provides the list of metadata types that are decomposed by default, and the types that you can optionally decompose. For
optional metadata types, the table also shows the corresponding `--behavior` flag value.


Project Setup Decomposed Metadata Types

Source Format Structure of Decomposed Metadata Types

This section provides details about how the decomposed metadata types are broken down into their local source format structure.

Note: Decomposition of the optional metadata types (custom labels, permission sets, sharing rules, and workflows) is a pilot or
[beta service that is subject to the Beta Services Terms at Agreements - Salesforce.com or a written Unified Pilot Agreement if](https://www.salesforce.com/company/legal/agreements/)
[executed by Customer, and applicable terms in the Product Terms Directory. Use of this pilot or beta service is at the Customer's](https://ptd.salesforce.com/?_ga=2.247987783.1372150065.1709219475-629000709.1639001992)
sole discretion.

Custom Objects

Custom objects are decomposed by default.

When you convert from metadata format to source format, your custom objects are placed in the
_`<package-directory>`_ `/main/default/objects` directory. Each object has its own subdirectory that reflects the type of
custom object. Some parts of the custom objects are extracted into in these subdirectories:

**•** `businessProcesses`

**•** `compactLayouts`

**•** `fields`

**•** `fieldSets`

**•** `indexes`

**•** `listViews`

**•** `recordTypes`

**•** `sharingReasons`

**•** `validationRules`

**•** `webLinks`

The parts of the custom object that aren’t extracted are placed in a _`<object-name>`_ `.object-meta.xml` file.

Custom Object Translations

Custom object translations are decomposed by default.

Custom object translations reside in the _`<package-directory>`_ `/main/default/objectTranslations` directory, each
in their own subdirectory named after the custom object translation. Custom object translations and field translations are extracted into
their own files within the custom object translation’s directory.

**•** For field names, _`<field_name>`_ `.fieldTranslation-meta.xml`

**•** For object names, _`<object_name>`_ `.objectTranslation-meta.xml`

The remaining pieces of the custom object translation that aren’t field translations are placed in a file called
_`<objectTranslation-name>`_ `.objectTranslation-meta.xml` .

[See Salesforce Help: Translation Workbench for more information.](https://help.salesforce.com/s/articleView?id=platform.workbench.htm&type=5&language=en_US)

Custom Labels (Beta)

Custom labels aren’t decomposed by default; you must specifically configure your DX project to decompose them. See Start Decomposing
the Optional Metadata Types (Beta) for details.


Project Setup Decomposed Metadata Types

By default, all custom labels for your entire org are contained in a single file called `CustomLabels.labels-meta.xml` that
resides in the _`<package-directory>`_ `/labels` directory. Each package directory can have its own
`CustomLabels.labels-meta.xml` file.

If you choose to decompose custom labels, individual `CustomLabel` components appear one time in a dedicated
`*.label-meta.xml` source file. The name of each `*.label-meta.xml` source file is derived from the `fullName` of the
`CustomLabel` component it contains. This example shows four custom label files in the default package directory.

You can further organize custom labels in your DX project, as long as you follow these guidelines:

**•** All `*.label-meta.xml` source files must be contained by a `labels` source directory.

**•** You can create a `labels` source directory in each of your multiple package directories in your DX project.

**•** You can create subdirectories of the `labels` source directory to further organize your `*.label-meta.xml` files.

Here are some examples of different ways you can organize custom labels.


Project Setup Decomposed Metadata Types

External Service Registrations (Beta)

External service registrations aren’t decomposed by default; you must specifically configure your DX project to decompose them. See
Start Decomposing the Optional Metadata Types (Beta) for details.

By default, an external service registration is contained in a file called
_`<external-service-registration-name>`_ `.externalServiceRegistration-meta.xml` that resides in the
_`<package directory>`_ `/main/default/externalServiceRegistrations` directory.

If you choose to decompose external service registrations, they’re still stored in the top-level _`<package`_
_`directory>`_ `/main/default/externalServiceRegistrations` directory. But each registration is decomposed into
two source files when you retrieve it to your Salesforce DX project. One of the files is in YAML format and contains an OpenAPI spec.
When you deploy the registration to your org, the two files are re-converted into the one metadata API XML file.

For example, let's say the name of your external service registration metadata component is `BankService` . The two source files after
decomposition are:

**•** `BankService.yaml` : A YAML file that contains the contents of the `schema` metadata component field. This field contains
an OpenAPI 2.0.x or OpenAPI 3.0.x schema in JSON or YAML format. If the field's content is in JSON format in your org, it's always
converted to YAML format when retrieved to your DX project.

**•** `BankService.externalServiceRegistration-meta.xml` : A standard metadata API XML file that contains all the
fields _except_ `schema` .

Permission Sets (Beta)

Permission sets aren’t decomposed by default; you must specifically configure your DX project to decompose them. See Start Decomposing
the Optional Metadata Types (Beta) for details.

By default, a permission set is contained in a file called _`<permission-set-name>`_ `.permissionset-meta.xml` that resides
in the _`<package-directory>`_ `/main/default/permissionsets` directory.

If you choose to decompose permission sets, they’re still stored in the top-level
_`<package-directory>`_ `/main/default/permissionsets` directory. This graphic shows how a sample permission set
called `MyPermSet` is then decomposed into its smaller XML files.


Project Setup Decomposed Metadata Types

Here are some highlights about the decomposition:

**•** The decomposed files for a specific permission set are contained in a subdirectory named the same as the permission set, `MyPermSet`
in our example.

**•** The specific permission set directory contains a single file called `<Name>.permissionset-meta.xml file`, where
_`<Name>`_ is the directory name. This XML file contains information such as the permission set label, description, and license. In our
example, the file is called `MyPermSet.permissionset-meta.xml` .

**•** The `objectSettings` directory consolidates object-related permissions and settings into a single file for each object, with
name _`<ObjectName>`_ `.objectSettings-meta.xml` .

**•** The remaining permissions and settings are in focused files with a category-specific extension, such as
`MyPermSet.applicationVisibilities-meta.xml` or `MyPermSet.flowAccesses-meta.xml` .

Sharing Rules (Beta)

Sharing rules aren’t decomposed by default; you must specifically configure your DX project to decompose them. See Start Decomposing
the Optional Metadata Types (Beta) for details.

By default, all sharing rules for an object are contained in a file called _`<object-name>`_ `.sharingRules-meta.xml` that resides
in the _`<package directory>`_ `/main/default/sharingRules` directory. The _`object-name`_ refers to the object to
which the sharing rule applies.

If you choose to decompose sharing rules, they’re still stored in the top-level _`<package`_
_`directory>`_ `/main/default/sharingRules` directory. But the sharing rules are grouped into subdirectories with the same
name as the object that the sharing rule is associated with. Within this object subdirectory, parts of the sharing rule are extracted into
these subdirectories.

**•** `sharingCriteriaRules`

**•** `sharingGuestRules`

**•** `sharingOwnerRules`

**•** `sharingTerritoryRules`

The parts of the sharing rule that aren’t extracted are placed in a _`<object-name>`_ `.sharingRules-meta.xml` file.


## Project Setup How to Exclude Source When Syncing

Workflows (Beta)

Workflows aren’t decomposed by default; you must specifically configure your DX project to decompose them. See Start Decomposing
the Optional Metadata Types (Beta) for details.

By default, all workflows for an object are contained in a file called _`<object-name>`_ `.workflow-meta.xml` that resides in the
_`<package directory>`_ `/main/default/workflows` directory. The _`object-name`_ refers to the object to which the
workflow applies.

If you choose to decompose workflows, they’re still stored in the top-level _`<package`_
_`directory>`_ `/main/default/workflows` directory. But the workflows are grouped into subdirectories with the same name
as the object that the workflow is associated with. Within this object subdirectory, parts of the workflow are extracted into these
subdirectories.

**•** `workflowAlerts`

**•** `workflowFieldUpdates`

**•** `workflowKnowledgePublishes`

**•** `workflowOutboundMessages`

**•** `workflowRules`

**•** `workflowSends`

**•** `workflowTasks`

The parts of the workflow that aren’t extracted are placed in a _`<object-name>`_ `.workflow-meta.xml` file.

## How to Exclude Source When Syncing

When syncing metadata between your local file system and a target org, you often have source files you want to exclude. Similarly, you
often want to exclude certain files when converting source to Salesforce DX source format. In both cases, you can exclude individual
files or all files in a specific directory with a `.forceignore` file.

The `.forceignore` file excludes files when running most of the `project` commands, such as `project deploy start`,
`project retrieve start`, `project convert source`, and `project delete source` .

Structure of the **`.forceignore`** File

The `.forceignore` file structure mimics the `.gitignore` structure. Each line in `.forceignore` specifies a pattern that
corresponds to one or more files. The files typically represent metadata components, but can be any files you want to exclude, such as
LWC configuration JSON files or tests.

The `project` commands, when parsing the `.forceignore` file, use the same rules and patterns as the `.gitignore` file. A
few common examples of these rules and patterns include:

**•** Always use the forward slash ( `/` ) as a directory separator, even on operating systems that use back slashes, such as Microsoft Windows.

**•** An asterisk ( `*` ) matches anything except a forward slash ( `/` ).

**•** Two consecutive asterisks ( `**` ) in patterns have special meaning, depending on where they’re located in the pathname. See for
examples.

**•** For readability, use blank lines as separators in the `.forceignore` file.

[There are many more rules and patterns. See the git documentation for details.](https://git-scm.com/docs/gitignore)


Project Setup How to Exclude Source When Syncing

Determine the Exact Filename for a Metadata Component

As you build your `.forceignore` file, you sometimes need the exact name of the metadata components that you want to exclude.
The easiest way to determine the name of a particular component is to look at the package directory that contains the source files, such
as the default `force-app` directory.

For example, profile metadata components live in the `main/default/profiles` directory. Let’s say that the directory contains
the source file `NotUsedProfile.profile-meta.xml` . To specify that the `project` commands exclude this component,
add this entry to your `.forceignore` :

```
   **/NotUsedProfile.profile-meta.xml

```

Another way to determine the exact name of a metadata component is to look at the output of the `project` commands if you’re
also using source tracking. For example, if you have either local or remote changes, run the `project deploy preview` or
`project retrieve preview` command to display the full pathname of the changed components. This output displays the
filename of the `Dreamhouse` permission set and the `Settings` custom tab in the Path column of the Will Deploy section:

```
   sf project deploy preview

   Will Deploy [2] files.

    Type Fullname Path

    ───────────────────────

   ───────────────────────────────────────────────────────────────────────

    PermissionSet dreamhouse

   force-app/main/default/permissionsets/dreamhouse.permissionset-meta.xml

    CustomTab Settings force-app/main/default/tabs/Settings.tab-meta.xml

```

Other Files That the Source Commands Ignore

The source commands ignore these files even if they aren’t included in your `.forceignore` file:

**•** Any source file or directory that begins with a “dot”, such as `.DS_Store` or `.sf`

**•** Any file that ends in `.dup`

**•** `package2-descriptor.json`

**•** `package2-manifest.json`

Exclude Remote Changes Not Yet Synced with Your Local Source

Sometimes, you make a change directly in an org but you don’t want to pull that change into your local DX project. To exclude remote
metadata changes, add an entry to `.forceignore` that represents the metadata source file that would be created if you _did_ retrieve
it.

For example, if you have a permission set named `Dreamhouse,` add this entry to `.forceignore` :

```
   **/Dreamhouse.permissionset-meta.xml

```

Exclude MetadataWithContent Types

[Metadata components that include content, such as ApexClass or EmailTemplate, extend the MetadataWithContent type. These](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_metadatawithcontent.htm)
components have two source files: one for the content itself, such as the Apex code or email template, and the accompanying metadata
file. For example, the source files for the HelloWorld Apex class are `HelloWorld.cls` and `HelloWorld.cls-meta.xml` .


Project Setup How to Exclude Source When Syncing

To exclude a MetadataWithContent component, such as an ApexClass, either list both source files in the `.forceignore` file, or use
an asterisk. For example:

```
   # Explicilty list the HelloWorld source files to be excluded

   helloWorld/main/default/classes/HelloWorld.cls

   helloWorld/main/default/classes/HelloWorld.cls-meta.xml

   # Exclude the HelloWorld Apex class using an asterisk

   helloWorld/main/default/classes/HelloWorld.cls*

```

Exclude Bundles and File Groups

Use two consecutive asterisks ( `**` ) to ignore files spread across multiple directories with just one `.forceignore` entry.

For example, to exclude all resource files related to a Lightning web component named `myLwcComponent`, add this entry to exclude
the entire component bundle:

```
   **/lwc/myLwcComponent

```

To exclude all Apex classes:

```
   **/classes

```

Metadata with Special Characters

If a metadata name has special characters (such as forward slashes, backslashes, or quotation marks), we encode the file name on the
local file system for all operating systems. For example, if you retrieve a custom profile called Custom: Marketing Profile, the colon is
encoded in the resulting file name.

```
   Custom%3A Marketing Profile.profile-meta.xml

```

If you reference a file name with special characters in `.forceignore`, use the encoded file name.

Where to Put **`.forceignore`**

Be sure the paths that you specify in `.forceignore` are relative to the directory containing the `.forceignore` file. For the
`.forceignore` file to work its magic, you must put it in the proper location, depending on which command you’re running.

**•** Add the `.forceignore` file to the root of your project for the `project` source tracking commands.

**•** Add the file to the metadata retrieve directory (with `package.xml` ) for `project convert mdapi` .

Multiple **`.forceignore`** Files in a Single Project

You typically have only one `.forceignore` file in your Salesforce DX project, usually in the project’s root directory. However, it’s
possible to have more, so it’s important to know which `.forceignore` file the `project` commands use when deploying or
retrieving a particular source file.

When the `project` commands are determining whether to exclude a source file, they traverse up the directory tree from where the
source file lives, looking for a `.forceignore` file. When they find one, they refer to it to determine whether to exclude the source
file, and then stop. They don’t continue looking for another `.forceignore` file.

Let’s look at an example. Imagine you have a `.forceignore` file in the root directory of your project, and it doesn’t exclude any Apex
classes. In addition to the standard `force-app` package directory, you’ve configured a second package directory called


Project Setup How to Exclude Source When Syncing

`second-package`, which has its own `.forceignore` file at its root. This `.forceignore` file excludes Apex classes that start
with `Paged` . The `second-package` package directory has an Apex class called `PagedResult` in its `main/default/classes`
subdirectory. Here’s what it looks like in VS Code.

Let’s say you run this command in the project to deploy all Apex classes in all package directories.

```
   sf project deploy start --metadata ApexClass

```

Because the `PagedResult` Apex class lives in the `second-package` package directory, the deploy command refers to the
`.forceignore` in that directory, and excludes the source files associated with the Apex class. The command doesn’t refer to the
project `.forceignore` file.

Let’s now assume that the `force-app` directory contains a `PagedNewResult` Apex class. The deploy command refers to the
project `.forceignore` file and thus doesn’t exclude the associated source files. Or in other words, the command deploys the files
associated with the `PagedNewResult` Apex class.

Sample Syntax

Here are some options for indicating which source to exclude. In this example, all paths are relative to the project root directory.

```
   # Specify a relative path to a directory from the project root

   helloWorld/main/default/classes

   # Specify a wildcard directory - any directory named “classes” is excluded

   **classes

   # Specify file extensions

   **.cls*

   **.pdf

   # Specify a specific file

   helloWorld/main/default/HelloWorld.cls*

```


## Project Setup Create a Salesforce DX Project from Existing Source

List the Files and Directories Currently Being Ignored

Use the `project list ignored` command to list the files and directories in your project that the `project` commands are
currently ignoring. The `project list ignored` command refers to the `.forceignore` file to determine the list of ignored
files.

To list all the files in all package directories that are ignored, run the command without any flags. Use the `--source-dir` flag to
limit the check to a specific file or directory. If you specify a directory, the command checks all subdirectories recursively.

This example checks if a particular file is ignored.

```
   sf project list ignored --source-dir package.xml

```

This example gets a list of all ignored files in a specific directory.

```
   sf project list ignored --source-dir force-app/main/default

```

Sample output if the command finds ignored files:

```
   Found the following ignored files:

   force-app/main/default/aura/.eslintrc.json

   force-app/main/default/lwc/.eslintrc.json

   force-app/main/default/lwc/jsconfig.json

```

Sample output if the file isn’t ignored:

```
   No ignored files found in paths:

   README.md

```

SEE ALSO:

Retrieve Changes to Profiles with Source Tracking

## Create a Salesforce DX Project from Existing Source

If you’re a Salesforce developer, partner, or ISV, you likely have existing source in a managed package in your packaging org or application
source in your sandbox or production org. Before you begin using Salesforce DX, retrieve the existing source into a Salesforce DX project.

**1.** Create a Salesforce DX project.

```
     sf project generate --name MyProject

```

**2.** Change to the project directory.

```
     cd MyProject

```

**3.** Retrieve your source by running the `project retrieve start` command. The location and format of your current source
determine the command flags you must use.


Project Setup Create a Salesforce DX Project from Existing Source

Tip: If you already have a repo that follows the directory structure created from a Metadata API retrieve, then your source files
in the repo are in metadata format. You can convert these files into source format and include them in your Salesforce DX
project. See Convert Files in Metadata Format to Source Format for details.

**4.** If the retrieve created a package directory in your project, add it to your `sfdx-project.json` file.

Do you have source in a sandbox or production org, but you don’t have a manifest file ( `package.xml` ) for retrieving it to your project?
Use the `project generate manifest` CLI command to create one. For example, this command generates a manifest from
the metadata components in the org with the alias `prod-org` .

```
sf project generate manifest --from-org prod-org

```

See the command help for more examples and information.

```
sf project generate manifest --help

```


## Project Setup Convert Files in Metadata Format to Source Format

[You can also refer to Sample package.xml Manifest Files in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/manifest_samples.htm) _Metadata API Developer Guide_ .

SEE ALSO:

Create a Salesforce DX Project

Salesforce DX Project Structure and Source Format

Salesforce DX Project Configuration

## Convert Files in Metadata Format to Source Format

_VS Code Command_ [: SFDX: Create Project, SFDX: Create Project with Manifest](https://developer.salesforce.com/docs/platform/sfvscode-extensions/guide/create-project.html)

## Convert Files in Metadata Format to Source Format

If you already have a repo in which you’ve retrieved metadata from an org using the Metadata API directly, the files are in metadata
format. You can convert these files into source format and add them to your Salesforce DX project. You can then deploy and retrieve
them to and from your org using CLI commands and use source tracking to track changes.

The convert command ignores all files that start with a “dot,” such as `.DS_Store` . To exclude more files from the convert process,
add a `.forceignore` file.

**1.** Change to your Salesforce DX project directory.

**2.** Convert the files from metadata format to source format with the `project convert mdapi` command. Let’s say your
metadata-format files are in a directory called `/Users/testing/mdapi_project` .

```
     sf project convert mdapi --root-dir /Users/testing/mdapi_project

```

The `--root-dir` flag is the name of the directory that contains the metadata format files.

The converted source is stored in the default package directory indicated in the `sfdx-project.json` file, typically named
`force-app` . Use the `--output-dir` flag to put the converted files in a different package directory; the command creates the
directory if it doesn’t exist.

**3.** If the convert created a package directory in your project, add it to your `sfdx-project.json` file.

SEE ALSO:

Salesforce DX Project Configuration

## Salesforce DX Usernames and Orgs

Many Salesforce CLI commands connect to an org to complete their task. For example, the `org create scratch` command,
which creates a scratch org, connects to a Dev Hub org. The `project deploy start` and `project retrieve start`
commands synchronize source code between your project and an org. In each case, the CLI command requires a username to determine
which org to connect to. Usernames are unique within the entire Salesforce ecosystem and are associated with just one org.

When you create a scratch org, the CLI generates a username. The username looks like an email address, such as
test-wvkpnfm5z113@example.com. You don’t need a password to connect to or open a scratch org, although you can generate one
later with the `org generate password` command.

Salesforce recommends that you set the org that you connect to the most during development as your default org. The easiest way to
set it is when you log in to a Dev Hub org or create a scratch org; you can also use the `config` commands. Specify the


Project Setup Salesforce DX Usernames and Orgs

`--set-default-dev-hub` or `--set-default` flag, respectively. You can also create an alias to make the org’s usernames
more readable and intuitive. You can use usernames or their aliases interchangeably for all CLI commands that connect to an org.

These examples set the default org and aliases when you log in and authorize an org, in this case a Dev Hub org, and then when you
create a scratch org.

```
   sf org login web --set-default-dev-hub --alias my-hub-org

   sf org create scratch --definition-file config/project-scratch-def.json --set-default

   --alias my-scratch-org

```

To verify whether a CLI command requires an org connection, look at its flag list with the `-h` flag. Commands that have the
`--target-dev-hub` flag connect to the Dev Hub org. Similarly, commands that have `--target-org` connect to scratch orgs,
sandboxes, and so on. This example displays the flag list and help information about `org create scratch` .

```
   sf org create scratch -h

```

When you run a CLI command that requires an org connection and you don’t specify a username, the command uses the default. To
display all the orgs that you've authorized or created, run `org list` . The default Dev Hub and scratch orgs are marked with an emoji
on the left; see the legend at the end of the display for details.

Let's run through a few examples. This example deploys source code to the org that you've set as the default.

```
   sf project deploy start

```

To specify an org other than the default, use `--target-org` . For example, let’s say you created a scratch org with the alias
`my-other-scratch-org` . It’s not the default but you still want to deploy source to it.

```
   sf project deploy start --target-org my-other-scratch-org

```

This example shows how to use the `--target-dev-hub` flag to specify a non-default Dev Hub org when creating a scratch org.

```
   sf org create scratch --target-dev-hub jdoe@mydevhub.com --definition-file my-org-def.json

    --alias yet-another-scratch-org

```

More About Setting Default Orgs

If you’ve already created a scratch org, you can set it, or any other org, as your default by running the `config set` command from
your project directory.

```
   sf config set target-org test-wvkpnfm5z113@example.com

```

The command sets the value locally, so it works only for the current project. To use the default org for all projects on your computer,
specify the `--global` flag. You can run this command from any directory. Local project defaults override global defaults.

```
   sf config set target-org test-wvkpnfm5z113@example.com --global

```

The process is similar to set a default Dev Hub org, except you use the `target-dev-hub` config variable.

```
   sf config set target-dev-hub jdoe@mydevhub.com

```

To unset a config variable, run the `config unset` command. Use the `--global` flag to unset it for all your Salesforce DX projects.

```
   sf config unset target-org --global

```

To view all the configuration variables you’ve set, run `config list` ; if you run it from a project directory it also lists the local ones.

```
   sf config list

```


Project Setup Salesforce DX Usernames and Orgs

More About Aliasing

Use the `alias set` command to set an alias for a scratch org you’ve already created, or any org after you’ve authorized it. You can
create an alias for any org: Dev Hub, scratch org, production, sandbox, and so on. So when you issue a command that requires the org’s
username, using an easily-remembered alias speeds things up.

```
   sf alias set my-scratch-org test-wvkpnfm5z113@example.com

```

An alias also makes it easy to set a default org. The previous example of using `config set` to set `target-org` now becomes
much more digestible when you use an alias rather than the actual username.

```
   sf config set target-org my-scratch-org

```

Set multiple aliases with a single command by separating the name-value pairs with a space; in this case you must use the equal sign.

```
   sf alias set org1=<username> org2=<username>

```

You can associate an alias with only one username at a time. If you set it multiple times, the alias points to the most recent username.
For example, if you run the following two commands, the alias my-org is set to test-wvkpnfm5z113@example.com.

```
   sf alias set my-org test-blahdiblah@example.com

   sf alias set my-org test-wvkpnfm5z113@example.com

```

To view all aliases that you’ve set, use one of the following commands.

```
   sf alias list

   sf org list

```

To remove an alias, use the `alias unset` command.

```
   sf alias unset my-org

```

List All Your Orgs

Use the `org list` command to display the usernames and aliases for the orgs that you’ve authorized and the active scratch orgs
that you’ve created.

```
   sf org list

      Type Alias Username Org ID

     Status Expires

    ──────────────────────────────────────────────────────────────────────────────────────

    ───────────────────────────────

    D DevHub JulesDevHub jules@sf.com 00DB0001234c7jiMAA

    Connected

     Sandbox jules@sf.com.jssandtwo 00D020012344XTiEAM

    Connected

    O Scratch my-scratch-org test-qjrr9q5d13o8@example.com 00DMN0012342Gez2AE

    Active 2023-08-21

   Legend: D=Default DevHub, O=Default Org Use --all to see expired and deleted scratch

    orgs

```

The output lists the orgs that you’ve authorized or created, including Dev Hub orgs, production orgs, scratch orgs, and sandboxes. The
table displays the usernames that you specified when you authorized the orgs, their aliases, their IDs, and whether the CLI can connect


## Project Setup Link a Namespace to a Dev Hub Org

to it. An emoji on the left points to the default org or Dev Hub; refer to the legend at the bottom for details. Scratch orgs also display
their expiration dates.

To view more information, such as the scratch org creation date and associated DevHub org, and instance URL for all orgs, use the
`--verbose` flag.

```
   sf org list --verbose

```

Use the `--clean` flag to remove non-active scratch orgs from the list. The command prompts you before it does anything.

```
   sf org list --clean

```

SEE ALSO:

Authorization

Build Your Own Scratch Org Definition File

Create Scratch Orgs

Generate or Change a Password for a Scratch Org User

Deploy Source From Your Project to the Scratch Org

## Link a Namespace to a Dev Hub Org

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

You can’t link orgs without a namespace: sandboxes, scratch orgs, patch orgs, and branch orgs require a namespace to be linked to
the Namespace Registry.


## Project Setup Salesforce DX Project Configuration

To view all the namespaces linked to the Namespace Registry, select the **All Namespace Registries** list view.

SEE ALSO:

[Get a Trial Development Environment for Free](https://developer.salesforce.com/free-trials)

_[Lightning Aura Components Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.lightning.meta/lightning/namespaces_creating.htm)_ : Create a Namespace in Your Org

Add Salesforce DX Users

[Salesforce Help: My Domain](https://help.salesforce.com/articleView?id=domain_name_overview.htm&type=5&language=en_US)

## Salesforce DX Project Configuration

The project configuration file `sfdx-project.json` indicates that the directory is a Salesforce DX project. The configuration file
contains project information and facilitates the authorization of orgs and the creation of second-generation packages. It also tells
Salesforce CLI where to put files when syncing between the project and org.

We provide sample `sfdx-project.json` files in the sample repos for creating a project using Salesforce CLI or Salesforce Extensions
for VS Code.

Note: Are you planning to create second-generation packages? When you’re ready, add packaging-specific configuration options
[to support package creation. See Project Configuration File for a Second-Generation Managed Package.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev2gp_config_file.htm)

We recommend that you check in this file with your source.

```
   {

   "packageDirectories" : [

      { "path": "force-app", "default": true},

      { "path" : "unpackaged" },

      { "path" : "utils" }

     ],

   "namespace": "",

   "sfdcLoginUrl" : "https://login.salesforce.com",

   "sourceApiVersion": "63.0"

   }

```

You can manually edit these parameters.

name (required for Salesforce Functions)

Salesforce DX or Salesforce Functions project name.

namespace (optional)

The global namespace that is used with a package. The namespace must be registered with an org that is associated with your Dev Hub
org. This namespace is assigned to scratch orgs created with the `org create scratch` command. If you’re creating an unlocked
package, you have the option to create a package with no namespace.

Important: Register the namespace with Salesforce and then connect the org with the registered namespace to the Dev Hub
org.


Project Setup Salesforce DX Project Configuration

oauthLocalPort (optional)

By default, the OAuth port is 1717. Change this port if 1717 is already in use and you plan to create a connected app in your Dev Hub
org to support JWT-based authorization. Be sure you also follow the steps in Create a Connected App in Your Org to change the callback
URL.

packageAliases (optional)

[Aliases for package IDs, which can often be cryptic. See Project Configuration File for a Second-Generation Managed Package for details.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev2gp_config_file.htm)

packageDirectories (required)

Package directories indicate which directories to target when syncing source to and from the org. These directories can contain source
files from your managed or unmanaged package. They can also contain unpackaged source files produced by, for example, an ant tool
or change set. For information on all `packageDirectories` [options, see Project Configuration File for a Second-Generation](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev2gp_config_file.htm)
[Managed Package.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev2gp_config_file.htm)

Keep these things in mind when working with package directories.

**•** The location of the package directory is relative to the project. Don’t specify an absolute path. The following two examples are
equivalent.

```
     "path": "helloWorld"

     "path" : "./helloWorld"

```

**•** You can have only one default path (package directory). If you have only one path, we assume it’s the default, so you don’t have to
explicitly set the `default` parameter. If you have multiple paths, you must indicate which one is the default.

**•** Salesforce CLI uses the default package directory as the target directory when retrieving changes from the org to the local project.
This default path is also used when creating second-generation packages.

**•** If you don’t specify an output directory, the default package directory is also where files are stored during source conversions. Source
conversions are both from metadata format to source format, and from source format to metadata format.

plugins (optional)

[To use the custom plugins you’ve created with your Salesforce DX project, add a](https://github.com/salesforcecli/cli/wiki/Quick-Introduction-to-Developing-sf-Plugins) `plugins` section to the `sfdx-project.json`
file. In this section, add configuration values and settings to change your plugins’ behavior.

```
   "plugins": {

     "yourPluginName": {

      "timeOutValue": "2"

     },

     "yourOtherPluginName": {

      "yourCustomProperty": true

     }

   }

```

Store configuration variables for only those values that you want to check in to source control for the project. These configuration values
affect your whole development team.


Project Setup Salesforce DX Project Configuration

pushPackageDirectoriesSequentially (optional) (Deprecated)

Note: This property is deprecated and applies only to the deprecated `force:source:push` command. It doesn't affect the
behavior of the `project deploy start` command. To deploy packages sequentially, and in a specific order, use
separate `project deploy start` commands in the desired order.

Set to `true` to push multiple package directories in the order they're listed in `packageDirectories` when using
`force:source:push` . The directories are pushed in separate transactions. The default value of this property is `false`, which
means that multiple package directories are deployed in a single transaction without regard to order. Example:

```
   "packageDirectories": [

      {

       "path": "es-base-custom",

       "default": true

      },

      {

       "path": "es-base-ext"

      }

     ],

     "pushPackageDirectoriesSequentially": true,

```

replacements (optional)

Automatically replace strings in your metadata source files with specific values right before you deploy the files to an org.

[See Replace Strings in Code Before Deploying for details.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_ws_string_replace.htm)

sfdcLoginUrl (optional)

The login URL that the `org login` commands use. If not specified, the default is `https://login.salesforce.com` . Override
the default value if you want users to authorize to a specific Salesforce instance. For example, if you want to authorize into a sandbox
org, set this parameter to `https://test.salesforce.com` .

If you don’t specify a default login URL here, or if you run `org login` outside the project, specify the instance URL when authorizing
the org with the `--instance-url` flag.

sourceApiVersion (optional)

The API version that the source is compatible with.

The `sourceApiVersion` value determines the fields retrieved for each metadata type during `project deploy`, `project`
`retrieve`, or `project convert` . This field is important if you’re using a metadata type that has changed in a recent release.
You’d want to specify the version of your metadata source. For example, let's say a new field was added to the CustomTab for API version
63.0. If you retrieve components for version 57.0 or earlier, you see errors when running the `project` commands because the
components don't include that field.

[Don’t confuse this project configuration parameter with the org-api-version CLI configuration variable, which has a similar name. See](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_setup.meta/sfdx_setup/sfdx_dev_cli_config_values.htm)
[How API Version and Source API Version Work in Salesforce CLI for more information and the default value.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_setup.meta/sfdx_setup/sfdx_setup_apiversion.htm)


## Project Setup Multiple Package Directories

sourceBehaviorOptions (optional) (Beta)

Specify which metadata types in your Salesforce DX project are decomposed. Custom objects and custom object translations are always
decomposed by default. Decomposition refers to splitting a single, often large, metadata XML file into smaller XML files based on its
subtypes.

Note: Decomposition of permission sets, custom labels, sharing rules, and workflows is a pilot or beta service that is subject to
[the Beta Services Terms at Agreements - Salesforce.com or a written Unified Pilot Agreement if executed by Customer, and](https://www.salesforce.com/company/legal/agreements/)
[applicable terms in the Product Terms Directory. Use of this pilot or beta service is at the Customer's sole discretion.](https://ptd.salesforce.com/?_ga=2.247987783.1372150065.1709219475-629000709.1639001992)

Don't manually update your `sfdx-project.json` file with this option. Rather, run the `project convert`
`source-behavior` Salesforce CLI command which updates the file for you, and also breaks up the associated metadata file XML
into smaller files. See Start Decomposing the Optional Metadata Types (Beta) on page 31 for details.

Possible values:

**•** `decomposeCustomLabelsBeta2` [—Decompose the CustomLabels metadata type.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_customlabels.htm)

**•** `decomposeExternalServiceRegistrationBeta` [—Decompose the ExternalServiceRegistration metadata type.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_externalserviceregistration.htm)

**•** `decomposePermissionSetBeta2` [—Decompose the PermissionSet metadata type.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_permissionset.htm)

**•** `decomposeSharingRulesBeta` [—Decompose the SharingRules metadata type](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_sharingrules.htm)

**•** `decomposeWorkflowBeta` [—Decompose the WorkFlow metadata type.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_workflow.htm)

Example:

```
   "sourceBehaviorOptions": ["decomposePermissionSetBeta2", "decomposeCustomLabelsBeta2"]

```

SEE ALSO:

Link a Namespace to a Dev Hub Org

Authorization

How to Exclude Source When Syncing

Retrieve Source from the Scratch Org to Your Project

Deploy Source From Your Project to the Scratch Org

## Multiple Package Directories

When you create your Salesforce DX project, we recommend that you organize your metadata into logical groupings by creating multiple
package directories locally. You then define these directories in your `sfdx-project.json` file. You can group similar code and
source files for an application or customization to better organize your team’s repository. Later, if you decide to use unlocked or
second-generation managed packages (2GP), these directories correspond to the actual unlocked or 2GP packages.

Note: For clarity, a package directory refers to the local (client-side) directory that contains decomposed metadata files, that is,
metadata in source format. This directory doesn’t always result in an unlocked or 2GP package. Package refers to an unlocked or
2GP package.

In your `sfdx-project.json` file, list each package directory separately in the `packageDirectories` section. Each local
package directory adheres to the standard Salesforce DX project structure.

The multiple package directory structure is client-side (local) only. When you deploy the source to the org with `project deploy`
`start`, there’s no association between its local package directory location and the package in the org. You specify that metadata
belongs to a specific unlocked or 2GP package in an org by explicitly installing the package.


Project Setup Multiple Package Directories

All of the `project` commands that deploy, retrieve, and convert metadata support multiple package directories.

How Do I Set It Up?

Setting up multiple package directories is easy. How you organize your local source code among these directories takes more thought
and planning, and depends on your development environment. Plan how to organize your code before you get started. Keep your
source code well organized as your project grows to make it easier and more efficient for your developers to work.

Let’s say you put the decomposed metadata files for a custom object MyObject in the default package directory. You can then put files
for a new field MyField on MyObject in a different “extension” package directory without having to also include the MyObject files.
[Although this example is simple, you can organize your code in any number of different ways. These blog posts provide some ideas.](https://developer.salesforce.com/blogs/2018/06/working-with-modular-development-and-unlocked-packages-part-1.html)

Here’s how you set up multiple package directories. Let’s first look at a sample `sfdx-project.json` snippet:

```
   "packageDirectories": [

      {

       "path": "es-base-custom",

       "default": true

      },

      {

       "path": "es-base-ext"

      },

      {

       "path": "es-base-styles"

      }

     ],

```

The sample `sfdx-project.json` snippet defines three package directories: `es-base-custom` (the default), `es-base-ext`,
and `es-base-styles` . Let’s say your top-level local project directory is called `easy-spaces-lwc` . The directory hierarchy
underneath it looks something like this:

Each `es-base-*` directory adheres to the standard Salesforce DX project structure. For example, the `es-base-ext` directory
looks something like this:


Project Setup Multiple Package Directories

Now add the decomposed metadata source to these multiple package directories in the way that best suits your development environment.

How Does It Work?

Let's go through a few examples to see how `project deploy start` and `project retrieve start` work with multiple
package directories.

For new orgs, the `default project deploy start` command deploys all the metadata in all multiple package directories
listed in your `sfdx-project.json` file. After that, the command deploys only metadata that's new, changed, or marked for delete.
By default, the command deploys the metadata in a single transaction, as if you had just one package directory.

```
   sf project deploy start --target-org my-org

```

You can also target the metadata you want to deploy. You can deploy specific package directories, specific metadata components,
components listed in a manifest file, and more. This example deploys the metadata in the `es-base-custom` package directory:

```
   sf project deploy start --source-dir es-base-custom --target-org my-org

```

To deploy more than one package directory, specify the `--source-dir` flag multiple times. This example deploys all the package
directories configured in the sample `sfdx-project.json` file shown in the previous section.

```
   sf project deploy start --source-dir es-base-custom --source-dir es-base-ext --source-dir

    es-base-styles --target-org my-org

```

This example deploys all Apex classes found in all your multiple package directories:

```
   sf project deploy start --metadata ApexClass --target-org my-org

```

When you run `project retrieve start`, the command retrieves all remote changes from the org into your local project. For
each retrieved component, the command looks in all package directories for a local match. If it finds a match, the command updates it.
If it doesn't find a match, the command copies the local component into the default package directory, which in our example is
`es-base-custom` .

```
   sf project retrieve start --target-org my-org

```

You can then move the retrieved files into the package directory that makes sense for your project. After you deploy the moved files
back to the org with `project deploy start`, Salesforce CLI tracks their new location.

You can also use `project retrieve start` to retrieve targeted metadata from your org. Existing metadata is retrieved into its
correct local package directory and new metadata into the default package directory. This example retrieves only the metadata components
contained in the local `es-base-custom` package directory:

```
   sf project retrieve start --source-dir es-base-custom --target-org my-org

```

This example retrieves all Apex classes from your org; new classes go into the default package directory and classes that exist locally go
into their corresponding package directory.

```
   sf project retrieve start --metadata ApexClass --target-org my-org

```

Push Source Sequentially

By default, `project deploy start` deploys metadata to your org in a single transaction, regardless of the order that you list
your multiple package directories in `sfdx-project.json` . But sometimes you must specify the exact order that the package
directories are pushed. Reasons include:


## Project Setup Replace Strings in Code Before Deploying or Packaging

**•** The number of recomposed metadata component files in your local project exceeds the Salesforce metadata limit of 10,000 files
per retrieve or deploy. One workaround is to split up your metadata into multiple package directories that each contain less than
this limit and push each directory sequentially, and thus separately.

**•** You have dependencies between multiple package directories, which requires that they be pushed in a specific order.

**•** More than one package directory contains the same metadata component, and you want to specify which one is deployed last so
it's not overwritten.

If you need multiple deployments in a specific order, run `project deploy start` several times with the `--source-dir` or
`--metadata` flags in the desired order.

SEE ALSO:

_Developer Guide_ [: Second-Generation Managed Packages](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp.htm)

_Developer Guide_ [: Install and Uninstall Second-Generation Managed Packages](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_install_upgrade.htm)

Salesforce DX Project Structure and Source Format

_Salesforce Developers Blog_ [: Working with Modular Development and Unlocked Packages](https://developer.salesforce.com/blogs/2018/06/working-with-modular-development-and-unlocked-packages-part-1.html)

## Replace Strings in Code Before Deploying or Packaging

Automatically replace strings in your metadata source files with specific values right before you deploy the files to an org or create a
package version.

These sample use cases describe scenarios for using string replacement:

**•** A NamedCredential contains an endpoint that you use for testing. But when you deploy the source to your production org, you
want to specify a different endpoint.

**•** An ExternalDataSource contains a password that you don’t want to store in your repository, but you’re required to deploy the
password along with your metadata.

**•** You deploy near-identical code to multiple orgs. You want to conditionally swap out some values depending on which org you’re
deploying to.

For the `project deploy start` command, string replacement occurs when source-formatted files are converted to metadata
API format, and then a ZIP file is created and deployed to the org. It also occurs when you run the `package version create`
command, which converts source files as part of the package creation process. The changes that result from string replacement are
never written to your project source; they apply only to the deployed or packaged files.

Note: For simplicity, the rest of this topic assumes that you’re using string replacement before deploying to your org, but the
same ideas also apply to creating a package version.

Configure String Replacement

Configure string replacement by adding a `replacements` property to your `sfdx-project.json` file. The property accepts
multiple entries that consist of keys that define the:

**•** Source file or files that contain the string to be replaced.

**•** The string to be replaced.

**•** The replacement value.

To see how string replacements work, let’s look at an example; see more examples later in this topic.


Project Setup Replace Strings in Code Before Deploying or Packaging

This sample `sfdx-project.json` specifies that when the file `force-app/main/default/classes/myClass.cls`
is deployed, all occurrences of the string `replaceMe` are replaced with the value of the THE_REPLACEMENT environment variable:

```
   {

     "packageDirectories": [

      {

        "path": "force-app",

        "default": true

      }

     ],

     "name": "myproj",

     "replacements": [

      {

       "filename": "force-app/main/default/classes/myClass.cls",

       "stringToReplace": "replaceMe",

       "replaceWithEnv": "THE_REPLACEMENT"

      }

     ]

   }

```

You can specify these keys in the `replacements` property.

**Location of Files**
One of the following properties is required:

**•** `filename` : Single file that contains the string to be replaced.

**•** `glob` : Collection of files that contain the string to be replaced. Example: `**/classes/*.cls` .

**String to be Replaced**
One of the following properties is required:

**•** `stringToReplace` : The string to be replaced.

**•** `regexToReplace` : A regular expression (regex) that specifies a string pattern to be replaced.

**Replacement Value**
One of the following properties is required:

**•** `replaceWithEnv` : Specifies that the string is replaced with the value of the specified environment variable.

**•** `replaceWithFile` : Specifies that the string is replaced with the contents of the specified file.

**Conditional Processing**
These properties are optional:

**•** `replaceWhenEnv` : Specifies that a string replacement occur only when a specific environment variable is set to a specific
value. Use the property `env` to specify the environment variable and the property `value` to specify the value that triggers
the string replacement.

**•** `allowUnsetEnvVariable` : Boolean property used with the `replaceWithEnv` property. When set to `true`, specifies
that if the `replaceWithEnv` environment variable isn’t set, then remove the replacement string from the file before deploying.
In other words, replace it with nothing. When set to `false` (the default value), you get an error when the `replaceWithEnv`
environment variable isn’t set.

Follow these syntax rules:

**•** Always use forward slashes for directories ( `/` ), even on Windows.


Project Setup Replace Strings in Code Before Deploying or Packaging

**•** Both JSON and regular expressions use the backslash ( `\` ) as an escape character. As a result, when you use a regular expression to
match a dot, which requires escaping, you must use _two_ backslashes for the `regexToReplace` value:

```
     "regexToReplace" : "\\."

```

Similarly, to match a single backslash, you must specify three of them.

```
     "regexToReplace" : "\\\"

```

Examples

This example is similar to the previous example but shows how to configure string replacement for two files:

```
   "replacements": [

     {

      "filename": "force-app/main/default/classes/FirstApexClass.cls",

      "stringToReplace": "replaceMe",

      "replaceWithEnv": "THE_REPLACEMENT"

     },

     {

      "filename": "force-app/main/default/classes/SecondApexClass.cls",

      "stringToReplace": "replaceMe",

      "replaceWithEnv": "THE_REPLACEMENT"

     }

   ]

```

This example shows how to specify that the string replacement occur only if an environment variable called DEPLOY_DESTINATION
exists and it has a value of `PROD` .

```
   "replacements": [

     {

      "filename": "force-app/main/default/classes/myClass.cls",

      "stringToReplace": "replaceMe",

      "replaceWithEnv": "THE_REPLACEMENT",

      "replaceWhenEnv": [{

       "env": "DEPLOY_DESTINATION",

       "value": "PROD"

      }]

     }

   ]

```

In this example, if the environment variable SOME_ENV_THAT_CAN_BE_BLANK isn’t set, the string `myNS__` in the `myClass.cls`
file is removed when the file is deployed. If the environment variable is set to a value, then that value replaces the `myNS__` string.

```
   "replacements": [

      {

       "filename": "/force-app/main/default/classes/myClass.cls",

       "stringToReplace": "myNS__",

       "replaceWithEnv": "SOME_ENV_THAT_CAN_BE_BLANK",

       "allowUnsetEnvVariable": true

      }

     ]

```


Project Setup Replace Strings in Code Before Deploying or Packaging

This example specifies that when the Apex class files in the `force-app/main/default` directory are deployed, all occurrences
of the string `replaceMe` are replaced with the contents of the file `replacementFiles/copyright.txt` .

```
   "replacements": [

     {

      "glob": "force-app/main/default/classes/*.cls",

      "stringToReplace": "replaceMe",

      "replaceWithFile": "replacementFiles/copyright.txt"

     }

   ]

```

Use a regular expression to specify a search pattern for text rather than the literal text. For example, Apex class XML files always contain
an `<apiVersion>` element that specifies the Salesforce API version, as shown in this snippet.

```
   <?xml version="1.0" encoding="UTF-8" ?>

   <ApexClass xmlns="http://soap.sforce.com/2006/04/metadata">

      <apiVersion>55.0</apiVersion>

      <status>Active</status>

   </ApexClass>

```

Let’s say you want to test your Apex classes on a more recent API version before you actually update all your classes. This example shows
how to use a regular expression to search for the `<apiVersion>` element. At deploy, the element is replaced with a specific string,
such as `<apiVersion>58.0</apiVersion>`, which is contained in the
`replacementFiles/latest-api-version.txt` file.

```
   "replacements": [

     {

      "glob": "force-app/main/default/classes/*.xml",

      "regexToReplace": "<apiVersion>\\d+\\.0</apiVersion>",

      "replaceWithFile": "replacementFiles/latest-api-version.txt"

     }

   ]

```

Tips and Tricks

**•** (macOS or Linux only) When using the `replaceWithEnv` or `replaceWhenEnv` properties, you can specify that the environment
variables apply to a single command by prepending the variables before the command execution. For example:

```
     THE_REPLACEMENT="some text" DEPLOY_DESTINATION=PROD sf project deploy start

```

Warning: Be careful when setting passwords or secrets this way, because they show up in your terminal history.

**•** If you’ve configured many string replacements, and are finding it difficult to manage, check out open-source tools that load the
[contents of one or more files to your environment, such as dotenv-cli. In this example, environment variables configured in two local](https://github.com/entropitor/dotenv-cli)
`.env` files are loaded before the `project deploy start` command execution:

```
     dotenv -e .env1 -e .env2 sf project deploy start

```

Warning: Don’t commit passwords or secrets in `.env` files.

**•** If you specify `--json` for `project deploy start`, the JSON output includes a `replacements` property that lists the
affected files and the string that was replaced. If you specify `--json` and `--concise`, the JSON output doesn’t include the
`replacements` property.


### Project Setup Test String Replacements

To view string replacement information in the `project deploy start` human-readable output, specify `--verbose` .

**•** Many of the string replacement use cases and examples in this topic use environment variables. How to set an environment variable
to the required value depends on your operating system, and is beyond the scope of this document. But for some hints, see the
[introduction of the Salesforce CLI Environment Variables topic in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_setup.meta/sfdx_setup/sfdx_dev_cli_env_variables.htm) _Salesforce CLI Setup Guide_ .

Considerations and Limitations

**•** If you configure multiple string replacements in multiple files, the performance of the deployment can degrade. Consider using the
`filename` key when possible, to ensure that you open only one file. If you must use `glob`, try to limit the number of files that
are opened by specifying a single directory or metadata type.

For example, `"glob": "force-app/main/default/classes/*.cls"` targets Apex class files in a specific directory,
which is better than `"glob": "**/classes/**”`, which searches for all Apex metadata files in all package directories.

**•** Be careful using string replacement in static resources. When not doing string replacement, Salesforce CLI simply zips up all static
resources when it first encounters their directory and deploys them as-is. If you configure string replacement for a large static resource
directory, the CLI must inspect a lot more files than usual, which can degrade performance.

**•** You can’t use string replacements when deploying in metadata format, such as with the command `project deploy start`
`--metadata-dir` .

**•** If your deployment times out, or you specify the `--async` flag of `project deploy start`, and then run `project`
`deploy resume` or `project deploy report` to see what happened, the deployed files contain string replacements
as usual. However, the output of `project deploy resume` and `project deploy report` don’t display the same
string replacement information as `project deploy start --verbose` would have.

### Test String Replacements

To test string replacement without actually deploying files to the org or creating a package version, follow these steps.

### Test String Replacements

To test string replacement without actually deploying files to the org or creating a package version, follow these steps.

**1.** Set the `SF_APPLY_REPLACEMENTS_ON_CONVERT` environment variable to `true` .

**2.** Run the `project convert source` command, which converts the source files into metadata API format. For example:

```
     sf project convert source --output-dir mdapiOut --source-dir force-app

```

**3.** Inspect the files in the output directory ( `mdapiOut` in our example) for the string replacements and what exactly will be deployed
to the org or packaged.

Warning: Be careful when writing passwords or secrets to the file system while testing. Also, be sure to reset any environment
variables you set during testing so they aren’t accidentally applied later.


# CHAPTER 4 Authorization

In this chapter ...

**•** Authorize an Org
Using a Browser

**•** Authorize an Org
Using the JWT Flow

**•** Create a Private Key
and Self-Signed
Digital Certificate

**•** Create an External
Client App in Your
Org

**•** Create a Connected
App in Your Org

# Authorization refers to logging into an org so you can run

commands that require access to the org. Creating an org with a
CLI command also automatically authorizes it. For example, you
authorize a Dev Hub org to allow you to create, delete, and manage
your Salesforce scratch orgs. After you set up your project on your
local machine, you authorize the Dev Hub org before you can create
a scratch org. When you run the command to create the scratch
org, Salesforce CLI automatically authorizes it.

You can also authorize other existing orgs, such as sandboxes or
packaging orgs, to provide more flexibility when using CLI
commands.

You authorize an org only one time. To switch between orgs during
development, specify the username that you used to log into the
org with either the `--target-org` or `--target-dev-hub`
flag. You can also set a default org or use an alias.

EDITIONS

Available in: Salesforce
Classic and Lightning
Experience

Dev Hub available in:
**Developer**, **Enterprise**,
**Performance**, and
**Unlimited** Editions

Scratch orgs are available
in: **Developer**, **Enterprise**,
**Group**, and **Professional**
Editions

**•** Use the Default

flag. You can also set a default org or use an alias.

Connected App
Securely You have some options when authorizing an org, depending on what you’re trying to accomplish.

**•** Use an Existing **•** The easiest option is to run `org login web`, which opens a browser in which you enter your
Access Token Salesforce credentials. This option is officially called the _OAuth 2.0 web server flow_ .

**•** Authorize an Org
Using Its SFDX
# Authorization URL • Authorization

Information for an
Org

**•** View Org
Authentication
Secrets

**•** Log Out of an Org

**•** For continuous integration (CI) or automated environments, use the `org login jwt` command.
This option is officially called the _OAuth 2.0 JSON Web Tokens (JWT) bearer flow_ . This flow is ideal for
scenarios where you can’t interactively log in to a browser, such as from a CI script.

You can also use the `org login sfdx-url` command in automated environments; this
method uses the org’s SFDX authorization URL.

Important: If your org is configured with high assurance (stepped up) authentication,
Salesforce prompts the user to verify their identity. This verification process means that you
can’t use the JWT flow or SFDX authorization URL with Salesforce CLI for headless authentication.

SEE ALSO:

Authorize an Org Using a Browser

Authorize an Org Using the JWT Flow

_Salesforce Help_ [: OAuth 2.0 Web Server Flow for Web App Integration](https://help.salesforce.com/articleView?id=remoteaccess_oauth_web_server_flow.htm&language=en_US)

_Salesforce Help_ [: OAuth 2.0 JWT Bearer Flow for Server-to-Server Integration](https://help.salesforce.com/articleView?id=remoteaccess_oauth_jwt_flow.htm&language=en_US)


## Authorization Authorize an Org Using a Browser Authorize an Org Using a Browser

Authorize an org with a browser by running a CLI command and entering your credentials in the browser that automatically opens.
That’s it!

Use this authorization method when multi-factor authentication (MFA) is enabled on your org, either directly with a username and
password or via single sign-on (SSO).

Important: You must have the **Approve Uninstalled Connected Apps** user permission to complete this task. Org administrators
have the permission by default.

**1.** Open a terminal (macOS and Linux) or command prompt (Windows).

**2.** Run the `org login web` CLI command. We recommend using the `--alias` flag to make it easy to refer to the org later.

```
     sf org login web --alias my-org

```

Use the `--set-default` flag if you want the org to be the default for commands that accept the `--target-org` flag. If
you’re authorizing a Dev Hub org, use the `--set-default-dev-hub` flag instead. See the `[org login web](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_org_commands_unified.htm#cli_reference_org_login_web_unified)` command
for examples.

**3.** In the browser window that opens, sign in to your org with your Salesforce login credentials. Click **Allow**, which allows Salesforce
CLI to access to your org.

**4.** Close the browser window. Your org is now authorized!

If the URL that you use to log in to your org isn’t the default ( `login.salesforce.com` ), update your project configuration file
( `sfdx-project.json` ). Set the `sfdcLoginUrl` option to your My Domain login URL. For example:

```
   "sfdcLoginUrl" : "https:// MyDomainName .my.salesforce.com"

```

This example is for a sandbox.

```
   "sfdcLoginUrl" : "https:// MyDomainName -- SandboxName .sandbox.my.salesforce.com"

```

Alternatively, you can use the `--instance-url` flag of `org login web` to specify the URL. This value overrides the login URL
you specified in the `sfdx-project.json` file. For example:

```
   sf org login web --alias my-hub-org --instance-url https://exciting.sandbox.my.salesforce.com

```

Note: We recommend that you use your enhanced My Domain login URL, as it isn’t affected by org migrations that change your
org’s Salesforce instance. Be sure you use the version that ends in `my.salesforce.com` instead of the URL you see in Lightning
Experience ( `.lightning.force.com` ). To verify the valid My Domain URL, from Setup, enter _`My Domain`_ in the Quick
Find box, then select **My Domain** .

The orgs you authorize for Salesforce CLI are required to have either an external client app (preferred) or a connected app. We provide
a default connected app called `Salesforce CLI` . If you need more security or control, such as setting the refresh token timeout


## Authorization Authorize an Org Using the JWT Flow

or specifying IP ranges, create your own external client app or connected app (only if you need to create scratch orgs or sandboxes).
You can also configure the default connected app to be more secure.

SEE ALSO:

_[Salesforce CLI Command Reference](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_org_commands_unified.htm#cli_reference_org_login_web_unified)_ : org login web

Create an External Client App in Your Org

Create a Connected App in Your Org

Use the Default Connected App Securely

Salesforce DX Project Configuration

_Salesforce Help_ [: Enhanced Domains](https://help.salesforce.com/s/articleView?id=products.domain_name_enhanced.htm&type=5&language=en_US)

_VS Code Command_ [: SFDX: Authorize an Org, SFDX: Authorize a Dev Hub](https://developer.salesforce.com/docs/platform/sfvscode-extensions/guide/default-org.html)

## Authorize an Org Using the JWT Flow

Use the JWT flow to authorize an org in continuous integration (CI) environments, which are fully automated and don’t support the
human interactivity of logging into a browser.

The JWT flow requires a digital certificate, also called a digital signature, to sign the JWT request. You can use your own certificate or
create a self-signed certificate using OpenSSL.

Important: If your org is configured with high assurance (stepped up) authentication, Salesforce prompts the user to verify their
identity. This verification process means that you can’t use the JWT flow and Salesforce CLI for headless authentication.

**1.** If you don’t have your own private key and digital certificate, you can use OpenSSL to create the key and a self-signed certificate.

It’s assumed in this task that your private key file is named `server.key` and your digital certificate is named `server.crt` .

**2.** Create an external client app and configure it for Salesforce DX.

This task includes uploading the `server.crt` digital certificate file. Make note of the consumer key when you finish configuring
the external client app because you need it later.

Important: If you're authorizing a Dev Hub org and plan to create scratch orgs or sandboxes with the `org create`
`scratch|sandbox` commands, then you must create a connected app instead of an external client app.

**3.** Open a terminal (macOS and Linux) or command prompt (Windows).

**4.** Run the `org login jwt` CLI command. We recommend using the `--alias` flag to make it easy to refer to the org later.
Specify the consumer key from your external client app or connected app with the `--client-id` flag, the path to the private
JWT key file ( `server.key` ), and the username for your org. For example:

```
     sf org login jwt --client-id 04580y4051234051 --jwt-key-file /Users/jdoe/JWT/server.key

      --username jdoe@myorg.com --alias my-hub-org

```

Use the `--set-default` flag if you want the org to be the default for commands that accept the `--target-org` flag. If
you’re authorizing a Dev Hub org, use the `--set-default-dev-hub` flag instead. See the `[org login jwt](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_org_commands_unified.htm#cli_reference_org_login_jwt_unified)` command
for examples.

You can authorize a scratch org using the same consumer key and private key file that you used to authorize its associated Dev Hub org.
See Authorize a Scratch Org Using the JWT Flow


### Authorization Authorize a Scratch Org Using the JWT Flow

If the URL that you use to log in to your org isn’t the default ( `login.salesforce.com` ), update your project configuration file
( `sfdx-project.json` ). Set the `sfdcLoginUrl` option to your enhanced My Domain login URL. For example:

```
   "sfdcLoginUrl" : "https:// MyDomainName .my.salesforce.com"

```

This example is for a sandbox.

```
   "sfdcLoginUrl" : "https:// MyDomainName -- SandboxName .sandbox.my.salesforce.com"

```

Alternatively, you can use the `--instance-url` flag of the `org login jwt` command to specify the URL. This value overrides
the login URL you specified in the `sfdx-project.json` file. For example:

```
   sf org login jwt --client-id 04580y4051234051 --jwt-key-file /Users/jdoe/JWT/server.key

   --username jdoe@myorg.com --alias my-hub-org --instance-url

   https://mydomain--mysandbox.sandbox.my.salesforce.com

```

Note: We recommend that you use your My Domain login URL, because it isn’t affected by org migrations that change your org’s
Salesforce instance. Be sure you use the version that ends in `my.salesforce.com` instead of the URL you see in Lightning
Experience ( `.lightning.force.com` ). To verify the valid My Domain URL, from Setup, enter _`My Domain`_ in the Quick
Find box, then select **My Domain** .

SEE ALSO:

_[Salesforce CLI Command Reference](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_org_commands_unified.htm#cli_reference_org_login_jwt_unified)_ : org login jwt

Create a Private Key and Self-Signed Digital Certificate

Create a Connected App in Your Org

Salesforce DX Project Configuration

_Salesforce Help_ [: Enhanced Domains](https://help.salesforce.com/s/articleView?id=products.domain_name_enhanced.htm&type=5&language=en_US)

_Salesforce Help_ [: Set Up Multi-Factor Authentication](https://help.salesforce.com/articleView?id=security_2fa_config.htm&language=en_US)

### Authorize a Scratch Org Using the JWT Flow

If you authorized your Dev Hub org using the `org login jwt` command, you can use the same digital certificate and private key
to authorize an associated scratch org. This method is useful for continuous integration (CI) systems that must authorize scratch orgs
after creating them, but don’t have access to the scratch org’s access token.

Before you begin, we assume that:

**•** You previously authorized your Dev Hub org with the `org login jwt` command.

**•** The private key file you used when authorizing your Dev Hub org is accessible and in `/Users/jdoe/JWT/server.key` .

**•** You’ve created a scratch org and have its administration user’s username, such as test-wvkpnfm5z113@example.com.

**•** You know the scratch org’s instance URL. If you don’t know it, you can query your Dev Hub org. For example:

```
     sf data query --target-org my-dev-hub --query "SELECT SignupUsername,LoginUrl FROM

     ScratchOrgInfo WHERE SignupUsername='test-wvkpnfm5z113@example.com'"

```

**1.** Copy the consumer key from the external client app (or connected app) that you created in your Dev Hub org.

**a.** Log in to your Dev Hub org.

**b.** From Setup, enter _`App Manager`_ in the Quick Find box to get to the Lightning Experience App Manager.

**c.** Locate the external client app (or connected app) in the apps list, then click the dropdown menu on the right side, and select
**View** .


## Authorization Create a Private Key and Self-Signed Digital Certificate

**d.** In the API (Enable OAuth Settings) section, click **Manage Consumer Details**

If prompted, verify your identity by entering the verification code that was automatically sent to your email address.

**e.** Copy the Consumer Key to your clipboard. The consumer key is a long string of numbers, letters, and characters, such as
3MVG9szVa2Rx_sqBb444p50Yj (example shortened for clarity.)

**2.** Open a terminal (macOS and Linux) or command prompt (Windows).

**3.** Run the `org login jwt` CLI command. The `--client-id` and `--jwt-key-file` flag values are the same as when
you ran the command to authorize a Dev Hub org. Set `--username` to the scratch org’s admin username and set
`--instance-url` to the scratch org’s instance URL, such as
`https://energy-enterprise-2539-dev-ed.scratch.my.salesforce.com` . For example:

```
     sf org login jwt --client-id 3MVG9szVa2Rx_sqBb444p50Yj \

     --jwt-key-file /Users/jdoe/JWT/server.key --username test-wvkpnfm5z113@example.com \

     --instance-url https://energy-enterprise-2539-dev-ed.scratch.my.salesforce.com

```

If you get an error that the user isn’t approved, it means that the scratch org information hasn’t yet been replicated. Wait a short
time and try again.

Note: If your scratch org is running on Hyperforce and the `--username` value of `org login jwt` is a non-admin scratch
org user, you can’t use your Dev Hub’s digital certificate and private key. To authorize the scratch org in this scenario, follow the
standard JWT flow steps.

SEE ALSO:

Authorize an Org Using the JWT Flow

_Salesforce Help_ [: Connected Apps](https://help.salesforce.com/articleView?id=connected_app_overview.htm&language=en_US)

Create Scratch Orgs

## Create a Private Key and Self-Signed Digital Certificate

Authorizing an org with the `org login jwt` command requires a digital certificate and the private key used to sign the certificate.
We highly recommend that you use your own private key and certificate issued by a certification authority. You can also use OpenSSL
to create a key and a self-signed digital certificate, just to get started. Using a private key and certificate is optional when you authorize
an org by logging into a browser.

Warning: The steps in this topic are for sample purposes only. You can use the generated key and certificate to get started, but
check with your company's security policies before you use either of them in a production environment.

This process produces two files:

**•** `server.key` —The private key. You specify this file when you authorize an org with the `org login jwt` command.

**•** `server.crt` —The digital certificate. You upload this file when you create the required external client app or connected app.

**1.** Open a terminal (macOS and Linux) or command prompt (Windows).

**2.** If necessary, install OpenSSL on your computer.

To check whether OpenSSL is installed on your computer, run the `which` command on macOS or Linux or the `where` command
on Windows.

```
     which openssl

```


## Authorization Create an External Client App in Your Org

**3.** Create a directory for storing the generated files, and change to the directory.

```
     mkdir /Users/jdoe/JWT

     cd /Users/jdoe/JWT

```

**4.** Generate a private key, and store it in a file called `server.key` .

```
     openssl genpkey -aes-256-cbc -algorithm RSA -pass pass:SomePassword -out server.pass.key

      -pkeyopt rsa_keygen_bits:2048

     openssl rsa -passin pass:SomePassword -in server.pass.key -out server.key

```

**5.** Generate a certificate signing request by using the `server.key` file. Store the certificate signing request in a file called
`server.csr` . Enter information about your company when prompted.

```
     openssl req -new -key server.key -out server.csr

```

**6.** Generate a self-signed digital certificate from the `server.key` and `server.csr` files. Store the certificate in a file called
`server.crt` .

```
     openssl x509 -req -sha256 -days 365 -in server.csr -signkey server.key -out server.crt

```

Now create a external client app and upload the digital certificate to it. If you're authorizing a Dev Hub and you plan to create scratch
orgs or sandboxes later with the `org create scratch|sandbox` commands, then you must create a connected app instead.

SEE ALSO:

[OpenSSL: Cryptography and SSL/TLS Tools](https://www.openssl.org/)

Create a Connected App in Your Org

Authorize an Org Using the JWT Flow

## Create an External Client App in Your Org

Salesforce CLI requires an external client app in the org that you're authorizing. An external client app is a packageable framework that
enables a third-party application (Salesforce CLI) to integrate with Salesforce by using APIs and security protocols. We provide a default
connected app when you authorize an org with the `org login web` command. For extra security, you can create your own external
client app in your org by using Setup and configure it with the settings of your choice. You're required to create an external client app
when authorizing the org with the `org login jwt` command.

Important: If you're authorizing a Dev Hub org and plan to create scratch orgs or sandboxes with the `org create`
`scratch|sandbox` commands, then you create a connected app instead.

In the next task, the steps marked _(Required for JWT)_ are required only if you’re creating an external client app to use with the `org`
`login jwt` command. In this case, you also need a file that contains a digital certificate, such as `server.crt` . You can use your
own private key and certificate issued by a certification authority. Or you can use OpenSSL to create a key and a self-signed digital
certificate. See Create a Private Key and Self-Signed Digital Certificate.

The steps marked _(Required for JWT)_ are optional if you’re creating an external client app to use with `org login web` .

**1.** Log in to your org.

**2.** From the Quick Find box in Setup, enter _`App Manager`_, then click **App Manager** .


Authorization Create an External Client App in Your Org

**3.** Click **New External Client App** .

**4.** [Update the basic information as needed, such as the external client app name and your contact email address.](https://help.salesforce.com/s/articleView?id=xcloud.create_a_local_external_client_app.htm&language=en_US)

**5.** Under **API (Enable OAuth Settings)**, click **Enable OAuth** .

**6.** Under **App Settings**, in the **Callback URL** box, enter _`http://localhost:1717/OauthRedirect`_ .

If port 1717 (the default) is already in use on your local machine, specify an available one instead. Then update your
`sfdx-project.json` file by setting the `oauthLocalPort` property to the new port. For example, if you set the callback
URL to _`http://localhost:1919/OauthRedirect`_ :

```
     "oauthLocalPort" : "1919"

```

**7.** In the **OAuth Scopes** section, select these scopes:

**•** **Manage user data via APIs (api)**

**•** **Manage user data via Web browsers (web)**

**•** **Perform requests at any time (refresh_token, offline_access)**

**8.** _(Required for JWT)_ In the **Flow Enablement** section, select **Enable JWT Bearer Flow** .

**9.** _(Required for JWT)_ Click **Upload Files** and upload the file that contains your digital certificate, such as `server.crt` .

**10.** Click **Create** .

The basic external client app is created and enabled, and you see the page to manage your new external client app. However, you
must further configure the external client app to use it with Salesforce CLI.

**11.** Click **Edit** .

**12.** _(Required for JWT, including substeps)_ Click the **Policies** tab.

**a.** Open **OAuth Policies** .

**b.** In the **Plugin Policies** section, set **Permitted Users** to _`Admin approved users are pre-authorized`_ .

**c.** Click **OK** .

**d.** In the **App Policies** section, select the profiles that are pre-authorized to use this external client app. Similarly, select the permission
sets. Create the profiles or permission sets if necessary.

**13.** If not currently there, click the **Policies** tab.

**14.** In the **App Authorization** section, under **OAuth Policies**, click **Expire refresh token after a specific time** .

**15.** In the **Refresh Token Validity Period** box, enter _`90`_ . For **Refresh Token Validity Unit**, select _`Day(s)`_ .

Setting a maximum of 90 days for the refresh token expiration is a security best practice. To continue running CLI commands against
an org whose refresh tokens have expired, reauthorize it with the `org login web` or `org login jwt` command.

**16.** In the **Session Timeout in Minutes** box, enter _`15`_ .

Setting a timeout for access tokens is a security best practice. Salesforce CLI automatically handles an expired access token by referring
to the refresh token.

**17.** Click **Save** .

Your external client app is ready to use.


### Authorization Get and Use the Consumer Key and Secret Get and Use the Consumer Key and Secret

When you're ready to run one of the `org login` commands that uses this external client app, follow these steps to get the consumer
key and secret:

**1.** Log in to your org.

**2.** From the Quick Find box in Setup, enter _`App Manager`_, and then click **External Client App Manager** .

**3.** Click your external client app.

**4.** Click the **Settings** tab.

**5.** Open **OAuth Settings** and click **Consumer Key and Secret** .

The **Verify Your Identiy** web page opens.

**6.** Check your email for a verification code, and then copy and paste the code in the **Verify Your Identity** web page.

**7.** Click **Verify** .

**8.** Click **Copy** next to **Consumer Key** .

Depending on whether you've specified that it's required, also copy the **Consumer Secret** .

To use the consumer key, use the `--client-id` flag of the `org login` commands. For example, if your consumer key is
04580y4051234051 and you’re authorizing a Dev Hub org by logging into it from a browser, run this command in a terminal (macOS
and Linux) or command prompt (Windows):

```
   sf org login web --client-id 04580y4051234051 --set-default-dev-hub --alias my-hub-org

```

If you specified in the external client app that the Web Server Flow requires a client (consumer) secret, the command prompts you for
it. The command then opens the login page for you to add your org credentials.

See the reference for `[org login web](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_org_commands_unified.htm#cli_reference_org_login_web_unified)` and `[org login jwt](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_org_commands_unified.htm#cli_reference_org_login_jwt_unified)` for more examples.

## Create a Connected App in Your Org

Salesforce CLI requires either an external client app (preferred) or connected app in the org that you're authorizing.

Warning: Create a connected app in your org **only** if it's your Dev Hub and you plan to later create scratch orgs or sandboxes
with the `org create scratch|sandbox` commands. Otherwise, create an external client app, which is the preferred
integration framework.

Connected apps are being deprecated. We plan to provide the information in this topic only until the requirement to use connected
apps for sandbox or scratch org creation is removed.

A connected app is a framework that enables an external application, in this case Salesforce CLI, to integrate with Salesforce using APIs
and standard protocols, such as OAuth. We provide a default connected app when you authorize an org with the `org login web`
command.

Important: You must have the **Approve Uninstalled Connected Apps** user permission to complete this task. Org administrators
have the permission by default.

In the task below, the steps marked _Required for JWT_ are required only if you’re creating a connected app to use with the `org login`
`jwt` command. In this case you also need a file that contains a digital certificate, such as `server.crt` . The steps are optional if
you’re creating a connected app to use with `org login web` .

**1.** Contact Salesforce Customer Support to enable the creation of connected apps in your org.


Authorization Create a Connected App in Your Org

Creating connected apps is now disabled by default, because connected apps are being deprecated. If you need to create a connected
[app, Salesforce Customer Support must enable an org perm in your org. This is a one-time process per org. See New connected](https://help.salesforce.com/s/articleView?id=005228017&type=1&language=en_US)
[apps can no longer be created in Spring ‘26.](https://help.salesforce.com/s/articleView?id=005228017&type=1&language=en_US)

**2.** Log in to your org.

**3.** From Setup, in the Quick Find box, enter _`External Client Apps,`_ and then select **Settings** .

**4.** Turn on **Allow creation of connected apps** and click **Enable** .

**5.** Click **New Connected App** .

**6.** [Update the basic information as needed, such as the connected app name and your email address.](https://help.salesforce.com/articleView?id=connected_app_create_basics.htm&language=en_US)

**7.** Select **Enable OAuth Settings** .

**8.** For the callback URL, enter _`http://localhost:1717/OauthRedirect`_ .

If port 1717 (the default) is already in use on your local machine, specify an available one instead. Then update your
`sfdx-project.json` file by setting the `oauthLocalPort` property to the new port. For example, if you set the callback
URL to _`http://localhost:1919/OauthRedirect`_ :

```
     "oauthLocalPort" : "1919"

```

**9.** (Required for JWT) Select **Use digital signatures** .

**10.** (Required for JWT) Click **Choose File** and upload file that contains your digital certificate, such as `server.crt` .

**11.** Add these OAuth scopes:

**•** **Manage user data via APIs (api)**

**•** **Manage user data via Web browsers (web)**

**•** **Perform requests at any time (refresh_token, offline_access)**

**12.** Click **Save**, then **Continue** .

**13.** Click **Manage Consumer Details** .

If prompted, verify your identity by entering the verification code that was automatically sent to your email address.

**14.** Click **Copy** next to Consumer Key because you need it later when you run an `org login` command. Depending on whether
you specify that it's required, also copy the Consumer Secret.

**15.** Click **Back to Manage Connected Apps** .

**16.** Click **Manage** .

**17.** Click **Edit Policies** .

**18.** In the OAuth Policies section, for the Refresh Token Policy field, click **Expire refresh token after:** and enter 90 days or less.

Setting a maximum of 90 days for the refresh token expiration is a security best practice. To continue running CLI commands against
an org whose refresh tokens have expired, reauthorize it with the `org login web` or `org login jwt` command.

**19.** In the Session Policies section, set **Timeout Value** to _`15 minutes`_ .

Setting a timeout for access tokens is a security best practice. Salesforce CLI automatically handles an expired access token by referring
to the refresh token.

**20.** (Required for JWT) In the OAuth Policies section, select **Admin approved users are pre-authorized** for permitted users, and click
**OK** .

**21.** Click **Save** .


## Authorization Use the Default Connected App Securely

**22.** (Required for JWT) Click **Manage Profiles**, select the profiles that are pre-authorized to use this connected app, and click **Save** .
Similarly, click **Manage Permission Sets** to select the permission sets. Create permission sets if necessary.

To specify the consumer key, use the `--client-id` flag of the `org login` commands. For example, if your consumer key is
04580y4051234051 and you’re authorizing a Dev Hub org by logging into it from a browser, run this command in a terminal (macOS
and Linux) or command prompt (Windows):

```
   sf org login web --client-id 04580y4051234051 --set-default-dev-hub --alias my-hub-org

```

If you specifed in the connected app that the web login flow requires a client (consumer) secret, the command prompts you for it. The
command then opens the login page for you to add your org credentials.

See the reference for `[org login web](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_org_commands_unified.htm#cli_reference_org_login_web_unified)` and `[org login jwt](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_org_commands_unified.htm#cli_reference_org_login_jwt_unified)` for more examples.

SEE ALSO:

Create a Private Key and Self-Signed Digital Certificate

_Salesforce Help_ [: Connected Apps](https://help.salesforce.com/articleView?id=connected_app_overview.htm&language=en_US)

Authorization

_Salesforce Help_ [: Set Up Multi-Factor Authentication](https://help.salesforce.com/articleView?id=security_2fa_config.htm&language=en_US)

## Use the Default Connected App Securely

If you authorize an org with the `org login web` command, but don't specify the `--client-id` flag, Salesforce CLI creates a
default connected app in the org called `Salesforce CLI` . However, its refresh tokens are set to never expire. As a security best
practice, Salesforce recommends that refresh tokens in your org expire after 90 days or fewer. Another security best practice is to set an
expiration for the access token to 15 minutes. Similar to refresh tokens, the access token in the default connected app is set to never
expire. To continue using this default connected app in a secure way, configure its policies.

Important: You must be the org administrator to install the default `Salesforce CLI` connected app, which is one of the
steps of this task.

**1.** Log in to your org.

**2.** From Setup, enter _`OAuth`_ in the Quick Find box, then select **Connected Apps OAuth Usage** .

**3.** Select the `Salesforce CLI` app and click **Install** . Confirm by clicking **Install** again.

**4.** Click **Edit Policies** .

**5.** In the OAuth Policies section, for the Refresh Token Policy field, click **Expire refresh token after:** and enter _`90 Days`_ or less.

**6.** In the Session Policies section, set **Timeout Value** to _`15 minutes`_ .

**7.** Click **Save** .

If you run a CLI command against an org whose refresh token has expired, you get an error. For example:

```
   ERROR running org open: Error authenticating with the refresh token due to: expired

   access/refresh token

```

The `org list` command also displays expired refresh token information in the CONNECTED STATUS column. To continue using the
org, reauthorize it with the `org login web` or `org login jwt` command.


## Authorization Use an Existing Access Token

Salesforce CLI automatically handles an expired access token by referring to the refresh token.

SEE ALSO:

_Salesforce Help_ [: Connected Apps](https://help.salesforce.com/articleView?id=connected_app_overview.htm&language=en_US)

Authorize an Org Using a Browser

Authorize an Org Using the JWT Flow

## Use an Existing Access Token

When you authorize an org using the `org login` commands, Salesforce CLI takes care of generating and refreshing all tokens, such
as the access token. But sometimes you want to run a few CLI commands against an existing org without going through the entire
authorization process. In this case, you provide the access token and URL of the Salesforce instance that hosts the org to which you want
to connect.

Almost all CLI commands that have the `--target-org | -o` flag accept an access token. The only exception is `org display`
`user` .

**1.** Open a terminal (macOS and Linux) or command prompt (Windows).

**2.** Run the `org display` command to get the instance URL for the org to connect to. See the value for the `Instance Url`
key.

```
     sf org display --target-org myorg

     === Org Description

      KEY VALUE

      ──────────────────────────────────────────────────────────────

      Access Token [REDACTED] Use 'sf org auth show-access-token' to view

     ...

      Instance Url https://creative-impala-20hx3-dev-ed.my.salesforce.com

     ...

```

**3.** Run the `org auth show-access-token` command to get the access token.

```
     sf org auth show-access-token --target-org myorg

     � You're about to reveal the access token for "myorg". This token grants full access

     to the org with your current permissions. Sharing or logging this token is equivalent

     to sharing your

     credentials. Do you want to continue?

     # Yes

     ┌──────────────┬────────────────────────────────────────────┐

     │Key │Value │

     ├──────────────┼────────────────────────────────────────────┤

     │Access Token │00D8H0000007wprAQkAQAlOT5H<truncated> │

     └──────────────┴────────────────────────────────────────────┘

## 4. Use config set to set the org-instance-url configuration variable. To set it locally, run the command from a Salesforce
```

DX project; to set it globally, use the `--global` flag.

```
     sf config set org-instance-url=https://creative-impala-20hx3-dev-ed.my.salesforce.com

     --global

```


## Authorization Authorize an Org Using Its SFDX Authorization URL

**5.** When you run the CLI command, use the org’s access token as the value for the `--target-org` flag rather than the org’s
username. For example:

```
     sf project deploy start --source-dir <source-dir> --target-org 00D8H0000007wprAQkAQAlOT5H

```

Tip: If your access token contains a `!` character, you must sometimes escape it with a backslash ( `\` ). For example, if your
access token is `00007wpr!AQkAQA`, specify it this way: `--target-org 00007wpr\!AQkAQA`

Salesforce CLI doesn’t store the access token in its internal files. It uses it only for this CLI command run.

SEE ALSO:

## Authorization Information for an Org

_[Salesforce CLI Command Reference](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_config_commands_unified.htm#cli_reference_config_set_unified)_ : config set

_[Salesforce CLI Command Reference](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_project_commands_unified.htm#cli_reference_project_deploy_start_unified)_ : project deploy start

## Authorize an Org Using Its SFDX Authorization URL

Use an org's Salesforce DX (SFDX) authorization URL to authorize an org in continuous integration (CI) environments, which are fully
automated and don’t support the human interactivity of logging into a browser.

**1.** Open a terminal (macOS and Linux) or command prompt (Windows) on the computer where you’ve already authorized the org
using a Web browser.

**2.** Get your org’s SFDX authorization URL and store it in a file by running this command.

```
     sf org auth show-sfdx-auth-url --target-org my-org --json > authFile.json

```

The JSON output includes a key called `sfdxAuthUrl`, whose value is the org’s SFDX authorization URL.

**3.** In your CI environment, authorize the org by referencing the `authFile.json` file with this command.

```
     sf org login sfdx-url --sfdx-url-file authFile.json

```

For more information and examples, see the reference about the `org login sfdx-url` [command in the Salesforce CLI Command](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_org_commands_unified.htm#cli_reference_org_login_sfdx-url_unified)
[Reference.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_org_commands_unified.htm#cli_reference_org_login_sfdx-url_unified)

## Authorization Information for an Org

You can view information for all orgs that you’ve authorized and the scratch orgs that you’ve created.

To view authorization information about an org, run this command from a terminal (macOS and Linux) or command prompt (Windows).

```
   sf org display --target-org <username-or-alias>

```

If you have set a default org, you don’t have to specify the `--target-org` flag. To display the usernames for all the active orgs that
you’ve authorized or created, run `org list` .

If you’ve set an alias for an org, you can specify it with the `--target-org` flag. This example uses the `my-scratch-org` alias.

```
   sf org display --target-org my-scratch-org

   Warning: Secrets are now hidden from 'sf org display' command output. Use the 'sf org auth'

    commands instead. As a temporary workaround, you can set SF_TEMP_SHOW_SECRETS=true to

```


## Authorization View Org Authentication Secrets

```
   render these secrets. This workaround will be removed in an upcoming release.

   === Org Description

    KEY VALUE

    ───────────────

   ────────────────────────────────────────────────────────────────────────────────────────────────────────────────

    Access Token [REDACTED] Use 'sf org auth show-access-token' to view

    Alias my-scratch-org

    Api Version 58.0

    Client Id PlatformCLI

    Created By jdoe@fabdevhub.org

    Created Date 2023-06-09T17:59:18.000+0000

    Dev Hub Id jdoe@fabdevhub.org

    Edition Developer

    Expiration Date 2023-06-16

    Id 00D8H0000007wprU

    Instance Url https://java-connect-41-dev-ed.scratch.my.salesforce.com

    Org Name Your Company

    Signup Username test-gm9uud@example.com

    Status Active

    Username test-gm9uud@example.com

```

Note: To help prevent security breaches, the `org display` output doesn’t include sensitive authentication information such
as access tokens, passwords, SFDX auth URLs, client secrets, or refresh tokens. To explicitly retrieve these secrets, use the `sf org`
`auth show-*` commands.

SEE ALSO:

[OAuth 2.0 Web Server Authentication Flow](https://help.salesforce.com/articleView?id=remoteaccess_oauth_web_server_flow.htm&language=en_US)

Salesforce DX Usernames and Orgs

## View Org Authentication Secrets

Use dedicated commands to explicitly retrieve sensitive authentication information, such as access tokens, passwords, and SFDX
authorization URLs.

To improve security, sensitive authentication information isn't displayed in the output of standard CLI commands, such as `sf org`
`display` and `sf org list` . Instead, use the dedicated `org auth show-*` commands to explicitly retrieve credentials when
needed.

Warning: The `org auth show-*` commands expose sensitive credentials that grant access to your org. Sharing or logging
these secrets is equivalent to sharing your login credentials, resulting in unintended access and escalation of privilege. Handle
them with care and avoid storing them in unencrypted files or logs.

View Access Token

To retrieve an org's access token, run this command from a terminal (macOS and Linux) or command prompt (Windows).

```
   sf org auth show-access-token --target-org <username-or-alias>

```


## Authorization Log Out of an Org

The command prompts you to confirm before displaying the token. To bypass the prompt in non-interactive environments such as
CI/CD pipelines, use the `--json` or `--no-prompt` flag.

View SFDX Authorization URL

To retrieve an org's Salesforce DX authorization URL, run this command.

```
   sf org auth show-sfdx-auth-url --target-org <username-or-alias>

```

This URL contains all the information needed to authorize the org in a continuous integration (CI) environment. The command prompts
you to confirm before displaying the URL. To bypass the prompt, use the `--json` or `--no-prompt` flag.

View User Password

To retrieve the password for a scratch org user, run this command.

```
   sf org auth show-user-password --target-org <username-or-alias>

```

The command prompts you to confirm before displaying the password. To bypass the prompt, use the `--json` or `--no-prompt`
flag.

## Log Out of an Org

For security purposes, you can use the Salesforce CLI to log out of any org you’ve previously authorized. This practice prevents other
users from accessing your orgs if you don’t want them to.

Important: The only way to access an org after you log out of it is with a password. By default, new scratch orgs contain one
administrator with no password. Therefore, to avoid losing access to a scratch org, set a password for at least one user of a scratch
org if you want to access it again after logging out. If you don’t want to access the scratch org again, delete it with `org delete`
`scratch` rather than log out of it.

To log out of an org, run `org logout` from a terminal (macOS and Linux) or command prompt (Windows). This example uses the
alias `my-hub-org` to log out.

```
   sf org logout --target-org my-hub-org

```

To log out of all your orgs, including scratch orgs, use the `--all` flag.

```
   sf org logout --all

```

To access an org again, other than a scratch org, reauthorize it.

When you log out of an org, it no longer shows up in the `org list` output. If you log out of a Dev Hub org, the associated scratch
orgs show up only if you specify the `--all` flag.

SEE ALSO:

_[Salesforce CLI Command Reference](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_org_commands_unified.htm#cli_reference_org_logout_unified)_ : org logout

_VS Code Command_ [: SFDX: Log Out from All Authorized Orgs, SFDX: Log Out from Default Org](https://developer.salesforce.com/docs/platform/sfvscode-extensions/guide/default-org.html)


# CHAPTER 5 Metadata Coverage

Launch the Metadata Coverage report to determine supported metadata for scratch org source tracking
purposes. The Metadata Coverage report is the ultimate source of truth for metadata coverage across
several channels. These channels include Metadata API, scratch org source tracking, unlocked packages,
second-generation managed packages, classic managed packages, and more.

[View the Metadata Coverage report.](https://developer.salesforce.com/docs/success/metadata-coverage-report/references/coverage-report/metadata-coverage-report.html)

[For more information, see Metadata Types in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_types_list.htm) _Metadata API Developer Guide_ .

We've moved the information on Hard-Deleted Components in Unlocked Packages.

SEE ALSO:

[Components Available in Managed Packages](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/packaging_packageable_components.htm)


# CHAPTER 6 Scratch Orgs

In this chapter ...

**•** Supported Scratch
Org Editions and
Allocations

The scratch org is a source-driven and disposable deployment of Salesforce code and metadata. A scratch
org is fully configurable, allowing developers to emulate different Salesforce editions with different
features and settings. You can share the scratch org configuration file with other team members, so you
all have the same basic org in which to do your development. In addition to code and metadata,
developers can install packages and deploy synthetic or dummy data for testing. Don’t add personal
data to scratch orgs.

**•** Build Your Own data to scratch orgs.
Scratch Org Definition
Scratch orgs drive developer productivity and collaboration during the development process, and
File
facilitate automated testing and continuous integration. You can use Salesforce CLI or an IDE to open

**•** Create a Scratch Org
your scratch org in a browser without logging in. Spin up a new scratch org when you want to:
Based on an Org
Shape **•** Start a new project.

**•** Create Scratch Orgs **•** Start a new feature branch.

# • Scratch Org • Test a new feature.

Snapshots **•** Start automated testing.

**•** Select the Salesforce

**•**

Release for a Scratch

**•**

Org

**•** Perform development tasks directly in an org.

**•** Start from “scratch” with a fresh new org.

**•** Deploy Source From Alternatives to scratch orgs are sandboxes and Developer Edition orgs, which are used as development
Your Project to the environments for many Salesforce development use cases. If you’re wondering whether to use a sandbox,
# Scratch Org scratch org, or Developer Edition org as your development environment, you’re not alone. To help you

[better understand which to choose, see the Salesforce Developers Blog: Choose the Right Salesforce](https://developer.salesforce.com/blogs/2024/05/choose-the-right-salesforce-org-for-the-right-job)

**•** Retrieve Source from
the Scratch Org to [Org for the Right Job.](https://developer.salesforce.com/blogs/2024/05/choose-the-right-salesforce-org-for-the-right-job)
Your Project

**•** Scratch Org Users

**•** Manage Scratch
Orgs from the Dev
Hub Org

Source Tracking

Source tracking refers to tracking the changes you make to your local source files and the metadata in
your org, and keeping both in sync.

**•** Scratch Org Error
Scratch orgs have source tracking enabled by default. You can opt out of source tracking when you
Codes
create the scratch org by specifying the `--no-track-source` flag of the `org create`
`scratch` command. This flag affects only your local configuration, not the scratch org itself. Salesforce
CLI sets a local configuration option `trackSource: false` as part of your authorization information
to the org. If you log out of the scratch org and then log back in again, source tracking is enabled again
by default.

If you’re actively in development mode, we suggest keeping source tracking enabled in your scratch
org so you can easily sync the changes between your org and your local project. But source tracking can
slow down deployments and retrievals, so it’s sometimes better to disable it if it’s not needed. Here are
some use cases.


Scratch Orgs

**•** Your continuous integration (CI) script simply creates a scratch org, deploys source, runs Apex and
browser tests, and then deletes the scratch org.

**•** You want to spin up a scratch org for a demo, user acceptance testing, or debugging.

**•** Your test data has changed and you want to ensure it’s correct by importing it into a scratch org.
But you haven’t changed any metadata or source code.

**•** You want to install and verify a package your CI built.

**•** You want to test a pull request by deploying code to a scratch org, but you don’t plan to change
the code.

Scratch Org Creation Methods

By default, scratch orgs are empty. They don’t contain much of the sample metadata that you get when
you sign up for an org, such as a Developer Edition org, the traditional way. Some of the things not
included in a scratch org are:

**•** Custom objects, fields, indexes, tabs, and entity definitions

**•** Sample data

**•** Sample Chatter feeds

**•** Dashboards and reports

**•** Workflows

**•** Picklists

**•** Profiles and permission sets

**•** Apex classes, triggers, and pages

Before creating a scratch org, you must configure it so it has the features, settings, licenses, and limits
that mirror a source org, often your production org. The combination of features, settings, edition, licenses,
and limits are what we refer to as the org’s shape.

We offer these methods for configuring scratch orgs:

**•** Build Your Own Scratch Org Definition File

**•** Create a Scratch Org Based on an Org Shape

**•** Create a Scratch Org Based on a Snapshot

On Which Salesforce Instances Are Scratch Orgs
Created?

Scratch orgs are created on sandbox instances. The sandbox instance depends on the country information
used when creating the Dev Hub org.

Scratch orgs for Government Cloud and Hyperforce are created in the region where the Dev Hub org is
physically located.

**•** Scratch orgs created from a Dev Hub org in Government Cloud are created in a Government Cloud
instance.

**•** Scratch orgs created from a Dev Hub org in Hyperforce are created on a Hyperforce instance.


Scratch Orgs

If you notice that your scratch orgs aren’t located in the expected region, create a Salesforce Support
case.

Scratch Org Expiration Policy

A scratch org is temporary and is deleted along with the associated ActiveScratchOrgs records from the
Dev Hub after their expiration. This expiration process ensures that teams frequently sync their changes
with their version control system and are working with the most recent version of their project.

Scratch orgs have a maximum 30 days lifespan. You can select a duration from 1 through 30 days at the
time of creation, with the default set at 7 days. After the scratch org has expired, you can’t restore it.

Note: Deleting a scratch org doesn’t terminate your scratch org subscription. If your subscription
is still active, you can create a new scratch org. Creating a new scratch org counts against your
daily and active scratch org limits.

SEE ALSO:

_Salesforce Admins Blog_ [: Sandboxes vs. Scratch Orgs and How to Use Them](https://admin.salesforce.com/blog/2023/sandboxes-vs-scratch-orgs-and-how-to-use-them)


## Scratch Orgs Supported Scratch Org Editions and Allocations Supported Scratch Org Editions and Allocations

Your Dev Hub org is often your production org, and you can enable Dev Hub in these editions: Developer, Enterprise, Unlimited, or
Performance. Your Dev Hub edition determines how many scratch orgs you can create. You choose one of the supported scratch org
editions each time you create a scratch org.

## Supported Scratch Org Editions

Possible values for the Salesforce edition of the scratch org are:

**•** Developer

**•** Enterprise

**•** Group

**•** Professional

Note: Partners can create partner edition scratch orgs: Partner Developer, Partner Enterprise, Partner Group, and Partner Professional.
[This feature is available only if creating scratch orgs from a Dev Hub in a partner business org. See Supported Scratch Org Editions](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/isv_partner_scratch_org_editions.htm)
[for Partners in the](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/isv_partner_scratch_org_editions.htm) _First-Generation Managed Packaging Developer Guide_ for details.

Scratch orgs have these storage limits:

**•** 500 MB for data

**•** 50 MB for files

[Entities defined as metadata types aren’t counted as part of storage allocations in scratch orgs. For more information about entities that](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_types_list.htm)
are counted against storage allocations, see _Salesforce Help_ [: Data and File Storage Allocations.](https://help.salesforce.com/s/articleView?id=xcloud.overview_storage.htm&type=5&language=en_US)

Supported Dev Hub Editions and Associated Scratch Org Allocations

To ensure optimal performance, your Dev Hub org edition determines your scratch org allocations. These allocations determine how
many scratch orgs you can create daily, and how many can be active at a given point.

[To try out scratch orgs, sign up for a Developer Edition org on Salesforce Developers, then enable Dev Hub.](https://developer.salesforce.com/signup?d=70130000000td6N)

Note: If you’re a partner or ISV, your scratch org allocations are likely different. See the _First-Generation Managed Packaging_
_Developer Guide_ for details.

The _active scratch org allocation_ is the maximum number of scratch orgs you can have at any given time based on the edition type. The
allocation becomes available if you delete a scratch org or if a scratch org expires. The _daily scratch org allocation_ is the maximum number
of successful scratch org creations you can initiate in a rolling (sliding) 24-hour window. Allocations are determined based on the number
of scratch orgs created in the preceding 24 hours.


## Scratch Orgs Build Your Own Scratch Org Definition File

List Active and Daily Scratch Orgs

Note: If your Salesforce admin provided access to the Dev Hub org using the Free Limited Access license and you can’t run this
command, contact your admin for assistance.

To view your scratch org allocations and how many are remaining, run this command in a terminal or command window against your
Dev Hub org. Only relevant limits ( `ActiveScratchOrgs` and `DailyScratchOrgs` ) are shown.

```
   sf limits api display --target-org <Dev Hub username or alias>

```

Look for these two limits in the output:

```
   Name Remaining Max

   ──────────────────────────────────────────────────── ─────────

   ActiveScratchOrgs 198 200

   DailyScratchOrgs 400 400

```

View Limits for a Scratch Org

To view limits information for a scratch org:

```
   sf limits api display --target-org <scratch org username or alias>

## Build Your Own Scratch Org Definition File

```

The scratch org definition file is a blueprint for a scratch org. It mimics the shape of an org that you use in the development lifecycle,
such as sandbox, packaging, or production.

The settings and configuration options associated with a scratch org determine its shape, including:

**•** Edition—The Salesforce edition of the scratch org, such as Developer, Enterprise, Group, or Professional.

**•** Add-on features—Functionality that isn’t included by default in an edition.

**•** Settings—Org and feature settings used to configure Salesforce products, such as Field Service and Experience Cloud.

Setting up different scratch org definition files allows you to easily create scratch orgs with different shapes for testing. For example, you
can turn Field Service on or off in a scratch org by setting the FieldService org preference in the definition file. If you want a scratch org
with sample data and metadata like you’re used to, add this option: `hasSampleData` .

We recommend that you keep this file in your project and check it in to your version control system. For example, create a team version
that you check in for all team members to use. Individual developers could also create their own local version that includes the scratch
org definition parameters. Examples of these parameters include email and last name, which identify who is creating the scratch org.

Scratch Org Definition File Name

You indicate the path to the scratch org configuration file when you create a scratch org with the `org create scratch` CLI
command.

**•** If you’re using Salesforce CLI on the command line, you can name this file whatever you like and locate it anywhere the CLI can
access.

**•** If you’re using Salesforce Extensions for VS Code, make sure that the scratch org definition file is located in the `config` folder of
your Salesforce DX project. Its name must also end in `scratch-def.json` .


Scratch Orgs Build Your Own Scratch Org Definition File

If you’re using a sample repo or creating a Salesforce DX project, the sample scratch org definition files are located in the `config`
directory. You can create different configuration files for different org shapes or testing scenarios. For easy identification, name the file
something descriptive, such as `devEdition-scratch-def.json` or `packaging-org-scratch-def.json` .

Scratch Org Definition File Options

Here are the options you can specify in the scratch org definition file:


Scratch Orgs Build Your Own Scratch Org Definition File


Scratch Orgs Build Your Own Scratch Org Definition File

Sample Scratch Org Definition File

Here’s what the scratch org definition JSON file looks like. For more information on features and settings, see Scratch Org Features.

```
   {

     "orgName": "Acme",

     "edition": "Enterprise",

     "features": ["Communities", "ServiceCloud", "Chatbot"],

     "settings": {

       "communitiesSettings": {

         "enableNetworksEnabled": true

       },

       "mobileSettings": {

         "enableS1EncryptedStoragePref2": true

       },

       "omniChannelSettings": {

         "enableOmniChannel": true

       },

       "caseSettings": {

         "systemUserEmail": "support@acme.com"

       }

     }

   }

```

Some features, such as Experience Cloud, can require a combination of a feature and a setting to work correctly for scratch orgs. Experience
Cloud uses the term `Communities` in its configuration. This code snippet sets both the feature and associated setting.

```
   "features": ["Communities"],

      "settings": {

        "communitiesSettings": {

         "enableNetworksEnabled": true

       },

        ...

```

Create a Custom Field for ScratchOrgInfo

You can add more options to the scratch org definition to manage your Dev Ops process. To do so, create a custom field on the
[ScratchOrgInfo object. (ScratchOrgInfo tracks scratch org creation and deletion.)](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_scratchorginfo.htm)

Important: If you’re making these changes directly in your production org, proceed with the appropriate level of caution. The
ScratchOrgInfo object isn’t available in sandboxes or scratch orgs.

In the Dev Hub org, create the custom field.

**•** From Setup, enter _`Object Manager`_ in the Quick Find box, then select **Object Manager** .

**•** Click **Scratch Org Info** .

**•** In Fields & Relationships, click **New** .

**•** Define the custom field, then click **Save** .


Scratch Orgs Build Your Own Scratch Org Definition File

After you create the custom field, you can pass it a value in the scratch org definition file by referencing it with its API name. Let’s say
you create two custom fields called `workitem` and `release` . Add the custom fields and associated values to the scratch org
definition, then create the scratch org:

```
   {

      "orgName": "MyCompany",

      "edition": "Developer",

      "workitem__c": "W-12345678",

      "release__c": "June 2024 pilot",

      "settings": {

         "omniChannelSettings": {

            "enableOmniChannel": true

      }

          }

   }

```

Set Object-Level Sharing Settings and Default Record Types

To install successfully, some packages require that you define object-level sharing settings and default record types before installation.
Set the sharing settings and default record types with `objectSettings` . In this sample scratch org definition file, we set a sharing
model and a default record type for opportunity, and a default record type for account.

```
   {

     "orgName": "MyCompany",

     "edition": "Developer",

     "features": ["Communities", "ServiceCloud", "Chatbot"],

     "settings": {

       "communitiesSettings": {

         "enableNetworksEnabled": true

       }

     }

     "objectSettings": {

      "opportunity": {

        "sharingModel": "private",

        "defaultRecordType": "default"

      },

      "account": {

        "defaultRecordType": "default"

      }

     }

   }

```

Scratch Org Features
The scratch org definition file contains the configuration values that determine the shape of the scratch org. You can enable these
supported add-on features in a scratch org.

Scratch Org Settings
Scratch org settings are the format for defining org preferences in the scratch org definition. Because you can use all Metadata API
settings, they’re the most comprehensive way to configure a scratch org. If a setting is supported in Metadata API, it’s supported in
scratch orgs. Settings provide you with fine-grained control because you can define values for all fields for a setting, rather than just
enabling or disabling it.


### Scratch Orgs Scratch Org Features Scratch Org Features

The scratch org definition file contains the configuration values that determine the shape of the scratch org. You can enable these
supported add-on features in a scratch org.

Note: Some scratch org features require a license or permissions in the Dev Hub org. If you can’t create the scratch org by just
specifying the feature name in the scratch org definition file, see your Salesforce admin for assistance.

Supported Features

Features aren’t case-sensitive. You can indicate them as all-caps, or as we define them here for readability. If a feature is followed by
<value>, you must specify a value as an incremental allocation or limit.

You can specify multiple feature values in a comma-delimited list in the scratch org definition file.

```
   "features": ["ServiceCloud", "API", "AuthorApex"],

```

AccountInspection
Enables the Account Intelligence view. The Account Intelligence view is a consolidated dashboard showing account metrics, activities,
and related opportunities and cases.

AccountingSubledgerGrowthEdition
Provides three permission sets that enable access to Accounting Subledger Growth features.

AccountingSubledgerStarterEdition
Provides three permission sets that enable access to Accounting Subledger Starter features.

AccountingSubledgerUser
Enables organization-wide access to Accounting Subledger Growth features when the package is installed.

AddCustomApps:<value>
Increases the maximum number of custom apps allowed in an org. Indicate a value from 1–30.

AddCustomObjects:<value>
Increases the maximum number of custom objects allowed in the org. Indicate a value from 1–30.

AddCustomRelationships:<value>
Increases the maximum number of custom relationships allowed on an object. Indicate a value from 1–10.

AddCustomTabs:<value>
Increases the maximum number of custom tabs allowed in an org. Indicate a value from 1–30.

AddDataComCRMRecordCredit:<value>
Increases record import credits assigned to a user in your scratch org. Indicate a value from 1–30.

AddInsightsQueryLimit:<value>
Increases the size of your CRM Analytics query results. Indicate a value from 1–30 (multiplier is 10). Setting the quantity to 6 increases
the query results to 60.

AdditionalFieldHistory:<value>
Increases the number of fields you can track history for beyond the default, which is 20 fields. Indicate a value between 1–40.

AdmissionsConnectUser
Enables the Admissions Connect components. Without this scratch org feature parameter, the custom Admissions Connect
components render as blank.


Scratch Orgs Scratch Org Features

AdvisorLinkFeature
Enables the Student Success Hub components. Without this scratch org feature parameter, the custom Student Success Hub
components render as blank.

AdvisorLinkPathwaysFeature
Enables the Pathways components. Without this scratch org feature parameter, the custom Pathways components render as blank.

AgentforceVibesUnmeteredAccess
Provides unmetered access to Agentforce Vibes with included AI models for standard prompting and development workflows.
Enables teams to build, iterate, and experiment with AI-assisted experiences without per-interaction credit consumption.

AIAttribution
Provides access to Einstein Attribution for Marketing Cloud Account Engagement. Einstein Attribution uses AI modeling to dynamically
assign attribution percentages to multiple campaign touchpoints.

AllUserIdServiceAccess
Enables all users to access all users’ information via the user ID service.

AnalyticsAdminPerms
Enables all permissions required to administer the CRM Analytics platform, including permissions to enable creating CRM Analytics
templated apps and CRM Analytics Apps.

AnalyticsAppEmbedded
Provides one CRM Analytics Embedded App license for the CRM Analytics platform.

ApexGuruCodeAnalyzer
Enables ApexGuru's generative AI-powered runtime insights in Salesforce Code Analyzer, which delivers Apex code quality
recommendations directly in developer IDEs.

ApexIntegrationTests (Developer Preview)
Enables you to run end-to-end Apex tests that make callouts to Agentforce and Data 360. Integration tests relax callout restrictions
and transaction rollback semantics, so you can validate real service interactions and assert on actual side effects in your scratch org,
without mock callouts.

API
Even in the editions (Professional, Group) that don’t provide API access, REST API is enabled by default. Use this scratch org feature
to access additional APIs (SOAP, Streaming, Bulk, Bulk 2.0).

ArcGraphCommunity
Lets you add Actionable Relationship Center (ARC) components to Experience Cloud pages so your users can view ARC Relationship
Graphs.

Assessments
Enables dynamic Assessments features, which enables both Assessment Questions and Assessment Question Sets.

AssetScheduling:<value>
Enables Asset Scheduling license. Asset Scheduling makes it easier to book rooms and equipments. Indicate a value between 1–10.

AssociationEngine
Enables the Association Engine, which automatically associates new accounts with the user’s current branch by creating branch unit
customer records.

AuthorApex
Enables you to access and modify Apex code in a scratch org. Enabled by default in Enterprise and Developer Editions.


Scratch Orgs Scratch Org Features

B2BCommerce
Provides the B2B License. B2BCommerce enables business-to-business (B2B) commerce in your org. Create and update B2B stores.
Create and manage buyer accounts. Sell products to other businesses.

B2BLoyaltyManagement
Enables the B2B Loyalty Management license. Create loyalty programs and set up loyalty program-specific processes that allow you
to recognize, rewards, and retain customers.

B2CCommerceGMV
Provides the B2B2C Commerce License. B2B2C Commerce allows you to quickly stand up an ecommerce site to promote brands
and sell products into multiple digital channels. You can create and update retail storefronts in your org, and create and manage
person accounts.

B2CLoyaltyManagement
Enables the Loyalty Management - Growth license. Create loyalty programs and set up loyalty program-specific processes that allow
you to recognize, rewards, and retain customers.

B2CLoyaltyManagementPlus
Enables the Loyalty Management - Advanced license. Create loyalty programs and set up loyalty program-specific processes that
allow you to recognize, rewards, and retain customers.

BatchManagement
Enables the Batch Management license. Batch Management allows you to process a high volume of records in manageable batches.

BenefitManagement
Enables the objects, features, and permissions for managing benefits programs, benefit disbursements, and benefit applicant tracking
in Public Sector Solutions.

BigObjectsBulkAPI
Enables the scratch org to use BigObjects in the Bulk API.

BillingAdvanced
Enables access to all the Billing features and objects that are available with the Revenue Cloud Billing license in the scratch org.

Briefcase
Enables the use of Briefcase Builder in a scratch org, which allows you to create offline briefcases that make selected records available
for viewing offline.

BudgetManagement
Gives users access to budget management features and objects. To enable budget management, add this feature to your scratch
org definition file.

BusinessRulesEngine
Enables Business Rules Engine, which enables both expression sets and lookup tables.

BYOCCaaS
Enables you to set up and test a partner contact center that integrates with supported Contact Center as a Service (CCaaS) providers
in your scratch org.

BYOOTT
Enables you to set up and test a Bring Your Own Channel for Messaging channel that integrates with supported Messaging providers
in your scratch org.

CacheOnlyKeys
Enables the cache-only keys service. This feature allows you to store your key material outside of Salesforce, and have the Cache-Only
Key Service fetch your key on demand from a key service that you control.


Scratch Orgs Scratch Org Features

CalloutSizeMB:<value>
Increases the maximum size of an Apex callout. Indicate a value between 3–12.

CampaignInfluence2
Provides access to Customizable Campaign Influence for Sales Cloud and Marketing Cloud Account Engagement. Customizable
Campaign Influence can auto-associate or allow manual creation of relationships among campaigns and opportunities to track
attribution.

CascadeDelete
Provides lookup relationships with the same cascading delete functionality previously only available to master-detail relationships.
To prevent records from being accidentally deleted, cascade-delete is disabled by default.

CaseClassification
Enables Einstein Case Classification. Case Classification offers recommendations to your agents so they can select the best value.
You can also automatically save the best recommendation and route the case to the right agent.

CaseWrapUp
Enables Einstein Case Wrap-Up. To help agents complete cases quickly, Einstein Case Wrap-Up recommends case field values based
on past chat transcripts.

CGAnalytics
Enables the Consumer Goods Analytics org perm in scratch orgs.

ChangeDataCapture
Enables Change Data Capture, if the scratch org edition doesn't automatically enable it.

Chatbot
Enables deployment of Bot metadata into a scratch org, and allows you to create and edit bots.

ChatterEmailFooterLogo
ChatterEmailFooterLogo allows you to use the Document ID of a logo image, which you can use to customize chatter emails.

ChatterEmailFooterText
ChatterEmailFooterText allows you to use footer text in customized Chatter emails.

ChatterEmailSenderName
ChatterEmailSenderName allows you to customize the name that appears as the sender’s name in the email notification. For example,
your company’s name.

CloneApplication
CloneApplication allows you to clone an existing custom Lightning app and make required customizations to the new app. This
way, you don’t have to start from scratch, especially when you want to create apps with simple variations.

CMSMaxContType
Limits the number of distinct content types you can create within Salesforce CMS to 21.

CMSMaxNodesPerContType
Limits the maximum number of child nodes (fields) you can create for a particular content type to 15.

CMSUnlimitedUse
Enables unlimited content records, content types, and bandwidth usage in Salesforce CMS.

Communities
Allows the org to create an Experience Cloud site. Experience Cloud uses the term Communities in its configuration. To use
Communities, you must also include communitiesSettings > enableNetworksEnabled in the settings section of your scratch org
definition file.


Scratch Orgs Scratch Org Features

CompareReportsOrgPerm
Enables the org permission to allow for comparison of Lightning Reports.

ConAppPluginExecuteAsUser
Enables the pluginExecutionUser field in the ConnectedApp Metadata API object.

ConcStreamingClients:<value>
Increases the maximum number of concurrent clients (subscribers) across all channels and for all event types for API version 36.0
and earlier. Indicate a value between 20–4,000.

ConnectedAppCustomNotifSubscription
Enables connected apps to subscribe to custom notification types, which are used to send custom desktop and mobile notifications.

ConnectedAppToolingAPI
Enables the use of connected apps with the Tooling API.

ConsentEventStream
Enables the Consent Event Stream permission for the org.

ConsolePersistenceInterval:<value>
Increases how often console data is saved, in minutes. Indicate a value between 0–500. To disable auto save, set the value to 0.

ContactsToMultipleAccounts
Enables the contacts to multiple accounts feature. This feature lets you relate a contact to two or more accounts.

ContractApprovals
Enables contract approvals, which allow you to track contracts through an approval process.

ContractManagement
Enables the Contract Lifecycle (CLM) Management features in the org.

ContractMgmtInd
Enables the Contract Lifecycle Management (CLM) features for Industries.

CoreCpq
Enables read-write access to Revenue Cloud features and objects. To use Revenue Cloud, you must also include
revenueManagementSettings > enableCoreCPQ in the settings section of your scratch org definition file.

CPQ
Enables the licensed features required to install the Salesforce CPQ managed package but doesn't install the package automatically.

CustomerDataPlatform
Enables the CustomerDataPlatform license in scratch orgs.

CustomerDataPlatformLite
Enables the Data Cloud license in scratch orgs. You must also include the CustomerDataPlatform feature and
enableCustomerDataPlatform Metadata API setting in your scratch org definition.

CustomerExperienceAnalytics
Enables the Customer Lifecycle Analytics org perm in scratch orgs.

CustomFieldDataTranslation
Enables translation of custom field data for Work Type Group, Service Territory, and Service Resource objects. You can enable data
translation for custom fields with Text, Text Area, Text Area (Long), Text Area (Rich), and URL types.

CustomNotificationType
Allows the org to create custom notification types, which are used to send custom desktop and mobile notifications.


Scratch Orgs Scratch Org Features

DataComDnbAccounts
Provides a license to Data.com account features.

DataComFullClean
Provides a license to Data.com cleaning features, and allows users to turn on auto fill clean settings for jobs.

DataMaskUser
Provides 30 Data Mask permission set licenses. This permission set enables access to an installed Salesforce Data Mask package.

DataProcessingEngine
Enables the Data Processing Engine license. Data Processing Engine helps transform data that's available in your Salesforce org and
write back the transformation results as new or updated records.

DebugApex
Enables Apex Interactive Debugger. You can use it to debug Apex code by setting breakpoints and checkpoints, and inspecting your
code to find bugs.

DecisionTable
Enables Decision Table license. Decision tables read business rules and decide the outcome for records in your Salesforce org or for
the values that you specify.

DefaultWorkflowUser
Sets the scratch org admin as the default workflow user.

DeferSharingCalc
Allows admins to suspend group membership and sharing rule calculations and to resume them later.

DevelopmentWave
Enables CRM Analytics development in a scratch org. It assigns five platform licenses and five CRM Analytics platform licenses to the
org, along with assigning the permission set license to the admin user. It also enables the CRM Analytics Templates and Einstein
Discovery features.

DeviceTrackingEnabled
Enables Device Tracking.

DevOpsCenter
Enables DevOps Center in scratch orgs so that partners can create second-generation managed packages that extend or enhance
the functionality in the DevOps Center application (base) package.

DisableManageIdConfAPI
Limits access to the LoginIP and ClientBrowser API objects to allow view or delete only.

DisclosureFramework
Provides the permission set licenses and permission sets required to configure Disclosure and Compliance Hub.

Division
Turns on the Manage Divisions feature under Company Settings. Divisions let you segment your organization's data into logical
sections, making searches, reports, and list views more meaningful to users. Divisions are useful for organizations with extremely
large amounts of data.

DocGen
Enables the Document Generation Feature in the Org.

DocGenDesigner
Enables the designers to create and configure document templates.

DocGenInd
Enables the Industry Document Generation features in the org.


Scratch Orgs Scratch Org Features

DocumentChecklist
Enables Document Tracking and Approval features, and adds the Document Checklist permission set. Document tracking features
let you define documents to upload and approve, which supports processes like loan applications or action plans.

DocumentReaderPageLimit
Limits the number of pages sent for data extraction to 5.

DSARPortability
Enables an org to access the DSARPortability feature in Privacy Center. Also, provides one seat each of the PrivacyCenter and
PrivacyCenterAddOn licenses.

DurableClassicStreamingAPI
Enables Durable PushTopic Streaming API for API version 37.0 and later.

DurableGenericStreamingAPI
Enables Durable Generic Streaming API for API version 37.0 and later.

DynamicClientCreationLimit
Allows the org to register up to 100 OAuth 2.0 connected apps through the dynamic client registration endpoint.

EAndUDigitalSales
Enables the Energy and Utilities Digital Sales feature in the org.

EAndUSelfServicePortal
Enables the Self Service Portal features for Digital Experience users in the org.

EAOutputConnectors
Enable CRM Analytics Output Connectors.

EASyncOut
Enable CRM Analytics SyncOut.

EdPredictionM3Threshold
Sets the number of records in the payload to 10, after which the Einstein Discovery prediction service uses M3.

EdPredictionTimeout
Sets the maximum duration of a single Einstein Discovery prediction to 100 milliseconds.

EdPredictionTimeoutBulk
Sets the maximum duration of a single Einstein Discovery prediction when it runs in bulk to 10 milliseconds.

EdPredictionTimeoutByomBulk
Sets the maximum duration of a single Bring Your Own Model (BYOM) Einstein Discovery prediction to 100 milliseconds.

EducationCloud: <value>
Enables use of Education Cloud.

Einstein1AIPlatform
Provides access to Einstein generative AI features such as Agentforce, Prompt Builder, Model Builder, and the Models API. To use
generative AI features, you must also include einsteinGptSettings > enableEinsteinGptPlatform in the settings section of your scratch
org definition file.

EinsteinAnalyticsPlus
Provides one CRM Analytics Plus license for the CRM Analytics platform.

EinsteinArticleRecommendations
Provides licenses for Einstein Article Recommendations. Einstein Article Recommendations uses data from past cases to identify
Knowledge articles that are most likely to help your customer service agents address customer inquiries.


Scratch Orgs Scratch Org Features

EinsteinBuilderFree
Provides a license that allows admins to create one enabled prediction with Einstein Prediction Builder. Einstein Prediction Builder
is custom AI for admins

EinsteinDocReader
Provides the license required to enable and use Intelligent Form Reader in a scratch org. Intelligent Form Reader uses optical character
recognition to automatically extract data with Amazon Textract.

EinsteinRecommendationBuilder
Provides a license to create recommendations with Einstein Recommendation Builder. Einstein Recommendation Builder lets you
build custom AI recommendations.

EinsteinSalesRepFdbk
Enables the Agentforce Sales Coach feature in an org. This scratch org feature also includes a large number of Einstein for Sales
Generative AI features.

EinsteinSearch
Provides the license required to use and enable Einstein Search features in a scratch org.

EinsteinVisits
Enables Consumer Goods Cloud. With Consumer Goods cloud, transform the way you collaborate with your retail channel partners.
Empower your sales managers to plan visits and analyze your business’s health across stores. Also, allow your field reps to track
inventory, take orders, and capture visit details using the Retail Execution mobile app.

EinsteinVisitsED
Enables Einstein Discovery, which can be used to get store visit recommendations. With Einstein Visits ED, you can create a visit
frequency strategy that allows Einstein to provide optimal store visit recommendations.

EmbeddedLoginForIE
Provides JavaScript files that support Embedded Login in IE11.

EmpPublishRateLimit:<value>
Increases the maximum number of standard-volume platform event notifications published per hour. Indicate a value between
1,000–10,000.

EnablePRM
Enables the partner relationship management permissions for the org.

EnableManageIdConfUI
Enables access to the LoginIP and ClientBrowser API objects to verify a user's identity in the UI.

Enablement
Enables features for creating, taking, and tracking sales programs with Enablement. Business operations experts and sales leaders
identify the revenue outcomes they want sales reps to achieve, such as increased average deal sizes or shorter ramp times. Then,
they create programs that help sales reps work towards those outcomes as part of their daily work.

EnableSetPasswordInApi
Enables you to use `sf org generate password` to change a password without providing the old password.

EncryptionStatisticsInterval:<value>
Defines the interval (in seconds) between encryption statistics gathering processes. The maximum value is 604,800 seconds (7 days).
The default is once per 86,400 seconds (24 hours).

EncryptionSyncInterval:<value>
Defines how frequently (in seconds) the org can synchronize data with the active key material. The default and maximum value is
604,800 seconds (7 days). To synchronize data more frequently, indicate a value, in seconds, equal to or larger than 0.


Scratch Orgs Scratch Org Features

EnergyAndUtilitiesCloud
Enables the Energy and Utilities Cloud features in the org.

Entitlements
Enables entitlements. Entitlements are units of customer support in Salesforce, such as phone support or web support that represent
terms in service agreements.

ERMAnalytics
Enables the ERM Analytics org perm in your scratch org.

EventLogFile
Enables API access to your org's event log files. The event log files contain information about your org’s operational events that you
can use to analyze usage trends and user behavior.

EntityTranslation
Enables translation of field data for Work Type Group, Service Territory, and Service Resource objects.

ExcludeSAMLSessionIndex
Excludes Session Index in SAML sign-on (SSO) and single logout (SLO) flows.

Explainability
Enables an org to use Decision Explainer features.

ExpressionSetMaxExecPerHour
Enables an org to run a maximum of 500,000 expression sets per hour by using Connect REST API.

ExternalIdentityLogin
Allows the scratch org to use Salesforce Customer Identity features associated with your External Identity license.

FieldAuditTrail
Enables Field Audit Trail for the org and allows a total 60 tracked fields. By default, 20 fields are tracked for all orgs, and 40 more are
tracked with Field Audit Trail.

FieldService:<value>
Provides the Field Service license. Indicate a value between 1–25.

FieldServiceAppointmentAssistantUser:<value>
Adds the Field Service Appointment Assistant permission set license. Indicate a value between 1–25.

FieldServiceDispatcherUser:<value>
Adds the Field Service Dispatcher permission set license. Indicate a value between 1–25.

FieldServiceLastMileUser:<value>
Adds the Field Service Last Mile permission set license. Indicate a value between 1–25.

FieldServiceMobileExtension
Adds the Field Service Mobile Extension permission set license.

FieldServiceMobileUser:<value>
Adds the Field Service Mobile permission set license. Indicate a value between 1–25.

FieldServiceSchedulingUser:<value>
Adds the Field Service Scheduling permission set license. Indicate a value between 1–25.

FinanceLogging
Adds Finance Logging objects to a scratch org. This feature is required for Finance Logging.


Scratch Orgs Scratch Org Features

FinancialServicesCommunityUser:<value>
Adds the Financial Services Insurance Community permission set license, and enables access to Financial Services insurance community
components and objects. Indicate a value between 1–10.

FinancialServicesInsuranceUser
Adds the Financial Services Insurance permission set license, and enables access to Financial Services insurance components and
objects.

FinancialServicesUser:<value>
Adds the Financial Services Cloud Standard permission set license. This permission set enables access to Lightning components and
the standard version of Financial Services Cloud. Also provides access to the standard Salesforce objects and custom Financial Services
Cloud objects. Indicate a value between 1–10.

FlowSites
Enables the use of flows in Salesforce Sites and customer portals.

ForceComPlatform
Adds one Salesforce Platform user license.

ForecastEnableCustomField
Enables custom currency and customer number fields for use as measures in forecasts based on opportunities.

FSCAlertFramework
Makes Financial Services Cloud Record Alert entities accessible in the scratch org.

FSCServiceProcess
Enables the Service Process Studio feature of Financial Service Cloud. Provides 10 seats each of the IndustriesServiceExcellenceAddOn
and FinancialServicesCloudStardardAddOn licenses. To enable the feature, you must also turn on the StandardServiceProcess setting
in Setup and grant users the AccessToServiceProcess permission.

Fundraising
Gives users access to Nonprofit Cloud for Fundraising features and objects in Salesforce.

GenericStreaming
Enables Generic Streaming API for API version 36.0 and earlier.

GenStreamingEventsPerDay:<value>
Increases the maximum number of delivered event notifications within a 24-hour period, shared by all CometD clients, with generic
streaming for API version 36.0 and earlier. Indicate a value between 10,000–50,000.

Grantmaking
Gives users access to Grantmaking features and objects in Salesforce and Experience Cloud.

GuidanceHubAllowed
Enables the Guidance Center panel in Lightning Experience. The Guidance Center shows suggested and assigned content in the
user’s flow of work. Suggested content is related to the app or page where the user is working. Assigned content includes guidance
sets for Salesforce admins, links or Trailhead modules assigned to users with Learning Paths, and Enablement programs for sales
reps.

HealthCloudAddOn
Enables use of Health Cloud.

HealthCloudEOLOverride
Salesforce retired the Health Cloud CandidatePatient object in Spring ‘22 to focus on the more robust Lead object. This scratch org
feature allows you to override that retirement and access the object.


Scratch Orgs Scratch Org Features

HealthCloudForCmty
Enables use of Health Cloud for Experience Cloud Sites.

HealthCloudMedicationReconciliation
Allows Medication Management to support Medication Reconciliation.

HealthCloudPNMAddOn
Enables use of Provider Network Management.

HealthCloudUser
This enables the scratch org to use the Health Cloud objects and features equivalent to the Health Cloud permission set license for
one user.

HighVelocitySales
Provides Sales Engagement licenses and enables Salesforce Inbox. Sales Engagement optimizes the inside sales process with a
high-productivity workspace. Sales managers can create custom sales processes that guide reps through handling different types
of prospects. And sales reps can rapidly handle prospects with a prioritized list and other productivity-boosting features. The Sales
Engagement feature can be deployed in scratch orgs, but the settings for the feature can’t be updated through the scratch org
definition file. Instead, configure settings directly in the Sales Engagement app.

HighVolumePlatformEventAddOn
Increases the daily delivery allocation of high-volume platform events or change data capture events by 100,000 events. This scratch
org feature simulates the purchase of an add-on. If the org has the `HighVolumePlatformEventAddOn`, the daily allocation
is flexible and isn’t enforced strictly to allow for usage peaks.

HLSAnalytics
Enables the HLS Analytics org perm in scratch orgs.

HoursBetweenCoverageJob:<value>
The frequency in hours when the sharing inheritance coverage report can be run for an object. Indicate a value between 1–24.

IdentityProvisioningFeatures
Enables use of Salesforce Identity User Provisioning.

IgnoreQueryParamWhitelist
Ignores allowlisting rules for query parameter filter rules. If enabled, you can add any query parameter to the URL.

IndustriesActionPlan
Provides a license for Action Plans. Action Plans allow you to define the tasks or document checklist items for completing a business
process.

IndustriesBranchManagement
Branch Management lets branch managers and administrators track the work output of branches, employees, and customer segments
in Financial Services Cloud.

IndustriesCompliantDataSharing
Grants users access to participant management and advanced configuration for data sharing to improve compliance with regulations
and company policies.

IndustriesMfgAdvncdAccFrcs
Enables Advanced Account Forecasting. With Advanced Account Forecasting, generate comprehensive, multi-horizon forecasts for
sales, operations, inventory, service, and other aspects of your business. Tailor your forecasting configurations to your objectives to
generate accurate, relevant forecasts.


Scratch Orgs Scratch Org Features

IndustriesMfgPartnerVisitMgmt
Enables Partner Visit Management. Partner Visit Management helps sales managers in your company schedule visits to partner and
distributor locations. Sales managers can use those visits to monitor performance, arrange for periodic check-ins, conduct trainings,
upsell and cross-sell products, and follow up on sales agreement renewals and warranty expiration.

IndustriesMfgProgram
Enables Program Based Business. With Program Based Business, program managers can manage the end-to-end lifecycle of a program
where they derive forecasts based on their customers’ forecasts, transform these forecasts into business opportunities, and convert
those opportunities into run-rate business. Program based business is common across multiple industries such as process, aerospace,
defense, automotive, engineer-to-order, and make-to-order environments.

IndustriesMfgRebates
Enables Rebate Management. Manage incentive programs, track rebate attainment, automate payouts, and gain insights into sales
performance and program effectiveness.

IndustriesMfgTargets
Enables Sales Agreements. With Sales Agreements, you can negotiate purchase and sale of products over a continued period. You
can also get insights into products, prices, discounts, and quantities. And you can track your planned and actual quantities and
revenues with real-time updates from orders and contracts.

IndustriesManufacturingCmty
Provides the Manufacturing Sales Agreement for the Community permission set license, which is intended for the usage of partner
community users. It also provides access to the Manufacturing community template for admins users to create communities.

IndustriesMfgAccountForecast
Enables Account Forecast. With Account Forecast, you can generate forecasts for your accounts based on orders, opportunities, and
sales agreements. You can also create formulas to calculate your forecasts per the requirements of your company.

InsightsPlatform
Enables the CRM Analytics Plus license for CRM Analytics.

InsuranceCalculationUser
Enables the calculation feature of Insurance. Provides 10 seats each of the BRERuntimeAddOn and OmniStudioRuntime licenses.
Also, provides one seat each of the OmniStudio and BREPlatformAccess licenses.

InsuranceClaimMgmt
Enables claim management features. Provides one seat of the InsuranceClaimMgmtAddOn license.

InsurancePolicyAdmin
Enables policy administration features. Provides one seat of the InsurancePolicyAdministrationAddOn license.

IntelligentDocumentReader
Provides the license required to enable and use Intelligent Document Reader in a scratch org. Intelligent Document Reader uses
optical character recognition to automatically extract data with Amazon Textract by using your AWS account.

InvestigativeCaseManagement
Enables the objects, features, and permissions for managing investigative cases, including evidence management and case proceedings,
in Public Sector Solutions.

InvoiceManagement
Enables access to all the Billing features and objects that are available with the Revenue Cloud Advanced license in the scratch org.

Interaction
Enables flows. A flow is the part of Salesforce Flow that collects data and performs actions in your Salesforce org or an external
system. Salesforce Flow provides two types of flows: screen flows and autolaunched flows.


Scratch Orgs Scratch Org Features

InvocableActionExt
Enables the use of InvocableActionExtension metadata to customize how Apex invocable action inputs appear in Flow Builder.

IoT
Enables IoT so the scratch org can consume platform events to perform business and service workflows using orchestrations and
contexts.

JigsawUser
Provides one license to Jigsaw features.

Knowledge
Enables Salesforce Knowledge and gives your website visitors, clients, partners, and service agents the ultimate support tool. Create
and manage a knowledge base with your company information, and securely share it when and where it's needed. Build a knowledge
base of articles that can include information on process, like how to reset your product to its defaults, or frequently asked questions.

LegacyLiveAgentRouting
Enables legacy Live Agent routing for Chat. Use Live Agent routing to chat in Salesforce Classic. Chats in Lightning Experience must
be routed using Omni-Channel.

LightningSalesConsole
Adds one Lighting Sales Console user license.

LightningScheduler
Enables Lightning Scheduler. Lightning Scheduler gives you tools to simplify appointment scheduling in Salesforce. Create a
personalized experience by scheduling customer appointments—in person, by phone, or by video—with the right person at the
right place and time.

LightningServiceConsole
Assigns the Lightning Service Console License to your scratch org so you can use the Lightning Service Console and access features
that help manage cases faster.

LiveAgent
Enables Chat for Service Cloud. Use web-based chat to quickly connect customers to agents for real-time support.

LiveMessage
Enables Messaging for Service Cloud. Use Messaging to quickly support customers using apps such as SMS text messaging and
Facebook Messenger.

LongLayoutSectionTitles
Allows page layout section titles to be up to 80 characters.

LoyaltyAnalytics
Enables Analytics for Loyalty license. The Analytics for Loyalty app gives you actionable insights into your loyalty programs.

LoyaltyEngine
Enables Loyalty Management Promotion Setup license. Promotion setup allows loyalty program managers to create loyalty program
processes. Loyalty program processes help you decide how incoming and new Accrual and Redemption-type transactions are
processed.

LoyaltyManagementStarter
Enables the Loyalty Management - Starter license. Create loyalty programs and set up loyalty program-specific processes that allow
you to recognize, rewards, and retain customers.

LoyaltyMaximumPartners:<value>
Increases the number of loyalty program partners that can be associated with a loyalty program in an org where the Loyalty
Management - Starter license is enabled. The default and maximum value is 1.


Scratch Orgs Scratch Org Features

LoyaltyMaximumPrograms:<value>
Increases the number of loyalty programs that can be created in an org where the Loyalty Management - Starter license is enabled.
The default and maximum value is 1.

LoyaltyMaxOrderLinePerHour:<value>
Increases the number of order lines that can be cumulatively processed per hour by loyalty program processes. Indicate a value
between 1–3,500,000.

LoyaltyMaxProcExecPerHour:<value>
Increases the number of transaction journals that can be processed by loyalty program processes per hour. Indicate a value between
1–500,000.

LoyaltyMaxTransactions:<value>
Increases the number of Transaction Journal records that can be processed. Indicate a value between 1–50,000,000.

LoyaltyMaxTrxnJournals:<value>
Increases the number of Transaction Journal records that can be stored in an org that has the Loyalty Management - Start license
enabled.

Macros
Enables macros in your scratch org. After enabling macros, add the macro browser to the Lightning Console so you can configure
predefined instructions for commonly used actions and apply them to multiple posts at the same time.

MarketingCloud
Provides licenses for Marketing Cloud Growth edition. These licenses provide access to campaigns, flows, emails, forms, landing
pages, and consent management features. You can send up to 20 emails per day from a scratch org.

MarketingUser
Provides access to the Campaigns object. Without this setting, Campaigns are read-only.

MaterialityAssessment
Provides the permission set licenses and permission sets required to configure materiality assessment in Net Zero Cloud.

MaxActiveDPEDefs:<value>
Increases the number of Data Processing Engine definitions that can be activated in the org. Indicate a value between 1–50.

MaxApexCodeSize:<value>
Limits the non-test, unmanaged Apex code size (in MB). To use a value greater than the default value of 10, contact Salesforce
Customer Support.

MaxAudTypeCriterionPerAud
Limits the number of audience type criteria available per audience. The default value is 10.

MaxCustomLabels:<value>
Limits the number of custom labels (measured in thousands). Setting the limit to 10 enables the scratch org to have 10,000 custom
labels. Indicate a value between 1–15.

MaxDatasetLinksPerDT:<value>
Increases the number of dataset links that can be associated with a decision table. Indicate a value between 1–3.

MaxDataSourcesPerDPE:<value>
Increases the number of Source Object nodes a Data Processing Engine definition can contain. Indicate a value between 1–50.

MaxDecisionTableAllowed:<value>
Increases the number of decision tables rules that can be created in the org. Indicate a value between 1–30.


Scratch Orgs Scratch Org Features

MaxFavoritesAllowed:<value>
Increases the number of Favorites allowed. Favorites allow users to create a shortcut to a Salesforce Page. Users can view their
Favorites by clicking the Favorites list dropdown in the header. Indicate a value between 0–200.

MaxFieldsPerNode:<value>
Increases the number of fields a node in a Data Processing Engine definition can contain. Indicate a value between 1–500.

MaxInputColumnsPerDT:<value>
Increases the number of input fields a decision table can contain. Indicate a value between 1–10.

MaxLoyaltyProcessRules:<value>
Increases the number of loyalty program process rules that can be created in the org. Indicate a value between 1–20.

MaxNodesPerDPE:<value>
Increases the number of nodes that a Data Processing Engine definition can contain. Indicate a value between 1–500.

MaxNoOfLexThemesAllowed:<value>
Increases the number of Themes allowed. Themes allow users to configure colors, fonts, images, sizes, and more. Access the list of
Themes in Setup, under Themes and Branding. Indicate a value between 0–300.

MaxOutputColumnsPerDT:<value>
Increases the number of output fields a decision table can contain. Indicate a value between 1–5.

MaxSourceObjectPerDSL:<value>
Increases the number of source objects that can be selected in a dataset link of a decision table. Indicate a value between 1–5.

MaxStreamingTopics:<value>
Increases the maximum number of delivered PushTopic event notifications within a 24-hour period, shared by all CometD clients.
Indicate a value between 40–100.

MaxUserNavItemsAllowed:<value>
Increases the number of navigation items a user can add to the navigation bar. Indicate a value between 0–500.

MaxUserStreamingChannels:<value>
Increases the maximum number of user-defined channels for generic streaming. Indicate a value between 20–1,000.

MaxWishlistsItemsPerWishlist
Limits the number of wishlist items per wishlist. The default value is 500.

MaxWishlistsPerStoreAccUsr
Limits the number of wishlists allowed per store, account, and user. The default value is 100.

MaxWritebacksPerDPE:<value>
Increases the number of Writeback Object nodes a Data Processing Engine definition can contain. Indicate a value between 1–50.

MedVisDescriptorLimit:<value>
Increases the number of sharing definitions allowed per record for sharing inheritance to be applied to an object. Indicate a value
between 150–1,600.

MinKeyRotationInterval
Sets the encryption key material rotation interval at once per 60 seconds. If this feature isn't specified, the rotation interval defaults
to once per 604,800 seconds (7 days) for Search Index key material, and once per 86,400 seconds (24 hours) for all other key material.

MobileExtMaxFileSizeMB:<value>
Increases the file size (in megabytes) for Field Service Mobile extensions. Indicate a value between 1–2,000.


Scratch Orgs Scratch Org Features

MobileSecurity
Enables Enhanced Mobile Security. With Enhanced Mobile Security, you can control a range of policies to create a security solution
tailored to your org’s needs. You can limit user access based on operating system versions, app versions, and device and network
security. You can also specify the severity of a violation.

MobileVoiceAndLLM
Allows mobile apps to download large language models (LLMs) and voice models for offline use from the model store service.
Normally, mobile apps have access to the model store service when Einstein is enabled, but the MobileVoiceAndLLM scratch org
feature enables offline voice without requiring orgs to fully enable Einstein.

MultiLevelMasterDetail
Allows the creation a special type of parent-child relationship between one object, the child, or detail, and another object, the parent,
or master.

MutualAuthentication
Requires client certificates to verify inbound requests for mutual authentication.

MyTrailhead
Enables access to a myTrailhead enablement site in a scratch org.

NonprofitCloudCaseManagementUser
Provides the permission set license required to use and configure the Salesforce.org Nonprofit Cloud Case Management managed
package. You can then install the package in the scratch org.

NumPlatformEvents:<value>
Increases the maximum number of platform event definitions that can be created. Indicate a value between 5–20.

ObjectLinking
Create rules to quickly link channel interactions to objects such as contacts, leads, or person accounts for customers (Beta).

OmnistudioMetadata
Enables Omnistudio metadata API. Using this API, customers can deploy and retrieve Omnistudio components programmatically.

OmnistudioRuntime
Enables business users to execute OmniScripts, DataMappers, FlexCards, and so on in the employee facing applications.

OmnistudioDesigner
Enables administrator or developer to create new OmniScripts/ DataMappers / Integration Procedures instances.

OrderManagement
Provides the Salesforce Order Management license. Order Management is your central hub for handling all aspects of the order
lifecycle, including order capture, fulfillment, shipping, payment processing, and servicing.

OrderSaveLogicEnabled
Enables scratch org support for New Order Save Behavior. OrderSaveLogicEnabled supports only New Order Save Behavior. If your
scratch org needs both Old and New Order Save Behavior, use OrderSaveBehaviorBoth.

OrderSaveBehaviorBoth
Enables scratch org support for both New Order Save Behavior and Old Order Save Behavior.

OutboundMessageHTTPSession
Enables using HTTP endpoint URLs in outbound message definitions that have the Send Session ID option selected.

OutcomeManagement
Gives users access to Outcome Management features and objects in Salesforce and Experience Cloud.

PardotScFeaturesCampaignInfluence
Enables additional campaign influence models, first touch, last touch, and even distribution for Pardot users.


Scratch Orgs Scratch Org Features

PersonAccounts
Enables person accounts in your scratch org.

PipelineInspection
Enables Pipeline Inspection. Pipeline Inspection is a consolidated pipeline view with metrics, opportunities, and highlights of recent
changes.

PlatformCache
Enables Platform Cache and allocates a 3 MB cache. The Lightning Platform Cache layer provides faster performance and better
reliability when caching Salesforce session and org data.

PlatformConnect:<value>
Enables Salesforce Connect and allows your users to view, search, and modify data that's stored outside your Salesforce org. Indicate
a value from 1–5.

PlatformEncryption
Shield Platform Encryption encrypts data at rest. You can manage key material and encrypt fields, files, and other data.

PlatformEventsPerDay:<value>
Increases the maximum number of delivered standard-volume platform event notifications within a 24-hour period, shared by all
CometD clients. Indicate a value between 10,000–50,000.

ProcessBuilder
Enables Process Builder, a Salesforce Flow tool that helps you automate your business processes.

ProductsAndSchedules
Enables product schedules in your scratch org. Enabling this feature lets you create default product schedules on products. Users
can also create schedules for individual products on opportunities.

ProductCatalogManagementAddOn
Enables read-write access to Product Catalog Management features and objects.

ProductCatalogManagementViewerAddOn
Enables read access to Product Catalog Management features and objects.

ProductCatalogManagementPCAddOn
Enables read access to Product Catalog Management features and objects for Partner Community Users in scratch orgs.

ProgramManagement
Enables access to all Program Management and Case Management features and objects.

ProviderFreePlatformCache
Provides 3 MB of free Platform Cache capacity for security-reviewed managed packages. This feature is made available through a
capacity type called Provider Free capacity and is automatically enabled in Developer Edition orgs. Allocate the Provider Free capacity
to a Platform Cache partition and add it to your managed package.

ProviderManagement
Enables the objects, features, and permissions for managing provider networks, care plans, and service delivery in Public Sector
Solutions.

PSSAssetManagement
Enables the objects, features, and permissions for managing assets in Public Sector Solutions.

PublicSectorAccess
Enables access to all Public Sector features and objects.

PublicSectorApplicationUsageCreditsAddOn
Enables additional usage of Public Sector applications based on their pricing.


Scratch Orgs Scratch Org Features

PublicSectorSiteTemplate
Allows Public Sector users access to build an Experience Cloud site from the templates available.

RateManagement
Enables Rate Management that allows you to set, manage, and optimize rates for usage-based products.

RecordTypes
Enables Record Type functionality. Record Types let you offer different business processes, picklist values, and page layouts to different
users.

RefreshOnInvalidSession
Enables automatic refreshes of Lightning pages when the user's session is invalid. If, however, the page detects a new token, it tries
to set that token and continue without a refresh.

RevSubscriptionManagement
Enables Subscription Management. Subscription Management is an API-first, product-to-cash solution for B2B subscriptions and
one-time sales.

S1ClientComponentCacheSize
Allows the org to have up to 5 pages of caching for Lightning Components.

SalesCloudEinstein
Enables Sales Cloud Einstein features and Salesforce Inbox. Sales Cloud Einstein brings AI to every step of the sales process.

SalesforceContentUser
Enables access to Salesforce content features.

SalesforceFeedbackManagementStarter
Provides a license to use the Salesforce Feedback Management - Starter features.

SalesforceHostedMCP
Enables hosted MCP servers on the scratch org. With this scratch org feature parameter, MCP clients can connect to available hosted
MCP servers.

SalesforceIdentityForCommunities
Adds Salesforce Identity components, including login and self-registration, to Experience Builder. This feature is required for Aura
components.

SalesforcePricing
Enables Salesforce Pricing, which allows you to set, manage, and optimize prices across your entire product portfolio

SalesUser
Provides a license for Sales Cloud features.

SAML20SingleLogout
Enables usage of SAML 2.0 single logout.

SCIMProtocol
Enables access support for the SCIM protocol base API.

ScvMultipartyAndConsult
Enables you to set up and test multiparty calls and consult calls for Service Cloud Voice with Partner Telephony.

SecurityEventEnabled
Enables access to security events in Event Monitoring.


Scratch Orgs Scratch Org Features

SentimentInsightsFeature
Provides the license required to enable and use Sentiment Insights in a scratch org. Use Sentiment Insights to analyze the sentiment
of your customers and get actionable insights to improve it.

ServiceCatalog
Enables Employee Service Catalog so you can create a catalog of products and services for your employees. It can also turn your
employees' requests for these products and services into approved and documented orders.

ServiceCloud
Assigns the Service Cloud license to your scratch org, so you can choose how your customers can reach you, such as by email, phone,
social media, online communities, chat, and text.

ServiceCloudVoicePartnerTelephony
Assigns the Service Cloud Voice with Partner Telephony add-on license to your scratch org, so you can set up a Service Cloud Voice
contact center that integrates with supported telephony providers. Indicate a value from 1–50.

ServiceUser
Adds one Service Cloud User license, and allows access to Service Cloud features.

SessionIdInLogEnabled
Enables Apex debug logs to include session IDs. If disabled, session IDs are replaced with "SESSION_ID_REMOVED" in debug logs.

SFDOInsightsDataIntegrityUser
Provides a license to Salesforce.org Insights Platform Data Integrity managed package. You can then install the package in the scratch
org.

SharedActivities
Allow users to relate multiple contacts to tasks and events.

Sites
Enables Salesforce Sites, which allows you to create public websites and applications that are directly integrated with your Salesforce
org. Users aren’t required to log in with a username and password.

SocialCustomerService
Enables Social Customer Service, sets post defaults, and either activates the Starter Pack or signs into your Social Studio account.

StateAndCountryPicklist
Enables state and country/territory picklists. State and country/territory picklists let users select states and countries from predefined,
standardized lists, instead of entering state, country, and territory data into text fields.

StreamingAPI
Enables Streaming API.

StreamingEventsPerDay:<value>
Increases the maximum number of delivered PushTopic event notifications within a 24-hour period, shared by all CometD clients
(API version 36.0 and earlier). Indicate a value between 10,000–50,000.

SubPerStreamingChannel:<value>
Increases the maximum number of concurrent clients (subscribers) per generic streaming channel (API version 36.0 and earlier).
Indicate a value between 20–4,000.

SubPerStreamingTopic:<value>
Increases the maximum number of concurrent clients (subscribers) per PushTopic streaming channel (API version 36.0 and earlier).
Indicate a value between 20–4,000.

SurveyAdvancedFeatures
Enables a license for the features available with the Salesforce Feedback Management - Growth license.


Scratch Orgs Scratch Org Features

SustainabilityCloud
Provides the permission set licenses and permission sets required to install and configure Sustainability Cloud. To enable or use CRM
Analytics and CRM Analytics templates, include the DevelopmentWave scratch org feature.

SustainabilityApp
Provides the permission set licenses and permission sets required to configure Net Zero Cloud. To enable or use Tableau CRM and
Tableau CRM templates, include the DevelopmentWave scratch org feature.

TalentRecruitmentManagement
Enables the objects, features, and permissions for managing the talent recruitment and hiring process in Public Sector Solutions.

TCRMforSustainability
Enables all permissions required to manage the Net Zero Analytics app by enabling Tableau CRM. You can create and share the
analytics app for your users to bring your environmental accounting in line with your financial accounting.

TimelineConditionsLimit
Limits the number of timeline record display conditions per event type to 3.

TimelineEventLimit
Limits the number of event types displayed on a timeline to 5.

TimelineRecordTypeLimit
Limits the number of related object record types per event type to 3.

TimeSheetTemplateSettings
Time Sheet Templates let you configure settings to create time sheets automatically. For example, you can create a template that
sets start and end dates. Assign templates to user profiles so that time sheets are created for the right users.

TransactionFinalizers
Enables you to implement and attach Apex Finalizers to Queueable Apex jobs.

UsageManagement
Enables Usage Management. Using Usage Management, you can setup, track, and manage the consumption of usage-based products.

VolunteerManagement
Gives users access to Volunteer Management features and objects in Salesforce.

WaveMaxCurrency
Increases the maximum number of supported currencies for CRM Analytics. Indicate a value between 1–5.

WavePlatform
Enables the Wave Platform license.

Workflow
Enables Workflow so you can automate standard internal procedures and processes.

WorkflowFlowActionFeature
Allows you to launch a flow from a workflow action.

WorkplaceCommandCenterUser
Enables access to Workplace Command Center features including access to objects such as Employee, Crisis, and
EmployeeCrisisAssessment.

WorkThanksPref
Enables the give thanks feature in Chatter.


Scratch Orgs Scratch Org Features

#### AccountInspection

Enables the Account Intelligence view. The Account Intelligence view is a consolidated dashboard showing account metrics, activities,
and related opportunities and cases.

#### AccountingSubledgerGrowthEdition

Provides three permission sets that enable access to Accounting Subledger Growth features.

More Information

Requires that you also include the DataProcessingEngine scratch org feature in your scratch org definition file. Requires that you enable
[Data Pipelines. Requires configuration using the Setup menu in the scratch org. See Accounting Subledger in Salesforce Help.](https://help.salesforce.com/s/articleView?id=sfdo.Accounting_Subledger.htm&language=en_US)

#### AccountingSubledgerStarterEdition

Provides three permission sets that enable access to Accounting Subledger Starter features.

More Information

Requires that you also include the DataProcessingEngine scratch org feature in your scratch org definition file. Requires that you enable
[Data Pipelines. Requires configuration using the Setup menu in the scratch org. See Accounting Subledger in Salesforce Help.](https://help.salesforce.com/s/articleView?id=sfdo.Accounting_Subledger.htm&language=en_US)

#### AccountingSubledgerUser

Enables organization-wide access to Accounting Subledger Growth features when the package is installed.

More Information

Requires that you install the Accounting Subledger or Accounting Subledger for Industries managed package. If you install the Accounting
[Subledger package, also set up the Opportunity object. See Accounting Subledger Legacy Documentation in Salesforce Help.](https://sfdo-docs.s3.us-west-2.amazonaws.com/Accounting_Subledger_Legacy_Documentation.pdf)

#### AddCustomApps:<value>

Increases the maximum number of custom apps allowed in an org. Indicate a value from 1–30.

Supported Quantities

1–30, Multiplier: 1

#### AddCustomObjects:<value>

Increases the maximum number of custom objects allowed in the org. Indicate a value from 1–30.

Supported Quantities

1–30, Multiplier: 1


Scratch Orgs Scratch Org Features

#### AddCustomRelationships:<value>

Increases the maximum number of custom relationships allowed on an object. Indicate a value from 1–10.

Supported Quantities

1–10, Multiplier: 5

#### AddCustomTabs:<value>

Increases the maximum number of custom tabs allowed in an org. Indicate a value from 1–30.

Supported Quantities

1–30, Multiplier: 1

#### AddDataComCRMRecordCredit:<value>

Increases record import credits assigned to a user in your scratch org. Indicate a value from 1–30.

Supported Quantities

1–30, Multiplier: 1

#### AddInsightsQueryLimit:<value>

Increases the size of your CRM Analytics query results. Indicate a value from 1–30 (multiplier is 10). Setting the quantity to 6 increases
the query results to 60.

Supported Quantities

1–30, Multiplier: 10

#### AdditionalFieldHistory:<value>

Increases the number of fields you can track history for beyond the default, which is 20 fields. Indicate a value between 1–40.

Supported Quantities

1–40, Multiplier: 1

More Information

Previous name: AddHistoryFieldsPerEntity.

#### AdmissionsConnectUser

Enables the Admissions Connect components. Without this scratch org feature parameter, the custom Admissions Connect components
render as blank.


Scratch Orgs Scratch Org Features

Scratch Org Definition File

Add these options to your scratch org definition file:

```
   {

     "orgName": "Omega - Dev Org",

     "edition": "Partner Developer",

     "hasSampleData": "true",

     "features": [

      "DevelopmentWave",

      "AdmissionsConnectUser",

      "Communities",

      "OmniStudioDesigner",

      "OmniStudioRuntime"

     ],

     "settings": {

       "lightningExperienceSettings": {

         "enableS1DesktopEnabled": true

       },

       "chatterSettings": {

         "enableChatter": true

       },

       "languageSettings": {

         "enableTranslationWorkbench": true

       },

       "enhancedNotesSettings": {

         "enableEnhancedNotes": true

       },

       "pathAssistantSettings": {

         "pathAssistantEnabled": true

       },

       "securitySettings": {

         "enableAdminLoginAsAnyUser":true

       },

       "userEngagementSettings": {

         "enableOrchestrationInSandbox": true,

         "enableOrgUserAssistEnabled": true,

         "enableShowSalesforceUserAssist": false

       },

       "experienceBundleSettings": {

         "enableExperienceBundleMetadata": true

       },

       "communitiesSettings": {

         "enableNetworksEnabled": true,

         "enableOotbProfExtUserOpsEnable": true

       },

       "mobileSettings": {

         "enableS1EncryptedStoragePref2": false

       }

     }

   }

```


Scratch Orgs Scratch Org Features

More Information

[Next, install the Admissions Connect package in the scratch org. For installation instructions, see Install Admissions Connect in Salesforce](https://help.salesforce.com/s/articleView?id=sfdo.AC_Install.htm&language=en_US)
Help.

#### AdvisorLinkFeature

Enables the Student Success Hub components. Without this scratch org feature parameter, the custom Student Success Hub components
render as blank.

Scratch Org Definition File

Add these options to your scratch org definition file:

```
   {

     "edition": "Partner Developer",

     "features": [

      "Communities",

      "FeatureParameterLicensing",

      "AdvisorLinkFeature"

     ],

     "orgName": "SAL - Dev Workspace",

     "hasSampleData": "true",

     "settings": {

      "chatterSettings": {

       "enableChatter": true

      },

      "communitiesSettings": {

       "enableNetworksEnabled": true,

       "enableOotbProfExtUserOpsEnable": true

      },

      "enhancedNotesSettings": {

       "enableEnhancedNotes": true

      },

      "experienceBundleSettings": {

       "enableExperienceBundleMetadata": true

      },

      "lightningExperienceSettings": {

       "enableS1DesktopEnabled": true

      },

      "mobileSettings": {

       "enableS1EncryptedStoragePref2": false

      },

      "languageSettings": {

       "enableTranslationWorkbench": true

      },

      "securitySettings": {

       "enableAdminLoginAsAnyUser": true

      }

     }

   }

```


Scratch Orgs Scratch Org Features

More Information

[Next, install the Student Success Hub package in the scratch org. For setup instructions, see Install Student Success Hub in Salesforce](https://help.salesforce.com/s/articleView?id=sfdo.SSH_Install.htm&language=en_US)
Help.

#### AdvisorLinkPathwaysFeature

Enables the Pathways components. Without this scratch org feature parameter, the custom Pathways components render as blank.

Scratch Org Definition File

Add these options to your scratch org definition file:

```
   {

     "orgName": "Pathways - Dev Org",

     "edition": "Partner Developer",

     "features": [

      "Communities",

      "FeatureParameterLicensing",

      "AdvisorLinkFeature",

      "AdvisorLinkPathwaysFeature"

     ],

     "settings": {

      "chatterSettings": {

       "enableChatter": true

      },

      "enhancedNotesSettings": {

       "enableEnhancedNotes": true

      },

      "communitiesSettings": {

       "enableNetworksEnabled": true

      },

      "languageSettings": {

       "enableTranslationWorkbench": true

      },

      "lightningExperienceSettings": {

       "enableS1DesktopEnabled": true

      },

      "mobileSettings": {

       "enableS1EncryptedStoragePref2": false

      }

     }

   }

```

More Information

[Next, install the Pathways package in the scratch org. For setup instructions, see Set Up Pathways in Salesforce Help.](https://help.salesforce.com/s/articleView?id=sfdo.ssh_setup_pathways.htm&language=en_US)

#### AgentforceVibesUnmeteredAccess

Provides unmetered access to Agentforce Vibes with included AI models for standard prompting and development workflows. Enables
teams to build, iterate, and experiment with AI-assisted experiences without per-interaction credit consumption.


Scratch Orgs Scratch Org Features

Sample Scratch Org Definition File

```
   {

           "orgName": "My Scratch Org",

           "edition": "Enterprise",

           "features": ["AgentforceVibesUnmeteredAccess"]

           }

   }

```

More Information

[This feature is available from the Summer 26 release. See Unmetered Platform Developer and Admin AI User Permission Set License in](https://help.salesforce.com/platform.users_license_types_psl_unmetered.htm&type=5)
Salesforce Help for more information.

#### AIAttribution

Provides access to Einstein Attribution for Marketing Cloud Account Engagement. Einstein Attribution uses AI modeling to dynamically
assign attribution percentages to multiple campaign touchpoints.

Sample Scratch Org Definition File

Before enabling Einstein Attribution, make sure that `enableAIAttribution` and `enableCampaignInfluence2` are set
to `true` .

```
   {

     "orgName": "NTOutfitters",

     "edition": "Enterprise",

     "features": ["AIAttribution"],

     "settings": {

      "campaignSettings": {

        "enableAIAttribution": true

        "enableCampaignInfluence2": true

      }

   }

```

More Information

This feature is available in Account Engagement Advanced and Premium editions.

Optional configuration steps are accessible in Setup in the scratch org. For more information, see _Salesforce Help_ [: Einstein Attribution.](https://help.salesforce.com/s/articleView?id=mktg.pardot_einstein_attribution_parent.htm&type=5&language=en_US)

#### AllUserIdServiceAccess

Enables all users to access all users’ information via the user ID service.

More Information

The AllUserIdServiceAccess permission is off by default for all new and existing orgs. To turn on this feature, contact Salesforce Customer
Support.


Scratch Orgs Scratch Org Features

#### AnalyticsAdminPerms

Enables all permissions required to administer the CRM Analytics platform, including permissions to enable creating CRM Analytics
templated apps and CRM Analytics Apps.

More Information

[See Set Up the CRM Analytics Platform in Salesforce Help for more information.](https://help.salesforce.com/articleView?id=bi_help_setup.htm&type=5&language=en_US)

#### AnalyticsAppEmbedded

Provides one CRM Analytics Embedded App license for the CRM Analytics platform.

#### ApexGuruCodeAnalyzer

Enables ApexGuru's generative AI-powered runtime insights in Salesforce Code Analyzer, which delivers Apex code quality
recommendations directly in developer IDEs.

More Information

To improve developer accuracy and speed, use ApexGuru in Salesforce Code Analyzer to detect antipatterns using both static analysis
and generative AI.

[For more information about ApexGuru, see ApexGuru Insights in Salesforce Help.](https://help.salesforce.com/s/articleView?id=xcloud.apexguru_overview.htm&type=5&language=en_US)

#### ApexIntegrationTests (Developer Preview)

Enables you to run end-to-end Apex tests that make callouts to Agentforce and Data 360. Integration tests relax callout restrictions and
transaction rollback semantics, so you can validate real service interactions and assert on actual side effects in your scratch org, without
mock callouts.

More Information

Note: ApexIntegrationTests is available as a developer preview. ApexIntegrationTests isn’t generally available unless or until
Salesforce announces its general availability in documentation or in press releases or public statements. All commands, parameters,
and other features are subject to change or deprecation at any time, with or without notice. Don't implement functionality in
production with these commands or tools.

[See Apex Integration Tests for Agentforce and Data 360 Services (Developer Preview) in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_testing_integration_testing.htm) _Apex Developer Guide_ .

Scratch Org Definition File

To enable ApexIntegrationTests, add these settings to your scratch org definition file.

```
   {

      "orgName": "<Org Name>",

      "edition": "Developer",

      "features": [

        "ApexIntegrationTests"

      ]

   }

```


Scratch Orgs Scratch Org Features

#### API

Even in the editions (Professional, Group) that don’t provide API access, REST API is enabled by default. Use this scratch org feature to
access additional APIs (SOAP, Streaming, Bulk, Bulk 2.0).

More Information

[See Salesforce editions with API access for more information.](https://help.salesforce.com/articleView?id=000326486&type=1&mode=1&language=en_US)

#### ArcGraphCommunity

Lets you add Actionable Relationship Center (ARC) components to Experience Cloud pages so your users can view ARC Relationship
Graphs.

More Information

Provides 1 seat of the FinancialServicesEALoginAddon add-on license.

[Requires that you install Financial Services Cloud. See Customize Experience Cloud Templates using ARC Components in Financial Services](https://developer.salesforce.com/docs/atlas.en-us.262.0.financial_services_cloud_admin_guide.meta/financial_services_cloud_admin_guide/fsc_admin_arc_experience_cloud.htm)
Cloud Administrator Guide.

#### Assessments

Enables dynamic Assessments features, which enables both Assessment Questions and Assessment Question Sets.

More Information

Add these options to your scratch org feature definition file. For "edition," you can indicate any of the supported scratch org feature
editions.

```
   {

     "orgName": "Sample Org",

     "edition": "Developer",

     "features": ["Assessments"],

     "settings": {

      "industriesSettings": {

       "enableIndustriesAssessment": true,

       "enableDiscoveryFrameworkMetadata": true

      }

     }

   }

```

[Add the Assessment to the page layout. See Page Layouts in Salesforce Help for more information.](https://help.salesforce.com/s/articleView?id=platform.customize_layout.htm&type=5&language=en_US)

#### AssetScheduling:<value>

Enables Asset Scheduling license. Asset Scheduling makes it easier to book rooms and equipments. Indicate a value between 1–10.

Supported Quantities

1–10


Scratch Orgs Scratch Org Features

More Information

[See Enable Asset Scheduling in Salesforce Scheduler in Salesforce Help for more information.](https://help.salesforce.com/articleView?id=ls_overview.htm&type=5;&language=en_US)

#### AssociationEngine

Enables the Association Engine, which automatically associates new accounts with the user’s current branch by creating branch unit
customer records.

More Information

Provides 11 seats of the FSCComprehensivePsl user license and 11 seats of the FSCComprehensiveAddOn add-on license.

[Requires that you install Financial Services Cloud. See AssociationEngineSettings in Metadata API Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_associationenginesettings.htm)

#### AuthorApex

Enables you to access and modify Apex code in a scratch org. Enabled by default in Enterprise and Developer Editions.

More Information

For Group and Professional Edition orgs, this feature is disabled by default. Enabling the AuthorApex feature lets you edit and test your
Apex classes.

#### B2BCommerce

Provides the B2B License. B2BCommerce enables business-to-business (B2B) commerce in your org. Create and update B2B stores. Create
and manage buyer accounts. Sell products to other businesses.

More Information

Requires that you also include the Communities scratch org feature in your scratch org definition file to create a store using B2B Commerce.
Not available in Professional, Partner Professional, Group, or Partner Group Edition orgs.

#### B2BLoyaltyManagement

Enables the B2B Loyalty Management license. Create loyalty programs and set up loyalty program-specific processes that allow you to
recognize, rewards, and retain customers.

More Information

[See Loyalty Management in Salesforce Help for more information.](https://help.salesforce.com/s/articleView?id=xcloud.loyaltyoverview.htm&type=5&language=en_US)

#### B2CCommerceGMV

Provides the B2B2C Commerce License. B2B2C Commerce allows you to quickly stand up an ecommerce site to promote brands and
sell products into multiple digital channels. You can create and update retail storefronts in your org, and create and manage person
accounts.


Scratch Orgs Scratch Org Features

More Information

Also requires the Communities feature in your scratch org definition file.

Not available in Professional, Partner Professional, Group, or Partner Group Edition orgs.

[For more information, see Salesforce Help at Salesforce B2B Commerce and B2B2C Commerce..](https://help.salesforce.com/s/articleView?id=commerce.comm_intro.htm&type=5&language=en_US)

#### B2CLoyaltyManagement

Enables the Loyalty Management - Growth license. Create loyalty programs and set up loyalty program-specific processes that allow
you to recognize, rewards, and retain customers.

More Information

[See Loyalty Management in Salesforce Help for more information.](https://help.salesforce.com/s/articleView?id=xcloud.loyaltyoverview.htm&type=5&language=en_US)

#### B2CLoyaltyManagementPlus

Enables the Loyalty Management - Advanced license. Create loyalty programs and set up loyalty program-specific processes that allow
you to recognize, rewards, and retain customers.

More Information

[See Loyalty Management in Salesforce Help for more information.](https://help.salesforce.com/s/articleView?id=xcloud.loyaltyoverview.htm&type=5&language=en_US)

#### BatchManagement

Enables the Batch Management license. Batch Management allows you to process a high volume of records in manageable batches.

More Information

[See Batch Management in Salesforce Help for more information.](https://help.salesforce.com/s/articleView?id=ind.concept_batch_management.htm&type=5&language=en_US)

#### BenefitManagement

Enables the objects, features, and permissions for managing benefits programs, benefit disbursements, and benefit applicant tracking
in Public Sector Solutions.

Sample Scratch Org Definition File

To enable BenefitManagement, add these features and settings to your scratch org definition file.

```
   {

      "orgName": "BM Org",

      "edition": "Developer",

      "features": ["BenefitManagement:2"],

      "settings": {

      "lightningExperienceSettings": {

      "enableS1DesktopEnabled": true

      },

      "mobileSettings": {

```


Scratch Orgs Scratch Org Features

```
      "enableS1EncryptedStoragePref2": false

      },

      "IndustriesSettings": {

      "enableIndustriesAssessment": true,

      "enableDiscoveryFrameworkMetadata": true,

      "enableInteractionSummaryPref": true,

      "enableBenefitManagementPreference": true,

      "enableGroupMembershipPref": true,

      "enableCaseReferralPref": true

      },

      "OmniStudioSettings": {

      "enableOmniStudioMetadata": false

      },

      "DocumentChecklistSettings": {

      "deleteDCIWithFiles": true

      }

      }

      }

#### BigObjectsBulkAPI

```

Enables the scratch org to use BigObjects in the Bulk API.

More Information

[See Big Objects Implementation Guide for more information.](https://developer.salesforce.com/docs/atlas.en-us.262.0.bigobjects.meta/bigobjects/big_object.htm)

#### BillingAdvanced

Enables access to all the Billing features and objects that are available with the Revenue Cloud Billing license in the scratch org.

More Information

**•** Available in Enterprise, Unlimited, and Developer Edition scratch orgs.

**•** Provides 10 seats of BillingAdvancedAddOn add-on licenses.

**•** [Enable Billing in Revenue Cloud and turn on Billing settings.](https://help.salesforce.com/s/articleView?id=ind.billing_setup_enable.htm&type=5&language=en_US)

**•** [Provides permission sets to access Billing features.](https://help.salesforce.com/s/articleView?id=ind.billing_permission_sets.htm&type=5&language=en_US)

**•** [See Manage Billing in Revenue Cloud for more information.](https://help.salesforce.com/s/articleView?id=ind.billing.htm&type=5&language=en_US)

Scratch Org Definition File

To enable BillingAdvanced, add these settings to your scratch org definition file.

```
   {

     "orgName": "<Org Name>",

     "adminEmail":"<Admin Email Address>"

     "edition": "<Edition Name>",

     "features": [

      "InvoiceManagement",

      "BillingAdvanced",

      "EnableSetPasswordInApi"

```


Scratch Orgs Scratch Org Features

```
     ],

     "settings": {

      "billingSettings": {

       "enableBillingSetup": true

      },

     "lightningExperienceSettings": {

        "enableS1DesktopEnabled": true

       }

     }

   }

#### Briefcase

```

Enables the use of Briefcase Builder in a scratch org, which allows you to create offline briefcases that make selected records available
for viewing offline.

#### BudgetManagement

Gives users access to budget management features and objects. To enable budget management, add this feature to your scratch org
definition file.

More Information

[See Budget Management in Salesforce Help for more information.](https://help.salesforce.com/s/articleView?id=ind.grmk_budget_management_for_grantmaking.htm&type=5&language=en_US)

#### BusinessRulesEngine

Enables Business Rules Engine, which enables both expression sets and lookup tables.

More Information

[Provides 10 Business Rules Engine Designer and 10 Business Rules Engine Runtime licenses. For more information, see Business Rules](https://help.salesforce.com/s/articleView?id=ind.business_rules_engine.htm&type=5&language=en_US)
[Engine in Salesforce Help.](https://help.salesforce.com/s/articleView?id=ind.business_rules_engine.htm&type=5&language=en_US)

#### BYOCCaaS

Enables you to set up and test a partner contact center that integrates with supported Contact Center as a Service (CCaaS) providers in
your scratch org.

More Information

This feature requires that you also include the `ServiceCloud` and `Scrt2Conversation` scratch org features in your scratch
org definition file. You must also enable second-generation managed packaging to use this feature in a scratch org. Available in Salesforce
Enterprise and Developer Editions.

[For setup and configuration steps, see Bring Your Own Channel for CCaaS in Salesforce Help.](https://help.salesforce.com/articleView?id=service.byoc_ccaas_setup.htm&type=5&language=en_US)


Scratch Orgs Scratch Org Features

Sample Scratch Org Definition File

```
   {

     "orgName": "BYO CCaaS Scratch Org",

     "edition": "Developer",

     "features": ["ServiceCloud", "Scrt2Conversation", "BYOCCaaS"

     "settings": {

      "lightningExperienceSettings": {

       "enableS1DesktopEnabled": true

      },

     "mobileSettings": {

       "enableS1EncryptedStoragePref2": false

      }

     }

   }

#### BYOOTT

```

Enables you to set up and test a Bring Your Own Channel for Messaging channel that integrates with supported Messaging providers
in your scratch org.

More Information

This feature requires that you also include the `ServiceCloud` and `Scrt2Conversation` scratch org features in your scratch
org definition file. You must also enable second-generation managed packaging to use this feature in a scratch org. Available in Salesforce
Enterprise and Developer Editions.

[For setup and configuration steps, see Bring Your Own Channel in Salesforce Help.](https://help.salesforce.com/articleView?id=service.partner_messaging_intro.htm&type=5&language=en_US)

Sample Scratch Org Definition File

```
   {

     "orgName": "BYOC Scratch Org",

     "edition": "Developer",

     "features": ["ServiceCloud", "Scrt2Conversation", "BYOOTT"

     "settings": {

      "lightningExperienceSettings": {

       "enableS1DesktopEnabled": true

      },

     "mobileSettings": {

       "enableS1EncryptedStoragePref2": false

      }

     }

   }

#### CacheOnlyKeys

```

Enables the cache-only keys service. This feature allows you to store your key material outside of Salesforce, and have the Cache-Only
Key Service fetch your key on demand from a key service that you control.


Scratch Orgs Scratch Org Features

More Information

[Requires enabling PlatformEncryption and configuration using the Setup menu in the scratch org. See Which User Permissions Does](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_scratch_orgs_def_file_config_values.htm#so_platformencryption)
[Shield Platform Encryption Require?, Generate a Tenant Secret with Salesforce, and Cache-Only Key Service in Salesforce Help.](https://help.salesforce.com/articleView?id=security_pe_permissions.htm&language=en_US)

#### CalloutSizeMB:<value>

Increases the maximum size of an Apex callout. Indicate a value between 3–12.

Supported Quantities

3–12, Multiplier: 1

#### CampaignInfluence2

Provides access to Customizable Campaign Influence for Sales Cloud and Marketing Cloud Account Engagement. Customizable Campaign
Influence can auto-associate or allow manual creation of relationships among campaigns and opportunities to track attribution.

Sample Scratch Org Definition File

To enable Customizable Campaign Influence, set `enableCampaignInfluence2` to `true` .

```
   {

     "orgName": "NTOutfitters",

     "edition": "Enterprise",

     "features": ["CampaignInfluence2"],

     "settings": {

      "campaignSettings": {

        "enableCampaignInfluence2": true

      }

   }

```

More Information

This feature is available in Salesforce Enterprise, Performance, Unlimited, and Developer Editions.

Optional configuration steps are accessible in Setup in the scratch org. For more information, see _Salesforce Help_ [: Customizable Campaign](https://help.salesforce.com/s/articleView?id=sales.campaigns_influence_customizable.htm&type=5&language=en_US)
[Influence.](https://help.salesforce.com/s/articleView?id=sales.campaigns_influence_customizable.htm&type=5&language=en_US)

#### CascadeDelete

Provides lookup relationships with the same cascading delete functionality previously only available to master-detail relationships. To
prevent records from being accidentally deleted, cascade-delete is disabled by default.

#### CaseClassification

Enables Einstein Case Classification. Case Classification offers recommendations to your agents so they can select the best value. You
can also automatically save the best recommendation and route the case to the right agent.


Scratch Orgs Scratch Org Features

#### CaseWrapUp

Enables Einstein Case Wrap-Up. To help agents complete cases quickly, Einstein Case Wrap-Up recommends case field values based on
past chat transcripts.

More Information

Available in Enterprise Edition scratch orgs.

Requires configuration using the Setup menu in the scratch org.

[See Set Up Einstein Classification Apps in Salesforce Help for more information.](https://help.salesforce.com/articleView?id=cc_service_what_is.htm&language=en_US)

#### CGAnalytics

Enables the Consumer Goods Analytics org perm in scratch orgs.

More Information

Provides 1 seat of the CGAnalyticsPlus add-on license.

#### ChangeDataCapture

Enables Change Data Capture, if the scratch org edition doesn't automatically enable it.

#### Chatbot

Enables deployment of Bot metadata into a scratch org, and allows you to create and edit bots.

More Information

To use this feature, turn on **Enable Einstein Features** in the Dev Hub org to accept the Terms of Service.

[See Einstein Bots in Salesforce Help for more information.](https://help.salesforce.com/articleView?id=bots_service_intro.htm&type=5&language=en_US)

#### ChatterEmailFooterLogo ChatterEmailFooterLogo allows you to use the Document ID of a logo image, which you can use to customize chatter emails.

More Information

[See Add Your Custom Brand to Email Notifications in Salesforce Help for more information.](https://help.salesforce.com/s/articleView?id=experience.collab_admin_email_customize.htm&type=5&language=en_US)

#### ChatterEmailFooterText ChatterEmailFooterText allows you to use footer text in customized Chatter emails.

More Information

[See Add Your Custom Brand to Email Notifications in Salesforce Help for more information.](https://help.salesforce.com/s/articleView?id=experience.collab_admin_email_customize.htm&type=5&language=en_US)


Scratch Orgs Scratch Org Features

#### ChatterEmailSenderName ChatterEmailSenderName allows you to customize the name that appears as the sender’s name in the email notification. For example,

your company’s name.

More Information

[See Chatter Email Settings and Branding in Salesforce Help for more information.](https://help.salesforce.com/s/articleView?id=experience.collab_admin_email_settings.htm&type=5&language=en_US)

#### CloneApplication CloneApplication allows you to clone an existing custom Lightning app and make required customizations to the new app. This way,

you don’t have to start from scratch, especially when you want to create apps with simple variations.

More Information

[See Create Lightning Apps in Salesforce Help for more information.](https://help.salesforce.com/s/articleView?id=platform.apps_lightning_create.htm.htm&type=5&language=en_US)

#### CMSMaxContType

Limits the number of distinct content types you can create within Salesforce CMS to 21.

#### CMSMaxNodesPerContType

Limits the maximum number of child nodes (fields) you can create for a particular content type to 15.

#### CMSUnlimitedUse

Enables unlimited content records, content types, and bandwidth usage in Salesforce CMS.

#### Communities

Allows the org to create an Experience Cloud site. Experience Cloud uses the term Communities in its configuration. To use Communities,
you must also include communitiesSettings > enableNetworksEnabled in the settings section of your scratch org definition file.

More Information

Available in Enterprise and Developer Edition scratch orgs.

#### CompareReportsOrgPerm

Enables the org permission to allow for comparison of Lightning Reports.

#### ConAppPluginExecuteAsUser

Enables the pluginExecutionUser field in the ConnectedApp Metadata API object.


Scratch Orgs Scratch Org Features

#### ConcStreamingClients:<value>

Increases the maximum number of concurrent clients (subscribers) across all channels and for all event types for API version 36.0 and
earlier. Indicate a value between 20–4,000.

Supported Quantities

20–4,000, Multiplier: 1

#### ConnectedAppCustomNotifSubscription

Enables connected apps to subscribe to custom notification types, which are used to send custom desktop and mobile notifications.

More Information

Sending custom notifications requires both CustomNotificationType to create notification types and
#### ConnectedAppCustomNotifSubscription to subscribe to notification types. See Manage Your Notifications with Notification Builder in

Salesforce Help for more information on custom notifications.

#### ConnectedAppToolingAPI

Enables the use of connected apps with the Tooling API.

#### ConsentEventStream

Enables the Consent Event Stream permission for the org.

More Information

[See Use the Consent Event Stream in Salesforce Help for more information.](https://help.salesforce.com/s/articleView?id=xcloud.consent_event_stream.htm&type=5&language=en_US)

#### ConsolePersistenceInterval:<value>

Increases how often console data is saved, in minutes. Indicate a value between 0–500. To disable auto save, set the value to 0.

Supported Quantities

0–500, Multiplier: 1

#### ContactsToMultipleAccounts

Enables the contacts to multiple accounts feature. This feature lets you relate a contact to two or more accounts.

#### ContractApprovals

Enables contract approvals, which allow you to track contracts through an approval process.


Scratch Orgs Scratch Org Features

#### ContractManagement

Enables the Contract Lifecycle (CLM) Management features in the org.

#### ContractMgmtInd

Enables the Contract Lifecycle Management (CLM) features for Industries.

#### CoreCpq

Enables read-write access to Revenue Cloud features and objects. To use Revenue Cloud, you must also include
revenueManagementSettings > enableCoreCPQ in the settings section of your scratch org definition file.

More Information

**•** Available in Developer and Enterprise scratch org editions.

**•** Provides 10 RevenueLifecycleManagementAddOn add-on licenses.

**•** Provides permission sets for Context Service, Business Rules Engine, Document Generation, Omnistudio, Data Processing Engine,
Product Catalog Management, Salesforce Pricing, Product Configurator, Transaction Management, Salesforce Contracts, Rate
Management, Dynamic Revenue Orchestrator, and Billing.

**•** Displays the setup pages for Context Service, Business Rules Engine, Document Generation, Omnistudio, Data Processing Engine,
Product Catalog Management, Salesforce Pricing, Revenue Settings (Product Configurator and Transaction Management), Contracts,
Rate Management, Dynamic Revenue Orchestrator, and Billing.

**•** [Requires configuration using the Setup menu in the scratch org. See Revenue Cloud.](https://help.salesforce.com/s/articleView?id=ind.revenue_lifecycle_management.htm&type=5&language=en_US)

Scratch Org Definition File

Add these options to your scratch org definition file.

```
   {

   "edition": "Enterprise",

   "features": [

   "BusinessRulesEngine",

   "Communities",

   "OrderSaveLogicEnabled",

   "OrderManagement",

   "OrderSaveBehaviorBoth",

   "PartnerCommunity",

   “CustomerCommunityPlus",

   "ContextService",

   "CoreCpq",

   "SalesforcePricing",

   "SalesforceConfiguratorEngine",

   "UsageManagement",

   "BillingAdvanced",

   "DocGen",

   "EnableSetPasswordInApi",

   "ProductCatalogManagementPCAddOn"

   ],

   "settings": {

   "communitiesSettings": {

```


Scratch Orgs Scratch Org Features

```
   "enableNetworksEnabled": true

   },

   "customAddressFieldSettings": {

   "enableCustomAddressField": true

   },

   "currencySettings": {

   "enableMultiCurrency": true

   },

   "experienceBundleSettings": {

   "enableExperienceBundleMetadata": true

   },

   "lightningExperienceSettings": {

   "enableS1DesktopEnabled": true

   },

   "industriesContextSettings": {

   "enableContextDefinitions": true

   },

   "opportunitySettings": {

   "enableOpportunityTeam": true

   },

   "revenueManagementSettings": {

   "enableCoreCPQ": true

   },

   "orderManagementSettings": {

   "enableOrderManagement": true

   },

   "orderSettings": {

   "enableOrders": true,

   "enableEnhancedCommerceOrders": true,

   "enableOrderEvents": true,

   "enableOptionalPricebook": true,

   "enableZeroQuantity": true,

   "enableNegativeQuantity": true

   },

   "quoteSettings": {

   "enableQuote": true,

   "enableQuotesWithoutOppEnabled": true

   },

   "industriesPricingSettings": {

   "enableSalesforcePricing": true

   },

   "industriesRatingSettings": {

   "enableRating": true,

   "enableRatingWaterfall": true,

   "enableRatingWaterfallPersistence": true

   },

   "DynamicFulfillmentOrchestratorSettings": {

   "enableDFOPref": true

   }

   },

     "orgName": "<your org name>",

     "adminEmail": "<your admin email>"

   }

```


Scratch Orgs Scratch Org Features

#### CPQ

Enables the licensed features required to install the Salesforce CPQ managed package but doesn't install the package automatically.

More Information

[For additional information and configuration steps, see Manage Your Quotes with CPQ in Salesforce Help.](https://help.salesforce.com/articleView?id=cpq_master.htm&type=5&language=en_US)

#### CustomerDataPlatform

Enables the CustomerDataPlatform license in scratch orgs.

Sample Scratch Org Definition File

```
   {

     "orgName": "Acme",

     "edition": "Developer",

     "features": ["CustomerDataPlatform", "CustomerDataPlatformLite"],

     "settings": {

      "customerDataPlatformSettings" : {

       "enableCustomerDataPlatform" : true

      }

     }

   }

```

More Information

To create scratch orgs that use Data Cloud, you must first log a case with [Salesforce Partner Support. This feature can be enabled on](https://partners.salesforce.com)
your Partner Business Org (PBO) only. After it’s enabled, you can create scratch orgs with Data Cloud features. .

See _Salesforce Help_ [: Feature Availability in Data Cloud and Customer Data Platform for a list of functionality available with the](https://help.salesforce.com/s/articleView?id=data.c360_a_feature_availability.htm&type=5&language=en_US)
#### CustomerDataPlatform license. CustomerDataPlatformLite

Enables the Data Cloud license in scratch orgs. You must also include the CustomerDataPlatform feature and enableCustomerDataPlatform
Metadata API setting in your scratch org definition.

Sample Scratch Org Definition File

```
   {

     "orgName": "Acme",

     "edition": "Developer",

     "features": ["CustomerDataPlatform", "CustomerDataPlatformLite"],

     "settings": {

      "customerDataPlatformSettings" : {

       "enableCustomerDataPlatform" : true

      }

     }

   }

```


Scratch Orgs Scratch Org Features

More Information

To create scratch orgs that use Data Cloud, you must first log a case with [Salesforce Partner Support. This feature can be enabled on](https://partners.salesforce.com)
your Partner Business Org (PBO) only. After it’s enabled, you can create scratch orgs with Data Cloud features.

See _Salesforce Help_ [: Feature Availability in Data Cloud and Customer Data Platform for a list of functionality available with the Data Cloud](https://help.salesforce.com/s/articleView?id=data.c360_a_feature_availability.htm&type=5&language=en_US)
license.

#### CustomerExperienceAnalytics

Enables the Customer Lifecycle Analytics org perm in scratch orgs.

More Information

Provides 1 seat of the CustomerExperienceAnalyticsPlus add-on license.

#### CustomFieldDataTranslation

Enables translation of custom field data for Work Type Group, Service Territory, and Service Resource objects. You can enable data
translation for custom fields with Text, Text Area, Text Area (Long), Text Area (Rich), and URL types.

More Information

Requires that you also include the EntityTranslation scratch org feature in your scratch org definition file. Not available in Professional,
Partner Professional, Group, or Partner Group Edition orgs.

#### CustomNotificationType

Allows the org to create custom notification types, which are used to send custom desktop and mobile notifications.

More Information

Sending custom notifications requires both CustomNotificationType to create notification types and
[ConnectedAppCustomNotifSubscription to subscribe to notification types. See Manage Your Notifications with Notification Builder in](https://help.salesforce.com/s/articleView?id=platform.notif_builder.htm&type=5&language=en_US)
Salesforce Help for more information on custom notifications.

#### DataComDnbAccounts

Provides a license to Data.com account features.

#### DataComFullClean

Provides a license to Data.com cleaning features, and allows users to turn on auto fill clean settings for jobs.

#### DataMaskUser

Provides 30 Data Mask permission set licenses. This permission set enables access to an installed Salesforce Data Mask package.


Scratch Orgs Scratch Org Features

More Information

[For additional installation and configuration steps, see Install the Managed Package in Salesforce Help.](https://help.salesforce.com/articleView?id=data_mask_install.htm&type=5&language=en_US)

#### DataProcessingEngine

Enables the Data Processing Engine license. Data Processing Engine helps transform data that's available in your Salesforce org and write
back the transformation results as new or updated records.

More Information

[See Data Processing Engine in Salesforce Help for more information.](https://help.salesforce.com/s/articleView?id=ind.dpe_intro.htm&type=5&language=en_US)

#### DebugApex

Enables Apex Interactive Debugger. You can use it to debug Apex code by setting breakpoints and checkpoints, and inspecting your
code to find bugs.

#### DecisionTable

Enables Decision Table license. Decision tables read business rules and decide the outcome for records in your Salesforce org or for the
values that you specify.

More Information

[See Decision Table in Salesforce Help for more information.](https://help.salesforce.com/s/articleView?id=concept_decision_table.htm&language=en_US)

#### DefaultWorkflowUser

Sets the scratch org admin as the default workflow user.

#### DeferSharingCalc

Allows admins to suspend group membership and sharing rule calculations and to resume them later.

More Information

[Requires configuration using the Setup menu in the scratch org. See Defer Sharing Calculations in Salesforce Help.](https://help.salesforce.com/articleView?id=security_sharing_defer_sharing_calculations.htm&type=5&language=en_US)

#### DevelopmentWave

Enables CRM Analytics development in a scratch org. It assigns five platform licenses and five CRM Analytics platform licenses to the org,
along with assigning the permission set license to the admin user. It also enables the CRM Analytics Templates and Einstein Discovery
features.

#### DeviceTrackingEnabled

Enables Device Tracking.


Scratch Orgs Scratch Org Features

#### DevOpsCenter

Enables DevOps Center in scratch orgs so that partners can create second-generation managed packages that extend or enhance the
functionality in the DevOps Center application (base) package.

Dev Hub Org

Ask a Salesforce admin to enable DevOps Center in the Dev Hub org. From Setup, enter _`DevOps Center`_ in the Quick Find box, then
select **DevOps Center** . You can create scratch orgs after the org preference is enabled.

Scratch Org Definition File

Add these options to your scratch org definition file:

```
   {

      "orgName": "Acme",

      "edition": "Enterprise",

      "features": ["DevOpsCenter"],

      "settings": {

        "devHubSettings": {

           "enableDevOpsCenterGA": true

           }

        }

      }

```

Scratch Org Definition File For Scratch Orgs Created from an Org Shape

If you create a scratch org based on an org shape with DevOps Center enabled, we still require that you add the DevOps Center feature
and setting to the scratch org definition for legal reasons as part of the DevOps Center terms and conditions.

```
   {

      "orgName": "Acme",

      "sourceOrg": "00DB1230400Ifx5",

      "features": ["DevOpsCenter"],

      "settings": {

        "devHubSettings": {

           "enableDevOpsCenterGA": true

           }

        }

      }

```

More Information

[Salesforce Help: Build an Extension Package for DevOps Center](https://help.salesforce.com/s/articleView?id=platform.devops_center_partners_extension_packages.htm&type=5&language=en_US)

#### DisableManageIdConfAPI

Limits access to the LoginIP and ClientBrowser API objects to allow view or delete only.

#### DisclosureFramework

Provides the permission set licenses and permission sets required to configure Disclosure and Compliance Hub.


Scratch Orgs Scratch Org Features

Scratch Org Definition File

Add these options to your scratch org definition file:

```
   {

     "orgName": "dch org",

     "edition": "Developer",

     "features": ["DisclosureFramework"],

     "settings": {

      "industriesSettings":{

       "enableGnrcDisclsFrmwrk": true,

       "enableIndustriesAssessment" : true

      }

     }

   }

```

More Information

[For configuration steps, see Disclosure and Compliance Hub in the Set Up and Maintain Net Zero Cloud guide in Salesforce Help.](https://help.salesforce.com/s/articleView?id=ind.netzero_setup_disclosure_and_compliance_hub.htm&type=5&language=en_US)

#### Division

Turns on the Manage Divisions feature under Company Settings. Divisions let you segment your organization's data into logical sections,
making searches, reports, and list views more meaningful to users. Divisions are useful for organizations with extremely large amounts
of data.

#### DocGen

Enables the Document Generation Feature in the Org.

#### DocGenDesigner

Enables the designers to create and configure document templates.

#### DocGenInd

Enables the Industry Document Generation features in the org.

#### DocumentChecklist

Enables Document Tracking and Approval features, and adds the Document Checklist permission set. Document tracking features let
you define documents to upload and approve, which supports processes like loan applications or action plans.

More Information

[See Enable Document Tracking and Approvals in the Financial Services Cloud Administrator Guide for more information.](https://developer.salesforce.com/docs/atlas.en-us.262.0.financial_services_cloud_admin_guide.meta/financial_services_cloud_admin_guide/admin_enable_doc_mgmt.htm)

#### DocumentReaderPageLimit

Limits the number of pages sent for data extraction to 5.


Scratch Orgs Scratch Org Features

More Information

[See Intelligent Form Reader in Salesforce Help for more information.](https://help.salesforce.com/s/articleView?id=ind.form_reader.htm&type=5&language=en_US)

#### DSARPortability

Enables an org to access the DSARPortability feature in Privacy Center. Also, provides one seat each of the PrivacyCenter and
PrivacyCenterAddOn licenses.

More Information

[See Portability in the Salesforce REST API Developer Guide for more information.](https://developer.salesforce.com/docs/atlas.en-us.242.0.api_rest.meta/api_rest/resources_portability.htm)

#### DurableClassicStreamingAPI

Enables Durable PushTopic Streaming API for API version 37.0 and later.

More Information

Available in Enterprise and Developer Edition scratch orgs.

#### DurableGenericStreamingAPI

Enables Durable Generic Streaming API for API version 37.0 and later.

More Information

Available in Enterprise and Developer Edition scratch orgs.

#### DynamicClientCreationLimit

Allows the org to register up to 100 OAuth 2.0 connected apps through the dynamic client registration endpoint.

#### EAndUDigitalSales

Enables the Energy and Utilities Digital Sales feature in the org.

#### EAndUSelfServicePortal

Enables the Self Service Portal features for Digital Experience users in the org.

#### EAOutputConnectors

Enable CRM Analytics Output Connectors.

More Information

[This scratch org requires the Dev Hub to have the EAOutputConnectors permission. See Salesforce Output Connection in Salesforce](https://help.salesforce.com/s/articleView?id=analytics.bi_integrate_connectors_output_salesforce.htm&type=5&language=en_US)
Help for more details.


Scratch Orgs Scratch Org Features

#### EASyncOut

Enable CRM Analytics SyncOut.

More Information

[This scratch org requires the Dev Hub to have the EASyncOut permission. See Sync Out for Snowflake in Salesforce Help for more details.](https://help.salesforce.com/s/articleView?id=analytics.bi_integrate_connectors_sync_out_snowflake.htm&type=5&language=en_US)

#### EdPredictionM3Threshold

Sets the number of records in the payload to 10, after which the Einstein Discovery prediction service uses M3.

#### EdPredictionTimeout

Sets the maximum duration of a single Einstein Discovery prediction to 100 milliseconds.

#### EdPredictionTimeoutBulk

Sets the maximum duration of a single Einstein Discovery prediction when it runs in bulk to 10 milliseconds.

#### EdPredictionTimeoutByomBulk

Sets the maximum duration of a single Bring Your Own Model (BYOM) Einstein Discovery prediction to 100 milliseconds.

#### EducationCloud: <value>

Enables use of Education Cloud.

Supported Quantities

Maximum: 10; Multiplier: 1

More Information

[Standard set up steps are required after enabling this feature. See Set Up Education Cloud in Salesforce Help for more information.](https://help.salesforce.com/s/articleView?id=sfdo.ec_set_up_education_cloud_2.htm&language=en_US)

#### Einstein1AIPlatform

Provides access to Einstein generative AI features such as Agentforce, Prompt Builder, Model Builder, and the Models API. To use generative
AI features, you must also include einsteinGptSettings > enableEinsteinGptPlatform in the settings section of your scratch org definition
file.

Scratch Org Definition File

Add these options to your scratch org definition file:

```
   {

     "orgName": "Agentforce scratch org",

     "edition": "Developer",

     "features": ["Einstein1AIPlatform"],

```


Scratch Orgs Scratch Org Features

```
     "settings": {

       "einsteinGptSettings": {

         "enableEinsteinGptPlatform": true

       }

     }

   }

```

Additional Configuration for Prompt Builder

After you generate the scratch org, Prompt Builder isn’t available until you assign yourself the Manage Prompts permission in the scratch
org.

When packaging a prompt template in second-generation packages, add the `EinsteinGPTPromptTemplateManager`
permission set to the `sfdx-project.json` [file. See Considerations for Packaging Prompt Templates in Salesforce Help for details.](https://help.salesforce.com/s/articleView?id=ai.prompt_builder_considerations_packaging.htm&language=en_US)

More Information

Available in Developer and Enterprise Edition scratch orgs.

Requires configuration using the Setup menu in the scratch org. Many generative AI features also require a Data Cloud license.

[See Einstein Generative AI in Salesforce Help for more information.](https://help.salesforce.com/s/articleView?id=ai.generative_ai_about.htm&type=5&language=en_US)

#### EinsteinAnalyticsPlus

Provides one CRM Analytics Plus license for the CRM Analytics platform.

#### EinsteinArticleRecommendations

Provides licenses for Einstein Article Recommendations. Einstein Article Recommendations uses data from past cases to identify Knowledge
articles that are most likely to help your customer service agents address customer inquiries.

More Information

Available in Enterprise Edition scratch orgs.

Requires configuration using the Setup menu in the scratch org.

[See Set Up Einstein Article Recommendations in Salesforce Help for more information.](https://help.salesforce.com/articleView?id=einstein_article_recommendations_set_up.htm&type=5&language=en_US)

#### EinsteinBuilderFree

Provides a license that allows admins to create one enabled prediction with Einstein Prediction Builder. Einstein Prediction Builder is
custom AI for admins

More Information

[For configuration steps, see Einstein Prediction Builder in Salesforce Help.](https://help.salesforce.com/articleView?id=custom_ai_prediction_builder.htm&type=0&language=en_US)


Scratch Orgs Scratch Org Features

#### EinsteinDocReader

Provides the license required to enable and use Intelligent Form Reader in a scratch org. Intelligent Form Reader uses optical character
recognition to automatically extract data with Amazon Textract.

More Information

To use this scratch org feature, the Dev Hub org requires the EinsteinDocReader and SalesforceManagedIFR permissions. For information
[about Intelligent Form Reader, see Intelligent Form Reader in Salesforce Help.](https://help.salesforce.com/s/articleView?id=ind.form_reader.htm&type=5&language=en_US)

#### EinsteinRecommendationBuilder

Provides a license to create recommendations with Einstein Recommendation Builder. Einstein Recommendation Builder lets you build
custom AI recommendations.

More Information

Enabled in Developer and Enterprise Editions.

Requires configuration using the Setup menu in the scratch org. You also need the EinsteinRecommendationBuilderMetadata feature
to use Einstein Recommendation Builder in scratch org.

#### EinsteinSalesRepFdbk

Enables the Agentforce Sales Coach feature in an org. This scratch org feature also includes a large number of Einstein for Sales Generative
AI features.

More Information

[The EinsteinSalesRepFdbk scratch org feature enables Agentforce for Sales standard actions, such as Create Close Plan, Get Product](https://help.salesforce.com/s/articleView?id=ai.copilot_actions_ref_close_plan.htm&language=en_US&type=5)
[Pricing, Meeting Follow-Up Email, Send Meeting Request, Identify Contact Role, Identify Key Contacts, Find Similar Opportunities, Review](https://help.salesforce.com/s/articleView?id=ai.copilot_actions_ref_get_product_pricing.htm&language=en_US&type=5)
[My Day, and Find Contact Interactions. It also enables Einstein Generative AI features, such as Sales Call Summaries, Call Explorer, Generative](https://help.salesforce.com/s/articleView?id=ai.copilot_actions_ref_review_my_day.htm&language=en_US&type=5)
[Conversation Insights, and Automatic Contact Enhancement.](https://help.salesforce.com/s/articleView?id=sales.eci_gen_insights.htm&type=5&language=en_US)

#### EinsteinSearch

Provides the license required to use and enable Einstein Search features in a scratch org.

More Information

Available in Professional and Enterprise Edition scratch orgs.

Requires configuration using the Setup menu in the scratch org.

#### EinsteinVisits

Enables Consumer Goods Cloud. With Consumer Goods cloud, transform the way you collaborate with your retail channel partners.
Empower your sales managers to plan visits and analyze your business’s health across stores. Also, allow your field reps to track inventory,
take orders, and capture visit details using the Retail Execution mobile app.


Scratch Orgs Scratch Org Features

#### EinsteinVisitsED

Enables Einstein Discovery, which can be used to get store visit recommendations. With Einstein Visits ED, you can create a visit frequency
strategy that allows Einstein to provide optimal store visit recommendations.

More Information

[See Create a Visit Frequency Next Best Action Strategy in Salesforce Help.](https://help.salesforce.com/s/articleView?id=ind.industries_einstein_visit_frequency_strategy.htm&type=5&language=en_US)

#### EmbeddedLoginForIE

Provides JavaScript files that support Embedded Login in IE11.

#### EmpPublishRateLimit:<value>

Increases the maximum number of standard-volume platform event notifications published per hour. Indicate a value between
1,000–10,000.

Supported Quantities

1,000–10,000, Multiplier: 1

#### EnablePRM

Enables the partner relationship management permissions for the org.

#### EnableManageIdConfUI

Enables access to the LoginIP and ClientBrowser API objects to verify a user's identity in the UI.

#### Enablement

Enables features for creating, taking, and tracking sales programs with Enablement. Business operations experts and sales leaders identify
the revenue outcomes they want sales reps to achieve, such as increased average deal sizes or shorter ramp times. Then, they create
programs that help sales reps work towards those outcomes as part of their daily work.

More Information

**•** Provides 5 Enablement add-on licenses, where each license provides 1 seat of the Enablement permission set license and 1 seat of
the Enablement Resources permission set license.

**•** Provides permission set groups, permission sets, and user permissions for managing and accessing sales programs data.

**•** Provides access to the Enablement Settings page in Setup, which provides guidance for assigning permissions and includes other
optional configuration settings.

[See Sales Programs and Partner Tracks with Enablement in Salesforce Help and see the Sales Programs and Partner Tracks with Enablement](https://help.salesforce.com/s/articleView?id=sales.enablement.htm&type=5&language=en_US)
[Developer Guide for more information.](https://developer.salesforce.com/docs/sales/enablement/overview)


Scratch Orgs Scratch Org Features

#### EnableSetPasswordInApi

Enables you to use `sf org generate password` to change a password without providing the old password.

#### EncryptionStatisticsInterval:<value>

Defines the interval (in seconds) between encryption statistics gathering processes. The maximum value is 604,800 seconds (7 days).
The default is once per 86,400 seconds (24 hours).

Supported Quantities

0–60,4800, Multiplier: 1

More Information

[Requires enabling PlatformEncryption and some configuration using the Setup menu in the scratch org. See Which User Permissions](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_scratch_orgs_def_file_config_values.htm#so_platformencryption)
[Does Shield Platform Encryption Require?, and Generate a Tenant Secret with Salesforce in Salesforce Help.](https://help.salesforce.com/articleView?id=security_pe_permissions.htm&language=en_US)

#### EncryptionSyncInterval:<value>

Defines how frequently (in seconds) the org can synchronize data with the active key material. The default and maximum value is 604,800
seconds (7 days). To synchronize data more frequently, indicate a value, in seconds, equal to or larger than 0.

Supported Quantities

0–604,800, Multiplier: 1

More Information

[Requires enabling PlatformEncryption and some configuration using the Setup menu in the scratch org. See Which User Permissions](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_scratch_orgs_def_file_config_values.htm#so_platformencryption)
[Does Shield Platform Encryption Require?, and Generate a Tenant Secret with Salesforce in Salesforce Help.](https://help.salesforce.com/articleView?id=security_pe_permissions.htm&language=en_US)

#### EnergyAndUtilitiesCloud

Enables the Energy and Utilities Cloud features in the org.

#### Entitlements

Enables entitlements. Entitlements are units of customer support in Salesforce, such as phone support or web support that represent
terms in service agreements.

#### ERMAnalytics

Enables the ERM Analytics org perm in your scratch org.

More Information

Provides 1 seat of the ERMAnalyticsPlus add-on license.


Scratch Orgs Scratch Org Features

#### EventLogFile

Enables API access to your org's event log files. The event log files contain information about your org’s operational events that you can
use to analyze usage trends and user behavior.

#### EntityTranslation

Enables translation of field data for Work Type Group, Service Territory, and Service Resource objects.

More Information

To translate custom field data, also include the CustomFieldDataTranslation scratch org feature in your scratch org definition file. Not
available in Professional, Partner Professional, Group, or Partner Group Edition orgs.

#### ExcludeSAMLSessionIndex

Excludes Session Index in SAML sign-on (SSO) and single logout (SLO) flows.

More Information

The ExcludeSAMLSessionIndex permission is off by default for all new and existing orgs. Enable this permission when Salesforce is the
identity provider and you don’t want the session index to be sent during SAML SSO. Enable this permission when Salesforce is the service
provider and you don’t want the session index to be sent during SLO. To turn on this feature, contact Salesforce Customer Support.

#### Explainability

Enables an org to use Decision Explainer features.

[For more information, see Decision Explainer for Expression Set in Salesforce developer documentation.](https://developer.salesforce.com/docs/atlas.en-us.262.0.industries_reference.meta/industries_reference/decision_explainer_bre_parent.htm)

#### ExpressionSetMaxExecPerHour

Enables an org to run a maximum of 500,000 expression sets per hour by using Connect REST API.

[For more information, see Expression Set in Salesforce developer documentation.](https://developer.salesforce.com/docs/atlas.en-us.262.0.industries_reference.meta/industries_reference/connect_resources_bre_expression_set.htm)

#### ExternalIdentityLogin

Allows the scratch org to use Salesforce Customer Identity features associated with your External Identity license.

#### FieldAuditTrail

Enables Field Audit Trail for the org and allows a total 60 tracked fields. By default, 20 fields are tracked for all orgs, and 40 more are
tracked with Field Audit Trail.

More Information

Previous name: RetainFieldHistory


Scratch Orgs Scratch Org Features

#### FieldService:<value>

Provides the Field Service license. Indicate a value between 1–25.

Supported Quantities

1–25, Multiplier: 1

More Information

[Available in Enterprise Edition. Enabled by default in Developer Edition. See Enable Field Service in Salesforce Help for more information.](https://help.salesforce.com/articleView?id=fs_enable.htm&language=en_US)

#### FieldServiceAppointmentAssistantUser:<value>

Adds the Field Service Appointment Assistant permission set license. Indicate a value between 1–25.

Supported Quantities

1–25, Multiplier: 1

More Information

[See Setup Field Service Appointment Assistant and Assign Field Service Permissions in Salesforce Help for more information.](https://help.salesforce.com/s/articleView?language=en_US&id=sf.mfs_appointment_assistant_parent.htm)

#### FieldServiceDispatcherUser:<value>

Adds the Field Service Dispatcher permission set license. Indicate a value between 1–25.

Supported Quantities

1–25, Multiplier: 1

More Information

[See Assign Field Service Permissions in Salesforce Help for more information.](https://help.salesforce.com/articleView?id=pfs_set_profiles_perms.htm&language=en_US)

#### FieldServiceLastMileUser:<value>

Adds the Field Service Last Mile permission set license. Indicate a value between 1–25.

Supported Quantities

1–25, Multiplier: 1

#### FieldServiceMobileExtension

Adds the Field Service Mobile Extension permission set license.


Scratch Orgs Scratch Org Features

#### FieldServiceMobileUser:<value>

Adds the Field Service Mobile permission set license. Indicate a value between 1–25.

Supported Quantities

1–25, Multiplier: 1

More Information

[See Assign Field Service Permissions in Salesforce Help for more information.](https://help.salesforce.com/articleView?id=pfs_set_profiles_perms.htm&language=en_US)

#### FieldServiceSchedulingUser:<value>

Adds the Field Service Scheduling permission set license. Indicate a value between 1–25.

Supported Quantities

1–25, Multiplier: 1

More Information

[See Assign Field Service Permissions in Salesforce Help for more information.](https://help.salesforce.com/articleView?id=pfs_set_profiles_perms.htm&language=en_US)

#### FinanceLogging

Adds Finance Logging objects to a scratch org. This feature is required for Finance Logging.

#### FinancialServicesCommunityUser:<value>

Adds the Financial Services Insurance Community permission set license, and enables access to Financial Services insurance community
components and objects. Indicate a value between 1–10.

Supported Quantities

1–10, Multiplier: 1

#### FinancialServicesInsuranceUser

Adds the Financial Services Insurance permission set license, and enables access to Financial Services insurance components and objects.

More Information

[See Get Started with Financial Services Cloud for Insurance in Salesforce Help.](https://help.salesforce.com/s/articleView?id=ind.fsc_admin_insurance_landing.htm&type=5&language=en_US)


Scratch Orgs Scratch Org Features

#### FinancialServicesUser:<value>

Adds the Financial Services Cloud Standard permission set license. This permission set enables access to Lightning components and the
standard version of Financial Services Cloud. Also provides access to the standard Salesforce objects and custom Financial Services Cloud
objects. Indicate a value between 1–10.

Supported Quantities

1–10, Multiplier: 1

#### FlowSites

Enables the use of flows in Salesforce Sites and customer portals.

#### ForceComPlatform

Adds one Salesforce Platform user license.

#### ForecastEnableCustomField

Enables custom currency and customer number fields for use as measures in forecasts based on opportunities.

More Information

[Available in Enterprise Edition and Unlimited Edition scratch orgs, and requires enabling Salesforce Forecasting in Setup. See Salesforce](https://help.salesforce.com/s/articleView?id=sales.forecasts3_intro.htm&type=5&language=en_US)
[Forecasting in Salesforce Help for more information.](https://help.salesforce.com/s/articleView?id=sales.forecasts3_intro.htm&type=5&language=en_US)

#### FSCAlertFramework

Makes Financial Services Cloud Record Alert entities accessible in the scratch org.

More Information

Provides 11 seats of the FSCComprehensivePsl user license and 11 seats of the FSCComprehensiveAddOn add-on license.

[Requires that you install Financial Services Cloud and OmniStudio. See Record Alerts in Financial Services Cloud Administrator Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.financial_services_cloud_admin_guide.meta/financial_services_cloud_admin_guide/fsc_admin_record_alerts.htm)

#### FSCServiceProcess

Enables the Service Process Studio feature of Financial Service Cloud. Provides 10 seats each of the IndustriesServiceExcellenceAddOn
and FinancialServicesCloudStardardAddOn licenses. To enable the feature, you must also turn on the StandardServiceProcess setting in
Setup and grant users the AccessToServiceProcess permission.

#### Fundraising

Gives users access to Nonprofit Cloud for Fundraising features and objects in Salesforce.


Scratch Orgs Scratch Org Features

Scratch Org Definition File

[See Nonprofit Cloud for Fundraising in Salesforce Help for more information. To enable Fundraising, add these settings to your scratch](https://help.salesforce.com/s/articleView?id=sfdo.NPC_FR_Nonprofit_Cloud_Fundraising.htm&language=en_US)
org definition file.

Note: The Fundraising licenses are assigned when the Fundraising feature is enabled in the scratch org.

```
   {

     "orgName": "Fundraising Org",

     "edition": "Enterprise",

     "features": [

      "AccountingSubledgerGrowthEdition",

      "IndustriesActionPlan",

      "AnalyticsQueryService",

      "PublicSectorAccess",

      "Fundraising",

      "IndustriesSalesExcellenceAddOn",

      "IndustriesServiceExcellenceAddOn",

      "MarketingUser",

      "ProgramManagement",

      "OmniStudioDesigner",

      "OmniStudioRuntime",

      "EnableSetPasswordInApi",

      "PersonAccounts"

     ],

     "settings": {

      "lightningExperienceSettings": {

       "enableS1DesktopEnabled": true

      },

      "IndustriesSettings": {

       "enableFundraising": true,

       "enableGiftEntryGrid": true,

       "enableGroupMembershipPref": true

      }

     }

   }

#### GenericStreaming

```

Enables Generic Streaming API for API version 36.0 and earlier.

More Information

Available in Enterprise and Developer Edition scratch orgs.

#### GenStreamingEventsPerDay:<value>

Increases the maximum number of delivered event notifications within a 24-hour period, shared by all CometD clients, with generic
streaming for API version 36.0 and earlier. Indicate a value between 10,000–50,000.

Supported Quantities

10,000–50,000, Multiplier: 1


Scratch Orgs Scratch Org Features

#### Grantmaking

Gives users access to Grantmaking features and objects in Salesforce and Experience Cloud.

More Information

[See Grantmaking in Salesforce Help for more information. To enable Grantmaking, add these settings to your scratch org definition file.](https://help.salesforce.com/s/articleView?id=ind.grmk_grantmaking.htm&type=5&language=en_US)

```
   {

     "features": ["Grantmaking"],

     "settings": {

      "IndustriesSettings": {

       "enableGrantmaking": true

      }

     }

   }

#### GuidanceHubAllowed

```

Enables the Guidance Center panel in Lightning Experience. The Guidance Center shows suggested and assigned content in the user’s
flow of work. Suggested content is related to the app or page where the user is working. Assigned content includes guidance sets for
Salesforce admins, links or Trailhead modules assigned to users with Learning Paths, and Enablement programs for sales reps.

More Information

Not available in Group Edition scratch orgs.

To use this scratch org feature, the Dev Hub org requires the GuidanceHubAllowed permission. If this permission isn't enabled in the
Dev Hub, contact Salesforce Customer Support.

[See Guidance Center in Salesforce Help for more information.](https://help.salesforce.com/s/articleView?id=platform.admin_guidancecenter_ov.htm&type=5&language=en_US)

#### HealthCloudAddOn

Enables use of Health Cloud.

More Information

[See Administer Health Cloud in Salesforce Help for more information.](https://help.salesforce.com/s/articleView?id=ind.healthcare_admin.htm&type=5&language=en_US)

#### HealthCloudEOLOverride

Salesforce retired the Health Cloud CandidatePatient object in Spring ‘22 to focus on the more robust Lead object. This scratch org
feature allows you to override that retirement and access the object.

More Information

[To use this scratch org feature, the Dev Hub org requires the HealthCloudEOLOverride permission. See Candidate Patient Data Entity](https://help.salesforce.com/s/articleView?id=000391944&type=1&language=en_US)
[Retirement in Salesforce Help for more information.](https://help.salesforce.com/s/articleView?id=000391944&type=1&language=en_US)


Scratch Orgs Scratch Org Features

#### HealthCloudForCmty

Enables use of Health Cloud for Experience Cloud Sites.

More Information

[See Experience Cloud Sites in Salesforce Help for more information.](https://help.salesforce.com/s/articleView?id=ind.admin_communities.htm&type=5&language=en_US)

#### HealthCloudMedicationReconciliation

Allows Medication Management to support Medication Reconciliation.

More Information

[See Enable Medication Management to Perform Medication Reconciliation in Salesforce Help for more information.](https://help.salesforce.com/s/articleView?id=ind.admin_medication_management_enable.htm&type=5&language=en_US)

#### HealthCloudPNMAddOn

Enables use of Provider Network Management.

More Information

[See Provider Network Management in Salesforce Help for more information.](https://help.salesforce.com/s/articleView?id=ind.admin_provider_network_management.htm&type=5&language=en_US)

#### HealthCloudUser

This enables the scratch org to use the Health Cloud objects and features equivalent to the Health Cloud permission set license for one
user.

More Information

[See Assign Health Cloud Permission Sets and Permission Set Licenses in Salesforce Help for more information.](https://help.salesforce.com/s/articleView?id=ind.admin_permissionset_licenses_assign.htm&type=5&language=en_US)

#### HighVelocitySales

Provides Sales Engagement licenses and enables Salesforce Inbox. Sales Engagement optimizes the inside sales process with a
high-productivity workspace. Sales managers can create custom sales processes that guide reps through handling different types of
prospects. And sales reps can rapidly handle prospects with a prioritized list and other productivity-boosting features. The Sales Engagement
feature can be deployed in scratch orgs, but the settings for the feature can’t be updated through the scratch org definition file. Instead,
configure settings directly in the Sales Engagement app.

#### HighVolumePlatformEventAddOn

Increases the daily delivery allocation of high-volume platform events or change data capture events by 100,000 events. This scratch
#### org feature simulates the purchase of an add-on. If the org has the HighVolumePlatformEventAddOn, the daily allocation is

flexible and isn’t enforced strictly to allow for usage peaks.


Scratch Orgs Scratch Org Features

More Information

[See Platform Event Allocations in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_events.meta/platform_events/platform_event_limits.htm) _Platform Events Developer Guide_ .

#### HLSAnalytics

Enables the HLS Analytics org perm in scratch orgs.

More Information

Provides 1 seat of the HealthCareAnalyticsPlus add-on license.

#### HoursBetweenCoverageJob:<value>

The frequency in hours when the sharing inheritance coverage report can be run for an object. Indicate a value between 1–24.

Supported Quantities

1–24, Multiplier: 1

#### IdentityProvisioningFeatures

Enables use of Salesforce Identity User Provisioning.

#### IgnoreQueryParamWhitelist

Ignores allowlisting rules for query parameter filter rules. If enabled, you can add any query parameter to the URL.

Note: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain terms
to avoid any effect on customer implementations.

#### IndustriesActionPlan

Provides a license for Action Plans. Action Plans allow you to define the tasks or document checklist items for completing a business
process.

More Information

Previous name: ActionPlan.

[For more information and configuration steps, see Enable Actions Plans in Salesforce Help.](https://help.salesforce.com/articleView?id=fsc_action_plans.htm&language=en_US)

#### IndustriesBranchManagement

Branch Management lets branch managers and administrators track the work output of branches, employees, and customer segments
in Financial Services Cloud.


Scratch Orgs Scratch Org Features

More Information

Provides the Branch Management add-on license and user permissions, plus 11 seats of the FSCComprehensivePsl user license and 11
seats of the FSCComprehensiveAddOn add-on license.

[Requires that you install Financial Services Cloud. See Branch Management in Financial Services Cloud Administrator Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.financial_services_cloud_admin_guide.meta/financial_services_cloud_admin_guide/fsc_admin_branch.htm)

#### IndustriesCompliantDataSharing

Grants users access to participant management and advanced configuration for data sharing to improve compliance with regulations
and company policies.

More Information

Provides 1 seat of the FinancialServicesCloudStandardAddOn add-on license.

[Requires that you install Financial Services Cloud. See Compliant Data Sharing in](https://developer.salesforce.com/docs/atlas.en-us.262.0.financial_services_cloud_admin_guide.meta/financial_services_cloud_admin_guide/fsc_admin_cds.htm) _Financial Services Cloud Administrator Guide_ .

#### IndustriesMfgAdvncdAccFrcs

Enables Advanced Account Forecasting. With Advanced Account Forecasting, generate comprehensive, multi-horizon forecasts for sales,
operations, inventory, service, and other aspects of your business. Tailor your forecasting configurations to your objectives to generate
accurate, relevant forecasts.

More Information

[See Create Holistic, Multi-Enterprise Forecasts with Advanced Account Forecasting in Salesforce Help for more information.](https://help.salesforce.com/s/articleView?id=ind.aaf_admin_parent_concept.htm&type=5&language=en_US)

#### IndustriesMfgPartnerVisitMgmt

Enables Partner Visit Management. Partner Visit Management helps sales managers in your company schedule visits to partner and
distributor locations. Sales managers can use those visits to monitor performance, arrange for periodic check-ins, conduct trainings,
upsell and cross-sell products, and follow up on sales agreement renewals and warranty expiration.

More Information

[See Partner Visit Management in Manufacturing Cloud in Salesforce Help for more information.](https://help.salesforce.com/s/articleView?id=ind.mfg_pvm_container.htm&type=5&language=en_US)

#### IndustriesMfgProgram

Enables Program Based Business. With Program Based Business, program managers can manage the end-to-end lifecycle of a program
where they derive forecasts based on their customers’ forecasts, transform these forecasts into business opportunities, and convert those
opportunities into run-rate business. Program based business is common across multiple industries such as process, aerospace, defense,
automotive, engineer-to-order, and make-to-order environments.

More Information

[See Learn About Program Based Business in Salesforce Help for more information.](https://help.salesforce.com/s/articleView?id=ind.pbb_parent_concept.htm&type=5&language=en_US)


Scratch Orgs Scratch Org Features

#### IndustriesMfgRebates

Enables Rebate Management. Manage incentive programs, track rebate attainment, automate payouts, and gain insights into sales
performance and program effectiveness.

More Information

[See Rebate Management in Salesforce Help for more information.](https://help.salesforce.com/s/articleView?id=xcloud.rebates_admin_parent.htm&language=en_US)

#### IndustriesMfgTargets

Enables Sales Agreements. With Sales Agreements, you can negotiate purchase and sale of products over a continued period. You can
also get insights into products, prices, discounts, and quantities. And you can track your planned and actual quantities and revenues
with real-time updates from orders and contracts.

More Information

[See Track Sales Compliance with Sales Agreements in Salesforce Help for more information.](https://help.salesforce.com/articleView?id=sa_admin_parent_concept.htm&type=5&language=en_US)

#### IndustriesManufacturingCmty

Provides the Manufacturing Sales Agreement for the Community permission set license, which is intended for the usage of partner
community users. It also provides access to the Manufacturing community template for admins users to create communities.

More Information

[See Improve Partner Collaboration with Communities in Salesforce Help for more information.](https://help.salesforce.com/articleView?id=sa_admin_communityoverview_concept.htm&type=5&language=en_US)

#### IndustriesMfgAccountForecast

Enables Account Forecast. With Account Forecast, you can generate forecasts for your accounts based on orders, opportunities, and
sales agreements. You can also create formulas to calculate your forecasts per the requirements of your company.

More Information

[See Create Account Forecasts to Enhance Your Planning in Salesforce Help for more information.](https://help.salesforce.com/articleView?id=af_admin_parent_concept.htm&type=5&language=en_US)

#### InsightsPlatform

Enables the CRM Analytics Plus license for CRM Analytics.

#### InsuranceCalculationUser

Enables the calculation feature of Insurance. Provides 10 seats each of the BRERuntimeAddOn and OmniStudioRuntime licenses. Also,
provides one seat each of the OmniStudio and BREPlatformAccess licenses.

#### InsuranceClaimMgmt

Enables claim management features. Provides one seat of the InsuranceClaimMgmtAddOn license.


Scratch Orgs Scratch Org Features

More Information

[See Manage Claims in Salesforce Help for more information.](https://help.salesforce.com/s/articleView?id=ind.insurance_claims_617267.htm&type=5&language=en_US)

#### InsurancePolicyAdmin

Enables policy administration features. Provides one seat of the InsurancePolicyAdministrationAddOn license.

More Information

[See Manage Insurance Policies in Salesforce Help for more information.](https://help.salesforce.com/s/articleView?id=ind.insurance_policy_administration_621128.htm&type=5&language=en_US)

#### IntelligentDocumentReader

Provides the license required to enable and use Intelligent Document Reader in a scratch org. Intelligent Document Reader uses optical
character recognition to automatically extract data with Amazon Textract by using your AWS account.

More Information

To use this scratch org feature, the Dev Hub org requires the EinsteinDocReader and BYOAForIFR permissions. For information about
[Intelligent Document Reader, see Intelligent Document Reader in Salesforce Help.](https://help.salesforce.com/s/articleView?id=ind.intelligent_document_reader.htm&type=5&language=en_US)

#### InvestigativeCaseManagement

Enables the objects, features, and permissions for managing investigative cases, including evidence management and case proceedings,
in Public Sector Solutions.

Sample Scratch Org Definition File

To enable InvestigativeCaseManagement, add these features and settings to your scratch org definition file.

```
   {

      "orgName": "ICM Org",

      "edition": "Developer",

      "features": [

      "InvestigativeCaseManagement:2"

      ],

      "settings": {

      "lightningExperienceSettings": {

      "enableS1DesktopEnabled": true

      },

      "mobileSettings": {

      "enableS1EncryptedStoragePref2": false

      },

      "industriesSettings": {

      "enableCarePlansPreference": true,

      "enableBenefitManagementPreference": true,

      "enableTimelinePref": true,

      "enableGroupMembershipPref": true,

      "enableIndustriesAssessment": true,

      "enableDiscoveryFrameworkMetadata": true,

      "enableInteractionSummaryPref": true,

```


Scratch Orgs Scratch Org Features

```
      "enableEnhancedUIForISPref": true,

      "enableInteractionCstmSharingPref": true,

      "enableCaseProceedingsPref": true,

      "enableEvidenceManagementPref": true,

      "enableInvestigativeCaseMgmntPrf": true,

      "enableDisbursementPreference": true,

      "enableCaseReferralPref": true

      }

      }

      }

#### InvoiceManagement

```

Enables access to all the Billing features and objects that are available with the Revenue Cloud Advanced license in the scratch org.

More Information

**•** Available in Enterprise, Unlimited, and Developer Edition scratch orgs.

**•** Provides 10 seats of BillingAddOn add-on licenses.

**•** [Enable Billing in Revenue Cloud and turn on the required Billing settings.](https://help.salesforce.com/s/articleView?id=ind.billing_setup_enable.htm&type=5&language=en_US)

**•** [Provides permission sets to access Billing features.](https://help.salesforce.com/s/articleView?id=ind.billing_permission_sets.htm&type=5&language=en_US)

**•** [See Manage Billing in Revenue Cloud for more information.](https://help.salesforce.com/s/articleView?id=ind.billing.htm&type=5&language=en_US)

Scratch Org Definition File

To enable InvoiceManagement, add these settings to your scratch org definition file.

```
   {

     "orgName": "<Org Name>",

     "adminEmail":"<Admin Email Address>"

     "edition": "<Edition Name>",

     "features": [

      "InvoiceManagement"

      "EnableSetPasswordInApi"

     ],

     "settings": {

      "billingSettings": {

       "enableBillingSetup": true

      },

     "lightningExperienceSettings": {

        "enableS1DesktopEnabled": true

       }

     }

   }

#### Interaction

```

Enables flows. A flow is the part of Salesforce Flow that collects data and performs actions in your Salesforce org or an external system.
Salesforce Flow provides two types of flows: screen flows and autolaunched flows.


Scratch Orgs Scratch Org Features

More Information

Requires configuration in the Setup menu of the scratch org.

#### InvocableActionExt

Enables the use of InvocableActionExtension metadata to customize how Apex invocable action inputs appear in Flow Builder.

More Information

Use InvocableActionExtension metadata files to add standard additional attributes to your Apex invocable action. These standard
additional attributes customize the action configuration experience in Flow Builder by controlling input parameter behavior, appearance,
and validation.

#### InvocableActionExtension metadata components have the suffix .invocableactionextension . Store these metadata

components in the `invocableactionextensions` folder. This metadata type is available in API version 65.0 and later.

[For more information about InvocableActionExtension, see InvocableActionExtension in the Metadata API Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_invocableactionextension.htm)

#### IoT

Enables IoT so the scratch org can consume platform events to perform business and service workflows using orchestrations and contexts.

More Information

Also requires Metadata API Settings in the scratch org definition file.

#### JigsawUser

Provides one license to Jigsaw features.

#### Knowledge

Enables Salesforce Knowledge and gives your website visitors, clients, partners, and service agents the ultimate support tool. Create and
manage a knowledge base with your company information, and securely share it when and where it's needed. Build a knowledge base
of articles that can include information on process, like how to reset your product to its defaults, or frequently asked questions.

More Information

[See Salesforce Knowledge in Salesforce Help for more information.](https://help.salesforce.com/articleView?id=knowledge_whatis.htm&type=5&language=en_US)

#### LegacyLiveAgentRouting

Enables legacy Live Agent routing for Chat. Use Live Agent routing to chat in Salesforce Classic. Chats in Lightning Experience must be
routed using Omni-Channel.

#### LightningSalesConsole

Adds one Lighting Sales Console user license.


Scratch Orgs Scratch Org Features

#### LightningScheduler

Enables Lightning Scheduler. Lightning Scheduler gives you tools to simplify appointment scheduling in Salesforce. Create a personalized
experience by scheduling customer appointments—in person, by phone, or by video—with the right person at the right place and
time.

More Information

[See Manage Appointments with Lightning Scheduler in Salesforce Help for more information.](https://help.salesforce.com/articleView?id=ls_overview.htm&type=5&language=en_US)

#### LightningServiceConsole

Assigns the Lightning Service Console License to your scratch org so you can use the Lightning Service Console and access features that
help manage cases faster.

More Information

[See Lightning Service Console in Salesforce Help for more information.](https://help.salesforce.com/articleView?id=console_lex_service_intro.htm&language=en_US)

#### LiveAgent

Enables Chat for Service Cloud. Use web-based chat to quickly connect customers to agents for real-time support.

#### LiveMessage

Enables Messaging for Service Cloud. Use Messaging to quickly support customers using apps such as SMS text messaging and Facebook
Messenger.

#### LongLayoutSectionTitles

Allows page layout section titles to be up to 80 characters.

More Information

To turn on this feature, contact Salesforce Customer Support.

#### LoyaltyAnalytics

Enables Analytics for Loyalty license. The Analytics for Loyalty app gives you actionable insights into your loyalty programs.

More Information

[See Analytics for Loyalty in Salesforce Help for more information.](https://help.salesforce.com/s/articleView?id=xcloud.analytics_loyalty_deploy_and_use.htm&type=5&language=en_US)

#### LoyaltyEngine

Enables Loyalty Management Promotion Setup license. Promotion setup allows loyalty program managers to create loyalty program
processes. Loyalty program processes help you decide how incoming and new Accrual and Redemption-type transactions are processed.


Scratch Orgs Scratch Org Features

More Information

[See Create Processes with Promotion Setup in Salesforce Help for more information.](https://help.salesforce.com/s/articleView?id=xcloud.promotion_setup.htm&type=5&language=en_US)

#### LoyaltyManagementStarter

Enables the Loyalty Management - Starter license. Create loyalty programs and set up loyalty program-specific processes that allow you
to recognize, rewards, and retain customers.

More Information

[See Loyalty Management in Salesforce Help for more information.](https://help.salesforce.com/s/articleView?id=xcloud.loyaltyoverview.htm&type=5&language=en_US)

#### LoyaltyMaximumPartners:<value>

Increases the number of loyalty program partners that can be associated with a loyalty program in an org where the Loyalty Management

    - Starter license is enabled. The default and maximum value is 1.

Supported Quantities

0–1, Multiplier: 1

#### LoyaltyMaximumPrograms:<value>

Increases the number of loyalty programs that can be created in an org where the Loyalty Management - Starter license is enabled. The
default and maximum value is 1.

Supported Quantities

0–1, Multiplier: 1

#### LoyaltyMaxOrderLinePerHour:<value>

Increases the number of order lines that can be cumulatively processed per hour by loyalty program processes. Indicate a value between
1–3,500,000.

Supported Quantities

1–3,500,000, Multiplier: 1

#### LoyaltyMaxProcExecPerHour:<value>

Increases the number of transaction journals that can be processed by loyalty program processes per hour. Indicate a value between
1–500,000.

Supported Quantities

1–500,000, Multiplier: 1


Scratch Orgs Scratch Org Features

#### LoyaltyMaxTransactions:<value>

Increases the number of Transaction Journal records that can be processed. Indicate a value between 1–50,000,000.

Supported Quantities

1–50,000,000, Multiplier: 1

#### LoyaltyMaxTrxnJournals:<value>

Increases the number of Transaction Journal records that can be stored in an org that has the Loyalty Management - Start license enabled.

Supported Quantities

1–25,000,000, Multiplier: 1

More Information

[See Transaction Journal Limits in Salesforce Help for more information.](https://help.salesforce.com/s/articleView?id=sf.transaction_journal_limit_starter.htm&language=en_US)

#### Macros

Enables macros in your scratch org. After enabling macros, add the macro browser to the Lightning Console so you can configure
predefined instructions for commonly used actions and apply them to multiple posts at the same time.

More Information

[See Set Up and Use Macros in Salesforce Help for more information.](https://help.salesforce.com/articleView?id=macros_def.htm&language=en_US)

#### MarketingCloud

Provides licenses for Marketing Cloud Growth edition. These licenses provide access to campaigns, flows, emails, forms, landing pages,
and consent management features. You can send up to 20 emails per day from a scratch org.

Scratch Org Definition File

```
   {

     "features": [

       "MarketingCloud",

       "CustomerDataPlatform",

       "CustomerDataPlatformLite",

       "EnableSetPasswordInApi",

     ],

     "settings": {

       "customerDataPlatformSettings": {

         "enableCustomerDataPlatform": true

       },

       "lightningExperienceSettings": {

         "enableS1DesktopEnabled": true

       },

       "mobileSettings": {

```


Scratch Orgs Scratch Org Features

```
         "enableS1EncryptedStoragePref2": false

       }

     }

   }

```

More Information

Marketing Cloud Growth edition uses Data Cloud to store engagement events, create segments, personalize messages, process decisions
in flows, and generate analytics. Salesforce ISVs that develop applications for Marketing Cloud Growth edition must have the Data Cloud
Scratch Org permission enabled in their Partner Business Orgs.

[You can enable Data Cloud in your scratch org by creating a case with Salesforce Partner Support. Use this template as a guide when](https://partners.salesforce.com/)
you submit your request, replacing _`{your_org_id_here}`_ with the ID of your Partner Business Org:

**•** **Subject** : _`Enable Data Cloud for scratch orgs in Dev Hub`_

**•** **Description** : _`Please enable Data Cloud scratch org permissions on my Partner Business`_

```
    Org. My org ID is {your_org_id_here}

```

**•** **Product and Topic** : _`Partner Programs & Benefits (License Request - Trial/Dev Org)`_

After Salesforce Partner Support completes your request, add the `CustomerDataPlatform` and
`CustomerDataPlatformLite` features to your scratch org definition file.

#### MarketingUser

Provides access to the Campaigns object. Without this setting, Campaigns are read-only.

#### MaterialityAssessment

Provides the permission set licenses and permission sets required to configure materiality assessment in Net Zero Cloud.

Scratch Org Definition File

Add these options to your scratch org definition file:

```
   {

      "orgName": "NZC Package Dev",

      "edition": "Enterprise",

      "features": [

       "DisclosureFramework",

       "DocGen",

       "DocGenDesigner",

       "DocGenInd",

       "OmnistudioDesigner",

       "OmnistudioRuntime",

       "SurveyAdvancedFeatures",

       "SustainabilityApp",

       "MaterialityAssessment:1"

      ],

      "settings": {

       "industriesSettings": {

        "enableGnrcDisclsFrmwrk": true,

        "enableIndustriesAssessment": true,

        "enableSustainabilityCloud": true,

```


Scratch Orgs Scratch Org Features

```
        "enableSCCarbonAccounting": true,

        "enableSCSNGManagement": true,

        "enableMaterialityAssessment": true,

        "enableInformationLibrary": true

      }

     }

   }

```

More Information

[For configuration steps, see Configure Net Zero Cloud and Enable the Disclosure and Compliance Hub in the Set Up and Maintain Net](https://help.salesforce.com/s/articleView?id=netzero_admin.htm&language=en_US)
Zero Cloud guide in Salesforce Help.

#### MaxActiveDPEDefs:<value>

Increases the number of Data Processing Engine definitions that can be activated in the org. Indicate a value between 1–50.

Supported Quantities

1–50, Multiplier: 1

#### MaxApexCodeSize:<value>

Limits the non-test, unmanaged Apex code size (in MB). To use a value greater than the default value of 10, contact Salesforce Customer
Support.

#### MaxAudTypeCriterionPerAud

Limits the number of audience type criteria available per audience. The default value is 10.

#### MaxCustomLabels:<value>

Limits the number of custom labels (measured in thousands). Setting the limit to 10 enables the scratch org to have 10,000 custom
labels. Indicate a value between 1–15.

Supported Quantities

1–15, Multiplier: 1,000

#### MaxDatasetLinksPerDT:<value>

Increases the number of dataset links that can be associated with a decision table. Indicate a value between 1–3.

Supported Quantities

1–3, Multiplier: 1


Scratch Orgs Scratch Org Features

#### MaxDataSourcesPerDPE:<value>

Increases the number of Source Object nodes a Data Processing Engine definition can contain. Indicate a value between 1–50.

Supported Quantities

1–50, Multiplier: 1

#### MaxDecisionTableAllowed:<value>

Increases the number of decision tables rules that can be created in the org. Indicate a value between 1–30.

Supported Quantities

1–30, Multiplier: 1

#### MaxFavoritesAllowed:<value>

Increases the number of Favorites allowed. Favorites allow users to create a shortcut to a Salesforce Page. Users can view their Favorites
by clicking the Favorites list dropdown in the header. Indicate a value between 0–200.

Supported Quantities

0–200, Multiplier: 1

#### MaxFieldsPerNode:<value>

Increases the number of fields a node in a Data Processing Engine definition can contain. Indicate a value between 1–500.

Supported Quantities

1–500, Multiplier: 1

#### MaxInputColumnsPerDT:<value>

Increases the number of input fields a decision table can contain. Indicate a value between 1–10.

Supported Quantities

1–10, Multiplier: 1

#### MaxLoyaltyProcessRules:<value>

Increases the number of loyalty program process rules that can be created in the org. Indicate a value between 1–20.

Supported Quantities

1–20, Multiplier: 1


Scratch Orgs Scratch Org Features

#### MaxNodesPerDPE:<value>

Increases the number of nodes that a Data Processing Engine definition can contain. Indicate a value between 1–500.

Supported Quantities

1–500, Multiplier: 1

#### MaxNoOfLexThemesAllowed:<value>

Increases the number of Themes allowed. Themes allow users to configure colors, fonts, images, sizes, and more. Access the list of
Themes in Setup, under Themes and Branding. Indicate a value between 0–300.

Supported Quantities

0–300, Multiplier: 1

#### MaxOutputColumnsPerDT:<value>

Increases the number of output fields a decision table can contain. Indicate a value between 1–5.

Supported Quantities

1–5, Multiplier: 1

#### MaxSourceObjectPerDSL:<value>

Increases the number of source objects that can be selected in a dataset link of a decision table. Indicate a value between 1–5.

Supported Quantities

1–5, Multiplier: 1

#### MaxStreamingTopics:<value>

Increases the maximum number of delivered PushTopic event notifications within a 24-hour period, shared by all CometD clients. Indicate
a value between 40–100.

Supported Quantities

40–100, Multiplier: 1

#### MaxUserNavItemsAllowed:<value>

Increases the number of navigation items a user can add to the navigation bar. Indicate a value between 0–500.

Supported Quantities

0–500, Multiplier: 1


Scratch Orgs Scratch Org Features

#### MaxUserStreamingChannels:<value>

Increases the maximum number of user-defined channels for generic streaming. Indicate a value between 20–1,000.

Supported Quantities

20–1,000, Multiplier: 1

#### MaxWishlistsItemsPerWishlist

Limits the number of wishlist items per wishlist. The default value is 500.

More Information

[For more information, see Salesforce Help at Salesforce B2B Commerce and D2C Commerce](https://help.salesforce.com/s/articleView?id=commerce.comm_intro.htm&type=5&language=en_US)

#### MaxWishlistsPerStoreAccUsr

Limits the number of wishlists allowed per store, account, and user. The default value is 100.

For example, if User1 is associated with Store1 and Store2, and has access to Account1 and Account2, then the wishlist limit is the same
for the combinations of User1 with Store1 and Account1, User1 with Store2 and Account2, and User1 with Store1 and Account2.

More Information

[For more information, see Salesforce Help at Salesforce B2B Commerce and D2C Commerce.](https://help.salesforce.com/s/articleView?id=commerce.comm_intro.htm&type=5&language=en_US)

#### MaxWritebacksPerDPE:<value>

Increases the number of Writeback Object nodes a Data Processing Engine definition can contain. Indicate a value between 1–50.

Supported Quantities

1–10, Multiplier: 1

#### MedVisDescriptorLimit:<value>

Increases the number of sharing definitions allowed per record for sharing inheritance to be applied to an object. Indicate a value between
150–1,600.

Supported Quantities

150–1,600, Multiplier: 1

#### MinKeyRotationInterval

Sets the encryption key material rotation interval at once per 60 seconds. If this feature isn't specified, the rotation interval defaults to
once per 604,800 seconds (7 days) for Search Index key material, and once per 86,400 seconds (24 hours) for all other key material.


Scratch Orgs Scratch Org Features

More Information

[Requires enabling PlatformEncryption and some configuration using the Setup menu in the scratch org. See Which User Permissions](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_scratch_orgs_def_file_config_values.htm#so_platformencryption)
[Does Shield Platform Encryption Require? and Generate a Tenant Secret with Salesforce in Salesforce Help.](https://help.salesforce.com/articleView?id=security_pe_permissions.htm&language=en_US)

#### MobileExtMaxFileSizeMB:<value>

Increases the file size (in megabytes) for Field Service Mobile extensions. Indicate a value between 1–2,000.

Supported Quantities

1–2,000, Multiplier: 1

#### MobileSecurity

Enables Enhanced Mobile Security. With Enhanced Mobile Security, you can control a range of policies to create a security solution
tailored to your org’s needs. You can limit user access based on operating system versions, app versions, and device and network security.
You can also specify the severity of a violation.

#### MobileVoiceAndLLM

Allows mobile apps to download large language models (LLMs) and voice models for offline use from the model store service. Normally,
mobile apps have access to the model store service when Einstein is enabled, but the MobileVoiceAndLLM scratch org feature enables
offline voice without requiring orgs to fully enable Einstein.

Sample Scratch Org Definition File

This sample scratch org definition file enables MobileVoiceAndLLM. Additionally, the sample scratch org definition configures
lightningExperienceSettings and mobileSettings.

```
   {

     "orgName": "Acme",

     "edition": "Developer",

     "features": ["MobileVoiceAndLLM"],

     "settings": {

      "lightningExperienceSettings": {

       "enableS1DesktopEnabled": true

      },

      "mobileSettings": {

       "enableS1EncryptedStoragePref2": false

      }

     }

   }

#### MultiLevelMasterDetail

```

Allows the creation a special type of parent-child relationship between one object, the child, or detail, and another object, the parent,
or master.


Scratch Orgs Scratch Org Features

#### MutualAuthentication

Requires client certificates to verify inbound requests for mutual authentication.

#### MyTrailhead

Enables access to a myTrailhead enablement site in a scratch org.

Scratch Org Definition File

Add these options to your scratch org definition file:

```
   {

     "orgName": "Acme",

     "edition": "Enterprise",

     "features": ["MyTrailhead"],

     "settings": {

      "trailheadSettings": {

       "enableMyTrailheadPref": true

      }

     }

   }

```

More Information

[Salesforce Help: Enablement Sites (myTrailhead)](https://help.salesforce.com/s/articleView?id=sales.mth_intro.htm&type=5&language=en_US)

#### NonprofitCloudCaseManagementUser

Provides the permission set license required to use and configure the Salesforce.org Nonprofit Cloud Case Management managed
package. You can then install the package in the scratch org.

More Information

[For installation and configuration steps, see Salesforce.org Nonprofit Cloud Case Management.](https://powerofus.force.com/s/article/CM-Documentation)

#### NumPlatformEvents:<value>

Increases the maximum number of platform event definitions that can be created. Indicate a value between 5–20.

Supported Quantities

5–20, Multiplier: 1

#### ObjectLinking

Create rules to quickly link channel interactions to objects such as contacts, leads, or person accounts for customers (Beta).


Scratch Orgs Scratch Org Features

#### OmnistudioMetadata

Enables Omnistudio metadata API. Using this API, customers can deploy and retrieve Omnistudio components programmatically.

[For more information, see Enable OmniStudio Metadata API Support.](https://help.salesforce.com/s/articleView?id=xcloud.os_enable_omnistudio_metadata_api_support.htm&type=5&language=en_US)

#### OmnistudioRuntime

Enables business users to execute OmniScripts, DataMappers, FlexCards, and so on in the employee facing applications.

#### OmnistudioDesigner

Enables administrator or developer to create new OmniScripts/ DataMappers / Integration Procedures instances.

#### OrderManagement

Provides the Salesforce Order Management license. Order Management is your central hub for handling all aspects of the order lifecycle,
including order capture, fulfillment, shipping, payment processing, and servicing.

More Information

Available in Enterprise and Developer Edition scratch orgs.

If you want to configure Order Management to use any of these features, enable it in your scratch org:

**•** MultiCurrency

**•** PersonAccounts

**•** ProcessBuilder

**•** StateAndCountryPicklist

Requires configuration using the Setup menu in the scratch org. For installation and configuration steps, see _Salesforce Help_ [: Salesforce](https://help.salesforce.com/s/articleView?id=commerce.om_order_management.htm&type=5&language=en_US)
[Order Management.](https://help.salesforce.com/s/articleView?id=commerce.om_order_management.htm&type=5&language=en_US)

Note: The implementation process includes turning on several Order and Order Management feature toggles in Setup. In a scratch
org, you can turn them on by including metadata settings in your scratch org definition file. For details about these settings, see
[OrderSettings and OrderManagementSettings in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_ordersettings.htm) _Metadata API Developer Guide_ .

#### OrderSaveLogicEnabled

Enables scratch org support for New Order Save Behavior. OrderSaveLogicEnabled supports only New Order Save Behavior. If your scratch
org needs both Old and New Order Save Behavior, use OrderSaveBehaviorBoth.

Scratch Org Definition File

To enable OrderSaveLogicEnabled, update your scratch org definitions file.

```
   {

     "features": ["OrderSaveLogicEnabled"],

     "settings": {

      "orderSettings": {

       "enableOrders": true

      }

```


Scratch Orgs Scratch Org Features

```
     }

   }

#### OrderSaveBehaviorBoth

```

Enables scratch org support for both New Order Save Behavior and Old Order Save Behavior.

Scratch Org Definition File

To enable OrderSaveLogicEnabled, update your scratch org definitions file.

```
   {

     "features": ["OrderSaveBehaviorBoth"],

     "settings": {

      "orderSettings": {

       "enableOrders": true

      }

     }

   }

#### OutboundMessageHTTPSession

```

Enables using HTTP endpoint URLs in outbound message definitions that have the Send Session ID option selected.

#### OutcomeManagement

Gives users access to Outcome Management features and objects in Salesforce and Experience Cloud.

More Information

[See Outcome Management in Salesforce Help for more information. To enable Outcome Management, add these settings to your](https://help.salesforce.com/s/articleView?id=ind.outcome_management.htm&type=5&language=en_US)
scratch org definition file.

```
   {

     "features": ["OutcomeManagement"],

     "settings": {

      "IndustriesSettings": {

       "enableOutcomes": true

      }

     }

   }

#### PardotScFeaturesCampaignInfluence

```

Enables additional campaign influence models, first touch, last touch, and even distribution for Pardot users.

#### PersonAccounts

Enables person accounts in your scratch org.


Scratch Orgs Scratch Org Features

More Information

Available in Enterprise and Developer Edition scratch orgs.

#### PipelineInspection

Enables Pipeline Inspection. Pipeline Inspection is a consolidated pipeline view with metrics, opportunities, and highlights of recent
changes.

More Information

Available in Enterprise Edition scratch orgs. To enable Pipeline Inspection in your scratch org, add this setting in your scratch org definition
file.

```
   "settings": {

      ...

      "opportunitySettings": {

       "enablePipelineInspectionFlow": true

      },

      ...

     }

#### PlatformCache

```

Enables Platform Cache and allocates a 3 MB cache. The Lightning Platform Cache layer provides faster performance and better reliability
when caching Salesforce session and org data.

More Information

[See Platform Cache in the Apex Developer Guide for more information.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_cache_namespace_overview.htm)

#### PlatformConnect:<value>

Enables Salesforce Connect and allows your users to view, search, and modify data that's stored outside your Salesforce org. Indicate a
value from 1–5.

Supported Quantities

1–5, Multiplier: 1

#### PlatformEncryption

Shield Platform Encryption encrypts data at rest. You can manage key material and encrypt fields, files, and other data.

#### PlatformEventsPerDay:<value>

Increases the maximum number of delivered standard-volume platform event notifications within a 24-hour period, shared by all CometD
clients. Indicate a value between 10,000–50,000.


Scratch Orgs Scratch Org Features

Supported Quantities

10,000–50,000, Multiplier: 1

#### ProcessBuilder

Enables Process Builder, a Salesforce Flow tool that helps you automate your business processes.

More Information

Requires configuration in the Setup menu of the scratch org.

[See Process Builder in Salesforce Help for more information.](https://help.salesforce.com/articleView?id=process_overview.htm&language=en_US)

#### ProductsAndSchedules

Enables product schedules in your scratch org. Enabling this feature lets you create default product schedules on products. Users can
also create schedules for individual products on opportunities.

#### ProductCatalogManagementAddOn

Enables read-write access to Product Catalog Management features and objects.

More Information

Available in Developer and Enterprise scratch org editions. Provides 1 Product Catalog Management add-on license.

#### ProductCatalogManagementViewerAddOn

Enables read access to Product Catalog Management features and objects.

More Information

Available in Developer and Enterprise scratch org editions. Provides 1 Product Catalog Management Viewer add-on license.

#### ProductCatalogManagementPCAddOn

Enables read access to Product Catalog Management features and objects for Partner Community Users in scratch orgs.

More Information

**•** Available in Developer and Enterprise scratch org editions.

**•** Provides 1 Product Catalog Management add-on license.

**•** Requires a partner community user to be set up. The partner community user must be granted the Product Catalog Management
Partner Community add-on license.

#### ProgramManagement

Enables access to all Program Management and Case Management features and objects.


Scratch Orgs Scratch Org Features

More Information

To enable ProgramManagement, add these settings to your scratch org definition file.

```
   {

     "orgName": "Sample Org",

     "edition": "Enterprise",

     "features": ["ProgramManagement"],

     "settings": {

      "IndustriesSettings": {

       "enableBenefitManagementPreference": true,

       "enableBenefitAndGoalSharingPref": true,

       "enableCarePlansPreference": true

      }

     }

   }

```

[Alternatively, enable the settings in the org manually. See Enable Program Management in Salesforce Help.](https://help.salesforce.com/s/articleView?id=sfdo.NPC_PM_Enable_Program_Management.htm&language=en_US)

#### ProviderFreePlatformCache

Provides 3 MB of free Platform Cache capacity for security-reviewed managed packages. This feature is made available through a capacity
type called Provider Free capacity and is automatically enabled in Developer Edition orgs. Allocate the Provider Free capacity to a Platform
Cache partition and add it to your managed package.

More Information

[See Set Up a Platform Cache Partition with Provider Free Capacity in Salesforce Help for more information.](https://help.salesforce.com/articleView?id=data_platform_cache_setup_provider_capacity.htm&type=5&language=en_US)

#### ProviderManagement

Enables the objects, features, and permissions for managing provider networks, care plans, and service delivery in Public Sector Solutions.

Sample Scratch Org Definition File

To enable ProviderManagement, add these features and settings to your scratch org definition file.

```
   {

      "orgName": "Provider Management Org",

      "edition": "Developer",

      "features": ["ProviderManagement:2"],

      "settings": {

      "lightningExperienceSettings": {

      "enableS1DesktopEnabled": true

      },

      "mobileSettings": {

      "enableS1EncryptedStoragePref2": false

      },

      "IndustriesSettings": {

      "enableBenefitAndGoalSharingPref": true,

      "enableBenefitManagementPreference": true,

      "enableCarePlansPreference": true,

      "enableCaseReferralPref": true,

```


Scratch Orgs Scratch Org Features

```
      "enableProviderManagementPref": true,

      "enableProviderMgmtSharingPref": true,

      "enableDisbursementPreference": true

      }

      }

      }

#### PSSAssetManagement

```

Enables the objects, features, and permissions for managing assets in Public Sector Solutions.

Sample Scratch Org Definition File

To enable PSSAssetManagement, add these features and settings to your scratch org definition file.

```
   {

      "orgName": "PSS Asset Management Org",

      "edition": "Enterprise",

      "features": [

      "PSSAssetManagement"

      ],

      "settings": {

      "industriesSettings": {

      "enableIndustriesAssessment": true,

      "enableDiscoveryFrameworkMetadata": true

      }

      }

      }

#### PublicSectorAccess

```

Enables access to all Public Sector features and objects.

#### PublicSectorApplicationUsageCreditsAddOn

Enables additional usage of Public Sector applications based on their pricing.

#### PublicSectorSiteTemplate

Allows Public Sector users access to build an Experience Cloud site from the templates available.

#### RateManagement

Enables Rate Management that allows you to set, manage, and optimize rates for usage-based products.

More Information

**•** Provides these set of licenses:

**–** 5 RatingEngineAccess platform licenses

**–** 5 RatingRunTimeAddOn add-on licenses


Scratch Orgs Scratch Org Features

**–** 5 RatingDesignTimeAddOn add-on licenses

**–** 10 FullCRM licenses

**•** [Requires you to enable CoreCpq to access Rate Management.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_scratch_orgs_def_file_config_values.htm#so_corecpq)

[See Configure Rate Pricing Calculations in Revenue Cloud in Salesforce Help for more information.](https://help.salesforce.com/s/articleView?id=ind.rm_rate_management.htm&type=5&language=en_US)

#### RecordTypes

Enables Record Type functionality. Record Types let you offer different business processes, picklist values, and page layouts to different
users.

#### RefreshOnInvalidSession

Enables automatic refreshes of Lightning pages when the user's session is invalid. If, however, the page detects a new token, it tries to
set that token and continue without a refresh.

#### RevSubscriptionManagement

Enables Subscription Management. Subscription Management is an API-first, product-to-cash solution for B2B subscriptions and one-time
sales.

More Information

Available in Enterprise and Developer scratch orgs. To enable Subscription Management in your scratch org, add this setting in your
scratch org definition file.

```
   "settings": {

      ...

      "subscriptionManagementSettings": {

       "enableSubscriptionManagement": true

      },

      ...

     }

```

For more information about Subscription Management, see
[https://developer.salesforce.com/docs/revenue/subscription-management/overview.](https://developer.salesforce.com/docs/revenue/subscription-management/overview)

#### S1ClientComponentCacheSize

Allows the org to have up to 5 pages of caching for Lightning Components.

#### SalesCloudEinstein

Enables Sales Cloud Einstein features and Salesforce Inbox. Sales Cloud Einstein brings AI to every step of the sales process.

More Information

Available in Enterprise Edition scratch orgs.

[See Sales Cloud Einstein in Salesforce Help for more information.](https://help.salesforce.com/articleView?id=einstein_sales.htm&type=5&language=en_US)


Scratch Orgs Scratch Org Features

#### SalesforceContentUser

Enables access to Salesforce content features.

#### SalesforceFeedbackManagementStarter

Provides a license to use the Salesforce Feedback Management - Starter features.

More Information

Available in Enterprise and Developer edition scratch orgs. To use the Salesforce Feedback Management - Starter features, enable Surveys
and assign the Salesforce Advanced Features Starter user permission to the scratch org user. For additional information on how to enable
[Surveys and configuration steps, see Enable Surveys and Configure Survey Settings and Assign User Permissions in Salesforce Help.](https://help.salesforce.com/s/articleView?id=xcloud.task_enable_surveys.htm&type=5&language=en_US)

#### SalesforceHostedMCP

Enables hosted MCP servers on the scratch org. With this scratch org feature parameter, MCP clients can connect to available hosted
MCP servers.

More Information

[Use of Salesforce hosted MCP servers requires setup of external clients. See Salesforce Hosted MCP Severs in Salesforce Help.](https://help.salesforce.com/s/articleView?id=platform.hosted_mcp_servers.htm&type=5&language=en_US)

#### SalesforceIdentityForCommunities

Adds Salesforce Identity components, including login and self-registration, to Experience Builder. This feature is required for Aura
components.

#### SalesforcePricing

Enables Salesforce Pricing, which allows you to set, manage, and optimize prices across your entire product portfolio

More Information

[Provides 5 Salesforce Pricing Design Time AddOn, 5 Salesforce Pricing Run Time AddOn licenses. For more information, see Salesforce](https://help.salesforce.com/s/articleView?id=ind.pricing_salesforce_pricing.htm&type=5&language=en_US)
[Pricing in Salesforce Help.](https://help.salesforce.com/s/articleView?id=ind.pricing_salesforce_pricing.htm&type=5&language=en_US)

#### SalesUser

Provides a license for Sales Cloud features.

#### SAML20SingleLogout

Enables usage of SAML 2.0 single logout.

#### SCIMProtocol

Enables access support for the SCIM protocol base API.


Scratch Orgs Scratch Org Features

#### ScvMultipartyAndConsult

Enables you to set up and test multiparty calls and consult calls for Service Cloud Voice with Partner Telephony.

More Information

This feature requires that you also include the `ServiceCloudVoicePartnerTelephony` scratch org feature in your scratch
org definition file. Available in Salesforce Enterprise, Unlimited, and Developer Editions.

[For setup and configuration steps, see Manage Multiparty Calls and Consult Calls in the Service Cloud Voice for Partner Telephony](https://developer.salesforce.com/docs/atlas.en-us.262.0.voice_pt_developer_guide.meta/voice_pt_developer_guide/voice_pt_multiparty_consult_calls.htm)
Developer Guide.

Sample Scratch Org Definition File

```
   {

     "orgName": "MultipartyScratchOrg",

     "edition": "Developer",

     "features": ["ScvMultipartyAndConsult", "ServiceCloudVoicePartnerTelephony"]

     "settings": {

      "lightningExperienceSettings": {

       "enableS1DesktopEnabled": true

      },

     "mobileSettings": {

       "enableS1EncryptedStoragePref2": false

      }

     }

   }

#### SecurityEventEnabled

```

Enables access to security events in Event Monitoring.

#### SentimentInsightsFeature

Provides the license required to enable and use Sentiment Insights in a scratch org. Use Sentiment Insights to analyze the sentiment of
your customers and get actionable insights to improve it.

More Information

To use this scratch org feature, the Dev Hub org requires the IESentimentAnalysis, AwsSentimentAnalysis, BYOAForSentiment, and
[IESentimentAnalysisEnabled permissions. For information about Sentiment Insights, see Sentiment Insights in Salesforce Help.](https://help.salesforce.com/s/articleView?id=xcloud.sentiment_insights.htm&type=5&language=en_US)

#### ServiceCatalog

Enables Employee Service Catalog so you can create a catalog of products and services for your employees. It can also turn your employees'
requests for these products and services into approved and documented orders.

More Information

[To use this scratch org feature, the Dev Hub org requires the ServiceCatalog permission. To learn more, see Employee Service Catalog.](https://help.salesforce.com/s/articleView?id=service.esc_get_started_with_employee_service_catalog.htm&type=5&language=en_US)


Scratch Orgs Scratch Org Features

#### ServiceCloud

Assigns the Service Cloud license to your scratch org, so you can choose how your customers can reach you, such as by email, phone,
social media, online communities, chat, and text.

#### ServiceCloudVoicePartnerTelephony

Assigns the Service Cloud Voice with Partner Telephony add-on license to your scratch org, so you can set up a Service Cloud Voice
contact center that integrates with supported telephony providers. Indicate a value from 1–50.

Supported Quantities

1–50, Multiplier: 1

More Information

[For setup and configuration steps, see Service Cloud Voice with Partner Telephony in Salesforce Help.](https://help.salesforce.com/articleView?id=service.voice_pt_setup.htm&type=5&language=en_US)

#### ServiceUser

Adds one Service Cloud User license, and allows access to Service Cloud features.

#### SessionIdInLogEnabled

Enables Apex debug logs to include session IDs. If disabled, session IDs are replaced with "SESSION_ID_REMOVED" in debug logs.

#### SFDOInsightsDataIntegrityUser

Provides a license to Salesforce.org Insights Platform Data Integrity managed package. You can then install the package in the scratch
org.

More Information

[For installation and configuration steps, see the Salesforce.org Insights Platform Data Integrity help.](https://powerofus.force.com/s/article/IP-Documentation)

#### SharedActivities

Allow users to relate multiple contacts to tasks and events.

More Information

[For additional installation and configuration steps, see Considerations for Enabling Shared Activities in Salesforce Help.](https://help.salesforce.com/s/articleView?id=sales.activities_shared_considerations.htm&type=5&language=en_US)

#### Sites

Enables Salesforce Sites, which allows you to create public websites and applications that are directly integrated with your Salesforce
org. Users aren’t required to log in with a username and password.


Scratch Orgs Scratch Org Features

More Information

You can create sites and communities in a scratch org, but custom domains, such as www.example.com, aren't supported.

#### SocialCustomerService

Enables Social Customer Service, sets post defaults, and either activates the Starter Pack or signs into your Social Studio account.

#### StateAndCountryPicklist

Enables state and country/territory picklists. State and country/territory picklists let users select states and countries from predefined,
standardized lists, instead of entering state, country, and territory data into text fields.

#### StreamingAPI

Enables Streaming API.

More Information

Available in Enterprise and Developer Edition scratch orgs.

#### StreamingEventsPerDay:<value>

Increases the maximum number of delivered PushTopic event notifications within a 24-hour period, shared by all CometD clients (API
version 36.0 and earlier). Indicate a value between 10,000–50,000.

Supported Quantities

10,000–50,000, Multiplier: 1

#### SubPerStreamingChannel:<value>

Increases the maximum number of concurrent clients (subscribers) per generic streaming channel (API version 36.0 and earlier). Indicate
a value between 20–4,000.

Supported Quantities

20–4,000, Multiplier: 1

#### SubPerStreamingTopic:<value>

Increases the maximum number of concurrent clients (subscribers) per PushTopic streaming channel (API version 36.0 and earlier).
Indicate a value between 20–4,000.

Supported Quantities

20–4,000, Multiplier: 1


Scratch Orgs Scratch Org Features

#### SurveyAdvancedFeatures

Enables a license for the features available with the Salesforce Feedback Management - Growth license.

More Information

Available in Enterprise and Developer edition scratch orgs. To use the Salesforce Feedback Management - Growth features, enable
Surveys and assign the Salesforce Surveys Advanced Features user permission to the scratch org user. For additional information on how
[to enable Surveys and configuration steps, see Enable Surveys and Configure Survey Settings and Assign User Permissions in Salesforce](https://help.salesforce.com/s/articleView?id=xcloud.task_enable_surveys.htm&type=5&language=en_US)
Help.

#### SustainabilityCloud

Provides the permission set licenses and permission sets required to install and configure Sustainability Cloud. To enable or use CRM
Analytics and CRM Analytics templates, include the DevelopmentWave scratch org feature.

More Information

[For installation and configuration steps, see Sustainability Cloud Legacy Documentation in the Set Up and Maintain Net Zero Cloud](https://help.salesforce.com/s/articleView?id=ind.sustainability_cloud_legacy_documentation.htm&type=5&language=en_US)
guide in Salesforce Help.

#### SustainabilityApp

Provides the permission set licenses and permission sets required to configure Net Zero Cloud. To enable or use Tableau CRM and Tableau
CRM templates, include the DevelopmentWave scratch org feature.

Scratch Org Definition File

Add these options to your scratch org definition file:

```
   {

     "orgName": "net zero scratch org",

     "edition": "Developer",

     "features": ["SustainabilityApp"],

     "settings": {

      "industriesSettings": {

       "enableSustainabilityCloud": true,

       "enableSCCarbonAccounting": true

      }

     }

   }

```

More Information

[For configuration steps, see Configure Net Zero Cloud in the Set Up and Maintain Net Zero Cloud guide in Salesforce Help.](https://help.salesforce.com/s/articleView?id=netzero_admin.htm&language=en_US)

#### TalentRecruitmentManagement

Enables the objects, features, and permissions for managing the talent recruitment and hiring process in Public Sector Solutions.


Scratch Orgs Scratch Org Features

Sample Scratch Org Definition File

To enable TalentRecruitmentManagement, add these features and settings to your scratch org definition file.

```
   {

      "orgName": "TRM Org",

      "edition": "Developer",

      "features": [

      "TalentRecruitmentManagement:4"

      ],

      "settings": {

      "lightningExperienceSettings": {

      "enableS1DesktopEnabled": true

      },

      "mobileSettings": {

      "enableS1EncryptedStoragePref2": false

      },

      "IndustriesSettings": {

      "enablePositionRecruitmentPref": true,

      "enableIndustriesAssessment": true,

      "enableDiscoveryFrameworkMetadata": true,

      "enableCriteriaBasedSearchAndFilter": true

      },

      "DocumentChecklistSettings": {

      "deleteDCIWithFiles": true

      }

      }

      }

#### TCRMforSustainability

```

Enables all permissions required to manage the Net Zero Analytics app by enabling Tableau CRM. You can create and share the analytics
app for your users to bring your environmental accounting in line with your financial accounting.

More Information

[For more information, see Deploy Net Zero Analytics in the Set Up and Maintain Net Zero Cloud guide in Salesforce Help.](https://help.salesforce.com/s/articleView?id=ind.netzero_admin_analytics_deploy.htm&type=5&language=en_US)

#### TimelineConditionsLimit

Limits the number of timeline record display conditions per event type to 3.

More Information

[See Provide Holistic Patient Care with Enhanced Timeline in Salesforce Help for more information.](https://help.salesforce.com/s/articleView?id=ind.hc_timeline.htm&type=5&language=en_US)

#### TimelineEventLimit

Limits the number of event types displayed on a timeline to 5.


Scratch Orgs Scratch Org Features

More Information

[See Provide Holistic Patient Care with Enhanced Timeline in Salesforce Help for more information.](https://help.salesforce.com/s/articleView?id=ind.hc_timeline.htm&type=5&language=en_US)

#### TimelineRecordTypeLimit

Limits the number of related object record types per event type to 3.

More Information

[See Provide Holistic Patient Care with Enhanced Timeline in Salesforce Help for more information.](https://help.salesforce.com/s/articleView?id=ind.hc_timeline.htm&type=5&language=en_US)

#### TimeSheetTemplateSettings

Time Sheet Templates let you configure settings to create time sheets automatically. For example, you can create a template that sets
start and end dates. Assign templates to user profiles so that time sheets are created for the right users.

More Information

[For configuration steps, see Create Time Sheet Templates in Salesforce Help.](https://help.salesforce.com/articleView?id=fs_create_timesheets.htm&type=5&language=en_US)

#### TransactionFinalizers

Enables you to implement and attach Apex Finalizers to Queueable Apex jobs.

More Information

Note: This functionality is currently in open pilot and subject to restrictions.

[See the Transaction Finalizers (Pilot) in Apex Developer Guide for more information.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_transaction_finalizers.htm)

#### UsageManagement

Enables Usage Management. Using Usage Management, you can setup, track, and manage the consumption of usage-based products.

More Information

**•** Provides 5 UsageManagementAddOn add-on licenses and 10 FullCRM licenses.

[See Usage Management in Salesforce Help for more information.](https://help.salesforce.com/s/articleView?id=ind.um_usage_management.htm&type=5&language=en_US)

#### VolunteerManagement

Gives users access to Volunteer Management features and objects in Salesforce.

Scratch Org Definition File

[See Nonprofit Cloud for Volunteer Management in Salesforce Help for more information. To enable Volunteer Management, add these](https://help.salesforce.com/s/articleView?id=sfdo.volunteer_mgmt_volunteer_management.htm&language=en_US)
settings to your scratch org definition file.


Scratch Orgs Scratch Org Features

Note: Volunteer Management licenses are assigned when the Volunteer Management feature is enabled in the scratch org.

```
   {

      "orgName": "Volunteer Management Org",

      "edition": "Enterprise",

      "hasSampleData": "false",

      "features": [

        "PersonAccounts",

        "VolunteerManagement"

      ],

      "settings": {

        "lightningExperienceSettings": {

           "enableS1DesktopEnabled": true

        },

        "IndustriesSettings": {

           "enableVolunteerManagement": true

        }

      }

     }

#### WaveMaxCurrency

```

Increases the maximum number of supported currencies for CRM Analytics. Indicate a value between 1–5.

#### WavePlatform

Enables the Wave Platform license.

#### Workflow

Enables Workflow so you can automate standard internal procedures and processes.

More Information

Requires configuration in the Setup menu of the scratch org.

#### WorkflowFlowActionFeature

Allows you to launch a flow from a workflow action.

More Information

This setting is supported only if you enabled the pilot program in your org for flow trigger workflow actions. If you enabled the pilot,
you can continue to create and edit flow trigger workflow actions.

If you didn't enable the pilot, use the Flows action in the ProcessBuilder scratch org feature instead.

#### WorkplaceCommandCenterUser

Enables access to Workplace Command Center features including access to objects such as Employee, Crisis, and EmployeeCrisisAssessment.


### Scratch Orgs Scratch Org Settings

More Information

[For additional installation and configuration steps, see Set Up Your Work.com Development Org in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.workdotcom_dev_guide.meta/workdotcom_dev_guide/wdc_cc_setup_dev_org.htm) _Workplace Command Center for_
_Work.com Developer Guide_ .

#### WorkThanksPref

Enables the give thanks feature in Chatter.

### Scratch Org Settings

Scratch org settings are the format for defining org preferences in the scratch org definition. Because you can use all Metadata API
settings, they’re the most comprehensive way to configure a scratch org. If a setting is supported in Metadata API, it’s supported in
scratch orgs. Settings provide you with fine-grained control because you can define values for all fields for a setting, rather than just
enabling or disabling it.

[For information on Metadata API settings and their supported fields, see Settings in](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_settings.htm) _Metadata API Developer Guide_ .

Important: Although the Settings are upper camel case in the _Metadata API Developer Guide_, be sure to indicate them as lower
camel case in the scratch org definition.

```
   {

     "orgName": "Acme",

     "edition": "Enterprise",

     "features": ["Communities", "ServiceCloud", "Chatbot"],

     "settings": {

       "communitiesSettings": {

         "enableNetworksEnabled": true

       },

       "lightningExperienceSettings": {

         "enableS1DesktopEnabled": true

       },

       "mobileSettings": {

         "enableS1EncryptedStoragePref2": true

       },

       "omniChannelSettings": {

         "enableOmniChannel": true

       },

       "caseSettings": {

         "systemUserEmail": "support@acme.com"

       }

     }

   }

```

[Here’s an example of how to configure SecuritySettings in your scratch org. In this case, to define session timeout, you nest the field](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_securitysettings.htm)
values.

```
   {

     "orgName": "Acme",

     "edition": "Enterprise",

     "features": [],

     "settings": {

        "mobileSettings": {

         "enableS1EncryptedStoragePref2": true

```


## Scratch Orgs Create a Scratch Org Based on an Org Shape

```
        },

       "securitySettings": {

         "sessionSettings":{

           "sessionTimeout": "TwelveHours"

         }

       }

     }

   }

```

[This example shows how to use NameSettings to enable middle names and suffixes in your org for these person objects: Contact, Lead,](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_namesettings.htm)
Person Account, and User.

```
   {

     "orgName": "Acme",

     "edition": "Enterprise",

     "settings": {

       "mobileSettings": {

         "enableS1EncryptedStoragePref2": true

        },

        "nameSettings": {

         "enableMiddleName": true,

         "enableNameSuffix": true

       }

     }

   }

## Create a Scratch Org Based on an Org Shape

```

We know it’s not easy to build a scratch org definition that mirrors the features and settings in your production org. With Org Shape for
Scratch Orgs, you can leave building the scratch org definition to us. After you capture the org’s shape, you can spin up scratch orgs
based on it.

**Available in:** Developer, Group, Professional, Unlimited, and Enterprise editions. The scratch org created from the org shape is the same
edition as the source org.

**Not available in:** Scratch orgs and sandboxes

What’s Included in Org Shape?

Features, Metadata API settings, edition, limits, and licenses determine what we refer to as an org’s shape. For further clarification, org
shape includes:

**•** Metadata API settings with `boolean` fields.

**•** Licenses associated with installed packages, but not the packages themselves. To use the associated package, install it in the scratch
org created from the org shape.

Note: Some features aren’t captured when the org shape is created. However, you can add the features manually to the scratch
org definition file. See Troubleshoot Org Shape for details.


### Scratch Orgs Enable Org Shape for Scratch Orgs

What’s Not Included in Org Shape?

**•** Metadata API settings with `integer` or `string` fields. However, you can manually add non-Boolean settings or other settings
not included in the source org to your scratch org definition. See Scratch Org Definition for Org Shape for examples.

**•** Metadata types

**•** Data

Org Shapes Are Specific to a Release

Scratch org shapes are associated with a specific Salesforce release. Be sure to recreate the org shape after the source org is upgraded
to the new Salesforce release. During a Salesforce major release transition, your Dev Hub org and source org can be on different release
versions. See Scratch Org Definition for Org Shape for options during the transition period.

Can I See the Org Shape File?

Org shapes are internal system files and aren’t viewable.

### Enable Org Shape for Scratch Orgs Enable Org Shape for Scratch Orgs in the org whose shape you want to capture (source org).

Org Shape Permissions
A Salesforce admin for the Dev Hub org must assign permissions to users who plan to create org shapes, or create scratch orgs based
on an org shape. If you already have a permission set for Salesforce DX users, you can update it to include access.

Create and Manage Org Shapes
Create an org shape to mimic the baseline setup (features, limits, edition, and Metadata API settings) of a source org without the
extraneous data and metadata. If the features, settings, or licenses of that org change, you can capture those updates by recreating
the org shape. You can have only one active org shape at a time. Org shapes are internal system files and aren’t viewable.

Scratch Org Definition for Org Shape
During org shape creation, we capture the features, settings, edition, licenses, and limits of the specified source org. This way, you
don’t have to manually include these items in the scratch org definition file. You can create a scratch org based solely on the source
org shape. Or you can add more features and settings in the scratch org definition file to include functionality not present in the
source org.

Troubleshoot Org Shape
Here are some issues you can encounter when using Org Shape for Scratch Orgs.

SEE ALSO:

_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_settings.htm)_ : Settings

### Enable Org Shape for Scratch Orgs Enable Org Shape for Scratch Orgs in the org whose shape you want to capture (source org).

Available in: Developer, Group, Professional, Unlimited, and Enterprise editions

Not available in: Scratch orgs and sandboxes

Be sure to:


### Scratch Orgs Org Shape Permissions

**•** Enable Org Shape for Scratch Orgs in both the source org and the Dev Hub org, if you want to capture the shape of an org that isn’t
also your Dev Hub org.

**•** When entering the org ID, use only the first 15 characters rather than the full 18-character org ID.

You can find the org ID in **Setup > Company Information** .

**1.** Enable Org Shape for Scratch Orgs in the Dev Hub org that you use to create scratch orgs. Contact a Salesforce admin if you require
assistance.

**a.** From Setup, enter _`Scratch Orgs`_ in the Quick Find box, then select **Scratch Orgs** .

**b.** Click the toggle for **Enable Org Shape for Scratch Orgs** .

**c.** In the text box, enter the 15-character org ID for the Dev Hub, then click **Save** .

**2.** (Optional) If the source org is different from the Dev Hub org, enable Org Shape for Scratch Orgs in the source org.

**a.** Log in to the source org.

**b.** From Setup, enter _`Scratch Orgs`_ in the Quick Find box, then select **Scratch Orgs** .

**c.** Click the toggle for **Enable Org Shape for Scratch Orgs** .

**d.** Enter the 15-character Dev Hub org ID that you’re using to create scratch orgs.

You can specify up to 50 Dev Hub org IDs to address these common use cases:

**•** You have multiple production orgs but your development team has access to only one. For the customization they're building, they
require the shape of another production org.

**•** Your developers use their own Dev Hub orgs and don't have access to the production org. However, they want to create scratch
orgs based on the shape of the production org.

**•** You're an ISV who uses your production org to create scratch orgs. You want to capture the shape of your first-generation packaging
org so you can build second-generation packages.

### Org Shape Permissions

A Salesforce admin for the Dev Hub org must assign permissions to users who plan to create org shapes, or create scratch orgs based
on an org shape. If you already have a permission set for Salesforce DX users, you can update it to include access.

You don’t require the “Modify All Records” permission to delete shapes created by others because there can be only one active shape
in the org at a time.


### Scratch Orgs Create and Manage Org Shapes

Supported Licenses

In addition to providing users with appropriate permissions, be sure to assign the Salesforce license to Org Shape users. Other user
licenses aren’t supported at this time.

SEE ALSO:

Add Salesforce DX Users

_[SOAP API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api.meta/api/sforce_api_objects_shaperepresentation.htm)_ : ShapeRepresentation

### Create and Manage Org Shapes

Create an org shape to mimic the baseline setup (features, limits, edition, and Metadata API settings) of a source org without the
extraneous data and metadata. If the features, settings, or licenses of that org change, you can capture those updates by recreating the
org shape. You can have only one active org shape at a time. Org shapes are internal system files and aren’t viewable.

An org shape captures Metadata API settings, not all metadata types. For example, customizations that appear in the org, such as
[Lightning Experience Themes, aren’t included as part of org shape. See Settings in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_settings.htm) _Metadata API Guide_ for the complete list.

[An org shape includes org preference and permissions. It doesn’t include data entries such as AddressSettings.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_addresssettings.htm)

Important: Scratch org shapes are associated with a specific Salesforce release. Be sure to recreate the org shape after the source
org is upgraded to the new Salesforce release.

**1.** Authorize both your Dev Hub org and the source org. Run this command for each org.

```
     sf auth web login --alias

```

**2.** Create the org shape for the source org. This command kicks off an asynchronous process to create the org shape.

```
     sf org create shape --target-org <source org username/alias>

     Successfully created org shape for 3SRB0000000TXbnOCG.

```

**3.** Check the status of the `shape:create` command.

```
     sf org shape list

     === Org Shapes

     ALIAS USERNAME ORG ID SHAPE STATUS CREATED BY CREATED DATE

     ───────────────────────────────────────────────────────────────────

     SrcOrg me@my.org 00DB1230000Ifx5MAC InProgress me@my.org 2020-08-06

```

You can use the org shape after the status is `Active` :

```
     === Org Shapes

     ALIAS USERNAME ORG ID SHAPE STATUS CREATED BY CREATED DATE

     ─────────────────────────────────────────────────────────────────────

     SrcOrg me@my.org 00DB1230000Ifx5MAC Active me@my.org 2020-08-06

```

If you run the `sf org create shape` command again for this org, the previous shape is marked inactive and replaced by a new
active shape.

If you don’t want to create scratch orgs based on this shape, you can delete the org shape. To delete an org shape:

```
   sf org delete shape --target-org <username/alias>

```


### Scratch Orgs Scratch Org Definition for Org Shape Scratch Org Definition for Org Shape

During org shape creation, we capture the features, settings, edition, licenses, and limits of the specified source org. This way, you don’t
have to manually include these items in the scratch org definition file. You can create a scratch org based solely on the source org shape.
Or you can add more features and settings in the scratch org definition file to include functionality not present in the source org.

Important: In the scratch org definition, indicate the 15-character `sourceOrg` instead of `edition` . The sourceOrg is the
org ID for the org whose shape you created. Use only the first 15 characters rather than the full 18-character org ID.

Simple Scratch Org Definition File

If your Dev Hub org, source org, and org shape are all on the same Salesforce version, you can use the simple scratch org definition.

```
   {

     "orgName": "Acme",

     "sourceOrg": "00DB1230400Ifx5"

   }

```

Scratch Org Definition File during Salesforce Release Transitions

During the Salesforce major release transition, your Dev Hub org and source org can be on different versions. If your Dev Hub org is on
a different version than your source org, add the `release` option to your scratch org definition file to create scratch orgs using the
org shape.

```
   {

     "orgName": "Acme",

     "sourceOrg": "00DB1230400Ifx5",

     "release": "previous"

   }

```

Scratch Org Definition File for DevOps Center

If you create a scratch org based on an org shape with DevOps Center enabled, we still require that you add the DevOps Center feature
and setting to the scratch org definition. We require that customers explicitly enable it for legal reasons as part of the DevOps Center
terms and conditions.

```
   {

      "orgName": "Acme",

      "sourceOrg": "00DB1230400Ifx5",

      "features": ["DevOpsCenter"],

      "settings": {

        "devHubSettings": {

           "enableDevOpsCenterGA": true

           }

```


### Scratch Orgs Troubleshoot Org Shape

```
        }

      }

```

Scratch Org Definition File with Other Features and Settings

To add features not captured by org shape, or to test features that your source org doesn't have, you can add more scratch org features
and Metadata API settings. Settings refer to the Settings metadata type, not all metadata types.

```
   {

     "orgName": "Acme",

     "sourceOrg": "00DB1230000Ifx5",

     "features": ["Communities", "ServiceCloud", "Chatbot"],

     "settings": {

       "communitiesSettings": {

         "enableNetworksEnabled": true

       },

       "mobileSettings": {

         "enableS1EncryptedStoragePref2": true

       },

       "omniChannelSettings": {

         "enableOmniChannel": true

       },

       "caseSettings": {

         "systemUserEmail": "support@acme.com"

       }

     }

   }

```

Next: Create a scratch org using the org shape scratch org definition file.

SEE ALSO:

_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_settings.htm)_ : Settings

### Troubleshoot Org Shape

Here are some issues you can encounter when using Org Shape for Scratch Orgs.

Some Features Not Captured by Org Shape

**Description:** Some features and settings aren’t enabled in the org shape, in many cases by design due to security or legal reasons.

**•** Chatbot

**•** DevOpsCenter

**•** MultiCurrency

**•** PersonAccounts

**Workaround:** Add them to the scratch org definition.

```
   {

      "orgName": "Acme",

      "sourceOrg": "00DB1230400Ifx5",

      "features": [”Chatbot”, "MultiCurrency", "DevOpsCenter"],

```


Scratch Orgs Troubleshoot Org Shape

```
      "settings":

       {

        "botSettings":

         "enableBots": true

       }

        "currencySettings":

         "enableMultiCurrency": true

       }

        "devHubSettings": {

         "enableDevOpsCenterGA": true

       }

     }

```

Some Field Service Features Aren't Enabled in Org Shape

**Description:** Even when the Field Service Enhanced Scheduling and Optimization, and Field Service Integration features are enabled
in the source org in which the org shape is created, these features aren’t enabled when creating a scratch org based on the org shape.

**Workaround:** Manually add the missing Field Service Metadata API settings to the scratch org definition depending on which features
are enabled in the source org.

Scenario 1: If the org shape included both the Field Service Enhanced Scheduling and Optimization, and Field Service Integration features,
manually add the Field Service Enhanced Scheduling and Optimization Metadata API setting, `o2EngineEnabled`, in the scratch
org definition file, which enables both features.

```
   "settings":

      {

      "fieldServiceSettings":

       {

        "fieldServiceOrgPref": true,

         "o2EngineEnabled": true

       }

      }

```

Scenario 2: If the org shape included only the Field Service Integration feature, manually add the Field Service Enhanced Scheduling and
Optimization Metadata API setting `optimizationServiceAccess`, to the scratch org definition file.

```
   "settings":

      {

      "fieldServiceSettings":

       {

        "fieldServiceOrgPref": true,

          "optimizationServiceAccess": true

       }

      }

```

DevOps Center Isn’t Enabled in a Scratch Org Based on an Org Shape

**Description:** Although DevOps Center is enabled in the source org, the scratch org created from the source org’s shape doesn’t have
DevOps Center enabled. The DevOps Center org preference is purposely toggled off. We require that customers explicitly enable it by
indicating the feature and setting in the scratch org definition file for legal reasons as part of the DevOps Center terms and conditions.

**Workaround:** Add the DevOps Center feature and setting to the scratch org definition file. See Scratch Org Definition for Org Shape for
details.


Scratch Orgs Troubleshoot Org Shape

ERROR running force:org:shape:list

**Description:** A trial org from which you created the org shape has expired. You could see either of these errors:

```
   ERROR running org list shape: Error authenticating with the refresh token due to: inactive

    user

   ERROR running org list shape: Error authenticating with the refresh token due to: expired

    access/refresh token

```

**Workaround:**

**•** Use `sf org logout` to log out and remove the expired org.

**•** Run `sf org list shape` again.

Can't create a Digital Experience Cloud Site Using Org Shape

**Description:** When you try to create a scratch org from an org shape that contains an Experience Cloud Site, you get an error.

```
   Required fields are missing: [Welcome Email Template, Change Password Email Template, Lost

    Password Template]

```

**Workaround:** None.

Error While Creating Scratch Org Using a Shape

**Description:** You see this error when creating a scratch org using a shape.

```
   ERROR running org create scratch: A fatal signup error occurred. Please try again.

   If you still see this error, contact Salesforce Support for assistance.

```

**Workaround:** Generate a new shape using the `org create shape` command, then try again.

Shift Status Picklists Aren’t Populated When Using a Shape With Field Service

**Description:** When you create a scratch org from a shape with Field Service enabled, the Status field picklist for Shifts is empty.

**Workaround:** Use an org shape with field service disabled, then enable field service in the scratch org definition file settings.

```
   {

    "orgName": "Acme",

    "sourceOrg": "00DB1230000Ifx5",

    "settings": {

      "fieldServiceSettings": {

         "fieldServiceOrgPref": true

      }

    }

   }

```

Org Shape Feature Accepts Only 15-Character Org IDs

**Description:** You can use only 15-character org IDs when enabling Org Shape for Scratch Orgs and specifying the source org in the
scratch org definition file. Org IDs are usually 18 characters long, which is what the `org list` command displays.

**Workaround:** Use only the first 15 characters of a standard 18-character org ID when working with the Org Shape feature.


## Scratch Orgs Create Scratch Orgs Create Scratch Orgs

Easily spin up a scratch org and open it directly from the command line.

Before you create a scratch org:

**•** Set up your Salesforce DX project

**•** Authorize the Dev Hub org

**•** Create the scratch org definition file (build your own or use an org shape)

You can create scratch orgs for different functions, such as for feature development, for development of packages that contain a
namespace, or for user acceptance testing.

Tip: Delete any unneeded or malfunctioning scratch orgs in the Dev Hub org or via the command line so that they don’t count
against your active scratch org allocations.

Indicate the path to the scratch definition file relative to your current directory. For sample repos and new projects, this file is located in
the `config` directory.

Ways to Create Scratch Orgs

Create a scratch org for development using a scratch org definition file, give the scratch org an alias, and indicate that this scratch org
is the default. Use the `--target-dev-hub` flag to specify your Dev Hub org’s username or alias; if you don’t specify this flag, the
command uses your default Dev Hub.

```
   sf org create scratch --definition-file config/project-scratch-def.json --alias MyScratchOrg

    --set-default --target-dev-hub MyHub

```

You can override many of the options in the user definition file by specifying the corresponding flag at the command line when you run
`org create scratch` . This technique allows multiple users or continuous integration jobs to share a base definition file and then
customize options when they run the command. This example overrides the adminEmail and edition options.

```
   sf org create scratch --definition-file config/project-scratch-def.json --admin-email

   me@email.com --edition developer

```

You’re not required to specify a definition file when you create a scratch org, as long as you specify the required flag `--edition` .

```
   sf org create scratch --edition developer

```

This example creates a scratch org from a snapshot with the specified name.

```
   sf org create scratch --snapshot dhsnapshot --wait 10 --target-dev-hub MyHub

```

This example creates a scratch org from an org shape with the specified ID.

```
   sf org create scratch --source-org 00DB1230000Ifx5

```

Create a scratch org for user acceptance testing or to test installations of packages. In this case, you don’t want to create a scratch org
with a namespace. You can use this command to override the namespace value in the scratch org definition file. This example also
specifies the scratch org’s duration, which indicates when the scratch org expires (in 1-30 days). The default duration is 7 days.

```
   sf org create scratch --definition-file config/project-scratch-def.json --no-namespace

   --duration-days 30

```


Scratch Orgs Create Scratch Orgs

Specify the Salesforce release for the scratch org. During the Salesforce release transition, you can specify the release (preview or previous)
when creating a scratch org. See Select the Salesforce Release for a Scratch Org for details.

```
   sf org create scratch --edition developer --release preview

```

Request a scratch org, but don’t wait for it complete, by specifying the `--async` flag.

```
   sf org create scratch --edition developer --async

```

The command displays a job ID that you pass to the `org resume scratch` command. Use this command to also resume a scratch
org creation that times out.

```
   sf org resume scratch --job-id 2SRB0000CSqdJOAT

```

Create a scratch org with source tracking disabled.

```
   sf org create scratch --definition-file config/project-scratch-def.json --no-track-source

```

View Scratch Org Creation Progress

While executing, the `org create scratch` command displays running information about the background processes. When the
command completes, it displays two important pieces of information: the org ID and the username.

```
    ──────────────Creating Scratch Org ──────────────

    � Prepare Request 11ms

    � Send Request 11.73s

    � Wait For Org - Skipped

    � Available 12ms

    � Authenticate 1.51s

    � Deploy Settings 2.14s

    � Done 0ms

    Request Id: 2SRWs000003y7mUOAQ (https://cbdocorg.my.salesforce.com/2SRWs000003y7mUOAQ)

    OrgId: 00DE200000DHqsM

    Username: test-lvsbbdryeaxn@example.com

    Alias: myscratch

    Elapsed Time: 15.40s

   Your scratch org is ready.

```

Open the Scratch Org

```
   sf org open --target-org test-st9thgoyyyq3@example.com

```

If you used the `--alias` flag to set an alias, you can use that value for `--target-org` .

```
   sf org open --target-org MyScratchOrg

```

Salesforce Release Transition Periods

Timing is everything during the Salesforce release transition period. During the transition period, you can intend to create a scratch org
on the current release but find that the scratch org is unexpectedly created on the preview release. If the instance on which the scratch


## Scratch Orgs Scratch Org Snapshots

is created transitions to the preview release after the creation request is initiated, the scratch org is created on the preview version instead
of the current version. During this transition period, there’s no way to know when the sandbox (CS) instance will be upgraded.

If you open the scratch org and it isn’t on the expected version, you have some options. See “How Release Transitions Can Affect the
Scratch Org Version” in Select the Salesforce Release for a Scratch Org.

Troubleshooting Tips

If the create command runs into an error, it’s not always clear if the scratch org was created. Issue this command on your Dev Hub org
to see if it returns the scratch org ID, which confirms the existence of a scratch org that was created today and owned by you:

```
   sf data query --query "SELECT ID, Name, Status FROM ScratchOrgInfo WHERE CreatedBy.Name =

    ' <your name> ' AND CreatedDate = TODAY" --target-org <Dev Hub org>

```

Use this information to determine if the creation actually worked. For example, let’s say your name is Jane Doe, and you created an alias
for your Dev Hub org called DevHub:

```
   sf data query --query "SELECT ID, Name, Status FROM ScratchOrgInfo WHERE CreatedBy.Name =

    'Jane Doe' AND CreatedDate = TODAY" --target-org DevHub

```

SEE ALSO:

[ScratchOrgInfo sObject API Reference](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_scratchorginfo.htm)

Project Setup

Authorization

Build Your Own Scratch Org Definition File

Deploy Source From Your Project to the Scratch Org

_VS Code Command_ [: SFDX: Create a Default Scratch Org](https://developer.salesforce.com/docs/platform/sfvscode-extensions/guide/vscode-overview.html)

## Scratch Org Snapshots

Capture the state of a scratch org’s configuration so that you can use it to create scratch org replicas. A snapshot is a point-in-time copy
of a scratch org that includes installed packages, features, limits, licenses, metadata, and data.

Configuring a scratch org with a project’s dependencies can be a manual and time-consuming process. It can require deploying dependent
metadata to it, seeding it with sample data, installing one or more packages, and then performing manual tasks directly in the scratch
org. And then, poof, the scratch org expires, and you have to start all over again. With scratch org snapshots, you can quickly replicate
scratch orgs with the required project dependencies.

How Snapshots Fit in the Development Lifecycle

Because a snapshot is a point-in-time copy of your scratch org, it’s static. To update your snapshot, delete it and create another snapshot.

You can create a snapshot from only a scratch org and, conversely, you can create only scratch orgs from a snapshot. Snapshots have
the same 200-MB data storage limit as scratch orgs. A snapshot isn’t meant to replace source-driven development or a version control
system. You continue to follow best development practices by externalizing and modularizing your project source.

Snapshots and scratch orgs don’t replace sandboxes for user acceptance testing. A snapshot is intended to contain the static dependencies
of a project, and not the entire happy soup of your production org.


Scratch Orgs Scratch Org Snapshots

Snapshot Allocations and Limits

Snapshots are associated with a Dev Hub org. Therefore, you must use the same Dev Hub org when you create the scratch org from the
snapshot.

**•** The number of snapshots you can create is the same as the active scratch org allocation based on edition type.

**•** Snapshots expire after 90 days. When a snapshot expires or is deleted, its status is updated automatically and its license becomes
immediately available.

**•** Snapshot data is retained for 100 days. When a snapshot expires, it’s associated data is deleted 10 days later. If a snapshot is deleted,
its associated data is deleted 100 days after its creation date.

To view your snapshot usage with Salesforce CLI, run:

```
   sf org list limits -o <Dev Hub username or alias>

```

Look for these values in the output:

```
   Name Remaining Max

   ────────────────────────────── ─────────

   ActiveOrgSnapshots 38 40

   DailyOrgSnapshots 35 40

```

Unsupported Features

These features aren’t copied to the snapshot because they risk exposing sensitive data or authentication secrets.

**•** Connected apps

**•** External credentials

**•** Named credentials

Get Started with Scratch Org Snapshots
Install the required Salesforce DX tools, then enable Dev Hub and Scratch Org Snapshots in an org, usually your production org.

Salesforce CLI Snapshot Commands
You must use Salesforce CLI commands to create and manage your scratch org snapshots.

Create a Scratch Org Snapshot
You can create a snapshot if the source scratch org wasn’t created using a snapshot or with a namespace.

Create a Snapshot for Use with Namespaced Scratch Orgs
While you can't use a namespaced scratch org to create a snapshot, you can create a namespaced scratch org from a snapshot. That
way, you can deploy namespaced metadata to the scratch org. Snapshots are intended to include only dependent packages,
metadata, and test data.


### Scratch Orgs Get Started with Scratch Org Snapshots

Create a Scratch Org Based on a Snapshot
The snapshot must belong to the Dev Hub that you’re using to create the scratch org. We recommend that you create a scratch org
definition file that references the snapshot, although you can also reference it directly with the `--snapshot` flag of `org create`
`scratch` . Changing or deleting a scratch org has no effect on a snapshot.

Create a Package Version Based on a Snapshot
If you’re a partner or ISV who builds second-generation managed packages that depend on base packages, you can create package
versions significantly faster by using scratch org snapshots. Using a snapshot to create a package version is a great choice if your
dependent base packages are stable.

Manage and Maintain Your Snapshots
You can check the status of snapshot creation, list all snapshots, and delete a snapshot.

### Get Started with Scratch Org Snapshots

Install the required Salesforce DX tools, then enable Dev Hub and Scratch Org Snapshots in an org, usually your production org.

**•** [Install Salesforce CLI.](https://developer.salesforce.com/tools/salesforcecli)

**•** [Enable Dev Hub in your production org.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_setup_enable_devhub.htm)

**•** [Authorize your Dev Hub org. The Dev Hub org is the org you use to create and manage scratch orgs.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_auth.htm)

**•** Enable Scratch Org Snapshots in the Dev Hub org.

**•** Provide users with permissions to create snapshots.

#### Enable Scratch Org Snapshots in the Dev Hub Org

A snapshot must belong to the Dev Hub org that you’re using to create the scratch orgs.

#### Assign a License and Permissions to Snapshot Users

Provide all non-admin Scratch Org Snapshots users with a supported license and access to the required scratch org and snapshot
objects. Dev Hub (production org) admins can create and manage snapshots by default.

#### Enable Scratch Org Snapshots in the Dev Hub Org

A snapshot must belong to the Dev Hub org that you’re using to create the scratch orgs.

**1.** Log into your Dev Hub org as the admin user.

**2.** From Setup, enter _`Scratch Orgs`_ in the Quick Find box, then select **Scratch Orgs** .

#### 3. Click to enable Enable Scratch Org Snapshots . Assign a License and Permissions to Snapshot Users

Provide all non-admin Scratch Org Snapshots users with a supported license and access to the
required scratch org and snapshot objects. Dev Hub (production org) admins can create and manage
snapshots by default.

**1.** Log in to your Dev Hub org as the admin user.

**2.** Assign to each snapshot user a Salesforce, Salesforce Platform, or Salesforce Limited Access license.

**3.** In Setup, create a permission set or select an existing one.

**4.** From the permission set’s Object Settings, select **Org Snapshots**, then click **Edit** .


EDITIONS

Available in: **Developer**,
**Enterprise**, **Group**,
**Professional**, and **Unlimited**
editions

Not available in: Scratch
orgs and sandboxes

### Scratch Orgs Salesforce CLI Snapshot Commands a. Under Object Permissions, select Read, Create, and Delete .

**b.** (Optional) Add these object permissions to the permission set.

**•** To allow users to see snapshots that other users create, select **View All Records** .

**•** To allow users to delete snapshots that other users create, select **Modify All Records** (Salesforce license only).

**5.** If snapshot users don’t already have access to the required scratch org objects (Scratch Org Info and Active Scratch Orgs) through
another permission set, include access to them in this permission set.

See _Required Permissions for Scratch Orgs_ in Create and Assign a Permission Set to Developer Users for details.

**6.** Save your changes.

**7.** Click **Manage Assignments**, then **Add Assignment** .

**8.** Select the users, click **Next**, and optionally set an expiration date.

**9.** Click **Assign**, then **Done** .

### Salesforce CLI Snapshot Commands

You must use Salesforce CLI commands to create and manage your scratch org snapshots.

```
   org create snapshot
```

Create a snapshot of a scratch org.

```
   org delete snapshot
```

Delete a scratch org snapshot.

```
   org get snapshot
```

Get details about a scratch org snapshot.

```
   org list snapshot
```

List scratch org snapshots that belong to the specified Dev Hub org.

Get Help in the Terminal for Command Syntax

The `--help` and `-h` flags enable you to get varying levels of help (comprehensive or abbreviated) right in the command window:

Example:

```
   sf org create snapshot --help

### Create a Scratch Org Snapshot

```

You can create a snapshot if the source scratch org wasn’t created using a snapshot or with a namespace.

Before you begin:

**•** Enable Dev Hub in your production org, or another org you use to create scratch orgs.

**•** Enable Scratch Org Snapshots in the Dev Hub org.

**•** Be sure that non-admin users have the proper permissions to use scratch orgs and snapshots. See Assign a License and Permissions
to Snapshot Users for details.

A snapshot captures the state of a scratch org at a point in time. To update your snapshot, delete it and create another snapshot. Unlike
an org shape, a snapshot includes installed packages, metadata, and data. The time to create a snapshot depends on the size of the
source scratch org. To speed up snapshot creation time, include only what’s necessary for your project.


### Scratch Orgs Create a Snapshot for Use with Namespaced Scratch Orgs

Note: If you continue to modify the source scratch org after you run the snapshot command, not all the modifications will be
reflected in the snapshot. Instead, complete the configuration of the source scratch org before creating the snapshot.

Command syntax:

```
   sf org create snapshot --name <name> --source-org <ID or alias of scratch org> \

   --target-dev-hub <username or alias of Dev Hub org> --description <text>

```

A snapshot name can have a maximum length of 15 characters. It can contain only alphanumeric characters (no special characters or
spaces, even if the name is surrounded by quotation marks during creation).

Tip: To view the aliases, usernames, and IDs of your authenticated orgs and scratch orgs, run the `org list` command.

Example:

```
   sf org create snapshot --name dhsnapshot --source-org dreamhouse-scratch \

   --target-dev-hub my-dev-hub --description "Dreamhouse app"

```

Your request is initially InProgress:

```
   Name Value

   ────────────────── ────────────────────

   Id 0Oo1Q0000004C93SXX

   Snapshot Name dhsnapshot

   Description Dreamhouse app

   Status InProgress

   Source Org 00D050000004ipAEXX

   Created Date 09/22/2023, 02:07 PM

   Last Modified Date 09/22/2023, 02:07 PM

   Expiration Date 2023-12-21

```

To check the status of the request, see Manage and Maintain Your Snapshots.

### Create a Snapshot for Use with Namespaced Scratch Orgs

While you can't use a namespaced scratch org to create a snapshot, you can create a namespaced scratch org from a snapshot. That
way, you can deploy namespaced metadata to the scratch org. Snapshots are intended to include only dependent packages, metadata,
and test data.

**1.** Create and register the namespace in the Dev Hub org and add it to the `sfdx-project.json` file.

**2.** When you create the scratch org that you plan to use as the source of the snapshot, be sure to indicate the `--no-namespace`
flag.

**3.** Create the scratch org snapshot.

**4.** Create a scratch org based on the snapshot.

The resulting scratch org has a namespace, which means that any unpackaged metadata from the snapshot is now namespaced in
the resulting scratch org.

SEE ALSO:

[Link a Namespace to a Dev Hub Org](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_reg_namespace.htm)


### Scratch Orgs Create a Scratch Org Based on a Snapshot Create a Scratch Org Based on a Snapshot

The snapshot must belong to the Dev Hub that you’re using to create the scratch org. We recommend that you create a scratch org
definition file that references the snapshot, although you can also reference it directly with the `--snapshot` flag of `org create`
`scratch` . Changing or deleting a scratch org has no effect on a snapshot.

Create the Scratch Org Definition File

The scratch org definition file is the blueprint for your scratch org. It’s likely that your snapshot includes all the required features and
settings to configure the scratch orgs created from it.

Using our Dreamhouse scratch org as an example, let’s create a scratch org definition file called `dhsnapshot-scratch-def.json`
that contains only two entries: `orgName` and `snapshot`, which is the name you gave the snapshot when you created it.

Important: Be sure you use the `snapshot` option instead of `edition` in the scratch org definition file.

```
   {

     "orgName": "Salesforce",

     "snapshot": "dhsnapshot"

   }

```

When creating the scratch org definition file, don’t include these options:

**•** edition

**•** features

**•** hasSampleData

**•** release

**•** sourceOrg

Add Settings to the Scratch Org Definition File to Override Default Snapshot Settings

Some scratch org settings aren’t inherited from the org snapshot. In these cases, you can add these settings in the scratch org definition
file to achieve the desired scratch org configuration when creating a scratch org from a snapshot.

This example scratch org definition file illustrates adding some scratch org settings, in the event that these settings weren’t inherited
from the scratch org snapshot.

```
   {

     "orgName": "Salesforce",

     "snapshot": "dhsnapshot",

     "settings": {

      "activitiesSettings": {

       "enableCalendarHomeLWC": false

      },

      "omniChannelSettings": {

       "enableOmniSkillRouting": true

       "enableOmniChannel": true

      },

      "experienceBundleSettings": {

       "enableExperienceBundleMetadata": true

      },

      "oauthOidcSettings": {

       "blockOAuthUnPwFlow": true

```


Scratch Orgs Create a Scratch Org Based on a Snapshot

```
      },

      "mobileSettings": {

       "enableS1EncryptedStoragePref2": false

      },

      "securitySettings": {

       "lockerServiceNext": false

      }

     }

   }

```

Create the Scratch Org Based On Your Snapshot

It can take Salesforce longer to create a scratch org from a snapshot, so we suggest you increase the `--wait` value so the command
doesn’t time out. Remember to set the `--target-dev-hub` flag to the same Dev Hub org associated with the snapshot.

For example:

```
   sf org create scratch --definition-file config/dhsnapshot-scratch-def.json \

   --alias dh-scratch-ci --wait 10 --target-dev-hub my-dev-hub

```

This example shows how to use the `--snapshot` flag to directly reference the snapshot without using a defintion file.

```
   sf org create scratch --snapshot dhsnapshot \

   --alias dh-scratch-ci --wait 10 --target-dev-hub my-dev-hub

```

You can indicate whether the scratch org you create from the snapshot has a namespace, which is important if you’re using scratch orgs
for second-generation package development.

**•** Define a namespace in the `sfdx-project.json` file. The resulting scratch org has a namespace, which means that any
unpackaged metadata from the snapshot is now namespaced in the resulting scratch org.

**•** Use the `--no-namespace` flag to ensure the resulting scratch org doesn’t have a namespace, even if you have a namespace
specified in the `sfdx-project.json` file.

Success! Development and testing with scratch orgs just got a whole lot easier.

Note: To minimize the time to create a scratch org, some scratch orgs based on snapshots can be created from a pool of orgs
that are preconfigured for creation. If a scratch org based on a snapshot is created from this pool, the scratch org information
shows that it was created by a role called Pooled Org Admin, rather than the user who created the scratch org.

Determine the Release Version for the Resulting Scratch Org

Normally, a scratch org is created on the same release version as the Dev Hub org regardless of how the scratch org was created: using
the standard method, an org shape, or a snapshot. However, during Salesforce Preview, a scratch org can be created on a different release
version from the Dev Hub org, if the snapshot release version differs from the Dev Hub’s release version.

During the Salesforce release transition, release version differences can occur for these scenarios:

**•** The Dev Hub org is on the current generally available Salesforce release, but the snapshot is created on the preview release version.

**•** The Dev Hub has upgraded to the preview release, but the snapshot was created on the current release version.

In cases where the Dev Hub org and snapshot release versions differ, the resulting scratch org is created on the same release version as
the snapshot, as illustrated in this table.


### Scratch Orgs Create a Package Version Based on a Snapshot

Snapshot Error Codes

[See Scratch Org Error Codes for details.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_scratch_orgs_error_codes.htm)

### Create a Package Version Based on a Snapshot

If you’re a partner or ISV who builds second-generation managed packages that depend on base packages, you can create package
versions significantly faster by using scratch org snapshots. Using a snapshot to create a package version is a great choice if your dependent
base packages are stable.

What Are the Benefits of Using a Snapshot When Developing a Package Version?

A snapshot includes all the dependencies and configurations required for your package. When you run the `package version`
`create` CLI command, we create a scratch org behind the scenes. That scratch org serves as a build org where we build your package.
In the build org we install the dependent packages you specified, and deploy the package metadata for the package version you're
creating.

If you install your dependent packages in the scratch org before you create the snapshot, and specify the snapshot when you create a
package version, the package build process bypasses these steps. Meaning, we don't install the dependent packages into the build org,
but use the snapshot instead. If you don’t use a snapshot, those dependent packages have to be installed each time you create a package
version, which can greatly prolong package creation times.

[For a more detailed explanation, see Second-Generation Managed Packaging Guide: When to Use Scratch Org Snapshots in Package](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/dev2gp_so_when_use_snapshot.htm)
[Development.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/dev2gp_so_when_use_snapshot.htm)

Why Can’t I Promote a Package Version Based on a Snapshot?

Using snapshots to create package versions speeds up the package development and testing process. However, a scratch org snapshot
could contain unpackaged metadata that’s not associated with the package. For example, if you’re an ISV that created a package version
with unpackaged metadata in a snapshot, it’s likely that your customers could encounter installation issues when you perform a push
upgrade to orgs that don’t contain the dependent metadata.

To ensure your package version is ready to release and doesn’t contain any unintended dependencies, you must build a package version
without a snapshot.

[Note: You can promote an unlocked package based on a snapshot. Only managed packages based on snapshots can’t be](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_unlocked_pkg_intro.htm)
promoted to the released state.

How Do I Create a Package Version Based on Snapshot?

[See Second-Generation Managed Packaging Guide: Create a Package Version Based on a Scratch Org Snapshot.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/dev2gp_so_pkg_snapshot.htm)


### Scratch Orgs Manage and Maintain Your Snapshots Manage and Maintain Your Snapshots

You can check the status of snapshot creation, list all snapshots, and delete a snapshot.

Check the Status of a Snapshot Creation

Creating a snapshot can take a while. Use the snapshot name or ID to check its creation status.

```
   sf org get snapshot --snapshot <name or ID> --target-dev-hub <username or alias>

```

For example:

```
   sf org get snapshot --snapshot dhsnapshot --target-dev-hub my-dev-hub

```

After the status changes to `Active`, you can use the snapshot to create scratch orgs.

```
   Name Value

    ────────────────── ────────────────────

    Id 0Oo1Q0000004C93SXX

    Snapshot Name dhsnapshot

    Description Dreamhouse app

    Status Active

    Source Org 00D050000004ipAEXX

    Created Date 09/22/2023, 02:07 PM

    Last Modified Date 09/22/2023, 02:14 PM

    Expiration Date 2024-09-21

    Last Cloned Date

    Last Cloned By Id

```

List All Scratch Org Snapshots

You can view all the snapshots in a Dev Hub org that you have access to. If you’re an admin, you can see all snapshots associated with
the Dev Hub org. If you’re a user, you can see only your snapshots, unless a Dev Hub admin gives you View All Records permissions.

```
   sf org list snapshot --target-dev-hub <username or alias>

```

Delete a Scratch Org Snapshot

If you don’t need a snapshot anymore or run out of active snapshots, you can delete a snapshot. Dev Hub admins can delete any snapshot,
while users can delete only their snapshots unless a Dev Hub admin gives the user Modify All Records permissions. Deleting a snapshot
frees up a license to create an additional snapshot, but the associated data is retained for 100 days after the snapshot was created.

This example identifies the snapshot for deletion by snapshot name.

```
   sf org delete snapshot --snapshot dhsnapshot --target-dev-hub my-dev-hub

```

This example identifies the snapshot for deletion by snapshot ID.

```
   sf org delete snapshot --snapshot 0OoWt00000000A1BCD --target-dev-hub my-dev-hub

## Select the Salesforce Release for a Scratch Org

```

During the Salesforce release transition, you can specify the release (preview or previous) when creating a scratch org.


Scratch Orgs Select the Salesforce Release for a Scratch Org

What Is Salesforce Preview?

During every major Salesforce release, you can get early access to the upcoming release in your scratch orgs and sandboxes to test new
customizations and features before your production org is upgraded. This window is called the Salesforce Preview. Scratch orgs created
on the upcoming release are called preview scratch orgs.

Normally, you create scratch orgs that are the same version as the Dev Hub. However, during the major Salesforce release transition that
happens three times a year, you can select the Salesforce release version `Preview` or `Previous`, based on the version of your Dev
Hub.

To try out new features in an upcoming release, you no longer have to create a trial Dev Hub on the upcoming version to create preview
scratch orgs. You can use your existing Dev Hub that includes your existing scratch org active and daily limits.

For example, you can select a version over the next three releases during these release transition dates. Preview start date is when
sandbox instances are upgraded. Preview end date is when all instances are on the GA release.

Because _previous_ and _preview_ are relative terms, your Dev Hub org version during the release transition determines their relative
significance. Here’s what happens when you try to create a scratch org with one of the release values.

Note: If you don’t specify a release value, the scratch org version is the same version as the Dev Hub org.

Create a Scratch Org for a Specific Release

You can specify the release version in the scratch org definition file or directly on the command line. Any value you set on the command
line overrides what you have defined in your scratch definition file.

**•** [Find out which instance your Dev Hub org is on: https://status.salesforce.com.](https://status.salesforce.com)

**•** Add the release option (lowercase) to your scratch org definition file.

```
     {

       "orgName": "Dreamhouse",

       "edition": "Developer",

       "release": "preview",

       "settings": {

         "mobileSettings": {

           "enableS1EncryptedStoragePref2": true

```


Scratch Orgs Select the Salesforce Release for a Scratch Org

```
         }

       }

     }

```

Alternatively, you can specify the release value directly on the command line with the `--release` flag. Any value you specify on
the command line overrides the value in the scratch org definition.

**•** Create the scratch org by executing the `org create scratch` command in a terminal (macOS and Linux) or command
prompt (Windows).

In this example, we’re creating a scratch org on the preview release.

```
     sf org create scratch --definition-file config/project-scratch-def.json --alias PreviewOrg

      --target-dev-hub DevHub --release preview

```

Be sure to set the `apiVersion` to match the scratch org version.

To set it globally for all DX projects:

```
   sf config set org-api-version 59.0 --global

```

To set it on the command line:

```
   SF_ORG_API_VERSION=59.0 sf org create scratch --definition-file

   config/project-scratch-def.json --alias PreviewOrg --target-dev-hub DevHub --release preview

```

Note: Regardless of the release version of your Dev Hub, you can use scratch org features that are available in the release (preview
or previous) of the scratch org you create.

How Release Transitions Can Affect the Scratch Org Version

During a Salesforce major release transition, the sandbox (CS) instances on which scratch orgs are created transition to the preview
release before your Dev Hub org does. During this transition period, you can intend to create a scratch org on the current generally
available release but unexpectedly discover that it was created on the preview release. Sandbox instances begin to transition to the
preview release several days before the preview start date. If the instance on which the scratch org is created transitions to the preview
release after the creation request is initiated, the scratch org is created on the preview version instead of the current version.

During this transition period, there’s no way to know when the sandbox instance will be upgraded. If the scratch org must be on the
current release, you can try these options:

**•** If it’s a day or two before the preview start date, recreate the scratch org. If the scratch org is again created on the preview release,
contact Salesforce Customer Support and open a case.

**•** Wait to create the scratch org until after the preview start date, and indicate `previous` as the release value in the scratch org
definition file.

What If I Want to Create a Pre-Release Scratch Org?

Pre-release is a very early build of the latest version of Salesforce that’s available before Salesforce Preview. It's not built to handle scale
and doesn't come with any Salesforce Support service-level agreements (SLAs). For this reason, the only way to create a pre-release
[scratch org is to sign up for a pre-release trial Dev Hub org (subject to availability).](https://sfdc.co/RR-Pre-Release)

SEE ALSO:

_VS Code Command_ [: SFDX: Create a Default Scratch Org](https://developer.salesforce.com/docs/platform/sfvscode-extensions/guide/vscode-overview.html)


## Scratch Orgs Deploy Source From Your Project to the Scratch Org Deploy Source From Your Project to the Scratch Org

After changing the source, you can sync the changes to your scratch org by deploying the changed source to it with the `project`
`deploy start` command.

Note: Scratch orgs have source tracking enabled by default. But sometimes you don’t want source tracking, such as in a continuous
integration environment when you want to speed up deployments. You can opt out of source tracking when you create the scratch
org by specifying the `--no-track-source` flag.

```
      sf org create scratch --definition-file config/project-scratch-def.json --no-track-source

```

See Create Scratch Orgs for more reasons to disable source tracking.

