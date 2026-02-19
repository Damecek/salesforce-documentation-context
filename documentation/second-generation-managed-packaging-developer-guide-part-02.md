#### What to Consider Before Removing Metadata Components

In most cases, removing metadata components from a second-generation managed package marks the component as deprecated
and doesn’t hard delete the component from the subscriber org. This approach to component removal ensures that package
upgrades don’t disrupt a subscriber’s org.

#### What to Consider Before Removing Metadata Components

In most cases, removing metadata components from a second-generation managed package marks the component as deprecated and
doesn’t hard delete the component from the subscriber org. This approach to component removal ensures that package upgrades don’t
disrupt a subscriber’s org.

But there’s a scenario where a deprecated component can lead to a package upgrade issue. This issue only pertains to deprecated
components, and no action is needed for hard deleted components.

[To see which components are deprecated and which are deleted, see Remove Metadata Components from Second-Generation Managed](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_remove_md_components.htm)
[Packages.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_remove_md_components.htm)

Here’s an example scenario of how a deprecated component leads to a package upgrade issue.

**1.** Subscriber A installs version 1.0 of a managed package.

**2.** A package developer removes project__c custom object, and creates package version 2.0.

**3.** Subscriber A upgrades from version 1.0 to version 2.0, and project__c is now marked as deprecated in their org. Any integration
with project__c that the subscriber created continues to work.

**4.** The package developer continues to refine their app, and then releases several new versions.


### Second-Generation Managed Packages Delete a Second-Generation Managed Package or Package

Version

**5.** During development of version 5.0, the package developer adds a component named project__c to the package.

**6.** A new subscriber, Subscriber B, successfully installs version 5.0.

**7.** Subscriber A tries to upgrade to version 5.0, but the installation fails because the admin at Subscriber A never deleted project__c
from their org.

**8.** The package developer has two paths to unblock Subscriber A.

**a.** Ask Subscriber A to remove all references to project__c, and then delete the component from their org.

**b.** Remove project__c from the package and release a new package version.

To prevent this kind of API name collisions in your packages, here are some best practices.

**Communicate within Your Team and Company**
Before you remove any metadata, assess the impact to the package and to any packages that depend on that package. If you remove
metadata in one package, that action has the potential to break the functionality of a package that depends on the removed metadata.
Communicate within your team and company so that other developers are aware of this change.

**Document Package Changes for Future Developers**
If you internally document the major changes that your package undergoes, including the name of metadata components that were
removed, you can help alert future package developers about previously used API names.

**Communicate Changes with Your Subscribers**
Educate your customers about the potential impact from any components you remove. In the Release Notes for your upgraded
package, list all components you’ve removed and notify customers of any necessary actions.

### Delete a Second-Generation Managed Package or Package Version

Use the `sf package version delete` and `sf package delete` commands to delete packages and package versions
that you no longer need.

To delete a package or package version, users need the Delete Second-Generation Packages user permission. Before you delete a package,
first delete all associated package versions.

**Considerations for Deleting a Package or Package Version**

**•** Deletion is permanent.

**•** Attempts to install a deleted package version will fail.

**•** Before deleting, ensure that the package or package version isn’t referenced as a dependency.


### Second-Generation Managed Packages Frequently Used Packaging Operations for

Second-Generation Managed Packages

**Examples:**

```
   $ sf package delete -p "Your Package Alias"

   $ sf package delete -p 0Ho...

   $ sf package version delete -p "Your Package Version Alias"

   $ sf package version delete -p 04t...

```

These CLI commands can’t be used with first-generation managed packages or package versions. To delete a first-generation managed
[package, see View Package Details in the](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/isv_viewing_package_details.htm) _First-Generation Managed Packaging Developer Guide_ .

### Frequently Used Packaging Operations for Second-Generation Managed

Packages

[For a complete list of Salesforce CLI packaging commands, see: Salesforce Command Line Reference Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_package_commands_unified.htm)

### Transfer a Second-Generation Managed Package to a Different Dev Hub

You can transfer the ownership of a second-generation managed package (managed 2GP) from one Dev Hub org to another. These
transfers can occur either internally between two Dev Hub orgs your company owns, or you can transfer a package externally to another
Salesforce Partner or ISV. This change provides a way to sell a second-generation managed package to a different company.

Note: Package transfers are only available for second-generation managed packages that have passed AppExchange security
review. If your managed 2GP package hasn’t passed security review, consider creating a new managed 2GP using your preferred
Dev Hub.

The package transfer feature is also available to unlocked packages. Dev Hub orgs aren’t used with first-generation managed
packages or unmanaged packages, so this feature doesn’t apply to those package types.


Second-Generation Managed Packages Transfer a Second-Generation Managed Package to a
Different Dev Hub

Request a Package Transfer to a Different Dev Hub

Start by logging a case with Salesforce Customer Support, and provide the following details.

`Subject:` Managed 2GP Package Transfer to a different Dev Hub

```
   Description:

```

In the description, list:

**•** Subscriber package ID of the package you’re transferring. This ID starts with 033.

To verify the 033 ID of your package, run the `sf package list` command with the `-–verbose` flag on the source Dev Hub
org.

**•** Dev Hub org ID for the source org.

**•** Dev Hub org ID for the destination org. The destination Dev Hub org can’t be a Developer Edition org or a trial org.

**•** Namespace of the package being transferred.

**•** Details about whether this package transfer is internal or external.

An external transfer occurs when you transfer a package to a Salesforce Partner or ISV who doesn’t work at your company.

**•** Acknowledge that you’ve reviewed and completed the steps listed in the `Prepare to Transfer Your Package` section,
including linking your namespace to the destination Dev Hub, and clearing your Apex Error Notification User.

If you’re transferring more than one package, file a separate case for each package.

After your case has been reviewed and approved, someone from Salesforce Customer Support will contact you to arrange a time to
initiate the package transfer.

Note: For security reasons, package transfers between a Dev Hub located in Government Cloud and a Dev Hub located outside
Government Cloud aren’t permitted.

Package Transfers to External Customers

If you’re transferring a package to another Salesforce Partner or ISV, provide:

**•** The source code and config settings needed to properly set up their Salesforce DX environment.

All config settings needed to properly set up the `sfdx-project.json` file, and a complete list of features and settings that
must be specified in their scratch org definition file.

**•** The login credentials to the namespace org. This information is required to link the package namespace to their Dev Hub org.

Prepare to Transfer Your Package

Here’s how you can help ensure a smooth package transfer.

**•** [Keep the namespace linked to the source Dev Hub. Before the package transfer, the namespace must be linked to both the source](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_create_namespace.htm)
and destination Dev Hub orgs.

**•** Before the package transfer process is initiated, ensure all push upgrades or package version creation processes have completed.

**•** Delete package versions that are no longer needed.

**•** If specified, clear the package’s Error Notification User using the `sf package update`
`--error-notification-username=` command. If you’re transferring the package to a Dev Hub org that you own, you
can set the Error Notification User to a user in the destination Dev Hub after the package transfer is complete. Note: Specifying
`--error-notification-username=` with no value after the equals sign clears any previously set username.


Second-Generation Managed Packages Transfer a Second-Generation Managed Package to a
Different Dev Hub

During the Package Transfer Process

All push upgrades or package version creation processes must be complete before the package transfer process is initiated. Salesforce
Customer Support will alert you about the date the package transfer will occur.

After the Package Transfer Is Complete

Run `sf package list` and verify that the package is no longer associated with your Dev Hub.

If the transferred package is still visible in your CLI output, and the recipient of the package transfer indicates the package transfer
succeeded, log a case with Salesforce Customer Support to remove the association of the package with your Dev Hub org.

Next, unpublish your existing AppExchange listing for this package.

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


Second-Generation Managed Packages Transfer a Second-Generation Managed Package to a
Different Dev Hub

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

What Package History Is Transferred?

When a package is transferred, all package versions, and all lines of ancestry are transferred. Customer upgrade paths aren’t affected.

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

#### Take Ownership of a Second-Generation Managed Package Transferred from a Different Dev Hub

You can take ownership of a second-generation managed package that is transferred from another Dev Hug org.

#### Take Ownership of a Second-Generation Managed Package Transferred from a

Different Dev Hub

You can take ownership of a second-generation managed package that is transferred from another Dev Hug org.

To initiate a package transfer from your Dev Hub org, see Transfer a Second-Generation Managed Package to a Different Dev Hub.

Note: For security reasons, package transfers between a Dev Hub located in Government Cloud and a Dev Hub located outside
Government Cloud aren’t permitted.

Transfers from External Customers

If you’re receiving the package from another Salesforce Partner or ISV, make sure they provide the source code for the package, and an
outline for the config settings needed to properly set up your Salesforce DX environment.

Request all the configuration settings required to properly set up the `sfdx-project.json` file, and a complete list of features and
settings that must be specified in your scratch org definition file.


Second-Generation Managed Packages Transfer a Second-Generation Managed Package to a
Different Dev Hub

Also ensure that the company who is transferring the ownership of the package provides the login credentials for the namespace org
they used. This information is needed to link the package namespace to your Dev Hub org.

Receive a Package Transfer

For internal transfers, skip this step. Only log the case described in Transfer a Second-Generation Managed Package to a Different Dev
Hub .

If you’re receiving a package from a different Salesforce Partner or ISV, start by linking the namespace of the package you are receiving
[to your Dev Hub org. See Link a Namespace to a Dev Hub Org in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_reg_namespace.htm) _Salesforce DX Developer Guide_ .

Next, log a case with Salesforce Customer Support, and provide the:

**•** Dev Hub org ID for the source org.

**•** Subscriber package ID of the package you’re receiving. This ID begins with 033.

**•** Dev Hub org ID for the destination org.

After the Package Transfer Is Complete

After the package transfer is complete, you’ll be notified by Salesforce Customer Support.

To verify that the transferred package is associated with your Dev Hub, run `sf package list` .

Impact of Package Transfers on Package IDs

Update Your Package Project File

Open and review the contents of the `sfdx-project.json` file that you received from the original package owner.

Open and review the contents of any scratch org definition files that you received from the original package owner. Definition files help
in setting up your scratch orgs during development. Use the `-–definition-file` parameter to specify a definition file when you
create a new package version.

If the package directories section lists additional packages that weren’t transferred to you, remove those references from the
`sfdx-project.json` file.

Next, review the package alias section of the `sfdx-project.json` file, and remove any references to package aliases that aren’t
associated with the package that was transferred.

Update the package alias of the transferred package to specify its 0Ho package ID.


### Second-Generation Managed Packages Contact Salesforce Partner Support to Enable Specific

Packaging Features

Before You Create a New Package Version

Similar to how you go about creating any new package versions, you must update the `sfdx-project.json` file, and update the
version number and ancestor ID. We recommend you set the ancestor ID to HIGHEST.

To designate a Dev Hub user to receive email notifications for unhandled Apex exceptions, and install, upgrade, or uninstall failures
associated with your package, run the `sf package update` command, and use the `--error-notification-username`
parameter.

What Package History Is Transferred?

Regardless of whether the package transfer occurred between two Dev Hub orgs you own, or the package was transferred externally to
a Dev Hub you don’t own, we transfer the package version history.

We transfer:

**•** Package name, namespace, type, and IDs. One exception is that the transferred package gets a new 0Ho ID.

**•** Package version info. This includes all the info that is typically displayed when you run the `sf package version list` or
`sf package version report` command.

We don’t transfer:

**•** Push upgrade history.

**•** Package version create requests.

**•** The username of the Dev Hub user who received Apex and other types of error notifications.

**•** Deleted package versions.

Next Steps

You’ve verified that the package is associated with your Dev Hub, you’ve updated your `sfdx-project.json` file, and perhaps
you’ve even created a new package version. Congrats! There’s still a couple more items of business left to complete.

**1.** Register the transferred package with your License Management Org.

If this is an external transfer, log a case with Salesforce Customer Support and request provide both your LMO org ID, and the 033
package ID.

**2.** [Publish Your Package on AppExchange](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_publish_appexchange.htm)

### Contact Salesforce Partner Support to Enable Specific Packaging Features

Certain packaging features can only be enabled by Salesforce Partner Support.

To log a case for Salesforce Partner Support, follow these steps.

**1.** [Log in to the Salesforce Partner Community.](https://partners.salesforce.com/)

**2.** Click the question icon and then click **Log a Case for Help** .

**3.** Complete the Subject and Description fields

**a.** After you enter a Description, a section called **Pick a different product & topic** will display.

**4.** For topic, select **AppExchange & Managed Packages** .

For Feature Management App enablement, select **ISV Technology Request** .

**5.** Provide any other required details, and then click **Create Case** .


## Second-Generation Managed Packages Best Practices for Second-Generation Managed Packages Best Practices for Second-Generation Managed Packages

We suggest that you follow these best practices when working with second-generation managed packages.

**•** We recommend that you work with only one Dev Hub, and enable Dev Hub in your partner business org.

**•** The Dev Hub org against which you run the `sf package create` command becomes the owner of the package. If the Dev
Hub org associated with a package expires or is deleted, its packages no longer work.

**•** Include the `--tag` option when you use the `sf package version create` and `sf package version update`
commands. This option helps you keep your version control system tags in sync with specific package versions.

**•** Create user-friendly aliases for packaging IDs, and include those aliases in your Salesforce DX project file and when running CLI
packaging commands. See: Package IDs and Aliases for Second-Generation Managed Packages.

**•** When adding components to your package, check the product documentation for that component to ensure that the product is
generally available (GA). If you choose to package a non-GA component, it may have limitations and isn't guaranteed to GA. This
scenario is particularly risky if the component can't be removed from a managed package.

## Manage Licenses for Managed Packages

Use the License Management App (LMA) to manage leads and licenses for your AppExchange
solutions. By integrating the LMA into your sales and marketing processes, you can better engage
with prospects, retain existing customers, and grow your ISV business. The LMA is a managed
package that is installed in all partner business orgs (PBO) and includes custom objects that track
details on packages, package versions, and licenses.

Note: The LMA is available only in English.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, and
**Unlimited** Editions

The LMA is available to eligible Salesforce partners. For more information on the Partner Program, including eligibility requirements, visit
[https://partners.salesforce.com.](https://partners.salesforce.com)


### Second-Generation Managed Packages Get Started with the License Management App Get Started with the License Management App

To start managing leads and licenses with the License Management App (LMA), complete these installation and configuration steps.

Lead and License Records in the License Management App
Each time a customer installs your managed package, the License Management App (LMA) creates lead and license records.

Modify a License Record
You can change a customer’s access to your offering by modifying a license record using the License Management App (LMA). For
example, you can increase or decrease the number of seats included with a license or change the expiration date.

Refresh Licenses for a Managed Package
To sync all license records for a package across all subscriber installations, you refresh the license. Refreshing the license can also
resolve discrepancies between the number of licenses in a subscriber’s org and the number displayed in the License Management
App (LMA). Refreshing is required when you move the LMA to a different org.

Extending the License Management App
The License Management App (LMA) is a managed package that you can customize and extend. In addition to using the LMA to
manage leads and licenses, many partners also integrate it into their existing business processes.

Move the License Management App to Another Salesforce Org
You can move an LMA to a different org, but your package and license records don’t automatically move with it. You must manually
relink your packages and refresh the licenses.

Troubleshoot the License Management App
If you’re experiencing issues with the License Management App, review these troubleshooting tips.

Best Practices for the License Management App
Follow these best practices when you use the License Management App (LMA).

Troubleshoot Subscriber Issues
Use the Subscriber Support Console to access information about your subscribers. Subscribers can also grant you login access to
troubleshoot issues directly within your app. After you’re granted access, you can log in to the subscriber’s org and view their
configuration and data to troubleshoot and resolve issues.

### Get Started with the License Management App

To start managing leads and licenses with the License Management App (LMA), complete these
installation and configuration steps.

Install the License Management App
The License Management App (LMA) is a managed package that is installed in all partner
business orgs. The org that the LMA is installed in is called the License Management Org (LMO).

Associate a Package with the License Management App
To receive lead and license records for your package, you connect your License Management
Org (LMO), your package, and the Salesforce Partner Console. Your LMO is the Salesforce org
where the License Management App (LMA) is installed.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, and
**Unlimited** Editions

Configure Permissions for the License Management App
Determine who needs access to the License Management App (LMA), and set object permissions. Consider using a permission set
to assign user permissions.


Second-Generation Managed Packages Get Started with the License Management App

#### Install the License Management App

The License Management App (LMA) is a managed package that is installed in all partner business
orgs. The org that the LMA is installed in is called the License Management Org (LMO).

We strongly recommend that you use your partner business org (PBO) as your LMO. However, you
can choose to install the LMA in another production org. Consider installing the LMA in an org that
your company is already using to manage sales, billing, and marketing.

USER PERMISSIONS

To install packages:

**•** Download AppExchange
Packages

Commercial use of the LMA is prohibited in Developer and Partner Developer Edition orgs. Installing
the LMA in a Developer Edition org is allowed only if you’re building integrations with the LMA and need an environment only for
development and testing purposes. You can install the LMA in Enterprise, Unlimited, or Performance Edition production orgs.

It’s not possible to have Slack or the Declarative Lookup Rollup Summary (DLRS) package installed in the same org as the LMA. If the org
in which you plan to install the LMA has either Slack or the DLRS package installed, uninstall them before you install the LMA. Alternatively,
install the LMA in a different org.

Note: To confirm whether your PBO already has the LMA installed, skip to step 4.

**1.** [To install the LMA in an org other than your PBO, log a case in the Partner Community. After we review the case, you receive an](https://partners.salesforce.com)
email with an installation URL.

**2.** Log in to the org where you want to install the LMA, and then go to the installation URL included in the email.

#### 3. Choose which users can access the LMA, and then click Install .

**4.** To confirm that the LMA is installed, open the App Launcher. If the installation was successful, the License Management App appears
in the list of available apps.

#### Associate a Package with the License Management App

To receive lead and license records for your package, you connect your License Management Org
(LMO), your package, and the Salesforce Partner Console. Your LMO is the Salesforce org where the
License Management App (LMA) is installed.

A single LMO can manage multiple 1GP and 2GP packages, but a package can be associated with
only one LMO.

**1.** Connect your packaging org (for 1GP) or your Dev Hub org (for 2GP) to the Partner Console.

**a.** [Log in to the Partner Community, and select the](https://partners.salesforce.com/) **Publishing** tab.

**b.** Click **Technologies**   - **Orgs** .

**c.** Click **Connect Technology**, and then click **Org** .

**d.** Click **Connect Org** .

USER PERMISSIONS

To manage licenses in the
Partner Community:

**•** Manage Listings

**e.** Log in to the org. Provide a username and a password with a security token appended. For example, if the password is ABC and
the token is 123, enter ABC123. Don’t remember your token? [Reset your security token.](https://help.salesforce.com/articleView?id=user_security_token.htm&type=5&language=en_US)

For 1GP packages, enter the login credentials for the packaging org. Repeat this step for all your 1GP packages.

For 2GP packages, enter the login credentials for the Dev Hub org. When you connect the Dev Hub org, all the 2GP packages
owned by the Dev Hub org are linked to the Partner Console.

**2.** Select the **Solutions** tab.

**3.** Locate the package you want to register with the LMO. To register each package you own, repeat this step.

**a.** Click the down arrow to expand the list of versions for your package.


Second-Generation Managed Packages Get Started with the License Management App

**b.** Click **Register Package** for the package version you want to register.

Package versions created after linking to your LMO inherit the association.

**c.** To register the package, log in to your LMO.

**4.** Set the default behavior you want for your package license, and then click **Save** .

After the package is registered, a license is created when customers install it. You can view which packages are registered in the LMA.

Note: Beta package versions don’t display in the LMA. Only managed-released package versions (1GP) and promoted package
versions (2GP) are visible in the LMA. Unlocked packages aren’t supported.

SEE ALSO:

_Salesforce Help:_ [Reset Your Security Token](https://help.salesforce.com/articleView?id=user_security_token.htm&type=5&language=en_US)

#### Configure Permissions for the License Management App

Determine who needs access to the License Management App (LMA), and set object permissions. Consider using a permission set to
assign user permissions.

Ensure that you:

**•** Install the LMA.

**•** Connect your packaging org (for 1GP) or your Dev Hub org (for 2GP) to the AppExchange Partner Console.

**•** Associate your package with the LMA.

**1.** Set object permissions for the license, package, and package version custom objects.

**2.** Set field-level security in user profiles or permission sets.


Second-Generation Managed Packages Get Started with the License Management App

**3.** Add related lists to page layouts.

##### Assign Permissions to the Subscriber Support Console

Create a permission set to provide users access to the Subscriber Support Console.

##### Assign Permissions to the Subscriber Support Console

Create a permission set to provide users access to the Subscriber Support Console.

Note: If you’ve already assigned these permissions via a profile or another permission set, you can skip this task.

**1.** From Setup, in the Quick Find box, enter _`Permission Sets`_, and select **Permission Sets** .

**2.** Click **New** and enter your permission set information.

**3.** On the Permission Set Overview page, locate the Apps section, and select **Visualforce Page Access** .

**a.** Click **Edit** .

**b.** Add **sfLma.LoginToPartnerBT** and **sfLma.SubscriberSupport** to the list of Enabled Visualforce pages, and then click **Save** .

**4.** On the Permission Set Overview page, locate the System section, and select **System Permissions** . Click **Edit** .

**a.** Select **Log in to Subscriber Organization**, and click **Save** .

**5.** From Setup, in the Quick Find box, enter _`Profiles`_, and select **Profiles** .

**a.** Click **Edit** .

**b.** Under Custom App Settings, select **License Management App** .

**c.** Under Custom Tab Settings, locate the Subscribers tab and select **Default On** .

**d.** Click **Save** .


### Second-Generation Managed Packages Lead and License Records in the License Management App Lead and License Records in the License Management App

Each time a customer installs your managed package, the License Management App (LMA) creates lead and license records.

The key objects in the LMA are Package, Lead, and License.

**•** Package—The LMA includes a Package custom object and a Package Version custom object. These objects display details about
each 1GP or 2GP package and package version you’ve listed on AppExchange.

**•** Lead —The Lead standard object gives you details about who installed your package, such as the installer’s name, company, and
email address. Lead records created by the LMA are just like the ones you use elsewhere in Salesforce, except the lead source is
Package Installation. You can manually convert leads into accounts and contacts. When you convert a lead, the license record links
to the converted account or contact.

**•** License—The License custom object gives you control over how many users in the customer’s org can access your package and for
how long. Each license record links to a lead record and a package record.

To understand which actions you must take and which actions the LMA handles for you, review this table.

[Note: Lead assignment rules aren't triggered for leads created by the LMA.](https://help.salesforce.com/s/articleView?id=service.customize_leadrules.htm&language=en_US)

### Modify a License Record

You can change a customer’s access to your offering by modifying a license record using the License Management App (LMA). For
example, you can increase or decrease the number of seats included with a license or change the expiration date.

Warning: You can't use the LMA to modify licenses provisioned through AppExchange Checkout. To modify licenses provisioned
[through Checkout, have your customers follow the instructions in Add or Remove Licenses from an AppExchange Checkout](https://developer.salesforce.com/docs/atlas.en-us.260.0.packagingGuide.meta/packagingGuide/appexchange_checkout_update_seats.htm)
[Subscription.](https://developer.salesforce.com/docs/atlas.en-us.260.0.packagingGuide.meta/packagingGuide/appexchange_checkout_update_seats.htm)

**1.** In the LMA, locate the license.

**2.** Click **Modify License** .

When the LMA is installed, the Edit button doesn’t appear on the license page layout, and the Modify License button is included
instead. This setup is intentional. You must edit license records on the Modified License page, don't attempt to edit license records
directly.

**3.** Update the field values as needed.


### Second-Generation Managed Packages Refresh Licenses for a Managed Package

**4.** Click **Save** .

### Refresh Licenses for a Managed Package

To sync all license records for a package across all subscriber installations, you refresh the license. Refreshing the license can also resolve
discrepancies between the number of licenses in a subscriber’s org and the number displayed in the License Management App (LMA).
Refreshing is required when you move the LMA to a different org.

Note: For each package, you can refresh licenses only one time per week.

**1.** From the LMA, select the **Packages** tab.

**2.** Open the package record.

### 3. Click Refresh Licenses . In Lightning Experience, Refresh Licenses is located in the dropdown menu. Extending the License Management App

The License Management App (LMA) is a managed package that you can customize and extend. In addition to using the LMA to manage
leads and licenses, many partners also integrate it into their existing business processes.

The LMA includes these custom objects:

**•** [License](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/lma_license_details.htm)

**•** Package on page 411

**•** Package Version on page 411

You can add custom fields to the objects as long as you don’t mark your custom fields as required.

Package and Package Version Object Fields
The License Management App (LMA) includes a Package custom object and a Package Version custom object. These objects display
details about each 1GP or 2GP package and package version you’ve listed on AppExchange.

License Object Fields
Use the License custom object to set limits on how many users in the subscriber’s org can use your app and for how long.


Second-Generation Managed Packages Extending the License Management App

Adding Custom Automation to License Management App Objects
Here are some examples of how you can use the License Management App (LMA) to grow your business and retain customers.

#### Package and Package Version Object Fields

The License Management App (LMA) includes a Package custom object and a Package Version custom object. These objects display
details about each 1GP or 2GP package and package version you’ve listed on AppExchange.

To view details about a package record, from the LMA, select the **Packages** tab, and then select the package name. You can view package
versions in the Package Version related list.

Note: The LMA creates the package records, which contain critical information for tracking your licenses and packages. Treat
these fields as read-only and ensure that your object permissions protect package records.

**Package Custom Object Fields** **Description**

`Developer Name` The name of the org that owns the package. For 1GP, the org name is the packaging org.
For 2GP, it’s the Dev Hub org.

`Developer Org ID` The 18-character ID of the org that owns the package. For 1GP, the org ID is the packaging
org ID. For 2GP, it’s the Dev Hub org ID.

`Last License Refresh` The date when the License Refresh tool was last run.

`Latest Version` The most recent package version you’ve released.

`Lead Manager` The owner of the lead records that the LMA creates when a customer installs your package.

`Next Available Refresh` The date when the License Refresh tool can be run again.

`Owner` The LMA owns all package records.

`Package ID` The 18-character ID that identifies the package. This ID starts with 033.

`Package Name` The name you specified when you created the package.

**Package Version Object Fields** **Description**

#### Package The package name and links to the package record’s detail page.

`Package Version Name` The name you specified when you created the package version.

`Release Date` The date you created this package version.

`Version Number` The version number in major.minor.patch format. For example, 3.1.0.

`Version ID` The 18-character ID of this package version.

#### License Object Fields

Use the License custom object to set limits on how many users in the subscriber’s org can use your app and for how long.

The License Management App (LMA) creates a license record every time your package is installed in an org. For example, if a subscriber
installs two of your 1GP packages and three of your 2GP packages, you have five license records for that subscriber in your LMA. If you


Second-Generation Managed Packages Extending the License Management App

deliver a 2GP app that is composed of multiple packages, a unique license record is created for each package in the app. You can allocate
up to 99,000,000 seats per subscriber license.

To view details about a license record, select the **Licenses** tab in the LMA, and then select and open the license record.

License records are automatically created and contain critical information for tracking licenses. Do not directly edit the license record.
[Instead, use the Modify License tool to change the expiration date, license status, and the number of licensed seats.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/lma_edit_license.htm)

**License Custom Object Fields** **Description**

`Account` A lookup field to the account record for a converted lead.

`Contact` A lookup field to the contact record for a converted lead.

`Created By` License records are always created by the LMA.

`Expiration Date` Displays the expiration date or `Does not expire` (default).

`Install Date` The date the subscriber installed this package version.

`Instance` The Salesforce instance where the subscriber’s org resides.

```
Lead

```

The lead record that the LMA created when the package was installed. A lead represents
the user who owns the license.

If you convert the lead into an opportunity, the lead name is retained but the lead record
no longer exists.

`License Name` An auto-generated number that represents an instance of a license. License names are in
the format of L-00001, and each new license is incremented by one.

```
Licensed Seats

```

Displays the number of licenses or `Site License` (default). When a package is installed
in a sandbox org, `Site License` is the default. If a free trial package is installed in a
sandbox org, the `Site License` is applied.

`License Status` The type of license: Active, Suspended, Trial, or Uninstalled.

`License Type` This is a legacy field and can be ignored.

`Org Edition` The edition of the subscriber’s org.

`Org Expiration Date` Applies only if the subscriber installs your package in a trial org. Indicates the date when
the trial org expires. It isn’t related to the package license expiration.

`Org Status` The status of the subscriber’s org: Active, Free, or Trial.

`Owner` The LMA owns all license records. Don’t edit this field.

`Package Version` A lookup field that links to the package version associated with this license.

`Package Version Number` The version number in major.minor.patch format. For example, 3.1.0.

`Sandbox` Indicates whether the license is for a package installed in a sandbox org.

`Subscriber Org ID` The 15-character ID representing the subscriber’s org.

```
Used Licenses

```

Displays the number of users who have a license to the package.

This field is blank if:

**•** A customer uninstalled the package.


### Second-Generation Managed Packages Move the License Management App to Another Salesforce

Org

**License Custom Object Fields** **Description**

**•** `Licensed Seats` is set to Site License.

#### Adding Custom Automation to License Management App Objects

Here are some examples of how you can use the License Management App (LMA) to grow your
business and retain customers.

Alert Sales Reps Before a License Expires

If you’re managing licenses for several packages, it can be difficult to track the various expirations.
If a license expires accidentally, you could even lose a customer. To help your customers with
renewals, set up an Apex trigger or create a flow to email a sales rep on your team before the license
expires.

Notify Customer-Retention Specialists When an Offering Is Uninstalled

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, and
**Unlimited** Editions

If a customer uninstalls your offering, find out why. By speaking to the customer, you have an opportunity to restore the business
relationship or receive feedback that helps you improve your offering.

To notify a customer-retention specialist on your team, follow these high-level steps.

**1.** Create an email template for the notification.

**2.** Create a workflow rule with a filter that specifies that the `License Status` equals _`Uninstalled`_ .

**3.** Associate the workflow rule with a workflow alert that sends an email to the retention specialist.

### Move the License Management App to Another Salesforce Org

You can move an LMA to a different org, but your package and license records don’t automatically
move with it. You must manually relink your packages and refresh the licenses.

It’s not possible to have Slack or the Declarative Lookup Rollup Summary (DLRS) package installed
in the same org as the LMA. If the org in which you plan to install the LMA has either Slack or the
DLRS package installed, uninstall them before you install the LMA. Alternatively, install the LMA in
a different org.

**1.** To remove the association between the LMA and the org where it’s currently installed, log a
case with Salesforce Partner Support on page 403.

**2.** Install the LMA in the new org on page 406.

**3.** Associate your packages with the new org on page 406.

**4.** Refresh licenses for your packages on page 410.


USER PERMISSIONS

To install packages:

**•** Download AppExchange
Packages

To manage licenses in the
Partner Community:

**•** Manage Listings

### Second-Generation Managed Packages Troubleshoot the License Management App Troubleshoot the License Management App

If you’re experiencing issues with the License Management App, review these troubleshooting tips.

#### Leads and Licenses Aren’t Being Created in the License Management App

When a customer installs your package, leads and license records are created. If these records
aren’t being created, review these configurations in the License Management Org (LMO). If you
resolve your issue using one of these recommendations, your missing licenses appear in the
LMA within a few days.

Proxy User Has Deactivated Message in the LMA
If you’re editing a license and see a “proxy user has deactivated” message, it's possible that the
subscriber org is locked, deleted, or disabled.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, and
**Unlimited** Editions

#### Leads and Licenses Aren’t Being Created in the License Management App

When a customer installs your package, leads and license records are created. If these records aren’t being created, review these
configurations in the License Management Org (LMO). If you resolve your issue using one of these recommendations, your missing
licenses appear in the LMA within a few days.

**Did the customer complete the package installation?**
When a customer clicks **Get it Now** on your AppExchange listing, Salesforce counts this selection as an installation. However, the
customer can cancel the installation before it’s completed, or the installation could have failed. If the installation doesn’t finish, a
license isn’t created.

**Is State and Country picklist validation enabled?**
To avoid state and country picklist-related lead failures, you have two options. Use the standard picklist integration values, or add
duplicate states and countries to your picklists.

**Standard picklist integration values**

To implement this option, use the Salesforce standard state and country picklists in your org, and leave the integration values as-is.
We recommend this option for most partners.

With this option, AppExchange leads propagate to your org with full state and country names, and the names match integration
values in the standard picklists.

**Add duplicate states and countries to your picklists.**

Implement this option if you have a requirement to use the two-letter state or country abbreviations in your org. For example, you
display abbreviations in the user interface or use them to integrate with other systems. Add duplicate states and countries to your
picklists with different integration values. Set one value to the two-letter state or country abbreviation. Set the other value to the
full state or country name. Make only the two-letter abbreviation picklist entries visible.

With this option, AppExchange leads propagate to your org with full state and country names, which match the full name integration
values in your org. You also have two-letter integration values to use as needed.

**Does the lead or license object have a trigger?**
Don’t use `before_create` or `before_update` triggers on leads and licenses. Instead, use `after_` triggers, or remove
all triggers. If a trigger fails, it can block license creation.

**Does the lead or license record have a required custom field?**
If yes, remove the requirement. The LMA doesn’t populate a required custom field, so it can prevent licenses or leads from being
created.


### Second-Generation Managed Packages Best Practices for the License Management App

**Is the lead manager a valid, active user?**
If not, the LMA can’t create leads and licenses.

**Does the lead or license record have a validation rule?**
Validation rules often block the creation of LMA lead or license records because the required field isn’t there.

**Does the lead or license have a workflow rule?**
Workflow rules sometimes prevent leads and licenses from being created. Remove the workflow rule.

**Was the lead converted to an account?**
When leads are converted to accounts, they’re no longer leads.

**Are you using standard duplicate rules for leads?**
When a customer installs your package, the LMA checks for existing leads and contacts. If an existing contact matches the customer
[who installed your package, a lead record isn’t created. To complete these checks, the LMA applies standard lead duplicate rules](https://help.salesforce.com/articleView?id=duplicate_rules_standard_lead_rule.htm&language=en_US)
[and matching rules. If you prefer to have the LMA associate every license with a lead regardless of whether there’s an existing contact](https://help.salesforce.com/articleView?id=matching_rules_standard_contact_rule.htm&language=en_US)
[match, customize the standard duplicate rule for leads and remove the matching rule for contacts.](https://help.salesforce.com/articleView?id=duplicate_prevention_map_of_tasks.htm&language=en_US)

#### Proxy User Has Deactivated Message in the LMA

If you’re editing a license and see a “proxy user has deactivated” message, it's possible that the subscriber org is locked, deleted, or
disabled.

If you attempt to contact the subscriber and they aren't responsive, consider deleting the license record.

### Best Practices for the License Management App

Follow these best practices when you use the License Management App (LMA).

**•** To take advantage of entitlements that are unique to AppExchange partners, use your partner business org as your License
Management Org.

**•** Create a list view filter for leads created by installed packages. The filter helps your team separate subscriber-based leads from leads
coming from other sources.

**•** Use the API to find licensed users. The `isCurrentUserLicensed` method determines if a user has a license to a managed
[package. For more information, see the Apex Reference Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_methods_system_userinfo.htm)

**•** Treat the LMA custom objects as read-only. Use the Modify License page to edit licenses. Don’t attempt to directly or programmatically
edit license records.

**•** The LMA automatically creates package, package version, and license records. Customizations, such as adding required custom fields
or creating workflow rules, triggers, or validation rules that require custom fields, can prevent the LMA from working properly.

### Troubleshoot Subscriber Issues

Use the Subscriber Support Console to access information about your subscribers. Subscribers can also grant you login access to
troubleshoot issues directly within your app. After you’re granted access, you can log in to the subscriber’s org and view their configuration
and data to troubleshoot and resolve issues.

To access the Subscriber Overview page, click the organization’s name from the **Subscribers** tab in the LMA.

Note: This feature is available to eligible Salesforce partners. For more information on the Partner Program, including eligibility
[requirements, see www.salesforce.com/partners.](https://partners.salesforce.com)


Second-Generation Managed Packages Troubleshoot Subscriber Issues

#### Request Login Access from Subscribers

To log in to a subscriber org, first request login access from the subscriber.

#### Log In to Subscriber Orgs

After your subscriber has granted you login access, you can log in to the subscriber org to troubleshoot the issue.

Debug Subscriber Orgs
After logging in to a subscriber’s org, you can view logs, obfuscated code in your package, and initiate ISV Customer Debugger
sessions.

#### Request Login Access from Subscribers

To log in to a subscriber org, first request login access from the subscriber.

Ask the subscriber to enable either **Grant Account Login Access** or **Grant Login Access** . If they don’t see your company listed, one
of the following applies.

**•** A system admin disabled the ability for non-admins to grant access.

**•** The user doesn’t have a license for the package.

**•** The package is licensed to the entire org. In this scenario, only an admin with the Manage Users permission can grant access.

**•** The org setting **Administrators Can Log in as Any User** is enabled.

Note: When the org setting **Administrators Can Log in as Any User** is disabled, login access is granted for a limited amount
of time, and the subscriber can revoke access at any time.

Any changes you make while logged in as a subscriber are logged in the subscriber org’s audit trail.

#### Log In to Subscriber Orgs

After your subscriber has granted you login access, you can log in to the subscriber org to
troubleshoot the issue.

Available in: **Enterprise**, **Performance**, and **Unlimited** Editions

USER PERMISSIONS

To log in to subscriber orgs:

**•** Log in to Subscriber Org

Note: You can only log in to orgs with a Salesforce Platform or full Salesforce license. You can’t log in to subscriber orgs on
Government Cloud instances. It's also not possible to log into a scratch org using the log in to subscriber org feature.

Multi-Factor Authentication Required to Log In to a Subscriber Org

Starting in Spring ’22, multi-factor authentication (MFA) is required when logging into the License Management Org (LMO). MFA is
required only for LMO users who require access to the Subscriber Support Console. This requirement provides subscribers an extra layer
of security by verifying the identity of the user accessing their org. You also have more control over which users log in to a subscriber
org.

[Determine which users require access to the Subscriber Support Console, and then set up multi-factor authentication (MFA) for those](https://help.salesforce.com/s/articleView?id=xcloud.mfa_direct_login_user_perm.htm&type=5&language=en_US)
users.

Log In to a Subscriber Org

After you’ve logged in to the LMO using multi-factor authentication (MFA), and your subscriber has granted you login access, you’re
ready to log in.


Second-Generation Managed Packages Troubleshoot Subscriber Issues

**1.** In the License Management App (LMA), click the **Subscribers** tab.

**2.** To find a subscriber org, enter a subscriber name or org ID in the search box, and click **Search** .

**3.** Click the name of the subscriber org.

**4.** On the Org Details page, click **Login** next to a user’s name. You have the same permissions as the user you logged in as.

**5.** When you’re finished troubleshooting, log out of the subscriber org.

Note: Some subscribers require MFA in addition to the MFA required for the LMO. Ask your subscriber if their org requires MFA
to log in. If so, your login attempt sends an MFA notification to your subscriber, and your login is blocked until your subscriber
responds to the notification. To ensure that your subscriber is available to respond to the MFA notification, consider coordinating
a specific login time.

Best Practices for Logging In

**•** Create an audit trial that indicates when and why a subscriber org login has occurred. You can create an audit trail by logging a case
in your LMO before each subscriber org login.

**•** When you access a subscriber org, you’re logged out of your LMO. To prevent your session from being automatically logged out of
your LMO when you log in to a subscriber org, use the org’s My Domain login URL.

**•** Allow only trusted support and engineering personnel to log in to a subscriber’s org. Because this feature can include full read/write
access to customer data and configurations, it’s vital to your reputation to preserve their security.

**•** Control who has login access by giving the Log in to Subscriber Org user permission to specific support personnel via a profile or
permission set. See Assign Permissions to the Subscriber Org Console on page 408.

#### Debug Subscriber Orgs

After logging in to a subscriber’s org, you can view logs, obfuscated code in your package, and initiate ISV Customer Debugger sessions.

Get Access to Debug Logs

You can debug your code by generating Apex debug logs that contain the output from your managed package. Using this log information,
you can troubleshoot issues that are specific to that subscriber.

[To get access to a subscriber’s Apex debug logs, you can either request login access from the subscriber, or use the License Management](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/lma_requesting_login_access.htm)
App (LMA) to enable debug logs for a namespace.

Important: Note these important considerations for enabling subscriber debug logs for a namespace.

**•** When you enable debug logs for a namespace, the Apex code for the managed package becomes visible to the subscriber
org.

**•** Because multiple packages can share a namespace in second-generation managed packaging (2GP), enabling debug logs for
2GP means enabling logs for all managed packages in the namespace. For example, a subscriber is reporting issues with
Package A and you enable debug logs for the namespace that includes Package A. The subscriber also uses Package B and
Package C that are in the same namespace. By enabling debug logs for the namespace that includes Package A, you also
enable debug logs for Package B and Package C.

Follow these steps to enable debug logs for a namespace through the LMA.

**1.** In the LMA, click the **Subscribers** tab.

**2.** Search for the subscriber’s name or org ID, then click the name of the subscriber org.

**3.** In the Packages & Licensing section, find the package that you want to troubleshoot.


## Second-Generation Managed Packages Manage Features in Second-Generation Managed Packages

**4.** In the Subscriber Debug Logs column, click **Enable** .

**5.** Review the confirmation message, then click **OK** .

After you enable debug logs, your Apex code remains visible to the subscriber org until you disable debug logs. To disable debug logs,
follow the same steps in the LMA.

Troubleshoot with Debug Logs

After you get access to a subscriber’s debug logs or you enable debug logs for a namespace, get debug logs from the Developer Console.

**1.** From Setup of the subscriber’s org, in the Quick Find box, enter _`Debug Logs`_, and then select **Debug Logs** .

**2.** Launch the Developer Console.

**3.** Perform the operation, and view the debug log with your output.

Subscribers are unable to see the logs you set up or generate because they contain your unobfuscated Apex code.

You can also view and edit data contained in protected custom settings from your managed packages when logged in as a user.

Troubleshoot with the ISV Debugger

Each License Management Org can use one free ISV Customer Debugger session at a time. The ISV Customer Debugger is part of the
[Salesforce Extensions for Visual Studio Code. You can use the ISV Customer Debugger only in sandbox orgs, so you can initiate debugging](https://developer.salesforce.com/tools/vscode)
sessions only from a customer’s sandbox.

[For details, see the ISV Customer Debugger documentation.](https://developer.salesforce.com/tools/vscode/en/apex/isv-debugger)

## Manage Features in Second-Generation Managed Packages

Take the License Management App (LMA) a step further by extending it with the Feature Management App (FMA).

Here at Salesforce, we sometimes run pilot programs, like the one we ran when we introduced Feature Management. Sometimes we
dark-launch features to see how they work in production before sharing them with you. Sometimes we make features available to select
orgs for limited-time trials. And sometimes we want to track activation metrics for those features.

With feature parameters, we’re extending this functionality to you. Install the FMA in your License Management Org (LMO). The FMA
extends the License Management App, and like the LMA, it’s a managed package.

Feature Parameter Metadata Types and Custom Objects
Feature parameters are represented as Metadata API types in your package metadata, as records of custom objects in your LMO,
and as hidden records in your subscriber’s org.

Set Up Feature Parameters
Set up the Feature Management App in your License Management Org, define feature parameters, and add them to your package.

Use LMO-to-Subscriber Feature Parameters to Enable and Disable Features
Feature parameters with a data flow direction value of `LMO to Subscriber` are writable at your end and read-only in your
subscriber’s org. These feature parameters serve as permissions or limits. Use LMO-to-subscriber feature parameters to enable or
disable new features or to control how many of a given resource your subscriber can use. Or, enable features for a limited trial period.
Assign values to LMO-to-subscriber feature parameters by updating junction object records in your LMO, and then check those
values in your code.


### Second-Generation Managed Packages Feature Parameter Metadata Types and Custom Objects

Track Preferences and Activation Metrics with Subscriber-to-LMO Feature Parameters
Use subscriber-to-LMO feature parameters to track feature activation in your subscriber’s org. Parameter values are assigned on the
subscriber’s end and then sent to your LMO. To collect the values, update the feature parameters in your subscriber’s org using Apex
code. Check with your legal team before obtaining activation metrics from your customers. Use activation metrics to collect only
aggregated data regarding feature activation.

Hide Custom Objects and Custom Permissions in Your Subscribers’ Orgs
Occasionally, you want to include custom permissions or custom objects in a package but not show them to your subscribers. For
example, if you're piloting a feature for a few select orgs, and want to hide custom permissions and custom objects related to the
pilot feature.

Best Practices for Feature Management
Here are some best practices when working with feature parameters.

Considerations for Feature Management
Keep these considerations in mind when working with feature parameters.

### Feature Parameter Metadata Types and Custom Objects

Feature parameters are represented as Metadata API types in your package metadata, as records of custom objects in your LMO, and as
hidden records in your subscriber’s org.

Feature Parameter Fields

Feature parameters are represented as Metadata API types and store boolean, integer, or date values.

The first time a subscriber installs your package, a `FeatureParameter__c` record is created in your LMO for each feature parameter.
The feature parameter records include these fields:

**•** `FullName__c`

**•** `DataType__c` ( `Boolean`, `Integer`, or `Date` )

**•** `DataFlowDirection__c`

**•** `Package__c`

**•** `IntroducedInPackageVersion__c`

**•** `Namespace_Prefix__c`

Note: After a feature parameter is included and released in the package version, the data flow direction can’t be changed.

Lifecycle of a Feature Parameter

**Set Up the Feature Parameter**
Start by defining your feature parameter in an XML file. Create one XML file for each feature parameter.

Depending on how you’re using the feature parameter, you’ll also write code that enables you to check access rights or collect usage
information after the parameter is set up.

**Subscriber Installs Your Managed Package**
When a subscriber installs or upgrades your package in their org, a `FeatureParameter__c` record for each feature parameter
is created in the LMO. If these records were created during a previous installation or upgrade, this step is skipped.


### Second-Generation Managed Packages Set Up Feature Parameters

During package installation, junction object records are created in both the subscriber org and your LMO. A junction object is a
custom object with two master-detail relationships. In this case, the relationships are between `FeatureParameter__c` and
`License__c` in the LMO. These records store the value of their associated feature parameter for the subscriber org.

**Utilize Your Feature Parameters**
Use the junction objects to override the feature parameters’ default values or to collect data. Depending on the value of each feature
parameter’s `DataFlowDirection__c` field, data flows to the subscriber org (from the LMO) or to the LMO (from the subscriber
org). That data is stored in the junction object records.

### Set Up Feature Parameters

Set up the Feature Management App in your License Management Org, define feature parameters, and add them to your package.

#### Install and Set Up the Feature Management App in Your License Management Org

Install the FMA in your LMO. Then add the Feature Parameters tab to your default view, and adjust your page layout for licenses to
display related lists for your feature parameters.

Create Feature Parameters for Your Second-Generation Managed Package
To create a feature parameter for a 2GP managed package, create an individual XML file. Here are details on the file naming convention,
folder structure, and the attributes you use when creating feature parameters.

#### Install and Set Up the Feature Management App in Your License Management Org

Install the FMA in your LMO. Then add the Feature Parameters tab to your default view, and adjust your page layout for licenses to display
related lists for your feature parameters.

**1.** [To request access to the FMA, log a support case in the Salesforce Partner Community. For product, specify](https://partners.salesforce.com) **Partner Programs &**
**Benefits** . For topic, specify **ISV Technology Request** . The FMA extends the License Management App, so be sure to install the
LMA before requesting access to the FMA.

**2.** To install the FMA, follow the instructions in your welcome email.

**3.** [Add the Feature Parameters tab to your default view. For details, see Customize My Tabs in Salesforce Help.](https://help.salesforce.com/articleView?id=user_userdisplay_tabs.htm&language=en_US)

**4.** Update your page layout for licenses.

**a.** Navigate to a license record’s detail page.

**b.** Click **Edit Layout** .

**c.** In the Related Lists section of the License Page Layout Editor, add these lists.

**•** Feature Parameter Booleans

**•** Feature Parameter Dates

**•** Feature Parameter Integers

**d.** For each related list, add these columns.

**•** Data Flow Direction

**•** Feature Parameter Name

**•** Full Name

**•** Master Label

**•** Value


Second-Generation Managed Packages Set Up Feature Parameters

#### Create Feature Parameters for Your Second-Generation Managed Package

To create a feature parameter for a 2GP managed package, create an individual XML file. Here are details on the file naming convention,
folder structure, and the attributes you use when creating feature parameters.

[Note: Feature parameters for managed 1GP packages are created in the packaging org’s UI, see Create Feature Parameters in](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/fma_create_feature_parameters.htm)
[Your Packaging Org in the](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/fma_create_feature_parameters.htm) _First-Generation Managed Packaging Developer Guide_ for details.

A package can include up to 200 feature parameters.

**Folder Structure**
Feature parameters are stored as files in your Salesforce DX project folder.

Under the root `force-app` folder, create a folder and name it featureParameters. Store your feature parameter files in the feature
parameters folder. Each feature parameter you create must have its own separate file.

Note: It’s not possible to create feature parameters using a scratch org’s user interface.

**File Naming Convention**
The naming format for feature parameter files is `<name>.featureParameter<type>-meta.xml` .

The name is the API name of the feature parameter.

The type is the feature parameter type. Feature parameters can be booleans, integers, or dates.

**Feature Parameter Attributes**
Feature parameters include these three fields.

Note: After a feature parameter is included and released in the package version, the data flow direction can’t be changed.


### Second-Generation Managed Packages Use LMO-to-Subscriber Feature Parameters to Enable and

Disable Features

**Examples of Feature Parameter file**

**AdvancedPricingEnabled.featureParameterBoolean-meta.xml**

```
     <FeatureParameterBoolean xmlns="http://soap.sforce.com/2006/04/metadata">

       <dataflowDirection>SubscriberToLmo</dataflowDirection>

       <masterLabel>Advanced Pricing Enabled</masterLabel>

       <value>true</value>

     </FeatureParameterBoolean>

```

**NumberofLedgers.featureParameterInteger-meta.xml**

```
     <?xml version="1.0" encoding="UTF-8"?>

     <FeatureParameterInteger xmlns="http://soap.sforce.com/2006/04/metadata">

       <dataflowDirection>SubscriberToLmo</dataflowDirection>

       <masterLabel>Number of Ledgers</masterLabel>

       <value>7</value>

     </FeatureParameterInteger>

```

**ProjectActivationDate.featureParameterDate-meta.xml**

```
     <?xml version="1.0" encoding="UTF-8"?>

     <FeatureParameterDate xmlns="http://soap.sforce.com/2006/04/metadata">

       <dataflowDirection>LmoToSubscriber</dataflowDirection>

       <masterLabel>Date of Activation of the Project</masterLabel>

       <value>2020-01-25</value>

     </FeatureParameterDate>

### Use LMO-to-Subscriber Feature Parameters to Enable and Disable Features

```

Feature parameters with a data flow direction value of `LMO to Subscriber` are writable at your end and read-only in your
subscriber’s org. These feature parameters serve as permissions or limits. Use LMO-to-subscriber feature parameters to enable or disable
new features or to control how many of a given resource your subscriber can use. Or, enable features for a limited trial period. Assign
values to LMO-to-subscriber feature parameters by updating junction object records in your LMO, and then check those values in your
code.

#### Assign Override Values in Your LMO

To override the default value of a feature parameter in a subscriber’s org, update the appropriate junction object record in your LMO.

Check LMO-to-Subscriber Values in Your Code
You can reference feature parameters in your code, just like you’d reference any other custom object.

#### Assign Override Values in Your LMO

To override the default value of a feature parameter in a subscriber’s org, update the appropriate junction object record in your LMO.

**1.** Open the license record for a subscriber’s installation of your package.

**2.** In the related list for Feature Parameter Booleans, Feature Parameter Integers, or Feature Parameter Dates, select the feature parameter
whose value you want to update.

**3.** Click **Edit** .

**4.** Set a value.

**5.** Click **Save** .


### Second-Generation Managed Packages Track Preferences and Activation Metrics with

Subscriber-to-LMO Feature Parameters

#### Check LMO-to-Subscriber Values in Your Code

You can reference feature parameters in your code, just like you’d reference any other custom object.

Use these Apex methods with LMO-to-subscriber feature parameters to check values in your subscriber’s org.

**•** `System.FeatureManagement.checkPackageBooleanValue('` _**`YourBooleanFeatureParameter`**_ `');`

**•** `System.FeatureManagement.checkPackageDateValue('` _**`YourDateFeatureParameter`**_ `');`

**•** `System.FeatureManagement.checkPackageIntegerValue('` _**`YourIntegerFeatureParameter`**_ `');`

### Track Preferences and Activation Metrics with Subscriber-to-LMO Feature

Parameters

Use subscriber-to-LMO feature parameters to track feature activation in your subscriber’s org. Parameter values are assigned on the
subscriber’s end and then sent to your LMO. To collect the values, update the feature parameters in your subscriber’s org using Apex
code. Check with your legal team before obtaining activation metrics from your customers. Use activation metrics to collect only
aggregated data regarding feature activation.

**•** `System.FeatureManagement.setPackageBooleanValue('` _**`YourBooleanFeatureParameter`**_ `',`

```
    booleanValue );

```

**•** `System.FeatureManagement.setPackageDateValue('` _**`YourDateFeatureParameter`**_ `',`

```
    datetimeValue );

```

**•** `System.FeatureManagement.setPackageIntegerValue('` _**`YourIntegerFeatureParameter`**_ `',`

```
    integerValue );

```

Warning: The `Value__c` field on subscriber-to-LMO feature parameters is editable in your LMO. But don’t change it. The
changes don’t propagate to your subscriber’s org, so your values will be out of sync.

[You can view the value of a subscriber-to-LMO feature parameter from the Subscriber Support Console.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/lma_subscriber_support_overview.htm)

### Hide Custom Objects and Custom Permissions in Your Subscribers’ Orgs

Occasionally, you want to include custom permissions or custom objects in a package but not show them to your subscribers. For
example, if you're piloting a feature for a few select orgs, and want to hide custom permissions and custom objects related to the pilot
feature.

Note: Check with your company’s legal team before releasing hidden functionality.

To hide custom objects when creating your package, set the value of their Visibility field to `Protected` . After you've set the visibility
[to Protected, you can later update it to Unprotected. To change the visibility of an object, use the CustomObject Metadata API and](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/customobject.htm)
update the `visibility` field.

To hide custom permissions when creating your package, from Setup, enter _`Custom Permissions`_ in the Quick Find box. Select
**Custom Permissions**    - _`Your Custom Permission`_    - **Edit** . Enable **Protected Component**, and then click **Save** . After your
package is installed, use the `System.FeatureManagement.changeProtection()` Apex method to hide and unhide
custom objects and permissions.

Warning: After you’ve released unprotected objects to subscribers, you can’t change the visibility to `Protected` .

To hide custom permissions in released packages:

**•** `System.FeatureManagement.changeProtection('` _**`YourCustomPermissionName`**_ `',`

```
    'CustomPermission', 'Protected');

```


### Second-Generation Managed Packages Best Practices for Feature Management

To unhide custom permissions and custom objects in released packages:

**•** `System.FeatureManagement.changeProtection('` _**`YourCustomPermissionName`**_ `',`

```
    'CustomPermission', 'Unprotected');

```

**•** `System.FeatureManagement.changeProtection('` _**`YourCustomObjectName__c`**_ `',` `'CustomObject',`

```
    'Unprotected');

```

SEE ALSO:

[Protected Components in Managed Packages](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg1_dev/packaging_protected_components.htm)

_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/customobject.htm)_ : customObject

_Apex Reference Guide_ [: Feature Management Methods, changeProtection](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_System_FeatureManagement.htm#apex_System_FeatureManagement_changeProtection)

### Best Practices for Feature Management

Here are some best practices when working with feature parameters.

**•** We recommend that you use this feature set in a test package and a test LMO before using it with your production package. Apply
changes to your production package only after fully understanding the product’s behavior.

**•** Create LMO-to-subscriber feature parameters to enable features from your LMO for individual subscriber orgs. Don’t use the Apex
code in your managed package to modify LMO-to-subscriber feature parameters’ values in subscriber orgs. You can’t send the
modified values back to your LMO, and your records will be out of sync.

Use LMO-to-subscriber feature parameters as read-only fields to manage app behavior. For example, use LMO-to-subscriber feature
parameters to track the maximum number of permitted e-signatures or to make enhanced reporting available.

**•** Create subscriber-to-LMO feature parameters to manage activation metrics. Set these feature parameters’ values in subscriber orgs
using the Apex code in your managed package. For example, use subscriber-to-LMO feature parameters to track the number of
e-signatures consumed or to check whether a customer has activated enhanced reporting.

### Considerations for Feature Management

Keep these considerations in mind when working with feature parameters.

**•** After a feature parameter is included in a promoted and released package version, we recommend that you only edit the value field
located in LMO-to-subscriber junction objects.

Modifying or deleting other fields or records related to feature parameters, including the data flow direction, may cause the FMA to
stop operating correctly.

**•** Don’t use the LMO to create or delete feature parameters.

**•** When you update LMO-to-subscriber values in your LMO, the values in your subscribers’ orgs are updated asynchronously. This
process can take several minutes.

**•** When you publish a push upgrade to your managed package, feature parameters in your LMO and your subscribers’ orgs are updated
asynchronously. Creating and updating the junction object records can take several minutes.

**•** When the Apex code in your package updates subscriber-to-LMO values in your subscriber’s org, the changes can take up to 24
hours to reach your LMO.


## Second-Generation Managed Packages Get Started with AppExchange App Analytics Get Started with AppExchange App Analytics

AppExchange App Analytics provides usage data about how subscribers interact with your AppExchange managed packages and
packaged components. You can use these details to identify attrition risks, inform feature development decisions, and improve user
experience.

Note: [AppExchange App Analytics is subject to certain usage restrictions as described in the AppExchange Program Policies.](https://www.salesforce.com/content/dam/web/en_us/www/documents/legal/Agreements/alliance-agreements-and-terms/salesforce-partner-program-policies.pdf)
[Usage data from Government Cloud and Government Cloud Plus orgs isn’t available in App Analytics.](https://www.salesforce.com/solutions/industries/government1/products/government-cloud/)

App Analytics is available for first- and second-generation (1GP and 2GP) managed packages that passed security review and are registered
to a License Management App. Usage data is provided as package usage logs, monthly package usage summaries, or subscriber snapshots.
All usage data is available as downloadable comma-separated value (.csv) files. To view the data in dashboard or visualization format,
[use CRM Analytics or a third-party analytics tool.](https://help.salesforce.com/articleView?id=bi_explorer.htm&language=en_US)

In a 24-hour period, you can download a maximum 20 GB of AppExchange App Analytics data.

App Analytics Use Cases
To achieve your business objectives, use App Analytics across your teams. Read this guide to understand common use cases and
how to map App Analytics data to sample product features.

Enable App Analytics on Your Second-Generation Managed Package
Activate AppExchange App Analytics on your second-generation (2GP) managed package to access AppExchange App Analytics
package usage logs and subscriber snapshots. Package usage summaries are available by default.

Download Package Usage Logs, Package Usage Summaries, and Subscriber Snapshots
To request package usage logs, monthly package usage summaries, and subscriber snapshots, use the AppAnalyticsQueryRequest
object. Usage logs, usage summaries, and subscriber snapshots are downloadable comma-separated value (.csv) files.

Considerations for Custom Interactions
Easily create and log custom interactions on your managed package using Apex. As subscribers interact with your package and your
Apex code is executed, the custom interactions that you defined are logged. Retrieve your custom interactions in your package's
AppExchange App Analytics usage logs and usage summaries.

AppExchange App Analytics Best Practices
To plan and maximize your AppExchange App Analytics query strategy, follow our best practices. First, use file compression to reduce
your data results file size. Second, schedule and automate your regular App Analytics queries. Third, plan, schedule, and automate
catch-up queries to supplement your regular query data.

Package Usage Summaries
Package usage summaries provide high-level metrics by calendar month. Discover how many users access your package and which
operations they perform.

Package Usage Logs
Analyze adoption and user behavior, then make informed feature development decisions based on data from package usage logs.
AppExchange App Analytics tracks UI, API-based, Lightning-based, and Apex operations, and it logs each CRUD operation on
components and custom objects in packages. Events from sandbox and trial orgs are tracked in package usage logs. Events from
scratch orgs aren’t tracked.

Subscriber Snapshots
Subscriber snapshots give you a point-in-time summary of subscriber activity. Use subscriber snapshots to see usage trends by org
and package.


### Second-Generation Managed Packages App Analytics Use Cases

Test Custom Integrations
To test your custom integrations in a nonproduction environment, use AppExchange App Analytics Simulation Mode. Submit an
App Analytics query request and receive sample usage data.

AppExchange App Analytics Developer Cookbook
Delve deeper into your AppExchange App Analytics managed package usage data by creating key performance indicators (KPIs).
First, complete some prerequisites and retrieve your App Analytics data. Next, prepare your CRM Analytics environment. Finally, to
build your KPIs, complete App Analytics recipes.

### App Analytics Use Cases

To achieve your business objectives, use App Analytics across your teams. Read this guide to
understand common use cases and how to map App Analytics data to sample product features.

### App Analytics Use Cases

While there are various use cases for App Analytics, these cases tend to be the most common.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions


Second-Generation Managed Packages App Analytics Use Cases


Second-Generation Managed Packages App Analytics Use Cases

There are other use cases where App Analytics isn’t a good fit. For example, we don’t recommend that you use App Analytics to audit
customer license usage based on the `user_id_token` in package usage logs. We provide usage data for users licensed to use your
package, for users who indirectly interact with it, and for automated processes.

Mapping App Analytics Data to Product Features

For the most common App Analytics use cases, analyze App Analytics usage data at a feature level. Feature-level analysis supports
conversations about those features that you have with subscribers and with your teams.

App Analytics data is organized around the concept of a `custom_entity`, which is the developer name of the components that are
included in your managed package. `custom_entity` information is included in package usage summaries, package usage logs,
and subscriber snapshots.

Example: Imagine that you want to understand how subscribers are using a new feature in your solution that enables them to
easily manage newsletter subscriptions from Salesforce. To build this feature, your developers add these components to your
managed package.

**•** A new custom object, `Newsletter_Subscription`

**•** A new Lightning Page, `SubscriptionPage`

**•** A new Lightning Component, `SubscriptionComponent`

**•** A new Apex Class, `SubscriptionHandler`

As subscribers interact with your components, interaction data flows through in App Analytics.

The volume of total App Analytics data from your feature’s data mixed with data for your entire solution across all subscribers can
be vast. To make it easier for you to analyze, employ one of these strategies.

**•** Select a single component that best represents usage for this feature, and look solely at the data where it appears under
`custom_entity` . In this example, the custom object `Newsletter_Subscription` is a good candidate because it
tracks CRUD events from all sources, not only from the other components.


### Second-Generation Managed Packages Enable App Analytics on Your Second-Generation Managed

Package

**•** Select a combination of components for a user journey that you care about. Using our example, select an interaction for
`SubscriptionPage`, followed by `SubscriptionComponent`, `SubscriptionHandler` and CRUD for
`Newsletter_Subscription` .

Package usage logs and subscriber snapshots are updated daily so that you can track subscriber usage more closely and more
frequently. Package usage summaries are updated monthly. To understand how we gather and make this data available to you,
[read How Does AppExchange App Analytics Data Flow?](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/app_analytics_data_flow.htm)

SEE ALSO:

How to Read App Analytics Package Usage Log Data

Customer Success Recipes

Troubleshoot Subscriber Issues

### Enable App Analytics on Your Second-Generation Managed Package

Activate AppExchange App Analytics on your second-generation (2GP) managed package to access
AppExchange App Analytics package usage logs and subscriber snapshots. Package usage summaries
are available by default.

To ensure that you’re running the latest version of Salesforce CLI and its plug-ins, run `sf update`
and `sf plugins update` .

**1.** Activate App Analytics on your managed 2GP package. `sf package update`

```
  --package "Your Package Alias" --enable-app-analytics

```

To deactivate App Analytics on your managed 2GP package, run this CLI command. `sf`

```
  package update --package "Your Package Alias"

  --no-enable-app-analytics

```

**2.** For any additional package that you want App Analytics data for, repeat step 1.

### Download Package Usage Logs, Package Usage

Summaries, and Subscriber Snapshots

To request package usage logs, monthly package usage summaries, and subscriber snapshots, use
the AppAnalyticsQueryRequest object. Usage logs, usage summaries, and subscriber snapshots are
downloadable comma-separated value (.csv) files.

EDITIONS

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions.

USER PERMISSIONS

To access packages and
package versions:

**•** Read on Packages,
Package Versions

To request and retrieve
AppExchange App Analytics
data:

**•** Create, Read, Edit,
Delete, View All, and
Modify All on the
AppAnalyticsQueryRequest
object

To enable App Analytics on your second-generation (2GP) managed packages, follow these
[instructions. To enable App Analytics on your first-generation (1GP) managed packages, follow these instructions.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/app_analytics_enable2gp.htm)

Then determine which team members need create, read, update, and delete (CRUD) access to the AppAnalyticsQueryRequest object,
[and consider creating a permission set for them. By default, admins have the permissions required to request package usage logs and](https://help.salesforce.com/articleView?id=perm_sets_create.htm&language=en_US)
usage summaries using the AppAnalyticsQueryRequest object.

In a 24-hour period, you can download up to 20 GB of AppExchange App Analytics data.

Package usage summary data is available to download for 10 years from the summary file log date. Package usage log data is available
to download for 45 days from the date that the log event occurred. Subscriber snapshot data is available to download for 45 days from
the snapshot date.

The usage data that AppExchange App Analytics collects depends on the org type and data type.


### Second-Generation Managed Packages Considerations for Custom Interactions

**Table 5: Data Type Collection Varies by Org Type**

Note: [AppExchange App Analytics is subject to certain usage restrictions as described in AppExchange Program Policies.](https://www.salesforce.com/content/dam/web/en_us/www/documents/legal/Agreements/alliance-agreements-and-terms/salesforce-partner-program-policies.pdf)

**1.** Log in to the License Management Org (LMO) that the package is registered to.

**2.** [From the LMO, complete the required fields in the AppAnalyticsQueryRequest object.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_appanalyticsqueryrequest.htm)

**3.** Retrieve the App Analytics Query Request object created in the API request. The `DownloadURL` field populates after the request
is completed.

**4.** Click the URL in the `DownloadURL` field in the App Analytics Query Request object, and download the .csv file.

Note: The download URL expires after 60 minutes.

### Considerations for Custom Interactions

Easily create and log custom interactions on your managed package using Apex. As subscribers
interact with your package and your Apex code is executed, the custom interactions that you defined
are logged. Retrieve your custom interactions in your package's AppExchange App Analytics usage
logs and usage summaries.

As an ISV partner, the complex features that you develop in your managed packages could involve
multiple actions on different objects, callouts to Apex functions, and much more. It can be difficult
to interpret how your subscribers interacted with specific packaged components via your
downloaded App Analytics package usage logs and summaries.

To provide you with more clarity about your subscribers’ events in custom ways and at different
granularity levels, create custom interactions in your managed packages using Apex.

With Apex custom interactions, you can discover:

**•** Which app feature a user interacted with

**•** How users flowed through a specific user journey

**•** Which UI components a user interacted with

Keep these considerations in mind:

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** A custom interaction can appear for a given user request up to 50 times. This limit avoids flooding the logs due to large loops.

**•** We recommend that you don’t call `IsvPartners.AppAnalytics.logCustomInteraction` from inside a loop.

**•** If the `IsvPartners.AppAnalytics.logCustomInteraction` method is called from a running Apex test, no
AppExchange App Analytics package usage log or package usage summary data is produced.


Second-Generation Managed Packages Considerations for Custom Interactions

Log Custom Interactions
Create and log custom interactions with your managed package using Apex.

SEE ALSO:

[Apex Developer Guide: Enums](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/langCon_apex_enums.htm)

Download Package Usage Logs, Package Usage Summaries, and Subscriber Snapshots

[Apex Reference Guide: IsvPartners Namespace](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_namespace_IsvPartners.htm)

Custom Interactions

Log Custom Interactions

Create and log custom interactions with your managed package using Apex.

**1.** In your packaged Apex code, include Apex enums that are associated with the events that you want to log as custom interactions.

**2.** In your Apex code, invoke `IsvPartners.AppAnalytics.logCustomInteraction`, using the enums that you created.

**3.** Test your code by running it in your development environment and checking your debug logs to be certain that the custom
interactions you created are being logged. Ensure that your debug log levels for `Apex Code` are set to `FINE` .

**4.** After you’re finished with your implementation, publish a new version of your managed package.

**5.** After subscribers install your package, retrieve your package usage logs and package usage summaries. Filter your package usage
log data on `custom_entity_type` by CustomInteractionLabel, and on `log_record_type` by CustomInteraction. Or filter
your package usage summary data on `custom_entity_type` by CustomInteractionLabel.

**6.** Analyze your custom interaction data.

Example: Let’s suppose you have a Lightning Web Component (LWC). Your LWC provides a list of related contacts for each
Account record, uses a table layout, and is wired to an Apex class. You add a new card layout to your LWC. To track how well users
are adopting this new layout, you log an interaction when a user switches between

layouts.

In your code, include Apex enums and invoke `IsvPartners.AppAnalytics.logCustomInteraction` .

Your LWC HTML code:

```
      <template>

        <div

           class="slds-var-m-top_medium slds-var-m-bottom_x-large slds-box

      slds-theme_default"

        >

           <h2 class="slds-text-heading_medium slds-var-m-bottom_medium">

             Change data view

           </h2>

        <!-- Button group: simple buttons -->

        <lightning-button-group class="slds-var-m-bottom_medium">

           <lightning-button

             label="Table"

             variant={tableVariant}

             onclick={handleClick}

        ></lightning-button>

```


Second-Generation Managed Packages Considerations for Custom Interactions

```
           <lightning-button

             label="Card"

             variant={cardVariant}

             onclick={handleClick}

           ></lightning-button>

        </lightning-button-group>

        <template lwc:if={displayTable}>

           <lightning-datatable

             key-field="id"

             data={records}

             columns={columns}

           ></lightning-datatable>

        </template>

        <template lwc:if={displayCard}>

           <div class="slds-grid slds-wrap slds-grid_pull-padded-small">

             <template for:each={records} for:item="contact">

           <div

             class="slds-col slds-small-size_1-of-1 slds-large-size_1-of-2

      slds-var-p_small"

             key={contact.id}

           >

             <lightning-card

               variant="Narrow"

               title={contact.name}

               icon-name="standard:contact"

             >

               <div class="slds-var-p-horizontal_small">

                  <p>{contact.name}</p>

                  <p>{contact.title}</p>

                  <p>

                    <lightning-formatted-phone

                    value={contact.phone}

                    ></lightning-formatted-phone>

                  </p>

                  <p>

                    <lightning-formatted-email

                    value={contact.email}

                    ></lightning-formatted-email>

                 </p>

               </div>

             </lightning-card>

           </div>

        </template>

        </div>

        </template>

         </div>

      </template>

```

Your LWC JavaScript code:

```
      import { LightningElement, wire, api } from "lwc";

      import { getRelatedListRecords } from "lightning/uiRelatedListApi";

      import logInteraction from "@salesforce/apex/LogContactListInteraction.log";

      export default class ContactList extends LightningElement {

```


Second-Generation Managed Packages Considerations for Custom Interactions

```
        @api recordId;

        error;

        records;

        displayTable = true;

        displayCard = false;

        columns = [

           { label: "Name", fieldName: "name" },

           { label: "Title", fieldName: "title" },

           { label: "Email", fieldName: "email", type: "email" },

           { label: "Phone", fieldName: "phone", type: "phone" }

        ];

        @wire(getRelatedListRecords, {

           parentRecordId: "$recordId",

           relatedListId: "Contacts",

           fields: [

             "Contact.Name",

             "Contact.Id",

             "Contact.Phone",

             "Contact.Email",

             "Contact.Title"

        ],

        sortBy: ["Contact.Name"]

        })

        contactList({ error, data }) {

           if (data) {

           this.records = data.records.map((item) => {

             return {

              name: item.fields.Name.value,

              id: item.fields.Id.value,

              title: item.fields.Title.value,

              email: item.fields.Email.value,

              phone: item.fields.Phone.value

              };

           });

           this.error = undefined;

        } else if (error) {

           this.error = error;

           this.records = undefined;

           }

        }

        handleClick(event) {

           if (event.target.label.toLowerCase() === "table") {

           this.displayTable = true;

           this.displayCard = false;

             logInteraction({ type: "table" });

           } else if (event.target.label.toLowerCase() === "card") {

              this.displayTable = false;

              this.displayCard = true;

              logInteraction({ type: "card" });

           }

        }

        get cardVariant() {

           return this.displayCard === true ? "brand" : "";

```


Second-Generation Managed Packages Considerations for Custom Interactions

```
        }

        get tableVariant() {

           return this.displayTable === true ? "brand" : "";

        }

      }

```

Your Apex class:

```
      public class LogContactListInteraction {

        public Enum ContactListLayouts { TABLE, CARD }

        @AuraEnabled

        public static void log(String type) {

           try {

            IsvPartners.AppAnalytics.logCustomInteraction(getInteractionLabel(type));

           } catch (Exception e) {

             throw new AuraHandledException(e.getMessage());

           }

        }

        private static ContactListLayouts getInteractionLabel(String type) {

           if (type.toLowerCase() == 'table') {

             return ContactListLayouts.TABLE;

           } else if (type.toLowerCase() == 'card') {

             return ContactListLayouts.CARD;

           }

           return null;

        }

      }

```

Next, you test your code. With your Apex code debug log level set to `FINE`, confirm that the custom interactions are logged by
finding events in your debug logs called `APP_ANALYTICS_FINE`, `APP_ANALYTICS_WARN`, or `APP_ANALYTICS_ERROR` .

```
      APP_ANALYTICS_FINE [External]IsvPartners.AppAnalytics.logCustomInteraction was called,

      but not from an installed managed package.

      This means that the code is ready to be packaged.

```

SEE ALSO:

Package Usage Logs Schema

Considerations for Custom Interactions


### Second-Generation Managed Packages AppExchange App Analytics Best Practices AppExchange App Analytics Best Practices

To plan and maximize your AppExchange App Analytics query strategy, follow our best practices.
First, use file compression to reduce your data results file size. Second, schedule and automate your
regular App Analytics queries. Third, plan, schedule, and automate catch-up queries to supplement
your regular query data.

#### How Does AppExchange App Analytics Data Flow?

As your customers use your managed packages, they produce data. Their usage data is collected
daily in our data lake from each Salesforce instance. Usage data arrives to our data lake
throughout the day. From time to time, there can be data arrival delays. Also, data builds and
timestamps vary by data type. For these reasons, to optimize your data retrieval, plan out your
AppExchange App Analytics query strategy.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

How Should I Plan My App Analytics Query Strategy?
Your detailed query strategy depends on the size and scope of your business and the data types that you’re querying.

Recommendations
Your query strategy varies based on your business size and scope. Also, your query strategy must adapt as your business grows. To
stay current, follow our App Analytics query recommendations for small, medium, and large-sized partners.

Where Do I Go for More Information About AppExchange App Analytics Queries?
Questions are natural when you start automating your queries and planning your query strategy. To find a good solution when you
have questions, review your code base and the size and skill of your development team.

#### How Does AppExchange App Analytics Data Flow?

As your customers use your managed packages, they produce data. Their usage data is collected
daily in our data lake from each Salesforce instance. Usage data arrives to our data lake throughout
the day. From time to time, there can be data arrival delays. Also, data builds and timestamps vary
by data type. For these reasons, to optimize your data retrieval, plan out your AppExchange App
Analytics query strategy.

Because Salesforce instances and your subscribers are located around the world, the time of data
collection varies by region. EU (EMEA) data arrives first, then North America (NA) data. Data from
Asia Pacific (AP) instances arrives last.

Our AppExchange App Analytics jobs run on local instance times on a non-peak schedule. Depending
on when you query for your data and where your customers are located, sometimes you retrieve
100% of your data at one time. Other times you must issue more queries to retrieve it all.


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Second-Generation Managed Packages AppExchange App Analytics Best Practices

Data delivery to and arrival in our data lake also depends on factors that can affect a given instance, such as the health of the instance
or technical dependencies. Ordinarily you can expect all your org data to arrive in the data lake by `23:00` Coordinated Universal Time
(UTC) the day after it was recorded. However, occasionally, there can be delays.

Each AppExchange App Analytics data type is also compiled at different times.


Second-Generation Managed Packages AppExchange App Analytics Best Practices

#### How Should I Plan My App Analytics Query Strategy?

Your detailed query strategy depends on the size and scope of your business and the data types
that you’re querying.

All partners can take advantage of these query strategies.

**•** Choose a data results `FileType` value, and select a corresponding `FileCompression` .
With this query strategy, you can choose `gzip` compression for `csv` files or `snappy` column
compression for `parquet` files.

**•** Create regularly scheduled, automated queries.

**•** To sweep in late-arriving data, create catch-up queries using the `AvailableSince` field.

Compress Your Results Files

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Your App Analytics query plan starts with your results file type and file compression. Data can eat up time and space, so do more with
less by specifying the type of file you download. Reduce your data download time by specifying how your results file is compressed.

If you don’t specify file type or file compression, your results file defaults to `csv` with no compression for backwards compatibility
reasons. If you choose the `parquet` file type, your results file includes data type information for each column.

We recommend that you always compress your results files. Choose from these SOAP API `AppAnalyticsQueryRequest`
`FileType` and `FileCompression` value combinations.

Note: When you download your App Analytics query result data, the HTTP response contains one or two important headers. The
Content-Type header indicates the file type ( `txt` / `csv` or `application` / `parquet` ). For queries with `csv` FileType and

`gzip` FileCompression, the Content-Encoding header indicates `gzip` encoding. Modern browsers often decode the
`gzip` -encoded file automatically, which results in a saved, uncompressed .csv file. Regardless if the file is automatically decoded
or not, its filename extension is .csv.


Second-Generation Managed Packages AppExchange App Analytics Best Practices

Schedule and Automate Your Queries

After you determine what queries to run and how often to run them, you want to schedule those queries. The easiest way is via automation.

What do we mean by automation? Write code that creates query request records on your schedule, monitors them, retrieves the data,
and stores your AppExchange App Analytics data somewhere. For example, you can store the data in a custom object in your License
Management Org.

Your automation options include, but aren’t limited to:

**•** Custom API integrations using REST or SOAP API calls

**•** Salesforce DX automation using the CLI

**•** Salesforce flows

**•** Apex triggers

For example, automate the retrieval of package usage summaries using Apex triggers.

If you want to also automate the retrieval of package usage log data, look to a different storage solution that scales with the data volume
the logs contain.

Create Catch-Up Queries

A catch-up query is like a broom, sweeping for data newly added to our data lake. Catch-up queries rely on you already having regular
queries in place.

For example, on March 2, 2021 `18:00 UTC` you run this regular query that retrieves package usage log data for March 1, 2021:

```
   sf data create record

   --sobjecttype AppAnalyticsQueryRequest

   --values "StartTime=2021-03-01T00:00:00Z

   EndTime=2021-03-02T00:00:00Z

   DataType=PackageUsageLog

   FileType=csv

   FileCompression=gzip"

```

Rerun that exact same query on March 3, 2021 `18:00 UTC`, but add the `AvailableSince` field set to the day and time you ran
your original query: `2021-03-02T18:00:00Z` . This query is your ad hoc catch-up query. It retrieves any data newly added to the
data lake for March 2 since you ran your regular query:

```
   sf data create record

   --sobjecttype AppAnalyticsQueryRequest

   --values "StartTime=2021-03-01T00:00:00Z

   EndTime=2021-03-02T00:00:00Z

   DataType=PackageUsageLog

   FileType=csv

   FileCompression=gzip

   AvailableSince=2021-03-02T18:00:00Z"

```

You can use catch-up queries in many different ways, which we discuss in more detail in the Recommendations section.

When creating catch-up queries, keep these considerations in mind.

**•** If `StartTime` is specified, the `AvailableSince` date must be later.

**•** If `EndTime` is specified, the `AvailableSince` date must be later.

**•** All queries must include `StartTime` or `AvailableSince` or both.

**•** `AvailableSince` must be earlier than now.


Second-Generation Managed Packages AppExchange App Analytics Best Practices

Note: What happens when you want to create an ad hoc catch-up query, but you forgot when you ran the original query? Use
Salesforce CLI and your original query’s `sObjectID` to look up the `QuerySubmittedTime`, like this: `sf data get`

`record --sobjecttype AppAnalyticsQueryRequest --sobjectid 0XIXXXXXXXXXXXXXXX` Set your
ad hoc catch-up query `AvailableSince` value to equal the `QuerySubmittedTime` .

SEE ALSO:

[Apache Parquet](https://parquet.apache.org/)

[Automate AppAnalytics - AWS Stack](https://medium.com/@kamipatel/automate-appanalytics-aws-stack-74cbebc49d2a)

#### Recommendations

Your query strategy varies based on your business size and scope. Also, your query strategy must
adapt as your business grows. To stay current, follow our App Analytics query recommendations
for small, medium, and large-sized partners.

Note: In the unlikely event of data delays, we regenerate data for log events that happened
up to 30 days in the past. To ensure that you consistently retrieve the most complete data,
we recommend that you schedule catch-up queries that look back 30 days.

##### Small-Sized Partners

Small-sized partners have manageable subscriber bases and one or two managed packages.
A small partner’s total daily usage data across all managed packages is 5 GB or less. Also, small
partner’s queries complete well under the 15-minute processing time limit.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Medium-Sized Partners
Medium-sized partners have bigger subscriber bases and about six managed packages. A medium-sized partner’s total daily usage
data across all managed packages is at or just over 20 GB. Also, this partner’s queries approach or hit the 15-minute processing time
limit.

Large-Sized Partners
Large partners have large subscriber bases and many managed packages. A large partner’s total daily data usage is more than 20
GB. Sometimes a large partner’s data from just one managed package is larger than the 20-GB daily limit. Also, large partners often
must create a smaller time range for each query to complete in under the 15-minute processing time limit.

##### Small-Sized Partners

Small-sized partners have manageable subscriber bases and one or two managed packages. A
small partner’s total daily usage data across all managed packages is 5 GB or less. Also, small partner’s
queries complete well under the 15-minute processing time limit.

Given how manageable smaller partners’ data is, after you run your regular queries one time, we
recommend that you run a daily catch-up query as your main query. Sweep in all data for all your
managed packages for the last 30 days.


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Second-Generation Managed Packages AppExchange App Analytics Best Practices

Example: Most of your customers use your package on an NA or EU instance, so you run your queries at `18:00 UTC` . You
have a couple customers on an AP instance, so you create catch-up queries to ensure that you capture data from around the world.

**•** On March 31 at `18:00 UTC`, run your regular queries.

Subscriber Snapshot

```
  sf data create record

  --sobjecttype AppAnalyticsQueryRequest

  --values "DataType=SubscriberSnapshot

  FileType=csv

  FileCompression=gzip

  StartTime=2020-03-30T00:00:00Z

  EndTime=2020-03-31T00:00:00Z"

```

Package Usage Summary

```
  sf data create record

  --sobjecttype AppAnalyticsQueryRequest

```


Second-Generation Managed Packages AppExchange App Analytics Best Practices

```
       --values "DataType=PackageUsageSummary

       FileType=csv

       FileCompression=gzip

       StartTime=2020-02-01T00:00:00Z

       EndTime=2020-03-01T00:00:00Z"

```

Package Usage Log

```
       sf data create record

       --sobjecttype AppAnalyticsQueryRequest

       --values "DataType=PackageUsageLog

       FileType=csv

       FileCompression=gzip

       StartTime=2020-03-30T00:00:00Z

       EndTime=2020-03-31T00:00:00Z"

```

**•** On April 1 at `18:00 UTC` run these three catch-up queries.

Subscriber Snapshot Catch-Up Query

```
       sf data create record

       --sobjecttype AppAnalyticsQueryRequest

       --values "DataType=SubscriberSnapshot

       FileType=csv

       FileCompression=gzip

       StartTime=2020-03-02T00:00:00Z

       AvailableSince=2020-03-31T18:00:00Z"

```

Package Usage Summary Catch-Up Query

```
       sf data create record

       --sobjecttype AppAnalyticsQueryRequest

       --values "DataType=PackageUsageSummary

       FileType=csv

       FileCompression=gzip

       StartTime=2020-03-01T00:00:00Z

       AvailableSince=2020-03-31T18:00:00Z"

```

Package Usage Log Catch-Up Query

```
       sf data create record

       --sobjecttype AppAnalyticsQueryRequest

       --values "DataType=PackageUsageLog

       FileType=csv

       FileCompression=gzip

       StartTime=2020-03-02T00:00:00Z

       AvailableSince=2020-03-31T18:00:00Z"

```

**•** On April 2 at `18:00 UTC`, run the same catch-up queries, but advance the subscriber snapshot and package usage log
`AvailableSince` and `StartTime` date by 1 day each. Advance the package usage summary `AvailableSince`
by 1 day.

Subscriber Snapshot Catch-Up Query

```
       sf data create record

       --sobjecttype AppAnalyticsQueryRequest

       --values "DataType=SubscriberSnapshot

```


Second-Generation Managed Packages AppExchange App Analytics Best Practices

```
       FileType=csv

       FileCompression=gzip

       StartTime=2020-03-03T00:00:00Z

       AvailableSince=2020-04-01T18:00:00Z"

```

Package Usage Summary Catch-Up Query

```
       sf data create record

       --sobjecttype AppAnalyticsQueryRequest

       --values "DataType=PackageUsageSummary

       FileType=csv

       FileCompression=gzip

       StartTime=2020-03-01T00:00:00Z

       AvailableSince=2020-04-01T18:00:00Z"

```

Package Usage Log Catch-Up Query

```
       sf data create record

       --sobjecttype AppAnalyticsQueryRequest

       --values "DataType=PackageUsageLog

       FileType=csv

       FileCompression=gzip

       StartTime=2020-03-03T00:00:00Z

       AvailableSince=2020-04-01T18:00:00Z"

##### Medium-Sized Partners

```

Medium-sized partners have bigger subscriber bases and about six managed packages. A
medium-sized partner’s total daily usage data across all managed packages is at or just over 20 GB.
Also, this partner’s queries approach or hit the 15-minute processing time limit.

We recommend that after you run your regular queries one time, use catch-up queries as your main
queries for subscriber snapshots and package usage summaries. Use a combination of daily queries
and catch-up queries for package usage logs.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions


Second-Generation Managed Packages AppExchange App Analytics Best Practices

Example: Half of your customers use your package on an NA or EU instance, so you run your regular queries at `18:00 UTC` .
The other half of your customers are on an AP instance, so you create catch-up queries to ensure that you capture data from around
the world.

**•** On March 31 at `18:00 UTC`, run your regular package usage log queries for each of your packages.

Package 1

```
    sf data create record

    --sobjecttype AppAnalyticsQueryRequest

    --values "StartTime=2021-03-30T00:00:00Z

    EndTime=2021-03-31T00:00:00Z

    DataType=PackageUsageLog

    PackageIds=0336XXXXXXXXXX

    FileType=csv

    FileCompression=gzip"

```

Package 2

```
    sf data create record

    --sobjecttype AppAnalyticsQueryRequest

    --values "StartTime=2021-03-30T00:00:00Z

    EndTime=2021-03-31T00:00:00Z

    DataType=PackageUsageLog

    PackageIds=0337XXXXXXXXXX

```


Second-Generation Managed Packages AppExchange App Analytics Best Practices

```
       FileType=csv

       FileCompression=gzip"

```

**•** On April 1 at `18:00 UTC` onwards, run regular and catch-up package usage log queries.

A. Regular Queries

Package 1

```
       sf data create record

       --sobjecttype AppAnalyticsQueryRequest

       --values "StartTime=2021-03-31T00:00:00Z

       EndTime=2021-04-01T00:00:00Z

       DataType=PackageUsageLog

       PackageIds=0336XXXXXXXXXX

       FileType=csv

       FileCompression=gzip"

```

Package 2

```
       sf data create record

       --sobjecttype AppAnalyticsQueryRequest

       --values "StartTime=2021-03-31T00:00:00Z

       EndTime=2021-04-01T00:00:00Z

       DataType=PackageUsageLog

       PackageIds=0337XXXXXXXXXX

       FileType=csv

       FileCompression=gzip"

```

B. Catch-Up Queries

Package 1

```
       sf data create record

       --sobjecttype AppAnalyticsQueryRequest

       --values "StartTime=2021-03-01T00:00:00Z

       EndTime=2021-03-31T00:00:00Z

       AvailableSince=2021-03-31T18:00:00Z

       DataType=PackageUsageLog

       PackageIds=0336XXXXXXXXXX

       FileType=csv

       FileCompression=gzip"

```

Package 2

```
       sf data create record

       --sobjecttype AppAnalyticsQueryRequest

       --values "StartTime=021-03-01T00:00:00Z

       EndTime=2021-03-31T00:00:00Z

       AvailableSince=2021-03-31T18:00:00Z

       DataType=PackageUsageLog

       PackageIds=0337XXXXXXXXXX

```


Second-Generation Managed Packages AppExchange App Analytics Best Practices

```
       FileType=csv

       FileCompression=gzip"

```

**•** On April 2, repeat the same queries that you ran on April 1, but advance the queries by a day.

A. Regular Queries

Package 1

```
       sf data create record

       --sobjecttype AppAnalyticsQueryRequest

       --values "StartTime=2021-04-01T00:00:00Z

       EndTime=2021-04-02T00:00:00Z

       DataType=PackageUsageLog

       PackageIds=0336XXXXXXXXXX

       FileType=csv

       FileCompression=gzip"

```

Package 2

```
       sf data create record

       --sobjecttype AppAnalyticsQueryRequest

       --values "StartTime=2021-04-01T00:00:00Z

       EndTime=2021-04-02T00:00:00Z

       DataType=PackageUsageLog

       PackageIds=0337XXXXXXXXXX

       FileType=csv

       FileCompression=gzip"

```

B. Catch-Up Queries

Package 1

```
       sf data create record

       --sobjecttype AppAnalyticsQueryRequest

       --values "StartTime=2021-03-02T00:00:00Z

       EndTime=2021-04-01T00:00:00Z

       AvailableSince=2021-04-01T18:00:00Z

       DataType=PackageUsageLog

       PackageIds=0336XXXXXXXXXX

       FileType=csv

       FileCompression=gzip"

```

Package 2

```
       sf data create record

       --sobjecttype AppAnalyticsQueryRequest

       --values "StartTime=2020-03-02T00:00:00Z

       EndTime=2021-04-01T00:00:00Z

       AvailableSince=2021-04-01T18:00:00Z

       DataType=PackageUsageLog

       PackageIds=0337XXXXXXXXXX

```


Second-Generation Managed Packages AppExchange App Analytics Best Practices

```
       FileType=csv

       FileCompression=gzip"

##### Large-Sized Partners

```


Second-Generation Managed Packages AppExchange App Analytics Best Practices

Example: Your customers use your package on all Salesforce instances around the world, and your managed packages produce
significant amounts of data. You schedule queries to run at the same time, each covering a 12-hour period, and you create a layered
catch-up query plan to capture data from all instances.

In this example, we show two of your dozens of managed packages.

**•** On March 31 at `18:00 UTC`, run your regular package usage log queries.

Package 1

```
       sf data create record data create record

       --sobjecttype AppAnalyticsQueryRequest

       --values "StartTime=2021-03-30T00:00:00

       EndTime=2021-03-30T12:00:00

       DataType=PackageUsageLog

       PackageIds=0336XXXXXXXXXX

       FileType=parquet

       FileCompression=snappy"

       sf data create record

       --sobjecttype AppAnalyticsQueryRequest

       --values "StartTime=2021-03-30T12:00:00

       EndTime=2021-03-31T00:00:00

       DataType=PackageUsageLog

       PackageIds=0336XXXXXXXXXX

       FileType=parquet

       FileCompression=snappy"

```

Package 2

```
       sf data create record

       --sobjecttype AppAnalyticsQueryRequest

       --values "StartTime=2021-03-30T00:00:00

       EndTime=2021-03-30T12:00:00

       DataType=PackageUsageLog

       PackageIds=0337XXXXXXXXXX

       FileType=parquet

       FileCompression=snappy"

       sf data create record

       --sobjecttype AppAnalyticsQueryRequest

       --values "StartTime=2021-03-30T12:00:00

       EndTime=2021-03-31T00:00:00

       DataType=PackageUsageLog

       PackageIds=0337XXXXXXXXXX

       FileType=parquet

       FileCompression=snappy"

```


Second-Generation Managed Packages AppExchange App Analytics Best Practices

**•** On April 1 at `18:00 UTC`, run your regular and catch-up package usage log queries.

A. Package Usage Log Regular Queries

Package 1

```
       sf data create record

       --sobjecttype AppAnalyticsQueryRequest

       --values "StartTime=2021-03-31T00:00:00Z

       EndTime=2021-03-31T12:00:00Z

       DataType=PackageUsageLog

       PackageIds=0336XXXXXXXXXX

       FileType=parquet

       FileCompression=snappy"

       sf data create record

       --sobjecttype AppAnalyticsQueryRequest

       --values "StartTime=2021-03-31T12:00:00Z

       EndTime=2021-04-01T00:00:00Z

       DataType=PackageUsageLog

       PackageIds=0336XXXXXXXXXX

       FileType=parquet

       FileCompression=snappy"

```

Package 2

```
       sf data create record

       --sobjecttype AppAnalyticsQueryRequest

       --values "StartTime=2021-03-31T00:00:00Z

       EndTime=2021-03-31T12:00:00Z

       DataType=PackageUsageLog

       PackageIds=0337XXXXXXXXXX

       FileType=parquet

       FileCompression=snappy"

       sf data create record

       --sobjecttype AppAnalyticsQueryRequest

       --values "StartTime=2021-03-31T12:00:00Z

       EndTime=2021-04-01T00:00:00Z

       DataType=PackageUsageLog

       PackageIds=0337XXXXXXXXXX

       FileType=parquet

       FileCompression=snappy"

```

B. Package Usage Log 2 Days Ago Catch-Up Queries

Package 1

```
       sf data create record

       --sobjecttype AppAnalyticsQueryRequest

       --values "StartTime=2021-03-30T00:00:00Z

```


Second-Generation Managed Packages AppExchange App Analytics Best Practices

```
       EndTime=2021-03-31T00:00:00Z

       DataType=PackageUsageLog

       PackageIds=0336XXXXXXXXXX

       FileType=parquet

       FileCompression=snappy

       AvailableSince=2020-03-31T18:00:00Z"

```

Package 2

```
       sf data create record

       --sobjecttype AppAnalyticsQueryRequest

       --values "StartTime=2021-03-30T00:00:00Z

       EndTime=2021-03-31T00:00:00Z

       DataType=PackageUsageLog

       PackageIds=0337XXXXXXXXXX

       FileType=parquet

       FileCompression=snappy

       AvailableSince=2020-03-31T18:00:00Z"

```

C. Package Usage Log From 3 to 30 Days Ago Catch-Up Queries

Package 1

```
       sf data create record

       --sobjecttype AppAnalyticsQueryRequest

       --values "StartTime=2021-03-01T00:00:00Z

       EndTime=2021-03-30T00:00:00Z

       DataType=PackageUsageLog

       PackageIds=0336XXXXXXXXXX

       FileType=parquet

       FileCompression=snappy

       AvailableSince=2020-03-31T18:00:00Z"

```

Package 2

```
       sf data create record

       --sobjecttype AppAnalyticsQueryRequest

       --values "StartTime=2021-03-01T00:00:00Z

       EndTime=2021-03-30T00:00:00Z

       DataType=PackageUsageLog

       PackageIds=0337XXXXXXXXXX

       FileType=parquet

       FileCompression=snappy

       AvailableSince=2020-03-31T18:00:00Z"

```

**•** On April 2 onwards, run your regular and your catch-up package usage log queries, advancing the dates by 1 day.

A. Package Usage Log Regular Queries


Second-Generation Managed Packages AppExchange App Analytics Best Practices

Package 1

```
       sf data create record

       --sobjecttype AppAnalyticsQueryRequest

       --values "StartTime=2021-04-01T00:00:00Z

       EndTime=2021-04-01T12:00:00Z

       DataType=PackageUsageLog

       PackageIds=0336XXXXXXXXXX

       FileType=parquet

       FileCompression=snappy"

       sf data create record

       --sobjecttype AppAnalyticsQueryRequest

       --values "StartTime=2021-04-01T12:00:00Z

       EndTime=2021-04-02T00:00:00Z

       DataType=PackageUsageLog

       PackageIds=0336XXXXXXXXXX

       FileType=parquet

       FileCompression=snappy"

```

Package 2

```
       sf data create record

       --sobjecttype AppAnalyticsQueryRequest

       --values "StartTime=2021-04-01T00:00:00Z

       EndTime=2021-04-01T12:00:00Z

       DataType=PackageUsageLog

       PackageIds=0337XXXXXXXXXX

       FileType=parquet

       FileCompression=snappy"

       sf data create record

       --sobjecttype AppAnalyticsQueryRequest

       --values "StartTime=2021-04-01T12:00:00Z

       EndTime=2021-04-02T00:00:00Z

       DataType=PackageUsageLog

       PackageIds=0337XXXXXXXXXX

       FileType=parquet

       FileCompression=snappy"

```

B. Package Usage Log 2 Days Ago Catch-Up Queries

Package 1

```
       sf data create record

       --sobjecttype AppAnalyticsQueryRequest

       --values "StartTime=2021-03-31T00:00:00Z

       EndTime=2021-04-01T00:00:00Z

       DataType=PackageUsageLog

       PackageIds=0336XXXXXXXXXX

       FileType=parquet

       FileCompression=snappy

       AvailableSince=2020-04-01T18:00:00Z”

```


Second-Generation Managed Packages AppExchange App Analytics Best Practices

Package 2

```
       sf data create record

       --sobjecttype AppAnalyticsQueryRequest

       --values "StartTime=2021-03-31T00:00:00Z

       EndTime=2021-04-01T00:00:00Z

       DataType=PackageUsageLog

       PackageIds=0337XXXXXXXXXX

       FileType=parquet

       FileCompression=snappy

       AvailableSince=2020-04-01T18:00:00Z"

```

C. Package Usage Log From 3 to 30 Days Ago Catch-Up Queries

Package 1

```
       sf data create record

       --sobjecttype AppAnalyticsQueryRequest

       --values "StartTime=2021-03-02T00:00:00Z

       EndTime=2021-03-31T00:00:00Z

       DataType=PackageUsageLog

       PackageIds=0336XXXXXXXXXX

       FileType=parquet

       FileCompression=snappy

       AvailableSince=2020-04-01T18:00:00Z"

```

Package 2

```
       sf data create record

       --sobjecttype AppAnalyticsQueryRequest

       --values "StartTime=2021-03-02T00:00:00Z

       EndTime=2021-03-31T00:00:00Z

       DataType=PackageUsageLog

       PackageIds=0337XXXXXXXXXX

       FileType=parquet

       FileCompression=snappy

       AvailableSince=2020-04-01T18:00:00Z"

#### Where Do I Go for More Information About AppExchange App Analytics Queries?

```

Questions are natural when you start automating your queries and planning your query strategy.
To find a good solution when you have questions, review your code base and the size and skill of
your development team.

If you still need help, try these resources:

**•** If you have an assigned AppExchange Partner Account Manager (PAM) or AppExchange
Technical Evangelist (TE), reach out to them.

**•** [Otherwise, go to the Partner Community and post a question to the ISV TE Experts - Partner](https://partners.salesforce.com/_ui/core/chatter/groups/GroupProfilePage?g=0F93A000000HWsf)
[Intelligence Chatter group.](https://partners.salesforce.com/_ui/core/chatter/groups/GroupProfilePage?g=0F93A000000HWsf)


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

### Second-Generation Managed Packages Package Usage Summaries Package Usage Summaries

Package usage summaries provide high-level metrics by calendar month. Discover how many users access your package and which
operations they perform.

Note: [AppExchange App Analytics is subject to certain usage restrictions as described in the AppExchange Program Policies.](https://www.salesforce.com/content/dam/web/en_us/www/documents/legal/Agreements/alliance-agreements-and-terms/salesforce-partner-program-policies.pdf)

AppExchange App Analytics tracks UI, API-based, Lightning-based, and Apex operations and logs each CRUD operation on components
and custom objects in packages. Events from sandbox, scratch, and trial orgs aren’t tracked in package usage summaries.

Partners and subscribers can access package usage data. Usage summaries become available at the beginning of the subsequent month.
For example, you can get the usage summary for May at the beginning of June.

**•** AppExchange Partners can request monthly usage summaries using the AppAnalyticsQueryRequest in SOAP API from the license
management org that owns the package.

**•** Subscribers can download usage summaries from Setup for any package that they installed that passed security review.

#### Package Usage Summary Schema

Use the package usage summary to discover how many users access your package and which operations they perform.

#### Package Usage Summary Schema

Use the package usage summary to discover how many users access your package and which operations they perform.

Package usage summaries contain aggregate data derived from related package usage logs. ISV partners have access to package usage
summaries by default, and they can activate access to package usage logs and subscriber snapshots. Subscribers only have access to
package usage summaries.


Second-Generation Managed Packages Package Usage Summaries


### Second-Generation Managed Packages Package Usage Logs

SEE ALSO:

### Package Usage Logs Schema Package Usage Logs

Analyze adoption and user behavior, then make informed feature development decisions based on data from package usage logs.
AppExchange App Analytics tracks UI, API-based, Lightning-based, and Apex operations, and it logs each CRUD operation on components
and custom objects in packages. Events from sandbox and trial orgs are tracked in package usage logs. Events from scratch orgs aren’t
tracked.

Note: [AppExchange App Analytics is subject to certain usage restrictions as described in the AppExchange Program Policies.](https://www.salesforce.com/content/dam/web/en_us/www/documents/legal/Agreements/alliance-agreements-and-terms/salesforce-partner-program-policies.pdf)

#### How to Read App Analytics Package Usage Log Data

App Analytics package usage logs contain data about how subscribers interact with your managed package. Your managed package
contains packaged components, and each package usage log line describes an interaction that a user has with one of your packaged
components. To understand that interaction, analyze each log line—or record—and focus on: what packaged component was
accessed, who interacted with that packaged component, and how that packaged component interaction occurred. Finally, analyze
the specific interaction data.

### Package Usage Logs Schema

Make informed development decisions based on package usage log data. Analyze adoption, user behavior, company information,
and Lightning app and page usage data. Package usage logs list activity during a 24-hour period, between 12:00 AM and 11:59 PM
UTC.

#### How to Read App Analytics Package Usage Log Data

App Analytics package usage logs contain data about how subscribers interact with your managed
package. Your managed package contains packaged components, and each package usage log
line describes an interaction that a user has with one of your packaged components. To understand
that interaction, analyze each log line—or record—and focus on: what packaged component was
accessed, who interacted with that packaged component, and how that packaged component
interaction occurred. Finally, analyze the specific interaction data.

Note: AppExchange App Analytics is subject to certain usage restrictions as described in the
[AppExchange Program Policies. Usage data from Government Cloud and Government Cloud](https://www.salesforce.com/content/dam/web/en_us/www/documents/legal/Agreements/alliance-agreements-and-terms/salesforce-partner-program-policies.pdf)
[Plus orgs isn’t available in App Analytics.](https://www.salesforce.com/solutions/industries/government1/products/government-cloud/)

Determine What Packaged Component Was Accessed
To analyze a package usage log record, always start with your packaged component.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Identify Who Interacted with Your Packaged Component
After you identify your packaged component, identify both the subscriber org and the user who triggered the interaction.


Second-Generation Managed Packages Package Usage Logs

Identify How a User Interacted with Your Packaged Component
After you identify your packaged component and who interacted with it, identify how the user interacted with your packaged
component.

Custom Object and External Object Interactions
When a log record in your package usage log has `custom_entity_type` equal to `CustomObject` or `ExternalObject`,
it means that a user performed an action that resulted in a create, read, update, or delete (CRUD) interaction on your object.

Lightning Interactions
Each record in your package usage log that has a `custom_entity_type` of `LightningComponent` or `LightningPage`
describes an interaction with your packaged Lightning component or page.

Apex Interactions
Each record in your package usage log that has a `custom_entity_type` of `ApexClass` or `ApexTrigger` describes an
interaction with your packaged Apex class or trigger.

Visualforce Interactions
Each record in your package usage log that has a `custom_entity_type` of `VisualforcePage` describes an interaction
with your packaged Visualforce pages.

CRM Analytics Asset Interactions
Each record in your package usage log that has a `custom_entity_type` of `AnalyticsDashboard`, `AnalyticsLens`,
or `AnalyticsRecipe` describes an interaction with your packaged CRM Analytics assets.

Custom Interactions
To understand which features and UI components a subscriber interacted with and how they flow through a user journey, create
custom interactions with Apex enums and the `IsvPartners.AppAnalytics.logCustomInteraction` Apex method.

SEE ALSO:

Package Usage Logs Schema

##### Determine What Packaged Component Was Accessed

To analyze a package usage log record, always start with your packaged component.

In App Analytics package usage logs, the name of each packaged component is represented by
the `custom_entity` field and its type is represented by the `custom_entity_type` field.
Your managed package likely contains multiple packaged components.

**•** To identify each packaged component uniquely, combine these fields.

**–** `package_id`

**–** `package_version_id`

**–** `managed_package_namespace`

**–** `custom_entity`

**–** `custom_entity_type`


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Second-Generation Managed Packages Package Usage Logs

##### Identify Who Interacted with Your Packaged Component

After you identify your packaged component, identify both the subscriber org and the user who
triggered the interaction.

**•** Identify the subscriber org with the `organization_id` . Some standard fields are always
populated and provide you with info about the subscriber org. Some supplemental fields, when
populated, add detail about that org.
This table describes the subscriber org fields.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**•** Use the `user_id_token` to identify and describe the user associated with the interaction. This hashed token represents the ID
of the user who accessed the package. The ID persists, even if a user’s details change, across any packages that the user interacts
with.
These supplemental fields, when populated, can provide you with more data about the user.

**–** `user_type`

**–** `user_agent`

**–** `user_country_code`

**–** `user_time_zone`

**–** `session_key`

**–** `login_key`

Because `user_id_token` can represent many different usage situations, we don’t recommend using App Analytics for auditing
customer license usage.

##### Identify How a User Interacted with Your Packaged Component

After you identify your packaged component and who interacted with it, identify how the user
interacted with your packaged component.

**•** Identify how the user interacted with your packaged component with `log_record_type` .
Other common fields associated with each interaction are:

**–** `request_id`

**–** `timestamp_derived`


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Second-Generation Managed Packages Package Usage Logs

##### Custom Object and External Object Interactions

When a log record in your package usage log has `custom_entity_type` equal to
`CustomObject` or `ExternalObject`, it means that a user performed an action that resulted
in a create, read, update, or delete (CRUD) interaction on your object.

To determine the type and amount of CRUD that occurred on your packaged component, focus
on:

**•** `operation_type`

**•** `operation_count`

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Many user actions result in CRUD, such as platform events, Apex REST API requests, or scheduled
job executions. Each action is related to a `log_record_type`, and each log record has some
standard fields that are always populated with data. For example, an Apex REST API request with a `log_record_type` of
`ApexRestApi` always has `url`, `api_version`, `http_method`, and `http_status_code` data. Many actions produce log
records with supplemental fields that are often populated. For example, an Apex REST API request sometimes has `request_status`,
`referrer_uri`, and `api_type` data.

CRUD from Apex REST API Requests

To analyze an Apex REST API request that resulted in a CRUD operation on your packaged component, look for a `log_record_type`
of `ApexRestApi` . Then use these fields to dig into the details of the Apex REST API interaction.

CRUD from Apex SOAP API Requests

To analyze an Apex SOAP API request that resulted in a CRUD operation on your packaged component, look for a `log_record_type`
of `ApexSoap` . Then use these fields to explore the details of the Apex SOAP API interaction.


Second-Generation Managed Packages Package Usage Logs

CRUD from REST API Requests

To analyze a REST API request that resulted in a CRUD operation on your packaged component, look for a `log_record_type` of
`RestApi` . Then use these fields to understand the details of the REST API interaction.

CRUD from SOAP API Requests

To analyze a SOAP API request that resulted in a CRUD operation on your packaged component, look for a `log_record_type` of
`API` . Then use these fields to uncover the details of the SOAP API interaction.

CRUD from Bulk API Requests

To analyze a Bulk API request that resulted in a CRUD operation on your packaged component, look for a `log_record_type` of
`BulkApiV1` or `BulkApiV2` . Then use these fields to discover the details of the Bulk API interaction.

CRUD from Scheduled Job Executions

To analyze a scheduled job execution that resulted in a CRUD operation on your packaged component, look for a `log_record_type`
of `CronJob` . There are no additional package usage log fields to describe scheduled job executions.


Second-Generation Managed Packages Package Usage Logs

CRUD from Platform Events

To analyze a platform event that resulted in a CRUD operation on your packaged component, look for a `log_record_type` of
`PlatformEventConsumer` . Then use these fields to discover the details of the platform event.

CRUD from Queueable Apex Executions

To analyze a queueable Apex execution that resulted in a CRUD operation on your packaged component, look for a `log_record_type`
of `QueuedExec` . There are no additional package usage log fields to describe Apex executions.

CRUD from Standard User Interface Requests

To analyze a user interaction that resulted in a CRUD operation on your packaged component, look for a `log_record_type` of
`URI` . Then use these fields to discover the details of the user interaction.

CRUD from Visualforce Remoting Requests

To analyze a Visualforce Remoting request that resulted in a CRUD operation on your packaged component, look for a
`log_record_type` of `VFRemoting` . Then use these fields to explore the details of the Visualforce Remoting request.


Second-Generation Managed Packages Package Usage Logs

CRUD from Visualforce Requests

To analyze a Visualforce request that resulted in a CRUD operation on your packaged component, look for a `log_record_type` of
`VisualforceRequest` . Then use these fields to explore the details of the Visualforce request.

CRUD from All Other User Actions

To analyze any other user action that results in a CRUD operation on your packaged component, look for a `log_record_type` of
`UnassociatedCRUD` . There are no additional package usage log fields to describe all other interactions.

Example: Let’s look at an example package usage log record and analyze the custom or external object interaction.

```
      {

         "timestamp_derived": "2022-12-15T05:47:35.945Z",

         "log_record_type": "VFRemoting",

         "request_id": "4mbhuJkvJ7Q83tlq2Z5aAk",

         "organization_id": "00Dxx0000006H2l",

         "organization_name": "MyCustomer Inc.",

         "organization_status": "Demo",

         "organization_edition": "Enterprise Edition",

         "organization_country_code": "IN",

         "organization_language_locale": "en_US",

         "organization_time_zone": "Australia/Sydney",

         "organization_instance": "GS0",

         "organization_type": "Production",

         "user_id_token": "005-rBBA92863JO8GJN3pT75gp0cG8a9z1vpH6MOti/359o=",

         "user_type": "Standard",

         "url":"uwlNmuT1+gH+xKq+xCoxiaAyOOhw8B4WLeQXAbgx+mA=",

         "package_id": "033xx0000004FqD",

         "package_version_id": "04txx0000004Idi",

         "managed_package_namespace": "Acme",

         "custom_entity": "Insurance_Agent",

         "custom_entity_type": "CustomObject",

```


Second-Generation Managed Packages Package Usage Logs

```
         "operation_type": "INSERT",

         "operation_count": 2,

         "session_key": "9/uZ+soHD+0UqKYt",

         "login_key": "5tjyGvX04w06xFgT",

        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36

      (KHTML, like Gecko) Chrome/IP_ADDRESS_REMOVED Safari/537.36",

         "user_country_code": "IN",

         "user_time_zone": "Asia/Kolkata",

         "class_name": "shwGCoJjDrkhbw+CY4TFzVxFWypN07UGvtGkexbj/y4=",

         "method_name": "3/UbV0E5yIW8a3c2Fb2XXjfWse1MUekEZWX44tp5TJs="

      }

```

The `Insurance_Agent` packaged component of type `CustomObject` had CRUD performed as a result of a user action
from the subscriber org `My Customer Inc.` Specifically, two records were inserted during a Visualforce Remoting request
that the user performed at 2022-12-15 at 05:47 am UTC.

The key data in this analysis are:

In this example, the Visualforce Remoting code isn’t owned by the package, so `url`, `class_name`, and `method_name` are
tokenized.

```
      "url": "uwlNmuT1+gH+xKq+xCoxiaAyOOhw8B4WLeQXAbgx+mA=",

      "class_name": "shwGCoJjDrkhbw+CY4TFzVxFWypN07UGvtGkexbj/y4=",

      "method_name": "3/UbV0E5yIW8a3c2Fb2XXjfWse1MUekEZWX44tp5TJs="

```

If the Visualforce Remoting code is part of the package, you see actual values instead of tokens.

SEE ALSO:

Package Usage Logs Schema


Second-Generation Managed Packages Package Usage Logs

##### Lightning Interactions

Each record in your package usage log that has a `custom_entity_type` of
`LightningComponent` or `LightningPage` describes an interaction with your packaged
Lightning component or page.

Note: We’re continually improving the recording of Lightning interaction data in package
usage logs. Many interactions with your packaged Lightning component or page are available
in AppExchange App Analytics, but not all. To determine which interactions we capture for
your specific package, compare your packaged components to your App Analytics package
usage logs.

Lightning User Interaction

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

When a user interacts with your `LightningPage` or `LightningComponent` packaged component, a `log_record_type`
of `LightningInteraction` is created. Some standard fields are always populated with data. For example, a Lightning component
interaction always has `app_name` and `ui_event_source` data. Lightning interactions have supplemental fields that are often
populated. For example, a Lightning interaction sometimes also has `page_app_name` and `page_context` data.

Lightning Page View

When a user views your Lightning page, a `log_record_type` of `LightningPageView` is created. Some standard fields are
always populated with data. For example, a Lightning page view always has `app_name` and `page_app_name` data. Lightning
page views have supplemental fields that are often populated. For example, a Lightning page view sometimes also has
`page_entity_type` and `prevpage_url` data.

Example: Let’s look at an example package usage log record and analyze the Lightning interaction.

```
   {

        "timestamp_derived": "2022-11-22T06:17:39.167Z",

        "log_record_type": "LightningInteraction",

        "request_id": "TID:7635077000004b3035",

```


Second-Generation Managed Packages Package Usage Logs

```
           "organization_id": "00Dxx0000006H2l",

           "organization_name": "MyCustomer Inc.",

           "organization_status": "Demo",

           "organization_edition": "Enterprise Edition",

           "organization_country_code": "IN",

           "organization_language_locale": "en_US",

           "organization_time_zone": "Australia/Sydney",

           "organization_instance": "GS0",

           "organization_type": "Production",

           "user_id_token": "005-9BwnBWYO5FMn4cZ1sLw7F3LmTpoe8M77GrZOZHL6xQk=",

           "user_type": "Standard",

           "package_id": "033xx0000004FqD",

           "package_version_id": "04txx0000004Idi",

           "managed_package_namespace": "Acme",

           "custom_entity": "Acme__Insurance_Agents",

           "custom_entity_type": "LightningPage",

           "session_key": "2l4YtFB/RmsRKVsS",

           "login_key": "fGV6RgVOH3ZCgl2v",

          "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36

      (KHTML, like Gecko) Chrome/IP_ADDRESS_REMOVED Safari/537.36",

           "user_country_code": "US",

           "user_time_zone": "America/Los_Angeles",

           "app_name": "one:one",

           "page_app_name": "Insurance_App",

           "page_context": "app_flexipage:lwcAppFlexipageWrapper",

           "ui_event_source": "click",

           "ui_event_type": "user",

           "ui_event_sequence_num": "10",

           "target_ui_element": "setup-app-nav-menu-item-link",

           "parent_ui_element": "global-setup",

           "page_url": "/lightning/n/Acme__Insurance_Agents"

        }

```

The `Acme_Insurance_Agents` Lightning page was interacted with as a result of a user action from subscriber org
`MyCustomer Inc` . Specifically, a Lightning interaction took place on the page on 2022-11-22 at 6:17 am.

The key data in this analysis are:


Second-Generation Managed Packages Package Usage Logs

Note: Lightning interaction data is captured on an event by event basis.

SEE ALSO:

Package Usage Logs Schema

[Lightning Interaction Event Type](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile_lightninginteraction.htm)

[Lightning Page View Event Type](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile_lightningpageview.htm)

##### Apex Interactions

Each record in your package usage log that has a `custom_entity_type` of `ApexClass` or `ApexTrigger` describes an
interaction with your packaged Apex class or trigger.

Available in: both Salesforce Classic and Lightning Experience

Available in: **Enterprise**, **Performance**, **Unlimited**, and **Developer** Editions

Apex Execution

When `log_record_type` is `ApexExecution`, the log record is associated with a user action that resulted in the execution of
Apex code from an Apex class or trigger. Only the outermost Apex is captured.

Apex Unexpected Exception

When `log_record_type` is `ApexUnexpectedException`, the log record is associated with a user action that resulted in an
Apex class or trigger throwing an unhandled exception. The `stack_trace` field provides detail about the Apex unexpected exceptions.

Example: Let’s look at an example package usage log record and analyze the Apex interaction.

```
      {

         "timestamp_derived": "2022-11-22T06:19:33.990Z",

         "log_record_type": "ApexExecution",

         "request_id": "4mbhxFWBBXz83tlq2Z5aAk",

         "organization_id": "00Dxx0000006H2l",

         "organization_name": "MyCustomer Inc.",

         "organization_status": "Demo",

         "organization_edition": "Enterprise Edition",

         "organization_country_code": "IN",

```


Second-Generation Managed Packages Package Usage Logs

```
         "organization_language_locale": "en_US",

         "organization_time_zone": "Australia/Sydney",

         "organization_instance": "GS0",

         "organization_type": "Production",

         "user_id_token": "005-9BwnBWYO5FMn4cZ1sLw7F3LmTpoe8M77GrZOZHL6xQk=",

         "user_type": "Standard",

         "package_id": "033xx0000004FqD",

         "package_version_id": "04txx0000004Idi",

         "managed_package_namespace": "Acme",

         "custom_entity": "InsuranceDetailsBatchable",

         "custom_entity_type": "ApexClass",

         "session_key": "2l4YtFB/RmsRKVsS",

         "login_key": "fGV6RgVOH3ZCgl2v",

        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36

      (KHTML, like Gecko) Chrome/IP_ADDRESS_REMOVED Safari/537.36",

         "user_country_code": "US",

         "user_time_zone": "America/Los_Angeles",

         "entry_point": "Acme.InsuranceDetailsBatchable",

         "num_soql_queries": "2",

         "quiddity": "A"

      }

```

The `InsuranceAgentDetailsBatchable` packaged component of type `ApexClass` was interacted with as a result
of a user action from subscriber org `MyCustomer Inc.` Specifically, an execution of a batch Apex job occurred on 2022-11-22
at 6:19 am. The batch Apex job is represented by Quiddity = A.

The key data in this analysis are:

SEE ALSO:

Package Usage Logs Schema

[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dev_guide.htm)


Second-Generation Managed Packages Package Usage Logs

##### Visualforce Interactions

Each record in your package usage log that has a `custom_entity_type` of
`VisualforcePage` describes an interaction with your packaged Visualforce pages.

Visualforce Requests

When a user performs an action that results in a request associated with your VisualForce page,
`log_record_type` equals `VisualforceRequest` . One standard field is always populated
with data: `url` .

Visualforce page requests also have supplemental fields that are often populated. For example, a
Visualforce page request sometimes also has `request_status` and `referrer_uri data` .

Use these fields to explore the details of the Visualforce request.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Example: Let’s look at an example package usage log record and analyze the Visualforce request.

```
{

   "timestamp_derived": "2022-11-22T06:23:23.836Z",

   "log_record_type": "VisualforceRequest",

   "request_id": "4mbi9e1ZVef83tlq2Z5aAk",

   "organization_id": "00Dxx0000006H2l",

   "organization_name": "MyCustomer Inc.",

   "organization_status": "Demo",

   "organization_edition": "Enterprise Edition",

   "organization_country_code": "IN",

   "organization_language_locale": "en_US",

   "organization_time_zone": "Australia/Sydney",

   "organization_instance": "GS0",

   "organization_type": "Production",

   "user_id_token": "005-9BwnBWYO5FMn4cZ1sLw7F3LmTpoe8M77GrZOZHL6xQk=",

   "user_type": "Standard",

   "url": "/apex/Acme__Agent_List",

   "package_id": "033xx0000004FqD",

   "package_version_id": "04txx0000004Idi",

   "managed_package_namespace": "Acme",

   "custom_entity": "/apex/Acme__Agent_List",

   "custom_entity_type": "VisualforcePage",

   "request_status": "S",

   "session_key": "2l4YtFB/RmsRKVsS",

   "login_key": "fGV6RgVOH3ZCgl2v",

   "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36

 (KHTML, like Gecko) Chrome/IP_ADDRESS_REMOVED Safari/537.36",

   "user_country_code": "US",

```


Second-Generation Managed Packages Package Usage Logs

```
         "user_time_zone": "America/Los_Angeles",

         "request_size": "826",

         "response_size": "1830"

      }

```

The Acme_Agent_List packaged component of type VisualforcePage was interacted with as a result of a user action from subscriber
org MyCustomer Inc on 2022-11-22 at 6:23 am.

The key data in this analysis are:

SEE ALSO:

Package Usage Logs Schema

[Visualforce Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.pages.meta/pages/pages_intro.htm)

##### CRM Analytics Asset Interactions

Each record in your package usage log that has a `custom_entity_type` of
`AnalyticsDashboard`, `AnalyticsLens`, or `AnalyticsRecipe` describes an
interaction with your packaged CRM Analytics assets.

Analytics Asset Runs

To analyze a run of your CRM Analytics asset, look for a `log_record_type` of
`AnalyticsAssetRun` .

Analytics Asset Views

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

To analyze a view of your CRM Analytics asset, look for a `log_record_type` of `AnalyticsAssetView` .


Second-Generation Managed Packages Package Usage Logs

Example: Let’s look at an example package usage log record and analyze the CRM Analytics asset interaction.

```
      {

         "timestamp_derived": "2022-11-22T06:19:49.820Z",

         "log_record_type": "AnalyticsAssetView",

         "request_id":"4mbhvyfahFf83tlq2Z5aAk",

         "organization_id": "00Dxx0000006H2l",

         "organization_name": "MyCustomer Inc.",

         "organization_status": "Demo",

         "organization_edition": "Enterprise Edition",

         "organization_country_code": "IN",

         "organization_language_locale": "en_US",

         "organization_time_zone": "Australia/Sydney",

         "organization_instance": "GS0",

         "organization_type": "Production",

         "user_id_token": "005-9BwnBWYO5FMn4cZ1sLw7F3LmTpoe8M77GrZOZHL6xQk=",

         "user_type": "Standard",

         "package_id": "033xx0000004FqD",

         "package_version_id": "04txx0000004Idi",

         "managed_package_namespace": "Acme",

         "custom_entity": "ClaimsDashboard",

         "custom_entity_type": "AnalyticsDashboard",

         "session_key": "2l4YtFB/RmsRKVsS",

         "login_key": "fGV6RgVOH3ZCgl2v",

        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36

      (KHTML, like Gecko) Chrome/IP_ADDRESS_REMOVED Safari/537.36",

         "user_country_code": "US",

         "user_time_zone": "America/Los_Angeles"

      }

```

The packaged Analytics dashboard, `ClaimsDashboard`, was interacted with by a standard user from the subscriber org
`MyCustom Inc.` Specifically, the user performed a view of `ClaimsDashboard` on 2022-11-22 at 6:19am UTC.

The key data in this analysis are:


Second-Generation Managed Packages Package Usage Logs

SEE ALSO:

Package Usage Logs Schema

[CRM Analytics Developer Center](https://developer.salesforce.com/developer-centers/crm-analytics)

##### Custom Interactions

To understand which features and UI components a subscriber interacted with and how they flow
through a user journey, create custom interactions with Apex enums and the
`IsvPartners.AppAnalytics.logCustomInteraction` Apex method.

Successful Custom Interactions

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

To analyze a custom interaction with your packaged components, look for a `log_record_type` of `CustomInteraction` and
a `custom_entity_type` of `CustomInteractionLabel` . The `custom_entity` contains a custom interaction label that
you created and that was logged.

Note: `interaction_id_token` is included only if an `interaction_id` was provided to the associated
`IsvPartners.AppAnalytics.logCustomInteraction` call. `interaction_id_token` is a hashed, tokenized
version of the raw interaction id that was provided.

Unsuccessful Custom Interactions

When `custom_entity_type` is equal to CustomInteractionFailure then the custom interaction couldn’t be logged. To determine
the reason for the failed logging, review the reason code provided by the `custom_entity` value.


Second-Generation Managed Packages Package Usage Logs

Example: Let’s look at an example package usage log record and analyze a successful Apex interaction.

```
      {

        "timestamp_derived": "2023-09-20T06:17:39.167Z",

        "log_record_type": "CustomInteraction",

        "request_id": "TID:7635077000004b3035",

        "organization_id": "00Dxx0000006H2l",

        "organization_name": "MyCustomer Inc.",

        "organization_status": "Demo",

        "organization_edition": "Enterprise Edition",

        "organization_country_code": "IN",

        "organization_language_locale": "en_US",

        "organization_time_zone": "Australia/Sydney",

        "organization_instance": "GS0",

        "organization_type": "Production",

        "user_id_token": "005-9BwnBWYO5FMn4cZ1sLw7F3LmTpoe8M77GrZOZHL6xQk=",

        "user_type": "Standard",

        "package_id": "033xx0000004FqD",

        "package_version_id": "04txx0000004Idi",

        "managed_package_namespace": "Acme",

        "custom_entity": "MyInteractionLabels.LoginButtonClicked",

        "custom_entity_type": "CustomInteractionLabel",

        "session_key": "2l4YtFB/RmsRKVsS",

        "login_key": "fGV6RgVOH3ZCgl2v",

        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36

      (KHTML, like Gecko) Chrome/IP_ADDRESS_REMOVED Safari/537.36",

        "user_country_code": "US",

        "user_time_zone": "America/Los_Angeles",

        "class_name": "Acme.MyController",

        "method_name": "loginButtonCallback",

        "line_number": 56,

        "interaction_id_token": "7NDe8HM8ZgPdBL+jiOpTW3/xKTwwL30dyxmKNxtyzi8="

      }

```

The `MyInteractionLabels.LoginButtonClicked` custom interaction label was logged as a custom interaction as
a result of a user action from subscriber org MyCustomer Inc on 2023-09-20 at 6:17 am. Specifically, the user interaction resulted
in logging a custom interaction from line number 56 of the `loginButtonCallback` method found in the


#### Second-Generation Managed Packages Package Usage Logs

`Acme.MyController` Apex class. In addition to the `InteractionLabels.LoginButtonClicked` label, an
interaction ID was provided to the log call resulting in an interaction token id value of
`7NDe8HM8ZgPdBL+jiOpTW3/xKTwwL30dyxmKNxtyzi8=` .

The key data in this analysis are:

SEE ALSO:

Download Package Usage Logs, Package Usage Summaries, and Subscriber Snapshots

Considerations for Custom Interactions

#### Package Usage Logs Schema

Make informed development decisions based on package usage log data. Analyze adoption, user behavior, company information, and
Lightning app and page usage data. Package usage logs list activity during a 24-hour period, between 12:00 AM and 11:59 PM UTC.


Second-Generation Managed Packages Package Usage Logs


Second-Generation Managed Packages Package Usage Logs


Second-Generation Managed Packages Package Usage Logs


Second-Generation Managed Packages Package Usage Logs


Second-Generation Managed Packages Package Usage Logs


Second-Generation Managed Packages Package Usage Logs


Second-Generation Managed Packages Package Usage Logs


### Second-Generation Managed Packages Subscriber Snapshots

### Subscriber Snapshots

Subscriber snapshots give you a point-in-time summary of subscriber activity. Use subscriber snapshots to see usage trends by org and
package.

[Note: AppExchange App Analytics is subject to certain usage restrictions, as described in the AppExchange Program Policies.](https://www.salesforce.com/content/dam/web/en_us/www/documents/legal/Agreements/alliance-agreements-and-terms/salesforce-partner-program-policies.pdf)

AppExchange App Analytics takes a daily snapshot of org, package, and custom entity data. Snapshots are captured daily at 00:00 UTC
and become available for download immediately. You request a date and time, or range of dates and times, and you receive one snapshot
per valid date and time requested. For example, if on April 7, 2023 you request a date and time range of
`StartTime=2023-04-04T00:00:00Z EndTime=2020-04-07T00:00:00Z`, you receive three snapshots, one for each
completed day.


Second-Generation Managed Packages Subscriber Snapshots


### Second-Generation Managed Packages Test Custom Integrations

The `attribute_name` and `attribute_value` fields are a `key-value` pair. Each pair has a specific scope. Some pairs provide
org-level metadata, and others provide custom entity, managed package, or package version metadata,

Interpret these two fields in tandem using the information in this table.

Note: As of Spring ’25, trial orgs aren’t included in subscriber snapshot MFA data.

### Test Custom Integrations

To test your custom integrations in a nonproduction environment, use AppExchange App Analytics
Simulation Mode. Submit an App Analytics query request and receive sample usage data.

Note: AppExchange App Analytics is subject to certain usage restrictions as described in the
[AppExchange Program Policies.](https://www.salesforce.com/content/dam/web/en_us/www/documents/legal/Agreements/alliance-agreements-and-terms/salesforce-partner-program-policies.pdf)

To receive sample usage data, enable simulation mode, then submit a query request that includes
a simulation mode package ID.

USER PERMISSIONS

To enable simulation mode:

**•** ModifyMetadata

**1.** [Enable simulation mode in your test org using the Metadata API AppAnalyticsSettings](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_appanalyticssettings.htm) `enableSimulationMode` org preference.

**2.** To simulate package usage log, usage summary, or subscriber snapshot downloads, complete the required fields in your SOAP API

[AppAnalyticsQueryRequest. Include](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_appanalyticsqueryrequest.htm) `DataType`, and leave `OrganizationIDs` blank. For `PackageIDs`, include at least
one simulation mode package ID that matches the scenario you’re testing.


### Second-Generation Managed Packages AppExchange App Analytics Developer Cookbook

**3.** Submit your query.

**4.** Check your API request.

**a.** If successful, retrieve the App Analytics Query Request object created in the API request. The `DownloadURL` field populates
when the request is completed.

**b.** If you get an error, edit your query. Use a smaller time window, such as a 14 days, or specify one org ID. Then resubmit your
query.

**5.** Download the comma-separated value (.csv) file containing sample usage data from the `DownloadURL` field in the App Analytics
Query Request object.

Important: When simulation mode is enabled, you can only access our sample usage data. Disable simulation mode to access
your production data.

### AppExchange App Analytics Developer Cookbook

Delve deeper into your AppExchange App Analytics managed package usage data by creating key
performance indicators (KPIs). First, complete some prerequisites and retrieve your App Analytics
data. Next, prepare your CRM Analytics environment. Finally, to build your KPIs, complete App
Analytics recipes.

Note: AppExchange App Analytics is subject to certain usage restrictions as described in the
[AppExchange Program Policies.](https://www.salesforce.com/content/dam/web/en_us/www/documents/legal/Agreements/alliance-agreements-and-terms/salesforce-partner-program-policies.pdf)

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

1. What Are Recipes?
The AppExchange App Analytics Developer Cookbook uses two distinct types of recipes: CRM
Analytics recipes and App Analytics recipes. The CRM Analytics recipes are foundational work
that you must complete before creating App Analytics recipes. App Analytics recipes build on your CRM Analytics recipe analytics
environment and result in key performance indicators (KPIs).

2. Before You Begin
Complete these prerequisites before you create App Analytics recipes.


Second-Generation Managed Packages AppExchange App Analytics Developer Cookbook

3. CRM Analytics Recipes
Set up your org to create AppExchange App Analytics recipes by building your CRM Analytics environment. You first create a
country-codes dataset. Then you create two CRM Analytics recipes to produce a dataset of your subscriber info, and an aggregate
dataset of all of your daily data.

4. App Analytics Recipes
To understand how your customers are using your managed packages and components, create App Analytics recipes. Each App
Analytics recipe produces a CRM Analytics lens and is a key performance indicator (KPI). Use CRM Analytics dashboards to visualize
your KPIs and gain deeper insights.

#### What Are Recipes?

The AppExchange App Analytics Developer Cookbook uses two distinct types of recipes: CRM
Analytics recipes and App Analytics recipes. The CRM Analytics recipes are foundational work that
you must complete before creating App Analytics recipes. App Analytics recipes build on your CRM
Analytics recipe analytics environment and result in key performance indicators (KPIs).

You can use any reporting tool to create KPIs, but we recommend our analytics powerhouse, CRM
Analytics. With CRM Analytics, you can easily integrate your License Management App (LMA) data
with your App Analytics data using datasets and CRM Analytics recipes.

CRM Analytics Recipes

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

If you’re familiar with CRM Analytics, you’re familiar with dataflows and CRM Analytics recipes. Dataflows are great for combining data
from multiple sources, while CRM Analytics recipes are great for performing transformations on a single dataset. To set up your App
Analytics recipe environment, create CRM Analytics recipes that combine a country code dataset, your LMA data, and your App Analytics
data. These CRM Analytics recipes are required to create App Analytics recipes.

App Analytics Recipes

App Analytics recipes are CRM Analytics lens formulas with SAQL code provided. Each App Analytics recipe results in a KPI that you can
use to visualize your data on a dashboard. Some examples include Daily and Monthly Active Users, and Custom Object Reads Per Day.
Complete your CRM Analytics recipes before starting with App Analytics recipes.


Second-Generation Managed Packages AppExchange App Analytics Developer Cookbook

#### Before You Begin

Complete these prerequisites before you create App Analytics recipes.

To brush up on your AppExchange App Analytics or CRM Analytics skills, we recommend completing
these Trailhead modules.

**•** [AppExchange Partner Intelligence Basics](https://trailhead.salesforce.com/en/content/learn/modules/appexchange-partner-intelligence-basics)

**•** [CRM Analytics Data Integration Basics](https://trailhead.salesforce.com/en/content/learn/modules/wave_enable_data_integration_basics)

**1.** [Set up your License Management Org (LMO).](https://developer.salesforce.com/docs/atlas.en-us.260.0.packagingGuide.meta/packagingGuide/package_associate_lmo.htm)

Use your LMO to track all Salesforce users who install your managed package. The LMO receives
a notification in the form of a lead record when a user installs or uninstalls your package. It also
tracks each package upload on AppExchange. Typically, as an AppExchange partner, you
[use your Partner Business Org (PBO) as your LMO.](https://developer.salesforce.com/docs/atlas.en-us.260.0.packagingGuide.meta/packagingGuide/isv1_3_quickstart.htm)

**2.** Register your security-reviewed managed package with your LMO. Follow the directions
[in Link a Package with Your License Management Organization.](https://developer.salesforce.com/docs/atlas.en-us.260.0.packagingGuide.meta/packagingGuide/package_associate_lmo.htm)

**3.** If you’re not using your PBO as your LMO, install the License Management App (LMA) in
your LMO. The LMA lets you manage leads and licenses for your AppExchange offerings.
[To install the LMA, read Get Started with the License Management App.](https://developer.salesforce.com/docs/atlas.en-us.260.0.packagingGuide.meta/packagingGuide/lma_setup.htm?search_text=license%20management%20app)

Note: If you’re using your PBO as your LMO, you’re all set. The LMA is automatically
installed for you.

**4.** Create an App Analytics Admin permission set that includes create and read access on
the AppAnalyticsQueryRequest object. Assign this permission to any non-Admin users
[so that they can create App Analytics requests. Read Create Permission Sets in Salesforce](https://help.salesforce.com/articleView?id=platform.perm_sets_create.htm&type=5&language=en_US)
Help if you need instructions.

**5.** [Set up the CLI using the Salesforce CLI Setup Guide. If you need a CLI refresher, take the](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_setup.meta/sfdx_setup/sfdx_setup_intro.htm)

[App Development with Salesforce DX Trailhead module.](https://trailhead.salesforce.com/en/content/learn/modules/sfdx_app_dev)

**6.** [Enable CRM Analytics in your Salesforce org.](https://help.salesforce.com/articleView?id=000335760&type=1&mode=1&language=en_US)

**7.** Create a CRM Analytics app named PartnerIntelligence.

To access License Management
App data, packages, and
package versions:

**•** Read on Licenses, Packages,
Package Versions

To request and retrieve
AppExchange App Analytics data:

**•** Create, Read, Edit, Delete,
View All, and Modify All on the
```
  AppAnalyticsQueryRequest
```

object

To use CRM Analytics:

**•** CRM Analytics Plus Admin
user

**8.** To request and retrieve a sample package usage log, create an AppExchange App Analytics query request using the CLI. Save the
CSV data file as `RawPackageLogFile.csv` .

**9.** To request and retrieve package usage logs automatically, create an automation. Which automation method you choose depends
on your business specifications and which data volume you’re automating.

**•** [For smaller datasets, such as package usage summaries, Apex scales well for automation. This GitHub repo has the details.](https://github.com/developerforce/partner-intelligence-basics)

**•** [For larger datasets, such as package usage logs, automate using an Amazon Web Services (AWS) stack.](https://medium.com/@kamipatel/automate-appanalytics-aws-stack-74cbebc49d2a)

**•** [You can also use the free Salesforce Labs app, App Analytics. It offers great functionality to retrieve and automate data collection](https://appexchange.salesforce.com/appxListingDetail?listingId=a0N3A00000G0nUXUAZ)
and to get started with recipes and dashboards. Salesforce Labs apps are developed by Salesforce employees and are unsupported.

Get Help with Prerequisites
If you need help with setting up your solution, you can request a consultation with a Platform Expert.


Second-Generation Managed Packages AppExchange App Analytics Developer Cookbook

##### Get Help with Prerequisites

If you need help with setting up your solution, you can request a consultation with a Platform Expert.

**1.** [Log in to the Salesforce Partner Community.](https://partners.salesforce.com)

**2.** Click the question icon and then click **Log a Case for Help** .

**3.** Provide any required details, and then click **Create Case** .

#### CRM Analytics Recipes

Set up your org to create AppExchange App Analytics recipes by building your CRM Analytics
environment. You first create a country-codes dataset. Then you create two CRM Analytics recipes
to produce a dataset of your subscriber info, and an aggregate dataset of all of your daily data.

**•** The first CRM Analytics recipe, LMAJoin, combines package and license data from your LMA
with your accounts and leads. It produces a dataset of your subscribers.

**•** The second CRM Analytics recipe, DailyAggregation, joins the LMAJoin dataset with your App
Analytics data. It produces the DailyAggregation dataset. All your App Analytics recipes are built
on top of your DailyAggregation dataset.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

1. Create the Country-Codes Dataset
To create visualizations of your country-based data in map format, you normalize the LMA country-code data to CRM Analytics
country-code format.

2. Connect to Your License Management App Data
Create an SFDC_Local connection to your License Management App (LMA) data.

3. Create the LMAJoin CRM Analytics Recipe
Create a CRM Analytics recipe that contains your License Management App (LMA) data.

4. Create Your App Analytics Dataset
Create a RawPackageLogFile App Analytics dataset using your `RawPackageLogFile.csv` file.

5. Create Your DailyAggregation CRM Analytics Recipe
You join your raw package log file data with your License Management App (LMA) data to create the DailyAggregation CRM Analytics
recipe. The recipe produces a dataset called DailyAggregation that you use to create App Analytics recipes.

SEE ALSO:

[Explore Data and Take Action with CRM Analytics](https://help.salesforce.com/articleView?id=analytics.bi.htm&type=5&language=en_US)


Second-Generation Managed Packages AppExchange App Analytics Developer Cookbook

##### Create the Country-Codes Dataset

To create visualizations of your country-based data in map format, you normalize the LMA
country-code data to CRM Analytics country-code format.

**1.** [Click country-codes.csv to download standardized country code data.](https://github.com/datasets/country-codes/blob/master/data/country-codes.csv)

**2.** Right-click **Raw** and click **Save Link As** .

**3.** Name the file `country-codes.txt`, and save it to your desktop.

##### 4. In Analytics Studio in CRM Analytics, click Create .

**5.** Click **Dataset** .

**6.** Click **CSV File** .

**7.** Select your `country-codes.txt` file.

**8.** Click **Next** .

**9.** Name your dataset _`country-codes`_ .

**10.** Select your **PartnerIntelligence** app.

**11.** Click **Next** .

**12.** Click **Upload File** .

##### Connect to Your License Management App Data

Create an SFDC_Local connection to your License Management App (LMA) data.

In your org in Analytics Studio in CRM Analytics:

**1.** Click **Data Manager** .

##### 2. Click Connect .

**3.** Click **Connect to Data** .

**4.** Click **SFDC_LOCAL** .

**5.** Click **Account** .

**6.** Click **Continue** .

**7.** Select all fields.

**8.** Click **Continue** .

**9.** Click **Save** .

**10.** Repeat steps 2 through 8 to connect to these objects.

**•** **Lead**

**•** **sfLma__License__c**

**•** **sfLma__Package__c**

**•** **sfLma__Package_Version__c**

**11.** Next to Account, click the down arrow.

**12.** Click **Run Data Sync** .

**13.** Repeat step 11 for these objects in your Connect window.

**•** **Lead**


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Second-Generation Managed Packages AppExchange App Analytics Developer Cookbook

**•** **sfLma__License__c**

**•** **sfLma__Package__c**

**•** **sfLma__Package_Version__c**

##### Create the LMAJoin CRM Analytics Recipe

Create a CRM Analytics recipe that contains your License Management App (LMA) data.

In your org in Analytics Studio in CRM Analytics:

**1.** Click **Data Manager** .

**2.** In Dataflows & Recipes on the Recipes tab, click **Create Recipe** .

**3.** Click **Add Input Data** .

**4.** Select **sfLma__License__c**, and select all columns.

**5.** Create a transform named _`License`_ with these specifications.

**•** Custom Formula: _`string(Id)`_

**•** Output Type: **Text**

**•** Length: _`255`_

**•** Default Value: _`blank`_

**•** Show Results In: **New Column (and Keep Original)**

**•** Column Label: _`LicenseRecordId`_

**6.** Add a join to Lead with these specifications.

**•** Select Input Data to Join: **Lead**

**•** Columns to Select: **Company**, **First Name**, **Id**, **Last Name**

**•** Join Type: **Lookup**

**•** Join Keys: **License: Record ID = Lead ID**

**•** API Name Prefix for Right Columns: _`Lead`_

**7.** Add a join to Account with these specifications.

**•** Select Input Data to Join: **Account**

**•** Columns to Select: **Name**

**•** Join Type: **Lookup**

**•** Join Keys: **Account Name = Account Name**

**•** API Name Prefix for Right Columns: _`Account`_

**8.** Add a join to sfLma__Package__c with these specifications.

**•** Select Input Data to Join: **sfLma__Package__c**

**•** Columns to Select: _`All fields`_

**•** Join Type: **Lookup**

**•** Join Keys: **Package = Record ID**

**•** API Name Prefix for Right Columns: _`Package`_

**9.** Create a transform between the join and `sfLma__Package__c` with these specifications.


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Second-Generation Managed Packages AppExchange App Analytics Developer Cookbook

**•** Custom Formula: _`substr(sfLma__Package_ID__c, 1, 15)`_

**•** Output Type: **Text**

**•** Length: _`255`_

**•** Default Value: none

**•** Show Results in: **New Column (and Keep Original)**

**•** Column Label: _`PackageID15`_

**10.** Create another join with these specifications.

**•** Select Input Data to Join: **sfLma__Package_Verzion__c**

**•** Columns to Select: _`All fields`_

**•** Join Type: **Lookup**

**•** Join Keys: **Package Version = Record ID**

**•** API Name Prefix for Right Columns: _`PackageVersion`_

**11.** Create an output with these specifications.

**•** Write To: **Dataset**

**•** Dataset Display Label: _`LMAJoin`_

**•** App Location: **PartnerIntelligence**

**•** Sharing Source: default

**•** Security Predicate: **Apply row-level security to the target dataset by adding a predicate filter condition**

**12.** Click **Apply** .

**13.** Click **Save** .

**14.** Save your recipe as _`LMAJoin`_ .

**15.** Click **Save and Run** .

**16.** To monitor the status of your job, click **Go to Data Monitor** .

Example: When complete, your LMAJoin CRM Analytics recipe looks like this.


Second-Generation Managed Packages AppExchange App Analytics Developer Cookbook

###### 1. Monitor Your LMAJoin CRM Analytics Recipe

CRM Analytics recipes can take a while to complete. Use these steps to monitor the status of your LMAJoin recipe.

###### 2. Run the LMAJoin CRM Analytics Recipe

To create a reusable dataset, schedule your LMAJoin CRM Analytics recipe to run on a regular basis. We recommend daily at midnight.

###### Monitor Your LMAJoin CRM Analytics Recipe

CRM Analytics recipes can take a while to complete. Use these steps to monitor the status of your
LMAJoin recipe.

In your org in Analytics Studio in CRM Analytics:

**1.** Click **Data Manager** .

###### 2. Click Monitor .

**3.** On the Jobs tab, locate your LMAJoin job.

**4.** When your job is Successful, click **Data** to view your completed LMAJoin dataset.

###### Run the LMAJoin CRM Analytics Recipe

To create a reusable dataset, schedule your LMAJoin CRM Analytics recipe to run on a regular basis.
We recommend daily at midnight.

In your org in Analytics Studio in CRM Analytics:

**1.** Click **Data Manager** .

**2.** Click **Dataflows & Recipes** .

**3.** Click the **Recipes** tab.

**4.** Next to your LMAJoin CRM Analytics recipe, click the arrow.

**5.** Click **Schedule**, and set up your schedule.

##### Create Your App Analytics Dataset

Create a RawPackageLogFile App Analytics dataset using your `RawPackageLogFile.csv`
file.

In your org in Analytics Studio in CRM Analytics:

##### 1. Click Create and select Dataset .

**2.** Click **CSV File** and select your `RawPackageLogFile.csv` file.

**3.** Click **Next** .

**4.** Name your dataset _`RawPackageLogFile`_ and select your **PartnerIntelligence** app.

**5.** Click **Next** .

EDITIONS

Available in: both **Salesforce**
**Classic** and **Lightning**
**Experience**

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

**6.** For **event_count**, **num_fields**, **num_soql_queries**, **operation_count**, and **rows_processed** fields, change the field type from
**Dimension** to **Measure** and add these specifications.

**•** Default value: _`0`_

**•** Scale: _`0`_

**•** Precision: _`18`_


Second-Generation Managed Packages AppExchange App Analytics Developer Cookbook

**7.** Search for **timestamp_derived** and make sure that its field type is **Date** .

**8.** Click **Upload File** .

##### Create Your DailyAggregation CRM Analytics Recipe

You join your raw package log file data with your License Management App (LMA) data to create
the DailyAggregation CRM Analytics recipe. The recipe produces a dataset called DailyAggregation
that you use to create App Analytics recipes.

In your org in Analytics Studio in CRM Analytics:

**1.** Click **Data Manager** .

**2.** Click **Dataflows & Recipes** .

**3.** On the Recipes tab, click **Create Recipe** .

**4.** Click **Add Input Data** .

**5.** Select **RawPackageLogFile** .

**6.** Select all the columns.

**7.** Create an aggregate with these specifications.

**Field** **Aggregate By**

```
  event_count Sum

  login_key Unique

  num_fields Sum

  num_soql_queries Sum

  operation_count Sum

  rows_processed Sum

  session_key Unique

```

**8.** In the aggregate, in Group Rows, click **+**, and select **timestamp_derived** .

**a.** Select **Year**, **Month**, and **Day** .

**b.** Click **Add** .

**9.** In the aggregate, in Group Rows, create a group for each of these fields.

**•** **api_type**

**•** **api_version**

**•** **app_name**

**•** **class_name**

**•** **cloned_from_organization**

**•** **custom_entity**

**•** **custom_entity_type**


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Second-Generation Managed Packages AppExchange App Analytics Developer Cookbook

**•** **entry_point**

**•** **event**

**•** **event_subscriber**

**•** **http_method**

**•** **http_status_code**

**•** **log_record_type**

**•** **managed_package_namespace**

**•** **method_name**

**•** **operation_type**

**•** **organization_country_code**

**10.** Create a transform named _`Create DMY Field`_ with this
formula. `to_date(concat(timestamp_derived_DAY,"/",timestamp_derived_MONTH,"/",timestamp_derived_YEAR),"dd/MM/yyyy"))`

**11.** Join your RawPackageLogFile dataset to your LMAData dataset using this information.

**•** Select Input Data to Join: **LMAData**

**•** Columns to Select: _`All fields`_

**•** Join Type: **Lookup**

**•** Join Keys: **organization_id = Subscriber Org ID** and **package_id = PackageID15**

**•** API Name Prefix for Right Columns: _`LMAData`_

**12.** Join your country-codes dataset to your LMAData dataset using this information.

**•** Select Input Data to Join: **country-codes**

**•** Columns to Select: _`All fields`_

**•** Join Type: **Lookup**

**•** Join Keys: **user_country_code = ISO3166-1-Alpha-2**

**•** API Name Prefix for Right Columns: _`UserCountry`_

**13.** Create a transform named _`Feature Name`_ .

**a.** Create as many CRM Analytics buckets as you need for your features, such as Inventory, Orders, and a catch-all bucket called
Other.

**b.** Note: A CRM Analytics bucket represents a category that you use to group your data. For example, say your app contains
multiple features, such as an inventory tracking feature and an order processing feature. Create a CRM Analytics bucket
for each feature. Each bucket contains the custom objects, pages, Lightning components, and Apex classes that pertain
to that feature. You can use these buckets to create Feature Adoption App Analytics recipes

Add your custom entities to the appropriate bucket.

**14.** Select **Output** and use these settings.

**•** Write To: **Dataset**

**•** Dataset Display Label: _`DailyAggregation`_

**•** App Location: **PartnerIntelligence**

**•** Sharing Source: default

**•** Security Predicate: **Apply row-level security to the target dataset by adding a predicate filter condition**

**•** Name: _`Create Daily Aggregation Dataset`_


Second-Generation Managed Packages AppExchange App Analytics Developer Cookbook

**15.** Click **Apply** .

**16.** Click **Save** .

**17.** Name your recipe _`DailyAggregation`_ .

**18.** Click **Save and Run** .

Example: When complete, your DailyAggregation recipe looks like this.

###### 1. Monitor the DailyAggregation CRM Analytics Recipe

CRM Analytics recipes can take a while to complete. Use these steps to monitor the status of your DailyAggregation recipe.

###### 2. Run the DailyAggregation CRM Analytics Recipe

To create a reusable dataset, schedule your DailyAggregation CRM Analytics recipe to run on a regular basis. We recommend daily
at midnight.

###### Monitor the DailyAggregation CRM Analytics Recipe

CRM Analytics recipes can take a while to complete. Use these steps to monitor the status of your
DailyAggregation recipe.

In your org in Analytics Studio in CRM Analytics:

**1.** Click **Data Manager** .

###### 2. Click Monitor .

**3.** On the Jobs tab, locate your DailyAggregation job.

**4.** When your job is Successful, click **Data** to view your completed DailyAggregation dataset.

###### Run the DailyAggregation CRM Analytics Recipe

To create a reusable dataset, schedule your DailyAggregation CRM Analytics recipe to run on a
regular basis. We recommend daily at midnight.

In your org in Analytics Studio in CRM Analytics:

**1.** Click **Data Manager** .

**2.** Click **Dataflows & Recipes** .

**3.** Click the **Recipes** tab.

**4.** Next to your DailyAggregation CRM Analytics recipe, click the arrow.


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Second-Generation Managed Packages AppExchange App Analytics Developer Cookbook

**5.** Click **Schedule**, and set up your schedule.

#### App Analytics Recipes

To understand how your customers are using your managed packages and components, create
App Analytics recipes. Each App Analytics recipe produces a CRM Analytics lens and is a key
performance indicator (KPI). Use CRM Analytics dashboards to visualize your KPIs and gain deeper
insights.

Note: AppExchange App Analytics is subject to certain usage restrictions as described in the
[AppExchange Program Policies. To request and retrieve package usage logs and subscriber](https://www.salesforce.com/content/dam/web/en_us/www/documents/legal/Agreements/alliance-agreements-and-terms/salesforce-partner-program-policies.pdf)
snapshots, activate App Analytics on your security-reviewed managed package by logging
[a support case in the Salesforce Partner Community. For product, specify](https://partners.salesforce.com/) **Partner Programs**
**& Benefits** . For topic, specify **ISV Technology Request** . You can access package usage
summaries without activation.

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

For example, to analyze a wide range of daily and monthly package usage metrics, build Daily and Monthly Active User App Analytics
recipes.

Example:

Customer Success Recipes
Customer success is a relationship-focused method of ensuring that your customers achieve their desired outcomes while using
your managed packages.

Custom Object Usage Recipes
Understanding how your customers use your custom objects is critical to managing the lifecycle of your managed package and its
custom objects. Start by measuring custom object usage by create, read, update, and delete (CRUD) operations.


Second-Generation Managed Packages AppExchange App Analytics Developer Cookbook

##### Customer Success Recipes

Customer success is a relationship-focused method of ensuring that your customers achieve their
desired outcomes while using your managed packages.

To measure customer success, you can create metrics that help you understand:

**•** Overall managed package usage

**•** Depth of managed package usage

**•** Growth

**•** Length of time as a customer

**•** Number of renewals

**•** Number of upsells

**•** Overall relationship

EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

As you learn more about your customers and how they use your managed packages, your list of customer success metrics expands.

To analyze user behavior, we rely on user-related and CRUD (create, read, update, and delete) App Analytics data fields to calculate
metrics. All user behavior calculations rely on how a unique user is defined.

**•** An individual that has used your managed package and its components

**•** Measured for a specified time period, such as a day, month, or year

An active user can be defined as: A user who has logged some type of package usage, such as CRUD activity, page views, or Lightning
interactions, during a specified time period.

Segment the unique and active users by time period, such as day, month, or quarter.

###### Create a Daily Unique Users Recipe

This recipe produces a unique count of users by day.

Create a Weekly Unique Users Recipe
This recipe produces a unique count of users by week.

Create a Monthly Unique Users Recipe
This recipe produces a unique count of users by month.

###### Create a Daily Unique Users Recipe

This recipe produces a unique count of users by day.

In your org in Analytics Studio in CRM Analytics:

**1.** In All items on the Datasets tab, select your DailyAggregation dataset.

**2.** Under Bar Length, click **Count of Rows** .

**3.** Click **Unique** .

**4.** Select **user_id_token** .

**5.** Select **Charts** .

**6.** Click **Column** .

**7.** Under Bars, click **+** and search for _`timestamp_DMY`_ .

**8.** Select **Year-Month-Day** .

**9.** Click **Save** .


Second-Generation Managed Packages AppExchange App Analytics Developer Cookbook

**10.** Name your lens _`Daily Unique Users`_ .

**11.** Select your PartnerIntelligence app.

**12.** Click **Save** .

Example:

SAQL:

```
      q = load "DailyAggregation";

      q = group q by ('timestamp_derived_DAY_formula_Year',

      'timestamp_derived_DAY_formula_Month', 'timestamp_derived_DAY_formula_Day');

      q = foreach q generate 'timestamp_derived_DAY_formula_Year' + "~~~" +

      'timestamp_derived_DAY_formula_Month' + "~~~" + 'timestamp_derived_DAY_formula_Day'

      as

      'timestamp_derived_DAY_formula_Year~~~timestamp_derived_DAY_formula_Month~~~timestamp_derived_DAY_formula_Day',

      unique('user_id_token') as 'unique_user_id_token';

      q = order q by

      'timestamp_derived_DAY_formula_Year~~~timestamp_derived_DAY_formula_Month~~~timestamp_derived_DAY_formula_Day'

      asc;

      q = limit q 2000;

###### Create a Weekly Unique Users Recipe

```

This recipe produces a unique count of users by week.

In your org in Analytics Studio in CRM Analytics:

**1.** In All items on the Datasets tab, select your DailyAggregation dataset.

**2.** Under Bar Length, click **Count of Rows** .

**3.** Click **Unique** .


Second-Generation Managed Packages AppExchange App Analytics Developer Cookbook

**4.** Select **user_id_token** .

**5.** Select **Charts** .

**6.** Click **Column** .

**7.** Under Bars, click **+** and search for _`timestamp_DMY`_ .

**8.** Select **Year-Week** .

**9.** Click **Save** .

**10.** Name your lens _`Weekly Unique Users`_ .

**11.** Select your PartnerIntelligence app.

**12.** Click **Save** .

Example:

SAQL:

```
      q = load "DailyAggregation";

      q = group q by ('timestamp_derived_DAY_formula_Year',

      'timestamp_derived_DAY_formula_Week');

      q = foreach q generate 'timestamp_derived_DAY_formula_Year' + "~~~" +

      'timestamp_derived_DAY_formula_Week' as

      'timestamp_derived_DAY_formula_Year~~~timestamp_derived_DAY_formula_Week',

      unique('user_id_token') as 'unique_user_id_token';

      q = order q by 'timestamp_derived_DAY_formula_Year~~~timestamp_derived_DAY_formula_Week'

      asc;

      q = limit q 2000;

###### Create a Monthly Unique Users Recipe

```

This recipe produces a unique count of users by month.

In your org in Analytics Studio in CRM Analytics:

**1.** In All items on the Datasets tab, select your DailyAggregation dataset.


Second-Generation Managed Packages AppExchange App Analytics Developer Cookbook

**2.** Under Bar Length, click **Count of Rows** .

**3.** Click **Unique** .

**4.** Select **user_id_token** .

**5.** Select **Charts** .

**6.** Click **Column** .

**7.** Under Bars, click **+** and search for **timestamp_DMY** .

**8.** Select **Year-Month** .

**9.** Click **Save** .

**10.** Name your lens _`Monthly Unique Users`_ .

**11.** Select your PartnerIntelligence app.

**12.** Click Save.

Example:

SAQL:

```
      q = load "DailyAggregation";

      q = group q by ('timestamp_derived_DAY_formula_Year',

      'timestamp_derived_DAY_formula_Month');

      q = foreach q generate 'timestamp_derived_DAY_formula_Year' + "~~~" +

      'timestamp_derived_DAY_formula_Month' as

      'timestamp_derived_DAY_formula_Year~~~timestamp_derived_DAY_formula_Month',

      unique('user_id_token') as 'unique_user_id_token';

      q = order q by 'timestamp_derived_DAY_formula_Year~~~timestamp_derived_DAY_formula_Month'

      asc;

      q = limit q 2000;

```


Second-Generation Managed Packages AppExchange App Analytics Developer Cookbook

##### Custom Object Usage Recipes

Understanding how your customers use your custom objects is critical to managing the lifecycle
of your managed package and its custom objects. Start by measuring custom object usage by
create, read, update, and delete (CRUD) operations.

###### Create a Custom Object Creates Per Day Recipe

This recipe produces a unique count of how many times per day a custom object was created.

Create a Custom Object Updates Per Day Recipe
This recipe produces a unique count of how many times per day a custom object was created.

Create a Custom Object Reads Per Day Recipe
This recipe produces a unique count of how many times per day a custom object was read.

###### Create a Custom Object Creates Per Day Recipe

This recipe produces a unique count of how many times per day a custom object was created.

In your org in Analytics Studio in CRM Analytics:

**1.** In All items on the Datasets tab, select your DailyAggregation dataset.

**2.** Select **Charts** .

**3.** Click **Column** and leave Bar Length as **Count of Rows** .

**4.** Under Bars, click **+** and search for **timestamp_DMY** .

**5.** Select **Year-Month-Day** .

**6.** Click **Filters** .

**7.** Click **+** .

**8.** Select **custom_entity_type** equals **CustomObject** .

**9.** Click **Apply** .

**10.** Click **+** .

**11.** Select **operation_type** Equals **INSERT** .

**12.** Click **Apply** .

**13.** Click **Data** .

**14.** Under Trellis, click **+** .

**15.** Select **custom_entity** .

**16.** Click **Save** .

**17.** Name your lens _`Custom Object Creates Per Day`_ .

**18.** Select your PartnerIntelligence app.

**19.** Click **Save** .


EDITIONS

Available in: both Salesforce
Classic and Lightning
Experience

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Second-Generation Managed Packages AppExchange App Analytics Developer Cookbook

Example:

SAQL:

```
      q = load "DailyAggregation";

      q = filter q by 'custom_entity_type' == "CustomObject";

      q = filter q by 'operation_type' == "INSERT";

      q = group q by ('timestamp_derived_DAY_formula_Year',

      'timestamp_derived_DAY_formula_Month', 'timestamp_derived_DAY_formula_Day',

      'custom_entity');

      q = foreach q generate 'timestamp_derived_DAY_formula_Year' + "~~~" +

      'timestamp_derived_DAY_formula_Month' + "~~~" + 'timestamp_derived_DAY_formula_Day'

      as

      'timestamp_derived_DAY_formula_Year~~~timestamp_derived_DAY_formula_Month~~~timestamp_derived_DAY_formula_Day',

      'custom_entity' as 'custom_entity', count() as 'count';

      q = order q by

      ('timestamp_derived_DAY_formula_Year~~~timestamp_derived_DAY_formula_Month~~~timestamp_derived_DAY_formula_Day'

      asc, 'custom_entity' asc);

      q = limit q 2000;

###### Create a Custom Object Updates Per Day Recipe

```

This recipe produces a unique count of how many times per day a custom object was created.

In your org in Analytics Studio in CRM Analytics:

**1.** In All items on the Datasets tab, select your DailyAggregation dataset.

**2.** Select **Charts** .

**3.** Click **Column** and leave Bar Length as **Count of Rows** .

**4.** Under Bars, click **+** and select **timestamp_DMY** .

**5.** Select **Year-Month-Day** .

**6.** Click the **Filters** tab.

**7.** Click **+** .

**8.** Select **custom_entity_type** Equals **CustomObject**

**9.** Click **Apply** .

**10.** Click **+** .


Second-Generation Managed Packages AppExchange App Analytics Developer Cookbook

**11.** Select **operation_type** Equals **UPDATE** .

**12.** Click **Apply** .

**13.** Click the **Data** tab.

**14.** Under Trellis, click **+** .

**15.** Select **custom_entity** .

**16.** Click **Save** .

**17.** Name your lens _`Custom Object Creates Per Day`_ .

**18.** Select your PartnerIntelligence app.

**19.** Click **Save** .

Example:

SAQL:

```
      q = load "DailyAggregation";

      q = filter q by 'custom_entity_type' == "CustomObject";

      q = filter q by 'operation_type' == "UPDATE";

      q = group q by ('timestamp_derived_DAY_formula_Year',

      'timestamp_derived_DAY_formula_Month', 'timestamp_derived_DAY_formula_Day',

      'custom_entity');

      q = foreach q generate 'timestamp_derived_DAY_formula_Year' + "~~~" +

      'timestamp_derived_DAY_formula_Month' + "~~~" + 'timestamp_derived_DAY_formula_Day'

      as

      'timestamp_derived_DAY_formula_Year~~~timestamp_derived_DAY_formula_Month~~~timestamp_derived_DAY_formula_Day',

      'custom_entity' as 'custom_entity', count() as 'count';

      q = order q by

      ('timestamp_derived_DAY_formula_Year~~~timestamp_derived_DAY_formula_Month~~~timestamp_derived_DAY_formula_Day'

```


Second-Generation Managed Packages AppExchange App Analytics Developer Cookbook

```
      asc, 'custom_entity' asc);

      q = limit q 2000;

###### Create a Custom Object Reads Per Day Recipe

```

This recipe produces a unique count of how many times per day a custom object was read.

In your org in Analytics Studio in CRM Analytics:

**1.** In All items on the Datasets tab, select your DailyAggregation dataset.

**2.** Select **Charts** .

**3.** Click **Column** and leave Bar Length as **Count of Rows** .

**4.** Under Bars, click **+** and search for **timestamp_DMY** .

**5.** Select **Year-Month-Day** .

**6.** Click **Filters** .

**7.** Click **+** .

**8.** Select **custom_entity_type** Equals **CustomObject**

**9.** Click **Apply** .

**10.** Click **+** .

**11.** Select **operation_type** Equals **READ** .

**12.** Click **Apply** .

**13.** Click **Data** .

**14.** Under Trellis, click **+** .

**15.** Select **custom_entity** .

**16.** Click **Save** .

**17.** Name your lens _`Custom Object Reads Per Day`_ .

**18.** Select your PartnerIntelligence app.

**19.** Click **Save** .

Example:


## Second-Generation Managed Packages Gaps Between First-Generation and Second-Generation

Managed Packaging

SAQL:

```
      q = load "DailyAggregation";

      q = filter q by 'custom_entity_type' == "CustomObject";

      q = filter q by 'operation_type' == "READ";

      q = group q by ('timestamp_derived_DAY_formula_Year',

      'timestamp_derived_DAY_formula_Month', 'timestamp_derived_DAY_formula_Day',

      'custom_entity');

      q = foreach q generate 'timestamp_derived_DAY_formula_Year' + "~~~" +

      'timestamp_derived_DAY_formula_Month' + "~~~" + 'timestamp_derived_DAY_formula_Day'

      as

      'timestamp_derived_DAY_formula_Year~~~timestamp_derived_DAY_formula_Month~~~timestamp_derived_DAY_formula_Day',

      'custom_entity' as 'custom_entity', count() as 'count';

      q = order q by

      ('timestamp_derived_DAY_formula_Year~~~timestamp_derived_DAY_formula_Month~~~timestamp_derived_DAY_formula_Day'

      asc, 'custom_entity' asc);

      q = limit q 2000;

## Gaps Between First-Generation and Second-Generation Managed
```

Packaging

The following functionality is supported in first-generation managed packaging, and not yet supported in second-generation managed
packaging. We’re working to address these feature gaps.

**•** Package versions can’t be deprecated.

**•** [Apex VersionProvider isn’t supported.](https://help.salesforce.com/articleView?id=code_version_settings_apex.htm&language=en_US)

**•** A default language for labels in packages can’t be specified.

[See the Metadata Coverage Report, for the latest information on supported metadata types.](https://developer.salesforce.com/docs/metadata-coverage)

