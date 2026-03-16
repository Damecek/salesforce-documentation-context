[While there are restrictions on what changes are allowed in a patch version, determining what qualifies as a major or minor change is](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_create_patch_version.htm)
largely up to you. When introducing major changes, increase the major version number, and increase the minor version number when
making smaller improvements.

### Code Coverage for Unlocked Packages

Before you can promote and release an unlocked package, the Apex code must meet a minimum 75% code coverage requirement. You
can install package versions that don't meet code coverage requirements only in scratch orgs and sandboxes.


### Unlocked Packages Considerations for Promoting Packages with Dependencies

Important: Unlocked package versions that were promoted to the released state before Winter ‘21 aren’t subject to code coverage
requirements.

To compute code coverage using Salesforce CLI, use the `--code-coverage` parameter when you run the `sf package`
`version create` command.

Package version creation can take longer to complete when code coverage is being computed, so consider when in the development
cycle to include the code coverage parameter. You can choose to skip code coverage, and you can skip all validation by specifying the
`--skip-validation` parameter. You can promote package versions only if they’re validated and meet code coverage requirements.

View code coverage information for a package version using `sf package version list` with the `--verbose` parameter,
or the `sf package version report` command in Salesforce CLI.

We don’t calculate code coverage for org-dependent unlocked packages.

### Considerations for Promoting Packages with Dependencies

If your company is developing a package that has a package dependency, ask yourself these questions before promoting (releasing) a
new package version.

Are you:

**•** Developing the base and extension package in parallel?

**•** Specifying skip validation when creating new package versions?

**•** Using the keywords `LATEST` or `RELEASED` when specifying the package dependency?

If you answered no to all these questions, your package doesn't have any tricky dependency scenarios and you can promote it when it's
ready. If you answered yes to any of these questions, keep reading.

Specifying Skip Validation

[When you create a package version and specify skip validation, the version is created without validating dependencies, package ancestors,](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_create_pkg_ver.htm)
or metadata.

If you develop your base package using skip validation, test your extension package using either a stable and previously promoted
version of the base package, or a non-skip validated base package version.

Most importantly, if you’re developing a version of your base package and extension package in parallel, ensure that you:

**•** First promote the base package version.

**•** Then specify the promoted package version in the dependency section of your extension package using the keyword `RELEASED` .

**•** Finally, create the extension package version.

After testing the extension package version, you then promote it. This process ensures that the extension package version that you
promote to the released state has as its dependency the promoted base package version.

Using the Keyword LATEST or RELEASED

A keyword is a variable that you can use to specify a package version number. The keyword `LATEST` maps to the most recently created
package version, which might not be the same as the promoted and released package version.

The keyword `RELEASED` maps to the promoted and released package version.

For example: If you create versions 1.0.0.1, 1.0.0.2, and 1.0.0.3, and promote version 1.0.0.2, then 1.0.0.RELEASED = 1.0.0.2, but 1.0.0.LATEST
= 1.0.0.3.


### Unlocked Packages Release an Unlocked Package

Example

Your company created a base package called PkgBase, and an extension package called PkgExtn.

PkgBase is under active development, and the development team is creating versions that specify `--skip-validation` .

PkgExtn version 2.3 is under active development and references its dependency on PkgBase by using the following definition in the
`sfdx-project.json` .

```
     {

         "path": "pkg-extension",

         "default": false,

         "package": "PkgExtn",

         "versionName": "v 2.3",

         "versionDescription": "Winter 2025",

         "versionNumber": "2.3.0.NEXT",

         "dependencies": [

           {

            "package": "PkgBase",

            "versionNumber": "1.1.0.LATEST"

           },

```

Before promoting version 2.3 of PkgExtn, you must test it using the promoted version 1.1.0 of PkgBase. Update the PkgExtn dependency
section of your `sfdx-project.json` and change the dependency from 1.1.0.LATEST to 1.1.0.RELEASED. If the tests succeed, then
create a new version of PkgExtn and ensure it works as expected with the promoted base package version.

### Release an Unlocked Package

Each new package version is marked as beta when its created. As you develop your package, you may create several package versions
before you create a version that is ready to be released and installed in production orgs.

Before you promote the package version, ensure that the user permission, **Promote a package version to released**, is enabled in the
Dev Hub org associated with the package. Consider creating a permission set with this user permission, and then assign the permission
set to the appropriate user profiles.

When you’re ready to release, use `sf package version promote` .

```
   sf package version promote --package "Expense Manager@1.3.0-7"

```

If the command is successful, a confirmation message appears.

```
   Successfully promoted the package version, ID: 04tB0000000719qIAA to released.

```

After the update succeeds, view the package details.

```
   sf package version report --package "Expense Manager@1.3.0.7"

```

Confirm that the value of the Released property is `true` .

```
   === Package Version

   NAME VALUE

   ────────────────────────────── ───────────────────

   Name ver 1.0

   Alias Expense Manager-1.0.0.5

   Package Version Id 05iB0000000CaahIAC

   Package Id 0HoB0000000CabmKAC

```


### Unlocked Packages Update an Unlocked Package Version

```
   Subscriber Package Version Id 04tB0000000NPbBIAW

   Version 1.0.0.5

   Description update version

   Branch

   Tag git commit id 08dcfsdf

   Released true

   Created Date 2018-05-08 09:48

   Installation URL

   https://login.salesforce.com/packaging/installPackage.apexp?p0=04tB0000000NPbBIAW

```

You can promote and release only once for each package version number, and you can’t undo this change.

### Update an Unlocked Package Version

You can update most properties of a package version from the command line. For example, you can change the package version name
or description. One important exception is that you can’t change the release status.

If the most recent package version has been released, increment either the major, minor, or patch version number for the next package
version you create.

Package version numbers use the format major.minor.patch.build. For example, if you released package 1.0.0.2, you could use 1.1.0.0,
2.0.0.0, or 1.0.1.0 for the next package version.

Example:

```
   sf package version update --package "Your Package Alias"

### Hard-Deleted Components in Unlocked Packages

```

When these components are removed from an unlocked package, they're hard deleted from the target install org during the package
upgrade.

**•** AccountForecastSettings

**•** AcctMgrTargetSettings

**•** ActionableListDefinition

**•** ActionPlanTemplate

**•** AccountingFieldMapping

**•** AccountingModelConfig

**•** AdvAccountForecastSet

**•** AdvAcctForecastDimSource

**•** AdvAcctForecastPeriodGroup

**•** AIApplicationConfig

**•** AIUsecaseDefinition

**•** AnalyticSnapshot

**•** ApexClass

**•** ApexComponent

**•** ApexPage

**•** ApexTrigger

**•** ApplicationRecordTypeConfig


Unlocked Packages Hard-Deleted Components in Unlocked Packages

**•** ApplicationSubtypeDefinition

**•** AppointmentAssignmentPolicy

**•** AssessmentQuestion

**•** AssessmentQuestionSet

**•** AssistantContextItem

**•** AssistantSkillQuickAction

**•** AssistantSkillSobjectAction

**•** AssistantVersion

**•** AuraDefinitionBundle

**•** BatchCalcJobDefinition

**•** BatchProcessJobDefinition

**•** BenefitAction

**•** BldgEnrgyIntensityCnfg

**•** BrandingSet

**•** BriefcaseDefinition

**•** BusinessProcessGroup

**•** BusinessProcessTypeDefinition

**•** CareBenefitVerifySettings

**•** CareLimitType

**•** CareProviderSearchConfig

**•** CareRequestConfiguration

**•** ChannelObjectLinkingRule

**•** ClaimFinancialSettings

**•** ClauseCatgConfiguration

**•** CompactLayout

**•** ContractType

**•** ConversationVendorInfo

**•** CustomApplication

**•** CustomPageWebLink

**•** CustomPermission

**•** CustomTab

**•** Dashboard

**•** DecisionMatrixDefinition

**•** DecisionMatrixDefinitionVersion

**•** DecisionTable

**•** DecisionTableDatasetLink

**•** DisclosureDefinition

**•** DisclosureDefinitionVersion

**•** DisclosureType

**•** DiscoveryAIModel


Unlocked Packages Hard-Deleted Components in Unlocked Packages

**•** DiscoveryGoal

**•** Document

**•** DocumentGenerationSetting

**•** DocumentType

**•** EmailServicesFunction

**•** EmailTemplate

**•** EmbeddedServiceBranding

**•** EmbeddedServiceConfig

**•** EmbeddedServiceLiveAgent

**•** EmbeddedServiceMenuSettings

**•** ESignatureConfig

**•** ESignatureEnvelopeConfig

**•** ExplainabilityActionDefinition

**•** ExplainabilityActionVersion

**•** ExplainabilityMsgTemplate

**•** ExpressionSetDefinition

**•** ExpressionSetDefinitionVersion

**•** ExpressionSetObjectAlias

**•** ExternalAIModel

**•** ExternalClientApplication

**•** ExtlClntAppMobileSettings

**•** ExtlClntAppOauthSettings

**•** ExternalDataSrcDescriptor

**•** ExternalServiceRegistration

**•** FeatureParameterBoolean

**•** FeatureParameterDate

**•** FeatureParameterInteger

**•** FieldRestrictionRule

**•** FieldServiceMobileExtension

**•** FlexiPage

**•** Flow

**•** FuelType

**•** FuelTypeSustnUom

**•** GatewayProviderPaymentMethodType

**•** HomePageComponent

**•** HomePageLayout

**•** IdentityVerificationProcDef

**•** InstalledPackage

**•** IntegrationHubSettings

**•** IntegrationHubSettingsType


Unlocked Packages Hard-Deleted Components in Unlocked Packages

**•** IntegrationProviderDef

**•** Layout

**•** Letterhead

**•** LicenseDefinition

**•** LightningComponentBundle

**•** LightningExperienceTheme

**•** LightningMessageChannel

**•** LightningOnboardingConfig

**•** ListView

**•** LiveChatAgentConfig

**•** LiveChatButton

**•** LiveChatSensitiveDataRule

**•** LocationUse

**•** LoyaltyProgramSetup

**•** MarketingAppExtActivity

**•** MarketingAppExtension

**•** MatchingRule

**•** MfgProgramTemplate

**•** MLDataDefinition

**•** MLPredictionDefinition

**•** NamedCredential

**•** NetworkBranding

**•** ObjectHierarchyRelationship

**•** OcrSampleDocument

**•** OcrTemplate

**•** OmniDataTransform

**•** OmniIntegrationProcedure

**•** OmniScript

**•** OmniUiCard

**•** PaymentGatewayProvider

**•** PermissionSet

**•** PermissionSetGroup

**•** PermissionSetLicense

**•** PipelineInspMetricConfig

**•** PlatformEventSubscriberConfig

**•** ProductAttributeSet

**•** ProductSpecificationTypeDefinition

**•** Profile

**•** QuickAction

**•** RecordAlertCategory


Unlocked Packages Hard-Deleted Components in Unlocked Packages

**•** RecordAlertDataSource

**•** RegisteredExternalService

**•** RelatedRecordAssocCriteria

**•** RelationshipGraphDefinition

**•** RemoteSiteSetting

**•** Report

**•** ReportType

**•** RestrictionRule

**•** SalesAgreementSettings

**•** SchedulingRule

**•** SchedulingObjective

**•** ScoreCategory

**•** ServiceAISetupDefinition

**•** ServiceAISetupField

**•** ServiceProcess

**•** SharingReason

**•** SharingRecalculation

**•** SlackApp

**•** StaticResource

**•** StnryAssetEnvSrcCnfg

**•** SustainabilityUom

**•** SustnUomConversion

**•** SvcCatalogCategory

**•** SvcCatalogFulfillmentFlow

**•** SvcCatalogItemDef

**•** TimelineObjectDefinition

**•** UIObjectRelationConfig

**•** UserAccessPolicy

**•** UserLicense

**•** UserProfileSearchScope

**•** ValidationRule

**•** VehicleAssetEmssnSrcCnfg

**•** ViewDefinition

**•** VirtualVisitConfig

**•** WaveApplication

**•** WaveComponent

**•** WaveDashboard

**•** WaveDataflow

**•** WaveDataset

**•** WaveLens


### Unlocked Packages Delete an Unlocked Package or Package Version

**•** WaveRecipe

**•** WaveTemplateBundle

**•** WaveXmd

**•** WebLink

**•** WebStoreTemplate

**•** WorkflowAlert

**•** WorkflowFieldUpdate

**•** WorkflowFlowAction

**•** WorkflowOutboundMessage

**•** WorkflowRule

**•** WorkflowTask

All other components are marked as deprecated when removed from an unlocked package. An admin can choose to remove deprecated
components. If the package is uninstalled, all components, including the deprecated components previously associated with the package,
are deleted from the org.

### Delete an Unlocked Package or Package Version

Use the `sf package version delete` and `sf package delete` to delete packages and package versions that you no
longer need.

To delete a package or package version, users need the Delete Second-Generation Packages user permission. Before you delete a package,
first delete all associated package versions.

**Considerations for Deleting a Package or Package Version**

**•** Deletion is permanent.

**•** Attempts to install a deleted package version will fail.

**•** Before deleting, ensure that the package or package version isn’t referenced as a dependency.

**Examples:**

```
   $ sf package delete -p "Your Package Alias"

   $ sf package delete -p 0Ho...

   $ sf package version delete -p "Your Package Version Alias"

   $ sf package version delete -p 04t...

```

These CLI commands can’t be used with first-generation managed packages or package versions. To delete a first-generation managed
[package, see View Package Details in the](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/isv_viewing_package_details.htm) _First-Generation Managed Packaging Developer Guide_ .


### Unlocked Packages View Package Details View Package Details

View the details of previously created packages and package versions from the command line.

To display a list of all packages in the Dev Hub org, use this command.

```
   sf package list --target-dev-hub my-hub

```

You can view the namespace, package name, ID, and other details in the output.

```
   Name Id Alias Description Type

   ─────────────── ────────────────── ────────────── ─────────── ─────────── ───────

   Expenser App 0HoB00000004CzRKAU Expenser App Unlocked

   Expenser Logic 0HoB00000004CzMKAU Expenser Logic Unlocked

   Expenser Schema 0HoB00000004CzHKAU Expenser Schema Unlocked

```

Include optional parameters to filter the list results based on the modification date, creation date, and to order by specific fields or
package IDs. To limit the details, use `--concise` . To show expanded details, use `--verbose` .

To display a list of all package versions in the Dev Hub org, use this command.

```
   sf package version list --target-dev-hub my-hub

```

You can view the namespace, version name, and other details in the output.

```
   Package Name Namespace Version Sub Pkg Ver Id Alias

   Installation Key Released

   ─────────────── ────────── ─────── ─────────────────── ───────────────────────

   ───────────────── ───────

   Expenser Schema 0.1.0.1 04tB0000000719qIAA Expenser Schema@0.1.0-1 false

           true

   Expenser Schema 0.2.0.1 04tB000000071AjIAI Expenser Schema@0.2.0-1 false

           true

   Expenser Schema 0.3.0.1 04tB000000071AtIAI Expenser Schema@0.3.0-1 false

           false

   Expenser Schema 0.3.0.2 04tB000000071AyIAI Expenser Schema@0.3.0-2 false

           true

   Expenser Schema 0.3.1.1 04tB0000000KGU6IAO Expenser Schema@0.3.1-1 false

           false

   Expenser Schema 0.3.1.2 04tB0000000KGUBIA4 Expenser Schema@0.3.1-2 false

           true

   Expenser Schema 0.3.2.1 04tB0000000KGUQIA4 Expenser Schema@0.3.2-1 false

           true

   Expenser Logic 0.1.0.1 04tB0000000719vIAA Expenser Logic@0.1.0-1 false

           true

   Expenser App 0.1.0.1 04tB000000071A0IAI Expenser App@0.1.0-1 false

           true

## Push a Package Upgrade for Unlocked Packages

```

Push upgrades enable you to upgrade packages installed in orgs, without asking org admins to install the upgrade themselves. You can
choose which orgs receive a push upgrade, what version the package is upgraded to, and when you want the upgrade to occur. Push
upgrades are particularly helpful if you need to push a change for a hot bug fix.


### Unlocked Packages Schedule a Push Upgrade Using CLI

Use Salesforce CLI or SOAP API to initiate the push upgrade, track the status of each job, and review error messages if any push upgrades
fail.

The CLI push upgrade commands are available to second-generation managed packages and unlocked packages. For unlocked packages,
push upgrades are enabled by default.

**Table 5: Package Types and Push Upgrade Options**

Push Upgrade Considerations for Unlocked Packages

**•** You can include new and changed features, or remove features during a push upgrade.

**•** When a push upgrade is installed, the Apex in the package is compiled.

**•** You can use push upgrades even if the package version requires a password.

### Schedule a Push Upgrade Using CLI

Use Salesforce CLI commands to schedule, abort, or view details about your push upgrade requests. Push upgrades let you upgrade
second-generation managed packages installed in subscriber orgs, without asking customers to install the upgrade themselves.

### Schedule a Push Upgrade Using CLI

Use Salesforce CLI commands to schedule, abort, or view details about your push upgrade requests. Push upgrades let you upgrade
second-generation managed packages installed in subscriber orgs, without asking customers to install the upgrade themselves.

The push upgrade feature is available to unlocked packages and second-generation managed packages only. To push a package upgrade
for a second-generation managed package, that package must have already passed the AppExchange security review.

Push upgrades for unlocked packages are enabled by default. To enable push upgrades for your second-generation managed package,
log a case with Salesforce Partner Support.

To initiate a push upgrade for an unlocked or second-generation managed package, the Create and Update Second-Generation Packages
user permission is required.

There are several aspects to scheduling a push upgrade for a package. At a high-level these include:

**•** Identifying the subscriber orgs and the org IDs that you want to upgrade

**•** Scheduling the push upgrade

**•** Tracking the progress and completion of the push upgrade

In some scenarios you may also need to abort a scheduled push upgrade, or analyze errors that occurred. Let’s review each of these
steps in more detail.

Determine the Orgs to Be Upgraded

There isn't a dedicated `push-upgrade` CLI command for this action, instead let's look at how to use the CLI `data query` command.


Unlocked Packages Schedule a Push Upgrade Using CLI

Push upgrades must be done in the context of the Dev Hub org that owns the package. To confirm the set of packages owned by a
specific Dev Hub org, run the `[package list](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_package_commands_unified.htm#cli_reference_package_list_unified)` command.

[Then authorize to the Dev Hub org that is the owner of the package are upgrading.](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_org_commands_unified.htm#cli_reference_org_login_web_unified)

```
   sf org login web --set-default-dev-hub

```

[If you're preparing to push a package upgrade, we assume your development environment is set up, if you aren't certain, review Set Up](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_pkg_dev_environment.htm)
[Your Development Environment.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_pkg_dev_environment.htm)

Here are three example queries you can use to retrieve a list of subscriber orgs that are eligible for a package upgrade. To review the
[possible fields that can be queried, see PackageSubscriber in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_packagesubscriber.htm) _Object Reference for the Salesforce Platform_ .

Each query requires either a subscriber package ID (starts with 033), or a subscriber package version ID (starts with 04t). To retrieve the
[subsciber package ID, use the package list command and specify the](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_package_commands_unified.htm#cli_reference_package_list_unified) `--verbose` flag. To retrieve the subscriber package version ID,
[use the package version list command.](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_package_commands_unified.htm#cli_reference_package_version_list_unified)

Query Example 1:

Compile a list of all orgs that have a specific package installed. This query requires the subscriber package ID (starts with 033).

```
   sf data query --target-org myDevHub --query "SELECT OrgKey, OrgName, OrgType, InstanceName,

    MetadataPackageId, MetadataPackageVersionId FROM PackageSubscriber WHERE MetadataPackageId

    = '033xxxxxxxxxxxxxxx'" --result-format json

```

If you copy and paste this query, update the target org and the subscriber package ID, before running the command. The target org is
the Dev Hub org that owns the package. Specify either the username or alias for the Dev Hub org.

Query Example 2:

Compile a list of orgs that have a specific package version installed, and pipe that output to a CSV file.

```
   sf data query --target-org myDevHub --query "SELECT OrgKey, OrgName, OrgType FROM

   PackageSubscriber WHERE MetadataPackageVersionId = '04t…'" --result-format csv

```

If you copy and paste this query, update the target org and the subscriber package version ID, before running the command. The target
org is the Dev Hub org that owns the package. Specify either the username or alias for the Dev Hub org.

This query returns as CSV file that you can use when scheduling the push upgrade. Before specifying the file in the `package`
`push-upgrade schedule` command, remove the first line of the CSV file. The CSV file can contain one org ID per line only.

Query Example 3:

Compile a list of all orgs that have a package version lower than version 2.7 installed. This query requires two separate steps.

Note: A single package has both a package ID (starts with 0Ho) and a subscriber package ID (starts with 033). For part one of this
two-part query, you must specify the 0Ho ID. If you run the `package list` command with the `--verbose` flag, you can
[determine both the 033 and 0Ho ID for a package. For more details on package IDs, see Package IDs and Aliases for](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_plan_pkg_types_pkg_ids.htm)
[Second-Generation Managed Packages.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_plan_pkg_types_pkg_ids.htm)

[First, query the Package2Version object to find all versions of your package that are numerically lower than the specified version (2.7).](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_tooling.meta/api_tooling/tooling_api_objects_package2version.htm)

```
   sf data query --target-org admin@packaging.com --use-tooling-api --query "SELECT

   SubscriberPackageVersionId FROM Package2Version WHERE Package2Id = '0HoPACKAGEIDxxxx' AND

    (MajorVersion < 2 OR (MajorVersion = 2 AND MinorVersion < 7))"

```

If you copy and paste this query, update the target org, the Package ID (starts with 0Ho), and the major and minor version before running
the command. The target org is the Dev Hub org that owns the package. Specify either the username or alias for the Dev Hub org.

Note the `SubscriberPackageVersionId` values (starts with 04t) returned by this query.


Unlocked Packages Schedule a Push Upgrade Using CLI

[Next, query the PackageSubscriber object using the subscriber package version IDs (starts with 04t) from the previous step.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_packagesubscriber.htm)

```
   sf data query --target-org myDevHub --query "SELECT OrgKey FROM PackageSubscriber WHERE

   MetadataPackageVersionId IN ('04tID1', '04tID2', '04tID_etc')" --result-format csv >out.txt

```

If you copy and paste this query, update the target org and the subscriber package version IDs (starts with 04t) before running the
command. The target org is the Dev Hub org that owns the package. Specify either the username or alias for the Dev Hub org.

If you created a CSV file in this step and plan to use the file to schedule your push upgrade, you must remove the first line of the file so
that it contains a list of org IDs only.

Schedule a Package Push Upgrade

After you have the org IDs for the subscribers you're upgrading, you can schedule the push upgrade. Review these examples of the flags
you might include with the `package push-upgrade schedule` command. For more details on this command, see the
[Salesforce CLI Command Reference.](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_package_commands_unified.htm#cli_reference_package_push-upgrade_schedule_unified)

When scheduling a push upgrade you have a choice about how to specify the orgs you want upgraded. You can use either flag:

**•** `--org-file` and provide a CSV file of all the orgs to be upgraded, or

**•** `--org-list` and specify a comma-separated list of org IDs in the command line when you run the push upgrade CLI command

If using a org file, it must contain one org ID per line only.

Examples for package push-upgrade schedule

Schedule a push upgrade that initiates at a specified time with a list of org IDs:

```
   sf package push-upgrade schedule --package 04txyz --start-time "2024-12-06T21:00:00"

   --org-list 00DAxx, 00DBx

```

Schedule a push upgrade that initiates as soon as possible using a list of orgs in a CSV file:

```
   sf package push-upgrade schedule --package 04txyz --org-file upgrade-orgs.csv

```

Note: If you don't specify the `--start-time` flag, the push upgrade begins as soon as resources are available. When specfiying
a start time, schedule during off peak hours. Specify start time in UTC.

Retrieve Details about Scheduled Package Push Upgrades

Use the `package push-upgrade list` or `package push-upgrade report` commands to retrieve details about push
upgrades that have been scheduled or completed for a package.

Examples for `package push-upgrade list` :

List all package push upgrade requests for a specified package:

```
   sf package push-upgrade list --package 033xyz --target-dev-hub myDevHub

```

List all package push upgrade requests for a specified package scheduled in the last 30 days:

```
   sf package push-upgrade list --package 033xyz --scheduled-last-days 30 --target-dev-hub

   myDevHub

```

List all package push upgrade requests with a status of Failed. This status occurs if the push upgrade fails for one or more orgs.

```
   sf package push-upgrade list --package 033xyz –-status Failed

```


## Unlocked Packages Install an Unlocked Package

List all package push upgrade requests with a status of Succeeded:

```
   sf package push-upgrade list --package 033xyz –-status Succeeded

```

Generate a report about a specific push upgrade request:

```
   sf package push-upgrade report --push-request-id 0DVxyz --target-dev-hub myDevHub

```

The `package push-upgrade list` command displays these fields: push request ID, package version ID, package version
number, status of the push upgrade request, push upgrade request scheduled start date and time, the number of orgs scheduled for
push upgrade, the number of orgs that were successfully upgraded, the number of orgs that failed to be upgraded, and push upgrade
request created date and time.

The `package push-upgrade report` command provides additional information, including error details.

Cancel a Pending Package Push Upgrade Request

If your push upgrade request has a status of either `Created` or `Pending` you can cancel the push upgrade by running the `package`
`push-upgrade abort` command. To retrieve the status of your push upgrade request, run either `package push-upgrade`
`list` or `package push-upgrade report` .

To cancel a specified push upgrade request:

```
   sf package push-upgrade abort --push-request-id 0DVxyz

```

Retrieve Error Messages for a Package Push Upgrade

There isn't a dedicated push upgrade CLI command for this retrieving error message, instead let's look at how to use the CLI `data`
`query` [command. Use this example query to retrieve error messages stored in the PackagePushError object.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_packagepusherror.htm)

Example:

```
   sf data query --query "SELECT Id, PackagePushJobId, PackagePushJob.SubscriberOrganizationKey,

    ErrorDetails, ErrorMessage, ErrorSeverity, ErrorTitle, ErrorType FROM PackagePushError

   WHERE PackagePushJob.PackagePushRequestId='$PUSH_REQUEST_ID'" --target-org myDevHub

## Install an Unlocked Package

```

Install unlocked packages using the CLI or the browser. You can install package versions in a scratch org, sandbox org, DE org, or production
org.

Install Packages with the CLI
If you’re working with the Salesforce CLI, you can use the `sf package install` command to install packages in a scratch
org or target subscriber org.

Install Unlocked Packages from a URL
Install unlocked packages from the CLI or from a browser, similar to how you install managed packages.

Upgrade a Version of an Unlocked Package
A package upgrade occurs when you install a new package version into an org that has a previous version of that package installed.

Sample Script for Installing Unlocked Packages with Dependencies
Use this sample script as a basis to create your own script to install packages with dependencies. This script contains a query that
finds dependent packages and installs them in the correct dependency order.


### Unlocked Packages Install Packages with the CLI Install Packages with the CLI

If you’re working with the Salesforce CLI, you can use the `sf package install` command to install packages in a scratch org or
target subscriber org.

Before you install a package to a scratch org, run this command to list all the packages and locate the ID or package alias.

```
   sf package version list

```

Identify the version you want to install. Enter this command, supplying the package alias or package ID (starts with 04t).

```
   sf package install --package "Expense Manager@1.2.0-12" --target-org jdoe@example.com

```

By default, the package install command provides admins access to the installed package. To provide access to all users, specify
`--security-type AllUsers` when you run the package install command.

If you’ve already set the scratch org with a default username, enter just the package version ID.

```
   sf package install --package "Expense Manager@1.2.0-12"

```

Note: If you’ve defined an alias (with the `-a` parameter), you can specify the alias instead of the username for `--target-org` .

The CLI displays status messages regarding the installation.

```
   Waiting for the subscriber package version install request to get processed. Status =

   InProgress Successfully installed the subscriber package version: 04txx0000000FIuAAM.

```

Control Package Installation Timeouts

When you issue a `sf package install` command, it takes a few minutes for a package version to become available in the target
org and for installation to complete. To allow sufficient time for a successful install, use these parameters that represent mutually exclusive
timers.

**•** `--publish-wait` defines the maximum number of minutes that the command waits for the package version to be available
in the target org. The default is 0. If the package is not available in the target org in this time frame, the install is terminated.

Setting `--publish-wait` is useful when you create a new package version and then immediately try to install it to target orgs.

Note: If `--publish-wait` is set to 0, the package installation immediately fails, unless the package version is already
available in the target org.

**•** `--wait` defines the maximum number of minutes that the command waits for the installation to complete after the package is
available. The default is 0. When the `--wait` interval ends, the install command completes, but the installation continues until it
either fails or succeeds. You can poll the status of the installation using `sf package install report` .

Note: The `--wait` timer takes effect after the time specified by `--publish-wait` has elapsed. If the
`--publish-wait` interval times out before the package is available in the target org, the `--wait` interval never starts.

For example, consider a package called Expense Manager that takes five minutes to become available on the target org, and 11 minutes
to install. The following command has `publish-wait` set to three minutes and `wait` set to 10 minutes. Because Expense Manager
requires more time than the set `publish-wait` interval, the installation is aborted at the end of the three-minute `publish-wait`
interval.

```
   sf package install --package "Expense Manager@1.2.0-12" --publish-wait 3 --wait 10

```

The following command has `publish-wait` set to six minutes and `wait` set to 10 minutes. If not already available, Expense
Manager takes five minutes to become available on the target org. The clock then starts ticking for the 10-minute `wait` time. At the


### Unlocked Packages Install Unlocked Packages from a URL

end of 10 minutes, the command completes because the `wait` time interval has elapsed, although the installation is not yet complete.
At this point, `sf package install report` indicates that the installation is in progress. After one more minute, the installation
completes and `sf package install report` indicates a successful installation.

```
   sf package install --package "Expense Manager@1.2.0-12" --publish-wait 6 --wait 10

```

SEE ALSO:

_[Salesforce CLI Command Reference](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_package_commands_unified.htm#cli_reference_package_install_unified)_ package install

_Salesforce Help:_ [Determine Which Users Can Access a Package](https://help.salesforce.com/s/articleView?id=xcloud.pkg_subscriber_determine_access.htm&type=5&language=en_US)

### Install Unlocked Packages from a URL

Install unlocked packages from the CLI or from a browser, similar to how you install managed packages.

If you create packages from the CLI, you can derive an installation URL for the package by adding the subscriber package ID to your Dev
Hub URL. You can use this URL to test different deployment or installation scenarios.

For example, if the package version has the subscriber package ID, 04tB00000009oZ3JBI, add the ID as the value of apvId.

```
   https:// MyDomainName .lightning.force.com/packagingSetupUI/ipLanding.app?apvId=04tB00000009oZ3JBI

```

Anyone with the URL and a valid login to a Salesforce org can install the package.

To install the package:

**1.** In a browser, enter the installation URL.

**2.** Enter your username and password for the Salesforce org in which you want to install the package, and then click **Login** .

**3.** If the package is protected by an installation key, enter the installation key.

### 4. For a default installation, click Install .

A message describes the progress. You receive a confirmation message when the installation is complete.

SEE ALSO:

_Salesforce Help:_ [Determine Which Users Can Access a Package](https://help.salesforce.com/s/articleView?id=xcloud.pkg_subscriber_determine_access.htm&type=5&language=en_US)

### Upgrade a Version of an Unlocked Package

A package upgrade occurs when you install a new package version into an org that has a previous version of that package installed.

To upgrade a package, use the package install CLI command

```
   sf package install --package 04t... --target-org me@example.com

```

[For more examples and details about this command, see package install in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_package_commands_unified.htm#cli_reference_package_install_unified) _Salesforce CLI Command Reference_ .

When you perform a package upgrade, here’s what to expect for metadata changes.

When you upgrade to a new unlocked package version, you choose whether to require successful compilation of all Apex in the org
and package ( `--apex-compile all` ), or only the Apex in the package ( `--apex-compile package` ).

**•** Metadata introduced in the new version is installed as part of the upgrade.

**•** If an upgraded component has the same API name as a component already in the target org, the component is overwritten with
the changes.

**•** If a component in the upgrade was deleted from the target org, the component is re-created during the upgrade.


### Unlocked Packages Sample Script for Installing Unlocked Packages with

Dependencies

**•** Metadata that was removed in the new package version is also removed from the target org as part of the upgrade. Removed
metadata is metadata not included in the current package version install, but present in the previous package version installed in
the target org. If metadata is removed before the upgrade occurs, the upgrade proceeds normally. Some examples where metadata
is deprecated and not deleted are:

**–** User-entered data in custom objects and fields are deprecated and not deleted. Admins can export such data if necessary.

**–** An object such as an Apex class is deprecated and not deleted if it’s referenced in a Lightning component that is part of the
package.

**•** In API version 45.0 and later (Salesforce CLI version 45.0.9 or later), you can specify what happens to removed metadata during
package upgrade. Use the `sf package install` command’s `-t` | `--upgrade-type` parameter, specifying one of these
values:

**–** `Delete` specifies to delete all removed components, except for custom objects and custom fields, that don’t have dependencies.

**–** `DeprecateOnly` specifies that all removed components must be marked deprecated. The removed metadata exists in the
target org after package upgrade, but is shown in the UI as deprecated from the package. This option is useful when migrating
metadata from one package to another.

**–** `Mixed` (the default) specifies that some removed components are deleted, and other components are marked deprecated.
For more information on hard-deleted components, see Hard-Deleted Components in Unlocked Packages.

It's possible to install a lower package version on top of a higher package version, but seriously consider this scenario before attempting
it. This is not the same as a rollback, which isn't possible.

[Note: For package installs into production orgs, or any org that has Apex Compile on Deploy enabled, the platform compiles all](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_deploying.htm)
Apex in the org after the package install or upgrade operation completes. This approach assures that package installs and upgrades
don’t impact the performance of an org, and is done even if `--apex-compile package` is specified.

### Sample Script for Installing Unlocked Packages with Dependencies

Use this sample script as a basis to create your own script to install packages with dependencies. This script contains a query that finds
dependent packages and installs them in the correct dependency order.

### Sample Script

Note: Be sure to replace the package version ID and scratch org user name with your own specific details.

```
   #!/bin/bash

   # The execution of this script stops if a command or pipeline has an error.

   # For example, failure to install a dependent package will cause the script

   # to stop execution.

   set -e

   # Specify a package version id (starts with 04t)

   # If you know the package alias but not the id, use sf package version list to find it.

```


Unlocked Packages Sample Script for Installing Unlocked Packages with
Dependencies

```
   PACKAGE=04tB0000000NmnHIAS

   # Specify the user name of the subscriber org.

   USER_NAME=test-bvdfz3m9tqdf@example.com

   # Specify the timeout in minutes for package installation.

   WAIT_TIME=15

   echo "Retrieving dependencies for package Id: "$PACKAGE

   # Execute soql query to retrieve package dependencies in json format.

   RESULT_JSON=`sf data query -u $USER_NAME -t -q "SELECT Dependencies FROM

   SubscriberPackageVersion WHERE Id='$PACKAGE'" --json`

   # Parse the json string using python to test whether the result json contains a list of

   ids or not.

   DEPENDENCIES=`echo $RESULT_JSON | python -c 'import sys, json; print

   json.load(sys.stdin)["result"]["records"][0]["Dependencies"]'`

   # If the parsed dependencies is None, the package has no dependencies. Otherwise, parse

   the result into a list of ids.

   # Then loop through the ids to install each of the dependent packages.

   if [[ "$DEPENDENCIES" != 'None' ]]; then

      DEPENDENCIES=`echo $RESULT_JSON | python -c '

   import sys, json

   ids = json.load(sys.stdin)["result"]["records"][0]["Dependencies"]["ids"]

   dependencies = []

   for id in ids:

      dependencies.append(id["subscriberPackageVersionId"])

   print " ".join(dependencies)

   '`

```


## Unlocked Packages Migrate Deprecated Metadata from Unlocked Packages

```
      echo "The package you are installing depends on these packages (in correct dependency

    order): "$DEPENDENCIES

      for id in $DEPENDENCIES

      do

        echo "Installing dependent package: "$id

        sf package install --package $id -u $USER_NAME -w $WAIT_TIME --publish-wait 10

      done

   else

      echo "The package has no dependencies"

   fi

   # After processing the dependencies, proceed to install the specified package.

   echo "Installing package: "$PACKAGE

   sf package install --package $PACKAGE -u $USER_NAME -w $WAIT_TIME --publish-wait 10

   exit 0;

## Migrate Deprecated Metadata from Unlocked Packages

```

You can deprecate metadata in an unlocked package, move that metadata to a new package, and then install the new package in your
production org.

As you create more unlocked packages, you can refactor your package and move metadata from one unlocked package to another
unlocked package if necessary.

To move production metadata from package A to package B, follow these steps.

**1.** Identify the metadata to be moved from package A to package B.

**2.** Remove the metadata from package A, create a version, and release the package.

**3.** Add the metadata to package B, create a version, and release the package.

**4.** In your production org, upgrade package A.

**5.** In your production org, install package B.

Your metadata is now a part of package B in your production org.


## Unlocked Packages Uninstall an Unlocked Package Uninstall an Unlocked Package

You can uninstall a package from an org using Salesforce CLI or from the Setup UI. When you uninstall unlocked packages, all components
in the package, as well as any deprecated components previously associated with the package, are deleted from the org.

To use the CLI to uninstall a package from the target org, authorize the Dev Hub org and run this command.

```
   sf package uninstall --package "Expense Manager@2.3.0-5"

```

You can also uninstall a package from the web browser. Open the Salesforce org where you installed the package.

```
   sf org open -u me@my.org

```

Then uninstall the package.

**1.** From Setup, enter _`Installed Packages`_ in the Quick Find box, then select **Installed Packages** .

## 2. Click Uninstall next to the package that you want to remove.

**3.** Determine whether to save and export a copy of the package’s data, and then select the corresponding radio button.

## 4. Select Yes, I want to uninstall and click Uninstall .

Considerations on Uninstalling Packages

**•** If you’re uninstalling a package that includes a custom object, all components on that custom object are also deleted. Deleted items
include custom fields, validation rules, custom buttons, and links, workflow rules, and approval processes.

**•** You can’t uninstall a package whenever a component not included in the uninstall references any component in the package. For
example:

**–** When an installed package includes any component on a standard object that another component references, Salesforce prevents
you from uninstalling the package. An example is a package that includes a custom user field with a workflow rule that gets
triggered when the value of that field is a specific value. Uninstalling the package would prevent your workflow from working.

**–** When you’ve installed two unrelated packages that each include a custom object and one custom object component references
a component in the other, you can’t uninstall the package. An example is if you install an expense report app that includes a
custom user field and create a validation rule on another installed custom object that references that custom user field. However,
uninstalling the expense report app prevents the validation rule from working.

**–** When an installed folder contains components you added after installation, Salesforce prevents you from uninstalling the package.

**–** When an installed letterhead is used for an email template you added after installation, Salesforce prevents you from uninstalling
the package.

**–** When an installed package includes a custom field that’s referenced by Einstein Prediction Builder or Case Classification, Salesforce
prevents you from uninstalling the package. Before uninstalling the package, edit the prediction in Prediction Builder or Case
Classification so that it no longer references the custom field.

**•** You can’t uninstall a package that removes all active business and person account record types. Activate at least one other business
or person account record type, and try again.

**•** You can’t uninstall a package if a background job is updating a field added by the package, such as an update to a roll-up summary
field. Wait until the background job finishes, and try again.

## Transfer an Unlocked Package to a Different Dev Hub

You can transfer the ownership of an unlocked package from one Dev Hub org to another.


Unlocked Packages Transfer an Unlocked Package to a Different Dev Hub

Note: This package transfer feature is available only to unlocked packages and second-generation managed packages. Dev Hub
orgs aren’t used with first-generation managed packages or unmanaged packages, so this feature doesn’t apply to those package
types.

Request a Package Transfer to a Different Dev Hub

Start by logging a case with Salesforce Customer Support, and provide the following details:

`Subject:` Unlocked Package Transfer to a different Dev Hub

```
   Description:

```

In the description, list:

**•** Subscriber package ID of the package you’re transferring. This ID starts with 033.

To verify the 033 ID of your package, run the `sf package list` command with the `-–verbose` flag on the source Dev
Hub org.

**•** Dev Hub org ID for the source org.

**•** Dev Hub org ID for the destination org. The destination Dev Hub org can’t be a Developer Edition org or a trial org.

**•** (Optional) Namespace of the package being transferred. If the package is a no-namespace unlocked package, skip this step.

**•** Acknowledge that you’ve reviewed and completed the steps listed in the `Prepare to Transfer Your Package` section,
including linking your namespace to the destination Dev Hub, and clearing your Apex Error Notification User.

If you’re transferring more than one package, file a separate case for each package.

After your case has been reviewed and approved, someone from Salesforce Customer Support will contact you to arrange a time to
initiate the package transfer.

Note: For security reasons, package transfers between a Dev Hub located in Government Cloud and a Dev Hub located outside
Government Cloud aren’t permitted.

Prepare to Transfer Your Package

Here’s how you can help ensure a smooth package transfer.

**•** If the package you’re transferring has a namespace, keep the namespace linked to the source Dev Hub. Before the package transfer,
[the namespace must be linked to both the source and destination Dev Hub orgs.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_create_namespace.htm)

**•** Before the package transfer process is initiated, ensure all push upgrades or package version creation processes have completed.

**•** Delete package versions that are no longer needed.

**•** If specified, clear the package’s Error Notification User using the `sf package update`
`--error-notification-username=` command. If you’re transferring the package to a Dev Hub org you own, you can
set the Error Notification User to a user in the destination Dev Hub after the package transfer is complete. Note: Specifying
`--error-notification-username=` with no value after the equals sign clears any previously set username.

During the Package Transfer Process

All push upgrades or package version creation processes must be complete before the package transfer process is initiated. Salesforce
Customer Support will alert you about the date the package transfer will occur.


Unlocked Packages Transfer an Unlocked Package to a Different Dev Hub

After the Package Transfer Is Complete

Run `sf package list` and verify that the package is no longer associated with your Dev Hub.

Impact of Package Transfers on Package IDs

Update Your Package Project File

Before you create new packages or package versions on your Dev Hub, update your `sfdx-project.json` file and remove all
references to the transferred package from the package directory and package alias sections.

If you have packages in your Dev Hub that depend on the package that you’re transferring, update the package dependency section in
your `sfdx-project.json` file to explicitly specify the 04t ID of the transferred package that you depend on.

For example, if you transferred pkgA to a different Dev Hub, and your `sfdx-project.json` file lists the package dependency like
this.

```
   "dependencies": [

     {

       "package": "pkgA"

       "versionNumber": "2.0.0.LATEST"

     }

   ]

```

Update the dependency to either specify the 04t ID of pkgA.

```
   "dependencies": [

     {

       "package": "04tB0000000UzH5IAK"

     }

   ]

```

Or specify the dependency using a package alias.

```
   "dependencies": [

     {

       "package": "pkgA2.0.0-1"

     }

   "packageAliases": {

      "pkgA2.0.0-1": "04tB0000000UzH5IAK"

   }

   ]

```


### Unlocked Packages Take Ownership of an Unlocked Package Transferred from

a Different Dev Hub

What Package History Is Transferred?

When a package is transferred, all package versions, and all lines of ancestry are transferred. Upgrade paths aren’t affected.

Regardless of whether the package transfer occurred between two Dev Hub orgs you own, or the package was transferred externally to
a Dev Hub you don’t own, we transfer the package version history.

We transfer:

**•** Package name, namespace, type, and IDs. One exception is that the transferred package gets a new 0Ho ID.

**•** Package version info. This includes all the info that is typically displayed when you run the `sf package version list` or
`sf package version report` command.

We don’t transfer:

**•** Push upgrade history.

**•** Package version create requests.

**•** The username of the Dev Hub user who received Apex and other types of error notifications. This optional user is set using
`--error-notification-username` .

**•** Deleted package versions.

### Take Ownership of an Unlocked Package Transferred from a Different Dev Hub

You can take ownership of an unlocked package that is transferred from another Dev Hug org.

### Take Ownership of an Unlocked Package Transferred from a Different Dev

Hub

You can take ownership of an unlocked package that is transferred from another Dev Hug org.

To initiate a package transfer from your Dev Hub org, see Transfer an Unlocked Package to a Different Dev Hub.

Note: For security reasons, package transfers between a Dev Hub located in Government Cloud and a Dev Hub located outside
Government Cloud aren’t permitted.

Receive a Package Transfer

[Link the namespace of the package you’re receiving to your Dev Hub org. See Link a Namespace to a Dev Hub Org in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_reg_namespace.htm) _Salesforce DX_
_Developer Guide_ . If the package isn’t associated with a namespace, skip this step.

After the Package Transfer Is Complete

After the package transfer is complete, you’ll be notified by Salesforce Customer Support.

To verify that the transferred package is associated with your Dev Hub, run `sf package list` .

Impact of Package Transfers on Package IDs


Unlocked Packages Take Ownership of an Unlocked Package Transferred from
a Different Dev Hub

Update Your Package Project File

Open and review the contents of the `sfdx-project.json` file associated with the transferred package.

Open and review the contents of any scratch org definition files associated with the transferred package. Definition files help in setting
up your scratch orgs during development. Use the `–definition-file` parameter to specify a definition file when you create a
new package version.

If the package directories section lists additional packages that weren’t transferred to you, remove those references from the
`sfdx-project.json` file.

Next, review the package alias section of the `sfdx-project.json` file, and remove any references to package aliases that aren’t
associated with the package that was transferred.

Update the package alias of the transferred package to specify its 0Ho package ID.

Before You Create a New Package Version

Similar to how you go about creating new package versions, you must update the `sfdx-project.json` file, and update the
version number.

To designate a Dev Hub user to receive email notifications for unhandled Apex exceptions, and install, upgrade, or uninstall failures
associated with your package, run the `sf package update` command, and use the `--error-notification-username`
parameter.

What Package History Is Transferred?

We transfer:

**•** Package name, namespace, type, and IDs. One exception is that the transferred package gets a new 0Ho ID.

**•** Package version info. This includes all the info that is typically displayed when you run the `sf package version list` or
`sf package version report` command.

We don’t transfer:

**•** Push upgrade history.

**•** Package version create requests.

**•** The username of the Dev Hub user who received Apex and other types of error notifications.

**•** Deleted package versions.


# CHAPTER 14 Continuous Integration

In this chapter ...

Continuous integration (CI) is a software development practice in which developers regularly integrate
their code changes into a source code repository. To ensure that the new code does not introduce bugs,
automated builds and tests run before or after developers check in their changes.

# • Continuous automated builds and tests run before or after developers check in their changes.

Integration Using
Many third-party CI tools are available for you to choose from. Salesforce DX easily integrates into these
CircleCI
tools so that you can set up continuous integration for your Salesforce applications.

# • Continuous

Integration Using
Jenkins

# • Continuous

Integration with
Travis CI

**•** Sample CI Repos for
Org Development
Model

**•** Sample CI Repos for
Package
Development Model

SEE ALSO:

_Salesforce Help:_ [Install and Configure DevOps Center](https://help.salesforce.com/s/articleView?id=platform.devops_center_setup.htm&type=5&language=en_US)

_Salesforce Help:_ [Manage and Release Changes Easily and Collaboratively with DevOps Center](https://help.salesforce.com/s/articleView?id=platform.devops_center_overview.htm&type=5&language=en_US)


## Continuous Integration Continuous Integration Using CircleCI Continuous Integration Using CircleCI

CircleCI is a commonly used integration tool that integrates with your existing version control system to push incremental updates to
the environments you specify. CircleCI can be used as a cloud-based or on-premise tool. These instructions demonstrate how to use
GitHub, CircleCI, and your Dev Hub org for continuous integration.

### Configure Your Environment for CircleCI

Before integrating your existing CircleCI framework, configure your Dev Hub org and CircleCI project.

Connect CircleCI to Your DevHub
Authorize CircleCI to push content to your Dev Hub org via a connected app.

SEE ALSO:

[CircleCI](http://www.circleci.com/)

[The sfdx-circleci-package Github Repo](https://github.com/forcedotcom/sfdx-circleci-package)

[The sfdx-circleci-org Github Repo](https://github.com/forcedotcom/sfdx-circleci-org)

### Configure Your Environment for CircleCI

Before integrating your existing CircleCI framework, configure your Dev Hub org and CircleCI project.

**1.** [Set up your GitHub repository with CircleCI. You can follow the sign-up steps on the CircleCI website to access your code on GitHub.](https://circleci.com/docs/first-steps/)

**2.** [Install the Salesforce CLI, if you haven’t already.](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_setup.meta/sfdx_setup/sfdx_setup_install_cli.htm)

**3.** Follow Authorize an Org Using the JWT Flow for your Dev Hub org, if you haven’t already.

**4.** Encrypt your server key.

**a.** First, generate a key and initialization vector (iv) to encrypt your `server.key` file locally. CircleCI uses the key and iv to decrypt
your server key in the build environment.

Run the following command in the directory containing your `server.key` file. For the _`<passphrase>`_ value, enter a
word of your own choosing to create a unique key.

```
       openssl enc -aes-256-cbc -k <passphrase> -P -md sha1 -nosalt

```

The key and iv value display in the output.

```
       key=****24B2

       iv =****DA58

```

**b.** Note the key and iv values, you need them later.

**c.** Encrypt the `server.key` file using the newly generated key and iv values. Run the following command in the directory
containing your `server.key` file, replacing _`<key>`_ and _`<iv>`_ with the values from the previous step.

```
       openssl enc -nosalt -aes-256-cbc -in server.key -out server.key.enc -base64 -K <key>

       -iv <iv>

```

Note: Use the key and iv values only once, and don't use them to encrypt more than the `server.key` . While you can
reuse this pair to encrypt other things, it is considered a security violation to do so.


### Continuous Integration Connect CircleCI to Your DevHub

You generate a new key and iv value every time you run the command in step a. In other words, you can't regenerate the same
pair. If you lose these values you must generate new ones and encrypt again.

Next, you’ll store the key, iv, and contents of `server.key.enc` as protected environment variables in the CircleCI UI. These values
are considered secret, so take the appropriate precautions to protect them.

### Connect CircleCI to Your DevHub

Authorize CircleCI to push content to your Dev Hub org via a connected app.

**1.** Make sure that you have Salesforce CLI installed. Check by running `sf version` and confirm that you see version information.
[If you don't have it installed, see Install Salesforce CLI.](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_setup.meta/sfdx_setup/sfdx_setup_install_cli.htm#sfdx_setup_install_cli)

**2.** Confirm you can perform a JWT-based authorization from the directory containing your `server.key` file. Run the following
command from the directory containing your `server.key` (replace _`<your_consumer_key>`_ and _`<your_username>`_
values where indicated).

```
     sf org login jwt --client-id <your_consumer_key> --jwt-key-file server.key --username

     <your_username> --set-default-dev-hub

```

**3.** [Fork the sfdx-circleci repo into your GitHub account using the](http://help.github.com/fork-a-repo/) **Fork** link at the top of the page.

**4.** Create a local directory for this project and clone your forked repo locally into the new directory. Replace _`<git_username>`_
with your own GitHub username.

```
     git clone https://github.com/ <git_username> /sfdx-circleci.git

```

**5.** Retrieve the generated consumer key from your JWT-Based Authorization connected app. From Setup, in the Quick Find box, enter
_`App`_, and then select **App Manager** . Select **View** in the row-menu next to the connected app.

**6.** In the CircleCI UI, you see a project named sfdx-circleci. In the project settings, store the consumer key in a CircleCI environment
variable named `HUB_CONSUMER_KEY` [. For more information, see the CircleCI documentation Setting an Environment Variable](https://circleci.com/docs/env-vars/#setting-an-environment-variable-in-a-project)
[in a Project.](https://circleci.com/docs/env-vars/#setting-an-environment-variable-in-a-project)

**7.** Store the username that you use to access your Dev Hub in a CircleCI environment variable named `HUB_SFDX_USER` using the
CircleCI UI.

**8.** Store the key and iv values from Encrypt Your Server Key in CircleCI environment variables named `DECRYPTION_KEY` and
`DECRYPTION_IV`, respectively. When you finish setting the environment variables, your project screen looks like the following
image.


## Continuous Integration Continuous Integration Using Jenkins

Note: In the directory containing your `server.key` file, use the command `rm server.key` to remove the
`server.key` . Never store keys or certificates in a public place.

You’re ready to go! Now when you commit and push a change, your change kicks off a CircleCI build.

**•** Contribute to the repository – If you find any issues or opportunities for improving this repository, fix them! Feel free to contribute
[to this project, fork this repository, and then change the content. After you make your changes, share them with the community by](http://help.github.com/fork-a-repo/)
[sending a pull request. See How to send pull requests for more information about contributing to GitHub projects.](http://help.github.com/send-pull-requests/)

**•** [Report issues – If you find any issues with this demo that you can't fix, feel free to report them in the issues section of this repository.](https://github.com/forcedotcom/sfdx-circleci/issues)

## Continuous Integration Using Jenkins

Jenkins is an open-source, extensible automation server for implementing continuous integration and continuous delivery. You can
easily integrate Salesforce DX into the Jenkins framework to automate testing of Salesforce applications against scratch orgs.

To integrate Jenkins, we assume:

**•** You are familiar with how Jenkins works. You can configure and use Jenkins in many ways. We focus on integrating Salesforce DX
into Jenkins multibranch pipelines.

**•** The computer on which the Jenkins server is running has access to your version control system and to the repository that contains
your Salesforce application.

Configure Your Environment for Jenkins
Before integrating your Dev Hub and scratch orgs into your existing Jenkins framework, configure your Jenkins environment. Our
example assumes that you’re working in a package development model.


### Continuous Integration Configure Your Environment for Jenkins

Jenkinsfile Walkthrough
The sample Jenkinsfile shows how to integrate your Dev Hub and scratch orgs into a Jenkins job. The sample uses Jenkins Multibranch
Pipelines. Every Jenkins setup is different. This walkthrough describes one of the ways to automate testing of your Salesforce
applications. The walkthrough highlights Salesforce CLI commands to create a scratch org, upload your code, and run your tests.

Sample Jenkinsfile
A `Jenkinsfile` is a text file that contains the definition of a Jenkins Pipeline. This `Jenkinsfile` shows how to integrate
Salesforce CLI commands to automate testing of your Salesforce applications using scratch orgs.

SEE ALSO:

[Jenkins](https://jenkins.io/)

[Pipeline-as-code with Multibranch Workflows in Jenkins](https://jenkins.io/blog/2015/12/03/pipeline-as-code-with-multibranch-workflows-in-jenkins/)

### Configure Your Environment for Jenkins

Before integrating your Dev Hub and scratch orgs into your existing Jenkins framework, configure your Jenkins environment. Our example
assumes that you’re working in a package development model.

**1.** In your Dev Hub org, create a connected app as described by the JWT-based authorization flow. This step includes obtaining or

creating a private key and digital certificate.

Make note of your consumer key (sometimes called a client ID) when you save the connected app. You need the consumer key to
set up your Jenkins environment. Also have available the private key file used to sign the digital certificate.

**2.** On the computer that’s running the Jenkins server, do the following.

**a.** Download and install Salesforce CLI.

**b.** [Store the private key file as a Jenkins Secret File using the Jenkins Admin Credentials interface. Make note of the new entry’s ID.](https://wiki.jenkins-ci.org/display/JENKINS/Credentials+Binding+Plugin)

You later reference this Credentials entry in your `Jenkinsfile` .

**c.** Set the following variables in your Jenkins environment.

**•** SF_USERNAME—The username for the Dev Hub org, such as juliet.capulet@myenvhub.com.

**•** SF_INSTANCE_URL—The login URL of the Salesforce instance that hosts the Dev Hub org. The default is
https://login.salesforce.com. We recommend that you update this value to the My Domain login URL for the Dev Hub org.
You can find an org’s My Domain login URL on the My Domain page in Setup.

**•** SF_CONSUMER_KEY—The consumer key that was returned after you created a connected app in your Dev Hub org.

**•** SERVER_KEY_CREDENTALS_ID—The credentials ID for the private key file that you stored in the Jenkins Admin Credentials
interface.

**•** PACKAGE_NAME-The name of your package, such as My Package.

**•** PACKAGE_VERSION-The version of your package, which starts with 04t.

**•** TEST_LEVEL-The test level for your package, such as RunLocalTests.

The names for these environment variables are just suggestions. You can use any name as long as you specify it in the
`Jenkinsfile` .

You can also optionally set the SF_AUTOUPDATE_DISABLE variable to `true` to disable auto-update of Salesforce CLI. CLI
auto-update can interfere with the execution of a Jenkins job.

**3.** Set up your Salesforce DX project so that you can create a scratch org.


### Continuous Integration Jenkinsfile Walkthrough

**4.** (Optional) Install the Custom Tools Plugin into your Jenkins console, and create a custom tool that references Salesforce CLI. The
Jenkins walkthrough assumes that you created a custom tool named toolbelt in the `/usr/local/bin` directory, which is the
directory in which Salesforce CLI is installed.

SEE ALSO:

Authorize an Org Using the JWT Flow

_[Salesforce CLI Setup Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_setup.meta/sfdx_setup)_

[Jenkins: Credentials Binding Plugin](https://wiki.jenkins-ci.org/display/JENKINS/Credentials+Binding+Plugin)

Project Setup

### Jenkinsfile Walkthrough

The sample Jenkinsfile shows how to integrate your Dev Hub and scratch orgs into a Jenkins job. The sample uses Jenkins Multibranch
Pipelines. Every Jenkins setup is different. This walkthrough describes one of the ways to automate testing of your Salesforce applications.
The walkthrough highlights Salesforce CLI commands to create a scratch org, upload your code, and run your tests.

[This walkthrough relies on the sfdx-jenkins-package Jenkinsfile. We assume that you’re familiar with the structure of the Jenkinsfile,](https://github.com/forcedotcom/sfdx-jenkins-package/blob/master/Jenkinsfile)
Jenkins Pipeline DSL, and the Groovy programming language. This walkthrough demonstrates implementing a Jenkins pipeline using
Salesforce CLI and scratch orgs. See the CLI Command Reference regarding the commands used.

### This workflow most closely corresponds to Jenkinsfile stages.

**•** Define Variables

**•** Check Out the Source Code

**•** Wrap All Stages in a withCredentials Command

**•** Wrap All Stages in a withEnv Command

**•** Authorize Your Dev Hub Org and Create a Scratch Org

**•** Push Source and Assign a Permission Set

**•** Run Apex Tests

**•** Delete the Scratch Org

**•** Create a Package

**•** Create a Scratch Org and Display Info

**•** Install Package, Run Unit Tests, and Delete Scratch Org

Define Variables

Use the `def` keyword to define the variables required by Salesforce CLI commands. Assign each variable the corresponding environment
variable that you previously set in your Jenkins environment.

```
   def SF_CONSUMER_KEY=env.SF_CONSUMER_KEY

   def SERVER_KEY_CREDENTALS_ID=env.SERVER_KEY_CREDENTALS_ID

   def TEST_LEVEL='RunLocalTests'

   def PACKAGE_NAME='0Ho1U000000CaUzSAK'

   def PACKAGE_VERSION

   def SF_INSTANCE_URL = env.SF_INSTANCE_URL ?: "https:// MyDomainName .my.salesforce.com"

```

Define the `SF_USERNAME` variable, but don’t set its value. You do that later.

```
   def SF_USERNAME

```


Continuous Integration Jenkinsfile Walkthrough

Although not required, we assume that you used the Jenkins Global Tool Configuration to create the `toolbelt` custom tool that
points to the CLI installation directory. In your `Jenkinsfile`, use the tool command to set the value of the `toolbelt` variable to
this custom tool.

```
   def toolbelt = tool 'toolbelt'

```

You can now reference the Salesforce CLI executable in the `Jenkinsfile` using `${toolbelt}/sf` .

Check Out the Source Code

Before testing your code, get the appropriate version or branch from your version control system (VCS) repository. In this example, we
use the `checkout scm` Jenkins command. We assume that the Jenkins administrator has already configured the environment to
access the correct VCS repository and check out the correct branch.

```
   stage('checkout source') {

        // when running in multi-branch job, one must issue this command

        checkout scm

     }

```

Wrap All Stages in a withCredentials Command

You previously stored the JWT private key file as a Jenkins Secret File using the Credentials interface. Therefore, you must use the
`withCredentials` command in the body of the `Jenkinsfile` to access the secret file. The `withCredentials` command
lets you name a credential entry, which is then extracted from the credential store and provided to the enclosed code through a variable.
When using `withCredentials`, put all stages within its code block.

This example stores the credential ID for the JWT key file in the variable `SERVER_KEY_CREDENTALS_ID` . You defined the
`SERVER_KEY_CREDENTALS_ID` earlier and set it to its corresponding environment variable. The `withCredentials` command
fetches the contents of the secret file from the credential store and places the contents in a temporary location. The location is stored
in the variable `server_key_file` . You use the `server_key_file` variable with the `org login jwt` command to specify
the private key securely.

```
   withCredentials([file(credentialsId: SERVER_KEY_CREDENTALS_ID, variable: 'server_key_file')])

     # all stages will go here

   }

```

Wrap All Stages in a **`withEnv`** Command

When running Jenkins jobs, it’s helpful to understand where files are being stored. There are two main directories to be mindful of: the
workspace directory and the home directory. The workspace directory is unique to each job while the home directory is the same for
all jobs.

The `withCredentials` command stores the JWT key file in the Jenkins workspace during the job. However, Salesforce CLI `auth`
commands store authentication files in the home directory; these authentication files persist outside of the duration of the job.

This setup isn’t a problem when you run a single job but can cause problems when you run multiple jobs. So, what happens if you run
multiple jobs using the same Dev Hub or other Salesforce user? When the CLI tries to connect to the Dev Hub as the user you authenticated,
it fails to refresh the token. Why? The CLI tries to use a JWT key file that no longer exists in the other workspace, regardless of the
`withCredentials` for the current job.

If you set the home directory to match the workspace directory using `withEnv`, the authentication files are unique for each job.
Creating unique auth files per job is also more secure because each job has access only to the auth files it creates.


Continuous Integration Jenkinsfile Walkthrough

When using `withEnv`, put all stages within its code block,

```
   withEnv(["HOME=${env.WORKSPACE}"]) {

     # all stages will go here

   }

```

Note: If you don’t use a pipeline or you run commands outside of a pipeline stage, add a home environment specification to your
script: `export HOME=$WORKSPACE` .

Authorize Your Dev Hub Org and Create a Scratch Org

This `sfdx-jenkins-package` example uses two stages: one stage to authorize the Dev Hub org and another stage to create a
scratch org.

```
   // ------------------------------------------------------------------------
   // Authorize the Dev Hub org with JWT key and give it an alias.

   // ------------------------------------------------------------------------
   stage('Authorize DevHub') {

     rc = command "${toolbelt}/sf org login jwt --instance-url ${SF_INSTANCE_URL} --client-id

    ${SF_CONSUMER_KEY} --username ${SF_USERNAME} --jwt-key-file ${server_key_file}

   --set-default-dev-hub --alias HubOrg"

      if (rc != 0) {

        error 'Salesforce dev hub org authorization failed.'

      }

   }

   // ------------------------------------------------------------------------
   // Create new scratch org to test your code.

   // ------------------------------------------------------------------------
   stage('Create Test Scratch Org') {

      rc = command "${toolbelt}/sf org create scratch --target-dev-hub HubOrg --set-default

    --definition-file config/project-scratch-def.json --alias ciorg --wait 10 --duration-days

    1"

      if (rc != 0) {

        error 'Salesforce test scratch org creation failed.'

      }

   }

```

Use `org login jwt` to authorize your Dev Hub org.

You’re required to run this step only one time, but we suggest you add it to your `Jenkinsfile` and authorize each time you run
the Jenkins job. This way you’re always sure that the Jenkins job isn’t aborted due to lack of authorization. There’s typically little harm in
authorizing multiple times, but keep in mind that the API call limit for your scratch org’s edition still applies.

Use the flags of the `org login jwt` command to provide information about the Dev Hub org that you’re authorizing. The values
for the `--client-id`, `--username`, and `--instance-url` flags are the SF_CONSUMER_KEY, HubOrg, and SF_INSTANCE_URL
environment variables you previously defined, respectively. The value of the `--jwt-key-file` flag is the `server_key_file`
variable that you set in the previous section using the `withCredentials` command. The `--set-default-dev-hub` flag
specifies that this HubOrg is the default Dev Hub org for creating scratch orgs.

Note: It’s a best practice to have a unique authentication file for each Jenkins job using the `withEnv` wrapper. But it’s possible
to authorize a Dev Hub on your Jenkins machine instead. The advantage is that your authentication is set centrally on your machine


Continuous Integration Jenkinsfile Walkthrough

for any Jenkins job you run. The disadvantage is security: Every job has access to all authenticated users whether you want them
to or not.

If you do want to auth to your Dev Hub on your Jenkins machine, follow these steps:

**•** On the Jenkins machine as the Jenkins user, authorize to your Dev Hub using any of the `org login` commands.

**•** In your Jenkinsfile, remove the `withCredentials`, `withEnv`, and `org login jwt` statements.

Use the `org create scratch` CLI command to create a scratch org. In the example, the CLI command uses the
`config/project-scratch-def.json` file (relative to the project directory) to create the scratch org. The `--json` flag
specifies the output as JSON format. The `--set-default` flag sets the new scratch org as the default.

The Groovy code that parses the JSON output of the `org create scratch` command extracts the username that was auto-generated
as part of the org creation. This username, stored in the SF_USERNAME variable, is used with the CLI commands that push source, assign
a permission set, and so on.

Push Source and Assign a Permission Set

Let’s populate your new scratch org with metadata. This example uses the `project deploy start` command to deploy your
source to the org. The source includes all the pieces that make up your Salesforce application: Apex classes and test classes, permission
sets, layouts, triggers, custom objects, and so on.

```
   // ------------------------------------------------------------------------
   // Push source to test scratch org.

   // ------------------------------------------------------------------------
   stage('Push To Test Scratch Org') {

      rc = command "${toolbelt}/sf project deploy start --target-org ciorg"

      if (rc != 0) {

        error 'Salesforce push to test scratch org failed.'

      }

   }

```

Recall the SF_USERNAME variable that contains the auto-generated username that was output by the `org create scratch`
command in an earlier stage. The code uses this variable as the argument to the `--target-org` flag to specify the username for
the new scratch org.

The `project deploy start` command deploys all the Salesforce-related files that it finds in your project. Add a `.forceignore`
file to your repository to list the files that you don’t want pushed to the org.

Run Apex Tests

Now that your source code and test source are pushed to the scratch org, run the `apex run test` command to run Apex tests.

```
   // ------------------------------------------------------------------------
   // Run unit tests in test scratch org.

   // ------------------------------------------------------------------------
   stage('Run Tests In Test Scratch Org') {

     rc = command "${toolbelt}/sf apex run test --target-org ciorg --wait 10 --result-format

    tap --code-coverage --test-level ${TEST_LEVEL}"

      if (rc != 0) {

        error 'Salesforce unit test run in test scratch org failed.'

```


Continuous Integration Jenkinsfile Walkthrough

```
      }

   }

```

You can specify various flags to the `apex run test` CLI command. In the example:

**•** The `--test-level ${TEST_LEVEL}` flag runs all tests in the scratch org, except tests that originate from installed managed
packages. You can also specify `RunLocalTests` to run only local tests, `RunSpecifiedTests` to run only certain Apex tests
or suites or `RunAllTestsInOrg` to run all tests in the org.

**•** The `--result-format tap` flag specifies that the command output is in Test Anything Protocol (TAP) format. The test results
that are written to a file are still in JUnit and JSON formats.

**•** The `--target-org ciorg` flag specifies the username for accessing the scratch org (the value in SF_USERNAME).

The `apex run test` command writes its test results in JUnit format.

Delete the Scratch Org

Salesforce reserves the right to delete a scratch org a specified number of days after it was created. You can also create a stage in your
pipeline that uses `org delete scratch` to explicitly delete your scratch org when the tests complete. This cleanup ensures better
management of your resources.

```
   // ------------------------------------------------------------------------
   // Delete package install scratch org.

   // ------------------------------------------------------------------------
   stage('Delete Package Install Scratch Org') {

      rc = command "${toolbelt}/sf org delete scratch --target-org installorg --no-prompt"

      if (rc != 0) {

        error 'Salesforce package install scratch org deletion failed.'

      }

   }

```

Create a Package

Now, let’s create a package. If you’re new to packaging, you can think about a package as a container that you fill with metadata. It
contains a set of related features, customizations, and schema. You use packages to move metadata from one Salesforce org to another.
After you create a package, add metadata and create a new package version.

```
   // ------------------------------------------------------------------------
   // Create package version.

   // ------------------------------------------------------------------------
   stage('Create Package Version') {

      if (isUnix()) {

        output = sh returnStdout: true, script: "${toolbelt}/sf package version create

   --package ${PACKAGE_NAME} --installation-key-bypass --wait 10 --json --target-dev-hub

   HubOrg"

      } else {

        output = bat(returnStdout: true, script: "${toolbelt}/sf package version create

   --package ${PACKAGE_NAME} --installation-key-bypass --wait 10 --json --target-dev-hub

   HubOrg").trim()

        output = output.readLines().drop(1).join(" ")

   }

```


Continuous Integration Jenkinsfile Walkthrough

```
      // Wait 5 minutes for package replication.

      sleep 300

      def jsonSlurper = new JsonSlurperClassic()

      def response = jsonSlurper.parseText(output)

      PACKAGE_VERSION = response.result.SubscriberPackageVersionId

      response = null

      echo ${PACKAGE_VERSION}

   }

```

Create a Scratch Org and Display Info

Remember when you created a scratch org earlier? Now let’s create a scratch org to install your package into, and display info about
that scratch org.

```
   // ------------------------------------------------------------------------
   // Create new scratch org to install package to.

   // ------------------------------------------------------------------------
   stage('Create Package Install Scratch Org') {

      rc = command "${toolbelt}/sf org create scratch --target-dev-hub HubOrg --set-default

    --definition-file config/project-scratch-def.json --alias installorg --wait 10

   --duration-days 1"

      if (rc != 0) {

        error 'Salesforce package install scratch org creation failed.'

      }

   }

   // ------------------------------------------------------------------------
   // Display install scratch org info.

   // ------------------------------------------------------------------------
   stage('Display Install Scratch Org') {

      rc = command "${toolbelt}/sf org display --target-org installorg"

      if (rc != 0) {

        error 'Salesforce install scratch org display failed.'

      }

   }

```

Install Package, Run Unit Tests, and Delete Scratch Org

To finish up, install your package in your scratch org, run unit tests, then delete the scratch org. That’s it!

```
   // ------------------------------------------------------------------------
   // Install package in scratch org.

   // ------------------------------------------------------------------------
   stage('Install Package In Scratch Org') {

```


### Continuous Integration Sample Jenkinsfile

```
      rc = command "${toolbelt}/sf package install --package ${PACKAGE_VERSION} --target-org

    installorg --wait 10"

      if (rc != 0) {

        error 'Salesforce package install failed.'

      }

   }

   // ------------------------------------------------------------------------
   // Run unit tests in package install scratch org.

   // ------------------------------------------------------------------------
   stage('Run Tests In Package Install Scratch Org') {

      rc = command "${toolbelt}/sf apex run test --target-org installorg --result-format tap

    --code-coverage --test-level ${TEST_LEVEL} --wait 10"

      if (rc != 0) {

        error 'Salesforce unit test run in pacakge install scratch org failed.'

      }

   }

   // ------------------------------------------------------------------------
   // Delete package install scratch org.

   // ------------------------------------------------------------------------
   stage('Delete Package Install Scratch Org') {

      rc = command "${toolbelt}/sf org delete scratch --target-org installorg --no-prompt"

      if (rc != 0) {

        error 'Salesforce package install scratch org deletion failed.'

      }

   }

```

SEE ALSO:

### Sample Jenkinsfile

[Pipeline-as-code with Multibranch Workflows in Jenkins](https://jenkins.io/blog/2015/12/03/pipeline-as-code-with-multibranch-workflows-in-jenkins/)

[TAP: Test Anything Protocol](https://testanything.org/)

Configure Your Environment for Jenkins

_[Salesforce CLI Command Reference](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_cli_reference.meta/sfdx_cli_reference)_

### Sample Jenkinsfile

A `Jenkinsfile` is a text file that contains the definition of a Jenkins Pipeline. This `Jenkinsfile` shows how to integrate Salesforce
CLI commands to automate testing of your Salesforce applications using scratch orgs.

[The Jenkinsfile Walkthrough topic uses this sfdx-jenkins-package](https://github.com/forcedotcom/sfdx-jenkins-package/blob/master/Jenkinsfile) `Jenkinsfile` as an example.

```
   #!groovy

   import groovy.json.JsonSlurperClassic

   node {

```


Continuous Integration Sample Jenkinsfile

```
      def SF_CONSUMER_KEY=env.SF_CONSUMER_KEY

      def SF_USERNAME=env.SF_USERNAME

      def SERVER_KEY_CREDENTALS_ID=env.SERVER_KEY_CREDENTALS_ID

      def TEST_LEVEL='RunLocalTests'

      def PACKAGE_NAME='0Ho1U000000CaUzSAK'

      def PACKAGE_VERSION

      def SF_INSTANCE_URL = env.SF_INSTANCE_URL ?: "https://login.salesforce.com"

      def toolbelt = tool 'toolbelt'

      // ------------------------------------------------------------------------
      // Check out code from source control.

      // ------------------------------------------------------------------------
      stage('checkout source') {

        checkout scm

      }

      // ------------------------------------------------------------------------
      // Run all the enclosed stages with access to the Salesforce

      // JWT key credentials.

      // ------------------------------------------------------------------------
      withEnv(["HOME=${env.WORKSPACE}"]) {

        withCredentials([file(credentialsId: SERVER_KEY_CREDENTALS_ID, variable:

   'server_key_file')]) {

           // ------------------------------------------------------------------------
           // Authorize the Dev Hub org with JWT key and give it an alias.

           // ------------------------------------------------------------------------
           stage('Authorize DevHub') {

            rc = command "${toolbelt}/sf org login jwt --instance-url ${SF_INSTANCE_URL}

    --client-id ${SF_CONSUMER_KEY} --username ${SF_USERNAME} --jwt-key-file ${server_key_file}

    --set-default-dev-hub --alias HubOrg"

             if (rc != 0) {

               error 'Salesforce dev hub org authorization failed.'

             }

           }

           // ------------------------------------------------------------------------
           // Create new scratch org to test your code.

           // ------------------------------------------------------------------------
           stage('Create Test Scratch Org') {

             rc = command "${toolbelt}/sf org create scratch --target-dev-hub HubOrg

   --set-default --definition-file config/project-scratch-def.json --alias ciorg --wait 10

   --duration-days 1"

             if (rc != 0) {

```


Continuous Integration Sample Jenkinsfile

```
               error 'Salesforce test scratch org creation failed.'

             }

           }

           // ------------------------------------------------------------------------
           // Display test scratch org info.

           // ------------------------------------------------------------------------
           stage('Display Test Scratch Org') {

             rc = command "${toolbelt}/sf org display --target-org ciorg"

             if (rc != 0) {

               error 'Salesforce test scratch org display failed.'

             }

           }

           // ------------------------------------------------------------------------
           // Push source to test scratch org.

           // ------------------------------------------------------------------------
           stage('Push To Test Scratch Org') {

             rc = command "${toolbelt}/sf project deploy start --target-org ciorg"

             if (rc != 0) {

               error 'Salesforce push to test scratch org failed.'

             }

           }

           // ------------------------------------------------------------------------
           // Run unit tests in test scratch org.

           // ------------------------------------------------------------------------
           stage('Run Tests In Test Scratch Org') {

             rc = command "${toolbelt}/sf apex run test --target-org ciorg --wait 10

   --result-format tap --code-coverage --test-level ${TEST_LEVEL}"

             if (rc != 0) {

               error 'Salesforce unit test run in test scratch org failed.'

             }

           }

           // ------------------------------------------------------------------------
           // Delete test scratch org.

           // ------------------------------------------------------------------------
           stage('Delete Test Scratch Org') {

             rc = command "${toolbelt}/sf org delete scratch --target-org installorg

   --no-prompt"

             if (rc != 0) {

               error 'Salesforce test scratch org deletion failed.'

             }

           }

```


Continuous Integration Sample Jenkinsfile

```
           // ------------------------------------------------------------------------
           // Create package version.

           // ------------------------------------------------------------------------
           stage('Create Package Version') {

             if (isUnix()) {

              output = sh returnStdout: true, script: "${toolbelt}/sf package version

    create --package ${PACKAGE_NAME} --installation-key-bypass --wait 10 --json --target-dev-hub

    HubOrg"

             } else {

              output = bat(returnStdout: true, script: "${toolbelt}/sf package version

    create --package ${PACKAGE_NAME} --installation-key-bypass --wait 10 --json --target-dev-hub

    HubOrg").trim()

               output = output.readLines().drop(1).join(" ")

             }

             // Wait 5 minutes for package replication.

             sleep 300

             def jsonSlurper = new JsonSlurperClassic()

             def response = jsonSlurper.parseText(output)

             PACKAGE_VERSION = response.result.SubscriberPackageVersionId

             response = null

             echo ${PACKAGE_VERSION}

           }

           // ------------------------------------------------------------------------
           // Create new scratch org to install package to.

           // ------------------------------------------------------------------------
           stage('Create Package Install Scratch Org') {

             rc = command "${toolbelt}/sf org create scratch --target-dev-hub HubOrg

   --set-default --definition-file config/project-scratch-def.json --alias installorg --wait

    10 --duration-days 1"

             if (rc != 0) {

               error 'Salesforce package install scratch org creation failed.'

             }

           }

           // ------------------------------------------------------------------------
           // Display install scratch org info.

           // ------------------------------------------------------------------------
           stage('Display Install Scratch Org') {

             rc = command "${toolbelt}/sf org display --target-org installorg"

             if (rc != 0) {

               error 'Salesforce install scratch org display failed.'

             }

```


Continuous Integration Sample Jenkinsfile

```
           }

           // ------------------------------------------------------------------------
           // Install package in scratch org.

           // ------------------------------------------------------------------------
           stage('Install Package In Scratch Org') {

             rc = command "${toolbelt}/sf package install --package ${PACKAGE_VERSION}

    --target-org installorg --wait 10"

             if (rc != 0) {

               error 'Salesforce package install failed.'

             }

           }

           // ------------------------------------------------------------------------
           // Run unit tests in package install scratch org.

           // ------------------------------------------------------------------------
           stage('Run Tests In Package Install Scratch Org') {

             rc = command "${toolbelt}/sf apex run test --target-org installorg

   --result-format tap --code-coverage --test-level ${TEST_LEVEL} --wait 10"

             if (rc != 0) {

              error 'Salesforce unit test run in pacakge install scratch org failed.'

             }

           }

           // ------------------------------------------------------------------------
           // Delete package install scratch org.

           // ------------------------------------------------------------------------
           stage('Delete Package Install Scratch Org') {

             rc = command "${toolbelt}/sf org delete scratch --target-org installorg

   --no-prompt"

             if (rc != 0) {

               error 'Salesforce package install scratch org deletion failed.'

             }

           }

        }

      }

   }

   def command(script) {

      if (isUnix()) {

        return sh(returnStatus: true, script: script);

      } else {

        return bat(returnStatus: true, script: script);

```


## Continuous Integration Continuous Integration with Travis CI

```
      }

   }

```

SEE ALSO:

Jenkinsfile Walkthrough

## Continuous Integration with Travis CI

Travis CI is a cloud-based continuous integration (CI) service for building and testing software projects hosted on GitHub.

For help with setting up Travis CI, see:

**•** [Sample Travis CI repo for Org Development model](https://github.com/forcedotcom/sfdx-travisci-org)

**•** [Sample Travis CI repo for Package Development model](https://github.com/forcedotcom/sfdx-travisci-package)

SEE ALSO:

[sfdx-travisci Sample GitHub Repo](https://github.com/forcedotcom/sfdx-travisci)

[Travis CI](https://travis-ci.org/)

## Sample CI Repos for Org Development Model

Get started quickly with CI by cloning a sample repository from your vendor of choice. Each repo has a sample configuration file and a
comprehensive `README.md` with step-by-step information.

These sample repositories support the org development model. This model uses Salesforce CLI, a source control system, and sandboxes
[during the application life cycle. To determine if this model is right for you, head over and earn your badge by completing the Org](https://trailhead.salesforce.com/content/learn/modules/org-development-model)
[Development Model module.](https://trailhead.salesforce.com/content/learn/modules/org-development-model)

## Sample CI Repos for Package Development Model

Get started quickly with CI by cloning a sample repository from your vendor of choice. Each repo has a sample configuration file and a
comprehensive `README.md` with step-by-step information.


Continuous Integration Sample CI Repos for Package Development Model

These sample repositories support the package development model. This model uses Salesforce CLI, a source control system, scratch
orgs for development, and sandboxes for testing and staging. To determine if this model is right for you, head over and earn your badge
[by completing the Package Development Model module.](https://trailhead.salesforce.com/content/learn/modules/sfdx_dev_model)


# CHAPTER 15 Troubleshoot Salesforce DX

In this chapter ...

**•** Resolve Common
Authorization Errors

**•** Error: No default dev
hub found

**•** Unable to Work After
Failed Org
Authorization

**•** Error: The consumer
key is already taken

**•** CLI Version
Information

Here are some tips to help you troubleshoot issues.

SEE ALSO:

[Salesforce Trailblazer Community](https://success.salesforce.com/_ui/core/chatter/groups/GroupProfilePage?g=0F93A000000HTp1)


## Troubleshoot Salesforce DX Resolve Common Authorization Errors Resolve Common Authorization Errors

### Errors sometimes occur when you run either org login web or org login jwt to log into and authorize an org. Here are

some of the more common errors, what they mean, and what you can do to try to fix them.

Before you begin, update to the most recent version of Salesforce CLI and check if you still see the issue. Salesforce releases a new CLI
version every week.

If you installed Salesforce CLI using the installers, run this command.

```
   sf update

```

If you installed using npm, run this command.

```
   npm install --global @salesforce/cli

```

For each error, we provide this information:

**•** **Error text** : Literal text of the error.

**•** **Error name** : The name of the error, which is also displayed in the error message.

**•** **What it likely means** : While it’s often difficult to determine precisely what happened in your environment, we make a best guess
about what it could be.

**•** **Recommended fixes** : One or more things you can try to fix the problem, with the one most likely to work listed first.

**•** **NOT RECOMMENDED** : Actions you should never take.

### org login web Errors These errors can occur when you run org login web to authorize an org by logging into it using a web browser.

Error: authentication failure

**•** **Error text** : `Invalid client credentials. Verify the OAuth client secret and ID. Error`

```
    authenticating with auth code due to: invalid_grant::authentication failure

```

**•** **Error name** : `AuthCodeExchangeError`

**•** **What it likely means** : You don’t have permission to access the org. The problem can stem from an issue with the connected app,
settings, org settings, or with a customization, such as a guest flow that must run before authorization.

**•** **Recommended fixes** :

**–** Use the most recent version of Salesforce CLI and its core plugins. To verify, run the `doctor` command.

**–** Make sure that the org is configured to allow API access, and that you specifically have API access to the org. Both settings are
required to run any CLI command that involves an org.

**–** Use the correct instance URL when logging in to the org, and make sure that it’s in the correct enhanced My Domain format. To
find your org's instance URL, log into it, go to the Setup > Company Settings > My Domain page, and see **Current My Domain**
**URL** [. See My Domain Login and Application URL Formats with Enhanced Domains.](https://help.salesforce.com/s/articleView?id=products.domain_name_url_formats.htm&type=5&language=en_US)

**–** Check that your connected app settings are correct, especially if you created your own rather than use the default Salesforce CLI
[connected app. See Create a Connected App in Your Org.](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_auth_connected_app.htm)


Troubleshoot Salesforce DX org login web Errors

Error: unable to get local issuer certificate

**•** **Error text** : `Invalid client credentials. Verify the OAuth client secret and ID. Error`

```
    authenticating with auth code due to: request to

    https://test.salesforce.com//services/oauth2/token failed, reason: unable to get

    local issuer certificate

```

**•** **Error name** : `AuthCodeExchangeError` or `AuthCodeUsernameRetrievalError`

**•** **What it likely means** : Node.js can’t find the certificate that it uses for HTTPS traffic in the certificate store on the local computer.
The problem can be related to a proxy, firewall, or VPN that’s between the client and server. For example, the proxy could be
configured for "deep inspection" in which the proxy swaps the SSL certificate with its own certificate to allow it to inspect traffic,
and the proxy certificate is causing the error.

**•** **Recommended fixes** :

**–** Set the `NODE_EXTRA_CA_CERTS` environment variable to include expected certificates.

**–** If using a proxy, make sure that the `HTTPS_PROXY` and `HTTP_PROXY` environment variables are set properly.

**–** Check the proxy settings for specific certificate behavior.

**•** **NOT RECOMMENDED** :

**–** Don’t set `NODE_TLS_REJECT_UNAUTHORIZED=0`, which disables certificate verification for Salesforce CLI requests and
allows man-in-the-middle attacks.

**–** Don’t set the `strict-ssl=false` npm configuration setting. This setting allows npm to use HTTP rather than HTTPS and
allows unencrypted traffic and man-in-the-middle attacks.

Error: grant type not supported

**•** **Error text** : `Invalid client credentials. Verify the OAuth client secret and ID. Error`

```
    authenticating with auth code due to: unsupported_grant_type::grant type not supported

```

**•** **Error name** : `AuthCodeExchangeError`

**•** **What it likely means** : The OAuth 2.0 endpoint doesn’t support the grant_type value passed to it. If you're using the default Salesforce
CLI connected app, this error usually means that you're using the wrong instance URL to log in. If you’re using a different connected
app, check to see if it’s configured correctly for the grant types used by the CLI.

**•** **Recommended fixes** :

**–** Use the correct instance URL when logging in to the org, and make sure that it’s in the correct enhanced My Domain format. To
find your org's instance URL, log into it, go to the Setup > Company Settings > My Domain page, and see **Current My Domain**
**URL** [. See My Domain Login and Application URL Formats with Enhanced Domains.](https://help.salesforce.com/s/articleView?id=products.domain_name_url_formats.htm&type=5&language=en_US)

**–** Don't use a Lightning URL for your instance URL. For example, use `https://MyDomainName.my.salesforce.com`
and not `https://MyDomainName.lightning.force.com` .

**–** Make sure you always use `https`, and not `http`, for all URLs.

**–** Make sure that the org is configured to allow API access, and that you specifically have API access to the org. Both settings are
required to run any CLI command that involves an org.

**–** Check that the clock on your local computer is accurate. If too much time (over 3 minutes) passes between the auth code
generation and the request for an access token, an error like this can occur.

**–** [If you're using a custom connected app rather than the default Salesforce CLI one, check that the settings are correct. See Create](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_auth_connected_app.htm)
[a Connected App in Your Org.](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_auth_connected_app.htm)


Troubleshoot Salesforce DX org login web Errors

Error: ECONNRESET

**•** **Error text** : `Invalid client credentials. Verify the OAuth client secret and ID. Error`

```
    authenticating with auth code due to: request to

    https://test.salesforce.com//services/oauth2/token failed, reason: read ECONNRESET

```

**•** **Error name** : `AuthCodeExchangeError`

**•** **What it likely means** : Your org reset the connection.

**•** **Recommended fixes** :

**–** Rerun the `org login web` command. This error is sometimes temporary and simply reauthorizing the org fixes it.

**–** Use the most recent version of Salesforce CLI and its core plugins. To verify, run the `doctor` command.

**–** Use the correct instance URL when logging in to the org, and make sure that it’s in the correct enhanced My Domain format. To
find your org's instance URL, log into it, go to the Setup > Company Settings > My Domain page, and see **Current My Domain**
**URL** [. See My Domain Login and Application URL Formats with Enhanced Domains.](https://help.salesforce.com/s/articleView?id=products.domain_name_url_formats.htm&type=5&language=en_US)

Error: ETIMEDOUT

**•** **Error text** : `Invalid client credentials. Verify the OAuth client secret and ID. Error`

```
    authenticating with auth code due to: request to

    https://test.salesforce.com//services/oauth2/token failed, reason: connect ETIMEDOUT

```

**•** **Error name** : `AuthCodeExchangeError`

**•** **What it likely means** : The connection to your org timed out.

**•** **Recommended fixes** :

**–** Rerun the `org login web` command. This error is sometimes temporary and simply reauthorizing the org fixes it.

**–** Use the most recent version of Salesforce CLI and its core plugins. To verify, run the `doctor` command.

**–** Use the correct instance URL when logging in to the org, and make sure that it’s in the correct enhanced My Domain format. To
find your org's instance URL, log into it, go to the Setup > Company Settings > My Domain page, and see **Current My Domain**
**URL** [. See My Domain Login and Application URL Formats with Enhanced Domains.](https://help.salesforce.com/s/articleView?id=products.domain_name_url_formats.htm&type=5&language=en_US)

Error: self-signed certificate in certificate chain

**•** **Error text** : `Invalid client credentials. Verify the OAuth client secret and ID. Error`

```
    authenticating with auth code due to: request to

    https://login.salesforce.com//services/oauth2/token failed, reason: self-signed

    certificate in certificate chain

```

**•** **Error name** : `AuthCodeExchangeError` or `AuthCodeUsernameRetrievalError`

**•** **What it likely means** : During certificate verification, Node.js encountered a certificate that can't be chained to a root certificate in
the local trust store, or the root certificate is not locally trusted. The problem can be related to a proxy, firewall, or VPN that’s between
the client and server. For example, the proxy could be configured for "deep inspection" in which the proxy swaps the SSL certificate
with its own certificate to allow it to inspect traffic, and the proxy certificate is causing the error.

**•** **Recommended fixes** :

**–** Don't trust any unknown certificates.

**–** Make sure all certificates are properly created.

**–** Make sure that the certificates you're using are trusted within the trust store or added to the `NODE_EXTRA_CA_CERTS`
environment variable.


### Troubleshoot Salesforce DX org login jwt Errors

**–** If using a proxy, make sure that the `HTTPS_PROXY` and `HTTP_PROXY` environment variables are set properly.

**–** Check the proxy settings for specific certificate behavior.

**•** **NOT RECOMMENDED** :

**–** Don’t set `NODE_TLS_REJECT_UNAUTHORIZED=0`, which disables certificate verification for Salesforce CLI requests and
allows man-in-the-middle attacks.

**–** Don’t set the `strict-ssl=false` npm configuration setting. This setting allows npm to use HTTP rather than HTTPS and
allows unencrypted traffic and man-in-the-middle attacks.

Error: IP restricted

**•** **Error text** : `Invalid client credentials. Verify the OAuth client secret and ID. Error`

```
    authenticating with auth code due to: ip restricted

```

**•** **Error name** : `AuthCodeExchangeError`

**•** **What it likely means** : The org has IP restrictions enabled. If Salesforce CLI attempts to log in and authorize an org from an IP address
that isn't allowed, then this error is thrown.

**•** **Recommended fix** [: If the IP address that Salesforce CLI uses is known and allowed, update your org's Trusted IP Ranges.](https://help.salesforce.com/s/articleView?id=xcloud.security_networkaccess.htm&type=5&language=en_US)

Error: ENOTFOUND

**•** **Error text** : `Invalid client credentials. Verify the OAuth client secret and ID. Error`

```
    authenticating with auth code due to: request to

    https://login.salesforce.com/services/oauth2/token failed, reason: getaddrinfo

    ENOTFOUND login.salesforce.com

### • Error name : AuthCodeExchangeError or AuthCodeUsernameRetrievalError

```

**•** **What it likely means** : The domain name couldn't be resolved within the time limit. The error could be caused by an incorrect
instance URL, a DNS issue, or a proxy issue.

**•** **Recommended fixes** :

**–** Use the most recent version of Salesforce CLI and its core plugins. To verify, run the `doctor` command.

**–** Use the correct instance URL when logging in to the org, and make sure that it’s in the correct enhanced My Domain format. To
find your org's instance URL, log into it, go to the Setup > Company Settings > My Domain page, and see **Current My Domain**
**URL** [. See My Domain Login and Application URL Formats with Enhanced Domains.](https://help.salesforce.com/s/articleView?id=products.domain_name_url_formats.htm&type=5&language=en_US)

**–** Don't use a Lightning URL for your instance URL. For example, use `https://MyDomainName.my.salesforce.com`
and not `https://MyDomainName.lightning.force.com` .

**–** Make sure you can use a command-line tool, such as `nslookup`, to resolve the domain manually from the same computer
from which you're running the `org login web` command.

**–** If using a proxy, make sure that the `HTTPS_PROXY` and `HTTP_PROXY` environment variables are set properly.

### org login jwt Errors These errors can occur when you run org login jwt to authorize an org by logging into it with the JWT flow.


Troubleshoot Salesforce DX org login jwt Errors

Error: user hasn't approved this consumer

**•** **Error text** : `We encountered a JSON web token error, which is likely not an issue with`

```
    Salesforce CLI. Here’s the error: Error authenticating with JWT. Errors encountered:

    user hasn't approved this consumer

```

**•** **Error name** : `JwtGrantError`

**•** **What it likely means** : Your connected app settings aren't configured correctly or a new connected app hasn't finished replicating.

**•** **Recommended fixes** :

**–** Use the most recent version of Salesforce CLI and its core plugins. To verify, run the `doctor` command.

**–** If you recently created the connected app, wait a few minutes for it to finish replicating and then try to authorize again.

**–** Check that your connected app settings are correct, especially if you created your own rather than used the default Salesforce
[CLI connected app. See Create a Connected App in Your Org. In particular, on the main page where you manage the connected](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_auth_connected_app.htm)
app:

**•** Set **Permitted Users** to `Admin approved users are pre-authorized` .

**•** Add the profile of the user you want to authorize by clicking **Manage Profiles** .

**–** Use the correct instance URL when logging in to the org, and make sure that it’s in the correct enhanced My Domain format.
You can specify the instance URL either with the `--instance-url` command flag or the `SF_AUDIENCE_URL` environment
variable, although `SF_AUDIENCE_URL` isn't usually needed for production environments. To find your org's instance URL,
log into it, go to the Setup > Company Settings > My Domain page, and see **Current My Domain URL** [. See My Domain Login](https://help.salesforce.com/s/articleView?id=products.domain_name_url_formats.htm&type=5&language=en_US)
[and Application URL Formats with Enhanced Domains.](https://help.salesforce.com/s/articleView?id=products.domain_name_url_formats.htm&type=5&language=en_US)

**–** Don't use a Lightning URL for your instance URL. For example, use `https://MyDomainName.my.salesforce.com`
and not `https://MyDomainName.lightning.force.com` .

Error: client identifier invalid

**•** **Error text** : `We encountered a JSON web token error, which is likely not an issue with`

```
    Salesforce CLI. Here’s the error: Error authenticating with JWT. Errors encountered:

    client identifier invalid

```

**•** **Error name** : `JwtGrantError`

**•** **What it likely means** : The OAuth client ID (also called consumer key) that you passed to the command's `--client-id` flag
doesn’t match the one specified in the connected app.

**•** **Recommended fixes** :

**–** Use the most recent version of Salesforce CLI and its core plugins. To verify, run the `doctor` command.

**–** Make sure that the client ID and client secret that are configured in your connected app settings match the values you passed
to the `org login jwt` command.

**–** Use the correct instance URL when logging in to the org, and make sure that it’s in the correct enhanced My Domain format.
You can specify the instance URL either with the `--instance-url` command flag or the `SF_AUDIENCE_URL` environment
variable, although `SF_AUDIENCE_URL` isn't usually needed for production environments. To find your org's instance URL,
log into it, go to the Setup > Company Settings > My Domain page, and see **Current My Domain URL** [. See My Domain Login](https://help.salesforce.com/s/articleView?id=products.domain_name_url_formats.htm&type=5&language=en_US)
[and Application URL Formats with Enhanced Domains.](https://help.salesforce.com/s/articleView?id=products.domain_name_url_formats.htm&type=5&language=en_US)

**–** Don't use a Lightning URL for your instance URL. For example, use `https://MyDomainName.my.salesforce.com`
and not `https://MyDomainName.lightning.force.com` .


Troubleshoot Salesforce DX org login jwt Errors

Error: ENOENT

**•** **Error text** : `We encountered a JSON web token error, which is likely not an issue with`

```
    Salesforce CLI. Here’s the error: ENOENT: no such file or directory, open

    '/workspace/my-repository/server.key'

```

**•** **Error name** : `JwtGrantError`

**•** **What it likely means** : The private JWT key file that you specified with the `--jwt-key-file` flag of the `org login jwt`
either doesn't exist or it's in a different location. This issue typically occurs in CI (continuous integration) environments where the
private JWT key file is accessible for only specific actions.

**•** **Recommended fix** : Make sure that the private JWT key file exists in the specified location and is accessible by all Salesforce CLI
commands that interact with an org, because these commands must authenticate before they can send API requests.

Error: HTML response

**•** **Error text** : `Data Not Available webpage. “The data you were trying to access could not be`

```
    found. It may be due to another user deleting the data or a system error. If you

    know the data is not deleted but cannot access it, please look at our support page”

```

**•** **Error name** : `JwtGrantError`

**•** **What it likely means** : The org is temporarily down for maintenance or isn't yet ready for API requests.

**•** **Recommended fixes** : This error is probably temporary. Wait a few minutes and retry. If this error happens regularly, contact Salesforce
Customer Support.

Error: audience is invalid

**•** **Error text** : `We encountered a JSON web token error, which is likely not an issue with`

```
    Salesforce CLI. Here’s the error: Error authenticating with JWT. Errors encountered:

    audience is invalid [audience=https://login.salesforce.com

    login=https://test.salesforce.com/]

```

**•** **Error name** : `JwtGrantError`

**•** **What it likely means** : This error usually occurs with other errors such as `user hasn't approved this consumer` . This
error can also indicate that you used the incorrect instance URL with the command.

**•** **Recommended fixes** :

**–** Use the most recent version of Salesforce CLI and its core plugins. To verify, run the `doctor` command.

**–** Use the correct instance URL when logging in to the org, and make sure that it’s in the correct enhanced My Domain format.
You can specify the instance URL either with the `--instance-url` command flag or the `SF_AUDIENCE_URL` environment
variable, although `SF_AUDIENCE_URL` isn't usually needed for production environments. To find your org's instance URL,
log into it, go to the Setup > Company Settings > My Domain page, and see **Current My Domain URL** [. See My Domain Login](https://help.salesforce.com/s/articleView?id=products.domain_name_url_formats.htm&type=5&language=en_US)
[and Application URL Formats with Enhanced Domains.](https://help.salesforce.com/s/articleView?id=products.domain_name_url_formats.htm&type=5&language=en_US)

**–** Don't use a Lightning URL for your instance URL. For example, use `https://MyDomainName.my.salesforce.com`
and not `https://MyDomainName.lightning.force.com` .

**–** If using a proxy, make sure that the `HTTPS_PROXY` and `HTTP_PROXY` environment variables are set properly.


## Troubleshoot Salesforce DX Error: No default dev hub found

**–** If you see additional errors, check this topic for troubleshooting information about those errors.

SEE ALSO:

[Authorize an Org Using a Browser](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_auth_web_flow.htm)

[Authorize an Org Using the JWT Flow](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_auth_jwt_flow.htm)

_Salesforce Help_ [: OAuth 2.0 Web Server Flow for Web App Integration](https://help.salesforce.com/s/articleView?id=xcloud.remoteaccess_oauth_web_server_flow.htm&type=5&language=en_US)

_Salesforce Help_ [: Set Trusted IP Ranges for Your Organization](https://help.salesforce.com/s/articleView?id=xcloud.security_networkaccess.htm&type=5&language=en_US)

## Error: No default dev hub found

You see this error when you try to create a scratch org due to an authorization issue.

Let’s say you successfully authorize a Dev Hub org using the `--set-default-dev-hub` flag. The username associated with the
org is your default Dev Hub username. You then successfully create a scratch org without using the `--target-dev-hub` flag. But
when you try to create a scratch org another time using the same CLI command, you get this error:

```
   Error (1): No default dev hub found. Use -v or --target-dev-hub to specify an environment.

```

What happened?

**Answer** : You’re no longer in the directory where you ran the authorization command. The directory from which you use the
`--set-default-dev-hub` flag matters.

If you run the authorization command from the root of your project directory, the `target-dev-hub` config variable is set locally.
The value applies only when you run the command from the same project directory. If you change to a different directory and run `org`
`create scratch`, the local setting of the default Dev Hub org no longer applies and you get an error.

Solve the problem by doing one of the following.

**•** Set `target-dev-hub` globally so that you can run `org create scratch` from any directory.

```
     sf config set target-dev-hub=<devhubusername> --global

```

**•** Run `org create scratch` from the same project directory where you authorized your Dev Hub org.

**•** Use the `--target-dev-hub` flag with `org create scratch` to run it from any directory.

```
     sf target-dev-hub --definition-file <file> --target-dev-hub <devhubusername> --alias

     my-scratch-org

```

**•** To check whether you’ve set configuration values globally or locally, use this command and check the Location column.

```
     sf config list

```

SEE ALSO:

How Salesforce Developer Experience (DX) Tooling Changes the Way You Work

## Unable to Work After Failed Org Authorization

Sometimes you try to authorize a Dev Hub org or a scratch org using the Salesforce CLI or an IDE, but you don’t successfully log in to
the org. The port remains open for the stray authorization process, and you can’t use the CLI or IDE. To proceed, end the process manually.


## Troubleshoot Salesforce DX Error: The consumer key is already taken

macOS or Linux

To recover from a failed org authorization on macOS or Linux, use a terminal to kill the process running on port 1717.

**1.** From a terminal, run:

```
     lsof -i tcp:1717

```

**2.** In the results, find the ID for the process that’s using the port.

**3.** Run:

```
     kill -9 <the process ID>

```

Windows

To recover from a failed org authorization on Windows, use the Task Manager to end the Node process.

**1.** Press Ctrl+Alt+Delete, then click **Task Manager** .

**2.** Select the **Process** tab.

**3.** Find the process named `Node` .

Note: If you’re a Node.js developer, you can have several running processes with this name.

**4.** Select the process that you want to end, and then click **End Process** .

## Error: The consumer key is already taken

Let’s say you run `project retrieve start` on an org in which you’ve created a connected app. When you try to deploy the
retrieved source to a different org, the deploy fails with the error `The consumer key is already taken` . What happened?

Connected apps include a consumer key that a website or app uses to identify itself to Salesforce. Consumer keys must be unique across
the entire Salesforce ecosystem. When you try to deploy the retrieved (and unchanged) source file associated with the connected app
to a new org, the deploy fails due to duplicate consumer keys.

You have a few options to work around this problem.

**•** Remove the connected app source file from your project before you deploy your source to the new org. As a result, the connected
app isn’t created. The connected app source file is named something like
`force-app/main/default/connectedApps/MyConnApp.connectedApp-meta.xml` .

**•** Update the file for the connected app and change the value of the `<consumerKey>` element to a unique value. Here’s a snippet
of a sample connected app file that shows the `<consumerKey>` element.

```
     <?xml version="1.0" encoding="UTF-8"?>

     <ConnectedApp xmlns="http://soap.sforce.com/2006/04/metadata">

       <contactEmail>john@doecompany.com</contactEmail>

       <contactPhone>5556789</contactPhone>

       <label>MyConnApp</label>

       <oauthConfig>

          <callbackUrl>http://localhost:1717/OauthRedirect</callbackUrl>

          <consumerKey>3MVG9PG9sFc71i9n55UWbx2</consumerKey>

```


## Troubleshoot Salesforce DX CLI Version Information

```
          <isAdminApproved>false</isAdminApproved>

     ...

```

SEE ALSO:

_Salesforce Help_ [: Connected Apps](https://help.salesforce.com/s/articleView?id=xcloud.connected_app_overview.htm&type=5&language=en_US)

## CLI Version Information

Use these commands to view version information about Salesforce CLI.

```
   sf plugins --core // Version of the CLI and all installed plug-ins

   sf --version // CLI version

```


# CHAPTER 16 Limitations for Salesforce DX

Here are some known issues you could run into while using Salesforce DX.

[For the latest known issues, visit the Trailblazer Community’s Known Issues page and the issues tab in](https://success.salesforce.com/issues_index?tag=Salesforce%20DX)
[the Salesforce CLI’s main GitHub repo.](https://github.com/forcedotcom/cli/issues)

Salesforce CLI

**Can’t Import Record Types Using Salesforce CLI**
**Description:** We don't support RecordType when running the `data tree import` command.

**Workaround:** None.

**Limited Support for Shell Environments on Windows**
**Description:** Salesforce CLI is tested on the Command Prompt ( `cmd.exe` ) and Powershell. There
are known issues in the Cygwin and Min-GW environments, and with Windows Subsystem for Linux
(WSL). Until these environments are tested and supported in a future release, we recommend that
you use a supported shell.

**Workaround:** None.

Dev Hub and Scratch Orgs

**Salesforce CLI Sometimes Doesn’t Recognize Scratch Orgs with Communities**
**Description:** Sometimes, but not in all cases, the Salesforce CLI doesn’t acknowledge the creation
of scratch orgs with the Communities feature. You can’t open the scratch org using the CLI, even
though the scratch org is listed in Dev Hub.

**Workaround:** You can try this workaround, although it doesn’t fix the issue in all cases. Delete the
scratch org in Dev Hub, then create a new scratch org using the CLI. Deleting and recreating scratch
orgs counts against your daily scratch org limits.

**Error Occurs If You Pull a Community and Deploy It**
**Description:** The error occurs because the scratch org doesn’t have the required guest license.

**Workaround:** In your scratch org definition file, if you specify the Communities feature, also specify
the Sites feature.


Limitations for Salesforce DX

Source Management

**ERROR: Entity of type 'RecordType' named 'Account.PersonAccount' cannot be found**
**Description:** Although you can turn on Person Accounts in your scratch org by adding the feature
to your scratch org definition, running `project deploy start` or `project deploy`
`retrieve` results in an error.

**Workaround:** None.

**`project convert source`** **Doesn’t Add Post-Install Scripts to** **`package.xml`**
**Description:** If you run `project convert source`, `package.xml` doesn’t include the
post install script.

**Workaround:** To fix this issue, choose one of these methods:

**•** Manually add the `<postInstallClass>` element to the `package.xml` in the metadata
directory that `project convert source` produces.

**•** Manually add the element to the package in the release org or org to which you are deploying
the package.

**Must Manually Enable Feed Tracking in an Object's Metadata File**
**Description:** If you enable feed tracking on a standard or custom object, then run `project`
`retrieve start`, feed tracking doesn't get enabled.

**Workaround:** In your Salesforce DX project, manually enable feed tracking on the standard or
custom object in its metadata file ( `-meta.xml` ) by adding
`<enableFeeds>true</enableFeeds>` .

**Unable to Push Lookup Filters to a Scratch Org**
**Description:** When you execute the `project deploy start` command to deploy the source
of a relationship field that has a lookup filter, you sometimes get this error:

```
  duplicate value found: <unknown> duplicates value on record with
```

`id: <unknown> at line num, col num` .

**Workaround:** None.

Deployment

**Compile on Deploy Can Increase Deployment Times in Scratch Orgs**
**Description:** If your deployment times for Apex code are slow, your scratch org might have the
`enableCompileOnDeploy` setting set to `true` .

**Workaround:** To turn it off, set it to `false` (the default) or delete the setting from the scratch org
definition.

```
  {

   "orgName": "My Company",

   "edition": "Developer",

   "features": [],

   "settings": {

    "lightningExperienceSettings": {

        "enableS1DesktopEnabled": true

      },

      "apexSettings": {

```


Limitations for Salesforce DX

```
        "enableCompileOnDeploy": false

      }

   }

  }

```

Managed First-Generation Packages

**When You Install a Package in a Scratch Org, No Tests Are Performed**
**Description:** If you include tests as part of your continuous integration process, those tests don’t
run when you install a package in a scratch org.

**Workaround:** You can manually execute tests after the package is installed.

**New Terminology in CLI for Managed Package Password**
**Description:** When you use the CLI to add an installation key to a package version or to install a
key-protected package version, the flag name of the key is `--installationkey` . When you
view a managed package version in the Salesforce user interface, the same package attribute is
called “Password”. In the API, the corresponding field name, “password”, is unchanged.

**Workaround:** None.

Managed Second-Generation Packages

**Protected Custom Metadata and Custom Settings are Visible to Developers in a Scratch Org If**
**Installed Packages Share a Namespace**
**Description:** Use caution when you store secrets in your second-generation packages using protected
custom metadata or protected custom settings. You can create multiple second-generation packages
with the same namespace. However, when you install these packages in a scratch org, these secrets
are visible to any of your developers that are working in a scratch org with a shared namespace. In
the future, we might add a “package-protected” keyword to prevent access to package secrets in
these situations.

**Workaround:** None.

Unlocked Packages

**Protected Custom Metadata and Custom Settings are Visible to Developers in a Scratch Org If**
**Installed Packages Share a Namespace**
**Description:** Use caution when you store secrets in your unlocked packages using protected custom
metadata or protected custom settings. You can create multiple unlocked packages with the same
namespace. However, when you install these packages in a scratch org, these secrets are visible to
any of your developers that are working in a scratch org with a shared namespace. In the future, we
might add a “package-protected” keyword to prevent access to package secrets in these situations.

**Workaround:** None.

