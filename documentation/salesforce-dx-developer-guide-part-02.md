The first time you deploy source to the org, all source in the package directories in the `sfdx-project.json` file is deployed to the
scratch org to complete the initial setup. At this point, Salesforce CLI starts source-tracking locally on the file system and remotely in the
scratch org to determine which metadata has changed. Let’s say you deployed an Apex class to a scratch org and then decide to modify
the class in the scratch org instead of your local file system. Salesforce CLI tracks in which local package directory the class was created,
so when you retrieve it back to your project, it knows where it belongs.

To run the deploy commands described in the remainder of this topic, first open a terminal (macOS and Linux) or command window
(Windows) and then change to your Salesforce DX project directory.

Preview a Deployment

Before you deploy source to an org, you can preview the components that will be deployed, the potential conflicts, and the ignored
files by executing `project deploy preview` . For example, this command displays a preview of deploying all the source in your
project to a scratch org with alias `MyGroovyScratchOrg` .

```
   sf project deploy preview --target-org MyGroovyScratchOrg

```

Use flags to target the source you want to preview, such as only the source listed in a manifest. In this example, `--target-org`
points to the scratch org’s username.

```
   sf project deploy preview --manifest package.xml --target-org test-am6xqkossaq8@example.com

```

Tip: You can create an alias for an org using `alias set` . To display the usernames and aliases of all the scratch orgs you’ve
created, run `org list` .

Deploy Source to a Scratch Org

To deploy changed local source to your default scratch org, run this command.

```
   sf project deploy start

```

The command displays what it deployed. This sample output shows a deployment of the `PropertyController` Apex class.

```
   Deploying v58.0 metadata to test-am6xqkossaq8@example.com using the v59.0 SOAP API.

   Deploy ID: 0Af7e00001WsuoSCAR

   Status: Succeeded | ████████████████████████████████████████| 1/1 Components (Errors:0)

   | 0/0 Tests (Errors:0)

   Deployed Source

   =====================================================================================================

```


Scratch Orgs Deploy Source From Your Project to the Scratch Org

```
   | State Name Type Path

   | ──────────────────────────────────

   ──────────────────────────────────────────────────────────────

   | Changed PropertyController ApexClass force-app/main/default/classes/PropertyController.cls

   | Changed PropertyController ApexClass

   force-app/main/default/classes/PropertyController.cls-meta.xml

```

Use flags to target the source you want to deploy, rather than everything that’s changed.

**•** Use the `--metadata` flag to deploy specific metadata components, such as Apex classes.

**•** Use the `--manifest` flag to deploy components in a manifest file.

**•** Use `--source-dir` to deploy source in a package directory.

[See the reference information about project deploy start for examples and other flags you can specify.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_project_commands_unified.htm#cli_reference_project_deploy_start_unified)

Select Files to Ignore During Deploys

It’s likely that you have some files that you don’t want to sync between the project and scratch org. Add these files to the `.forceignore`
file so they’re ignored by the deploy command.

If the Deploy Detects Warnings

If you run `project deploy start`, and warnings occur, Salesforce CLI doesn’t deploy the source. Warnings can occur, for example,
if your project source is using an outdated version. If you want to ignore these warnings and deploy the source to the scratch org, run:

```
   sf project deploy start --ignore-warnings

```

Tip: Although you can successfully deploy using this option, we recommend addressing the issues in the source files. For example,
if you see a warning because a Visualforce page is using an outdated version, consider updating your page to the current version
of Visualforce. This way, you can take advantage of new features and performance improvements.

If the Deploy Detects File Conflicts

During development, you change files locally in your file system and change the scratch org directly using the builders and editors that
Salesforce supplies. Usually, these changes don’t cause a conflict and involve unique files. Also, the `project deploy start`
command doesn’t handle merges. Projects and scratch orgs are meant to be used by one developer.

However, if you run `project deploy start`, and conflicts are detected, Salesforce CLI terminates the operation and doesn’t
deploy the source. Instead, it displays conflict information, such as this sample output. The PropertyController Apex class has been
changed both locally and in the org, but the changes are in conflict.

```
   sf project deploy start

    STATE FULL NAME TYPE FILE PATH

    ───────────────────────────────────

   ─────────────────────────────────────────────────────────────────────────────────────────────────────────

    Conflict PropertyController ApexClass

   <dir>/force-app/main/default/classes/PropertyController.cls-meta.xml

    Conflict PropertyController ApexClass

```


## Scratch Orgs Retrieve Source from the Scratch Org to Your Project

```
   <dir>/force-app/main/default/classes/PropertyController.cls

   Error (1): There are changes in the org that conflict with the local changes you're trying

    to deploy.

```

First decide which change you want to keep. To keep the local change, rerun the deploy and specify the `--ignore-conflicts`
flag.

```
   sf project deploy start --ignore-conflicts

```

To keep the change that’s in the org, run the `project retrieve start` command to retrieve the change to your local project,
and specify the `--ignore-conflicts` flag.

```
   sf project retrieve start --ignore-conflicts

```

SEE ALSO:

How to Exclude Source When Syncing

## Retrieve Source from the Scratch Org to Your Project

Track Changes Between Your Project and Org

_VS Code Command_ [: SFDX: Deploy Source to Org](https://developer.salesforce.com/docs/platform/sfvscode-extensions/guide/deploy-changes.html)

## Retrieve Source from the Scratch Org to Your Project

After you do an initial deploy, your changes are tracked between your local file system and your scratch org. If you change metadata in
your scratch org, retrieve those changes to your local project to keep both in sync.

Note: Scratch orgs have source tracking enabled by default. But sometimes you don’t want source tracking, such as in a continuous
integration environment when you want to speed up deployments. You can opt out of source tracking when you create the scratch
org by specifying the `--no-track-source` flag.

```
      sf org create scratch --definition-file config/project-scratch-def.json --no-track-source

```

See Create Scratch Orgs for more reasons to disable source tracking.

To run the retrieve commands described in the remainder of this topic, first open a terminal (macOS and Linux) or command window
(Windows) and then change to your Salesforce DX project directory.

Preview a Retrieve

Before you retrieve metadata from an org, you can preview the components that will be retrieved, the potential conflicts, and the ignored
files by executing `project retrieve preview` . For example, this command displays a preview of retrieving changed metadata
from a scratch org with the alias `MyGroovyScratchOrg` to your local project.

```
   sf project retrieve preview --target-org MyGroovyScratchOrg

```

Tip: You can create an alias for an org using `alias set` . To display the usernames and aliases of all the scratch orgs you’ve
created, run `org list` .


Scratch Orgs Retrieve Source from the Scratch Org to Your Project

Retrieve Metadata from Your Scratch Org

To retrieve changed source from your default scratch org to your project, run this command

```
   sf project retrieve start

```

The command displays what it retrieved and where in your local Salesforce DX project it puts it. This sample output shows a retrieve of
the `DiscountSpecial` Apex class and `DiscountPermSet` permission set into the `force-app/main/default` directory.

```
   Preparing retrieve request...

   Preparing retrieve request... Succeeded

   Retrieved Source

   ====================================================================================================================

   | State Name Type Path

   | ───────────────────────────────────

   ────────────────────────────────────────────────────────────────────────────

   | Created DiscountSpecial ApexClass force-app/main/default/classes/DiscountSpecial.cls

   | Created DiscountSpecial ApexClass

   force-app/main/default/classes/DiscountSpecial.cls-meta.xml

   | Created DiscountPermSet PermissionSet

   force-app/main/default/permissionsets/DiscountPermSet.permissionset-meta.xml

```

Use flags to target the source you want to retrieve, rather than everything that’s changed.

**•** Use the `--metadata` flag to retrieve specific metadata components, such as Apex classes.

**•** Use the `--manifest` flag to retrieve components in a manifest file.

**•** Use `--source-dir` to retrieve source in a package directory.

[See the reference information about project retrieve start for examples and other flags you can specify.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_project_commands_unified.htm#cli_reference_project_retrieve_start_unified)

Select Files to Ignore During Retrieves

It’s likely that you have some files that you don’t want to sync between the project and scratch org. Add these files to the `.forceignore`
file so they’re ignored by the retrieve command.

If the Retrieve Detects File Conflicts

During development, you change files locally in your file system and change the scratch org using builders and editors. Usually, these
changes don’t cause a conflict and involve unique files. Also, the `project retrieve start` command doesn’t handle merges.
Projects and scratch orgs are meant to be used by one developer.

However, if you run `project retrieve start`, and conflicts are detected, Salesforce CLI terminates the operation and doesn’t
retrieve the source. Instead, it displays conflict information, such as this sample output. The PropertyController Apex class has been
changed both locally and in the org, but the changes are in conflict.

```
   sf project retrieve start

   Preparing retrieve request... � Sending request to org

    STATE FULL NAME TYPE FILE PATH

    ───────────────────────────────────

   ───────────────────────────────────────────────────────────────────

```


## Scratch Orgs Scratch Org Users

```
    Conflict PropertyController ApexClass

   <dir>force-app/main/default/classes/PropertyController.cls-meta.xml

   Preparing retrieve request... Error

   Error (1): There are changes in your local files that conflict with the org changes you're

    trying to retrieve.

```

First decide which change you want to keep. To keep the change that’s in the org, rerun the retrieve and specify the
`--ignore-conflicts` flag.

```
   sf project retrieve start --ignore-conflicts

```

To keep the local change, run the `project deploy start` command to deploy the change to your org, and specify the
`--ignore-conflicts` flag.

```
   sf project deploy start --ignore-conflicts

```

SEE ALSO:

Retrieve Source from the Scratch Org to Your Project

How to Exclude Source When Syncing

Track Changes Between Your Project and Org

_VS Code Command_ [: SFDX: Retrieve Source to Org](https://developer.salesforce.com/docs/platform/sfvscode-extensions/guide/deploy-changes.html)

## Scratch Org Users

A scratch org includes one administrator user by default. The admin user is typically adequate for all your testing needs. But sometimes
you need other users to test with different profiles and permission sets.

You can create a user by opening the scratch org in your browser and navigating to the Users page in Setup. You can also use the `org`
`create user` CLI command to easily integrate the task into a continuous integration job.

Scratch Org User Limits, Defaults, and Considerations

**•** You can run the `org create user` command only for scratch orgs. If you try to create a user for a non-scratch org, the command
fails.

**•** Your scratch org edition determines the number of available user licenses. The number of licenses determines the number of users
you can create. For example, a Developer Edition org includes a maximum of two Salesforce user licenses. Therefore, in addition to
the default administrator user, you can create one standard user.

**•** The new user’s username must be unique across all Salesforce orgs and in the form of an email address. The `org create user`
command provides the `--set-unique-username` flag to ensure uniqueness. The username is active only within the bounds
of the associated scratch org.

**•** You can’t delete a user using Salesforce CLI, just like you can’t delete a Salesforce user using Setup. The user is deactivated when
you delete the scratch org with which the user is associated. Deactivating a user frees up the user license. But you can’t reuse
usernames, even if the associated user has been deactivated.

**•** The simplest way to create a user is to let the `org create user` command assign default or generated characteristics to the
new user. If you want to customize your new user, create a definition file and specify it with the `--definition-file` ( `-f` )
flag. In the file, you can include all the User object fields and a set of Salesforce DX-specific options, described in User Definition File
for Customizing a Scratch Org User. You can also specify these options on the command line.


### Scratch Orgs Create a Scratch Org User

**•** If you don’t customize your new user, the `org create user` command creates a user with these default characteristics.

**–** The username is the existing administrator’s username prepended with a timestamp. For example, if the administrator username
is test-wvkpnfm5z113@example.com, the new username is something like 1505759162830_test-wvkpnfm5z113@example.com.

**–** The user’s profile is Standard User.

**–** The values of the required fields of the User object are the corresponding values of the administrator user. For example, if the
administrator’s locale (specifically the LocaleSidKey field of User object) is en_US, the new user’s locale is also en_US.

**•** After the new user has been created, Salesforce CLI automatically authenticates it to the scratch org so the new user can immediately
start using the scratch org. Salesforce CLI uses the same authentication method that was used on the associated Dev Hub org. Due
to Hyperforce limitations, if the Dev Hub authentication used the JWT flow and the scratch org is on Hyperforce, then the scratch
org user creation fails. For this reason, if you plan to create scratch org users, authenticate to the Dev Hub org with either the `org`
`login web` or `org login sfdx-url` command, and not `org login jwt` .

How Scratch Org Users Can Log In to the Scratch Org

How you log in to a scratch org can depend on if you’re the default admin user, or on which infrastructure the scratch org was created.
To determine the infrastructure, find the **Instance** [on the Company Information Setup page, then go to Find My Instance.](https://availability.salesforce.com/find-my-instance/)

**•** Regardless of the instance, default admin users can log in using `test.salesforce.com` or the My Domain URL, such as
`https://MyDomainName.scratch.my.salesforce.com` .

**•** If the scratch org is on a Salesforce first-party instance, other users can log in using `test.salesforce.com` or the My Domain
URL.

**•** If the scratch org is on a Hyperforce instance, other users must log in using the My Domain URL.

### Create a Scratch Org User

Although scratch orgs were designed to be used by one developer, sometimes you need other users to test with different profiles
and permission sets.

User Definition File for Customizing a Scratch Org User
To customize a new scratch org user, rather than use the default and generated values, create a definition file.

Generate or Change a Password for a Scratch Org User
By default, new scratch orgs contain one administrator user with no password. Use the `org generate password` CLI command
to generate or change a password for this admin user. After it's set, you can’t unset a password, you can only change it.

SEE ALSO:

[User Object API Reference](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_user.htm)

[UserRole Object API Reference](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_role.htm)

### Create a Scratch Org User

Although scratch orgs were designed to be used by one developer, sometimes you need other users to test with different profiles and
permission sets.

Use the `org create user` command to create a user. Specify the `--set-alias` flag to assign a simple name to the user that
you can reference in later CLI commands. When the command completes, it outputs the new username and user ID.

```
   sf org create user --set-alias qa-user --target-org my-scratch

   Successfully created user "1690397809_test-st9thgoyyyq3@example.com" with ID 0058I002inzvQAA

```


Scratch Orgs Create a Scratch Org User

```
    for org 00D80000PhAkUAK.

   See more details about this user by running "sf org user display -o

   1690397809774_test-st9thgoyyyq3@example.com".

```

Users are associated with a specific scratch org. Specify the scratch org username or alias at the command line with the `--target-org`
flag if it isn’t already set as the default. If you try to create a user for a non-scratch org, the `org create user` command fails.

You can customize the new user by creating a definition file and specifying it with the `--definition-file` flag.

```
   sf org create user --set-alias qa-user --definition-file config/user-def.json

```

View the list of users associated with a scratch org with the `org list users` command. The (A) on the left identifies the administrator
user that was created when the scratch org was created.

```
   sf org list users --target-org my-scratch

   === Users in org 00D80000PhAkUAK

    Default Alias Username Profile Name User

    Id

    ────────────────────────────────────────────────────────────────────────────────

   ───────────────

    (A) my-scratch test-st9thgoyyyq3@example.com System Administrator

   0058I002inzvQAA

         qa-user 1690397809_test-st9thgoyyyq3@example.com Standard User

   0058I002inzvQAA

```

Display details about a user with the `org display user` command.

```
   sf org display user --target-org qa-user

   Warning: Secrets are now hidden from 'sf org display user' command output. Use the 'sf org

    auth' commands instead. <truncated for readability>

   === User Description

    key label

    ────────────

   ────────────────────────────────────────────────────────────────────────────────────────────────────────────────

    Username 1690397809_test-st9thgoyyyq3@example.com

    Profile Name Standard User

    Id 0058I002inzvQAA

    Org Id 00D80000PhAkUAK

    Access Token [REDACTED] Use 'sf org auth show-access-token' to view

    Instance Url https://connect-enterprise-1121-dev-ed.scratch.my.salesforce.com

    Login Url https://connect-enterprise-1121-dev-ed.scratch.my.salesforce.com

    Alias qa-user

```

Display sensitive information (access token, password, and SFDX Auth URL) about a user with these `org auth` commands.


### Scratch Orgs User Definition File for Customizing a Scratch Org User

**•** `org auth show-access-token`

**•** `org auth show-sfdx-auth-url`

**•** `org auth show-password`

### User Definition File for Customizing a Scratch Org User

To customize a new scratch org user, rather than use the default and generated values, create a definition file.

The user definition file uses JSON format and can include any Salesforce User object field and these Salesforce DX-specific options.

The user definition file options are case-insensitive. However, we recommend that you use lower camel case for the Salesforce DX-specific
options and upper camel case for the User object fields. This format is consistent with other Salesforce DX definition files.


### Scratch Orgs Generate or Change a Password for a Scratch Org User

This user definition file includes some User object fields and all four Salesforce DX options ( `profileName`, `permsets`,
`generatePassword`, and `roleDeveloperName` ).

```
   {

      "Username": "tester1@sfdx.org",

      "LastName": "Hobbs",

      "Email": "tester1@sfdx.org",

      "Alias": "tester1",

      "TimeZoneSidKey": "America/Denver",

      "LocaleSidKey": "en_US",

      "EmailEncodingKey": "UTF-8",

      "LanguageLocaleKey": "en_US",

      "profileName": "Standard Platform User",

      "permsets": ["Dreamhouse", "Cloudhouse"],

      "generatePassword": true,

      "roleDeveloperName": "Customer_Support"

   }

```

In the example, the username `tester1@sfdx.org` must be unique across the entire Salesforce ecosystem. Otherwise, the `org`
`create user` command fails. We recommend that you use the `--set-unique-username` flag, which overrides the value
in the configuration file and ensures a unique username. The alias in the Alias option is different from the alias that you specify with the
`--set-alias` flag of `org create user` . Use the Alias option only with the Salesforce UI. The `--set-alias` flag is local to
the computer from which you run the CLI, and you can use it with other CLI commands.

Indicate the path to the user definition file with the `--definition-file` flag. You can name this file whatever you like and store
it anywhere the CLI can access.

```
   sf org create user --set-alias qa-user --definition-file config/user-def.json --target-org

    my-scratch

```

You can override an option in the user definition file by specifying it as a name-value pair at the command line. This technique allows
multiple users or continuous integration jobs to share a base definition file and then customize options when they run the command.
This example overrides the username, list of permission sets, and whether to generate a password.

```
   sf org create user --set-alias qa-user --definition-file config/user-def.json

   permsets="Dreamy,Cloudy" Username=tester345@sfdx.org generatePassword=false --target-org

   my-scratch

```

You can also add options at the command line that aren’t in the user definition file. This example adds the City option.

```
   sf org create user --set-alias qa-user --definition-file config/user-def.json City=Oakland

    --target-org my-scratch

```

SEE ALSO:

[User sObject API Reference](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_user.htm)

### Generate or Change a Password for a Scratch Org User

By default, new scratch orgs contain one administrator user with no password. Use the `org generate password` CLI command
to generate or change a password for this admin user. After it's set, you can’t unset a password, you can only change it.

You can also use the `--on-behalf-of` flag to generate a password for a scratch org user that you've created locally with the `org`
`create user` command. You can’t use the `org generate password` command for users that you created in the scratch
org with Setup.


Scratch Orgs Generate or Change a Password for a Scratch Org User

**1.** Generate a password for a scratch org user with this command:

```
     sf org generate password --target-org <username-or-alias>

```

You can run this command for scratch org users only. The command outputs the generated password.

The target org must be the username or alias for the scratch org admin user. Use the `--on-behalf-of` flag to assign passwords
to multiple users at once, including admin users, or to users who don’t have permissions to do it themselves. Specify multiple locally
created users by specifying multiple `--on-behalf-of` flags. For example, let’s say the my-scratch alias corresponds to the
scratch org’s admin user, and you want to generate a password for users with aliases `ci-user` and `qa-user` :

```
     sf org generate password --target-org my-scratch --on-behalf-of ci-user --on-behalf-of

      qa-user

```

By default, the command generates a password that's 13 characters in length; the possible characters include all lower and upper
case letters, numbers, and symbols. To change the password strength, use the `--length` and `--complexity` flags. The
`--complexity` flag is a number from 0 through 5; the higher the value, the more possible characters are used, which strengthens
the password. The default value is 5. See the command-line help for a description of each value. This example shows how to generate
a password that's 20 characters long:

```
     sf org generate password --target-org my-scratch --length 20

```

**2.** View the generated password and other user details with the `org display user` and `org auth` commands:

```
     sf org display user --target-org qa-user

     Warning: Secrets are now hidden from 'sf org display user' command output. Use the 'sf

      org auth' commands instead. <truncated for readability>

     === User Description

      key label

      ────────────

     ────────────────────────────────────────────────────────────────────────────────────────────────────────────────

      Username 1690397809_test-st9thgoyyyq3@example.com

      Profile Name Standard User

      Id 0058I002inzvQAA

      Org Id 00D80000PhAkUAK

      Access Token [REDACTED] Use 'sf org auth show-access-token' to view

      Instance Url https://connect-enterprise-1121-dev-ed.scratch.my.salesforce.com

      Login Url https://connect-enterprise-1121-dev-ed.scratch.my.salesforce.com

      Alias qa-user

     sf org auth show-user-password --target-org qa-user

     � You're about to reveal the password for "agentdx258_test1@trailhead.th". Do you want

      to continue? Yes

     ┌──────────┬──────────────────────┐

     │Key │Value │

     ├──────────┼──────────────────────┤

     │Password │bgzz_8hOmeftqvrfxxgi │

     └──────────┴──────────────────────┘

     sf org auth show-access-token --target-org qa-user

     � You're about to reveal the access token for "qa-user". This token grants full access

      to the org with your current permissions. Sharing or logging

     this token is equivalent to sharing your credentials. Do you want to continue? Yes

```


## Scratch Orgs Manage Scratch Orgs from the Dev Hub Org

```
     ┌──────────────┬────────────────────────────|

     │Key │Value |

     ├──────────────┼────────────────────────────|

     │Access Token │00DWs00000GuX<truncated> |

     └──────────────┴────────────────────────────|

```

**3.** Log in to the scratch org with the new password:

**a.** From the `org display user` output, copy the value of the Instance URL and paste it into your browser. In our example,
the instance URL is `https://connect-enterprise-1121-dev-ed.scratch.my.salesforce.com` .

**b.** If you’ve already opened the scratch org with the `org open` command, you’re automatically logged in again. To try out the
new password, log out and enter the username and password listed in the output of the `org display user` command.

**c.** Click **Log In to Sandbox** .

Note: If you change a scratch org user’s password using the Salesforce UI, the new password doesn’t show up in the `org`
`display user` output.

## Manage Scratch Orgs from the Dev Hub Org

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

Deleting the request (ScratchOrgInfo) also deletes the active scratch org.

SEE ALSO:

Add Salesforce DX Users

## Scratch Org Error Codes

If scratch org creation fails, the system generates an error code that can help you identify the cause. Some of these errors are generated
by the SignupRequest API and apply to all org signups.


Scratch Orgs Scratch Org Error Codes

Note: These error codes are specific to scratch org signups. Additional error codes for other org signup scenarios are included in
the _Object Reference for the Salesforce Platform_ [: SignupRequest.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_signuprequest.htm)


# CHAPTER 7 Sandboxes

USER PERMISSIONS

To view a sandbox:

**•** View Setup and
Configuration

To create, refresh, activate,
and delete a sandbox:

**•** Manage Dev Sandboxes
(Developer or Developer
Pro only) or Manage
# Sandboxes (all sandbox

types)

In this chapter ...

**•** Authorize Your
Production Org

**•** Create a Sandbox
Definition File

# Sandboxes are copies of your Salesforce org that you can use for

development, testing, and training, without compromising the
data and applications in your production org.

Salesforce offers sandboxes and a set of deployment tools, so you
can:

**•** Isolate customization and development work from your

**•** Create, Clone, or
production environment until you’re ready to deploy changes.
Refresh a Sandbox

**•** Test changes against copies of your production data and users.

**•** Provide a training environment.

**•** Coordinate individual changes into one deployment to
production.

Traditionally, you or your admin has created and managed your
sandboxes through the Setup UI. But we realize that many developers want the ability to create and
manage their developer and testing environments programmatically, and to automate their CI processes.
Salesforce CLI enables you to do both.

Alternatives to sandboxes are scratch orgs and Developer Edition orgs, which are used as development
environments for many Salesforce development use cases. If you’re wondering whether to use a sandbox,
scratch org, or Developer Edition org as your development environment, you’re not alone. To help you
[better understand which to choose, see the Salesforce Developers Blog: Choose the Right Salesforce](https://developer.salesforce.com/blogs/2024/05/choose-the-right-salesforce-org-for-the-right-job)
[Org for the Right Job.](https://developer.salesforce.com/blogs/2024/05/choose-the-right-salesforce-org-for-the-right-job)


## Sandboxes Authorize Your Production Org Authorize Your Production Org

JWT and Web-based flows require a production org with sandbox licenses instead of a Dev Hub. However, it’s OK if your production org
is also a Dev Hub org.

[The examples in Authorize an Org Using the JWT-Based Flow and Authorize an Org Using the Web-Based Flow are geared toward scratch](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_auth_jwt_flow.htm#sfdx_dev_auth_jwt_flow)
orgs. Follow these tips to successfully authorize your production org.

**•** Be sure to use _`https://login.salesforce.com`_ for `sfdcLoginUrl` in `sfdx-project.json` file. Alternatively,
you can use `org login jwt --instance-url` to specify the URL directly on the command line. This value overrides the
login URL you specified in the `sfdx-project.json` file.

**•** Specify the username for your production org when running the `org login jwt` command. No need to specify a Dev Hub or
indicate a default Dev Hub.

**•** The JWT authorization flow requires that you create a connected app. When you create the connected app, log in to your production
org, not a Dev Hub org.

## Create a Sandbox Definition File

Before you can create a sandbox using Salesforce CLI, define the configuration for it in a sandbox definition file. The sandbox definition
file is a blueprint for the sandbox. You can create different definition files for each sandbox type that you use in the development process.

Sandbox Configuration Values


Sandboxes Create a Sandbox Definition File


Sandboxes Create a Sandbox Definition File

Sample Sandbox Definition File

Although you can place the sandbox definition file anywhere, we recommend keeping it in your Salesforce DX project in the `config`
directory. When naming the file, we suggest providing a descriptive name that ends in `sandbox-def.json`, for example,
`developer-sandbox-def.json` .

Here's a sample definition file for creating a sandbox:

```
{

   "sandboxName": "dev1",

   "licenseType": "Developer"

}

```

Here's a sample definition file for cloning a sandbox:

```
{

   "sandboxName": "dev1clone",

   "sourceSandboxName": "dev1"

}

```


## Sandboxes Create, Clone, or Refresh a Sandbox

Here's a sample definition file for creating a sandbox with the `features` option:

```
   {

       "sandboxName": "dev1",

       "licenseType": "Developer" or "Developer_Pro",

       "features": "['SandboxStorage']"

   }

```

SEE ALSO:

_Tooling API_ [: SandboxInfo](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_tooling.meta/api_tooling/tooling_api_objects_sandboxinfo.htm)

_Salesforce Help_ [: Public and Personal Groups](https://help.salesforce.com/articleView?id=user_groups.htm&language=en_US)

## Create, Clone, or Refresh a Sandbox

Create a sandbox to use for development, testing, or training. Clone a sandbox to copy its data and metadata to another sandbox. Refresh
an existing sandbox to get the latest metadata, and sometimes data, from the source org.

Before you create or clone a sandbox:

**•** Create a Salesforce DX project with a manifest file.

**•** Authorize to a production org with available sandbox licenses.

**•** Create the sandbox definition file.

Why We Recommend Using Aliases

When you create or clone a sandbox, the usernames generated in the sandbox are based on the usernames present in the production
org or sandbox. The username looks like an email address, such as `username@company.com.dev1` . If the resulting username
isn’t unique, we prepend some characters and digits to the username. The modified username looks something like
`00x7Vqusername@company.com.dev1` .

As you can imagine, remembering these usernames can be challenging, especially if you have several sandboxes you’re managing.
Aliasing is a powerful way to manage and track your orgs, and we consider it a best practice. So when you issue a command that requires
the username, using an alias that you can remember can speed up things.

If you didn’t set an alias when you created the sandbox, you can set one later.

```
   sf alias set MyDevSandbox username@company.com.dev1

```

Create a Sandbox

Optional: Create a Sandbox Definition File

When you create a sandbox, Salesforce copies the metadata and data (for Partial Copy and Full) from your production org to a sandbox
org. Specify the username or alias of your production org with the `--target-org` flag.

```
   sf org create sandbox --target-org prodOrg --definition-file config/dev-sandbox-def.json

   --alias MyDevSandbox --set-default --wait 30

```

The command asks you to confirm the sandbox configuration and then shows information as the sandbox is being created.

The `--set-default` flag indicates that this sandbox is your default org for all CLI commands. If you’re working with several orgs
and you don’t want this one to be the default, exclude this flag.


Sandboxes Create, Clone, or Refresh a Sandbox

To directly define the required sandbox options, or to override the values defined in the sandbox definition file, specify appropriate flags
on the command line.

```
   sf org create sandbox --name FullSbx --license-type=Full --target-org prodOrg --alias

   MyFullSandbox --wait 30

```

Tip: Because the sandbox is processed in a queue, the sandbox creation process can take longer than the default wait time of 6
minutes. We recommend setting a larger value for `--wait`, for example, 30 minutes.

How long the creation process takes depends on the size and complexity of your production org. You see status messages posted to
output:

```
   Sandbox Create... � 00:28:00 until timeout. 26%

    Field Value

    ─────────────────────────────────────────

    Id 0GR1Q888800HORuWAO

    SandboxName dev11

    Status Processing

    LicenseType DEVELOPER

    SandboxInfoId 0GQ1Q000009999mWAO

    Created Date 2023-10-17T21:42:49.000+0000

    CopyProgress 26%

    SandboxOrg 00DP0099993zEZj

   --------------------
   Sandbox Create Stages

   � - Pending

   … - Processing

   … - Activating

   … - Authenticating

```

After the wait period is over, you can run the `org resume sandbox` command to check the status of the sandbox creation process.
If the sandbox is created within the wait time, Salesforce CLI automatically authenticates in to the sandbox. And the sandbox appears
in the output of the `org list` command. Team members can authenticate to the sandbox by running the `org web login`
command and providing their usernames and passwords.

```
   sf org web login --instance-url https://test.salesforce.com

```

Clone a Sandbox

You can create a sandbox by cloning an existing sandbox rather than using your production org as your source. You can save time by
customizing a sandbox with a set of data and metadata and then replicating it. Use the `--source-sandbox-name` flag to specify
the existing sandbox name and the `--name` flag to the name of the new sandbox. You can also use the `--sourceId` flag to specify
the existing sandbox by its ID rather than its name. Both sandboxes must be associated with the specified production org that contains
the sandbox licenses. ( `--target-org` flag).

Sandbox cloning simplifies having multiple concurrent streams of work in your application lifecycle. You can set up a sandbox for each
type of work, such as development, testing, and staging. Your colleagues can easily clone individual sandboxes instead of sharing one
sandbox and stepping on each other’s toes.

```
   sf org create sandbox --source-sandbox-name FullSbx --name NewSbx --target-org prodOrg

   --alias MyDevSandbox --set-default --wait 30

```

Tip: Because the sandbox is processed in a queue, the sandbox cloning process can take longer than the default wait time of 6
minutes. We recommend setting a larger value for `--wait`, for example, 30 minutes.


Sandboxes Create, Clone, or Refresh a Sandbox

After the wait period is over, you can run the `org resume sandbox` command to check the status of the sandbox cloning process.
If the sandbox is cloned within the wait time, the CLI automatically authenticates in to the sandbox. And the sandbox appears in the
output of the `org list` command. Team members can authenticate to the sandbox by running the `org web login` command
and providing their usernames and passwords.

```
   sf org web login --instance-url https://test.salesforce.com

```

Check the Sandbox Status

Creating or cloning a sandbox can take several minutes. If the command times out, it displays a job ID that you can pass to the `org`
`resume sandbox` command to report on creation or cloning status. When the sandbox is ready, this command also authenticates
to the sandbox.

```
   sf org resume sandbox --job-id 0GR1888880000HORuWAO --target-org prodOrg

```

If the `org create sandbox` command times out, the alias isn’t set. However, you can set it using the `alias set` command:

```
   sf alias set MyDevSandbox username@company.com.dev1

```

Open a Sandbox

After the sandbox is ready, you can open it by specifying its username or alias. However, you don’t have to provide its password because
the CLI manages the authentication details for you.

```
   sf org open --target-org MyDevSandbox

```

Refresh a Sandbox

Refreshing an existing sandbox updates its metadata from the source org. If the sandbox is a clone or if it uses a sandbox template, the
refresh process also updates the sandbox org’s data.

```
   sf org refresh sandbox --name FullSbx --target-org prodOrg

```

Be sure the value of `--name` is the sandbox name, and not its alias. The `--target-org` flag can be either the username or alias
of the source org.

To change the configuration of the refreshed sandbox, specify a definition file with the `--definition-file` flag. Then include
the configuration options you want to change, such as `licenseType`, `templateID`, or `copyArchivedActivities` (full
sandbox only.) You can’t, however, change the sandbox name using the `org refresh sandbox` command. To change the
sandbox name, first delete it with the `org delete sandbox` command. Then recreate it with the `org create sandbox`
command and give it a new name.

Delete a Sandbox

You can delete a sandbox using Salesforce CLI, whether you created it locally with `org create sandbox` or logged into an existing
sandbox with a `org login` command. You must also have previously logged into the production org that contains the sandbox
license.

```
   sf org delete sandbox --target-org MyDevSandbox

```


Sandboxes Create, Clone, or Refresh a Sandbox

Next:

**•** Retrieve metadata from your sandbox to your local DX project.

**•** Develop directly in your sandbox, then retrieve the changes to your local DX project.

**•** Deploy local changes to a sandbox.

SEE ALSO:

_Salesforce Help_ [: Deploy Enhancements from Sandboxes](https://help.salesforce.com/articleView?id=deploy_sandboxes_parent.htm&language=en_US)

_Salesforce Help_ [: Create, Clone, or Refresh a Sandbox Using Setup UI](https://help.salesforce.com/articleView?id=data_sandbox_create_parent.htm&language=en_US)

Authorize an Org Using the JWT Flow

Authorize an Org Using a Browser


# CHAPTER 8 Track Changes Between Your Project and Org

In this chapter ... Use source tracking to track the changes between your local project and a scratch org or sandbox when
you create, update, or delete source code.

**•** Manage Source
Source tracking has no direct effect on the org; it affects only your local environment. Specifically,
Tracking for Your org
Salesforce CLI checks a local configuration file to determine whether you’ve enabled source tracking for

**•** Preview Changes

a particular org. If you have, then source tracking operations are executed when you work with the org,

Identified by Source

such as using the `project deploy start` command.

Tracking

The `project deploy|retrieve start` commands without flags deploy or retrieve all changed

**•** Deploy and Retrieve
Changes Identified source between your local project and the target org. For more granular control, use flags to specify
by Source Tracking specific metadata components, package directories, or manifest files to deploy or retrieve. This example
retrieves the `MyFabClass` Apex class:

**•** Resolve Conflicts
Between Your Local
Project and Org

```
sf project retrieve start --metadata ApexClass:MyFabClass

```

In addition to listing the changes you make, source tracking makes it possible to:

**•** Best Practices

**•** Performance **•** Automatically track changes to metadata components, saving you from tracking them manually.
Considerations of **•** See changes deployed to a sandbox by other developers.
Source Tracking

**•** See changes deployed to a sandbox by other developers.

**•** Deploy or retrieve changed source.

**•** Identify and resolve conflicts between your local project and scratch org or sandbox before deploying
or retrieving source.

To see which metadata components support source tracking, check the Source Tracking column of the
[Metadata Coverage Report.](https://developer.salesforce.com/docs/success/metadata-coverage-report/references/coverage-report/metadata-coverage-report.html)


## Track Changes Between Your Project and Org Manage Source Tracking for Your org Manage Source Tracking for Your org

Source tracking works only if your target org allows it. Don’t worry, you can still deploy or retrieve metadata to and from an org without
source tracking. But the commands don’t check for conflicts, and you must specify exactly what you want to deploy or retrieve using an
appropriate flag, such as `--source-dir` or `--metadata` .

Org Editions that Support Source Tracking

**•** Developer Edition orgs, production orgs, Partial Copy sandboxes, and Full sandboxes—Source tracking isn’t supported.

**•** Developer and Developer Pro sandboxes—Source tracking is supported if their associated production org has been enabled for
source tracking.

**•** Scratch orgs—Source tracking is always supported.

Manage Source Tracking in New Orgs

Scratch Orgs have source tracking enabled by default. For Developer and Developer Pro sandboxes, source tracking is also enabled by
default as long as their associated production org has been enabled for source tracking.

You can opt out of source tracking when you create the scratch org or sandbox by specifying the `--no-track-source` flag of the
`org create scratch|sandbox` command. This flag affects only your local configuration, not the org itself. Salesforce CLI sets
a local configuration option `trackSource: false` as part of your authorization information to the org. If you log out of the org
and then log back in again, source tracking is enabled again by default.

Here’s how to create a scratch org with source tracking disabled.

```
    sf org create scratch --target-dev-hub=MyHub --definition-file

   config/project-scratch-def.json --no-track-source

```

Here’s a sandbox example.

```
   sf org create sandbox --definition-file config/dev-sandbox-def.json --target-org prodOrg

   --no-track-source

```

Manage Source Tracking in Existing Orgs

You can change whether an existing scratch org or sandbox allows source tracking with these two commands:

**•** `org enable tracking` : Allow Salesforce CLI to track changes in your source files between your project and an org.

**•** `org disable tracking` : Prevent Salesforce CLI from tracking changes in your source files between your project and an org.

This example shows how to enable source tracking in an org with alias `mySandbox` ; the command returns an error if the org doesn't
support tracking, such as a Full sandbox.

```
   sf org enable tracking --target-org mySandbox

```


## Track Changes Between Your Project and Org Preview Changes Identified by Source Tracking

Let’s say you have a sandbox that you use for integration tests, and you want to deploy source to it but not wait for tracking operations.
This example shows how to disable source tracking on an org with alias `mySandbox` :

```
   sf org disable tracking --target-org mySandbox

```

SEE ALSO:

_VS Code Command_ [: SFDX: Create a Default Scratch Org](https://developer.salesforce.com/docs/platform/sfvscode-extensions/guide/vscode-overview.html)

## Preview Changes Identified by Source Tracking

To see changes between your local project and target org, navigate to the project directory for which you want to see changes. Then
run one of the preview commands, which display either the local changes in your project you can deploy to your org, or the org changes
that you can retrieve.

**1.** In a terminal or command window, navigate to the project directory. In this example, the directory is named MyProject.

```
     cd /Users/joe/dx-projects/MyProject

```

**2.** To see what’s changed between your project and org, run either the `project deploy preview` or `project retrieve`
`preview` command. Include the `--target-org` flag to specify the username or alias of the scratch org or sandbox that you
want to compare with your local project. In this example, the command displays the local changes that can be deployed to the
sandbox with the alias `DevSandbox` .

```
     sf project deploy preview --target-org DevSandbox

```

Similarly, this example displays the remote changes in the sandbox that can be retrieved back into the local project.

```
     sf project retrieve preview --target-org DevSandbox

```

The `project deploy preview` command accepts the `--metadata`, `--source-dir`, and `--manifest` flags,
which you can use to preview more granular deployments. This example previews a deployment of only `ApexClass` metadata:

```
     sf project deploy preview --metadata ApexClass --target-org DevSandbox

```

This `project deploy preview` sample output shows that there are local changes to the `WidgetClass` Apex class and
WidgetObject__c custom object that can be deployed to the org.

```
   sf project deploy preview --target-org DevSandbox

   No conflicts found.

   No files will be deleted.

   Will Deploy [2] files.

    Type Fullname Path

    ───────────────────────────

   ──────────────────────────────────────────────────────────────────────────────

    ApexClass WidgetClass force-app/main/default/classes/WidgetClass.cls-meta.xml

    CustomObject WidgetObject__c

   force-app/main/default/objects/WidgetObject__c/WidgetObject__c.object-meta.xml

```


## Track Changes Between Your Project and Org Deploy and Retrieve Changes Identified by Source Tracking

```
   No files were ignored. Update your .forceignore file if you want to ignore certain files.

```

This `project retrieve preview` sample output shows that there are remote changes to the `GizmoClass` Apex class and
GizmoObject__c custom object (and its layout) that can be retrieved from the org to the local project. The output also shows that there
are no conflicts between the project and org.

```
   sf project retrieve preview --target-org DevSandbox

   No conflicts found.

   No files will be deleted.

   Will Retrieve [3] files.

    Type Fullname Path

    ─────────────────────────────────────────────────

    Layout GizmoObject__c-GizmoObject Layout

    CustomObject GizmoObject__c

    ApexClass GizmoClass

   Ignored [2] files. These files won't retrieve because they're ignored by your .forceignore

    file.

    Type Fullname Path

    ──────────────────────────────────────────────

    Profile Admin

    Profile B2B Reordering Portal Buyer Profile

```

The preview commands use tables of change information with three columns: Type, Fullname, and Path. Each row represents one
change.

**•** _Type_ is the changed component’s metadata type. It describes what the component is, such as an Apex class or a custom object.

**•** _Fullname_ is the API name of the component.

**•** _Path_ is the location of the component in your local project. If it’s blank, the component isn’t present in your local project. When
blank, it usually means that a component is present in the org but not in your local project.

If source tracking doesn’t detect any changes, then the preview commands return a statement saying `No results found` .

```
   === Source Status

   No results found

```

After previewing the changes in the source in your local project and the org, you’re ready to deploy or retrieve and resolve potential
conflicts.

## Deploy and Retrieve Changes Identified by Source Tracking

When you create a Salesforce app, you typically use both low-code and pro-code techniques. An example of low-code is creating a
custom object directly in an org using Setup. An example of pro-code is creating an Apex class in your local project using an IDE, such
as VS Code. As you work, source tracking identifies changes so you can keep the remote metadata in the org in sync with the source in
your local project.

The process is iterative. First you preview the remote and local changes. If conflicts exist, you resolve them. You must now ensure that
these changes exist in both the org and your local project. So you retrieve the remote changes to your local project, then push them to
your source control repository, to ensure that the source control system contains all your changes and is the source of historical truth.


Track Changes Between Your Project and Org Deploy and Retrieve Changes Identified by Source Tracking

You deploy your local changes, such as Apex code, to the org so you can validate and test it. And you keep iterating through this process
until you finish developing the Salesforce app.

To see source tracking in action, let’s look at some examples.

Say you run `project retrieve preview` and see remote changes.

```
   sf project retrieve preview --target-org DevSandbox

   No conflicts found.

   No files will be deleted.

   Will Retrieve [3] files.

    Type Fullname Path

    ─────────────────────────────────────────────────

    Layout GizmoObject__c-GizmoObject Layout

    CustomObject GizmoObject__c

    ApexClass GizmoClass

   Ignored [2] files. These files won't retrieve because they're ignored by your .forceignore

    file.

    Type Fullname Path

    ──────────────────────────────────────────────

    Profile Admin

    Profile B2B Reordering Portal Buyer Profile

```

Retrieve the changes in your org to your local project with the `project retrieve start` command. Now that the components
have been created locally, the Path column has a value and it includes the default package directory.

```
   sf project retrieve start --target-org DevSandbox

   Preparing retrieve request... � Sending request to org

   Preparing retrieve request... Succeeded

   Retrieved Source

   =========================================================================================================================================

   | State Name Type Path

   | ────────────────────────────────────────────────────

   ────────────────────────────────────────────────────────────────────────────────

   | Created GizmoClass ApexClass

   force-app/main/default/classes/GizmoClass.cls

   | Created GizmoClass ApexClass

   force-app/main/default/classes/GizmoClass.cls-meta.xml

   | Created GizmoObject__c CustomObject

   force-app/main/default/objects/GizmoObject__c/GizmoObject__c.object-meta.xml

   | Created GizmoObject__c-GizmoObject Layout Layout

   force-app/main/default/layouts/GizmoObject__c-GizmoObject Layout.layout-meta.xml

```

After retrieving the source, run `project retrieve preview` again. Now, source tracking reports that there’s nothing to retrieve.

```
   sf project retrieve preview

   No conflicts found.

   No files will be deleted.

```


Track Changes Between Your Project and Org Deploy and Retrieve Changes Identified by Source Tracking

```
   No files will be retrieved.

   Ignored [2] files. These files won't retrieve because they're ignored by your .forceignore

    file.

    Type Fullname Path

    ──────────────────────────────────────────────

    Profile Admin

    Profile B2B Reordering Portal Buyer Profile

```

Let’s now look at deploying. To preview your local changes, run `project deploy preview` .

```
   sf project deploy preview --target-org DevSandbox

   No conflicts found.

   No files will be deleted.

   Will Deploy [2] files.

    Type Fullname Path

    ───────────────────────────

   ──────────────────────────────────────────────────────────────────────────────

    ApexClass WidgetClass force-app/main/default/classes/WidgetClass.cls-meta.xml

    CustomObject WidgetObject__c

   force-app/main/default/objects/WidgetObject__c/WidgetObject__c.object-meta.xml

   No files were ignored. Update your .forceignore file if you want to ignore certain files.

```

Then deploy your local changes. After deploying to a sandbox, other developers that are using the sandbox can see your changes.

```
   sf project deploy start --target-org DevSandbox

   Deploying v59.0 metadata to test-ikspctiorkzs@example.com using the v59.0 SOAP API.

   Deploy ID: 0Af8D00000pNmKySAK

   Status: Succeeded | ████████████████████████████████████████| 2/2 Components (Errors:0)

   | 0/0 Tests (Errors:0)

   Deployed Source

   =====================================================================================================================

   | State Name Type Path

   | ──────────────────────────────────

   ──────────────────────────────────────────────────────────────────────────────

   | Created WidgetClass ApexClass force-app/main/default/classes/WidgetClass.cls

   | Created WidgetClass ApexClass

   force-app/main/default/classes/WidgetClass.cls-meta.xml

   | Created WidgetObject__c CustomObject

   force-app/main/default/objects/WidgetObject__c/WidgetObject__c.object-meta.xml

```

Run `project deploy preview` again.

```
   sf project deploy preview

   No conflicts found.

```


### Track Changes Between Your Project and Org Retrieve Changes to Profiles with Source Tracking

```
   No files will be deleted.

   No files will be deployed.

   No files were ignored. Update your .forceignore file if you want to ignore certain files.

```

The command reports there’s nothing to deploy, indicating that your local project and the org are synchronized.

### Retrieve Changes to Profiles with Source Tracking

Retrieving profiles behaves a little differently with source tracking.

SEE ALSO:

_VS Code Command_ [: SFDX: Deploy|Retrieve Source to|from Org](https://developer.salesforce.com/docs/platform/sfvscode-extensions/guide/deploy-changes.html)

### Retrieve Changes to Profiles with Source Tracking

Retrieving profiles behaves a little differently with source tracking.

Important: In general, we recommend that you use permission sets instead of profiles. Profiles aren’t consistent across orgs, and
the source files that are retrieved and deployed depend on the org type, the tracking state, and other metadata in the operation.
If you decide to continue using profiles, we recommend that you exclude them when you deploy or retrieve by adding them to
the `.forceignore` file.

Without source tracking, retrieving profiles only returns some profile information. Retrieving profiles returns information about profiles
that pertains to other items specified in the `package.xml` file.

For example, retrieving profiles with this `package.xml` file returns profile permissions for the MyCustomField__c custom field on
the Account object.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

    <types>

     <members>Account.MyCustomField__c</members>

     <name>CustomField</name>

    </types>

    <types>

     <members>*</members>

     <name>Profile</name>

    </types>

    <version>50.0</version>

   </Package>

```

With source tracking, retrieving profiles returns profile information pertaining to anything else specified in the `package.xml` file
plus any components getting tracked by source tracking. That includes any entity for which a change exists between your local project
and the org.


## Track Changes Between Your Project and Org Resolve Conflicts Between Your Local Project and Org

For example, say you create a custom field on the Opportunity object called OppCustomField__c in your local environment. Source
tracking detects the change and reports it. Now you retrieve profiles using the same `package.xml` file as you did when source
tracking was off.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

    <types>

     <members>Account.MyCustomField__c</members>

     <name>CustomField</name>

    </types>

    <types>

     <members>*</members>

     <name>Profile</name>

    </types>

    <version>50.0</version>

   </Package>

```

Even though the `package.xml` file doesn’t reference OppCustomField__c, because source tracking is tracking the new custom field,
your retrieve returns profile permissions for both the MyCustomField__c custom field on the Account object and the OppCustomField__c
on the Opportunity object.

[For more information about retrieving profiles, see the Profile metadata type in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_profile.htm) _Metadata API Developer Guide_ .

Note: Although source retrieves don’t include `package.xml` files, retrieve requests return profile information pertaining to
everything reported by source tracking.

SEE ALSO:

_Salesforce Help_ [: Permission Sets](https://help.salesforce.com/s/articleView?id=platform.perm_sets_overview.htm&type=5&language=en_US)

How to Exclude Source When Syncing

## Resolve Conflicts Between Your Local Project and Org

As a best practice, if conflicts exist for components in your local project or in the org, resolve them before moving forward. You can
resolve the conflict manually, or overwrite one version of a component with another. Only overwrite changes if you're certain that the
new version is the one you want to use.

Say you run `project deploy preview` and see conflicting changes between your local project and in the org. For example,
this command output shows that `WidgetClass` has conflicting changes but `GizmoClass` is ready to be deployed.

```
   sf project deploy preview --target-org DevSandbox

   Conflicts [1]. Run the command with the --ignore-conflicts flag to override.

    Type Fullname Path

    ───────────────────────────────────────────────────────────────────────────

    ApexClass WidgetClass force-app/main/default/classes/WidgetClass.cls-meta.xml

   No files will be deleted.

   Will Deploy [1] files.

    Type Fullname Path

    ─────────────────────────────────────────────────────────────────────────

    ApexClass GizmoClass force-app/main/default/classes/GizmoClass.cls-meta.xml

```


## Track Changes Between Your Project and Org Best Practices

```
   No files were ignored. Update your .forceignore file if you want to ignore certain files.

```

If you try to actually deploy the source, Salesforce CLI reports the conflict again and stops the operation from completing. You see similar
conflict messages when you run `project retrieve preview` . To successfully deploy or retrieve, first resolve the conflicts, and
then overwrite either your local project or the org with the resolved file. Let’s see how this works.

Overwrite Conflicting Changes

If you decide that the local version is correct, overwrite the conflicting change in the org by including the `--ignore-conflicts`
flag when you deploy. In our example, because only `WidgetClass` has conflicting changes, let’s first deploy just that component
to get rid of the conflicts and then deploy the non-conflicting source later.

```
   sf project deploy start --metadata ApexClass:WidgetClass --ignore-conflicts --target-org

   DevSandbox

```

The DevSandbox org now has the same version of `WidgetClass` that was in your local project. When you run `project deploy`
`preview` again you see no conflicting changes messages.

If, however, you decide that the version of `WidgetClass` in the org is the correct one, overwrite your local copy by retrieving the
DevSandbox org version while ignoring conflicts.

```
   sf project retrieve start --metadata ApexClass:WidgetClass --ignore-conflicts --target-org

    DevSandbox

```

Your local project now has the same version of `WidgetClass` that was in your org.

Well done, you resolved the conflict! Now run `project deploy start` without any special flags to finish deploying `GizmoClass`
and any other new local source.

```
   sf project deploy start --target-org DevSandbox

   Deploying v59.0 metadata to test-ikspctiorkzs@example.com using the v59.0 SOAP API.

   Deploy ID: 0Af8D00000pNtEUSA0

   Status: Succeeded | ████████████████████████████████████████| 1/1 Components (Errors:0)

   | 0/0 Tests (Errors:0)

   Deployed Source

   =====================================================================================

   | State Name Type Path

   | ────────────────────────────────────────────────────────────────────────────────

   | Created GizmoClass ApexClass force-app/main/default/classes/GizmoClass.cls

   | Created GizmoClass ApexClass force-app/main/default/classes/GizmoClass.cls-meta.xml

```

SEE ALSO:

_VS Code Documentation_ [: Detect Conflicts on Deploy](https://developer.salesforce.com/docs/platform/sfvscode-extensions/guide/detect-conflicts.html)

## Best Practices

Get the most out of source tracking by following these best practices.


## Track Changes Between Your Project and Org Performance Considerations of Source Tracking

Retrieve changes and resolve conflicts before deploying your changes to
a sandbox

This practice helps other developers incorporate your changes and facilitates collaboration.

Review metadata change history with a version control system like Git

With a version control system, you can version your changes, track change history, and review metadata changes before promoting to
other environments, such as a sandbox.

Get source tracking files back into sync

If source tracking gets confused and starts reporting inaccuracies, you can use the `project deploy|retrieve start`
commands to get back into sync. Which command you use depends on which source you most trust: use `project deploy start`
if you trust your local source files and `project retrieve start` if you trust what’s in your org. For either command, specify
the `--ignore-conflicts` flag. See Resolve Conflicts Between Your Local Project and Org for details and examples.

## Performance Considerations of Source Tracking

Source tracking performs extra functions to determine changes to source tracked components, such as running more queries and waiting
for the SourceMember Tooling API object to be updated after a deployment. So, some commands can take a little longer to run when
working with medium-to-large sized projects. If you’re working with small projects, you don’t notice any slowdown.

A medium-sized project has 30 or more components or 50 or more tests. A project with 25 components and 51 tests is considered
medium.

A large-sized project is 600 or more components or 150 or more tests. A project with 610 components and 140 tests is considered large.

If you experience long-running commands, break up your projects into smaller sets of components, and deploy the smaller sets.

You can also opt out of source tracking when you create a scratch org or sandbox by specifying the `--no-track-source` flag of
the `org create scratch|sandbox` command. See Source Tracking for use cases.

If creating a scratch org or sandbox for use as a development environment in DevOps Center, don’t disable source tracking.


# CHAPTER 9 Work with Data

In this chapter ... Development environments, such as scratch orgs and developer sandboxes, need a set of stock data for
testing.

**•** Work With Small
Sometimes, the stock data in a development environment doesn’t meet your development needs. Apex
Datasets
tests generally create their own data. Therefore, if Apex tests are the only tests you’re running in a scratch

**•** Work With Large
org, you probably don’t need to worry about data for the time being. However, other tests, such as UI,
Datasets
API, or user acceptance tests, do need baseline data. Scale and performance testing often requires a very

**•** Work With Individual
large set of data. Make sure that you use consistent datasets when you run tests of each type.
Records

Scratch orgs come with the same set of data as the edition on which they’re based. For example, Developer

**•** Run a SOQL or SOSL
Edition orgs typically include 10–15 records for key standard objects, such as Account, Contact, and
Query
Lead. These records come in handy when you’re testing something like a new Apex trigger, flow, or

**•** Upload a File to Your
Lightning web component.
Org

The following sections describe the Salesforce CLI commands you can use to populate your orgs and
provide basic usage examples. The commands you use depend on your current stage of development.

SEE ALSO:

_Salesforce DX Developer Guide_ [: Supported Scratch Org Editions and Allocations](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_scratch_orgs_editions_and_allocations.htm)

_Salesforce Help_ [: Sandbox Licenses and Storage Limits by Type](https://help.salesforce.com/s/articleView?id=platform.data_sandbox_environments.htm&type=5&language=en_US)

_[Salesforce Help](https://help.salesforce.com/s/articleView?id=xcloud.scalability_overview.htm&type=5&language=en_US)_ : Scalability

_Salesforce Help_ [: Secure Your Sandbox Data with Salesforce Data Mask](https://help.salesforce.com/s/articleView?id=platform.data_mask_overview.htm&type=5&language=en_US)


## Work with Data Work With Small Datasets Work With Small Datasets

Use the `data export|import tree` commands to move small sets of data between orgs, such as fewer than 3,000 records.
These commands use JSON files to describe Salesforce records and the relationships between them. Developers can use these commands
to quickly and easily create small sets of representative data in a scratch org when developing or testing their code.

The `data export tree` command uses one or more SOQL queries to select the data in an org that it writes to the JSON files. The
queries can be for one or more Salesforce objects, using either a multi-level relationship query or multiple individual queries. The JSON
files use the sObject tree format, which is a collection of nested parent-child records with a single root record. You then use these JSON
files to import data into an org with the `data import tree` command.

When exporting records from two or more Salesforce objects, we recommend using the `--plan` flag. Specifying this flag generates
separate JSON files for each object and a plan definition file that aggregates them, thus making imports easier. When using plans, you
can export up to five levels of child objects using a relationship query, or export multiple objects that don't necessarily have relationships
by specifying multiple queries.

Let’s look at a few examples to see the power of these commands.

Data from a Single Salesforce Object

For this example, imagine you created a set of useful Account records while working on your application in a scratch org. Exporting
these records allows you to save this data as a JSON file in your version control system. Later, you can use this file to import the same
set of Account records into a new scratch org or sandbox as you continue to develop and refine your application.

This example shows how to export Account records from your default org:

```
   sf data export tree \

   --query "SELECT Name, Industry, TickerSymbol from Account" \

   --output-dir test-data

```

The `--query` flag specifies the SOQL query that selects the records you want to export; in this case it’s very simple and touches just
one object: Account. For simplicity, the example SOQL query includes only a few Account fields, but in real life you include the writable
fields that you want to export. Don’t include fields that aren’t writable, such as formula fields. The `--output-dir` flag specifies the
directory in which to write the single JSON file.

The output JSON file is always named after the queried object, in this case `Account.json` . The file is in the sObject Tree format and
looks something like this:

```
   {

      "records": [

        {

           "attributes": {

             "type": "Account",

             "referenceId": "AccountRef1"

           },

           "Name": "Edge Communications",

           "Industry": "Electronics",

           "TickerSymbol": "EDGE"

        },

        {

           "attributes": {

             "type": "Account",

             "referenceId": "AccountRef2"

           },

```


Work with Data Work With Small Datasets

```
           "Name": "Burlington Textiles Corp of America",

           "Industry": "Apparel",

           "TickerSymbol": "BTXT"

        }

     ]

   }

```

For each record, the `type` key specifies its object, such as Account in our example. The `referenceID` key is a stand-in for a record
ID; when imported into a new org the record gets a different ID than in the org where it was exported from. These stand-in IDs help
preserve relationships, such as lookups, between imported records.

To import these records into a new scratch org, use this CLI command:

```
   sf data import tree \

   --files test-data/Account.json \

   --target-org new-scratch-org

```

You use the `--files` flag to specify the JSON file that has the records, and `--target-org` to specify the org into which you want
to import the records.

Data from Salesforce Objects with Parent/Child Relationships

Now imagine you created a useful set of both Account and Contact records while working on your application in a scratch org. To export
records from both of these objects, you must use a SOQL relationship query. When combined with the `--plan` flag, the query results
in multiple data JSON files and a plan definition file that includes references to preserve the relationships between records from different
objects. As a result, your data is correctly imported into a new org.

Here’s what your new export command looks like. The SOQL query now has a relationship subquery that includes child Contact records
for each Account record found. As before, the SOQL query includes only a few fields, but you can specify any writable fields required by
your dataset:

```
   sf data export tree \

     --query "SELECT Name, Industry, TickerSymbol, (SELECT FirstName, LastName, Email, Phone

    FROM Contacts) FROM Account" \

      --output-dir test-data --plan

```

When the command finishes, the output directory contains an `Account.json` file with the Account records, just as before. But it
also now contains a `Contact.json` file with Contact records, and a file called `Account-Contact-plan.json` that details
the plan for importing all the records. The plan outlines the relationships between the objects that were exported and specifies the order
in which to load them when imported. For example, contacts typically have references to accounts, so the Account records must be
imported before the Contact records.

Here’s the corresponding command to import these records into an org with alias `new-scratch-org` :

```
   sf data import tree \

      --plan test-data/Account-Contact-plan.json --target-org new-scratch-org

```

This import uses the `--plan` flag to specify the name of the plan definition file created by the export command. Without a plan you
must import each object separately, so using a plan makes imports much easier.

Data from Salesforce Objects with Junction Relationships

A junction object is a Salesforce object with two master-detail relationships that models a many-to-many relationship between two
objects. An example of a junction object is AccountContactRelation, which represents a relationship between a contact and one or more
accounts.


## Work with Data Work With Large Datasets

Let’s say you created several many-to-many relationships between your contacts and accounts while working on your application in a
scratch org. To export the records from both these objects while preserving the junction object relationships, you must specify multiple
queries during the export. To do so, use the `--query` flag multiple times when executing the `data export tree` command.
For example, you can combine individual queries against the Account, Contact, and AccountContactRelation objects, ensuring that the
references for all exported data match and can then be imported into a new org.

```
   sf data export tree \

      --query "SELECT Name, Industry, TickerSymbol FROM Account" \

      --query "SELECT FirstName, LastName, Email, Phone FROM Contact" \

      --query "select ID, ContactId, AccountId from AccountContactRelation" \

      --output-dir test-data-junction --plan

```

When executing the `data export tree` with multiple queries, the plan definition file is always named `plan.json` . As always,
this file outlines the relationships between the exported objects and specifies the order in which records are loaded during import. The
import command itself is similar to previous examples.

```
   sf data import tree --plan test-data-junction/plan.json --target-org new-scratch-org

```

Tip: To automatically enable the feature to relate a contact to multiple accounts in a scratch org, specify the
ContactsToMultipleAccounts feature in the scratch org definition file. For example:

```
      {

       "orgName": "Dreamhouse",

       "edition": "Developer",

       "features": ["Walkthroughs", "EnableSetPasswordInApi", "ContactsToMultipleAccounts"],

      …

      }

```

SEE ALSO:

_[Salesforce CLI Command Reference](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_data_commands_unified.htm)_ : data Commands

_[SOQL and SOSL Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_sosl_intro.htm)_

_[REST API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_rest.meta/api_rest/resources_composite_sobject_tree.htm)_ : sObject Tree

_Salesforce Help_ [: Create a Many-to-Many Object Relationship (Junction Objects)](https://help.salesforce.com/s/articleView?id=platform.relationships_manytomany.htm&language=en_US)

_Salesforce Help_ [: Contacts to Multiple Accounts](https://help.salesforce.com/s/articleView?id=sales.shared_contacts_overview.htm&type=5&language=en_US)

_[Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_accountcontactrelation.htm)_ : AccountContactRelation

## Work With Large Datasets

When you’re ready to do more real-world testing, you often need large sets of data, such as millions of records. In this case, you use the
various `data bulk` CLI commands to move the data around, typically between sandboxes. These commands are also useful when
automating data extractions and data loads in production orgs.

Salesforce CLI’s `data bulk` commands use the Salesforce Bulk API 2.0, which is optimized for working with large sets of data. You
can use these CLI commands to import, export, update, upsert, or delete many records asynchronously; collectively these actions are
also known as bulk ingests. The commands work in pairs: first run a command such as `data import bulk` to submit a bulk ingest
request, and then later run `data import resume` to view the status and results. Salesforce processes the request in the background.

Here are the bulk commands:

**•** `data export bulk|resume`

**•** `data import bulk|resume`


Work with Data Work With Large Datasets

**•** `data delete bulk|resume`

**•** `data upsert bulk|resume`

**•** `data update bulk|resume`

**•** `data bulk results`

Let’s see how these commands work.

Bulk Export and Import

Let’s first assume you already have many records in an org that you want to export and store in a file so you can later import them into
another org for scale testing. Use a SOQL query to select the records you want to export; you can query only one Salesforce object. This
example shows how to export records from the Account object from your default org:

```
   sf data export bulk \

      --query "SELECT Name, Phone, Website FROM Account" \

      --output-file accounts.csv --wait 10

```

When the request finishes, the file `accounts.csv` contains the records in comma-separated values (CSV) format. The `--wait` flag
specifies that the command waits for 10 minutes to complete before it times out.

Warning: The `data export bulk` command uses Bulk API 2.0, which limits the type of SOQL queries you can run. For
example, you can’t use clauses such as `GROUP BY` or `LIMIT`, or aggregate functions such as `count()` . For the complete list
of limitations, see the _SOQL Considerations_ section in the _Bulk API Developer Guide_ .

Here are a few other flags you can specify to customize the export.

This example gets the SOQL query from the `soql-query.txt` file, writes the records to a file in JSON format, and includes soft-deleted
records; it also runs on an org with the alias `my-org` :

```
   sf data export bulk \

      --query-file soql-query.txt --result-format json --all-rows \

      --output-file accounts-all.json --wait 10 --target-org my-org

```

Bulk exports can take a while, depending on how many records are returned by the SOQL query. In our previous examples, we specified
that the command wait for 10 minutes for it to finish. If the command times out, it displays the `data export resume` command
you must run to get the status and results of the job. The command then returns control of the terminal, even though the job processing
is still happening in the background. The resume command uses a job ID, or you can use the `--use-most-recent` flag to resume
the most recently run job.

```
   sf data export resume --job-id 750xx00fake00005sAAA

```


Work with Data Work With Large Datasets

To bulk import the records from a file, run the `data import bulk` command. Similar to exporting, you can import records into
only one Salesforce object at a time, so the records in the file must be for the same object. Also, bulk import supports only files in CSV
format, not JSON.

This example shows how to bulk import records from the `accounts.csv` file into the Account object in the org with the alias
`new-scratch-org` . You must specify the column delimiter used in the file, which in this example is the comma.

```
   sf data import bulk --file accounts.csv --sobject Account \

     --column-delimiter COMMA --wait 10 --target-org new-scratch-org

```

Important: The format of the CSV file from which you’re importing must follow the rules and guidelines imposed by Bulk API
2.0. For example, the first row lists the fields you’re importing, and you must include all the object's required fields. For complete
documentation about creating these files, see the _Prepare Data to Ingest_ section of the _Bulk API Developer Guide_ .

The CSV file created by the `data export bulk` command follows the required formatting rules and guidelines.

Similar to the bulk export command, if the import times out, it completes and displays the `data import resume` command you
must run to get the status and results of the job. You can also use the `--use-most-recent` flag to resume the most recently run
import job.

```
   sf data import resume --use-most-recent

```

Bulk Delete

Use the `data delete bulk` command to delete multiple records at once from a single Salesforce object. You must specify a
comma-separated values (CSV) file that has only one column (named Id) and then the list of record IDs you want to delete, one ID per
line. This sample CSV file snippet is for deleting account records:

```
   Id

   0017z00000m14R9AAI

   0017z00000m5a0nAAA

   0017z00000m5a0oAAA

```

This example deletes the accounts listed in the specified CSV file from the default org:

```
   sf data delete bulk --sobject Account --file delete-accounts.csv --wait 10

```

As with all the bulk data commands, if the `data delete bulk` command times out, it displays the `data delete resume`
command you must run to see the status and results.

By default, the `data delete bulk` command puts the deleted records into the Salesforce Recycle Bin. You can specify that you
want the records to be marked for immediate deletion, also known as hard delete, by including the `--hard-delete` flag.

Important: You must have the "Bulk API Hard Delete” system permission to use the `--hard-delete` flag. This system
permission is disabled by default and can be enabled only by your Salesforce admin.

Bulk Update and Upsert

The `data update bulk` and `data upsert bulk` commands both read a CSV file that has new field values for a single
Salesforce object. The first column in the file must be a record ID. The remaining columns are the fields you want to update. This sample
CSV file snippet is for updating the Name field of the Account object:

```
   Id,Name

   0017z00000m14R9AAI,"New Name One"

```


Work with Data Work With Large Datasets

```
   0017z00000m5930AAA,"New Name Two"

   0017z00000m5931AAA,"New Name Three"

```

Important: See _Prepare Data to Ingest_ in the _Bulk API Developer Guide_ for full documentation about the format of the CSV file when
bulk updating and upserting.

However, when you run `data update bulk`, you can update only existing records; if the command finds an ID in the CSV file that
doesn’t currently exist, the command fails. By contrast, if you run `data upsert bulk` on the same CSV file, the command updates
existing records and creates a record if necessary.

This example updates records of the Account object of your default org using the `accounts-update.csv` file:

```
   sf data update bulk --file accounts-update.csv \

     --sobject Account --wait 10

```

If all the records in `accounts-update.csv` exist, then the command completes successfully and the Account object fields are
updated with their new values. To also insert new records, you must use `data upsert bulk` . The command requires the
`--external-id` flag, which for this example we set to just the Id field. Then, in the CSV file, rows that contain no value for the Id
column are inserted as new records. For example:

```
   Id,Name

   0017z00000m14R9AAI,"New Name One"

   0017z00000m5930AAA,"New Name Two"

   0017z00000m5931AAA,"New Name Three"

  ,"New Account”

```

Here’s how to run the upsert command:

```
   sf data upsert bulk --file accounts-update.csv \

     --sobject Account --external-id Id --wait 10

```

As with all the bulk data commands, if the `data update|upsert bulk` commands time out, they display the `data`
`update|upsert resume` commands you must run to see the status and results.

Get Detailed Results From Any Bulk Ingest Job

Use the `data bulk results` CLI command to get detailed results from any completed bulk ingest job that you previously ran
using any Salesforce tool. Examples of these tools include:

**•** The bulk Salesforce CLI commands discussed in this topic, such as `data import bulk` and `data upsert bulk`

**•** Data Loader

**•** A partner product on AppExchange that uses Bulk API 2.0

The `data bulk results` command requires that the bulk ingest job has completed; the command also needs the job ID. For
example, if you’re using `data import bulk`, and it’s still processing, run `data import resume` first and wait for it to complete.
Make note of the outputted job ID.

The `data bulk results` command first shows a summary of the job results. It includes the overall status, the executed operation,
the affected Salesforce object, and the number of successful and failed records that were processed. For example:

```
   sf data bulk results --job-id 75fake00CZBD1IAP --target-org my-scratch

   Status: JobComplete

   Operation: insert

   Object: Account

```


## Work with Data Work With Individual Records

```
   Processed records: 13

   Successful records: 13

   Saved successful results to 75fake00CZBD1IAP-success-records.csv

```

The command also provides a CSV file that contains details of every successful record that was processed, including the new Salesforce
record IDs; in our sample output, the name of the file is `75fake00CZBD1IAP-success-records.csv` . If any errors occurred
during the bulk ingest job, the command generates separate CSV files with details about the failures, and if possible, the unprocessed
records.

SEE ALSO:

_[Salesforce CLI Command Reference](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_data_commands_unified.htm)_ : data Commands

_Salesforce Help_ [: Sandbox Licenses and Storage Limits by Type](https://help.salesforce.com/s/articleView?id=platform.data_sandbox_environments.htm&type=5&language=en_US)

_[Bulk API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_asynch.meta/api_asynch/bulk_api_2_0.htm)_ : Bulk API 2.0

_[Bulk API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_asynch.meta/api_asynch/queries.htm)_ : SOQL Considerations

_[Bulk API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_asynch.meta/api_asynch/datafiles_prepare_data.htm)_ : Prepare Data to Ingest

_[Data Loader Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.dataLoader.meta/dataLoader/data_loader_intro.htm)_

[Salesforce AppExchange](https://appexchange.salesforce.com/)

## Work With Individual Records

Everyone’s process is unique, and you don’t always need the same data as your teammates. When you want to create, modify, or delete
individual records quickly, use the `data record` commands, such as `data create record` . With these commands you specify
field values directly at the command line, so you don’t need any CSV or JSON data files. These commands work with both standard and
custom Salesforce objects, and Tooling API objects.

Create a Record

This example shows how to create a record in the Account object in your default org:

```
   sf data create record --sobject Account \

     --values "Name='Exciting Company' Website=www.example.com NumberOfEmployees=45

   Phone='(415) 555-1212'"

```

Use the `--values` flag to specify field values in the form `<fieldName>=<value>` . Be sure to use the object’s field API name
and not its label. Separate multiple pairs with spaces, and use single quotes for individual values that include spaces. You must specify
a value for all required object fields.

Use the `--use-tooling-api` flag to create a Tooling API object record. This example creates a record in the TraceFlag Tooling
API object:

```
   sf data create record --use-tooling-api --sobject TraceFlag \

     --values "DebugLevelId=7dl170000008U36AAE StartDate=2024-12-15T00:26:04.000+0000 \

     ExpirationDate=2024-12-15T00:56:04.000+0000 LogType=CLASS_TRACING

   TracedEntityId=01p17000000R6bLAAS"

```


Work with Data Work With Individual Records

Get a Record

Use the `data get record` command to retrieve and display a single record of a Salesforce standard or Tooling API object. The
command first displays basic information about the record, such as its ID, and then displays all the record’s fields, one field per line. Fields
with no values are displayed as null.

Identify the record by either its ID ( `--record-id` flag) or with a list of field-value pairs ( `--where` flag). If your list of fields identifies
more than one record, the command fails; the error displays how many records were found.

When using `--where` to identify a record by its field values, be sure to use the object’s field API name and not its label. Separate
multiple field-value pairs with spaces, and use single quotes for individual values that include spaces.

For example, to display the Account record that we added in the previous section, run this command:

```
   sf data get record --sobject Account \

      --where "Name='Exciting Company' Website=www.example.com"

```

If you noted the record ID when you created the record, you can use it to display the record this way:

```
   sf data get record --sobject Account --record-id 001Oy0000xyz123

```

Here’s the example for Tooling API objects:

```
   sf data get record --use-tooling-api --sobject TraceFlag --record-id 7tf8c00xx

```

Update or Delete a Record

Use the `data update|delete record` commands to change an existing object or Tooling API record.

Identify the record by either its ID ( `--record-id` flag) or with a list of field-value pairs ( `--where` flag). If your list of fields identifies
more than one record, the command fails; the error displays how many records were found.

To update a field, use the `--values` flag to specify the new field value. For both `--values` and `--where`, be sure to use the
object’s field API name and not its label. Separate multiple field-value pairs with spaces, and use single quotes for individual values that
include spaces.

For example, let’s say the phone number for the Exciting Company account changed; here’s the CLI command to update the record:

```
   sf data update record --sobject Account \

     --where "Name='Exciting Company'" --values "Phone='(510) 555-1212'"

```

Here’s how you delete the record:

```
   sf data delete record --sobject Account --where "Name='Exciting Company'"

```

This example shows how to delete a record of a Tooling API object using its record ID:

```
   sf data delete record --use-tooling-api --sobject TraceFlag --record-id 7tf8c00xx

```

SEE ALSO:

_[Salesforce CLI Command Reference](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_data_commands_unified.htm)_ : data Commands

_[Tooling API](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_tooling.meta/api_tooling/tooling_api_objects_traceflag.htm)_ : TraceFlag


## Work with Data Run a SOQL or SOSL Query Run a SOQL or SOSL Query

It’s often useful to run a CLI command to quickly query a Salesforce object or search for specific terms across many objects. For example,
maybe you want to see all the Account records for the energy industry, or search for contact or lead names that begin with the letters
JO. Salesforce provides two robust search languages for just these use cases: SOQL and SOSL.

SOQL

Use Salesforce Object Query Language (SOQL) to search a single Salesforce or Tooling API object for specific information. SOQL is similar
to the SELECT statement in the widely used Structured Query Language (SQL) but is designed specifically for Salesforce data.

This example shows how to run a simple SOQL query against the Account object in your default org:

```
   sf data query --query "SELECT ID, Name FROM Account WHERE Industry='Energy'"

```

If your query is long, you can store it in a file and specify the file name to the `--file` flag, as shown in this example, which runs against
an org with the alias `new-scratch-org` :

```
   sf data query --file query.txt --target-org new-scratch-org

```

Tip: If your query returns more than 2,000 records, use the `data export bulk` command instead.

Use the `--all-rows` flag to also return records that have been soft-deleted due to a merge or delete. By default, deleted records
aren’t returned. To change the format of the output, such as to comma-separated values (CSV) or JSON, use the `--result-format`
flag.

```
   sf data query --query "SELECT ID, Name FROM Account WHERE Industry='Energy'" --all-rows

   --result-format json

```

To query a Tooling API object, include the `--use-tooling-api` flag. This example also shows how to use the `--output-file`
to write output to a file in CSV format.

```
   sf data query --query "SELECT ID, Name FROM ApexClass" --use-tooling-api --result-format

   csv --output-file query-output.csv

```

SOSL

Use Salesforce Object Search Language (SOSL) search fields across multiple objects.

This SOSL query searches the contacts and leads in your default org for names that start with Jo:

```
   sf data search

     --query "FIND {Jo*} IN Name FIELDS Returning Contact(Name, Phone), Lead(Name, Phone)"

```

If your SOSL search query is long, you can store it in a file and specify the filename to the `--file` flag, as shown in this example, which
runs against an org with the alias `new-scratch-org` :

```
   sf data search --file query.txt --target-org new-scratch-org

```


## Work with Data Upload a File to Your Org

Specify `--result-format csv` to write a comma-separated value (CSV) file to disk:

```
   sf data search --file query.txt --result-format csv

```

SEE ALSO:

_[Salesforce CLI Command Reference](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_data_commands_unified.htm)_ : data Commands

_[SOQL and SOSL Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_sosl_intro.htm)_

## Upload a File to Your Org

Use the `data create` file CLI command to upload a local file to your org. The file is uploaded to the ContentDocument standard
object; when the command finishes it outputs the new record ID. In the Salesforce UI, the uploaded file is available from the Files tab.
The command always creates a new file in the org; you can’t update an existing file. If you create a file with the name of an existing file,
a new duplicate record is created.

This simple example shows how to upload the file called `astro.png` to an org with the alias `new-scratch-org` :

```
   sf data create file --file astro.png --target-org new-scratch-org

```

By default, the `Title` field of the new ContentDocument record is the same as the name of the file (without the extension). In the
example, the title is `astro` . Use the `--title` flag to give it a new title:

```
   sf data create file --file astro.png --title "Astro Running" --target-org new-scratch-org

```

By default, the uploaded file isn’t attached to a Salesforce record, such as an account or contact. If you know the ID of the record to which
you want to attach the uploaded file, specify it with the `--parent-id` flag. This example attaches the file to a contact because the
ID starts with `003` :

```
   sf data create file --file astro.png --parent-id 003O300000WLdtwIAD --title "Astro Running"

    --target-org new-scratch-org

```

SEE ALSO:

_[Salesforce CLI Command Reference](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_data_commands_unified.htm)_ : data Commands

_[Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_contentdocument.htm)_ : ContentDocument


# CHAPTER 10 Salesforce DX MCP Server and Tools (Beta)

In this chapter ...

**•** Quick Start Using the
VS Code With Copilot
MCP Client (Beta)

Use the Salesforce DX MCP Server and its tools to enter natural language prompts in your IDE to complete
standard DX tasks like syncing metadata, running Apex and agent tests, and creating scratch orgs. The
DX MCP server includes over 60 MCP tools for various Salesforce features, such as DevOps, LWC
development, and code analysis. These tools provide predictable, secure, and structured context to large
language models (LLMs), ensuring efficient and accurate results.

**•** Install and Configure
the Salesforce DX Note: Salesforce DX MCP Server is a pilot or beta service that is subject to the Beta Services Terms
MCP Server (Beta) [at Agreements - Salesforce.com or a written Unified Pilot Agreement if executed by Customer,](https://www.salesforce.com/company/legal/agreements/)

[and applicable terms in the Product Terms Directory. Use of this pilot or beta service is at the](https://ptd.salesforce.com/)

**•** Use the Core
Customer's sole discretion.
# Salesforce DX MCP

Tools (Beta) Let's see how this work with an example. Say you enter `Deploy my metadata` in your IDE's agentic
chat window. The LLM sees that the DX MCP Server provides a `deploy_metadata` MCP tool, which
sounds perfect! The LLM then calls that tool within the context of your local DX project. Success and
error messages that result from the metadata deploy are then returned back to the LLM to determine
the next steps. In sum, the MCP DX tools guide the LLM to accomplish your goals in the the most accurate,
tested, and up-to-date way.

If the LLM didn't have the specific context for your prompt, it would still come up with a suggestion,
and eventually even the correct one. But because the LLM might be relying on out-of-date training data,
getting to the correct answer often involves inefficiencies, guesswork, and unpredictable behavior. MCP
solves this problem.

The Salesforce DX MCP Server is a specialized Model Context Protocol (MCP) implementation designed
[to facilitate seamless interaction between LLMs and Salesforce orgs. See MCP Solutions for Developers](https://developer.salesforce.com/docs/einstein/genai/guide/mcp.html)
in the _Agentforce Developer Guide_ for general MCP information and descriptions of other Salesforce MCP
Servers.

Key features of Salesforce DX MCP Server include:

**•** Direct interaction with Salesforce orgs through LLM-driven tools.

**•** Secure access using TypeScript libraries (not shelling out to Salesforce CLI).

**•** Improved security by avoiding the exposure of secrets in plain text.

**•** Granular access control with org allowlisting.

**•** Modular tool architecture for easy extensibility.

Salesforce DX MCP Server Security Features

The Salesforce DX MCP Server was designed with security as a top priority.

**•** Uses TypeScript libraries directly.

**–** Greatly decreases the size of the MCP Server.


Salesforce DX MCP Server and Tools (Beta)

**–** Significantly reduces the risk of remote code execution (RCE).

**•** No secrets needed in configuration.

**–** Eliminates the risk of plain text secret exposure.

**–** Accesses pre-existing (encrypted) auth files on the user's machine.

**–** Implements allowlisting for auth info key/values to prevent sensitive data exposure.

**•** No secrets exposed via MCP tools.

**–** Prevents other tools from accessing unencrypted tokens.

**–** Tools pass usernames around instead of tokens.

**•** Granular access control.

**–** MCP Server can access auth info for only orgs that have been explicitly allowlisted.

**–** Users specify allowed orgs when starting the server.

Agentforce Vibes Extension Includes the Salesforce
DX MCP Server

Agentforce Vibes is an AI-powered Salesforce developer tool that's available as an easy-to-install Visual
Studio Code (VS Code) extension. It includes Agentforce, an intelligent coding partner that provides
information and, most importantly, can take action.

The Salesforce DX MCP Server is pre-configured in Agentforce Vibes, so you can start using the DX MCP
tools immediately after you install the extension in VS Code.

[See Set Up Agentforce Vibes and Build with Agentforce for more information.](https://developer.salesforce.com/docs/platform/einstein-for-devs/guide/einstein-setup.html)

Types of MCP Tools Included in Salesforce DX MCP
Server

The Salesforce DX MCP Server includes many tools for working with different Salesforce features. To
narrow the LLM context, the DX MCP Server groups the tools into toolsets based on functionality. You
can then easily enable only those tools you want to use, rather than enable them all and overwhelm the
LLM.

These are the high-level types of MCP tools included in the DX MCP Server:

**•** **Core DX** : Usual DX tools for working with orgs, deploying and retrieving metadata, and so on.

**•** **Code Analysis** : Run a static analysis of your code using Salesforce Code Analyzer.

**•** **DevOps** : Manage work items, resolve merge conflicts, and troubleshoot deployment problems
within DevOps Center.

**•** **Lightning Types** : Create and enhance custom Lightning types to define complex data structures
and build custom user interfaces for Agentforce, Prompt Builder, and other Salesforce applications.
[See the Lightning Types MCP Tool documentation.](https://developer.salesforce.com/docs/platform/lightning-types/guide/lightning-types-mcp-tool.html)

**•** **Lightning Web Components (LWC) and Aura** : Help you design, build, test, and optimize LWC
code and facilitate Aura migration to LWC.


Salesforce DX MCP Server and Tools (Beta)

**•** **Mobile** : Help LWC developers create Lightning web components that integrate with device-native
features and adhere to Mobile Offline design patterns.

**•** **Scale Products** : Use ApexGuru to detect and fix Apex performance issues.

MCP Terminology

Here are the MCP-specific terms we use in this document.

**•** **MCP Server**               - An MCP server lets users interact with a system (such as Salesforce) using an LLM and
natural language instead of an API. MCP servers provide the LLM with tools, prompts, and resources
that the LLM can use to perform specific tasks.

**•** **MCP Tools**               - Executable functions that the LLM can call to perform actions.

**•** **MCP Toolsets**               - Logical groups of MCP tools based on their functionality. For example, the Salesforce
DX MCP Server has `metadata` and `orgs` toolsets.

**•** **MCP Client**               - The interface (such as Agentforce) or IDE (such as Cursor) that can host an MCP server
and act as an interface to the LLM. Also called MCP Host, although this document uses the term
MCP client.

SEE ALSO:

_GitHub_ [: Salesforce DX MCP Server Repository](https://github.com/salesforcecli/mcp)


## Salesforce DX MCP Server and Tools (Beta) Quick Start Using the VS Code With Copilot MCP Client (Beta) Quick Start Using the VS Code With Copilot MCP Client (Beta)

Get started with the Salesforce DX MCP Server using Visual Studio Code (VS Code) as the MCP client. After you configure it with the
Salesforce DX MCP Server, you then use GitHub Copilot and natural language to easily execute typical Salesforce DX development tasks,
such as creating scratch orgs, deploying or retrieving metadata, and viewing org records.

For the best getting-started experience, make sure that you have a standard Salesforce DX environment set up on your computer. In
particular:

**•** [Install Node.js on your computer. We recommend you use the Active LTS version.](https://nodejs.org/en)

**•** [Install Salesforce CLI on your computer.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_setup.meta/sfdx_setup/sfdx_setup_install_cli.htm#sfdx_setup_install_cli)

**•** [Install VS Code on your computer.](https://code.visualstudio.com/docs)

**•** [Create a Salesforce DX project and open it in VS Code. You can also clone an example repo, such as dreamhouse-lwc, which is a](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_ws_create_new.htm)
ready-to-use DX project that contains a simple Salesforce application, with metadata and test data.

**•** [Authorize at least one development Salesforce org to use with your DX project, such as a Trailhead playground, sandbox, scratch](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_auth_web_flow.htm)
org, or Developer Edition org, and set it as your default org.

If you want to create a scratch org using MCP, then you must also authorize a Dev Hub org.

[You also need a GitHub account.](https://github.com/)

Okay, let’s do it!

**1.** Create a `.vscode/mcp.json` file at the root of your DX project and add this JSON:

```
      {

      "servers": {

       "Salesforce DX": {

         "command": "npx",

         "args": ["-y", "@salesforce/mcp@latest",

              "--orgs", "DEFAULT_TARGET_ORG",

              "--toolsets", "orgs,metadata,data,users,testing"]

       }

      }

     }

```

[You can also configure the DX MCP Server globally by editing the VS Code settings.json file and adding a similar JSON snippet but](https://code.visualstudio.com/docs/configure/settings#_settings-file-locations)
contained in an `mcp:servers` section.

The `--orgs` flag is required and specifies the authorized orgs you're allowing the DX MCP Server to access. The `--toolsets`
flag specifies the toolsets it should consult when determining the specific tool to run. See Configure the Salesforce DX MCP Server
for Your Environment (Beta) for the available values for the two flags.

**2.** Open VS Code, go to **View -> Command Palette** and find and click **MCP: List Servers** .

Tip: You can also get to the command palette by pressing Ctrl+Shift+P (Windows or Linux) or Command-Shift-P (macOS).

**3.** Click **Salesforce DX**, then **Start Server** .
Click **Yes** if you’re asked if the DX MCP Server is trustworthy.

Check the **Output** tab for the server status and errors. The output also shows information such as the MCP tools and toolsets that
were registered, and which MCP tool registration was skipped because they’re not generally available (NON-GA).

When the DX MCP Server is ready, you see a message like this (your server version might be different):

```
     � Salesforce MCP Server v0.21.2 running on stdio

```


## Salesforce DX MCP Server and Tools (Beta) Install and Configure the Salesforce DX MCP Server (Beta)

**4. Run Chat: Open Chat (Agent)** from the command palette to start a new GitHub Copilot chat session. If necessary, you’re asked to
log in to GitHub and authorize VS Code to access it.
[Be sure your GitHub Copilot chat window is in Agent mode; if you're in Ask or Edit mode, use the little drop-down to switch.](https://github.blog/ai-and-ml/github-copilot/copilot-ask-edit-and-agent-modes-what-they-do-and-when-to-use-them/)

**5.** In the GitHub Copilot chat window, use natural language to explain what you want to do. The DX MCP Server determines which
configured tool to use, and then shows it to you along with other information. Review the chosen tool and parameters, then click
**Continue** to run the tool and see the results of your request.
Try out these sample prompts:

**•** _Do I have any active scratch orgs? What about inactive scratch orgs?_

**•** _Show me all the available information about all my orgs._

**•** _Show me all the accounts in the org with the alias_ _`my-org`_ _._

**•** _Deploy the Apex classes in my DX project to the org with the alias_ _`my-org`_ _._

**•** _Retrieve all agents from my org._

**6.** To stop, restart, or view the DX MCP Server configuration, run the **MCP: List Servers** command, click **Salesforce DX**, then click the
appropriate option.

SEE ALSO:

_GitHub_ [: Salesforce DX MCP Server Repository](https://github.com/salesforcecli/mcp)

## Install and Configure the Salesforce DX MCP Server (Beta)

Install the Salesforce DX MCP Server in your MCP client to start using the tools.

Follow these steps:

**1.** [Install Node.js on your computer. We recommend you use the Active LTS version.](https://nodejs.org/en)

### 2. Add the Salesforce DX MCP Server to Your MCP Client (Beta).

**3.** Configure the Salesforce DX MCP Server for Your Environment (Beta).

### Add the Salesforce DX MCP Server to Your MCP Client (Beta)

The Salesforce DX MCP Server is an `npm` package called `@salesforce/mcp` . Adding the DX MCP Server to an MCP client typically
involves updating a JSON file that tells the MCP client how to run the `@salesforce/mcp` package using npx and specifying the
`args` option to configure the DX MCP Server. We recommend that you also use the `@latest` tag ( `@salesforce/mcp@latest` )
so you always get the latest version of the DX MCP Server.

While each MCP client has different JSON files, the format of the `args` option is always the same.

Agentforce Vibes

The Salesforce DX MCP Server is pre-configured in Agentforce Vibes. See Agentforce Vibes Extension Includes the Salesforce DX MCP
Server.

VS Code with Copilot

See the Quick Start Using the VS Code With Copilot MCP Client (Beta), which uses VS Code with GitHub Copilot as the example. The
topic includes details about which JSON file to update and an example JSON snippet.


### Salesforce DX MCP Server and Tools (Beta) Configure the Salesforce DX MCP Server for Your Environment

(Beta)

Other MCP Clients

[To configure the Salesforce DX MCP Server in other MCP clients, such as Claude Code and Cursor, see the README for the Salesforce DX](https://github.com/salesforcecli/mcp/blob/main/README.md)
MCP Server GitHub repository.

### Configure the Salesforce DX MCP Server for Your Environment (Beta)

After you’ve added the basic Salesforce DX MCP Server to your MCP client, configure the server for your specific environment by updating
the `args` option with new flags or new values to the flags.

Surround the flag name and its value each in double quotes, and separate all flags and values with commas. Boolean flags don't take a
value.

Let’s just run through some examples so you get the idea. Then see later sections for the full list of values you can specify for the `args`
option and its flags.

This basic example (for the VS Code with Copilot MCP client) configures the DX MCP Server to access your default org and enables the
core DX toolsets.

```
   {

     "servers": {

      "Salesforce DX": {

       "command": "npx",

       "args": ["-y", "@salesforce/mcp@latest",

            "--orgs", "DEFAULT_TARGET_ORG",

            "--toolsets", "orgs,metadata,data,users,testing"]

      }

     }

   }

```

The `"-y", "@salesforce/mcp@latest"` part tells the `npx` command to automatically install the latest version of the
`@salesforce/mcp` npm package instead of asking permission. Don't change this.

From now on we’ll show examples of just the `args` option, which is the key configuration option for the Salesforce DX MCP Server.

This example shows how to enable just the `data`, `orgs`, and `metadata` toolsets and allow access to two orgs: your default Dev
Hub org and an org with username `test-org@example.com` .

```
   "args": ["-y", "@salesforce/mcp@latest",

         "--orgs", "DEFAULT_TARGET_DEV_HUB,test-org@example.com",

         "--toolsets", "data,orgs,metadata"]

```

This example shows how to configure access to two orgs for which you specified aliases when you authorized them ( `my-scratch-org`
and `my-dev-hub` ).

```
   "args": ["-y", "@salesforce/mcp@latest",

         "--orgs", "my-scratch-org,my-dev-hub",

         "--toolsets", "data,orgs,metadata"]

```

This example allows the MCP Server to access all your authorized orgs, all toolsets, and tools that are not yet generally available. In other
words, this enables everything! Only do this if you truly need everything.

```
   "args": ["-y", "@salesforce/mcp@latest",

         "--orgs", "ALLOW_ALL_ORGS",

         "--toolsets", "all",

         "--allow-non-ga-tools"]

```


Salesforce DX MCP Server and Tools (Beta) Configure the Salesforce DX MCP Server for Your Environment
(Beta)

This example enables five tool sets ( `data`, `orgs`, `metadata`, `lwc-experts`, and `code-analysis` ) and a specific tool
( `run_apex_test` ) from a different toolset.

```
   "args": ["-y", "@salesforce/mcp@latest",

         "--orgs", "DEFAULT_TARGET_ORG",

         "--toolsets", "data,orgs,metadata,lwc-experts,code-analysis",

         "--tools", "run_apex_test",

         "--allow-non-ga-tools"]

```

This example allows access to both your default org and default Dev Hub org. It also enables three specific MCP tools rather than using
toolsets. The `core` toolset is always enabled, even if you don't specify it in the server configuration.

```
   "args": ["-y", "@salesforce/mcp@latest",

         "--orgs", "DEFAULT_TARGET_ORG,DEFAULT_TARGET_DEV_HUB",

         "--tools", "list_all_orgs,deploy_metadata,run_apex_test"]

```

This example enables the `orgs` toolset and the specific tool `deploy_metadata` .

```
   "args": ["-y", "@salesforce/mcp@latest",

         "--orgs", "DEFAULT_TARGET_ORG",

         "--toolsets", "orgs",

         "--tools", "deploy_metadata"]

```

Valid Values for the **`args`** Option

These are the flags that you can pass to the `args` option.

**Table 1: Valid values for the args option**


Salesforce DX MCP Server and Tools (Beta) Configure the Salesforce DX MCP Server for Your Environment
(Beta)

Valid Values for the --orgs Flag

The Salesforce MCP tools require an org, and so you must include the required `--orgs` flag and specify at least one authorized org.
Separate multiple values with commas.

We recommend that, for security reasons, you don’t automatically specify all the orgs you’ve authorized but instead only the orgs you
want the DX MCP Server to access.

Tip: If you’re limiting the MCP tools to those that don’t typically require a Salesforce org (such as Salesforce Code Analyzer tools
in the `code-analysis` toolset), you must still set the `--orgs` flag, such as `--orgs DEFAULT_TARGET_ORG` . You
don’t get an error on server start, even if you haven’t set a default org.

[You must explicitly authorize the orgs on your computer before the MCP server can access them. Use the](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_auth_web_flow.htm) `org login web` Salesforce
CLI command or the **VS Code SFDX: Authorize an Org** command from the command palette.

These are the available values for the `--orgs` flag.


Salesforce DX MCP Server and Tools (Beta) Configure the Salesforce DX MCP Server for Your Environment
(Beta)

**Table 2: Valid values for the --orgs Flag**

Valid Values for the **`--toolsets`** Flag

The Salesforce DX MCP Server uses toolsets to logically group MCP tools based on functionality; use the `--toolsets` flag to specify
the ones you want to enable for your environment. Separate multiple toolsets commas.

Tip: If you enable an MCP tool with the `--toolsets` flag, you can then disable it in your MCP client, which takes precedence.

These are the available toolsets. For some of these toolsets, the complete list of included tools is documented in separate documentation,
as indicated.

**Table 3: Valid values for the --toolsets Flag**


Salesforce DX MCP Server and Tools (Beta) Configure the Salesforce DX MCP Server for Your Environment
(Beta)


### Salesforce DX MCP Server and Tools (Beta) Manage the Salesforce DX MCP Server (Beta)

Valid Values for the **`--tools`** Flag

You can use the `--tools` flag to enable specific tools. Use the `--toolsets` and `--tools` flags in combination to enable, for
example, all the tools in the `orgs` toolset and just one tool ( `run_apex_test` ) in the testing toolset. Separate multiple tools with
commas.

Tip: If you enable an MCP tool with the `--tools` or `--toolsets` flag, you can then disable it in your MCP client, which
takes precedence.

The easiest way to find the name of a specific MCP tool is using your MCP client. For example, in VS Code with GitHub Copilot, click the
**Configure Tools** button in the bottom-right of the chat window to see all the available tools, including the Salesforce DX ones.

[The Salesforce DX MCP Server GitHub repository README also has a list of the available MCP tools.](https://github.com/salesforcecli/mcp/blob/main/README.md)

You can also refer to the documentation for the different types of MCP tools:

**•** Core Salesforce DX MCP Tools Documentation on page 243

**•** [DevOps Center MCP Tools Documentation](https://help.salesforce.com/s/articleView?id=platform.devops_center_mcp_intro.htm&language=en_US)

**•** [Code Analyzer MCP Tools Documentation](https://developer.salesforce.com/docs/platform/salesforce-code-analyzer/guide/mcp.html)

**•** [Mobile MCP Tools Documentation](https://developer.salesforce.com/docs/atlas.en-us.262.0.mobile_offline.meta/mobile_offline/dx_mobile_mcp_tools.htm)

**•** [LWC MCP Tools Documentation](https://developer.salesforce.com/docs/platform/lwc/guide/mcp-intro.html)

**•** [ApexGuru MCP Tools Documentation](https://help.salesforce.com/s/articleView?id=xcloud.apexguru_salesforce_dx_mcp.htm&type=5&language=en_US)

### Manage the Salesforce DX MCP Server (Beta)

The exact steps to manage the Salesforce DX MCP Server depends on your MCP client.

But most clients allow you to:

**•** Stop and restart the server. If a new version of the DX MCP Server `npm` package ( `@salesforce/mcp` ) was released, then it’s
automatically updated.

**•** Set the LLM models that the DX MCP Server can use.

Check your MCP client documentation for details.

MCP Server Updates and Feedback

[Release notes are available at the issue-only Github repository for the Salesforce DX MCP server. In this GitHub repository, you can also](https://github.com/forcedotcom/mcp/tree/main/releasenotes)
report bugs and suggest feedback.

[To report bugs, first check if someone else already reported the issue. If you don’t see your bug listed, open a new issue.](https://github.com/forcedotcom/mcp/issues)

[For feature requests and other related topics, first review the existing discussions before you open a new discussion.](https://github.com/forcedotcom/mcp/discussions)

Note: GitHub isn’t a mechanism for receiving support under any agreement or SLA. If you require immediate assistance, contact
[Salesforce Customer Support.](https://help.salesforce.com/s/articleView?id=000384365&type=1&language=en_US)

SEE ALSO:

_GitHub_ [: Salesforce DX MCP Server Repository](https://github.com/salesforcecli/mcp)


## Salesforce DX MCP Server and Tools (Beta) Use the Core Salesforce DX MCP Tools (Beta) Use the Core Salesforce DX MCP Tools (Beta)

Use the core Salesforce DX MCP tools to run classic DX tasks, such as work with orgs, retrieve and deploy metadata, run Apex tests, and
more.

The core DX tools are grouped into these toolsets:

**•** `orgs`

**•** `metadata`

**•** `data`

**•** `users`

**•** `testing`

See the toolset topic for information about the other available toolsets, such as DevOps and LWC, and links to documentation about
how to effectively use them.

Prerequisites for Using the Core DX MCP Tools

To work with the core DX MCP tools, you need the standard Salesforce DX environment set up on your computer. In particular:

**•** Install and configure the Salesforce DX MCP Server in your MCP client.

**•** [Install Salesforce CLI on your computer.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_setup.meta/sfdx_setup/sfdx_setup_install_cli.htm#sfdx_setup_install_cli)

**•** [Install VS Code on your computer.](https://code.visualstudio.com/docs)

**•** [Create a Salesforce DX project and open it in VS Code. You can also clone an example repo, such as dreamhouse-lwc, which is a](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_ws_create_new.htm)
ready-to-use DX project that contains a simple Salesforce application, with metadata and test data.

**•** [Authorize at least one development Salesforce org to use with your DX project, such as a Trailhead playground, sandbox, scratch](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_auth_web_flow.htm)
org, or Developer Edition org, and set it as your default org.

If you want to create a scratch org using MCP, then you must also authorize a Dev Hub org.

Sample Prompts that Invoke the Core DX MCP Tools

Here are some sample prompts to get you started using the core DX MCP tools. You never call a specific MCP tool directly; as always in
this exciting new AI world, you use natural language to tell the LLM what you want to accomplish, and it then figures out what tools to
call to complete the task.

You can configure your MCP client to automatically run MCP tools that just provide information, but to ask for your explicit confirmation
before it runs a tool that makes a real change in your local DX project or in your org. We think this behavior is a good idea.

**Get information about the orgs that the DX MCP Server knows about:**

**•** _List all my orgs and provide all the details you know about them._

**•** _Fully describe the org with the alias my-org._

Tips:

**•** If the MCP client doesn’t list the authorized orgs that you want to use, update the `--orgs` flag in your DX MCP Server configuration
and either add the org’s alias or username or specify `ALLOW_ALL_ORGS` .

**•** In general, if the LLM seems to be getting confused, start a new chat session which clears the context. This tip applies to pretty much
all LLM usage.

**Open your org in a browser:**


Salesforce DX MCP Server and Tools (Beta) Use the Core Salesforce DX MCP Tools (Beta)

**•** _Open my org in a browser._

**•** _Open the Resort Manager agent in Agent Builder._

**•** _Open the Get Experiences flow in its associated builder._

**•** _Open the file I’m currently working on (in my IDE) in my org._

Tips:

**•** To open an agent or flow in its associated org builder, you must have the metadata files in your Salesforce DX project. Try retrieving
them if they’re in your org, but not in your DX project.

**Work with scratch orgs and snapshots:**

**•** _Do I have any active scratch orgs? What about inactive scratch orgs?_

**•** _Create a scratch org, give it the alias my-scratch, and make it my default org._

**•** _Create a snapshot from the scratch org you just created._

**•** _Create a scratch org from the snapshot you just created._

**•** _Delete the scratch org with the alias my-scratch._

Tips:

**•** If you successfully create a scratch org using a prompt, but it doesn’t show up when you ask to list your orgs, update the `--orgs`
flag in your DX MCP Server configuration and either add the new scratch org alias or username or specify `ALLOW_ALL_ORGS` .

**Get information about your org:**

**•** _Show me all the accounts in my org._

**•** _What are all the fields of the account object?_

**•** _Show me all the accounts in my org; include the name, billing address, web site, and phone fields._

**•** _How many system administrators do I have in my org? What are their usernames?_

**Deploy and retrieve metadata:**

**•** _Deploy all local Apex classes to my org._

**•** _Deploy everything in my DX project to my org._

**•** _Retrieve all agents from my org._

**Run tests:**

**•** _Run all local Apex tests and diagnose any failures._

**•** _Run all agent tests._

Core DX MCP Tools Reference

The core Salesforce DX MCP Server provides these tools for working with orgs, metadata, and so on. We provide this reference information
so you understand what kinds of tasks these tools can accomplish; you don’t call these tools directly, but rather the LLM does.

The tools marked NON-GA are not yet generally available, specify the `--allow-non-ga-tools` flag in your DX MCP Server
configuration to use them. See Configure the Salesforce DX MCP Server for Your Environment.

**Table 4: Core DX MCP Tools**


Salesforce DX MCP Server and Tools (Beta) Use the Core Salesforce DX MCP Tools (Beta)

SEE ALSO:

_GitHub_ [: Salesforce DX MCP Server Repository](https://github.com/salesforcecli/mcp)


# CHAPTER 11 Development

In this chapter ... After you import some test data, you’ve completed the process of setting up your project. Now, you’re
ready to start the development process.

**•** Develop Against Any
Org

**•** Assign a Permission Create Source Files from the CLI
Set

**•** Create Lightning To add source files from the CLI, make sure that you’re working in an appropriate directory. For example,
Apps and Aura if your package directory is called `force-app`, create Apex classes in
Components `force-app/main/default/classes` . You can organize your source as you want underneath

**•** Create Lightning Web each package directory except for documents, custom objects, and custom object translations.
Components As of API version 45.0, you can build Lightning components using two programming models: Lightning

**•** Create an Apex Web Components and Aura Components. To organize your components’ source files, your Aura
Class components must be in the `aura` directory. Your Lightning web components must be in the `lwc`

**•** Create an Apex directory.
Trigger
Execute one of these commands.

**•** Create a Custom

**•** `apex generate class`
Object

**•** `apex generate trigger`

**•** Execute Anonymous
Apex **•** `cmdt generate object`

**•** Run Apex Tests **•** `cmdt generate field`

**•** `cmdt generate record`

**•** `cmdt generate records`

**•** `cmdt generate fromorg`

**•** `lightning generate app`

**•** `lightning generate component`

**•** `lightning generate event`

**•** `lightning generate interface`

**•** `lightning generate test`

**•** `schema generate sobject`

**•** `schema generate field`

**•** `schema generate platformevent`

**•** `schema generate tab`

**•** `static-resource generate`

**•** `visualforce generate component`

**•** `visualforce generate page`


Development

Many of the commands have these two helpful optional flags:

Tip: If you want to know more information about a command, run it with the `--help` flag. For
example, `sf apex generate class --help` .

Edit Source Files

Use your favorite code editor to edit Apex classes, Visualforce pages and components, Lightning web
components, and Aura components in your project. You can also make edits in the Setup UI of your org
and then use `project retrieve start` to retrieve those changes to your project. For Lightning
pages (FlexiPage files) that are already in your org, use the shortcut to open Lightning App Builder in a
scratch org from your default browser. Lightning Pages are stored in the `flexipages` directory.

To edit a FlexiPage in your default browser—for example, to edit the Property_Record_Page
source—execute this command from the `flexipages` directory.

```
sf org open --source-file Property_Record_Page.flexipage-meta.xml

```

If you want to generate a URL that loads the `.flexipage-meta.xml` file in Lightning App Builder
but doesn’t launch your browser, use the `--url-only | -r` flag.

```
sf org open --source-file Property_Record_Page.flexipage-meta.xml

--url-only

```

SEE ALSO:

_[Salesforce CLI Command Reference](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_unified.htm)_


## Development Develop Against Any Org Develop Against Any Org

After developing against scratch or sandbox orgs that have source tracking enabled, you eventually test and validate your changes in a
non-source-tracked org.

You can use Salesforce CLI to retrieve and deploy metadata (in metadata format) to non-source-tracked orgs with the same ease as
[retrieving and deploying source (in source format) to and from scratch orgs. If you’re new to Salesforce CLI, Salesforce DX Project Structure](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_source_file_format.htm)
[and Source File Format explains the difference between source format and metadata format.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_source_file_format.htm)

Using `project retrieve start`, you can retrieve the metadata you need in source format to your local file system (DX project).
When your changes are ready for testing or production, you can use `project deploy start` to deploy your local files directly
to a non-source-tracked org.

Not sure what metadata types are supported or which metadata types support wild cards in `package.xml` [? See Metadata Types in](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_types_list.htm)
the _Metadata API Developer Guide_ .

Before You Begin

Before you begin, don't forget to:

**•** Create a Salesforce DX project that includes a manifest (package.xml). Run `project generate --name mywork`
`MyProject --manifest` .

**•** Authorize your non-source-tracked org. If connecting to a sandbox, edit your `sfdx-project.json` file to set `sfdcLoginUrl`
to `https://test.salesforce.com` [before you authorize the org. Don't forget to create aliases for your non-source-tracked](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_cli_usernames_orgs.htm)
orgs.

Metadata Names That Require Encoding on the Command Line

When retrieving or deploying metadata using the `--metadata` option, commas in metadata names require encoding to work
properly.

**Don’t:** `sf project deploy start --metadata "Profile:Standard User" --metadata`

```
   "Layout:Page,Console"

```

**Do:** `sf project deploy start --metadata "Profile:Standard User" --metadata`

```
   "Layout:Page %2C Console"

```

Retrieve Source from a Non-Source-Tracked Org

Use the `project retrieve start` command to retrieve source from orgs that don’t have source tracking, such as a sandbox
or your production org. If you already have the source code and metadata in a VCS, you might be able to skip this step. If you're starting
anew, you retrieve the metadata associated with the feature, project, or customization you're working on.

You can retrieve metadata in source format using one of these methods:

**•** Specify a `package.xml` that lists the components to retrieve.

**•** Specify a comma-separated list of metadata component names.

**•** Specify a comma-separated list of source file paths to retrieve. You can use the source path option when source exists locally, for
example, after you've done an initial retrieve.

**•** Specify a comma-separated list of package names.

If the comma-separated list you’re supplying contains spaces, enclose the entire comma-separated list in one set of double quotes.


Development Develop Against Any Org

You can specify only one scoping parameter when retrieving metadata: `--metadata`, `--source-dir`, or `--manifest` . If you
indicate `--package-name`, you can include one additional scoping parameter.

```
sf project retrieve start --package-name DreamHouse --manifest manifest/package.xml

```

Deploy Source to a Non-Source-Tracked Org

Use the `project deploy start` command to deploy source to orgs that don’t have source tracking, such as a sandbox or
production org.

You can deploy metadata in source format using these methods:

**•** Specify a `package.xml` that lists the components to deploy

**•** Specify a comma-separated list of metadata component names

**•** Specify a comma-separated list of source file paths to deploy

If the comma-separated list you’re supplying contains spaces, enclose the entire comma-separated list in one set of double quotes.


Development Develop Against Any Org

Delete Non-Tracked Source

Use the `project delete source` command to delete components from orgs that don’t have source tracking, such as sandboxes.

If the source exists locally in a DX project, you can delete metadata by specifying the path to the source or by listing individual metadata
components. If the comma-separated list you’re supplying contains spaces, enclose the entire comma-separated list in one set of double
quotes.

Do You Want to Retain the Generated Metadata?

Normally, when you run some CLI commands, a temporary directory with all the metadata is created then deleted upon successful
completion of the command. However, retaining these files can be useful for several reasons. You can debug problems that occur during
command execution. You can use the generated `package.xml` when running subsequent commands, or as a starting point for
creating a manifest that includes all the metadata you care about.

To retain all the metadata in a specified directory path when you run these commands, set the SF_MDAPI_TEMP_DIR environment
variable:

**•** `project deploy start`

**•** `project retrieve start`


## Development Assign a Permission Set

**•** `project delete source`

**•** `project convert mdapi|source`

**•** `org create scratch` (if your scratch org definition contains scratch org settings, not org preferences)

Example:

```
   SF_MDAPI_TEMP_DIR=/users/myName/myDXProject/metadata

```

SEE ALSO:

_VS Code Command_ [: SFDX: Deploy|Retrieve|Delete Source From Org](https://developer.salesforce.com/docs/platform/sfvscode-extensions/guide/deploy-changes.html)

## Assign a Permission Set

After creating your scratch org and deploying the source, you must sometimes give your users access to your application, especially if
your app contains custom objects.

**1.** If needed, create the permission set in the scratch org.

**a.** Open the scratch org in your browser.

```
       sf org open --target-org <scratch org username/alias>

```

**b.** From Setup, enter _`Perm`_ in the Quick Find box, then select **Permission Sets** .

**c.** Click **New** .

**d.** Enter a descriptive label for the permission set, then click **Save** .

**e.** Under Apps, click **Assigned Apps**       - **Edit** .

**f.** Under Available Apps, select your app, then click **Add** to move it to Enabled Apps.

**g.** Click **Save** .

**2.** Retrieve the permission set from the scratch org to your project.

```
     sf project retrieve start --target-org <scratch org username/alias>

```

**3.** Assign the permission set to one or more users of the org that contains the app:

```
     sf org assign permset --name <permset_name> --target-org <username/alias>

```

The target username must have permission to assign a permission set. Use the `--on-behalf-of` flag to assign a permission
set to non-administrator users.

```
     sf org assign permset --name <permset_name> --target-org <admin-user> --on-behalf-of

     <non-admin-user>

```

You can also assign permission set licenses to users using the `org assign permsetlicense` command. It works similarly to
the `org assign permset` command.

SEE ALSO:

_Salesforce Help_ [: Permission Sets](https://help.salesforce.com/s/articleView?id=platform.perm_sets_overview.htm&type=5&language=en_US)

_Salesforce Help_ [: Permission Set Licenses](https://help.salesforce.com/s/articleView?id=platform.users_permissionset_licenses_overview.htm&type=5&language=en_US)


## Development Create Lightning Apps and Aura Components Create Lightning Apps and Aura Components

You can use Salesforce CLI to create Lightning apps and Aura components in your local Salesforce DX project. The generated files live
in an `aura` directory in a package directory of your project.

**1.** Open a terminal (macOS and Linux) or command prompt Windows and change to your Salesforce DX project directory.

**2.** Create the `aura` directory in the location you want to generate the Lightning app and Aura components. For example, if you want
to generate them in the default package directory, create the `force-app/main/default/aura` directory if it doesn’t exist.

**3.** Create a Lightning app or an Aura component; specify the app or component name with the `--name` flag and the `aura` directory
with the `--output-dir` flag.

```
     sf lightning generate app --name myApp --output-dir force-app/main/default/aura

     sf lightning generate component --type aura --name myAuraComponent --output-dir

     force-app/main/default/aura

```

Use the `project deploy start` command to deploy the new Lightning app and Aura component to your org.

```
   sf project deploy start --metadata AuraDefinitionBundle:myApp --metadata

   AuraDefinitionBundle:myAuraComponent

```

SEE ALSO:

_VS Code Command_ [: SFDX: Create Aura App|Component|Event|Interface](https://developer.salesforce.com/docs/platform/sfvscode-extensions/guide/aura-writing.html)

## Create Lightning Web Components Create Lightning Web Components

You can use Salesforce CLI to create Lightning web components in your local Salesforce DX project. The generated files live in a `lwc`
directory in a package directory of your project.

Note: Want to develop your Lightning web components in a real-time preview of your Lightning app or Experience Cloud site?
[Try the new Local Dev experience, which lets you iterate faster on your components without deploying code or manually refreshing](https://developer.salesforce.com/docs/platform/lwc/guide/get-started-test-components.html)
the preview.

**1.** Open a terminal (macOS and Linux) or command prompt Windows and change to your Salesforce DX project directory.

**2.** Create the `lwc` directory in the location you want to generate the Lightning app and Aura components. For example, if you want
to generate them in the default package directory, create the `force-app/main/default/aura` directory if it doesn’t exist.

**3.** Create the Lightning web component; specify the component name with the `--name` flag and the `lwc` directory with the
`--output-dir` flag.

```
     sf lightning generate component --type lwc --name myLightningWebComponent --output-dir

      force-app/main/default/lwc

```


## Development Create an Apex Class

Use the `project deploy start` command to deploy your new Lightning web component to your org.

```
   sf project deploy start --metadata LightningComponentBundle:myLightningWebComponent

```

SEE ALSO:

Create Lightning Apps and Aura Components

_Lightning Web Components Dev Guide_ [: Introducing Lightning Web Components](https://developer.salesforce.com/docs/component-library/documentation/lwc)

_VS Code Command_ [: SFDX: Create Lightning Web Component | Test](https://developer.salesforce.com/docs/platform/sfvscode-extensions/guide/lwc-writing.html)

## Create an Apex Class

You can use Salesforce CLI to create Apex classes in your local Salesforce DX project. The generated class files live in a `classes` directory
in a package directory of your project.

**1.** Open a terminal (macOS and Linux) or command prompt Windows and change to your Salesforce DX project directory.

**2.** Create the `classes` directory in the location you want to generate the Apex class. For example, if you want to generate it in the
default package directory, create the `force-app/main/default/classes` directory if it doesn’t exist.

**3.** Create the Apex class; specify the class name with the `--name` flag and the `classes` directory with the `--output-dir`
flag.

```
     sf apex generate class --name myClass --output-dir force-app/main/default/classes

```

The command generates two files:

**•** `myClass.cls-meta.xml` —metadata file

**•** `myClass.cls` —Apex source file

By default, the command creates an empty Apex class. However, you can select different templates, depending on what you’re creating,
by specifying the `--template` flag.

This example selects the `ApexException` template.

```
sf apex generate class --name myException --template ApexException --output-dir

force-app/main/default/classes

```


## Development Create an Apex Trigger

Use the `project deploy start` command to deploy the new Apex class to your org.

```
   sf project deploy start --metadata ApexClass:myClass

```

SEE ALSO:

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dev_guide.htm)_

_VS Code Command_ [: SFDX: Create Apex Class](https://developer.salesforce.com/docs/platform/sfvscode-extensions/guide/apex-overview.html)

## Create an Apex Trigger

Use Apex triggers to perform custom actions before or after a change to a Salesforce record, such as an insertion, update, or deletion.
You can use Salesforce CLI to create Apex triggers in your local Salesforce DX project. The generated files live in a `triggers` directory
in a package directory of your project.

**1.** Open a terminal (macOS and Linux) or command prompt Windows and change to your Salesforce DX project directory.

**2.** Create the `triggers` directory in the location you want to generate the Apex trigger. For example, if you want to generate it in
the default package directory, create the `force-app/main/default/triggers` directory if it doesn’t exist.

**3.** Generate the Apex trigger; specify the trigger name with the `--name` flag and the `triggers` directory with the `--output-dir`
flag.

```
     sf apex generate trigger --name myTrigger --output-dir force-app/main/default/triggers

```

By default, the generated trigger is for `before insert` events on the generic sObject. Use the `--event` and `--sobject`
flags to change these default values. This example generates a trigger that fires before and after an insert into the Account object.

```
     sf apex generate trigger --name myTrigger --event 'before insert,after insert' --sobject

      Account --output-dir force-app/main/default/triggers

```

The command generates two files.

**•** `myTrigger.trigger-meta.xml` —metadata file

**•** `myTrigger.trigger` —Apex trigger source file

Use the `project deploy start` command to deploy the new Apex trigger to your org.

```
   sf project deploy start --metadata ApexTrigger:myTrigger --target-org myscratch

```

SEE ALSO:

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_triggers.htm)_ : Triggers

_Trailhead_ [: Apex Triggers](https://trailhead.salesforce.com/en/modules/apex_triggers)

_VS Code Command_ [: SFDX: Create Apex Trigger](https://developer.salesforce.com/docs/platform/sfvscode-extensions/guide/apex-overview.html)

## Create a Custom Object

You can use Salesforce CLI to generate the metadata files for new custom objects in your local Salesforce DX project.

**1.** Open a terminal (macOS and Linux) or command prompt Windows and change to your Salesforce DX project directory.


## Development Execute Anonymous Apex

**2.** Run the interactive `schema generate sobject` command. You must specify a label for your new custom object with the
`--label` flag. The command uses this label to provide intelligent suggestions for other object properties, such as its API name
and plural label.

```
     sf schema generate sobject --label "New Object"

```

Answer all the questions about your new object, such as the location of the generated files in your Salesforce DX project and whether
to enable various object properties.

After you create your custom object:

**•** Create a custom field on your new object with the interactive `schema generate field` command, which generates the
necessary metadata files in your project. You can also use the command to create a custom field on a standard object, such as
Account.

**•** Create a custom tab for your new object with the `schema generate tab` command.

Then deploy your new custom object to your org.

```
   sf project deploy start --metadata CustomObject:NewObject__c --target-org myscratch

```

The first time you deploy your new custom object to a source-tracking org, the org creates additional properties and sets new defaults
on it. For this reason, we recommend that you immediately retrieve the custom object so your local source files are updated with this
new information.

SEE ALSO:

_Salesforce Help_ [: Fields Required for Creating Custom Objects](https://help.salesforce.com/s/articleView?id=platform.dev_objectcreate.htm&type=5&language=en_US)

_Salesforce Help_ [: Custom Field Types](https://help.salesforce.com/s/articleView?id=platform.custom_field_types.htm&type=5&language=en_US)

_Salesforce Help_ [: Custom Field Attributes](https://help.salesforce.com/s/articleView?id=platform.custom_field_types.htm&type=5&language=en_US)

## Execute Anonymous Apex

You can execute an anonymous block of Apex code in an org with the `apex run` Salesforce CLI command.

**1.** Open a terminal (macOS and Linux) or command prompt Windows and change to your Salesforce DX project directory.

**2.** Run the `apex run` command with no flags to open an interactive shell. At the prompt, enter all your Apex code; press CTRL-D
when you're finished. Your code is then executed in a single execute anonymous request in the specified org, or the default org if
you don’t specify one.

```
     sf apex run --target-org myscratch

```

This output shows an example of executing the Apex code `system.debug ('Hello world!');`

```
     Start typing Apex code. Press the Enter key after each line, then press CTRL+D when

     finished.

     system.debug ('Hello world!');

     Compiled successfully.

     Executed successfully.

     58.0 APEX_CODE,DEBUG;APEX_PROFILING,INFO

     Execute Anonymous: system.debug ('Hello world!');

     14:23:06.174

     (174742273)|USER_INFO|[EXTERNAL]|0058H000005QWcE|test-ux9lpg9jyyqt@example.com|(GMT-07:00)

      Pacific Daylight Time (America/Los_Angeles)|GMT-07:00

```


## Development Run Apex Tests

```
     14:23:06.174 (174785450)|EXECUTION_STARTED

     14:23:06.174 (174792639)|CODE_UNIT_STARTED|[EXTERNAL]|execute_anonymous_apex

     14:23:06.174 (175417814)|USER_DEBUG|[1]|DEBUG|Hello world!

     14:23:06.175 (175529797)|CUMULATIVE_LIMIT_USAGE

     14:23:06.175 (175529797)|LIMIT_USAGE_FOR_NS|(default)|

      Number of SOQL queries: 0 out of 100

      Number of query rows: 0 out of 50000

      Number of SOSL queries: 0 out of 20

      Number of DML statements: 0 out of 150

      Number of Publish Immediate DML: 0 out of 150

      Number of DML rows: 0 out of 10000

      Maximum CPU time: 0 out of 10000

      Maximum heap size: 0 out of 6000000

      Number of callouts: 0 out of 100

      Number of Email Invocations: 0 out of 10

      Number of future calls: 0 out of 50

      Number of queueable jobs added to the queue: 0 out of 50

      Number of Mobile Apex push calls: 0 out of 10

     14:23:06.175 (175529797)|CUMULATIVE_LIMIT_USAGE_END

     14:23:06.174 (175598235)|CODE_UNIT_FINISHED|execute_anonymous_apex

     14:23:06.174 (175617689)|EXECUTION_FINISHED

```

Use the `--file` flag to execute Apex code in a file rather than interactively.

```
     sf apex run --file ~/test.apex

```

SEE ALSO:

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_anonymous_block.htm)_ : Anonymous Blocks

_VS Code Command_ [: SFDX: Execute Anonymous Apex with Currently Selected Text | Editor Contents](https://developer.salesforce.com/docs/platform/sfvscode-extensions/guide/apex-writing.html#anonymous-apex)

## Run Apex Tests

When you’re ready to test changes to your source code, you can run Apex tests in an org using Salesforce CLI on the command line. You
can also run Apex tests from Salesforce Extensions for VS Code or from within third-party continuous integration tools, such as Jenkins
or CircleCI.

Minimum User Permissions and Settings Required

The user running Apex tests must have these user permissions in the org:

**•** View Setup and Configuration

**•** API Enabled

Also ensure that the Enable Streaming API setting is enabled in the org’s user interface. The setting is enabled by default.

[See User Permissions and Configure User Interface Settings for details.](https://help.salesforce.com/articleView?id=platform.admin_userperms.htm&type=5&language=en_US)


Development Run Apex Tests

Run All Apex Tests and View Results

This command runs all Apex tests in the specified org asynchronously, which is the default behavior.

```
   sf apex run test --target-org myscratch

```

The command outputs the `apex get test` command with a job ID that you can then run to view the full results. For example:

```
   sf apex get test --test-run-id 7078HzRMVV --target-org myscratch

```

For more examples, see the help for the commands by running `sf apex run test --help` and `sf apex get test`
`--help` [CLI commands, or read the Salesforce CLI Reference, which contains the same information as the help output.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_apex_commands_unified.htm)

Determine Code Coverage in Orgs With Large Volumes of Apex Code

Before deploying Apex classes and triggers to your production org, or including them in an AppExchange managed package, you must
write unit tests that cover 75% of the total Apex code in your org. You can retrieve information about your current code coverage
percentage using one of these tools:

**•** Salesforce CLI: Specify the --code-coverage flag of the apex run test command. Or

**•** VS Code: Check the `retrieve-test-code-coverage` setting.

Both methods produce a report with detailed information about the code coverage of all Apex classes in your org.

To improve the performance for large test runs, check the **Store Only Aggregate Code Coverage** setting in your org from **Setup**    **Apex Test Execution**    - **Options...** . This setting improves the performance of gathering code coverage information for large orgs with
many Apex classes by turning off per-class code coverage. When the setting is checked, the Apex Code Coverage by Class table in the
Apex test results contains all Apex classes and triggers listed in `ApexCodeCoverageAggregate`, including classes that aren't
covered by the tests in the current Apex test run. You can drill down and check which classes aren’t covered, and then adjust your unit
tests to reach the required code coverage.

To minimize scrolling while viewing your code coverage information when you run only a handful of Apex tests, we recommend
unchecking the **Store Only Aggregate Code Coverage** setting. The Apex Code Coverage by Class table then shows only the Apex
classes and triggers covered by the current Apex test run. The calculation of per-class code coverage filters the entries in this table to
include only classes that were directly touched by the test methods in the run.

Here’s an example of how you can use the **Store Only Aggregate Code Coverage** setting to investigate and resolve code coverage
issues. A nightly build with the setting checked shows that the `Class032` has only 57% code coverage.


Development Run Apex Tests

Uncheck the setting and run the test on `Class032` to get code coverage information for just that class. Use this information to write
more unit tests for the class with low coverage. As you keep checking the new code coverage percentage of `Class032`, you no longer
have to scroll through the long results of all your Apex tests.


### Development Debug Apex Debug Apex

If you use Salesforce Extensions for Visual Studio Code (VS Code) for your development tasks, you have a choice of Apex Debugger
extensions. Whichever debugger you chose, you set breakpoints in your Apex classes and step through their execution to inspect
your code in real time to find bugs. You can run Apex tests in VS Code or on the command line.

Generate and View Apex Debug Logs
Apex debug logs can record database operations, system processes, and errors that occur when executing a transaction or running
unit tests in any authenticated org. Enable the Debug Log in Salesforce Extensions for VS Code, then view the logs with VS Code or
Salesforce CLI.

SEE ALSO:

_Apex Developer Guide_ [: Debugging, Testing, and Deploying Apex](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_debug_test_deploy.htm)

_[Salesforce CLI Command Reference](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_apex_commands_unified.htm)_ : Apex Commands

[Test Anything Protocol (TAP)](https://testanything.org/)

_VS Code Command_ [: SFDX: Run Apex Tests | Test Suite](https://developer.salesforce.com/docs/platform/sfvscode-extensions/guide/apex-testing.html)

### Debug Apex

If you use Salesforce Extensions for Visual Studio Code (VS Code) for your development tasks, you have a choice of Apex Debugger
extensions. Whichever debugger you chose, you set breakpoints in your Apex classes and step through their execution to inspect your
code in real time to find bugs. You can run Apex tests in VS Code or on the command line.


### Development Generate and View Apex Debug Logs

Apex Replay Debugger

[Apex Replay Debugger is available for use without any additional licenses. To configure and use it, see Apex Replay Debugger.](https://developer.salesforce.com/docs/platform/sfvscode-extensions/guide/replay-debugger.html)

Apex Interactive Debugger

You must have at least one available Apex Debugger session in your Dev Hub org. To purchase more sessions for an org, contact your
[System Admin to open a case.](https://help.salesforce.com/articleView?id=000314082&type=1&mode=1&language=en_US)

**•** Performance Edition and Unlimited Edition orgs include one Apex Debugger session.

**•** Apex Debuggers sessions aren’t available in Trial and Developer Edition orgs.

**•** You can purchase Apex Debugger sessions for Enterprise Edition orgs.

Enable the Apex Debugger in your scratch orgs by adding the `DebugApex` feature to your scratch org definition file:

```
   "features": "DebugApex"

```

[To configure and use it, see Apex Interactive Debugger.](https://developer.salesforce.com/docs/platform/sfvscode-extensions/guide/interactive-debugger.html)

ISV Customer Debugger (Salesforce Extensions for VS Code Only)

ISV Customer Debugger is part of the Apex Interactive Debugger ( `salesforcedx-vscode-apex-debugger` ) extension, so
you don’t have to install anything other than the Salesforce Extension Pack and its prerequisites. You can debug only sandbox orgs.

[See ISV Customer Debugger in Salesforce Extensions for VS Code for details.](https://developer.salesforce.com/docs/platform/sfvscode-extensions/guide/isv-debugger.html)

SEE ALSO:

[Visual Studio Marketplace: Apex Replay Debugger extension](https://marketplace.visualstudio.com/items?itemName=salesforce.salesforcedx-vscode-apex-replay-debugger)

[Visual Studio Marketplace: Apex Interactive Debugger extension](https://marketplace.visualstudio.com/items?itemName=salesforce.salesforcedx-vscode-apex-debugger)

### Generate and View Apex Debug Logs

Apex debug logs can record database operations, system processes, and errors that occur when executing a transaction or running unit
tests in any authenticated org. Enable the Debug Log in Salesforce Extensions for VS Code, then view the logs with VS Code or Salesforce
CLI.

**1.** In Salesforce Extensions for VS Code, prepare the org to generate logs and configure the debugger.

**a.** Log in to the org.

**b.** For Replay Debugger, run **SFDX: Turn on Apex Debug Log for Replay Debugger** .

**c.** [Create a launch configuration file for Replay Debugger or Interactive Debugger.](https://developer.salesforce.com/docs/platform/sfvscode-extensions/guide/replay-debugger.html)

**2.** After you run the tests, get a list of the debug logs.

```
     sf apex list log --target-org myscratch

     APPLICATION DURATION (MS) ID LOCATION SIZE (B) LOG USER OPERATION REQUEST

      START TIME STATUS

     ─────────────────────────────── ────────────────────────────────────────────────

      ─────────── ───────

     Unknown 1143 07L9Axx SystemLog 23900 User User ApexTestHandler Api

      2017-09-05x Success

```


Development Generate and View Apex Debug Logs

**3.** View a debug log by passing its ID to the `apex get log` command.

```
     sf apex get log --log-id 07L9A000000aBYGUA2

     38.0

     APEX_CODE,FINEST;APEX_PROFILING,INFO;CALLOUT,INFO;DB,INFO;SYSTEM,DEBUG;VALIDATION,INFO;VISUALFORCE,INFO;WAVE,INFO;WORKFLOW,INFO

     15:58:57.3

     (3717091)|USER_INFO|[EXTERNAL]|0059A000000TwPM|test-ktjauhgzinnp@example.com|Pacific

     Standard Time|GMT-07:00

     15:58:57.3 (3888677)|EXECUTION_STARTED

     15:58:57.3

     (3924515)|CODE_UNIT_STARTED|[EXTERNAL]|01p9A000000FmMN|RejectDuplicateFavoriteTest.acceptNonDuplicate()

     15:58:57.3 (5372873)|HEAP_ALLOCATE|[72]|Bytes:3

     ...

```

SEE ALSO:

_[Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_debugging_debug_log.htm)_ : Debug Log


# CHAPTER 12 Build and Release Your App

In this chapter ...

When you finish writing your code, the next step is to deploy it. We offer different deployment options
based on your role and needs as a customer, system integrator, or independent software vendor (ISV)
partner.

# • Build and Release partner.

Your App with
To learn about the benefits of the different development models, review these Trailhead modules:
Metadata API

**•** [Org Development Model](https://trailhead.salesforce.com/content/learn/modules/org-development-model)

**•** [Package Development Model](https://trailhead.salesforce.com/content/learn/modules/sfdx_dev_model)

**•** [Quick Start: Unlocked Packages](https://trailhead.salesforce.com/projects/quick-start-unlocked-packages)

**•** [Unlocked Packages for Customers](https://trailhead.salesforce.com/trails/sfdx_get_started/modules/unlocked-packages-for-customers)

You have several tooling options, based on how you decide to build and release yours apps.

Customers and Non-ISV Partners

**•** [Agentforce Vibes IDE – A web-based integrated development environment that has all the power](https://developer.salesforce.com/docs/platform/code-builder/guide/codebuilder-overview.html)
and flexibility of Visual Studio Code, Salesforce Extensions for VS Code, and Salesforce CLI in your
web browser.

**•** [Salesforce Extensions for VS Code – A set of extensions that come with rich tools for developing on](https://developer.salesforce.com/docs/platform/sfvscode-extensions/guide/vscode-overview.html)
the Salesforce platform.

**•** [Salesforce CLI – A command-line interface that simplifies development and build automation when](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_setup.meta/sfdx_setup/sfdx_setup_intro.htm)
working with your Salesforce org

**•** [Metadata API – An API for deploying, retrieving, creating, updatinge, or deleting customizations.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_use_cases_deploy_prod.htm)

**•** [DevOps Center – Change and release management for declarative and pro-code developers.](https://help.salesforce.com/s/articleView?id=platform.devops_center_setup.htm&type=5&language=en_US)

**•** [Unlocked Packages – For customers who want to organize metadata into a package and deploy the](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_unlocked_pkg_intro.htm)
metadata (via packages) to different orgs.

ISV Partners

**•** Second-Generation Managed Packages

If you’re an ISV that develops apps and lists them on AppExchange, Salesforce recommends managed
packages.

Second-generation managed packaging (managed 2GP) ushers in a new way for AppExchange
partners to develop, distribute, and manage their apps and metadata. You can use managed 2GP
to organize your source, build small modular packages, integrate with your version control system,
and better utilize your custom Apex code. You can execute all packaging operations via Salesforce
CLI, or automate them using scripts.


Build and Release Your App

[For more information on managed 2GP packages, see the Second-Generation Managed Packaging](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp.htm)

**•** First-Generation Managed Packages

Similar to managed 2GP, managed 1GP packages are used by ISVs to distribute their business apps
to customers via AppExchange.

If you’re familiar with first-generation managed packages and want to learn more about how 1GP
[differs from 2GP, see Comparison of First- and Second-Generation Managed Packages.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_comparison.htm)

[For more information on managed 1GP packages, see Create a First-Generation Managed Package](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/sfdx_dev_build_release.htm)
[using Salesforce DX.](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/sfdx_dev_build_release.htm)


## Build and Release Your App Build and Release Your App with Metadata API Build and Release Your App with Metadata API

Develop and test your app in your sandboxes. Use Salesforce CLI or Salesforce Extensions for VS Code to retrieve and deploy your source.
This development work flow is called the org development model.

Develop and Test in a Sandbox Using the Org Development Model

Similar to change sets, the release artifact is a set of changed metadata to update in the production org. You can develop, test, and
deploy your changes using the `project deploy` commands. If you want to know more about this development model, see the
[Org Development Model module in Trailhead.](https://trailhead.salesforce.com/content/learn/modules/org-development-model)

Development and Release Environments

**1. Develop and test:** Each team member has their own Developer sandbox to create their assigned customization. Developer sandboxes
contain no production data.

**2. Build release:** Team members each migrate their customizations from their respective developer sandboxes to a shared Developer
Pro sandbox for integration. Developer Pro sandboxes don’t contain production data, but you can seed them with testing data.

**3. Test release:** For user-acceptance testing, the team uses a Partial sandbox to create a complete replica of production.

**4. Release:** After the release is in production, the team can use the Full sandbox to train users without the risk of altering production
data. A Full sandbox includes a copy of production data.


Build and Release Your App Build and Release Your App with Metadata API

What Tools Do I Need?

Considerations for Deploying Apex Code

To deploy Apex to production, unit tests of your Apex code must meet coverage requirements. Code coverage indicates how many
executable lines of code in your classes and triggers are covered by your test methods. Write test methods to test your triggers and
classes, and then run those tests to generate code coverage information.

If you don’t specify a test level when initiating a deployment, the default test execution behavior depends on the contents of your
deployment package.

**•** If your deployment package contains Apex classes or triggers, when you deploy to production, all tests are executed, except tests
that originate from a managed package.

**•** If your package doesn’t contain Apex code, no tests are run by default.

You can run tests for a deployment of non-Apex components. You can override the default test execution behavior by setting the test
level in your deployment options. Test levels are enforced regardless of the types of components present in your deployment package.


### Build and Release Your App Develop and Test Changes Locally

We recommend that you run all local tests in your development environment, such as a sandbox, before deploying to production.
Running tests in your development environment reduces the number of tests required in a production deployment.

### Develop and Test Changes Locally

Develop changes in source format, deploying to and retrieving from your Developer sandbox.

Build and Test the Release Artifact
After your team has finished its development tasks, transition to the build release phase to integrate your changes in a Developer
Pro sandbox. Then build the release artifact.

Test the Release Artifact in a Staging Environment
Stage the changes and run regression tests in a Full sandbox.

Release Your App to Production
Now that all your tests have passed in the Full sandbox, you’re ready to deploy to production.

Cancel a Metadata Deployment
You can cancel a metadata deployment from Salesforce CLI and specify a wait time for the command to complete.

### Develop and Test Changes Locally

Develop changes in source format, deploying to and retrieving from your Developer sandbox.

These steps provide the high-level work flow.

**1.** Create a DX project.

A DX project has a specific structure and configuration files that Salesforce DX tooling requires. See Create a Salesforce DX Project.

**2.** Create a source control repository or use an existing one.

If you’re using an existing repo, be sure it has the required DX configuration files. See Salesforce DX Project Structure and Source
Format.

**3.** Authorize the Developer sandbox.

See Authorize an Org Using a Browser.

**4.** Perform development tasks in your developer sandbox.

**5.** Retrieve the changes from the developer sandbox.

If your sandbox is source tracked, changes are automatically identified. To retrieve just the changed metadata:

```
     sf project retrieve start

```

If your sandbox isn’t source tracked, or want to retrieve metadata that hasn’t changed, or you want to retrieve many changes, you
can use a manifest ( `package.xml` ).

```
     sf project retrieve start --manifest path/to/package.xml

```

Run `sf project retrieve start --help` for all command options with examples.

**6.** Commit the changes to the source control repository.

[Next: Deploy all changes the team has made to the first testing environment to test those changes. See Salesforce CLI Reference: deploy](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_deploy_commands_unified.htm)
[Commands.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_deploy_commands_unified.htm)


### Build and Release Your App Build and Test the Release Artifact Build and Test the Release Artifact

After your team has finished its development tasks, transition to the build release phase to integrate your changes in a Developer Pro
sandbox. Then build the release artifact.

Here are the high-level steps in the work flow to create the release artifact.

**1.** Pull the changes from the repo so your local project contains all the changes your team has made.

**2.** Authorize the Developer Pro sandbox.

**3.** Run the deploy command that mimics what you’ll deploy to production, for example:

```
     sf project source deploy --manifest manifest/package.xml --target-org dev-pro-sandbox

     \

     --test-level RunSpecifiedTests --tests TestMyCode

```

**4.** Open the sandbox.

**5.** Perform testing.

**6.** If the testing passes, continue to the test release phase where you deploy the release artifact to the partial sandbox. Then perform
user-acceptance testing.

After the testing passes, move to the release phase and perform regression tests in the Full sandbox.

### Test the Release Artifact in a Staging Environment

Stage the changes and run regression tests in a Full sandbox.

After you have made all your changes based on the integration testing, the next step is to stage the changes in a Full sandbox. The
process of deploying changes to the Full sandbox is similar to the process you used to deploy changes to your Developer Pro sandbox.
This phase includes regression testing and mimics how you release the changes to production.

These steps provide the high-level work flow.

**1.** Authorize the Full sandbox.

**2.** (Optional) If you made any changes based on your testing in the Developer Pro sandbox, create a release artifact ( `.zip` ). If not, use
the existing release artifact.

**3.** To validate the deployment without saving the components in the target org, run all local (regression) tests. A validation enables
you to verify the results of tests that would be executed during a deployment, but doesn’t commit any changes.

```
     sf project deploy validate --manifest manifest/package.xml --target-org full-sandbox

     --test-level RunLocalTests

```

**4.** Test the actual production deployment steps in the staging sandbox. Set up the same quick deploy that you plan to execute against
the production org.

```
     sf project deploy validate --manifest manifest/package.xml --target-org full-sandbox

     --test-level RunSpecifiedTests

```

This command returns a job ID that you reference in the quick deploy.

**5.** Next, test the quick deploy using the job ID returned in the previous step.

```
     sf project deploy quick --target-org full-sandbox --job-id jobID

```

After you validate a deployment, you have 10 days to perform the quick deployment to production.


### Build and Release Your App Release Your App to Production Release Your App to Production

Now that all your tests have passed in the Full sandbox, you’re ready to deploy to production.

**1.** In your deployment run list, complete any pre-deployment tasks.

**2.** Authorize your production org.

**3.** Set up the quick deploy by validating the deployment.

```
     sf project deploy validate --source-dir force-app --target-org prod-org --test-level

     RunLocalTests

```

This command returns a job ID that you reference in the quick deploy.

**4.** After the tests are run, verify that all the Apex tests have passed. Be sure that the tests cover at least 75% of the code being deployed.

**5.** Run the quick deploy:

```
     sf project deploy quick --target-org prod-org --job-id jobID

```

**6.** Open the production org, then perform any post-deployment tasks listed in the deployment run list.

### Cancel a Metadata Deployment

You can cancel a metadata deployment from Salesforce CLI and specify a wait time for the command to complete.

To cancel your most recent deployment, run `project deploy cancel --use-most-recent` . You can cancel earlier
deployments by using the `--job-id <JOBID>` flag to specify the deployment that you want to cancel.

```
   sf project deploy cancel --job-id <jobid>

```

The default wait time for the cancel command to complete and display its results in the terminal window is 33 minutes. If the command
isn’t completed by the end of the wait period, the CLI returns control of the terminal window to you. You can adjust the wait time as
needed by specifying the number of minutes in the `--wait` flag, as shown in the following example:

```
   sf project deploy cancel --wait 20 --use-most-recent

```

Curious about the status of a canceled deployment? Run a deployment report.

```
   sf project deploy report --use-most-recent

```


# CHAPTER 13 Unlocked Packages

In this chapter ...

**•** What’s an Unlocked
Package?

Salesforce offers different types of packages, and unlocked packages are especially suited for internal
business apps. Unless you plan to distribute an app on AppExchange, an unlocked package is the right
package type for most use cases. You can use unlocked packages to organize your existing metadata,
package an app, extend an app that you’ve purchased from AppExchange, or package new metadata.

**•** Package-Based
Unlocked packages follow a source-driven development model. The source of truth of the metadata
Development Model
contained in the package is your version control system, not what’s in an org. This model brings with it

**•** Before You Create
all the benefits of modern source-driven development models.
# Unlocked Packages

**•** Know Your Orgs

**•** Create
Org-Dependent
# Unlocked Packages

**•** Workflow for
# Unlocked Packages

**•** Configure Unlocked
Packages

**•** How We Handle
Profile Settings in
# Unlocked Packages

**•** Develop Unlocked
Packages

**•** Push a Package
Upgrade for
# Unlocked Packages

**•** Install an Unlocked
Package

**•** Migrate Deprecated
Metadata from
# Unlocked Packages

**•** Uninstall an
# Unlocked Package

**•** Transfer an Unlocked
Package to a
Different Dev Hub

Note: If you’re an AppExchange partner that plans to distribute your app to customers via
[AppExchange, use second-generation managed packaging. See Second-Generation Managed](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp.htm)
[Packages for more information.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp.htm)


## Unlocked Packages What’s an Unlocked Package? What’s an Unlocked Package?

If you’re new to packaging, think of a package as a container that you fill with metadata. It contains a set of related features, customizations,
and schema. Unlocked packages help you add, edit, and remove metadata in your org in a trackable way. You can apply your metadata
to multiple orgs, and upgrade your Salesforce apps easier and faster. Unlocked packages are especially suited for internal business apps.

[Unlocked packages differ from managed packages, which have manageability rules that determine the behavior of each metadata](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/packaging_packageable_components.htm)
component in the package. With an unlocked package, you have a lot of flexibility. Your admins can make changes directly in production
in response to emergency change requests because metadata in unlocked packages can be modified in a production org.

At the same time, this flexibility comes with responsibility. Ensure that you have the proper governance in place to prevent cases where
package updates overwrite changes that admins make directly in production. You can avoid this issue by ensuring that your admins
communicate with your development team whenever they edit any packaged metadata directly in the production org.

Each unlocked package has a distinct lifecycle. When you add metadata to an existing unlocked package, you create a new package
version. While the package is continually evolving, each package version is an immutable artifact that never changes.

A package version contains the specific metadata and features associated with the package version at the time it was created. As you
iterate on your package, and add, remove, or change the packaged metadata, you create many package versions.

You can install a package version in a scratch, sandbox, trial, Developer Edition, or production org. Installing a package version is similar
to deploying metadata. Each package version has a version number, and subscribers can install a new package version into their org
through a package upgrade.

Note: Because package versions are immutable, they can also be used as artifacts for Continuous Integration (CI) and Continuous
Delivery (CD) processes.

You can repeat the package development cycle any number of times. You can change metadata, create a package version, test the
package version, and finally install the package to a production org. This distinct app development lifecycle lets you control exactly what,
when and how your metadata is rolled out. In the installed org, you can inspect which metadata came from which package and the set
of all metadata associated with a specific package.

## Package-Based Development Model

To demonstrate the power of unlocked packages, here’s how packaging works in the traditional development model. For most production
orgs, metadata traditionally is contained in two buckets: a set of managed packages installed from AppExchange, and unpackaged
metadata.

Customers often invest in Salesforce customizations to support business processes and extend the power of the Salesforce platform. In
the development model, your Salesforce org’s monolith of unpackaged metadata contains all the metadata that belongs to a custom
app or extension. Because that metadata isn’t isolated or organized, it can be difficult to understand, upgrade, and maintain.

In the package development model, you can organize your unpackaged metadata in your production org into well-defined packages.
And you can use Salesforce DX projects to organize your source into package directories with everything managed in a version control
system of your choice. Your end goal is to create packages using those directories that are versionable, easy to maintain, update, install,
and upgrade.

Unlocked packages allow you to declare multi-level dependencies on one or many managed and unlocked packages, which keeps your
packages small and modular. You can use the command line to execute unlocked packaging operations, or you can include
packaging-specific Salesforce CLI commands in a script and automate your package development.


## Unlocked Packages Before You Create Unlocked Packages Before You Create Unlocked Packages

When you use unlocked packaging, to be sure that you set it up correctly, verify the following.

Did you?

**•** [Enable Dev Hub in Your Org](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_setup_enable_devhub.htm)

**•** [Enable Second-Generation Managed Packaging](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_setup_enable_secondgen_pkg.htm)

**•** [Install Salesforce CLI](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_setup.meta/sfdx_setup/sfdx_setup_intro.htm)

Note: Unlocked packaging is available with these licenses: Salesforce or Salesforce Limited Access - Free (partners only).

Developers who work with unlocked packages need the correct permission set in the Dev Hub org. Developers need either the System
[Administrator profile or the Create and Update Second-Generation Packages permission. For more information, see Add Salesforce DX](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_setup_add_users.htm)
[Users.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_setup_add_users.htm)

The maximum number of unlocked package versions that you can create from a Dev Hub per day is the same as your daily scratch org
allocation. To request a limit increase, contact Salesforce Customer Support.

Scratch orgs and packages count separately, so creating an unlocked package doesn’t count against your daily scratch org limit. To view
your scratch org limits, use the CLI:

```
   sf limits api display

```

[For more information on scratch org limits, see Scratch Orgs.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_scratch_orgs.htm)

## Know Your Orgs

Some of the orgs that you use with unlocked packaging have a unique purpose.

Choose Your Dev Hub Org

Use the Dev Hub org for these purposes.

When you create an unlocked package using Salesforce CLI, you associate the package with a specific Dev Hub org. When you’re ready
to define and create a package for production use, be sure to create the package using the Dev Hub in one of your production orgs.

The Dev Hub org is the owner of all unlocked packages you create, and is used:

**•** To link your namespaces if you want to create namespaced unlocked packages

**•** To authorize and run your `sf package` commands

If an unlocked package is associated with a non-production Dev Hub org, and that org expires or becomes inactive, the installed package
can't be updated, and new attempts to install the package may fail.

Namespace Org

If you are using a namespace, you must create an org for the sole purpose of specifying the namespace for your package. We refer to
this org as your namespace org.. If you want to use the namespace strictly for testing, choose a disposable namespace.

After you create a namespace org and use it to specify your namespace, open your Dev Hub org and link the namespace org to your
Dev Hub org.


## Unlocked Packages Create Org-Dependent Unlocked Packages

Other Orgs

When you work with packages, you also use these orgs:

**•** You can create scratch orgs on the fly to use while testing your packages.

**•** The target or installation org is where you install the package.

## Create Org-Dependent Unlocked Packages

Org-dependent unlocked packages are a variation of unlocked packages that allow you to create
packages that depend on unpackaged metadata in the org where you plan to install the package
(installation org).

Untangling your production org metadata can be a daunting project. But now you have a solution
that enables you to package metadata without completely accounting for all metadata dependencies:
org-dependent unlocked packages. When you use org-dependent unlocked packages, metadata
validation occurs during package installation, instead of during package version creation.

USER PERMISSIONS

To create packages:

**•** Create and Update
Second-Generation
Packages

Longstanding and large production orgs often accumulate large amounts of metadata that are difficult to modularize when adopting
a package-based Application Lifecycle Management (ALM) approach. Instead, you can package metadata that depends on unpackaged
metadata in the installation org.

Note: Org-dependent unlocked packages are a variation of unlocked packages, and not a separate package type. They follow
[the same package development steps, and use the same supported metadata types as unlocked packages.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_unlocked_pkg_workflow.htm)

To create an org-dependent unlocked package, specify the `orgdependent` CLI parameter on the `sf package create` CLI
command.

```
sf package create -t Unlocked -r force-app -n MyPackage --org-dependent

```


## Unlocked Packages Workflow for Unlocked Packages

To review which of your packages are org-dependent unlocked packages, use `sf package list --verbose` .

## Workflow for Unlocked Packages

You can create and install an unlocked package directly from the Salesforce command line.

Review and complete the steps in Before You Create Unlocked Packages before starting this workflow.

The basic workflow includes these steps. See specific topics for details about each step.

**1.** Create a DX project.

```
  sf project generate --output-dir expense-manager-workspace --name expenser-app

```

**2.** Authorize the Dev Hub org, and create a scratch org.

```
  sf org login web --set-default-dev-hub --alias MyDevHub

```

When you perform this step, include the `--set-default-dev-hub` option. You can then omit the Dev Hub username when
running subsequent Salesforce CLI commands.

Tip: If you define an alias for each org you work with, it’s easy to switch between different orgs from the command line. You
can authorize different orgs as you iterate through the package development cycle.

**3.** Create a scratch org and develop the package. You can use VS Code and the Setup UI in the scratch org to build and retrieve the
pieces you want to include in your package. Navigate to the expenser-app directory, and then run this command.

```
  sf org create scratch --definition-file config/project-scratch-def.json --alias MyTestOrg1

   --duration-days 30

```

**4.** Verify that all package components are in the project directory where you want to create a package.

**5.** From the Salesforce DX project directory, create the package.

```
  sf package create --name "Expense Manager" --path force-app

  --package-type Unlocked

```

**6.** Review your `sfdx-project.json` file. The CLI automatically updates the project file to include the package directory and
creates an alias based on the package name.

```
  {

    "packageDirectories": [

      {

       "path": "force-app",

       "default": true,

       "package": "Expense Manager",

       "versionName": "ver 0.1",

```


## Unlocked Packages Configure Unlocked Packages

```
          "versionNumber": "0.1.0.NEXT"

         }

       ],

       "namespace": "",

       "sfdcLoginUrl": "https://login.salesforce.com",

       "sourceApiVersion": "59.0",

       "packageAliases": {

         "Expense Manager": "0Hoxxx"

       }

     }

```

Notice the placeholder values for `versionName` and `versionNumber` .

Specify the features and org settings required for the metadata in your package using an external . `json` file, such as the scratch org
definition file. You can specify using the `--definition-file` flag with the `sf package version create` command,
or list the definition file in your `sfdx-project.json` file. See: Project Configuration File for Unlocked Packages

**7.** Create a package version. This example assumes the package metadata is in the `force-app` directory.

```
     sf package version create --package "Expense Manager" --installation-key test1234 --wait

      10

```

**8.** Install and test the package version in a scratch org. Use a different scratch org from the one you used in step three.

```
     sf package install --package "Expense Manager@0.1.0-1" --target-org MyTestOrg1

     --installation-key test1234 --wait 10 --publish-wait 10

```

**9.** After the package is installed, open the scratch org to view the package.

```
     sf org open --target-org MyTestOrg1

```

Package versions are beta until you promote them to a managed-released state. See: Release an Unlocked Package.

## Configure Unlocked Packages

You include an entry in the `sfdx-project.json` file for each package to specify its alias, version details, dependencies, features,
and org settings. From the command line, you can also set or change options, such as specifying an installation key, update the package
name, or add a description.

Project Configuration File for Unlocked Packages
The project configuration file is a blueprint for your project. The settings in the file create an outline of your package and determine
the package attributes and package contents.

Unlocked Packaging Keywords
A keyword is a variable that you can use to specify a package version number.

Package Installation Key
To ensure the security of the metadata in your package, you must specify an installation key when creating a package version.
Package creators provide the key to authorized subscribers so they can install the package. Package installers provide the key during
installation, whether installing the package from the CLI or from a browser. An installation key is the first step during installation.
The key ensures that no package information, such as the name or components, is disclosed until the correct installation key is
supplied.


### Unlocked Packages Project Configuration File for Unlocked Packages

Extract Dependency Information from Unlocked Packages
For an installed unlocked package, you can now run a simple SOQL query to extract its dependency information. You can also create
a script to automate the installation of unlocked packages with dependencies.

Understanding Namespaces
A namespace is a 1-15 character alphanumeric identifier that distinguishes your package and its contents from other packages in
your org.

Share Release Notes and Post-Install Instructions
Share details about what’s new and changed in a released unlocked package with your users.

Specify Unpackaged Metadata or Apex Access for Apex Tests (Unlocked Packages)

Best Practices for Unlocked Packages
We suggest that you follow these best practices when working with unlocked packages.

Package IDs and Aliases for Unlocked Packages
During the package lifecycle, packages and package versions are identified by an ID or package alias. When you create a package or
package version, Salesforce CLI creates a package alias based on the package name, and stores that name in the
`sfdx-project.json` file. When you run CLI commands or write scripts to automate packaging workflows, it’s often easier to
reference the package alias, instead of the package ID or package version ID.

Frequently Used Unlocked Packaging Operations

### Project Configuration File for Unlocked Packages

The project configuration file is a blueprint for your project. The settings in the file create an outline of your package and determine the
package attributes and package contents.

Here are the parameters you can specify in the project configuration file.


Unlocked Packages Project Configuration File for Unlocked Packages


Unlocked Packages Project Configuration File for Unlocked Packages


Unlocked Packages Project Configuration File for Unlocked Packages


Unlocked Packages Project Configuration File for Unlocked Packages


Unlocked Packages Project Configuration File for Unlocked Packages

When you specify a parameter using Salesforce CLI, it overrides the value listed in the project definition file.

The Salesforce DX project definition file is a JSON file located in the root directory of your project. Use the `sf project generate`
CLI command to generate a project file that you can build upon. Here’s how the parameters in `packageDirectories` appear.

```
   {

     "namespace": "",

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

         "postInstallUrl": "https://expenser.com/post-install-instructions.html",

         "releaseNotesUrl": "https://expenser.com/summer-2024-release-notes.html",

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

```


### Unlocked Packages Unlocked Packaging Keywords

```
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

### Unlocked Packaging Keywords

A keyword is a variable that you can use to specify a package version number.

You can use keywords to automatically increment the value of the package build numbers, ancestor version numbers, set the package
dependency to the latest version, or the latest released and promoted version.


### Unlocked Packages Package Installation Key

### Package Installation Key

To ensure the security of the metadata in your package, you must specify an installation key when creating a package version. Package
creators provide the key to authorized subscribers so they can install the package. Package installers provide the key during installation,
whether installing the package from the CLI or from a browser. An installation key is the first step during installation. The key ensures
that no package information, such as the name or components, is disclosed until the correct installation key is supplied.

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
sf package version create --package "Expense Manager" --directory common \

--tag 'Release 1.0.0' --installation-key-bypass

```


### Unlocked Packages Extract Dependency Information from Unlocked Packages

Check Whether a Package Version Requires an Installation Key

To determine whether a package version requires an installation key, use either the `sf package version list` or `sf package`
`version report` CLI command.

### Extract Dependency Information from Unlocked Packages

For an installed unlocked package, you can now run a simple SOQL query to extract its dependency information. You can also create a
script to automate the installation of unlocked packages with dependencies.

The SubscriberPackageVersion Tooling API object now provides dependency information. Using a SOQL query on SubscriberPackageVersion,
you can identify the packages on which your unlocked package has a dependency. You can get the (04t) IDs and the correct install order
for those packages.

Example: Package B has a dependency on package A. Package D depends on packages B and C. Here’s a sample
`sfdx-project.json` that you would have specified while creating a package version. Package D dependencies are noted
as packages A, B, and C.

```
      {

        "packageDirectories": [

           {

             "path": "pkg-a-workspace",

             "package": "pkgA",

             "versionName": "ver 4.9",

             "versionNumber": "4.9.0.NEXT",

             "default": true

           },

           {

             "path": "pkg-b-workspace",

             "package": "pkgB",

             "versionName": "ver 3.17",

             "versionNumber": "3.17.0.NEXT",

             "default": false,

             "dependencies": [

               {

                  "package": "pkgA",

                  "versionNumber": "3.3.0.LATEST"

               }

             ]

           },

           {

             "path": "pkg-c-workspace",

             "package": "pkgC",

             "versionName": "ver 2.1",

             "versionNumber": "2.1.0.NEXT",

             "default": false

           },

           {

             "path": "pkg-d-workspace",

             "package": "pkgD",

             "versionName": "ver 1.1",

             "versionNumber": "1.1.0.NEXT",

             "default": false,

             "dependencies": [

```


### Unlocked Packages Understanding Namespaces

```
               {

                  "package": "pkgA",

                  "versionNumber": "3.3.0.LATEST"

               },

               {

                  "package": "pkgB",

                  "versionNumber": "3.12.0.LATEST"

               },

               {

                  "package": "pkgC",

                  "versionNumber": "2.1.0.LATEST"

               }

             ]

           }

        ],

        "namespace": "",

        "sfdcLoginUrl": "https://login.salesforce.com",

        "sourceApiVersion": "44.0",

        "packageAliases": {

           "pkgA": "0HoB00000008Oq6KAE",

           "pkgB": "0HoB00000008OqBKAU",

           "pkgC": "0HoB00000008OqGKAU",

           "pkgD": "0HoB00000008OqGKAQ"

        }

      }

```

Before installing pkgD (with ID=04txx000000082hAAA), use this SOQL query to determine its dependencies. The username is
typically the target subscriber org where the unlocked package is to be installed.

```
      sf data query -u {USERNAME} -t

        -q "SELECT Dependencies FROM SubscriberPackageVersion

          WHERE Id='04txx000000082hAAA'" --json

```

You see this output when you run the query, with the (04t) IDs for pkgA, pkgB, and pkgC in that order.

```
      "Dependencies":{"Ids":[

        {"subscriberPackageVersionId":"04txx000000080vAAA"},

        {"subscriberPackageVersionId":"04txx000000082XAAQ"},

        {"subscriberPackageVersionId":"04txx0000000AiGAAU"}]}

### Understanding Namespaces

```

A namespace is a 1-15 character alphanumeric identifier that distinguishes your package and its contents from other packages in your
org.

When you specify a package namespace, every component added to a package has the namespace prefixed to the component API
name. Let’s say you have a custom object called Insurance_Agent with the API name, `Insurance_Agent__c` . If you add this
component to a package associated with the Acme namespace, the API name becomes `Acme__Insurance_Agent__c` .

You can choose to create unlocked packages with or without a specific namespace. A namespace is assigned to a package at the time
that it’s created and can’t be changed.


Unlocked Packages Understanding Namespaces

Important: When creating a namespace, use something that’s useful and informative to users. However, don’t name a namespace
after a person (for example, by using a person's name, nickname, or private information).

When you work with namespaces, keep these considerations in mind.

**•** You can develop more than one unlocked package with the same namespace but you can associate each package with only a single
namespace.

**•** If you work with more than one namespace, we recommend that you set up one project for each namespace.

**•** [If you have unlocked packages and managed packages in the same namespace, make sure to enable debug logging at the namespace](https://help.salesforce.com/s/articleView?id=xcloud.code_add_users_debug_log.htm&language=en_US)
[level so that you can capture logs from Apex classes across packages.](https://help.salesforce.com/s/articleView?id=xcloud.code_add_users_debug_log.htm&language=en_US)

#### Create and Register Your Namespace

With unlocked packages, you can share a single namespace with multiple packages. Since sharing of code is much easier if your
package shares the same namespace, we recommend that if use namepaces, you use a single namespace for your namespaced
unlocked packages.

Avoid Namespace Collisions
Namespaces impact the combination of package types you can install in an org.

Namespace-Based Visibility for Apex Classes in Unlocked Packages
The `@namespaceAccessible` makes public Apex in a package available to other packages that use the same namespace.
Without this annotation, Apex classes, methods, interfaces, and properties defined in an unlocked package aren’t accessible to the
other packages with which they share a namespace. Apex that is declared global is always available across all namespaces, and
needs no annotation.

#### Create and Register Your Namespace

With unlocked packages, you can share a single namespace with multiple packages. Since sharing of code is much easier if your package
shares the same namespace, we recommend that if use namepaces, you use a single namespace for your namespaced unlocked packages.

To create a namespace:

**1.** Sign up for a new Developer Edition org.

**2.** In Setup, enter _`Package Manager`_ in the Quick Find box, and select **Package Manager** .

**3.** In Namespace Settings, click **Edit** .

**4.** Enter a namespace and select **Check Availability** .

**5.** (Optional) Select a package to associate with this namespace, or select **None**, then click **Review** .


Unlocked Packages Understanding Namespaces

**6.** Review your selections, and then click **Save** .

To register a namespace:

**1.** [To link the namespace that you created with your Dev Hub, use Namespace Registry. See Link a Namespace to a Dev Hub for details.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_reg_namespace.htm)

**2.** In the `sfdx-project.json` file, specify your namespace using the namespace attribute. When you create a new unlocked
package, the package is associated with the namespace specified in the `sfdx-project.json` file.

#### Avoid Namespace Collisions

Namespaces impact the combination of package types you can install in an org.

To understand how namespaces affect the types of packages you can install in a namespaced or no-namespace org, review this table.

To understand how namespaces affect the combination of packages that can be installed into one org, review this table.


Unlocked Packages Understanding Namespaces

Namespaces and Package Dependencies

A namespaced unlocked package can’t depend on an unlocked package without a namespace.

#### Namespace-Based Visibility for Apex Classes in Unlocked Packages

The `@namespaceAccessible` makes public Apex in a package available to other packages that use the same namespace. Without
this annotation, Apex classes, methods, interfaces, and properties defined in an unlocked package aren’t accessible to the other packages
with which they share a namespace. Apex that is declared global is always available across all namespaces, and needs no annotation.

Considerations for Apex Accessibility Across Packages

**•** A Lightning component outside the package can access a public Apex method installed from a no-namespace unlocked package.
The component can be installed from another package or created in the org. For accessing Apex methods, a no-namespace unlocked
package is treated the same as an unmanaged package.

**•** You can't use the `@namespaceAccessible` annotation for an `@AuraEnabled` Apex method.

**•** You can add or remove the `@namespaceAccessible` annotation at any time, even on managed and released Apex code.
Make sure that you don’t have dependent packages relying on the functionality of the annotation before adding or removing it.


### Unlocked Packages Share Release Notes and Post-Install Instructions

**•** When adding or removing `@namespaceAccessible` Apex from a package, consider the impact to users with installed versions
of other packages that reference this package’s annotation. Before pushing a package upgrade, ensure that no user is running a
package version that would fail to fully compile when the upgrade is pushed.

This example shows an Apex class marked with the `@namespaceAccessible` annotation. The class is accessible to other packages
within the same namespace. The first constructor is also visible within the namespace, but the second constructor isn’t.

```
   // A namespace-visible Apex class

   @namespaceAccessible

   public class MyClass {

      private Boolean bypassFLS;

      // A namespace-visible constructor that only allows secure use

      @namespaceAccessible

      public MyClass() {

        bypassFLS = false;

      }

      // A package private constructor that allows use in trusted contexts,

      // but only internal to the package

      public MyClass (Boolean bypassFLS) {

        this.bypassFLS = bypassFLS;

      }

      @namespaceAccessible

      protected Boolean getBypassFLS() {

        return bypassFLS;

      }

   }

### Share Release Notes and Post-Install Instructions

```

Share details about what’s new and changed in a released unlocked package with your users.

Share details about what’s new and changed in an unlocked package with your users. You can specify a release notes URL to display on
the package detail page in the user’s org. And you can share instructions about using your package by specifying a post install URL. The
release notes and post install URLs display on the Installed Packages page in Setup, after a successful package installation. For users who
install packages using an installation URL, the package installer page displays a link to release notes. And users are redirected to your
post install URL following a successful package installation or upgrade.

Specify the `postInstallUrl` and `releaseNotesUrl` attributes in the `packageDirectories` section for the package.

```
     "packageDirectories": [

       {

         "path": "expenser-schema",

         "default": true,

         "package": "Expense Schema",

         "versionName": ""ver 0.3.2"",

         "versionNumber": "0.3.2.NEXT",

         "postInstallUrl": "https://expenser.com/post-install-instructions.html",

         "releaseNotesUrl": "https://expenser.com/winter-2020-release-notes.html"

        },

        ],

        {

         "namespace": "",

         "sfdcLoginUrl": "https://login.salesforce.com",

```


### Unlocked Packages Specify Unpackaged Metadata or Apex Access for Apex

Tests (Unlocked Packages)

```
         "sourceApiVersion": "47.0",

         "packageAliases": {

           "Expenser Schema": "0HoB00000004CzHKAU",

           "Expenser Schema@0.1.0-1": "04tB0000000719qIAA"

       }

   }

```

You can also use the `--post-install-url` and the `--release-notes-url` Salesforce CLI parameters with the `sf`
`package version create` command. The CLI parameters override the URLs specified in the `sfdx-project.json` file.

### Specify Unpackaged Metadata or Apex Access for Apex Tests (Unlocked

Packages)

Specify Unpackaged Metadata for Package Version Creation Tests

Specify the path to the unpackaged metadata in your `sfdx-project.json` file.

In this example, metadata in the `my-unpackaged-directory` is available for test runs during the package version creation of
the TV_unl package.

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

```


### Unlocked Packages Best Practices for Unlocked Packages

```
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

[Note: To assign user licenses, use the runAs Method. User licenses can't be assigned in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_testing_tools_runas.htm) `sfdx-project.json` file.

### Best Practices for Unlocked Packages

We suggest that you follow these best practices when working with unlocked packages.

**•** We recommend that you work with only one Dev Hub, and enable Dev Hub in a production org.

**•** The Dev Hub org against which you run the `sf package create` command becomes the owner of the package. If the Dev
Hub org associated with a package expires or is deleted, its packages no longer work.

**•** Use care in deciding how to utilize namespaces. For most customers, we recommend working with no namespace or a single
namespace to avoid unnecessary complexity in managing components. If you’re test-driving unlocked packages, use a test namespace.

Use real namespaces only when you’re ready to embark on a development path headed for release in a production org.

Note: You can’t install a no-namespace, unlocked package into any org with a namespace (for example, a scratch org with
a namespace).

**•** Include the `--tag` option when you use the `sf package version create` and `sf package version update`
commands. This option helps you keep your version control system tags in sync with specific package versions.

**•** Create user-friendly aliases for packaging IDs, and include those aliases in your Salesforce DX project file and when running CLI
packaging commands. See: Package IDs and Aliases for Unlocked Packages.

### Package IDs and Aliases for Unlocked Packages

During the package lifecycle, packages and package versions are identified by an ID or package alias. When you create a package or
package version, Salesforce CLI creates a package alias based on the package name, and stores that name in the `sfdx-project.json`
file. When you run CLI commands or write scripts to automate packaging workflows, it’s often easier to reference the package alias,
instead of the package ID or package version ID.

Package aliases are stored in the `sfdx-project.json` file as name-value pairs, in which the name is the alias and the value is the
ID. You can modify package aliases for existing packages and package versions in the project file.

At the command line, you also see IDs for things like package members (a component in a package) and requests (like a `sf package`
`version create` request).

Note: As a shortcut, the documentation sometimes refers to an ID by its three-character prefix. For example, a package version
ID always starts with `04t` .

Here are the most commonly used IDs.


### Unlocked Packages Frequently Used Unlocked Packaging Operations

### Frequently Used Unlocked Packaging Operations

[For a complete list of Salesforce CLI packaging commands, see: Salesforce Command Line Reference Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference.htm)


## Unlocked Packages How We Handle Profile Settings in Unlocked Packages How We Handle Profile Settings in Unlocked Packages

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

Repeat this step for any other profile you expect to contain your profile settings. Don’t look for the profile name you created; we
apply profile settings to existing profiles in the subscriber org.

Whenever possible, use package permission sets instead of profile settings. Subscribers who install your package can easily assign your
permission set to their users.


## Unlocked Packages Develop Unlocked Packages

Note: During a push upgrade, some profile settings related to Apex classes and field-level security aren’t automatically assigned
to the System Admin profile. To ensure that user access is set up correctly after a push upgrade, communicate with your customer.
Make sure they review and update their profile settings after a push upgrade.

Retain License Settings in Unlocked Packages

By default, license settings in profiles are removed during package creation. To retain these settings, specify the
`includeProfileUserLicenses` parameter in your `sfdx-project.json` file. In this scenario, the license settings are
retained and applied to the profiles in the subscriber org that are selected during package installation.

```
   "packageDirectories": [

      {

        "package": "PackageA",

        "path": "common",

        "versionName": "ver 0.1",

        "versionNumber": "0.1.0.NEXT",

        "default": false,

        includeProfileUserLicenses: true

      }

   ]

## Develop Unlocked Packages

```

A package is a top-level container that holds important details about the app or package: the package name, description, and associated
namespace.

You supply the package details in the package descriptor section of your `sfdx-project.json` project configuration file.

Create and Update an Unlocked Package
When you’re ready to test or share your package, use the `sf package create` command to create a package.

Create New Versions of an Unlocked Package
A package version is a fixed snapshot of the package contents and related metadata. The package version lets you manage changes
and track what’s different each time you release or deploy a specific set of changes.

Guidance for Package Version Numbering
Use package versions to evolve your managed package, and release subsequent package versions without breaking existing package
users. Every package version is a fixed snapshot of the package contents and related metadata.

Code Coverage for Unlocked Packages
Before you can promote and release an unlocked package, the Apex code must meet a minimum 75% code coverage requirement.
You can install package versions that don't meet code coverage requirements only in scratch orgs and sandboxes.

Considerations for Promoting Packages with Dependencies
If your company is developing a package that has a package dependency, ask yourself these questions before promoting (releasing)
a new package version.

Release an Unlocked Package
Each new package version is marked as beta when its created. As you develop your package, you may create several package versions
before you create a version that is ready to be released and installed in production orgs.


### Unlocked Packages Create and Update an Unlocked Package

Update an Unlocked Package Version
You can update most properties of a package version from the command line. For example, you can change the package version
name or description. One important exception is that you can’t change the release status.

Hard-Deleted Components in Unlocked Packages
When these components are removed from an unlocked package, they're hard deleted from the target install org during the package
upgrade.

Delete an Unlocked Package or Package Version
Use the `sf package version delete` and `sf package delete` to delete packages and package versions that you
no longer need.

View Package Details
View the details of previously created packages and package versions from the command line.

### Create and Update an Unlocked Package

When you’re ready to test or share your package, use the `sf package create` command to create a package.

If you are using a namespace, specify the package namespace in the `sfdx-project.json` file. To learn more, see Understanding
Namespaces.

To create the package, change to the project directory. The name becomes the package alias, which is automatically added to the project
file. You can choose to designate an active Dev Hub org user to receive email notifications for Apex gacks, and install, upgrade, or uninstall
failures associated with your packages.

```
   sf package create --name "Expenser App" --package-type Unlocked --path \

   "expenser-main" --target-dev-hub my-hub --error-notification-username me@devhub.org

```

The output is similar to this example.

```
   sfdx-project.json has been updated.

   Successfully created a package. 0HoB00000004CzHKAU

   === Ids

   NAME VALUE

   ────────── ──────────────────

   Package Id 0HoB00000004CzHKAU

```

Metadata Limits in Unlocked Packages

Update the Package

To update the name, description, or the user to receive error notifications of an existing package, use this command.

```
   sf package update --package "Expense App" --name "Expense Manager App" \

   --description "New Description" --error-notification-username me2@devhub.org

```


### Unlocked Packages Create New Versions of an Unlocked Package

Note: You can’t change the package namespace or package type after you create the package.

### Create New Versions of an Unlocked Package

A package version is a fixed snapshot of the package contents and related metadata. The package version lets you manage changes and
track what’s different each time you release or deploy a specific set of changes.

Before you create a package version, first verify package details, such as the package name, dependencies, and update the versionNumber
parameter in the `sfdx-project.json` file. Verify that the metadata you want to change or add in the new package version is in
the package’s main directory.

When you create a package version, you have three options regarding how package validations are handled.

**•** (Default) Complete all validations of dependencies, package ancestors, and metadata before the package version is returned.

**•** Perform validations asynchronously.

**•** Skip validation on the package version.

Create an Unlocked Package Version (Default Option)

Create the package version with this command. Specify the package alias or ID (0Ho). You can also include a scratch definition file that
contains a list of features and setting that the metadata of the package version depends on.

```
   sf package version create --package "Expenser App" --installation-key “HIF83kS8kS7C” \

   --definitionfile config/project-scratch-def.json --code-coverage --wait 10

```

Note: When creating a package version, specify a `--wait` time to run the command. If the package version is created within
that time, the `sfdx-project.json` file is automatically updated with the package version information. If not, you must
manually edit the project file.

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


Unlocked Packages Create New Versions of an Unlocked Package

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


Unlocked Packages Create New Versions of an Unlocked Package

Use Keyword NEXT to Ensure Package Version Numbers Are Unique

To ensure your version number is unique, use the keyword `NEXT` when you set the version number in your `sfdx-project.json`
file.

For example, `"versionNumber": "1.2.0.NEXT"` .

If you don’t use `NEXT`, and you also forget to update the version number in your `sfdx-project.json` file, the new package
version uses the same number as the previous package version. Although we don’t enforce uniqueness on package version numbers,
every package version is assigned a unique subscriber package version ID (starts with 04t).

How Many Package Versions Can I Create Per Day?

Run this command to see how many package versions you can create per day and how many you have remaining.

```
   sf limits api display

```

Look for the `Package2VersionCreates` entry.

```
   NAME REMAINING MAXIMUM

   ───────────────────────────────────── ───────── ─────────

   Package2VersionCreates 23 50

#### Simplify Unlocked Package Development by Creating and Specifying an Org Shape
```

If your package’s metadata depends on a complex set of features, settings, or licenses, it can be difficult to declaratively specify these
dependencies in a scratch org definition file. Instead, create an org shape of your production org, or another development org, and
specify that source org’s ID in your scratch org definition file. During package creation, we mimic the source org’s environment when
we build and validate your package’s metadata.

Use Branches in Unlocked Packaging
Development teams who use branches in their source control system (SCS), often build package versions based on the metadata
in a particular branch of code.

Target a Specific Release for Your Unlocked Packages During Salesforce Release Transitions
During major Salesforce release transitions, you can specify `preview` or `previous` when creating a package version. Specifying
the release version for a package allows you to test upcoming features, run regression tests, and support customers regardless of
which Salesforce release their org is on. Previously, you could only create package versions that matched the Salesforce release your
Dev Hub org was on.

#### Simplify Unlocked Package Development by Creating and Specifying an Org Shape

If your package’s metadata depends on a complex set of features, settings, or licenses, it can be difficult to declaratively specify these
dependencies in a scratch org definition file. Instead, create an org shape of your production org, or another development org, and
specify that source org’s ID in your scratch org definition file. During package creation, we mimic the source org’s environment when
we build and validate your package’s metadata.

[Before using this feature, get familiar with how Org Shape for Scratch Orgs works.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_shape_intro.htm)

[Then enable the scratch org setting in your source org, generate the org shape, and edit your scratch org definition file to include the](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_shape_enable_org_shape.htm)
org name and 15-character source org ID.

```
   {

     "orgName": "Acme",

```


Unlocked Packages Create New Versions of an Unlocked Package

```
     "sourceOrg": "00DB1230400Ifx5"

   }

#### Use Branches in Unlocked Packaging

```

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

Package Dependencies and Branches

By default, your package can have dependencies on other packages in the same branch. For package dependencies based on packages
in other branches, explicitly set the branch attribute in the `sfdx.project.json` file.


Unlocked Packages Create New Versions of an Unlocked Package

#### Target a Specific Release for Your Unlocked Packages During Salesforce Release

Transitions

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


### Unlocked Packages Guidance for Package Version Numbering

Then when you create your package version, specify the scratch org definition file.

```
   sf package version create --package pkgA --definition-file config/project-scratch-def.json

```

Preview start date is when sandbox instances are upgraded. Preview end date is when all instances are on the GA release.

### Guidance for Package Version Numbering

Use package versions to evolve your managed package, and release subsequent package versions without breaking existing package
users. Every package version is a fixed snapshot of the package contents and related metadata.

While the format for package version number is predetermined, how you determine a version number, and whether you enforce
uniqueness on package version numbers is left to package developers. The format for package version numbers is
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


### Unlocked Packages Code Coverage for Unlocked Packages

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

Considerations for Deleting a Package or Package Version

**•** Deletion is permanent.

**•** Attempts to install a deleted package version will fail.

**•** Before deleting, ensure that the package or package version isn’t referenced as a dependency.

Examples

```
   $ sf package delete -p "Your Package Alias"

   $ sf package delete -p 0Ho...

   $ sf package version delete -p "Your Package Version Alias"

   $ sf package version delete -p 04t...

```


### Unlocked Packages View Package Details

These CLI commands can’t be used with first-generation managed packages or package versions. To delete a first-generation managed
[package, see View Package Details in the](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/isv_viewing_package_details.htm) _First-Generation Managed Packaging Developer Guide_ .

### View Package Details

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

```


## Unlocked Packages Push a Package Upgrade for Unlocked Packages Push a Package Upgrade for Unlocked Packages

Push upgrades enable you to upgrade packages installed in orgs, without asking org admins to install the upgrade themselves. You can
choose which orgs receive a push upgrade, what version the package is upgraded to, and when you want the upgrade to occur. Push
upgrades are particularly helpful if you need to push a change for a hot bug fix.

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


Unlocked Packages Schedule a Push Upgrade Using CLI

In some scenarios you may also need to abort a scheduled push upgrade, or analyze errors that occurred. Let’s review each of these
steps in more detail.

Determine the Orgs to Be Upgraded

There isn't a dedicated `push-upgrade` CLI command for this action, instead let's look at how to use the CLI `data query` command.

Push upgrades must be done in the context of the Dev Hub org that owns the package. To confirm the set of packages owned by a
specific Dev Hub org, run the `[package list](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_package_commands_unified.htm#cli_reference_package_list_unified)` command.

[Then authorize to the Dev Hub org that is the owner of the package are upgrading.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_org_commands_unified.htm#cli_reference_org_login_web_unified)

```
   sf org login web --set-default-dev-hub

```

[If you're preparing to push a package upgrade, we assume your development environment is set up, if you aren't certain, review Set Up](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_pkg_dev_environment.htm)
[Your Development Environment.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_pkg_dev_environment.htm)

Here are three example queries you can use to retrieve a list of subscriber orgs that are eligible for a package upgrade. To review the
[possible fields that can be queried, see PackageSubscriber in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_packagesubscriber.htm) _Object Reference for the Salesforce Platform_ .

Each query requires either a subscriber package ID (starts with 033), or a subscriber package version ID (starts with 04t). To retrieve the
[subsciber package ID, use the package list command and specify the](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_package_commands_unified.htm#cli_reference_package_list_unified) `--verbose` flag. To retrieve the subscriber package version ID,
[use the package version list command.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_package_commands_unified.htm#cli_reference_package_version_list_unified)

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


Unlocked Packages Schedule a Push Upgrade Using CLI

[First, query the Package2Version object to find all versions of your package that are numerically lower than the specified version (2.7).](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_tooling.meta/api_tooling/tooling_api_objects_package2version.htm)

```
   sf data query --target-org admin@packaging.com --use-tooling-api --query "SELECT

   SubscriberPackageVersionId FROM Package2Version WHERE Package2Id = '0HoPACKAGEIDxxxx' AND

    (MajorVersion < 2 OR (MajorVersion = 2 AND MinorVersion < 7))"

```

If you copy and paste this query, update the target org, the Package ID (starts with 0Ho), and the major and minor version before running
the command. The target org is the Dev Hub org that owns the package. Specify either the username or alias for the Dev Hub org.

Note the `SubscriberPackageVersionId` values (starts with 04t) returned by this query.

[Next, query the PackageSubscriber object using the subscriber package version IDs (starts with 04t) from the previous step.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_packagesubscriber.htm)

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
[Salesforce CLI Command Reference.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_package_commands_unified.htm#cli_reference_package_push-upgrade_schedule_unified)

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


## Unlocked Packages Install an Unlocked Package

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
`query` [command. Use this example query to retrieve error messages stored in the PackagePushError object.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_packagepusherror.htm)

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


### Unlocked Packages Install Packages with the CLI

Install Unlocked Packages from a URL
Install unlocked packages from the CLI or from a browser, similar to how you install managed packages.

Upgrade a Version of an Unlocked Package
A package upgrade occurs when you install a new package version into an org that has a previous version of that package installed.

Sample Script for Installing Unlocked Packages with Dependencies
Use this sample script as a basis to create your own script to install packages with dependencies. This script contains a query that
finds dependent packages and installs them in the correct dependency order.

### Install Packages with the CLI

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


### Unlocked Packages Install Unlocked Packages from a URL

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

_[Salesforce CLI Command Reference](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_package_commands_unified.htm#cli_reference_package_install_unified)_ package install

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


### Unlocked Packages Sample Script for Installing Unlocked Packages with

Dependencies

To upgrade a package, use the package install CLI command

```
   sf package install --package 04t... --target-org me@example.com

```

[For more examples and details about this command, see package install in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_package_commands_unified.htm#cli_reference_package_install_unified) _Salesforce CLI Command Reference_ .

When you perform a package upgrade, here’s what to expect for metadata changes.

When you upgrade to a new unlocked package version, you choose whether to require successful compilation of all Apex in the org
and package ( `--apex-compile all` ), or only the Apex in the package ( `--apex-compile package` ).

**•** Metadata introduced in the new version is installed as part of the upgrade.

**•** If an upgraded component has the same API name as a component already in the target org, the component is overwritten with
the changes.

**•** If a component in the upgrade was deleted from the target org, the component is re-created during the upgrade.

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

[Note: For package installs into production orgs, or any org that has Apex Compile on Deploy enabled, the platform compiles all](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_deploying.htm)
Apex in the org after the package install or upgrade operation completes. This approach assures that package installs and upgrades
don’t impact the performance of an org, and is done even if `--apex-compile package` is specified.

### Sample Script for Installing Unlocked Packages with Dependencies

Use this sample script as a basis to create your own script to install packages with dependencies. This script contains a query that finds
dependent packages and installs them in the correct dependency order.


Unlocked Packages Sample Script for Installing Unlocked Packages with
Dependencies

Sample Script

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

   # Parse the json string using python to test whether the result json contains a list of

   ids or not.

   DEPENDENCIES=`echo $RESULT_JSON | python -c 'import sys, json; print

   json.load(sys.stdin)["result"]["records"][0]["Dependencies"]'`

   # If the parsed dependencies is None, the package has no dependencies. Otherwise, parse

   the result into a list of ids.

   # Then loop through the ids to install each of the dependent packages.

```


Unlocked Packages Sample Script for Installing Unlocked Packages with
Dependencies

```
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

   # After processing the dependencies, proceed to install the specified package.

   echo "Installing package: "$PACKAGE

   sf package install --package $PACKAGE -u $USER_NAME -w $WAIT_TIME --publish-wait 10

   exit 0;

```


## Unlocked Packages Migrate Deprecated Metadata from Unlocked Packages Migrate Deprecated Metadata from Unlocked Packages

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

## Uninstall an Unlocked Package

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


## Unlocked Packages Transfer an Unlocked Package to a Different Dev Hub

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


Unlocked Packages Transfer an Unlocked Package to a Different Dev Hub

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

```


### Unlocked Packages Take Ownership of an Unlocked Package Transferred from

a Different Dev Hub

```
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

**•** Deleted package versions. Package versions that were deleted prior to the transfer are no longer recoverable or visible through
Salesforce CLI commands.

### Take Ownership of an Unlocked Package Transferred from a Different Dev Hub

You can take ownership of an unlocked package that is transferred from another Dev Hug org.

### Take Ownership of an Unlocked Package Transferred from a Different Dev

Hub

You can take ownership of an unlocked package that is transferred from another Dev Hug org.

To initiate a package transfer from your Dev Hub org, see Transfer an Unlocked Package to a Different Dev Hub.


Unlocked Packages Take Ownership of an Unlocked Package Transferred from
a Different Dev Hub

Note: For security reasons, package transfers between a Dev Hub located in Government Cloud and a Dev Hub located outside
Government Cloud aren’t permitted.

Receive a Package Transfer

[Link the namespace of the package you’re receiving to your Dev Hub org. See Link a Namespace to a Dev Hub Org in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_reg_namespace.htm) _Salesforce DX_
_Developer Guide_ . If the package isn’t associated with a namespace, skip this step.

After the Package Transfer Is Complete

After the package transfer is complete, you’ll be notified by Salesforce Customer Support.

To verify that the transferred package is associated with your Dev Hub, run `sf package list` .

Impact of Package Transfers on Package IDs

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


Unlocked Packages Take Ownership of an Unlocked Package Transferred from
a Different Dev Hub

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

**2.** [Install the Salesforce CLI, if you haven’t already.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_setup.meta/sfdx_setup/sfdx_setup_install_cli.htm)

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
[If you don't have it installed, see Install Salesforce CLI.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_setup.meta/sfdx_setup/sfdx_setup_install_cli.htm#sfdx_setup_install_cli)

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

_[Salesforce CLI Setup Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_setup.meta/sfdx_setup)_

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

_[Salesforce CLI Command Reference](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_cli_reference.meta/sfdx_cli_reference)_

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
[connected app. See Create a Connected App in Your Org.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_auth_connected_app.htm)


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

**–** [If you're using a custom connected app rather than the default Salesforce CLI one, check that the settings are correct. See Create](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_auth_connected_app.htm)
[a Connected App in Your Org.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_auth_connected_app.htm)


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
[CLI connected app. See Create a Connected App in Your Org. In particular, on the main page where you manage the connected](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_auth_connected_app.htm)
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

[Authorize an Org Using a Browser](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_auth_web_flow.htm)

[Authorize an Org Using the JWT Flow](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_auth_jwt_flow.htm)

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

