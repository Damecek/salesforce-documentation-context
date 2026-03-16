are reflected in the subscriber’s org upon install. In managed packages, a subscriber can’t disassociate workflow actions from a
workflow rule if it was associated by the developer.

**•** On install, all workflow rules newly created in the installed or upgraded package, have the same activation status as in the uploaded
package.

**•** You can't package workflow rules with time triggers.

### Workflow Task

This metadata type references an assigned workflow task.

Component Manageability Rules

Note: When creating a new package or package version, use the Flow component instead of Workflow components. If your
managed package already includes Workflow components, come up with a plan to migrate to use Flow.

Manageability rules determine whether you, or the subscriber, can edit or remove components after the package version is created and
promoted to the released state.


## Second-Generation Managed Packages Behavior of Specific Metadata in Second-Generation

Managed Packages

Packageable In: Second-Generation Managed Packages (2GP), First-Generation
Managed Packages (1GP)

Component Is Updated During Package Upgrade Yes

Subscriber Can Delete Component From Org No

Package Developer Can Remove Component From Package Yes. Supported in both 1GP and 2GP packages. Both protected
and non-protected components can be removed.

Component Has IP Protection No

Editable Properties After Package Promotion or Installation

Only Package Developer Can Edit

**•** None

Both Package Developer and Subscriber Can Edit

**•** Assign To

**•** Comments

**•** Due Date

**•** Priority

**•** Record Type

**•** Status

Neither Package Developer or Subscriber Can Edit

**•** Subject

More Information

**Feature Name**
Metadata Name: Workflow

Component Type in 1GP Package Manager UI: Workflow Task

**•** Salesforce prevents you from uploading workflow tasks that are assigned to a role. Change the `Assigned To` field to a user
before uploading your app. During installation, Salesforce replaces that user with the user installing the app, and the installer can
customize it as necessary.

**•** [This component can be marked as protected. For more details, see Protected Components in the](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/packaging_protected_components.htm) _First-Generation Managed Packaging_
_Developer Guide_ .

## Behavior of Specific Metadata in Second-Generation Managed

Packages

Learn how profiles and namespace visibility are handled for second-generation managed packages.

Package Agentforce Metadata Components
Bring the power of conversational AI to your apps with Agentforce.


Second-Generation Managed Packages Behavior of Specific Metadata in Second-Generation
Managed Packages

Develop and Package Agent Templates Using Scratch Orgs
At a high-level, agents are distributed by ISVs as agent templates. To package an agent template you first create and test an agent
in a namespaced scratch org, retrieve the agent to your Salesforce DX project, generate an agent template from the agent using
Salesforce CLI, and finally package the agent template.

Package Data Cloud Metadata Components
Utilize the power of Data Cloud in your apps by including Data Cloud metadata in your managed packages. Working with Data Cloud
metadata has some unique requirements. Review these details to understand how to work with Data Cloud metadata in your
packages.

Protected Components in Managed Packages
Developers can mark certain components as _protected_ . Protected components can’t be linked to or referenced by components
created in a subscriber org. A developer can delete a protected component in a future release without worrying about failing
installations. However, after a component is marked as unprotected and is released globally, the developer can’t delete it.

Set Up a Platform Cache Partition with Provider Free Capacity
Salesforce provides 3 MB of free Platform Cache capacity for security-reviewed managed packages. This is made available through
a capacity type called Provider Free capacity and is automatically enabled in all Developer edition orgs.

Metadata Access in Apex Code
Use the `Metadata` namespace in Apex to access metadata in your package.

Permission Sets and Profile Settings in Packages
Permission sets, permission set groups, and profile settings are all ways to grant permissions and other access settings to a package.
Only use a profile setting if permission sets don’t support the specific access you need to grant. In all other instances, use permission
sets or permission set groups.

Protecting Your Intellectual Property
The details of your custom objects, custom links, reports, and other installed items are revealed to installers so that they can check
for malicious content. However, revealing an app’s components prevents developers from protecting some intellectual property.

Call Salesforce URLs Within a Package
The URLs that Salesforce serves for a target org vary based on the org type and configuration. To build packages that support all
possible URL formats, use relative URLs whenever possible. If your package functionality requires a full URL, use the Apex
`DomainCreator` class to get the corresponding hostname. This method allows your package to work in all orgs, regardless of
the org type and My Domain settings.

Namespace-Based Visibility for Apex Classes in Second-Generation Managed Packages
The `@NamespaceAccessible` makes public Apex in a package available to other packages that use the same namespace.
Without this annotation, Apex classes, methods, interfaces, and properties defined in a second-generation managed package aren’t
accessible to the other packages with which they share a namespace. Apex that is declared global is always available across all
namespaces, and needs no annotation.

Work with Services Outside of Salesforce

Package Connected Apps in Second-Generation Managed Packaging
Add a connected app to a second-generation managed package.

Test and Respond to the New Order Save Behavior
To make sure custom application logic works accurately on records associated with the Order object, turn on the Enable New Order
Save Behavior setting, and test the behavior. We recommend that you support both the new and old order save behavior during
testing.


### Second-Generation Managed Packages Package Agentforce Metadata Components Package Agentforce Metadata Components

Bring the power of conversational AI to your apps with Agentforce.

Before you add Agentforce metadata to your package:

**•** [Review the setup steps in Get Access to Scratch Orgs That Have Agentforce.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/dev2gp_scratch_orgs_agentforce.htm)

**•** [Create your agent’s actions and topics in the Agentforce Asset Library. See Create a Custom Agent Action and Create a Custom Topic](https://help.salesforce.com/s/articleView?id=ai.copilot_actions_custom.htm&language=en_US)
for instructions. Any agent action or topic that will be packaged must be in the Agentforce Asset Library.

**Table 2: Packageable Agentforce Metadata**

SEE ALSO:

[Get Access to Scratch Orgs That Have Agentforce](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/dev2gp_scratch_orgs_agentforce.htm)

_Salesforce Help_ [: Considerations for Packaging Prompt Templates](https://help.salesforce.com/s/articleView?id=ai.prompt_builder_considerations_packaging.htm&language=en_US)

_Trailhead_ [: Quick Start: Build Your First Agent with Agentforce](https://trailhead.salesforce.com/content/learn/projects/quick-start-build-your-first-agent-with-agentforce)

_Salesforce Help_ [: Agentforce: Agents](https://help.salesforce.com/s/articleView?id=ai.copilot_intro.htm&type=5&language=en_US)

_[Agentforce Developer Guide](https://developer.salesforce.com/docs/einstein/genai/guide/get-started.html)_

_Salesforce Help_ [: The Building Blocks of Agents](https://help.salesforce.com/s/articleView?id=ai.copilot_building_blocks.htm&type=5&language=en_US)

_Salesforce Help_ [: Customize Your Agents with Topics and Actions](https://help.salesforce.com/s/articleView?id=ai.copilot_topics_actions.htm&type=5&language=en_US)

_Salesforce Help_ [: Considerations for Agents](https://help.salesforce.com/s/articleView?id=ai.copilot_considerations.htm&type=5&language=en_US)

_Salesforce Help_ [: AI Project Success](https://help.salesforce.com/s/articleView?id=ai.generative_ai_plan_project.htm&type=5&language=en_US)

### Develop and Package Agent Templates Using Scratch Orgs

At a high-level, agents are distributed by ISVs as agent templates. To package an agent template you first create and test an agent in a
namespaced scratch org, retrieve the agent to your Salesforce DX project, generate an agent template from the agent using Salesforce
CLI, and finally package the agent template.

[Important: If you’re packaging an agent template in October 2025 or later, follow the workaround instructions for packaging](https://help.salesforce.com/s/issue?id=a02Ka00000ji2nu)
[agent templates. Due to a known issue with packaging local actions and topics, you must package agent templates using the](https://help.salesforce.com/s/issue?id=a02Ka00000ji2nu)
workaround instructions at this time.

Workflow for Agent Template Development


Second-Generation Managed Packages Develop and Package Agent Templates Using Scratch Orgs

Agent and Agent Template Metadata

To package an agent template it helps to first understand the metadata types that make up an agent and an agent template.

Agents are defined by these major metadata types.

**•** Bot

**•** BotVersion

**•** GenAiPlannerBundle

The GenAiPlannerBundle type in turn defines the agent's topics and actions. The `agent generate template` Salesforce CLI
command brings together the metadata files for these three types and generates a BotTemplate file for a specific agent (Bot and
BotVersion). You then use the BotTemplate file, and the GenAiPlannerBundle file, to package the agent template in a managed package.


Second-Generation Managed Packages Develop and Package Agent Templates Using Scratch Orgs

Create an Agent

Create and test your agent.

From Setup in your scratch org, enter _`Agents`_ in the Quick Find box, and select **Agentforce Agents** . Then locate and enable the
**Agentforce** setting and refresh the page.

**1.** Click **New Agent**, and then select an agent type.

**2.** Follow the guided setup steps, and then click **Create** .

[For more guidance, see the documentation for the agent type you chose. For details about creating an agent, see Set Up Your Agent.](https://help.salesforce.com/s/articleView?id=ai.agent_setup_explore_types.htm&language=en_US)

[Agentforce-enabled scratch orgs have access to the Agentforce Testing Center. For more detailed information on testing your agents](https://help.salesforce.com/s/articleView?id=ai.agent_testing_center.htm&language=en_US)
[directly in your DX project, see Test an Agent with Agentforce DX in the](https://developer.salesforce.com/docs/einstein/genai/guide/agent-dx-test.html) _Agentforce Developer Guide_ .

Set Up Your Salesforce DX Project and Scratch Org

To set up a Salesforce DX project and scratch org, you must already have a namespace and scratch org ready to use.

[For guidance on obtaining a namespace or an Agentforce-enabled scratch org, see Get Access to Scratch Orgs with Agentforce Enabled.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/dev2gp_scratch_orgs_agentforce.htm)

[Note: To package BotTemplate metadata, you must first enable Einstein Chatbot in your Dev Hub org. You must also specify this](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_dev.meta/sfdx_dev/sfdx_setup_enable_einstein.htm)
metadata in your `project-scratch-def.json` file.


Second-Generation Managed Packages Develop and Package Agent Templates Using Scratch Orgs

**1.** If you’re using an existing Salesforce DX project that contains Apex classes, flows, or prompt templates for your agent, deploy them
to the scratch org.

```
     sf project deploy start --source-dir force-app --target-org MyNamespacedScratchOrg

```

**2.** Open the scratch org.

```
     sf org open

```

Develop Your Agentforce Package

After you have built and tested your agent, you are ready to start packaging it.

**1.** Retrieve the relevant metadata into your Salesforce DX project.

```
     sf project retrieve start --metadata Agent:My_Awesome_Agent –-target-org

     MyNamespacedScratchOrg

```

**2.** Create an agent template metadata source file.

In this example, we are generating an agent template from a Bot metadata file in your DX project that corresponds to the
`My_Awesome_Agent` agent. A single Bot can have multiple BotVersions. Use the `--agent-version` flag to specify the
version.

```
     sf agent generate template --agent-file

     force-app/main/default/bots/My_Awesome_Agent/My_Awesome_Agent.bot-meta.xml --agent-version

      1

```

For more details on the `agent generate template` [command, see the Salesforce CLI Reference Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_agent_commands_unified.htm#cli_reference_agent_generate_template_unified)

**3.** Deploy the agent template metadata source file to your scratch org.

```
     sf project deploy start --source-dir force-app --target-org MyNamespacedScratchOrg

```

**4.** When you're satisfied with your agent template, remove the following metadata from your package directory.

**a.** The GenAiPlannerBundle file that was part of your original agent. This file was used to create a new, separate GenAiPlannerBundle
file for your agent template and is not necessary to package. Remove the GenAiPlannerBundle file that does not have “Template”
in the name.

**b.** The Bot and BotVersion. Removing these metadata types prevents errors during packaging, since agents aren’t packageable.

Note: To package prompt templates, you must assign permissions in the `sfdx-project.json` [file. See Packaging](https://help.salesforce.com/s/articleView?id=ai.prompt_builder_considerations_packaging.htm&type=5&language=en_US)
[Considerations for Prompt Templates.](https://help.salesforce.com/s/articleView?id=ai.prompt_builder_considerations_packaging.htm&type=5&language=en_US)

**5.** [After you’ve tested your agent, create a new package version that contains the template and all dependencies. Possible dependencies](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_create_pkg_ver.htm)
include: topics, actions, Apex classes, flows, and prompt templates.

```
     sf package version create --package "Agentforce App" --installation-key “HIF83kS8kS7C”

      --definition-file config/project-scratch-def.json --code-coverage --wait 10

```

After a subscriber installs your package in their Agentforce-enabled org, they can use the Agentforce UI to create an agent from your
template.


### Second-Generation Managed Packages Package Data Cloud Metadata Components

SEE ALSO:

[Get Access to Scratch Orgs That Have Agentforce](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/dev2gp_scratch_orgs_agentforce.htm)

[Package Agentforce Metadata Components](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/dev2gp_packageable_agentforce_md.htm)

_Salesforce Help_ [: Agentforce: Agents](https://help.salesforce.com/s/articleView?id=ai.copilot_intro.htm&type=5&language=en_US)

_[Agentforce Developer Guide](https://developer.salesforce.com/docs/einstein/genai/guide/get-started.html)_

_Salesforce Help_ [: The Building Blocks of Agents](https://help.salesforce.com/s/articleView?id=ai.copilot_building_blocks.htm&type=5&language=en_US)

### Package Data Cloud Metadata Components

Utilize the power of Data Cloud in your apps by including Data Cloud metadata in your managed packages. Working with Data Cloud
metadata has some unique requirements. Review these details to understand how to work with Data Cloud metadata in your packages.

Enable Data Cloud for Scratch Orgs

To create scratch orgs or package Data Cloud components, you must have Dev Hub enabled in your Partner Business Org. Then, you
[can request that Data Cloud for Scratch Orgs be enabled by logging a case with Salesforce Partner Support. Data Cloud for Scratch Orgs](https://partners.salesforce.com)
is only available to scratch orgs associated with the Dev Hub in your Partner Business Org.

Create Dedicated Data Cloud Packages

When creating a managed package with Data Cloud metadata, you must isolate the Data Cloud metadata from the other Salesforce
metadata by creating separate packages that contain only Data Cloud metadata. Then create package dependencies between your
dedicated Data Cloud package and any related packages.

Add Data Cloud Metadata to a Data Kit

When packaging Data Cloud metadata, you must add the metadata to a data kit, and then add the data kit to the managed package.
[Data kits streamline the package creation and installation process. For more details, see Packages and Data Kits in the](https://developer.salesforce.com/docs/platform/data-cloud-dev/guide/packages-data-kits.html) _Data Cloud Developer_
_Guide_ .


### Second-Generation Managed Packages Protected Components in Managed Packages

Data Cloud One Companion Connected Orgs

Packages can’t be installed on orgs that are connected to Data Cloud as Data Cloud One companion orgs. When Data Cloud customers
install a managed package containing Data Cloud metadata, they must install the package in their Data Cloud home org. For customers
using Data Cloud One, any package installed into data spaces shared with a companion org are automatically installed into the companion
org. Companion orgs automatically receive package updates when the package in the home org is upgraded.

These package-related actions can’t be initiated in companion connected orgs, and must instead be initiated in the Data Cloud One
home org.

**•** Installing a managed package

**•** Uninstalling a managed package

**•** Deleting package metadata

**•** Receiving a package push upgrade

SEE ALSO:

_Data Cloud Developer Guide_ [: Get Started with Data Cloud Development](https://developer.salesforce.com/docs/platform/data-cloud-dev/guide/get-started.html)

_Data Cloud Developer Guide_ [: Workflow for Data Cloud Second-Generation Managed Packages](https://developer.salesforce.com/docs/platform/data-cloud-dev/guide/data-cloud-2gp-workflow.html)

_Data Cloud Developer Guide_ [: Metadata Components for Data Cloud Cheat Sheet](https://developer.salesforce.com/docs/platform/data-cloud-dev/guide/component-cheatsheet.html)

_Salesforce Help_ [: Connect Salesforce CRM Orgs to Data Cloud](https://help.salesforce.com/s/articleView?id=data.c360_a_connect_salesforce_orgs.htm&type=5&language=en_US)

### Protected Components in Managed Packages

Developers can mark certain components as _protected_ . Protected components can’t be linked to or referenced by components created
in a subscriber org. A developer can delete a protected component in a future release without worrying about failing installations.
However, after a component is marked as unprotected and is released globally, the developer can’t delete it.

Developers can mark these components as protected in managed packages.

**•** Custom labels

**•** Custom links (for Home page only)

**•** Custom metadata types

**•** Custom objects

**•** Custom permissions

**•** Custom settings

**•** Workflow alerts

**•** Workflow field updates

**•** Workflow outbound messages

**•** Workflow tasks


### Second-Generation Managed Packages Set Up a Platform Cache Partition with Provider Free Capacity

Considerations for Protected Custom Objects in Subscriber Sandboxes

When a subscriber creates either a full or partial sandbox copy using a template, protected custom objects don’t display in the list of
objects to copy. As a result, data contained in the records of protected custom objects isn’t copied to these sandboxes. If a full sandbox
is created without selecting a sandbox template, data from protected custom objects is copied to the sandbox.

SEE ALSO:

[Hide Custom Objects and Custom Permissions in Your Subscribers' Orgs](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg2_dev/fma_hide_custom_objects_permissions.htm)

### Set Up a Platform Cache Partition with Provider Free Capacity

Salesforce provides 3 MB of free Platform Cache capacity for security-reviewed managed packages. This is made available through a
capacity type called Provider Free capacity and is automatically enabled in all Developer edition orgs.

Follow the steps here to allocate the Provider Free capacity to a Platform Cache partition before adding it to your managed package.

Note: If a Platform Cache partition is already part of your managed package, you can choose to edit the existing partition and
allocate the Provider Free capacity to it.

Create a partition from the Platform Cache page and then set it up to use the Provider Free capacity

**1.** From Setup, in the Quick Find box, enter _`Platform Cache`_, and then select **Platform Cache** .

As the Provider Free capacity is automatically enabled in all Developer edition orgs, the Org’s Capacity Breakdown donut chart shows
the Provider Free capacity.

**2.** Click **New Platform Cache Partition** .

**3.** In the `Label` box, enter a name for the partition. The name can contain alphanumeric characters only and must be unique in your
org.

**4.** In the `Description` box, enter an optional description for the partition.

**5.** In the Capacity section, allocate separate capacities for session cache and org cache from the available Provider Free capacity.

**6.** Save the new Platform Cache partition.

You can add this new Platform Cache partition to your managed package. When a security-reviewed managed package with Platform
Cache partition is installed on the subscriber org, the Provider Free capacity is allocated and automatically made available to the installed
partition. The managed package can start using the Platform Cache partition; no post-install script or manual allocation is required.

Note: If the managed package is not AppExchange-certified and security-reviewed, the Provider Free capacity resets to zero and
will not be allocated to the installed Platform Cache partition.

When a Platform Cache partition with Provider Free capacity is installed in a subscriber org, the Provider Free capacity allocated is
non-editable. The provider free capacity of one installed partition can’t be used for any other partition.

Tip: After you install a Platform Cache partition with Provider Free capacity, you can edit the partition and make additional
allocations from the available platform cache capacity of the org.

### Metadata Access in Apex Code Use the Metadata namespace in Apex to access metadata in your package. Your package may need to retrieve or modify metadata during installation or update. The Metadata namespace in Apex provides

classes that represent metadata types, as well as classes that let you retrieve and deploy metadata components to the subscriber org.
These considerations apply to metadata in Apex:


### Second-Generation Managed Packages Permission Sets and Profile Settings in Packages

**•** You can create, retrieve, and update metadata components in Apex code, but you can’t delete components.

**•** You can currently access records of custom metadata types and page layouts in Apex.

**•** Managed packages not approved by Salesforce can’t access metadata in the subscriber org, unless the subscriber org enables the
**Allow metadata deploy by Apex from non-certified Apex package version** org preference. Use this org preference when
doing test or beta releases of your managed packages.

If your package accesses metadata during installation or update, or contains a custom setup interface that accesses metadata, you must
notify the user. For installs that access metadata, notify the user in the description of your package. The notice should let customers
know that your package has the ability to modify the subscriber org’s metadata.

You can write your own notice, or use this sample:

```
   This package can access and change metadata outside its namespace in the Salesforce

   org where it’s installed.

```

Salesforce verifies the notice during the security review.

[For more information, see Metadata in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_metadata.htm) _Apex Developer Guide_ .

### Permission Sets and Profile Settings in Packages

Permission sets, permission set groups, and profile settings are all ways to grant permissions and
other access settings to a package. Only use a profile setting if permission sets don’t support the
specific access you need to grant. In all other instances, use permission sets or permission set groups.

Important: Where possible, we changed noninclusive terms to align with our company
value of Equality. We maintained certain terms to avoid any effect on customer
implementations.

### **Behavior Permission Sets Profile Settings**

EDITIONS

Available in: **Enterprise**,
**Performance**, **Unlimited**,
and **Developer** Editions

Permission sets are
available in: **Contact**
**Manager**, **Professional**,
**Group**, **Enterprise**,
**Performance**, **Unlimited**,
**Developer**, and
**Database.com** Editions

What permissions and settings
are included?

**•** Assigned custom apps **•** Assigned custom apps

**•** Custom object permissions **•** Assigned connected apps

**•** External object permissions **•** Tab settings

**•** Custom field permissions **•** Page layout assignments

**•** Custom metadata types **•** Record type assignments
permissions

**•** Custom field permissions

**•** Custom permissions

**•** Custom metadata type

**•** Custom settings permissions
permissions

**•** Custom object permissions

**•** Custom tab visibility

**•** Custom permissions

settings

**•** Custom permissions

**•** Custom settings

**•** Apex class access
permissions

**•** Visualforce page access

**•** External object permissions

**•** External data source access **•** Apex class access

**•** Record types

**•** Visualforce page access

Note: Although
permission sets include

standard tab visibility

**•** External data source access


Second-Generation Managed Packages Permission Sets and Profile Settings in Packages

**Behavior** **Permission Sets** **Profile Settings**

settings, these settings can’t be
packaged as permission set
components.

If a permission set includes an
assigned custom app, it’s possible
that a subscriber can delete the app.
In that case, when the package is
later upgraded, the assigned custom
app is removed from the permission
set.

Can they be upgraded in managed Yes. Profile settings are applied to existing
packages? profiles in the subscriber’s org on install or
upgrade. Only permissions related to new
components created as part of the install or
upgrade are applied.

Can subscribers edit them? No. Yes.

Can you clone or create them?

Yes. However, if a subscriber clones a
permission set or creates one that’s based
on a packaged permission set, it isn’t
updated in subsequent upgrades. Only the

permission sets included in a package are
upgraded.

Yes. Subscribers can clone any profile that
includes permissions and settings related
to packaged components.

Do they include standard object No. Also, you can’t include object No.
permissions? permissions for a custom object in a
master-detail relationship where the master
is a standard object.

Do they include user permissions? No. No.

Are they included in the installation wizard? No. Subscribers must assign permission sets Yes. Profile settings are applied to existing
after installation. profiles in the subscriber’s org on install or

upgrade. Only permissions related to new
components created as part of the install or
upgrade are applied. Affected components
(listed with the developerName) can include
new:

**•** Fields (CustomField)

**•** Objects (CustomObject),

**•** Tabs (CustomTab)

**•** Apps (CustomApplication)

**•** Apex classes (ApexClass)

**•** Apex pages (ApexPage)

**•** Layouts (Layout)


Second-Generation Managed Packages Permission Sets and Profile Settings in Packages

**Behavior** **Permission Sets** **Profile Settings**

**•** Record types (RecordType)

**•** Custom permissions
(CustomPermission)

**•** Custom settings (CustomSetting)

**•** Custom metadata types
(CustomMetadata)

What are the user license requirements?

A permission set is only installed if the
subscriber org has at least one user license
that matches the permission set. For
example, permission sets with the Salesforce

Platform user license aren’t installed in an
org that has no Salesforce Platform user
licenses. If a subscriber later acquires a
license, the subscriber must reinstall the
package to get the permission sets
associated with the newly acquired license.

Permission sets with no user license are
always installed. If you assign a permission
set that doesn’t include a user license, the
user’s existing license must allow its enabled
settings and permissions. Otherwise, the
assignment fails.

None. In a subscriber org, the installation
overrides the profile settings, not their user
licenses.

How are they assigned to users? Subscribers must assign packaged Profile settings are applied to existing
permission sets after installing the package. profiles.

Can permission sets in an extension package Same behavior as for permission sets.

A permission set in the extension package

grant access to objects installed in a base

can't modify access permissions for either

package?
the parent objects in the base package or
the associated child objects in the extension
package.

Best Practices

**•** If users need access to apps, standard tabs, page layouts, and record types, don't use permission sets as the sole permission-granting
model for your app.

**•** Create packaged permission sets that grant access to the custom components in a package, but not standard Salesforce components.

Permission Set Groups
You can organize permission sets into groups and include them in first and second-generation managed packages. Permission set
groups can be updated when you upgrade the package.


Second-Generation Managed Packages Permission Sets and Profile Settings in Packages

#### Custom Profile Settings

Create profiles to define how users access objects and data, and what they can do within your app. For example, profiles specify
custom object permissions and the tab visibility for your app. When installing or upgrading your app, admins can associate your
custom profiles with existing non-standard profiles. Permissions in your custom profile that are related to new components created
as part of the install or upgrade are added to the existing profile. The security settings associated with standard objects and existing
custom objects in an installer’s organization are unaffected.

How We Handle Profile Settings in Second-Generation Managed Packages
During package version creation for unlocked or second-generation managed packages, the build system inspects the contents of
all profiles in the DX project directory, not just the directory specified in the path, and preserves only the profile settings that are
directly related to the metadata in the package. The profile itself, and any profile settings unrelated to the package’s metadata are
discarded from the package.

#### Permission Set Groups

You can organize permission sets into groups and include them in first and second-generation managed packages. Permission set groups
can be updated when you upgrade the package.

Keep these considerations in mind when you organize permission sets into groups to include in your managed packages:

Important: You can't include object permissions for standard objects in managed packages. During package installation, all
object permissions for standard objects are ignored, and aren't installed in the org.

Also:

**•** You can’t add permission sets constrained by a permission set license to managed or unmanaged packages.

**•** You can only package permissions for metadata that’s included in your package.

**•** You can add or remove permission sets in permission set groups as part of a package upgrade. Subscribers can also modify the
permission set groups by muting permissions or adding or removing local permissions sets. Subscribers can't remove included
permission sets from the permission set groups in the managed package.

SEE ALSO:

_Salesforce Help_ [: Create a Permission Set Group](https://help.salesforce.com/s/articleView?id=platform.perm_set_groups_create.htm&type=5&language=en_US)

_Salesforce Help_ [: Permission Set Group Considerations](https://help.salesforce.com/s/articleView?id=platform.perm_set_groups_considerations.htm&type=5&language=en_US)

#### Custom Profile Settings

Create profiles to define how users access objects and data, and what they can do within your app. For example, profiles specify custom
object permissions and the tab visibility for your app. When installing or upgrading your app, admins can associate your custom profiles
with existing non-standard profiles. Permissions in your custom profile that are related to new components created as part of the install
or upgrade are added to the existing profile. The security settings associated with standard objects and existing custom objects in an
installer’s organization are unaffected.

Consider these tips when creating custom profiles for apps you want to publish.

**•** Give each custom profile a name that identifies the profile as belonging to the app. For example, if you’re creating a Human Resources
app named “HR2GO,” a good profile name would be ”HR2GO Approving Manager.”

**•** If your custom profiles have a hierarchy, use a name that indicates the profile’s location in the hierarchy. For example, name a
senior-level manager’s profile ”HR2GO Level 2 Approving Manager.”

**•** Avoid custom profile names that can be interpreted differently in other organizations. For example, the profile name ”HR2GO Level
2 Approving Manager” is open to less interpretation than ”Sr. Manager.”


Second-Generation Managed Packages Permission Sets and Profile Settings in Packages

**•** Provide a meaningful description for each profile. The description displays to the user installing your app.

Alternatively, you can use permission sets to maintain control of permission settings through the upgrade process. Permission sets
contain a subset of profile access settings, including object permissions, field permissions, Apex class access, and Visualforce page access.
These permissions are the same as those available on profiles. You can add a permission set as a component in a package.

Note: In packages, assigned apps and tab settings aren’t included in permission set components.

#### How We Handle Profile Settings in Second-Generation Managed Packages

During package version creation for unlocked or second-generation managed packages, the build system inspects the contents of all
profiles in the DX project directory, not just the directory specified in the path, and preserves only the profile settings that are directly
related to the metadata in the package. The profile itself, and any profile settings unrelated to the package’s metadata are discarded
from the package.

During package installation, the preserved profile settings are applied only to existing profiles in the subscriber org. The profile itself isn’t
installed in the subscriber org.

To control which profile settings are included, use the `scopeProfiles` [parameter in the project configuration file.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev2gp_config_file.htm)

Note: Packages that contain only profiles and no additional metadata aren’t allowed and fail during package version creation.

To test the behavior of your packaged profile, install your package in a scratch org.

**1.** From Setup, enter _`Profile`_ in the Quick Find box, and then locate and inspect the profiles you selected during package installation.

**2.** Check whether your profile settings have been applied to that profile.


### Second-Generation Managed Packages Protecting Your Intellectual Property

Repeat this step for any other profile you expect to contain your profile settings. Don’t look for the profile name you created; we
apply profile settings to existing profiles in the subscriber org.

Whenever possible, use package permission sets instead of profile settings. Subscribers who install your package can easily assign your
permission set to their users.

Note: During a push upgrade, some profile settings related to Apex classes and field-level security aren’t automatically assigned
to the System Admin profile. To ensure that user access is set up correctly after a push upgrade, communicate with your customer.
Make sure they review and update their profile settings after a push upgrade.

### Protecting Your Intellectual Property

The details of your custom objects, custom links, reports, and other installed items are revealed to installers so that they can check for
malicious content. However, revealing an app’s components prevents developers from protecting some intellectual property.

To protect your intellectual property, consider the following:

**•** Only publish package components that are your intellectual property and that you have the rights to share.

**•** After your components are available on AppExchange, you can’t recall them from anyone who has installed them.

**•** The information in the components that you package and publish might be visible to customers. Use caution when adding your
code to a formula, Visualforce page, or other component that you can’t hide in your app.

**•** The code contained in an Apex class, trigger, Lightning, or Visualforce component that’s part of a managed package is obfuscated
and can’t be viewed in an installing org. The only exceptions are methods declared as global. You can view global method signatures
in an installing org. In addition, License Management Org users with the View and Debug Managed Apex permission can view their
packages’ obfuscated Apex classes when logged in to subscriber orgs via the Subscriber Support Console.

**•** If a custom setting is contained in a managed package, and the `Visibility` is specified as Protected, the custom setting isn’t
contained in the list of components for the package on the subscriber’s org. All data for the custom setting is hidden from the
subscriber.

### Call Salesforce URLs Within a Package

The URLs that Salesforce serves for a target org vary based on the org type and configuration. To build packages that support all possible
URL formats, use relative URLs whenever possible. If your package functionality requires a full URL, use the Apex `DomainCreator`
class to get the corresponding hostname. This method allows your package to work in all orgs, regardless of the org type and My Domain
settings.

The formats for My Domain URLs vary between production and sandbox orgs. With partitioned domains, hostname formats also vary
for demo, Developer Edition, free, patch, and scratch orgs, plus Trailhead playgrounds. For example, there are currently two possible
[formats for sandbox My Domain login hostname formats and ten possible Visualforce hostname formats. For more information, see My](https://help.salesforce.com/s/articleView?id=products.domain_name_app_url_changes.htm&type=5&language=en_US)
[Domain URL Formats and Partitioned Domains in Salesforce Help.](https://help.salesforce.com/s/articleView?id=products.domain_name_app_url_changes.htm&type=5&language=en_US)

In general, use relative URLs whenever possible within your packages. If a full URL is required, use the `[System.DomainCreator](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_System_DomainCreator.htm)`
Apex class to get the URL’s hostname.

Note: The `System.DomainCreator` Apex class is available in API version 54.0 and later.

Use the My Domain Login URL for Logins

All Salesforce orgs have a My Domain, an org-specific subdomain for the URLs that Salesforce hosts for that org. Customers have the
option to prevent user and SOAP API logins from the generic `login.salesforce.com` and `test.salesforce.com`
hostnames. When those options are enabled, logins require the My Domain login URL.


Second-Generation Managed Packages Call Salesforce URLs Within a Package

To get the My Domain login URL format for an org, use the `getOrgMyDomainHostname()` method of the
`System.DomainCreator` Apex class.

```
   //Get the My Domain login hostname

   String myDomainHostname = DomainCreator.getOrgMyDomainHostname();

```

In this case, in a production org with a My Domain name of `mycompany`, `myDomainHostname` returns
`mycompany.my.salesforce.com` .

Use Relative URLs

Whenever possible, we recommend that you use a relative URL, which only includes the path within your packages.

For example, assume that you want to add a link on the Visualforce page with a URL of
`https://` _`MyDomainName`_ `--` _`PackageName`_ `.vf.force.com/apex/myCases` to a Visualforce page with the URL,
`https://` _`MyDomainName`_ `--` _`PackageName`_ `.vf.force.com/apex/newCase` . In this case, use the relative path when
referencing the page: `/apex/newCase` .

Generate Hostnames for Full URLs

Sometimes a full URL is required. For example, when your package delivers a Visualforce page that includes content delivered by your
package. If your package includes full URLs, use the `System.DomainCreator` Apex class to get the associated hostnames.
Otherwise, users can experience issues with your package functionality.

For example, to return the hostname for Visualforce pages, use the `getVisualforceHostname(packageName)` method of
the `System.DomainCreator` Apex class.

```
   //Define the name of your package as a string

   String packageName = 'abcpackage';

   //Get the Visualforce hostname

   String vfHostname = DomainCreator.getVisualforceHostname(packageName);

   //Build the URL for creating a new case

   System.URL vfNewCaseUrl = new URL('https', vfHostname, '/apex/newCase');

```

In this example, in a production org with enhanced domains and a My Domain name of `mycompany`, `vfNewCaseUrl` returns
`https://mycompany--abcpackage.vf.force.com/apex/newCase` .

Get Part of a Domain

If you find code in your package that parses a known URL or domain to get a value, we recommend that you update that code to use
one of the newer Apex classes. Code that assumes a specific URL format can fail.

If you need a hostname, assess whether you can use the `System.DomainCreator` class.

If you need that value for another reason, use the Apex `[System.DomainParser](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_System_DomainParser.htm)` or `[System.Domain](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_System_Domain.htm)` class instead.

In this example, we parse a known URL to get the domain type, the org’s My Domain name, and the package name.

```
   //Parse a known URL

   System.Domain domain = DomainParser.parse('https://mycompany--abcpackage.vf.force.com');

   //Get the domain type

   System.DomainType domainType = domain.getDomainType(); // Returns VISUALFORCE_DOMAIN

```


### Second-Generation Managed Packages Namespace-Based Visibility for Apex Classes in

Second-Generation Managed Packages

```
   //Get the org’s My Domain name

   String myDomainName = domain.getMyDomainName(); // Returns mycompany

   //Get the package name

   String packageName = domain.getPackageName(); // Returns abcpackage

### Namespace-Based Visibility for Apex Classes in Second-Generation
```

Managed Packages

The `@NamespaceAccessible` makes public Apex in a package available to other packages that use the same namespace. Without
this annotation, Apex classes, methods, interfaces, and properties defined in a second-generation managed package aren’t accessible
to the other packages with which they share a namespace. Apex that is declared global is always available across all namespaces, and
needs no annotation.

Considerations for Apex Accessibility Across Packages

**•** You can’t use the `@NamespaceAccessible` annotation for an `@AuraEnabled` Apex method or an `@InvocableMethod`
Apex method.

**•** You can add or remove the `@NamespaceAccessible` annotation at any time, even on managed and released Apex code.
Make sure that you don’t have dependent packages relying on the functionality of the annotation before adding or removing it.

**•** When adding or removing `@NamespaceAccessible` Apex from a package, consider the impact to customers with installed
versions of other packages that reference this package’s annotation. Before pushing a package upgrade, ensure that no customer
is running a package version that would fail to fully compile when the upgrade is pushed.

**•** If a public interface is declared as `@NamespaceAccessible`, then all interface members inherit the annotation. Individual
interface members can’t be annotated with `@NamespaceAccessible` .

**•** If a public or protected variable or method is declared as `@NamespaceAccessible`, its defining class must be either global or
public with the `@NamespaceAccessible` annotation.

**•** If a public or protected inner class is declared as `@NamespaceAccessible`, its enclosing class must be either global or public
with the `@NamespaceAccessible` annotation.

This example shows an Apex class marked with the `@NamespaceAccessible` annotation. The class is accessible to other packages
within the same namespace. The first constructor is also visible within the namespace, but the second constructor isn’t.

```
   // A namespace-visible Apex class

   @NamespaceAccessible

   public class MyClass {

      private Boolean bypassFLS;

      // A namespace-visible constructor that only allows secure use

      @NamespaceAccessible

      public MyClass() {

        bypassFLS = false;

      }

      // A package private constructor that allows use in trusted contexts,

      // but only internal to the package

      public MyClass (Boolean bypassFLS) {

        this.bypassFLS = bypassFLS;

      }

      @NamespaceAccessible

```


### Second-Generation Managed Packages Work with Services Outside of Salesforce

```
      protected Boolean getBypassFLS() {

        return bypassFLS;

      }

   }

```

SEE ALSO:

[Namespaces for Second-Generation Managed Packages](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_plan_namespaces.htm)

[Create and Register Your Namespace for Second-Generation Managed Packages](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_create_namespace.htm)

[Link a Namespace to a Dev Hub Org](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_reg_namespace.htm)

### Work with Services Outside of Salesforce

You might want to update your Salesforce data when changes occur in another service. Likewise, you might also want to update the
data in a service outside of Salesforce based on changes to your Salesforce data. For example, you might want to send a mass email to
more contacts and leads than Salesforce allows. You can use an external mail service that allows users to build a recipient list of names
and email addresses using the contact and lead information in your Salesforce organization.

An app built on the Salesforce Platform can connect with a service outside of Salesforce in many ways. For example, you can:

**•** create a custom link or custom formula field that passes information to an external service.

**•** use the Platform APIs to transfer data in and out of Salesforce.

**•** use an Apex class that contains a Web service method.

Warning: Don’t store usernames and passwords within any external service.

Provisioning a Service External to Salesforce

If your app links to an external service, users who install the app must be signed up to use the service. Provide access in one of two ways:

**•** Access by all active users in an organization with no real need to identify an individual

**•** Access on a per user basis where identification of the individual is important

The Salesforce service provides two globally unique IDs to support these options. The user ID identifies an individual and is unique across
all organizations. User IDs are never reused. Likewise, the organization ID uniquely identifies the organization.

Avoid using email addresses, company names, and Salesforce usernames when providing access to an external service. Usernames can
change over time and email addresses and company names can be duplicated.

If you’re providing access to an external service, we recommend the following:

**•** Use Single Sign-On (SSO) techniques to identify new users when they use your service.

**•** For each point of entry to your app, such as a custom link or web tab, include the user ID in the parameter string. Have your service
examine the user ID to verify that the user ID belongs to a known user. Include a session ID in the parameter string so that your
service can read back through the Lightning Platform API and validate that this user has an active session and is authenticated.

**•** Offer the external service for any known users. For new users, display an alternative page to collect the required information.

**•** Don’t store passwords for individual users. Besides the obvious security risks, many organizations reset passwords on a regular basis,
which requires the user to update the password on your system as well. We recommend designing your external service to use the
user ID and session ID to authenticate and identify users.

**•** If your application requires asynchronous updates after a user session has expired, dedicate a distinct administrator user license for
this.


### Second-Generation Managed Packages Package Connected Apps in Second-Generation Managed

Packaging

### Package Connected Apps in Second-Generation Managed Packaging

Add a connected app to a second-generation managed package.

Note: Consider using External Client Apps instead. External Client Apps are the new and improved generation of connected apps.
[For details, see Package External Client Apps In Second-Generation Managed Packages](https://help.salesforce.com/s/articleView?id=release-notes.rn_packaging_external_client_app.htm&release=250&language=en_US)

[Prerequisites: Create a connected app.](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_auth_connected_app.htm)

**1.** Create a first-generation managed package (1GP) and add the connected app. It’s fine if the connected app is the only component
in the package. Use the same namespace as the 2GP package for the 1GP package.

Take note of the version number of the connected app; you’ll use this number later.

**2.** From your packaging org, upload the 1GP package to create a package version.

**3.** Promote the 1GP version to the released state.

Promoting the 1GP version allows the connected app to be included in a second-generation managed package. You don’t need to
install the 1GP version into an org.

**4.** Navigate to the source for your connected app, or pull the source from the org where the connected app is being developed.

**5.** Create a source `.xml` file in your 2GP directory and reference the connected app you want to include. See the _Sample Source File_
section.

**6.** Create a second-generation managed package and add in the source code for the connected app. Add the source code manually.
You can’t use `sf project retrieve start` or the `retrieve()` Metadata API call to add the source code.

Example: **Sample Source File**

```
      <ConnectedApp xmlns="http://soap.sforce.com/2006/04/metadata">

        <developerName>db_0110_ns4__A_Connected_App</developerName>

        <label>A Connected App</label>

        <version>1.0</version>

      </ConnectedApp>

```

The `developerName` is the combination of your namespace (db_0110_ns4) and the name of your connected app
(A_Connected_App).

The `version` specified in the source file is the version number of the connected app. Use decimal formatting when specifying
the version number. The version number must match the version number of the connected app before it was added to the 1GP
managed package.

Note: When you add a connected app to a 1GP package, and upload the package, the version number of the connected
app is auto incremented. For example, when version 4.0 of a connected app is added to a 1GP package, the package version
increments the version number of the connected app from 4.0 to 5.0. When creating the source file for your 2GP package,
specify the version number of the connected app before it was uploaded into a 1GP package, in this case, 4.0.

### Test and Respond to the New Order Save Behavior

To make sure custom application logic works accurately on records associated with the Order object, turn on the Enable New Order
Save Behavior setting, and test the behavior. We recommend that you support both the new and old order save behavior during testing.

[The Enable New Order Save Behavior setting helps Salesforce correctly evaluate custom application logic on records associated with](https://help.salesforce.com/s/articleView?id=sales.new_order_save_behavior_setup.htm&type=5&language=en_US)
the Order object.


Second-Generation Managed Packages Test and Respond to the New Order Save Behavior

If you create any type of package that includes the Order object, the installed package sometimes doesn’t work. If a subscriber org relies
on a different order save behavior than their installed packages, the installed packages sometimes don’t work. To ensure the expected
behavior, test Enable New Order Save Behavior with your installed packages.

After Enable New Order Save Behavior is selected, Salesforce evaluates and runs these customizations whenever an update to an order
item record changes the parent order record.

**•** Order and order item validation rules

**•** Order and order item Apex triggers and classes

**•** Order and order item flows and processes

Note: Enable New Order Save Behavior affects all package types: unlocked, unmanaged, first-generation managed package (1GP),
and second-generation managed package (2GP).

You can install packages that support old Order Save Behavior on subscriber orgs where New Order Save Behavior is enabled. However,
you must verify that your package works with the new order save behavior.

After you verify that your package works with the new order save behavior and that all your packages associated with your Dev Hub org
work with the new order save behavior, you can choose to enable the update in your Dev Hub org. We recommend that you support
both the new and old order save behavior during your testing.

Test Unmanaged and First-Generation Managed Packages

**•** From Setup, in the Quick Find box, enter _`Release Updates`_, and select **Release Updates** . Locate the Enable New Order Save
Behavior tile, and select **Enable Test Run** .

**•** Test the impact of the new behavior when an order or order item is edited. Review any custom application logic such as validation
rules, Apex triggers and classes, workflow rules, flows, and processes.

**•** To show that your package is compatible with both new and old order save conditions, from Setup, in the Quick Find box, enter
_`Package`_ . Select the package that you tested and select **Upload** .

**•** Locate the Package Requirements section and disable **New Order Save Behavior** .

When this setting is disabled and the release update is enabled, subscriber orgs using either the new or old order save behavior can
install your package.

Test Unlocked and Second-Generation Managed Packages

**•** After creating a scratch org, enable the Release Update in it. From Setup, in the Quick Find box, enter _`Release Updates`_, and
then select **Release Updates** . Locate the Enable New Order Save Behavior tile, and select **Enable Test Run** .

**•** Test the impact of the new behavior when an order or order item is edited. Review any custom application logic such as validation
rules, Apex triggers and classes, workflow rules, flows, and processes.

When you’re ready to create a package version, specify the order save behavior in the definition file.

**Table 3: Order Save Behavior Options**


## Second-Generation Managed Packages Develop Second-Generation Managed Packages

## Develop Second-Generation Managed Packages

Ready to get started? Create your first second-generation managed package, and then update and create new versions of your package.

Create a Second-Generation Managed Package
A package is a top-level container that holds important details about the app or package: the package name, description, and
associated namespace. When you’re ready to test or share your package, use the `sf package create` Salesforce CLI command
to create a package.

View Package Details for a Second-Generation Managed Package
View the details of previously created second-generation managed packages from the command line.

Create Versions of a Second-Generation Managed Package
A package version is a fixed snapshot of the package contents and related metadata. The package version is an installable, immutable
artifact that lets you manage changes and track what’s different each time you release or deploy a specific set of changes.

Guidance for Package Version Numbering
Use package versions to evolve your managed package, and release subsequent package versions without breaking existing package
users. Every package version is a fixed snapshot of the package contents and related metadata.

View Details about a Second-Generation Managed Package Version
Retrieve details about second-generation managed package versions that are in progress, or have already been created.

Project Configuration File for a Second-Generation Managed Package
The project configuration file is a blueprint for your project. The settings in the file create an outline of your managed 2GP package
and determine the package attributes and package contents.

Get Ready to Promote and Release a Second-Generation Managed Package Version
By now it’s likely that you’ve already created many different versions of your managed 2GP package and tested them. When you
have a package version that you're ready to distribute, promoting the package version is the next step.


### Second-Generation Managed Packages Create a Second-Generation Managed Package

Specify a Package Ancestor in the Project File for a Second-Generation Managed Package
When you create a second-generation managed package version you specify a package ancestor in your `sfdx-project.json`
file. We require that the package ancestor you specify is the highest promoted package version number for that package. You can
either update the ancestor version number each time you create a package version, or you can use a keyword.

### Create a Second-Generation Managed Package

A package is a top-level container that holds important details about the app or package: the package name, description, and associated
namespace. When you’re ready to test or share your package, use the `sf package create` Salesforce CLI command to create a
package.

To create a package, change to the project directory in the CLI. The package name you enter becomes the package alias, and is automatically
added to the project file. You can choose to designate an active Dev Hub org user to receive email notifications for Apex gacks, and
[install, upgrade, or uninstall failures associated with your packages. For definitions of each parameter shown here, see sf package create](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_package_commands_unified.htm#cli_reference_package_create_unified)
in the Salesforce CLI Reference Guide.

```
   sf package create --name "Expenser App" --package-type Managed \

   --path "expenser-main" --target-dev-hub my-hub --error-notification-username \

   me@devhub.org

```

The package details you supply when you create a package are automatically added to your `sfdx-project.json` [project](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev2gp_config_file.htm)
[configuration file.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev2gp_config_file.htm)

Metadata Limits in Second-Generation Managed Packages

Update Details about a Package

To update the name or description of an existing package, use this command.

```
   sf package update --package "Expense App" --name "Expense Manager App" \

   --description "The Winter ’21 release is packed with an exciting set of features." \

   --error-notification-username me2@devhub.org

```

Note: You can’t change the package namespace or package type after you create the package.

After you promote at least one package version to the released state, you can also use the `sf package update` CLI command to
recommend a specific version of the package to your subscribers. See Recommend a Specific Package Version to Your Subscribers on
page 364 for more information.

### View Package Details for a Second-Generation Managed Package

View the details of previously created second-generation managed packages from the command line.


### Second-Generation Managed Packages Create Versions of a Second-Generation Managed Package

To display a list of all packages in the Dev Hub org, use this command.

```
   sf package list --target-dev-hub my-hub

```

You can view the namespace, package name, ID, and other details in the output.

```
   Namespace Prefix Name Id Alias Description Type

   ─────────────── ──────────────── ────────────────── ──────────── ─────────── ───────

   db_exp_manager Expenser App 0HoB00000004CzRKAU Expenser App Managed

   db_exp_manager Expenser Logic 0HoB00000004CzMKAU Expenser Logic Managed

   db_exp_manager Expenser Schema 0HoB00000004CzHKAU Expenser Schema Managed

```

Include optional parameters to filter the list results based on the modification date, creation date, and to order by specific fields or
package IDs. To limit the details, use `--concise` .

To show expanded details, use `--verbose` The verbose parameter displays these additional details.

**•** Created By

**•** Error Notification Username

**•** Subscriber Package ID

### Create Versions of a Second-Generation Managed Package

A package version is a fixed snapshot of the package contents and related metadata. The package version is an installable, immutable
artifact that lets you manage changes and track what’s different each time you release or deploy a specific set of changes.

Before you create a package version, first verify package details, such as the package name, dependencies, and update the versionNumber
parameter in the `sfdx-project.json` file. Verify that the metadata you want to change or add in the new package version is in
the package’s main directory.

Tip: Review Advanced Project Configuration Parameters for Second-Generation Managed Packages on page 385 for optional
features that you can enable in the new package version.

When you create a package version, you have three options regarding how package validations are handled.

**•** (Default) Complete all validations of dependencies, package ancestors, and metadata before the package version is returned.

**•** Perform validations asynchronously.

**•** Skip validation on the package version.

Create a Managed 2GP Package Version (Default Option)

Create the package version with this command. Specify the package alias or ID (0Ho). You can also include a scratch definition file that
contains a list of features and settings that the metadata of the package version depends on.

```
   sf package version create --package "Expenser App" --installation-key “HIF83kS8kS7C” \

   --definition-file config/project-scratch-def.json --code-coverage --wait 10

```

Note: When creating a package version, specify a `--wait` time to run the command. If the package version is created within
that time, the `sfdx-project.json` file is automatically updated with the package version information. If not, you must
manually edit the project file.


Second-Generation Managed Packages Create Versions of a Second-Generation Managed Package

It can be a long-running process to create a package version, depending on the package size and other variables. You can easily view
the status and monitor progress.

```
   sf package version create report --package-create-request-id 08cxx00000000YDAAY

```

The output shows details about the request.

```
   === Package Version Create Request

   NAME VALUE

   ───────────────────────────── ────────────────────

   Version Create Request Id 08cB00000004CBxIAM

   Status InProgress

   Package Id 0HoB00000004C9hKAE

   Package Version Id 05iB0000000CaaNIAS

   Subscriber Package Version Id 04tB0000000NOimIAG

   Tag git commit id 08dcfsdf

   Branch

   CreatedDate 2024-05-08 09:48

   Installation URL

   https://login.salesforce.com/packaging/installPackage.apexp?p0=04tB0000000NOimIAG

```

You can find the request ID (08c) in the initial output of `sf package version create` .

Depending on the size of the package and other variables, the create request can take several minutes. When you have more than one
pending request to create package versions, you can view a list of all requests with this command.

```
   sf package version create list --created-last-days 0

```

Details for each request display as shown here (IDs and labels truncated).

```
   === Package Version Create Requests [3]

   ID STATUS PACKAGE2 ID PKG2 VERSION ID SUB PKG2 VER ID TAG BRANCH CREATED DATE ===

   08c... Error 0Ho...

   08c... Success 0Ho... 05i... 04t... 2024-06-22 12:07

   08c... Success 0Ho... 05i... 04t... 2024-06-23 14:55

```

Async Validation

Async validation creates a new package version before completing package validations. If your development team is using continuous
integration (CI) scripts, you can leverage async validation to get an installable artifact sooner so you can start post-package creation
steps.

To specify async validation, include the - - `async-validation` parameter.

```
   sf package version create --async-validation <rest of command syntax>

```

Sample Command-Line Output

```
   Version create.... Create version status: PerformingValidations

   The validations for this package version are in progress, but you can now begin testing

   this package version.

   To determine whether all package validations complete successfully, run "sf package version

    create report --package-create-request-id 08cxx", and review the Status.

   Async validated package versions can be promoted only if all validations complete

   successfully.

   Successfully created the package version [08cxx. Subscriber Package Version Id: 04txx

   Package Installation URL:

```


### Second-Generation Managed Packages Guidance for Package Version Numbering

```
   https://login.salesforce.com/packaging/installPackage.apexp?p0=04txx

   As an alternative, you can use the "sf package:install" command.

```

The command-line output provides you a package creation request ID that starts with 08c. To confirm whether all package validations
complete successfully, use the 08cxx ID when and run `sf package version create report`
`--package-create-request-id 08cxx` . Then validate that the `Status` is listed as `Success` . Async validated package
versions can be promoted only if all validations complete successfully.

Skip Validation

Skips validation of dependencies, package ancestors, and metadata during package version creation. Skipping validation significantly
reduces the time it takes to create a new package version, but package versions created using skip validation can’t be promoted to the
released state.

```
   sf package version create --skip-validation <rest of command syntax>

```

Note: You can't specify both skip validation and code coverage, because code coverage is calculated during validation.

You also can't specify both skip validation and async validation at the same time.

Update Details about a Managed 2GP Package Version

You can update most properties of a package version from the command line. For example, you can change the package version name
or description. One important exception is that you can’t change the release status.

In this example, we’re adding the tag parameter and specifying the git commit ID associated with this package version.

```
   sf package version update --package "Expenser App@1.3.0-5" --tag "git commit id 08dcfsdf"

```

After the update is complete, you’ll see output that looks like

```
   Successfully updated the package version. 04tB0000000KPhnIAG

```

How Many Managed 2GP Package Versions Can I Create Per Day?

Run this command to see how many package versions you can create per day and how many you have remaining.

```
   sf limits api display

```

Look for the `Package2VersionCreates` entry.

```
   NAME REMAINING MAXIMUM

   ───────────────────────────────────── ───────── ─────────

   Package2VersionCreates 23 50

### Guidance for Package Version Numbering

```

Use package versions to evolve your managed package, and release subsequent package versions without breaking existing package
users. Every package version is a fixed snapshot of the package contents and related metadata.

While the format for package version number is predetermined, how you determine a version number, and whether you enforce
uniqueness on package version numbers is left to package developers. The format for package version numbers is


Second-Generation Managed Packages Guidance for Package Version Numbering

MAJOR.MINOR.PATCH.BUILD. Every package version has both a version number that you determine (for example, 2.2.0.1), and a unique
[subscriber package version ID](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_plan_pkg_types_pkg_ids.htm) (starts with 04t) that is auto-assigned when you create the package version.

Before you promote a particular MAJOR.MINOR.PATCH package version, it’s possible to create multiple package versions that have unique
04t IDs, but all share the same version number, for example 2.2.0.1. There are a few approaches you can take to ensure each package
version number is unique. Keep reading to learn more, but let’s start by learning how to specify a package version number.

How Do I Specify the Package Version Number?

The `versionNumber` attribute in your `sfdx-project.json` [project configuration file](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev2gp_config_file.htm) determines the version number that is
assigned the next time you create a managed 2GP version. Before creating a new package version, you must manually increment this
attribute in the project file. If you don't increment the versionNumber, then you can wind up with multiple package versions with the
same version number, but unique subscriber package version IDs (starts with 04t).

```
   {

     "namespace": "exp-mgr",

     "sfdcLoginUrl": "https://login.salesforce.com",

     "sourceApiVersion": "61.0",

     "packageDirectories": [

       {

         "path": "util",

         "default": true,

         "package": "Expense Manager - Util",

         "versionName": "Summer ‘24",

         "versionDescription": "Summer 2024 Expense Manager Util Package",

         "versionNumber": "2.2.0.1",

         "definitionFile": "config/scratch-org-def.json"

       },

```

Use the Keyword NEXT to Enforce Unique Build Numbers

As best practice, don’t create multiple package versions that have the same MAJOR.MINOR.PATCH.BUILD version number. An easy way
to ensure the build portion of your version number is unique is to use the keyword `NEXT` when you set the version number in your
`sfdx-project.json` file. This way, you don’t have to manually increment the version number when you want to create a new
package version.

```
   {

     "namespace": "exp-mgr",

     "sfdcLoginUrl": "https://login.salesforce.com",

     "sourceApiVersion": "61.0",

     "packageDirectories": [

       {

         "path": "util",

         "default": true,

         "package": "Expense Manager - Util",

         "versionName": "Summer ‘24",

         "versionDescription": "Summer 2024 Expense Manager Util Package",

         "versionNumber": "2.2.0.NEXT",

         "definitionFile": "config/scratch-org-def.json"

       },

```


### Second-Generation Managed Packages View Details about a Second-Generation Managed Package

Version

Use the CLI Flag to Override a Package Version Number

You can also override the version number listed in your project file, by using the `--version-number` flag when you create a new
package version.

```
   sf package version create -p "my2gp" -–version-number 2.2.0.NEXT <rest of command syntax>

```

By using the keyword NEXT with the `--version-number` flag in the CLI, you ensure the build portion of the version number is
unique.

Note: Keep in mind, the `--version-number` flag doesn't update your `sfdx-project.json` . To keep the VersionNumber
in the project file current, update it manually.

What Happens to Version Numbering After You Promote a Package Version?

After you promote a package version with a specific MAJOR.MINOR.PATCH version you can’t continue to create package versions that
use that same MAJOR.MINOR.PATCH version number. If you attempt to do so, you receive an error message.

How Do I Determine Whether to Use a New Major, Minor, or Patch Version?

[While there are restrictions on what changes are allowed in a patch version, determining what qualifies as a major or minor change is](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_create_patch_version.htm)
largely up to you. When introducing major changes, increase the major version number, and increase the minor version number when
making smaller improvements.

### View Details about a Second-Generation Managed Package Version

Retrieve details about second-generation managed package versions that are in progress, or have already been created.

View Status and Progress Details for a Managed 2GP Package Version

Depending on the package size and other variables, creating a package version can be a long-running process. You can easily view the
status and monitor progress using this report command.

```
   sf package version create report --package-create-request-id 08cxx00000000YDAAY

```

The output shows details about the request.

```
   === Package Version Create Request

   NAME VALUE

   ───────────────────────────── ────────────────────

   Version Create Request Id 08cB00000004CBxIAM

   Status InProgress

   Package Id 0HoB00000004C9hKAE

   Package Version Id 05iB0000000CaaNIAS

   Subscriber Package Version Id 04tB0000000NOimIAG

   Tag git commit id 08dcfsdf

   Branch

   CreatedDate 2018-05-08 09:48

   Installation URL

   https://login.salesforce.com/packaging/installPackage.apexp?p0=04tB0000000NOimIAG

```

You can find the request ID (08c) in the initial output of `sf package version create` .


Second-Generation Managed Packages View Details about a Second-Generation Managed Package
Version

If you have more than one pending request to create package versions, you can view a list of all requests with this command.

```
   sf package version create list --created-last-days 0

```

Details for each request display as shown here (IDs and labels truncated).

```
   === Package Version Create Requests [3]

   ID STATUS PACKAGE2 ID PKG2 VERSION ID SUB PKG2 VER ID TAG BRANCH CREATED DATE ===

   08c... Error 0Ho...

   08c... Success 0Ho... 05i... 04t... 2022-06-22 12:07

   08c... Success 0Ho... 05i... 04t... 2022-06-23 14:55

```

Retrieve List of all Package Versions Associated with a Dev Hub Org

To display a list of all package versions in the Dev Hub org, use this command.

```
   sf package version list --target-dev-hub my-hub

```

You can view the namespace, version name, and other details in the output.

```
   Package Name Namespace Version Sub Pkg Ver Id Alias

    Installation Key Released

   ─────────────── ─────────────── ─────── ─────────────────── ────────────────────────

    ───────────────── ───────

   Expenser Schema db_exp_manager 0.1.0.1 04tB0000000719qIAA Expenser Schema@0.1.0-1

    false true

   Expenser Schema db_exp_manager 0.2.0.1 04tB000000071AjIAI Expenser Schema@0.2.0-1

    false true

   Expenser Schema db_exp_manager 0.3.0.1 04tB000000071AtIAI Expenser Schema@0.3.0-1

    false false

   Expenser Schema db_exp_manager 0.3.0.2 04tB000000071AyIAI Expenser Schema@0.3.0-2

    false true

   Expenser Schema db_exp_manager 0.3.1.1 04tB0000000KGU6IAO Expenser Schema@0.3.1-1

    false false

   Expenser Schema db_exp_manager 0.3.1.2 04tB0000000KGUBIA4 Expenser Schema@0.3.1-2

    false true

   Expenser Schema db_exp_manager 0.3.2.1 04tB0000000KGUQIA4 Expenser Schema@0.3.2-1

    false true

   Expenser Logic db_exp_manager 0.1.0.1 04tB0000000719vIAA Expenser Logic@0.1.0-1

    false true

   Expenser App db_exp_manager 0.1.0.1 04tB000000071A0IAI Expenser App@0.1.0-1

    false true

```

To view details about a specific package, include `--package` parameter when you run `sf package version list` .

To show expanded details, use `--verbose` The verbose parameter displays these additional details.

**•** Ancestor

**•** Ancestor Version

**•** Branch

**•** Build Duration in Seconds

**•** Code Coverage

**•** Code Coverage Met

**•** Created By


### Second-Generation Managed Packages Project Configuration File for a Second-Generation Managed

Package

**•** Created Date

**•** Description

**•** Installation URL

**•** Language

**•** Managed Metadata Removed

**•** Metadata File Size

**•** Number of Metadata Files

**•** Package ID

**•** Package Version ID

**•** Release Version

**•** Tag

**•** Validation Skipped

**•** WasTransferred

### Project Configuration File for a Second-Generation Managed Package

The project configuration file is a blueprint for your project. The settings in the file create an outline of your managed 2GP package and
determine the package attributes and package contents.

Here are some of the parameters you can specify in the project configuration file. For additional parameters, see Advanced Project
Configuration Parameters for Second-Generation Managed Packages.


Second-Generation Managed Packages Project Configuration File for a Second-Generation Managed
Package


Second-Generation Managed Packages Project Configuration File for a Second-Generation Managed
Package


Second-Generation Managed Packages Project Configuration File for a Second-Generation Managed
Package

When you specify a parameter using Salesforce CLI, it overrides the value listed in the project definition file.

The Salesforce DX project definition file is a JSON file is located in the root directory of your project. Use the `sf project generate`
CLI command to generate a project file that you can build upon. Here’s how the parameters in `packageDirectories` appear.

```
   {

     "namespace": "exp-mgr",

     "sfdcLoginUrl": "https://login.salesforce.com",

     "sourceApiVersion": "61.0",

     "packageDirectories": [

       {

         "path": "util",

         "default": true,

         "package": "Expense Manager - Util",

         "versionName": "Summer ‘24",

         "versionDescription": "Welcome to Summer 2024 Release of Expense Manager Util

   Package",

         "versionNumber": "4.7.0.NEXT",

         "definitionFile": "config/scratch-org-def.json"

       },

       {

         "path": "exp-core",

         "default": false,

         "package": "Expense Manager",

         "versionName": "v 3.2",

         "versionDescription": "Summer 2024 Release",

         "versionNumber": "3.2.0.NEXT",

         "ancestorVersion": "3.0.0.7",

         "definitionFile": "config/scratch-org-def.json",

         "dependencies": [

           {

            "package": "Expense Manager - Util",

            "versionNumber": "4.7.0.LATEST"

           },

           {

            "package" : "External Apex Library - 1.0.0.4"

           }

         ]

       }

     ],

     "packageAliases": {

       "Expense Manager - Util": "0HoB00000004CFpKAM",

       "External Apex Library@1.0.0.4": "04tB0000000IB1EIAW",

       "Expense Manager": "0HoB00000004CFuKAM"}

   }

```

What If I Don’t Want My Salesforce DX Project Automatically Updated?

In some circumstances, you don’t want to have automatic updates to the `sfdx-project.json` file. When you require more control,
use these environment variables to suppress automatic updates to the project file.


### Second-Generation Managed Packages Get Ready to Promote and Release a Second-Generation

Managed Package Version

SEE ALSO:

[Advanced Project Configuration Parameters for Second-Generation Managed Packages](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev2gp_adv_config_file.htm)

### Get Ready to Promote and Release a Second-Generation Managed

Package Version

By now it’s likely that you’ve already created many different versions of your managed 2GP package and tested them. When you have
a package version that you're ready to distribute, promoting the package version is the next step.

Each package version you create is a beta version, unless you promote it to the managed-released state. Beta versions can be installed
in only scratch orgs and sandboxes. After you install a beta version into an org, you can’t later upgrade that installed beta version. Keep
this in mind when you select which org to install and test your beta package version. If you use this sandbox as part of your release
pipeline, then using a disposable scratch org is a better option to test your beta package.

[A beta package version must pass a 75% code coverage requirement before it can be promoted. To learn more, see Code Coverage for](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_code_coverage.htm)
[Second-Generation Managed Packages.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_code_coverage.htm)

To promote a package version to the released state, run the `sf package version promote` Salesforce CLI command. For
[step-by-step instructions on promoting a package version, see Release a Second Generation Managed Package.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_create_pkg_ver_promote.htm)

After a package version is promoted, you can install it in either a production org or development orgs, and can be distributed to your
customers.

For every minor package version, you can promote only one beta version. For example, if you create several beta versions of package
version 2.3, only one of those versions can be promoted. After promoting package version 2.3, start your new development using version
number 2.4.

After a package version is promoted to the released state, you can't reverse the promotion. If you discover you don’t want to distribute
a version you promoted, you can’t reverse that version back to the beta state. To ensure that that version isn’t inadvertently shared and
installed in a customer org, we recommend you use the `sf package version update` Salesforce CLI command and set the
installation key to something cryptic and difficult to guess.

SEE ALSO:

[Considerations for Promoting Packages with Dependencies](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/dev2gp_considerations_pkg_dependency.htm)

[Release a Second-Generation Managed Package](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_create_pkg_ver_promote.htm)

[Code Coverage for Second-Generation Managed Packages](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_code_coverage.htm)

### Specify a Package Ancestor in the Project File for a Second-Generation

Managed Package

When you create a second-generation managed package version you specify a package ancestor in your `sfdx-project.json`
file. We require that the package ancestor you specify is the highest promoted package version number for that package. You can either
update the ancestor version number each time you create a package version, or you can use a keyword.


Second-Generation Managed Packages Specify a Package Ancestor in the Project File for a
Second-Generation Managed Package

Here are three different ways to set the package ancestor.

Use the HIGHEST Keyword (Recommended)

Use the keyword HIGHEST with either the `ancestorId` or `ancestorVersion` attribute in the `sfdx-project.json` file.
This keyword automatically sets the ancestor to the highest promoted package version number.

```
   "packageDirectories": [

   {

   "path": "util",

   "package": "Expense Manager - Util",

   "versionNumber": "4.7.0.NEXT",

   "ancestorVersion": "HIGHEST"

   },

```

This keyword makes it easy to set your package ancestor to use linear versioning, until you have a reason to break from linear versioning.

Use the Ancestor Version Attribute

Set the `ancestorVersion` attribute in the `sfdx-project.json` file to the package version’s major.minor.patch number.
This approach requires you to update the ancestor version number every time the major, minor, or patch value changes.

```
   "packageDirectories": [

   {

   "path": "util",

   "package": "Expense Manager - Util",

   "versionNumber": "4.7.0.NEXT",

   "ancestorVersion": “4.6.0”

   },

```

Use the Ancestor ID Attribute

Set the `ancestorId` attribute in the `sfdx-project.json` file to either the 04t ID or the package version’s alias. This approach
requires you to update the ancestor version number every time you create a package version.

```
   "packageDirectories": [

   {

   "path": "util",

   "package": "Expense Manager - Util",

   "versionNumber": "4.7.0.NEXT",

   "ancestorId": "04tB0000000cWwnIAE"

   },

   "packageDirectories": [

   {

   "path": "util",

   "package": "Expense Manager - Util",

   "versionNumber": "4.7.0.NEXT",

   "ancestorId": "expense-manager@4.6.0.1"

   },

```

Note: Only package versions that have been promoted to managed-released state, can be listed as an ancestor.


## Second-Generation Managed Packages Install and Uninstall Second-Generation Managed Packages

Override Linear Package Ancestry Behavior

To break from linear package versioning, specify a package ancestor that isn’t the highest promoted package version and use the
Salesforce CLI parameter `--skip-ancestor-check` when you create a package version.

```
   sf package version create --package "Expenser App" --skip-ancestor-check

```

The CLI parameter indicates that you’re intentionally choosing to specify a package version that isn’t the highest promoted package
version.

You can choose to not specify a package ancestor by using the keyword, NONE, with either the `ancestorId` or `ancestorVersion`
attribute in the `sfdx-project.json` file.

```
   "packageDirectories": [

   {

   "path": "util",

   "package": "Expense Manager - Util",

   "versionNumber": "4.7.0.NEXT",

   "ancestorVersion": "NONE"

   },

```

Because package ancestors determine package upgrade paths, existing customers can’t upgrade to a package version that is created
without a specified ancestor. Use NONE if you don’t plan to promote the package version you’re creating.

If you’ve already promoted a previous package version, and you set the ancestor to NONE on a new package version associated with
the same package, include `--skip-ancestor-check` when you create that package version. When you create your first package
version, you can also set the ancestor to NONE and specify `--skip-ancestor-check` .

What to Remember about Package Ancestry

**•** Package ancestry determines whether existing packages can be upgraded to newer package versions. If you’re breaking from linear
versioning, or plan to abandon a package version that is installed in customer orgs, consider how your existing customers will be
impacted, and whether an upgrade path is available to them.

**•** If you abandon a package version, delete the version using the Salesforce CLI command `sf package version delete` .

If you aren’t able to delete the package version, then update the package version’s installation key so the abandoned package version
can’t be inadvertently installed. Use `sf package version update` to update the installation key.

## Install and Uninstall Second-Generation Managed Packages

Use a disposable scratch org to test your second-generation managed packages (managed 2GP). You can install or uninstall a managed
2GP package using a Salesforce CLI command, or from the Setup page. Because you can't upgrade a beta package version, be sure you
don't install it in a sandbox that you use in your release pipeline, such as UAT or staging.

Use the CLI to Install a Second-Generation Managed Package
If you’re working with the Salesforce CLI, you can use the `sf package install` command to install packages in a scratch
org or target subscriber org.

Use a URL to Install a Second-Generation Managed Package
Install a second-generation managed package from a browser.


### Second-Generation Managed Packages Use the CLI to Install a Second-Generation Managed Package

Install Notifications for Unauthorized Managed Packages
When you distribute a managed package that AppExchange Partner Program hasn’t authorized, we notify customers during the
installation process. The notification is removed after the package is approved.

Upgrade a Second-Generation Managed Package Version
A package upgrade occurs when you install a new package version into an org that has a previous version of that package installed.

Resolve Apex Test Failures
Package installs or upgrades may fail for not passing Apex test coverage. However, some of these failures can be ignored. For example,
a developer might write an Apex test that makes assumptions about a subscriber's data.

Run Apex on Package Install/Upgrade
App developers can specify an Apex script to run automatically after a subscriber installs or upgrades a managed package. This script
makes it possible to customize the package install or upgrade, based on details of the subscriber’s organization. For instance, you
can use the script to populate custom settings, create sample data, send an email to the installer, notify an external system, or kick
off a batch operation to populate a new field across a large set of data. For simplicity, you can only specify one post install script. It
must be an Apex class that is a member of the package.

Customize Second-Generation Managed Package Installs and Uninstalls Using Scripts
Customize a second-generation managed package (managed 2GP) install or upgrade by specifying an Apex post install script to
run automatically after a subscriber installs or upgrades a managed 2GP package. You can also specify an Apex uninstall script to
run automatically when a subscriber uninstalls a managed 2GP package.

Sample Script for Installing Second-Generation Managed Packages with Dependencies
Use this sample script as a basis to create your own script to install second-generation managed packages with dependencies. This
script contains a query that finds dependent packages and installs them in the correct dependency order.

Uninstall a Second-Generation Managed Package
You can uninstall a second-generation managed package from an org using Salesforce CLI or from the Setup UI. When you uninstall
second-generation managed packages, all components in the package, including any deprecated components that were previously
associated with the package, are deleted from the org.

### Use the CLI to Install a Second-Generation Managed Package

If you’re working with the Salesforce CLI, you can use the `sf package install` command to install packages in a scratch org or
target subscriber org.

Before you install a second-generation managed package (managed 2GP) in a scratch org, run this command to list all the packages
and locate the ID or package alias.

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


### Second-Generation Managed Packages Use a URL to Install a Second-Generation Managed Package

The CLI displays status messages regarding the installation.

```
   Waiting for the subscriber package version install request to get processed. Status =

   InProgress Successfully installed the subscriber package version: 04txx0000000FIuAAM.

```

Control Managed 2GP Package Installation Timeouts

When you issue a `sf package install` command, it takes a few minutes for a package version to become available in the target
org and for installation to complete. To allow sufficient time for a successful install, use these parameters that represent mutually exclusive
timers.

**•** `--publish-wait` defines the maximum number of minutes that the command waits for the package version to be available
in the target org. The default is 0. If the package is not available in the target org in this time frame, the install is terminated.

Setting `--publish-wait` is useful when you create a new package version and then immediately try to install it to target orgs.

Note: If `--publish-wait` is set to 0, the package installation immediately fails, unless the package version is already
available in the target org.

**•** `--wait` defines the maximum number of minutes that the command waits for the installation to complete after the package is
available. The default is 0. When the --wait interval ends, the install command completes, but the installation continues until it either
fails or succeeds. You can poll the status of the installation using `sf package install report` .

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
end of 10 minutes, the command completes because the `wait` time interval has elapsed, although the installation is not yet complete.
At this point, `sf package install report` indicates that the installation is in progress. After one more minute, the installation
completes and `sf package install report` indicates a successful installation.

```
   sf package install --package "Expense Manager@1.2.0-12" --publish-wait 6 --wait 10

```

SEE ALSO:

_[Salesforce CLI Command Reference](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_package_commands_unified.htm#cli_reference_package_install_unified)_ package install

_Salesforce Help:_ [Determine Which Users Can Access a Package](https://help.salesforce.com/s/articleView?id=xcloud.pkg_subscriber_determine_access.htm&type=5&language=en_US)

### Use a URL to Install a Second-Generation Managed Package

Install a second-generation managed package from a browser.

If you create packages from the CLI, you can derive an installation URL for the package by adding the subscriber package ID to your Dev
Hub URL. You can use this URL to test different deployment or installation scenarios.

For example, if the package version has the subscriber package ID, 04tB00000009oZ3JBI, add the ID as the value of apvId.


### Second-Generation Managed Packages Install Notifications for Unauthorized Managed Packages

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

### Install Notifications for Unauthorized Managed Packages

When you distribute a managed package that AppExchange Partner Program hasn’t authorized, we notify customers during the installation
process. The notification is removed after the package is approved.

The notification appears when customers configure the package installation settings (1). Before customers install the package, they must
confirm that they understand that the package isn’t authorized for distribution (2).

The notification displays when a managed package:

**•** Has never been through security review or is under review

**•** Didn’t pass the security review

**•** Isn’t authorized by AppExchange Partner Program for another reason

If the AppExchange Partner Program approves the package, it’s authorized for distribution, and the notification is removed. When you
publish a new version of the package, it’s automatically authorized for distribution.

[For information about the AppExchange Partner Program and its requirements, visit the Salesforce Partner Community.](https://partners.salesforce.com/s/education/general/Partner_Program)


### Second-Generation Managed Packages Upgrade a Second-Generation Managed Package Version Upgrade a Second-Generation Managed Package Version

A package upgrade occurs when you install a new package version into an org that has a previous version of that package installed.

When you perform a package upgrade, here’s what to expect for metadata changes.

**•** Metadata introduced in the new version is installed as part of the upgrade.

**•** Metadata modified in the new version is updated as part of the upgrade.

**•** Metadata removed in the new version is either deprecated or deleted as part of the upgrade.

To upgrade a package, use the package install CLI command

```
   sf package install --package 04t... --target-org me@example.com

```

[For more examples and details about this command, see package install in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_package_commands_unified.htm#cli_reference_package_install_unified) _Salesforce CLI Command Reference_ .

Beta packages aren’t upgradeable. To install a new beta package or released version, first uninstall the beta package.

To upgrade a package version, the new version must be a direct descendent of the package version installed in your org. See Specify a
Package Ancestor in the Project File for a Second-Generation Managed Package for more information.

SEE ALSO:

_[Salesforce CLI Command Reference](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_package_commands_unified.htm#cli_reference_package_install_unified)_ package install

### Resolve Apex Test Failures

Package installs or upgrades may fail for not passing Apex test coverage. However, some of these failures can be ignored. For example,
a developer might write an Apex test that makes assumptions about a subscriber's data.

If your install fails due to an Apex test failure, check for the following:

**•** Make sure that you’re staging all necessary data required for your Apex test, instead of relying on subscriber data that exists.

**•** If a subscriber creates a validation rule, required field, or trigger on an object referenced by your package, your test might fail if it
performs DML on this object. If this object is created only for testing purposes and never at runtime, and the creation fails due to
these conflicts, you might be safe to ignore the error and continue the test. Otherwise, contact the customer and determine the
impact.

### Run Apex on Package Install/Upgrade

App developers can specify an Apex script to run automatically after a subscriber installs or upgrades a managed package. This script
makes it possible to customize the package install or upgrade, based on details of the subscriber’s organization. For instance, you can
use the script to populate custom settings, create sample data, send an email to the installer, notify an external system, or kick off a batch
operation to populate a new field across a large set of data. For simplicity, you can only specify one post install script. It must be an Apex
class that is a member of the package.

The post install script is invoked after tests have been run, and is subject to default governor limits. It runs as a special system user that
represents your package, so all operations performed by the script appear to be done by your package. You can access this user by using
UserInfo. You can only see this user at runtime, not while running tests.

If the script fails, the install/upgrade is aborted. Any errors in the script are emailed to the user specified in the **Notify on Apex Error**
field of the package. If no user is specified, the install/upgrade details are unavailable.

The post install script has the following additional properties.

**•** It can initiate batch, scheduled, and future jobs.


Second-Generation Managed Packages Run Apex on Package Install/Upgrade

**•** It can’t access Session IDs.

**•** It can only perform callouts using an async operation. The callout occurs after the script is run and the install is complete and
committed.

**•** It can’t call another Apex class in the package if that Apex class uses the `with sharing` or `inherit sharing` keyword.
[These keywords can prevent the package from successfully installing. To learn more, see the Apex Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)

Note: You can’t run a post install script in a new trial organization provisioned using Trialforce. The script only runs when a
subscriber installs your package in an existing organization.

#### How Does a Post Install Script Work?

A post install script is an Apex class that implements the `InstallHandler` interface.

Example of a Post Install Script

Specifying a Post Install Script
After you’ve created and tested the post install script, you can specify it in the **Post Install Script** lookup field on the Package Detail
page. In subsequent patch releases, you can change the contents of the script but not the Apex class.

#### How Does a Post Install Script Work?

A post install script is an Apex class that implements the `InstallHandler` interface.

This interface has a single method called `onInstall` that specifies the actions to be performed on installation.

```
   global interface InstallHandler {

     void onInstall(InstallContext context)

   }

```

The `onInstall` method takes a context object as its argument, which provides the following information.

**•** The org ID of the organization in which the installation takes place.

**•** The user ID of the user who initiated the installation.

**•** The version number of the previously installed package (specified using the `Version` class). This is always a three-part number,
such as 1.2.0.

**•** Whether the installation is an upgrade

**•** Whether the installation is a push

The context argument is an object whose type is the `InstallContext` interface. This interface is automatically implemented by
the system. The following definition of the `InstallContext` interface shows the methods you can call on the context argument.

```
   global interface InstallContext {

     ID organizationId();

     ID installerId();

     Boolean isUpgrade();

     Boolean isPush();

     Version previousVersion();

   }

```

**Version Methods and Class**

You can use the methods in the `System.Version` class to get the version of a managed package and to compare package versions.
A package version is a number that identifies the set of components in a package. The version number has the format
_`majorNumber.minorNumber.patchNumber`_ (for example, 2.1.3). The major and minor numbers increase to a chosen value
during every non-patch release. Major and minor number increases always use a patch number of 0.


Second-Generation Managed Packages Run Apex on Package Install/Upgrade

The following are instance methods for the `System.Version` class.

**Method** **Arguments** **Return Type** **Description**

`compareTo` System.Version _`version`_ Integer Compares the current version with the specified
version and returns one of the following values:

**•** Zero if the current package version is equal
to the specified package version

**•** An Integer value greater than zero if the
current package version is greater than the
specified package version

**•** An Integer value less than zero if the
current package version is less than the
specified package version

If a two-part version is being compared to a
three-part version, the patch number is ignored
and the comparison is based only on the major
and minor numbers.

`major` Integer Returns the major package version of the calling
code.

`minor` Integer Returns the minor package version of the
calling code.

`patch` Integer Returns the patch package version of the calling
code or `null` if there’s no patch version.

The `System` class contains two methods that you can use to specify conditional logic, so different package versions exhibit different
behavior.

**•** `System.requestVersion` : Returns a two-part version that contains the major and minor version numbers of a package.Using
this method, you can determine the version of an installed instance of your package from which the calling code is referencing your
package. Based on the version that the calling code has, you can customize the behavior of your package code.

**•** `System.runAs(System.Version)` : Changes the current package version to the package version specified in the argument.

When a subscriber has installed multiple versions of your package and writes code that references Apex classes or triggers in your
package, they must select the version they’re referencing. You can execute different code paths in your package’s Apex code based on
the version setting of the calling Apex code making the reference. You can determine the calling code’s package version setting by
calling the `System.requestVersion` method in the package code.

#### Example of a Post Install Script

The following sample post install script performs these actions on package install/upgrade.

**•** If the previous version is null, that is, the package is being installed for the first time, the script:

**–** Creates a new Account called Newco and verifies that it was created.

**–** Creates a new instance of the custom object Survey, called Client Satisfaction Survey.

**–** Sends an email message to the subscriber confirming installation of the package.


Second-Generation Managed Packages Run Apex on Package Install/Upgrade

**•** If the previous version is 1.0, the script creates a new instance of Survey called ”Upgrading from Version 1.0”.

**•** If the package is an upgrade, the script creates a new instance of Survey called ”Sample Survey during Upgrade”.

**•** If the upgrade is being pushed, the script creates a new instance of Survey called ”Sample Survey during Push”.

```
   public class PostInstallClass implements InstallHandler {

     global void onInstall(InstallContext context) {

      if(context.previousVersion() == null) {

       Account a = new Account(name='Newco');

       insert(a);

       Survey__c obj = new Survey__c(name='Client Satisfaction Survey');

       insert obj;

       User u = [Select Id, Email from User where Id =:context.installerID()];

       String toAddress= u.Email;

       String[] toAddresses = new String[]{toAddress};

       Messaging.SingleEmailMessage mail =

        new Messaging.SingleEmailMessage();

       mail.setToAddresses(toAddresses);

       mail.setReplyTo('support@package.dev');

       mail.setSenderDisplayName('My Package Support');

       mail.setSubject('Package install successful');

       mail.setPlainTextBody('Thanks for installing the package.');

       Messaging.sendEmail(new Messaging.Email[] { mail });

       }

      else

       if(context.previousVersion().compareTo(new Version(1,0)) == 0) {

       Survey__c obj = new Survey__c(name='Upgrading from Version 1.0');

       insert(obj);

       }

      if(context.isUpgrade()) {

       Survey__c obj = new Survey__c(name='Sample Survey during Upgrade');

       insert obj;

       }

      if(context.isPush()) {

       Survey__c obj = new Survey__c(name='Sample Survey during Push');

       insert obj;

       }

      }

     }

```

You can test a post install script using the new `testInstall` method of the `Test` class. This method takes the following arguments.

**•** A class that implements the `InstallHandler` interface.

**•** A `Version` object that specifies the version number of the existing package.

**•** An optional Boolean value that is `true` if the installation is a push. The default is `false` .

This sample shows how to test a post install script implemented in the `PostInstallClass` Apex class.

```
   @isTest

   static void testInstallScript() {

     PostInstallClass postinstall = new PostInstallClass();

      Test.testInstall(postinstall, null);

      Test.testInstall(postinstall, new Version(1,0), true);

      List<Account> a = [Select id, name from Account where name ='Newco'];

```


### Second-Generation Managed Packages Customize Second-Generation Managed Package Installs

and Uninstalls Using Scripts

```
      System.assertEquals(1, a.size(), 'Account not found');

     }

#### Specifying a Post Install Script

```

After you’ve created and tested the post install script, you can specify it in the **Post Install Script** lookup field on the Package Detail
page. In subsequent patch releases, you can change the contents of the script but not the Apex class.

The class selection is also available via the Metadata API as `Package.postInstallClass` . This is represented in package.xml as
a `<postInstallClass>foo</postInstallClass>` element.

SEE ALSO:

### Customize Second-Generation Managed Package Installs and Uninstalls Using Scripts Customize Second-Generation Managed Package Installs and Uninstalls

Using Scripts

Customize a second-generation managed package (managed 2GP) install or upgrade by specifying an Apex post install script to run
automatically after a subscriber installs or upgrades a managed 2GP package. You can also specify an Apex uninstall script to run
automatically when a subscriber uninstalls a managed 2GP package.

[For more information, see Run Apex on Package Install/Upgrade and Run Apex on Package Uninstall.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/apex_post_install_script.htm)

Specify post install and uninstall scripts in the `sfdx-project.json` file.

```
     "packageDirectories": [

       {

         "path": "expenser-schema",

         "default": true,

         "package": "Expense Schema",

         "versionName": ""ver 0.3.2"",

         "versionNumber": "0.3.2.NEXT",

         "postInstallScript": "PostInstallScript",

         "uninstallScript": "UninstallScript",

         "postInstallUrl": "https://expenser.com/post-install-instructions.html",

         "releaseNotesUrl": "https://expenser.com/winter-2020-release-notes.html"

        },

        ],

        {

         "namespace": "db_exp_manager",

         "sfdcLoginUrl": "https://login.salesforce.com",

         "sourceApiVersion": "47.0",

         "packageAliases": {

           "Expenser Schema": "0HoB00000004CzHKAU",

           "Expenser Schema@0.1.0-1": "04tB0000000719qIAA"

         }

```

You can also use the `--post-install-script` and the `--uninstall-script` Salesforce CLI parameters with the `sf`
`package version create` command. The CLI parameters override the scripts specified in the `sfdx-project.json`
`file` .

Note: Include the Apex classes for your post-install and uninstall scripts with the metadata in your package.


### Second-Generation Managed Packages Sample Script for Installing Second-Generation Managed

Packages with Dependencies

You can designate an active Dev Hub org user to receive email notifications for Apex gacks, and install, upgrade, or uninstall failures
associated with your packages. In Salesforce CLI run `sf package create --error-notification-username`
`me@devhub.org` or `sf package update --error-notification-username me@devhub.org` . In Tooling API,
use the `PackageErrorUsername` field on the Package2 object.

### Sample Script for Installing Second-Generation Managed Packages with

Dependencies

Use this sample script as a basis to create your own script to install second-generation managed packages with dependencies. This script
contains a query that finds dependent packages and installs them in the correct dependency order.

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

   PACKAGE=04tB0000000NmnHIAS

   # Specify the user name of the subscriber org.

   USER_NAME=test-bvdfz3m9tqdf@example.com

   # Specify the timeout in minutes for package installation.

   WAIT_TIME=15

   echo "Retrieving dependencies for package Id: "$PACKAGE

   # Execute soql query to retrieve package dependencies in json format.

   RESULT_JSON=`sf data query -u $USER_NAME -t -q "SELECT Dependencies FROM

   SubscriberPackageVersion WHERE Id='$PACKAGE'" --json`

```


Second-Generation Managed Packages Sample Script for Installing Second-Generation Managed
Packages with Dependencies

```
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

```


### Second-Generation Managed Packages Uninstall a Second-Generation Managed Package

```
   # After processing the dependencies, proceed to install the specified package.

   echo "Installing package: "$PACKAGE

   sf package install --package $PACKAGE -u $USER_NAME -w $WAIT_TIME --publish-wait 10

   exit 0;

### Uninstall a Second-Generation Managed Package

```

You can uninstall a second-generation managed package from an org using Salesforce CLI or from the Setup UI. When you uninstall
second-generation managed packages, all components in the package, including any deprecated components that were previously
associated with the package, are deleted from the org.

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

### 2. Click Uninstall next to the package that you want to remove.

**3.** Determine whether to save and export a copy of the package’s data, and then select the corresponding radio button.

### 4. Select Yes, I want to uninstall and click Uninstall .

Considerations on Uninstalling Packages

**•** If you’re uninstalling a package that includes a custom object, all components on that custom object are also deleted. Deleted items
include custom fields, validation rules, custom buttons, and links, and approval processes.

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


## Second-Generation Managed Packages Prepare to Distribute Your Second-Generation Managed

Package

**–** When an installed package includes a custom field that’s referenced by Einstein Prediction Builder or Case Classification, Salesforce
prevents you from uninstalling the package. Before uninstalling the package, edit the prediction in Prediction Builder or Case
Classification so that it no longer references the custom field.

**•** You can’t uninstall a package that removes all active business and person account record types. Activate at least one other business
or person account record type, and try again.

**•** You can’t uninstall a package if a background job is updating a field added by the package, such as an update to a roll-up summary
field. Wait until the background job finishes, and try again.

SEE ALSO:

_[Salesforce CLI Command Reference](https://developer.salesforce.com/docs/atlas.en-us.250.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_package_commands_unified.htm#cli_reference_package_uninstall_unified)_ package uninstall

## Prepare to Distribute Your Second-Generation Managed Package

Before you release a version of your second-generation managed package, ensure that you understand the code coverage requirements,
release logistics, and how to publish your app on AppExchange.

### Code Coverage for Second-Generation Managed Packages

Before you can release and distribute a second-generation managed package version on AppExchange, the Apex code must meet
a minimum 75% code coverage requirement. And every Apex Trigger in a package needs test coverage.

Package Installation Key for Second-Generation Managed Packages
To ensure the security of the metadata in your second-generation managed package, you must specify an installation key when
creating a package version. Package creators provide the key to authorized subscribers so they can install the package. Package
installers provide the key during installation, whether installing the package from the CLI or from a browser. An installation key is
the first step during installation. The key ensures that no package information, such as the name or components, is disclosed until
the correct installation key is supplied.

Release a Second-Generation Managed Package
Each new second-generation managed package version is marked as beta when created. As you develop your package, you may
create several package versions before you create a version that is ready to be released and distributed. Only released package
versions can be listed on AppExchange and installed in customer orgs.

Share Release Notes and Post-Install Instructions for Second-Generation Managed Packages
Share details with your subscribers about what’s new and changed in a released second-generation managed package.

Publishing Your App on AppExchange
If you’ve published a first-generation managed package, you’ll notice the process for publishing a second-generation managed
package (managed 2GP) is different. After you link your Dev Hub org to the AppExchange partner console, all your released managed
2GP package versions are visible in the partner console.

Recommend a Specific Package Version to Your Subscribers
You can choose to recommend that your subscribers upgrade to a specific, released version of your package.

### Code Coverage for Second-Generation Managed Packages

Before you can release and distribute a second-generation managed package version on AppExchange, the Apex code must meet a
minimum 75% code coverage requirement. And every Apex Trigger in a package needs test coverage.


### Second-Generation Managed Packages Package Installation Key for Second-Generation Managed

Packages

To compute code coverage using Salesforce CLI, use the `--code-coverage` parameter when you run the `sf package`
`version create` command.

Package version creation often takes longer to complete when code coverage is being computed, so consider when to include the code
coverage parameter. You can create beta package versions without computing code coverage, but these beta versions can’t be promoted.

If you try to promote a beta package version to managed-released and the version was created without specifying code coverage, or
the code coverage in the package version is less than 75%, the package promotion fails. Code coverage is calculated during package
version validation. If you skip validation using the `--skip-validation` parameter, code coverage isn’t calculated for that package
version.

View code coverage information for a package version using `sf package version list` with the `--verbose` parameter,
or `sf package version report` command in Salesforce CLI.

### Package Installation Key for Second-Generation Managed Packages

To ensure the security of the metadata in your second-generation managed package, you must specify an installation key when creating
a package version. Package creators provide the key to authorized subscribers so they can install the package. Package installers provide
the key during installation, whether installing the package from the CLI or from a browser. An installation key is the first step during
installation. The key ensures that no package information, such as the name or components, is disclosed until the correct installation
key is supplied.

To set the installation key, add the `--installation-key` parameter to the command when you create the package version. This
command creates a package and protects it with the installation key.

```
   sf package version create --package "Expense Manager" --installation-key "JSB7s8vXU93fI"

```

Supply the installation key when you install the package version in the target org.

```
   sf package install --package "Expense Manager" --installation-key "JSB7s8vXU93fI”

```

Change the Installation Key for an Existing Package Version

You can change the installation key for an existing package version with the `sf package version update` command.

```
   sf package version update --package "Expense Manager@1.2.0-4" --installation-key

   “HIF83kS8kS7C”

```

Create a Package Version Without an Installation Key

If you don’t require security measures to protect your package metadata, you can create a package version without an installation key.

```
   sf package version create --package "Expense Manager" --installation-key-bypass

```

Check Whether a Package Version Requires an Installation Key

To determine whether a package version requires an installation key, use the `sf package version list` CLI command.


### Second-Generation Managed Packages Release a Second-Generation Managed Package Release a Second-Generation Managed Package

Each new second-generation managed package version is marked as beta when created. As you develop your package, you may create
several package versions before you create a version that is ready to be released and distributed. Only released package versions can be
listed on AppExchange and installed in customer orgs.

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

   Subscriber Package Version Id 04tB0000000NPbBIAW

   Version 1.0.0.5

   Description update version

   Branch

   Tag git commit id 08dcfsdf

   Released true

   Created Date 2021-05-08 09:48

   Installation URL

   https://login.salesforce.com/packaging/installPackage.apexp?p0=04tB0000000NPbBIAW

```

You can promote and release only one time for each package version number, and you can’t undo this change.

### Share Release Notes and Post-Install Instructions for Second-Generation

Managed Packages

Share details with your subscribers about what’s new and changed in a released second-generation managed package.

You can specify a release notes URL to display on the package detail page in the subscriber’s org. And you can share instructions about
using your package by specifying a post install URL. The release notes and post install URLs display on the Installed Packages page in
Setup, after a successful package installation. For subscribers who install packages using an installation URL, the package installer page
displays a link to release notes. And subscribers are redirected to your post install URL following a successful package installation or
upgrade.


### Second-Generation Managed Packages Publishing Your App on AppExchange

Specify the `postInstallUrl` and `releaseNotesUrl` attributes in the `packageDirectories` section for the package.

```
     "packageDirectories": [

       {

         "path": "expenser-schema",

         "default": true,

         "package": "Expense Schema",

         "versionName": ""ver 0.3.2"",

         "versionNumber": "0.3.2.NEXT",

         "postInstallScript": "PostInstallScript",

         "uninstallScript": "UninstallScript",

         "postInstallUrl": "https://expenser.com/post-install-instructions.html",

         "releaseNotesUrl": "https://expenser.com/winter-2020-release-notes.html"

        },

        ],

        {

         "namespace": "db_exp_manager",

         "sfdcLoginUrl": "https://login.salesforce.com",

         "sourceApiVersion": "47.0",

         "packageAliases": {

           "Expenser Schema": "0HoB00000004CzHKAU",

           "Expenser Schema@0.1.0-1": "04tB0000000719qIAA"

         }

```

You can also use the `--post-install-url` and the `--release-notes-url` Salesforce CLI parameters with the `sf`
`package version create` command. The CLI parameters override the URLs specified in the `sfdx-project.json` file.

### Publishing Your App on AppExchange

If you’ve published a first-generation managed package, you’ll notice the process for publishing a second-generation managed package
(managed 2GP) is different. After you link your Dev Hub org to the AppExchange partner console, all your released managed 2GP package
versions are visible in the partner console.

[To list an app on AppExchange, it must pass the AppExchange security review. For more information, see Pass the AppExchange Security](https://developer.salesforce.com/docs/atlas.en-us.260.0.packagingGuide.meta/packagingGuide/security_review_guidelines.htm)
[Review in the ISVforce Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.packagingGuide.meta/packagingGuide/security_review_guidelines.htm)

Link Dev Hub to the AppExchange Partner Console

**•** [Log in to the Salesforce Partner Community.](https://partners.salesforce.com/)

### • Select the Publishing tab

**•** Click **Technologies**

**•** Click **Org**

**•** Click **Connect Technology**, and **Org**

**•** Click **Connect Org** and **Allow**, and enter the login credentials for your Dev Hub org.

Register Your Managed 2GP Package

**•** From the Solutions tab, locate the package version you want to register, and click **Register Package** . Registering a package links
[the package to your license management app.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/packaging_manage_licenses.htm)

**•** Enter the login credentials for the Dev Hub org associated with the package in the modal window.

**•** Set the default license behavior for the package, including trial length, and number of seats included with the license, and click **Save** .


### Second-Generation Managed Packages Recommend a Specific Package Version to Your Subscribers

Packages that share a namespace can be associated with the same License Management Org (LMO), or you can associate the packages
with different LMOs.

SEE ALSO:

_ISVforce Guide_ [: Create or Edit Your AppExchange Listing](https://developer.salesforce.com/docs/atlas.en-us.260.0.packagingGuide.meta/packagingGuide/appexchange_publish_listings.htm)

_ISVforce Guide_ [: Pass the AppExchange Security Review](https://developer.salesforce.com/docs/atlas.en-us.260.0.packagingGuide.meta/packagingGuide/security_review_guidelines.htm)

### Recommend a Specific Package Version to Your Subscribers

You can choose to recommend that your subscribers upgrade to a specific, released version of your package.

When you set a package version as the recommended version, your subscribers see an **Upgrade to Recommended Version** option
on the Installed Packages page in their org.

To set a package’s recommended version, run the `sf package update` CLI command and specify the package version in the
`--recommended-version-id` flag. This example sets _`PackageA@1.0`_ as the recommended version.

```
   sf package update --package 0Ho.. --target-dev-hub devhub@example.com

   --recommended-version-id PackageA@1.0

```

Keep in mind these requirements and considerations for setting a recommended version:

**•** You can set one recommended version per package.

**•** Only released package versions can be set as the recommended version.

**•** The recommended version is not required to be the latest, released version of a package.

**•** When you update the recommended version, the new version that you set must be a descendant of the previous version in the
[package ancestry. If the package versions don’t share an ancestry tree, you’ll get an error when you try to update the package’s](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_package_ancestor_intro.htm)
recommended version. To bypass this error, you can use the `sf package update` CLI command’s
`--skip-ancestor-check` flag.

SEE ALSO:

Release a Second-Generation Managed Package

_[Salesforce CLI Command Reference](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_package_commands_unified.htm#cli_reference_package_update_unified)_ : package update

## Push a Package Upgrade for Second-Generation Managed Packages

Push upgrades enable you to upgrade second-generation managed packages installed in subscriber orgs, without asking customers to
install the upgrade themselves. You can choose which orgs receive a push upgrade, what version the package is upgraded to, and when
you want the upgrade to occur. Push upgrades are helpful if you need to push a change for a hot bug fix.

Use Salesforce CLI or SOAP API to initiate the push upgrade, track the status of each job, and review error messages if any push upgrades
fail.

The push upgrade feature is only available to first- and second-generation managed packages that have passed the AppExchange
security review. The CLI push upgrade commands are available to second-generation managed packages and unlocked packages. To


### Second-Generation Managed Packages Schedule a Push Upgrade Using CLI

enable push upgrades for your managed package, log a case with Salesforce Partner Support on page 406. For details on the security
[review process, see Pass the AppExchange Security Review in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.packagingGuide.meta/packagingGuide/security_review_guidelines.htm) _ISVforce Guide_ .

**Table 4: Package Types and Push Upgrade Options**

Push Upgrade Considerations for Second-Generation Managed Packages

**•** You can push upgrades to packages that have passed AppExchange security review only.

**•** The same manageability rules for package version upgrades are applicable to push upgrades.

**•** When a push upgrade is installed, the Apex in package is compiled.

**•** Push upgrades can be used even if the package version requires a password.

### Schedule a Push Upgrade Using CLI

Use Salesforce CLI commands to schedule, abort, or view details about your push upgrade requests. Push upgrades let you upgrade
second-generation managed packages installed in subscriber orgs, without asking customers to install the upgrade themselves.

Schedule a Push Upgrade Using SOAP API for First- and Second-Generation Managed Packages
After you’ve created an updated version of your package, you can automatically deploy it to customers using a push upgrade.

Enable a Package Subscriber to Restrict Push Upgrades
In certain scenarios, a Salesforce customer may require the ability to block push upgrades of managed packages that they have
installed in their org. Customized push upgrades let Salesforce Partners give customers the ability to restrict push upgrades to a
specific customer org for a specific package.

Assign Access to New and Changed Features in First- and Second-Generation Managed Packages
Determine how to provide existing non-admin users access to new and changed features. By default, any new components included
in the push upgrade package version are assigned only to admins.

Sample Post Install Script for a Push Upgrade for First- and Second-Generation Managed Packages
Automate the assignment of new components to existing users of a package.

Push Upgrade Best Practices
Push Upgrade is one of the most powerful features we provide to our partners. Pushing an upgrade without proper planning and
preparation can result in significant customer satisfaction issues. Here are some best practices to consider.

### Schedule a Push Upgrade Using CLI

Use Salesforce CLI commands to schedule, abort, or view details about your push upgrade requests. Push upgrades let you upgrade
second-generation managed packages installed in subscriber orgs, without asking customers to install the upgrade themselves.

The push upgrade feature is available to unlocked packages and second-generation managed packages only. To push a package upgrade
for a second-generation managed package, that package must have already passed the AppExchange security review.

Push upgrades for unlocked packages are enabled by default. To enable push upgrades for your second-generation managed package,
log a case with Salesforce Partner Support.


Second-Generation Managed Packages Schedule a Push Upgrade Using CLI

To initiate a push upgrade for an unlocked or second-generation managed package, the Create and Update Second-Generation Packages
user permission is required.

There are several aspects to scheduling a push upgrade for a package. At a high-level these include:

**•** Identifying the subscriber orgs and the org IDs that you want to upgrade

**•** Scheduling the push upgrade

**•** Tracking the progress and completion of the push upgrade

In some scenarios you may also need to abort a scheduled push upgrade, or analyze errors that occurred. Let’s review each of these
steps in more detail.

Note: Partners can also grant select customers the ability to block push upgrades by setting up customized push upgrades. See
Enable a Package Subscriber to Restrict Push Upgrades on page 369 for more information.

Determine the Orgs to Be Upgraded

There isn't a dedicated `push-upgrade` CLI command for this action, instead let's look at how to use the CLI `data query` command.

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


Second-Generation Managed Packages Schedule a Push Upgrade Using CLI

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


Second-Generation Managed Packages Schedule a Push Upgrade Using CLI

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

```


### Second-Generation Managed Packages Schedule a Push Upgrade Using SOAP API for First- and

Second-Generation Managed Packages

### Schedule a Push Upgrade Using SOAP API for First- and Second-Generation

Managed Packages

After you’ve created an updated version of your package, you can automatically deploy it to customers using a push upgrade.

Note: Partners can also grant select customers the ability to block push upgrades by setting up customized push upgrades. See
### Enable a Package Subscriber to Restrict Push Upgrades on page 369 for more information.

For code samples and more detailed steps, see SOAP API object documentation linked in each step.

**1.** [Authenticate to your Dev Hub org.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/sforce_api_calls_login.htm)

**2.** [Query MetadataPackage to verify package details.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_metadatapackage.htm)

**3.** [Query MetadataPackageVersion to verify the package version to use for the push upgrade.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_metadatapackageversion.htm)

**4.** [Query PackageSubscriber to retrieve details about subscriber orgs such as the org ID and installed package version. To retrieve](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_packagesubscriber.htm)
information about more than 2,000 subscribers, use SOAP API `[queryMore()](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/sforce_api_calls_querymore.htm)` call.

**5.** [Create a PackagePushRequest object. Specify the](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_packagepushrequest.htm) `PackageVersionId` and `ScheduledStartTime` (optional). If you omit
the `ScheduledStartTime`, the push begins when you set the PackagePushRequest's status to `Pending` .

**6.** [Create a PackagePushJob for each subscriber and associate it with the](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_packagepushjob.htm) `PackagePushRequest` you created in the previous
step.

**7.** Schedule the push upgrade by changing the status of the `PackagePushRequest` to `Pending` .

Note: Scheduled push upgrades begin as soon as resources are available on the Salesforce instance, which is either at or after
the start time you specify. In certain scenarios, the push upgrade could start a few hours after the scheduled start time.

### Enable a Package Subscriber to Restrict Push Upgrades

In certain scenarios, a Salesforce customer may require the ability to block push upgrades of managed packages that they have installed
in their org. Customized push upgrades let Salesforce Partners give customers the ability to restrict push upgrades to a specific customer
org for a specific package.

Setting up customized push upgrades requires both the Salesforce Partner and Salesforce Customer to complete specific enablement
steps.

**1.** The Salesforce Partner enables customized push upgrades for a package installed in the customer org.

**a.** As the Salesforce Partner, log in to either your 1GP packaging org, or your Dev Hub org (for managed 2GP packages) using the
system administrator account.

**b.** Click the gear icon and select **Developer Console** .

**c.** In the Developer Console, select **Debug**, and then select **Open Execute Anonymous Window** .

**d.** Enter the following code, but remember to replace the `packageID` (starts with _`033`_ ) and `subscriberOrgID` (starts
with _`00D`_ ) text for the package ID and customer org you’re enabling.

```
       String pucId1 = PushUpgradeCustomizationRepository.create('packageID',

       'subscriberOrgID', true);

       System.debug('pucId1 =' + pucId1);

```

If the customer wants to block push upgrades to multiple production orgs, you must specify each org ID. Here’s an example of
how to enable customized push upgrades for more than one org.

```
       String pucId1 = PushUpgradeCustomizationRepository.create('packageID',

       'subscriberOrgID', true);

```


### Second-Generation Managed Packages Assign Access to New and Changed Features in First- and

Second-Generation Managed Packages

```
       System.debug('pucId1 =' + pucId1);

       String pucId2 = PushUpgradeCustomizationRepository.create('packageID',

       'subscriberOrgID', true);

       System.debug('pucId2 =' + pucId2);

```

**e.** Click **Open Log** and then click **Execute** .

**f.** Click the **Debug Only** checkbox and verify that the push upgrade customization record was created.

The record looks something like: `11:09:15:814 USER_DEBUG [2]|DEBUG|pucId1 =12COK000000000B`

**g.** Contact the Salesforce Customer and let them know that customized push upgrades is enabled on your end.

Note: Sandbox orgs automatically get the ability to block push upgrades if the parent production org has been granted the
ability to block push upgrades by the Salesforce Partner.

**2.** After the Salesforce Partner enables customized push upgrades, the Salesforce Customer blocks push upgrades from Setup in the
customer org.

**a.** As the Salesforce Customer, log in to your org.

**b.** From Setup, enter _`Installed Packages`_ in the Quick Find box, and then select **Installed Packages** .

**c.** Select the package you’ve requested to block push upgrades, and then select **Block Push Upgrades** .

**d.** Verify that the **Push upgrades are now blocked** checkbox is selected.

Salesforce Customers can resume push upgrades at any time by selecting the **Allow Push Upgrades** button. While the block is enabled,
package upgrades can only be installed manually.

Salesforce Partners can view and manage existing customized push upgrades by using the PushUpgradeCustomizationRepository Apex
Class.

Note these considerations for customized push upgrades.

**•** [If your package is a managed 2GP and has customized push upgrades enabled, and you then transfer the ownership of the managed](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev2gp_package_transfer.htm)
[2GP from one Dev Hub to another, the new Dev Hub won’t retain the required permissions. In addition, the](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev2gp_package_transfer.htm)
PushUpgradeCustomizationRepository records for blocking push upgrades won’t be retained. To continue using customized push
upgrades with the new Dev Hub org, repeat Steps 1 and 2.

**•** It’s not possible to block push upgrades on a patch version of a package. If the customer has a patch version installed, they must
upgrade to a non-patch version of the package before they can block push upgrades.

### Assign Access to New and Changed Features in First- and

Second-Generation Managed Packages

Determine how to provide existing non-admin users access to new and changed features. By default, any new components included
in the push upgrade package version are assigned only to admins.


### Second-Generation Managed Packages Sample Post Install Script for a Push Upgrade for First- and

Second-Generation Managed Packages

### Sample Post Install Script for a Push Upgrade for First- and

Second-Generation Managed Packages

Automate the assignment of new components to existing users of a package.

Note: Post-install scripts can be used with first and second-generation managed packages only.

For more information on writing a post-install Apex script, see Run Apex on Package Install/Upgrade on page 352.

In this sample script, the package upgrade contains new Visualforce pages and a new permission set that grants access to those pages.
The script performs the following actions.

**•** Gets the Id of the Visualforce pages in the old version of the package

**•** Gets the permission sets that have access to those pages

**•** Gets the list of profiles associated with these permission sets

**•** Gets the list of users who have those profiles assigned

**•** Assigns the permission set in the new package to those users

```
global class PostInstallClass implements InstallHandler {

   global void onInstall(InstallContext context) {

     //Get the Id of the Visualforce pages

     List<ApexPage> pagesList = [SELECT Id FROM ApexPage WHERE NamespacePrefix =

        'TestPackage' AND Name = 'vfpage1'];

     //Get the permission sets that have access to those pages

     List<SetupEntityAccess> setupEntityAccessList = [SELECT Id,

        ParentId, SetupEntityId, SetupEntityType FROM SetupEntityAccess

        WHERE SetupEntityId IN :pagesList];

     Set<ID> PermissionSetList = new Set<ID> ();

     for (SetupEntityAccess sea : setupEntityAccessList) {

        PermissionSetList.add(sea.ParentId);

     }

     List<PermissionSet> PermissionSetWithProfileIdList =

        [SELECT id, Name, IsOwnedByProfile, Profile.Name,

        ProfileId FROM PermissionSet WHERE IsOwnedByProfile = true

        AND Id IN :PermissionSetList];

     //Get the list of profiles associated with those permission sets

     Set<ID> ProfileList = new Set<ID> ();

```


### Second-Generation Managed Packages Push Upgrade Best Practices

```
        for (PermissionSet per : PermissionSetWithProfileIdList) {

           ProfileList.add(per.ProfileId);

        }

        //Get the list of users who have those profiles assigned

        List<User> UserList = [SELECT id FROM User where ProfileId IN :ProfileList];

        //Assign the permission set in the new package to those users

        List<PermissionSet> PermissionSetToAssignList = [SELECT id, Name

           FROM PermissionSet WHERE Name='TestPermSet' AND

           NamespacePrefix = 'TestPackage'];

        PermissionSet PermissionSetToAssign = PermissionSetToAssignList[0];

        List<PermissionSetAssignment> PermissionSetAssignmentList = new

   List<PermissionSetAssignment>();

        for (User us : UserList) {

           PermissionSetAssignment psa = new PermissionSetAssignment();

           psa.PermissionSetId = PermissionSetToAssign.id;

           psa.AssigneeId = us.id;

           PermissionSetAssignmentList.add(psa);

        }

        insert PermissionSetAssignmentList;

      }

   }

   // Test for the post install class

   @isTest

   private class PostInstallClassTest {

      @isTest

      public static void test() {

       PostInstallClass myClass = new PostInstallClass();

       Test.testInstall(myClass, null);

      }

   }

### Push Upgrade Best Practices

```

Push Upgrade is one of the most powerful features we provide to our partners. Pushing an upgrade without proper planning and
preparation can result in significant customer satisfaction issues. Here are some best practices to consider.

Plan, Test, and Communicate

**•** Share an upgrade timeline plan with your customers so they know when you’ll upgrade, and how often.

**•** Plan when you want to push upgrades to your customers’ orgs. Keep in mind that most customers don’t want changes around their
month-end, quarter-end, and year-end or audit cycles. Do your customers have other critical time periods when they don’t want
any changes to their org? For example, there might be certain times when they don’t have staff available to verify changes or perform
any required post-installation steps.

**•** Schedule push upgrades during your customers’ off-peak hours, such as late evening and night. Have you considered time zone
issues? Do you have customers outside the United States who have different off-peak hours? You can schedule push upgrades to
any number of customer organizations at a time. Consider grouping organizations by time zone, if business hours vary widely across
your customer base.


## Second-Generation Managed Packages Advanced Features for Second-Generation Managed

Packages

**•** Don’t schedule push upgrades close to Salesforce-planned maintenance windows. In most cases, it might be better to wait 3-4
weeks after a major Salesforce release before you push major upgrades.

**•** Test, test, and test! Since you’re pushing changes to the organization instead of the customer pulling in changes, there’s a higher
bar to ensure the new version of your app works well in all customer configurations.

Stagger Your Push Upgrades

**•** Don’t push changes to all customers at once. It’s important to ensure that you have sufficient resources to handle support cases if
there are issues. Also, it’s important that you discover possible issues before your entire customer base is affected.

**•** Push to your own test organizations first to confirm that the push happens seamlessly. Log in to your test organization after the push
upgrade and test to see that everything works as expected.

**•** When applicable, push to the sandbox organizations of your customers first before pushing to their production organizations. Give
them a week or more to test, validate, and fix in the sandbox environment before you push to their production organizations.

**•** Push upgrades to small batches of customer production organizations initially. For example, if you have 1,000 customers, push
upgrades to 50 or 100 customers at a time, at least the first few times. After you have confidence in the results, you can upgrade
customers in larger batches.

Focus on Customer Trust

**•** You’re responsible for ensuring that your customers’ organizations aren’t adversely affected by your upgrade. Avoid making changes
to the package, such as changes to validation rules or formula fields, that might break external integrations made by the customer.
If for some reason you do, test and communicate well in advance. Please keep in mind that you can impact customer data, not just
metadata, by pushing an upgrade that has bugs.

**•** Write an Apex test on install to do basic sanity testing to confirm that the upgraded app works as expected.

**•** If you’re enhancing an existing feature, use a post-install script to automatically assign new components to existing users using
permission sets.

**•** If you’re adding a new feature, don’t auto-assign the feature to existing users. Communicate and work with the admins of the
customer org so they can determine who should have access to the new feature, and the timing of the rollout.

## Advanced Features for Second-Generation Managed Packages

After you're comfortable with creating second-generation managed packages, learn about these advanced features to customize your
package development processes.

Package Ancestors for Second-Generation Managed Packages
Second-generation managed packaging (managed 2GP) offers a flexible package versioning model that lets you break your linear
versioning and abandon a package version you no longer want to build upon. We call these versioning decisions _package ancestry_ .

Patch Versions for Second-Generation Managed Packages
Patch versions are a way to fix small issues with your second-generation managed package without introducing major feature
changes. Customers who are using an older version of your package can install a patch and not be forced to upgrade to a new major
package version.


Second-Generation Managed Packages Advanced Features for Second-Generation Managed
Packages

Create Dependencies Between Second-Generation Managed Packages
To avoid monolithic package development practices, plan to develop smaller, modular packages that group similar functionality
and components. You can then define the dependencies between these packages. A package dependency is when metadata
contained in one package depends on metadata contained in another package. For example, defining dependencies allow you to
extend the functionality of a base package with components and metadata located in a separate package.

Considerations for Promoting Packages with Dependencies
If your company is developing a package that has a package dependency, ask yourself these questions before promoting (releasing)
a new package version.

Advanced Project Configuration Parameters for Second-Generation Managed Packages
As your managed 2GP package development becomes more complex, consider including these optional parameters in your
`sfdx-project.json` file.

Second-Generation Managed Packaging Keywords
A keyword is a variable that you can use to specify a package version number.

Target a Specific Release for Your Second-Generation Managed Packages During Salesforce Release Transitions
During major Salesforce release transitions, you can specify `preview` or `previous` when creating a package version. Specifying
the release version for a package allows you to test upcoming features, run regression tests, and support customers regardless of
which Salesforce release their org is on. Previously, you could only create package versions that matched the Salesforce release your
Dev Hub org was on.

Use Branches in Second-Generation Managed Packaging
Development teams who use branches in their source control system (SCS), often build package versions based on the metadata
in a particular branch of code.

Specify Unpackaged Metadata or Apex Access for Package Version Creation Tests for Second-Generation Managed Packages
For scenarios where you require metadata that isn’t part of your second-generation managed package, but is necessary for Apex
test runs, you can specify the path containing unpackaged metadata in the `sfdx-project.json` file. The unpackaged metadata
isn’t included in the package and isn’t installed in subscriber orgs.

Package IDs and Aliases for Second-Generation Managed Packages
During the package lifecycle, packages and package versions are identified by an ID or package alias. When you create a
second-generation managed package or package version, Salesforce CLI creates a package alias based on the package name, and
stores that name in the packageAliases section of the `sfdx-project.json` file. When you run CLI commands or write scripts
to automate packaging workflows, it’s often easier to reference the package alias, instead of the package ID or package version ID.

Avoid Namespace Collisions in Second-Generation Managed Packages
Namespaces impact the combination of package types that you can install in an org.

Remove Metadata Components from Second-Generation Managed Packages
Remove metadata components such as Apex classes that you no longer want in your second-generation managed packages.

Delete a Second-Generation Managed Package or Package Version
Use the `sf package version delete` and `sf package delete` commands to delete packages and package versions
that you no longer need.

Frequently Used Packaging Operations for Second-Generation Managed Packages

Transfer a Second-Generation Managed Package to a Different Dev Hub
You can transfer the ownership of a second-generation managed package (managed 2GP) from one Dev Hub org to another. These
transfers can occur either internally between two Dev Hub orgs your company owns, or you can transfer a package externally to
another Salesforce Partner or ISV. This change provides a way to sell a managed 2GP package to a different company.


### Second-Generation Managed Packages Package Ancestors for Second-Generation Managed

Packages

Contact Salesforce Partner Support to Enable Specific Packaging Features
Certain packaging features can only be enabled by Salesforce Partner Support.

### Package Ancestors for Second-Generation Managed Packages

Second-generation managed packaging (managed 2GP) offers a flexible package versioning model that lets you break your linear
versioning and abandon a package version you no longer want to build upon. We call these versioning decisions _package ancestry_ .

Note: Only package versions that have been promoted to the managed-released state can be specified as a package ancestor.

When package versioning is linear, the package version number (formatted as major.minor.patch.build) always increments to an increasing
number. For example, looking at just the major and minor version numbers, linear versioning looks something like 1.0  1.1  1.2  2.0.
The next package version created in this linear versioning example must be higher than 2.0.

How Managed 2GP Package Versioning Affects Package Upgrades

Before we dig into package ancestry and how managed 2GP lets you break your linear versioning, let’s clarify how package versioning
impacts package upgrades. Let’s use our previous example of a package version history that looks like this, 1.0  1.1  1.2  2.0. A customer
could install version 1.0 and upgrade through each of the subsequent package versions, or they could skip versions and upgrade from
1.0 to 2.0. As long as they upgrade from a lower package version number to a higher package version number, the package upgrade
succeeds.

But what if during your development process you create a package version that you don’t want to build upon? Managed 2GP lets you
break free from linear versioning and select a different package version to build upon.

Say your team creates version 1.0, then 1.1, then 1.2 and oops! 1.2 made a mess of 1.1. Not a problem. When you create a package
version, you specify which package version is the ancestor. So you abandon 1.2, and make 1.1 the ancestor of 1.3. And this process can
be repeated. For example, the illustration shows how to abandon 1.5, and build 1.6 off 1.4.

This more complex and tree-like versioning has the added benefit of making it possible for two or more development teams to do
parallel package development.


Second-Generation Managed Packages Package Ancestors for Second-Generation Managed
Packages

With Great Power Comes Great Responsibility

The flexibility to break from linear versioning is powerful. But remember that if abandoned versions like 1.2 and 1.5 are installed in
customer orgs, those customers no longer have an upgrade path. Packages can only upgrade along the ancestry line. For example, you
can upgrade from version 1.1 to 1.7, but not from version 1.5 to 1.7.

Patch Versions and Package Ancestry

[You can’t specify a patch version, such as 1.0.2, as a direct ancestor of a non-patch version. Instead, use the](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_create_patch_version.htm)
[keyword](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_config_keywords.htm) `“ancestorVersion" : "HIGHEST”`, or specify a non-patch version as the ancestor. Installed patch versions inherit
the upgrade path of the non-patch version with the same major and minor number. For example, patch version 1.0.3 has the same
upgrade path as 1.0.0.

#### Understanding Package Upgrades with Ancestry

Review how package ancestry impacts which package version upgrades are allowed.

View Package Ancestry
Use Salesforce CLI commands to quickly confirm your package’s ancestor, or to create a visualization of the package ancestry tree.

SEE ALSO:

#### Understanding Package Upgrades with Ancestry

[View Package Ancestry](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_view_ancestors.htm)

[Namespace-Based Visibility for Apex Classes in Second-Generation Managed Packages](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_namespace_visibility.htm)

#### Understanding Package Upgrades with Ancestry

Review how package ancestry impacts which package version upgrades are allowed.

Refer to this table and the package ancestry tree to understand whether your subscribers can upgrade between these 2GP package
versions.

**Example Package Ancestry Tree**


Second-Generation Managed Packages Package Ancestors for Second-Generation Managed
Packages


Second-Generation Managed Packages Package Ancestors for Second-Generation Managed
Packages

#### View Package Ancestry

Use Salesforce CLI commands to quickly confirm your package’s ancestor, or to create a visualization of the package ancestry tree.

View Package Ancestor Details in Salesforce CLI

Use the `sf package version report` or `sf package version list` command to view the name and version number
of the package ancestor.

Output from `sf package version report` command.

Output from `sf package version list` command.

Visualize Package Ancestry

Use the `displayancestry` CLI command to create visualizations of your package or package version’s ancestry tree. You can view
the visualization in Salesforce CLI or use the `dot-code` parameter to generate output that can be used in graph visualization software.

Use `sf package version displayancestry` to quickly visualize your package ancestry and understand the possible
package upgrade paths.


### Second-Generation Managed Packages Patch Versions for Second-Generation Managed Packages

To generate `dotcode` output, specify `sf package version displayancestry --dot-code` .

### Patch Versions for Second-Generation Managed Packages

Patch versions are a way to fix small issues with your second-generation managed package without introducing major feature changes.
Customers who are using an older version of your package can install a patch and not be forced to upgrade to a new major package
version.

Package versions follow a major.minor.patch.build number format. Any package version number that contains a non-zero patch number
is a patch version. For example, 1.1.2.5 is a patch version, but 1.1.0.4 isn’t.

Patch versions are intended for small changes like a fixing a bug. You can’t:

**•** Add package components.

**•** Delete existing package components.

**•** Change the API and dynamic Apex access controls.

**•** Deprecate any Apex code.

**•** Add new Apex class relationships, such as extends.

**•** Add Apex access modifiers, such as virtual or global.

**•** Add features, settings, package dependencies, or web services.

**•** Change a component from protected to global.

**•** Change the visibility of CustomSettings or CustomMetadataType from protected to public.

When creating a patch version, you must specify the package ancestor. The major and minor numbers of the patch version and the
package ancestor must match. And the specified package ancestor must be managed-released.

You can specify another patch version as the package ancestor of a patch version. But you can’t specify a patch version as a direct ancestor
[of a non-patch version. Instead, use the keyword](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_config_keywords.htm) `“ancestorVersion" : "HIGHEST”`, or specify a non-patch version as the
ancestor.

Installed patch versions inherit the upgrade path of the non-patch version with the same major and minor number. For example, patch
version 1.0.3 has the same upgrade path as 1.0.0. See Specify a Package Ancestor in the Project File for a Second-Generation Managed
Package for more information about how to specify a package ancestor.

When you create a patch version, the patch automatically inherits the features and settings defined in the package ancestor’s scratch
org definition file. To create a patch, follow the same steps as you do when you create a package version, and increment the patch
number.


### Second-Generation Managed Packages Create Dependencies Between Second-Generation Managed

Packages

Note: To enable patch versioning, log a case with Salesforce Partner Support on page 406 and request that patch versioning be
enabled in the org where you created the namespace for this package. Patch versioning is available to only to packages that have
passed AppExchange security review.

SEE ALSO:

[Specify a Package Ancestor in the Project File for a Second-Generation Managed Package](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_config_ancestors.htm)

[Second-Generation Managed Packaging Keywords](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_config_keywords.htm)

### Create Dependencies Between Second-Generation Managed Packages

To avoid monolithic package development practices, plan to develop smaller, modular packages that group similar functionality and
components. You can then define the dependencies between these packages. A package dependency is when metadata contained in
one package depends on metadata contained in another package. For example, defining dependencies allow you to extend the
functionality of a base package with components and metadata located in a separate package.

How to Specify a Managed 2GP Package Dependency

[Note: To understand which combination of managed 2GP and managed 1GP package dependencies are supported, see Which](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_dependency_overview.htm)
[Package Types Can Your Package Depend On?.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_dependency_overview.htm)

To specify dependencies between managed packages associated with the same Dev Hub, use either the package version alias or a
combination of the package name and the version number.

Example 1:

```
   "dependencies": [

     {

       "package": "MyPackageName@0.1.0.1"

     }

   ]

```

Example 2:

```
   "dependencies": [

     {

       "package": "MyPackageName",

       "versionNumber": "1.0.0.RELEASED"

     }

   ]

```

To specify a dependency on a managed package that isn’t associated with your Dev Hub:

```
   "dependencies": [

     {

       "package": "04txxx"

     }

   ]

```

Note: You can use the RELEASED keyword for the version number to set the dependency.

To denote dependencies with package IDs instead of package aliases, use:

**•** The `0Ho` ID if you specify the package ID along with the version number


Second-Generation Managed Packages Create Dependencies Between Second-Generation Managed
Packages

**•** The `04t` ID if you specify only the package version ID

Specifying Multiple Package Dependencies

If your package has more than one dependency, provide a comma-separated list of packages in the order of installation.

For example, if your package depends on the package Expense Manager - Util, which in turn depends on the package External Apex
Library, the package dependencies are:

```
   "dependencies": [

     {

       "package" : "External Apex Library - 1.0.0.4"

      },

     {

       "package": "Expense Manager - Util",

       "versionNumber": "4.7.0.RELEASED"

     }

   ]

```

If the package has multilevel dependencies, you can optionally set the `calculateTransitiveDependencies` parameter to
_`true`_ in the `sfdx-project.json` file. When `calculateTransitiveDependencies` is _`true`_, you can specify the
package’s direct dependencies only, and the indirect (transitive) dependencies are calculated for you.

For example, if `calculateTransitiveDependencies` is enabled and the package depends on the package Expense Manager

    - Util, which in turn depends on the package External Apex Library, the package dependency is:

```
   "dependencies": [

     {

       "package": "Expense Manager - Util",

       "versionNumber": "4.7.0.RELEASED"

     }

   ]

```

Which Types of Dependencies Are Supported?

**Circular Dependencies**
Circular dependencies among packages aren’t supported.

A circular dependency occurs when pkgC depends on pkgB, pkgB depends on pkgA, and pkgA depends on pkgC.

**Multi-level Dependencies**
Multi-level package dependencies are supported.

A multi-level dependency occurs when pkgC depends on pkgB, and pkgB depends on pkgA.


Second-Generation Managed Packages Create Dependencies Between Second-Generation Managed
Packages

By default, you list all dependencies at all levels in the `sfdx-project.json` file. To specify only the package’s direct dependencies
and have the indirect (transitive) dependencies calculated for you, you can optionally set
`calculateTransitiveDependencies` to _`true`_ in the `sfdx-project.json` file.

When `calculateTransitiveDependencies` is not enabled, list all dependencies in the `sfdx-project.json` file
in the package installation order. In this example, pkgA must be installed first, followed by pkgB, and then pkgC. The dependencies
specified for pkgC are both pkgA and pkgB.

```
     {

       "packageDirectories": [

          {

            "path": "pkgA-wsp",

            "default": true,

            "package": "pkgA",

            "versionName": "ver 1.3",

            "versionNumber": "1.3.0.NEXT",

            "ancestorVersion": "1.1.0.RELEASED"

          },

          {

            "path": "pkgB-wsp",

            "default": false,

            "package": "pkgB",

            "versionName": "ver 2.3",

            "versionNumber": "2.3.0.NEXT",

            "ancestorVersion": "2.0.0.RELEASED",

            "dependencies": [

               {

                "package": "pkgA@1.1.0.RELEASED"

               }

             ]

          },

          {

            "path": "pkgC-wsp",

            "default": false,

            "package": "pkgC",

            "versionName": "ver 0.1",

            "versionNumber": "0.1.0.NEXT",

            "dependencies": [

               {

                "package": "pkgA@1.1.0.RELEASED"

               },

```


Second-Generation Managed Packages Create Dependencies Between Second-Generation Managed
Packages

```
               {

                 "package": "pkgB@2.0.0.RELEASED"

               }

             ]

          }

       ],

     }

```

When `calculateTransitiveDependencies` is set to _`true`_, specify each package’s direct dependencies only. In this
example, pkgC depends on pkgB, pkgB depends on pkgA, and pkgC’s indirect dependency on pkgA is calculated for you.

```
     {

       "packageDirectories": [

          {

            "path": "pkgA-wsp",

            "default": true,

            "package": "pkgA",

            "versionName": "ver 1.3",

            "versionNumber": "1.3.0.NEXT",

            "ancestorVersion": "1.1.0.RELEASED"

          },

          {

            "path": "pkgB-wsp",

            "default": false,

            "package": "pkgB",

            "versionName": "ver 2.3",

            "versionNumber": "2.3.0.NEXT",

            "ancestorVersion": "2.0.0.RELEASED",

            "dependencies": [

               {

                "package": "pkgA@1.1.0.RELEASED"

               }

             ]

          },

          {

            "path": "pkgC-wsp",

            "default": false,

            "package": "pkgC",

            "versionName": "ver 0.1",

            "versionNumber": "0.1.0.NEXT",

            "calculateTransitiveDependencies": true,

            "dependencies": [

               {

                 "package": "pkgB@2.0.0.RELEASED"

               }

             ]

          }

       ],

     }

```


### Second-Generation Managed Packages Considerations for Promoting Packages with Dependencies

The specified package version number also impacts the installation of package dependencies. Before pkgB can be installed, pkgA
version 1.1 or higher must first be installed. If this condition isn’t met, the installation of pkgB fails.

SEE ALSO:

[Advanced Project Configuration Parameters for Second-Generation Managed Packages](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev2gp_adv_config_file.htm)

[Which Package Types Can Your Package Depend On?](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_dependency_overview.htm)

### Considerations for Promoting Packages with Dependencies Considerations for Promoting Packages with Dependencies

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

Example

Your company created a base package called PkgBase, and an extension package called PkgExtn.


### Second-Generation Managed Packages Advanced Project Configuration Parameters for

Second-Generation Managed Packages

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

SEE ALSO:

[Create and Update Versions of a Second-Generation Managed Package](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_create_pkg_ver.htm)

[Get Ready to Promote and Release a Second-Generation Managed Package Version](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_get_ready_promote.htm)

[Create Dependencies Between Second-Generation Managed Packages](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_create_dependencies.htm)

[Second-Generation Managed Packaging Keywords](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_config_keywords.htm)

### Advanced Project Configuration Parameters for Second-Generation

Managed Packages

As your managed 2GP package development becomes more complex, consider including these optional parameters in your
`sfdx-project.json` file.


Second-Generation Managed Packages Advanced Project Configuration Parameters for
Second-Generation Managed Packages


Second-Generation Managed Packages Advanced Project Configuration Parameters for
Second-Generation Managed Packages


Second-Generation Managed Packages Advanced Project Configuration Parameters for
Second-Generation Managed Packages


### Second-Generation Managed Packages Second-Generation Managed Packaging Keywords

SEE ALSO:

[Project Configuration File for a Second-Generation Managed Package](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev2gp_config_file.htm)

### Second-Generation Managed Packaging Keywords

A keyword is a variable that you can use to specify a package version number.

You can use keywords to automatically increment the value of the package build numbers, ancestor version numbers, set the package
dependency to the latest version, or the latest released and promoted version.


### Second-Generation Managed Packages Target a Specific Release for Your Second-Generation

Managed Packages During Salesforce Release Transitions

### Target a Specific Release for Your Second-Generation Managed Packages

During Salesforce Release Transitions

During major Salesforce release transitions, you can specify `preview` or `previous` when creating a package version. Specifying
the release version for a package allows you to test upcoming features, run regression tests, and support customers regardless of which
Salesforce release their org is on. Previously, you could only create package versions that matched the Salesforce release your Dev Hub
org was on.

To create a package version based on a preview or previous Salesforce release version, create a scratch org definition file that includes
either:

```
{

   "release": "previous"

}

```

or

```
{

   "release": "preview"

}

```

In the `sfdx-project.json` file, set the `sourceApiVersion` to correspond with the release version of the package version
you’re creating. If you are targeting a previous release, any `sourceApiVersion` value below the current release is accepted.

Then when you create your package version, specify the scratch org definition file.

```
sf package version create --package pkgA --definition-file config/project-scratch-def.json

```

Preview start date is when sandbox instances are upgraded. Preview end date is when all instances are on the GA release.


### Second-Generation Managed Packages Use Branches in Second-Generation Managed Packaging Use Branches in Second-Generation Managed Packaging

Development teams who use branches in their source control system (SCS), often build package versions based on the metadata in a
particular branch of code.

To identify which branch in your SCS a package version is based on, tag your package version with a branch name using `--branch`
attribute in this Salesforce CLI command.

```
   sf package version create --branch featureA

```

You can specify any alphanumeric value up to 240 characters as the branch name.

You can also specify the branch name in the package directories section of the `sfdx-project.json` file.

```
   "packageDirectories": [

      {

        "path": "util",

        "default": true,

        "package": "pkgA",

        "versionName": "Spring ‘21",

        "versionNumber": "4.7.0.NEXT",

        "branch": "featureA"

      }]

```

When you specify a branch, the package alias for that package version is automatically appended with the branch name. You can view
the package alias in the `sfdx.project.json` file.

```
   "packageAliases": {

      "pkgA@1.0.0.4-featureA":"04tB0000000IB1EIAW"}

```

Keep in mind that version numbers increment within each branch, and not across branches. For example, you could have two or more
beta package versions with the version number 1.3.0.1.

Although more than one beta package version can have the same version number, there can be only one promoted and released
package version for a given major.minor.patch package version.


Second-Generation Managed Packages

Package Dependencies and Branches

### Specify Unpackaged Metadata or Apex Access for Package

Version Creation Tests for Second-Generation Managed
Packages

By default, your package can have dependencies on other packages in the same branch. For package dependencies based on packages
in other branches, explicitly set the branch attribute in the `sfdx.project.json` file.

### Specify Unpackaged Metadata or Apex Access for Package Version

Creation Tests for Second-Generation Managed Packages

For scenarios where you require metadata that isn’t part of your second-generation managed package, but is necessary for Apex test
runs, you can specify the path containing unpackaged metadata in the `sfdx-project.json` file. The unpackaged metadata isn’t
included in the package and isn’t installed in subscriber orgs.

Specify Unpackaged Metadata for Package Version Creation Tests

Specify the path to the unpackaged metadata in your `sfdx-project.json` file.

In this example, metadata in the `my-unpackaged-directory` is available for test runs during the package version creation of
the TV_unl package.

```
"packageDirectories": [

   {

```


### Second-Generation Managed Packages Package IDs and Aliases for Second-Generation Managed

Packages

```
        "path": "force-app",

        "package": "TV_unl",

        "versionName": "ver 0.1",

        "versionNumber": "0.1.0.NEXT",

        "default": true,

        "unpackagedMetadata": {

           "path": "my-unpackaged-directory"

        }

      },

   ]

```

The `unpackagedMetadata` attribute is intended for metadata that isn’t part of your package. You can’t include the same metadata
in both an unpackaged directory and a packaged directory.

Manage Apex Access for Package Version Creation Tests

Sometimes the Apex tests that you write require a user to have certain permission sets or permission set licenses. Use the
`apexTestAccess` setting to assign permission sets and permission set licenses to the user in whose context your Apex tests get
run at package version creation.

```
   "packageDirectories": [

      {

        "path": "force-app",

        "package": "TV_unl",

        "versionName": "ver 0.1",

        "versionNumber": "0.1.0.NEXT",

        "default": true,

        "unpackagedMetadata": {

           "path": "my-unpackaged-directory"

        },

        "apexTestAccess": {

            "permissionSets": [

               "Permission_Set_1",

               "Permission_Set_2"

            ],

            "permissionSetLicenses": [

               "SalesConsoleUser"

            ]

          }

      },

   ]

```

[Note: To assign user licenses, use the runAs Method. User licenses can't be assigned in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_testing_tools_runas.htm) `sfdx-project.json` file.

### Package IDs and Aliases for Second-Generation Managed Packages

During the package lifecycle, packages and package versions are identified by an ID or package alias. When you create a second-generation
managed package or package version, Salesforce CLI creates a package alias based on the package name, and stores that name in the
packageAliases section of the `sfdx-project.json` file. When you run CLI commands or write scripts to automate packaging
workflows, it’s often easier to reference the package alias, instead of the package ID or package version ID.


### Second-Generation Managed Packages Avoid Namespace Collisions in Second-Generation Managed

Packages

Package aliases are stored in the `sfdx-project.json` file as name-value pairs, in which the name is the alias and the value is the
ID. You can modify package aliases for existing packages and package versions in the project file.

At the command line, you also see IDs for things like package members (a component in a package) and requests (like a `sf package`
`version create` request).

Note: As a shortcut, the documentation sometimes refers to an ID by its three-character prefix. For example, a package version
ID always starts with `04t` .

Here are the most commonly used IDs.

### Avoid Namespace Collisions in Second-Generation Managed Packages

Namespaces impact the combination of package types that you can install in an org.

Important: When sharing a namespace, be intentional about managing component names across packages within that namespace.
Ensure that packages associated with the same namespace don’t include components with the same API name. If two packages
include a component with the same API name, you can’t install these packages into the same org.

To understand how namespaces affect the types of packages you can install in a namespaced or no-namespace org, review this table.


Second-Generation Managed Packages Avoid Namespace Collisions in Second-Generation Managed
Packages

To understand how namespaces affect the combination of packages that can be installed into one org, review this table.


### Second-Generation Managed Packages Remove Metadata Components from Second-Generation

Managed Packages

SEE ALSO:

[Namespaces for Second-Generation Managed Packages](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_plan_namespaces.htm)

[Create and Register Your Namespace for Second-Generation Managed Packages](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_create_namespace.htm)

[Link a Namespace to a Dev Hub Org](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_reg_namespace.htm)

### Remove Metadata Components from Second-Generation Managed

Packages

Remove metadata components such as Apex classes that you no longer want in your second-generation managed packages.

Impact of Component Removal in Subscriber Orgs

During a package upgrade, only certain component types are hard deleted and removed from the subscriber org. Most metadata
components that were removed from a package version remain in the subscriber org after package upgrade and are marked as deprecated.
When a package is upgraded in the subscriber org, the Setup Audit Trail logs which components were removed. Admins of a subscriber
org can delete deprecated metadata. If the subscriber uninstalls the package, deprecated metadata that was previously associated with
the package is deleted.

You can remove these metadata components from second-generation managed packages.


Second-Generation Managed Packages Remove Metadata Components from Second-Generation
Managed Packages


Second-Generation Managed Packages Remove Metadata Components from Second-Generation
Managed Packages

How to Remove Metadata Components

To request access to this feature, log a case with Salesforce Partner Support on page 406.

After your request is approved, remove the metadata component’s source file from your Salesforce DX project, and create a package
version. Test the new package version to ensure it’s working properly without the removed metadata.

Before You Remove Metadata Components from Second-Generation Managed
Packages

To ensure you can successfully remove metadata components from a second-generation managed package, keep these details in mind.

**•** Request access to the feature, if you haven’t already.

**•** Familiarize yourself with the list of metadata components that can be removed.

**•** Ensure that there aren’t dependencies on the metadata you plan to remove. If any component in the package depends on or
references the component you're removing, the package version creation operation fails. After you remove a component, you can't
access any customizations that depend on the removed component.

Remove Metadata Dependencies Within a Package

If there are dependencies to the metadata component you plan to remove, resolve the dependency before removing the metadata
component.

For example, before deleting a custom field that is referenced in a page layout, edit the page layout and remove the reference to the
custom field. Then remove the custom field from your source file, and create a package version.


Second-Generation Managed Packages Remove Metadata Components from Second-Generation
Managed Packages

Some scenarios require a two-step approach to component removal. For example, let's say you plan to remove a Visualforce page that
contains a Visualforce component and replace it with a Lightning page that contains a Lightning component. Removing both the
Visualforce page and Visualforce component in a single upgrade could cause issues for your subscribers. These issues occur because
Visualforce components are deleted, and Visualforce pages are deprecated during package upgrade.

To avoid issues for your subscribers in this example, remove the reference to the Visualforce component from the Visualforce page,
create a package version, and push the upgrade. Then remove the Visualforce page from your package version, and push this upgrade
to subscribers.

Remove Dependencies Located in Other Packages

Before you remove a metadata component, first remove all references to the metadata, including references in other packages that
depend on that metadata component. For example, if you’re removing a public Apex class, ensure your other packages aren’t referencing
that class using the Apex `@namespaceAccessible` annotation.

In this section, PackageA refers to the package in which you plan to remove a metadata component. And PackageB is any package that
depends on the metadata you’re removing from PackageA. If you have references to the metadata component or Apex class in PackageB,
follow these steps:

**1.** Remove the reference to the metadata component from PackageB.

**2.** Create a version of PackageB.

**3.** Push the new version of PackageB to your subscribers.

**4.** Repeat these steps if any other packages include a reference to the metadata you plan to remove from PackageA.

After you've removed all references to the metadata component, remove the metadata component’s source file from the Salesforce DX
project of PackageA. Then create a version of PackageA. Before pushing this upgrade to subscribers, test the new package version to
ensure it’s working properly.

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
Salesforce Partner or ISV. This change provides a way to sell a managed 2GP package to a different company.

Note: Package transfers are only available for managed 2GP packages that have passed AppExchange security review. If your
managed 2GP package hasn’t passed security review, consider creating a new managed 2GP package using your preferred Dev
Hub.

A managed 2GP package that has been converted from a first-generation managed package (1GP) can’t be transferred to another
Dev Hub org. When you convert a package to 2GP, the association between the package and the Dev Hub org can’t be changed.

The package transfer feature is also available to unlocked packages. Dev Hub orgs aren’t used with managed 1GP packages or
unmanaged packages, so this feature doesn’t apply to those package types.


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

**•** Package on page 414

**•** Package Version on page 414

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
case with Salesforce Partner Support on page 406.

**2.** Install the LMA in the new org on page 409.

**3.** Associate your packages with the new org on page 409.

**4.** Refresh licenses for your packages on page 413.


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
After logging in to a subscriber’s org, you can view logs and initiate ISV Customer Debugger sessions.

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

**1.** In the License Management App (LMA), click the **Subscribers** tab.


Second-Generation Managed Packages Troubleshoot Subscriber Issues

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
permission set. See Assign Permissions to the Subscriber Org Console on page 411.

#### Debug Subscriber Orgs

After logging in to a subscriber’s org, you can view logs and initiate ISV Customer Debugger sessions.

Get Access to Debug Logs

You can debug your code by generating Apex debug logs that contain the output from your managed package. Using this log information,
you can troubleshoot issues that are specific to that subscriber.

[To get access to a subscriber’s Apex debug logs, you can either request login access from the subscriber, or use the License Management](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/lma_requesting_login_access.htm)
App (LMA) to enable debug logs for a namespace.

Important: Note these important considerations for enabling subscriber debug logs for a namespace.

**•** When you enable debug logs for a namespace, the subscriber org displays debug statements from those managed packages.
Logs from Apex code execution in that namespace become visible in the subscriber org.

**•** Because multiple packages can share a namespace in second-generation managed packaging (2GP), enabling debug logs for
2GP means enabling logs for all managed packages in the namespace. For example, a subscriber is reporting issues with
Package A and you enable debug logs for the namespace that includes Package A. The subscriber also uses Package B and
Package C that are in the same namespace. By enabling debug logs for the namespace that includes Package A, you also
enable debug logs for Package B and Package C.

Follow these steps to enable debug logs for a namespace through the LMA.

**1.** In the LMA, click the **Subscribers** tab.

**2.** Search for the subscriber’s name or org ID, then click the name of the subscriber org.

**3.** In the Packages & Licensing section, find the package that you want to troubleshoot.

**4.** In the Subscriber Debug Logs column, click **Enable** .


## Second-Generation Managed Packages Manage Features in Second-Generation Managed Packages

**5.** Review the confirmation message, then click **OK** .

After you enable debug logs, the logs from Apex code execution remain visible to the subscriber org until you disable debug logs. To
disable debug logs, follow the same steps in the LMA.

Troubleshoot with Debug Logs

After you get access to a subscriber’s debug logs or you enable debug logs for a namespace, get debug logs from the Developer Console.

**1.** From Setup of the subscriber’s org, in the Quick Find box, enter _`Debug Logs`_, and then select **Debug Logs** .

**2.** Launch the Developer Console.

**3.** Perform the operation, and view the debug log with your output.

Subscribers can see the debug logs you generate, and these logs contain your unobfuscated Apex code.

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

[See the Metadata Coverage Report, for the latest information on supported metadata types.](https://developer.salesforce.com/docs/success/metadata-coverage-report/references/coverage-report/metadata-coverage-report.html)

