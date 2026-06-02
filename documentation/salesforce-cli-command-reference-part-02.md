(https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_classes_annotation_isTest.htm). Each class and
trigger in the deployment package must be covered by the executed tests for a minimum of 75% code coverage. This coverage is
computed for each class and triggers individually and is different than the overall coverage percentage.

If you don’t specify a test level, the default behavior depends on the contents of your deployment package and target org. For more
information, see "Running Tests in a Deployment"
(https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_deploy_running_tests.htm) in the "Metadata
API Developer Guide".

Type: option

Permissible values are: NoTestRun, RunSpecifiedTests, RunLocalTests, RunAllTestsInOrg, RunRelevantTests

**`-r`** **|** **`--no-prompt`**
Optional

Don't prompt for delete confirmation.

Type: boolean

**`-m`** **|** **`--metadata METADATA`**
Optional

Metadata components to delete.

If you specify this flag, don’t specify --source-dir.

Type: option

**`-p`** **|** **`--source-dir SOURCE-DIR`**
Optional

Source file paths to delete.


Salesforce CLI Command Reference project Commands

The supplied paths can be a single file (in which case the operation is applied to only one file) or a folder (in which case the operation
is applied to all metadata types in the directory and its sub-directories).

If you specify this flag, don’t specify --metadata.

Type: option

**`-t`** **|** **`--track-source`**
Optional

If the delete succeeds, update the source tracking information.

Type: boolean

**`-f`** **|** **`--force-overwrite`**
Optional

Ignore conflict warnings and overwrite changes to the org.

Type: boolean

```
   --verbose
```

Optional

Verbose output of the delete result.

Type: boolean

Aliases for **`project delete source`**

```
   force:source:delete

#### **`project delete tracking`**

```

Delete all local source tracking information.

#### Description for project delete tracking

WARNING: This command deletes or overwrites all existing source tracking files. Use with extreme caution.

Deletes all local source tracking information. When you next run 'project deploy preview', Salesforce CLI displays all local and remote
files as changed, and any files with the same name are listed as conflicts.

#### Examples for project delete tracking

Delete local source tracking for the org with alias "my-scratch":

```
   $ sf project delete tracking --target-org my-scratch

```

Flags

```
   --json
```

Optional

Format output as json.

Type: boolean


Salesforce CLI Command Reference project Commands

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

**`-o`** **|** **`--target-org TARGET-ORG`**
Required

Username or alias of the target org. Not required if the `target-org` configuration variable is already set.

Type: option

**`-p`** **|** **`--no-prompt`**
Optional

Don't prompt for source tracking override confirmation.

Type: boolean

Aliases for **`project delete tracking`**

```
   force:source:tracking:clear

#### **`project deploy cancel`**

```

Cancel a deploy operation.

#### Description for project deploy cancel

Use this command to cancel a deploy operation that hasn't yet completed in the org. Deploy operations include standard deploys, quick
deploys, deploy validations, and deploy cancellations.

Run this command by either passing it a job ID or specifying the --use-most-recent flag to use the job ID of the most recent deploy
operation.

#### Examples for project deploy cancel

Cancel a deploy operation using a job ID:

```
   sf project deploy cancel --job-id 0Af0x000017yLUFCA2

```

Cancel the most recent deploy operation:

```
   sf project deploy cancel --use-most-recent

```

Flags

```
   --json
```

Optional


Salesforce CLI Command Reference project Commands

Format output as json.

Type: boolean

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option

**`-o`** **|** **`--target-org TARGET-ORG`**
Optional

Username or alias of the target org.

Type: option

```
   --async
```

Optional

Run the command asynchronously.

The command immediately returns the control of the terminal to you. This way, you can continue to use the CLI. To resume watching
the cancellation, run "sf project deploy resume". To check the status of the cancellation, run "sf project deploy report".

Type: boolean

**`-i`** **|** **`--job-id JOB-ID`**
Optional

Job ID of the deploy operation you want to cancel.

These commands return a job ID if they time out or you specified the --async flag:

      - sf project deploy start

      - sf project deploy validate

      - sf project deploy quick

      - sf project deploy cancel

The job ID is valid for 10 days from when you started the deploy operation.

Type: option

**`-r`** **|** **`--use-most-recent`**
Optional

Use the job ID of the most recent deploy operation.

For performance reasons, this flag uses job IDs for deploy operations that started only in the past 3 days or less. If your most recent
deploy operations was more than 3 days ago, this flag won't find a job ID.

Type: boolean

**`-w`** **|** **`--wait WAIT`**
Optional

Number of minutes to wait for the command to complete and display results.

If the command continues to run after the wait period, the CLI returns control of the terminal window to you. To resume watching
the cancellation, run "sf project deploy resume". To check the status of the cancellation, run "sf project deploy report".

Type: option


Salesforce CLI Command Reference project Commands

Aliases for **`project deploy cancel`**

```
   deploy:metadata:cancel

#### project deploy pipeline quick (Beta)

```

Quickly deploy a validated deployment to an org.

Note: This feature is a Beta Service. Customers may opt to try such Beta Service in its sole discretion. Any use of the Beta Service
is subject to the applicable Beta Services Terms provided at Agreements and Terms
[(https://www.salesforce.com/company/legal/agreements/).](https://www.salesforce.com/company/legal/agreements/)

#### Description for project deploy pipeline quick

The first time you run any "project deploy pipeline" command, be sure to authorize the org in which DevOps Center is installed. The
easiest way to authorize an org is with the "org login web" command.

Before you run this command, create a validated deployment with the "project deploy pipeline validate" command, which returns a job
ID. Validated deployments haven't been deployed to the org yet; you deploy them with this command. Either pass the job ID to this
command or use the --use-most-recent flag to use the job ID of the most recently validated deployment. For the quick deploy to succeed,
the associated validated deployment must also have succeeded.

Executing this quick deploy command takes less time than a standard deploy because it skips running Apex tests. These tests were
previously run as part of the validation. Validating first and then running a quick deploy is useful if the deployment to your production
org take several hours and you don’t want to risk a failed deploy.

This command doesn't support source-tracking. The source you deploy overwrites the corresponding metadata in your org. This command
doesn’t attempt to merge your source with the versions in your org.

#### Examples for project deploy pipeline quick

Run a quick deploy using your default Devops Center org and a job ID:

```
   sf project deploy pipeline quick --job-id 0Af0x000017yLUFCA2

```

Asynchronously run a quick deploy of the most recently validated deployment using an org with alias "my-prod-org":

```
   sf project deploy pipeline quick --async --use-most-recent --devops-center-username

   my-prod-org

```

Flags

```
   --json
```

Optional

Format output as json.

Type: boolean

```
   --async
```

Optional

Run the command asynchronously.


Salesforce CLI Command Reference project Commands

The command immediately returns the job ID and control of the terminal to you. This way, you can continue to use the CLI. To
resume the deployment, run "sf project deploy pipeline resume". To check the status of the deployment, run "sf project deploy
pipeline report".

Type: boolean

```
   --concise
```

Optional

Show concise output of the command result.

Type: boolean

```
   --verbose
```

Optional

Show verbose output of the command result.

Type: boolean

**`-w`** **|** **`--wait WAIT`**
Optional

Number of minutes to wait for command to complete and display results.

If the command continues to run after the wait period, the CLI returns control of the terminal window to you and returns the job ID.
To check the status of the operation, run "sf project deploy pipeline report".

Type: option

Default value: 33 minutes

**`-c`** **|** **`--devops-center-username DEVOPS-CENTER-USERNAME`**
Required

Username or alias of the DevOps Center org.

Type: option

**`-i`** **|** **`--job-id JOB-ID`**
Optional

Job ID of the validated deployment to quick deploy.

The job ID is valid for 10 days from when you started the validation.

Type: option

**`-r`** **|** **`--use-most-recent`**
Optional

Use the job ID of the most recently validated deployment.

For performance reasons, this flag uses only job IDs that were validated in the past 3 days or less. If your most recent deployment
validation was more than 3 days ago, this flag won't find the job ID.

Type: boolean

#### project deploy pipeline report (Beta)

Check the status of a pipeline deploy operation.

Note: This feature is a Beta Service. Customers may opt to try such Beta Service in its sole discretion. Any use of the Beta Service
is subject to the applicable Beta Services Terms provided at Agreements and Terms
[(https://www.salesforce.com/company/legal/agreements/).](https://www.salesforce.com/company/legal/agreements/)


Salesforce CLI Command Reference project Commands

Description for **`project deploy pipeline report`**

The first time you run any "project deploy pipeline" command, be sure to authorize the org in which DevOps Center is installed. The
easiest way to authorize an org is with the "org login web" command.

Run this command by either indicating a job ID or specifying the —use-most-recent flag to use the job ID of the most recent deploy
operation.

Examples for **`project deploy pipeline report`**

Check the status using a job ID:

```
   sf project deploy pipeline report --devops-center-username MyStagingSandbox --job-id

   0Af0x000017yLUFCA2

```

Check the status of the most recent deploy operation:

```
   sf project deploy pipeline report --devops-center-username MyStagingSandbox --use-most-recent

```

Flags

```
   --json
```

Optional

Format output as json.

Type: boolean

**`-c`** **|** **`--devops-center-username DEVOPS-CENTER-USERNAME`**
Required

Username or alias of the DevOps Center org.

Type: option

**`-i`** **|** **`--job-id JOB-ID`**
Optional

Job ID of the pipeline deployment to check the status of.

The job ID is valid for 10 days from when you started the deploy operation.

Type: option

**`-r`** **|** **`--use-most-recent`**
Optional

Use the job ID of the most recent deploy operation.

For performance reasons, this flag uses job IDs for deploy operations that started in the past 3 days or fewer. If your most recent
operation was longer than 3 days ago, this flag won't find the job ID.

Type: boolean

#### project deploy pipeline resume (Beta)

Resume watching a pipeline deploy operation.


Salesforce CLI Command Reference project Commands

Note: This feature is a Beta Service. Customers may opt to try such Beta Service in its sole discretion. Any use of the Beta Service
is subject to the applicable Beta Services Terms provided at Agreements and Terms
[(https://www.salesforce.com/company/legal/agreements/).](https://www.salesforce.com/company/legal/agreements/)

Description for **`project deploy pipeline resume`**

The first time you run any "project deploy pipeline" command, be sure to authorize the org in which DevOps Center is installed. The
easiest way to authorize an org is with the "org login web" command.

Use this command to resume watching a pipeline deploy operation if the original command times out or you specified the --async flag.

Run this command by either indicating a job ID or specifying the --use-most-recent flag to use the job ID of the most recent deploy
operation.

Examples for **`project deploy pipeline resume`**

Resume watching a deploy operation using a job ID:

```
   sf project deploy pipeline resume --job-id 0Af0x000017yLUFCA2

```

Resume watching the most recent deploy operation:

```
   sf project deploy pipeline resume --use-most-recent

```

Flags

```
   --json
```

Optional

Format output as json.

Type: boolean

**`-c`** **|** **`--devops-center-username DEVOPS-CENTER-USERNAME`**
Required

Username or alias of the DevOps Center org.

Type: option

**`-i`** **|** **`--job-id JOB-ID`**
Optional

Job ID of the pipeline deploy operation you want to resume.

These commands return a job ID if they time out or you specified the --async flag:

      - sf project deploy pipeline start

      - sf project deploy pipeline validate

      - sf project deploy pipeline quick

The job ID is valid for 10 days from when you started the deploy operation.

Type: option

**`-r`** **|** **`--use-most-recent`**
Optional

Use the job ID of the most recent deploy operation.


Salesforce CLI Command Reference project Commands

For performance reasons, this flag uses job IDs for operations that started in the past 3 days or fewer. If your most recent operation
was longer than 3 days ago, this flag won't find a job ID.

Type: boolean

```
   --concise
```

Optional

Show concise output of the command result.

Type: boolean

```
   --verbose
```

Optional

Show verbose output of the command result.

Type: boolean

**`-w`** **|** **`--wait WAIT`**
Optional

Number of minutes to wait for command to complete and display results.

If the command continues to run after the wait period, the CLI returns control of the terminal window to you and returns the job ID.
To check the status of the operation, run "sf project deploy pipeline report".

Type: option

Default value: 33 minutes

#### project deploy pipeline start (Beta)

Deploy changes from a branch to the pipeline stage’s org.

Note: This feature is a Beta Service. Customers may opt to try such Beta Service in its sole discretion. Any use of the Beta Service
is subject to the applicable Beta Services Terms provided at Agreements and Terms
[(https://www.salesforce.com/company/legal/agreements/).](https://www.salesforce.com/company/legal/agreements/)

#### Description for project deploy pipeline start

The first time you run any "project deploy pipeline" command, be sure to authorize the org in which DevOps Center is installed. The
easiest way to authorize an org is with the "org login web" command.

Before you run this command, changes in the pipeline stage's branch must be merged in the source control repository.

#### Examples for project deploy pipeline start

Deploy changes in the Staging branch to the Staging environment (sandbox), if the previous stage is the bundling stage:

```
   sf project deploy pipeline start --devops-center-project-name “Recruiting App” --branch-name

    staging --devops-center-username MyStagingSandbox --bundle-version-name 1.0

```

Deploy all changes in the main branch to the release environment:

```
   sf project deploy pipeline start --devops-center-project-name “Recruiting App” --branch-name

    main --devops-center-username MyReleaseOrg --deploy-all

```


Salesforce CLI Command Reference project Commands

Flags

```
   --json
```

Optional

Format output as json.

Type: boolean

**`-b`** **|** **`--branch-name BRANCH-NAME`**
Required

Name of the branch in the source control repository that corresponds to the pipeline stage that you want to deploy the changes to.

Type: option

**`-v`** **|** **`--bundle-version-name BUNDLE-VERSION-NAME`**
Optional

Version name of the bundle.

You must indicate the bundle version if deploying to the environment that corresponds to the first stage after the bundling stage.

Type: option

**`-a`** **|** **`--deploy-all`**
Optional

Deploy all metadata in the branch to the stage's org.

If you don’t specify this flag, only changes in the stage’s branch are deployed.

Type: boolean

**`-p`** **|** **`--devops-center-project-name DEVOPS-CENTER-PROJECT-NAME`**
Required

Name of the DevOps Center project.

Type: option

**`-c`** **|** **`--devops-center-username DEVOPS-CENTER-USERNAME`**
Required

Username or alias of the DevOps Center org.

Type: option

**`-t`** **|** **`--tests TESTS`**
Optional

Apex tests to run when --test-level is RunSpecifiedTests.

Separate multiple test names with commas. Enclose the entire flag value in double quotes if a test name contains spaces.

Type: option

**`-l`** **|** **`--test-level TEST-LEVEL`**
Optional

Deployment Apex testing level.

Valid values are:

      - NoTestRun — No tests are run. This test level applies only to deployments to development environments, such as sandbox,
Developer Edition, or trial orgs. This test level is the default for development environments.


Salesforce CLI Command Reference project Commands

      - RunSpecifiedTests — Runs only the tests that you specify with the --tests flag. Code coverage requirements differ from the default
coverage requirements when using this test level. Executed tests must comprise a minimum of 75% code coverage for each class
and trigger in the deployment package. This coverage is computed for each class and trigger individually and is different than the
overall coverage percentage.

      - RunLocalTests — All tests in your org are run, except the ones that originate from installed managed and unlocked packages. This
test level is the default for production deployments that include Apex classes or triggers.

      - RunAllTestsInOrg — All tests in your org are run, including tests of managed packages.

If you don’t specify a test level, the default behavior depends on the contents of your deployment package. For more information,
see the section "Running Tests in a Deployment" in the "Metadata API Developer Guide".
(https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_deploy_running_tests.htm)

Type: option

Permissible values are: NoTestRun, RunSpecifiedTests, RunLocalTests, RunAllTestsInOrg

```
   --async
```

Optional

Run the command asynchronously.

The command immediately returns the job ID and control of the terminal to you. This way, you can continue to use the CLI. To
resume the deployment, run "sf project deploy pipeline resume". To check the status of the deployment, run "sf project deploy
pipeline report".

Type: boolean

**`-w`** **|** **`--wait WAIT`**
Optional

Number of minutes to wait for command to complete and display results.

If the command continues to run after the wait period, the CLI returns control of the terminal window to you and returns the job ID.
To check the status of the operation, run "sf project deploy pipeline report".

Type: option

Default value: 33 minutes

```
   --verbose
```

Optional

Show verbose output of the command result.

Type: boolean

```
   --concise
```

Optional

Show concise output of the command result.

Type: boolean

#### project deploy pipeline validate (Beta)

Perform a validate-only deployment from a branch to the pipeline stage’s org.

Note: This feature is a Beta Service. Customers may opt to try such Beta Service in its sole discretion. Any use of the Beta Service
is subject to the applicable Beta Services Terms provided at Agreements and Terms
[(https://www.salesforce.com/company/legal/agreements/).](https://www.salesforce.com/company/legal/agreements/)


Salesforce CLI Command Reference project Commands

Description for **`project deploy pipeline validate`**

The first time you run any "project deploy pipeline" command, be sure to authorize the org in which DevOps Center is installed. The
easiest way to authorize an org is with the "org login web" command.

A validation runs Apex tests to verify whether a deployment will succeed without actually deploying the metadata to your environment,
so you can then quickly deploy the changes later without re-running the tests.

Examples for **`project deploy pipeline validate`**

Perform a validate-only deployment from the Staging branch to the Staging environment (sandbox):

```
   sf project deploy pipeline validate --devops-center-project-name “Recruiting App”

   --branch-name staging --devops-center-username MyStagingSandbox

```

Perform a validate-only deployment of all changes from the main branch to the release environment:

```
   sf project deploy pipeline validate --devops-center-project-name “Recruiting App”

   --branch-name main --devops-center-username MyReleaseOrg --deploy-all

```

Flags

```
   --json
```

Optional

Format output as json.

Type: boolean

**`-b`** **|** **`--branch-name BRANCH-NAME`**
Required

Name of the branch in the source control repository that corresponds to the pipeline stage that you want to deploy the changes to.

Type: option

**`-v`** **|** **`--bundle-version-name BUNDLE-VERSION-NAME`**
Optional

Version name of the bundle.

You must indicate the bundle version if deploying to the environment that corresponds to the first stage after the bundling stage.

Type: option

**`-a`** **|** **`--deploy-all`**
Optional

Deploy all metadata in the branch to the stage's org.

If you don’t specify this flag, only changes in the stage’s branch are deployed.

Type: boolean

**`-p`** **|** **`--devops-center-project-name DEVOPS-CENTER-PROJECT-NAME`**
Required

Name of the DevOps Center project.

Type: option

**`-c`** **|** **`--devops-center-username DEVOPS-CENTER-USERNAME`**
Required


Salesforce CLI Command Reference project Commands

Username or alias of the DevOps Center org.

Type: option

**`-t`** **|** **`--tests TESTS`**
Optional

Apex tests to run when --test-level is RunSpecifiedTests.

Separate multiple test names with commas. Enclose the entire flag value in double quotes if a test name contains spaces.

Type: option

**`-l`** **|** **`--test-level TEST-LEVEL`**
Optional

Deployment Apex testing level.

Valid values are:

      - NoTestRun — No tests are run. This test level applies only to deployments to development environments, such as sandbox,
Developer Edition, or trial orgs. This test level is the default for development environments.

      - RunSpecifiedTests — Runs only the tests that you specify with the --tests flag. Code coverage requirements differ from the default
coverage requirements when using this test level. Executed tests must comprise a minimum of 75% code coverage for each class
and trigger in the deployment package. This coverage is computed for each class and trigger individually and is different than the
overall coverage percentage.

      - RunLocalTests — All tests in your org are run, except the ones that originate from installed managed and unlocked packages. This
test level is the default for production deployments that include Apex classes or triggers.

      - RunAllTestsInOrg — All tests in your org are run, including tests of managed packages.

If you don’t specify a test level, the default behavior depends on the contents of your deployment package. For more information,
see the section "Running Tests in a Deployment" in the "Metadata API Developer Guide".
(https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_deploy_running_tests.htm)

Type: option

Permissible values are: NoTestRun, RunSpecifiedTests, RunLocalTests, RunAllTestsInOrg

```
   --async
```

Optional

Run the command asynchronously.

The command immediately returns the job ID and control of the terminal to you. This way, you can continue to use the CLI. To
resume the deployment, run "sf project deploy pipeline resume". To check the status of the deployment, run "sf project deploy
pipeline report".

Type: boolean

**`-w`** **|** **`--wait WAIT`**
Optional

Number of minutes to wait for command to complete and display results.

If the command continues to run after the wait period, the CLI returns control of the terminal window to you and returns the job ID.
To check the status of the operation, run "sf project deploy pipeline report".

Type: option

Default value: 33 minutes

```
   --verbose
```

Optional


Salesforce CLI Command Reference project Commands

Show verbose output of the command result.

Type: boolean

```
   --concise
```

Optional

Show concise output of the command result.

Type: boolean

#### **`project deploy preview`**

Preview a deployment to see what will deploy to the org, the potential conflicts, and the ignored files.

#### Description for project deploy preview

You must run this command from within a project.

The command outputs a table that describes what will happen if you run the "sf project deploy start" command. The table lists the
metadata components that will be deployed and deleted. The table also lists the current conflicts between files in your local project and
components in the org. Finally, the table lists the files that won't be deployed because they're included in your .forceignore file.

If your org allows source tracking, then this command displays potential conflicts between the org and your local project. Some orgs,
such as production org, never allow source tracking. Source tracking is enabled by default on scratch and sandbox orgs; you can disable
source tracking when you create the orgs by specifying the --no-track-source flag on the "sf org create scratch|sandbox" commands.

To preview the deployment of multiple metadata components, either set multiple --metadata <name> flags or a single --metadata flag
with multiple names separated by spaces. Enclose names that contain spaces in one set of double quotes. The same syntax applies to
--source-dir.

#### Examples for project deploy preview

NOTE: The commands to preview a deployment and actually deploy it use similar flags. We provide a few preview examples here, but
see the help for "sf project deploy start" for more examples that you can adapt for previewing.

Preview the deployment of source files in a directory, such as force-app, to your default org:

```
   sf project deploy preview --source-dir force-app

```

Preview the deployment of all Apex classes to an org with alias "my-scratch":

```
   sf project deploy preview --metadata ApexClass --target-org my-scratch

```

Preview deployment of a specific Apex class:

```
   sf project deploy preview --metadata ApexClass:MyApexClass

```

Preview deployment of all components listed in a manifest:

```
   sf project deploy preview --manifest path/to/package.xml

```

Flags

```
   --json
```

Optional

Format output as json.


Salesforce CLI Command Reference project Commands

Type: boolean

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option

**`-c`** **|** **`--ignore-conflicts`**
Optional

Don't display conflicts in preview of the deployment.

This flag applies only to orgs that allow source tracking. It has no effect on orgs that don't allow it, such as production orgs.

Type: boolean

**`-x`** **|** **`--manifest MANIFEST`**
Optional

Full file path for manifest (package.xml) of components to preview.

All child components are included. If you specify this flag, don’t specify --metadata or --source-dir.

Type: option

**`-m`** **|** **`--metadata METADATA`**
Optional

Metadata component names to preview.

Type: option

**`-d`** **|** **`--source-dir SOURCE-DIR`**
Optional

Path to the local source files to preview.

The supplied path can be to a single file (in which case the operation is applied to only one file) or to a folder (in which case the
operation is applied to all metadata types in the directory and its subdirectories).

If you specify this flag, don’t specify --metadata or --manifest.

Type: option

**`-o`** **|** **`--target-org TARGET-ORG`**
Required

Username or alias of the target org. Not required if the `target-org` configuration variable is already set.

Type: option

```
   --concise
```

Optional

Show only the changes that will be deployed; omits files that are forceignored.

Type: boolean

Aliases for **`project deploy preview`**

```
   deploy:metadata:preview

```


Salesforce CLI Command Reference project Commands

#### **`project deploy quick`**

Quickly deploy a validated deployment to an org.

#### Description for project deploy quick

Before you run this command, first create a validated deployment with the "sf project deploy validate" command, which returns a job
ID. Validated deployments haven't been deployed to the org yet; you deploy them with this command. Either pass the job ID to this
command or use the --use-most-recent flag to use the job ID of the most recently validated deployment. For the quick deploy to succeed,
the associated validated deployment must also have succeeded.

Executing this quick deploy command takes less time than a standard deploy because it skips running Apex tests. These tests were
previously run as part of the validation. Validating first and then running a quick deploy is useful if the deployment to your production
org take several hours and you don’t want to risk a failed deploy.

This command doesn't support source-tracking. The source you deploy overwrites the corresponding metadata in your org. This command
doesn’t attempt to merge your source with the versions in your org.

Note: Don't use this command on sandboxes; the command is intended to be used on production orgs. By default, sandboxes don't run
tests during a deploy. Use "sf project deploy start" instead.

#### Examples for project deploy quick

Run a quick deploy to your default org using a job ID:

```
   sf project deploy quick --job-id 0Af0x000017yLUFCA2

```

Asynchronously run a quick deploy of the most recently validated deployment to an org with alias "my-prod-org":

```
   sf project deploy quick --async --use-most-recent --target-org my-prod-org

```

Flags

```
   --json
```

Optional

Format output as json.

Type: boolean

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option

```
   --async
```

Optional

Run the command asynchronously.

The command immediately returns the control of the terminal to you. This way, you can continue to use the CLI. To resume watching
the deploy, run "sf project deploy resume". To check the status of the deploy, run "sf project deploy report".

Type: boolean

```
   --concise
```

Optional


Salesforce CLI Command Reference project Commands

Show concise output of the deploy result.

Type: boolean

**`-i`** **|** **`--job-id JOB-ID`**
Optional

Job ID of the deployment you want to quick deploy.

The job ID is valid for 10 days from when you started the validation.

Type: option

**`-o`** **|** **`--target-org TARGET-ORG`**
Optional

Username or alias of the target org.

Type: option

**`-r`** **|** **`--use-most-recent`**
Optional

Use the job ID of the most recently validated deployment.

For performance reasons, this flag uses only job IDs that were validated in the past 3 days or less. If your most recent deployment
validation was more than 3 days ago, this flag won't find a job ID.

Type: boolean

```
   --verbose
```

Optional

Show verbose output of the deploy result.

Type: boolean

**`-w`** **|** **`--wait WAIT`**
Optional

Number of minutes to wait for the command to complete and display results.

If the command continues to run after the wait period, the CLI returns control of the terminal window to you. To resume watching
the deploy, run "sf project deploy resume". To check the status of the deploy, run "sf project deploy report".

Type: option

Default value: 33 minutes

**`-a`** **|** **`--api-version API-VERSION`**
Optional

Target API version for the deploy.

Use this flag to override the default API version with the API version of your package.xml file. The default API version is the latest
version supported by the CLI.

Type: option

Aliases for **`project deploy quick`**

```
   deploy:metadata:quick

```


Salesforce CLI Command Reference project Commands

#### **`project deploy report`**

Check or poll for the status of a deploy operation.

#### Description for project deploy report

Deploy operations include standard deploys, quick deploys, deploy validations, and deploy cancellations.

Run this command by either passing it a job ID or specifying the --use-most-recent flag to use the job ID of the most recent deploy
operation. If you specify the --wait flag, the command polls for the status every second until the timeout of --wait minutes. If you don't
specify the --wait flag, the command simply checks and displays the status of the deploy; the command doesn't poll for the status.

You typically don't specify the --target-org flag because the cached job already references the org to which you deployed. But if you run
this command on a computer different than the one from which you deployed, then you must specify the --target-org and it must point
to the same org.

This command doesn't update source tracking information.

#### Examples for project deploy report

Check the status using a job ID:

```
   sf project deploy report --job-id 0Af0x000017yLUFCA2

```

Check the status of the most recent deploy operation:

```
   sf project deploy report --use-most-recent

```

Poll for the status using a job ID and target org:

```
   sf project deploy report --job-id 0Af0x000017yLUFCA2 --target-org me@my.org --wait 30

```

Flags

```
   --json
```

Optional

Format output as json.

Type: boolean

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option

**`-o`** **|** **`--target-org TARGET-ORG`**
Optional

Username or alias of the target org.

Type: option

**`-i`** **|** **`--job-id JOB-ID`**
Optional

Job ID of the deploy operation you want to check the status of.

These commands return a job ID if they time out or you specified the --async flag:


Salesforce CLI Command Reference project Commands

      - sf project deploy start

      - sf project deploy validate

      - sf project deploy quick

      - sf project deploy cancel

The job ID is valid for 10 days from when you started the deploy operation.

Type: option

**`-r`** **|** **`--use-most-recent`**
Optional

Use the job ID of the most recent deploy operation.

For performance reasons, this flag uses job IDs for deploy operations that started only in the past 3 days or less. If your most recent
operation was more than 3 days ago, this flag won't find a job ID.

Type: boolean

```
   --coverage-formatters COVERAGE-FORMATTERS
```

Optional

Format of the code coverage results.

For multiple formatters, repeat the flag for each formatter.

--coverage-formatters lcov --coverage-formatters clover

Type: option

Permissible values are: clover, cobertura, html-spa, html, json, json-summary, lcovonly, none, teamcity, text, text-summary

```
   --junit
```

Optional

Output JUnit test results.

Type: boolean

```
   --results-dir RESULTS-DIR
```

Optional

Output directory for code coverage and JUnit results; defaults to the deploy ID.

Type: option

**`-w`** **|** **`--wait WAIT`**
Optional

Number of minutes to wait for command to complete and display results.

If the command continues to run after the wait period, the CLI returns control of the terminal window to you and returns the job ID.
To resume the deployment, run "sf project deploy resume". To check the status of the deployment, run "sf project deploy report".

Type: option

Aliases for **`project deploy report`**

```
   deploy:metadata:report

```


Salesforce CLI Command Reference project Commands

#### **`project deploy resume`**

Resume watching a deploy operation and update source tracking when the deploy completes.

#### Description for project deploy resume

Use this command to resume watching a deploy operation if the original command times out or you specified the --async flag. Deploy
operations include standard deploys, quick deploys, deploy validations, and deploy cancellations. This command doesn't resume the
original operation itself, because the operation always continues after you've started it, regardless of whether you're watching it or not.
When the deploy completes, source tracking information is updated as needed.

Run this command by either passing it a job ID or specifying the --use-most-recent flag to use the job ID of the most recent deploy
operation.

#### Examples for project deploy resume

Resume watching a deploy operation using a job ID:

```
   sf project deploy resume --job-id 0Af0x000017yLUFCA2

```

Resume watching the most recent deploy operation:

```
   sf project deploy resume --use-most-recent

```

Flags

```
   --json
```

Optional

Format output as json.

Type: boolean

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option

```
   --concise
```

Optional

Show concise output of the deploy operation result.

Type: boolean

**`-i`** **|** **`--job-id JOB-ID`**
Optional

Job ID of the deploy operation you want to resume.

These commands return a job ID if they time out or you specified the --async flag:

      - sf project deploy start

      - sf project deploy validate

      - sf project deploy quick

      - sf project deploy cancel


Salesforce CLI Command Reference project Commands

The job ID is valid for 10 days from when you started the deploy operation.

Type: option

**`-r`** **|** **`--use-most-recent`**
Optional

Use the job ID of the most recent deploy operation.

For performance reasons, this flag uses job IDs for deploy operations that started only in the past 3 days or less. If your most recent
operation was more than 3 days ago, this flag won't find a job ID.

Type: boolean

```
   --verbose
```

Optional

Show verbose output of the deploy operation result.

Type: boolean

**`-w`** **|** **`--wait WAIT`**
Optional

Number of minutes to wait for the command to complete and display results.

If the command continues to run after the wait period, the CLI returns control of the terminal window to you. To resume watching
the deploy operation, run this command again. To check the status of the deploy operation, run "sf project deploy report".

Type: option

```
   --coverage-formatters COVERAGE-FORMATTERS
```

Optional

Format of the code coverage results.

For multiple formatters, repeat the flag for each formatter.

--coverage-formatters lcov --coverage-formatters clover

Type: option

Permissible values are: clover, cobertura, html-spa, html, json, json-summary, lcovonly, none, teamcity, text, text-summary

```
   --junit
```

Optional

Output JUnit test results.

Type: boolean

```
   --results-dir RESULTS-DIR
```

Optional

Output directory for code coverage and JUnit results; defaults to the deploy ID.

Type: option

Aliases for **`project deploy resume`**

```
   deploy:metadata:resume

```


Salesforce CLI Command Reference project Commands

#### **`project deploy start`**

Deploy metadata to an org from your local project.

#### Description for project deploy start

You must run this command from within a project.

Metadata components are deployed in source format by default. Deploy them in metadata format by specifying the --metadata-dir flag,
which specifies the root directory or ZIP file that contains the metadata formatted files you want to deploy.

If your org allows source tracking, then this command tracks the changes in your source. Some orgs, such as production orgs, never
allow source tracking. Source tracking is enabled by default on scratch and sandbox orgs; you can disable source tracking when you
create the orgs by specifying the --no-track-source flag on the "sf org create scratch|sandbox" commands.

To deploy multiple metadata components, either set multiple --metadata <name> flags or a single --metadata flag with multiple names
separated by spaces. Enclose names that contain spaces in one set of double quotes. The same syntax applies to --source-dir.

#### Examples for project deploy start

Deploy local changes not in the org; uses your default org:

```
   sf project deploy start

```

Deploy all source files in the "force-app" directory to an org with alias "my-scratch"; show only concise output, in other words don't print
a list of all the source that was deployed:

```
   sf project deploy start --source-dir force-app --target-org my-scratch --concise

```

Deploy all the Apex classes and custom objects that are in the "force-app" directory. The list views, layouts, etc, that are associated with
the custom objects are also deployed. Both examples are equivalent:

```
   sf project deploy start --source-dir force-app/main/default/classes

   force-app/main/default/objects

   sf project deploy start --source-dir force-app/main/default/classes --source-dir

   force-app/main/default/objects

```

Deploy all Apex classes that are in all package directories defined in the "sfdx-project.json" file:

```
   sf project deploy start --metadata ApexClass

```

Deploy a specific Apex class; ignore any conflicts between the local project and org (be careful with this flag, because it will overwrite
the Apex class in the org if there are conflicts!):

```
   sf project deploy start --metadata ApexClass:MyApexClass --ignore-conflicts

```

Deploy specific Apex classes that match a pattern; in this example, deploy Apex classes whose names contain the string "MyApex". Also
ignore any deployment warnings (again, be careful with this flag! You typically want to see the warnings):

```
   sf project deploy start --metadata 'ApexClass:MyApex*' --ignore-warnings

```

Deploy a custom object called ExcitingObject that's in the SBQQ namespace:

```
   sf project deploy start --metadata CustomObject:SBQQ__ExcitingObject

```


Salesforce CLI Command Reference project Commands

Deploy all custom objects in the SBQQ namespace by using a wildcard and quotes:

```
   sf project deploy start --metadata 'CustomObject:SBQQ__*'

```

Deploy all custom objects and Apex classes found in all defined package directories (both examples are equivalent):

```
   sf project deploy start --metadata CustomObject ApexClass

   sf project deploy start --metadata CustomObject --metadata ApexClass

```

Deploy all Apex classes and a profile that has a space in its name:

```
   sf project deploy start --metadata ApexClass --metadata "Profile:My Profile"

```

Deploy all components listed in a manifest:

```
   sf project deploy start --manifest path/to/package.xml

```

Run the tests that aren’t in any managed packages as part of a deployment:

```
   sf project deploy start --metadata ApexClass --test-level RunLocalTests

```

Deploy all metadata formatted files in the "MDAPI" directory:

```
   sf project deploy start --metadata-dir MDAPI

```

Deploy all metadata formatted files in the "MDAPI" directory; items listed in the MDAPI/destructiveChangesPre.xml and
MDAPI/destructiveChangesPost.xml manifests are immediately eligible for deletion rather than stored in the Recycle Bin:

```
   sf project deploy start --metadata-dir MDAPI --purge-on-delete

```

Flags

```
   --json
```

Optional

Format output as json.

Type: boolean

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option

**`-a`** **|** **`--api-version API-VERSION`**
Optional

Target API version for the deploy.

Use this flag to override the default API version with the API version of your package.xml file. The default API version is the latest
version supported by the CLI.

Type: option

```
   --async
```

Optional

Run the command asynchronously.


Salesforce CLI Command Reference project Commands

The command immediately returns the job ID and control of the terminal to you. This way, you can continue to use the CLI. To
resume the deployment, run "sf project deploy resume". To check the status of the deployment, run "sf project deploy report".

Type: boolean

```
   --concise
```

Optional

Show concise output of the deploy result.

Type: boolean

```
   --dry-run
```

Optional

Validate deploy and run Apex tests but don’t save to the org.

Type: boolean

**`-c`** **|** **`--ignore-conflicts`**
Optional

Ignore conflicts and deploy local files, even if they overwrite changes in the org.

This flag applies only to orgs that allow source tracking. It has no effect on orgs that don't allow it, such as production orgs.

Type: boolean

**`-r`** **|** **`--ignore-errors`**
Optional

Ignore any errors and don’t roll back deployment.

Never use this flag when deploying to a production org. If you specify it, components without errors are deployed and components
with errors are skipped, and could result in an inconsistent production org.

Type: boolean

**`-g`** **|** **`--ignore-warnings`**
Optional

Ignore warnings and allow a deployment to complete successfully.

If you specify this flag, and a warning occurs, the success status of the deployment is set to true. If you don't specify this flag, and a
warning occurs, then the success status is set to false, and the warning is treated like an error.

This flag is useful in a CI environment and your deployment includes destructive changes; if you try to delete a component that
doesn't exist in the org, you get a warning. In this case, to ensure that the command returns a success value of true, specify this flag.

Type: boolean

**`-x`** **|** **`--manifest MANIFEST`**
Optional

Full file path for manifest (package.xml) of components to deploy.

All child components are included. If you specify this flag, don’t specify --metadata or --source-dir.

Type: option

**`-m`** **|** **`--metadata METADATA`**
Optional

Metadata component names to deploy. Wildcards (`*` ) supported as long as you use quotes, such as `ApexClass:MyClass*`.

Type: option


Salesforce CLI Command Reference project Commands

```
   --metadata-dir METADATA-DIR
```

Optional

Root of directory or zip file of metadata formatted files to deploy.

Type: option

```
   --single-package
```

Optional

Indicates that the metadata zip file points to a directory structure for a single package.

Type: boolean

**`-d`** **|** **`--source-dir SOURCE-DIR`**
Optional

Path to the local source files to deploy.

The supplied path can be to a single file (in which case the operation is applied to only one file) or to a folder (in which case the
operation is applied to all metadata types in the directory and its subdirectories).

If you specify this flag, don’t specify --metadata or --manifest.

Type: option

**`-o`** **|** **`--target-org TARGET-ORG`**
Required

Username or alias of the target org. Not required if the `target-org` configuration variable is already set.

Type: option

**`-t`** **|** **`--tests TESTS`**
Optional

Apex tests to run when --test-level is RunSpecifiedTests.

If a test name contains a space, enclose it in double quotes.

For multiple test names, use one of the following formats:

      - Repeat the flag for multiple test names: --tests Test1 --tests Test2 --tests "Test With Space"

      - Separate the test names with spaces: --tests Test1 Test2 "Test With Space"

Type: option

**`-l`** **|** **`--test-level TEST-LEVEL`**
Optional

Deployment Apex testing level.

Valid values are:

      - NoTestRun — No tests are run. This test level applies only to deployments to development environments, such as sandbox,
Developer Edition, or trial orgs. This test level is the default for development environments.

      - RunSpecifiedTests — Runs only the tests that you specify with the --tests flag. Code coverage requirements differ from the default
coverage requirements when using this test level. Executed tests must comprise a minimum of 75% code coverage for each class
and trigger in the deployment package. This coverage is computed for each class and trigger individually and is different than the
overall coverage percentage.

      - RunLocalTests — All tests in your org are run, except the ones that originate from installed managed and unlocked packages. This
test level is the default for production deployments that include Apex classes or triggers.

      - RunAllTestsInOrg — All tests in your org are run, including tests of managed packages.


Salesforce CLI Command Reference project Commands

      - RunRelevantTests (Beta) — Runs only tests that are relevant to the files being deployed. Salesforce automatically identifies the
relevant tests based on an analysis of the deployment payload and the payload dependencies. For fine-grained control, you can also
annotate test classes so that they always run in certain conditions. See "@IsTest Annotation" in the "Apex Developer Guide"
(https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_classes_annotation_isTest.htm). Each class and
trigger in the deployment package must be covered by the executed tests for a minimum of 75% code coverage. This coverage is
computed for each class and triggers individually and is different than the overall coverage percentage.

If you don’t specify a test level, the default behavior depends on the contents of your deployment package and target org. For more
information, see "Running Tests in a Deployment"
(https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_deploy_running_tests.htm) in the "Metadata
API Developer Guide".

Type: option

Permissible values are: NoTestRun, RunSpecifiedTests, RunLocalTests, RunAllTestsInOrg, RunRelevantTests

```
   --verbose
```

Optional

Show verbose output of the deploy result.

Type: boolean

**`-w`** **|** **`--wait WAIT`**
Optional

Number of minutes to wait for command to complete and display results.

If the command continues to run after the wait period, the CLI returns control of the terminal window to you and returns the job ID.
To resume the deployment, run "sf project deploy resume". To check the status of the deployment, run "sf project deploy report".

Type: option

Default value: 33 minutes

```
   --purge-on-delete
```

Optional

Specify that deleted components in the destructive changes manifest file are immediately eligible for deletion rather than being
stored in the Recycle Bin.

Type: boolean

```
   --pre-destructive-changes PRE-DESTRUCTIVE-CHANGES
```

Optional

File path for a manifest (destructiveChangesPre.xml) of components to delete before the deploy.

Type: option

```
   --post-destructive-changes POST-DESTRUCTIVE-CHANGES
```

Optional

File path for a manifest (destructiveChangesPost.xml) of components to delete after the deploy.

Type: option

```
   --coverage-formatters COVERAGE-FORMATTERS
```

Optional

Format of the code coverage results.

For multiple formatters, repeat the flag for each formatter.

--coverage-formatters lcov --coverage-formatters clover


Salesforce CLI Command Reference project Commands

Type: option

Permissible values are: clover, cobertura, html-spa, html, json, json-summary, lcovonly, none, teamcity, text, text-summary

```
   --junit
```

Optional

Output JUnit test results.

Type: boolean

```
   --results-dir RESULTS-DIR
```

Optional

Output directory for code coverage and JUnit results; defaults to the deploy ID.

Type: option

Aliases for **`project deploy start`**

```
   deploy:metadata

#### **`project deploy validate`**

```

Validate a metadata deployment without actually executing it.

#### Description for project deploy validate

Use this command to verify whether a deployment will succeed without actually deploying the metadata to your org. This command
is similar to "sf project deploy start", except you're required to run Apex tests, and the command returns a job ID rather than executing
the deployment. If the validation succeeds, then you pass this job ID to the "sf project deploy quick" command to actually deploy the
metadata. This quick deploy takes less time because it skips running Apex tests. The job ID is valid for 10 days from when you started
the validation. Validating first is useful if the deployment to your production org take several hours and you don’t want to risk a failed
deploy.

You must run this command from within a project.

This command doesn't support source-tracking. When you quick deploy with the resulting job ID, the source you deploy overwrites the
corresponding metadata in your org.

To validate the deployment of multiple metadata components, either set multiple --metadata <name> flags or a single --metadata flag
with multiple names separated by spaces. Enclose names that contain spaces in one set of double quotes. The same syntax applies to
--source-dir.

Note: Don't use this command on sandboxes; the command is intended to be used on production orgs. By default, sandboxes don't run
tests during a deploy. If you want to validate a deployment with tests on a sandbox, use "sf project deploy start --dry-run --test-level
RunLocalTests" instead.

#### Examples for project deploy validate

NOTE: These examples focus on validating large deployments. See the help for "sf project deploy start" for examples of deploying smaller
sets of metadata which you can also use to validate.

Validate the deployment of all source files in the "force-app" directory to the default org:

```
   sf project deploy validate --source-dir force-app

```


Salesforce CLI Command Reference project Commands

Validate the deployment of all source files in two directories: "force-app" and "force-app-utils":

```
   sf project deploy validate --source-dir force-app --source-dir force-app-utils

```

Asynchronously validate the deployment and run all tests in the org with alias "my-prod-org"; command immediately returns the job
ID:

```
   sf project deploy validate --source-dir force-app --async --test-level RunAllTestsInOrg

   --target-org my-prod-org

```

Validate the deployment of all components listed in a manifest:

```
   sf project deploy validate --manifest path/to/package.xml

```

Flags

```
   --json
```

Optional

Format output as json.

Type: boolean

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option

**`-a`** **|** **`--api-version API-VERSION`**
Optional

Target API version for the validation.

Use this flag to override the default API version with the API version of your package.xml file. The default API version is the latest
version supported by the CLI.

Type: option

```
   --async
```

Optional

Run the command asynchronously.

The command immediately returns the job ID and control of the terminal to you. This way, you can continue to use the CLI. To
resume watching the validation, run "sf project deploy resume". To check the status of the validation, run "sf project deploy report".

Type: boolean

```
   --concise
```

Optional

Show concise output of the validation result.

Type: boolean

**`-x`** **|** **`--manifest MANIFEST`**
Optional

Full file path for manifest (package.xml) of components to validate for deployment.

All child components are included. If you specify this flag, don’t specify --metadata or --source-dir.

Type: option


Salesforce CLI Command Reference project Commands

**`-m`** **|** **`--metadata METADATA`**
Optional

Metadata component names to validate for deployment.

Type: option

**`-d`** **|** **`--source-dir SOURCE-DIR`**
Optional

Path to the local source files to validate for deployment.

The supplied path can be to a single file (in which case the operation is applied to only one file) or to a folder (in which case the
operation is applied to all metadata types in the directory and its subdirectories).

If you specify this flag, don’t specify --metadata or --manifest.

Type: option

```
   --metadata-dir METADATA-DIR
```

Optional

Root of directory or zip file of metadata formatted files to deploy.

Type: option

```
   --single-package
```

Optional

Indicates that the metadata zip file points to a directory structure for a single package.

Type: boolean

**`-o`** **|** **`--target-org TARGET-ORG`**
Required

Username or alias of the target org. Not required if the `target-org` configuration variable is already set.

Type: option

**`-t`** **|** **`--tests TESTS`**
Optional

Apex tests to run when --test-level is RunSpecifiedTests.

If a test name contains a space, enclose it in double quotes.

For multiple test names, use one of the following formats:

      - Repeat the flag for multiple test names: --tests Test1 --tests Test2 --tests "Test With Space"

      - Separate the test names with spaces: --tests Test1 Test2 "Test With Space"

Type: option

**`-l`** **|** **`--test-level TEST-LEVEL`**
Optional

Deployment Apex testing level.

Valid values are:

      - RunSpecifiedTests — Runs only the tests that you specify with the --tests flag. Code coverage requirements differ from the default
coverage requirements when using this test level. Executed tests must comprise a minimum of 75% code coverage for each class
and trigger in the deployment package. This coverage is computed for each class and trigger individually and is different than the
overall coverage percentage.


Salesforce CLI Command Reference project Commands

      - RunLocalTests — All tests in your org are run, except the ones that originate from installed managed and unlocked packages. This
test level is the default.

      - RunAllTestsInOrg — All tests in your org are run, including tests of managed packages.

      - RunRelevantTests (Beta) — Runs only tests that are relevant to the files being deployed. Salesforce automatically identifies the
relevant tests based on an analysis of the deployment payload and the payload dependencies. For fine-grained control, you can also
annotate test classes so that they always run in certain conditions. See "@IsTest Annotation" in the "Apex Developer Guide"
(https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_classes_annotation_isTest.htm). Each class and
trigger in the deployment package must be covered by the executed tests for a minimum of 75% code coverage. This coverage is
computed for each class and triggers individually and is different than the overall coverage percentage.

If you don’t specify a test level, the default behavior depends on the contents of your deployment package and target org. For more
information, see "Running Tests in a Deployment"
(https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_deploy_running_tests.htm) in the "Metadata
API Developer Guide".

Type: option

Permissible values are: RunAllTestsInOrg, RunLocalTests, RunSpecifiedTests, RunRelevantTests

Default value: RunLocalTests

```
   --verbose
```

Optional

Show verbose output of the validation result.

Type: boolean

**`-w`** **|** **`--wait WAIT`**
Optional

Number of minutes to wait for the command to complete and display results.

If the command continues to run after the wait period, the CLI returns control of the terminal window to you and returns the job ID.
To resume watching the validation, run "sf project deploy resume". To check the status of the validation, run "sf project deploy report".

Type: option

Default value: 33 minutes

**`-g`** **|** **`--ignore-warnings`**
Optional

Ignore warnings and allow a deployment to complete successfully.

If you specify this flag, and a warning occurs, the success status of the deployment is set to true. If you don't specify this flag, and a
warning occurs, then the success status is set to false, and the warning is treated like an error.

This flag is useful in a CI environment and your deployment includes destructive changes; if you try to delete a component that
doesn't exist in the org, you get a warning. In this case, to ensure that the command returns a success value of true, specify this flag.

Type: boolean

```
   --coverage-formatters COVERAGE-FORMATTERS
```

Optional

Format of the code coverage results.

For multiple formatters, repeat the flag for each formatter.

--coverage-formatters lcov --coverage-formatters clover

Type: option


Salesforce CLI Command Reference project Commands

Permissible values are: clover, cobertura, html-spa, html, json, json-summary, lcovonly, none, teamcity, text, text-summary

```
   --junit
```

Optional

Output JUnit test results.

Type: boolean

```
   --results-dir RESULTS-DIR
```

Optional

Output directory for code coverage and JUnit results; defaults to the deploy ID.

Type: option

```
   --purge-on-delete
```

Optional

Specify that deleted components in the destructive changes manifest file are immediately eligible for deletion rather than being
stored in the Recycle Bin.

Type: boolean

```
   --pre-destructive-changes PRE-DESTRUCTIVE-CHANGES
```

Optional

File path for a manifest (destructiveChangesPre.xml) of components to delete before the deploy

Type: option

```
   --post-destructive-changes POST-DESTRUCTIVE-CHANGES
```

Optional

File path for a manifest (destructiveChangesPost.xml) of components to delete after the deploy.

Type: option

Aliases for **`project deploy validate`**

```
   deploy:metadata:validate

#### **`project generate manifest`**

```

Create a project manifest that lists the metadata components you want to deploy or retrieve.

#### Description for project generate manifest

Create a manifest from a list of metadata components (--metadata) or from one or more local directories that contain source files
(--source-dir). You can specify either of these flags, not both.

Use --type to specify the type of manifest you want to create. The resulting manifest files have specific names, such as the standard
package.xml or destructiveChanges.xml to delete metadata. Valid values for this flag, and their respective file names, are:

    - package : package.xml (default)

    - pre : destructiveChangesPre.xml

    - post : destructiveChangesPost.xml

    - destroy : destructiveChanges.xml


Salesforce CLI Command Reference project Commands

See https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_deploy_deleting_files.htm for information about
these destructive manifest files.

Use --name to specify a custom name for the generated manifest if the pre-defined ones don’t suit your needs. You can specify either
--type or --name, but not both.

To include multiple metadata components, either set multiple --metadata <name> flags or a single --metadata flag with multiple names
separated by spaces. Enclose names that contain spaces in one set of double quotes. The same syntax applies to --include-packages
and --source-dir.

To build a manifest from the metadata in an org, use the --from-org flag. You can combine --from-org with the --metadata flag to include
only certain metadata types, or with the --excluded-metadata flag to exclude certain metadata types. When building a manifest from
an org, the command makes many concurrent API calls to discover the metadata that exists in the org. To limit the number of concurrent
requests, use the SF_LIST_METADATA_BATCH_SIZE environment variable and set it to a size that works best for your org and environment.
If you experience timeouts or inconsistent manifest contents, then setting this environment variable can improve accuracy. However,
the command takes longer to run because it sends fewer requests at a time.

Examples for **`project generate manifest`**

Create a manifest for deploying or retrieving all Apex classes and custom objects:

```
   $ sf project generate manifest --metadata ApexClass --metadata CustomObject

```

Create a manifest for deleting the specified Apex class:

```
   $ sf project generate manifest --metadata ApexClass:MyApexClass --type destroy

```

Create a manifest for deploying or retrieving all the metadata components in the specified local directory; name the file myNewManifest.xml:

```
   $ sf project generate manifest --source-dir force-app --name myNewManifest

```

Create a manifest from the metadata components in the specified org and include metadata in any unlocked packages:

```
   $ sf project generate manifest --from-org test@myorg.com --include-packages unlocked

```

Create a manifest from specific metadata types in an org:

```
   $ sf project generate manifest --from-org test@myorg.com --metadata

   ApexClass,CustomObject,CustomLabels

```

Create a manifest from all metadata components in an org excluding specific metadata types:

```
   $ sf project generate manifest --from-org test@myorg.com --excluded-metadata StandardValueSet

```

Flags

```
   --json
```

Optional

Format output as json.

Type: boolean

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option


Salesforce CLI Command Reference project Commands

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

**`-m`** **|** **`--metadata METADATA`**
Optional

Names of metadata components to include in the manifest.

Type: option

**`-p`** **|** **`--source-dir SOURCE-DIR`**
Optional

Paths to the local source files to include in the manifest.

Type: option

**`-n`** **|** **`--name NAME`**
Optional

Name of a custom manifest file to create.

Type: option

**`-t`** **|** **`--type TYPE`**
Optional

Type of manifest to create; the type determines the name of the created file.

Type: option

Permissible values are: pre, post, destroy, package

**`-c`** **|** **`--include-packages INCLUDE-PACKAGES`**
Optional

Package types (managed, unlocked) whose metadata is included in the manifest; by default, metadata in managed and unlocked
packages is excluded. Metadata in unmanaged packages is always included.

Type: option

Permissible values are: managed, unlocked

```
   --excluded-metadata EXCLUDED-METADATA
```

Optional

Metadata types to exclude when building a manifest from an org. Specify the name of the type, not the name of a specific component.

Type: option

```
   --from-org FROM-ORG
```

Optional

Username or alias of the org that contains the metadata components from which to build a manifest.

Type: option

**`-d`** **|** **`--output-dir OUTPUT-DIR`**
Optional

Directory to save the created manifest.

Type: option


Salesforce CLI Command Reference project Commands

Aliases for **`project generate manifest`**

```
   force:source:manifest:create

#### **`project list ignored`**

```

Check your local project package directories for forceignored files.

#### Description for project list ignored

When deploying or retrieving metadata between your local project and an org, you can specify the source files you want to exclude
with a .forceignore file. The .forceignore file structure mimics the .gitignore structure. Each line in .forceignore specifies a pattern that
corresponds to one or more files. The files typically represent metadata components, but can be any files you want to exclude, such as
LWC configuration JSON files or tests.

#### Examples for project list ignored

List all the files in all package directories that are ignored:

```
   sf project list ignored

```

List all the files in a specific directory that are ignored:

```
   sf project list ignored --source-dir force-app

```

Check if a particular file is ignored:

```
   sf project list ignored --source-dir package.xml

```

Flags

```
   --json
```

Optional

Format output as json.

Type: boolean

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option

**`-p`** **|** **`--source-dir SOURCE-DIR`**
Optional

File or directory of files that the command checks for foreceignored files.

Type: option

#### Aliases for project list ignored

```
   force:source:ignored:list

```


Salesforce CLI Command Reference project Commands

#### **`project reset tracking`**

Reset local and remote source tracking.

#### Description for project reset tracking

WARNING: This command deletes or overwrites all existing source tracking files. Use with extreme caution.

Resets local and remote source tracking so that Salesforce CLI no longer registers differences between your local files and those in the
org. When you next run 'project deploy preview', Salesforce CLI returns no results, even though conflicts might actually exist. Salesforce
CLI then resumes tracking new source changes as usual.

Use the --revision flag to reset source tracking to a specific revision number of an org source member. To get the revision number, query
the SourceMember Tooling API object with the 'data soql' command. For example:

sf data query --query "SELECT MemberName, MemberType, RevisionCounter FROM SourceMember" --use-tooling-api --target-org
my-scratch

#### Examples for project reset tracking

Reset source tracking for the org with alias "my-scratch":

```
   $ sf project reset tracking --target-org my-scratch

```

Reset source tracking to revision number 30 for your default org:

```
   $ sf project reset tracking --revision 30

```

Flags

```
   --json
```

Optional

Format output as json.

Type: boolean

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option

**`-o`** **|** **`--target-org TARGET-ORG`**
Required

Username or alias of the target org. Not required if the `target-org` configuration variable is already set.

Type: option

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

**`-r`** **|** **`--revision REVISION`**
Optional


Salesforce CLI Command Reference project Commands

SourceMember revision counter number to reset to.

Type: option

**`-p`** **|** **`--no-prompt`**
Optional

Don't prompt for source tracking override confirmation.

Type: boolean

Aliases for **`project reset tracking`**

```
   force:source:tracking:reset

#### **`project retrieve preview`**

```

Preview a retrieval to see what will be retrieved from the org, the potential conflicts, and the ignored files.

#### Description for project retrieve preview

You must run this command from within a project.

The command outputs a table that describes what will happen if you run the "sf project retrieve start" command. The table lists the
metadata components that will be retrieved and deleted. The table also lists the current conflicts between files in your local project and
components in the org. Finally, the table lists the files that won't be retrieved because they're included in your .forceignore file.

If your org allows source tracking, then this command displays potential conflicts between the org and your local project. Some orgs,
such as production org, never allow source tracking. Source tracking is enabled by default on scratch and sandbox orgs; you can disable
source tracking when you create the orgs by specifying the --no-track-source flag on the "sf org create scratch|sandbox" commands.

#### Examples for project retrieve preview

Preview the retrieve of all changes from your default org:

```
   sf project retrieve preview

```

Preview the retrieve when ignoring any conflicts from an org with alias "my-scratch":

```
   sf project retrieve preview --ignore-conflicts --target-org my-scratch

```

Flags

```
   --json
```

Optional

Format output as json.

Type: boolean

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option


Salesforce CLI Command Reference project Commands

**`-c`** **|** **`--ignore-conflicts`**
Optional

Don't display conflicts in the preview of the retrieval.

This flag applies only to orgs that allow source tracking. It has no effect on orgs that don't allow it, such as production orgs.

Type: boolean

**`-o`** **|** **`--target-org TARGET-ORG`**
Required

Username or alias of the target org. Not required if the `target-org` configuration variable is already set.

Type: option

```
   --concise
```

Optional

Show only the changes that will be retrieved; omits files that are forceignored.

Type: boolean

Aliases for **`project retrieve preview`**

```
   retrieve:metadata:preview

#### **`project retrieve start`**

```

Retrieve metadata from an org to your local project.

#### Description for project retrieve start

You must run this command from within a project.

Metadata components are retrieved in source format by default. Retrieve them in metadata format by specifying the --target-metadata-dir
flag, which retrieves the components into a ZIP file in the specified directory.

If your org allows source tracking, then this command tracks the changes in your source. Some orgs, such as production orgs, never
allow source tracking. Source tracking is enabled by default on scratch and sandbox orgs; you can disable source tracking when you
create the orgs by specifying the --no-track-source flag on the "sf org create scratch|sandbox" commands.

To retrieve multiple metadata components, either use multiple --metadata <name> flags or use a single --metadata flag with multiple
names separated by spaces. Enclose names that contain spaces in one set of double quotes. The same syntax applies to --source-dir.

#### Examples for project retrieve start

Retrieve all remote changes from your default org:

```
   sf project retrieve start

```

Retrieve the source files in the "force-app" directory from an org with alias "my-scratch":

```
   sf project retrieve start --source-dir force-app --target-org my-scratch

```


Salesforce CLI Command Reference project Commands

Retrieve all the Apex classes and custom objects whose source is in the "force-app" directory. The list views, layouts, etc, that are associated
with the custom objects are also retrieved. Both examples are equivalent:

```
   sf project retrieve start --source-dir force-app/main/default/classes

   force-app/main/default/objects

   sf project retrieve start --source-dir force-app/main/default/classes --source-dir

   force-app/main/default/objects

```

Retrieve all Apex classes that are in all package directories defined in the "sfdx-project.json" file:

```
   sf project retrieve start --metadata ApexClass

```

Retrieve a specific Apex class; ignore any conflicts between the local project and org (be careful with this flag, because it will overwrite
the Apex class source files in your local project if there are conflicts!):

```
   sf project retrieve start --metadata ApexClass:MyApexClass --ignore-conflicts

```

Retrieve specific Apex classes that match a pattern; in this example, retrieve Apex classes whose names contain the string "MyApex":

```
   sf project retrieve start --metadata 'ApexClass:MyApex*'

```

Retrieve a custom object called ExcitingObject that's in the SBQQ namespace:

```
   sf project retrieve start --metadata CustomObject:SBQQ__ExcitingObject

```

Retrieve all custom objects in the SBQQ namespace by using a wildcard and quotes:

```
   sf project retrieve start --metadata 'CustomObject:SBQQ__*'

```

Retrieve all list views for the Case standard object:

```
   sf project retrieve start --metadata 'ListView:Case*'

```

Retrieve all custom objects and Apex classes found in all defined package directories (both examples are equivalent):

```
   sf project retrieve start --metadata CustomObject ApexClass

   sf project retrieve start --metadata CustomObject --metadata ApexClass

```

Retrieve all metadata components listed in a manifest:

```
   sf project retrieve start --manifest path/to/package.xml

```

Retrieve metadata from a package:

```
   sf project retrieve start --package-name MyPackageName

```

Retrieve metadata from multiple packages, one of which has a space in its name (both examples are equivalent):

```
   sf project retrieve start --package-name Package1 "PackageName With Spaces" Package3

   sf project retrieve start --package-name Package1 --package-name "PackageName With Spaces"

    --package-name Package3

```

Retrieve the metadata components listed in the force-app directory, but retrieve them in metadata format into a ZIP file in the "output"
directory:

```
   sf project retrieve start --source-dir force-app --target-metadata-dir output

```


Salesforce CLI Command Reference project Commands

Retrieve in metadata format and automatically extract the contents into the "output" directory:

```
   sf project retrieve start --source-dir force-app --target-metadata-dir output --unzip

```

Flags

```
   --json
```

Optional

Format output as json.

Type: boolean

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option

**`-a`** **|** **`--api-version API-VERSION`**
Optional

Target API version for the retrieve.

Use this flag to override the default API version, which is the latest version supported the CLI, with the API version in your package.xml
file.

Type: option

**`-c`** **|** **`--ignore-conflicts`**
Optional

Ignore conflicts and retrieve and save files to your local filesystem, even if they overwrite your local changes.

This flag applies only to orgs that allow source tracking. It has no effect on orgs that don't allow it, such as production orgs.

Type: boolean

**`-x`** **|** **`--manifest MANIFEST`**
Optional

File path for the manifest (package.xml) that specifies the components to retrieve.

If you specify this flag, don’t specify --metadata or --source-dir.

Type: option

**`-m`** **|** **`--metadata METADATA`**
Optional

Metadata component names to retrieve. Wildcards (`*`) supported as long as you use quotes, such as `ApexClass:MyClass*`.

Type: option

**`-n`** **|** **`--package-name PACKAGE-NAME`**
Optional

Package names to retrieve. Use of this flag is for reference only; don't use it to retrieve packaged metadata for development.

The metadata of the supplied package name(s) will be retrieved into a child directory of the project. The name of that child directory
matches the name of the package. The retrieved metadata is meant for your reference only, don't add it to a source control system
for development and deployment. For package development, retrieve the metadata using a manifest (`--manifest` flag) or by targeting
a source controlled package directory within your project (`--source-dir` flag).


Salesforce CLI Command Reference project Commands

Type: option

**`-r`** **|** **`--output-dir OUTPUT-DIR`**
Optional

Directory root for the retrieved source files.

The root of the directory structure into which the source files are retrieved.

If the target directory matches one of the package directories in your sfdx-project.json file, the command fails.

Running the command multiple times with the same target adds new files and overwrites existing files.

Type: option

```
   --single-package
```

Optional

Indicates that the zip file points to a directory structure for a single package.

Type: boolean

**`-d`** **|** **`--source-dir SOURCE-DIR`**
Optional

File paths for source to retrieve from the org.

The supplied paths can be to a single file (in which case the operation is applied to only one file) or to a folder (in which case the
operation is applied to all source files in the directory and its subdirectories).

Type: option

**`-t`** **|** **`--target-metadata-dir TARGET-METADATA-DIR`**
Optional

Directory that will contain the retrieved metadata format files or ZIP.

Type: option

**`-o`** **|** **`--target-org TARGET-ORG`**
Required

Username or alias of the target org. Not required if the `target-org` configuration variable is already set.

Type: option

**`-w`** **|** **`--wait WAIT`**
Optional

Number of minutes to wait for the command to complete and display results to the terminal window.

If the command continues to run after the wait period, the CLI returns control of the terminal window to you.

Type: option

Default value: 33 minutes

**`-z`** **|** **`--unzip`**
Optional

Extract all files from the retrieved zip file.

Type: boolean

```
   --zip-file-name ZIP-FILE-NAME
```

Optional

File name to use for the retrieved zip file.


### Salesforce CLI Command Reference schema Commands

Type: option

Aliases for **`project retrieve start`**

```
   retrieve:metadata

### schema Commands

```

Generate metadata files.

#### schema generate field

Generate metadata source files for a new custom field on a specified object.

schema generate platformevent
Generate metadata source files for a new platform event.

schema generate sobject
Generate metadata source files for a new custom object.

schema generate tab
Generate the metadata source files for a new custom tab on a custom object.

#### **`schema generate field`**

Generate metadata source files for a new custom field on a specified object.

#### Description for schema generate field

This command is interactive and must be run in a Salesforce DX project directory. You're required to specify the field's label with the
"--label" flag. The command uses this label to provide intelligent suggestions for other field properties, such as its API name.

You can generate a custom field on either a standard object, such as Account, or a custom object. In both cases, the source files for the
object must already exist in your local project before you run this command. If you create a relationship field, the source files for the
parent object must also exist in your local directory. Use the command "sf metadata retrieve -m CustomObject:<object>" to retrieve
source files for both standard and custom objects from your org. To create a custom object, run the "sf generate metadata sobject"
command or use the Object Manager UI in your Salesforce org.

#### Examples for schema generate field

Create a field with the specified label; the command prompts you for the object:

```
   sf schema generate field --label "My Field"

```

Specify the local path to the object's folder:

```
   sf schema generate field --label "My Field" --object

   force-app/main/default/objects/MyObject__c

```

Flags

```
   --flags-dir FLAGS-DIR
```

Optional


Salesforce CLI Command Reference schema Commands

Import flag values from a directory.

Type: option

**`-l`** **|** **`--label LABEL`**
Required

The field's label.

Type: option

**`-o`** **|** **`--object OBJECT`**
Optional

The directory that contains the object's source files.

The object source files in your local project are grouped in a directoy with the same name as the object. Custom object names always
end in "__c". An example of the object directory for the Account standard object is "force-app/main/default/objects/Account" An
example custom object directory is "force-app/main/default/objects/MyObject__c"

If you don't specify this flag, the command prompts you to choose from your local objects.

Type: option

Aliases for **`schema generate field`**

```
   generate:metadata:field

#### **`schema generate platformevent`**

```

Generate metadata source files for a new platform event.

#### Description for schema generate platformevent

This command is interactive and must be run in a Salesforce DX project directory. You're required to specify the event's label with the
"--label" flag. The command uses this label to provide intelligent suggestions for other event properties, such as its API name.

#### Examples for schema generate platformevent

Create a platform event with the specified label:

```
   sf schema generate platformevent --label "My Platform Event"

```

Flags

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option

**`-l`** **|** **`--label LABEL`**
Required

The platform event's label.

Type: option


Salesforce CLI Command Reference schema Commands

Aliases for **`schema generate platformevent`**

```
   generate:metadata:platformevent

#### **`schema generate sobject`**

```

Generate metadata source files for a new custom object.

#### Description for schema generate sobject

This command is interactive and must be run in a Salesforce DX project directory. You're required to specify the object's label with the
"--label" flag. The command uses this label to provide intelligent suggestions for other object properties, such as its API name and plural
label.

All Salesforce objects are required to have a Name field, so this command also prompts you for the label and type of the Name field. Run
the "sf metadata generate field" command to create additional fields for the object.

To reduce the number of prompts, use the "--use-default-features" flag to automatically enable some features, such as reporting and
search on the object.

#### Examples for schema generate sobject

Create a custom object with the specified label and be prompted for additional information:

```
   sf schema generate sobject --label "My Object"

```

Create a custom object and enable optional features without prompting:

```
   sf schema generate sobject --label "My Object" --use-default-features

```

Flags

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option

**`-l`** **|** **`--label LABEL`**
Required

The custom object's label.

Type: option

**`-f`** **|** **`--use-default-features`**
Optional

Enable all optional features without prompting.

Enables these features:

      - Search: Allows users to find the custom object's records when they search, including SOSL.

      - Feeds: Enables feed tracking.

      - Reports: Allows reporting of the data in the custom object records.

      - History: Enables object history tracking.


Salesforce CLI Command Reference schema Commands

      - Activities: Allows users to associate tasks and scheduled calendar events related to the custom object records.

      - Bulk API: With Sharing and Streaming API, classifies the custom object as an Enterprise Application object.

      - Sharing: With Bulk API and Streaming API, classifies the custom object as an Enterprise Application object.

      - Streaming API: With Bulk API and Sharing, classifies the custom object as an Enterprise Application object.

Type: boolean

Aliases for **`schema generate sobject`**

```
   generate:metadata:sobject

#### **`schema generate tab`**

```

Generate the metadata source files for a new custom tab on a custom object.

#### Description for schema generate tab

Custom tabs let you display custom object data or other web content in Salesforce. Custom tabs appear in Salesforce as an item in the
app’s navigation bar and in the App Launcher.

This command must be run in a Salesforce DX project directory. You must pass all required information to it with the required flags. The
source files for the custom object for which you're generating a tab don't need to exist in your local project.

#### Examples for schema generate tab

Create a tab on the `MyObject__c` custom object:

```
   sf schema generate tab --object `MyObject__c` --icon 54 --directory

   force-app/main/default/tabs

```

Flags

```
   --json
```

Optional

Format output as json.

Type: boolean

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option

**`-o`** **|** **`--object OBJECT`**
Required

API name of the custom object you're generating a tab for.

The API name for a custom object always ends in `__c`, such as `MyObject__c`.

Type: option


### Salesforce CLI Command Reference sobject Commands

**`-d`** **|** **`--directory DIRECTORY`**
Required

Path to a "tabs" directory that will contain the source files for your new tab.

Type: option

**`-i`** **|** **`--icon ICON`**
Required

Number from 1 to 100 that specifies the color scheme and icon for the custom tab.

See https://lightningdesignsystem.com/icons/#custom for the available icons.

Type: option

Default value: 1

Aliases for **`schema generate tab`**

```
   generate:metadata:tab

### sobject Commands

```

Commands to interact with Salesforce objects.

#### sobject describe

Display the metadata for a standard or custom object or a Tooling API object.

sobject list
List all Salesforce objects of a specified category.

#### **`sobject describe`**

Display the metadata for a standard or custom object or a Tooling API object.

#### Description for sobject describe

The metadata is displayed in JSON format. See this topic for a description of each property:
https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_calls_describesobjects_describesobjectresult.htm.

This command displays metadata for Salesforce objects by default. Use the --use-tooling-api flag to view metadata for a Tooling API
object.

#### Examples for sobject describe

Display the metadata of the "Account" standard object in your default org:

```
   sf sobject describe --sobject Account

```

Display the metadata of the "MyObject__c" custom object in the org with alias "my-scratch-org":

```
   sf sobject describe --sobject MyObject__c --target-org my-scratch-org

```


Salesforce CLI Command Reference sobject Commands

Display the metadata of the ApexCodeCoverage Tooling API object in your default org:

```
   sf sobject describe --sobject ApexCodeCoverage --use-tooling-api

```

Flags

```
   --json
```

Optional

Format output as json.

Type: boolean

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option

**`-o`** **|** **`--target-org TARGET-ORG`**
Required

Username or alias of the target org. Not required if the `target-org` configuration variable is already set.

Type: option

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

**`-s`** **|** **`--sobject SOBJECT`**
Required

API name of the object to describe.

Type: option

**`-t`** **|** **`--use-tooling-api`**
Optional

Use Tooling API to display metadata for Tooling API objects.

Type: boolean

Aliases for **`sobject describe`**

```
   force:schema:sobject:describe

#### **`sobject list`**

```

List all Salesforce objects of a specified category.

#### Description for sobject list

You can list the standard objects, custom objects, or all. The lists include only Salesforce objects, not Tooling API objects.


### Salesforce CLI Command Reference template Commands

Examples for **`sobject list`**

List all objects in your default org:

```
   sf sobject list --sobject all

```

List only custom objects in the org with alias "my-scratch-org":

```
   sf sobject list --sobject custom --target-org my-scratch-org

```

Flags

```
   --json
```

Optional

Format output as json.

Type: boolean

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option

**`-o`** **|** **`--target-org TARGET-ORG`**
Required

Username or alias of the target org. Not required if the `target-org` configuration variable is already set.

Type: option

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

**`-s`** **|** **`--sobject SOBJECT`**
Optional

Category of objects to list.

Type: option

Default value: ALL

Aliases for **`sobject list`**

```
   force:schema:sobject:list

### template Commands

```

Collection of Salesforce templates.

template generate analytics template
Generate a simple Analytics template.


Salesforce CLI Command Reference template Commands

template generate apex class
Generate an Apex class.

template generate apex trigger
Generate an Apex trigger.

template generate digital-experience site (Developer Preview)
Generate an Experience Cloud site.

template generate flexipage (Beta)
Generate a FlexiPage, also known as a Lightning page.

template generate lightning app
Generate a Lightning App.

template generate lightning component
Generate a bundle for an Aura component or a Lightning web component.

template generate lightning event
Generate a Lightning Event.

template generate lightning interface
Generate a Lightning Interface.

template generate lightning test
Generate a Lightning test.

template generate project
Generate a Salesforce DX project.

template generate static-resource
Generate a static resource.

template generate ui-bundle
Generate a UI bundle, which contains the code and metadata to build a UI experience that uses non-native Salesforce frameworks,
such as React.

template generate visualforce component
Generate a Visualforce Component.

template generate visualforce page
Generate a Visualforce Page.

#### **`template generate analytics template`**

Generate a simple Analytics template.

#### Description for template generate analytics template

The metadata files associated with the Analytics template must be contained in a parent directory called "waveTemplates" in your
package directory. Either run this command from an existing directory of this name, or use the --output-dir flag to generate one or point
to an existing one.


Salesforce CLI Command Reference template Commands

Examples for **`template generate analytics template`**

Generate the metadata files for a simple Analytics template file called myTemplate in the force-app/main/default/waveTemplates
directory:

```
   sf template generate analytics template --name myTemplate --output-dir

   force-app/main/default/waveTemplates

```

Flags

```
   --json
```

Optional

Format output as json.

Type: boolean

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option

**`-d`** **|** **`--output-dir OUTPUT-DIR`**
Optional

Directory for saving the created files.

The location can be an absolute path or relative to the current working directory. The default is the current directory.

Type: option

Default value: .

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

**`-n`** **|** **`--name NAME`**
Required

Name of the Analytics template.

Type: option

Aliases for **`template generate analytics template`**

```
   force:analytics:template:create

   analytics generate template

#### **`template generate apex class`**

```

Generate an Apex class.


Salesforce CLI Command Reference template Commands

Description for **`template generate apex class`**

Generates the Apex *.cls file and associated metadata file. These files must be contained in a parent directory called "classes" in your
package directory. Either run this command from an existing directory of this name, or use the --output-dir flag to generate one or point
to an existing one.

Examples for **`template generate apex class`**

Generate two metadata files associated with the MyClass Apex class (MyClass.cls and MyClass.cls-meta.xml) in the current directory:

```
   sf template generate apex class --name MyClass

```

Similar to previous example, but generates the files in the "force-app/main/default/classes" directory:

```
   sf template generate apex class --name MyClass --output-dir force-app/main/default/classes

```

Flags

```
   --json
```

Optional

Format output as json.

Type: boolean

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option

**`-n`** **|** **`--name NAME`**
Required

Name of the generated Apex class.

The name can be up to 40 characters and must start with a letter.

Type: option

**`-t`** **|** **`--template TEMPLATE`**
Optional

Template to use for file creation.

Supplied parameter values or default values are filled into a copy of the template.

Type: option

Permissible values are: ApexException, ApexUnitTest, BasicUnitTest, DefaultApexClass, InboundEmailService

Default value: DefaultApexClass

**`-d`** **|** **`--output-dir OUTPUT-DIR`**
Optional

Directory for saving the created files.

The location can be an absolute path or relative to the current working directory. The default is the current directory.

Type: option

Default value: .


Salesforce CLI Command Reference template Commands

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

Aliases for **`template generate apex class`**

```
   force:apex:class:create

   apex:generate:class

#### **`template generate apex trigger`**

```

Generate an Apex trigger.

#### Description for template generate apex trigger

Generates the Apex trigger *.trigger file and associated metadata file. These files must be contained in a parent directory called "triggers"
in your package directory. Either run this command from an existing directory of this name, or use the --output-dir flag to generate one
or point to an existing one.

If you don't specify the --sobject flag, the .trigger file contains the generic placeholder SOBJECT; replace it with the Salesforce object you
want to generate a trigger for. If you don't specify --event, "before insert" is used.

#### Examples for template generate apex trigger

Generate two files associated with the MyTrigger Apex trigger (MyTrigger.trigger and MyTrigger.trigger-meta.xml) in the current directory:

```
   sf template generate apex trigger --name MyTrigger

```

Similar to the previous example, but generate the files in the "force-app/main/default/triggers" directory:

```
   sf template generate apex trigger --name MyTrigger --output-dir

   force-app/main/default/triggers

```

Generate files for a trigger that fires on the Account object before and after an insert:

```
   sf template generate apex trigger --name MyTrigger --sobject Account --event "before

   insert,after insert"

```

Flags

```
   --json
```

Optional

Format output as json.

Type: boolean

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.


Salesforce CLI Command Reference template Commands

Type: option

**`-n`** **|** **`--name NAME`**
Required

Name of the generated Apex trigger

The name can be up to 40 characters and must start with a letter.

Type: option

**`-t`** **|** **`--template TEMPLATE`**
Optional

Template to use for file creation.

Supplied parameter values or default values are filled into a copy of the template.

Type: option

Permissible values are: ApexTrigger

Default value: ApexTrigger

**`-d`** **|** **`--output-dir OUTPUT-DIR`**
Optional

Directory for saving the created files.

The location can be an absolute path or relative to the current working directory. The default is the current directory.

Type: option

Default value: .

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

**`-s`** **|** **`--sobject SOBJECT`**
Optional

Salesforce object to generate a trigger on.

Type: option

Default value: SOBJECT

**`-e`** **|** **`--event EVENT`**
Optional

Events that fire the trigger.

Type: option

Permissible values are: before insert, before update, before delete, after insert, after update, after delete, after undelete

Default value: before insert

Aliases for **`template generate apex trigger`**

```
   force:apex:trigger:create

   apex:generate:trigger

```


Salesforce CLI Command Reference template Commands

#### template generate digital-experience site (Developer Preview)

Generate an Experience Cloud site.

Note: This command is available as a developer preview. The command isn’t generally available unless or until Salesforce announces
its general availability in documentation or in press releases or public statements. All commands, parameters, and other features
are subject to change or deprecation at any time, with or without notice. Don't implement functionality developed with these
commands or tools.

#### Description for template generate digital-experience site

Creates the metadata of an Experience Cloud site with the specified template, name, and URL path prefix. The output includes all the
necessary metadata files, including DigitalExperienceConfig, DigitalExperienceBundle, Network, and CustomSite.

Unlike `sf community create`, which builds the site directly in the org, this command generates only the local metadata.

#### Examples for template generate digital-experience site

Generate an Experience Cloud site using the Build Your Own (LWR) template. The site is called "mysite" and has the URL path prefix
"mysite":

```
   sf template generate digital-experience site --template-name "Build Your Own (LWR)" --name

    mysite --url-path-prefix mysite

```

Generate an Experience Cloud site like the last example, but generate the files into the specified output directory:

```
   sf template generate digital-experience site --template-name "Build Your Own (LWR)" --name

    mysite --url-path-prefix mysite --output-dir force-app/main/default

```

Flags

```
   --json
```

Optional

Format output as json.

Type: boolean

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option

**`-o`** **|** **`--target-org TARGET-ORG`**
Optional

Username or alias of the target org.

Type: option

**`-n`** **|** **`--name NAME`**
Required

Name of the Experience Cloud site to generate.

Type: option


Salesforce CLI Command Reference template Commands

**`-t`** **|** **`--template-name TEMPLATE-NAME`**
Required

Template to use when generating the site.

Type: option

Permissible values are: Build Your Own (LWR)

**`-p`** **|** **`--url-path-prefix URL-PATH-PREFIX`**
Optional

URL path prefix for the site; must contain only alphanumeric characters.

Type: option

**`-e`** **|** **`--admin-email ADMIN-EMAIL`**
Optional

Email address for the site administrator. Defaults to the username of the currently authenticated user.

Type: option

**`-d`** **|** **`--output-dir OUTPUT-DIR`**
Optional

Directory to generate the site files in.

The location can be an absolute path or relative to the current working directory. If not specified, the command reads your
sfdx-project.json file and uses the default package directory. When running outside a Salesforce DX project, defaults to the current
directory.

Type: option

#### template generate flexipage (Beta)

Generate a FlexiPage, also known as a Lightning page.

Note: This feature is a Beta Service. Customers may opt to try such Beta Service in its sole discretion. Any use of the Beta Service
is subject to the applicable Beta Services Terms provided at Agreements and Terms
[(https://www.salesforce.com/company/legal/agreements/).](https://www.salesforce.com/company/legal/agreements/)

#### Description for template generate flexipage

FlexiPages are the metadata types associated with a Lightning page. A Lightning page represents a customizable screen made up of
regions containing Lightning components.

You can use this command to generate these types of FlexiPages; specify the type with the --template flag:

    - AppPage: A Lightning page used as the home page for a custom app or a standalone application page.

    - HomePage: A Lightning page used to override the Home page in Lightning Experience.

    - RecordPage: A Lightning page used to override an object record page in Lightning Experience. Requires that you specify the object
name with the --sobject flag.


Salesforce CLI Command Reference template Commands

Examples for **`template generate flexipage`**

Generate a RecordPage FlexiPage for the Account object in the current directory:

```
   sf template generate flexipage --name Account_Record_Page --template RecordPage --sobject

    Account

```

Generate an AppPage FlexiPage in the "force-app/main/default/flexipages" directory:

```
   sf template generate flexipage --name Sales_Dashboard --template AppPage --output-dir

   force-app/main/default/flexipages

```

Generate a HomePage FlexiPage with a custom label:

```
   sf template generate flexipage --name Custom_Home --template HomePage --label "Sales Home

    Page"

```

Generate a RecordPage with dynamic highlights and detail fields:

```
   sf template generate flexipage --name Property_Page --template RecordPage --sobject

   Rental_Property__c --primary-field Name --secondary-fields Property_Address__c,City__c

   --detail-fields Name,Property_Address__c,City__c,Monthly_Rent__c,Bedrooms__c

```

Flags

```
   --json
```

Optional

Format output as json.

Type: boolean

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option

**`-n`** **|** **`--name NAME`**
Required

Name of the FlexiPage.

The name can contain only alphanumeric characters, must start with a letter, and can't end with an underscore or contain two
consecutive underscores.

Type: option

**`-t`** **|** **`--template TEMPLATE`**
Required

Template type for the FlexiPage.

Type: option

Permissible values are: RecordPage, AppPage, HomePage

**`-d`** **|** **`--output-dir OUTPUT-DIR`**
Optional

Directory for saving the created files.

The location can be an absolute path or relative to the current working directory. The default is the current directory.


Salesforce CLI Command Reference template Commands

Type: option

Default value: .

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

```
   --label LABEL
```

Optional

Label of this FlexiPage; if not specified, uses the FlexiPage name as the label.

Type: option

```
   --description DESCRIPTION
```

Optional

Description for the FlexiPage, which provides context about its purpose.

Type: option

**`-s`** **|** **`--sobject SOBJECT`**
Optional

API name of the Salesforce object; required when creating a RecordPage.

For RecordPage FlexiPages, you must specify the associated object API name, such as 'Account', 'Opportunity', or 'Custom_Object__c'.
This sets the `sobjectType` field in the FlexiPage metadata.

Type: option

```
   --primary-field PRIMARY-FIELD
```

Optional

Primary field for the dynamic highlights header; typically 'Name'. Used only with RecordPage.

Type: option

```
   --secondary-fields SECONDARY-FIELDS
```

Optional

Secondary fields shown in the dynamic highlights header. Specify multiple fields separated by commas. Maximum of 11 fields. Used
only with RecordPage.

Type: option

```
   --detail-fields DETAIL-FIELDS
```

Optional

Fields to display in the Details tab. Specify multiple fields separated by commas. Fields are split into two columns. Used only with
RecordPage.

Type: option

#### **`template generate lightning app`**

Generate a Lightning App.


Salesforce CLI Command Reference template Commands

Description for **`template generate lightning app`**

Generates a Lightning App bundle in the specified directory or the current working directory. The bundle consists of multiple files in a
folder with the designated name.

Examples for **`template generate lightning app`**

Generate the metadata files for a Lightning app bundle called "myapp" in the current directory:

```
   sf template generate lightning app --name myapp

```

Similar to the previous example, but generate the files in the "force-app/main/default/aura" directory:

```
   sf template generate lightning app --name myapp --output-dir force-app/main/default/aura

```

Flags

```
   --json
```

Optional

Format output as json.

Type: boolean

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option

**`-n`** **|** **`--name NAME`**
Required

Name of the generated Lightning App.

The name can be up to 40 characters and must start with a letter.

Type: option

**`-t`** **|** **`--template TEMPLATE`**
Optional

Template to use for file creation.

Supplied parameter values or default values are filled into a copy of the template. For Lightning Web Components, if this flag isn't
specified, the CLI command automatically selects the template based on the "defaultLwcLanguage" field in the DX project's
"sfdx-project.json" file.

Type: option

Permissible values are: DefaultLightningApp

Default value: DefaultLightningApp

**`-d`** **|** **`--output-dir OUTPUT-DIR`**
Optional

Directory for saving the created files.

The location can be an absolute path or relative to the current working directory. The default is the current directory.

Type: option


Salesforce CLI Command Reference template Commands

Default value: .

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

Aliases for **`template generate lightning app`**

```
   force:lightning:app:create

   lightning:generate:app

#### **`template generate lightning component`**

```

Generate a bundle for an Aura component or a Lightning web component.

#### Description for template generate lightning component

Generates the bundle in the specified directory or the current working directory. The bundle consists of multiple files in a directory with
the designated name. Lightning web components are contained in the directory with name "lwc", Aura components in "aura".

To generate a Lightning web component, pass "--type lwc" to the command. If you don’t specify --type, Salesforce CLI generates an
Aura component by default.

#### Examples for template generate lightning component

Generate the metadata files for an Aura component bundle in the current directory:

```
   sf template generate lightning component --name mycomponent

```

Generate a Lightning web component bundle in the current directory:

```
   sf template generate lightning component --name mycomponent --type lwc

```

Generate an Aura component bundle in the "force-app/main/default/aura" directory:

```
   sf template generate lightning component --name mycomponent --output-dir

   force-app/main/default/aura

```

Generate a Lightning web component bundle in the "force-app/main/default/lwc" directory:

```
   sf template generate lightning component --name mycomponent --type lwc --output-dir

   force-app/main/default/lwc

```

Generate a TypeScript Lightning Web Component:

```
   sf template generate lightning component --name mycomponent --type lwc --template typescript

```

Flags

```
   --json
```

Optional


Salesforce CLI Command Reference template Commands

Format output as json.

Type: boolean

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option

**`-n`** **|** **`--name NAME`**
Required

Name of the generated Lightning Component.

The name can be up to 40 characters and must start with a letter.

Type: option

**`-t`** **|** **`--template TEMPLATE`**
Optional

Template to use for file creation.

Supplied parameter values or default values are filled into a copy of the template. For Lightning Web Components, if this flag isn't
specified, the CLI command automatically selects the template based on the "defaultLwcLanguage" field in the DX project's
"sfdx-project.json" file.

Type: option

Permissible values are: default, analyticsDashboard, analyticsDashboardWithStep, typescript

Default value: default

**`-d`** **|** **`--output-dir OUTPUT-DIR`**
Optional

Directory for saving the created files.

The location can be an absolute path or relative to the current working directory. The default is the current directory.

Type: option

Default value: .

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

```
   --type TYPE
```

Optional

Type of the component bundle.

Type: option

Permissible values are: aura, lwc

Default value: aura


Salesforce CLI Command Reference template Commands

Aliases for **`template generate lightning component`**

```
   force:lightning:component:create

   lightning:generate:component

#### **`template generate lightning event`**

```

Generate a Lightning Event.

#### Description for template generate lightning event

Generates a Lightning Event bundle in the specified directory or the current working directory. The bundle consists of multiple files in
a folder with the designated name.

#### Examples for template generate lightning event

Generate the metadata files for a Lightning event bundle called "myevent" in the current directory:

```
   sf template generate lightning event --name myevent

```

Similar to previous example, but generate the files in the "force-app/main/default/aura" directory:

```
   sf template generate lightning event --name myevent --output-dir force-app/main/default/aura

```

Flags

```
   --json
```

Optional

Format output as json.

Type: boolean

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option

**`-n`** **|** **`--name NAME`**
Required

Name of the generated Lightning Event.

The name can be up to 40 characters and must start with a letter.

Type: option

**`-t`** **|** **`--template TEMPLATE`**
Optional

Template to use for file creation.

Supplied parameter values or default values are filled into a copy of the template. For Lightning Web Components, if this flag isn't
specified, the CLI command automatically selects the template based on the "defaultLwcLanguage" field in the DX project's
"sfdx-project.json" file.


Salesforce CLI Command Reference template Commands

Type: option

Permissible values are: DefaultLightningEvt

Default value: DefaultLightningEvt

**`-d`** **|** **`--output-dir OUTPUT-DIR`**
Optional

Directory for saving the created files.

The location can be an absolute path or relative to the current working directory. The default is the current directory.

Type: option

Default value: .

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

Aliases for **`template generate lightning event`**

```
   force:lightning:event:create

   lightning:generate:event

#### **`template generate lightning interface`**

```

Generate a Lightning Interface.

#### Description for template generate lightning interface

Generates a Lightning Interface bundle in the specified directory or the current working directory. The bundle consists of multiple files
in a folder with the designated name.

#### Examples for template generate lightning interface

Generate the metadata files for a Lightning interface bundle called "myinterface" in the current directory:

```
   sf template generate lightning interface --name myinterface

```

Similar to the previous example but generate the files in the "force-app/main/default/aura" directory:

```
   sf template generate lightning interface --name myinterface --output-dir

   force-app/main/default/aura

```

Flags

```
   --json
```

Optional

Format output as json.

Type: boolean


Salesforce CLI Command Reference template Commands

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option

**`-n`** **|** **`--name NAME`**
Required

Name of the generated Lightning Interface.

The name can be up to 40 characters and must start with a letter.

Type: option

**`-t`** **|** **`--template TEMPLATE`**
Optional

Template to use for file creation.

Supplied parameter values or default values are filled into a copy of the template. For Lightning Web Components, if this flag isn't
specified, the CLI command automatically selects the template based on the "defaultLwcLanguage" field in the DX project's
"sfdx-project.json" file.

Type: option

Permissible values are: DefaultLightningIntf

Default value: DefaultLightningIntf

**`-d`** **|** **`--output-dir OUTPUT-DIR`**
Optional

Directory for saving the created files.

The location can be an absolute path or relative to the current working directory. The default is the current directory.

Type: option

Default value: .

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

Aliases for **`template generate lightning interface`**

```
   force:lightning:interface:create

   lightning:generate:interface

#### **`template generate lightning test`**

```

Generate a Lightning test.

#### Description for template generate lightning test

Generates the test in the specified directory or the current working directory. The .resource file and associated metadata file are generated.


Salesforce CLI Command Reference template Commands

Examples for **`template generate lightning test`**

Generate the metadata files for the Lightning test called MyLightningTest in the current directory:

```
   sf template generate lightning test --name MyLightningTest

```

Similar to the previous example but generate the files in the "force-app/main/default/lightningTests" directory:

```
   sf template generate lightning test --name MyLightningTest --output-dir

   force-app/main/default/lightningTests

```

Flags

```
   --json
```

Optional

Format output as json.

Type: boolean

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option

**`-n`** **|** **`--name NAME`**
Required

Name of the generated Lightning Test.

Name of the new Lightning test; can be up to 40 characters and must start with a letter.

Type: option

**`-t`** **|** **`--template TEMPLATE`**
Optional

Template to use for file creation.

Supplied parameter values or default values are filled into a copy of the template. For Lightning Web Components, if this flag isn't
specified, the CLI command automatically selects the template based on the "defaultLwcLanguage" field in the DX project's
"sfdx-project.json" file.

Type: option

Permissible values are: DefaultLightningTest

Default value: DefaultLightningTest

**`-d`** **|** **`--output-dir OUTPUT-DIR`**
Optional

Directory for saving the created files.

The location can be an absolute path or relative to the current working directory. The default is the current directory.

Type: option

Default value: .

```
   --api-version API-VERSION
```

Optional


Salesforce CLI Command Reference template Commands

Override the api version used for api requests made by this command

Type: option

Aliases for **`template generate lightning test`**

```
   force:lightning:test:create

   lightning:generate:test

#### **`template generate project`**

```

Generate a Salesforce DX project.

#### Description for template generate project

A Salesforce DX project has a specific structure and a configuration file (sfdx-project.json) that identifies the directory as a Salesforce DX
project. This command generates the necessary configuration files and directories to get you started.

By default, the generated sfdx-project.json file sets the sourceApiVersion property to the default API version currently used by Salesforce
CLI. To specify a different version, set the apiVersion configuration variable. For example: "sf config set apiVersion=57.0 --global".

#### Examples for template generate project

Generate a project called "mywork":

```
   sf template generate project --name mywork

```

Similar to previous example, but generate the files in a directory called "myapp":

```
   sf template generate project --name mywork --default-package-dir myapp

```

Similar to prevoius example, but also generate a default package.xml manifest file:

```
   sf template generate project --name mywork --default-package-dir myapp --manifest

```

Generate a project with the minimum files and directories:

```
   sf template generate project --name mywork --template empty

```

Generate a project in which the Lightning Web Components use TypeScript rather than the default JavaScript:

```
   sf template generate project --name mywork --lwc-language typescript

```

Flags

```
   --json
```

Optional

Format output as json.

Type: boolean

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.


Salesforce CLI Command Reference template Commands

Type: option

**`-n`** **|** **`--name NAME`**
Required

Name of the generated project.

Generates a project directory with this name; any valid directory name is accepted. Also sets the "name" property in the sfdx-project.json
file to this name.

Type: option

**`-t`** **|** **`--template TEMPLATE`**
Optional

Template to use for project creation.

The template determines the sample configuration files and directories that this command generates. For example, the empty
template provides these files and directory to get you started.

      - .forceignore

      - config/project-scratch-def.json

      - sfdx-project.json

      - package.json

      - force-app (basic source directory structure)

The standard template provides a complete force-app directory structure so you know where to put your source. It also provides
additional files and scripts, especially useful when using Salesforce Extensions for VS Code. For example:

      - .gitignore: Use Git for version control.

      - .prettierrc and .prettierignore: Use Prettier to format your Aura components.

      - .vscode/extensions.json: When launched, Visual Studio Code, prompts you to install the recommended extensions for your project.

      - .vscode/launch.json: Configures Replay Debugger.

      - .vscode/settings.json: Additional configuration settings.

The analytics template provides similar files and the force-app/main/default/waveTemplates directory.

The reactinternalapp and reactexternalapp templates provide React-based project scaffolding for internal and external UI bundle
use cases.

The agent template provides project scaffolding for building Agentforce agents and includes a sample agent called Local Info Agent.

Type: option

Permissible values are: standard, empty, analytics, reactinternalapp, reactexternalapp, agent

Default value: standard

**`-d`** **|** **`--output-dir OUTPUT-DIR`**
Optional

Directory for saving the created files.

The location can be an absolute path or relative to the current working directory. The default is the current directory.

Type: option

Default value: .

**`-s`** **|** **`--namespace NAMESPACE`**
Optional


Salesforce CLI Command Reference template Commands

Namespace associated with this project and any connected scratch orgs.

Type: option

**`-p`** **|** **`--default-package-dir DEFAULT-PACKAGE-DIR`**
Optional

Default package directory name.

Metadata items such as classes and Lightning bundles are placed inside this folder.

Type: option

Default value: force-app

**`-x`** **|** **`--manifest`**
Optional

Generate a manifest (package.xml) for change-set based development.

Generates a default manifest (package.xml) for fetching Apex, Visualforce, Lightning components, and static resources.

Type: boolean

```
   --lwc-language LWC-LANGUAGE
```

Optional

Language of the Lightning Web Components. If not specified, "javascript" is used.

When set to `'typescript'`, generates TypeScript configuration files (tsconfig.json, package.json with TypeScript dependencies, and
TypeScript-aware ESLint config). When you deploy the TypeScript-based Lightning Web Components, the TypeScript files are first
compiled locally for validation and then the `.ts` files are deployed to your org for server-side type stripping.

Type: option

Permissible values are: javascript, typescript

```
   --api-version API-VERSION
```

Optional

Will set this version as sourceApiVersion in the sfdx-project.json file

Override the api version used for api requests made by this command

Type: option

Aliases for **`template generate project`**

```
   force:project:create

   project:generate

#### **`template generate static-resource`**

```

Generate a static resource.

#### Description for template generate static-resource

Generates the metadata resource file in the specified directory or the current working directory. Static resource files must be contained
in a parent directory called "staticresources" in your package directory. Either run this command from an existing directory of this name,
or use the --output-dir flag to create one or point to an existing one.


Salesforce CLI Command Reference template Commands

Examples for **`template generate static-resource`**

Generate the metadata file for a static resource called MyResource in the current directory:

```
   sf template generate static-resource --name MyResource

```

Similar to previous example, but specifies a MIME type of application/json:

```
   sf template generate static-resource --name MyResource --type application/json

```

Generate the resource file in the "force-app/main/default/staticresources" directory:

```
   sf template generate static-resource --name MyResource --output-dir

   force-app/main/default/staticresources

```

Flags

```
   --json
```

Optional

Format output as json.

Type: boolean

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option

**`-n`** **|** **`--name NAME`**
Required

Name of the generated static resource.

This name can contain only underscores and alphanumeric characters, and must be unique in your org. It must begin with a letter,
not include spaces, not end with an underscore, and not contain two consecutive underscores.

Type: option

```
   --type TYPE
```

Optional

Content type (mime type) of the generated static resource.

Must be a valid MIME type such as application/json, application/javascript, application/zip, text/plain, text/css, etc.

Type: option

Default value: application/zip

**`-d`** **|** **`--output-dir OUTPUT-DIR`**
Optional

Directory for saving the created files.

The location can be an absolute path or relative to the current working directory. The default is the current directory.

Type: option

Default value: .

```
   --api-version API-VERSION
```

Optional


Salesforce CLI Command Reference template Commands

Override the api version used for api requests made by this command

Type: option

Aliases for **`template generate static-resource`**

```
   force:staticresource:create

   static-resource:generate

#### **`template generate ui-bundle`**

```

Generate a UI bundle, which contains the code and metadata to build a UI experience that uses non-native Salesforce frameworks, such
as React.

#### Description for template generate ui-bundle

Salesforce provides native UI frameworks, such as Lighting Web Components (LWC), to build applications that run on the Salesforce
Platform. But you can also use non-native JavaScript- or TypeScript-based UI frameworks, such as React, to build a UI experience for the
Salesforce Platform and that you can launch from the App Launcher.

These non-native UI experiences are defined by the "UIBundle" metadata type in your DX project. Use this command to generate the
required DX project structure and files. For example, when you run this command and specify the name MyUiBundle, then the files are
generated into a "uiBundles/MyUiBundle" directory. Use the --output-dir flag to specify a different directory.

Use the --template flag for generating the files to get started with a speciic UI framework, such as React. Check out the README.md file
in the generated "uiBundles/<bundlename>" directory for more information about the template.

#### Examples for template generate ui-bundle

Generate a UI bundle called MyUiBundle in the current directory:

```
   sf template generate ui-bundle --name MyUiBundle

```

Generate a React-based UI bundle:

```
   sf template generate ui-bundle --name MyReactApp --template reactbasic

```

Generate the React-based UI bundle in the "force-app/main/default/uiBundles" directory:

```
   sf template generate ui-bundle --name MyUiBundle --template reactbasic --output-dir

   force-app/main/default/uiBundles

```

Flags

```
   --json
```

Optional

Format output as json.

Type: boolean

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.


Salesforce CLI Command Reference template Commands

Type: option

**`-n`** **|** **`--name NAME`**
Required

API name of the generated UI bundle.

This name can contain only underscores and alphanumeric characters, and must be unique in your org. It must begin with a letter,
not include spaces, not end with an underscore, and not contain two consecutive underscores.

Type: option

**`-t`** **|** **`--template TEMPLATE`**
Optional

Template to use when creating the files for a specific UI framework.

Supplied parameter values or default values are filled into a copy of the template.

Type: option

Permissible values are: default, reactbasic

Default value: default

**`-l`** **|** **`--label LABEL`**
Optional

Master label for the UI bundle.

If not specified, the label is derived from the name.

Type: option

**`-d`** **|** **`--output-dir OUTPUT-DIR`**
Optional

Directory into which the files are created.

The location can be an absolute path or relative to the current working directory.

If not specified, the command reads your sfdx-project.json and defaults to "uiBundles" directory within your default package directory.
When running outside a Salesforce DX project, defaults to the current directory.

**Important:** This command automatically ensures the output directory ends with "uiBundles". If your specified path doesn't end
with "uiBundles", it's automatically appended. The UI bundle is created at "<output-dir>/<name>".

**Examples:**

      - "--output-dir force-app/main/default" Creates a UI bundle at "force-app/main/default/uiBundles/MyUiBundle/"

      - "--output-dir force-app/main/default/uiBundles" Creates a UI bundle at "force-app/main/default/uiBundles/MyUiBundle/" (no
change)

Type: option

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

#### **`template generate visualforce component`**

Generate a Visualforce Component.


Salesforce CLI Command Reference template Commands

Description for **`template generate visualforce component`**

The command generates the .Component file and associated metadata file in the specified directory or the current working directory
by default.

Examples for **`template generate visualforce component`**

Generate the metadata files for a Visualforce component in the current directory:

```
   sf template generate visualforce component --name mycomponent --label mylabel

```

Similar to previous example, but generate the files in the directory "force-app/main/default/components":

```
   sf template generate visualforce component --name mycomponent --label mylabel --output-dir

    components

```

Flags

```
   --json
```

Optional

Format output as json.

Type: boolean

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option

**`-n`** **|** **`--name NAME`**
Required

Name of the generated Visualforce Component.

The name can be up to 40 characters and must start with a letter.

Type: option

**`-t`** **|** **`--template TEMPLATE`**
Optional

Template to use for file creation.

Supplied parameter values or default values are filled into a copy of the template.

Type: option

Permissible values are: DefaultVFComponent

Default value: DefaultVFComponent

**`-d`** **|** **`--output-dir OUTPUT-DIR`**
Optional

Directory for saving the created files.

The location can be an absolute path or relative to the current working directory. The default is the current directory.

Type: option

Default value: .


Salesforce CLI Command Reference template Commands

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

**`-l`** **|** **`--label LABEL`**
Required

Visualforce Component label.

Type: option

Aliases for **`template generate visualforce component`**

```
   force:visualforce:component:create

   visualforce:generate:component

#### **`template generate visualforce page`**

```

Generate a Visualforce Page.

#### Description for template generate visualforce page

The command generates the .Page file and associated metadata file in the specified directory or the current working directory by default.

#### Examples for template generate visualforce page

Generate the metadata files for a Visualforce page in the current directory:

```
   sf template generate visualforce page --name mypage --label mylabel

```

Similar to previous example, but generate the files in the directory "force-app/main/default/pages":

```
   sf template generate visualforce page --name mypage --label mylabel --output-dir pages

```

Flags

```
   --json
```

Optional

Format output as json.

Type: boolean

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option

**`-n`** **|** **`--name NAME`**
Required

Name of the generated Visualforce Page.


### Salesforce CLI Command Reference ui-bundle Commands

The name can be up to 40 characters and must start with a letter.

Type: option

**`-d`** **|** **`--output-dir OUTPUT-DIR`**
Optional

Directory for saving the created files.

The location can be an absolute path or relative to the current working directory. The default is the current directory.

Type: option

Default value: .

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

**`-l`** **|** **`--label LABEL`**
Required

Visualforce Page label.

Type: option

Aliases for **`template generate visualforce page`**

```
   force:visualforce:page:create

   visualforce:generate:page

### ui-bundle Commands

```

Work with UI bundles

#### ui-bundle dev

Preview a UI bundle locally and in real-time, without deploying it to your org.

#### **`ui-bundle dev`**

Preview a UI bundle locally and in real-time, without deploying it to your org.

#### Description for ui-bundle dev

A UI bundle refers to an application that runs on Salesforce Platform that uses a non-native UI framework, such as React. Salesforce
provides native UI frameworks, such as Lighting Web Components (LWC), to build applications that run on the Salesforce Platform. But
you can also use non-native JavaScript- or TypeScript-based UI frameworks, such as React, to build a UI experience for the Salesforce
Platform and that you can launch from the App Launcher. UI bundles are defined by the UiBundle metadata type in your DX project.

This command starts a local development (dev) server so you can preview a UI bundle using the local metadata files in your DX project.
Using a local preview helps you quickly develop UI bundles, because you don't have to continually deploy metadata to your org.


Salesforce CLI Command Reference ui-bundle Commands

The command also launches a local proxy server that sits between your UI bundle and Salesforce, automatically injecting authentication
headers from Salesforce CLI's stored tokens. The proxy allows your UI bundle to make authenticated API calls to Salesforce without
exposing credentials.

Even though you're previewing the UI bundle locally and not deploying anything to an org, you're still required to authorize and specify
an org to use this command.

Examples for **`ui-bundle dev`**

Start the local development (dev) server by automatically discovering the UI bundle's ui-bundle.json file; use the org with alias "myorg":

```
   sf ui-bundle dev --target-org myorg

```

Start the dev server by explicitly specifying the UI bundle's name:

```
   sf ui-bundle dev --name myBundle --target-org myorg

```

Start at the specified dev server URL:

```
   sf ui-bundle dev --name myBundle --url http://localhost:5173 --target-org myorg

```

Start with a custom proxy port and automatically open the proxy server URL in your browser:

```
   sf ui-bundle dev --target-org myorg --port 4546 --open

```

Start with debug logging enabled by specifing the SF_LOG_LEVEL environment variable before running the command:

SF_LOG_LEVEL=debug sf ui-bundle dev --target-org myorg

Flags

```
   --json
```

Optional

Format output as json.

Type: boolean

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option

**`-n`** **|** **`--name NAME`**
Optional

Name of the UI bundle to preview.

The unique name of the UI bundle, as defined by the "name" property in the ui-bundle.json runtime configuration file. The
ui-bundle.json file is located in the "uiBundles" metadata directory of your DX project, such as
force-app/main/default/uiBundles/MyBundle/ui-bundle.json.

If you don't specify this flag, the command automatically discovers the ui-bundle.json files in the current directory and subdirectories.
If the command finds only one ui-bundle.json, it automatically uses it. If it finds multiple files, the command prompts you to select
one.

Type: option


### Salesforce CLI Command Reference Help for sf Commands

**`-u`** **|** **`--url URL`**
Optional

URL where your developer server runs, such as https://localhost:5173. All UI, static, and hot deployment requests are forwarded to
this URL.

You must specify this flag if the UI bundle's ui-bundle.json file doesn't contain a value for either the "dev.command" or "dev.url"
configuration properties. All non-Salesforce API requests are forwarded to this URL.

If you specify this flag, it overrides the value in the ui-bundle.json file.

This is the order of precedence that the dev server uses for the URL: --url flag > manifest dev.url > URL from the dev server process
(which was started using either manifest dev.command or default npm run dev).

Type: option

**`-p`** **|** **`--port PORT`**
Optional

Local port where the proxy server listens.

Be sure your browser connects to this port, and not directly to the dev server. The proxy then forwards authenticated requests to
Salesforce and other requests to your local dev server.

Type: option

**`-o`** **|** **`--target-org TARGET-ORG`**
Required

Username or alias of the target org. Not required if the `target-org` configuration variable is already set.

Type: option

**`-b`** **|** **`--open`**
Optional

Automatically open the proxy server URL in your default browser when the dev server is ready.

This flag saves you from manually copying and pasting the URL. The browser opens to the proxy URL, and not the dev server URL
directly, which ensures that all requests are property authenticated.

Type: boolean

### Help for sf Commands

The `-h` and `--help` flags show details about `sf` topics and their commands.

The short `-h` flag shows a subset of the command-line help and is meant for quick reference. The long `--help` flag shows the complete
command-line help.

The short help ( `-h` ) for commands has these parts.

**1. Short Description of Command**

At the top of the `-h` output (with no heading), a short description of the command is shown.

**2. Usage**

The command signature on the Usage line uses the docopt format.

**•** All available flags are listed. Flags that have short names are listed using their short names.

**•** Flags that take a value show `<value>` immediately after the flag’s name.

**•** Optional flags are in square brackets ( `[ … ]` ).


## Salesforce CLI Command Reference Salesforce Functions (Retired)

**•** Required flags have no annotation.

**•** For flags that accept a limited set of values, the values are shown after the flag name, separated by pipes ( `--flagname`
`value1|value2|value3` ).

**3. Flags**

The Flags section lists all the command’s flags, including their short name, long name, and purpose. Flags are grouped for easier
reading, such as global flags and other groups relevant to a specific command.

For flags that take multiple values, you have two ways to specify the values:

**•** Specify the flag multiple times, where each flag takes a different single value.

**•** Specify the flag one time, but separate all the values with a space.

For example, the following commands are equivalent:

```
     sf deploy metadata --metadata ApexClass --metadata CustomObject --metadata

     AnotherCustomObject

     sf deploy metadata --metadata ApexClass CustomObject AnotherCustomObject

```

Flags that accept a limited list of values include the values in parentheses, with the default value specified with the `default`
keyword.

The long help ( `--help` ) for commands has the same parts as the preceding short help `-h` ) and these additional parts.

**1. Description**

Usage notes.

**2. Examples**

All examples include a brief description.

**3. Flag Descriptions**

Some flags have optional additional usage notes.

## Salesforce Functions (Retired)

Salesforce Functions was retired on Jan 31, 2025. We removed the reference information for the Salesforce Functions CLI commands
from this guide on Feb 5, 2025.

[If you need reference information about the Salesforce Functions commands, see the Winter '25 Salesforce CLI Command Reference.](https://developer.salesforce.com/docs/atlas.en-us.252.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_functions_commands_unified.htm)

## sfdx (Deprecated) The sfdx -style commands are deprecated. We removed the reference information for them on June 12, 2024. As of April 2023, maintenance of sfdx (v7) has ended, and we no longer support it. We strongly discourage using sfdx (v7) due to the absence of any updates, bug fixes, or technical support. We urge you to transition to the latest version of Salesforce CLI, sf (v2), to

ensure compliance with current security standards and to benefit from ongoing enhancements. Failure to upgrade can result in
unresolvable issues.

## If you need reference information about the sfdx -style commands, see the Spring ‘24 Salesforce CLI Command Reference.


### Salesforce CLI Command Reference Migrate sfdx-Style Commands to Their sf-Style Equivalents Migrate sfdx-Style Commands to Their sf-Style Equivalents

We recommend that you start using the new `sf` commands in your continuous integration (CI) scripts and in your day-to-day work
as soon as possible. This section provides information on how to migrate. Migrating scripts are the focus, though this section also
applies to running impromptu commands at a terminal. The `sfdx` -style commands, such as `force:org:create`, continue
to work for now, although they’re deprecated.

### Migrate sfdx -Style Commands to Their sf -Style Equivalents

We recommend that you start using the new `sf` commands in your continuous integration (CI) scripts and in your day-to-day work as
soon as possible. This section provides information on how to migrate. Migrating scripts are the focus, though this section also applies
to running impromptu commands at a terminal. The `sfdx` -style commands, such as `force:org:create`, continue to work for
now, although they’re deprecated.

Follow these high-level steps to migrate.

**•** If you’re still using version 7 of the `sfdx` executable of Salesforce CLI (also referred to as `sfdx` (v7)), move to version 2 of the `sf`
executable ( `sf` (v2)) immediately. See Move from `[sfdx](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_setup.meta/sfdx_setup/sfdx_setup_move_to_sf_v2.htm)` (v7) to `sf` (v2) for details.

**•** Read an overview of the changes, including important usage differences.

**•** Run `dev convert script` to convert a large portion of your CI script.

**•** Manually update the remainder of your script.

Where is the Reference for **`sfdx`** -Style Commands?

We removed the reference information about `sfdx` -style commands from this guide on June 12, 2024. If you need the information,
[see the Spring ‘24 Salesforce CLI Command Reference.](https://developer.salesforce.com/docs/atlas.en-us.248.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference.htm)

Overview of Command and Usage Differences

The deprecated `sfdx` commands are different from the `sf` ones in these key ways. Other sections in this migration guide go into
details.

**•** Some commands and flags have new names, but their behavior and JSON output is the same as their `sfdx` equivalents. To migrate,
rename your existing commands and flags. For example, let’s say you have this command.

```
     force:apex:execute --targetusername <org> –--apexcodefile <file>

```

Here’s its `sf` -style equivalent.

```
     apex run --target-org <org> --file <file>

```

**•** For other `sfdx` -style commands, we created `sf` commands that likely behave differently, so migrating to them requires a bit more
effort. The inputs and JSON output for these new commands are also likely different from their `sfdx` equivalents. For example,
`force:org:create` is now two commands: `org create scratch` and `org create sandbox` .

In these cases the `sfdx` command is still available for backward compatibility.

**•** Configuration and environment variables have new names. For example, `targetusername` is now `target-org`, and
SFDX_DEFAULTUSERNAME is now SF_TARGET_ORG.

**•** We no longer use the `force` topic, except for a handful of commands that we kept for backward compatibility.

Read these usage differences between the `sfdx` -style and `sf` -style commands, and apply them when necessary.


Salesforce CLI Command Reference Migrate sfdx-Style Commands to Their sf-Style Equivalents

**•** When flags for new `sf` commands take multiple values, you specify the flag multiple times, with each flag taking a different single
value. For example:

```
     sf project deploy start --metadata ApexClass:SampleDataController --metadata

     ApexClass:PropertyController

```

Previously, with the deprecated `sfdx` -style commands, you specified the flag one time and separated the values with commas.
For example:

```
     sfdx force:source:deploy --metadata

     ApexClass:SampleDataController,ApexClass:PropertyController

```

You can continue using this comma-separated style with existing commands before you migrate. But when you migrate to the `sf`
commands, make sure that you use this new style because new and future commands don’t support the comma-separated style.
An example is specifying multiple Apex test classes and code coverage formats to the `project deploy start` command.
If you continue using commas, the command doesn’t return an error, but the Apex tests probably didn’t all run.

For example, use this syntax.

```
     sf project deploy start --metadata ApexClass --tests FirstTest --tests SecondTest --tests

      “Third Test” --coverage-formatters json --coverage-formatters html

```

But don’t use this syntax.

```
     sf project deploy start --metadata ApexClass --tests FirstTest,SecondTest,“Third Test”

      --coverage-formatters json,html

```

**•** The `sf` commands accept either spaces or colons between topics, commands, and subcommands. For example, both of these
command formats to get a configuration variable are valid.

```
     sf config get target-org

     sf config:get target-org

```

Run the **`dev convert script`** Command

Begin your migration by running the `dev convert script` command to update your CI scripts. The command replaces many
of the `sfdx` commands and flags with their `sf` equivalents.

Warning: We provide the `dev convert script` command to get you started with the migration. To ensure that they
work as expected, you must test the converted scripts thoroughly.

First, install the `plugin-dev` Salesforce CLI plugin, which contains the conversion command.

```
   sfdx plugins install @salesforce/plugin-dev

```

Then pass your script file to the `dev convert script` command with the `--script` flag.

```
   sfdx dev convert script --script ./myScript.yml

```

The command scans your script file, and each time it finds an `sfdx` command or flag, it prompts whether you want to replace it with
the new `sf` equivalent. The command overwrites your original file.

While `dev convert script` can convert a large portion of your script, it likely can’t convert all of it because there’s not always a
one-to-one mapping between the previous and new commands. In these cases, `dev convert script` doesn't replace the
`sfdx` -style command but instead adds a comment that starts with `#ERROR` .


Salesforce CLI Command Reference Migrate sfdx-Style Commands to Their sf-Style Equivalents

Migrate Scripts Manually

Because `dev convert script` typically can’t convert your entire script, you must migrate the remainder of the commands
manually. You can update your entire script manually if you want.

The easiest way to find the `sf` -style equivalent of a `sfdx` command is to read the `sfdx` [section of the Salesforce CLI Command](https://developer.salesforce.com/docs/atlas.en-us.248.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference.htm)
[Reference. Each deprecated](https://developer.salesforce.com/docs/atlas.en-us.248.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference.htm) `sfdx` command displays information about the new equivalent `sf` command and the new flag names.

You can also look at the deprecation warnings when you run an `sfdx` command. The warnings display the new `sf` -style equivalent
command and flag names. To display help information about the _new_ equivalent command along with examples, run the old command
with the `--help` flag.

Most commands are a simple one-to-one mapping, including flag name changes. Let’s take `auth:jwt:grant` as an example. The
[reference tells you to use the new](https://developer.salesforce.com/docs/atlas.en-us.248.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_auth_jwt.htm#cli_reference_auth_jwt_grant) `org login jwt` command instead, and it lists how the flag names have changed. Here’s an
example of the deprecated `sfdx` -style command.

```
   sfdx auth:jwt:grant --username jdoe@example.org --jwtkeyfile /Users/jdoe/JWT/server.key

   --clientid 123456 --setdefaultdevhubusername

```

Here’s the `sf` -style equivalent.

```
   sf org login jwt --username jdoe@example.org --jwt-key-file /Users/jdoe/JWT/server.key

   --client-id 123456 --set-default-dev-hub

```

The `force:apex` commands also have a one-to-one mapping to the new `sf` -style commands. Here’s an example of the
`[force:apex:test:run](https://developer.salesforce.com/docs/atlas.en-us.248.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_force_apex.htm#cli_reference_force_apex_test_run)` command.

```
   sfdx force:apex:test:run --suitenames "MySuite,MyOtherSuite" --codecoverage

   --detailedcoverage --targetusename my-scratch --outputdir tests/output"

```

Here’s the `sf` -style equivalent.

```
   sf apex run test --suite-names "MySuite,MyOtherSuite" --code-coverage --detailed-coverage

    --target-org my-scratch --output-dir tests/output"

```

Some commands aren’t a direct one-to-one mapping, or their behavior changed, so migrating them requires more effort. For additional
information about these commands, see these topics.

**•** force:source:* and force:mdapi:* Commands Migration

**•** force:org:* Commands Migration

**•** force:data:bulk:* Commands Migration

High-Level Overview of Common Flag Name Changes

This table provides an overview of common Salesforce CLI flag name changes.


Salesforce CLI Command Reference Migrate sfdx-Style Commands to Their sf-Style Equivalents

For less common flags, the `sf` -style name is often similar to the `sfdx` -style one, but it has dashes to make it easier to read. We also
standardized many of the flags across all topics and commands, such as using `--output-dir` consistently for the directory to write
the results of a command. Here are a few more examples.

**•** `project:create --outputdir` is now `project generate --output-dir` .

**•** `force:source:deploy --sourcepath` is now `project deploy start --source-dir` .

**•** `force:apex:class:create --classname` is now `apex generate class --name` .

**•** `force:package:create --errornotificationusername` is now `package create`
`--error-notification-username` .

As always, for command and flag name changes for a specific deprecated `sfdx` [command, see its reference page in the Salesforce CLI](https://developer.salesforce.com/docs/atlas.en-us.248.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference.htm)
[Command Reference.](https://developer.salesforce.com/docs/atlas.en-us.248.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference.htm)

#### force:source:* and force:mdapi:* Commands Migration Migrating the force:source:* and force:mdapi:* commands is straightforward in most cases, although some scenarios

require some rework.

force:org:* Commands Migration
Migrating the `force:org:*` commands is straight forward in most cases, although some scenarios require some rework.

force:data:bulk:* Commands Migration
We added four new `sf` commands that use Bulk API 2.0 to upsert and delete data to and from your org. All the `sfdx` commands
use Bulk API 1.0.

Configuration and Environment Variable Names Migration
Because the `dev convert script` conversion command doesn’t update configuration and environment variables to their
new names, we recommend that you update them manually to avoid deprecation warnings. Although the existing `sfdx` -style
variable names continue to work, we recommend that you start using the new `sf` -style ones. When you use the old ones, you get
a warning with the name of the new configuration and environment variable to use.

Source Tracking in New sf-Style Commands
Source tracking in the new `sf` -style commands works basically the same as in the `sfdx` -style commands, but with a few small
differences outlined in this topic.

Mapping sfdx Commands to Their sf Equivalents
This table maps the `sfdx` -style commands, such as `force:org:create`, to their closest `sf` -style equivalent, such as `org`
`create sandbox` or `org create scratch` . To help you migrate your continuous integration (CI) scripts to use the new
`sf` -style commands, each `sfdx` -style entry links to a command reference page that provides more information.

Mapping sf Commands to Their sfdx Equivalents
This table maps the core `sf` -style commands, such as `org create sandbox`, to their closest `sfdx` -style equivalent, such
as `force:org:create` .

#### force:source:* and force:mdapi:* Commands Migration Migrating the force:source:* and force:mdapi:* commands is straightforward in most cases, although some scenarios

require some rework.

Note: If you’re still using version 7 of the `sfdx` executable of Salesforce CLI (also referred to as `sfdx` (v7)), move to version 2
of the `sf` executable ( `sf` (v2)). See Move from `[sfdx](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_setup.meta/sfdx_setup/sfdx_setup_move_to_sf_v2.htm)` (v7) to `sf` (v2) for details.

We introduced two `sf` -style commands, `project deploy start` and `project retrieve start`, to replace these six
#### deprecated force commands.


Salesforce CLI Command Reference Migrate sfdx-Style Commands to Their sf-Style Equivalents

**•** `force:source:push`

**•** `force:source:pull`

**•** `force:source:deploy`

**•** `force:source:retrieve`

**•** `force:mdapi:deploy`

**•** `force:mdapi:retrieve`

It was often confusing to determine which `force` command to use because they all have similar functionality. For example, both
`force:source:push` and `force:source:deploy` move source format files from your project to the org. Now it’s simple:
use `project deploy start` to deploy metadata to your org and `project retrieve start` to retrieve metadata from
your org.

By default, both new commands work with files in source format. If you want to deploy or retrieve in metadata format, use the
`--metadata-dir` or `--target-metadata-dir` flags, respectively.

The `project deploy|retrieve start` commands support source tracking. However, because these two commands
encapsulate the functionality of the six `force` commands, source tracking works a bit differently. For more information, see Source
Tracking in New sf-Style Commands.

The table summarizes the mapping between the `force:source:*` and `force:mdapi:*` commands to their new `sf` -style
equivalents. The usage notes indicate if the mapping is a simple one-to-one. If it is, you migrate them by replacing their command and
flag names in your scripts. Some command migrations require changes beyond simple name replacements, or the functionality has
changed, as described in the usage notes. For more guidance, see the examples after the table.

For all command migrations, refer to the reference pages for each `force` command in the Salesforce CLI Command Reference for
details.

**•** `[force:source:*](https://developer.salesforce.com/docs/atlas.en-us.248.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_force_source.htm)`

**•** `[force:mdapi:*](https://developer.salesforce.com/docs/atlas.en-us.248.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_force_mdapi.htm)`


Salesforce CLI Command Reference Migrate sfdx-Style Commands to Their sf-Style Equivalents


Salesforce CLI Command Reference Migrate sfdx-Style Commands to Their sf-Style Equivalents


Salesforce CLI Command Reference Migrate sfdx-Style Commands to Their sf-Style Equivalents

A few examples can help you get started with these new commands.

Note: To differentiate the examples, we preface `sfdx` -style commands with `sfdx` and `sf` -style commands with `sf` . However,
you can indicate either `sf` or `sfdx` when running any CLI command.

**`force:source`** Examples

This `force` command converts source-formatted files into metadata format.

```
   sfdx force:source:convert --rootdir path/to/source --outputdir path/to/outputdir

   --packagename "My Package"

```

Here’s the `sf` -style equivalent.

```
   sf project convert source --root-dir path/to/source --output-dir path/to/outputdir

   --package-name 'My Package'

```

This `force` command deploys multiple metadata types.

```
   sfdx force:source:deploy --metadata "ApexClass,CustomObject" --testlevel RunSpecifiedTests

    --runtests MyTests --targetusername my-scratch

```

Here’s the `sf` -style equivalent in which the `--metadata` flag is specified multiple times.

```
   sf project deploy start --metadata ApexClass --metadata CustomObject --test-level

   RunSpecifiedTests --tests MyTests --target-org my-scratch

```

This `force` command pushes (deploys) all the changes in your project to an org.

```
   sfdx force:source:push --targetusername myscratch --forceoverwrite --wait 10

```

Here’s the `sf` -style equivalent.

```
   sf project deploy start --target-org myscratch --ignore-conflicts --wait 10

```

This `force` command retrieves the source in the specified directories.

```
   sfdx force:source:retrieve --sourcepath

   "path/to/objects/MyCustomObject/fields/MyField.field-meta.xml, path/to/apex/classes"

```


Salesforce CLI Command Reference Migrate sfdx-Style Commands to Their sf-Style Equivalents

Here’s the `sf` -style equivalent in which the `--source-dir` flag is specified multiple times.

```
   sf project retrieve start --source-dir

   path/to/objects/MyCustomObject/fields/MyField.field-meta.xml --source-dir

   path/to/apex/classes

```

This `force` command opens a metadata file in Lightning App Builder.

```
   sfdx force:source:open --source-file

   force-app/main/default/flexipages/Hello.flexipage-meta.xml --urlonly --targetusername

   myscratch

```

Here’s the `sf` -style equivalent that uses the `org open` command.

```
   sf org open --source-path force-app/main/default/flexipages/Hello.flexipage-meta.xml

   --url-only --target-org myscratch

```

This `force` command pulls (retrieves) all the changes in your org to your project.

```
   sfdx force:source:pull --targetusername myscratch --forceoverwrite --wait 10

```

Here’s the `sf` -style equivalent.

```
   sf project retrieve start --target-org myscratch --ignore-conflicts --wait 10

```

This `force` command shows how your local project differs from the org.

```
   sfdx force:source:status --targetusername myscratch --local

```

Here’s the `sf` -style equivalent; the command requires that you specify what you want preview, in this case, with the `--manifest`
flag.

```
   sf project deploy preview --target-org myscratch --manifest package.xml

```

**`force:mdapi`** Examples

This `force` command deploys metadata format files in the specified directory.

```
   sfdx force:mdapi:deploy --deploydir some/path --wait 1000 --checkonly --testlevel

   RunAllTestsInOrg --targetusername my-test-org

```

There are two `sf` -style equivalents.

```
   sf project deploy start --dry-run --metadata-dir some/path --wait 1000 --test-level

   RunAllTestsInOrg --target-org my-test-org

   sf project deploy validate --metadata-dir some/path --wait 1000 --test-level RunAllTestsInOrg

    --target-org my-test-org

```

This `force` command deploys a .zip file that contains metadata files.

```
   sfdx force:mdapi:deploy sfdx force:mdapi:deploy --zipfile stuff.zip --resultsdir --junit

```

Here’s the `sf` -style equivalent.

```
   sf project deploy start --metadata-dir stuff.zip --results-dir --junit

```

This `force` command retrieves metadata defined in a manifest file into the target directory.

```
   sfdx force:mdapi:retrieve --retrievetargetdir path/to/retrieve/dir --unpackaged package.xml

```


Salesforce CLI Command Reference Migrate sfdx-Style Commands to Their sf-Style Equivalents

Here’s the `sf` -style equivalent.

```
   sf project retrieve start --target-metadata-dir path/to/retrieve/dir --manifest package.xml

```

Overview of New Commands and Functionality

In addition to the new `project deploy start` and `project retrieve start`, we introduced other commands and
flags that improve the Salesforce CLI’s usability.

**•** Preview a deployment to your org with the `project deploy preview` command.

The command outputs a table that shows what happens when you run the `project deploy start` command. The table
displays a preview of the metadata components that are deployed and deleted, and the current conflicts between your project and
org. The table also lists the files that aren’t deployed because they’re included in your `.forceignore` file.

**•** Similarly, preview a retrieve from your org with the `project retrieve preview` command.

**•** Validate a deployment, and then quickly deploy it later, with the `project deploy validate` and `project deploy`
`quick` command pair.

Use `project deploy validate` to verify whether a deployment can succeed without actually deploying the metadata to
your org. This command is similar to `project deploy start`, except that you’re required to run Apex tests, and the command
returns a job ID rather than actually executing the deployment. If the validation succeeds, then you pass this job ID to the `project`
`deploy quick` command to actually deploy the metadata. This type of deploy takes less time because it skips running Apex
tests.

You can also use the `--dry-run` flag of `project deploy start` to get a preview of a deploy. Use this preview method
if you don’t plan to later do a quick deploy. This way of previewing provides more flexibility because you can use all the flags of the
`project deploy start` command, such as making destructive changes with the
`--pre|post-destructive-changes` flags. The `project deploy validate` provides just a subset of the full
deployment flags.

**•** These new deploy commands that take a job ID now also have the handy `--use-most-recent` flag to automatically use the
job ID of the most recent deploy operation.

**–** `project deploy cancel`

**–** `project deploy quick`

**–** `project deploy report`

**–** `project deploy resume`

**•** These new deploy commands have the `--async` flag to run the command asynchronously.

**–** `project deploy cancel`

**–** `project deploy quick`

**–** `project deploy resume`

**–** `project deploy validate`

**•** Delete source from a non-source-tracked org with the `project delete source` command.

#### force:org:* Commands Migration Migrating the force:org:* commands is straight forward in most cases, although some scenarios require some rework.


Salesforce CLI Command Reference Migrate sfdx-Style Commands to Their sf-Style Equivalents

Note: If you’re still using version 7 of the `sfdx` executable of Salesforce CLI (also referred to as `sfdx` (v7)), move to version 2
of the `sf` executable ( `sf` (v2)). See Move from `[sfdx](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_setup.meta/sfdx_setup/sfdx_setup_move_to_sf_v2.htm)` (v7) to `sf` (v2) for details.

This table summarizes the mapping between the existing `force:org:*` commands and their new `sf` -style equivalents. The usage
notes indicate if the mapping is one-to-one. If it is, you migrate them by changing their command and flag names as listed in the
[reference page for each](https://developer.salesforce.com/docs/atlas.en-us.248.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_force_org.htm) `force:org:*` command. Some command migrations require more changes, as described in the usage
notes. For more guidance, see the examples after the table.


Salesforce CLI Command Reference Migrate sfdx-Style Commands to Their sf-Style Equivalents

We also introduced the command `org resume scratch` to resume a scratch org creation if it times out. Previously, you could
no longer connect to it, and you manually deleted it from your Dev Hub org. Now you can resume where it left off using a job ID or the
`--use-most-recent` flag. When the org creation finishes, the command automatically authenticates to the org, saves the org info
locally, and deploys any configured settings.

A few examples can help you get started with these new commands.

Note: To differentiate the examples, we preface `sfdx` -style commands with `sfdx` and `sf` -style commands with `sf` . However,
you can indicate either `sf` or `sfdx` when running any CLI command.

Let’s start with the deprecated `force:org:create` [command. The reference tells you to use either](https://developer.salesforce.com/docs/atlas.en-us.248.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_force_org.htm#cli_reference_force_org_create) `org create sandbox`
or `org create scratch`, depending on what you want to create. Let’s say you want to migrate this `force` command.

```
   sfdx force:org:create --definitionfile config/scratch-def.json --setalias MyScratchOrg

   --targetdevhubusername MyDevHub --nonamespace --setdefaultusername

```

Because the command creates a scratch org, use this equivalent `sf` command.

```
   sf org create scratch --definition-file config/scratch-def.json --alias MyScratchOrg

   --target-dev-hub MyDevHub --no-namespace --set-default

```

This `force` example specifies scratch org options as key-value pairs at the command line, which is no longer allowed.

```
   sfdx force:org:create adminEmail=me@email.com edition=Developer

   username=admin_user@orgname.org --country=GB --targetdevhubusername MyDevHub

```

In the `sf` -style equivalent, use the `--edition`, `--admin-email`, and `--username` flags instead. But because `country`
doesn’t have an equivalent flag, you must specify a scratch org definition file that contains the `country` option. Here’s what the new
command looks like.

```
   sf force:org:create --definition-file config/scratch-def.json --admin-email me@email.com

   --edition=developer --username=admin_user@orgname.org --targetdevhubusername MyDevHub

```

In the previous example, the `--edition` flag takes lowercase values for Salesforce editions. To see the full list of valid editions, run
`org create scratch -h` .

Here’s an example of a scratch org definition file that contains the `country` option.

```
   {

      "orgName": "Dreamhouse",

      "edition": "Developer",

      "country": "GB",

      "features": ["Walkthroughs", "EnableSetPasswordInApi"],

      "settings": {

        "lightningExperienceSettings": {

           "enableS1DesktopEnabled": true

        },

        "mobileSettings": {

           "enableS1EncryptedStoragePref2": false

        }

      }

   }

```

This `force` example creates a sandbox.

```
   sfdx force:org:create --type sandbox --definitionfile config/dev-sandbox-def.json --setalias

    MyDevSandbox --targetusername ProdOrg

```


Salesforce CLI Command Reference Migrate sfdx-Style Commands to Their sf-Style Equivalents

Here’s the equivalent `sf` -style command.

```
   sf org create sandbox --definition-file config/dev-sandbox-def.json --alias MyDevSandbox

   --target-org ProdOrg

#### This force example clones a sandbox by specifying the SourceSandboxName and SandboxName key-value pairs at the
```

command line.

```
   sfdx force:org:clone --type sandbox SourceSandboxName=ExistingSandbox

   SandboxName=NewClonedSandbox --setalias MyDevSandbox --targetusername ProdOrg

```

In the `sf` -style command, use flags instead.

```
   sf org create sandbox --clone ExistingSandbox --name NewClonedSandbox --alias MyDevSandbox

    --target-org ProdOrg

#### This force example deletes a scratch org.

   sfdx force:org:delete --targetusername MyScratchOrg --noprompt

```

Here’s the equivalent `sf` -style command.

```
   sf org delete scratch --target-org MyScratchOrg --no-prompt

#### force:data:bulk:* Commands Migration

```

We added four new `sf` commands that use Bulk API 2.0 to upsert and delete data to and from your org. All the `sfdx` commands use
Bulk API 1.0.

Note: If you’re still using version 7 of the `sfdx` executable of Salesforce CLI (also referred to as `sfdx` (v7)), move to version 2
of the `sf` executable ( `sf` (v2)). See Move from `[sfdx](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_setup.meta/sfdx_setup/sfdx_setup_move_to_sf_v2.htm)` (v7) to `sf` (v2) for details.

These new `sf` commands use Bulk API 2.0.

**•** `data delete bulk`

**•** `data delete resume`

**•** `data upsert bulk`

**•** `data upsert resume`

We generally recommend that you start using the new `sf` commands instead of these equivalent `sfdx` commands that use Bulk API
1.0.

**•** `force:data:bulk:delete`

**•** `force:data:bulk:upsert`

**•** `force:data:bulk:status`

However, one reason to keep using the `force:data:bulk:upsert` command is if you want to run the upsert serially with
the `--serial` flag. The new Bulk API 2.0 commands don’t support serial execution. For this reason, and for users who want to continue
#### using Bulk API 1.0, we aren’t deprecating the force:data:bulk:* commands at this time.


Salesforce CLI Command Reference Migrate sfdx-Style Commands to Their sf-Style Equivalents

#### Configuration and Environment Variable Names Migration

Because the `dev convert script` conversion command doesn’t update configuration and environment variables to their new
names, we recommend that you update them manually to avoid deprecation warnings. Although the existing `sfdx` -style variable
names continue to work, we recommend that you start using the new `sf` -style ones. When you use the old ones, you get a warning
with the name of the new configuration and environment variable to use.

Note: If you’re still using version 7 of the `sfdx` executable of Salesforce CLI (also referred to as `sfdx` (v7)), move to version 2
of the `sf` executable ( `sf` (v2)). See Move from `[sfdx](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_setup.meta/sfdx_setup/sfdx_setup_move_to_sf_v2.htm)` (v7) to `sf` (v2) for details.

Configuration Variables

The `sfdx` -style configuration variables are aliased to their `sf` -style equivalents. As a result, you can use either the `sfdx` or the `sf`
variable names with the `config` commands. But the commands always work on the `sf` variable names. For example, `config`
`set` and `config unset` always set the configuration with the `sf` name, even if you specify the `sfdx` name. All `config`
commands display the `sf` name in their outputs, even if you specified the `sfdx` name in the command.

These examples show the rules in action.

```
   sf config set defaultusername=my-scratch-org

   Warning: Deprecated config name: defaultusername. Please use target-org instead.

   Set Config

   ===================================

   | Name Value Success

   | ───────────────────────────────

   | target-org my-scratch-org true

   sf config list

   List Config

   ===========================================

   | Name Value Location

   | ───────────────────────────────────────

   | target-org my-scratch-org Local

   sf config get defaultusername

   Warning: Deprecated config name: defaultusername. Please use target-org instead.

   Get Config

   ===================================

   | Name Value Success

   | ───────────────────────────────

   | target-org my-scratch-org true

```

Use this table to migrate your scripts to use the new `sf` -style configuration variable names.


Salesforce CLI Command Reference Migrate sfdx-Style Commands to Their sf-Style Equivalents

Environment Variables

You can set both the new `sf` -style and old `sfdx` -style environment variables. However, if they’re set to different values, Salesforce CLI
uses the `sf` one and displays a warning.

To migrate most environment variables, change the initial SFDX to SF. However, some variables have bigger changes, as displayed in
[this table, while others haven’t changed their name. For the full list, see Salesforce CLI Environment Variables.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_setup.meta/sfdx_setup/sfdx_dev_cli_env_variables.htm)

**Equivalent** `sf` **-style Environment Variable** **Equivalent** `sf` **-style Environment Variable**

SFDX_API_VERSION SF_ORG_API_VERSION

SFDX_CUSTOM_ORG_METADATA_TEMPLATES SF_ORG_CUSTOM_METADATA_TEMPLATES

SFDX_DEFAULTDEVHUBUSERNAME SF_TARGET_DEV_HUB

SFDX_DEFAULTUSERNAME SF_TARGET_ORG

SFDX_INSTANCE_URL SF_ORG_INSTANCE_URL

SFDX_MAX_QUERY_LIMIT SF_ORG_MAX_QUERY_LIMIT

SFDX_REST_DEPLOY SF_ORG_METADATA_REST_DEPLOY

For example, here’s how to set your default Dev Hub org to an alias with an environment variable before running the command to create
a scratch org.

```
   SF_TARGET_DEV_HUB=MyDevHub sf org create scratch --definition-file config/scratch-def.json

#### Source Tracking in New sf -Style Commands

```

Source tracking in the new `sf` -style commands works basically the same as in the `sfdx` -style commands, but with a few small
differences outlined in this topic.

Note: If you’re still using version 7 of the `sfdx` executable of Salesforce CLI (also referred to as `sfdx` (v7)), move to version 2
of the `sf` executable ( `sf` (v2)). See Move from `[sfdx](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_setup.meta/sfdx_setup/sfdx_setup_move_to_sf_v2.htm)` (v7) to `sf` (v2) for details.

These `sf` -style commands support source tracking.

**•** `project deploy start`

**•** `project delete source`

**•** `project retrieve start`

The `sf` -style commands encapsulate the functionality of these six deprecated `sfdx` -style commands.

**•** `force:source:push`


Salesforce CLI Command Reference Migrate sfdx-Style Commands to Their sf-Style Equivalents

**•** `force:source:pull`

**•** `force:source:deploy`

**•** `force:source:retrieve`

**•** `force:mdapi:deploy`

**•** `force:mdapi:retrieve`

Let’s start with deploying. The first time you run `project deploy start` on a scratch or sandbox org that allows source tracking,
the command deploys all the source files from your local project. But when you next run the command, it deploys only the files that
changed locally. If you use one of the flags to narrow the deploy list, `--source-dir`, `--metadata`, or `--manifest`, then the
command deploys only the changed files in the specified directory, metadata, or manifest. If you don’t specify any of the flags, then the
command deploys all changes in the project, similar to how the `sfdx` -style command `force:source:push` works.

If you run `project retrieve start` on a newly created org, nothing happens because there are no changes to track yet. When
you next run the command, any changes in the org are retrieved. These changes include updates from other users who connect to the
org, not just your changes. If you don’t specify `--source-dir`, `--metadata`, or `--manifest`, then all changes in the org are
retrieved, just like the `sfdx` -style command `force:source:pull` .

If one of these commands detects a conflict in the files you’re about to deploy or retrieve, the command displays the conflicts. To force
the deployment or retrieval of the changes, use the `--ignore-conflicts` flag. This flag is similar to the `--forceoverwrite`
flag of many of the `force:source` commands. For example:

```
   sf project deploy start --source-dir force-app --ignore-conflicts

```

Determine If Your Org Allows Source Tracking

Source tracking works only if your target org allows it. Don’t worry, you can still deploy or retrieve metadata to and from an org without
source tracking. But the commands don’t check for conflicts, and you must specify what you want to deploy or retrieve using an
appropriate flag, such as `--source-dir` .

Here’s how to determine whether your org allows source tracking.

**•** For Developer Edition orgs, production orgs, Partial Copy sandboxes, and Full sandboxes, source tracking isn’t available.

**•** For Developer and Developer Pro sandboxes:

**–** Source tracking is enabled if their associated production org has been enabled for source tracking.

**–** Source tracking is possible when you create the sandbox with the `--no-track-source` flag of the `org create`
`sandbox` command. For example:

```
       sf org create sandbox --definition-file config/dev-sandbox-def.json --target-org

       prodOrg --no-track-source

```

**•** Scratch orgs have source tracking by default.

**–** You can opt out of source tracking when you create the scratch org with the `--no-track-source` flag of the `org`
`create scratch` command. This flag affects only your local configuration, not the scratch org itself. Salesforce CLI sets a
local configuration option `trackSource: false` as part of your authorization information to the org. If you log out of the
scratch org and then log back in again, source tracking is enabled again by default. Here’s how to create a scratch org with source
tracking disabled.

```
       sf org create scratch --target-dev-hub=MyHub --definition-file

       config/project-scratch-def.json --no-track-source

```


Salesforce CLI Command Reference Migrate sfdx-Style Commands to Their sf-Style Equivalents

Tip: You can use the `[org disable tracking](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_org_commands_unified.htm#cli_reference_org_disable_tracking_unified)` or `[org enable tracking](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_org_commands_unified.htm#cli_reference_org_enable_tracking_unified)` commands to disable or enable source
tracking on an existing org.

SEE ALSO:

_Salesforce DX Developer Guide_ [: Track Changes Between Your Project and Org](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_source_tracking.htm)

#### Mapping sfdx Commands to Their sf Equivalents

This table maps the `sfdx` -style commands, such as `force:org:create`, to their closest `sf` -style equivalent, such as `org`
`create sandbox` or `org create scratch` . To help you migrate your continuous integration (CI) scripts to use the new
`sf` -style commands, each `sfdx` -style entry links to a command reference page that provides more information.

Note: If you’re still using version 7 of the `sfdx` executable of Salesforce CLI (also referred to as `sfdx` (v7)), move to version 2
of the `sf` executable ( `sf` (v2)). See Move from `[sfdx](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_setup.meta/sfdx_setup/sfdx_setup_move_to_sf_v2.htm)` (v7) to `sf` (v2) for details.


Salesforce CLI Command Reference Migrate sfdx-Style Commands to Their sf-Style Equivalents


Salesforce CLI Command Reference Migrate sfdx-Style Commands to Their sf-Style Equivalents


Salesforce CLI Command Reference Migrate sfdx-Style Commands to Their sf-Style Equivalents


Salesforce CLI Command Reference Migrate sfdx-Style Commands to Their sf-Style Equivalents


Salesforce CLI Command Reference Migrate sfdx-Style Commands to Their sf-Style Equivalents

#### Mapping sf Commands to Their sfdx Equivalents

This table maps the core `sf` -style commands, such as `org create sandbox`, to their closest `sfdx` -style equivalent, such as
`force:org:create` .

Note: If you’re still using version 7 of the `sfdx` executable of Salesforce CLI (also referred to as `sfdx` (v7)), move to version 2
of the `sf` executable ( `sf` (v2)). See Move from `[sfdx](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_setup.meta/sfdx_setup/sfdx_setup_move_to_sf_v2.htm)` (v7) to `sf` (v2) for details.


Salesforce CLI Command Reference Migrate sfdx-Style Commands to Their sf-Style Equivalents


Salesforce CLI Command Reference Migrate sfdx-Style Commands to Their sf-Style Equivalents


Salesforce CLI Command Reference Migrate sfdx-Style Commands to Their sf-Style Equivalents


## Salesforce CLI Command Reference CLI Deprecation Policy CLI Deprecation Policy

Salesforce deprecates CLI commands and flags when, for example, the underlying API changes.

The Salesforce CLI deprecation policy is:

**•** Salesforce announces new and upcoming deprecations of commands and flags in the weekly Salesforce CLI release notes.

**•** Salesforce can deprecate a command or flag at any time.

**•** When you run the deprecated command, Salesforce provides a deprecation warning for a minimum of 4 months.

**•** Salesforce removes the deprecated command or flag 4 months, or more, after the deprecation warning first appears.

**•** If you use a command or flag that’s been deprecated but not yet removed, you get a warning message in `stderr` in the
human-readable output. If you specify JSON output, the warning is presented as a property. The message includes the plugin version
in which we plan to remove the command or flag. The command help also includes deprecation information when appropriate.

**•** When possible, Salesforce provides a functional alternative to the deprecated command or flag.


## Salesforce CLI Command Reference Discover Salesforce Plugins

**•** [For our policy on changes to a Salesforce CLI command’s JSON response, see Support for JSON Responses.](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_setup.meta/sfdx_setup/sfdx_dev_cli_json_support.htm)

## Discover Salesforce Plugins

Check out these other plugins that work with specific Salesforce features. These plugins are created by Salesforce.

**CRM Analytics Plugin**

CRM Analytics is a cloud-based platform for connecting data from multiple sources, creating interactive views of that data, and
sharing those views in apps.

Use the CRM Analytics CLI plugin to create scratch orgs with Analytics Studio, which you can use to develop and test source code.
The plugin includes commands that call a subset of the Analytics REST API endpoints to manage CRM Analytics assets programmatically.
Create and iteratively develop CRM Analytics templates. Update and delete apps, dashboards, lenses, and dataflows. Use history
commands to restore previous versions of dashboards and dataflows. Manage the auto-install lifecycle for embedded templated
apps.

[See Develop with the Analytics Plugin for the Salesforce CLI for documentation and more information.](https://help.salesforce.com/articleView?id=analytics.bi_dev_tools_cli_analytics_plugin.htm&type=5&language=en_US)

**Salesforce Code Analyzer Plugin**

The Salesforce Code Analyzer plugin is a unified tool for static analysis of source code, in multiple languages (including Apex), with
a consistent command-line interface and report output. The plugin supports multiple third-party engines, such as PMD, CPD, ESLint,
and RetireJS. The plugin also supports Salesforce engines, such as Flow Scanner and Regex.

The plugin creates "rule violations" when the scanner identifies issues. Developers use this information as feedback to fix their code.
Integrate this plugin into your continuous integration (CI) solution to continually enforce the rules and ensure high-quality code.

[See Salesforce Code Analyzer for documentation and more information.](https://developer.salesforce.com/docs/platform/salesforce-code-analyzer/overview)

