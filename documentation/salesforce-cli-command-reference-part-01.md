# Salesforce CLI Command Reference

> Source: https://resources.docs.salesforce.com/latest/latest/en-us/sfdc/pdf/sfdx_cli_reference.pdf
> Fetched: 2026-06-02T08:10:56Z
Salesforce CLI Command
Reference

Salesforce, Summer ’26

Last updated: May 28, 2026

© Copyright 2000–2026 Salesforce, Inc. All rights reserved. Salesforce is a registered trademark of Salesforce, Inc., as are other
names and marks. Other marks appearing herein may be trademarks of their respective owners.

CONTENTS

**SALESFORCE CLI COMMAND REFERENCE . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1**

Release Notes **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1**
sf **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1**
Salesforce Functions (Retired) **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 332**
sfdx (Deprecated) **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 332**
CLI Deprecation Policy **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 358**
Discover Salesforce Plugins **. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 359**

SALESFORCE CLI COMMAND REFERENCE

This command reference contains information about the Salesforce CLI commands and their flags.

Salesforce CLI Release Notes
Use the Release Notes to learn about the most recent updates and changes to Salesforce CLI.

## sf

Commands to manage Salesforce DX projects, create and manage scratch orgs and sandboxes, synchronize source to and from
orgs, create and install packages, and more.

Salesforce Functions (Retired)
Salesforce Functions was retired on Jan 31, 2025. We removed the reference information for the Salesforce Functions CLI commands
from this guide on Feb 5, 2025.

## sfdx (Deprecated) The sfdx -style commands are deprecated. We removed the reference information for them on June 12, 2024.

CLI Deprecation Policy
Salesforce deprecates CLI commands and flags when, for example, the underlying API changes.

Discover Salesforce Plugins
Check out these other plugins that work with specific Salesforce features. These plugins are created by Salesforce.

Salesforce CLI Release Notes

Use the Release Notes to learn about the most recent updates and changes to Salesforce CLI.

[We release new versions of Salesforce CLI weekly. Read the weekly release notes to learn about new features, changes, and bug fixes in](https://github.com/forcedotcom/cli/blob/main/releasenotes/README.md)
both the current release and the release candidate.

## sf

Commands to manage Salesforce DX projects, create and manage scratch orgs and sandboxes, synchronize source to and from orgs,
create and install packages, and more.

## This version of the sf command reference includes details about version 2.137.6 of the sf executable of Salesforce CLI and the

following plug-in versions:

**•** `@salesforce/plugin-deploy-retrieve` version 3.24.50

**•** `@salesforce/plugin-settings` version 2.4.82

**•** `@salesforce/plugin-info` version 3.4.136

**•** `@salesforce/plugin-sobject` version 1.4.110

**•** `@salesforce/plugin-limits` version 3.3.91

**•** `@salesforce/plugin-schema` version 3.3.115

**•** `@salesforce/plugin-custom-metadata` version 3.3.104


Salesforce CLI Command Reference sf

**•** `@salesforce/plugin-data` version 4.0.103

**•** `@salesforce/plugin-community` version 3.3.63

**•** `@salesforce/plugin-signups` version 2.6.71

**•** `@salesforce/plugin-user` version 3.10.1

**•** `@salesforce/plugin-org` version 5.11.4

**•** `@salesforce/plugin-packaging` version 2.28.3

**•** `@salesforce/plugin-templates` version 56.17.4

**•** `@salesforce/plugin-apex` version 3.9.31

**•** `@salesforce/plugin-auth` version 4.4.1

**•** `@salesforce/plugin-dev` version 2.5.2

**•** `@salesforce/sfdx-plugin-lwc-test` version 1.2.1

**•** `@salesforce/plugin-devops-center` version 1.2.27

**•** `@salesforce/plugin-marketplace` version 1.3.28

**•** `@salesforce/plugin-code-analyzer` version 5.13.0

**•** `@salesforce/plugin-api` version 1.3.36

**•** `@salesforce/plugin-agent` version 1.40.5

**•** `@salesforce/plugin-flow` version 1.0.5

**•** `@salesforce/plugin-lightning-dev` version 6.2.17

**•** `@salesforce/plugin-ui-bundle-dev` version 1.2.2

For information about installing Salesforce CLI, see the _[Salesforce CLI Setup Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_setup.meta/sfdx_setup/sfdx_setup_install_cli.htm)_ .

For information about Salesforce CLI changes, see the _[Salesforce CLI Release Notes](https://github.com/forcedotcom/cli/blob/main/releasenotes/README.md)_ .

agent Commands
Commands to work with agents.

alias Commands
Use the alias commands to manage your aliases.

apex Commands
Use the apex commands to create Apex classes, execute anonymous blocks, view your logs, run Apex tests, and view Apex test
results.

api Commands
Commands to interact with API calls.

cmdt Commands
Generate custom metadata types and their records.

code-analyzer Commands
Analyze your code to ensure it adheres to best practices.

community Commands
Create and publish an Experience Cloud site.

config Commands
Commands to configure Salesforce CLI.


### Salesforce CLI Command Reference agent Commands

data Commands
Manage records in your org.

dev Commands
Commands for sf plugin development.

doctor Commands
Tools for diagnosing problems with Salesforce CLI.

flow Commands
Commands for testing flows

force Commands
Legacy commands for backward compatibility.

info Commands
Access Salesforce CLI information from the command line.

lightning Commands
Commands to work with Lightning applications.

logic Commands
Use the logic commands to run Apex and Flow tests and view the test results.

org Commands
Commands to create and manage orgs and scratch org users.

package Commands
Commands to develop and install unlocked packages and managed 2GP packages.

package1 Commands
Commands to develop first-generation managed and unmanaged packages.

plugins Commands
Find and manage plugins

project Commands
Work with projects, such as deploy and retrieve metadata.

schema Commands
Generate metadata files.

sobject Commands
Commands to interact with Salesforce objects.

template Commands
Collection of Salesforce templates.

ui-bundle Commands
Work with UI bundles

Help for sf Commands
The `-h` and `--help` flags show details about `sf` topics and their commands.

### agent Commands

Commands to work with agents.


Salesforce CLI Command Reference agent Commands

agent activate
Activate an agent in an org.

agent create
Create an agent in your org using a local agent spec file.

agent deactivate
Deactivate an agent in an org.

agent generate agent-spec
Generate an agent spec, which is a YAML file that captures what an agent can do.

agent generate authoring-bundle
Generate an authoring bundle from an existing agent spec YAML file.

agent generate template
Generate an agent template from an existing agent in your DX project so you can then package the template in a second-generation
managed package.

agent generate test-spec
Generate an agent test spec, which is a YAML file that lists the test cases for testing a specific agent.

agent preview
Interact with an agent to preview how it responds to your statements, questions, and commands (utterances).

agent preview end
End an existing programmatic agent preview session and get trace location.

agent preview send
Send a message to an existing agent preview session.

agent preview sessions
List all known programmatic agent preview sessions.

agent preview start
Start a programmatic agent preview session.

agent publish authoring-bundle
Publish an authoring bundle to your org, which results in a new agent or a new version of an existing agent.

agent test create
Create an agent test in your org using a local test spec YAML file.

agent test list
List the available agent tests in your org.

agent test results
Get the results of a completed agent test run.

agent test resume
Resume an agent test that you previously started in your org so you can view the test results.

agent test run
Start an agent test in your org.

agent test run-eval (Beta)
Run rich evaluation tests against an Agentforce agent.

agent trace delete
Delete trace files from an agent preview session.


Salesforce CLI Command Reference agent Commands

agent trace list
List the available trace files that were recorded during all agent preview sessions.

agent trace read
Read trace files from an agent preview session.

agent validate authoring-bundle
Validate an authoring bundle to ensure its Agent Script file compiles successfully and can be used to publish an agent.

#### **`agent activate`**

Activate an agent in an org.

#### Description for agent activate

Activating an agent makes it immediately available to your users. A published agent must be active before you can preview it with the
"agent preview" CLI command or VS Code. Agents can have multiple versions; only one version can be active at a time.

If you run the command without the --api-name or --version flags, the command provides a list of agent API names and versions for
you to choose from. Use the flags to specify the exact agent and version without being prompted. If you use the --json flag and not
--version, then the latest agent version is automatically activated.

The value of the --version flag is always a number, corresponding to the "vX" part of the "BotVersion" metadata in your project. For
example, if you have a force-app/main/default/bots/My_Agent/v4.botVersion-meta.xml file in your project, then you activate this version
with the "--version 4" flag.

#### Examples for agent activate

Activate an agent in your default target org by being prompted for both its API name and version:

```
   sf agent activate

```

Activate version 2 of an agent with API name Resort_Manager in the org with alias "my-org":

```
   sf agent activate --api-name Resort_Manager --version 2 --target-org my-org

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


Salesforce CLI Command Reference agent Commands

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

**`-n`** **|** **`--api-name API-NAME`**
Optional

API name of the agent to activate; if not specified, the command provides a list that you choose from.

Type: option

```
   --version VERSION
```

Optional

Version number of the agent to activate; if not specified, the command provides a list that you choose from.

Type: option

#### **`agent create`**

Create an agent in your org using a local agent spec file.

#### Description for agent create

NOTE: This command creates an agent that doesn't use Agent Script as its blueprint. We generally don't recommend you use this
workflow to create an agent. Rather, use the "agent generate|validate|publish authoring-bundle" commands to author agents that use
the Agent Script language. See "Author an Agent"
(https://developer.salesforce.com/docs/einstein/genai/guide/agent-dx-nga-author-agent.html) for details.

To run this command, you must have an agent spec file, which is a YAML file that define the agent properties and contains a list of
AI-generated topics. Topics define the range of jobs the agent can handle. Use the "agent generate agent-spec" CLI command to generate
an agent spec file. Then specify the file to this command using the --spec flag, along with the name (label) of the new agent with the
--name flag. If you don't specify any of the required flags, the command prompts you.

When this command completes, your org contains the new agent, which you can then edit and customize in the Agent Builder UI. The
new agent's topics are the same as the ones listed in the agent spec file. The agent might also have some AI-generated actions, or you
can add them. This command also retrieves all the metadata files associated with the new agent to your local Salesforce DX project.

Use the --preview flag to review what the agent looks like without actually saving it in your org. When previewing, the command creates
a JSON file in the current directory with all the agent details. The name of the JSON file is the agent's API name and a timestamp.

To open the new agent in your org's Agent Builder UI, run this command: "sf org open agent --api-name <api-name>".

#### Examples for agent create

Create an agent by being prompted for the required information, such as the agent spec file and agent name, and then create it in your
default org:

```
   sf agent create

```

Create an agent by specifying the agent name, API name, and spec file with flags; use the org with alias "my-org"; the command fails if
the API name is already being used in your org:

```
   sf agent create --name "Resort Manager" --api-name Resort_Manager --spec

   specs/resortManagerAgent.yaml --target-org my-org

```


Salesforce CLI Command Reference agent Commands

Preview the creation of an agent named "Resort Manager" and use your default org:

```
   sf agent create --name "Resort Manager" --spec specs/resortManagerAgent.yaml --preview

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

```
   --name NAME
```

Optional

Name (label) of the new agent.

Type: option

```
   --api-name API-NAME
```

Optional

API name of the new agent; if not specified, the API name is derived from the agent name (label); the API name must not exist in
the org.

Type: option

```
   --spec SPEC
```

Optional

Path to an agent spec file.

Type: option

```
   --preview
```

Optional

Preview the agent without saving it in your org.

Type: boolean


Salesforce CLI Command Reference agent Commands

#### **`agent deactivate`**

Deactivate an agent in an org.

#### Description for agent deactivate

Deactivating an agent makes it unavailable to your users. To make changes to an agent, such as adding or removing topics or actions,
you must deactivate it. You can't preview an agent with the "agent preview" CLI command or VS Code if it's deactivated.

If you run the command without the --api-name flag, the command provides a list of agent API names for you to choose from. Use the
flag to specify the exact agent without being prompted.

#### Examples for agent deactivate

Deactivate an agent in your default target org by being prompted:

```
   sf agent deactivate

```

Deactivate the agent Resort_Manager in the org with alias "my_org":

```
   sf agent deactivate --api-name Resort_Manager --target-org my-org

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

**`-n`** **|** **`--api-name API-NAME`**
Optional

API name of the agent to deactivate; if not specified, the command provides a list that you choose from.

Type: option


Salesforce CLI Command Reference agent Commands

#### **`agent generate agent-spec`**

Generate an agent spec, which is a YAML file that captures what an agent can do.

#### Description for agent generate agent-spec

An agent spec is a YAML-formatted file that contains basic information about the agent, such as its role, company description, and an
AI-generated list of topics based on this information. Topics define the range of jobs your agent can handle.

Use flags, such as --role and --company-description, to provide details about your company and the role that the agent plays in your
company. If you prefer, you can also be prompted for the basic information; use --full-interview to be prompted for all required and
optional properties. Upon command execution, the large language model (LLM) associated with your org uses the provided information
to generate a list of topics for the agent. Because the LLM uses the company and role information to generate the topics, we recommend
that you provide accurate, complete, and specific details so the LLM generates the best and most relevant topics. Once generated, you
can edit the spec file; for example, you can remove topics that don't apply or change a topic's description.

You can also iterate the spec generation process by using the --spec flag to pass an existing agent spec file to this command, and then
using the --role, --company-description, etc, flags to refine your agent properties. Iteratively improving the description of your agent
allows the LLM to generate progressively better topics.

You can also specify other agent properties, such as a custom prompt template, how to ground the prompt template to add context to
the agent's prompts, the tone of the prompts, and the username of a user in the org to assign to the agent.

When your agent spec is ready, generate an authoring bundle from it by passing the spec file to the --spec flag of the "agent generate
authoring-bundle" CLI command. An authoring bundle is a metadata type that contains an Agent Script file, which is the blueprint for
an agent. (While not recommended, you can also use the agent spec file to immediately create an agent with the "agent create" command.
We don't recommend this workflow because these types of agents don't use Agent Script, and are thus less flexible and more difficult
to maintain.)

#### Examples for agent generate agent-spec

Generate an agent spec in the default location and use flags to specify the agent properties, such as its role and your company details;
use your default org:

```
   sf agent generate agent-spec --type customer --role "Field customer complaints and manage

    employee schedules." --company-name "Coral Cloud Resorts" --company-description "Provide

    customers with exceptional destination activities, unforgettable experiences, and

   reservation services."

```

Generate an agent spec by being prompted for the required agent properties and generate a maxiumum of 5 topics; write the generated
file to the "specs/resortManagerSpec.yaml" file and use the org with alias "my-org":

```
   sf agent generate agent-spec --max-topics 5 --output-file specs/resortManagerAgent.yaml

   --target-org my-org

```

Be prompted for all required and optional agent properties; use your default org:

```
   sf agent generate agent-spec --full-interview

```

Specify an existing agent spec file called "specs/resortManagerAgent.yaml", and then overwrite it with a new version that contains newly
AI-generated topics based on the updated role information passed in with the --role flag:

```
   sf agent generate agent-spec --spec specs/resortManagerAgent.yaml --output-file

   specs/resortManagerAgent.yaml --role "Field customer complaints, manage employee schedules,

    and ensure all resort operations are running smoothly"

```


Salesforce CLI Command Reference agent Commands

Specify that the conversational tone of the agent is formal and to attach the "resortmanager@myorg.com" username to it; be prompted
for the required properties and use your default org:

```
   sf agent generate agent-spec --tone formal --agent-user resortmanager@myorg.com

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

```
   --type TYPE
```

Optional

Type of agent to create. Internal types are copilots used internally by your company and customer types are the agents you create
for your customers.

Type: option

Permissible values are: customer, internal

```
   --role ROLE
```

Optional

Role of the agent.

Type: option

```
   --company-name COMPANY-NAME
```

Optional

Name of your company.

Type: option

```
   --company-description COMPANY-DESCRIPTION
```

Optional

Description of your company.

Type: option


Salesforce CLI Command Reference agent Commands

```
   --company-website COMPANY-WEBSITE
```

Optional

Website URL of your company.

Type: option

```
   --max-topics MAX-TOPICS
```

Optional

Maximum number of topics to generate in the agent spec; default is 5.

Type: option

```
   --agent-user AGENT-USER
```

Optional

Username of a user in your org to assign to your agent; determines what your agent can access and do.

Type: option

```
   --enrich-logs ENRICH-LOGS
```

Optional

Adds agent conversation data to event logs so you can view all agent session activity in one place.

Type: option

Permissible values are: true, false

```
   --tone TONE
```

Optional

Conversational style of the agent, such as how it expresses your brand personality in its messages through word choice, punctuation,
and sentence structure.

Type: option

Permissible values are: formal, casual, neutral

```
   --spec SPEC
```

Optional

Agent spec file, in YAML format, to use as input to the command.

Type: option

```
   --output-file OUTPUT-FILE
```

Optional

Path for the generated YAML agent spec file; can be an absolute or relative path.

Type: option

Default value: specs/agentSpec.yaml

```
   --full-interview
```

Optional

Prompt for both required and optional flags.

Type: boolean

```
   --prompt-template PROMPT-TEMPLATE
```

Optional

API name of a customized prompt template to use instead of the default prompt template.


Salesforce CLI Command Reference agent Commands

Type: option

```
   --grounding-context GROUNDING-CONTEXT
```

Optional

Context information and personalization that's added to your prompts when using a custom prompt template.

Type: option

```
   --force-overwrite
```

Optional

Don't prompt the user to confirm that an existing spec file will be overwritten.

Type: boolean

#### **`agent generate authoring-bundle`**

Generate an authoring bundle from an existing agent spec YAML file.

#### Description for agent generate authoring-bundle

Authoring bundles are metadata components that contain an agent's Agent Script file. The Agent Script file is the agent's blueprint; it
fully describes what the agent can do using the Agent Script language.

Use this command to generate a new authoring bundle based on an agent spec YAML file, which you create with the "agent generate
agent-spec" command. The agent spec YAML file is a high-level description of the agent; it describes its essence rather than exactly
what it can do. The resulting Agent Script file is customized to reflect what's in the agent spec file. You can also create an authoring
bundle without an agent spec file by specifying the "--no-spec" flag; in this case, the resulting Agent Script file is just the default boilerplate.

The metadata type for authoring bundles is aiAuthoringBundle, which consist of a standard "<bundle-api-name>.bundle-meta.xml"
metadata file and the Agent Script file (with extension ".agent"). When you run this command, the new authoring bundle is generated
in the force-app/main/default/aiAuthoringBundles/<bundle-api-name> directory. Use the --output-dir flag to generate them elsewhere.

After you generate the initial authoring bundle, code the Agent Script file so your agent behaves exactly as you want. The Agent Script
file generated by this command is just a first draft of your agent! Interactively test the agent by conversing with it using the "agent
preview" command. Then publish the agent to your org with the "agent publish authoring-bundle" command.

This command requires an org because it uses it to access an LLM for generating the Agent Script file.

#### Examples for agent generate authoring-bundle

Generate an authoring bundle by being prompted for all required values, such as the agent spec YAML file, the bundle name, and the
API name; use your default org:

```
   sf agent generate authoring-bundle

```

Generate an authoring bundle without using an agent spec file; give the bundle the label "My Authoring Bundle" and use your default
org:

```
   sf agent generate authoring-bundle --no-spec --name "My Authoring Bundle"

```

Generate an authoring bundle from the "specs/agentSpec.yaml" agent spec YAML file and give it the label "My Authoring Bundle"; use
your default org:

```
   sf agent generate authoring-bundle --spec specs/agentSpec.yaml --name "My Authoring Bundle"

```


Salesforce CLI Command Reference agent Commands

Similar to previous example, but generate the authoring bundle files in the "other-package-dir/main/default" package directory; use the
org with alias "my-dev-org":

```
   sf agent generate authoring-bundle --spec specs/agentSpec.yaml --name "My Authoring Bundle"

    --output-dir other-package-dir/main/default --target-org my-dev-org

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
   --api-name API-NAME
```

Optional

API name of the new authoring bundle; if not specified, the API name is derived from the authoring bundle name (label); the API
name can't exist in the org.

Type: option

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

**`-f`** **|** **`--spec SPEC`**
Optional

Path to the agent spec YAML file. If you don't specify the flag, the command provides a list that you can choose from. Use the
--no-spec flag to skip using an agent spec entirely.

Type: option

```
   --no-spec
```

Optional

Skip prompting for an agent spec and use the default Agent Script boilerplate in the generated authoring bundle.

Type: boolean

**`-d`** **|** **`--output-dir OUTPUT-DIR`**
Optional

Directory where the authoring bundle files are generated.

Type: option


Salesforce CLI Command Reference agent Commands

**`-n`** **|** **`--name NAME`**
Optional

Name (label) of the authoring bundle; if not specified, you're prompted for the name.

Type: option

```
   --force-overwrite
```

Optional

Overwrite the existing authoring bundle if one with the same API name already exists locally.

Type: boolean

#### **`agent generate template`**

Generate an agent template from an existing agent in your DX project so you can then package the template in a second-generation
managed package.

#### Description for agent generate template

WARNING: This command doesn't work for agents that were created from an Agent Script file. In other words, you can't currently package
an agent template for agents that use Agent Script.

At a high-level, agents are defined by the Bot, BotVersion, and GenAiPlannerBundle metadata types. The GenAiPlannerBundle type in
turn defines the agent's topics and actions. This command uses the metadata files for these three types, located in your local DX project,
to generate a BotTemplate metadata file for a specific agent (Bot). You then use the BotTemplate metadata file, along with the
GenAiPlannerBundle metadata file that references the BotTemplate, to package the template in a managed package that you can share
between orgs or on AppExchange.

Use the --agent-file flag to specify the relative or full pathname of the Bot metadata file, such as
force-app/main/default/bots/My_Awesome_Agent/My_Awesome_Agent.bot-meta.xml. A single Bot can have multiple BotVersions,
so use the --agent-version flag to specify the version. The corresponding BotVersion metadata file must exist locally. For example, if you
specify "--agent-version 4", then the file force-app/main/default/bots/My_Awesome_Agent/v4.botVersion-meta.xml must exist.

The new BotTemplate metadata file is generated in the "botTemplates" directory in the output directory specified with the --output-dir
flag, and has the name <Agent_API_name>\_v<Version>\_Template.botTemplate-meta.xml, such as
my-package/botTemplates/My_Awesome_Agent_v4_Template.botTemplate-meta.xml. The command displays the full pathname of
the generated files when it completes.

See "Develop and Package Agent Templates Using Scratch Orgs"
(https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/dev2gp_package_agent_templates.htm) for details
about the complete process, which includes using a scratch org to create and test the agent, retrieving the agent metadata to your DX
project, running this command to create the agent template, and then packaging the template.

#### Examples for agent generate template

Generate an agent template from the My_Awesome_Agent Bot metadata file in your DX project and save the BotTemplate and
GenAiPlannerBundle to the specified directory; use version 1 of the agent. The agent that the template is based on is in the org with
alias "my-scratch-org":

```
   sf agent generate template --agent-file

   force-app/main/default/bots/My_Awesome_Agent/My_Awesome_Agent.bot-meta.xml --agent-version

    1 --output-dir my-package --source-org my-scratch-org

```


Salesforce CLI Command Reference agent Commands

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
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

**`-s`** **|** **`--source-org SOURCE-ORG`**
Required

Username or alias of the namespaced scratch org that contains the agent which this template is based on.

Type: option

```
   --agent-version AGENT-VERSION
```

Required

Version of the agent (BotVersion).

Type: option

**`-f`** **|** **`--agent-file AGENT-FILE`**
Required

Path to an agent (Bot) metadata file.

Type: option

**`-r`** **|** **`--output-dir OUTPUT-DIR`**
Optional

Directory where the generated BotTemplate and GenAiPlannerBundle files are saved.

Type: option

#### **`agent generate test-spec`**

Generate an agent test spec, which is a YAML file that lists the test cases for testing a specific agent.

#### Description for agent generate test-spec

The first step when using Salesforce CLI to create an agent test in your org is to use this interactive command to generate a local
YAML-formatted test spec file. The test spec YAML file contains information about the agent being tested, such as its API name, and
then one or more test cases. This command uses the metadata components in your DX project when prompting for information, such
as the agent API name; it doesn't look in your org.


Salesforce CLI Command Reference agent Commands

To generate a specific agent test case, this command prompts you for this information; when possible, the command provides a list of
options for you to choose from:

    - Utterance: Natural language statement, question, or command used to test the agent.

    - Expected topic: API name of the topic you expect the agent to use when responding to the utterance.

    - Expected actions: One or more API names of the expection actions the agent takes.

    - Expected outcome: Natural language description of the outcome you expect.

    - (Optional) Custom evaluation: Test an agent's response for specific strings or numbers.

    - (Optional) Conversation history: Boilerplate for additional context you can add to the test in the form of a conversation history.

You can manually add contextVariables to test cases in the generated YAML file to inject contextual data (such as CaseId or RoutableId)
into agent sessions. This is useful for testing agent behavior with different contextual information.

When your test spec is ready, you then run the "agent test create" command to actually create the test in your org and synchronize the
metadata with your DX project. The metadata type for an agent test is AiEvaluationDefinition.

If you have an existing AiEvaluationDefinition metadata XML file in your DX project, you can generate its equivalent YAML test spec file
with the --from-definition flag.

Examples for **`agent generate test-spec`**

Generate an agent test spec YAML file interactively:

```
   sf agent generate test-spec

```

Generate an agent test spec YAML file and specify a name for the new file; if the file exists, overwrite it without confirmation:

```
   sf agent generate test-spec --output-file specs/Resort_Manager-new-version-testSpec.yaml

   --force-overwrite

```

Generate an agent test spec YAML file from an existing AiEvaluationDefinition metadata XML file in your DX project:

```
   sf agent generate test-spec --from-definition

   force-app//main/default/aiEvaluationDefinitions/Resort_Manager_Tests.aiEvaluationDefinition-meta.xml

```

Flags

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option

**`-d`** **|** **`--from-definition FROM-DEFINITION`**
Optional

Filepath to the AIEvaluationDefinition metadata XML file in your DX project that you want to convert to a test spec YAML file.

Type: option

```
   --force-overwrite
```

Optional

Don't prompt for confirmation when overwriting an existing test spec YAML file.

Type: boolean


Salesforce CLI Command Reference agent Commands

**`-f`** **|** **`--output-file OUTPUT-FILE`**
Optional

Name of the generated test spec YAML file. Default value is "specs/<AGENT_API_NAME>-testSpec.yaml".

Type: option

#### **`agent preview`**

Interact with an agent to preview how it responds to your statements, questions, and commands (utterances).

#### Description for agent preview

Use this command to have a natural language conversation with an agent, either while you code its local Agent Script file or when it's
published to an org. Previewing an agent acts like an initial test to make sure it responds to your utterances as you expect. For example,
you can test that the agent uses a particular topic when asked a question, and then whether it invokes the correct action associated
with that topic. This command is the CLI-equivalent of the Preview panel in your org's Agentforce Builder UI.

Run without flags, this command provides a list of agents to preview, divided into two categories: "Agent Script", which are agents that
have a local authoring bundle in your DX project, or "Published", which are agents that are published and activated in your org. Authoring
bundles contain an agent's Agent Script file. You then choose the agent you want to preview from the list. Or you can use the
--authoring-bundle flag to specify a local authoring bundle's API name or --api-name to specify an activated published agent.

When previewing an agent from its Agent Script file, you can use these two modes:

    - Simulated mode (Default): Uses only the Agent Script file to converse, and it simulates (mocks) all the actions. Use this mode if none
of the Apex classes, flows, or prompt templates that implement your actions are available yet. The LLM uses the information about topics
in the Agent Script file to simulate what the action does or how it responds.

    - Live mode: Uses the actual Apex classes, flows, and prompt templates in your development org in the agent preview. If you've changed
the Apex classe, flows, or prompt templates in your local DX project, then you must deploy them to your development org if you want
to use them in your live preview.

You can use the Apex Replay Debugger to debug your Apex classes when using live mode for Agent Script files and for activated
published agents; specify the --apex-debug flag.

Once connected to your agent, the preview interface is simple: in the "Start typing..." prompt, enter a statement, question, or command;
when you're done, enter Return. Your utterance is posted on the right along with a timestamp. The agent then responds on the left. To
exit the conversation, hit ESC or Control+C.

When the session concludes, the command asks if you want to save the API responses and chat transcripts. By default, the files are saved
to the "./temp/agent-preview" directory. Specify a new default directory with the --output-dir flag.

#### Examples for agent preview

Preview an agent by choosing from the list of available local Agent Script or published agents. If previewing a local Agent Script agent,
use simulated mode. Use the org with alias "my-dev-org".

```
   sf agent preview --target-org my-dev-org

```

Preview an agent in live mode by choosing from a list of authoring bundles. Save the conversation transcripts to the
"./transcripts/my-preview" directory, enable the Apex debug logs, and use your default org:

```
   sf agent preview --use-live-actions --apex-debug --output-dir transcripts/my-preview

```


Salesforce CLI Command Reference agent Commands

Flags

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

**`-n`** **|** **`--api-name API-NAME`**
Optional

API name of the activated published agent you want to interact with.

Type: option

```
   --authoring-bundle AUTHORING-BUNDLE
```

Optional

API name of the authoring bundle metadata component that contains the agent's Agent Script file.

Type: option

**`-d`** **|** **`--output-dir OUTPUT-DIR`**
Optional

Directory where conversation transcripts are saved.

Type: option

**`-x`** **|** **`--apex-debug`**
Optional

Enable Apex debug logging during the agent preview conversation.

Type: boolean

```
   --use-live-actions
```

Optional

Use real actions in the org; if not specified, preview uses AI to simulate (mock) actions.

Type: boolean

#### **`agent preview end`**

End an existing programmatic agent preview session and get trace location.


Salesforce CLI Command Reference agent Commands

Description for **`agent preview end`**

You must have previously started a programmatic agent preview session with the "agent preview start" command to then use this
command to end it. This command also displays the local directory where the session trace files are stored.

The original "agent preview start" command outputs a session ID which you then use with the --session-id flag of this command to end
the session. You don't have to specify the --session-id flag if an agent has only one active preview session. You must also use either the
--authoring-bundle or --api-name flag to specify the API name of the authoring bundle or the published agent, respectively. To find
either API name, navigate to your package directory in your DX project. The API name of an authoring bundle is the same as its directory
name under the "aiAuthoringBundles" metadata directory. Similarly, the published agent's API name is the same as its directory name
under the "Bots" metadata directory.

Use the --all flag to end all active preview sessions at once. You can combine --all with --api-name or --authoring-bundle to end only
sessions for a specific agent, or use --all on its own to end every session across all agents in the project.

Examples for **`agent preview end`**

End a preview session of a published agent by specifying its session ID and API name; use the default org:

```
   sf agent preview end --session-id <SESSION_ID> --api-name My_Published_Agent

```

Similar to previous example, but don't specify a session ID; you get an error if the published agent has more than one active session. Use
the org with alias "my-dev-org":

```
   sf agent preview end --api-name My_Published_Agent --target-org my-dev-org

```

End a preview session of an agent using its authoring bundle API name; you get an error if the agent has more than one active session.

```
   sf agent preview end --authoring-bundle My_Local_Agent

```

End all active preview sessions for a specific agent without prompting:

```
   sf agent preview end --all --authoring-bundle My_Local_Agent --target-org <target_org>

   --no-prompt

```

End all active preview sessions across every agent in the local session cache for an org:

```
   sf agent preview end --all --target-org <target_org>

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


Salesforce CLI Command Reference agent Commands

Type: option

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

```
   --session-id SESSION-ID
```

Optional

Session ID outputted by "agent preview start". Not required when the agent has exactly one active session. Run "agent preview
sessions" to see the list of all sessions.

Type: option

**`-n`** **|** **`--api-name API-NAME`**
Optional

API name of the activated published agent you want to preview.

Type: option

```
   --authoring-bundle AUTHORING-BUNDLE
```

Optional

API name of the authoring bundle metadata component that contains the agent's Agent Script file.

Type: option

```
   --all
```

Optional

End all active preview sessions. Combine with --api-name or --authoring-bundle to limit to a specific agent, or use with only
--target-org to end sessions for all agents found in the local session cache. Requires --target-org.

Type: boolean

**`-p`** **|** **`--no-prompt`**
Optional

Don't prompt for confirmation before ending sessions. Has an effect only when used with --all.

Type: boolean

#### **`agent preview send`**

Send a message to an existing agent preview session.

#### Description for agent preview send

You must have previously started a programmatic agent preview session with the "agent preview start" command to then use this
command to send the agent a message (utterance). This command then displays the agent's response.

The original "agent preview start" command outputs a session ID which you then use with the --session-id flag of this command to send
a message. You don't have to specify the --session-id flag if an agent has only one active preview session. You must also use either the
--authoring-bundle or --api-name flag to specify the API name of the authoring bundle or the published agent, respecitvely. To find
either API name, navigate to your package directory in your DX project. The API name of an authoring bundle is the same as its directory
name under the "aiAuthoringBundles" metadata directory. Similarly, the published agent's API name is the same as its directory name
under the "Bots" metadata directory.


Salesforce CLI Command Reference agent Commands

Examples for **`agent preview send`**

Send a message to an activated published agent using its API name and session ID; use the default org:

```
   sf agent preview send --utterance "What can you help me with?" --api-name My_Published_Agent

    --session-id <SESSION_ID>

```

Similar to previous example, but don't specify a session ID; you get an error if the agent has more than one active session. Use the org
with alias "my-dev-org":

```
   sf agent preview send --utterance "What can you help me with?" --api-name My_Published_Agent

    --target-org my-dev-org

```

Send a message to an agent using its authoring bundle API name; you get an error if the agent has more than one active session:

```
   sf agent preview send --utterance "what can you help me with?" --authoring-bundle

   My_Local_Agent

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

```
   --session-id SESSION-ID
```

Optional

Session ID outputted by "agent preview start". Not required when the agent has exactly one active session. Run "agent preview
sessions" to see list of all sessions.

Type: option

**`-u`** **|** **`--utterance UTTERANCE`**
Required

Utterance to send to the agent, enclosed in double quotes.

Type: option


Salesforce CLI Command Reference agent Commands

**`-n`** **|** **`--api-name API-NAME`**
Optional

API name of the activated published agent you want to preview.

Type: option

```
   --authoring-bundle AUTHORING-BUNDLE
```

Optional

API name of the authoring bundle metadata component that contains the agent's Agent Script file.

Type: option

#### **`agent preview sessions`**

List all known programmatic agent preview sessions.

#### Description for agent preview sessions

This command lists the agent preview sessions that were started with the "agent preview start" command and are still in the local cache.
Use this command to discover specific session IDs that you can pass to the "agent preview send" or "agent preview end" commands
with the --session-id flag.

Programmatic agent preview sessions can be started for both published activated agents and by using an agent's local authoring bundle,
which contains its Agent Script file. In this command's output table, the Agent column contains either the API name of the authoring
bundle or the published agent, whichever was used when starting the session. In the table, if the same API name has multiple rows with
different session IDs, then it means that you previously started multiple preview sessions with the associated agent.

#### Examples for agent preview sessions

List all cached agent preview sessions:

```
   sf agent preview sessions

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

#### **`agent preview start`**

Start a programmatic agent preview session.


Salesforce CLI Command Reference agent Commands

Description for **`agent preview start`**

This command outputs a session ID that you then use with the "agent preview send" command to send an utterance to the agent. Use
the "agent preview sessions" command to list all active sessions and the "agent preview end" command to end a specific session.

Identify the agent you want to start previewing with either the --authoring-bundle flag to specify a local authoring bundle's API name
or --api-name to specify an activated published agent's API name. To find either API name, navigate to your package directory in your
DX project. The API name of an authoring bundle is the same as its directory name under the "aiAuthoringBundles" metadata directory.
Similarly, the published agent's API name is the same as its directory name under the "Bots" metadata directory.

When starting a preview session with --authoring-bundle, you must explicitly specify the execution mode using one of these flags:

    - --use-live-actions: Executes real Apex classes, flows, and other actions in the org. This surfaces compile and validation errors during
preview.

    - --simulate-actions: Uses AI to simulate action execution without calling real implementations.

Published agents (--api-name) always use live actions. The mode flags are optional and have no effect for published agents.

Examples for **`agent preview start`**

Start a programmatic agent preview session by specifying an authoring bundle; use simulated actions. Use the org with alias "my-dev-org":

```
   sf agent preview start --authoring-bundle My_Agent_Bundle --target-org my-dev-org

   --simulate-actions

```

Similar to previous example but use live actions and the default org:

```
   sf agent preview start --authoring-bundle My_Agent_Bundle --use-live-actions

```

Start a preview session with an activated published agent (always uses live actions):

```
   sf agent preview start --api-name My_Published_Agent

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


Salesforce CLI Command Reference agent Commands

Type: option

**`-n`** **|** **`--api-name API-NAME`**
Optional

API name of the activated published agent you want to preview.

Type: option

```
   --authoring-bundle AUTHORING-BUNDLE
```

Optional

API name of the authoring bundle metadata component that contains the agent's Agent Script file.

Type: option

```
   --use-live-actions
```

Optional

Execute real actions in the org (Apex classes, flows, etc.). Required with --authoring-bundle.

Type: boolean

```
   --simulate-actions
```

Optional

Use AI to simulate action execution instead of calling real actions. Required with --authoring-bundle.

Type: boolean

#### **`agent publish authoring-bundle`**

Publish an authoring bundle to your org, which results in a new agent or a new version of an existing agent.

#### Description for agent publish authoring-bundle

An authoring bundle is a metadata type (named aiAuthoringBundle) that provides the blueprint for an agent. The metadata type contains
two files: the standard metatada XML file and an Agent Script file (extension ".agent") that fully describes the agent using the Agent
Script language.

When you publish an authoring bundle to your org, a number of things happen. First, this command validates that the Agent Script file
successfully compiles. If there are compilation errors, the command exits and you must fix the Agent Script file to continue. Once the
Agent Script file compiles, then it's published to the org, which in turn creates new associated metadata (Bot, BotVersion, GenAiX), or
new versions of the metadata if the agent already exists. The new or updated metadata is retrieved back to your DX project; specify the
--skip-retrieve flag to skip this step. Finally, the authoring bundle metadata (AiAuthoringBundle) is deployed to your org.

This command uses the API name of the authoring bundle.

#### Examples for agent publish authoring-bundle

Publish an authoring bundle by being prompted for its API name; use your default org:

```
   sf agent publish authoring-bundle

```

Publish an authoring bundle with API name MyAuthoringBundle to the org with alias "my-dev-org":

```
   sf agent publish authoring-bundle --api-name MyAuthoringbundle --target-org my-dev-org

```


Salesforce CLI Command Reference agent Commands

Publish with verbose output to see all retrieved and deployed metadata components:

```
   sf agent publish authoring-bundle --api-name MyAuthoringbundle --verbose

```

Publish with concise output showing only essential information:

```
   sf agent publish authoring-bundle --api-name MyAuthoringbundle --concise

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

**`-n`** **|** **`--api-name API-NAME`**
Optional

API name of the authoring bundle you want to publish; if not specified, the command provides a list that you can choose from.

Type: option

```
   --skip-retrieve
```

Optional

Don't retrieve the metadata associated with the agent to your DX project.

Type: boolean

**`-v`** **|** **`--verbose`**
Optional

Display detailed output showing all metadata components retrieved and deployed during the publish process.

Type: boolean

```
   --concise
```

Optional

Display minimal output with only essential information about the publish operation.

Type: boolean


Salesforce CLI Command Reference agent Commands

#### **`agent test create`**

Create an agent test in your org using a local test spec YAML file.

#### Description for agent test create

To run this command, you must have an agent test spec file, which is a YAML file that lists the test cases for testing a specific agent. Use
the "agent generate test-spec" CLI command to generate a test spec file. Then specify the file to this command with the --spec flag, or
run this command with no flags to be prompted.

When this command completes, your org contains the new agent test, which you can view and edit using the Testing Center UI. This
command also retrieves the metadata component (AiEvaluationDefinition) associated with the new test to your local Salesforce DX
project and displays its filename.

After you've created the test in the org, use the "agent test run" command to run it.

#### Examples for agent test create

Create an agent test interactively and be prompted for the test spec and API name of the test in the org; use the default org:

```
   sf agent test create

```

Create an agent test and use flags to specify all required information; if a test with same API name already exists in the org, overwrite it
without confirmation. Use the org with alias "my-org":

```
   sf agent test create --spec specs/Resort_Manager-testSpec.yaml --api-name Resort_Manager_Test

    --force-overwrite --target-org my-org

```

Preview what the agent test metadata (AiEvaluationDefinition) looks like without deploying it to your default org:

```
   sf agent test create --spec specs/Resort_Manager-testSpec.yaml --api-name Resort_Manager_Test

    --preview

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
   --api-name API-NAME
```

Optional

API name of the new test; the API name must not exist in the org.

Type: option

```
   --spec SPEC
```

Optional

Path to the test spec YAML file.


Salesforce CLI Command Reference agent Commands

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

```
   --preview
```

Optional

Preview the test metadata file (AiEvaluationDefinition) without deploying to your org.

Type: boolean

```
   --force-overwrite
```

Optional

Don't prompt for confirmation when overwriting an existing test (based on API name) in your org.

Type: boolean

#### **`agent test list`**

List the available agent tests in your org.

#### Description for agent test list

The command outputs a table with the name (API name) of each test along with its unique ID, type ('agentforce-studio' or 'testing-center'),
and the date it was created in the org.

#### Examples for agent test list

List the agent tests in your default org:

```
   sf agent test list

```

List the agent tests in an org with alias "my-org""

```
   sf agent test list --target-org my-org

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


Salesforce CLI Command Reference agent Commands

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

#### **`agent test results`**

Get the results of a completed agent test run.

#### Description for agent test results

This command requires a job ID, which the original "agent test run" command displays when it completes. You can also use the
--use-most-recent flag to see results for the most recently run agent test.

By default, this command outputs test results in human-readable tables for each test case. The tables show whether the test case passed,
the expected and actual values, the test score, how long the test took, and more. Use the --result-format to display the test results in
JSON or Junit format. Use the --output-dir flag to write the results to a file rather than to the terminal.

#### Examples for agent test results

Get the results of an agent test run in your default org using its job ID:

```
   sf agent test results --job-id 4KBfake0000003F4AQ

```

Get the results of the most recently run agent test in an org with alias "my-org":

```
   sf agent test results --use-most-recent --target-org my-org

```

Get the results of the most recently run agent test in your default org, and write the JSON-formatted results into a directory called
"test-results":

```
   sf agent test results --use-most-recent --output-dir ./test-results --result-format json

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


Salesforce CLI Command Reference agent Commands

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

**`-i`** **|** **`--job-id JOB-ID`**
Required

Job ID of the completed agent test run.

Type: option

```
   --result-format RESULT-FORMAT
```

Optional

Format of the agent test run results.

Type: option

Permissible values are: json, human, junit, tap

Default value: human

**`-d`** **|** **`--output-dir OUTPUT-DIR`**
Optional

Directory to write the agent test results into.

If the agent test run completes, write the results to the specified directory. If the test is still running, the test results aren't written.

Type: option

```
   --test-runner TEST-RUNNER
```

Optional

Explicitly specify which test runner to use (agentforce-studio or testing-center).

By default, the command automatically detects which test runner to use based on the test definition metadata type in your org. Use
this flag to explicitly specify the runner type. 'agentforce-studio' uses AiTestingDefinition metadata. 'testing-center' uses
AiEvaluationDefinition metadata.

Type: option

Permissible values are: agentforce-studio, testing-center

```
   --verbose
```

Optional

Show generated data in the test results output.

When enabled, includes detailed generated data (such as invoked actions) in the human-readable test results output. This is useful
for debugging test failures and understanding what actions were actually invoked during the test run.

The generated data is in JSON format and includes the Apex classes or Flows that were invoked, the Salesforce objects that were
touched, and so on. Use the JSON structure of this information to build the test case JSONPath expression when using custom
evaluations.


Salesforce CLI Command Reference agent Commands

Type: boolean

#### **`agent test resume`**

Resume an agent test that you previously started in your org so you can view the test results.

#### Description for agent test resume

This command requires a job ID, which the original "agent test run" command displays when it completes. You can also use the
--use-most-recent flag to see results for the most recently run agent test.

Use the --wait flag to specify the number of minutes for this command to wait for the agent test to complete; if the test completes by
the end of the wait time, the command displays the test results. If not, the CLI returns control of the terminal to you, and you must run
"agent test resume" again.

By default, this command outputs test results in human-readable tables for each test case. The tables show whether the test case passed,
the expected and actual values, the test score, how long the test took, and more. Use the --result-format to display the test results in
JSON or Junit format. Use the --output-dir flag to write the results to a file rather than to the terminal.

#### Examples for agent test resume

Resume an agent test in your default org using a job ID:

```
   sf agent test resume --job-id 4KBfake0000003F4AQ

```

Resume the most recently-run agent test in an org with alias "my-org" org; wait 10 minutes for the tests to finish:

```
   sf agent test resume --use-most-recent --wait 10 --target-org my-org

```

Resume the most recent agent test in your default org, and write the JSON-formatted results into a directory called "test-results":

```
   sf agent test resume --use-most-recent --output-dir ./test-results --result-format json

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


Salesforce CLI Command Reference agent Commands

Override the api version used for api requests made by this command

Type: option

**`-i`** **|** **`--job-id JOB-ID`**
Optional

Job ID of the original agent test run.

Type: option

**`-r`** **|** **`--use-most-recent`**
Optional

Use the job ID of the most recent agent test run.

Type: boolean

**`-w`** **|** **`--wait WAIT`**
Optional

Number of minutes to wait for the command to complete and display results to the terminal window.

Type: option

```
   --result-format RESULT-FORMAT
```

Optional

Format of the agent test run results.

Type: option

Permissible values are: json, human, junit, tap

Default value: human

**`-d`** **|** **`--output-dir OUTPUT-DIR`**
Optional

Directory to write the agent test results into.

If the agent test run completes, write the results to the specified directory. If the test is still running, the test results aren't written.

Type: option

```
   --test-runner TEST-RUNNER
```

Optional

Explicitly specify which test runner to use (agentforce-studio or testing-center).

By default, the command automatically detects which test runner to use based on the test definition metadata type in your org. Use
this flag to explicitly specify the runner type. 'agentforce-studio' uses AiTestingDefinition metadata. 'testing-center' uses
AiEvaluationDefinition metadata.

Type: option

Permissible values are: agentforce-studio, testing-center

```
   --verbose
```

Optional

Show generated data in the test results output.

When enabled, includes detailed generated data (such as invoked actions) in the human-readable test results output. This is useful
for debugging test failures and understanding what actions were actually invoked during the test run.


Salesforce CLI Command Reference agent Commands

The generated data is in JSON format and includes the Apex classes or Flows that were invoked, the Salesforce objects that were
touched, and so on. Use the JSON structure of this information to build the test case JSONPath expression when using custom
evaluations.

Type: boolean

#### **`agent test run`**

Start an agent test in your org.

#### Description for agent test run

Use the --api-name flag to specify the name of the agent test you want to run. Use the output of the "agent test list" command to get
the names of all the available agent tests in your org.

By default, this command starts the agent test in your org, but it doesn't wait for the test to finish. Instead, it displays the "agent test
resume" command, with a job ID, that you execute to see the results of the test run, and then returns control of the terminal window
to you. Use the --wait flag to specify the number of minutes for the command to wait for the agent test to complete; if the test completes
by the end of the wait time, the command displays the test results. If not, run "agent test resume".

By default, this command outputs test results in human-readable tables for each test case, if the test completes in time. The tables show
whether the test case passed, the expected and actual values, the test score, how long the test took, and more. Use the --result-format
to display the test results in JSON or Junit format. Use the --output-dir flag to write the results to a file rather than to the terminal.

#### Examples for agent test run

Start an agent test called Resort_Manager_Test for an agent in your default org, don't wait for the test to finish:

```
   sf agent test run --api-name Resort_Manager_Test

```

Start an agent test for an agent in an org with alias "my-org" and wait for 10 minutes for the test to finish:

```
   sf agent test run --api-name Resort_Manager_Test --wait 10 --target-org my-org

```

Start an agent test and write the JSON-formatted results into a directory called "test-results":

```
   sf agent test run --api-name Resort_Manager_Test --wait 10 --output-dir ./test-results

   --result-format json

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


Salesforce CLI Command Reference agent Commands

Username or alias of the target org. Not required if the `target-org` configuration variable is already set.

Type: option

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

**`-n`** **|** **`--api-name API-NAME`**
Optional

API name of the agent test to run; corresponds to the name of the AiEvaluationDefinition metadata component that implements
the agent test.

Type: option

**`-w`** **|** **`--wait WAIT`**
Optional

Number of minutes to wait for the command to complete and display results to the terminal window.

Type: option

```
   --result-format RESULT-FORMAT
```

Optional

Format of the agent test run results.

Type: option

Permissible values are: json, human, junit, tap

Default value: human

**`-d`** **|** **`--output-dir OUTPUT-DIR`**
Optional

Directory to write the agent test results into.

If the agent test run completes, write the results to the specified directory. If the test is still running, the test results aren't written.

Type: option

```
   --test-runner TEST-RUNNER
```

Optional

Explicitly specify which test runner to use (agentforce-studio or testing-center).

By default, the command automatically detects which test runner to use based on the test definition metadata type in your org. Use
this flag to explicitly specify the runner type. 'agentforce-studio' uses AiTestingDefinition metadata. 'testing-center' uses
AiEvaluationDefinition metadata.

Type: option

Permissible values are: agentforce-studio, testing-center

```
   --verbose
```

Optional

Show generated data in the test results output.

When enabled, includes detailed generated data (such as invoked actions) in the human-readable test results output. This is useful
for debugging test failures and understanding what actions were actually invoked during the test run.


Salesforce CLI Command Reference agent Commands

The generated data is in JSON format and includes the Apex classes or Flows that were invoked, the Salesforce objects that were
touched, and so on. Use the JSON structure of this information to build the test case JSONPath expression when using custom
evaluations.

Type: boolean

#### agent test run-eval (Beta)

Run rich evaluation tests against an Agentforce agent.

Note: This feature is a Beta Service. Customers may opt to try such Beta Service in its sole discretion. Any use of the Beta Service
is subject to the applicable Beta Services Terms provided at Agreements and Terms
[(https://www.salesforce.com/company/legal/agreements/).](https://www.salesforce.com/company/legal/agreements/)

#### Description for agent test run-eval

Specify the tests you want to run with one of these inputs to the --spec flag:

    - YAML test spec generated by the `agent generate test-spec` CLI command

    - JSON payload

When you provide a YAML test spec, this command automatically translates test cases into internal state-based evaluation framework
calls and infers the agent name from the test spec's `subjectName` field. As a result, you can use the same test spec with both the `agent
test run` and `agent test run-eval` commands. YAML test specs also support context variables, which allow you to inject contextual data
(such as CaseId or RoutableId) into agent sessions for testing with different contexts.

When you provide a JSON payload, it's sent directly to the evaluation framework with optional normalization. The normalizer auto-corrects
common field name mistakes, converts shorthand references to JSONPath, and injects defaults. Use `--no-normalize` to disable this
auto-normalization. JSON payloads can also include context_variables on agent.create_session steps for the same contextual testing
capabilities as when you use a YAML test spec.

This command supports more than 8 evaluator types, including subagent routing assertions, action invocation checks, string/numeric
assertions, semantic similarity scoring, and LLM-based quality ratings.

#### Examples for agent test run-eval

Run tests using a YAML test spec on the org with alias "my-org":

```
   sf agent test run-eval --spec specs/my-agent-testSpec.yaml --target-org my-org

```

Run tests using a YAML spec with explicit agent name override; use your default org:

```
   sf agent test run-eval --spec specs/my-agent-testSpec.yaml --api-name My_Agent

```

Run tests using a JSON payload:

```
   sf agent test run-eval --spec specs/eval-payload.json --target-org my-org

```

Run tests and output results in JUnit format; useful for continuous integration and deployment (CI/CD):

```
   sf agent test run-eval --spec specs/my-agent-testSpec.yaml --target-org my-org

   --result-format junit

```

Run tests with contextVariables to inject contextual data into agent sessions (add contextVariables to test cases in your YAML spec):

```
   sf agent test run-eval --spec specs/agent-with-context.yaml --target-org my-org

```


Salesforce CLI Command Reference agent Commands

Pipe JSON payload from stdin (--spec flag is automatically populated from stdin):

```
   $ echo '{"tests":[...]}' | sf agent test run-eval --spec --target-org my-org

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

**`-s`** **|** **`--spec SPEC`**
Required

Path to test spec file (YAML or JSON). Supports reading from stdin when piping content.

Type: option

**`-n`** **|** **`--api-name API-NAME`**
Optional

Agent API name (also called DeveloperName) used to resolve agent_id and agent_version_id. Auto-inferred from the YAML spec's
subjectName.

Type: option

```
   --result-format RESULT-FORMAT
```

Optional

Format of the agent test run results.

Type: option

Permissible values are: json, human, junit, tap

Default value: human

```
   --batch-size BATCH-SIZE
```

Optional

Number of tests per API request (max 5).

Type: option


Salesforce CLI Command Reference agent Commands

Default value: 5

```
   --no-normalize
```

Optional

Disable auto-normalization of field names and shorthand references.

Type: boolean

#### **`agent trace delete`**

Delete trace files from an agent preview session.

#### Description for agent trace delete

When you run an agent preview conversation (either interactive or programmatic), trace files are automatically recorded and saved in
your local DX project. Use this command to delete some or all of the trace files.

By default, this command shows a preview of what will be deleted and prompts for confirmation. Use --no-prompt to skip confirmation.

Without filters, this comamnd deletes all trace files for all agents and sessions. Use flags to narrow the scope: filter by agent API name
(--agent), by session (--session-id), or by age (--older-than).

#### Examples for agent trace delete

Delete all traces for all agents and sessions; prompt for confirmation:

```
   sf agent trace delete

```

Delete all traces for a specific agent:

```
   sf agent trace delete --agent My_Agent

```

Delete traces from a specific session:

```
   sf agent trace delete --session-id <SESSION_ID>

```

Delete traces older than 7 days:

```
   sf agent trace delete --older-than 7d

```

Delete traces older than 24 hours for a specific agent; don't prompt for confirmation:

```
   sf agent trace delete --agent My_Agent --older-than 24h --no-prompt

```

Delete all traces for all agents and sessions; don't prompt for confirmation:

```
   sf agent trace delete --no-prompt

```

Flags

```
   --json
```

Optional

Format output as json.

Type: boolean


Salesforce CLI Command Reference agent Commands

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option

**`-a`** **|** **`--agent AGENT`**
Optional

API name of the agent used to filter the list of trace files you want to delete. Matches against the API name used when starting the
session, either an authoring bundle or a published agent API name.

Type: option

```
   --session-id SESSION-ID
```

Optional

Session ID used to filter the list of trace files you want to delete. Use the "agent preview sessions" CLI command to list all known
agent preview sessions along with their session IDs.

Type: option

```
   --older-than OLDER-THAN
```

Optional

Duration used to filter the list of trace files; only files older than the duration are deleted. Accepts a number followed by a unit:
m/minutes, h/hours, d/days, w/weeks. Examples: 7d, 24h, 2w.

Type: option

```
   --no-prompt
```

Optional

Skip the confirmation prompt and delete immediately.

Type: boolean

#### **`agent trace list`**

List the available trace files that were recorded during all agent preview sessions.

#### Description for agent trace list

When you run an agent preview conversation (either interactive or programmatic), trace files are automatically recorded and saved in
your local DX project. By default, this command lists all trace files for all agents and all of their sessions. Use flags to narrow results: filter
by agent name (--agent), by session (--session-id), or by date (--since).

Each row in the output corresponds to one trace file, which in turn corresponds to one agent session. The Agent column shows the
authoring bundle or API name used when starting the session.

#### Examples for agent trace list

List all trace files for all agents and sessions:

```
   sf agent trace list

```

List all trace files for a specific agent:

```
   sf agent trace list --agent My_Agent

```


Salesforce CLI Command Reference agent Commands

List trace files for a specific session:

```
   sf agent trace list --session-id <SESSION_ID>

```

List trace files recorded on or after April 20, 2026 (date-only, interpreted as UTC midnight):

```
   sf agent trace list --since 2026-04-20

```

List trace files recorded on or after a specific UTC time:

```
   sf agent trace list --since 2026-04-20T14:00:00Z

```

Filter by agent and date together:

```
   sf agent trace list --agent My_Agent --since 2026-04-20

```

Return results as JSON:

```
   sf agent trace list --json

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
   --session-id SESSION-ID
```

Optional

Session ID used to filter the list of trace files. Use the "agent preview sessions" CLI command to list all known agent preview sessions
along with their session IDs.

Type: option

**`-a`** **|** **`--agent AGENT`**
Optional

API name of the agent used to filter the list of available trace files. Matches against the API name used when starting the session,
either an authoring bundle or a published agent API name.

Type: option

```
   --since SINCE
```

Optional

Date used to filter the list of trace files; only those recorded on or after the date are listed.

Accepts ISO 8601 format: date-only (2026-04-20), date-time (2026-04-20T14:00:00Z), or date-time with milliseconds
(2026-04-20T14:00:00.000Z). The "Recorded At" values shown in the table output are valid inputs.

Type: option


Salesforce CLI Command Reference agent Commands

#### **`agent trace read`**

Read trace files from an agent preview session.

#### Description for agent trace read

When you run an agent preview conversation (either interactive or programmatic), trace files are automatically recorded and saved in
your local DX project. Each turn (utterance or response) of a conversation creates trace data. Use this command to view trace data for a
specific preview session, so you can then analyze the trace data to observe, monitor, investigate, and troubleshoot agent events and
behavior.

Use the --format flag to specify one of these formats of the outputted trace data:

    - summary (Default): A per-turn narrative showing topic routing, actions executed, and the agent's response. Use this to quickly understand
what happened in a preview session.

    - detail: Diagnostic drill-down into a specific dimension. Filters output to only the trace steps relevant to that dimension, minimizing
noise.

    - raw: Unprocessed trace JSON. Use this as a fallback when the trace schema has changed or you need to perform custom analysis.

If you specify "--format detail", you must also specify a dimension with the --dimension flag. Dimensions are a way to slice and analyze
the agent execution trace from a specific angle or concern. Instead of looking at the raw sequence of everything that happened, each
dimension filters and organizes the trace data to answer a specific type of question. These are the available dimensions and the information
they provide:

    - actions: The actions the agent executed. Includes action name, input parameters, output, and latency. Use this dimension to understand
what the agent actually did when answering an utterance in the preview session.

    - grounding: The reasoning steps used by the LLM. Use this dimension to see how the agent "thought" about the problem - the AI
reasoning that determined which actions to take.

    - routing: How the agent navigated between subagents. Use this dimension to understand conversation flow - when and why the agent
switched between different subagents or contexts during the conversation.

    - errors: Aggregates all errors during the session. Use this dimension to quickly identify and debug issues across all steps.

#### Examples for agent trace read

Show a session trace summary for all turns in the session with the specified ID:

```
   sf agent trace read --session-id <SESSION_ID>

```

Show a trace summary for the second turn (utterance or response) of the conversation:

```
   sf agent trace read --session-id <SESSION_ID> --turn 2

```

Drill into action execution across all turns:

```
   sf agent trace read --session-id <SESSION_ID> --format detail --dimension actions

```

Drill into routing decisions for the first turn of the conversation:

```
   sf agent trace read --session-id <SESSION_ID> --format detail --dimension routing --turn

   1

```

Show all errors across the session:

```
   sf agent trace read --session-id <SESSION_ID> --format detail --dimension errors

```


Salesforce CLI Command Reference agent Commands

Output raw trace JSON for custom parsing:

```
   sf agent trace read --session-id <SESSION_ID> --format raw

```

Return results as JSON:

```
   sf agent trace read --session-id <SESSION_ID> --json

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

**`-s`** **|** **`--session-id SESSION-ID`**
Required

Session ID to read traces for. Use the "agent preview sessions" CLI command to list all known agent preview sessions along with
their session IDs

Type: option

**`-f`** **|** **`--format FORMAT`**
Optional

Output format of the trace data; specifies the level of detail you want in the trace files.

Type: option

Permissible values are: summary, detail, raw

Default value: summary

**`-d`** **|** **`--dimension DIMENSION`**
Optional

Dimension to drill into when using "--format detail"; used to filter and organize the trace data to answer a specific type of question.

Type: option

Permissible values are: actions, grounding, routing, errors

**`-t`** **|** **`--turn TURN`**
Optional

Turn number for which you want trace data. A turn is a single utterance or response in a conversation, starting with 1.

Type: option

#### **`agent validate authoring-bundle`**

Validate an authoring bundle to ensure its Agent Script file compiles successfully and can be used to publish an agent.


Salesforce CLI Command Reference agent Commands

Description for **`agent validate authoring-bundle`**

An authoring bundle is a metadata type (named aiAuthoringBundle) that provides the blueprint for an agent. The metadata type contains
two files: the standard metatada XML file and an Agent Script file (extension ".agent") that fully describes the agent using the Agent
Script language.

This command validates that the Agent Script file in the authoring bundle compiles without errors so that you can later publish the
bundle to your org. Use this command while you code the Agent Script file to ensure that it's valid. If the validation fails, the command
outputs the list of syntax errors, a brief description of the error, and the location in the Agent Script file where the error occurred.

This command uses the API name of the authoring bundle. If you don't provide an API name with the --api-name flag, the command
searches the current DX project and outputs a list of authoring bundles that it found for you to choose from.

Examples for **`agent validate authoring-bundle`**

Validate an authoring bundle by being prompted for its API name; use your default org:

```
   sf agent validate authoring-bundle

```

Validate an authoring bundle with API name MyAuthoringBundle; use the org with alias "my-dev-org":

```
   sf agent validate authoring-bundle --api-name MyAuthoringBundle --target-org my-dev-org

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

**`-n`** **|** **`--api-name API-NAME`**
Optional

API name of the authoring bundle you want to validate; if not specified, the command provides a list that you can choose from.

Type: option


### Salesforce CLI Command Reference alias Commands alias Commands

Use the alias commands to manage your aliases.

#### alias list

List all aliases currently set on your local computer.

#### alias set

Set one or more aliases on your local computer.

alias unset
Unset one or more aliases that are currently set on your local computer.

#### **`alias list`**

List all aliases currently set on your local computer.

#### Description for alias list

Aliases are global, which means that you can use all the listed aliases in any Salesforce DX project on your computer.

#### Examples for alias list

List all the aliases you've set:

```
   sf alias list

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

#### Aliases for alias list

```
   force:alias:list

#### **`alias set`**

```

Set one or more aliases on your local computer.


Salesforce CLI Command Reference alias Commands

Description for **`alias set`**

Aliases are user-defined short names that make it easier to use the CLI. For example, users often set an alias for a scratch org usernames
because they're long and unintuitive. Check the --help of a CLI command to determine where you can use an alias.

You can associate an alias with only one value at a time. If you set an alias multiple times, the alias points to the most recent value. Aliases
are global; after you set an alias, you can use it in any Salesforce DX project on your computer.

Use quotes to specify an alias value that contains spaces. You typically use an equal sign to set your alias, although you don't need it if
you're setting a single alias in a command.

Examples for **`alias set`**

Set an alias for a scratch org username:

```
   sf alias set my-scratch-org=test-sadbiytjsupn@example.com

```

Set multiple aliases with a single command:

```
   sf alias set my-scratch-org=test-sadbiytjsupn@example.com

   my-other-scratch-org=test-ss0xut7txzxf@example.com

```

Set an alias that contains spaces:

```
   sf alias set my-alias='alias with spaces'

```

Set a single alias without using an equal sign:

```
   sf alias set my-scratch-org test-ss0xut7txzxf@example.com

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

Aliases for **`alias set`**

```
   force:alias:set

#### **`alias unset`**

```

Unset one or more aliases that are currently set on your local computer.

#### Description for alias unset

Aliases are global, so when you unset one it's no longer available in any Salesforce DX project.


### Salesforce CLI Command Reference apex Commands

Examples for **`alias unset`**

Unset an alias:

```
   sf alias unset my-alias

```

Unset multiple aliases with a single command:

```
   sf alias unset my-alias my-other-alias

```

Unset all aliases:

```
   sf alias unset --all [--no-prompt]

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

**`-a`** **|** **`--all`**
Optional

Unset all currently set aliases.

Type: boolean

**`-p`** **|** **`--no-prompt`**
Optional

Don't prompt the user for confirmation when unsetting all aliases.

Type: boolean

Aliases for **`alias unset`**

```
   force:alias:unset

### apex Commands

```

Use the apex commands to create Apex classes, execute anonymous blocks, view your logs, run Apex tests, and view Apex test results.

apex get log
Fetch the specified log or given number of most recent logs from the org.

apex get test
Display test results for a specific asynchronous test run.


Salesforce CLI Command Reference apex Commands

apex list log
Display a list of IDs and general information about debug logs.

apex run
Execute anonymous Apex code entered on the command line or from a local file.

apex run test
Invoke Apex tests in an org.

apex tail log
Activate debug logging and display logs in the terminal.

#### **`apex get log`**

Fetch the specified log or given number of most recent logs from the org.

#### Description for apex get log

To get the IDs for your debug logs, run "sf apex log list". Executing this command without flags returns the most recent log.

#### Examples for apex get log

Fetch the log in your default org using an ID:

```
   sf apex get log --log-id <log id>

```

Fetch the log in the org with the specified username using an ID:

```
   sf apex get log --log-id <log id> --target-org me@my.org

```

Fetch the two most recent logs in your default org:

```
   sf apex get log --number 2

```

Similar to previous example, but save the two log files in the specified directory:

```
   sf apex get log --output-dir /Users/sfdxUser/logs --number 2

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


Salesforce CLI Command Reference apex Commands

Type: option

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

**`-i`** **|** **`--log-id LOG-ID`**
Optional

ID of the specific log to display.

Type: option

**`-n`** **|** **`--number NUMBER`**
Optional

Number of the most recent logs to display.

Type: option

**`-d`** **|** **`--output-dir OUTPUT-DIR`**
Optional

Directory for saving the log files.

The location can be an absolute path or relative to the current working directory. The default is the current directory.

Type: option

Aliases for **`apex get log`**

```
   force:apex:log:get

#### **`apex get test`**

```

Display test results for a specific asynchronous test run.

#### Description for apex get test

Provide a test run ID to display test results for an enqueued or completed asynchronous test run. The test run ID is displayed after running
the "sf apex test run" command.

To see code coverage results, use the --code-coverage flag with --result-format. The output displays a high-level summary of the test
run and the code coverage values for classes in your org. If you specify human-readable result format, use the --detailed-coverage flag
to see detailed coverage results for each test method run.

#### Examples for apex get test

Display test results for your default org using a test run ID:

```
   sf apex get test --test-run-id <test run id>

```

Similar to previous example, but output the result in JUnit format:

```
   sf apex get test --test-run-id <test run id> --result-format junit

```


Salesforce CLI Command Reference apex Commands

Also retrieve code coverage results and output in JSON format:

```
   sf apex get test --test-run-id <test run id> --code-coverage --json

```

Specify a directory in which to save the test results from the org with the specified username (rather than your default org):

```
   sf apex get test --test-run-id <test run id> --code-coverage --output-dir <path to outputdir>

    --target-org me@myorg'

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

**`-i`** **|** **`--test-run-id TEST-RUN-ID`**
Required

ID of the test run.

Type: option

**`-c`** **|** **`--code-coverage`**
Optional

Retrieve code coverage results.

Type: boolean

```
   --detailed-coverage
```

Optional

Display detailed code coverage per test.

Type: boolean

**`-d`** **|** **`--output-dir OUTPUT-DIR`**
Optional

Directory in which to store test result files.

Type: option


Salesforce CLI Command Reference apex Commands

**`-r`** **|** **`--result-format RESULT-FORMAT`**
Optional

Format of the test results.

Type: option

Permissible values are: human, tap, junit, json

Default value: human

```
   --concise
```

Optional

Display only failed test results; works with human-readable output only.

Type: boolean

Aliases for **`apex get test`**

```
   force:apex:test:report

#### **`apex list log`**

```

Display a list of IDs and general information about debug logs.

#### Description for apex list log

Run this command in a project to list the IDs and general information for all debug logs in your default org.

To fetch a specific log from your org, obtain the ID from this command's output, then run the “sf apex log get” command.

#### Examples for apex list log

List the IDs and information about the debug logs in your default org:

```
   sf apex list log

```

Similar to previous example, but use the org with the specified username:

```
   sf apex list log --target-org me@my.org

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


Salesforce CLI Command Reference apex Commands

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

Aliases for **`apex list log`**

```
   force:apex:log:list

#### **`apex run`**

```

Execute anonymous Apex code entered on the command line or from a local file.

#### Description for apex run

If you don’t run this command from within a Salesforce DX project, you must specify the —-target-org flag.

To execute your code interactively, run this command with no flags. At the prompt, enter all your Apex code; press CTRL-D when you're
finished. Your code is then executed in a single execute anonymous request.

For more information, see "Anonymous Blocks" in the Apex Developer Guide.

#### Examples for apex run

Execute the Apex code that's in the ~/test.apex file in the org with the specified username:

```
   sf apex run --target-org testusername@salesforce.org --file ~/test.apex

```

Similar to previous example, but execute the code in your default org:

```
   sf apex run --file ~/test.apex

```

Run the command with no flags to start interactive mode; the code will execute in your default org when you exit. At the prompt, start
type Apex code and press the Enter key after each line. Press CTRL+D when finished.

```
   sf apex run

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


Salesforce CLI Command Reference apex Commands

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

**`-f`** **|** **`--file FILE`**
Optional

Path to a local file that contains Apex code.

Type: option

#### Aliases for apex run

```
   force:apex:execute

#### **`apex run test`**

```

Invoke Apex tests in an org.

#### Description for apex run test

Specify which tests to run by using the --class-names, --suite-names, or --tests flags. Alternatively, use the --test-level flag to run all the
tests in your org, local tests, or specified tests.

To see code coverage results, use the --code-coverage flag with --result-format. The output displays a high-level summary of the test
run and the code coverage values for classes in your org. If you specify human-readable result format, use the --detailed-coverage flag
to see detailed coverage results for each test method run.

By default, Apex tests run asynchronously and immediately return a test run ID. You can use the --wait flag to specify the number of
minutes to wait; if the tests finish in that timeframe, the command displays the results. If the tests haven't finished by the end of the wait
time, the command displays a test run ID. Use the "sf apex get test --test-run-id" command to get the results.

To run both Apex and Flow tests together, run the "sf logic run test" CLI command, which has similar flags as this command, but expands
the --tests flag to also include Flow tests.

You must have the "View All Data" system permission to use this command. The permission is disabled by default and can be enabled
only by a system administrator.

NOTE: The testRunCoverage value (JSON and JUnit result formats) is a percentage of the covered lines and total lines from all the Apex
classes evaluated by the tests in this run.


Salesforce CLI Command Reference apex Commands

Examples for **`apex run test`**

Run all Apex tests and suites in your default org:

```
   sf apex run test

```

Run the specified Apex test classes in your default org and display results in human-readable form:

```
   sf apex run test --class-names MyClassTest --class-names MyOtherClassTest --result-format

    human

```

Run the specified Apex test suites in your default org and include code coverage results and additional details:

```
   sf apex run test --suite-names MySuite --suite-names MyOtherSuite --code-coverage

   --detailed-coverage

```

Run the specified Apex tests in your default org and display results in human-readable output:

```
   sf apex run test --tests MyClassTest.testCoolFeature --tests MyClassTest.testAwesomeFeature

    --tests AnotherClassTest --tests namespace.TheirClassTest.testThis --result-format human

```

Run all tests in the org with the specified username with the specified test level; save the output to the specified directory:

```
   sf apex run test --test-level RunLocalTests --output-dir <path to outputdir> --target-org

    me@my.org

```

Run all tests in the org asynchronously:

```
   sf apex run test --target-org myscratch

```

Run all tests synchronously; the command waits to display the test results until all tests finish:

```
   sf apex run test --synchronous

```

Run specific tests using the --test-level flag:

```
   sf apex run test --test-level RunLocalTests

```

Run Apex tests on all the methods in the specified class; output results in Test Anything Protocol (TAP) format and request code coverage
results:

```
   sf apex run test --class-names TestA --class-names TestB --result-format tap --code-coverage

```

Run Apex tests on methods specified using the standard Class.method notation; if you specify a test class without a method, the command
runs all methods in the class:

```
   sf apex run test --tests TestA.excitingMethod --tests TestA.boringMethod --tests TestB

```

Run Apex tests on methods specified using the standard Class.method notation with a namespace:

```
   sf apex run test --tests ns.TestA.excitingMethod --tests ns.TestA.boringMethod --tests

   ns.TestB

```

Flags

```
   --json
```

Optional

Format output as json.

Type: boolean


Salesforce CLI Command Reference apex Commands

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

**`-c`** **|** **`--code-coverage`**
Optional

Retrieve code coverage results.

Type: boolean

**`-d`** **|** **`--output-dir OUTPUT-DIR`**
Optional

Directory in which to store test run files.

Type: option

**`-l`** **|** **`--test-level TEST-LEVEL`**
Optional

Level of tests to run; default is RunLocalTests.

Here's what the levels mean:

      - RunSpecifiedTests — Only the tests that you specify in the runTests option are run. Code coverage requirements differ from the
default coverage requirements when using this test level. The executed tests must cover each class and trigger in the deployment
package for a minimum of 75% code coverage. This coverage is computed for each class and triggers individually, and is different
than the overall coverage percentage.

      - RunLocalTests — All local tests in your org, including tests that originate from no-namespaced unlocked packages, are run. The
tests that originate from installed managed packages and namespaced unlocked packages aren't run. This test level is the default
for production deployments that include Apex classes or triggers.

      - RunAllTestsInOrg — All tests are run. The tests include all tests in your org.

Type: option

Permissible values are: RunLocalTests, RunAllTestsInOrg, RunSpecifiedTests

**`-n`** **|** **`--class-names CLASS-NAMES`**
Optional

Apex test class names to run; default is all classes.

If you select --class-names, you can't specify --suite-names or --tests.

For multiple classes, repeat the flag for each.

--class-names Class1 --class-names Class2


Salesforce CLI Command Reference apex Commands

Type: option

**`-r`** **|** **`--result-format RESULT-FORMAT`**
Optional

Format of the test results.

Type: option

Permissible values are: human, tap, junit, json

Default value: human

**`-s`** **|** **`--suite-names SUITE-NAMES`**
Optional

Apex test suite names to run.

If you select --suite-names, you can't specify --class-names or --tests.

For multiple suites, repeat the flag for each.

--suite-names Suite1 --suite-names Suite2

Type: option

**`-t`** **|** **`--tests TESTS`**
Optional

Apex test class names or IDs and, if applicable, test methods to run; default is all tests.

If you specify --tests, you can't specify --class-names or --suite-names

For multiple tests, repeat the flag for each.

--tests Test1 --tests Test2

Type: option

**`-i`** **|** **`--poll-interval POLL-INTERVAL`**
Optional

Number of seconds to wait between retries.

Type: option

**`-w`** **|** **`--wait WAIT`**
Optional

Sets the streaming client socket timeout in minutes; specify a longer wait time if timeouts occur frequently.

Type: option

**`-y`** **|** **`--synchronous`**
Optional

Runs test methods from a single Apex class synchronously; if not specified, tests are run asynchronously.

Type: boolean

**`-v`** **|** **`--detailed-coverage`**
Optional

Display detailed code coverage per test.

Type: boolean

```
   --concise
```

Optional


Salesforce CLI Command Reference apex Commands

Display only failed test results; works with human-readable output only.

Type: boolean

Aliases for **`apex run test`**

```
   force:apex:test:run

#### **`apex tail log`**

```

Activate debug logging and display logs in the terminal.

#### Description for apex tail log

You can also pipe the logs to a file.

#### Examples for apex tail log

Activate debug logging:

```
   sf apex tail log

```

Specify a debug level:

```
   sf apex tail log --debug-level MyDebugLevel

```

Skip the trace flag setup and apply default colors:

```
   sf apex tail log --color --skip-trace-flag

```

Flags

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

**`-c`** **|** **`--color`**
Optional

Apply default colors to noteworthy log lines.

Type: boolean


### Salesforce CLI Command Reference api Commands

**`-d`** **|** **`--debug-level DEBUG-LEVEL`**
Optional

Debug level to set on the DEVELOPER_LOG trace flag for your user.

Type: option

**`-s`** **|** **`--skip-trace-flag`**
Optional

Skip trace flag setup. Assumes that a trace flag and debug level are fully set up.

Type: boolean

Aliases for **`apex tail log`**

```
   force:apex:log:tail

### api Commands

```

Commands to interact with API calls.

#### api request graphql (Beta)

Execute a GraphQL statement.

api request rest (Beta)
Make an authenticated HTTP request using the Salesforce REST API.

#### api request graphql (Beta)

Execute a GraphQL statement.

Note: This feature is a Beta Service. Customers may opt to try such Beta Service in its sole discretion. Any use of the Beta Service
is subject to the applicable Beta Services Terms provided at Agreements and Terms
[(https://www.salesforce.com/company/legal/agreements/).](https://www.salesforce.com/company/legal/agreements/)

#### Description for api request graphql

Specify the GraphQL statement with the "--body" flag, either directly at the command line or with a file that contains the statement. You
can query Salesforce records using a "query" statement or use mutations to modify Salesforce records.

This command uses the GraphQL API to query or modify Salesforce objects. For details about the API, and examples of queries and
mutations, see https://developer.salesforce.com/docs/platform/graphql/guide/graphql-about.html.

#### Examples for api request graphql

Execute a GraphQL query on the Account object by specifying the query directly to the "--body" flag; the command uses your default
org:

```
   sf api request graphql --body "query accounts { uiapi { query { Account { edges { node {

   Id \n Name { value } } } } } } }"

```


Salesforce CLI Command Reference api Commands

Read the GraphQL statement from a file called "example.txt" and execute it on an org with alias "my-org":

```
   sf api request graphql --body example.txt --target-org my-org

```

Pipe the GraphQL statement that you want to execute from standard input to the command:

```
   $ echo graphql | sf api request graphql --body 
```

Write the output of the command to a file called "output.txt" and include the HTTP response status and headers:

```
   sf api request graphql --body example.txt --stream-to-file output.txt --include

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

**`-S`** **|** **`--stream-to-file STREAM-TO-FILE`**
Optional

Stream responses to a file.

Type: option

**`-i`** **|** **`--include`**
Optional

Include the HTTP response status and headers in the output.

Type: boolean

```
   --body BODY
```

Required

File or content with the GraphQL statement. Specify "-" to read from standard input.

Type: option


Salesforce CLI Command Reference api Commands

#### api request rest (Beta)

Make an authenticated HTTP request using the Salesforce REST API.

Note: This feature is a Beta Service. Customers may opt to try such Beta Service in its sole discretion. Any use of the Beta Service
is subject to the applicable Beta Services Terms provided at Agreements and Terms
[(https://www.salesforce.com/company/legal/agreements/).](https://www.salesforce.com/company/legal/agreements/)

#### Description for api request rest

When sending the HTTP request with the "--body" flag, you can specify the request directly at the command line or with a file that
contains the request.

For a full list of supported REST endpoints and resources, see
https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_list.htm.

#### Examples for api request rest

List information about limits in the org with alias "my-org":

```
   sf api request rest 'services/data/v56.0/limits' --target-org my-org

```

List all endpoints in your default org; write the output to a file called "output.txt" and include the HTTP response status and headers:

```
   sf api request rest '/services/data/v56.0/' --stream-to-file output.txt --include

```

Get the response in XML format by specifying the "Accept" HTTP header:

```
   sf api request rest '/services/data/v56.0/limits' --header 'Accept: application/xml'

```

Create an account record using the POST method; specify the request details directly in the "--body" flag:

```
   sf api request rest /services/data/v56.0/sobjects/account --body "{\"Name\" : \"Account

   from REST API\",\"ShippingCity\" : \"Boise\"}" --method POST

```

Create an account record using the information in a file called "info.json" (note the @ prefixing the file name):

```
   sf api request rest '/services/data/v56.0/sobjects/account' --body @info.json --method

   POST

```

Update an account record using the PATCH method:

```
   sf api request rest '/services/data/v56.0/sobjects/account/<Account ID>' --body

   "{\"BillingCity\": \"San Francisco\"}" --method PATCH

```

Store the values for the request header, body, and so on, in a file, which you then specify with the --file flag; see the description of --file
for more information:

```
   sf api request rest --file myFile.json

```

Flags

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option


Salesforce CLI Command Reference api Commands

**`-o`** **|** **`--target-org TARGET-ORG`**
Required

Username or alias of the target org. Not required if the `target-org` configuration variable is already set.

Type: option

**`-i`** **|** **`--include`**
Optional

Include the HTTP response status and headers in the output.

Type: boolean

**`-X`** **|** **`--method METHOD`**
Optional

HTTP method for the request.

Type: option

Permissible values are: GET, POST, PUT, PATCH, HEAD, DELETE, OPTIONS, TRACE

**`-H`** **|** **`--header HEADER`**
Optional

HTTP header in "key:value" format.

Type: option

**`-f`** **|** **`--file FILE`**
Optional

JSON file that contains values for the request header, body, method, and URL.

Use this flag instead of specifying the request details with individual flags, such as --body or --method. This schema defines how to
create the JSON file:

{

url: { raw: string } | string;

method: 'GET', 'POST', 'PUT', 'PATCH', 'HEAD', 'DELETE', 'OPTIONS', 'TRACE';

description?: string;

header: string | Array<Record<string, string>>;

body: { mode: 'raw' | 'formdata'; raw: string; formdata: FormData };

}

Salesforce CLI defined this schema to be mimic Postman schemas; both share similar properties. The CLI's schema also supports
Postman Collections to reuse and share requests. As a result, you can build an API call using Postman, export and save it to a file,
and then use the file as a value to this flag. For information about Postman, see https://learning.postman.com/.

Here's a simple example of a JSON file that contains values for the request URL, method, and body:

{

"url": "sobjects/Account/<Account ID>",

"method": "PATCH",

"body" : {

"mode": "raw",

"raw": {


### Salesforce CLI Command Reference cmdt Commands

"BillingCity": "Boise"

}

}

}

See more examples in the plugin-api test directory, including JSON files that use "formdata" to define collections:
https://github.com/salesforcecli/plugin-api/tree/main/test/test-files/data-project.

Type: option

**`-S`** **|** **`--stream-to-file STREAM-TO-FILE`**
Optional

Stream responses to a file.

Type: option

**`-b`** **|** **`--body BODY`**
Optional

File or content for the body of the HTTP request. Specify "-" to read from standard input or "" for an empty body. If passing a file,
prefix the filename with '@'.

Type: option

### cmdt Commands

Generate custom metadata types and their records.

#### cmdt generate field

Generate a field for a custom metadata type based on the provided field type.

cmdt generate fromorg
Generate a custom metadata type and all its records from a Salesforce object.

cmdt generate object
Generate a new custom metadata type in the current project.

cmdt generate record
Generate a new record for a given custom metadata type in the current project.

cmdt generate records
Generate new custom metadata type records from a CSV file.

#### **`cmdt generate field`**

Generate a field for a custom metadata type based on the provided field type.

#### Description for cmdt generate field

Similar to a custom object, a custom metadata type has a list of custom fields that represent aspects of the metadata.

This command creates a metadata file that describes the new custom metadata type field. By default, the file is created in a "fields"
directory in the current directory. Use the --output-directory to generate the file in the directory that contains the custom metadata type
metdata files, such as "force-app/main/default/objects/MyCmdt__mdt" for the custom metadata type called MyCmdt.


Salesforce CLI Command Reference cmdt Commands

Examples for **`cmdt generate field`**

Generate a metadata file for a custom checkbox field and add the file to the MyCmdt__mdt/fields directory:

```
   sf cmdt generate field --name MyCheckboxField --type Checkbox --output-directory

   force-app/main/default/objects/MyCmdt__mdt

```

Generate a metadata file for a custom picklist field and add a few values:

```
   sf cmdt generate field --name MyPicklistField --type Picklist --picklist-values A

   --picklist-values B --picklist-values C --output-directory

   force-app/main/default/objects/MyCmdt__mdt

```

Generate a metadata file for a custom number field and specify 2 decimal places:

```
   sf cmdt generate field --name MyNumberField --type Number --decimal-places 2

   --output-directory force-app/main/default/objects/MyCmdt__mdt

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

Unique name for the field.

Type: option

**`-f`** **|** **`--type TYPE`**
Required

Type of the field.

You can't use this command to create a custom metadata type field of type "Metadata Relationship". Use the Salesforce Setup UI
instead.

Type: option

Permissible values are: Checkbox, Date, DateTime, Email, Number, Percent, Phone, Picklist, Text, TextArea, LongTextArea, Url

**`-p`** **|** **`--picklist-values PICKLIST-VALUES`**
Optional

Picklist values; required for picklist fields.

Type: option

**`-s`** **|** **`--decimal-places DECIMAL-PLACES`**
Optional

Number of decimal places to use for number or percent fields.


Salesforce CLI Command Reference cmdt Commands

The value must be greater than or equal to zero. Default value is 0.

Type: option

**`-l`** **|** **`--label LABEL`**
Optional

Label for the field.

Type: option

**`-d`** **|** **`--output-directory OUTPUT-DIRECTORY`**
Optional

Directory to store newly-created field definition files.

New files are automatically created in the "fields" directory. The location can be an absolute path or relative to the current working
directory. The default is the current directory.

Type: option

Aliases for **`cmdt generate field`**

```
   force:cmdt:field:create

   cmdt:field:create

#### **`cmdt generate fromorg`**

```

Generate a custom metadata type and all its records from a Salesforce object.

#### Description for cmdt generate fromorg

Use this command to migrate existing custom objects or custom settings in an org to custom metadata types. If a field of the Salesforce
object is of an unsupported type, the field type is automatically converted to text. Run "sf cmdt generate field --help" to see the list of
supported cmdt field types, listed in the --type flag summary. Use the --ignore-unsupported to ignore these fields.

This command creates the metadata files that describe the new custom metadata type and its fields in the
"force-app/main/default/objects/TypeName__mdt" directory by default, where "TypeName" is the value of the required --dev-name
flag. Use --type-output-directory to create them in a different directory.

#### Examples for cmdt generate fromorg

Generate a custom metadata type from a custom object called MySourceObject__c in your default org:

```
   sf cmdt generate fromorg --dev-name MyCMDT --sobject MySourceObject__c

```

Generate a custom metadata type from a custom object in an org with alias my-scratch-org; ignore unsupported field types instead of
converting them to text:

```
   sf cmdt generate fromorg --dev-name MyCMDT --sobject MySourceObject__c --ignore-unsupported

    --target-org my-scratch-org

```

Generate a protected custom metadata type from a custom object:

```
   sf cmdt generate fromorg --dev-name MyCMDT --sobject MySourceObject__c --visibility Protected

```


Salesforce CLI Command Reference cmdt Commands

Generate a protected custom metadata type from a custom setting with a specific singular and plural label:

```
   sf cmdt generate fromorg --dev-name MyCMDT --label "My CMDT" --plural-label "My CMDTs"

   --sobject MySourceSetting__c --visibility Protected

```

Generate a custom metadata type and put the resulting metadata files in the specified directory:

```
   sf cmdt generate fromorg --dev-name MyCMDT --sobject MySourceObject__c

   --type-output-directory path/to/my/cmdt/directory

```

Generate a custom metadata type and put the resulting record metadata file(s) in the specified directory:

```
   sf cmdt generate fromorg --dev-name MyCMDT --sobject MySourceObject__c --records-output-dir

    path/to/my/cmdt/record/directory

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

**`-n`** **|** **`--dev-name DEV-NAME`**
Required

Name of the custom metadata type.

Type: option

**`-l`** **|** **`--label LABEL`**
Optional

Label for the custom metadata type.

Type: option

**`-p`** **|** **`--plural-label PLURAL-LABEL`**
Optional

Plural version of the label value; if blank, uses label.

Type: option


Salesforce CLI Command Reference cmdt Commands

**`-v`** **|** **`--visibility VISIBILITY`**
Optional

Who can see the custom metadata type.

For more information on what each option means, see this topic in Salesforce Help:
https://help.salesforce.com/s/articleView?id=sf.custommetadatatypes_ui_create.htm&type=5.

Type: option

Permissible values are: PackageProtected, Protected, Public

Default value: Public

**`-s`** **|** **`--sobject SOBJECT`**
Required

API name of the source Salesforce object used to generate the custom metadata type.

Type: option

**`-i`** **|** **`--ignore-unsupported`**
Optional

Ignore unsupported field types.

In this context, "ignore" means that the fields aren't created. The default behavior is to create fields of type text and convert the field
values to text.

Type: boolean

**`-d`** **|** **`--type-output-directory TYPE-OUTPUT-DIRECTORY`**
Optional

Directory to store newly-created custom metadata type files.

Type: option

Default value: force-app/main/default/objects

**`-r`** **|** **`--records-output-dir RECORDS-OUTPUT-DIR`**
Optional

Directory to store newly-created custom metadata record files.

Type: option

Default value: force-app/main/default/customMetadata

Aliases for **`cmdt generate fromorg`**

```
   force:cmdt:generate

#### **`cmdt generate object`**

```

Generate a new custom metadata type in the current project.

#### Description for cmdt generate object

This command creates a metadata file that describes the new custom metadata type. By default, the file is created in the
MyCustomType__mdt directory in the current directory, where MyCustomType is the value of the required --type-name flag. Use the
--output-directory to generate the file in a package directory with other custom metadata types, such as "force-app/main/default/objects".


Salesforce CLI Command Reference cmdt Commands

Examples for **`cmdt generate object`**

Generate a custom metadata type with developer name 'MyCustomType'; this name is also used as the label:

```
   sf cmdt generate object --type-name MyCustomType

```

Generate a protected custom metadata type with a specific label:

```
   sf cmdt generate object --type-name MyCustomType --label "Custom Type" --plural-label

   "Custom Types" --visibility Protected

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

**`-n`** **|** **`--type-name TYPE-NAME`**
Required

Unique object name for the custom metadata type.

The name can contain only underscores and alphanumeric characters, and must be unique in your org. It must begin with a letter,
not include spaces, not end with an underscore, and not contain two consecutive underscores.

Type: option

**`-l`** **|** **`--label LABEL`**
Optional

Label for the custom metadata type.

Type: option

**`-p`** **|** **`--plural-label PLURAL-LABEL`**
Optional

Plural version of the label value; if blank, uses label.

Type: option

**`-v`** **|** **`--visibility VISIBILITY`**
Optional

Who can see the custom metadata type.

For more information on what each option means, see this topic in Salesforce Help:
https://help.salesforce.com/s/articleView?id=sf.custommetadatatypes_ui_create.htm&type=5.

Type: option

Permissible values are: PackageProtected, Protected, Public

Default value: Public


Salesforce CLI Command Reference cmdt Commands

**`-d`** **|** **`--output-directory OUTPUT-DIRECTORY`**
Optional

Directory to store the newly-created custom metadata type files

The location can be an absolute path or relative to the current working directory. The default is the current directory.

Type: option

Aliases for **`cmdt generate object`**

```
   force:cmdt:create

   cmdt:create

#### **`cmdt generate record`**

```

Generate a new record for a given custom metadata type in the current project.

#### Description for cmdt generate record

The custom metadata type must already exist in your project. You must specify a name for the new record. Use name=value pairs to
specify the values for the fields, such as MyTextField="some text here" or MyNumberField=32.

#### Examples for cmdt generate record

Create a record metadata file for custom metadata type 'MyCMT' with specified values for two custom fields:

```
   sf cmdt generate record --type-name MyCMT__mdt --record-name MyRecord My_Custom_Field_1=Foo

    My_Custom_Field_2=Bar

```

Create a protected record metadata file for custom metadata type 'MyCMT' with a specific label and values specified for two custom
fields:

```
   sf cmdt generate record --type-name MyCMT__mdt --record-name MyRecord --label "My Record"

    --protected true My_Custom_Field_1=Foo My_Custom_Field_2=Bar

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

**`-t`** **|** **`--type-name TYPE-NAME`**
Required

API name of the custom metadata type to create a record for; must end in "__mdt".


Salesforce CLI Command Reference cmdt Commands

Type: option

**`-n`** **|** **`--record-name RECORD-NAME`**
Required

Name of the new record.

Type: option

**`-l`** **|** **`--label LABEL`**
Optional

Label for the new record.

Type: option

**`-p`** **|** **`--protected PROTECTED`**
Optional

Protect the record when it's in a managed package.

Protected records can only be accessed by code in the same managed package namespace.

Type: option

Permissible values are: true, false

Default value: false

**`-i`** **|** **`--input-directory INPUT-DIRECTORY`**
Optional

Directory from which to get the custom metadata type definition from.

Type: option

Default value: force-app/main/default/objects

**`-d`** **|** **`--output-directory OUTPUT-DIRECTORY`**
Optional

Directory to store newly-created custom metadata record files.

Type: option

Default value: force-app/main/default/customMetadata

#### Aliases for cmdt generate record

```
   force:cmdt:record:create

   cmdt:record:create

#### **`cmdt generate records`**

```

Generate new custom metadata type records from a CSV file.

#### Description for cmdt generate records

The custom metadata type must already exist in your project. By default, the Name column is used to determine the record name; use
the --name-column flag to specify a different column.


Salesforce CLI Command Reference cmdt Commands

Examples for **`cmdt generate records`**

Generate record metadata files from values in a CSV file for the custom metadata type MyCmdt. Use 'Name' as the column that specifies
the record name:

```
   sf cmdt generate records --csv path/to/my.csv --type-name MyCmdt

```

Generate record metadata files from a CSV file in the directory different from the default, and use 'PrimaryKey' as the column that specifies
the record name:

```
   sf cmdt generate records --csv path/to/my.csv --type-name MyCmdt --input-directory

   path/to/my/cmdt/directory --name-column "PrimaryKey"

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

**`-f`** **|** **`--csv CSV`**
Required

Pathname of the CSV file.

Type: option

**`-t`** **|** **`--type-name TYPE-NAME`**
Required

API name of the custom metadata type to create a record for.

The '__mdt' suffix is appended to the end of the name if it's omitted.

Type: option

**`-i`** **|** **`--input-directory INPUT-DIRECTORY`**
Optional

Directory from which to get the custom metadata type definition from.

Type: option

Default value: force-app/main/default/objects

**`-d`** **|** **`--output-directory OUTPUT-DIRECTORY`**
Optional

Directory to store newly-created custom metadata record files.

Type: option

Default value: force-app/main/default/customMetadata

**`-n`** **|** **`--name-column NAME-COLUMN`**
Optional


### Salesforce CLI Command Reference code-analyzer Commands

Column used to determine the name of the record.

Type: option

Default value: Name

Aliases for **`cmdt generate records`**

```
   force:cmdt:record:insert

   cmdt:record:insert

### code-analyzer Commands

```

Analyze your code to ensure it adheres to best practices.

#### code-analyzer config

Output the current state of configuration for Code Analyzer.

code-analyzer rules
List the rules that are available to analyze your code.

code-analyzer run
Analyze your code with a selection of rules to ensure good coding practices.

#### **`code-analyzer config`**

Output the current state of configuration for Code Analyzer.

#### Description for code-analyzer config

Code Analyzer gives you the ability to configure settings that modify Code Analyzer's behavior, to override the tags and severity levels
of rules, and to configure the engine specific settings. Use this command to see the current state of this configuration. You can also save
this state to a YAML-formatted file that you can modify for your needs.

To apply a custom configuration with Code Analyzer, either keep your custom configuration settings in a `code-analyzer.yml` file located
in the current folder from which you are executing commands, or specify the location of your custom configuration file to the Code
Analyzer commands with the --config-file flag.

We're continually improving Salesforce Code Analyzer. Tell us what you think! Give feedback at https://sfdc.co/CodeAnalyzerFeedback.

#### Examples for code-analyzer config

Display the current state of the Code Analyzer configuration using the default behavior: display top level configuration, display the engine
and rule override settings associated with all the rules; and automatically apply any existing custom configuration settings found in a
`code-analyzer.yml` or `code-analyzer.yaml` file in the current folder:

```
   sf code-analyzer config

```

This example is identical to the previous one, assuming that `./code-analyzer.yml` exists in your current folder.

```
   sf code-analyzer config --config-file ./code-analyzer.yml --rule-selector all

```


Salesforce CLI Command Reference code-analyzer Commands

Write the current state of configuration to the file `code-analyzer.yml`, including any configuration from an existing `code-analyzer.yml`
file. The command preserves all values from the original config, but overwrites any comments:

```
   sf code-analyzer config --config-file ./code-analyzer.yml --output-file code-analyzer.yml

```

Display the configuration state for just the recommended rules, instead of all the rules:

```
   sf code-analyzer config --rule-selector Recommended

```

Display all the default rule values for the recommended rules, instead of only the rule values you've explicitly overriden in your
`code-analyzer.yml` file. By default, only overriden rule values are displayed unless you specify the `--include-unmodified-rules` flag:

```
   sf code-analyzer config --rule-selector Recommended --include-unmodified-rules

```

Display the configuration state associated with all the rules that are applicable to the files targeted within the folder `./src`:

```
   sf code-analyzer config --target ./src

```

Display any relevant configuration settings associated with the rule name 'no-undef' from the 'eslint' engine:

```
   sf code-analyzer config --rule-selector eslint:no-undef

```

Display any relevant configuration settings associated with PMD rules whose severity is 2 or 3:

```
   sf code-analyzer config --rule-selector "pmd:(2,3)"

```

Load an existing configuration file called `existing-config.yml`, and then write the configuration to a new file called `new-config.yml`,
the configuration state that is applicable to all rules that are relevant to the workspace located in the current folder:

```
   sf code-analyzer config --config-file ./existing-config.yml --workspace . --output-file

   ./subfolder-config.yml

```

Flags

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option

**`-w`** **|** **`--workspace WORKSPACE`**
Optional

Set of files that make up your workspace.

Use the `--workspace` flag to display only the configuration associated with the rules that apply to the files that make up your
workspace. Typically, a workspace is a single project folder that contains all your files. But it can also consist of one or more folders,
one or more files, and use glob patterns (wildcards). If you specify this flag multiple times, then your workspace is the sum of the
files and folders.

This command uses the types of files in the workspace, such as JavaScript or Typescript, to determine the applicable configuration
state. For example, if your workspace contains only JavaScript files, then the command doesn't display configuration state associated
with TypeScript rules. The command uses a file's extension to determine what kind of file it is, such as ".ts" for TypeScript.

Some engines can be configured to add additional rules based on what it finds in your workspace. For example, if you set the
engines.eslint.auto_discover_eslint_config value of your `code-analyzer.yml` file to true, then supplying your workspace allows the
"eslint" engine to examine your files in order to find ESLint configuration files that could potentially add in additional rules.

If you specify `--target` but not `--workspace`, then the current folder '.' is used as your workspace.


Salesforce CLI Command Reference code-analyzer Commands

Type: option

**`-t`** **|** **`--target TARGET`**
Optional

Subset of files within your workspace that you want to target for analysis.

Use the `--target` flag to display the configuration state associated with the rules that apply to only a subset of targeted files within
your workspace. You can specify a target as a file, a folder, or a glob pattern. If you specify this flag multiple times, then the full list
of targeted files is the sum of the files and folders.

The command uses the type of the targeted files, such as JavaScript or Typescript, to determine which configuration state is applicable.
For example, if you target only JavaScript files, then the command doesn't display the configuration state associated with TypeScript
rules. The command uses a file's extension to determine what kind of file it is, such as ".ts" for TypeScript.

Each targeted file must live within the workspace specified by the `–-workspace` flag.

If you specify `--workspace` but not `--target`, then all the files within your workspace are targeted.

Type: option

**`-r`** **|** **`--rule-selector RULE-SELECTOR`**
Optional

Selection of rules, based on engine name, severity level, rule name, tag, or a combination of criteria separated by colons and commas,
and grouped by parentheses.

Use the `--rule-selector` flag to display only the configuration associated with the rules based on specific criteria. You can select by
engine, such as the rules associated with the "retire-js" or "eslint" engine. Or select by the severity of the rules, such as high or
moderate. You can also select rules using tag values or rule names.

You can further filter the list by combining different criteria using colons to represent logical AND, commas to represent logical OR,
and parentheses to create groupings. For example, `--rule-selector "pmd:(Performance,Security):2"` reduces the output to only
contain the configuration state associated with PMD rules that have the Performance or Security tag and a severity of 2. You may
also specify the flag multiple times to OR multiple selectors together. For example, `--rule-selector Performance,Security` is equivalent
to `--rule-selector Performance --rule-selector Security`. Note that if you use parentheses in your selector, the selector should be
wrapped in double-quotes.

If you don't specify this flag, then the command uses the "all" rule selector.

Run `sf code-analyzer config --rule-selector Recommended` to display the configuration state associated with just the 'Recommended'
rules, instead of all the rules.

Type: option

Default value: all

**`-c`** **|** **`--config-file CONFIG-FILE`**
Optional

Path to the existing configuration file used to customize the engines and rules.

Use this flag to apply the customizations from a custom Code Analyzer configuration file to be displayed alongside the current Code
Analyzer configuration state.

If you don't specify this flag, then the command looks for and applies a file named `code-analyzer.yml` or `code-analyzer.yaml` in
your current folder.

Type: option

**`-f`** **|** **`--output-file OUTPUT-FILE`**
Optional

Output file to write the configuration state to. The file is written in YAML format.


Salesforce CLI Command Reference code-analyzer Commands

If you specify a file within folder, such as `--output-file ./config/code-analyzer.yml`, the folder must already exist, or you get an error.
If the file already exists, a prompt asks if you want to overwrite it.

If you don't specify this flag, the command outputs the configuration state to the terminal.

Type: option

```
   --include-unmodified-rules
```

Optional

Include unmodified rules in the rule override settings.

The default behavior of the config command is to not include the unmodified rules with their default values in the rule override
settings (for the rules selected via the `–-rule-selector` flag). This default behavior prevents your configuration file from being
unnecessarily large. If you want to include the unmodified rules, in addition to the modified rules, then specify this flag.

Type: boolean

```
   --no-suppressions
```

Optional

Exclude suppressions from the output configuration.

When specified, the 'suppressions' field is not included in the configuration state. Since the 'suppressions' field may contain file or
folder paths specific to a specific path, use this flag to make it easy to share your configuration state to be used for a different
workspace.

Type: boolean

#### **`code-analyzer rules`**

List the rules that are available to analyze your code.

#### Description for code-analyzer rules

You can also view details about the rules, such as the engine it's associated with, tags, and description.

Use this command to determine the exact set of rules to analyze your code. The `code-analyzer run` command has similar flags as this
command, so once you've determined the flag values for this command that list the rules you want to run, you specify the same values
to the `code-analyzer run` command.

We're continually improving Salesforce Code Analyzer. Tell us what you think! Give feedback at https://sfdc.co/CodeAnalyzerFeedback.

#### Examples for code-analyzer rules

List rules using the default behavior: include rules from all engines that have a "Recommended" tag; display the rules using concise table
format; and automatically apply rule or engine overrides if a `code-analyzer.yml` or `code-analyzer.yaml` file exists in the current folder:

```
   sf code-analyzer rules

```

The previous example is equivalent to this example:

```
   sf code-analyzer rules --rule-selector Recommended --view table --config-file

   ./code-analyzer.yml

```

List the recommended rules for the "eslint" engine:

```
   sf code-analyzer rules --rule-selector eslint:Recommended

```


Salesforce CLI Command Reference code-analyzer Commands

List all the rules for the "eslint" engine:

```
   sf code-analyzer rules --rule-selector eslint

```

The previous example is equivalent to this example:

```
   sf code-analyzer rules --rule-selector eslint:all

```

List the details about all rules for all engines; also write the rules in JSON format to a file called "rules.json" in the "out" folder, which must
already exist:

```
   sf code-analyzer rules --rule-selector all --output-file ./out/rules.json --view detail

```

Get a more accurate list of the rules that apply specifically to your workspace (all the files in the current folder):

```
   sf code-analyzer rules --rule-selector all --workspace .

```

List the recommended rules associated with a workspace that targets all the files in the folder "./other-source" and only the Apex class
files (extension .cls) under the folder "./force-app":

```
   sf code-analyzer rules --rule-selector Recommended --workspace . --target ./other-source

   --target ./force-app/**/*.cls

```

List all the "eslint" engine rules that have a moderate severity (3) and the recommended "retire-js" engine rules with any severity:

```
   sf code-analyzer rules --rule-selector eslint:3 --rule-selector retire-js:Recommended

```

List all the "pmd" engine rules that have a severity of moderate (3) or high (2) and the "Performance" tag.

```
   sf code-analyzer rules --rule-selector "pmd:(2,3):Performance"

```

Similar to the previous example, but apply the rule overrides and engine settings from the configuration file called `code-analyzer2.yml`
in the current folder. If, for example, you changed the severity of an "eslint" rule from moderate (3) to high (2) in the configuration file,
then that rule isn't listed:

```
   sf code-analyzer rules --rule-selector eslint:3 --rule-selector retire-js:Recommended

   --config-file ./code-analyzer2.yml

```

List the details of the "getter-return" rule of the "eslint" engine and the rules named "no-inner-declarations" in any engine:

```
   sf code-analyzer rules --rule-selector eslint:getter-return --rule-selector

   no-inner-declarations --view detail

```

List the details of the recommended "eslint" engine rules that have the tag "problem" and high severity level (2) that apply when targeting
the files within the folder "./force-app":

```
   sf code-analyzer rules --rule-selector eslint:Recommended:problem:2 --view detail --target

    ./force-app

```

Flags

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option

**`-w`** **|** **`--workspace WORKSPACE`**
Optional


Salesforce CLI Command Reference code-analyzer Commands

Set of files that make up your workspace.

Use the `--workspace` flag to return a more accurate list of the rules that apply to the files that make up your workspace. Typically,
a workspace is a single project folder that contains all your files. But it can also consist of one or more folders, one or more files, and
use glob patterns (wildcards). If you specify this flag multiple times, then your workspace is the sum of the files and folders.

The command uses the types of files in the workspace, such as JavaScript or Typescript, to determine which rules to list. For example,
if your workspace contains only JavaScript files, the command doesn't list TypeScript rules. The command uses a file's extension to
determine what kind of file it is, such as ".ts" for TypeScript.

Some engines may be configured to add additional rules based on what it finds in your workspace. For example, if you set the
engines.eslint.auto_discover_eslint_config value of your `code-analyzer.yml` file to true, then supplying your workspace allows the
"eslint" engine to examine your files in order to find ESLint configuration files that could potentially add in additional rules.

If you specify `--target` but not `--workspace`, then the current folder '.' is used as your workspace.

Type: option

**`-t`** **|** **`--target TARGET`**
Optional

Subset of files within your workspace that you want to target for analysis.

Use the `--target` flag to return a more accurate list of the rules that apply to only a subset of targeted files within your workspace.
You can specify a target as a file, a folder, or a glob pattern. If you specify this flag multiple times, then the full list of targeted files is
the sum of the files and folders.

The command uses the type of the targeted files, such as JavaScript or Typescript, to determine which rules to list. For example, if
you target only JavaScript files, the command doesn't list TypeScript rules. The command uses a file's extension to determine what
kind of file it is, such as ".ts" for TypeScript.

Each targeted file must live within the workspace specified by the –-workspace flag.

If you specify `--workspace` but not `--target`, then all the files within your workspace are targeted.

Type: option

**`-r`** **|** **`--rule-selector RULE-SELECTOR`**
Optional

Selection of rules, based on engine name, severity level, rule name, tag, or a combination of criteria separated by colons.

Use the `--rule-selector` flag to select the list of rules based on specific criteria. For example, you can select by engine, such as the
rules associated with the "retire-js" or "eslint" engine. Or select by the severity of the rules, such as high or moderate. You can also
select rules using tag values or rule names. Every rule has a name, which is unique within the scope of an engine. Most rules have
tags, although it's not required. An example of a tag is "Recommended".

You can further filter the list by combining different criteria using colons to represent logical AND, commas to represent logical OR,
and parentheses to create groupings. For example, `--rule-selector "pmd:(Performance,Security):2"` lists rules associated only with
the "pmd" engine that have the Security or Performance tags and a high severity (2). You may also specify the flag multiple times
to OR multiple selectors together. For example, `--rule-selector Performance,Security` is equivalent to `--rule-selector Performance
--rule-selector Security`. Note that if you use parentheses in your selector, the selector should be wrapped in double-quotes.

Run `sf code-analyzer rules --rule-selector all` to list the possible values for engine name, rule name, tags, and severity levels that
you can use with this flag.

Type: option

Default value: Recommended

**`-c`** **|** **`--config-file CONFIG-FILE`**
Optional


Salesforce CLI Command Reference code-analyzer Commands

Path to the configuration file used to customize the engines and rules.

Code Analyzer has an internal default configuration for its rule and engine properties. If you want to override these defaults, you can
create a Code Analyzer configuration file.

We recommend that you name your Code Analyzer configuration file `code-analyzer.yml` or `code-analyzer.yaml` and put it at the
root of your workspace. You then don't need to use this flag when you run the `code-analyzer rules` command from the root of
your workspace, because it automatically looks for either file in the current folder, and if found, applies its rule overrides and engine
settings. If you want to name the file something else, or put it in an alternative folder, then you must specify this flag.

To help you get started, use the `code-analyzer config` command to create your first Code Analyzer configuration file. With it, you
can change the severity of an existing rule, change a rule's tags, and so on. Then use this flag to specify the file so that the command
takes your customizations into account.

Type: option

**`-f`** **|** **`--output-file OUTPUT-FILE`**
Optional

Name of the file where the selected rules are written. The file format depends on the extension you specify; the currently supported
extensions are .json and .csv

If you don't specify this flag, the command outputs the rules to only the terminal. Use this flag to write the rules to a file; the format
of the rules depends on the extension you provide. For example, `--output-file rules.csv` creates a comma-separated values file. You
can specify one of these extensions:

       - .csv

       - .json

To output the rules to multiple files, specify this flag multiple times. For example, `--output-file rules.json --output-file rules.csv`
creates both a JSON file and a CSV file.

If you specify a file within folder, such as `--output-file ./out/rules.json`, the folder must already exist, or you get an error. If the file
already exists, it's overwritten without prompting.

Type: option

**`-v`** **|** **`--view VIEW`**
Optional

Format to display the rules in the terminal.

The format `table` is concise and shows minimal output, the format `detail` shows all available information.

If you specify neither `--view` nor `--output-file`, then the default table view is shown. If you specify `--output-file` but not `--view`,
only summary information is shown in the terminal.

Type: option

Permissible values are: detail, table

#### **`code-analyzer run`**

Analyze your code with a selection of rules to ensure good coding practices.

#### Description for code-analyzer run

You can scan your codebase with the recommended rules. Or use flags to filter the rules based on engines (such as "retire-js" or "eslint"),
rule names, tags, and more.


Salesforce CLI Command Reference code-analyzer Commands

If you want to preview the list of rules before you actually run them, use the `code-analyzer rules` command, which also has the
`--config-file`, `--rule-selector`, `--target`, and `--workspace` flags that together define the list of rules to be run.

We're continually improving Salesforce Code Analyzer. Tell us what you think! Give feedback at https://sfdc.co/CodeAnalyzerFeedback.

Examples for **`code-analyzer run`**

Analyze code using the default behavior: analyze all the files in the current folder (default workspace) using the Recommended rules;
display the output in the terminal with the concise table view; and automatically apply rule or engine overrides if a `code-analyzer.yml`
or `code-analyzer.yaml` file exists in the current folder:

```
   sf code-analyzer run

```

The previous example is equivalent to this example:

```
   sf code-analyzer run --rule-selector Recommended --workspace . --target . --view table

   --config-file ./code-analyzer.yml

```

Analyze the files using the recommended "eslint" rules and show details of the violations:

```
   sf code-analyzer run --rule-selector eslint:Recommended --view detail

```

Analyze the files using all the "eslint" rules:

```
   sf code-analyzer run --rule-selector eslint

```

The previous example is equivalent to this example:

```
   sf code-analyzer run --rule-selector eslint:all

```

Analyze the files using all rules for all engines:

```
   sf code-analyzer run --rule-selector all

```

Analyze the files using only rules in the "pmd" engine with a severity of high (2) or moderate (3), and the "Performance" tag.

```
   sf code-analyzer run --rule-selector "pmd:(2,3):Performance"

```

Analyze files using the recommended "retire-js" rules; target all the files in the folder "./other-source" and only the Apex class files
(extension .cls) in the folder "./force-app":

```
   sf code-analyzer run --rule-selector retire-js:Recommended --target ./other-source --target

    ./force-app/**/*.cls

```

Specify a custom configuration file and output the results to the "results.csv" file in CSV format; the commands fails if it finds a violation
that exceeds the moderate severity level (3):

```
   sf code-analyzer run --config-file ./code-analyzer2.yml --output-file results.csv

   --severity-threshold 3

```

Analyze the files using all the "eslint" engine rules that have a moderate severity (3) and the recommended "retire-js" engine rules with
any severity:

```
   sf code-analyzer run --rule-selector eslint:3 --rule-selector retire-js:Recommended

```

Analyze the files using only the "getter-return" rule of the "eslint" engine and any rule named "no-inner-declarations" from any engine:

```
   sf code-analyzer run --rule-selector eslint:getter-return --rule-selector

   no-inner-declarations

```


Salesforce CLI Command Reference code-analyzer Commands

Analyze the files and ignore all inline suppression markers (code-analyzer-suppress/unsuppress) in the source code:

```
   sf code-analyzer run --no-suppressions

```

Flags

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option

**`-w`** **|** **`--workspace WORKSPACE`**
Optional

Set of files that make up your workspace.

Typically, a workspace is a single project folder that contains all your files. But it can also consist of one or more folders, one or more
files, and use glob patterns (wildcards). If you specify this flag multiple times, then your workspace is the sum of the files and folders.

Some engines often need your entire code base to perform an analysis, even if you want to target only a subset of the files within
your workspace, such as with the `--target` flag. For example, the Salesforce Graph Engine might need to compile your entire project
in order to properly build a graph so it can perform a data flow analysis on the paths that start in your targeted files.

If you don't specify the `--workspace` flag, then the current folder '.' is used as your workspace.

Type: option

Default value: .

**`-t`** **|** **`--target TARGET`**
Optional

Subset of files within your workspace to be targeted for analysis.

You can specify a target as a file, a folder, or a glob pattern.

If you specify this flag multiple times, then the full list of targeted files is the sum of the files and folders.

Each targeted file must live within the workspace that you specified with the `–-workspace` flag.

If you don't specify the `--target` flag, then all the files within your workspace (specified by the `--workspace` flag) are targeted for
analysis.

Type: option

**`-r`** **|** **`--rule-selector RULE-SELECTOR`**
Optional

Selection of rules, based on engine name, severity level, rule name, tag, or a combination of criteria separated by colons.

Use the `--rule-selector` flag to select the list of rules to run based on specific criteria. For example, you can select by engine, such
as the rules associated with the "retire-js" or "eslint" engine. Or select by the severity of the rules, such as high or moderate. You can
also select rules using tag values or rule names. Every rule has a name, which is unique within the scope of an engine. Most rules
have tags, although it's not required. An example of a tag is "Recommended".

You can further filter the list by combining different criteria using colons to represent logical AND, commas to represent logical OR,
and parentheses to create groupings. For example, `--rule-selector "pmd:(Performance,Security):2"` runs rules associated only with
the "pmd" engine that have the Security or Performance tags and a high severity (2). You may also specify the flag multiple times
to OR multiple selectors together. For example, `--rule-selector Performance,Security` is equivalent to `--rule-selector Performance
--rule-selector Security`. Note that if you use parentheses in your selector, the selector should be wrapped in double-quotes.


Salesforce CLI Command Reference code-analyzer Commands

Run `sf code-analyzer rules --rule-selector all` to see the possible values for engine name, rule name, tags, and severity levels that
you can use with this flag.

Type: option

Default value: Recommended

**`-s`** **|** **`--severity-threshold SEVERITY-THRESHOLD`**
Optional

Severity level of a found violation that must be met or exceeded to cause this command to fail with a non-zero exit code.

You can specify either a number (2) or its equivalent string ("High").

Type: option

**`-v`** **|** **`--view VIEW`**
Optional

Format to display the command results in the terminal.

The format `table` is concise and shows minimal output, the format `detail` shows all available information.

If you specify neither `--view` nor `--output-file`, then the default table view is shown. If you specify `--output-file` but not `--view`,
only summary information is shown.

Type: option

Permissible values are: detail, table

**`-f`** **|** **`--output-file OUTPUT-FILE`**
Optional

Name of the file where the analysis results are written. The file format depends on the extension you specify, such as .csv, .html, .xml,
and so on.

If you don't specify this flag, the command outputs the results to only the terminal. Use this flag to print the results to a file; the
format of the results depends on the extension you provide. For example, `--output-file results.csv` creates a comma-separated
values file. You can specify one of these extensions:

       - .csv

      - .html or .htm

       - .json

       - .sarif or .sarif.json

      - .xml

To output the results to multiple files, specify this flag multiple times. For example: `--output-file results.json --output-file report.html`
creates both a JSON results file and an HTML file.

If you specify a file within a folder, such as `--output-file ./out/results.json`, the folder must already exist, or you get an error. If the
file already exists, it's overwritten without prompting.

Type: option

**`-c`** **|** **`--config-file CONFIG-FILE`**
Optional

Path to the configuration file used to customize the engines and rules.

Code Analyzer has an internal default configuration for its rule and engine properties. If you want to override these defaults, you can
create a Code Analyzer configuration file.


### Salesforce CLI Command Reference community Commands

We recommend that you name your Code Analyzer configuration file `code-analyzer.yml` or `code-analyzer.yaml` and put it at the
root of your workspace. You then don't need to use this flag when you run the `code-analyzer run` command from the root of your
workspace, because it automatically looks for either file in the current folder, and if found, applies its rule overrides and engine
settings. If you want to name the file something else, or put it in an alternative folder, then you must specify this flag.

To help you get started, use the `code-analyzer config` command to create your first Code Analyzer configuration file. With it, you
can change the severity of an existing rule, change a rule's tags, and so on. Then use this flag to specify the file so that the command
takes your customizations into account.

Type: option

```
   --include-fixes
```

Optional

Include fix data for violations when available.

When enabled, the output includes fix information for violations that have auto-fixes available. Each fix contains a code location and
the replacement code. This flag may increase analysis time because engines must perform additional processing to compute fixes.

Type: boolean

```
   --include-suggestions
```

Optional

Include suggestion data for violations when available.

When enabled, the output includes suggestion information for violations that have suggestions available. Each suggestion contains
a code location and a message describing the suggested change.

Type: boolean

```
   --no-suppressions
```

Optional

Disable processing of inline and bulk suppression markers.

When specified, any inline suppression markers (code-analyzer-suppress, code-analyzer-suppress-line, and
code-analyzer-suppress-next-line) found in targeted files are ignored and any suppressions supplied by your Code Analyzer
configuration file are ignored so that no violations are suppressed by them.

Note: If you have a `code-analyzer.yml` or `code-analyzer.yaml` configuration file with the `suppressions.disable_suppressions` field,
the configuration file takes precedence over this flag.

Type: boolean

### community Commands

Create and publish an Experience Cloud site.

community create
Create an Experience Cloud site using a template.

community list template
Retrieve the list of templates available in your org.

community publish
Publish an Experience Builder site to make it live.


Salesforce CLI Command Reference community Commands

#### **`community create`**

Create an Experience Cloud site using a template.

#### Description for community create

Run the "community list template" command to see the templates available in your org. See 'Which Experience Cloud Template Should
I Use?' in Salesforce Help for more information about the different template types available.
(https://help.salesforce.com/s/articleView?id=sf.siteforce_commtemp_intro.htm&type=5)

When you create a site with the Build Your Own (LWR) template, you must also specify the AuthenticationType value using the format
templateParams.AuthenticationType=value, where value is AUTHENTICATED or AUTHENTICATED_WITH_PUBLIC_ACCESS_ENABLED.
Name and values are case-sensitive. See 'DigitalExperienceBundle' in the Metadata API Developer Guide for more information.
(https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_digitalexperiencebundle.htm)

The site creation process is an async job that generates a jobId. To check the site creation status, query the BackgroundOperation object
and enter the jobId as the Id. See ‘BackgroundOperation’ in the Object Reference for the Salesforce Platform for more information.
(https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_backgroundoperation.htm)

If the job doesn’t complete within 10 minutes, it times out. You receive an error message and must restart the site creation process.
Completed jobs expire after 24 hours and are removed from the database.

When you run this command, it creates the site in preview status, which means that the site isn't yet live. After you finish building your
site, you can make it live.

If you have an Experience Builder site, publish the site using the "community publish" command to make it live.

If you have a Salesforce Tabs + Visualforce site, to activate the site and make it live, update the status field of the Network type in Metadata
API. (https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_network.htm) Alternatively, in Experience
Workspaces, go to Administration | Settings, and click Activate.

For Experience Builder sites, activating the site sends a welcome email to site members.

#### Examples for community create

Create an Experience Cloud site using template 'Customer Service' and URL path prefix 'customers':

```
   sf community create --name 'My Customer Site' --template-name 'Customer Service'

   --url-path-prefix customers --description 'My customer site'

```

Create a site using 'Partner Central' template:

```
   sf community create --name partnercentral --template-name 'Partner Central' --url-path-prefix

    partners

```

Create a site using the 'Build Your Own (LWR)' template with authentication type of UNAUTHENTICATED:

```
   sf community create --name lwrsite --template-name 'Build Your Own (LWR)' --url-path-prefix

    lwrsite templateParams.AuthenticationType=UNAUTHENTICATED

```

Flags

```
   --json
```

Optional

Format output as json.

Type: boolean


Salesforce CLI Command Reference community Commands

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option

**`-n`** **|** **`--name NAME`**
Required

Name of the site to create.

Type: option

**`-t`** **|** **`--template-name TEMPLATE-NAME`**
Required

Template to use to create a site.

An example of a template is Customer Service. Run the "community template list" command to see which templates are available
in your org.

Type: option

**`-p`** **|** **`--url-path-prefix URL-PATH-PREFIX`**
Optional

URL to append to the domain created when Digital Experiences was enabled for this org.

For example, if your domain name is https://MyDomainName.my.site.com and you create a customer site, enter 'customers' to create
the unique URL https://MyDomainName.my.site.com/customers.

Type: option

**`-d`** **|** **`--description DESCRIPTION`**
Optional

Description of the site.

The description displays in Digital Experiences - All Sites in Setup and helps with site identification.

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

Aliases for **`community create`**

```
   force:community:create

```


Salesforce CLI Command Reference community Commands

#### **`community list template`**

Retrieve the list of templates available in your org.

#### Description for community list template

See 'Which Experience Cloud Template Should I Use?'
(https://help.salesforce.com/s/articleView?id=sf.siteforce_commtemp_intro.htm&type=5) in Salesforce Help for more information about
the different template types available for Experience Cloud.

#### Examples for community list template

Retrieve the template list from an org with alias my-scratch-org:

```
   sf community list template --target-org my-scratch-org

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

#### Aliases for community list template

```
   force:community:template:list

#### **`community publish`**

```

Publish an Experience Builder site to make it live.


Salesforce CLI Command Reference community Commands

Description for **`community publish`**

Each time you publish a site, you update the live site with the most recent updates. When you publish an Experience Builder site for the
first time, you make the site's URL live and enable login access for site members.

In addition to publishing, you must activate a site to send a welcome email to all site members. Activation is also required to set up SEO
for Experience Builder sites. To activate a site, update the status field of the Network type in Metadata API.
(https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_network.htm) Alternatively, in Experience Workspaces,
go to Administration | Settings, and click Activate.

An email notification informs you when your changes are live on the published site. The site publish process is an async job that generates
a jobId. To check the site publish status manually, query the BackgroundOperation object and enter the jobId as the Id. See
‘BackgroundOperation’ in the Object Reference for the Salesforce Platform for more information.
(https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_backgroundoperation.htm)

If the job doesn’t complete within 15 minutes, it times out. You receive an error message and must restart the site publish process.
Completed jobs expire after 24 hours and are removed from the database.

Examples for **`community publish`**

Publish the Experience Builder site with name "My Customer Site':

```
   sf community publish --name 'My Customer Site'

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

Name of the Experience Builder site to publish.

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


### Salesforce CLI Command Reference config Commands

Aliases for **`community publish`**

```
   force:community:publish

### config Commands

```

Commands to configure Salesforce CLI.

#### config get

Get the value of a configuration variable.

config list
List the configuration variables that you've previously set.

config set
Set one or more configuration variables, such as your default org.

config unset
Unset local or global configuration variables.

#### **`config get`**

Get the value of a configuration variable.

#### Description for config get

Run "sf config list" to see the configuration variables you've already set and their level (local or global).

Run "sf config set" to set a configuration variable. For the full list of available configuration variables, see
https://developer.salesforce.com/docs/atlas.en-us.sfdx_setup.meta/sfdx_setup/sfdx_dev_cli_config_values.htm.

#### Examples for config get

Get the value of the "target-org" configuration variable.

```
   sf config get target-org

```

Get multiple configuration variables and display whether they're set locally or globally:

```
   sf config get target-org api-version --verbose

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


Salesforce CLI Command Reference config Commands

Type: option

```
   --verbose
```

Optional

Display whether the configuration variables are set locally or globally.

Type: boolean

Aliases for **`config get`**

```
   force:config:get

#### **`config list`**

```

List the configuration variables that you've previously set.

#### Description for config list

A config variable can be global or local, depending on whether you used the --global flag when you set it. Local config variables apply
only to the current project and override global config variables, which apply to all projects. You can set all config variables as environment
variables. Environment variables override their equivalent local and global config variables.

The output of this command takes into account your current context. For example, let's say you run this command from a Salesforce DX
project in which you've locally set the "target-org" config variable. The command displays the local value, even if you've also set "target-org"
globally. If you haven't set the config variable locally, then the global value is displayed, if set. If you set the SF_TARGET_ORG environment
variable, it's displayed as such and overrides any locally or globally set "target-org" config variable.

For the full list of available configuration variables, see
https://developer.salesforce.com/docs/atlas.en-us.sfdx_setup.meta/sfdx_setup/sfdx_dev_cli_config_values.htm.

#### Examples for config list

List the global and local configuration variables that apply to your current context:

```
   $ sf config list

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


Salesforce CLI Command Reference config Commands

Aliases for **`config list`**

```
   force:config:list

#### **`config set`**

```

Set one or more configuration variables, such as your default org.

#### Description for config set

Use configuration variables to set CLI defaults, such as your default org or the API version you want the CLI to use. For example, if you
set the "target-org" configuration variable, you don't need to specify it as a "sf deploy metadata" flag if you're deploying to your default
org.

Local configuration variables apply only to your current project. Global variables, specified with the --global flag, apply in any Salesforce
DX project.

The resolution order if you've set a flag value in multiple ways is as follows:

1. Flag value specified at the command line.

2. Local (project-level) configuration variable.

3. Global configuration variable.

Run "sf config list" to see the configuration variables you've already set and their level (local or global).

If you're setting a single config variable, you don't need to use an equal sign between the variable and value. But you must use the equal
sign if setting multiple config variables.

For the full list of available configuration variables, see
https://developer.salesforce.com/docs/atlas.en-us.sfdx_setup.meta/sfdx_setup/sfdx_dev_cli_config_values.htm.

#### Examples for config set

Set the local target-org configuration variable to an org username:

```
   sf config set target-org me@my.org

```

Set the local target-org configuration variable to an alias:

```
   sf config set target-org my-scratch-org

```

Set the global target-org and target-dev-hub configuration variables using aliases:

```
   sf config set --global target-org=my-scratch-org target-dev-hub=my-dev-hub

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


Salesforce CLI Command Reference config Commands

Import flag values from a directory.

Type: option

**`-g`** **|** **`--global`**
Optional

Set the configuration variables globally, so they can be used from any Salesforce DX project.

Type: boolean

Aliases for **`config set`**

```
   force:config:set

#### **`config unset`**

```

Unset local or global configuration variables.

#### Description for config unset

Local configuration variables apply only to your current project. Global configuration variables apply in any Salesforce DX project.

For the full list of available configuration variables, see
https://developer.salesforce.com/docs/atlas.en-us.sfdx_setup.meta/sfdx_setup/sfdx_dev_cli_config_values.htm.

#### Examples for config unset

Unset the local "target-org" configuration variable:

```
   sf config unset target-org

```

Unset multiple configuration variables globally:

```
   sf config unset target-org api-version --global

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

**`-g`** **|** **`--global`**
Optional

Unset the configuration variables globally.

Type: boolean


### Salesforce CLI Command Reference data Commands

Aliases for **`config unset`**

```
   force:config:unset

### data Commands

```

Manage records in your org.

data bulk results
Get the results of a bulk ingest job that you previously ran.

data create file
Upload a local file to an org.

data create record
Create and insert a record into a Salesforce or Tooling API object.

data delete bulk
Bulk delete records from an org using a CSV file. Uses Bulk API 2.0.

data delete record
Deletes a single record from a Salesforce or Tooling API object.

data delete resume
Resume a bulk delete job that you previously started. Uses Bulk API 2.0.

data export bulk
Bulk export records from an org into a file using a SOQL query. Uses Bulk API 2.0.

data export resume
Resume a bulk export job that you previously started. Uses Bulk API 2.0.

data export tree
Export data from an org into one or more JSON files.

data get record
Retrieve and display a single record of a Salesforce or Tooling API object.

data import bulk
Bulk import records into a Salesforce object from a CSV file. Uses Bulk API 2.0.

data import resume
Resume a bulk import job that you previously started. Uses Bulk API 2.0.

data import tree
Import data from one or more JSON files into an org.

data query
Execute a SOQL query.

data resume
View the status of a bulk data load job or batch.

data search
Execute a SOSL text-based search query.


Salesforce CLI Command Reference data Commands

data update bulk
Bulk update records to an org from a CSV file. Uses Bulk API 2.0.

data update record
Updates a single record of a Salesforce or Tooling API object.

data update resume
Resume a bulk update job that you previously started. Uses Bulk API 2.0.

data upsert bulk
Bulk upsert records to an org from a CSV file. Uses Bulk API 2.0.

data upsert resume
Resume a bulk upsert job that you previously started. Uses Bulk API 2.0.

#### **`data bulk results`**

Get the results of a bulk ingest job that you previously ran.

#### Description for data bulk results

Use this command to get the complete results after running one of the CLI commands that uses Bulk API 2.0 to ingest (import, update,
upsert, or delete) large datasets to your org, such as "data import bulk". The previously-run bulk command must have completed; if it's
still processing, run the corresponding resume command first, such as "data import resume." Make note of the job ID of the previous
bulk command because you use it to run this command.

You can also use this command to get results from running a bulk ingest job with a different tool, such as Data Loader, as long as you
have the job ID. For information on Data Loader, see
https://developer.salesforce.com/docs/atlas.en-us.dataLoader.meta/dataLoader/data_loader_intro.htm.

This command first displays the status of the previous bulk job, the operation that was executed in the org (such as insert or hard delete),
and the updated Salesforce object. The command then displays how many records were processed in total, and how many were
successful or failed. Finally, the output displays the names of the generated CSV-formatted files that contain the specific results for each
ingested record. Depending on the success or failure of the bulk command, the results files can include the IDs of inserted records or
the specific errors. When possible, if the ingest job failed or was aborted, you also get a CSV file with the unprocessed results.

#### Examples for data bulk results

Get results from a bulk ingest job; use the org with alias "my-scratch":

```
   sf data bulk results --job-id 7507i000fake341G --target-org my-scratch

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


Salesforce CLI Command Reference data Commands

Type: option

**`-i`** **|** **`--job-id JOB-ID`**
Required

Job ID of the bulk job.

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

#### **`data create file`**

Upload a local file to an org.

#### Description for data create file

This command always creates a new file in the org; you can't update an existing file. After a successful upload, the command displays
the ID of the new ContentDocument record which represents the uploaded file.

By default, the uploaded file isn't attached to a record; in the Salesforce UI the file shows up in the Files tab. You can optionally attach
the file to an existing record, such as an account, as long as you know its record ID.

You can also give the file a new name after it's been uploaded; by default its name in the org is the same as the local file name.

#### Examples for data create file

Upload the local file "resources/astro.png" to your default org:

```
   sf data create file --file resources/astro.png

```

Give the file a different filename after it's uploaded to the org with alias "my-scratch":

```
   sf data create file --file resources/astro.png --title AstroOnABoat.png --target-org

   my-scratch

```

Attach the file to a record in the org:

```
   sf data create file --file path/to/astro.png --parent-id a03fakeLoJWPIA3

```

Flags

```
   --json
```

Optional

Format output as json.

Type: boolean


Salesforce CLI Command Reference data Commands

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

**`-t`** **|** **`--title TITLE`**
Optional

New title given to the file (ContentDocument) after it's uploaded.

Type: option

**`-f`** **|** **`--file FILE`**
Required

Path of file to upload.

Type: option

**`-i`** **|** **`--parent-id PARENT-ID`**
Optional

ID of the record to attach the file to.

Type: option

#### **`data create record`**

Create and insert a record into a Salesforce or Tooling API object.

#### Description for data create record

You must specify a value for all required fields of the object.

When specifying fields, use the format <fieldName>=<value>. Enclose all field-value pairs in one set of double quotation marks, delimited
by spaces. Enclose values that contain spaces in single quotes.

This command inserts a record into Salesforce objects by default. Use the --use-tooling-api flag to insert into a Tooling API object.

#### Examples for data create record

Insert a record into the Account object of your default org; only the required Name field has a value:

```
   sf data create record --sobject Account --values "Name=Acme"

```


Salesforce CLI Command Reference data Commands

Insert an Account record with values for two fields, one value contains a space; the command uses the org with alias "my-scratch":

```
   sf data create record --sobject Account --values "Name='Universal Containers'

   Website=www.example.com" --target-org my-scratch

```

Insert a record into the Tooling API object TraceFlag:

```
   sf data create record --use-tooling-api --sobject TraceFlag --values

   "DebugLevelId=7dl170000008U36AAE StartDate=2022-12-15T00:26:04.000+0000

   ExpirationDate=2022-12-15T00:56:04.000+0000 LogType=CLASS_TRACING

   TracedEntityId=01p17000000R6bLAAS"

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

API name of the Salesforce or Tooling API object that you're inserting a record into.

Type: option

**`-v`** **|** **`--values VALUES`**
Required

Values for the flags in the form <fieldName>=<value>, separate multiple pairs with spaces.

Type: option

**`-t`** **|** **`--use-tooling-api`**
Optional

Use Tooling API so you can insert a record in a Tooling API object.

Type: boolean


Salesforce CLI Command Reference data Commands

Aliases for **`data create record`**

```
   force:data:record:create

#### **`data delete bulk`**

```

Bulk delete records from an org using a CSV file. Uses Bulk API 2.0.

#### Description for data delete bulk

The CSV file must have only one column ("Id") and then the list of record IDs you want to delete, one ID per line.

When you execute this command, it starts a job, displays the ID, and then immediately returns control of the terminal to you by default.
If you prefer to wait, set the --wait flag to the number of minutes; if it times out, the command outputs the IDs. Use the job ID to check
the status of the job with the "sf data delete resume" command.

#### Examples for data delete bulk

Bulk delete Account records from your default org using the list of IDs in the "files/delete.csv" file:

```
   sf data delete bulk --sobject Account --file files/delete.csv

```

Bulk delete records from a custom object in an org with alias my-scratch and wait 5 minutes for the command to complete:

```
   sf data delete bulk --sobject MyObject__c --file files/delete.csv --wait 5 --target-org

   my-scratch

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

**`-f`** **|** **`--file FILE`**
Required


Salesforce CLI Command Reference data Commands

CSV file that contains the IDs of the records to update or delete.

Type: option

**`-s`** **|** **`--sobject SOBJECT`**
Required

API name of the Salesforce object, either standard or custom, that you want to update or delete records from.

Type: option

**`-w`** **|** **`--wait WAIT`**
Optional

Number of minutes to wait for the command to complete before displaying the results.

Type: option

```
   --line-ending LINE-ENDING
```

Optional

Line ending used in the CSV file. Default value on Windows is `CRLF`; on macOS and Linux it's `LF`.

Type: option

Permissible values are: CRLF, LF

```
   --hard-delete
```

Optional

Mark the records as immediately eligible for deletion by your org. If you don't specify this flag, the deleted records go into the Recycle
Bin.

You must have the "Bulk API Hard Delete" system permission to use this flag. The permission is disabled by default and can be
enabled only by a system administrator.

Type: boolean

#### **`data delete record`**

Deletes a single record from a Salesforce or Tooling API object.

#### Description for data delete record

Specify the record you want to delete with either its ID or with a list of field-value pairs that identify the record. If your list of fields identifies
more than one record, the delete fails; the error displays how many records were found.

When specifying field-value pairs, use the format <fieldName>=<value>. Enclose all field-value pairs in one set of double quotation
marks, delimited by spaces. Enclose values that contain spaces in single quotes.

This command deletes a record from Salesforce objects by default. Use the --use-tooling-api flag to delete from a Tooling API object.

#### Examples for data delete record

Delete a record from Account with the specified (truncated) ID:

```
   sf data delete record --sobject Account --record-id 00180XX

```

Delete a record from Account whose name equals "Acme":

```
   sf data delete record --sobject Account --where "Name=Acme"

```


Salesforce CLI Command Reference data Commands

Delete a record from Account identified with two field values, one that contains a space; the command uses the org with alias "my-scratch":

```
   sf data delete record --sobject Account --where "Name='Universal Containers' Phone='(123)

    456-7890'" --target-org myscratch

```

Delete a record from the Tooling API object TraceFlag with the specified (truncated) ID:

```
   sf data delete record --use-tooling-api --sobject TraceFlag --record-id 7tf8c

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

API name of the Salesforce or Tooling API object that you're deleting a record from.

Type: option

**`-i`** **|** **`--record-id RECORD-ID`**
Optional

ID of the record you’re deleting.

Type: option

**`-w`** **|** **`--where WHERE`**
Optional

List of <fieldName>=<value> pairs that identify the record you want to delete.

Type: option

**`-t`** **|** **`--use-tooling-api`**
Optional

Use Tooling API so you can delete a record from a Tooling API object.

Type: boolean


Salesforce CLI Command Reference data Commands

Aliases for **`data delete record`**

```
   force:data:record:delete

#### **`data delete resume`**

```

Resume a bulk delete job that you previously started. Uses Bulk API 2.0.

#### Description for data delete resume

The command uses the job ID returned by the "sf data delete bulk" command or the most recently-run bulk delete job.

#### Examples for data delete resume

Resume a bulk delete job from your default org using an ID:

```
   sf data delete resume --job-id 750xx000000005sAAA

```

Resume the most recently run bulk delete job for an org with alias my-scratch:

```
   sf data delete resume --use-most-recent --target-org my-scratch

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

Username or alias of the target org. Not required if the "target-org" configuration variable is already set.

Type: option

**`-i`** **|** **`--job-id JOB-ID`**
Optional

ID of the job you want to resume.

Type: option

```
   --use-most-recent
```

Optional

Use the ID of the most recently-run bulk job.

Type: boolean

Default value: true


Salesforce CLI Command Reference data Commands

```
   --wait WAIT
```

Optional

Number of minutes to wait for the command to complete before displaying the results.

Type: option

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

#### **`data export bulk`**

Bulk export records from an org into a file using a SOQL query. Uses Bulk API 2.0.

#### Description for data export bulk

You can use this command to export millions of records from an org, either to migrate data or to back it up.

Use a SOQL query to specify the fields of a standard or custom object that you want to export. Specify the SOQL query either at the
command line with the --query flag or read it from a file with the --query-file flag; you can't specify both flags. The --output-file flag is
required, which means you can only write the records to a file, in either CSV or JSON format.

Bulk exports can take a while, depending on how many records are returned by the SOQL query. If the command times out, the command
displays the job ID. To see the status and get the results of the job, run "sf data export resume" and pass the job ID to the --job-id flag.

IMPORTANT: This command uses Bulk API 2.0, which limits the type of SOQL queries you can run. For example, you can't use aggregate
functions such as count(). For the complete list of limitations, see the "SOQL Considerations" section in the "Bulk API 2.0 and Bulk API
Developer Guide" (https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/queries.htm).

#### Examples for data export bulk

Export the Id, Name, and Account.Name fields of the Contact object into a CSV-formatted file; if the export doesn't complete in 10
minutes, the command ends and displays a job ID. Use the org with alias "my-scratch":

```
   sf data export bulk --query "SELECT Id, Name, Account.Name FROM Contact" --output-file

   export-accounts.csv --wait 10 --target-org my-scratch

```

Similar to previous example, but use the default org, export the records into a JSON-formatted file, and include records that have been
soft deleted:

```
   sf data export bulk --query "SELECT Id, Name, Account.Name FROM Contact" --output-file

   export-accounts.json --result-format json --wait 10 --all-rows

```

Flags

```
   --json
```

Optional

Format output as json.

Type: boolean


Salesforce CLI Command Reference data Commands

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

**`-w`** **|** **`--wait WAIT`**
Optional

Time to wait for the command to finish, in minutes.

Type: option

**`-q`** **|** **`--query QUERY`**
Optional

SOQL query to execute.

Type: option

```
   --query-file QUERY-FILE
```

Optional

File that contains the SOQL query.

Type: option

```
   --all-rows
```

Optional

Include records that have been soft-deleted due to a merge or delete. By default, deleted records are not returned.

Type: boolean

```
   --output-file OUTPUT-FILE
```

Required

File where records are written.

Type: option

**`-r`** **|** **`--result-format RESULT-FORMAT`**
Required

Format to write the results.

Type: option

Permissible values are: csv, json

Default value: csv


Salesforce CLI Command Reference data Commands

```
   --column-delimiter COLUMN-DELIMITER
```

Optional

Column delimiter to be used when writing CSV output. Default is COMMA.

Type: option

Permissible values are: BACKQUOTE, CARET, COMMA, PIPE, SEMICOLON, TAB

```
   --line-ending LINE-ENDING
```

Optional

Line ending to be used when writing CSV output. Default value on Windows is is `CRLF`; on macOS and Linux it's `LR`.

Type: option

Permissible values are: LF, CRLF

#### **`data export resume`**

Resume a bulk export job that you previously started. Uses Bulk API 2.0.

#### Description for data export resume

When the original "data export bulk" command times out, it displays a job ID. To see the status and get the results of the bulk export,
run this command by either passing it the job ID or using the --use-most-recent flag to specify the most recent bulk export job.

Using either `--job-id` or `--use-most-recent` will properly resolve to the correct org where the bulk job was started based on the cached
data by "data export bulk".

#### Examples for data export resume

Resume a bulk export job run by specifying a job ID:

```
   sf data export resume --job-id 750xx000000005sAAA

```

Resume the most recently-run bulk export job:

```
   sf data export resume --use-most-recent

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

**`-i`** **|** **`--job-id JOB-ID`**
Optional

Job ID of the bulk export.


Salesforce CLI Command Reference data Commands

Type: option

```
   --use-most-recent
```

Optional

Use the job ID of the bulk export job that was most recently run.

Type: boolean

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

#### **`data export tree`**

Export data from an org into one or more JSON files.

#### Description for data export tree

Specify a SOQL query, either directly at the command line or read from a file, to retrieve the data you want to export. The exported data
is written to JSON files in sObject tree format, which is a collection of nested, parent-child records with a single root record. Use these
JSON files to import data into an org with the "sf data import tree" command.

If your SOQL query references multiple objects, the command generates a single JSON file by default. You can specify the --plan flag to
generate separate JSON files for each object and a plan definition file that aggregates them. You then specify just this plan definition
file when you import the data into an org.

The SOQL query can return a maximum of 2,000 records. For more information, see the REST API Developer Guide.
(https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_composite_sobject_tree.htm).

#### Examples for data export tree

Export records retrieved with the specified SOQL query into a single JSON file in the current directory; the command uses your default
org:

```
   sf data export tree --query "SELECT Id, Name, (SELECT Name, Address__c FROM Properties__r)

    FROM Broker__c"

```

Export data using a SOQL query in the "query.txt" file and generate JSON files for each object and a plan that aggregates them:

```
   sf data export tree --query query.txt --plan

```

Prepend "export-demo" before each generated file and generate the files in the "export-out" directory; run the command on the org
with alias "my-scratch":

```
   sf data export tree --query query.txt --plan --prefix export-demo --output-dir export-out

    --target-org my-scratch

```

Flags

```
   --json
```

Optional

Format output as json.


Salesforce CLI Command Reference data Commands

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

**`-q`** **|** **`--query QUERY`**
Required

SOQL query, or filepath of a file that contains the query, to retrieve records.

Type: option

**`-p`** **|** **`--plan`**
Optional

Generate multiple sObject tree files and a plan definition file for aggregated import.

Type: boolean

**`-x`** **|** **`--prefix PREFIX`**
Optional

Prefix of generated files.

Type: option

**`-d`** **|** **`--output-dir OUTPUT-DIR`**
Optional

Directory in which to generate the JSON files; default is current directory.

Type: option

Aliases for **`data export tree`**

```
   force:data:tree:export

#### **`data get record`**

```

Retrieve and display a single record of a Salesforce or Tooling API object.

#### Description for data get record

Specify the record you want to retrieve with either its ID or with a list of field-value pairs that identify the record. If your list of fields
identifies more than one record, the command fails; the error displays how many records were found.


Salesforce CLI Command Reference data Commands

When specifying field-value pairs, use the format <fieldName>=<value>. Enclose all field-value pairs in one set of double quotation
marks, delimited by spaces. Enclose values that contain spaces in single quotes.

The command displays all the record's fields and their values, one field per terminal line. Fields with no values are displayed as "null".

This command retrieves a record from Salesforce objects by default. Use the --use-tooling-api flag to retrieve from a Tooling API object.

Examples for **`data get record`**

Retrieve and display a record from Account with the specified (truncated) ID:

```
   sf data get record --sobject Account --record-id 00180XX

```

Retrieve a record from Account whose name equals "Acme":

```
   sf data get record --sobject Account --where "Name=Acme"

```

Retrieve a record from Account identified with two field values, one that contains a space; the command uses the org with alias
"my-scratch":

```
   sf data get record --sobject Account --where "Name='Universal Containers' Phone='(123)

   456-7890'" --target-org myscratch

```

Retrieve a record from the Tooling API object TraceFlag with the specified (truncated) ID:

```
   sf data get record --use-tooling-api --sobject TraceFlag --record-id 7tf8c

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

API name of the Salesforce or Tooling API object that you're retrieving a record from.

Type: option


Salesforce CLI Command Reference data Commands

**`-i`** **|** **`--record-id RECORD-ID`**
Optional

ID of the record you’re retrieving.

Type: option

**`-w`** **|** **`--where WHERE`**
Optional

List of <fieldName>=<value> pairs that identify the record you want to display.

Type: option

**`-t`** **|** **`--use-tooling-api`**
Optional

Use Tooling API so you can retrieve a record from a Tooling API object.

Type: boolean

Aliases for **`data get record`**

```
   force:data:record:get

#### **`data import bulk`**

```

Bulk import records into a Salesforce object from a CSV file. Uses Bulk API 2.0.

#### Description for data import bulk

You can use this command to import millions of records into the object from a file in comma-separated values (CSV) format.

All the records in the CSV file must be for the same Salesforce object. Specify the object with the `--sobject` flag.

Bulk imports can take a while, depending on how many records are in the CSV file. If the command times out, the command displays
the job ID. To see the status and get the results of the job, run "sf data import resume" and pass the job ID to the --job-id flag.

For information and examples about how to prepare your CSV files, see "Prepare Data to Ingest" in the "Bulk API 2.0 and Bulk API Developer
Guide" (https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/datafiles_prepare_data.htm).

#### Examples for data import bulk

Import Account records from a CSV-formatted file into an org with alias "my-scratch"; if the import doesn't complete in 10 minutes, the
command ends and displays a job ID:

```
   sf data import bulk --file accounts.csv --sobject Account --wait 10 --target-org my-scratch

```

Flags

```
   --json
```

Optional

Format output as json.

Type: boolean


Salesforce CLI Command Reference data Commands

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option

**`-f`** **|** **`--file FILE`**
Required

CSV file that contains the Salesforce object records you want to import.

Type: option

**`-s`** **|** **`--sobject SOBJECT`**
Required

API name of the Salesforce object, either standard or custom, into which you're importing records.

Type: option

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

**`-w`** **|** **`--wait WAIT`**
Optional

Time to wait for the command to finish, in minutes.

Type: option

**`-o`** **|** **`--target-org TARGET-ORG`**
Required

Username or alias of the target org. Not required if the `target-org` configuration variable is already set.

Type: option

```
   --line-ending LINE-ENDING
```

Optional

Line ending used in the CSV file. Default value on Windows is `CRLF`; on macOS and Linux it's `LF`.

Type: option

Permissible values are: CRLF, LF

```
   --column-delimiter COLUMN-DELIMITER
```

Optional

Column delimiter used in the CSV file.

Type: option

Permissible values are: BACKQUOTE, CARET, COMMA, PIPE, SEMICOLON, TAB

#### **`data import resume`**

Resume a bulk import job that you previously started. Uses Bulk API 2.0.


Salesforce CLI Command Reference data Commands

Description for **`data import resume`**

When the original "sf data import bulk" command times out, it displays a job ID. To see the status and get the results of the bulk import,
run this command by either passing it the job ID or using the --use-most-recent flag to specify the most recent bulk import job.

Examples for **`data import resume`**

Resume a bulk import job to your default org using an ID:

```
   sf data import resume --job-id 750xx000000005sAAA

```

Resume the most recently run bulk import job for an org with alias my-scratch:

```
   sf data import resume --use-most-recent --target-org my-scratch

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
   --use-most-recent
```

Optional

Use the job ID of the bulk import job that was most recently run.

Type: boolean

**`-i`** **|** **`--job-id JOB-ID`**
Optional

Job ID of the bulk import.

Type: option

**`-w`** **|** **`--wait WAIT`**
Optional

Time to wait for the command to finish, in minutes.

Type: option

#### **`data import tree`**

Import data from one or more JSON files into an org.

#### Description for data import tree

The JSON files that contain the data are in sObject tree format, which is a collection of nested, parent-child records with a single root
record. Use the "sf data export tree" command to generate these JSON files.


Salesforce CLI Command Reference data Commands

If you used the --plan flag when exporting the data to generate a plan definition file, use the --plan flag to reference the file when you
import. If you're not using a plan, use the --files flag to list the files. If you specify multiple JSON files that depend on each other in a
parent-child relationship, be sure you list them in the correct order.

Examples for **`data import tree`**

Import the records contained in two JSON files into the org with alias "my-scratch":

```
   sf data import tree --files Contact.json,Account.json --target-org my-scratch

```

Import records using a plan definition file into your default org:

```
   sf data import tree --plan Account-Contact-plan.json

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

**`-f`** **|** **`--files FILES`**
Optional

Comma-separated and in-order JSON files that contain the records, in sObject tree format, that you want to insert.

Type: option

**`-p`** **|** **`--plan PLAN`**
Optional

Plan definition file to insert multiple data files.

Unlike when you use the `--files` flag, the files listed in the plan definition file **can** contain more then 200 records. When the CLI
executes the import, it automatically batches the records to comply with the 200 record limit set by the API.

The order in which you list the files in the plan definition file matters. Specifically, records with lookups to records in another file
should be listed AFTER that file. For example, let's say you're loading Account and Contact records, and the contacts have references
to those accounts. Be sure you list the Accounts file before the Contacts file.


Salesforce CLI Command Reference data Commands

The plan definition file has the following schema:

      - items(object) - SObject Type: Definition of records to be insert per SObject Type

      - sobject(string) - Name of SObject: Child file references must have SObject roots of this type

       - files(array) - Files: An array of files paths to load

Type: option

Aliases for **`data import tree`**

```
   force:data:tree:import

#### **`data query`**

```

Execute a SOQL query.

#### Description for data query

Specify the SOQL query at the command line with the --query flag or read the query from a file with the --file flag.

If your query returns more than 10,000 records, prefer to use the `sf data export bulk` command instead. It runs the query using Bulk API
2.0, which has higher limits than the default API used by the command.

#### Examples for data query

Specify a SOQL query at the command line; the command uses your default org:

```
   sf data query --query "SELECT Id, Name, Account.Name FROM Contact"

```

Read the SOQL query from a file called "query.txt" and write the CSV-formatted output to a file; the command uses the org with alias
"my-scratch":

```
   sf data query --file query.txt --output-file output.csv --result-format csv --target-org

   my-scratch

```

Use Tooling API to run a query on the ApexTrigger Tooling API object:

```
   sf data query --query "SELECT Name FROM ApexTrigger" --use-tooling-api

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


Salesforce CLI Command Reference data Commands

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

**`-q`** **|** **`--query QUERY`**
Optional

SOQL query to execute.

Type: option

**`-f`** **|** **`--file FILE`**
Optional

File that contains the SOQL query.

Type: option

**`-t`** **|** **`--use-tooling-api`**
Optional

Use Tooling API so you can run queries on Tooling API objects.

Type: boolean

```
   --all-rows
```

Optional

Include deleted records. By default, deleted records are not returned.

Type: boolean

**`-r`** **|** **`--result-format RESULT-FORMAT`**
Optional

Format to display the results; the --json flag overrides this flag.

Type: option

Permissible values are: human, csv, json

Default value: human

```
   --output-file OUTPUT-FILE
```

Optional

File where records are written; only CSV and JSON output formats are supported.

Type: option

Aliases for **`data query`**

```
   force:data:soql:query

```


Salesforce CLI Command Reference data Commands

#### **`data resume`**

View the status of a bulk data load job or batch.

#### Description for data resume

Run this command using the job ID or batch ID returned from the "sf data delete bulk" or "sf data upsert bulk" commands.

#### Examples for data resume

View the status of a bulk load job:

```
   sf data resume --job-id 750xx000000005sAAA

```

View the status of a bulk load job and a specific batches:

```
   sf data resume --job-id 750xx000000005sAAA --batch-id 751xx000000005nAAA

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

**`-b`** **|** **`--batch-id BATCH-ID`**
Optional

ID of the batch whose status you want to view; you must also specify the job ID.

Type: option

**`-i`** **|** **`--job-id JOB-ID`**
Required

ID of the job whose status you want to view.

Type: option


Salesforce CLI Command Reference data Commands

#### **`data search`**

Execute a SOSL text-based search query.

#### Description for data search

Specify the SOSL query at the command line with the --query flag or read the query from a file with the --file flag.

By default, the results are written to the terminal in human-readable format. If you specify `--result-format csv`, the output is written to
one or more CSV (comma-separated values) files. The file names correspond to the Salesforce objects in the results, such as Account.csv.
Both `--result-format human` and `--result-format json` display only to the terminal.

#### Examples for data search

Specify a SOSL query at the command line; the command uses your default org:

```
   sf data search --query "FIND {Anna Jones} IN Name Fields RETURNING Contact (Name, Phone)"

```

Read the SOSL query from a file called "query.txt"; the command uses the org with alias "my-scratch":

```
   sf data search --file query.txt --target-org my-scratch

```

Similar to the previous example, but write the results to one or more CSV files, depending on the Salesforce objects in the results:

```
   sf data search --file query.txt --target-org my-scratch --result-format csv

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

**`-q`** **|** **`--query QUERY`**
Optional

SOSL query to execute.


Salesforce CLI Command Reference data Commands

Type: option

**`-f`** **|** **`--file FILE`**
Optional

File that contains the SOSL query.

Type: option

**`-r`** **|** **`--result-format RESULT-FORMAT`**
Optional

Format to display the results, or to write to disk if you specify "csv".

Type: option

Permissible values are: human, csv, json

Default value: human

#### **`data update bulk`**

Bulk update records to an org from a CSV file. Uses Bulk API 2.0.

#### Description for data update bulk

You can use this command to update millions of Salesforce object records based on a file in comma-separated values (CSV) format.

All the records in the CSV file must be for the same Salesforce object. Specify the object with the `--sobject` flag. The first column of
every line in the CSV file must be an ID of the record you want to update. The CSV file can contain only existing records; if a record in the
file doesn't currently exist in the Salesforce object, the command fails. Consider using "sf data upsert bulk" if you also want to insert new
records.

Bulk updates can take a while, depending on how many records are in the CSV file. If the command times out, the command displays
the job ID. To see the status and get the results of the job, run "sf data update resume" and pass the job ID to the --job-id flag.

For information and examples about how to prepare your CSV files, see "Prepare Data to Ingest" in the "Bulk API 2.0 and Bulk API Developer
Guide" (https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/datafiles_prepare_data.htm).

#### Examples for data update bulk

Update Account records from a CSV-formatted file into an org with alias "my-scratch"; if the update doesn't complete in 10 minutes, the
command ends and displays a job ID:

```
   sf data update bulk --file accounts.csv --sobject Account --wait 10 --target-org my-scratch

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


Salesforce CLI Command Reference data Commands

Type: option

**`-w`** **|** **`--wait WAIT`**
Optional

Time to wait for the command to finish, in minutes.

Type: option

**`-f`** **|** **`--file FILE`**
Required

CSV file that contains the Salesforce object records you want to update.

Type: option

**`-s`** **|** **`--sobject SOBJECT`**
Required

API name of the Salesforce object, either standard or custom, which you are updating.

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

```
   --line-ending LINE-ENDING
```

Optional

Line ending used in the CSV file. Default value on Windows is `CRLF`; on macOS and Linux it's `LF`.

Type: option

Permissible values are: CRLF, LF

```
   --column-delimiter COLUMN-DELIMITER
```

Optional

Column delimiter used in the CSV file.

Type: option

Permissible values are: BACKQUOTE, CARET, COMMA, PIPE, SEMICOLON, TAB

#### **`data update record`**

Updates a single record of a Salesforce or Tooling API object.

#### Description for data update record

Specify the record you want to update with either its ID or with a list of field-value pairs that identify the record. If your list of fields
identifies more than one record, the update fails; the error displays how many records were found.


Salesforce CLI Command Reference data Commands

When using field-value pairs for both identifying the record and specifiyng the new field values, use the format <fieldName>=<value>.
Enclose all field-value pairs in one set of double quotation marks, delimited by spaces. Enclose values that contain spaces in single quotes.

This command updates a record in Salesforce objects by default. Use the --use-tooling-api flag to update a Tooling API object.

Examples for **`data update record`**

Update the Name field of an Account record with the specified (truncated) ID:

```
   sf data update record --sobject Account --record-id 001D0 --values "Name=NewAcme"

```

Update the Name field of an Account record whose current name is 'Old Acme':

```
   sf data update record --sobject Account --where "Name='Old Acme'" --values "Name='New

   Acme'"

```

Update the Name and Website fields of an Account record with the specified (truncated) ID:

```
   sf data update record --sobject Account --record-id 001D0 --values "Name='Acme III'

   Website=www.example.com"

```

Update the ExpirationDate field of a record of the Tooling API object TraceFlag using the specified (truncated) ID:

```
   sf data update record -t --sobject TraceFlag --record-id 7tf170000009cUBAAY --values

   "ExpirationDate=2017-12-01T00:58:04.000+0000"

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

API name of the Salesforce or Tooling API object that contains the record you're updating.

Type: option


Salesforce CLI Command Reference data Commands

**`-i`** **|** **`--record-id RECORD-ID`**
Optional

ID of the record you’re updating.

Type: option

**`-w`** **|** **`--where WHERE`**
Optional

List of <fieldName>=<value> pairs that identify the record you want to update.

Type: option

**`-v`** **|** **`--values VALUES`**
Required

Fields that you're updating, in the format of <fieldName>=<value> pairs.

Type: option

**`-t`** **|** **`--use-tooling-api`**
Optional

Use Tooling API so you can update a record in a Tooling API object.

Type: boolean

Aliases for **`data update record`**

```
   force:data:record:update

#### **`data update resume`**

```

Resume a bulk update job that you previously started. Uses Bulk API 2.0.

#### Description for data update resume

When the original "sf data update bulk" command times out, it displays a job ID. To see the status and get the results of the bulk update,
run this command by either passing it the job ID or using the --use-most-recent flag to specify the most recent bulk update job.

Using either `--job-id` or `--use-most-recent` will properly resolve to the correct org where the bulk job was started based on the cached
data by "data update bulk".

#### Examples for data update resume

Resume a bulk update job using a job ID:

```
   sf data update resume --job-id 750xx000000005sAAA

```

Resume the most recently run bulk update job:

```
   sf data update resume --use-most-recent

```

Flags

```
   --json
```

Optional


Salesforce CLI Command Reference data Commands

Format output as json.

Type: boolean

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option

```
   --use-most-recent
```

Optional

Use the job ID of the bulk update job that was most recently run.

Type: boolean

**`-i`** **|** **`--job-id JOB-ID`**
Optional

Job ID of the bulk update.

Type: option

**`-w`** **|** **`--wait WAIT`**
Optional

Time to wait for the command to finish, in minutes.

Type: option

#### **`data upsert bulk`**

Bulk upsert records to an org from a CSV file. Uses Bulk API 2.0.

#### Description for data upsert bulk

An upsert refers to inserting a record into a Salesforce object if the record doesn't already exist, or updating it if it does exist.

When you execute this command, it starts a job, displays the ID, and then immediately returns control of the terminal to you by default.
If you prefer to wait, set the --wait flag to the number of minutes; if it times out, the command outputs the IDs. Use the job and batch
IDs to check the status of the job with the "sf data upsert resume" command.

See "Prepare CSV Files" in the Bulk API Developer Guide for details on formatting your CSV file.
(https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/datafiles_prepare_csv.htm)

#### Examples for data upsert bulk

Bulk upsert records to the Contact object in your default org:

```
   sf data upsert bulk --sobject Contact --file files/contacts.csv --external-id Id

```

Bulk upsert records to a custom object in an org with alias my-scratch and wait 5 minutes for the command to complete:

```
   sf data upsert bulk --sobject MyObject__c --file files/file.csv --external-id MyField__c

   --wait 5 --target-org my-scratch

```


Salesforce CLI Command Reference data Commands

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

**`-f`** **|** **`--file FILE`**
Required

CSV file that contains the IDs of the records to update or delete.

Type: option

**`-s`** **|** **`--sobject SOBJECT`**
Required

API name of the Salesforce object, either standard or custom, that you want to update or delete records from.

Type: option

**`-w`** **|** **`--wait WAIT`**
Optional

Number of minutes to wait for the command to complete before displaying the results.

Type: option

```
   --line-ending LINE-ENDING
```

Optional

Line ending used in the CSV file. Default value on Windows is `CRLF`; on macOS and Linux it's `LF`.

Type: option

Permissible values are: CRLF, LF

```
   --column-delimiter COLUMN-DELIMITER
```

Optional

Column delimiter used in the CSV file.

Type: option

Permissible values are: BACKQUOTE, CARET, COMMA, PIPE, SEMICOLON, TAB


Salesforce CLI Command Reference data Commands

**`-i`** **|** **`--external-id EXTERNAL-ID`**
Required

Name of the external ID field, or the Id field.

Type: option

#### **`data upsert resume`**

Resume a bulk upsert job that you previously started. Uses Bulk API 2.0.

#### Description for data upsert resume

The command uses the job ID returned from the "sf data upsert bulk" command or the most recently-run bulk upsert job.

#### Examples for data upsert resume

Resume a bulk upsert job from your default org using an ID:

```
   sf data upsert resume --job-id 750xx000000005sAAA

```

Resume the most recently run bulk upsert job for an org with alias my-scratch:

```
   sf data upsert resume --use-most-recent --target-org my-scratch

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

Username or alias of the target org. Not required if the "target-org" configuration variable is already set.

Type: option

**`-i`** **|** **`--job-id JOB-ID`**
Optional

ID of the job you want to resume.

Type: option

```
   --use-most-recent
```

Optional

Use the ID of the most recently-run bulk job.

Type: boolean


### Salesforce CLI Command Reference dev Commands

Default value: true

```
   --wait WAIT
```

Optional

Number of minutes to wait for the command to complete before displaying the results.

Type: option

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

### dev Commands

Commands for sf plugin development.

#### dev audit messages

Audit messages in a plugin's messages directory to locate unused messages and missing messages that have references in source
code.

dev convert messages
Convert a .json messages file into Markdown.

dev convert script
Convert a script file that contains deprecated sfdx-style commands to use the new sf-style commands instead.

dev generate command
Generate a new sf command.

dev generate flag
Generate a flag for an existing command.

dev generate plugin
Generate a new sf plugin.

#### **`dev audit messages`**

Audit messages in a plugin's messages directory to locate unused messages and missing messages that have references in source code.

#### Examples for dev audit messages

Audit messages using default directories:

```
   sf dev audit messages

```

Audit messages in the "messages" directory in the current working directory; the plugin's source directory is in "src":

```
   sf dev audit messages --messages-dir ./messages --source-dir ./src

```


Salesforce CLI Command Reference dev Commands

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

**`-p`** **|** **`--project-dir PROJECT-DIR`**
Optional

Location of the project where messages are to be audited.

Type: option

Default value: .

**`-m`** **|** **`--messages-dir MESSAGES-DIR`**
Optional

Directory that contains the plugin's message files.

The default is the "messages" directory in the current working directory.

Type: option

Default value: messages

**`-s`** **|** **`--source-dir SOURCE-DIR`**
Optional

Directory that contains the plugin's source code.

The default is the "src" directory in the current working directory.

Type: option

Default value: src

#### **`dev convert messages`**

Convert a .json messages file into Markdown.

#### Description for dev convert messages

Preserves the filename and the original messages file, then creates a new file with the Markdown extension and standard headers for
the command and flag summaries, descriptions, and so on. After you review the new Markdown file, delete the old .json file.

#### Examples for dev convert messages

Convert the my-command.json message file into my-command.md with the standard messages headers:

```
   sf dev convert messages --filename my-command.json

```


Salesforce CLI Command Reference dev Commands

Similar to previous example, but specify the plugin project directory:

```
   sf dev convert messages --project-dir ./path/to/plugin --filename my-command.json

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

**`-p`** **|** **`--project-dir PROJECT-DIR`**
Optional

Location of the project whose messages are to be converted.

Type: option

Default value: .

**`-f`** **|** **`--file-name FILE-NAME`**
Required

Filename to convert.

Type: option

#### **`dev convert script`**

Convert a script file that contains deprecated sfdx-style commands to use the new sf-style commands instead.

#### Description for dev convert script

Important: Use this command only to get started on the sfdx->sf script migration. We don't guarantee that the new sf-style command
replacements work correctly or as you expect. You must test, and probably update, the new script before putting it into production. We
also don't guarantee that the JSON results are the same as before.

This command can convert a large part of your script, but possibly not all. There are some sfdx-style commands that don't have an
obvious sf-style equivalent. In this case, this command doesn't replace the sfdx-style command but instead adds a comment to remind
you that you must convert it manually. See the Salesforce CLI Command Reference for migration information about each deprecated
sfdx-style command: https://developer.salesforce.com/docs/atlas.en-us.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference.htm.

This command is interactive; as it scans your script, it prompts you when it finds an sfdx-style command or flag and asks if you want to
convert it to the displayed suggestion. The command doesn't update the script file directly; rather, it creates a new file whose name is
the original name but with "-converted" appended to it. The script replaces all instances of "sfdx" with "sf". For each prompt you answer
"y" to, the command replaces the sfdx-style names with their equivalent sf-style ones. For example, "sfdx force:apex:execute
--targetusername myscratch" is replaced with "sf apex run --target-org myscratch".


Salesforce CLI Command Reference dev Commands

Examples for **`dev convert script`**

Convert the YAML file called "myScript.yml" located in the current directory; the new file that contains the replacements is called
"myScript-converted.yml":

```
   sf dev convert script --script ./myScript.yml

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

**`-s`** **|** **`--script SCRIPT`**
Required

Filepath to the script you want to convert.

Type: option

#### **`dev generate command`**

Generate a new sf command.

#### Description for dev generate command

You must run this command from within a plugin directory, such as the directory created with the "sf dev generate plugin" command.

The command generates basic source files, messages (\*.md), and test files for your new command. The Typescript files contain import
statements for the minimum required Salesforce libraries, and scaffold some basic code. The new type names come from the value you
passed to the --name flag.

The command updates the package.json file, so if it detects conflicts with the existing file, you're prompted whether you want to overwrite
the file. There are a number of package.json updates required for a new command, so we recommend you answer "y" so the command
takes care of them all. If you answer "n", you must update the package.json file manually.

#### Examples for dev generate command

Generate the files for a new "sf my exciting command":

```
   sf dev generate command --name my:exciting:command

```

Flags

```
   --flags-dir FLAGS-DIR
```

Optional


Salesforce CLI Command Reference dev Commands

Import flag values from a directory.

Type: option

**`-n`** **|** **`--name NAME`**
Required

Name of the new command. Use colons to separate the topic and command names.

Type: option

```
   --force
```

Optional

Overwrite existing files.

Type: boolean

```
   --dry-run
```

Optional

Display the changes that would be made without writing them to disk.

Type: boolean

```
   --nuts
```

Optional

Generate a NUT test file for the command.

Type: boolean

Default value: true

```
   --unit
```

Optional

Generate a unit test file for the command.

Type: boolean

Default value: true

#### **`dev generate flag`**

Generate a flag for an existing command.

#### Description for dev generate flag

You must run this command from within a plugin directory, such as the directory created with the "sf dev generate plugin" command.

This command is interactive. It first discovers all the commands currently implemented in the plugin, and asks you which you want to
create a new flag for. It then prompts for other flag properties, such as its long name, optional short name, type, whether it's required,
and so on. Long flag names must be kebab-case and not camelCase. The command doesn't let you use an existing long or short flag
name. When the command completes, the Typescript file for the command is updated with the code for the new flag.

Use the --dry-run flag to review new code for the command file without actually updating it.

#### Examples for dev generate flag

Generate a new flag and update the command file:

```
   sf dev generate flag

```


Salesforce CLI Command Reference dev Commands

Don't actually update the command file, just view the generated code:

```
   sf dev generate flag --dry-run

```

Flags

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option

**`-d`** **|** **`--dry-run`**
Optional

Print new flag code instead of adding it to the command file.

Type: boolean

#### **`dev generate plugin`**

Generate a new sf plugin.

#### Description for dev generate plugin

This command is interactive. You're prompted for information to populate your new plugin, such as its name, description, author, and
percentage of code coverage you want. The command clones the 'salesforcecli/plugin-template-sf' GitHub repository, installs the
plug-in's npm package dependencies using yarn install, and updates the package properties.

When the command completes, your new plugin contains the source, message, and test files for a sample "sf hello world" command.

#### Examples for dev generate plugin

```
   sf dev generate plugin

```

Flags

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option

```
   --dry-run
```

Optional

Display the changes that would be made without writing them to disk.

Type: boolean

#### Aliases for dev generate plugin

```
   plugins:generate

```


### Salesforce CLI Command Reference doctor Commands doctor Commands

Tools for diagnosing problems with Salesforce CLI.

### doctor

Gather CLI configuration data and run diagnostic tests to discover and report potential problems in your environment.

### **`doctor`**

Gather CLI configuration data and run diagnostic tests to discover and report potential problems in your environment.

### Description for doctor

When you run the doctor command without parameters, it first displays a diagnostic overview of your environment. It then writes a
detailed diagnosis to a JSON file in the current directory. Use the --outputdir to specify a different directory. To run diagnostic tests on
a specific plugin, use the --plugin parameter. If the plugin isn't listening to the doctor, then you get a warning.

Use the --command parameter to run a specific command in debug mode; the doctor writes both stdout and stderr to \*.log files that
you can provide to Salesforce Customer Support or attach to a GitHub issue.

Plugin providers can also implement their own doctor diagnostic tests by listening to the "sf-doctor" event and running plugin specific
tests that are then included in the doctor diagnostics log.

### Examples for doctor

Run CLI doctor diagnostics:

```
   sf doctor

```

Run CLI doctor diagnostics and the specified command, and write the debug output to a file:

```
   sf doctor --command "force:org:list --all"

```

Run CLI doctor diagnostics for a specific plugin:

```
   sf doctor --plugin @salesforce/plugin-source

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

**`-c`** **|** **`--command COMMAND`**
Optional

Command to run in debug mode; results are written to a log file.


### Salesforce CLI Command Reference flow Commands

Type: option

**`-p`** **|** **`--plugin PLUGIN`**
Optional

Specific plugin on which to run diagnostics.

Type: option

**`-d`** **|** **`--output-dir OUTPUT-DIR`**
Optional

Directory to save all created files rather than the current working directory.

Type: option

**`-i`** **|** **`--create-issue`**
Optional

Create a new issue on our GitHub repo and attach all diagnostic results.

Type: boolean

### flow Commands

Commands for testing flows

#### flow get test

Display test results for a specific asynchronous test run.

flow run test
Invoke flow tests in an org.

#### **`flow get test`**

Display test results for a specific asynchronous test run.

#### Description for flow get test

Provide a flow test run ID to display test results for an enqueued or completed asynchronous test run. The test run ID is displayed after
running the "sf flow run test" command.

To see code coverage results, use the --code-coverage flag with --result-format. The output displays a high-level summary of the test
run and the code coverage values for flow tests in your org. If you specify human-readable result format, use the --detailed-coverage
flag to see detailed coverage results for each test method run.

#### Examples for flow get test

Display flow test results for your default org using a test run ID:

```
   sf flow get test --test-run-id <test run id>

```

Similar to previous example, but output the result in JUnit format:

```
   sf flow get test --test-run-id <test run id> --result-format junit

```


Salesforce CLI Command Reference flow Commands

Also retrieve code coverage results and output in JSON format:

```
   sf flow get test --test-run-id <test run id> --code-coverage --json

```

Specify a directory in which to save the test results from the org with the “me@my.org” username (rather than your default org):

```
   sf flow get test --test-run-id <test run id> --code-coverage --output-dir <path to outputdir>

    --target-org me@my.org'

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

**`-i`** **|** **`--test-run-id TEST-RUN-ID`**
Required

ID of the test run.

Type: option

**`-c`** **|** **`--code-coverage`**
Optional

Retrieve code coverage results.

Type: boolean

```
   --detailed-coverage
```

Optional

Not available for flow tests.

Type: boolean

**`-d`** **|** **`--output-dir OUTPUT-DIR`**
Optional

Directory in which to store test result files.

Type: option


Salesforce CLI Command Reference flow Commands

**`-r`** **|** **`--result-format RESULT-FORMAT`**
Optional

Format of the test results.

Type: option

Permissible values are: human, tap, junit, json

Default value: human

```
   --concise
```

Optional

Display only failed test results; works with human-readable output only.

Type: boolean

#### **`flow run test`**

Invoke flow tests in an org.

#### Description for flow run test

Specify which tests to run by using the --class-names flag followed by the names of the flows you want to test. For example, if you save
a flow with the name Flow1, then use: --class-names Flow1.

To see code coverage results, use the --code-coverage flag with --result-format. The output displays a high-level summary of the test
run and the code coverage values for classes in your org. If you specify human-readable result format, use the --detailed-coverage flag
to see detailed coverage results for each test method run.

By default, "flow run test" runs asynchronously and immediately returns a test run ID. If you use the -–synchronous flag, you can use the
--wait flag to specify the number of minutes to wait; if the tests finish in that timeframe, the command displays the results. If the tests
haven't finished by the end of the wait time, the command displays a test run ID. Use the "flow get test --test-run-id" command to get
the results.

To run both Flow and Apex tests together, run the "sf logic run test" CLI command, which has similar flags as this command, but expands
the --tests flag to also include Apex tests.

You must have the "View All Data" org system permission to use this command. The permission is disabled by default and can be enabled
only by a system administrator.

#### Examples for flow run test

Run all local tests in your default org:

```
   sf flow run test --test-level RunLocalTests

```

Run all the Flow1 and Flow2 flow tests in the org with alias “scratchOrg”:

```
   sf flow run test --target-org scratchOrg --class-names Flow1 --class-names Flow2

```

Run specific Flow1 and Flow2 flow tests in your default org:

```
   sf flow run test --tests Flow1.Test1 --tests Flow2.Test2 --test-level RunSpecifiedTests

```

Run all tests synchronously in your default org; the command waits to display the test results until all tests finish:

```
   sf flow run test –synchronous

```


Salesforce CLI Command Reference flow Commands

Run all local tests in the org with the username “me@my.org”; save the output to the specified directory:

```
   sf flow run test --test-level RunLocalTests --output-dir /Users/susan/temp/cliOutput

   --target-org me@my.org

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

**`-r`** **|** **`--result-format RESULT-FORMAT`**
Optional

Format of the test results.

Type: option

Permissible values are: human, tap, junit, json

Default value: human

```
   --concise
```

Optional

Display only failed test results; works with human-readable output only.

Type: boolean

**`-d`** **|** **`--output-dir OUTPUT-DIR`**
Optional

Directory in which to store test result files.

Type: option

**`-c`** **|** **`--code-coverage`**
Optional

Retrieve code coverage results.

Type: boolean


### Salesforce CLI Command Reference force Commands

**`-y`** **|** **`--synchronous`**
Optional

Run flow tests for one flow synchronously; if not specified, tests are run asynchronously.

Type: boolean

**`-l`** **|** **`--test-level TEST-LEVEL`**
Optional

Level of tests to run; default is RunLocalTests.

Here's what the levels mean:

      - RunLocalTests — All tests in your org are run, except the ones that originate from installed managed and unlocked packages.

      - RunAllTestsInOrg — All tests are run. The tests include all tests in your org, including tests of managed packages.

      - RunSpecifiedTests - Only the tests that you specify with the --tests flag are run.

Type: option

Permissible values are: RunLocalTests, RunAllTestsInOrg, RunSpecifiedTests

**`-n`** **|** **`--class-names CLASS-NAMES`**
Optional

Flow names that contain flow tests to run.

Default is all flow tests. If you select --class-names, you can't specify --tests.

Type: option

**`-s`** **|** **`--suite-names SUITE-NAMES`**
Optional

Not available for flow tests.

Not available for flow tests.

Type: option

**`-t`** **|** **`--tests TESTS`**
Optional

Flow test names to run.

Default is all flow tests. If you specify --tests, you can't specify --class-names.

Type: option

### force Commands

Legacy commands for backward compatibility.

force data bulk delete
Bulk delete records from an org using a CSV file. Uses Bulk API 1.0.

force data bulk status
View the status of a bulk data load job or batch. Uses Bulk API 1.0.

force data bulk upsert
Bulk upsert records to an org from a CSV file. Uses Bulk API 1.0.


Salesforce CLI Command Reference force Commands

force lightning lwc test create

force lightning lwc test run

force lightning lwc test setup

#### **`force data bulk delete`**

Bulk delete records from an org using a CSV file. Uses Bulk API 1.0.

#### Description for force data bulk delete

The CSV file must have only one column ("Id") and then the list of record IDs you want to delete, one ID per line.

When you execute this command, it starts a job and one or more batches, displays their IDs, and then immediately returns control of
the terminal to you by default. If you prefer to wait, set the --wait flag to the number of minutes; if it times out, the command outputs
the IDs. Use the job and batch IDs to check the status of the job with the "sf force data bulk status" command. A single job can contain
many batches, depending on the length of the CSV file.

#### Examples for force data bulk delete

Bulk delete Account records from your default org using the list of IDs in the "files/delete.csv" file:

```
   sf force data bulk delete --sobject Account --file files/delete.csv

```

Bulk delete records from a custom object in an org with alias my-scratch and wait 5 minutes for the command to complete:

```
   sf force data bulk delete --sobject MyObject__c --file files/delete.csv --wait 5 --target-org

    my-scratch

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


Salesforce CLI Command Reference force Commands

**`-f`** **|** **`--file FILE`**
Required

CSV file that contains the IDs of the records to delete.

Type: option

**`-s`** **|** **`--sobject SOBJECT`**
Required

API name of the Salesforce object, either standard or custom, that you want to delete records from.

Type: option

**`-w`** **|** **`--wait WAIT`**
Optional

Number of minutes to wait for the command to complete before displaying the results.

Type: option

#### **`force data bulk status`**

View the status of a bulk data load job or batch. Uses Bulk API 1.0.

#### Description for force data bulk status

Run this command using the job ID or batch ID returned from the "sf force data bulk delete" or "sf force data bulk upsert" commands.

#### Examples for force data bulk status

View the status of a bulk load job in your default org:

```
   sf force data bulk status --job-id 750xx000000005sAAA

```

View the status of a bulk load job and a specific batches in an org with alias my-scratch:

```
   sf force data bulk status --job-id 750xx000000005sAAA --batch-id 751xx000000005nAAA

   --target-org my-scratch

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


Salesforce CLI Command Reference force Commands

Type: option

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

**`-b`** **|** **`--batch-id BATCH-ID`**
Optional

ID of the batch whose status you want to view; you must also specify the job ID.

Type: option

**`-i`** **|** **`--job-id JOB-ID`**
Required

ID of the job whose status you want to view.

Type: option

#### **`force data bulk upsert`**

Bulk upsert records to an org from a CSV file. Uses Bulk API 1.0.

#### Description for force data bulk upsert

An upsert refers to inserting a record into a Salesforce object if the record doesn't already exist, or updating it if it does exist.

When you execute this command, it starts a job and one or more batches, displays their IDs, and then immediately returns control of
the terminal to you by default. If you prefer to wait, set the --wait flag to the number of minutes; if it times out, the command outputs
the IDs. Use the job and batch IDs to check the status of the job with the "sf force data bulk status" command. A single job can contain
many batches, depending on the length of the CSV file.

See "Prepare CSV Files" in the Bulk API Developer Guide for details on formatting your CSV file.
(https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/datafiles_csv_preparing.htm)

By default, the job runs the batches in parallel, which we recommend. You can run jobs serially by specifying the --serial flag. But don't
process data in serial mode unless you know this would otherwise result in lock timeouts and you can't reorganize your batches to avoid
the locks.

#### Examples for force data bulk upsert

Bulk upsert records to the Contact object in your default org:

```
   sf --sobject Contact --file files/contacts.csv --external-id Id

```

Bulk upsert records to a custom object in an org with alias my-scratch and wait 5 minutes for the command to complete:

```
   sf force data bulk upsert --sobject MyObject__c --file files/file.csv --external-id

   MyField__c --wait 5 --target-org my-scratch

```

Flags

```
   --json
```

Optional


Salesforce CLI Command Reference force Commands

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

**`-i`** **|** **`--external-id EXTERNAL-ID`**
Required

Name of the external ID field, or the Id field.

Type: option

**`-f`** **|** **`--file FILE`**
Required

CSV file that contains the records to upsert.

Type: option

**`-s`** **|** **`--sobject SOBJECT`**
Required

API name of the Salesforce object, either standard or custom, that you want to upsert records to.

Type: option

**`-w`** **|** **`--wait WAIT`**
Optional

Number of minutes to wait for the command to complete before displaying the results.

Type: option

**`-r`** **|** **`--serial`**
Optional

Run batches in serial mode.

Type: boolean

#### **`force lightning lwc test create`** Description for force lightning lwc test create

creates a Lightning web component test file with boilerplate code inside a __tests__ directory.


Salesforce CLI Command Reference force Commands

Examples for **`force lightning lwc test create`**

```
   $ sfdx force:lightning:lwc:test:create -f force-app/main/default/lwc/myButton/myButton.js

```

Flags

```
   --json
```

Optional

format output as json

Type: boolean

```
   --loglevel LOGLEVEL
```

Optional

logging level for this command invocation

Type: enum

Permissible values are: trace, debug, info, warn, error, fatal, TRACE, DEBUG, INFO, WARN, ERROR, FATAL

Default value: warn

**`-f`** **|** **`--filepath FILEPATH`**
Required

path to Lightning web component .js file to create a test for

Type: string

#### **`force lightning lwc test run`** Description for force lightning lwc test run

invokes Lightning Web Components Jest unit tests.

#### Examples for force lightning lwc test run

```
   $ sfdx force:lightning:lwc:test:run

   $ sfdx force:lightning:lwc:test:run -w

```

Flags

```
   --json
```

Optional

format output as json

Type: boolean

```
   --loglevel LOGLEVEL
```

Optional

logging level for this command invocation

Type: enum


### Salesforce CLI Command Reference info Commands

Permissible values are: trace, debug, info, warn, error, fatal, TRACE, DEBUG, INFO, WARN, ERROR, FATAL

Default value: warn

**`-d`** **|** **`--debug`**
Optional

run tests in debug mode

Type: boolean

```
   --watch
```

Optional

run tests in watch mode

Type: boolean

#### **`force lightning lwc test setup`** Description for force lightning lwc test setup

install Jest unit testing tools for Lightning Web Components.

#### Examples for force lightning lwc test setup

```
   $ sfdx force:lightning:lwc:test:setup

```

Flags

```
   --json
```

Optional

format output as json

Type: boolean

```
   --loglevel LOGLEVEL
```

Optional

logging level for this command invocation

Type: enum

Permissible values are: trace, debug, info, warn, error, fatal, TRACE, DEBUG, INFO, WARN, ERROR, FATAL

Default value: warn

### info Commands

Access Salesforce CLI information from the command line.

info releasenotes display
Display Salesforce CLI release notes on the command line.


### Salesforce CLI Command Reference lightning Commands

#### **`info releasenotes display`**

Display Salesforce CLI release notes on the command line.

#### Description for info releasenotes display

By default, this command displays release notes for the currently installed CLI version on your computer. Use the --version flag to view
release notes for a different release.

#### Examples for info releasenotes display

Display release notes for the currently installed CLI version:

```
   sf info releasenotes display

```

Display release notes for CLI version 7.120.0:

```
   sf info releasenotes display --version 7.120.0

```

Display release notes for the CLI version that corresponds to a tag (stable, stable-rc, latest, latest-rc, rc):

```
   sf info releasenotes display --version latest

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

**`-v`** **|** **`--version VERSION`**
Optional

CLI version or tag for which to display release notes.

Type: option

#### Aliases for info releasenotes display

```
   whatsnew

### lightning Commands

```

Commands to work with Lightning applications.

lightning dev app
Preview a Lightning Experience app locally and in real-time, without deploying it.


Salesforce CLI Command Reference lightning Commands

lightning dev component
Preview LWC components in isolation.

lightning dev site
Preview an Experience Builder site locally and in real-time, without deploying it.

#### **`lightning dev app`**

Preview a Lightning Experience app locally and in real-time, without deploying it.

#### Description for lightning dev app

Use Local Dev to see local changes to your app in a real-time preview that you don't have to deploy or manually refresh. To let you
quickly iterate on your Lightning web components (LWCs) and pages, your app preview automatically refreshes when Local Dev detects
source code changes.

When you edit these local files with Local Dev enabled, your org automatically reflects these changes.

    - Basic HTML and CSS edits to LWCs

    - JavaScript changes to LWCs that don't affect the component's public API

    - Importing new custom LWCs

    - Importing another instance of an existing LWC

To apply any other local changes not listed above, you must deploy them to your org using the `sf project deploy start` command.

When you make changes directly in your org (like saving new component properties), they're automatically deployed to your live app.
To update your local version of the app with those changes, you must retrieve them from your org using the `sf project retrieve start`
command.

If you run the command without flags, it displays a list of devices for you to choose from. Then it lists the apps that it found in your local
DX project for you to choose. Use the --device or --name flags to bypass the questions. The command also asks if you want to enable
Local Dev in your org if it isn't already.

To learn more about Local Dev enablement, considerations, and limitations, see the Lightning Web Components Developer Guide
(https://developer.salesforce.com/docs/platform/lwc/guide/get-started-test-components.html).

#### Examples for lightning dev app

Preview the default app for the target org "myOrg" in a desktop environment:

```
   sf lightning dev app --target-org myOrg

```

Preview the app "myApp" for the target org "myOrg" in a desktop environment:

```
   sf lightning dev app --name MyApp --target-org myOrg --device-type desktop

```

Preview the default app for target org "myOrg" on an iOS device:

```
   sf lightning dev app --target-org myOrg --device-type ios --device-id "iPhone 15 Pro Max"

```

Flags

```
   --flags-dir FLAGS-DIR
```

Optional


Salesforce CLI Command Reference lightning Commands

Import flag values from a directory.

Type: option

**`-n`** **|** **`--name NAME`**
Optional

Name of the Lightning Experience app to preview.

Type: option

**`-o`** **|** **`--target-org TARGET-ORG`**
Required

Username or alias of the target org. Not required if the `target-org` configuration variable is already set.

Type: option

**`-t`** **|** **`--device-type DEVICE-TYPE`**
Optional

Type of device to display the app preview.

Type: option

Permissible values are: desktop, ios, android

**`-i`** **|** **`--device-id DEVICE-ID`**
Optional

ID of the mobile device to display the preview if device type is set to `ios` or `android`. The default value is the ID of the first available
mobile device.

Type: option

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

#### **`lightning dev component`**

Preview LWC components in isolation.

#### Description for lightning dev component

Component preview launches an isolated development environment for Lightning Web Components, enabling rapid iteration without
needing to deploy changes. The server provides real-time previews of your components through hot module replacement (HMR),
automatically refreshing the view when source files are modified.

When running the development server, these changes are immediately reflected:

    - Component template (HTML) modifications

    - Styling updates in component CSS files

    - JavaScript logic changes that don't modify the component's API

    - Adding or updating internal component dependencies

    - Modifying static resources used by the component


Salesforce CLI Command Reference lightning Commands

If you run the command without flags, it displays a list of components that it found in your local DX project for you to choose to preview.
Use the --name flag to bypass the question. The command also asks if you want to enable Local Dev in your org if it isn't already.

See the LWC Developer Guide for more information about component development best practices and limitations
(https://developer.salesforce.com/docs/platform/lwc/guide/get-started-best-practices.html).

Examples for **`lightning dev component`**

Select a component interactively and launch the component preview; use your default org:

```
   sf lightning dev component

```

Launch component preview for "myComponent"; use the org with alias "myscratch":

```
   sf lightning dev component --name myComponent --target-org myscratch

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
Optional

Name of a component to preview.

Type: option

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

**`-c`** **|** **`--client-select`**
Optional

Launch component preview without selecting a component.

Type: boolean

**`-o`** **|** **`--target-org TARGET-ORG`**
Required

Username or alias of the target org. Not required if the `target-org` configuration variable is already set.

Type: option


Salesforce CLI Command Reference lightning Commands

#### **`lightning dev site`**

Preview an Experience Builder site locally and in real-time, without deploying it.

#### Description for lightning dev site

Enable Local Dev to see local changes to your site in a real-time preview that you don't have to deploy or manually refresh. To let you
quickly iterate on your Lightning web components (LWCs) and pages, your site preview automatically refreshes when Local Dev detects
source code changes.

When you edit these local files with Local Dev enabled, your org automatically reflects these changes.

    - Basic HTML and CSS edits to LWCs

    - JavaScript changes to LWCs that don't affect the component's public API

    - Importing new custom LWCs

    - Importing another instance of an existing LWC

To apply any other local changes not listed above, you must deploy them to your org using the `sf project deploy start` command. Then
republish your site and restart the server for the Local Dev experience.

If you run the command without flags, it displays a list of Experience Builder sites that it found in your local DX project for you to choose
from. Use the --name flag to bypass the question. The command also asks if you want to enable Local Dev in your org if it isn't already.

For more considerations and limitations, see the Lightning Web Components Developer Guide.

#### Examples for lightning dev site

Select a site to preview from the org with alias "myOrg":

```
   sf lightning dev site --target-org myOrg

```

Preview the site "Partner Central" from your default org:

```
   sf lightning dev site --name "Partner Central"

```

Flags

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option

**`-n`** **|** **`--name NAME`**
Optional

Name of the Experience Builder site to preview. It must match a site name from the current org.

Type: option

**`-o`** **|** **`--target-org TARGET-ORG`**
Required

Username or alias of the target org. Not required if the `target-org` configuration variable is already set.

Type: option


### Salesforce CLI Command Reference logic Commands

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

### logic Commands

Use the logic commands to run Apex and Flow tests and view the test results.

#### logic get test (Beta)

Get the results of a test run.

logic run test (Beta)
Invoke tests for Apex and Flows in an org.

#### logic get test (Beta)

Get the results of a test run.

Note: This feature is a Beta Service. Customers may opt to try such Beta Service in its sole discretion. Any use of the Beta Service
is subject to the applicable Beta Services Terms provided at Agreements and Terms
[(https://www.salesforce.com/company/legal/agreements/).](https://www.salesforce.com/company/legal/agreements/)

#### Description for logic get test

When you run 'sf logic run test' to test Apex classes and Flows asynchronously, it returns a test run ID. Use that ID with this command
to see the results.

To see code coverage results, use the --code-coverage flag with --result-format. The output displays a high-level summary of the test
run and the code coverage values for classes in your org. If you specify human-readable result format, use the --detailed-coverage flag
to see detailed coverage results for each test method run.

#### Examples for logic get test

Get the results for a specific test run ID in the default human-readable format; uses your default org:

```
   sf logic get test --test-run-id <test run id>

```

Get the results for a specific test run ID, format them as JUnit, and save them to the "test-results/junit" directory; uses the org with alias
"my-scratch":

```
   sf logic get test --test-run-id <test run id> --result-format junit --target-org my-scratch

```

Flags

```
   --json
```

Optional

Format output as json.

Type: boolean


Salesforce CLI Command Reference logic Commands

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

**`-i`** **|** **`--test-run-id TEST-RUN-ID`**
Required

ID of the test run.

Type: option

**`-c`** **|** **`--code-coverage`**
Optional

Retrieve code coverage results.

Type: boolean

```
   --detailed-coverage
```

Optional

Display detailed code coverage per test.

Type: boolean

**`-d`** **|** **`--output-dir OUTPUT-DIR`**
Optional

Directory in which to store test result files.

Type: option

**`-r`** **|** **`--result-format RESULT-FORMAT`**
Optional

Format of the test results.

Type: option

Permissible values are: human, tap, junit, json

Default value: human

```
   --concise
```

Optional

Display only failed test results; works with human-readable output only.

Type: boolean


Salesforce CLI Command Reference logic Commands

#### logic run test (Beta)

Invoke tests for Apex and Flows in an org.

Note: This feature is a Beta Service. Customers may opt to try such Beta Service in its sole discretion. Any use of the Beta Service
is subject to the applicable Beta Services Terms provided at Agreements and Terms
[(https://www.salesforce.com/company/legal/agreements/).](https://www.salesforce.com/company/legal/agreements/)

#### Description for logic run test

This command provides a single and unified way to run tests for multiple Salesforce features, such as Apex classes and Flows. Running
the tests together with a single command ensures seamless interoperability between the features.

By default, the command executes asynchronously and returns a test run ID. Then use the "sf logic get test" command to retrieve the
results. If you want to wait for the test run to complete and see the results in the command output, use the --synchronous flag.

To run specific tests, use the --tests flag and pass it the names of Apex and Flow tests. For Apex, simply specify the name of the Apex
test class. For Flows, use the format "FlowTesting.<name-of-flow-test>". To find the name of all the flow tests in your org, run this
command and specify the Flow category, such as "sf logic run test --synchronous --test-category Flow --test-level RunAllTestsInOrg".
The command displays a table of all the flow tests it ran; see the "TEST NAME" column for the full name of all available flow tests in your
org.

You can also run specific test methods, although if you run the tests synchronously, the methods must belong to a single Apex class or
Flow test. To run all tests of a certain category, use --test-category and --test-level together. If neither of these flags is specified, all local
tests for all categories are run by default. You can also use the --class-names and --suite-names flags to run Apex test classes or suites.

To see code coverage results, use the --code-coverage flag with --result-format. The output displays a high-level summary of the test
run and the code coverage values for the tested classes or flows. If you specify human-readable result format, use the --detailed-coverage
flag to see detailed coverage results for each test method run.

You must have the "View All Data" org system permission to use this command. The permission is disabled by default and can be enabled
only by a system administrator.

#### Examples for logic run test

Run a mix of specific Apex and Flow tests asynchronously in your default org:

```
   sf logic run test --tests

   MyApexClassTest,FlowTesting.Modify_Account_Desc.Modify_Account_Desc_TestAccountDescription

```

Run all local Apex and Flow tests and wait for the results to complete; run the tests in the org with alias "my-scratch":

```
   sf logic run test --test-level RunLocalTests --test-category Apex --test-category Flow

   --synchronous --target-org my-scratch

```

Run two methods in an Apex test class and an Apex test suite:

```
   sf logic run test --class-names MyApexClassTest.methodA --class-names MyApexClassTest.methodB

    --suite-names MySuite

```

Run all local tests for all categories (the default behavior), save the JUnit results to the "test-results" directory, and include code coverage
results:

```
   sf logic run test --result-format junit --output-dir test-results --synchronous

   --code-coverage

```


Salesforce CLI Command Reference logic Commands

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

**`-c`** **|** **`--code-coverage`**
Optional

Retrieve code coverage results.

Type: boolean

**`-d`** **|** **`--output-dir OUTPUT-DIR`**
Optional

Directory in which to store test run files.

Type: option

**`-l`** **|** **`--test-level TEST-LEVEL`**
Optional

Level of tests to run; default is RunLocalTests.

Here's what the levels mean:

      - RunSpecifiedTests — Only the tests that you specify in the runTests option are run. Code coverage requirements differ from the
default coverage requirements when using this test level. The executed tests must cover each class and trigger in the deployment
package for a minimum of 75% code coverage. This coverage is computed for each class and triggers individually, and is different
than the overall coverage percentage.

      - RunLocalTests — All local tests in your org, including tests that originate from no-namespaced unlocked packages, are run. The
tests that originate from installed managed packages and namespaced unlocked packages aren't run. This test level is the default
for production deployments that include Apex classes or triggers.

      - RunAllTestsInOrg — All tests are run. The tests include all tests in your org.

Type: option

Permissible values are: RunLocalTests, RunAllTestsInOrg, RunSpecifiedTests


Salesforce CLI Command Reference logic Commands

**`-n`** **|** **`--class-names CLASS-NAMES`**
Optional

Apex test class names to run; default is all classes.

If you select --class-names, you can't specify --suite-names or --tests.

For multiple classes, repeat the flag for each.

--class-names Class1 --class-names Class2

Type: option

**`-r`** **|** **`--result-format RESULT-FORMAT`**
Optional

Format of the test results.

Type: option

Permissible values are: human, tap, junit, json

Default value: human

**`-s`** **|** **`--suite-names SUITE-NAMES`**
Optional

Apex test suite names to run.

If you select --suite-names, you can't specify --class-names or --tests.

For multiple suites, repeat the flag for each.

--suite-names Suite1 --suite-names Suite2

Type: option

**`-t`** **|** **`--tests TESTS`**
Optional

Comma-separated list of test names to run. Can include Apex test classes and Flow tests.

If you specify --tests, you can't specify --class-names or --suite-names

For multiple tests, repeat the flag for each.

--tests Test1 --tests Test2

Type: option

**`-w`** **|** **`--wait WAIT`**
Optional

Sets the streaming client socket timeout in minutes; specify a longer wait time if timeouts occur frequently.

Type: option

**`-y`** **|** **`--synchronous`**
Optional

Runs test methods from a single Apex class synchronously; if not specified, tests are run asynchronously.

Type: boolean

**`-v`** **|** **`--detailed-coverage`**
Optional

Display detailed code coverage per test.


### Salesforce CLI Command Reference org Commands

Type: boolean

```
   --concise
```

Optional

Display only failed test results; works with human-readable output only.

Type: boolean

```
   --test-category TEST-CATEGORY
```

Optional

Category of tests to run, such as Apex or Flow.

Type: option

Permissible values are: Apex, Flow

### org Commands

Commands to create and manage orgs and scratch org users.

org assign permset
Assign a permission set to one or more org users.

org assign permsetlicense
Assign a permission set license to one or more org users.

org auth show-access-token
Show the current access token for an org.

org auth show-sfdx-auth-url
Show the SFDX Auth URL for an org.

org auth show-user-password
Show the stored password for an org's user.

org create agent-user
Create the default Salesforce user that is used to run an agent.

org create sandbox
Create a sandbox org.

org create scratch
Create a scratch org.

org create shape
Create a scratch org configuration (shape) based on the specified source org.

org create snapshot
Create a snapshot of a scratch org.

org create user
Create a user for a scratch org.

org delete sandbox
Delete a sandbox.

org delete scratch
Delete a scratch org.


Salesforce CLI Command Reference org Commands

org delete shape
Delete all org shapes for a target org.

org delete snapshot
Delete a scratch org snapshot.

org disable tracking
Prevent Salesforce CLI from tracking changes in your source files between your project and an org.

org display
Display information about an org.

org display user
Display information about a Salesforce user.

org enable tracking
Allow Salesforce CLI to track changes in your source files between your project and an org.

org generate password
Generate a random password for scratch org users.

org get snapshot
Get details about a scratch org snapshot.

org list
List all orgs you’ve created or authenticated to.

org list auth
List authorization information about the orgs you created or logged into.

org list limits
Display information about limits in your org.

org list metadata
List the metadata components and properties of a specified type.

org list metadata-types
Display details about the metadata types that are enabled for your org.

org list shape
List all org shapes you’ve created.

org list snapshot
List scratch org snapshots.

org list sobject record-counts
Display record counts for the specified standard or custom objects.

org list users
List all locally-authenticated users of an org.

org login access-token
Authorize an org using an existing Salesforce access token.

org login jwt
Log in to a Salesforce org using a JSON web token (JWT).

org login sfdx-url
Authorize an org using a Salesforce DX authorization URL stored in a file or through standard input (stdin).


Salesforce CLI Command Reference org Commands

org login web
Log in to a Salesforce org using the web server flow.

org logout
Log out of a Salesforce org.

org open
Open your default scratch org, or another specified org, in a browser.

org open agent
Open an agent in your org's Agentforce Builder UI in a browser.

org open authoring-bundle (Deprecated)
The command `org open authoring-bundle` has been deprecated. Open your org in Agentforce Studio, specifically in
the list view showing the list of agents.

org refresh sandbox
Refresh a sandbox org using the sandbox name.

org resume sandbox
Check the status of a sandbox creation, and log in to it if it's ready.

org resume scratch
Resume the creation of an incomplete scratch org.

#### **`org assign permset`**

Assign a permission set to one or more org users.

#### Description for org assign permset

To specify an alias for the --target-org or --on-behalf-of flags, use the CLI username alias, such as the one you set with the "alias set"
command. Don't use the value of the Alias field of the User Salesforce object for the org user.

To assign multiple permission sets, either set multiple --name flags or a single --name flag with multiple names separated by spaces.
Enclose names that contain spaces in one set of double quotes. The same syntax applies to --on-behalf-of.

#### Examples for org assign permset

Assign two permission sets called DreamHouse and CloudHouse to original admin user of your default org:

```
   sf org assign permset --name DreamHouse --name CloudHouse

```

Assign the Dreamhouse permission set to the original admin user of the org with alias "my-scratch":

```
   sf org assign permset --name DreamHouse --target-org my-scratch

```

Assign the Dreamhouse permission set to the specified list of users of your default org:

```
   sf org assign permset --name DreamHouse --on-behalf-of user1@my.org --on-behalf-of user2

   --on-behalf-of user

```

Flags

```
   --json
```

Optional


Salesforce CLI Command Reference org Commands

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

Permission set to assign.

Type: option

**`-b`** **|** **`--on-behalf-of ON-BEHALF-OF`**
Optional

Username or alias to assign the permission set to.

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

#### **`org assign permsetlicense`**

Assign a permission set license to one or more org users.

#### Description for org assign permsetlicense

To specify an alias for the --target-org or --on-behalf-of flags, use the CLI username alias, such as the one you set with the "alias set"
command. Don't use the value of the Alias field of the User Salesforce object for the org user.

To assign multiple permission sets, either set multiple --name flags or a single --name flag with multiple names separated by spaces.
Enclose names that contain spaces in one set of double quotes. The same syntax applies to --on-behalf-of.

#### Examples for org assign permsetlicense

Assign the DreamHouse permission set license to original admin user of your default org:

```
   sf org assign permsetlicense --name DreamHouse

```

Assign two permission set licenses to the original admin user of the org with alias "my-scratch":

```
   sf org assign permsetlicense --name DreamHouse --name CloudHouse --target-org my-scratch

```


Salesforce CLI Command Reference org Commands

Assign the Dreamhouse permission set license to the specified list of users of your default org:

```
   sf org assign permsetlicense --name DreamHouse --on-behalf-of user1@my.org --on-behalf-of

    user2 --on-behalf-of user3

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

Name of the permission set license to assign.

Type: option

**`-b`** **|** **`--on-behalf-of ON-BEHALF-OF`**
Optional

Usernames or alias to assign the permission set license to.

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

#### **`org auth show-access-token`**

Show the current access token for an org.

#### Description for org auth show-access-token

Because access tokens are sensitive credentials that grant full access to an org, this command prompts for confirmation before revealing
the token. Skip confirmation by specifying either the --no-prompt or --json flag.


Salesforce CLI Command Reference org Commands

Examples for **`org auth show-access-token`**

Show the access token for the default org:

```
   sf org auth show-access-token

```

Show the access token for an org with alias "my-org":

```
   sf org auth show-access-token --target-org my-org

```

Show the access token without the confirmation prompt:

```
   sf org auth show-access-token --target-org my-org --no-prompt

```

Get the access token as JSON for use in scripts:

```
   sf org auth show-access-token --target-org my-org --json

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

**`-p`** **|** **`--no-prompt`**
Optional

Skip the security warning and reveal the access token without confirmation.

Type: boolean

#### **`org auth show-sfdx-auth-url`**

Show the SFDX Auth URL for an org.

#### Description for org auth show-sfdx-auth-url

Shows the SFDX Auth URL for an org. This URL is only available for orgs authenticated via a web-based OAuth flow. This command
prompts for confirmation before revealing it. Skip confirmation by specifying either the --no-prompt or --json flag.


Salesforce CLI Command Reference org Commands

Examples for **`org auth show-sfdx-auth-url`**

Show the SFDX Auth URL for the default org:

```
   sf org auth show-sfdx-auth-url

```

Show the SFDX Auth URL for an org with alias "my-org":

```
   sf org auth show-sfdx-auth-url --target-org my-org

```

Show the SFDX Auth URL without the confirmation prompt:

```
   sf org auth show-sfdx-auth-url --target-org my-org --no-prompt

```

Get the SFDX Auth URL as JSON for use in scripts:

```
   sf org auth show-sfdx-auth-url --target-org my-org --json

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

**`-p`** **|** **`--no-prompt`**
Optional

Skip the security warning and reveal the SFDX Auth URL without confirmation.

Type: boolean

#### **`org auth show-user-password`**

Show the stored password for an org's user.

#### Description for org auth show-user-password

This command shows only passwords that were generated locally in your DX project with either the "org generate password" or "org
create user" CLI command. If you generated a password for a user in Setup in your org, you can't show it with this command.

Because passwords are sensitive credentials, this command prompts for confirmation before revealing it. Skip confirmation by specifying
either the --no-prompt or --json flag.


Salesforce CLI Command Reference org Commands

Examples for **`org auth show-user-password`**

Show the password for the default org's user:

```
   sf org auth show-user-password

```

Show the password for an org with alias "my-org":

```
   sf org auth show-user-password --target-org my-org

```

Show the password without the confirmation prompt:

```
   sf org auth show-user-password --target-org my-org --no-prompt

```

Get the password as JSON for use in scripts:

```
   sf org auth show-user-password --target-org my-org --json

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

**`-p`** **|** **`--no-prompt`**
Optional

Skip the security warning and reveal the password without confirmation.

Type: boolean

#### **`org create agent-user`**

Create the default Salesforce user that is used to run an agent.

#### Description for org create agent-user

You specify this user in the agent's Agent Script file using the "default_agent_user" parameter in the "config" block.

By default, this command:

    - Generates a user called "Agent User" with a globally unique username. Use flags to change these default names.

    - Sets the user's email to the new username.


Salesforce CLI Command Reference org Commands

    - Assigns the user the "Einstein Agent User" profile.

    - Assigns the user these required permission sets: AgentforceServiceAgentBase, AgentforceServiceAgentUser,

EinsteinGPTPromptTemplateUser

    - Checks that the user licenses required by the profile and permission sets are available in your org.

The generated user doesn't have a password. You can’t log into Salesforce using the agent user's username. Only

Salesforce users with admin permissions can view or edit an agent user in Setup.

To assign additional permission sets or licenses after the user was created, use the "org assign permset" or "org assign

permsetlicense" commands.

When the command completes, it displays a summary of what it did, including the new agent user's username and ID, the

available licenses associated with the Einstein Agent User profile, and the profile and permission sets assigned to the

agent user.

Examples for **`org create agent-user`**

Create an agent user with an auto-generated username; create the user in the org with alias "myorg":

```
   sf org create agent-user --target-org myorg

```

Create an agent user by specifying a base username pattern; to make the username unique, the command appends a unique

identifier:

```
   sf org create agent-user --base-username service-agent@corp.com --target-org myorg

```

Create an agent user with an auto-generated username but the custom name "Service Agent"; create the user in your

default org:

```
   sf org create agent-user --first-name Service --last-name Agent

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


Salesforce CLI Command Reference org Commands

Override the api version used for api requests made by this command

Type: option

```
   --base-username BASE-USERNAME
```

Optional

Base username pattern. A unique ID is appended to ensure global uniqueness of the usename.

Specify a base username in email format, such as "service-agent@corp.com". The command then appends a 12-character

globally unique ID (GUID) to the name before the "@" sign, which ensures that the username is globally unique across all

Salesforce orgs and sandboxes.

For example, if you specify "service-agent@corp.com", then the username might be "service-agent.a1b2c3d4e5f6@corp.com".

If not specified, the command auto-generates the username using this pattern: "agent.user.<GUID>@your-org-domain.com".

Type: option

```
   --first-name FIRST-NAME
```

Optional

First name for the agent user.

Type: option

Default value: Agent

```
   --last-name LAST-NAME
```

Optional

Last name for the agent user.

Type: option

Default value: User

#### **`org create sandbox`**

Create a sandbox org.

#### Description for org create sandbox

There are two ways to create a sandbox org: specify a definition file that contains the sandbox options or use the --name and --license-type
flags to specify the two required options. If you want to set an option other than name or license type, such as apexClassId, you must
use a definition file.

You can also use this command to clone an existing sandbox. Use the --source-sandbox-name flag to specify the existing sandbox name
and the --name flag to the name of the new sandbox.

#### Examples for org create sandbox

Create a sandbox org using a definition file and give it the alias "MyDevSandbox". The production org that contains the sandbox license
has the alias "prodOrg".

```
   sf org create sandbox --definition-file config/dev-sandbox-def.json --alias MyDevSandbox

   --target-org prodOrg

```


Salesforce CLI Command Reference org Commands

Create a sandbox org by directly specifying its name and type of license (Developer) instead of using a definition file. Set the sandbox
org as your default.

```
   sf org create sandbox --name mysandbox --license-type Developer --alias MyDevSandbox

   --target-org prodOrg --set-default

```

Clone the existing sandbox with name "ExistingSandbox" and name the new sandbox "NewClonedSandbox". Set the new sandbox as
your default org. Wait for 30 minutes for the sandbox creation to complete.

```
   sf org create sandbox --source-sandbox-name ExistingSandbox --name NewClonedSandbox

   --target-org prodOrg --alias MyDevSandbox --set-default --wait 30

```

Clone the existing sandbox with ID "0GQB0000000TVobOAG" and do not wait.

```
   sf org create sandbox --source-id 0GQB0000000TVobOAG --name SbxClone --target-org prodOrg

    --async

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

**`-f`** **|** **`--definition-file DEFINITION-FILE`**
Optional

Path to a sandbox definition file.

The sandbox definition file is a blueprint for the sandbox. You can create different definition files for each sandbox type that you use
in the development process. See
<https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_sandbox_definition.htm> for all the options
you can specify in the definition file.

Type: option

**`-s`** **|** **`--set-default`**
Optional

Set the sandbox org as your default org.

Type: boolean

**`-a`** **|** **`--alias ALIAS`**
Optional

Alias for the sandbox org.

When you create a sandbox, the generated usernames are based on the usernames present in the production org. To ensure
uniqueness, the new usernames are appended with the name of the sandbox. For example, the username "user@example.com" in
the production org results in the username "user@example.com.mysandbox" in a sandbox named "mysandbox". When you set an
alias for a sandbox org, it's assigned to the resulting username of the user running this command.


Salesforce CLI Command Reference org Commands

Type: option

**`-w`** **|** **`--wait WAIT`**
Optional

Number of minutes to wait for the sandbox org to be ready.

If the command continues to run after the wait period, the CLI returns control of the terminal to you and displays the "sf org resume
sandbox" command you run to check the status of the create. The displayed command includes the job ID for the running sandbox
creation.

Type: option

Default value: 30 minutes

**`-i`** **|** **`--poll-interval POLL-INTERVAL`**
Optional

Number of seconds to wait between retries.

Type: option

Default value: 30 seconds

```
   --async
```

Optional

Request the sandbox creation, but don't wait for it to complete.

The command immediately displays the job ID and returns control of the terminal to you. This way, you can continue to use the CLI.
To check the status of the sandbox creation, run "sf org resume sandbox".

Type: boolean

**`-n`** **|** **`--name NAME`**
Optional

Name of the sandbox org.

The name must be a unique alphanumeric string (10 or fewer characters) to identify the sandbox. You can’t reuse a name while a
sandbox is in the process of being deleted.

Type: option

```
   --source-sandbox-name SOURCE-SANDBOX-NAME
```

Optional

Name of the sandbox org to clone.

The value of --source-sandbox-name must be an existing sandbox. The existing sandbox, and the new sandbox specified with the
--name flag, must both be associated with the production org (--target-org) that contains the sandbox licenses.

You can specify either --source-sandbox-name or --source-id when cloning an existing sandbox, but not both.

Type: option

```
   --source-id SOURCE-ID
```

Optional

ID of the sandbox org to clone.

The value of --source-id must be an existing sandbox (SandboxInfo.Id). The existing sandbox, and the new sandbox specified with
the --name flag, must both be associated with the production org (--target-org) that contains the sandbox licenses.

You can specify either --source-sandbox-name or --source-id when cloning an existing sandbox, but not both.

Type: option


Salesforce CLI Command Reference org Commands

**`-l`** **|** **`--license-type LICENSE-TYPE`**
Optional

Type of sandbox license.

Type: option

Permissible values are: Developer, Developer_Pro, Partial, Full

**`-o`** **|** **`--target-org TARGET-ORG`**
Required

Username or alias of the production org that contains the sandbox license.

When it creates the sandbox org, Salesforce copies the metadata, and optionally data, from your production org to the new sandbox
org.

Type: option

```
   --no-prompt
```

Optional

Don't prompt for confirmation about the sandbox configuration.

Type: boolean

```
   --no-track-source
```

Optional

Do not use source tracking for this sandbox.

We recommend you enable source tracking in Developer and Developer Pro sandbox, which is why it's the default behavior. Source
tracking allows you to track the changes you make to your metadata, both in your local project and in the sandbox, and to detect
any conflicts between the two.

To disable source tracking in the new sandbox, specify the --no-track-source flag. The main reason to disable source tracking is for
performance. For example, while you probably want to deploy metadata and run Apex tests in your CI/CD jobs, you probably don't
want to incur the costs of source tracking (checking for conflicts, polling the SourceMember object, various file system operations.)
This is a good use case for disabling source tracking in the sandbox.

Type: boolean

Aliases for **`org create sandbox`**

```
   env:create:sandbox

#### **`org create scratch`**

```

Create a scratch org.

#### Description for org create scratch

There are four ways to create a scratch org:

    - Specify a definition file that contains the scratch org options.

    - Use the --edition flag to specify the one required option; this method doesn't require a defintion file.

    - Use the --snapshot flag to create a scratch org from a snapshot. Snapshots are a point-in-time copy of a scratch org; you create a
snapshot with the "sf org create snapshot" command.


Salesforce CLI Command Reference org Commands

    - Use the --source-org flag to create a scratch org from an org shape. Org shapes mimic the baseline setup of a source org without the
extraneous data and metadata; you create an org shape with the "sf org create shape" command.

The --edition, --snapshot, and --source-org flags are mutually exclusive, which means if you specify one, you can't also specify the others.

For any of the methods, you can also use these flags; if you use them with --definition-file, they override their equivalent option in the
scratch org definition file:

    - --description

    - --name (equivalent to the "orgName" option)

    - --username

    - --release

    - --admin-email (equivalent to the "adminEmail" option)

If you want to set options such as org features or settings, you must use a definition file.

You must specify a Dev Hub to create a scratch org, either with the --target-dev-hub flag or by setting your default Dev Hub with the
target-dev-hub configuration variable.

Examples for **`org create scratch`**

Create a Developer edition scratch org using your default Dev Hub and give the scratch org an alias:

```
   sf org create scratch --edition developer --alias my-scratch-org

```

Create a scratch org with a definition file. Specify the Dev Hub using its alias, set the scratch org as your default, and specify that it expires
in 3 days:

```
   sf org create scratch --target-dev-hub MyHub --definition-file

   config/project-scratch-def.json --set-default --duration-days 3

```

Create a preview Enterprise edition scratch org; for use only during Salesforce release transition periods:

```
   sf org create scratch --edition enterprise --alias my-scratch-org --target-dev-hub MyHub

   --release preview

```

Create a scratch org from a snapshot called "NightlyBranch"; be sure you specify the same Dev Hub org associated with the snapshot.
We recommend you increase the --wait time because creating a scratch org from a snapshot can take a while:

```
   sf org create scratch --alias my-scratch-org --target-dev-hub MyHub --snapshot NightlyBranch

    --wait 10

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


Salesforce CLI Command Reference org Commands

**`-a`** **|** **`--alias ALIAS`**
Optional

Alias for the scratch org.

New scratch orgs include one administrator by default. The admin user's username is auto-generated and looks something like
test-wvkpnfm5z113@example.com. When you set an alias for a new scratch org, it's assigned this username.

Type: option

```
   --async
```

Optional

Request the org, but don't wait for it to complete.

The command immediately displays the job ID and returns control of the terminal to you. This way, you can continue to use the CLI.
To resume the scratch org creation, run "sf org resume scratch".

Type: boolean

**`-d`** **|** **`--set-default`**
Optional

Set the scratch org as your default org

Type: boolean

**`-f`** **|** **`--definition-file DEFINITION-FILE`**
Optional

Path to a scratch org definition file.

The scratch org definition file is a blueprint for the scratch org. It mimics the shape of an org that you use in the development life
cycle, such as acceptance testing, packaging, or production. See
<https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_scratch_orgs_def_file.htm> for all the
option you can specify in the definition file.

Type: option

**`-v`** **|** **`--target-dev-hub TARGET-DEV-HUB`**
Required

Username or alias of the Dev Hub org.

Overrides the value of the target-dev-hub configuration variable, if set.

Type: option

**`-c`** **|** **`--no-ancestors`**
Optional

Don't include second-generation managed package (2GP) ancestors in the scratch org.

Type: boolean

**`-e`** **|** **`--edition EDITION`**
Optional

Salesforce edition of the scratch org. Overrides the value of the "edition" option in the definition file, if set.

The editions that begin with "partner-" are available only if the Dev Hub org is a Partner Business Org.

Type: option

Permissible values are: developer, enterprise, group, professional, partner-developer, partner-enterprise, partner-group,
partner-professional


Salesforce CLI Command Reference org Commands

**`-s`** **|** **`--snapshot SNAPSHOT`**
Optional

Name of the snapshot to use when creating this scratch org. Overrides the value of the "snapshot" option in the defintion file, if set.

To view the names of the available snapshots for a given Dev Hub org, run the "sf org list snapshot" command.

Type: option

**`-m`** **|** **`--no-namespace`**
Optional

Create the scratch org with no namespace, even if the Dev Hub has a namespace.

Type: boolean

**`-y`** **|** **`--duration-days DURATION-DAYS`**
Optional

Number of days before the org expires.

Type: option

Default value: 7 days

**`-w`** **|** **`--wait WAIT`**
Optional

Number of minutes to wait for the scratch org to be ready.

If the command continues to run after the wait period, the CLI returns control of the terminal to you and displays the job ID. To
resume the scratch org creation, run the org resume scratch command and pass it the job ID.

Type: option

Default value: 5 minutes

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

**`-i`** **|** **`--client-id CLIENT-ID`**
Optional

Consumer key of the Dev Hub connected app.

Type: option

**`-t`** **|** **`--track-source`**
Optional

Use source tracking for this scratch org. Set --no-track-source to disable source tracking.

We recommend you enable source tracking in scratch orgs, which is why it's the default behavior. Source tracking allows you to
track the changes you make to your metadata, both in your local project and in the scratch org, and to detect any conflicts between
the two.

To disable source tracking in the new scratch org, specify the --no-track-source flag. The main reason to disable source tracking is
for performance. For example, while you probably want to deploy metadata and run Apex tests in your CI/CD jobs, you probably
don't want to incur the costs of source tracking (checking for conflicts, polling the SourceMember object, various file system
operations.) This is a good use case for disabling source tracking in the scratch org.

Type: boolean


Salesforce CLI Command Reference org Commands

Default value: true

```
   --username USERNAME
```

Optional

Username of the scratch org admin user. Overrides the value of the "username" option in the definition file, if set.

The username must be unique within the entire scratch org and sandbox universe. You must add your own logic to ensure uniqueness.

Omit this flag to have Salesforce generate a unique username for your org.

Type: option

```
   --description DESCRIPTION
```

Optional

Description of the scratch org in the Dev Hub. Overrides the value of the "description" option in the definition file, if set.

Type: option

```
   --name NAME
```

Optional

Name of the org, such as "Acme Company". Overrides the value of the "orgName" option in the definition file, if set.

Type: option

```
   --release RELEASE
```

Optional

Release of the scratch org as compared to the Dev Hub release.

By default, scratch orgs are on the same release as the Dev Hub. During Salesforce release transition periods, you can override this
default behavior and opt in or out of the new release.

Type: option

Permissible values are: preview, previous

```
   --admin-email ADMIN-EMAIL
```

Optional

Email address that will be applied to the org's admin user. Overrides the value of the "adminEmail" option in the definition file, if set.

Type: option

```
   --source-org SOURCE-ORG
```

Optional

15-character ID of the org shape that the new scratch org is based on. Overrides the value of the "sourceOrg" option in the definition
file, if set.

To view the names of the available org shapes for a given Dev Hub org, run the "sf org list shape" command.

Type: option

Aliases for **`org create scratch`**

```
   env:create:scratch

#### **`org create shape`**

```

Create a scratch org configuration (shape) based on the specified source org.


Salesforce CLI Command Reference org Commands

Description for **`org create shape`**

Scratch org shapes mimic the baseline setup (features, limits, edition, and Metadata API settings) of a source org without the extraneous
data and metadata.

Run "sf org list shape" to view the available org shapes and their IDs.

To create a scratch org from an org shape, include the "sourceOrg" property in the scratch org definition file and set it to the org ID of
the source org. Then create a scratch org with the "sf org create scratch" command.

Examples for **`org create shape`**

Create an org shape for the source org with alias SourceOrg:

```
   sf org create shape --target-org SourceOrg

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

Aliases for **`org create shape`**

```
   force:org:shape:create

#### **`org create snapshot`**

```

Create a snapshot of a scratch org.

#### Description for org create snapshot

A snapshot is a point-in-time copy of a scratch org. The copy is referenced by its unique name in a scratch org definition file.

Use "sf org get snapshot" to get details, including status, about a snapshot creation request.


Salesforce CLI Command Reference org Commands

To create a scratch org from a snapshot, include the "snapshot" option (instead of "edition") in the scratch org definition file and set it
to the name of the snapshot. Then use "sf org create scratch" to create the scratch org.

Examples for **`org create snapshot`**

Create a snapshot called "Dependencies" using the source scratch org ID and your default Dev Hub org:

```
   sf org create snapshot --source-org 00Dxx0000000000 --name Dependencies --description

   'Contains PackageA v1.1.0'

```

Create a snapshot called "NightlyBranch" using the source scratch org username and a Dev Hub org with alias NightlyDevHub:

```
   sf org create snapshot --source-org myuser@myorg --name NightlyBranch --description 'Contains

    PkgA v2.1.0 and PkgB 3.3.0' --target-dev-hub NightlyDevHub

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

**`-v`** **|** **`--target-dev-hub TARGET-DEV-HUB`**
Required

Username or alias of the Dev Hub org. Not required if the `target-dev-hub` configuration variable is already set.

Type: option

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

**`-o`** **|** **`--source-org SOURCE-ORG`**
Required

ID or locally authenticated username or alias of scratch org to snapshot.

Type: option

**`-n`** **|** **`--name NAME`**
Required

Unique name of snapshot.

Type: option

**`-d`** **|** **`--description DESCRIPTION`**
Optional

Description of snapshot.


Salesforce CLI Command Reference org Commands

Use this description to document the contents of the snapshot. We suggest that you include a reference point, such as a version
control system tag or commit ID.

Type: option

Aliases for **`org create snapshot`**

```
   force:org:snapshot:create

#### **`org create user`**

```

Create a user for a scratch org.

#### Description for org create user

A scratch org includes one administrator user by default. For testing purposes, however, you sometimes need to create additional users.

The easiest way to create a user is to let this command assign default or generated characteristics to the new user. If you want to customize
your new user, create a definition file and specify it with the --definition-file flag. In the file, you can include all the User sObject (Salesforce
object) fields and Salesforce DX-specific options, as described in "User Definition File for Customizing a Scratch Org User"
(https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_scratch_orgs_users_def_file.htm). You can also
specify these options on the command line.

If you don't customize your new user, this command creates a user with the following default characteristics:

    - The username is the existing administrator’s username prepended with a timestamp, such as
1505759162830_test-wvkpnfm5z113@example.com.

    - The user’s profile is Standard User.

    - The values of the required fields of the User sObject are the corresponding values of the administrator user.

    - The user has no password.

Use the --set-alias flag to assign a simple name to the user that you can reference in later CLI commands. This alias is local and different
from the Alias field of the User sObject record of the new user, which you set in the Setup UI.

When this command completes, it displays the new username and user ID. Run the "org display user" command to get more information
about the new user.

After the new user has been created, Salesforce CLI automatically authenticates it to the scratch org so the new user can immediately
start using the scratch org. The CLI uses the same authentication method that was used on the associated Dev Hub org. Due to Hyperforce
limitations, the scratch org user creation fails if the Dev Hub authentication used the JWT flow and the scratch org is on Hyperforce. For
this reason, if you plan to create scratch org users, authenticate to the Dev Hub org with either the "org login web" or "org login sfdx-url"
command, and not "org login jwt".

For more information about user limits, defaults, and other considerations when creating a new scratch org user, see
https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_scratch_orgs_users.htm.

#### Examples for org create user

Create a user for your default scratch org and let this command generate a username, user ID, and other characteristics:

```
   sf org create user

```


Salesforce CLI Command Reference org Commands

Create a user with alias "testuser1" using a user definition file. Set the "profileName" option to "Chatter Free User", which overrides the
value in the defintion file if it also exists there. Create the user for the scratch org with alias "my-scratch":

```
   sf org create user --set-alias testuser1 --definition-file config/project-user-def.json

   profileName='Chatter Free User' --target-org my-scratch

```

Create a user by specifying the username, email, and perm set assignment at the command line; command fails if the username already
exists in Salesforce:

```
   sf org create user username=testuser1@my.org email=me@my.org permsets=DreamHouse

```

Create a user with a definition file, set the email value as specified (overriding any value in the definition file), and generate a password
for the user. If the username in the definition file isn't unique, the command appends the org ID to make it unique:

```
   sf org create user --definition-file config/project-user-def.json email=me@my.org

   generatepassword=true --set-unique-username

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

**`-a`** **|** **`--set-alias SET-ALIAS`**
Optional

Set an alias for the created username to reference in other CLI commands.

Type: option

**`-f`** **|** **`--definition-file DEFINITION-FILE`**
Optional

File path to a user definition file for customizing the new user.

The user definition file uses JSON format and can include any Salesforce User sObject field and Salesforce DX-specific options. See
https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_scratch_orgs_users_def_file.htm for more
information.

Type: option

**`-s`** **|** **`--set-unique-username`**
Optional

Force the username, if specified in the definition file or at the command line, to be unique by appending the org ID.

The new user’s username must be unique across all Salesforce orgs and in the form of an email address. If you let this command
generate a username for you, it's guaranteed to be unique. If you specify an existing username in a definition file, the command fails.
Set this flag to force the username to be unique; as a result, the username might be different than what you specify in the definition
file.

Type: boolean


Salesforce CLI Command Reference org Commands

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

Aliases for **`org create user`**

```
   force:user:create

#### **`org delete sandbox`**

```

Delete a sandbox.

#### Description for org delete sandbox

Salesforce CLI marks the org for deletion in the production org that contains the sandbox licenses and then deletes all local references
to the org from your computer.

Specify a sandbox with either the username you used when you logged into it, or the alias you gave the sandbox when you created it.
Run "sf org list" to view all your orgs, including sandboxes, and their aliases.

Both the sandbox and the associated production org must already be authenticated with the CLI to successfully delete the sandbox.

#### Examples for org delete sandbox

Delete a sandbox with alias my-sandbox:

```
   sf org delete sandbox --target-org my-sandbox

```

Specify a username instead of an alias:

```
   sf org delete sandbox --target-org myusername@example.com.qa

```

Delete the sandbox without prompting to confirm:

```
   sf org delete sandbox --target-org my-sandbox --no-prompt

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


Salesforce CLI Command Reference org Commands

Import flag values from a directory.

Type: option

**`-o`** **|** **`--target-org TARGET-ORG`**
Required

Username or alias of the target org. Not required if the `target-org` configuration variable is already set.

Type: option

**`-p`** **|** **`--no-prompt`**
Optional

Don't prompt the user to confirm the deletion.

Type: boolean

Aliases for **`org delete sandbox`**

```
   env:delete:sandbox

#### **`org delete scratch`**

```

Delete a scratch org.

#### Description for org delete scratch

Salesforce CLI marks the org for deletion in the Dev Hub org and then deletes all local references to the org from your computer.

Specify a scratch org with either the username or the alias you gave the scratch org when you created it. Run "sf org list" to view all your
orgs, including scratch orgs, and their aliases.

#### Examples for org delete scratch

Delete a scratch org with alias my-scratch-org:

```
   sf org delete scratch --target-org my-scratch-org

```

Specify a username instead of an alias:

```
   sf org delete scratch --target-org test-123456-abcdefg@example.com

```

Delete the scratch org without prompting to confirm :

```
   sf org delete scratch --target-org my-scratch-org --no-prompt

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


Salesforce CLI Command Reference org Commands

Import flag values from a directory.

Type: option

**`-o`** **|** **`--target-org TARGET-ORG`**
Required

Username or alias of the target org. Not required if the `target-org` configuration variable is already set.

Type: option

**`-p`** **|** **`--no-prompt`**
Optional

Don't prompt the user to confirm the deletion.

Type: boolean

Aliases for **`org delete scratch`**

```
   env:delete:scratch

#### **`org delete shape`**

```

Delete all org shapes for a target org.

#### Description for org delete shape

A source org can have only one active org shape. If you try to create an org shape for a source org that already has one, the previous
shape is marked inactive and replaced by a new active shape. If you don’t want to create scratch orgs based on this shape, you can delete
the org shape.

#### Examples for org delete shape

Delete all org shapes for the source org with alias SourceOrg:

```
   sf org delete shape --target-org SourceOrg

```

Delete all org shapes without prompting:

```
   sf org delete shape --target-org SourceOrg --no-prompt

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


Salesforce CLI Command Reference org Commands

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

**`-p`** **|** **`--no-prompt`**
Optional

Don't prompt for confirmation.

Type: boolean

Aliases for **`org delete shape`**

```
   force:org:shape:delete

#### **`org delete snapshot`**

```

Delete a scratch org snapshot.

#### Description for org delete snapshot

Dev Hub admins can delete any snapshot. Users can delete only their own snapshots, unless a Dev Hub admin gives the user Modify All
permission, which works only with the Salesforce license.

#### Examples for org delete snapshot

Delete a snapshot from the default Dev Hub using the snapshot ID:

```
   sf org delete snapshot --snapshot 0Oo...

```

Delete a snapshot from the specified Dev Hub using the snapshot name:

```
   sf org delete snapshot --snapshot BaseSnapshot --target-dev-hub SnapshotDevHub

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


Salesforce CLI Command Reference org Commands

Type: option

**`-v`** **|** **`--target-dev-hub TARGET-DEV-HUB`**
Required

Username or alias of the Dev Hub org. Not required if the `target-dev-hub` configuration variable is already set.

Type: option

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

**`-s`** **|** **`--snapshot SNAPSHOT`**
Required

Name or ID of snapshot to delete.

The IDs of scratch org snapshots start with 0Oo.

Type: option

**`-p`** **|** **`--no-prompt`**
Optional

Don't prompt the user to confirm the deletion.

Type: boolean

Aliases for **`org delete snapshot`**

```
   force:org:snapshot:delete

#### **`org disable tracking`**

```

Prevent Salesforce CLI from tracking changes in your source files between your project and an org.

#### Description for org disable tracking

Disabling source tracking has no direct effect on the org, it affects only your local environment. Specifically, Salesforce CLI stores the
setting in the org's local configuration file so that no source tracking operations are executed when working with the org.

#### Examples for org disable tracking

Disable source tracking for an org with alias "myscratch":

```
   sf org disable tracking --target-org myscratch

```

Disable source tracking for an org using a username:

```
   sf org disable tracking --target-org you@example.com

```

Disable source tracking for your default org:

```
   sf org disable tracking

```


Salesforce CLI Command Reference org Commands

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

#### **`org display`**

Display information about an org.

#### Description for org display

Output includes your access token, client Id, connected status, org ID, instance URL, username, and alias, if applicable.

Use --verbose to include the SFDX auth URL. WARNING: The SFDX auth URL contains sensitive information, such as a refresh token that
can be used to access an org. Don't share or distribute this URL or token.

Including --verbose displays the sfdxAuthUrl property only if you authenticated to the org using "org login web" (not "org login jwt").

#### Examples for org display

Display information about your default org:

```
   $ sf org display

```

Display information, including the sfdxAuthUrl property, about the org with alias TestOrg1:

```
   $ sf org display --target-org TestOrg1 --verbose

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


Salesforce CLI Command Reference org Commands

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

```
   --verbose
```

Optional

Display the sfdxAuthUrl property.

Type: boolean

#### Aliases for org display

```
   force:org:display

#### **`org display user`**

```

Display information about a Salesforce user.

#### Description for org display user

Output includes the profile name, org ID, instance URL, login URL, and alias if applicable. The displayed alias is local and different from
the Alias field of the User sObject record of the new user, which you set in the Setup UI.

#### Examples for org display user

Display information about the admin user of your default scratch org:

```
   sf org display user

```

Display information about the specified user and output in JSON format:

```
   sf org display user --target-org me@my.org --json

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


Salesforce CLI Command Reference org Commands

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

Aliases for **`org display user`**

```
   force:user:display

#### **`org enable tracking`**

```

Allow Salesforce CLI to track changes in your source files between your project and an org.

#### Description for org enable tracking

Enabling source tracking has no direct effect on the org, it affects only your local environment. Specifically, Salesforce CLI stores the
setting in the org's local configuration file so that source tracking operations are executed when working with the org.

This command throws an error if the org doesn't support tracking. Examples of orgs that don't support source tracking include Developer
Edition orgs, production orgs, Partial Copy sandboxes, and Full sandboxes.

#### Examples for org enable tracking

Enable source tracking for an org with alias "myscratch":

```
   sf org enable tracking --target-org myscratch

```

Enable source tracking for an org using a username:

```
   sf org enable tracking --target-org you@example.com

```

Enable source tracking for your default org:

```
   sf org enable tracking

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


Salesforce CLI Command Reference org Commands

Import flag values from a directory.

Type: option

**`-o`** **|** **`--target-org TARGET-ORG`**
Required

Username or alias of the target org. Not required if the `target-org` configuration variable is already set.

Type: option

#### **`org generate password`**

Generate a random password for scratch org users.

#### Description for org generate password

By default, new scratch orgs contain one admin user with no password. Use this command to generate or change a password for this
admin user. After it's set, you can’t unset a password, you can only change it.

You can also use the --on-behalf-of flag to generate a password for a scratch org user that you've created locally with the "org create
user" command. This command doesn't work for users you created in the scratch org using Setup.

To change the password strength, set the --complexity flag to a value between 0 and 5. Each value specifies the types of characters used
in the generated password:

0 - lower case letters only

1 - lower case letters and numbers only

2 - lower case letters and symbols only

3 - lower and upper case letters and numbers only

4 - lower and upper case letters and symbols only

5 - lower and upper case letters and numbers and symbols only

To see a password that was previously generated, run "org auth show-user-password".

#### Examples for org generate password

Generate a password for the original admin user of your default scratch org:

```
   sf org generate password

```

Generate a password that contains 25 characters for the original admin user of the scratch org with alias "my-scratch":

```
   sf org generate password --length 25 --target-org my-scratch

```

Generate a password for your default scratch org admin user that uses lower and upper case letters and numbers only:

```
   sf org generate password --complexity 3

```

Generate a password for the specified users in the default scratch org; these users must have been created locally with the "org create
user" command:

```
   sf org generate password --on-behalf-of user1@my.org --on-behalf-of user2@my.org

   --on-behalf-of user3@my.org

```


Salesforce CLI Command Reference org Commands

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

**`-b`** **|** **`--on-behalf-of ON-BEHALF-OF`**
Optional

Comma-separated list of usernames or aliases to assign the password to; must have been created locally with the "org create user"
command.

Type: option

**`-l`** **|** **`--length LENGTH`**
Optional

Number of characters in the generated password; valid values are between 20 and 100. Default value is 20.

Type: option

Default value: 20

**`-c`** **|** **`--complexity COMPLEXITY`**
Optional

Level of password complexity or strength; the higher the value, the stronger the password.

Type: option

Default value: 5

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

#### **`org get snapshot`**

Get details about a scratch org snapshot.

#### Description for org get snapshot

Snapshot creation can take a while. Use this command with the snapshot name or ID to check its creation status. After the status changes
to Active, you can use the snapshot to create scratch orgs.


Salesforce CLI Command Reference org Commands

To create a snapshot, use the "sf org create snapshot" command. To retrieve a list of all snapshots, use "sf org list snapshot".

Examples for **`org get snapshot`**

Get snapshot details using its ID and the default Dev Hub org:

```
   sf org get snapshot --snapshot 0Oo...

```

Get snapshot details using its name from a Dev Hub org with alias SnapshotDevHub:

```
   sf org get snapshot --snapshot Dependencies --target-dev-hub SnapshotDevHub

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

**`-v`** **|** **`--target-dev-hub TARGET-DEV-HUB`**
Required

Username or alias of the Dev Hub org. Not required if the `target-dev-hub` configuration variable is already set.

Type: option

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

**`-s`** **|** **`--snapshot SNAPSHOT`**
Required

Name or ID of snapshot to retrieve.

The IDs of scratch org snapshots start with 0Oo.

Type: option

Aliases for **`org get snapshot`**

```
   force:org:snapshot:get

#### **`org list`**

```

List all orgs you’ve created or authenticated to.


Salesforce CLI Command Reference org Commands

Examples for **`org list`**

List all orgs you've created or authenticated to:

```
   $ sf org list

```

List all orgs, including expired, deleted, and unknown-status orgs; don't include the connection status:

```
   $ sf org list --skip-connection-status --all

```

List orgs and remove local org authorization info about non-active scratch orgs:

```
   $ sf org list --clean

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
   --verbose
```

Optional

List more information about each org.

Type: boolean

```
   --all
```

Optional

Include expired, deleted, and unknown-status scratch orgs.

Type: boolean

```
   --clean
```

Optional

Remove all local org authorizations for non-active scratch orgs. Use "org logout" to remove non-scratch orgs.

Type: boolean

**`-p`** **|** **`--no-prompt`**
Optional

Don't prompt for confirmation.

Type: boolean

```
   --skip-connection-status
```

Optional

Skip retrieving the connection status of non-scratch orgs.

Type: boolean


Salesforce CLI Command Reference org Commands

#### Aliases for org list

```
   force:org:list

#### **`org list auth`**

```

List authorization information about the orgs you created or logged into.

#### Description for org list auth

This command uses local authorization information that Salesforce CLI caches when you create a scratch org or log into an org. The
command doesn't actually connect to the orgs to verify that they're still active. As a result, this command executes very quickly. If you
want to view live information about your authorized orgs, such as their connection status, use the "org list" command.

#### Examples for org list auth

List local authorization information about your orgs:

```
   sf org list auth

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

#### Aliases for org list auth

```
   force:auth:list

   auth:list

#### **`org list limits`**

```

Display information about limits in your org.

#### Description for org list limits

For each limit, this command returns the maximum allocation and the remaining allocation based on usage. See this topic for a description
of each limit: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_limits.htm.


Salesforce CLI Command Reference org Commands

Examples for **`org list limits`**

Display limits in your default org:

```
   sf org list limits

```

Display limits in the org with alias "my-scratch-org":

```
   sf org list limits --target-org my-scratch-org

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

Aliases for **`org list limits`**

```
   force:limits:api:display

   limits:api:display

#### **`org list metadata`**

```

List the metadata components and properties of a specified type.

#### Description for org list metadata

Use this command to identify individual components in your manifest file or if you want a high-level view of particular metadata types
in your org. For example, you can use this command to return a list of names of all the CustomObject or Layout components in your
org, then use this information in a retrieve command that returns a subset of these components.

The username that you use to connect to the org must have the Modify All Data or Modify Metadata Through Metadata API Functions
permission.


Salesforce CLI Command Reference org Commands

Examples for **`org list metadata`**

List the CustomObject components, and their properties, in the org with alias "my-dev-org":

```
   $ sf org list metadata --metadata-type CustomObject --target-org my-dev-org

```

List the CustomObject components in your default org, write the output to the specified file, and use API version 57.0:

```
   $ sf org list metadata --metadata-type CustomObject --api-version 57.0 --output-file

   /path/to/outputfilename.txt

```

List the Dashboard components in your default org that are contained in the "folderSales" folder, write the output to the specified file,
and use API version 57.0:

```
   $ sf org list metadata --metadata-type Dashboard --folder folderSales --api-version 57.0

   --output-file /path/to/outputfilename.txt

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
   --api-version API-VERSION
```

Optional

API version to use; default is the most recent API version.

Override the api version used for api requests made by this command

Type: option

**`-o`** **|** **`--target-org TARGET-ORG`**
Required

Username or alias of the target org. Not required if the `target-org` configuration variable is already set.

Type: option

**`-f`** **|** **`--output-file OUTPUT-FILE`**
Optional

Pathname of the file in which to write the results.

Type: option

**`-m`** **|** **`--metadata-type METADATA-TYPE`**
Required

Metadata type to be retrieved, such as CustomObject; metadata type names are case-sensitive.

Type: option


Salesforce CLI Command Reference org Commands

```
   --folder FOLDER
```

Optional

Folder associated with the component; required for components that use folders; folder names are case-sensitive.

Examples of metadata types that use folders are Dashboard, Document, EmailTemplate, and Report.

Type: option

#### Aliases for org list metadata

```
   force:mdapi:listmetadata

#### **`org list metadata-types`**

```

Display details about the metadata types that are enabled for your org.

#### Description for org list metadata-types

The information includes Apex classes and triggers, custom objects, custom fields on standard objects, tab sets that define an app, and
many other metadata types. Use this information to identify the syntax needed for a <name> element in a manifest file (package.xml).

The username that you use to connect to the org must have the Modify All Data or Modify Metadata Through Metadata API Functions
permission.

#### Examples for org list metadata-types

Display information about all known and enabled metadata types in the org with alias "my-dev-org" using API version 57.0:

```
   $ sf org list metadata-types --api-version 57.0 --target-org my-dev-org

```

Display only the metadata types that aren't yet supported by Salesforce CLI in your default org and write the results to the specified file:

```
   $ sf org list metadata-types --output-file /path/to/outputfilename.txt --filter-known

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
   --api-version API-VERSION
```

Optional

API version to use; default is the most recent API version.

Override the api version used for api requests made by this command


Salesforce CLI Command Reference org Commands

Type: option

**`-o`** **|** **`--target-org TARGET-ORG`**
Required

Username or alias of the target org. Not required if the `target-org` configuration variable is already set.

Type: option

**`-f`** **|** **`--output-file OUTPUT-FILE`**
Optional

Pathname of the file in which to write the results.

Directing the output to a file makes it easier to extract relevant information for your package.xml manifest file. The default output
destination is the terminal or command window console.

Type: option

Aliases for **`org list metadata-types`**

```
   force:mdapi:describemetadata

#### **`org list shape`**

```

List all org shapes you’ve created.

#### Description for org list shape

The output includes the alias, username, and ID of the source org, the status of the org shape creation, and more. Use the org ID to
update your scratch org configuration file so you can create a scratch org based on this org shape.

#### Examples for org list shape

List all org shapes you've created:

```
   sf org list shape

```

List all org shapes in JSON format and write the output to a file:

```
   sf org list shape --json > tmp/MyOrgShapeList.json

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


Salesforce CLI Command Reference org Commands

Aliases for **`org list shape`**

```
   force:org:shape:list

#### **`org list snapshot`**

```

List scratch org snapshots.

#### Description for org list snapshot

You can view all the snapshots in a Dev Hub that you have access to. If you’re an admin, you can see all snapshots associated with the
Dev Hub org. If you’re a user, you can see only your snapshots unless a Dev Hub admin gives you View All permissions.

To create a snapshot, use the "sf org create snapshot" command. To get details about a snapshot request, use "sf org get snapshot".

#### Examples for org list snapshot

List snapshots in the default Dev Hub:

```
   sf org list snapshot

```

List snapshots in the Dev Hub with alias SnapshotDevHub:

```
   sf org list snapshot --target-dev-hub SnapshotDevHub

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

**`-v`** **|** **`--target-dev-hub TARGET-DEV-HUB`**
Required

Username or alias of the Dev Hub org. Not required if the `target-dev-hub` configuration variable is already set.

Type: option

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

#### Aliases for org list snapshot

```
   force:org:snapshot:list

```


Salesforce CLI Command Reference org Commands

#### **`org list sobject record-counts`**

Display record counts for the specified standard or custom objects.

#### Description for org list sobject record-counts

Use this command to get an approximate count of the records in standard or custom objects in your org. These record counts are the
same as the counts listed in the Storage Usage page in the Setup UI. The record counts are approximate because they're calculated
asynchronously and your org's storage usage isn't updated immediately. To display all available record counts, run the command without
the --sobject flag.

#### Examples for org list sobject record-counts

Display all available record counts in your default org:

```
   sf org list sobject record-counts

```

Display record counts for the Account, Contact, Lead, and Opportunity objects in your default org:

```
   sf org list sobject record-counts --sobject Account --sobject Contact --sobject Lead

   --sobject Opportunity

```

Display record counts for the Account and Lead objects for the org with alias "my-scratch-org":

```
   sf org list sobject record-counts --sobject Account --sobject Lead --target-org

   my-scratch-org

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

**`-s`** **|** **`--sobject SOBJECT`**
Optional

API name of the standard or custom object for which to display record counts.

Type: option

**`-o`** **|** **`--target-org TARGET-ORG`**
Required

Username or alias of the target org. Not required if the `target-org` configuration variable is already set.

Type: option

```
   --api-version API-VERSION
```

Optional


Salesforce CLI Command Reference org Commands

Override the api version used for api requests made by this command

Type: option

Aliases for **`org list sobject record-counts`**

```
   force:limits:recordcounts:display

   limits:recordcounts:display

#### **`org list users`**

```

List all locally-authenticated users of an org.

#### Description for org list users

For scratch orgs, the list includes any users you've created with the "org create user" command; the original scratch org admin user is
marked with "(A)". For other orgs, the list includes the users you used to authenticate to the org.

#### Examples for org list users

List the locally-authenticated users of your default org:

```
   sf org list users

```

List the locally-authenticated users of the specified org:

```
   sf org list users --target-org me@my.org

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


Salesforce CLI Command Reference org Commands

Aliases for **`org list users`**

```
   force:user:list

#### **`org login access-token`**

```

Authorize an org using an existing Salesforce access token.

#### Description for org login access-token

By default, the command runs interactively and asks you for the access token. If you previously authorized the org, the command prompts
whether you want to overwrite the local file. Specify --no-prompt to not be prompted.

To use the command in a CI/CD script, set the SF_ACCESS_TOKEN environment variable to the access token. Then run the command
with the --no-prompt parameter.

#### Examples for org login access-token

Authorize an org on https://mycompany.my.salesforce.com; the command prompts you for the access token:

```
   sf org login access-token --instance-url https://mycompany.my.salesforce.com

```

Authorize the org without being prompted; you must have previously set the SF_ACCESS_TOKEN environment variable to the access
token:

```
   sf org login access-token --instance-url https://dev-hub.my.salesforce.com --no-prompt

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

**`-r`** **|** **`--instance-url INSTANCE-URL`**
Required

URL of the instance that the org lives on.

If you specify an --instance-url value, this value overrides the sfdcLoginUrl value in your sfdx-project.json file.

To specify a My Domain URL, use the format "https://<MyDomainName>.my.salesforce.com".

To specify a sandbox, set --instance-url to "https://<MyDomainName>--<SandboxName>.sandbox.my.salesforce.com".

Type: option

**`-d`** **|** **`--set-default-dev-hub`**
Optional

Set the authenticated org as the default Dev Hub.


Salesforce CLI Command Reference org Commands

Type: boolean

**`-s`** **|** **`--set-default`**
Optional

Set the authenticated org as the default that all org-related commands run against.

Type: boolean

**`-a`** **|** **`--alias ALIAS`**
Optional

Alias for the org.

Type: option

**`-p`** **|** **`--no-prompt`**
Optional

Don't prompt for confirmation.

Type: boolean

Aliases for **`org login access-token`**

```
   force:auth:accesstoken:store

   auth:accesstoken:store

#### **`org login jwt`**

```

Log in to a Salesforce org using a JSON web token (JWT).

#### Description for org login jwt

Use this command in automated environments where you can’t interactively log in with a browser, such as in CI/CD scripts.

Logging into an org authorizes the CLI to run other commands that connect to that org, such as deploying or retrieving a project. You
can log into many types of orgs, such as sandboxes, Dev Hubs, Env Hubs, production orgs, and scratch orgs.

Complete these steps before you run this command:

1. Create a digital certificate (also called digital signature) and the private key to sign the certificate. You can use your own key and
certificate issued by a certification authority. Or use OpenSSL to create a key and a self-signed digital certificate.

2. Store the private key in a file on your computer. When you run this command, you set the --jwt-key-file flag to this file.

3. Create a custom connected app in your org using the digital certificate. Make note of the consumer key (also called client id) that’s
generated for you. Be sure the username of the user logging in is approved to use the connected app. When you run this command,
you set the --client-id flag to the consumer key.

See https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_auth_jwt_flow.htm for more information.

We recommend that you set an alias when you log into an org. Aliases make it easy to later reference this org when running commands
that require it. If you don’t set an alias, you use the username that you specified when you logged in to the org. If you run multiple
commands that reference the same org, consider setting the org as your default. Use --set-default for your default scratch org or sandbox,
or --set-default-dev-hub for your default Dev Hub.


Salesforce CLI Command Reference org Commands

Examples for **`org login jwt`**

Log into an org with username jdoe@example.org and on the default instance URL (https://login.salesforce.com). The private key is
stored in the file /Users/jdoe/JWT/server.key and the command uses the connected app with consumer key (client id) 04580y4051234051.

```
   sf org login jwt --username jdoe@example.org --jwt-key-file /Users/jdoe/JWT/server.key

   --client-id 04580y4051234051

```

Set the org as the default and give it an alias:

```
   sf org login jwt --username jdoe@example.org --jwt-key-file /Users/jdoe/JWT/server.key

   --client-id 04580y4051234051 --alias ci-org --set-default

```

Set the org as the default Dev Hub and give it an alias:

```
   sf org login jwt --username jdoe@example.org --jwt-key-file /Users/jdoe/JWT/server.key

   --client-id 04580y4051234051 --alias ci-dev-hub --set-default-dev-hub

```

Log in to a sandbox using URL https://MyDomainName--SandboxName.sandbox.my.salesforce.com:

```
   sf org login jwt --username jdoe@example.org --jwt-key-file /Users/jdoe/JWT/server.key

   --client-id 04580y4051234051 --alias ci-org --set-default --instance-url

   https://MyDomainName--SandboxName.sandbox.my.salesforce.com

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

**`-o`** **|** **`--username USERNAME`**
Required

Username of the user logging in.

Type: option

**`-f`** **|** **`--jwt-key-file JWT-KEY-FILE`**
Required

Path to a file containing the private key.

Type: option

**`-i`** **|** **`--client-id CLIENT-ID`**
Required

OAuth client ID (also called consumer key) of your custom connected app.

Type: option

**`-r`** **|** **`--instance-url INSTANCE-URL`**
Optional


Salesforce CLI Command Reference org Commands

URL of the instance that the org lives on.

If you specify an --instance-url value, this value overrides the sfdcLoginUrl value in your sfdx-project.json file.

To specify a My Domain URL, use the format "https://<MyDomainName>.my.salesforce.com".

To specify a sandbox, set --instance-url to "https://<MyDomainName>--<SandboxName>.sandbox.my.salesforce.com".

Type: option

**`-d`** **|** **`--set-default-dev-hub`**
Optional

Set the authenticated org as the default Dev Hub.

Type: boolean

**`-s`** **|** **`--set-default`**
Optional

Set the authenticated org as the default that all org-related commands run against.

Type: boolean

**`-a`** **|** **`--alias ALIAS`**
Optional

Alias for the org.

Type: option

Aliases for **`org login jwt`**

```
   force:auth:jwt:grant

   auth:jwt:grant

#### **`org login sfdx-url`**

```

Authorize an org using a Salesforce DX authorization URL stored in a file or through standard input (stdin).

#### Description for org login sfdx-url

You use the Salesforce DX (SFDX) authorization URL to authorize Salesforce CLI to connect to a target org. The URL contains the required
data to accomplish the authorization, such as the client ID, client secret, and instance URL. You must specify the SFDX authorization URL
in this format: "force://<clientId>:<clientSecret>:<refreshToken>@<instanceUrl>". Replace <clientId>, <clientSecret>, <refreshToken>,
and <instanceUrl> with the values specific to your target org. For <instanceUrl>, don't include a protocol (such as "https://"). Note that
although the SFDX authorization URL starts with "force://", it has nothing to do with the actual authorization. Salesforce CLI always
communicates with your org using HTTPS.

To see the SFDX authorization URL for an org, run "org auth show-sfdx-auth-url".

You have three options when creating the authorization file. The easiest option is to redirect the output of the "sf org auth
show-sfdx-auth-url --json" command into a file. For example, using an org with alias my-org that you've already authorized:

```
      $ sf org auth show-sfdx-auth-url --target-org my-org --json > authFile.json

```


Salesforce CLI Command Reference org Commands

The resulting JSON file contains the URL in the "sfdxAuthUrl" property of the "result" object. You can then reference the file when running
this command:

```
      $ sf org login sfdx-url --sfdx-url-file authFile.json

```

NOTE: The SFDX auth URL is only available for orgs authorized with a web-based OAuth flow, and not the JWT bearer flow.

You can also create a JSON file that has a top-level property named sfdxAuthUrl whose value is the authorization URL. Finally, you can
create a normal text file that includes just the URL and nothing else.

Alternatively, you can pipe the SFDX authorization URL through standard input by specifying the --sfdx-url-stdin flag.

Examples for **`org login sfdx-url`**

Authorize an org using the SFDX authorization URL in the files/authFile.json file:

```
   sf org login sfdx-url --sfdx-url-file files/authFile.json

```

Similar to previous example, but set the org as your default and give it an alias MyDefaultOrg:

```
   sf org login sfdx-url --sfdx-url-file files/authFile.json --set-default --alias MyDefaultOrg

```

Pipe the SFDX authorization URL from stdin:

```
   $ echo url | sf org login sfdx-url --sfdx-url-stdin

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

**`-f`** **|** **`--sfdx-url-file SFDX-URL-FILE`**
Optional

Path to a file that contains the Salesforce DX authorization URL.

Type: option

**`-u`** **|** **`--sfdx-url-stdin SFDX-URL-STDIN`**
Optional

Pipe the Salesforce DX authorization URL through standard input (stdin).

Type: option

**`-d`** **|** **`--set-default-dev-hub`**
Optional

Set the authenticated org as the default Dev Hub.

Type: boolean


Salesforce CLI Command Reference org Commands

**`-s`** **|** **`--set-default`**
Optional

Set the authenticated org as the default that all org-related commands run against.

Type: boolean

**`-a`** **|** **`--alias ALIAS`**
Optional

Alias for the org.

Type: option

Aliases for **`org login sfdx-url`**

```
   force:auth:sfdxurl:store

   auth:sfdxurl:store

#### **`org login web`**

```

Log in to a Salesforce org using the web server flow.

#### Description for org login web

Opens a Salesforce instance URL in a web browser so you can enter your credentials and log in to your org. After you log in, you can
close the browser window.

Logging into an org authorizes the CLI to run other commands that connect to that org, such as deploying or retrieving metadata. You
can log into many types of orgs, such as sandboxes, Dev Hubs, Env Hubs, production orgs, and scratch orgs.

We recommend that you set an alias when you log into an org. Aliases make it easy to later reference this org when running commands
that require it. If you don’t set an alias, you use the username that you specified when you logged in to the org. If you run multiple
commands that reference the same org, consider setting the org as your default. Use --set-default for your default scratch org or sandbox,
or --set-default-dev-hub for your default Dev Hub.

By default, this command uses the global out-of-the-box connected app in your org. If you need more security or control, such as setting
the refresh token timeout or specifying IP ranges, create your own connected app using a digital certificate. Make note of the consumer
key (also called cliend id) that’s generated for you. Then specify the consumer key with the --client-id flag.

You can also use this command to link one or more connected or external client apps in an org to an already-authenticated user. Then
Salesforce CLI commands that have API-specific requirements, such as new OAuth scopes or JWT-based access tokens, can use these
custom client apps rather than the default one. To create the link, you use the --client-app flag to give the link a name and the --username
flag to specify the already-authenticated user. Use the --scopes flag to add OAuth scopes if required. After you create the link, you then
use the --client-app value in the other command that has the API-specific requirements. An example of a command that uses this feature
is "agent preview"; see the "Preview an Agent" section in the "Agentforce Developer Guide" for details and examples.
(https://developer.salesforce.com/docs/einstein/genai/guide/agent-dx-preview.html)

#### Examples for org login web

Run the command with no flags to open the default Salesforce login page (https://login.salesforce.com):

```
   sf org login web

```


Salesforce CLI Command Reference org Commands

Log in to your Dev Hub, set it as your default Dev Hub, and set an alias that you reference later when you create a scratch org:

```
   sf org login web --set-default-dev-hub --alias dev-hub

```

Log in to a sandbox and set it as your default org:

```
   sf org login web --instance-url https://MyDomainName--SandboxName.sandbox.my.salesforce.com

    --set-default

```

Use --browser to specify a specific browser, such as Google Chrome:

```
   sf org login web --instance-url https://MyDomainName--SandboxName.sandbox.my.salesforce.com

    --set-default --browser chrome

```

Use your own connected app by specifying its consumer key (also called client ID) and specify additional OAuth scopes:

```
   sf org login web --instance-url https://MyDomainName--SandboxName.sandbox.my.salesforce.com

    --set-default --browser chrome --client-id 04580y4051234051 --scopes "sfap_api chatbot_api"

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

**`-b`** **|** **`--browser BROWSER`**
Optional

Browser in which to open the org.

If you don’t specify --browser, the command uses your default browser. The exact names of the browser applications differ depending
on the operating system you're on; check your documentation for details.

Type: option

Permissible values are: chrome, edge, firefox

**`-i`** **|** **`--client-id CLIENT-ID`**
Optional

OAuth client ID (also called consumer key) of your custom connected app.

Type: option

**`-r`** **|** **`--instance-url INSTANCE-URL`**
Optional

URL of the instance that the org lives on.

If you specify an --instance-url value, this value overrides the sfdcLoginUrl value in your sfdx-project.json file.

To specify a My Domain URL, use the format "https://<MyDomainName>.my.salesforce.com".

To specify a sandbox, set --instance-url to "https://<MyDomainName>--<SandboxName>.sandbox.my.salesforce.com".


Salesforce CLI Command Reference org Commands

Type: option

**`-d`** **|** **`--set-default-dev-hub`**
Optional

Set the authenticated org as the default Dev Hub.

Type: boolean

**`-s`** **|** **`--set-default`**
Optional

Set the authenticated org as the default that all org-related commands run against.

Type: boolean

**`-a`** **|** **`--alias ALIAS`**
Optional

Alias for the org.

Type: option

**`-c`** **|** **`--client-app CLIENT-APP`**
Optional

Name to give to the link between the connected app or external client and the already-authenticated user. You can specify any
string you want. Must be used with --username.

Type: option

```
   --username USERNAME
```

Optional

Username of the already-authenticated user to link to the connected app or external client app. Must be used with --client-app.

Type: option

```
   --scopes SCOPES
```

Optional

Authentication (OAuth) scopes to request. Use the scope's short name; specify multiple scopes using just one flag instance and
separated by spaces: --scopes "sfap_api chatbot_api".

Type: option

Aliases for **`org login web`**

```
   force:auth:web:login

   auth:web:login

#### **`org logout`**

```

Log out of a Salesforce org.

#### Description for org logout

If you run this command with no flags and no default org set in your config or environment, it first displays a list of orgs you've created
or logged into, with none of the orgs selected. Use the arrow keys to scroll through the list and the space bar to select the orgs you want
to log out of. Press Enter when you're done; the command asks for a final confirmation before logging out of the selected orgs.


Salesforce CLI Command Reference org Commands

The process is similar if you specify --all, except that in the initial list of orgs, they're all selected. Use --target-org to logout of a specific
org. In both these cases by default, you must still confirm that you want to log out. Use --no-prompt to never be asked for confirmation
when also using --all or --target-org.

Be careful! If you log out of a scratch org without having access to its password, you can't access the scratch org again, either through
the CLI or the Salesforce UI.

Use the --client-app flag to log out of the link you previously created between an authenticated user and a connected app or external
client app; you create these links with "org login web --client-app". Run "org display" to get the list of client app names.

Examples for **`org logout`**

Interactively select the orgs to log out of:

```
   sf org logout

```

Log out of the org with username me@my.org:

```
   sf org logout --target-org me@my.org

```

Log out of all orgs after confirmation:

```
   sf org logout --all

```

Logout of the org with alias my-scratch and don't prompt for confirmation:

```
   sf org logout --target-org my-scratch --no-prompt

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

**`-c`** **|** **`--client-app CLIENT-APP`**
Optional

Client app to log out of.

Type: option

**`-a`** **|** **`--all`**
Optional

Include all authenticated orgs.


Salesforce CLI Command Reference org Commands

All orgs includes Dev Hubs, sandboxes, DE orgs, and expired, deleted, and unknown-status scratch orgs.

Type: boolean

**`-p`** **|** **`--no-prompt`**
Optional

Don't prompt for confirmation.

Type: boolean

Aliases for **`org logout`**

```
   force:auth:logout

   auth:logout

#### **`org open`**

```

Open your default scratch org, or another specified org, in a browser.

#### Description for org open

To open a specific page, specify the portion of the URL after "https://mydomain.my.salesforce.com" as the value for the --path flag. For
example, specify "--path lightning" to open Lightning Experience, or specify "--path /apex/YourPage" to open a Visualforce page.

Use the --source-file flag to open ApexPage, FlexiPage, Flow, or Agent metadata from your local project in the associated Builder within
the Org.

To generate a URL but not launch it in your browser, specify --url-only.

To open in a specific browser, use the --browser flag. Supported browsers are "chrome", "edge", and "firefox". If you don't specify --browser,
the org opens in your default browser.

#### Examples for org open

Open your default org in your default browser:

```
   $ sf org open

```

Open your default org in an incognito window of your default browser:

```
   $ sf org open --private

```

Open the org with alias MyTestOrg1 in the Firefox browser:

```
   $ sf org open --target-org MyTestOrg1 --browser firefox

```

Display the navigation URL for the Lightning Experience page for your default org, but don't open the page in a browser:

```
   $ sf org open --url-only --path lightning

```

Open a local Lightning page in your default org's Lightning App Builder:

```
   $ sf org open --source-file force-app/main/default/flexipages/Hello.flexipage-meta.xml

```


Salesforce CLI Command Reference org Commands

Open a local Flow in Flow Builder:

```
   $ sf org open --source-file force-app/main/default/flows/Hello.flow-meta.xml

```

Open local Agent metadata (Bot) in Agent Builder:

```
   $ sf org open --source-file

   force-app/main/default/bots/Coral_Cloud_Agent/Coral_Cloud_Agent.bot-meta.xml

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

```
   --private
```

Optional

Open the org in the default browser using private (incognito) mode.

Type: boolean

**`-b`** **|** **`--browser BROWSER`**
Optional

Browser where the org opens.

Type: option

Permissible values are: chrome, edge, firefox

**`-p`** **|** **`--path PATH`**
Optional

Navigation URL path to open a specific page.

Type: option

**`-r`** **|** **`--url-only`**
Optional

Display navigation URL, but don’t launch browser.


Salesforce CLI Command Reference org Commands

Type: boolean

**`-f`** **|** **`--source-file SOURCE-FILE`**
Optional

Path to ApexPage, FlexiPage, Flow, or Agent metadata to open in the associated Builder.

Type: option

#### Aliases for org open

```
   force:org:open

   force:source:open

#### **`org open agent`**

```

Open an agent in your org's Agentforce Builder UI in a browser.

#### Description for org open agent

Use the --api-name flag to open an agent using its API name in the Agentforce Builder UI of your org. Alternatively, use the
--authoring-bundle flag to open an agent using the API name of its authoring bundle. The two API names are typically the same for the
same agent. Optionally specify the --version flag to open a specific version of the agent.

To generate the URL but not launch it in your browser, specify --url-only.

To open Agentforce Builder in a specific browser, use the --browser flag. Supported browsers are "chrome", "edge", and "firefox". If you
don't specify --browser, the org opens in your default browser.

#### Examples for org open agent

Open the agent with API name Coral_Cloud_Agent in your default org using your default browser; opens the highest version:

```
   $ sf org open agent --api-name Coral_Cloud_Agent

```

Open the agent in an incognito window of your default browser:

```
   $ sf org open agent --private --api-name Coral_Cloud_Agent:

```

Open the agent in an org with alias MyTestOrg1 using the Firefox browser:

```
   $ sf org open agent --target-org MyTestOrg1 --browser firefox --api-name Coral_Cloud_Agent

```

Open an agent in Agentforce Builder using its authoring bundle API name:

```
   $ sf org open agent --authoring-bundle Coral_Cloud_Agent

```

Open a version 1 of an agent in Agentforce Builder:

```
   $ sf org open agent --authoring-bundle Coral_Cloud_Agent --version 1

```

Flags

```
   --json
```

Optional


Salesforce CLI Command Reference org Commands

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

**`-n`** **|** **`--api-name API-NAME`**
Optional

API name, also known as developer name, of the agent you want to open in the org's Agentforce Builder UI.

Type: option

```
   --private
```

Optional

Open the agent in the default browser using private (incognito) mode.

Type: boolean

**`-b`** **|** **`--browser BROWSER`**
Optional

Browser where the org opens.

Type: option

Permissible values are: chrome, edge, firefox

**`-r`** **|** **`--url-only`**
Optional

Display navigation URL, but don’t launch browser.

Type: boolean

```
   --authoring-bundle AUTHORING-BUNDLE
```

Optional

API name of the agent's authoring bundle to open in Agentforce Builder.

Type: option

```
   --version VERSION
```

Optional

Version number of the agent to open in Agentforce Builder. If not specified, the highest version is opened by default.

Type: option


Salesforce CLI Command Reference org Commands

#### org open authoring-bundle (Deprecated) The command org open authoring-bundle has been deprecated. Open your org in Agentforce Studio, specifically in the list

view showing the list of agents.

#### Description for org open authoring-bundle

The list view shows the agents in your org that are implemented with Agent Script and an authoring bundle. Click on an agent name
to open it in Agentforce Builder in a new browser window.

To generate the URL but not launch it in your browser, specify --url-only.

#### Examples for org open authoring-bundle

Open the agents list view in your default org using your default browser:

```
   $ sf org open authoring-bundle

```

Open the agents list view in an incognito window of your default browser:

```
   $ sf org open authoring-bundle --private

```

Open the agents list view in an org with alias MyTestOrg1 using the Firefox browser:

```
   $ sf org open authoring-bundle --target-org MyTestOrg1 --browser firefox

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

```
   --private
```

Optional

Open the org in the default browser using private (incognito) mode.


Salesforce CLI Command Reference org Commands

Type: boolean

**`-b`** **|** **`--browser BROWSER`**
Optional

Browser where the org opens.

Type: option

Permissible values are: chrome, edge, firefox

**`-r`** **|** **`--url-only`**
Optional

Display navigation URL, but don't launch browser.

Type: boolean

#### **`org refresh sandbox`**

Refresh a sandbox org using the sandbox name.

#### Description for org refresh sandbox

Refreshing a sandbox copies the metadata, and optionally data, from your source org to the refreshed sandbox org. You can optionally
specify a definition file if you want to change the configuration of the refreshed sandbox, such as its license type or template ID. You
can also use the --source-id or --source-sandbox-name flags to change the refreshed sandbox org's original source org to a new org; in
this case, the refreshed sandbox org's metadata is updated with the new source org's metadata.

You're not allowed to change the sandbox name when you refresh it with this command. If you want to change the sandbox name, first
delete it with the "org delete sandbox" command. And then recreate it with the "org create sandbox" command and give it a new name.

#### Examples for org refresh sandbox

Refresh the sandbox named "devSbx1". The production org that contains the sandbox license has the alias "prodOrg".

```
   sf org refresh sandbox --name devSbx1 --target-org prodOrg

```

Refresh the sandbox named "devSbx2", and override the configuration of the refreshed sandbox with the properties in the specified
defintion file. The default target org is the production org, so you don't need to specify the `--target-org` flag in this case.

```
   sf org refresh sandbox --name devSbx2 --definition-file devSbx2-config.json

```

Refresh the sandbox using the name defined in the definition file. The production org that contains the sandbox license has the alias
"prodOrg".

```
   sf org refresh sandbox --definition-file devSbx3-config.json --target-org prodOrg

```

Refresh the sandbox named "devSbx2" by changing its original source org to be a sandbox called "devSbx3":

```
   sf org refresh sandbox --name devSbx2 --source-sandbox-name devSbx3 --target-org prodOrg

```

Flags

```
   --json
```

Optional

Format output as json.


Salesforce CLI Command Reference org Commands

Type: boolean

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option

```
   --no-auto-activate
```

Optional

Disable auto-activation of the sandbox after a successful refresh.

By default, a sandbox auto-activates after a refresh. Use this flag to control sandbox activation manually.

Type: boolean

**`-w`** **|** **`--wait WAIT`**
Optional

Number of minutes to poll for sandbox refresh status.

If the command continues to run after the wait period, the CLI returns control of the terminal to you and displays the "sf org resume
sandbox" command for you run to check the status of the refresh. The displayed command includes the job ID for the running
sandbox refresh.

Type: option

Default value: 30 minutes

**`-i`** **|** **`--poll-interval POLL-INTERVAL`**
Optional

Number of seconds to wait between status polling requests.

Type: option

Default value: 30 seconds

```
   --source-sandbox-name SOURCE-SANDBOX-NAME
```

Optional

Name of the sandbox org that becomes the new source org for the refreshed sandbox.

The value of --source-sandbox-name must be an existing sandbox. The new source sandbox, and the refreshed sandbox specified
with the --name flag, must both be associated with the production org (--target-org) that contains the sandbox licenses.

You can specify either --source-sandbox-name or --source-id when refreshing an existing sandbox, but not both.

Type: option

```
   --source-id SOURCE-ID
```

Optional

ID of the sandbox org that becomes the new source org for the refreshed sandbox.

The value of --source-id must be an existing sandbox. The new source sandbox, and the refreshed sandbox specified with the --name
flag, must both be associated with the production org (--target-org) that contains the sandbox licenses.

You can specify either --source-id or --source-sandbox-name when refreshing an existing sandbox, but not both.

Type: option

```
   --async
```

Optional

Request the sandbox refresh, but don't wait for it to complete.


Salesforce CLI Command Reference org Commands

The command immediately displays the job ID and returns control of the terminal to you. This way, you can continue to use the CLI.
To check the status of the sandbox refresh, run "sf org resume sandbox".

Type: boolean

**`-n`** **|** **`--name NAME`**
Optional

Name of the existing sandbox org in your production org that you want to refresh.

Type: option

**`-f`** **|** **`--definition-file DEFINITION-FILE`**
Optional

Path to a sandbox definition file for overriding its configuration when you refresh it.

The sandbox definition file is a blueprint for the sandbox; use the file to change the sandbox configuration during a refresh. If you
don't want to change the sandbox configuration when you refresh it, then simply use the --name flag to specify the sandbox and
don't use this flag. See
<https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_sandbox_definition.htm> for all the options
you can specify in the definition file.

Type: option

**`-o`** **|** **`--target-org TARGET-ORG`**
Required

Username or alias of the production org that contains the sandbox license.

Type: option

```
   --no-prompt
```

Optional

Don't prompt for confirmation about the sandbox refresh.

Type: boolean

#### **`org resume sandbox`**

Check the status of a sandbox creation, and log in to it if it's ready.

#### Description for org resume sandbox

Sandbox creation can take a long time. If the original "sf org create sandbox" command either times out, or you specified the --async
flag, the command displays a job ID. Use this job ID to check whether the sandbox creation is complete, and if it is, the command then
logs into it.

You can also use the sandbox name to check the status or the --use-most-recent flag to use the job ID of the most recent sandbox
creation.

#### Examples for org resume sandbox

Check the status of a sandbox creation using its name and specify a production org with alias "prodOrg":

```
   sf org resume sandbox --name mysandbox --target-org prodOrg

```


Salesforce CLI Command Reference org Commands

Check the status using the job ID:

```
   sf org resume sandbox --job-id 0GRxxxxxxxx

```

Check the status of the most recent sandbox create request:

```
   sf org resume sandbox --use-most-recent

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

**`-w`** **|** **`--wait WAIT`**
Optional

Number of minutes to wait for the sandbox org to be ready.

If the command continues to run after the wait period, the CLI returns control of the terminal window to you and returns the job ID.
To resume checking the sandbox creation, rerun this command.

Type: option

**`-n`** **|** **`--name NAME`**
Optional

Name of the sandbox org.

Type: option

**`-i`** **|** **`--job-id JOB-ID`**
Optional

Job ID of the incomplete sandbox creation that you want to check the status of.

The job ID is valid for 24 hours after you start the sandbox creation.

Type: option

**`-l`** **|** **`--use-most-recent`**
Optional

Use the most recent sandbox create request.

Type: boolean

**`-o`** **|** **`--target-org TARGET-ORG`**
Optional

Username or alias of the production org that contains the sandbox license.

When it creates the sandbox org, Salesforce copies the metadata, and optionally data, from your production org to the new sandbox
org.


Salesforce CLI Command Reference org Commands

Type: option

Aliases for **`org resume sandbox`**

```
   env:resume:sandbox

#### **`org resume scratch`**

```

Resume the creation of an incomplete scratch org.

#### Description for org resume scratch

When the original "sf org create scratch" command either times out or is run with the --async flag, it displays a job ID.

Run this command by either passing it a job ID or using the --use-most-recent flag to specify the most recent incomplete scratch org.

#### Examples for org resume scratch

Resume a scratch org create with a job ID:

```
   sf org resume scratch --job-id 2SR3u0000008fBDGAY

```

Resume your most recent incomplete scratch org:

```
   sf org resume scratch --use-most-recent

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

**`-i`** **|** **`--job-id JOB-ID`**
Optional

Job ID of the incomplete scratch org create that you want to resume.

The job ID is the same as the record ID of the incomplete scratch org in the ScratchOrgInfo object of the Dev Hub.

The job ID is valid for 24 hours after you start the scratch org creation.

Type: option

**`-r`** **|** **`--use-most-recent`**
Optional

Use the job ID of the most recent incomplete scratch org.

Type: boolean


### Salesforce CLI Command Reference package Commands

**`-w`** **|** **`--wait WAIT`**
Optional

Number of minutes to wait for the scratch org to be ready.

If the command continues to run after the wait period, the CLI returns control of the terminal window to you and returns the job ID.
To resume checking the scratch creation, rerun this command.

Type: option

Aliases for **`org resume scratch`**

```
   env:resume:scratch

### package Commands

```

Commands to develop and install unlocked packages and managed 2GP packages.

package convert
Convert a managed-released first-generation managed package into a second-generation managed package.

package create
Create a package.

package delete
Delete a package.

package install
Install or upgrade a version of a package in the target org.

package install report
Retrieve the status of a package installation request.

package installed list
List the org’s installed packages.

package list
List all packages in the Dev Hub org.

package push-upgrade abort
Abort a package push upgrade that has been scheduled. Only push upgrade requests with a status of Created or Pending can be
aborted.

package push-upgrade list
Lists the status of push upgrade requests for a given package.

package push-upgrade report
Retrieve the status of a package push upgrade.

package push-upgrade schedule
Schedule a package push upgrade.

package uninstall
Uninstall a second-generation package from the target org.


Salesforce CLI Command Reference package Commands

package uninstall report
Retrieve the status of a package uninstall request.

package update
Update package details.

package version create
Create a package version in the Dev Hub org.

package version create list
List package version creation requests.

package version create report
Retrieve details about a package version creation request.

package version delete
Delete a package version.

package version displayancestry
Display the ancestry tree for a 2GP managed package version.

package version displaydependencies
Display the dependency graph for an unlocked or 2GP managed package version.

package version list
List all package versions in the Dev Hub org.

package version promote
Promote a package version to released.

package version report
Retrieve details about a package version in the Dev Hub org.

package version retrieve
Retrieve package metadata for a specified package version. Package metadata can be retrieved for only second-generation managed
package versions or unlocked packages.

package version update
Update a package version.

#### **`package convert`**

Convert a managed-released first-generation managed package into a second-generation managed package.

#### Description for package convert

The package conversion command automatically selects the latest released major.minor first-generation managed package version,
and converts it into a second-generation managed package version.

Use --patch-version to specify a released patch version.

To retrieve details about a package version create request, including status and package version ID (04t), run "sf package version create
report -i 08c...".

To protect the contents of your package and to prevent unauthorized installation of your package, specify the --installation-key flag.

To promote a package version to released, you must use the --code-coverage parameter. The package must also meet the code coverage
requirements.


Salesforce CLI Command Reference package Commands

To list package version creation requests in the org, run "sf package version create list".

Examples for **`package convert`**

Create a second-generation managed package version from the first-generation managed package with the specified ID and give it the
installation key "password123"; uses your default Dev Hub org:

```
   sf package convert --package 033... --installation-key password123

```

Similar to previous example, but uses the specified Dev Hub org:

```
   sf package convert --package 033... --installation-key password123 --target-dev-hub

   devhuborg@example.com

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

**`-v`** **|** **`--target-dev-hub TARGET-DEV-HUB`**
Required

Username or alias of the Dev Hub org. Not required if the `target-dev-hub` configuration variable is already set.

Type: option

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

**`-p`** **|** **`--package PACKAGE`**
Required

ID (starts with 033) of the first-generation managed package to convert.

Type: option

**`-k`** **|** **`--installation-key INSTALLATION-KEY`**
Optional

Installation key for key-protected package.

Either an --installation-key value or the --installation-key-bypass flag is required.

Type: option

**`-f`** **|** **`--definition-file DEFINITION-FILE`**
Optional

Path to a definition file that contains features and org preferences that the metadata of the package version depends on.


Salesforce CLI Command Reference package Commands

This definition file is similar to the scratch org definition file.

Type: option

**`-x`** **|** **`--installation-key-bypass`**
Optional

Bypass the installation key requirement.

If you bypass this requirement, anyone can install your package. Either an --installation-key value or the --installation-key-bypass
flag is required.

Type: boolean

**`-w`** **|** **`--wait WAIT`**
Optional

Minutes to wait for the package version to be created.

Type: option

Default value: 0 minutes

**`-m`** **|** **`--seed-metadata SEED-METADATA`**
Optional

Directory containing metadata to be deployed prior to conversion.

The directory containing metadata that will be deployed on the build org prior to attempting package conversion.

Type: option

```
   --verbose
```

Optional

Display verbose command output.

Type: boolean

**`-a`** **|** **`--patch-version PATCH-VERSION`**
Optional

Specific released patch version to be converted.

Specify a released patch version as major.minor.patch to convert to a second-generation managed package version.

Type: option

**`-c`** **|** **`--code-coverage`**
Optional

Calculate and store the code coverage percentage by running the packaged Apex tests included in this package version.

Before you can promote and release a managed package version, the Apex code must meet a minimum 75% code coverage
requirement.

Type: boolean

Aliases for **`package convert`**

```
   force:package:convert

```


Salesforce CLI Command Reference package Commands

#### **`package create`**

Create a package.

#### Description for package create

First, use this command to create a package. Then create a package version.

If you don’t have a namespace defined in your sfdx-project.json file, use --no-namespace.

Your --name value must be unique within your namespace.

Run 'sf package list to list all packages in the Dev Hub org.

#### Examples for package create

Create an unlocked package from the files in the "force-app" directory; uses your default Dev Hub org:

```
   sf package create --name MyUnlockedPackage --package-type Unlocked --path force-app

```

Create a managed packaged from the "force-app" directory files, give the package a description, and use the specified Dev Hub org:

```
   sf package create --name MyManagedPackage --description "Your Package Descripton"

   --package-type Managed --path force-app --target-dev-hub devhub@example.com

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

**`-v`** **|** **`--target-dev-hub TARGET-DEV-HUB`**
Required

Username or alias of the Dev Hub org. Not required if the `target-dev-hub` configuration variable is already set.

Type: option

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

**`-n`** **|** **`--name NAME`**
Required

Name of the package to create.

Type: option


Salesforce CLI Command Reference package Commands

**`-t`** **|** **`--package-type PACKAGE-TYPE`**
Required

Type of package.

The options for package type are Managed and Unlocked (Managed=DeveloperManagedSubscriberManaged,
Unlocked=DeveloperControlledSubscriberEditable). These options determine upgrade and editability rules.

Type: option

Permissible values are: Managed, Unlocked

**`-d`** **|** **`--description DESCRIPTION`**
Optional

Description of the package.

Type: option

**`-e`** **|** **`--no-namespace`**
Optional

Create the package with no namespace; available only for unlocked packages.

This flag is useful when you’re migrating an existing org to packages. But use a namespaced package for new metadata.

Type: boolean

**`-r`** **|** **`--path PATH`**
Required

Path to directory that contains the contents of the package.

Type: option

```
   --org-dependent
```

Optional

Depends on unpackaged metadata in the installation org; applies to unlocked packages only.

Use Source Tracking in Sandboxes to develop your org-dependent unlocked package. For more information, see "Create Org-Dependent
Unlocked Packages" in the Salesforce DX Developer Guide.

Type: boolean

**`-o`** **|** **`--error-notification-username ERROR-NOTIFICATION-USERNAME`**
Optional

Active Dev Hub user designated to receive email notifications for package errors.

Email notifications include information about unhandled Apex exceptions, and install, upgrade, or uninstall failures associated with
your package.

Type: option

Aliases for **`package create`**

```
   force:package:create

#### **`package delete`**

```

Delete a package.


Salesforce CLI Command Reference package Commands

Description for **`package delete`**

Specify the ID or alias of the package you want to delete.

Delete unlocked and second-generation managed packages. Before you delete a package, first delete all associated package versions.

Examples for **`package delete`**

Delete a package using its alias from your default Dev Hub org:

```
   sf package delete --package "Your Package Alias"

```

Delete a package using its ID from the specified Dev Hub org:

```
   sf package delete --package 0Ho... --target-dev-hub devhub@example.com

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

**`-v`** **|** **`--target-dev-hub TARGET-DEV-HUB`**
Required

Username or alias of the Dev Hub org. Not required if the `target-dev-hub` configuration variable is already set.

Type: option

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

**`-n`** **|** **`--no-prompt`**
Optional

Don't prompt before deleting the package.

Type: boolean

**`-p`** **|** **`--package PACKAGE`**
Required

ID (starts with 0Ho) or alias of the package to delete.

Type: option


Salesforce CLI Command Reference package Commands

Aliases for **`package delete`**

```
   force:package:delete

#### **`package install`**

```

Install or upgrade a version of a package in the target org.

#### Description for package install

To install or upgrade a package, specify a specific version of the package using the 04t package ID. The package and the version you
specified installs in your default target org unless you supply the username for a different target org.

When upgrading an unlocked package, include the --upgrade-type value to specify whether any removed components are deprecated
or deleted. To delete components that can be safely deleted and deprecate the others, specify "--upgrade-type Mixed" (the default). To
deprecate all removed components, specify "--upgrade-type DeprecateOnly". To delete all removed components, except for custom
objects and custom fields, that don't have dependencies, specify "--upgrade-type Delete". (Note: This option can result in the loss of
data that is associated with the deleted components.)

#### Examples for package install

Install or upgrade a package version with the specified ID in the org with username "me@example.com":

```
   sf package install --package 04t... --target-org me@example.com

```

Install or upgrade a package version with the specified alias into your default org:

```
   sf package install --package awesome_package_alias

```

Install or upgrade a package version with an alias that includes spaces into your default org:

```
   sf package install --package "Awesome Package Alias"

```

Upgrade an unlocked package version with the specified ID and deprecate all removed components:

```
   sf package install --package 04t... --upgrade-type DeprecateOnly

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


Salesforce CLI Command Reference package Commands

Type: option

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

**`-w`** **|** **`--wait WAIT`**
Optional

Number of minutes to wait for installation status.

Type: option

Default value: 0 minutes

**`-k`** **|** **`--installation-key INSTALLATION-KEY`**
Optional

Installation key for key-protected package (default: null).

Type: option

**`-b`** **|** **`--publish-wait PUBLISH-WAIT`**
Optional

Maximum number of minutes to wait for the Subscriber Package Version ID to become available in the target org before canceling
the install request.

Type: option

Default value: 0 minutes

**`-r`** **|** **`--no-prompt`**
Optional

Don't prompt for confirmation.

Allows the following without an explicit confirmation response: 1) Remote Site Settings and Content Security Policy websites to
send or receive data, and 2) --upgrade-type Delete to proceed.

Type: boolean

**`-p`** **|** **`--package PACKAGE`**
Required

ID (starts with 04t) or alias of the package version to install.

Type: option

**`-a`** **|** **`--apex-compile APEX-COMPILE`**
Optional

Compile all Apex in the org and package, or only Apex in the package; unlocked packages only.

Applies to unlocked packages only. Specifies whether to compile all Apex in the org and package, or only the Apex in the package.

For package installs into production orgs, or any org that has Apex Compile on Deploy enabled, the platform compiles all Apex in
the org after the package install or upgrade operation completes.

This approach assures that package installs and upgrades don’t impact the performance of an org, and is done even if --apex-compile
package is specified.

Type: option

Permissible values are: all, package


Salesforce CLI Command Reference package Commands

Default value: all

**`-s`** **|** **`--security-type SECURITY-TYPE`**
Optional

Security access type for the installed package. Available options are AdminsOnly and AllUsers.

Type: option

Permissible values are: AllUsers, AdminsOnly

Default value: AdminsOnly

**`-t`** **|** **`--upgrade-type UPGRADE-TYPE`**
Optional

Upgrade type for the package installation; available only for unlocked packages.

For unlocked package upgrades, set this flag to one of these values:

      - DeprecateOnly: Mark all removed components as deprecated.

      - Mixed: Delete all removed components that can be safely deleted and deprecate the other components.

      - Delete: Delete removed components, except for custom objects and custom fields, that don't have dependencies.

Type: option

Permissible values are: DeprecateOnly, Mixed, Delete

Default value: Mixed

#### Aliases for package install

```
   force:package:install

#### **`package install report`**

```

Retrieve the status of a package installation request.

#### Examples for package install report

Retrieve the status of a package installation request with the specified ID on your default org:

```
   sf package install report --request-id 0Hf...

```

Similar to previous example, except use the org with username me@example.com:

```
   sf package install report --request-id 0Hf... --target-org me@example.com

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


Salesforce CLI Command Reference package Commands

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

**`-i`** **|** **`--request-id REQUEST-ID`**
Required

ID of the package install request you want to check; starts with 0Hf.

Type: option

Aliases for **`package install report`**

```
   force:package:install:report

#### **`package installed list`**

```

List the org’s installed packages.

#### Examples for package installed list

List the installed packages in your default org:

```
   sf package installed list

```

List the installed packages in the org with username me@example.com:

```
   sf package installed list --target-org me@example.com

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


Salesforce CLI Command Reference package Commands

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

Aliases for **`package installed list`**

```
   force:package:installed:list

#### **`package list`**

```

List all packages in the Dev Hub org.

#### Description for package list

Description

#### Examples for package list

List all packages in the specified Dev Hub org:

```
   sf package list --target-dev-hub devhub@example.com

```

List all packages details in the specified Dev Hub org, and show extended details about each package:

```
   sf package list --target-dev-hub devhub@example.com --verbose

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

**`-v`** **|** **`--target-dev-hub TARGET-DEV-HUB`**
Required

Username or alias of the Dev Hub org. Not required if the `target-dev-hub` configuration variable is already set.

Type: option


Salesforce CLI Command Reference package Commands

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

```
   --verbose
```

Optional

Display extended package detail.

Type: boolean

Aliases for **`package list`**

```
   force:package:list

#### **`package push-upgrade abort`**

```

Abort a package push upgrade that has been scheduled. Only push upgrade requests with a status of Created or Pending can be aborted.

#### Description for package push-upgrade abort

Specify the request ID that you want to abort. If applicable, the command displays errors related to the request.

To show all requests in the org, run "sf package pushupgrade list --package 033...".

#### Examples for package push-upgrade abort

Cancel the specified package push upgrade request with the specified ID; uses your default Dev Hub org:

```
   sf package push-upgrade abort --push-request-id 0DV...

```

Cancel the specified package push upgrade request in the Dev Hub org with username devhub@example.com:

```
   sf package push-upgrade abort --push-request-id 0DV... --target-dev-hub devhub@example.com

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

**`-v`** **|** **`--target-dev-hub TARGET-DEV-HUB`**
Required

Username or alias of the Dev Hub org. Not required if the `target-dev-hub` configuration variable is already set.


Salesforce CLI Command Reference package Commands

Type: option

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

**`-i`** **|** **`--push-request-id PUSH-REQUEST-ID`**
Required

ID of the package push request (starts with 0DV). This ID is returned after the package push-upgrade schedule command completes
successfully.

Type: option

#### **`package push-upgrade list`**

Lists the status of push upgrade requests for a given package.

#### Description for package push-upgrade list

Shows the details of each request to create a push upgrade in the Dev Hub org.

All filter parameters are applied using the AND logical operator (not OR).

To get information about a specific request, run "sf package pushupgrade report" and supply the request ID.

#### Examples for package push-upgrade list

List all package push upgrade requests in the specified Dev Hub org:

```
   sf package push-upgrade list --package 033xyz --target-dev-hub myHub

```

List all package push upgrade requests in the specified Dev Hub org scheduled in the last 30 days:

```
   sf package push-upgrade list --package 033xyz --scheduled-last-days 30 --target-dev-hub

   myHub

```

List all package push upgrade with a status Succeeded:

```
   sf package push-upgrade list --package 033xyz –-status Succeeded

```

List all package push upgrade with a status Failed:

```
   sf package push-upgrade list --package 033xyz –-status Failed

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


Salesforce CLI Command Reference package Commands

Import flag values from a directory.

Type: option

**`-v`** **|** **`--target-dev-hub TARGET-DEV-HUB`**
Required

Username or alias of the Dev Hub org. Not required if the `target-dev-hub` configuration variable is already set.

Type: option

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

**`-p`** **|** **`--package PACKAGE`**
Required

Package ID (starts with 033) of the package that you want push upgrade information for.

Type: option

**`-l`** **|** **`--scheduled-last-days SCHEDULED-LAST-DAYS`**
Optional

Number of days in the past for which to display the list of push upgrade requests that were scheduled. Used to filter the list output
to only recently scheduled push upgrades.

Type: option

**`-s`** **|** **`--status STATUS`**
Optional

Status used to filter the list output Valid values are: Created, Canceled, Pending, In Progress, Failed, or Succeeded

Type: option

Permissible values are: Created, Cancelled, Pending, In Progress, Failed, Succeeded

```
   --show-push-migrations-only
```

Optional

Display only push upgrade requests for package migrations.

Type: boolean

Aliases for **`package push-upgrade list`**

```
   force:package:push-upgrade:list

#### **`package push-upgrade report`**

```

Retrieve the status of a package push upgrade.

#### Description for package push-upgrade report

Specify the request ID for which you want to view details. If applicable, the command displays errors related to the request.

To show all requests in the org, run "sf package pushupgrade list".


Salesforce CLI Command Reference package Commands

Examples for **`package push-upgrade report`**

Retrieve details about the package push upgrade with the specified ID; uses your default Dev Hub org:

```
   sf package push-upgrade report --push-request-id 0DV...

```

Retrieve details about the specified package push request in the Dev Hub org with username devhub@example.com:

```
   sf package push-upgrade report --push-request-id 0DV... --target-dev-hub devhub@example.com

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

**`-v`** **|** **`--target-dev-hub TARGET-DEV-HUB`**
Required

Username or alias of the Dev Hub org. Not required if the `target-dev-hub` configuration variable is already set.

Type: option

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

**`-i`** **|** **`--push-request-id PUSH-REQUEST-ID`**
Required

ID of the package push request (starts with 0DV). This ID is returned after the package push-upgrade schedule command completes
successfully.

Type: option

Aliases for **`package push-upgrade report`**

```
   force:package:push-upgrade:report

#### **`package push-upgrade schedule`**

```

Schedule a package push upgrade.

#### Description for package push-upgrade schedule

Represents a push upgrade request for upgrading a package in one or many orgs from one version to another version.


Salesforce CLI Command Reference package Commands

To initiate a push upgrade for an unlocked or second-generation managed package, the Create and Update Second-Generation Packages
user permission is required.

For second-generation managed packages, the push upgrade feature is available only for packages that have passed AppExchange
security review. To enable push upgrades for your managed package, log a support case in the Salesforce Partner Community.

For unlocked packages, push upgrades are enabled by default.

Use the -–migrate-to-2GP flag to indicate you’re installing a converted second-generation managed package into an org that has the
first-generation managed package version of that package installed.

Examples for **`package push-upgrade schedule`**

Schedule a push upgrade that initiates at a specified time:

```
   sf package push-upgrade schedule --package 04txyz --start-time "2024-12-06T21:00:00"

   --org-file upgrade-orgs.csv --target-dev-hub myHub

```

Schedule a push upgrade that initiates as soon as possible:

```
   sf package push-upgrade schedule --package 04txyz --org-file upgrade-orgs.csv

   --target-dev-hub myHub

```

Schedule a push migration from a 1GP package to a 2GP package:

```
   sf package push-upgrade schedule --migrate-to-2gp --package 04txyz --start-time

   "2024-12-06T21:00:00" --org-file upgrade-orgs.csv --target-dev-hub myHub

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

**`-v`** **|** **`--target-dev-hub TARGET-DEV-HUB`**
Required

Username or alias of the Dev Hub org that owns the package.

Overrides the value of the target-dev-hub configuration variable, if set.

Type: option

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

**`-p`** **|** **`--package PACKAGE`**
Required


Salesforce CLI Command Reference package Commands

ID (starts with 04t) of the package version that the package is being upgraded to. The package version must be an active, non-beta
package version.

Type: option

**`-t`** **|** **`--start-time START-TIME`**
Optional

Date and time (UTC) when the push upgrade is processed. Set to the earliest time that you want Salesforce to attempt to start the
upgrade.

Scheduled push upgrades begin as soon as resources are available on the Salesforce instance, which is either at or after the start
time you specify. In certain scenarios, the push upgrade starts a few hours after the scheduled start time.

As a best practice, schedule push upgrades at off-peak hours like 1:00 AM Saturday.

If you don't specify this flag, the push upgrade is scheduled to run as soon as resources are available on the Salesforce instance.

Type: option

**`-l`** **|** **`--org-list ORG-LIST`**
Optional

Comma-separated list of subscriber org IDs that need the package upgrade. Either --org-list or --org-file must be specified.

Type: option

**`-f`** **|** **`--org-file ORG-FILE`**
Optional

Filename of the CSV file that contains the list of subscriber org IDs that need the package upgrade. Either --org-list or --org-file must
be specified.

The file must contain one org per line. The org ID must be the only value in each row.

All listed orgs must have a package version installed in their org that is lower than the package version you specified for the --package
flag.

Type: option

```
   --migrate-to-2gp
```

Optional

Upgrade from a first-generation managed package (1GP) to a second-generation managed package (2GP). Required when you’re
pushing a 2GP package to orgs with the 1GP version installed.

Type: boolean

#### **`package uninstall`**

Uninstall a second-generation package from the target org.

#### Description for package uninstall

Specify the package ID for a second-generation package.

To list the org’s installed packages, run "sf package installed list".

To uninstall a first-generation package, from Setup, enter Installed Packages in the Quick Find box, then select Installed Packages.


Salesforce CLI Command Reference package Commands

Examples for **`package uninstall`**

Uninstall a package with specified ID from an org with username me@example.com:

```
   sf package uninstall --package 04t... --target-org me@example.com

```

Uninstall a package with the specified alias from your default org:

```
   sf package uninstall --package undesirable_package_alias

```

Uninstall a package with an alias that contains spaces from your default org:

```
   sf package uninstall --package "Undesirable Package Alias"

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

**`-w`** **|** **`--wait WAIT`**
Optional

Number of minutes to wait for uninstall status.

Type: option

Default value: 0 minutes

**`-p`** **|** **`--package PACKAGE`**
Required

ID (starts with 04t) or alias of the package version to uninstall.

Type: option

Aliases for **`package uninstall`**

```
   force:package:uninstall

```


Salesforce CLI Command Reference package Commands

#### **`package uninstall report`**

Retrieve the status of a package uninstall request.

#### Examples for package uninstall report

Retrieve the status of a package uninstall in your default org using the specified request ID:

```
   sf package uninstall report --request-id 06y...

```

Similar to previous example, but use the org with username me@example.com:

```
   sf package uninstall report --request-id 06y... --target-org me@example.com

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

**`-i`** **|** **`--request-id REQUEST-ID`**
Required

ID of the package uninstall request you want to check; starts with 06y.

Type: option

#### Aliases for package uninstall report

```
   force:package:uninstall:report

#### **`package update`**

```

Update package details.


Salesforce CLI Command Reference package Commands

Description for **`package update`**

Specify a new value for each option you want to update.

Run "sf package list" to list all packages in the Dev Hub org.

Examples for **`package update`**

Update the name of the package with the specified alias; uses your default Dev Hub org:

```
   sf package update --package "Your Package Alias" --name "New Package Name"

```

Update the description of the package with the specified ID; uses the specified Dev Hub org:

```
   sf package update --package 0Ho... --description "New Package Description" --target-dev-hub

    devhub@example.com

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

**`-v`** **|** **`--target-dev-hub TARGET-DEV-HUB`**
Required

Username or alias of the Dev Hub org. Not required if the `target-dev-hub` configuration variable is already set.

Type: option

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

**`-p`** **|** **`--package PACKAGE`**
Required

ID (starts with 0Ho) or alias of the package to update.

Type: option

**`-n`** **|** **`--name NAME`**
Optional

New name of the package.

Type: option

**`-d`** **|** **`--description DESCRIPTION`**
Optional


Salesforce CLI Command Reference package Commands

New description of the package.

Type: option

**`-o`** **|** **`--error-notification-username ERROR-NOTIFICATION-USERNAME`**
Optional

Active Dev Hub user designated to receive email notifications for package errors.

Email notifications include information about unhandled Apex exceptions, and install, upgrade, or uninstall failures associated with
your package.

Type: option

```
   --enable-app-analytics
```

Optional

Enable AppExchange App Analytics usage data collection on this managed package and its components.

Type: boolean

**`-r`** **|** **`--recommended-version-id RECOMMENDED-VERSION-ID`**
Optional

ID of the package version that's installed when subscribers click the Upgrade to Recommended Version option on the Installed
Packages page of their org.

Specify the recommended package version for subscribers to install. If a subscriber has a package version installed in their org that's
lower than the version you set, the subscriber sees the Upgrade to Recommended Version option on the Installed Packages page.
Only released package versions can be set as the recommended version.

Type: option

```
   --skip-ancestor-check
```

Optional

Bypass the ancestry check for setting a recommended version.

Type: boolean

Aliases for **`package update`**

```
   force:package:update

#### **`package version create`**

```

Create a package version in the Dev Hub org.

#### Description for package version create

The package version is based on the package contents in the specified directory.

To retrieve details about a package version create request, including status and package version ID (04t), run "sf package version create
report -i 08c...".

We recommend that you specify the --installation-key parameter to protect the contents of your package and to prevent unauthorized
installation of your package.

To list package version creation requests in the org, run "sf package version create list".


Salesforce CLI Command Reference package Commands

To promote a package version to released, you must use the --code-coverage parameter. The package must also meet the code coverage
requirements. This requirement applies to both managed and unlocked packages.

We don’t calculate code coverage for org-dependent unlocked packages, or for package versions that specify --skip-validation.

Examples for **`package version create`**

Create a package version from the contents of the "common" directory and give it an installation key of "password123"; uses your default
Dev Hub org:

```
   sf package version create --path common --installation-key password123

```

Create a package version from a package with the specified alias; uses the Dev Hub org with username devhub@example.com:

```
   sf package version create --package "Your Package Alias" --installation-key password123

   --target-dev-hub devhub@example.com

```

Create a package version from a package with the specified ID:

```
   sf package version create --package 0Ho... --installation-key password123

```

Create a package version and skip the validation step:

```
   sf package version create --path common --installation-key password123 --skip-validation

```

Create a package version and perform package validations asynchronously:

```
   sf package version create --path common --installation-key password123 --async-validation

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

**`-v`** **|** **`--target-dev-hub TARGET-DEV-HUB`**
Required

Username or alias of the Dev Hub org. Not required if the `target-dev-hub` configuration variable is already set.

Type: option

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

**`-b`** **|** **`--branch BRANCH`**
Optional


Salesforce CLI Command Reference package Commands

Name of the branch in your source control system that the package version is based on.

Type: option

**`-c`** **|** **`--code-coverage`**
Optional

Calculate and store the code coverage percentage by running the packaged Apex tests included in this package version.

Before you can promote and release a managed or unlocked package version, the Apex code must meet a minimum 75% code
coverage requirement. We don’t calculate code coverage for org-dependent unlocked packages or for package versions that specify
--skip-validation.

Type: boolean

**`-f`** **|** **`--definition-file DEFINITION-FILE`**
Optional

Path to a definition file similar to scratch org definition file that contains the list of features and org preferences that the metadata
of the package version depends on.

For a patch version, the features specified in this file are ignored, and instead the features specified for the ancestor version are used.

Type: option

**`-k`** **|** **`--installation-key INSTALLATION-KEY`**
Optional

Installation key for key-protected package. (either --installation-key or --installation-key-bypass is required)

Type: option

**`-x`** **|** **`--installation-key-bypass`**
Optional

Bypass the installation key requirement. (either --installation-key or --installation-key-bypass is required)

If you bypass this requirement, anyone can install your package.

Type: boolean

**`-p`** **|** **`--package PACKAGE`**
Optional

ID (starts with 0Ho) or alias of the package to create a version of.

Type: option

**`-d`** **|** **`--path PATH`**
Optional

Path to the directory that contains the contents of the package.

Type: option

```
   --post-install-script POST-INSTALL-SCRIPT
```

Optional

Name of the post-install script; applies to managed packages only.

The post-install script is an Apex class within this package that is run in the installing org after installations or upgrades of this package
version.

Type: option

```
   --post-install-url POST-INSTALL-URL
```

Optional


Salesforce CLI Command Reference package Commands

Post-install instructions URL.

The contents of the post-installation instructions URL are displayed in the UI after installation of the package version.

Type: option

```
   --releasenotes-url RELEASENOTES-URL
```

Optional

Release notes URL.

This link is displayed in the package installation UI to provide release notes for this package version to subscribers.

Type: option

```
   --skip-ancestor-check
```

Optional

Override ancestry requirements, which allows you to specify a package ancestor that isn’t the highest released package version.

Type: boolean

```
   --skip-validation
```

Optional

Skip validation during package version creation; you can’t promote unvalidated package versions.

Skips validation of dependencies, package ancestors, and metadata during package version creation. Skipping validation reduces
the time it takes to create a new package version, but you can promote only validated package versions. Skipping validation can
suppress important errors that can surface at a later stage. You can specify skip validation or code coverage, but not both. Code
coverage is calculated during validation.

Type: boolean

```
   --async-validation
```

Optional

Return a new package version before completing package validations.

Specifying async validation returns the package version earlier in the process, allowing you to install and test the new version right
away. If your development team is using continuous integration (CI) scripts, async validation can reduce your overall CI run time.

Type: boolean

```
   --generate-pkg-zip
```

Optional

Generate a package ZIP file that you can use for debugging or to examine the package contents.

Type: boolean

**`-t`** **|** **`--tag TAG`**
Optional

Package version’s tag.

Type: option

```
   --uninstall-script UNINSTALL-SCRIPT
```

Optional

Uninstall script name; applies to managed packages only.

The uninstall script is an Apex class within this package that is run in the installing org after uninstallations of this package.

Type: option


Salesforce CLI Command Reference package Commands

**`-e`** **|** **`--version-description VERSION-DESCRIPTION`**
Optional

Description of the package version to be created; overrides the sfdx-project.json value.

Type: option

**`-a`** **|** **`--version-name VERSION-NAME`**
Optional

Name of the package version to be created; overrides the sfdx-project.json value.

Type: option

**`-n`** **|** **`--version-number VERSION-NUMBER`**
Optional

Version number of the package version to be created; overrides the sfdx-project.json value.

For information about the format of the version number, see
https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev2gp_config_file.htm.

Type: option

**`-w`** **|** **`--wait WAIT`**
Optional

Number of minutes to wait for the package version to be created.

Type: option

Default value: 0 minutes

```
   --language LANGUAGE
```

Optional

Language for the package.

Specify the language using a language code listed under "Supported Languages" in Salesforce Help. If no language is specified, the
language defaults to the language of the Dev Hub user who created the package.

Type: option

```
   --verbose
```

Optional

Display verbose command output.

Display verbose command output. When polling for the status of the creation, this will output status and timeout data on a separate
line for each poll request, which is useful in CI systems where timeouts can occur with long periods of no output from commands.

Type: boolean

#### Aliases for package version create

```
   force:package:version:create

#### **`package version create list`**

```

List package version creation requests.


Salesforce CLI Command Reference package Commands

Description for **`package version create list`**

Shows the details of each request to create a package version in the Dev Hub org.

All filter parameters are applied using the AND logical operator (not OR).

To get information about a specific request, run "sf package version create report" and supply the request ID.

Examples for **`package version create list`**

List all package version creation requests in your default Dev Hub org:

```
   sf package version create list

```

List package version creation requests from the last 3 days in the Dev Hub org with username devhub@example.com:

```
   sf package version create list --created-last-days 3 --target-dev-hub

```

List package version creation requests with status Error:

```
   sf package version create list --status Error

```

List package version creation requests with status InProgress:

```
   sf package version create list --status InProgress

```

List package version creation requests with status Success that were created today:

```
   sf package version create list --created-last-days 0 --status Success

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

**`-v`** **|** **`--target-dev-hub TARGET-DEV-HUB`**
Required

Username or alias of the Dev Hub org. Not required if the `target-dev-hub` configuration variable is already set.

Type: option

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

**`-c`** **|** **`--created-last-days CREATED-LAST-DAYS`**
Optional


Salesforce CLI Command Reference package Commands

Number of days since the request was created, starting at 00:00:00 of first day to now. Use 0 for today.

Type: option

**`-s`** **|** **`--status STATUS`**
Optional

Status of the version creation request, used to filter the list.

Type: option

Permissible values are: Queued, InProgress, Success, Error

```
   --show-conversions-only
```

Optional

Filter the list output to display only converted package version.

Type: boolean

```
   --verbose
```

Optional

Displays additional information at a slight performance cost, such as the version name and number for each package version create
request.

Type: boolean

Aliases for **`package version create list`**

```
   force:package:version:create:list

#### **`package version create report`**

```

Retrieve details about a package version creation request.

#### Description for package version create report

Specify the request ID for which you want to view details. If applicable, the command displays errors related to the request.

To show all requests in the org, run "sf package version create list".

#### Examples for package version create report

Retrieve details about the package version creation request with the specified ID; uses your default Dev Hub org:

```
   sf package version create report --package-create-request-id 08c...

```

Retrieve details about the specified package version creation request in the Dev Hub org with username devhub@example.com:

```
   sf package version create report --package-create-request-id 08c... --target-dev-hub

   devhub@example.com

```

Flags

```
   --json
```

Optional

Format output as json.


Salesforce CLI Command Reference package Commands

Type: boolean

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option

**`-v`** **|** **`--target-dev-hub TARGET-DEV-HUB`**
Required

Username or alias of the Dev Hub org. Not required if the `target-dev-hub` configuration variable is already set.

Type: option

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

**`-i`** **|** **`--package-create-request-id PACKAGE-CREATE-REQUEST-ID`**
Required

ID (starts with 08c) of the package version creation request you want to display.

Type: option

Aliases for **`package version create report`**

```
   force:package:version:create:report

#### **`package version delete`**

```

Delete a package version.

#### Description for package version delete

Specify the ID or alias of the package version you want to delete. In second-generation managed packaging, only beta package versions
can be deleted. Before deleting a package version, review the considerations outlined in
https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_package_deletion.htm.

#### Examples for package version delete

Delete a package version with the specified alias using your default Dev Hub org:

```
   sf package version delete --package "Your Package Alias"

```

Delete a package version with the specified ID using the Dev Hub org with username "devhub@example.com":

```
   sf package version delete --package 04t... --target-org devhub@example.com

```

Flags

```
   --json
```

Optional


Salesforce CLI Command Reference package Commands

Format output as json.

Type: boolean

```
   --flags-dir FLAGS-DIR
```

Optional

Import flag values from a directory.

Type: option

**`-v`** **|** **`--target-dev-hub TARGET-DEV-HUB`**
Required

Username or alias of the Dev Hub org. Not required if the `target-dev-hub` configuration variable is already set.

Type: option

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

**`-n`** **|** **`--no-prompt`**
Optional

Don’t prompt before deleting the package version.

Type: boolean

**`-p`** **|** **`--package PACKAGE`**
Required

ID (starts with 04t) or alias of the package version to delete.

Type: option

Aliases for **`package version delete`**

```
   force:package:version:delete

#### **`package version displayancestry`**

```

Display the ancestry tree for a 2GP managed package version.

#### Examples for package version displayancestry

Display the ancestry tree for a package version with the specified alias, using your default Dev Hub org:

```
   sf package version displayancestry --package package_version_alias

```

Similar to previous example, but display the output in DOT code:

```
   sf package version displayancestry --package package_version_alias --dot-code

```

Display the ancestry tree for a package with the specified ID, using the Dev Hub org with username devhub@example.com:

```
   sf package version displayancestry --package OHo... --target-dev-hub devhub@example.com

```


Salesforce CLI Command Reference package Commands

Display the ancestry tree of a package version with the specified ID, using your default Dev Hub org:

```
   sf package version displayancestry --package 04t...

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

**`-v`** **|** **`--target-dev-hub TARGET-DEV-HUB`**
Required

Username or alias of the Dev Hub org. Not required if the `target-dev-hub` configuration variable is already set.

Type: option

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

**`-p`** **|** **`--package PACKAGE`**
Required

ID or alias of the package (starts with 0Ho) or package version (starts with 04t) to display ancestry for.

If you specify a package ID (starts with 0Ho) or alias, the ancestor tree for every package version associated with the package ID is
displayed. If you specify a package version (starts with 04t) or alias, the ancestry tree of the specified package version is displayed.

Type: option

```
   --dot-code
```

Optional

Display the ancestry tree in DOT code.

You can use the DOT code output in graph visualization software to create tree visualizations.

Type: boolean

```
   --verbose
```

Optional

Display both the package version ID (starts with 04t) and the version number (major.minor.patch.build) in the ancestry tree.

Type: boolean

Aliases for **`package version displayancestry`**

```
   force:package:version:displayancestry

```


Salesforce CLI Command Reference package Commands

#### **`package version displaydependencies`**

Display the dependency graph for an unlocked or 2GP managed package version.

#### Examples for package version displaydependencies

Display the dependency graph for a package version with the specified alias, using your default Dev Hub org and the default edge-direction:

```
   sf package version displaydependencies --package package_version_alias

```

Display the dependency graph for a package version with the specified ID and display the graph using a root-last edge direction. Use
the Dev Hub org with username devhub@example.com:

```
   sf package version displaydependencies --package 04t... --edge-direction root-last

   --target-dev-hub devhub@example.com

```

Display the dependency graph of a version create request with the specified ID, using your default Dev Hub org and the default
edge-direction:

```
   sf package version displaydependencies --package 08c...

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

**`-v`** **|** **`--target-dev-hub TARGET-DEV-HUB`**
Required

Username or alias of the Dev Hub org. Not required if the `target-dev-hub` configuration variable is already set.

Type: option

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

**`-p`** **|** **`--package PACKAGE`**
Required

ID or alias of the package version (starts with 04t) or the package version create request (starts with 08c) to display the dependency
graph for.

Before running this command, update your sfdx-project.json file to specify the calculateTransitiveDependencies attribute, and set
the value to true. This command returns GraphViz code, which can be compiled to a graph using DOT code or another graph
visualization software.

Type: option


Salesforce CLI Command Reference package Commands

```
   --edge-direction EDGE-DIRECTION
```

Optional

Order (root-first or root-last) in which the dependencies are displayed.

A root-first graph declares the root as the package that must be installed last. A root-last graph is the reverse order of root-first. If
you specify "--edge-direction root-last", the graph displays the packages in the order they must be installed. The root starts with the
farthest leaf of the package dependencies and ends with the base package, which must be installed last.

Type: option

Permissible values are: root-first, root-last

Default value: root-first

```
   --verbose
```

Optional

Display both the package version ID (starts with 04t) and the version number (major.minor.patch.build) in each node.

Type: boolean

#### **`package version list`**

List all package versions in the Dev Hub org.

#### Description for package version list

Description

#### Examples for package version list

List package versions in your default Dev Hub org that were created in the last 3 days; show only the released versions and order the list
using the PatchVersion field. Display extended details about each package version:

```
   sf package version list --verbose --created-last-days 3 --released --order-by PatchVersion

```

List the released package versions for the two specified packages that were modified today; use the Dev Hub org with username
devhub@example.com:

```
   sf package version list --packages 0Ho000000000000,0Ho000000000001 --released

   --modified-last-days 0 --target-dev-hub devhub@example.com

```

List all released package versions in your default Dev Hub org:

```
   sf package version list --released

```

List package versions that were modified today in your default Dev Hub org; show limited details about each one:

```
   sf package version list --concise --modified-last-days 0

```

List package versions that are based on the "featureA" branch in your source control system that were modified today in your default
Dev Hub org; show limited details about each one:

```
   sf package version list --concise --modified-last-days 0 --branch featureA

```

List released package versions that were created in the last 3 days in your default Dev Hub org; show limited details:

```
   sf package version list --concise --created-last-days 3 --released

```


Salesforce CLI Command Reference package Commands

List released package versions that were modified today for the two packages with specified aliases in your default Dev Hub org:

```
   sf package version list --packages exp-mgr,exp-mgr-util --released --modified-last-days 0

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

**`-v`** **|** **`--target-dev-hub TARGET-DEV-HUB`**
Required

Username or alias of the Dev Hub org. Not required if the `target-dev-hub` configuration variable is already set.

Type: option

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

**`-c`** **|** **`--created-last-days CREATED-LAST-DAYS`**
Optional

Number of days since the request was created, starting at 00:00:00 of first day to now. Use 0 for today.

Type: option

```
   --concise
```

Optional

Display limited package version details.

Type: boolean

```
   --show-conversions-only
```

Optional

Filter the list output to display only converted package version.

Type: boolean

**`-m`** **|** **`--modified-last-days MODIFIED-LAST-DAYS`**
Optional

Number of days since the items were modified, starting at 00:00:00 of first day to now. Use 0 for today.

Type: option

**`-p`** **|** **`--packages PACKAGES`**
Optional

Comma-delimited list of packages (aliases or 0Ho IDs) to list.


Salesforce CLI Command Reference package Commands

Type: option

**`-r`** **|** **`--released`**
Optional

Display released versions only (IsReleased=true).

Type: boolean

**`-b`** **|** **`--branch BRANCH`**
Optional

Branch in your source control system used to filter the results; only package versions based on the specified branch are listed.

Type: option

**`-o`** **|** **`--order-by ORDER-BY`**
Optional

Package version fields used to order the list.

Type: option

```
   --verbose
```

Optional

Display extended package version details.

Type: boolean

Aliases for **`package version list`**

```
   force:package:version:list

#### **`package version promote`**

```

Promote a package version to released.

#### Description for package version promote

Supply the ID or alias of the package version you want to promote. Promotes the package version to released status.

#### Examples for package version promote

Promote the package version with the specified ID to released; uses your default Dev Hub org:

```
   sf package version promote --package 04t...

```

Promote the package version with the specified alias to released; uses the Dev Hub org with username devhub@example.com:

```
   sf package version promote --package awesome_package_alias --target-dev-hub

   devhub@example.com

```

Promote the package version with an alias that has spaces to released:

```
   sf package version promote --package "Awesome Package Alias"

```


Salesforce CLI Command Reference package Commands

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

**`-v`** **|** **`--target-dev-hub TARGET-DEV-HUB`**
Required

Username or alias of the Dev Hub org. Not required if the `target-dev-hub` configuration variable is already set.

Type: option

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

**`-p`** **|** **`--package PACKAGE`**
Required

ID (starts with 04t) or alias of the package version to promote.

Type: option

**`-n`** **|** **`--no-prompt`**
Optional

Don't prompt to confirm setting the package version as released.

Type: boolean

Aliases for **`package version promote`**

```
   force:package:version:promote

#### **`package version report`**

```

Retrieve details about a package version in the Dev Hub org.

#### Description for package version report

To update package version values, run "sf package version update".

#### Examples for package version report

Retrieve details about the package version with the specified ID from your default Dev Hub org:

```
   sf package version report --package 04t...

```


Salesforce CLI Command Reference package Commands

Retrieve details about the package version with the specified alias (that contains spaces) from the Dev Hub org with username
devhub@example.com:

```
   sf package version report --package "Your Package Alias" --target-dev-hub devhub@example.com

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

**`-v`** **|** **`--target-dev-hub TARGET-DEV-HUB`**
Required

Username or alias of the Dev Hub org. Not required if the `target-dev-hub` configuration variable is already set.

Type: option

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

**`-p`** **|** **`--package PACKAGE`**
Required

ID (starts with 04t) or alias of the package to retrieve details for.

Type: option

```
   --verbose
```

Optional

Display extended package version details.

Type: boolean

Aliases for **`package version report`**

```
   force:package:version:report

#### **`package version retrieve`**

```

Retrieve package metadata for a specified package version. Package metadata can be retrieved for only second-generation managed
package versions or unlocked packages.


Salesforce CLI Command Reference package Commands

Description for **`package version retrieve`**

Retrieving a package version downloads the metadata into the directory you specify.

When you run this command, specify the subscriber package version ID (starts with 04t) and the path to an empty directory.

By default, the package version retrieve command is available to 2GP managed packages that were converted from 1GP. To use this
command with a managed package created using 2GP (not converted from 1GP) or with an unlocked package, specify
IsDevUsePkgZipRequested = true in the Package2VersionCreateRequest Tooling API object. If you run this command and the zip folder
with the package version’s source files is missing, confirm that IsDevUsePkgZipRequested is set to true.

Examples for **`package version retrieve`**

Retrieve package metadata for a converted subscriber package version ID (starts with 04t) into my-directory/ within your Salesforce DX
project directory:

```
   sf package version retrieve --package 04tXXX --output-dir my-directory/ --target-dev-hub

   devhub@example.com

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
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

**`-v`** **|** **`--target-dev-hub TARGET-DEV-HUB`**
Required

Username or alias of the Dev Hub org. Not required if the `target-dev-hub` configuration variable is already set.

Type: option

**`-p`** **|** **`--package PACKAGE`**
Required

Subscriber package version ID (starts with 04t).

Type: option

**`-d`** **|** **`--output-dir OUTPUT-DIR`**
Optional

Path within your Salesforce DX project directory in which to download the metadata. This directory must be empty.

Type: option


Salesforce CLI Command Reference package Commands

Default value: force-app

#### **`package version update`**

Update a package version.

#### Description for package version update

Specify a new value for each option you want to update.

To display details about a package version, run "sf package version display".

#### Examples for package version update

Update the package version that has the specified alias (that contains spaces) with a new installation key "password123"; uses your
default Dev Hub org:

```
   sf package version update --package "Your Package Alias" --installation-key password123

```

Update the package version that has the specified ID with a new branch and tag; use the Dev Hub org with username
devhub@example.com:

```
   sf package version update --package 04t... --branch main --tag 'Release 1.0.7'

   --target-dev-hub devhub@example.com

```

Update the package version that has the specified ID with a new description:

```
   sf package version update --package 04t... --version-description "New Package Version

   Description"

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

**`-v`** **|** **`--target-dev-hub TARGET-DEV-HUB`**
Required

Username or alias of the Dev Hub org. Not required if the `target-dev-hub` configuration variable is already set.

Type: option

```
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option


### Salesforce CLI Command Reference package1 Commands

**`-p`** **|** **`--package PACKAGE`**
Required

ID (starts with 04t) or alias of the package to update a version of.

Type: option

**`-a`** **|** **`--version-name VERSION-NAME`**
Optional

New package version name.

Type: option

**`-e`** **|** **`--version-description VERSION-DESCRIPTION`**
Optional

New package version description.

Type: option

**`-b`** **|** **`--branch BRANCH`**
Optional

New package version branch.

Type: option

**`-t`** **|** **`--tag TAG`**
Optional

New package version tag.

Type: option

**`-k`** **|** **`--installation-key INSTALLATION-KEY`**
Optional

New installation key for key-protected package (default: null)

Type: option

Aliases for **`package version update`**

```
   force:package:version:update

### package1 Commands

```

Commands to develop first-generation managed and unmanaged packages.

package1 version create
Create a first-generation package version in the release org.

package1 version create get
Retrieve the status of a package version creation request.

package1 version display
Display details about a first-generation package version.


Salesforce CLI Command Reference package1 Commands

package1 version list
List package versions for the specified first-generation package or for the org.

#### **`package1 version create`**

Create a first-generation package version in the release org.

#### Description for package1 version create

The package version is based on the contents of the specified metadata package. Omit --managed-released if you want to create an
unmanaged package version.

#### Examples for package1 version create

Create a first-generation package version from the package with the specified ID and name the package version "example"; use your
default org:

```
   sf package1 version create --package-id 033... --name example

```

Same as previous example, but provide a description and wait for 30 minutes for the package version to be created; use the specified
org:

```
   sf package1 version create --package-id 033... --name example --description "example

   description" --wait 30 --target-org myorg@example.com

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

**`-i`** **|** **`--package-id PACKAGE-ID`**
Required

ID of the metadata package (starts with 033) of which you’re creating a new version.


Salesforce CLI Command Reference package1 Commands

Type: option

**`-n`** **|** **`--name NAME`**
Required

Package version name.

Type: option

**`-d`** **|** **`--description DESCRIPTION`**
Optional

Package version description.

Type: option

**`-v`** **|** **`--version VERSION`**
Optional

Package version in major.minor format, for example, 3.2.

Type: option

**`-m`** **|** **`--managed-released`**
Optional

Create a managed package version.

To create a beta version, don’t include this parameter.

Type: boolean

**`-r`** **|** **`--release-notes-url RELEASE-NOTES-URL`**
Optional

Release notes URL.

This link is displayed in the package installation UI to provide release notes for this package version to subscribers.

Type: option

**`-p`** **|** **`--post-install-url POST-INSTALL-URL`**
Optional

Post install URL.

The contents of the post-installation instructions URL are displayed in the UI after installation of the package version.

Type: option

**`-k`** **|** **`--installation-key INSTALLATION-KEY`**
Optional

Installation key for key-protected package (default: null).

Type: option

**`-w`** **|** **`--wait WAIT`**
Optional

Minutes to wait for the package version to be created (default: 2 minutes).

Type: option

Aliases for **`package1 version create`**

```
   force:package1:version:create

```


Salesforce CLI Command Reference package1 Commands

#### **`package1 version create get`**

Retrieve the status of a package version creation request.

#### Examples for package1 version create get

Get the status of the creation request for the package version with the specified ID in your default org:

```
   sf package1 version create get --request-id 0HD...

```

Same as previous example, but use the specified org:

```
   sf package1 version create get --request-id 0HD... --target-org myorg@example.com

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

**`-i`** **|** **`--request-id REQUEST-ID`**
Required

ID of the PackageUploadRequest (starts with 0HD).

Type: option

#### Aliases for package1 version create get

```
   force:package1:version:create:get

#### **`package1 version display`**

```

Display details about a first-generation package version.


Salesforce CLI Command Reference package1 Commands

Examples for **`package1 version display`**

Display details about the first-generation package version with the specified ID in your default org:

```
   sf package1 version display --package-version-id 04t...

```

Same as previous example, but use the specified org:

```
   sf package1 version display --package-version-id 04t... --target-org myorg@example.com

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

**`-i`** **|** **`--package-version-id PACKAGE-VERSION-ID`**
Required

ID (starts with 04t) of the metadata package version whose details you want to display.

Type: option

Aliases for **`package1 version display`**

```
   force:package1:version:display

#### **`package1 version list`**

```

List package versions for the specified first-generation package or for the org.

#### Examples for package1 version list

List all first-generation package versions in your default org:

```
   sf package1 version list

```


### Salesforce CLI Command Reference plugins Commands

List package versions for the specified first-generation package in the specifief org:

```
   sf package1 version list --package-id 033... --target-org myorg@example.com

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

**`-i`** **|** **`--package-id PACKAGE-ID`**
Optional

Metadata package ID (starts with 033) whose package versions you want to list.

If not specified, shows all versions for all packages (managed and unmanaged) in the org.

Type: option

Aliases for **`package1 version list`**

```
   force:package1:version:list

### plugins Commands

```

Find and manage plugins

#### plugins discover

See a list of 3rd-party sf plugins you can install.

#### **`plugins discover`**

See a list of 3rd-party sf plugins you can install.


### Salesforce CLI Command Reference project Commands

Examples for **`plugins discover`**

```
   sf plugins discover

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

### project Commands

Work with projects, such as deploy and retrieve metadata.

project convert mdapi
Convert metadata retrieved via Metadata API into the source format used in Salesforce DX projects.

project convert source
Convert source-formatted files into metadata that you can deploy using Metadata API.

project convert source-behavior (Beta)
Enable a behavior of your project source files, and then update your Salesforce DX project to implement the behavior.

project delete source
Delete source from your project and from a non-source-tracked org.

project delete tracking
Delete all local source tracking information.

project deploy cancel
Cancel a deploy operation.

project deploy pipeline quick (Beta)
Quickly deploy a validated deployment to an org.

project deploy pipeline report (Beta)
Check the status of a pipeline deploy operation.

project deploy pipeline resume (Beta)
Resume watching a pipeline deploy operation.

project deploy pipeline start (Beta)
Deploy changes from a branch to the pipeline stage’s org.

project deploy pipeline validate (Beta)
Perform a validate-only deployment from a branch to the pipeline stage’s org.


Salesforce CLI Command Reference project Commands

project deploy preview
Preview a deployment to see what will deploy to the org, the potential conflicts, and the ignored files.

project deploy quick
Quickly deploy a validated deployment to an org.

project deploy report
Check or poll for the status of a deploy operation.

project deploy resume
Resume watching a deploy operation and update source tracking when the deploy completes.

project deploy start
Deploy metadata to an org from your local project.

project deploy validate
Validate a metadata deployment without actually executing it.

project generate manifest
Create a project manifest that lists the metadata components you want to deploy or retrieve.

project list ignored
Check your local project package directories for forceignored files.

project reset tracking
Reset local and remote source tracking.

project retrieve preview
Preview a retrieval to see what will be retrieved from the org, the potential conflicts, and the ignored files.

project retrieve start
Retrieve metadata from an org to your local project.

#### **`project convert mdapi`**

Convert metadata retrieved via Metadata API into the source format used in Salesforce DX projects.

#### Description for project convert mdapi

To use Salesforce CLI to work with components that you retrieved via Metadata API, first convert your files from the metadata format to
the source format using this command.

To convert files from the source format back to the metadata format, run "sf project convert source".

To convert multiple metadata components, either set multiple --metadata <name> flags or a single --metadata flag with multiple names
separated by spaces. Enclose names that contain spaces in one set of double quotes. The same syntax applies to --source-dir.

#### Examples for project convert mdapi

Convert metadata formatted files in the specified directory into source formatted files; writes converted files to your default package
directory:

```
   $ sf project convert mdapi --root-dir path/to/metadata

```

Similar to previous example, but writes converted files to the specified output directory:

```
   $ sf project convert mdapi --root-dir path/to/metadata --output-dir path/to/outputdir

```


Salesforce CLI Command Reference project Commands

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
   --api-version API-VERSION
```

Optional

Override the api version used for api requests made by this command

Type: option

**`-r`** **|** **`--root-dir ROOT-DIR`**
Required

Root directory that contains the Metadata API–formatted metadata.

Type: option

**`-d`** **|** **`--output-dir OUTPUT-DIR`**
Optional

Directory to store your files in after they’re converted to source format; can be an absolute or relative path.

Type: option

**`-x`** **|** **`--manifest MANIFEST`**
Optional

File path to manifest (package.xml) of metadata types to convert.

If you specify this flag, don’t specify --metadata or --source-dir.

Type: option

**`-p`** **|** **`--metadata-dir METADATA-DIR`**
Optional

Root of directory or zip file of metadata formatted files to convert.

The supplied paths can be to a single file (in which case the operation is applied to only one file) or to a folder (in which case the
operation is applied to all metadata types in the directory and its sub-directories).

If you specify this flag, don’t specify --manifest or --metadata. If the comma-separated list you’re supplying contains spaces, enclose
the entire comma-separated list in one set of double quotes.

Type: option

**`-m`** **|** **`--metadata METADATA`**
Optional

Metadata component names to convert.

Type: option


Salesforce CLI Command Reference project Commands

Aliases for **`project convert mdapi`**

```
   force:mdapi:convert

#### **`project convert source`**

```

Convert source-formatted files into metadata that you can deploy using Metadata API.

#### Description for project convert source

To convert source-formatted files into the metadata format, so that you can deploy them using Metadata API, run this command. Then
deploy the metadata using "sf project deploy".

To convert Metadata API–formatted files into the source format, run "sf project convert mdapi".

To specify a package name that includes spaces, enclose the name in single quotes.

To convert multiple components, either set multiple --metadata <name> flags or a single --metadata flag with multiple names separated
by spaces. Enclose names that contain spaces in one set of double quotes. The same syntax applies to --source-dir.

#### Examples for project convert source

Convert source-formatted files in the specified directory into metadata-formatted files; writes converted files into a new directory:

```
   $ sf project convert source --root-dir path/to/source

```

Similar to previous example, but writes converted files to the specified output directory and associates the files with the specified package:

```
   $ sf project convert source --root-dir path/to/source --output-dir path/to/outputdir

   --package-name 'My Package'

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
   --api-version API-VERSION
```

Optional

API Version to use in the generated project's manifest. By default, will use the version from sfdx-project.json

Override the api version used for api requests made by this command

Type: option

**`-r`** **|** **`--root-dir ROOT-DIR`**
Optional

Source directory other than the default package to convert.


Salesforce CLI Command Reference project Commands

Type: option

**`-d`** **|** **`--output-dir OUTPUT-DIR`**
Optional

Output directory to store the Metadata API–formatted files in.

Type: option

Default value: metadataPackage_1779988371889

**`-n`** **|** **`--package-name PACKAGE-NAME`**
Optional

Name of the package to associate with the metadata-formatted files.

Type: option

**`-x`** **|** **`--manifest MANIFEST`**
Optional

Path to the manifest (package.xml) file that specifies the metadata types to convert.

If you specify this flag, don’t specify --metadata or --source-dir.

Type: option

**`-p`** **|** **`--source-dir SOURCE-DIR`**
Optional

Paths to the local source files to convert.

The supplied paths can be to a single file (in which case the operation is applied to only one file) or to a folder (in which case the
operation is applied to all metadata types in the directory and its sub-directories).

If you specify this flag, don’t specify --manifest or --metadata.

Type: option

**`-m`** **|** **`--metadata METADATA`**
Optional

Metadata component names to convert.

Type: option

#### Aliases for project convert source

```
   force:source:convert

#### project convert source-behavior (Beta)

```

Enable a behavior of your project source files, and then update your Salesforce DX project to implement the behavior.

Note: This feature is a Beta Service. Customers may opt to try such Beta Service in its sole discretion. Any use of the Beta Service
is subject to the applicable Beta Services Terms provided at Agreements and Terms
[(https://www.salesforce.com/company/legal/agreements/).](https://www.salesforce.com/company/legal/agreements/)

#### Description for project convert source-behavior

Specifically, this command updates the "sourceBehaviorOption" option in the "sfdx-project.json" file and then converts the associated
local source files in your project as needed.


Salesforce CLI Command Reference project Commands

For example, run this command with the "--behavior decomposePermissionSetBeta" flag to start decomposing permission sets when
you deploy or retrieve them. Decomposing means breaking up the monolithic metadata API format XML file that corresponds to a
metadata component into smaller XML files and directories based on its subtypes. Permission sets are not decomposed by default; you
must opt-in to start decomposing them by using this command. When the command finishes, your "sfdx-project.json" file is updated
to always decompose permission sets, and the existing permission set files in your local package directories are converted into the new
decomposed format. You run this command only once for a given behavior change.

For more information about the possible values for the --behavior flag, see the "sourceBehaviorOptions" section in the
https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_ws_config.htm topic.

Examples for **`project convert source-behavior`**

Update your Salesforce DX project to decompose custom permission sets:

```
   sf project convert source-behavior --behavior decomposePermissionSetBeta

```

Display what the command would do, but don't change any existing files:

```
   sf project convert source-behavior --behavior decomposePermissionSetBeta --dry-run

```

Keep the temporary directory that contains the interim metadata API formatted files:

```
   sf project convert source-behavior --behavior decomposePermissionSetBeta --dry-run

   --preserve-temp-dir

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

**`-b`** **|** **`--behavior BEHAVIOR`**
Required

Behavior to enable; the values correspond to the possible values of the "sourceBehaviorOption" option in the "sfdx-project.json" file.

Type: option

Permissible values are: decomposeCustomLabelsBeta2, decomposeCustomLabelsBeta, decomposePermissionSetBeta,
decomposePermissionSetBeta2, decomposeSharingRulesBeta, decomposeWorkflowBeta, decomposeExternalServiceRegistrationBeta

```
   --dry-run
```

Optional

Display what the command would do, but don't make any actual changes.

Type: boolean

```
   --preserve-temp-dir
```

Optional


Salesforce CLI Command Reference project Commands

Don't delete the metadata API format temporary directory that this command creates. Useful for debugging.

Type: boolean

**`-o`** **|** **`--target-org TARGET-ORG`**
Optional

Username or alias of the target org.

Type: option

#### **`project delete source`**

Delete source from your project and from a non-source-tracked org.

#### Description for project delete source

Use this command to delete components from orgs that don’t have source tracking. To remove deleted items from orgs that have source
tracking enabled, "sf project deploy start".

When you run this command, both the local source file and the metadata component in the org are deleted.

To delete multiple metadata components, either set multiple --metadata <name> flags or a single --metadata flag with multiple names
separated by spaces. Enclose names that contain spaces in one set of double quotes. The same syntax applies to --source-dir.

#### Examples for project delete source

Delete all local Apex source files and all Apex classes from the org with alias "my-scratch":

```
   sf project delete source --metadata ApexClass --target-org my-scratch

```

Delete a specific Apex class and a Profile that has a space in it from your default org; don't prompt for confirmation:

```
   sf project delete source --metadata ApexClass:MyFabulousApexClass --metadata "Profile: My

    Profile" --no-prompt

```

Run the tests that aren’t in any managed packages as part of the deletion; if the delete succeeds, and the org has source-tracking enabled,
update the source tracking information:

```
   sf project delete source --metadata ApexClass --test-level RunLocalTests --track-source

```

Delete the Apex source files in a directory and the corresponding components from your default org:

```
   sf project delete source --source-dir force-app/main/default/classes

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


Salesforce CLI Command Reference project Commands

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

**`-c`** **|** **`--check-only`**
Optional

Validate delete command but don't delete anything from the org or the local project.

IMPORTANT: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Validates the deleted metadata and runs all Apex tests, but prevents the deletion from being saved to the org.

If you change a field type from Master-Detail to Lookup or vice versa, that change isn’t supported when using the --check-only flag
to test a deletion (validation). This kind of change isn’t supported for test deletions to avoid the risk of data loss or corruption. If a
change that isn’t supported for test deletions is included in a deletion package, the test deletion fails and issues an error.

If your deletion package changes a field type from Master-Detail to Lookup or vice versa, you can still validate the changes prior to
deploying to Production by performing a full deletion to another test Sandbox. A full deletion includes a validation of the changes
as part of the deletion process.

Note: A Metadata API deletion that includes Master-Detail relationships deletes all detail records in the Recycle Bin in the following
cases.

1. For a deletion with a new Master-Detail field, soft delete (send to the Recycle Bin) all detail records before proceeding to delete
the Master-Detail field, or the deletion fails. During the deletion, detail records are permanently deleted from the Recycle Bin and
cannot be recovered.

2. For a deletion that converts a Lookup field relationship to a Master-Detail relationship, detail records must reference a master
record or be soft-deleted (sent to the Recycle Bin) for the deletion to succeed. However, a successful deletion permanently deletes
any detail records in the Recycle Bin.

Type: boolean

**`-w`** **|** **`--wait WAIT`**
Optional

Number of minutes to wait for the command to finish.

If the command continues to run after the wait period, the CLI returns control of the terminal window to you.

Type: option

Default value: 33 minutes

```
   --tests TESTS
```

Optional

Apex tests to run when --test-level is RunSpecifiedTests.

If a test name contains a space, enclose it in double quotes.

For multiple test names, use one of the following formats:


Salesforce CLI Command Reference project Commands

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

      - RunRelevantTests (Beta) — Runs only tests that are relevant to the files being deployed. Salesforce automatically identifies the
relevant tests based on an analysis of the deployment payload and the payload dependencies. For fine-grained control, you can also
annotate test classes so that they always run in certain conditions. See "@IsTest Annotation" in the "Apex Developer Guide"
