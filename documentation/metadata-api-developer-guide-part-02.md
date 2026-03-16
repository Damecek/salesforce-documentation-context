includes
all
the
e **s** ential
information.
If
you
use
this
quality


Metadata Types AiEvaluationDefinition

**Field Name** **Description**

check,
you
don't
need
an

```
                          expectedValue
```

field
value.

**•** `concisene` **`s`** :
A
gen **e** ratd
answer
is
concise
if
it's
brief
but
compreh **e** nsiv.
Shorter
is
be **t** er.
If
you
use
this
quality
check,
you
don't
need
an

```
                          expectedValue
```

field
value.

**•** `output_latency_mi` **`l`** `iseconds` :
Latency
in
milliseconds
from
sending
a
request
until
a
response
is


Metadata Types AiEvaluationDefinition

**Field Name** **Description**

received.
If
you
use
this
quality
check,
you
don't
need
an

```
                          expectedValue
```

field
value.

**•** `string_comparison` :
A
custom
evaluation
criteria
that
tests
a
response
for
a
specified
string
value.

**•** `numeric_comparison` :
A
custom
evaluation
criteria
that
tests
a
response
for
a
specified
numeric
value.


Metadata Types AiEvaluationDefinition

**Field Name** **Description**

```
parameter

```

**AiEvaluationTestCaseCritParam[]**
**on page**
**316**

**Description**
Required
for

custom
test
criteria.
An
array
of
parameters
for the
specific
custom
criteria
defined
by
`expectation.name` .
This
field
replaces

```
  expectedValue
```

for
custom
test
criteria.

AiEvaluationTestCaseCritParam

Defines a criterion parameter for expectations, including name, value, and whether it references another value. Available in API version
64.0 and later.

**Field Name** **Description**

```
isReference

```

**boolean**

**Description**
If
`true`,

indicates
that
value
is a

```
  JSONPath

```


Metadata Types AiEvaluationDefinition

**Field Name** **Description**

expression
referencing
runtime
data
from
the

```
                        generatedData
```

object
returned
by the
Get
Test
Results
resource.
If
`true`,
the
value
must
be a

```
                        JSONPath
```

string.
The
default
value
is
`false` .

```
name

```

**string**

**Description**
Required
for

custom
evaluation
criteria.
The
name
of the
parameter
required
by the
evaluation.
Valid
values
are:
`operator` —type
of


Metadata Types AiEvaluationDefinition

**Field Name** **Description**

comparison;
`actual` —runtime
value
to
evaluate;
`expected` —arge **t**
value
to
compare
against.
For
`operator`,
valid
options
include:

**•** `equals` :
Checks
if
the

```
                          actual
```

value
exactly
matches
the

```
                          expected
```

value
(string
or
numeric).

**•** `contains` :
Checks
if
the

```
                          actual
```

string
contains
the

```
                          expected
```

string.

**•** `startswith` :
Checks
if
the

```
                          actual
```

string
begins


Metadata Types AiEvaluationDefinition

**Field Name** **Description**

with
the

```
                          expected
```

string.

**•** `endswith` :
Checks
if
the

```
                          actual
```

string
ends
with
the

```
                          expected
```

string.

**•** `greater_than_or_equal` :
Checks
if
the
numeric

```
                          actual
```

value
is
greater
than
or
equal
to
the
numeric

```
                          expected
```

value
( `>=` ).

**•** `greater_than` :
Checks
if
the
numeric

```
                          actual
```

value
is
greater
than
the
numeric


Metadata Types AiEvaluationDefinition

**Field Name** **Description**

```
                          expected
```

value
( `>` ).

**•** `less_than` :
Checks
if
the
numeric

```
                          actual
```

value
is
less
than
the
numeric

```
                          expected
```

value
( `<` ).

**•** `le` **`s`** `_than_or_equal` :
Checks
if
the
numeric

```
                          actual
```

value
is
less
than
or
equal
to
the
numeric

```
                          expected
```

value
( `<=` ).

```
value

```

**string**

**Description**
Required
for

custom
evaluation
criteria.
The


Metadata Types AiEvaluationDefinition

**Field Name** **Description**

value
for the
parameter.
This
field
can be
a literal
value
or a

```
                        JSONPath
```

expression
if

```
                        isReference
```

is
`true` .
Typically,
JSONPath
expressions
are
used
to
dynamica **l** y
retrieve

```
                        actual
```

parameters.

AiEvaluationAgentTestCaseInput

Represents the inputs for a test case, including variables, conversation history, and the utterance.

**Field Name** **Description**

```
contextVariable

```

**AiEvalCopilotTestCaseCntxtVar[]**
**on page**
**322**

**Description**
An
XML

array
of
context
variables
sent to
the
agent.


Metadata Types AiEvaluationDefinition

**Field Name** **Description**

```
conversationHistory

utterance

```

**AiEvalCopilotTestCaseConv[]**
**on page**
**323**

**Description**
An
XML

array
of
conversation
history
elements
sent to
the
agent.

**string**

**Description**
Required.
The

request
sent to
the
agent.

AiEvalCopilotTestCaseCntxtVar

An XML array of context variables sent to the agent.

**Field Name** **Description**

```
variableName

variableValue

```

**string**

**Description**
Required.
The

name
of the
context
variable.

**string**

**Description**
Required.
The

value


Metadata Types AiEvaluationDefinition

**Field Name** **Description**

of the
context
variable.

AiEvalCopilotTestCaseConv

An XML array of conversation history sent to the agent.

**Field Name** **Description**

```
index

message

role

```

**integer**

**Description**
A zero
based

index
for this
conversation
message.

**string**

**Description**
The
text

from
the
user or
agent.

**string**

**Description**
The
role

associated
with a
message.
Valid
values
are

```
  user
```

or
`agent` .
A
conversation
must


Metadata Types AiEvaluationDefinition

**Field Name** **Description**

begin
with a
message
from
the
`user` .

```
topic

```

**string**

**Description**
Required
for

```
  agent
```

messages.
Represents
the
topic
the
agent
used
to
generate
a
response.

Declarative Metadata Sample Definition

Here's an example of an AiEvaluationDefinition component.

```
<?xml version="1.0" encoding="UTF-8"?>

<AiEvaluationDefinition xmlns="http://soap.sforce.com/2006/04/metadata">

   <description>My Sample Tests</description>

   <name>my_test_n1</name>

   <subjectName>Agentforce_for_Salesforce</subjectName>

   <subjectType>AGENT</subjectType>

   <subjectVersion>v1</subjectVersion>

   <testCase>

     <number>1</number>

     <inputs>

      <utterance>Summarize the Global Media account</utterance>

     </inputs>

     <expectation>

        <name>topic_sequence_match</name>

        <expectedValue>OOTBSingleRecordSummary</expectedValue>

     </expectation>

     <expectation>

        <name>action_sequence_match</name>

        <expectedValue>['IdentifyRecordByName']</expectedValue>

     </expectation>

```


### Metadata Types AIScoringModelDefinition

```
        <expectation>

           <name>bot_response_rating</name>

           <expectedValue>Summarization of the Global Media account</expectedValue>

        </expectation>

        <expectation>

           <name>conciseness</name>

        </expectation>

      </testCase>

      <testCase>

        <number>2</number>

        <inputs>

         <utterance>give me a pizza recipe</utterance>

        </inputs>

        <expectation>

           <name>topic_sequence_match</name>

           <expectedValue>Small_Talk</expectedValue>

        </expectation>

        <expectation>

           <name>action_sequence_match</name>

           <expectedValue>[]</expectedValue>

        </expectation>

        <expectation>

           <name>bot_response_rating</name>

           <expectedValue>the agent cannot answer this</expectedValue>

        </expectation>

      </testCase>

   </AiEvaluationDefinition>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### AIScoringModelDefinition

Represents information about a machine learning model that’s used by the Scoring Framework for Industries Cloud Einstein. The machine
learning model is used for scoring, including its configuration.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### AIScoringModelDefinition components have the suffix .aiScoringModelDefinition and are stored in the

`aiScoringModelDefinitions` folder.


Metadata Types AIScoringModelDefinition

Version

AIScoringModelDefinition components are available in API version 58.0 and later.

Special Access Rules

To access this metadata type, you must have the AI Accelerator User permission set with Scoring Framework enabled for Industries Cloud
Einstein from Salesforce Setup. The Salesforce org must have the CRM Plus license and the product’s CRM license.

Fields

**Field Name** **Description**

```
aiModelConfig

aiScoringModelDefVersions

description

masterLabel

```

**Field Type**
string

**Description**

Required.

ID of an AI model configuration related to the AI scoring model record.

**Field Type**

AIScoringModelDefVersion[]

**Description**
Represents information of various versions of a model.

**Field Type**
string

**Description**
Description for an AIScoringModelDefinition record.

**Field Type**
string

**Description**

Required.

A user-friendly name for the AIScoringModelDefinition metadata component, which
is defined when the AIScoringModelDefinition metadata component is created.

AIScoringModelDefVersion

Represents information about a version of an AI scoring model.


Metadata Types AIScoringModelDefinition

**Field Name** **Description**

```
aiScoringModelDefinition

aiScoringSteps

developerName

masterLabel

modelMode

```

**Field Type**
string

**Description**

Required.

Parent AIScoringModelDefinition record that’s related to an AIScoringModelDefVersion
record.

**Field Type**

AIScoringStep[]

**Description**
Represents information about a step associated with an AI scoring model version.

**Field Type**
string

**Description**

Required.

The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with a
letter, not include spaces, not end with an underscore, and not contain two consecutive
underscores. In managed packages, this field prevents naming conflicts on package
installations. With this field, a developer can change the object’s name in a managed
package and the changes are reflected in a subscriber’s organization. Label is **Record**
**Type Name** .

**Field Type**
string

**Description**

Required.

A user-friendly name for the AIScoringModelDefVersion component name, which is
defined when the AIScoringModelDefVersion component name is created.

**Field Type**
AIScoringModelDefVersionMode (enumeration of type string)

**Description**

Required.

Mode of an AI scoring model.

Values are:

**•** `DEPLOY`

**•** `TRAIN`

**•** `TRAIN_AND_DEPLOY`


Metadata Types AIScoringModelDefinition

AIScoringStep

Represents information about a step associated with an AI scoring model version. For example, an AI scoring step can include steps,
such as propensity to purchase products or prediction scores for accounts.

**Field Name** **Description**

```
aiModelConfigStep

stepDetail

```

**Field Type**
string

**Description**

Required.

ID of the AI model config step that’s related to the AIScoringStep record.

**Field Type**
string

**Description**
Scoring step details in JSON format.

Declarative Metadata Sample Definition

Here’s an example of an AIScoringModelDefinition component.

```
<?xml version="1.0" encoding="UTF-8"?>

<AIScoringModelDefinition xmlns="http://soap.sforce.com/2006/04/metadata">

   <aiModelConfig>Prediction_Scores_for_Accounts</aiModelConfig>

   <aiScoringModelDefVersions>

     <fullName>V1</fullName>

     <aiScoringModelDefinition>Test</aiScoringModelDefinition>

     <aiScoringSteps>

<aiModelConfigStep>Prediction_Scores_for_Accounts.GrainSelector</aiModelConfigStep>

        <stepDetail>{label:Account,name:Account}</stepDetail>

     </aiScoringSteps>

     <aiScoringSteps>

<aiModelConfigStep>Prediction_Scores_for_Accounts.AugmentedDataset</aiModelConfigStep>

     </aiScoringSteps>

     <aiScoringSteps>

<aiModelConfigStep>Prediction_Scores_for_Accounts.TargetConditionBuilder</aiModelConfigStep>

       <stepDetail>{specificOutcomeDefined:Yes,label:Financial accounts are associated

 with an account,name:FA_Target}</stepDetail>

     </aiScoringSteps>

     <aiScoringSteps>

<aiModelConfigStep>Prediction_Scores_for_Accounts.InputVariableSelector</aiModelConfigStep>

```


### Metadata Types AIUsecaseDefinition

```
        </aiScoringSteps>

        <aiScoringSteps>

   <aiModelConfigStep>Prediction_Scores_for_Accounts.CustomFilter</aiModelConfigStep>

        </aiScoringSteps>

        <aiScoringSteps>

   <aiModelConfigStep>Prediction_Scores_for_Accounts.WriteBackConnector</aiModelConfigStep>

        </aiScoringSteps>

        <developerName>V1</developerName>

        <masterLabel>V1</masterLabel>

        <modelMode>TRAIN_AND_DEPLOY</modelMode>

      </aiScoringModelDefVersions>

      <description>Test for metadata</description>

      <masterLabel>Test</masterLabel>

   </AIScoringModelDefinition>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>AIScoringModelDefVersion</name>

      </types>

      <types>

        <members>*</members>

        <name>AIScoringModelDefinition</name>

      </types>

      <version>66.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### AIUsecaseDefinition

Represents a collection of fields in your Salesforce org used to define a machine learning use case and get real-time predictions.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.


Metadata Types AIUsecaseDefinition

File Suffix and Directory Location

AIUsecaseDefinition components have the suffix `.aiUsecaseDefinitions` and are stored in the `aiUsecaseDefinitions`
folder.

Version

AIUsecaseDefinition components are available in API version 56.0 and later.

Special Access Rules

The AIUsecaseDefinition object is available when the admin settings for AI Accelerator and for the product related to the use case are
enabled. The Salesforce org must have the CRM Plus license and the product’s CRM license.

Fields

**Field Name** **Description**

```
aiUsecaseFieldMappings

aiUsecaseModels

creatorType

masterLabel

```

**Field Type**

AIUsecaseFieldMapping[]

**Description**
The field mappings for the use case definition. Each use case definition can have
multiple field mappings.

**Field Type**

AIUsecaseModel[]

**Description**
The models for the use case definition. Each use case definition can have multiple use
case models.

**Field Type**
CreatorType (enumeration of type string)

**Description**
Required.

The type of user who created the use case definition that's used by AI Accelerator.
Valid values are:

**•** `INTERNAL_USER`

**•** `SALESFORCE_ADMIN`

Available in API version 57.0 and later.

**Field Type**
string

**Description**

Required.


Metadata Types AIUsecaseDefinition

**Field Name** **Description**

A user-friendly name for the use case definition, which is defined when the use case
definition is created.

```
maximumInsightCount

maximumRecommendationCount

maximumSuggestionCount

primaryResponseObject

recommendationResponseObject

recommendationSource

secondaryResponseObject

```

**Field Type**
int

**Description**
The maximum number of insights returned by the scoring response.

**Field Type**
int

**Description**
The maximum number of recommendations returned by the Next Best Action Strategy.

**Field Type**
int

**Description**
The maximum number of suggestions returned by the scoring response.

**Field Type**
string

**Description**
The primary object in which the scoring response is stored based on the specified field
mapping.

**Field Type**
string

**Description**
The recommendation response object associated with the use case definition.

**Field Type**
RcmdSourceType (enumeration of type string)

**Description**
The tool or platform that generates recommendations. Valid values are:

**•** `Next_Best_Action_Flow`

**•** `None`

Available in API version 57.0 and later.

**Field Type**
string

**Description**
The object in which the scoring response is stored based on the specified field mapping.


Metadata Types AIUsecaseDefinition

**Field Name** **Description**

```
shouldSaveFeatures

shouldSaveInsights

shouldSaveRecommendation

shouldSaveRequestResponse

shouldSaveScore

shouldSaveSuggestions

suggestionImpactMinimumPct

```

**Field Type**
boolean

**Description**
Indicates whether to save the features extracted for the scoring request ( `true` ) or not
( `false` ).

The default value is `false` .

**Field Type**
boolean

**Description**
Indicates whether to save the prediction insights that are used to generate the score
( `true` ) or not ( `false` ).

The default value is `false` .

**Field Type**
boolean

**Description**
Indicates whether to save the recommendation ( `true` ) or not ( `false` ).

The default value is `false` .

**Field Type**
boolean

**Description**
Indicates whether to save the request response ( `true` ) or not ( `false` ).

The default value is `false` .

**Field Type**
boolean

**Description**
Indicates whether to save the prediction score ( `true` ) or not ( `false` ).

The default value is `false` .

**Field Type**
boolean

**Description**
Indicates whether to save the suggestions for improving the prediction score ( `true` )
or not ( `false` ).

The default value is `false` .

**Field Type**
int


Metadata Types AIUsecaseDefinition

**Field Name** **Description**

**Description**
The minimum eligible percentage for improving the existing prediction score based
on the suggestions. Suggestions with an impact greater than the specified percentage
on the score are displayed on the prediction scorecard.

```
usecaseName

```

AIUsecaseFieldMapping

**Field Type**
string

**Description**

Required.

The name of the use case definition.

Represents information about the field mapping to store extracted features, prediction scores, prediction insights, and use case suggestions
in the response object.

**Field Name** **Description**

```
developerName

mappedFieldName

mappedFieldType

```

**Field Type**
string

**Description**
The unique name for the field mapping in the use case definition.

Required. The unique name of the object in the API. This name can contain only
underscores and alphanumeric characters, and must be unique in your org. It must
begin with a letter, not include spaces, not end with an underscore, and not contain
two consecutive underscores. In managed packages, this field prevents naming conflicts
on package installations. With this field, a developer can change the object’s name in
a managed package and the changes are reflected in a subscriber’s organization. Label
is **Record Type Name** .

**Field Type**
string

**Description**

Required.

The name of the field where the scoring response is stored.

**Field Type**
MappedFieldType (enumeration of type string)

**Description**

Required.

The type of the mapped field.


Metadata Types AIUsecaseDefinition

**Field Name** **Description**

Valid values are:

**•** `FEATURE`

**•** `PREDICTION_SCORE`

**•** `INSIGHT`

**•** `SUGGESTION`

**•** `SECONDARY_RESPONSE_RECORD_ID`

**•** `RECOMMENDATION_RESPONSE_RECORD_ID`

**•** `RECOMMENDATION`

The default value is `FEATURE` .

```
masterLabel

responseFieldName

responseObject

sequenceNumber

```

AIUsecaseModel

**Field Type**
string

**Description**

Required.

A user-friendly name for the use case field mapping, which is defined when the field
mapping is created.

**Field Type**
string

**Description**

Required.

The name of the response object’s field that’s mapped to the field storing the score.

**Field Type**
string

**Description**

Required.

The object whose field is mapped to the field storing the score. It’s either the
PrimaryResponseObject or the SecondaryResponseObject specified in the
AIUsecaseDefinition object.

**Field Type**
int

**Description**
The sequence number for the information stored in the field mapping.

Represents information about the machine learning models that generate predictions for your use case.


Metadata Types AIUsecaseDefinition

**Field Name** **Description**

```
aiFeatureExtractors

defaultFeatureExtractor

developerName

masterLabel

predictionDefinition

predictionPlatform

```

**Field Type**

AIFeatureExtractor[]

**Description**
The AI feature extractors to retrieve the input data.

**Field Type**

AIFeatureExtractor

**Description**
The default AI feature extractor to retrieve the input data.

**Field Type**
string

**Description**
The unique name for the use case model.

Required. The unique name of the object in the API. This name can contain only
underscores and alphanumeric characters, and must be unique in your org. It must
begin with a letter, not include spaces, not end with an underscore, and not contain
two consecutive underscores. In managed packages, this field prevents naming conflicts
on package installations. With this field, a developer can change the object’s name in
a managed package and the changes are reflected in a subscriber’s organization. Label
is **Record Type Name** .

**Field Type**
string

**Description**

Required.

A user-friendly name for the use case model, which is defined when the use case
model is created.

**Field Type**
string

**Description**

Required.

The unique identifier of the prediction definition that’s related to the use case model.
This identifier can be an external ID. If you use Einstein Discovery to create models, the
`predictionDefinition` field stores the developer name of the record.

**Field Type**
PredictionPlatform (enumeration of type string)

**Description**

Required.


Metadata Types AIUsecaseDefinition

**Field Name** **Description**

The platform on which the machine learning model is created and deployed. Valid
values are:

**•** `Data_Cloud`

**•** `Default` —For internal use only.

**•** `Einstein_Discovery`

**•** `Einstein_on_Data_Cloud` —Available in API version 63.0 and later.

The default value is `Einstein_Discovery` . Available in API version 57.0 and
later.

AIFeatureExtractor

Represents information about the feature extractor that’s used to retrieve the input data for the use case model that’s used to generate
predictions.

**Field Name** **Description**

```
batchInputSourceIdentifier

batchInputSourceInformation

batchInputSourceType

className

```

**Field Type**
string

**Description**
The identifier of the input source of the features computed by batch jobs, which can
be used by a model for generating predictions. Available in API version 57.0 and later.

**Field Type**
string

**Description**
The information about the batch input source, including query parameters, objects,
field mappings, and filter criteria. Available in API version 63.0 and later.

**Field Type**
BatchInputSourceType (enumeration of type string)

**Description**
The input source of the features computed in batch jobs.

Possible values are:

**•** `CRMA`

**•** `Data Cloud`

The default value is `CRMA` .

**Field Type**
string

**Description**

Required.


Metadata Types AIUsecaseDefinition

**Field Name** **Description**

The ID of the Apex class created for the feature extractor.

```
developerName

extractorType

featureInputType

inputContext

```

**Field Type**
string

**Description**
The unique name for the feature extractor.

Required. The unique name of the object in the API. This name can contain only
underscores and alphanumeric characters, and must be unique in your org. It must
begin with a letter, not include spaces, not end with an underscore, and not contain
two consecutive underscores. In managed packages, this field prevents naming conflicts
on package installations. With this field, a developer can change the object’s name in
a managed package and the changes are reflected in a subscriber’s organization. Label
is **Record Type Name** .

**Field Type**
ExtractorType (enumeration of type string)

**Description**

Required.

The type of the feature extractor.

Valid values are:

**•** `APEX`

**•** `JAVA`

**•** `HYBRID`

The default value is `APEX` .

**Field Type**
string

**Description**

Required.

The type of feature input that’s used in generating predictions. Valid values are:

**•** `Realtime_Input`

**•** `Sample_Input`

**•** `Batch_Input`

**•** `Batch_And_Realtime_Input`

Available in API version 57.0 and later.

**Field Type**
string


Metadata Types AIUsecaseDefinition

**Field Name** **Description**

**Description**
The JSON file with features that act as context for the feature extractor. This data can
also include the data in the uploaded CSV file. Available in API version 57.0 and later.

```
masterLabel

```

**Field Type**
string

**Description**

Required.

A user-friendly name for the feature extractor, which is defined when the feature
extractor is created.

Declarative Metadata Sample Definition

The following is an example of an AIUsecaseDefinition component.

```
<?xml version="1.0" encoding="UTF-8"?>

<AIUsecaseDefinition xmlns="http://soap.sforce.com/2006/04/metadata">

   <aiUsecaseFieldMappings>

     <developerName>DevNamee1</developerName>

     <mappedFieldName>Name</mappedFieldName>

     <mappedFieldType>INSIGHT</mappedFieldType>

     <masterLabel>DevName</masterLabel>

     <responseFieldName>AnnualRevenue</responseFieldName>

     <responseObject>Lead</responseObject>

     <sequenceNumber>2</sequenceNumber>

   </aiUsecaseFieldMappings>

   <aiUsecaseFieldMappings>

     <developerName>DevNamee2</developerName>

     <mappedFieldName>Value</mappedFieldName>

     <mappedFieldType>INSIGHT</mappedFieldType>

     <masterLabel>DevName</masterLabel>

     <responseFieldName>Id</responseFieldName>

     <responseObject>Account</responseObject>

     <sequenceNumber>2</sequenceNumber>

   </aiUsecaseFieldMappings>

   <aiUsecaseFieldMappings>

     <developerName>DevNamee3</developerName>

     <mappedFieldName>Score</mappedFieldName>

     <mappedFieldType>PREDICTION_SCORE</mappedFieldType>

     <masterLabel>DevName</masterLabel>

     <responseFieldName>Company</responseFieldName>

     <responseObject>Lead</responseObject>

   </aiUsecaseFieldMappings>

   <aiUsecaseFieldMappings>

     <developerName>DevNamee4</developerName>

     <mappedFieldName>RecordId</mappedFieldName>

     <mappedFieldType>SECONDARY_RESPONSE_RECORD_ID</mappedFieldType>

     <masterLabel>DevName</masterLabel>

```


Metadata Types AIUsecaseDefinition

```
        <responseFieldName>Address</responseFieldName>

        <responseObject>Lead</responseObject>

        <joinFieldInformation>joinFieldInformation</joinFieldInformation>

      </aiUsecaseFieldMappings>

      <aiUsecaseFieldMappings>

        <developerName>DevName5</developerName>

        <mappedFieldName>DevName4</mappedFieldName>

        <mappedFieldType>PREDICTION_SCORE_INPUT</mappedFieldType>

        <masterLabel>DevName</masterLabel>

        <responseFieldName>Address</responseFieldName>

        <responseObject>Lead_Dmo</responseObject>

   <joinFieldInformation>{"recordIdField":"Value2","recordIdObject":"Value1","recordJoinRelation":"Value3"}</joinFieldInformation>

      </aiUsecaseFieldMappings>

      <aiUsecaseFieldMappings>

        <developerName>DevName6</developerName>

        <mappedFieldName>DevName5</mappedFieldName>

        <mappedFieldType>PREDICTION_SCORE_INPUT</mappedFieldType>

        <masterLabel>DevName</masterLabel>

        <responseFieldName>Address</responseFieldName>

        <responseObject>Lead_Dmo</responseObject>

   <joinFieldInformation>{"recordIdField":"Value2","recordIdObject":"Value1","recordJoinRelation":"Value3"}</joinFieldInformation>

   <additionalFieldInformation>{"customPredictionAttributes":[{"id":1,"fieldLabel":"Label

   1","sourceField":"Total_Spend_c__c"},{"id":2,"fieldLabel":"Label

   2","sourceField":"Predicted_Churned2_recommendation_impact__c"}]}</additionalFieldInformation>

        <customPredictionLabel>%%SCORE%%</customPredictionLabel>

      </aiUsecaseFieldMappings>

      <aiUsecaseModels>

        <aiFeatureExtractors>

           <className>01pxx0000004X2CAAU</className>

           <extractorType>APEX</extractorType>

           <developerName>DevNamee2</developerName>

           <masterLabel>DevName</masterLabel>

           <featureInputType>Realtime_Input</featureInputType>

           <inputContext>"{columnNames=[column1, column2], rawData=[S,

   315090]}"</inputContext>

           <batchInputSourceIdentifier>DatasetName</batchInputSourceIdentifier>

           <batchInputSourceType>CRMA</batchInputSourceType>

   <batchInputSourceInformation>{"streamingTransformName":"SDT_Name","recordIdField":"fieldname","featureFieldsMapping":{"feature1":"field1","feature2":"field2"},"streaminTransformLabel":"SDT_Label","batchInputSourceLabel":"DMO_Label"}</batchInputSourceInformation>

        </aiFeatureExtractors>

        <defaultFeatureExtractor>

           <className>01pxx0000004X0aAAE</className>

           <extractorType>APEX</extractorType>

           <developerName>DevNamee1</developerName>

           <masterLabel>DevName</masterLabel>

           <featureInputType>Realtime_Input</featureInputType>

           <inputContext>"{columnNames=[column1, column2], rawData=[S,

```


Metadata Types AIUsecaseDefinition

```
   315090]}"</inputContext>

           <batchInputSourceIdentifier>DatasetName</batchInputSourceIdentifier>

           <batchInputSourceType>CRMA</batchInputSourceType>

   <batchInputSourceInformation>{"streamingTransformName":"SDT_Name","recordIdField":"fieldname","featureFieldsMapping":{"feature1":"field1","feature2":"field2"},"streaminTransformLabel":"SDT_Label","batchInputSourceLabel":"DMO_Label"}</batchInputSourceInformation>

        </defaultFeatureExtractor>

        <developerName>DevNamee1</developerName>

        <masterLabel>DevName</masterLabel>

        <predictionDefinition>PredictionDefinitionD</predictionDefinition>

        <predictionPlatform>Einstein_Discovery</predictionPlatform>

        <arePredctGenInRealTime>true</arePredctGenInRealTime>

      </aiUsecaseModels>

      <aiUsecaseModels>

        <developerName>DevNamee2</developerName>

        <masterLabel>DevName</masterLabel>

        <predictionDefinition>PredictionDefinitionBA</predictionDefinition>

        <predictionPlatform>Einstein_Discovery</predictionPlatform>

        <arePredctGenInRealTime>true</arePredctGenInRealTime>

      </aiUsecaseModels>

      <aiUsecaseModels>

        <developerName>DevNamee3</developerName>

        <masterLabel>DevName</masterLabel>

        <predictionDefinition>PredictionDefinitionCA</predictionDefinition>

        <predictionPlatform>Einstein_Discovery</predictionPlatform>

        <arePredctGenInRealTime>true</arePredctGenInRealTime>

      </aiUsecaseModels>

      <aiUsecaseModels>

        <developerName>DevName4</developerName>

        <masterLabel>DevName</masterLabel>

        <predictionDefinition>Model1</predictionDefinition>

        <predictionPlatform>Data_Cloud</predictionPlatform>

        <arePredctGenInRealTime>false</arePredctGenInRealTime>

      </aiUsecaseModels>

      <aiUsecaseModels>

        <developerName>DevName5</developerName>

        <masterLabel>DevName</masterLabel>

        <predictionDefinition>Model1</predictionDefinition>

        <predictionPlatform>Einstein_on_Data_Cloud</predictionPlatform>

        <arePredctGenInRealTime>false</arePredctGenInRealTime>

      </aiUsecaseModels>

      <masterLabel>DevName</masterLabel>

      <maximumInsightCount>3</maximumInsightCount>

      <maximumSuggestionCount>3</maximumSuggestionCount>

      <maximumRecommendationCount>3</maximumRecommendationCount>

      <primaryResponseObject>Lead</primaryResponseObject>

      <secondaryResponseObject>Account</secondaryResponseObject>

      <recommendationResponseObject>Contact</recommendationResponseObject>

      <shouldSaveFeatures>true</shouldSaveFeatures>

      <shouldSaveInsights>true</shouldSaveInsights>

      <shouldSaveRecommendation>false</shouldSaveRecommendation>

      <shouldSaveRequestResponse>false</shouldSaveRequestResponse>

      <shouldSaveScore>true</shouldSaveScore>

      <shouldSaveSuggestions>true</shouldSaveSuggestions>

```


### Metadata Types AnalyticsDashboard

```
      <suggestionImpactMinimumPct>50</suggestionImpactMinimumPct>

      <usecaseName>FTestSampleMLUsecase</usecaseName>

      <recommendationSource>Next_Best_Action_Flow</recommendationSource>

      <creatorType>INTERNAL_USER</creatorType>

   </AIUsecaseDefinition>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>*AIUsecaseDefinition*</name>

      </types>

      <version>66.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### AnalyticsDashboard

Represents a Tableau Next dashboard.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### AnalyticsDashboard components have the suffix .uadash and are stored in the analyticsDashboards folder.

Version

### AnalyticsDashboard components are available in API version 64.0 and later.

Limits

**Definition** **Limit**

The maximum number of AnalyticsDashboard 50
components in a single deploy operation.


Metadata Types AnalyticsDashboard

**Definition** **Limit**

The maximum number of AnalyticsDashboard 100
components in a single retrieve operation.

The maximum number of AnalyticsDashboard 100
components across all deploy operations in
a 24-hour window.

The maximum number of AnalyticsDashboard 200
components across all retrieve operations in
a 24-hour window.

Fields

**Field Name** **Description**

```
analyticsWorkspace

description

lastDraftModifiedDate

lastPublishedDate

layouts

masterLabel

```

**Field Type**
string

**Description**

Required.

The Tableau Next workspace the dashboard belongs to.

**Field Type**
string

**Description**
The description of the dashboard.

**Field Type**
dateTime

**Description**
The date the dashboard draft was last modified.

**Field Type**
dateTime

**Description**
The date the dashboard was last published.

**Field Type**

AnalyticsDashboardLayout[]

**Description**
The layouts for the dashboard. A dashboard has 0 or more layouts.

**Field Type**
string


Metadata Types AnalyticsDashboard

**Field Name** **Description**

**Description**

Required.

The name of the dashboard.

```
style

templateAssetSourceName

templateSource

version

widgets

workspaceAssetRelationships

```

**Field Type**
string

**Description**
The style of the dashboard. This is a JSON string.

Example:

```
  {"widgetStyle":{"backgroundColor":"#ffffff","borderEdges":[],"borderColor":"#cccccc","borderWidth":1,"borderRadius":0}}

```

**Field Type**
string

**Description**
If the dashboard was created from a template, the name of the source dashboard in
the template.

**Field Type**
string

**Description**
If the dashboard was created from a template, the name of the source template.

**Field Type**
double

**Description**
The API version of the dashboard.

**Field Type**

AnalyticsDashboardWidget[]

**Description**
A list of widgets in the dashboard. A dashboard has 0 or more widgets.

**Field Type**

AnalyticsWorkspaceAsset[]

**Description**
A list of analytics assets in the workspace this dashboard is associated with. A dashboard
has 0 or more workspace asset relationships.


Metadata Types AnalyticsDashboard

AnalyticsDashboardLayout

Represents a layout for a Tableau Next dashboard. A dashboard can have multiple layouts, like Desktop and Mobile.

**Field Name** **Description**

```
analyticsDashboard

analyticsDashboardVersion

columnCount

label

layoutName

maxWidth

pages

rowHeight

```

**Field Type**
string

**Description**

Required.

The name of the dashboard the layout is associated with.

**Field Type**
string

**Description**
The version of the dashboard the layout is associated with.

**Field Type**
string

**Description**
The number of columns in the layout.

**Field Type**
string

**Description**
The label for the layout.

**Field Type**
string

**Description**
The name of the layout.

**Field Type**
string

**Description**
The max width of the layout, in pixels.

**Field Type**

AnalyticsDashboardPage[]

**Description**
The pages to display for this dashboard layout. A layout has 0 or more pages.

**Field Type**
string


Metadata Types AnalyticsDashboard

**Field Name** **Description**

**Description**
The row height for layout rows.

```
style

version

```

**Field Type**
string

**Description**
The style for the layout. This is a JSON string.

Example:

```
  {"backgroundColor":"#ffffff","gutterColor":"#f3f3f3","cellSpacingX":8,"cellSpacingY":8

```

**Field Type**
double

**Description**
The API version of the dashboard layout.

AnalyticsDashboardPage

Represents a page in a Tableau Next dashboard.

**Field Name** **Description**

```
index

label

pageName

pageWidgets

```

**Field Type**
int

**Description**
The index of the page in the dashboard. An index of `0` is the first page of the dashboard.
No index is required if there is only the default page of the dashboard.

**Field Type**
string

**Description**
The label for the dashboard page.

**Field Type**
string

**Description**
The generated unique ID for the dashboard page.

**Field Type**

AnalyticsDashPageWidget[]

**Description**
A list of dashboard page widgets. A page has 0 or more page widgets.


Metadata Types AnalyticsDashboard

AnalyticsDashPageWidget

Represents an dashboard page widget for a Tableau Next dashboard page.

**Field Name** **Description**

```
analyticsDashboardWidget

colspan

column

row

rowspan

```

**Field Type**
string

**Description**

Required.

The name of dashboard widget, defined in the list of widgets for the dashboard.

**Field Type**
string

**Description**
The column span for the widget on the page. This is a numeric value.

**Field Type**
string

**Description**
The column the widget is placed in on the page. This is a numeric value.

**Field Type**
string

**Description**
The row the widget is placed in on the page. This is a numeric value.

**Field Type**
string

**Description**
The row span for the widget on the page. This is a numeric value.

AnalyticsDashboardWidget

Represents a widget on a Tableau Next dashboard.

**Field Name** **Description**

```
analyticsDashboard

```

**Field Type**
string

**Description**

Required.

The API name of the dashboard the widget is associated with.


Metadata Types AnalyticsDashboard

**Field Name** **Description**

```
buttonWidgetDefs

containerWidgetDefs

dynamicTokens

filterWidgetDefs

imageWidgetDefs

label

metricWidgetDefs

parameterWidgetDefs

```

**Field Type**

AnalyticsButtonWidgetDef[]

**Description**
The definition for a button widget type. A dashboard has 0 or more button widgets.
Required for button widget.

**Field Type**

AnalyticsContainerWidgetDef[]

**Description**
The definition for a container widget type. A dashboard has 0 or more container
widgets. Required for container widget.

**Field Type**

AnlytDshbrdWdgtDynamicTkn[]

**Description**
The definition for a dynamic widget token. A dashboard has 0 or more dynamic tokens.

**Field Type**

AnalyticsFilterWidgetDef[]

**Description**
The definition for a filter widget type. A dashboard has 0 or more filter widgets. Required
for filter widget.

**Field Type**

AnalyticsImageWidgetDef[]

**Description**
The definition for a image widget type. A dashboard has 0 or more image widgets.
Required for image widget.

**Field Type**
string

**Description**
The label for the widget.

**Field Type**

AnalyticsMetricWidgetDef[]

**Description**
The definition for a metric widget type. A dashboard has 0 or more metric widgets.
Required for metric widget.

**Field Type**

AnalyticsParamWidgetDef[]


Metadata Types AnalyticsDashboard

**Field Name** **Description**

**Description**
The definition for a parameter widget type. A dashboard has 0 or more paramet widgets.
Required for parameter widget.

```
textWidgetDefs

type

vizWidgetDefs

widgetActions

widgetName

```

**Field Type**

AnalyticsTextWidgetDef[]

**Description**
The definition for a text widget type. A dashboard has 0 or more text widgets. Required
for text widget.

**Field Type**
AnalyticsWidgetType (enumeration of type string)

**Description**

Required.

The widget type.

Values are:

**•** `button`

**•** `component`

**•** `container`

**•** `filter`

**•** `image`

**•** `metric`

**•** `parameter`

**•** `text`

**•** `summary`

**•** `visualization`

**Field Type**

AnalyticsVizWidgetDef[]

**Description**
The definition for a visualization widget type. A dashboard has 0 or more visualization
widgets. Required for visualization widget.

**Field Type**

AnalyticsAssetAction[]

**Description**
The actions for the widget. A widget has 0 or more text widgets.

**Field Type**
string


Metadata Types AnalyticsDashboard

**Field Name** **Description**

**Description**
The API name of the widget. Use this for the `analyticsDashboardWidget`
value in `AnalyticsDashPageWidget` .

AnalyticsAssetAction

Represents an action for a Tableau Next asset.

**Field Name** **Description**

```
actionType

analyticsAssetVerson

eventType

parameters

```

**Field Type**
AnalyticsActionType (enumeration of type string)

**Description**

Required.

The action type.

Values are:

**•** `flow`

**•** `navigate`

**•** `recordaction`

**Field Type**
string

**Description**

Optional.

The version of the Analytics asset the action is associated with.

**Field Type**
AnalyticsActionEventType (enumeration of type string)

**Description**

Required.

The action event type.

Values are:

**•** `click`

**•** `select`

**Field Type**
string

**Description**
The parameter for the action. This is a JSON string.


Metadata Types AnalyticsDashboard

**Field Name** **Description**

Example:

```
                       {"destination":{"type":"url","target":"www.salesforce.com"}}

```

```
version

```

**Field Type**
double

**Description**
The API version of the action.

AnalyticsButtonWidgetDef

Represents a button widget definition for a Tableau Next dashboard.

**Field Name** **Description**

```
parameters

```

**Field Type**
string

**Description**
The parameters for the button widget. This is a JSON String.

Example:

```
  {"text":"Button","alignmentX":"center","alignmentY":"center","fontSize":16}

```

AnalyticsContainerWidgetDef

Represents a container widget definition for a Tableau Next dashboard.

**Field Name** **Description**

```
parameters

```

**Field Type**
string

**Description**
The parameters for the container widget. This is a JSON String.

Example:

```
  {"widgetStyle":{"backgroundColor":"#1295FF","borderEdges":[]}}

```

AnlytDshbrdWdgtDynamicTkn

Represents a widget dynamic token for a Tableau Next dashboard.


Metadata Types AnalyticsDashboard

**Field Name** **Description**

```
description

label

source

tokenName

tokenSpec

type

```

AnalyticsFilterWidgetDef

**Field Type**
string

**Description**
The description for the dynamic token.

**Field Type**
string

**Description**
The label for the dynamic token.

**Field Type**
string

**Description**
The source object of the dynamic token.

**Field Type**
string

**Description**
The name of the dynamic token.

**Field Type**
string

**Description**
The specification for the dynamic token.

**Field Type**
AnalyticsDynamicTokenType

**Description**
The type of dynamic token. Valid values include `query` and `insights` .

Represents a filter widget definition for a Tableau Next dashboard.

**Field Name** **Description**

```
initialValues

```

**Field Type**
string

**Description**
The initial values for the filter.


Metadata Types AnalyticsDashboard

**Field Name** **Description**

```
parameters

source

```

**Field Type**
string

**Description**
The parameters for the filter widget. This is a JSON String.

Example:

```
  {"receiveFilterSource":{"filterMode":"all","widgetIds":[]},"filterOption":{"objectName":"Account","fieldName":"Account_Id","dataType":"Text","selectionType":"multiple"},"isLabelHidden":false}

```

**Field Type**
string

**Description**
The data source to apply the filter to.

AnalyticsImageWidgetDef

Represents a image widget definition for a Tableau Next dashboard.

**Field Name** **Description**

```
parameters

source

```

**Field Type**
string

**Description**
The parameters for the image widget. This is a JSON String.

**Field Type**
string

**Description**
The data source the image is associated with.

AnalyticsMetricWidgetDef

Represents a metric widget definition for a Tableau Next dashboard.

**Field Name** **Description**

```
parameters

```

**Field Type**
string

**Description**
The parameters for the filter widget. This is a JSON String.


Metadata Types AnalyticsDashboard

**Field Name** **Description**

Example:

```
                       {"metricOption":{"layout":{"componentVisibility":{"details":true,"title":true,"value":true,"comparison":true,"chart":true,"insights":false}},"sdmApiName":"AccountModel","sdmId":"2SMxx0000004CFUGA2"},"receiveFilterSource":{"filterMode":"all","widgetIds":[]}}

```

```
semanticModel

source

sourceDeprecated

version

```

**Field Type**
string

**Description**
The semantic model the metric is associated with.

**Field Type**
string

**Description**
The data source the metric is associated with.

**Field Type**
string

**Description**
Present if the data source the metric is associated with is deprecated.

**Field Type**
double

**Description**
The API version of the metric.

AnalyticsParamWidgetDef

Represents a parameters widget definition for a Tableau Next dashboard.

**Field Name** **Description**

```
initialValues

parameters

```

**Field Type**
string

**Description**
The initial values for the parameters.

**Field Type**
string

**Description**
The parameters for the filter widget. This is a JSON String.


Metadata Types AnalyticsDashboard

**Field Name** **Description**

Example:

```
                       {"parameterName":"AccountParameter_prm","isLabelHidden":false}

```

```
source

```

AnalyticsTextWidgetDef

**Field Type**
string

**Description**
The data source the parameters are associated with.

Represents a text widget definition for a Tableau Next dashboard.

**Field Name** **Description**

```
parameters

```

AnalyticsVizWidgetDef

**Field Type**
string

**Description**
The parameters for the filter widget. This is a JSON String.

Example:

```
  {"content":[{"attributes":{"color":"#000000","size":"12px"},"insert":"full

  dashboard"},{"attributes":{"align":"left"},"insert":"\n"}]}

```

Represents a visualization widget definition for a Tableau Next dashboard.

**Field Name** **Description**

```
analyticsVisualization

analyticsVizVersion

```

**Field Type**
string

**Description**
The API name of the visualization.

**Field Type**
string

**Description**
The version of the visualization.


Metadata Types AnalyticsDashboard

**Field Name** **Description**

```
parameters

```

**Field Type**
string

**Description**
The parameters for the filter widget. This is a JSON String.

Example:

```
  {"legendPosition":"Right","receiveFilterSource":{"filterMode":"all","widgetIds":[]}}

```

Declarative Metadata Sample Definition

The following is an example of an AnalyticsDashboard component.

```
<?xml version="1.0" encoding="UTF-8"?>

<AnalyticsDashboard xmlns="http://soap.sforce.com/2006/04/metadata"

xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

   <analyticsWorkspace>My_Workspace</analyticsWorkspace>

   <description>A dashboard</description>

   <layouts>

     <analyticsDashboard>My_Dashboard</analyticsDashboard>

     <columnCount>36</columnCount>

     <layoutName>default</layoutName>

     <maxWidth>1200</maxWidth>

     <label>layoutLabel</label>

     <pages>

        <index>0</index>

        <label>Page 1</label>

        <pageName>e412bc11-d43b-4fba-ab44-b31bb842b49a</pageName>

        <pageWidgets>

          <analyticsDashboardWidget>visualization_1</analyticsDashboardWidget>

          <colspan>11</colspan>

          <column>1</column>

          <row>2</row>

          <rowspan>10</rowspan>

        </pageWidgets>

        <pageWidgets>

          <analyticsDashboardWidget>button_1</analyticsDashboardWidget>

          <colspan>9</colspan>

          <column>13</column>

          <row>8</row>

          <rowspan>2</rowspan>

        </pageWidgets>

        <pageWidgets>

          <analyticsDashboardWidget>container_1</analyticsDashboardWidget>

          <colspan>11</colspan>

          <column>23</column>

          <row>2</row>

          <rowspan>10</rowspan>

        </pageWidgets>

        <pageWidgets>

```


Metadata Types AnalyticsDashboard

```
             <analyticsDashboardWidget>text_2</analyticsDashboardWidget>

             <colspan>9</colspan>

             <column>13</column>

             <row>5</row>

             <rowspan>2</rowspan>

           </pageWidgets>

           <pageWidgets>

             <analyticsDashboardWidget>metric_1</analyticsDashboardWidget>

             <colspan>11</colspan>

             <column>1</column>

             <row>13</row>

             <rowspan>10</rowspan>

           </pageWidgets>

           <pageWidgets>

             <analyticsDashboardWidget>list_4</analyticsDashboardWidget>

             <colspan>9</colspan>

             <column>13</column>

             <row>13</row>

             <rowspan>2</rowspan>

           </pageWidgets>

           <pageWidgets>

             <analyticsDashboardWidget>list_1</analyticsDashboardWidget>

             <colspan>9</colspan>

             <column>13</column>

             <row>2</row>

             <rowspan>2</rowspan>

           </pageWidgets>

        </pages>

        <rowHeight>24</rowHeight>

   <style>{&quot;backgroundColor&quot;:&quot;#ffffff&quot;,&quot;gutterColor&quot;:&quot;#f3f3f3&quot;,&quot;cellSpacingX&quot;:8,&quot;cellSpacingY&quot;:8}</style>

      </layouts>

      <masterLabel>My Dashboard</masterLabel>

   <style>{&quot;widgetStyle&quot;:{&quot;backgroundColor&quot;:&quot;#ffffff&quot;,&quot;borderEdges&quot;:[],&quot;borderColor&quot;:&quot;#cccccc&quot;,&quot;borderWidth&quot;:1,&quot;borderRadius&quot;:0}}</style>

      <version>64.0</version>

      <widgets>

        <analyticsDashboard>My_Dashboard</analyticsDashboard>

        <type>visualization</type>

        <vizWidgetDefs>

           <analyticsVisualization>New_Visualization</analyticsVisualization>

   <parameters>{&quot;legendPosition&quot;:&quot;Right&quot;,&quot;receiveFilterSource&quot;:{&quot;filterMode&quot;:&quot;all&quot;,&quot;widgetIds&quot;:[]}}</parameters>

        </vizWidgetDefs>

        <widgetName>visualization_1</widgetName>

      </widgets>

      <widgets>

        <analyticsDashboard>My_Dashboard</analyticsDashboard>

        <buttonWidgetDefs>

   <parameters>{&quot;text&quot;:&quot;Button&quot;,&quot;alignmentX&quot;:&quot;center&quot;,&quot;alignmentY&quot;:&quot;center&quot;,&quot;fontSize&quot;:16}</parameters>

```


Metadata Types AnalyticsDashboard

```
        </buttonWidgetDefs>

        <type>button</type>

        <widgetActions>

           <actionType>navigate</actionType>

           <eventType>click</eventType>

   <parameters>{&quot;destination&quot;:{&quot;type&quot;:&quot;url&quot;,&quot;target&quot;:&quot;www.salesforce.com&quot;}}</parameters>

           <version>63.0</version>

        </widgetActions>

        <widgetName>button_1</widgetName>

      </widgets>

      <widgets>

        <analyticsDashboard>My_Dashboard</analyticsDashboard>

        <containerWidgetDefs>

   <parameters>{&quot;widgetStyle&quot;:{&quot;backgroundColor&quot;:&quot;#1295FF&quot;,&quot;borderEdges&quot;:[]}}</parameters>

        </containerWidgetDefs>

        <type>container</type>

        <widgetName>container_1</widgetName>

      </widgets>

      <widgets>

        <analyticsDashboard>My_Dashboard</analyticsDashboard>

        <textWidgetDefs>

   <parameters>{&quot;content&quot;:[{&quot;attributes&quot;:{&quot;color&quot;:&quot;#000000&quot;,&quot;size&quot;:&quot;12px&quot;},&quot;insert&quot;:&quot;full

   dashboard&quot;},{&quot;attributes&quot;:{&quot;align&quot;:&quot;left&quot;},&quot;insert&quot;:&quot;\n&quot;}]}</parameters>

        </textWidgetDefs>

        <type>text</type>

        <widgetName>text_2</widgetName>

      </widgets>

      <widgets>

        <analyticsDashboard>My_Dashboard</analyticsDashboard>

        <metricWidgetDefs>

   <parameters>{&quot;metricOption&quot;:{&quot;layout&quot;:{&quot;componentVisibility&quot;:{&quot;details&quot;:true,&quot;title&quot;:true,&quot;value&quot;:true,&quot;comparison&quot;:true,&quot;chart&quot;:true,&quot;insights&quot;:false}},&quot;sdmApiName&quot;:&quot;AccountModel&quot;,&quot;sdmId&quot;:&quot;2SMxx0000004CFUGA2&quot;},&quot;receiveFilterSource&quot;:{&quot;filterMode&quot;:&quot;all&quot;,&quot;widgetIds&quot;:[]}}</parameters>

           <source>AccountMetric_mtc</source>

        </metricWidgetDefs>

        <type>metric</type>

        <widgetName>metric_1</widgetName>

      </widgets>

      <widgets>

        <analyticsDashboard>My_Dashboard</analyticsDashboard>

        <filterWidgetDefs>

           <initialValues>null</initialValues>

   <parameters>{&quot;receiveFilterSource&quot;:{&quot;filterMode&quot;:&quot;all&quot;,&quot;widgetIds&quot;:[]},&quot;filterOption&quot;:{&quot;objectName&quot;:&quot;Account&quot;,&quot;fieldName&quot;:&quot;Account_Id&quot;,&quot;dataType&quot;:&quot;Text&quot;,&quot;selectionType&quot;:&quot;multiple&quot;},&quot;isLabelHidden&quot;:false}</parameters>

           <source>AccountModel</source>

```


### Metadata Types AnalyticSnapshot

```
        </filterWidgetDefs>

        <label>Account Id</label>

        <type>filter</type>

        <widgetName>list_4</widgetName>

      </widgets>

      <widgets>

        <analyticsDashboard>My_Dashboard</analyticsDashboard>

        <label>AccountParameter</label>

        <parameterWidgetDefs>

           <initialValues>null</initialValues>

   <parameters>{&quot;parameterName&quot;:&quot;AccountParameter_prm&quot;,&quot;isLabelHidden&quot;:false}</parameters>

           <source>AccountModel</source>

        </parameterWidgetDefs>

        <type>parameter</type>

        <widgetName>list_1</widgetName>

      </widgets>

      <templateSource></templateSource>

      <templateAssetSourceName></templateAssetSourceName>

      <workspaceAssetRelationships>

        <asset xsi:nil="true"/>

        <assetType>AnalyticsDashboard</assetType>

        <assetUsageType>Created</assetUsageType>

        <workspace>My_Workspace</workspace>

      </workspaceAssetRelationships>

   </AnalyticsDashboard>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>My_Dashboard</members>

        <name>AnalyticsDashboard</name>

      </types>

      <version>64.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### AnalyticSnapshot

Represents a reporting snapshot. A reporting snapshot lets you report on historical data. Authorized users can save tabular or summary
report results to fields on a custom object, then map those fields to corresponding fields on a target object. They can then schedule
when to run the report to load the custom object's fields with the report's data. Reporting snapshots enable you to work with report
data similarly to how you work with other records in Salesforce.


Metadata Types AnalyticSnapshot

Declarative Metadata File Suffix and Directory Location

Lightning Platform AnalyticSnapshot components are stored in the `analyticSnapshots` directory of the corresponding package
directory. The file name matches the unique name of the reporting snapshot, and the extension is `.snapshot` .

Version

Lightning Platform AnalyticSnapshot components are available in API version 16.0 and later.

Fields

**Field** **Field Type** **Description**

`description` string A description of the reporting snapshot.

`groupColumn` string A column that specifies which level to extract data from the
source report. It’s only applicable for summary reports.

`mappings` AnalyticSnapshotMapping[] A list of reporting snapshot mappings. For valid values, see
AnalyticSnapshotMapping.

`name` string Required. The display name of the reporting snapshot.

`runningUser` string The username of the user whose role and _sharing_ settings are
used to run the reporting snapshot.

`sourceReport` string Required. The report where data is extracted from.

`targetObject` string Required. The custom object where data is inserted.

AnalyticSnapshotMapping

AnalyticSnapshotMapping defines the mapping for the reporting snapshot. Valid values are:

**Field** **Field Type** **Description**

`aggregateType` ReportSummaryType[] List that defines if and how each report field is summarized. For valid
(enumeration of type string) values, see ReportSummaryType.

`sourceField` string The sourceField can be one of the following:

**•** The field on the sourceReport that you want to map to the targetField
in the targetObject

**•** A summary of a filed on the sourceReport (for Summary reports only)

**•** A field on the reporting snapshot, such as JobName, RunningUser, or
ExecutionTime (set through the user interface)

**Note:** The sourceField must correspond to the sourceType you specify.

`sourceType` ReportJobSourceTypes[] List that defines the report format for the reporting snapshot. For valid
(enumeration of type string) values, see ReportJobSourceTypes.


Metadata Types AnalyticSnapshot

**Field** **Field Type** **Description**

`targetField` string A field on the targetObject into which this particular sourceField is inserted.

ReportJobSourceTypes

An enumeration of type string that defines the report format for the reporting snapshot. Valid values are:

**Enumeration Value** **Description**

`snapshot` Use this option if the sourceField contains snapshot-specific information such as JobName,
RunningUser, or ExecutionTime.

`summary` Use this option if referencing a summary (Sum, Average, Minimum, Maximum) of a field from
the sourceReport.

`tabular` Use this option if referencing an available column from the sourceReport.

Declarative Metadata Sample Definition

Here’s a sample XML definition of a reporting snapshot.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <AnalyticSnapshot xmlns="http://soap.sforce.com/2006/04/metadata">

      <description>my description</description>

      <groupColumn>INDUSTRY</groupColumn>

      <mappings>

        <aggregateType>Average</aggregateType>

        <sourceField>SALES</sourceField>

        <sourceType>summary</sourceType>

        <targetField> myObject __c.Name</targetField>

      </mappings>

      <mappings>

        <sourceField>ExecutionTime</sourceField>

        <sourceType>snapshot</sourceType>

        <targetField> myObject __c.field3__c</targetField>

      </mappings>

      <mappings>

        <sourceField>INDUSTRY</sourceField>

        <sourceType>tabular</sourceType>

        <targetField>testObject__c.Name</targetField>

      </mappings>

      <name>my snapshot</name >

      <runningUser>user@salesforce.com</runningUser>

      <sourceReport>myFolder/mytSummaryReport</sourceReport>

      <targetObject>myObject__c</targetObject>

   </AnalyticSnapshot>

```


### Metadata Types AnalyticsVisualization

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

Report

### AnalyticsVisualization

Represents a Tableau Next visualization.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### AnalyticsVisualization components have the suffix .uaviz and are stored in the analyticsVisualizations folder.

Version

### AnalyticsVisualization components are available in API version 64.0 and later.

Limits

**Definition** **Limit**

The maximum number of 50
### AnalyticsVisualization components in a single

deploy operation.

The maximum number of 100
### AnalyticsVisualization components in a single

retrieve operation.

The maximum number of 100
### AnalyticsVisualization components across all

deploy operations in a 24-hour window.

The maximum number of 200
### AnalyticsVisualization components across all

retrieve operations in a 24-hour window.


Metadata Types AnalyticsVisualization

Fields

**Field Name** **Description**

```
actions

analyticsWorkspace

dataSource

description

fields

lastDraftModifiedDate

lastPublishedDate

masterLabel

```

**Field Type**

AnalyticsAssetAction[]

**Description**
The actions for the visualization. A visualization has 0 or more actions.

**Field Type**
string

**Description**

Required.

The Tableau Next workspace the visualization belongs to.

**Field Type**
string

**Description**

Required.

The data source for the visualization.

**Field Type**
string

**Description**
The description for the visualization.

**Field Type**

AnalyticsVizField[]

**Description**
A list of data fields for the visualization. A visualization has 0 or more fields.

**Field Type**
dateTime

**Description**
The date and time the workspace draft was last modified.

**Field Type**
dateTime

**Description**
The date and time the workspace was last published.

**Field Type**
string


Metadata Types AnalyticsVisualization

**Field Name** **Description**

**Description**

Required.

The name of the visualization.

```
templateAssetSourceName

templateSource

version

views

visualSpecification

workspaceAssetRelationships

```

AnalyticsVizField

Represents a data field in a visualization.

**Field Type**
string

**Description**
If the visualization was created from a template, the name of the source visualization
in the template.

**Field Type**
string

**Description**
If the visualization was created from a template, the name of the source template.

**Field Type**
double

**Description**
The API version of the visualization.

**Field Type**

AnalyticsVizViewDef[]

**Description**
A list of views for the visualization. A visualization has 0 or more views.

**Field Type**
base64Binary

**Description**

Required.

The visual specification for the visualization.

**Field Type**

AnalyticsWorkspaceAsset[]

**Description**
A list of analytics assets in the workspace this visualization is associated with. A
visualization has 0 or more workspace asset relationships.


Metadata Types AnalyticsVisualization

**Field Name** **Description**

```
adHoCalc

analyticsVizVersion

computeUsing

displayCategory

fieldKey

fieldName

function

```

**Field Type**
string

**Description**
The expression to do an ad-hoc calculation with.

**Field Type**
string

**Description**
The version of the visualization the field is associated with.

**Field Type**
string

**Description**
The expression to compute the field value with.

**Field Type**
VisualizationFieldDisplayCategoryType (enumeration of type string)

**Description**
The display category type for the visualization field.

Values are:

**•** `Continuous`

**•** `Discrete`

**Field Type**
string

**Description**

Required.

The key for the field.

**Field Type**
string

**Description**
The name of the field.

**Field Type**
VisualizationFieldFunctionType (enumeration of type string)

**Description**
The function type of the visualization field.

Values are:

**•** `Avg`


Metadata Types AnalyticsVisualization

**Field Name** **Description**

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

**•** `My`

**•** `Stdev`

**•** `Stdevp`

**•** `Sum`

**•** `UserAgg`

**•** `Var`

**•** `Varp`

```
hierarchyName

```

**Field Type**
string

**Description**
The hierarchy name for the field.


Metadata Types AnalyticsVisualization

**Field Name** **Description**

```
label

objectName

quickTableCalc

role

type

```

AnalyticsVizViewDef

**Field Type**
string

**Description**
The label for the field.

**Field Type**
string

**Description**
The name of the data source object for the field.

**Field Type**
string

**Description**
The expression to do a quick table calculation with.

**Field Type**
VisualizationFieldRoleType (enumeration of type string)

**Description**
The role type of the visualization field.

Values are:

**•** `Dimension`

**•** `Measure`

**Field Type**
VisualizationFieldType (enumeration of type string)

**Description**
The type of the visualization field.

Values are:

**•** `Field`

**•** `MeasureNames`

**•** `MeasureValues`

Represents a view definition for a Tableau Next visualization.

**Field Name** **Description**

```
analyticsVizVersion

```

**Field Type**
string


Metadata Types AnalyticsVisualization

**Field Name** **Description**

**Description**
The version of the visualization the view is associated with.

```
fullName

isOriginal

masterLabel

version

viewSpecification

```

**Field Type**
string

**Description**

Required.

The full name of the view definition.

**Field Type**
boolean

**Description**

Required.

Indicates whether the view is original ( `true` ) or not ( `false` ).

**Field Type**
string

**Description**

Required.

The name of the view definition.

**Field Type**
double

**Description**
The API version of the visualization view.

**Field Type**
string

**Description**
The specification for the view definition.

Declarative Metadata Sample Definition

The following is an example of an AnalyticsVisualization component.

```
<?xml version="1.0" encoding="UTF-8"?>

<AnalyticsVisualization xmlns="http://soap.sforce.com/2006/04/metadata"

xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

  <analyticsWorkspace>My_Workspace</analyticsWorkspace>

  <description>A visualization</description>

  <dataSource>My_Semantic_Model</dataSource>

  <fields>

```


Metadata Types AnalyticsVisualization

```
      <displayCategory>Discrete</displayCategory>

      <fieldKey>Field1</fieldKey>

      <fieldName>Lead_Source18</fieldName>

      <objectName>Opportunity_Home</objectName>

      <role>Dimension</role>

      <type>Field</type>

     </fields>

     <fields>

      <fieldKey>Field2</fieldKey>

      <displayCategory>Continuous</displayCategory>

      <fieldName>Amount</fieldName>

      <function>Sum</function>

      <objectName>Opportunity_Home</objectName>

      <role>Measure</role>

      <type>Field</type>

     </fields>

     <views>

      <fullName>default</fullName>

      <masterLabel>My_Visualization_default</masterLabel>

      <viewSpecification>

   {&quot;filters&quot;:[{&quot;fieldKey&quot;:&quot;Field1&quot;,&quot;filterInfos&quot;:[{&quot;isCustom&quot;:false,&quot;isExcludes&quot;:false,&quot;type&quot;:&quot;In&quot;,&quot;useA l &quot;:false,&quot;values&quot;:[&quot;NewBusine s &quot;]},{&quot;includeA l ValuesWhenEmpty&quot;:true,&quot;isExcludes&quot;:false,&quot;operator&quot;:&quot;Contains&quot;,&quot;type&quot;:&quot;WildCard&quot;,&quot;value&quot;:&quot;&quot;}],&quot;isContext&quot;:false}],&quot;sorts&quot;:[{&quot;byField&quot;:&quot;Field2&quot;,&quot;fieldKey&quot;:&quot;Field1&quot;,&quot;order&quot;:&quot;Ascending&quot;,&quot;type&quot;:&quot;Nested&quot;}]}</viewSpecification>

      <isOriginal>true</isOriginal>

     </views>

     <masterLabel>My_Visualization</masterLabel>

     <version>64.0</version>

     <templateSource></templateSource>

     <templateAssetSourceName></templateAssetSourceName>

     <workspaceAssetRelationships>

      <asset xsi:nil="true"/>

      <assetType>AnalyticVisualization</assetType>

      <assetUsageType>Created</assetUsageType>

      <workspace>My_Workspace</workspace>

     </workspaceAssetRelationships>

   </AnalyticsVisualization>

```

The following is an example `package.xml` that references the metadata definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

    <Package xmlns="http://soap.sforce.com/2006/04/metadata">

    <types>

    <members>My_Visualization</members>

    <name>AnalyticsVisualization</name>

    </types>

    <version>64.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


### Metadata Types AnalyticsWorkspace AnalyticsWorkspace

Represents a Tableau Next workspace.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### AnalyticsWorkspace components have the suffix .analtyicsWorkspace and are stored in the analyticsWorkspaces

folder.

Version

### AnalyticsWorkspace components are available in API version 64 and later.

Limits

**Definition** **Limit**

The maximum number of AnalyticsWorkspace 50
components in a single deploy operation.

The maximum number of AnalyticsWorkspace 100
components in a single retrieve operation.

The maximum number of AnalyticsWorkspace 100
components across all deploy operations in
a 24-hour window.

The maximum number of AnalyticsWorkspace 200
components across all retrieve operations in
a 24-hour window.

Fields

**Field Name** **Description**

```
description

```

**Field Type**
string

**Description**
The workspace description.


Metadata Types AnalyticsWorkspace

**Field Name** **Description**

```
masterLabel

workspaceAssetRelationships

```

**Field Type**
string

**Description**

Required.

The name of the workspace.

**Field Type**

AnalyticsWorkspaceAsset[]

**Description**
The workspace assets associated with the workspace. A workspace has 1 or more
assets.

AnalyticsWorkspaceAsset

Represents a Tableau Next analytics asset.

**Field Name** **Description**

```
asset

assetType

```

**Field Type**
string

**Description**

Required.

The name of workspace asset

**Field Type**
AnalyticsWorkspaceAssetType (enumeration of type string)

**Description**

Required.

The workspace asset type

Values are:

**•** `AnalyticsDashboard` (Tableau Next Dashboard)

**•** `AnalyticsVisualization` (Tableau Next Visualization)

**•** `MktCalculatedInsightObject` (Data 360 Calculated Insight Object)

**•** `MktDataConnection` (Data 360 Connection)

**•** `MktDataLakeObject` (Data 360 Data Lake Object)

**•** `MktDataModelObject` (Data 360 Data Model Object)

**•** `SemanticModel` (Semantic Model)


Metadata Types AnalyticsWorkspace

**Field Name** **Description**

```
assetUsageType

metadataSourceType

workspace

```

**Field Type**
AnalyticsWorkspaceAssetUsageType (enumeration of type string)

**Description**

Required.

The workspace asset usage type.

Values are:

**•** `Created`

**•** `Referenced`

**Field Type**
AnalyticsWorkspaceAssetMetadataSourceType (enumeration of type string)

**Description**
The workspace asset metadata source type.

Values are:

**•** `Promoted`

**•** `Reused`

**Field Type**
string

**Description**

Required.

The workspace the asset belongs to.

Declarative Metadata Sample Definition

The following is an example of an AnalyticsWorkspace component.

```
<?xml version="1.0" encoding="UTF-8"?>

  <AnalyticsWorkspace xmlns="http://soap.sforce.com/2006/04/metadata">

  <description>An example for Analytics Workspace</description>

  <masterLabel>Analytics Workspace</masterLabel>

  <workspaceAssetRelationships>

   <asset>My Test Dashboard</asset>

   <assetType>AnalyticsDashboard</assetType>

   <assetUsageType>Created</assetUsageType>

   <metadataSourceType>Promoted</metadataSourceType>

   <workspace>Analytics Workspace</workspace>

  </workspaceAssetRelationships>

</AnalyticsWorkspace>

```


### Metadata Types AnimationRule

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

     <types>

      <members>*</members>

      <name>AnalyticsWorkspace</name>

     </types>

     <version>64.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### AnimationRule

Represents criteria for determining when an animation is displayed to Path users.This type extends the Metadata metadata type and
inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### AnimationRule components have the suffix animationRule and are stored in the animationRules folder.

Version

### AnimationRule components are available in API version 46.0 and later.

Fields

**Field Name** **Field Type** **Description**

`animationFrequency` picklist Required. The frequency with which an animation is displayed when a
user selects the designated picklist values in a path. Valid values are:

**•** `always`

**•** `often`

**•** `sometimes`

**•** `rarely`

A value of `always` triggers an animation every time. The values
`often`, `sometimes`, and `rarely` trigger an animation progressively
less frequently.


Metadata Types AnimationRule

**Field Name** **Field Type** **Description**

`developerName` string Required. The developer name for the animation rule.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this
field.

`isActive` boolean Required. Indicates whether the animation rule is active ( `true` ) or not
( `false` ).

`masterLabel` string Required. The label for the animation rule.

`recordTypeContext` picklist

Required. An enum to track whether this AnimationRule applies to all
record types for the associated sObject, or only to a single or main record
type. Valid values are `All`, `Master`, or `Custom` .

`recordTypeName` reference The record type selected for the sObject in which the animation is
displayed.

`sobjectType` string The object on which the animation rule is run.

`targetField` string Required. Name of the field used to determine when to display an
animation.

`targetFieldChangeToValues` string

Required. Values used to determine when to display an animation. When
a user selects a value in `targetField` that matches a value stored
in `targetFieldChangeToValues`, the animation is displayed.

Declarative Metadata Sample Definition

The following is an example of an AnimationRule component.

```
<?xml version="1.0" encoding="UTF-8"?>

<AnimationRule xmlns="http://soap.sforce.com/2006/04/metadata">

   <animationFrequency>Always</animationFrequency>

   <developerName>AnimationRule_DeveloperName</developerName>

   <isActive>true</isActive>

   <masterLabel>AnimationRule Label</masterLabel>

   <recordTypeContext>All</recordTypeContext>

   <recordTypeName>__MASTER__</recordTypeName>

   <sobjectType>Opportunity</sobjectType>

   <targetField>StageName</targetField>

  <targetFieldChangeToValues>Delivered, Negotiating, Closed Won</targetFieldChangeToValues>

</AnimationRule>

```

The following is an example `package.xml` that references the AnimationRule component.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>PathAssistant</members>

     <name>Settings</name>

   </types>

```


### Metadata Types AppFrameworkTemplateBundle

```
      <types>

        <members>AnimationRule_Developer_Name</members>

        <name>AnimationRule</name>

      </types>

      <version>46.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### AppFrameworkTemplateBundle

Represents the app framework template bundle. Use these templates for Data 360 and Tableau Next assets.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

An app framework template bundle is a folder that contains definition files for a template. Unlike other metadata components, a
### AppFrameworkTemplateBundle component isn’t represented with a single component file, but instead by a collection of JSON and

other definition files. Each definition file represents a resource in a template, such as semantic models, workspaces, visualizations, and
dashboards. For example, this directory structure shows the hierarchy of the folders and files for one app framework template definition,
myTemplate.

```
   appTemplates

     myTemplate

      template-info.json

      create-chain.json

      rules.json

      variables.json

      layout.json

      workspaces

       myWorkspace.json

      dashboards

       myDashboard.json

```

App framework template bundles must be under a top-level folder that’s named `appTemplates` . Each bundle must have its own
subfolder under the `appTemplate` folder and named with the template's fully qualified API name. The bundle folder must contain
a template-info.json file to specify the metadata about the template and the references to other definition files. An entire bundle doesn’t
have a suffix and definition files can have one of the these suffixes.


Metadata Types AppFrameworkTemplateBundle

Version

AppFrameworkTemplateBundle components are available in API version 64.0 and later.

Special Access Rules

Create definitions in both managed and unmanaged packages.

Fields

**Field Name** **Description**

```
assetVersion

description

label

maxAppCount

templateBadgeIcon

templateStatus

```

**Field Type**
double

**Description**
The API version of the template bundle.

**Field Type**
string

**Description**
The description for the template.

**Field Type**
string

**Description**
Required

The label for the template.

**Field Type**
int

**Description**
The maximum number of apps that can be created from this template.

**Field Type**
string

**Description**
The badge icon for the template. This must be a `.png` file type.

**Field Type**
string

**Description**
The status of the template.


### Metadata Types ArticleType

**Field Name** **Description**

```
templateSubtype

templateType

```

**Field Type**
string

**Description**
The subtype of the template.

**Field Type**
string

**Description**
The type of the template.

Declarative Metadata Sample Definition

This is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

<types>

   <members>myTemplate</members>

   <name>AppFrameworkTemplateBundle</name>

</types>

<version>64.0</version>

</Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about the manifest
[file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### ArticleType

Represents the metadata associated with an article type.

All articles in Salesforce Knowledge are assigned to an _article type_ . An article's type determines the type of content it contains, its
appearance, and which users can access it. For example, a simple FAQ article type can have two custom fields, `Question` and `Answer`,
where article managers enter data when creating or updating FAQ articles. A more complex article type can have dozens of fields
organized into several sections. Using layouts and templates, administrators can structure the article type in the most effective way for
its particular content. User access to article types is controlled by permissions. For each article type, an administrator can grant “Create,”
“Read,” “Edit,” or “Delete” permissions to users. For example, the article manager can allow internal users to read, create, and edit FAQ
[article types, but let partner users only read FAQs. See “Knowledge Article Types” in the Salesforce online help and Knowledge in the](https://help.salesforce.com/s/articleView?id=service.knowledge_article_types_manage.htm&type=5&language=en_US)
_SOAP API Developer Guide_ .


Metadata Types ArticleType

Declarative Metadata File Suffix and Directory Location

An ArticleType is defined as a custom object and is stored in the `objects` folder. ArticleTypes have a suffix `__kav` (instead of `__c`
for custom objects). ArticleType field names have a suffix of `__c` like other custom objects, and must be dot-qualified with the name
of the article type to which they belong. This is shown in the following sample `package.xml` file:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <fullName>articlefilemetadata</fullName>

      <apiAccessLevel>Unrestricted</apiAccessLevel>

      <types>

        <members>newarticle__kav.description__c</members>

        <name>CustomField</name>

      </types>

      <types>

        <members>newarticle__kav</members>

        <name>CustomObject</name>

      </types>

   </Package>

```

Version

ArticleTypes are available in API version 19.0 and later.

Fields

**Field Name** **Field Type** **Description**

`articleTypeChannel` articleTypeChannelDisplay

```
Display

```

`deploymentStatus` DeploymentStatus
(enumeration of type string)

Represents the article-type templates used to display an article in the
[various channels. See “Article Type Templates” in the Salesforce online](https://help.salesforce.com/s/articleView?id=service.knowledge_article_templates_create.htm&type=5&language=en_US)
help.

A string which represents the deployment status of a custom object or
field. Valid values are:

**•** `InDevelopment`

**•** `Deployed`

`description` string A description of the article type. Maximum of 1000 characters.

`fields` CustomField[] Represents one or more fields in the article type.

`gender` Gender

Indicates the gender of the noun that represents the object. This is used
for languages where words need different treatment depending on their
gender.

`label` string Label that represents the object throughout the Salesforce user interface.

`pluralLabel` string Plural version of the `label` value.


Metadata Types ArticleType

**Field Name** **Field Type** **Description**

`startsWith` StartsWith (enumeration of
type string)

ArticleTypeChannelDisplay

Indicates whether the noun starts with a vowel, consonant, or is a special
character. This is used for languages where words need different treatment
depending on the first character. Valid values are listed in StartsWith.

Determines the article-type templates that are used to display an article in its channels. Unless otherwise noted, all fields are createable,
filterable, and nillable.

**Field Name** **Field Type** **Description**

`articleTypeTemplates` ArticleTypeTemplate on page Indicates which article-type template applies in the specified channel.
378[]

ArticleTypeTemplate

Sets the article-type template for a specific channel. If not specified, the default article-type template applies.

**Field Name** **Field Type** **Description**

`channel` string Specifies the channel where the article-type template applies:

**•** `AllChannels` : all the available channels.

**•** `App` : the Articles tab in Salesforce Knowledge.

**•** `Pkb` : the public knowledge base.

**•** `Csp` : the Customer Portal.

**•** `Prm` : the partner portal.

`page` string

Represents the name of the custom Visualforce page used as a custom
article-type template. Use this field when you select `Page` in the
template field.

`template` string Indicates the article-type template used for the specified channel:

**•** `Page` : custom Visualforce page. When specifying this value, you
must also set the `page` field with the Visualforce page name.

**•** `Tab` : display the sections you defined in the layout as tabs.

**•** `Toc` : display the sections you defined in the layout as table of content.

Declarative Metadata Sample Definitions

A sample article type definition follows:

```
<?xml version="1.0" encoding="UTF-8"?>

<CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

   <articleTypeChannelDisplay>

```


Metadata Types ArticleType

```
        <articleTypeTemplates>

           <channel>App</channel>

           <template>Tab</template>

        </articleTypeTemplates>

        <articleTypeTemplates>

           <channel>Prm</channel>

           <template>Tab</template>

        </articleTypeTemplates>

        <articleTypeTemplates>

           <channel>Csp</channel>

           <template>Tab</template>

        </articleTypeTemplates>

        <articleTypeTemplates>

           <channel>Pkb</channel>

           <template>Toc</template>

        </articleTypeTemplates>

      </articleTypeChannelDisplay>

      <deploymentStatus>Deployed</deploymentStatus>

      <description>Article type with custom fields</description>

      <fields>

        <fullName>description__c</fullName>

        <label>Description</label>

        <length>48</length>

        <type>Text</type>

      </fields>

      <label>newarticle</label>

      <pluralLabel>newarticles</pluralLabel>

   </CustomObject>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

ArticleType Layout
Represents the metadata associated with an article type page layout. Article type layouts determine which fields users can view and
edit when entering data for an article. Article type layouts also determine which sections appear when users view articles.

ChannelLayout
Represents the metadata associated with a communication channel layout. Communication channel layouts let admins share article
content inline into communication channels (for example, in email publishers, Experience Builder sites, or social media publishers).
Admins can create a list of fields for an article type or record type that they want to share for each communication channel. You can
customize the order of the fields.

ArticleType CustomField
Represents the metadata associated with an article type custom field. Use this metadata type to create, update, or delete article type
custom field definitions.

SEE ALSO:

ArticleType Layout

ArticleType CustomField


#### Metadata Types ArticleType Layout ArticleType Layout

Represents the metadata associated with an article type page layout. Article type layouts determine which fields users can view and edit
when entering data for an article. Article type layouts also determine which sections appear when users view articles.

The format of the article, for example whether layout sections display as subtabs or as a single page with links, is defined by the article-type
template. Each article type has only one layout, but you can choose a different template for each of the article type's four channels. See
[Knowledge in](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/sforce_api_guidelines_knowledge.htm) _SOAP API Developer Guide_ .

File Suffix and Directory Location

ArticleType layouts are stored in the `layouts` directory of the corresponding package directory. The prefix must match with the article
type API name. The extension is `.layout` .

Version

ArticleType layouts are available in API version 19.0 and later.

Fields

**Field Name** **Field Type** **Description**

`layoutSections` LayoutSection[] The main sections of the layout containing the article fields. The
order here determines the layout order.

LayoutSection

LayoutSection represents a section of an ArticleType layout.

**Field Name** **Field Type** **Description**

`customLabel` boolean Indicates if this section's label is custom or standard (built-in). Custom
labels can be any text, but must be translated. Standard labels have a

predefined set of valid values, for example 'System Information', which
are automatically translated.

`label` string The label; either standard or custom, based on the `customLabel`
flag.

`layoutColumns` LayoutColumn[] The columns of the layout, depending on the style. Salesforce Knowledge
only supports one column in article type layouts.

```
style

```

LayoutColumn

LayoutSectionStyle The style of the layout. Salesforce Knowledge only supports the value
(enumeration of type `OneColumn`, which displays a one-column page.
string)

LayoutColumn represents the items in a column within a layout section.


Metadata Types ArticleType Layout

**Field Name** **Field Type** **Description**

`layoutItems` LayoutItem[] The individual items within a column (ordered from top to bottom).

LayoutItem

LayoutItem represents the valid values that define a layout item.

**Field Name** **Field Type** **Description**

`field` string The field name reference, for example `MyField__c` .

Declarative Metadata Sample Definition

The following is the definition of an ArticleType page layout:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Layout xmlns="http://soap.sforce.com/2006/04/metadata">

      <layoutSections>

        <customLabel>true</customLabel>

        <label>Description</label>

        <layoutColumns>

           <layoutItems>

             <field>description__c</field>

           </layoutItems>

           <layoutItems>

             <field>dateTime__c</field>

           </layoutItems>

        </layoutColumns>

        <style>OneColumn</style>

      </layoutSections>

      <layoutSections>

        <label>Data Sheet</label>

        <layoutColumns>

           <layoutItems>

             <field>file__c</field>

           </layoutItems>

        </layoutColumns>

        <style>OneColumn</style>

      </layoutSections>

   </Layout>

```

SEE ALSO:

ArticleType

ArticleType CustomField


#### Metadata Types ChannelLayout ChannelLayout

Represents the metadata associated with a communication channel layout. Communication channel layouts let admins share article
content inline into communication channels (for example, in email publishers, Experience Builder sites, or social media publishers).
Admins can create a list of fields for an article type or record type that they want to share for each communication channel. You can
customize the order of the fields.

File Suffix and Directory Location

Channel layout components have the suffix `.channelLayout` and are stored in the `channelLayouts` folder of the
corresponding package directory. The prefix must match with the article type API name. In Lightning Knowledge, the prefix must match
the API name for the knowledge object.

Version

Channel layout components are available in API version 32.0 and later.

Fields

**Field Name** **Field Type** **Description**

`doesExcludeFieldLabels` boolean Indicates whether field labels are excluded from the field contents in
the communication channels where this layout applies ( `true` ) or not

( `false` ). The default is `false`, meaning field labels are inserted.
Available when Lightning Knowledge is enabled in API version 48.0 and
later.

`doesExcludeFiles` boolean Indicates whether related files are left off emails ( `true` ) or attached to
emails ( `false` ). The default is `false`, meaning related files are

attached. Available when Lightning Knowledge is enabled in API version
48.0 and later.

`enabledChannels` string[] The communication channels where this layout applies. In API version
32.0 to 46.0, the only valid value is `Email` . When Lightning Knowledge

is enabled in API version 47.0 and later, `Chat`, `Messaging`, and
`Social` are added valid values.

`label` string Required. The label for this configuration.

#### layoutItems ChannelLayoutItem The article fields contained in the layout. The order here determines the

on page 383[] field order.

`recordType` string The name of the record type that the channel layout applies to. The
default is the primary record type. Available in API version 41.0 and later.


#### Metadata Types ArticleType CustomField

ChannelLayoutItem

**Field Name** **Field Type** **Description**

`field` string Required. Name of the field. The format is _`ArticleTypeName`_ . _`FieldName`_
or, in Lightning Knowledge, _`KnowledgeBaseName`_ . _`FieldName`_ .

Declarative Metadata Sample Definition

The following is an example of a ChannelLayout component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ChannelLayout xmlns="http://soap.sforce.com/2006/04/metadata">

      <label>Layout for Email</label>

      <layoutItems>

        <field>Knowledge.Question</field>

      </layoutItems>

      <layoutItems>

        <field>Knowledge.Answer</field>

      </layoutItems>

      <enabledChannels>Email</enabledChannels>

      <enabledChannels>Social</enabledChannels>

      <enabledChannels>Chat</enabledChannels>

      <doesExcludeFiles>false</doesExcludeFiles>

      <doesExcludeFieldLabels>true</doesExcludeFieldLabels>

   </ChannelLayout>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>ChannelLayout</name>

      </types>

      <version>41.0</version>

   </Package>

#### ArticleType CustomField

```

Represents the metadata associated with an article type custom field. Use this metadata type to create, update, or delete article type
custom field definitions.

This type extends the Metadata metadata type and inherits its `fullName` field.

Always specify the full name whenever you create or update a custom field. For example, a custom field on a custom object:

```
   MyArticleType__kav.MyCustomField__c

```


Metadata Types ArticleType CustomField

Declarative Metadata File Suffix and Directory Location

Custom fields are defined as part of the article type. ArticleType field names have a suffix of `__c` like other custom objects, and must
be dot-qualified with the name of the article type to which they belong. See ArticleType for more information.

Retrieving Custom Fields on Custom or Standard Objects

When you retrieve a custom or standard object, you return everything associated with the object. However, you can also retrieve only
the custom fields for an object by explicitly naming the object and fields in `package.xml` . The following definition in `package.xml`
retrieves the files `objects/MyCustomObject__c.object`, `objects/Account.object__c.object`, and
`objects/MyArticleType__kav.object`, each containing one custom field definition.

```
   <types>

      <members>MyCustomObject__c.MyCustomField__c</members>

      <members>Account.MyCustomAccountField__c</members>

      <members>MyArticleType__kav.MyOtherCustomField__c</members>

      <name>CustomField</name>

   </types>

```

Version

ArticleTypes custom fields are available in API version 19.0 and later.

Fields for ArticleType

Unless otherwise noted, all fields are createable, filterable, and nillable.

Note: If you create a knowledge validation rule, the errors always display at the top of the page, even if you add it beside the
field. Therefore, write the errors descriptively so authors know how to satisfy the validation rule. For example, identify which field
is causing the error. The Salesforce Classic user interface does not support field level error messages for articles.

**Field Name** **Field Type** **Description**

`defaultValue` string If specified, represents the default value of the field. This field
was deprecated in API version 48.0.

```
deleteConstraint

```

Metadata Field Types Provides deletion options for lookup relationships. Valid values
(enumeration of type are:
string)

**•** `Cascade` —Deletes the lookup record as well as
associated lookup fields.

**•** `Restrict` —Prevents the record from being deleted if
it's in a lookup relationship.

**•** `SetNull` —This is the default. If the lookup record is
deleted, the lookup field is cleared.

For more information on lookup relationships, see "Object
Relationships" in Salesforce Help.

`description` string Description of the field.


Metadata Types ArticleType CustomField

**Field Name** **Field Type** **Description**

`formula` string If specified, represents a formula on the field.

```
formulaTreatBlankAs

```

Metadata Field Types Indicates how to treat blanks in a formula. Valid values are:
(enumeration of type `BlankAsBlank` and `BlankAsZero` .
string)

`fullName` string Inherited from Metadata, this field is defined in the WSDL for
this metadata type. It must be specified when creating,

updating, or deleting. See `createMetadata()` to see an
example of this field specified for a call.

This value cannot be `null` .

`inlineHelpText` string Represents the content of field-level help. For more information,
see "Define Field-Level Help" in Salesforce Help.

`label` string Label for the field. You cannot update the label for standard
fields in Article Type such as Title, UrlName, Summary, etc.

`length` int Length of the field.

`picklist` Picklist (Including ( **Deprecated.** Use this field in API version 37.0 and earlier only.
Dependent Picklist) In later versions, use `valueSet` instead.) If specified, the field

is a picklist, and this field enumerates the picklist values and
labels.

`referenceTo` string If specified, indicates a reference this field has to another object.

`relationshipLabel` string Label for the relationship.

`relationshipName` string

If specified, indicates the value for one-to-many relationships.
For example, in the object MyObject that had a relationship to
YourObject, the relationship name might be YourObjects.

`required` boolean Indicates whether the field requires a value on creation ( `true` )
or not ( `false` ).

`type` FieldType Required. Indicates the field type for the field. Valid values are:

**•** `Checkbox` available in version 30.0 and later

**•** `Currency`

**•** `ArticleCurrency`

**•** `Date`

**•** `DateTime`

**•** `Email`

**•** `File`

**•** `Formula`

**•** `Html`

**•** `Lookup`

**•** `Number`


### Metadata Types ApexClass

**Field Name** **Field Type** **Description**

**•** `Percent`

**•** `Phone`

**•** `Picklist`

**•** `DependentPicklist`

**•** `MultiselectPicklist`

**•** `Text`

**•** `TextArea`

**•** `LongTextArea`

**•** `URL`

`visibleLines` int Indicates the number of lines displayed for the field.

Declarative Metadata Sample Definition

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

      <fields>

        <fullName>Comments__c</fullName>

        <description>add your comments about this object here</description>

        <label>Comments</label>

        <length>32000</length>

        <type>LongTextArea</type>

        <visibleLines>30</visibleLines>

      </fields>

   </CustomObject>

```

SEE ALSO:

ArticleType

ArticleType Layout

### ApexClass

Represents an Apex class. An Apex class is a template or blueprint from which Apex objects are created. Classes consist of other classes,
user-defined methods, variables, exception types, and static initialization code.

[For more information, see the Lightning Platform Apex Code Developer's Guide. This type extends the MetadataWithContent metadata](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/)
type and inherits its `content` and `fullName` fields.

Note: By default, you can’t deploy updates to an Apex class if there are one or more active jobs for that class. To deploy updates
in this case, do one of the following.

**•** Cancel Apex jobs before deploying changes to Apex code. Reschedule the jobs after the deployment.

**•** Enable deployments with Apex jobs in the Salesforce user interface in the Deployment Settings page.


Metadata Types ApexClass

Supported Calls

All Metadata API calls except CRUD-Based Calls, which prevents deployment outside of proper deployment lifecycle and test-execution
constraints.

Declarative Metadata File Suffix and Directory Location

The file suffix is `.cls` for the class file. The accompanying metadata file is named _`ClassName`_ `.cls-meta.xml` .

Apex classes are stored in the `classes` folder in the corresponding package directory.

Version

Apex classes are available in API version 10.0 and later.

Fields

This metadata type contains the following fields:

**Field Name** **Field Type** **Description**

`apiVersion` double
The API version for this class. Every class has an API version specified at creation.

`content` base64 The Apex class definition. Base 64-encoded binary data. Before making an API
call, client applications must encode the binary attachment data as base64. Upon

receiving a response, client applications must decode the base64 data to binary.
This conversion is handled for you by a SOAP client. This field is inherited from
the MetadataWithContent component.

`fullName` string The Apex class name. The name can only contain characters, letters, and the
underscore (_) character, must start with a letter, and can’t end with an

underscore or contain two consecutive underscore characters. This field is
inherited from the Metadata component.

`packageVersions` PackageVersion[]

The list of installed managed package versions that are referenced by this Apex
class.

[For more information about managed packages, see Second-Generation](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_dev2gp.htm)
[Managed Packages in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_dev2gp.htm) _Salesforce DX Developer Guide_ . This field is available in
API version 16.0 and later.

`status` ApexCodeUnitStatus
The status of the Apex class. The following string values are valid:
(enumeration of type string)

**•** `Active`                    - The class is active.

**•** `Deleted`                    - The class is marked for deletion. This value is useful for managed
packages, because it allows a class to be deleted when a managed package
is updated.

ApexCodeUnitStatus includes an `Inactive` option, but it’s only supported
for ApexTrigger; it isn’t supported for ApexClass.


Metadata Types ApexClass

PackageVersion

PackageVersion identifies a version of a managed package. A package version is a number that identifies the set of components included
in a package. The version number has the format _`majorNumber.minorNumber.patchNumber`_ (for example, 2.1.3). The major
and minor numbers increase to a chosen value during every major release. The _`patchNumber`_ is generated and updated only for a
patch release. It’s available in API version 16.0 and later.

[See Set Package Versions for Apex Classes and Triggers in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_manpkgs_subscriber_version.htm) _Apex Developer Guide_ .

**Field Name** **Field Type** **Description**

`namespace` string Required. In a packaging context, a namespace prefix is a one to 15-character
alphanumeric identifier that distinguishes your package and its contents from

packages of other developers on AppExchange. Namespace prefixes are
case-insensitive. For example, ABC and abc aren’t recognized as unique. Your
namespace prefix must be globally unique across all Salesforce orgs.

Salesforce automatically prepends your namespace prefix, followed by two
underscores (“__”), to all unique component names in your Salesforce
organization. A unique package component is one that requires a name that no
other component has within Salesforce, such as custom objects, custom fields,
custom links, s-controls, and validation rules. For more information about
[namespaces, see Create and Register Your Namespace in the](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_create_namespace.htm) _Second-Generation_
_Managed Packaging Developer Guide_ .

`majorNumber` int Required. The major number of the package version. A package version number
has a _`majorNumber.minorNumber`_ format.

`minorNumber` int Required. The minor number of the package version. A package version number
has a _`majorNumber.minorNumber`_ format.

Declarative Metadata Sample Definition

The following sample creates the `MyhelloWorld.cls` class, and the corresponding `MyHelloWorld.cls-meta.xml`
metadata file.

`MyHelloWorld.cls` file:

```
   public class MyHelloWorld {

   // This method updates the Hello field on a list

   // of accounts.

   public static void addHelloWorld(Account[] accs){

    for (Account a:accs){

     if (a.Hello__c != 'World')

     a.Hello__c = 'World';

     }

    }

   }

```

`MyHelloWorld.cls-meta.xml` :

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ApexClass xmlns="http://soap.sforce.com/2006/04/metadata">

```


### Metadata Types ApexComponent

```
      <apiVersion>66.0</apiVersion>

   </ApexClass>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

ApexTrigger

### ApexComponent

Represents a Visualforce component.

For more information, see Visualforce in Salesforce Help and StaticResource: MetadataWithContent on page 2327

Declarative Metadata File Suffix and Directory Location

The file suffix is `.component` for the page file. The accompanying metadata file is named _`ComponentName`_ `-meta.xml` .

Visualforce components are stored in the `components` folder in the corresponding package directory.

Version

Visualforce components are available in API version 12.0 and later.

Fields

This metadata type contains the following fields:

**Field Name** **Field Type** **Description**

`apiVersion` double The API version for this Visualforce component. Every component has an API
version specified at creation. This field is available in API version 16.0 and later.

`content` base64Binary The component content. Base 64-encoded binary data. Before making an API
call, client applications must encode the binary attachment data as base64. Upon

receiving a response, client applications must decode the base64 data to binary.
This conversion is handled for you by a SOAP client. This field is inherited from
the MetadataWithContent component.

`description` string A description of what the component does.

`fullName` string The component developer name used as a unique identifier for API access. The
`fullName` can contain only underscores and alphanumeric characters. It must

be unique, begin with a letter, not include spaces, not end with an underscore,
and not contain two consecutive underscores. This field is inherited from the
Metadata component.


### Metadata Types ApexEmailNotifications

**Field Name** **Field Type** **Description**

`label` string Required. The label for this component.

`packageVersions` PackageVersion[]

The list of installed managed package versions that are referenced by this
Visualforce component.

Package components and Visualforce custom component are distinct concepts.
A package is comprised of many elements, such as custom objects, Apex classes
and triggers, and custom pages and components.

[For more information about managed packages, see Second-Generation](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_dev2gp.htm)
[Managed Packages in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_dev2gp.htm) _Salesforce DX Developer Guide_ . This field is available in
API version 16.0 and later.

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

ApexPage

### ApexEmailNotifications

The ApexEmailNotifications type allows you to define users and email addresses that receive email for unhandled Apex errors. Flow
errors can also use this metadata type.

Declarative Metadata File Suffix and Directory Location

The component filename is `apexEmailNotifications.notifications` . The Apex email notification file is stored in the
`apexEmailNotifications` folder in the corresponding package directory.

Version

### ApexEmailNotifications components are available in API version 49.0 and later.

Fields

**Field Name** **Field Type** **Description**

### apexEmailNotification ApexEmailNotification A specific Apex email notification. You can specify multiple notifications. ApexEmailNotification

Represents an Apex email notification.


Metadata Types ApexEmailNotifications

Note: Each ApexEmailNotification can contain an email or a user but not both.

**Field Name** **Field Type** **Description**

`email` string The external email address to which the notification is sent. Mutually exclusive
with the `user` field.

`user` string The username of the Salesforce user to be notified. Mutually exclusive with the
`email` field.

Usage

Deploying ApexEmailNotifications deletes all previous notifications in the org. For example, consider two notifications, test1@example.com
and test2@example.com, that are deployed in an org. When the following `apexEmailNotifications.notifications` is
deployed, test1@example.com is deleted, because it's not in the deployed list.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ApexEmailNotifications xmlns="http://soap.sforce.com/2006/04/metadata">

      <apexEmailNotification>

        <email>test2@example.com</email>

      </apexEmailNotification>

   </ApexEmailNotifications>

```

Note: The ApexEmailNotifications metadata type isn't supported in `destructiveChanges.xml` . To delete specific
ApexEmailNotification items, deploy a new ApexEmailNotifications without those items. To delete all Apex email notifications in
an org, deploy an empty list of ApexEmailNotifications.

Declarative Metadata Sample Definition

To deploy Apex email notifications, you can specify either the exact file name or use a wildcard in `package.xml` .

This example specifies the exact file name in `package.xml` .

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>apexEmailNotifications</members>

        <name>ApexEmailNotifications</name>

      </types>

      <version>49.0</version>

   </Package>

```

This example uses a wildcard in `package.xml` .

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>ApexEmailNotifications</name>

      </types>

      <version>49.0</version>

   </Package>

```


### Metadata Types ApexPage

This sample deploys an Apex email notification that notifies a Salesforce user in the org.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ApexEmailNotifications xmlns="http://soap.sforce.com/2006/04/metadata">

      <apexEmailNotification>

        <user>user1@example.com</user>

      </apexEmailNotification>

   </ApexEmailNotifications>

```

This sample deploys an Apex email notification that notifies an external email address.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ApexEmailNotifications xmlns="http://soap.sforce.com/2006/04/metadata">

      <apexEmailNotification>

        <email>test@example.com</email>

      </apexEmailNotification>

   </ApexEmailNotifications>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### ApexPage

Represents a Visualforce page.

For more information, see _Visualforce_ in Salesforce Help. This type extends the MetadataWithContent metadata type and inherits its
`content` and `fullName` fields.

Declarative Metadata File Suffix and Directory Location

The file suffix is `.page` for the page file. The accompanying metadata file is named _`PageName`_ `-meta.xml` .

Visualforce pages are stored in the `pages` folder in the corresponding package directory.

Version

Visualforce pages are available in API version 11.0 and later.

Fields

This metadata type contains the following fields:

**Field Name** **Field Type** **Description**

`apiVersion` double

Required. The API version for this page. Every page has an API version
specified at creation. This field is available in API version 15.0 and later.
If you set this field to a number lower than 15.0, it’s changed to 15.0.


Metadata Types ApexPage

**Field Name** **Field Type** **Description**

`content` base64Binary The page content. Base 64-encoded binary data. Before making an
API call, client applications must encode the binary attachment data

as base64. Upon receiving a response, client applications must decode
the base64 data to binary. This conversion is handled for you by a
SOAP client. This field is inherited from the MetadataWithContent
component.

`description` string A description of what the page does.

`fullName` string The page developer name used as a unique identifier for API access.
The `fullName` can contain only underscores and alphanumeric

characters. It must be unique, begin with a letter, not include spaces,
not end with an underscore, and not contain two consecutive
underscores. This field is inherited from the Metadata component.

`availableInTouch` boolean Indicates if Visualforce tabs associated with the Visualforce page can
be used in the Salesforce mobile app. (Use of this field for Salesforce

Touch is deprecated.). This field is available in API version 27.0 and
later.

Standard object tabs that are overridden with a Visualforce page aren’t
supported in the Salesforce mobile app, even if you set this field for
the page. The default page for the object is displayed instead of the
Visualforce page.

`confirmationTokenRequired` boolean

Indicates whether `GET` requests for the page require a CSRF
confirmation token. This field is available in API version 28.0 and later.

If you change this field’s value from `false` to `true`, links to the
page require a CSRF token to be added to them, or the page is
inaccessible.

`label` string Required. The label for this page.

`packageVersions` PackageVersion[]

The list of installed managed package versions that are referenced by
this Visualforce page.

For more information about managed packages, see
[Second-Generation Managed Packages in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_dev2gp.htm) _Salesforce DX Developer_
_Guide_ . This field is available in API version 16.0 and later.

Declarative Metadata Sample Definition

The following sample creates the `MyPage.page` page, and the corresponding `MyPage.page-meta.xml` metadata file.

`SampleApexPage.page` file:

```
<apex:page>

<h1>Congratulations</h1>

This is your new Page.

</apex:page>

```


### Metadata Types ApexTestSuite

`SampleApexPage.page-meta.xml` :

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ApexPage xmlns="http://soap.sforce.com/2006/04/metadata">

      <description>This is a sample Visualforce page.</description>

      <label>SampleApexPage</label>

   </ApexPage>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

ApexComponent

### ApexTestSuite

Represents a suite of Apex test classes to include in a test run.

File Suffix and Directory Location

### ApexTestSuite components have the suffix .testSuite and are stored in the testSuites folder.

Version

### ApexTestSuite components are available in API version 38.0 and later.

Fields

**Field Name** **Field Type** **Description**

`testClassName` string[] A list of Apex test classes, specified by name, to include in this
test suite.

Declarative Metadata Sample Definition

To include namespaced tests in an Apex test suite, specify each namespace individually. Local Apex tests consist of all tests in the org
that don’t originate from managed packages.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ApexTestSuite xmlns="http://soap.sforce.com/2006/04/metadata">

     <testClassName> LocalTestClass </testClassName>

       <!-- LocalTestClass adds the test class named LocalTestClass. -->

     <testClassName> A*Class </testClassName>

       <!-- A*Class adds AClass, AnotherClass, AwesomeClass, and so on. -->

```


### Metadata Types ApexTrigger

```
     <testClassName> Namespace1.NamespacedTestClass </testClassName>

     <testClassName>*</testClassName> <!-- Adds all local tests. -->

     <testClassName> Namespace1 .*</testClassName> <!-- Adds all tests in Namespace1. -->

     <testClassName> Namespace2 .*</testClassName> <!-- Adds all tests in Namespace2. -->

   </ApexTestSuite>

```

These syntaxes are supported in `package.xml` . If the test classes in your suites are already present in the target org, you can omit
the `ApexClass` type in `package.xml` .

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

     <types>

       <members>*</members>

       <name>ApexClass</name>

     </types>

     <types>

       <members>*</members>

       <name>ApexTestSuite</name>

     </types>

     <version>38.0</version>

   </Package>

   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

     <types>

       <members>*</members>

       <name>ApexClass</name>

     </types>

     <types>

       <members> Suite1 </members>

       <members> Suite2 </members>

       <name>ApexTestSuite</name>

     </types>

     <version>38.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### ApexTrigger

Represents an Apex trigger. A trigger is Apex code that executes before or after specific data manipulation language (DML) events occur,
such as before object records are inserted into the database, or after records have been deleted.

For more information, see “Manage Apex Triggers” in Salesforce Help. This type extends the MetadataWithContent metadata type and
inherits its `content` and `fullName` fields.


Metadata Types ApexTrigger

Supported Calls

All Metadata API calls except CRUD-Based Calls, which prevents deployment outside of proper deployment lifecycle and test-execution
constraints.

Declarative Metadata File Suffix and Directory Location

The file suffix is `.trigger` for the trigger file. The accompanying metadata file is named _`TriggerName`_ `-meta.xml` .

Apex triggers are stored in the `triggers` folder in the corresponding package directory.

Version

Triggers are available in API version 10.0 and later.

Fields

This metadata type contains the following fields:

**Field Name** **Field Type** **Description**

`apiVersion` double Required. The API version for this trigger. Every trigger has an API version specified
at creation.

`content` base64 The Apex trigger definition. This field is inherited from the MetadataWithContent
component.

`fullName` string The Apex trigger name. The name can only contain characters, letters, and the
underscore (_) character, must start with a letter, and can’t end with an

underscore or contain two consecutive underscore characters. This field is
inherited from the Metadata component.

`packageVersions` PackageVersion[]

The list of installed managed package versions that are referenced by this Apex
trigger.

[For more information about managed packages, see the Second-Generation](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp.htm)
[Managed Packaging Developer Guide. This field is available in API version 16.0](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp.htm)
and later.

`status` ApexCodeUnitStatus Required. The status of the Apex trigger. The following string values are valid:
(enumeration of type string)

**•** `Active`                    - The trigger is active.

**•** `Inactive`                    - The trigger is inactive, but not deleted.

**•** `Deleted`                    - The trigger is marked for deletion. Useful for managed packages,
because it allows a trigger to be deleted when a managed package is
updated.


### Metadata Types AppMenu

Declarative Metadata Sample Definition

The following sample creates the `MyhelloWorld.trigger` trigger, and the corresponding
`MyHelloWorld.trigger-meta.xml` metadata file.

`MyHelloWorld.trigger` file:

```
   trigger helloWorldAccountTrigger on Account (before insert) {

     Account[] accs = Trigger.new;

     MyHelloWorld.addHelloWorld(accs);

   }

```

`MyHelloWorld.trigger-meta.xml` :

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ApexTrigger xmlns="http://soap.sforce.com/2006/04/metadata">

      <apiVersion>66.0</apiVersion>

   </ApexTrigger>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

ApexClass

### AppMenu

Represents the app menu or the Salesforce mobile navigation menu. Reserved for future use.

### AppointmentAssignmentPolicy

Represents the information about a resource assignment rule.This type extends the Metadata metadata type and inherits its `fullName`
field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### AppointmentAssignmentPolicy components have the suffix .policy and are stored in the appointmentSchedulingPolicies

folder.

Version

AppointmentSchedulingPolicy components are available in API version 53.0 and later.


Metadata Types AppointmentAssignmentPolicy

Fields

**Field Name** **Field Type** **Description**

`masterLabel` string Required. The label for the appointment assignment policy.

`policyApplicableDuration` string Required. The frequency at which the utilization of service resources is
calculated. Valid values are:

**•** `Monthly`

**•** `ParameterBased`

**•** `Weekly`

`policyType` string Required. The type of appointment assignment policy. Valid value is:

**•** `loadBalancing`

`utilizationFactor` string Required. Specifies the count type for the resource utilization. Valid values
are:

**•** `NumberOfAppointments`

**•** `TotalAppointmentDuration`

Declarative Metadata Sample Definition

The following is an example of an appointmentAssignmentPolicy component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <AppointmentAssignmentPolicy xmlns="http://soap.sforce.com/2006/04/metadata">

     <masterLabel>loadBalancing Assignment Policy</masterLabel>

     <policyType>loadBalancing</policyType>

     <policyApplicableDuration>Weekly</policyApplicableDuration>

     <utilizationFactor>TotalAppointmentDuration</utilizationFactor>

   </AppointmentAssignmentPolicy>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

     <types>

      <members>sample</members>

      <name>AppointmentAssignmentPolicy</name>

     </types>

     <version>53.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


### Metadata Types AppointmentSchedulingPolicy AppointmentSchedulingPolicy

Represents a set of rules for scheduling appointments using Lightning Scheduler. This type extends the Metadata metadata type and
inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### AppointmentSchedulingPolicy components have the suffix .policy and are stored in the appointmentSchedulingPolicies

folder.

Version

### AppointmentSchedulingPolicy components are available in API version 47.0 and later.

Special Access Rules

You must have the ViewSetup and CustomizeApplication user permissions to access the AppointmentSchedulingPolicy type.

Fields

**Field Name** **Field Type** **Description**

`appointmentAssignmentPolicy` string The name of the appointment assignment policy. This field is available
in API version 53.0 and later.

`appointmentStartTimeInterval` picklist Required. The proposed time interval in minutes between appointment
start times. For example, if you set the interval to `15`, appointments can

then begin at the top of the hour and at 15-minute intervals thereafter
(10:00 AM, 10:15 AM, 10:30 AM, and so on). Valid values are:

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


Metadata Types AppointmentSchedulingPolicy

**Field Name** **Field Type** **Description**

**•** `300`

**•** `360`

**•** `420`

**•** `480`

`extCalEventHandler` lookup Required. The API name of the custom Apex class that checks service
resources’ external calendar events and returns the time slots where

service resources are already booked. Available in API version 50.0 and
later.

`isSvcTerritoryMemberShiftUsed` boolean Required. Indicates whether to consider shifts of service territory
members when determining the availability of service resources for

appointments ( `true` ) or not ( `false` ). This field is available in API
version 54.0 and later.

`isSvcTerrOpHoursWithShiftsUsed` boolean Required. Indicates whether to consider the intersection of shifts and
service territory operating hours when determining the availability of

service resources for appointments ( `true` ) or not ( `false` ). This field
is available in API version 54.0 and later.

`masterLabel` string Required. The label for the appointment scheduling policy.

`shouldCheckExternalCalendar` boolean

`shouldConsiderCalendarEvents` boolean

`shouldEnforceExcludedResource` boolean

`shouldEnforceRequiredResource` boolean

`shouldMatchSkill` boolean

`shouldMatchSkillLevel` boolean

`shouldRespectVisitingHours` boolean

Required. Indicates whether to check the external calendar for resource
availability ( `true` ) or not ( `false` ). This field is available in API version
53.0 and later.

Required. Indicates whether to consider events on the Salesforce calendar
to determine the availability of service resources to be assigned to
appointments ( `true` ) or not ( `false` ).

Required. Indicates whether this appointment scheduling policy prevents
excluded service resources from being assigned to appointments ( `true` )
or not ( `false` ).

Required. Indicates whether this appointment scheduling policy allows
only required service resources to be assigned to appointments ( `true` )
or not ( `false` ).

Required. Indicates whether this appointment scheduling policy allows
only required service resources who have certain skills to be assigned
to appointments ( `true` ) or not ( `false` ).

Required. Indicates whether this appointment scheduling policy allows
only required service resources who have certain skills and skill levels to
be assigned to appointments ( `true` ) or not ( `false` ).

Required. Indicates whether this appointment scheduling policy prevents
users from scheduling appointments outside of an account’s visiting
hours ( `true` ) or not ( `false` ).


Metadata Types AppointmentSchedulingPolicy

**Field Name** **Field Type** **Description**

`shouldUsePrimaryMembers` boolean

`shouldUseSecondaryMembers` boolean

Required. Indicates whether this appointment scheduling policy allows
only service resources who are primary members of a service territory
to be assigned to appointments ( `true` ) or not ( `false` ).

Required. Indicates whether this appointment scheduling policy allows
service resources who are secondary members of a service territory to
be assigned to appointments ( `true` ) or not ( `false` ).

Declarative Metadata Sample Definition

The following is an example of an appointmentSchedulingPolicy component.

```
<?xml version="1.0" encoding="UTF-8"?>

<AppointmentSchedulingPolicy xmlns="http://soap.sforce.com/2006/04/metadata">

  <appointmentAssignmentPolicy>ResourceAssignmentRule1</appointmentAssignmentPolicy>

  <appointmentStartTimeInterval>15</appointmentStartTimeInterval>

  <masterLabel>Default Appointment Scheduling Policy</masterLabel>

  <shouldCheckExternalCalendar>true</shouldCheckExternalCalendar>

  <shouldConsiderCalendarEvents>true</shouldConsiderCalendarEvents>

  <shouldEnforceExcludedResource>true</shouldEnforceExcludedResource>

  <shouldEnforceRequiredResource>true</shouldEnforceRequiredResource>

  <shouldMatchSkill>true</shouldMatchSkill>

  <shouldMatchSkillLevel>false</shouldMatchSkillLevel>

  <shouldRespectVisitingHours>true</shouldRespectVisitingHours>

  <shouldUsePrimaryMembers>true</shouldUsePrimaryMembers>

  <shouldUseSecondaryMembers>true</shouldUseSecondaryMembers>

</AppointmentSchedulingPolicy>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

 <Package xmlns="http://soap.sforce.com/2006/04/metadata">

  <types>

   <members>sample</members>

   <name>AppointmentSchedulingPolicy</name>

  </types>

  <version>47.0</version>

 </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


### Metadata Types ApprovalProcess ApprovalProcess

Represents the metadata associated with an approval process. An approval process automates how records are approved in Salesforce.
An approval process specifies each step of approval, including who to request approval from and what to do at each point of the process.

This type extends the Metadata metadata type and inherits its `fullName` field.

Note:

**•** To use approval processes on Salesforce Knowledge articles with the Metadata API, the article type must be deployed. For
article version (_kav) in approval processes, the supported action types are: Knowledge Action, Email Alert, Field Update, and
Outbound Message.

**•** Send actions and approval processes for email drafts aren’t supported in the Metadata API.

**•** The metadata doesn’t include the order of active approval processes. Sometimes you have to reorder the approval processes
in the destination org after deployment.

File Suffix and Directory Location

### ApprovalProcess components have the suffix .approvalProcess and are stored in the approvalProcesses folder.

Version

### ApprovalProcess components are available in API version 28.0 and later.

Fields

**Field Name** **Field Type** **Description**

`active` boolean

`allowRecall` boolean

Required. Whether the approval process is active.

After an approval process is activated, you can’t add, delete,
or change the order of the steps or change its reject or skip
behavior, even if the process is inactive.

Whether to allow submitters to recall approval requests.

If set to `false`, only administrators can recall approval
requests.

`allowedSubmitters` ApprovalSubmitter[] Required. An array of users who are allowed to submit records
for approval.

`approvalPageFields` ApprovalPageField

Specifies which fields to display on the approval page, where
the approver goes to approve or reject the record. By default,
the approval page displays the following:

**•** `Name` field

**•** `Owner` field (except for child objects)

If you enable notifications in the Salesforce mobile app, keep
in mind that approvers can view this list of fields on a mobile


Metadata Types ApprovalProcess

**Field Name** **Field Type** **Description**

device. Select only the fields necessary for users to decide
whether to approve or reject records.

`approvalStep` ApprovalStep[] An array of approval step definitions.

`description` string Describes the approval process.

`emailTemplate` string

Specifies which Classic email template to use for approval
requests. If not specified, the default email template is used.

Lightning email templates aren’t packageable. We recommend
using a Classic email template.

When an approval process assigns an approval request to a
user, Salesforce sends the user an approval request email.

`enableMobileDeviceAccess` boolean Whether users can access an external version of the approval
page from any browser, including browsers on mobile devices,

without logging in to Salesforce. Corresponds to `Security`
`Settings` in the user interface.

If set to `true`, approval steps can’t have approvers of `type`
`adhoc` .

If set to `false`, approvers must log in to Salesforce to access
the approval page.

`entryCriteria` ApprovalEntryCriteria

Determines which records can enter the approval process.
Exclude this field to allow all records to enter the approval
process.

When you deploy an approval process with no entry criteria
to overwrite an existing approval process with entry criteria,

then the entry criteria from the existing process are applied
to the deployed process.

`finalApprovalActions` ApprovalAction Specifies which workflow actions to execute when all required
approvals have been given for a record.

`finalApprovalRecordLock` boolean Whether to keep the record locked after it receives all necessary
approvals. Default: `false` .

`finalRejectionActions` ApprovalAction Specifies which workflow actions to execute after a record
enters the final rejection state.

`finalRejectionRecordLock` boolean Whether to keep the record locked after it’s finally rejected.
Default: `false` .

`initialSubmissionActions` ApprovalAction Specifies which workflow actions to execute when a record is
initially submitted for approval.

`label` string Required. Name of the approval process.


Metadata Types ApprovalProcess

**Field Name** **Field Type** **Description**

`nextAutomatedApprover` NextAutomatedApprover

`postTemplate` string

Specifies a standard or custom user hierarchy field that can be
used to automatically assign the approver for an approval step.

If you exclude this field, then no approval step can use a user
hierarchy field to automatically assign the approver.

Post template to use for Approvals in Chatter.

Chatter post approval notifications are only available for
approval processes associated with an object that has been
enabled for feed tracking.

`recallActions` ApprovalAction Specifies which workflow actions to execute when a pending
approval request is withdrawn.

`recordEditability` RecordEditabilityType Specifies which users can edit records that are pending
(enumeration of type string) approval. When a record is submitted for approval, it’s

automatically locked to prevent other users from editing it
during the approval process. Valid values are:

**•** `AdminOnly` —Records pending approval can be edited
by:

**–** Users with the “Modify All Data” permission

**–** Users with the “Modify All Records” object-level
permission for the given object

**•** `AdminOrCurrentApprover` —Records pending
approval can be edited by:

**–** Users with the “Modify All Data” permission

**–** Users with the “Modify All Records” object-level
permission for the given object

**–** The assigned approver, who must have edit access to
the record through user permissions and the
organization-wide sharing defaults for the given object

`showApprovalHistory` boolean Whether to add the Approval History related list to the
approval page, which is where the approver can view the

approval request details and approve or reject the record. The
Approval History related list tracks a record through the
approval process.

If you also want to add the Approval History related list to
record detail and edit pages, use the Salesforce user interface
to customize the page layouts for the given object.

ApprovalSubmitter

Represents a user or set of users who can submit records for approval.


Metadata Types ApprovalProcess

**Field Name** **Field Type** **Description**

`submitter` string

Identifies a specific user or set of users who can submit records for approval. This field
is required, except when the following types are specified and the `submitter`
field is ignored:

**•** `owner`

**•** `creator`

**•** `allInternalUsers`

Example:

```
<allowedSubmitters>

   <type>allInternalUsers</type>

</allowedSubmitters>

<allowedSubmitters>

   <submitter>myGroup</submitter>

   <type>group</type>

</allowedSubmitters>

```

```
type

```

ProcessSubmitterType Required. Type of user or set of users who can submit records for approval. Valid values
(enumeration of type are:
string)

**•** `group`

**•** `role`

**•** `user`

**•** `roleSubordinates`

**•** `roleSubordinatesInternal`

**•** `owner`

**•** `creator`

**•** `partnerUser`

**•** `customerPortalUser`

**•** `portalRole`

**•** `portalRoleSubordinates`

**•** `allInternalUsers` —all Salesforce users in the organization

ApprovalPageField

Represents the selection of fields to display on the approval page, where an approver can view the approval request details and approve
or reject the record.

**Field Name** **Field Type** **Description**

`field` string[] An array of fields that are displayed on the page for the approver to approve
or reject the record.


Metadata Types ApprovalProcess

ApprovalStep

Represents a step in the approval process. Approval steps define the chain of approval for a particular approval process. Each step
determines which records can advance to that step, who to assign approval requests to, and whether to let each approver’s delegate
respond to the requests. The first step specifies what to do if a record doesn’t advance to that step. Later steps specify what happens if
an approver rejects the request.

Note:

**•** The order of the `ApprovalStep` entries in the approval process definition determines the order in which the approval
steps are executed.

**•** After an approval process is activated, you can’t add, delete, or change the order of the steps or change its reject or skip
behavior, even if the process is inactive.

**•** Each approval process supports up to 30 steps.

**Field Name** **Field Type** **Description**

`allowDelegate` boolean

Whether to allow delegated approvers in this step of the
approval process. A delegated approver is a user appointed by
an assigned approver as an alternate for approval requests.

`approvalActions` ApprovalAction Specifies which workflow actions to execute when a record is
approved in this step of the approval process.

`assignedApprover` ApprovalStepApprover Specifies the assigned approvers for this step of the approval
process.

`description` string Describes the approval step.

`entryCriteria` ApprovalEntryCriteria Determines which records can enter this step of the approval
process.

`ifCriteriaNotMet` StepCriteriaNotMetType Specifies what to do for records that don't meet the entry
(enumeration of type string) criteria. Valid values are:

**•** `ApproveRecord` —Approve the request and execute
all final approval actions.

**•** `RejectRecord` —Reject the request and execute all
final rejection actions. This option is available only for the
first step in the approval process.

**•** `GotoNextStep` —Skip to the next approval step. If you
select this option for the first approval step, and a record
doesn’t meet the entry criteria for any other step, the record
is rejected.

`label` string Required. Name of the approval step.

`name` string Required. Unique name of the approval step. It must contain
only underscores and alphanumeric characters, begin with a

letter, not include spaces, not end with an underscore, and not
contain two consecutive underscores. The requirement for
uniqueness is only within the specific approval process.


Metadata Types ApprovalProcess

**Field Name** **Field Type** **Description**

`rejectBehavior` ApprovalStepRejectBehavior Required, except for the first step in the approval process.
Specifies what happens if the approver rejects the request

during this approval step, unless it's the first step in the approval
process.

If the approver rejects the request in the first step in the approval
process, the reject behavior is determined by the
`finalRejectionActions` .

`rejectionActions` ApprovalAction Specifies which workflow actions to execute when a record is
rejected in this step of the approval process.

ApprovalAction

Represents the actions that occur as a result of an approval process.

**Field Name** **Field Type** **Description**

`action` WorkflowActionReference[] An array of workflow actions to execute.

ApprovalStepApprover

Represents the assigned approvers for an approval step. Each step supports up to 25 approvers.

**Field Name** **Field Type** **Description**

`approver` Approver[] An array of assigned approvers for this step of the approval process.

```
whenMultipleApprovers

```

Approver

RoutingType Specifies how to handle approval or rejection when multiple approvers
(enumeration of are assigned to the step. Valid values are:
type string)

**•** `Unanimous` —(Default) Require unanimous approval from all
approvers for this step. If any of the approvers reject the request, the
approval request for this step is rejected.

**•** `FirstResponse` —Approve or reject based on the first response.

Represents an assigned approver for an approval step. Check out _Considerations for Setting Approvers_ in Salesforce Help.

**Field Name** **Field Type** **Description**

`name` string Identifies an assigned approver. This field is required, except when the `type` is one of
the following and the `name` is ignored:

**•** `adhoc`

**•** `userHierarchyField`


Metadata Types ApprovalProcess

**Field Name** **Field Type** **Description**

```
type

```

NextOwnerType Combined with the specified `name`, `type` identifies an assigned approver. Valid values
(enumeration of type are:
string)

**•** `adhoc` —The approver for the step must be selected manually. For the first step, the
submitter selects the approver. For the second and later steps, the approver for the
previous step selects the approver. For this value, exclude the `name` field.

**•** `user` —A user in your organization. For this value, enter a username for the `name`
field.

**•** `userHierarchyField` —A user specified in a standard or custom user hierarchy
field, such as the standard `Manager` field. For this value, exclude the `name` field.
The user hierarchy field must be defined in the nextAutomatedApprovers for the
approval process.

**•** `relatedUserField` —A user specified in a user lookup field on the submitted
record, such as the `Last Modified By` field. For this value, enter the name of
the user lookup field for the `name` field.

**•** `queue` —Automatically assign to a queue. For this value, enter the name of the queue
for the `name` field.

ApprovalEntryCriteria

Represents the criteria that records must meet to enter the approval process or an approval step. Specify either filter criteria or a formula,
but not both.

**Field Name** **Field Type** **Description**

`booleanFilter` string Filter logic for `criteriaItems` . Exclude this field if you enter a `formula` .

`criteriaItems` FilterItem[]

Filter criteria that a record must meet to enter the approval process or approval
step.

Approval processes don’t support `valueField` entries in filter criteria.

`formula` string Formula that must evaluate to true for a record to enter the approval process
or approval step.

ApprovalStepRejectBehavior

Represents what happens if the approver rejects the request during this approval step, unless it's the first step in the approval process.
For the first step in the approval process, the reject behavior is determined by the approval process's final rejection actions.

**Field Name** **Field Type** **Description**

`type` StepRejectBehaviorType Not allowed in the first step of the approval process. Valid values are:
(enumeration of type string)

**•** `RejectRequest` —Rejects the request even if previous steps were approved.
Salesforce performs all rejection actions specified for this step and all final rejection
actions.


Metadata Types ApprovalProcess

**Field Name** **Field Type** **Description**

**•** `BackToPrevious` —Rejects the request, and returns the approval request to
the previous approver. Salesforce performs all rejection actions specified for this
step.

NextAutomatedApprover

Represents the user hierarchy field to use as the next automated approver for the approval process. If defined, the user specified in the
hierarchy field can be automatically assigned as the approver in one or more approval steps.

**Field Name** **Field** **Description**
**Type**

`useApproverFieldOfRecordOwner` boolean Required. Whether the first executed approval step uses the specified
`userHierarchyField` in the record owner’s user record—instead

of the submitter’s user record—as the approver. All remaining steps use
the specified `userHierarchyField` in the user record of the
preceding step’s approver.

`userHierarchyField` string Required. Standard or custom user hierarchy field whose value specifies
which user to assign as the approver. For example, the standard

`Manager` hierarchy field can be used to assign approvers for employee
PTO (paid time off) requests.

Declarative Metadata Sample Definition

The following is an example of an ApprovalProcess component:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ApprovalProcess xmlns="http://soap.sforce.com/2006/04/metadata">

      <active>false</active>

      <allowRecall>false</allowRecall>

      <allowedSubmitters>

        <type>owner</type>

      </allowedSubmitters>

      <allowedSubmitters>

        <submitter>USSalesRep</submitter>

        <type>role</type>

      </allowedSubmitters>

      <allowedSubmitters>

        <submitter>MarketingGroup</submitter>

        <type>group</type>

      </allowedSubmitters>

      <allowedSubmitters>

        <submitter>kcooper@example.com</submitter>

        <type>user</type>

      </allowedSubmitters>

      <approvalPageFields>

        <field>Name</field>

```


Metadata Types ApprovalProcess

```
        <field>Owner</field>

        <field>MyLeadCustomField__c</field>

        <field>Address</field>

      </approvalPageFields>

      <approvalStep>

        <allowDelegate>false</allowDelegate>

        <approvalActions>

           <action>

             <name>LeadApprovedTask1</name>

             <type>Task</type>

           </action>

           <action>

             <name>LeadApprovedTask2</name>

             <type>Task</type>

           </action>

        </approvalActions>

        <assignedApprover>

           <approver>

             <type>adhoc</type>

           </approver>

        </assignedApprover>

        <label>Step1</label>

        <name>Step1</name>

        <rejectionActions>

           <action>

             <name>LeadRejectedTask</name>

             <type>Task</type>

           </action>

        </rejectionActions>

      </approvalStep>

      <approvalStep>

        <allowDelegate>false</allowDelegate>

        <assignedApprover>

           <approver>

             <type>userHierarchyField</type>

           </approver>

        </assignedApprover>

        <entryCriteria>

           <criteriaItems>

             <field>Lead.CreatedDate</field>

             <operation>greaterThan</operation>

             <value>3/25/2013</value>

           </criteriaItems>

           <criteriaItems>

             <field>User.IsActive</field>

             <operation>notEqual</operation>

             <value>true</value>

           </criteriaItems>

        </entryCriteria>

        <ifCriteriaNotMet>ApproveRecord</ifCriteriaNotMet>

        <label>Step2</label>

        <name>Step2</name>

        <rejectBehavior>

           <type>RejectRequest</type>

```


Metadata Types ApprovalProcess

```
        </rejectBehavior>

      </approvalStep>

      <approvalStep>

        <allowDelegate>true</allowDelegate>

        <assignedApprover>

           <approver>

             <name>MarketingTeamQueue</name>

             <type>queue</type>

           </approver>

           <approver>

             <name>LastModifiedBy</name>

             <type>relatedUserField</type>

           </approver>

           <approver>

             <name>awheeler@example.com</name>

             <type>user</type>

           </approver>

           <whenMultipleApprovers>FirstResponse</whenMultipleApprovers>

        </assignedApprover>

        <entryCriteria>

           <formula>CONTAINS( MyLeadCustomField__c, 'Salesforce')</formula>

        </entryCriteria>

        <label>Step3</label>

        <name>Step3</name>

        <rejectBehavior>

           <type>BackToPrevious</type>

        </rejectBehavior>

      </approvalStep>

      <emailTemplate>MyFolder/LeadsNewassignmentnotification</emailTemplate>

      <enableMobileDeviceAccess>false</enableMobileDeviceAccess>

      <entryCriteria>

        <criteriaItems>

           <field>Lead.AnnualRevenue</field>

           <operation>greaterThan</operation>

           <value>10500</value>

        </criteriaItems>

        <criteriaItems>

           <field>Lead.MyLeadCustomField__c</field>

           <operation>equals</operation>

           <value>Salesforce</value>

        </criteriaItems>

      </entryCriteria>

      <finalApprovalActions>

        <action>

           <name>LeadEmailContacted</name>

           <type>Alert</type>

        </action>

      </finalApprovalActions>

      <finalApprovalRecordLock>true</finalApprovalRecordLock>

      <finalRejectionActions>

        <action>

           <name>ProcessRejectedMessageAction</name>

           <type>OutboundMessage</type>

        </action>

```


### Metadata Types AssignmentRules

```
      </finalRejectionActions>

      <finalRejectionRecordLock>false</finalRejectionRecordLock>

      <initialSubmissionActions>

        <action>

           <name>LeadFieldUpdate</name>

           <type>FieldUpdate</type>

        </action>

        <action>

           <name>NewLeadEmail</name>

           <type>Alert</type>

        </action>

      </initialSubmissionActions>

      <label>SampleProcess</label>

      <nextAutomatedApprover>

        <useApproverFieldOfRecordOwner>false</useApproverFieldOfRecordOwner>

        <userHierarchyField>customlookupuserfield__c</userHierarchyField>

      </nextAutomatedApprover>

      <postTemplate>MyPostTemplate</postTemplate>

      <recallActions>

        <action>

           <name>ProcessRecalledMessageAction</name>

           <type>OutboundMessage</type>

        </action>

      </recallActions>

      <recordEditability>AdminOnly</recordEditability>

      <showApprovalHistory>false</showApprovalHistory>

   </ApprovalProcess>

```

Wildcard Support in the Manifest File

Use the wildcard character `*` (asterisk) in the `package.xml` manifest file to retrieve all approval processes for all objects. You can’t
use it to retrieve a subset of approval processes. Syntax such as `Lead.*` isn’t supported. For information about using the manifest file,
see Deploying and Retrieving Metadata with the Zip File.

### AssignmentRules

Represents assignment rules that allow you to automatically route cases to the appropriate users or queues. You can access rules metadata
for all applicable objects, for a specific object, or for a specific rule on a specific object.

The `package.xml` syntax for accessing all assignment rules for all objects is:

```
      <types>

        <members>*</members>

        <name>AssignmentRules</name>

      </types>

```

All rules for a specific object use a similar syntax without the wildcard. For example, all assignment rules for the Case object would use
this syntax:

```
      <types>

        <members>Case</members>

        <name>AssignmentRules</name>

      </types>

```


Metadata Types AssignmentRules

You can also access specific assignment rules for an object. The following example only accesses the “samplerule” and “newrule”
assignment rules on the Case object. Notice that for this example the type name syntax is `AssignmentRule` and not
`AssignmentRules` .

```
      <types>

        <members>Case.samplerule</members>

        <members>Case.newrule</members>

        <name>AssignmentRule</name>

      </types>

```

File Suffix and Directory Location

Assignment rules for an object have the suffix `.assignmentRules` and are stored in the `assignmentRules` folder. For example,
all Case assignment rules are stored in the `Case.assignmentRules` file.

Version

AssignmentRules components are available in API version 27.0 and later.

Fields

**Field Name** **Field Type** **Description**

`assignmentRule` AssignmentRule[] Represents the definitions of the named assignment rules.

AssignmentRule

Specifies whether the rule is active or not and its definition. Rules are processed in the order they appear within the AssignmentRules
container.

**Field Name** **Field Type** **Description**

`active` boolean Indicates whether the assignment rule is active ( `true` ) or
not ( `false` ).

`fullname` string Inherited from Metadata, this field is defined in the WSDL
for this metadata type. It must be specified when creating,

updating, or deleting. See `createMetadata()` to see
an example of this field specified for a call.

This value can't be `null` .

`ruleEntry` `RuleEntry[]` Represents the type and description for the assignment
rule.

RuleEntry

Represents the fields used by the rule.


Metadata Types AssignmentRules

**Field Name** **Field Type** **Description**

`assignedTo` string The name of the user or queue the item is assigned to.

`assignedToType` `AssignToLookupValueType` Valid values are:
(enumeration of type string)

**•** `User`

**•** `Queue`

`booleanFilter` string Advanced filter conditions that were specified for the rule.

`criteriaItems` `FilterItem[]` The items in the list that define the assignment criteria.

`formula` string

The validation formula.

Specify either `formula` or `criteriaItems`, but not
both fields.

`notifyCcRecipients` boolean Specifies whether email addresses included on the Cc line
of an incoming Email-to-Case or Web-to-Lead message are

included on the Cc line of the auto-response to that
message ( `true` ) or not ( `false` ). Available in API version
32.0 and later.

`overrideExistingTeams` boolean

Specifies whether the case team resets when the
assignment is done `true` ) or if the current team is added
to the case instead of replacing the previous team ( `false` ).

`team` string[] The name of the case team. It can occur 0 or more times.

`template` string

Declarative Metadata Sample Definition

Specifies the template to use for the email that is
automatically sent to the designated recipient.

Lightning email templates aren’t packageable. We
recommend using a Classic email template.

The following is an example file showing two assignment rules on the Case object:

```
<AssignmentRules xmlns="http://soap.sforce.com/2006/04/metadata"

xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

   <assignmentRule>

     <fullName>samplerule</fullName>

     <active>false</active>

     <ruleEntry>

        <assignedTo>testUser@org.com</assignedTo>

        <assignedToType>User</assignedToType>

        <criteriaItems>

          <field>Case.IsEscalated</field>

          <operation>equals</operation>

          <value>True</value>

        </criteriaItems>

        <template>emailtemplate</template>

```


### Metadata Types AssessmentQuestion

```
        </ruleEntry>

      </assignmentRule>

      <assignmentRule>

        <fullName>Another samplerule</fullName>

        <active>false</active>

        <ruleEntry>

           <assignedTo>otherUser@org.com</assignedTo>

           <assignedToType>User</assignedToType>

           <criteriaItems>

             <field>Case.IsEscalated</field>

             <operation>equals</operation>

             <value>False</value>

           </criteriaItems>

           <template>emailtemplate</template>

        </ruleEntry>

      </assignmentRule>

   </AssignmentRules>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### AssessmentQuestion

Represents the container object that stores the questions required for an assessment.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### AssessmentQuestion components have the suffix .AssessmentQuestion and are stored in the AssessmentQuestions

folder.

Version

### AssessmentQuestion components are available in API version 55.0 and later.

Fields

**Field Name** **Description**

```
assessmentQuestionVersion

```

**Field Type**
### AssessmentQuestionVersion


Metadata Types AssessmentQuestion

**Field Name** **Description**

**Description**
The object that stores the question versions for the assessment questions.

```
dataType

developerName

displayTextCategory

formulaResponseDataType

name

questionCategory

```

**Field Type**
string

**Description**
Required.

The data type of the assessment question.

**Field Type**
string

**Description**

Required.

The developer name of the assessment question. Can contain only underscores and
alphanumeric characters and must be unique in your org. It must begin with a letter,
not include spaces, not end with an underscore, and not contain two consecutive
underscores.

**Field Type**
string

**Description**
Specifies the category of the display text when the data type is Text Block.

**Field Type**
string

**Description**
Specifies the data type of the question response calculated by a formula.

**Field Type**
string

**Description**

Required.

The name of the record.

**Field Type**
string

**Description**

Required.

Stores the question category.


Metadata Types AssessmentQuestion

**Field Name** **Description**

```
relatedQuestion

```

**Field Type**
string

**Description**
Specifies the related question. Used to define a question hierarchy.

AssessmentQuestionVersion

Stores the question versions for the assessment questions.

**Field Name** **Description**

```
additionalInformation

description

guidanceInformation

helpText

isActive

name

```

**Field Type**
string

**Description**
The additional details for a UI element, such as the disclosure text.

**Field Type**
string

**Description**
The description for the assessment question. This text isn’t rendered on the assessment.

**Field Type**
string

**Description**
The guidance for the assessment question.

**Field Type**
string

**Description**
The text that's added as an info bubble in the UI element related to the assessment question.

**Field Type**
boolean

**Description**
Required.

Indicates whether the current version of the assessment question is set to active ( `true` )
or not ( `false` ).

The default value is `false` .

**Field Type**
string


Metadata Types AssessmentQuestion

**Field Name** **Description**

**Description**
Required.

Name of the assessment question version record.

```
optionSourceResponseValue

questionText

responseValues

status

versionNumber

```

**Field Type**
boolean

**Description**
Indicates whether the response value source for an assessment question is configured as
custom ( `true` ) or sObject in the OmniStudio designer ( `false` ).

The default value is `false` .

**Field Type**
string

**Description**
Required.

The assessment question text. Contains the label for the assessment question that appears
on the assessment.

**Field Type**
string

**Description**
Holds the values to be defined in the picklist, multiselect picklist, or radio buttons.

**Field Type**
string

**Description**
Required.

Status of the assessment question version. Possible values are Draft, Active, or Archived.

**Field Type**
int

**Description**
Required.

The assessment question version number.

Declarative Metadata Sample Definition

The following is an example of an AssessmentQuestion component.

```
<?xml version="1.0" encoding="UTF-8"?>

```


Metadata Types AssessmentQuestion

```
   <AssessmentQuestion

    xmlns="http://soap.sforce.com/2006/04/metadata">

    <assessmentQuestionVersion>

     <additionalInformation>ParentQuestionDevName AI</additionalInformation>

     <description>ParentQuestionDevName Desc</description>

     <helpText>ParentQuestionDevName HT</helpText>

     <isActive>true</isActive>

     <name>ParentQuestionDevName</name>

     <optionSourceResponseValue>true</optionSourceResponseValue>

     <questionText>ParentQuestionDevName Text</questionText>

     <status>Active</status>

     <versionNumber>1</versionNumber>

    </assessmentQuestionVersion>

    <dataType>DateTime</dataType>

    <developerName>ParentQuestionDevName</developerName>

    <name>ParentQuestionDevName</name>

    <questionCategory>Demographic</questionCategory>

   </AssessmentQuestion>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package

    xmlns="http://soap.sforce.com/2006/04/metadata">

    <types>

     <members>*</members>

     <name>AssessmentQuestion</name>

    </types>

    <version>55.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

Usage

Before you retrieve assessment questions, we recommend that you review these considerations.

**•** When you retrieve an assessment question, you also get the related assessment question version with the status Active..

Note: If an active assessment question version doesn’t exist for the assessment question, then the latest assessment question
version with Status as Draft is retrieved.

**•** The value for the `<status>` tag in the XML definition must match the status of the related assessment question version.

**•** If an assessment question has a related assessment question (parent question), the XML definition must include the developer name
of the related assessment question.

**•** If the fields of an assessment question contain values, the XML definition must contain tags with those values when retrieving it.

Before you deploy assessment questions, we recommend that you review these considerations.

**•** If the Related Question isn’t available in the target org, deploying the assessment question fails.


### Metadata Types AssessmentQuestionSet

**•** If an assessment question with the same developer name exists in the target org, deploying the assessment question updates the
values of the other fields in the target org.

**•** If the `<versionNumber>` tag is present in the XML definition of an assessment question, deploying creates a version for that
question in the target org.

**•** If the Related Questions aren’t available in target org but available in the package, then deploying the questions inserts the Related
Questions in the correct order.

**•** If the assessment questions are associated with flows of type Discovery Framework Data Capture Flow, then deploy the assessment
questions first. After deploying the assessment questions, deploy the flows.

### AssessmentQuestionSet

Represents the container object for Assessment Questions.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### AssessmentQuestionSet components have the suffix .AssessmentQuestionSet and are stored in the AssessmentQuestionSets folder.

Version

### AssessmentQuestionSet components are available in API version 55.0 and later.

Fields

**Field Name** **Description**

```
assessmentQuestionDeveloperNames

developerName

```

**Field Type**
string[]

**Description**
The developer names for the assessment question. Can contain only underscores and
alphanumeric characters and must be unique in your org. It must begin with a letter,
not include spaces, not end with an underscore, and not contain two consecutive
underscores.

**Field Type**
string

**Description**
Required.

The developer name for the assessment question set. Can contain only underscores
and alphanumeric characters and must be unique in your org. It must begin with a


Metadata Types AssessmentQuestionSet

**Field Name** **Description**

letter, not include spaces, not end with an underscore, and not contain two consecutive
underscores.

```
name

```

**Field Type**
string

**Description**
Required.

The question set name.

Declarative Metadata Sample Definition

The following is an example of an AssessmentQuestionSet component.

```
<?xml version="1.0" encoding="UTF-8"?>

<AssessmentQuestionSet

 xmlns="http://soap.sforce.com/2006/04/metadata">

 <developerName>QuestionSetDevName</developerName>

 <name>QuestionSetName</name>

 <assessmentQuestionDeveloperNames>QuestionDevName</assessmentQuestionDeveloperNames>

</AssessmentQuestionSet>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package

 xmlns="http://soap.sforce.com/2006/04/metadata">

 <types>

  <members>*</members>

  <name>AssessmentQuestion</name>

 </types>

 <types>

  <members>*</members>

  <name>AssessmentQuestionSet</name>

 </types>

 <version>55.0</version>

</Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

Usage

Before you retrieve assessment question sets, we recommend that you review these considerations.


### Metadata Types Audience

**•** When retrieving an assessment question set, if its fields contain values, then the XML definition must contain tags with those values.

**•** When retrieving an assessment question set, if that set is associated with multiple questions, then the XML definition must contain
developer names of all the associated questions.

Before you deploy assessment question sets, we recommend that you review these considerations.

**•** When deploying an assessment question set, if an assessment question set with the same developer name doesn't exist in the target
org, deploying creates one with that name.

**•** If an assessment question set with the same developer name exists in the target org, then deploying the question set updates the
values of the other fields in the target org.

**•** If the questions associated with the assessment question set don't exist in the target org, deploying the assessment question set
fails.

**•** If the questions associated with the assessment question set don’t exist in the target org but are available in the package, then
deploying the assessment question sets inserts the questions in the correct order.

### Audience

Represents the audience in an Experience Builder site. An audience consists of different types of criteria, where the audience can be
assigned and used for targeting in a site. This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### Audience components have the suffix .audience and are stored in the audience folder.

Version

### Audience components are available in API version 44.0 and later.

Special Access Rules

Access to the Audience type requires the AudienceMetadata permission. This permission is on by default for orgs that have Networks
enabled.

Access to permission criteria for the Audience type requires the AudiencePermissionCriteria permission. This permission is available in
API version 45.0 and later and is on by default for orgs that have Networks enabled.

Fields

**Field Name** **Field Type** **Description**

`audienceName` string Required. The name of the audience.

`container` string Required. The name of the site or org that contains the audience.

### criteria AudienceCriteria Required. Criteria in an audience. This field is available in API version 47.0

and later.


Metadata Types Audience

**Field Name** **Field Type** **Description**

`criterion` AudienceCriterion[]

Removed. List of criteria in an audience.

This field is available in API version 44.0–46.0. In API version 47.0 and
later, use `criteria` instead.

`description` string The description of the audience.

`formula` string Formula used to determine the audience. This field is available in API
version 45.0 and later.

```
formulaFilterType

```

FormulaFilterType Indicates the audience’s formula type. Valid values are
(enumeration of

**•** `AllCriteriaMatch`

type string)

**•** `AllCriteriaMatch`

**•** `AnyCriterionMatches`

`isDefaultAudience` boolean

**•** `CustomLogicMatches` (available in API version 45.0 and later)

Indicates whether the audience is the default audience ( `true` ) or not
( `false` ). This field is available and required in API version 48.0. In API
version 49.0 and later, this field is optional.

The default audience file name is of format `Default_` _**`Network`**_
_**`Name`**_ `.audience` .

`targets` PersonalizationTarget Targets for the audience. This field is available in API version 47.0 and
Infos later.

AudienceCriteria

Represents criteria for an audience. This subtype is available in API version 47.0 and later.

**Field Name** **Field Type** **Description**

`criterion` AudienceCriterion[] List of criteria for an audience. An audience can have up to 100 criteria.

AudienceCriterion

Represents a criterion for an audience.

**Field Name** **Field Type** **Description**

`criteriaNumber` int The number associated with the criterion in a formula, for example (1 AND 2)
OR 3. This field is available in API version 45.0 and later.

`criterionValue` AudienceCriteriaValue The value of the criterion.

```
operator

```

AudienceCriterion The operator associated with this criterion. Valid values are:
Operator(enumeration

**•** `Equal`

of type string)

**•** `Equal`

**•** `NotEqual`

**•** `GreaterThan`


Metadata Types Audience

**Field Name** **Field Type** **Description**

**•** `GreaterThanOrEqual`

**•** `LessThan`

**•** `LessThanOrEqual`

**•** `Contains`

**•** `StartsWith`

**•** `Includes` (available in API version 45.0 and later)

**•** `NotIncludes` (available in API version 45.0 and later)

```
type

```

AudienceCriterion Required. Valid values are:
Type(enumeration of

**•** `GeoLocation`

type string)

**•** `GeoLocation`

**•** `Domain`

**•** `Profile`

**•** `FieldBased`

**•** `Permission` (available in API version 45.0 and later)

**•** `Default` (available in API version 47.0 and later)

**•** `Audience` (available in API version 53.0 and later)

For a list of AudienceCriteriaValue fields that you can use with each
AudienceCriterion `type` field value, see this table.

AudienceCriteriaValue

Represents the value of a criterion in an audience. For a list of AudienceCriteriaValue fields that you can use with each AudienceCriterion
`type` field value, see this table.

**Field Name** **Field Type** **Description**

`audienceDeveloperName` string

Developer name of the audience. This field is available in API version 53.0 and
later. You can use this field only when the value of the AudienceCriterion `type`
field is `Audience` .

`city` string City of a user. You can use this field only when the value of the
AudienceCriterion `type` field is `GeoLocation` .

`country` string Country of a user. You can use this field only when the value of the
AudienceCriterion `type` field is `GeoLocation` .

`domain` string Domain of a user. You can use this field only when the value of the
AudienceCriterion `type` field is `Domain` .

`entityField` string Field of an object. You can use this field only when the value of the
AudienceCriterion `type` field is `FieldBased` .

`entityType` string Type of object. You can use this field only when the value of the
AudienceCriterion `type` field is `FieldBased` .


Metadata Types Audience

**Field Name** **Field Type** **Description**

`fieldValue` string Value of a field. You can use this field only when the value of the
AudienceCriterion `type` field is `FieldBased` .

`isEnabled` string

`permissionName` string

`permissionType` string

Indicates whether the permission is enabled ( `true` ) or not ( `false` ) for a user.
This field is available in API version 45.0 and later. You can use this field used
only when the value of the AudienceCriterion `type` field is `Permission` .

Valid API name of a standard user or custom permission. This field is available
in API version 45.0 and later. You can use this field only when the value of the
AudienceCriterion `type` field is `Permission` .

Type of permission. Valid values are `Standard` and `Custom` . This field is
available in API version 45.0 and later. You can use this field only when the
value of the AudienceCriterion `type` field is `Permission` .

`profile` string Profile of a user. You can use this field only when the value of the
AudienceCriterion `type` field is `Profile` .

`subdivision` string Subdivision of a user. You can use this field only when the value of the
AudienceCriterion `type` field is `GeoLocation` .

This table summarizes which AudienceCriteriaValue fields you can use with the different AudienceCriterion `type` field values.

**AudienceCriterion Type** **AudienceCriteriaValue Fields**

```
GeoLocation

```

```
city

country

subdivision

```

```
Domain domain

Profile profile

```

```
FieldBased

Permission

```

```
entityField

entityType

fieldValue

isEnabled

permissionName

permissionType

```

```
Audience audienceDeveloperName

```

PersonalizationTargetInfos

Represents targets for an audience. This subtype is available in API version 47.0 and later.

When deploying an audience, you must include ExperienceBundle in your package to support experience variation targets.


Metadata Types Audience

**Field Name** **Field Type** **Description**

`target` PersonalizationTarget List of targets for an audience.
Info[]

PersonalizationTargetInfo

Represents a target for an audience. This subtype is available in API version 47.0 and later.

**Field Name** **Field Type** **Description**

`groupName` string

Required. Group name of the target. Groups bundle related target and audience
pairs. You can have up to 2,000 groups and 500 targets per group.

To determine the target group name, see
h **t** [ps://developer.salesforce.com/docs/atlas.en-us.communities_dev.meta/communities_dev/communities_dev_personalization_names.htm](https://developer.salesforce.com/docs/atlas.en-us.260.0.communities_dev.meta/communities_dev/communities_dev_personalization_names.htm)
in the _Experience Cloud Developer Guide_ .

`priority` int Priority of the target. Within a group, priority determines which target is returned
when the user matches more than one audience.

`targetType` string Required. Type of target, indicating the nature of the data being targeted.
Supported values include:

**•** `ExperienceVariation` (API version 47.0 and later)

**•** `NavigationLinkSet` (API version 49.0 and later)

**•** `Report` (API version 49.0 and later)

**•** `Dashboard` (API version 49.0 and later)

You can have up to 2,500 `ExperienceVariation` targets and 25,000
record targets.

For more information on the `ExperienceVariation` target type, see
ExperienceBundle.

`targetValue` string

Required. Value of the target, which is the developer name of the experience
variation, such as `ContactSupport_ContactSupportFor`
`California_Page` for a page variation.

To determine the target developer name, see
h **t** [ps://developer.salesforce.com/docs/atlas.en-us.communities_dev.meta/communities_dev/communities_dev_personalization_names.htm](https://developer.salesforce.com/docs/atlas.en-us.260.0.communities_dev.meta/communities_dev/communities_dev_personalization_names.htm)
in the _Experience Cloud Developer Guide_ .

Declarative Metadata Sample Definition

The following is an example of an Audience component.

```
<?xml version="1.0" encoding="UTF-8"?>

<Audience xmlns="http://soap.sforce.com/2006/04/metadata">

   <audienceName>Audience Metadata</audienceName>

   <container>Customer</container>

```


Metadata Types Audience

```
      <criteria>

        <criterion>

           <criteriaNumber>1</criteriaNumber>

           <criterionValue>

             <country>United States</country>

             <subdivision>Nevada</subdivision>

           </criterionValue>

           <operator>Equal</operator>

           <type>GeoLocation</type>

        </criterion>

        <criterion>

           <criteriaNumber>2</criteriaNumber>

           <criterionValue>

             <profile>customer community user</profile>

           </criterionValue>

           <operator>Equal</operator>

           <type>Profile</type>

        </criterion>

        <criterion>

           <criteriaNumber>3</criteriaNumber>

           <criterionValue>

             <domain>sampledomain.example.com</domain>

           </criterionValue>

           <operator>Equal</operator>

           <type>Domain</type>

        </criterion>

        <criterion>

           <criteriaNumber>4</criteriaNumber>

           <criterionValue>

            <entityField>Manager.Profile.CreatedBy.Contact.MailingCountry</entityField>

             <entityType>User</entityType>

             <fieldValue>USA</fieldValue>

           </criterionValue>

           <operator>StartsWith</operator>

           <type>FieldBased</type>

        </criterion>

        <criterion>

           <criteriaNumber>5</criteriaNumber>

           <criterionValue>

             <entityField>RecordTypeId</entityField>

             <entityType>CollaborationGroup</entityType>

             <fieldValue>CollaborationGroup.Group_RT2</fieldValue>

           </criterionValue>

           <operator>Equal</operator>

           <type>FieldBased</type>

        </criterion>

        <criterion>

           <criteriaNumber>6</criteriaNumber>

           <criterionValue>

             <isEnabled>true</isEnabled>

             <permissionName>ManageUsers</permissionName>

             <permissionType>Standard</permissionType>

           </criterionValue>

```


Metadata Types Audience

```
           <operator>Equal</operator>

           <type>Permission</type>

        </criterion>

        <criterion>

           <criteriaNumber>7</criteriaNumber>

           <criterionValue>

             <isEnabled>false</isEnabled>

             <permissionName>NamespaceXYZ__CustomPermABC</permissionName>

             <permissionType>Custom</permissionType>

           </criterionValue>

           <operator>Equal</operator>

           <type>Permission</type>

        </criterion>

        <criterion>

           <criteriaNumber>8</criteriaNumber>

           <criterionValue>

             <audienceDeveloperName>Audience1</audienceDeveloperName>

           </criterionValue>

           <operator>Equal</operator>

           <type>Audience</type>

        </criterion>

      </criteria>

      <formula>1 AND (2 OR 3 OR 4 OR 5 OR 6 OR 7) AND 8</formula>

      <formulaFilterType>CustomLogicMatches</formulaFilterType>

      <isDefaultAudience>false</isDefaultAudience>

      <targets>

        <target>

           <groupName>c194d79c-5c6b-4c6a-8d14-0e7042564355$#$Branding</groupName>

           <priority>1</priority>

           <targetType>ExperienceVariation</targetType>

           <targetValue>Customer_Service_testBrandingSet_Branding</targetValue>

        </target>

      </targets>

   </Audience>

```

Usage

You can’t use Metadata API to delete an audience.

In API version 47.0 and later, you can’t create an audience without criteria.

The list of targets provided in the input for an audience is considered the state of target assignments that you want. For example, see
the following information for deleting, creating, and updating targets.

If you don’t have a default audience, updating targets can result in the UI erroneously showing a target assigned to the default audience.
The target assignment data in the API is correct. To work around the UI issue, temporarily assign another target to the default audience
and then delete it.

Personalization using audience targeting varies what the user can see in the browser but doesn’t secure data in any way. To prevent
users accessing sensitive data, use standard Salesforce security features, such as sharing rules and permission sets.

**Delete targets**
To delete a single target from an audience, deploy the entire list of targets for the audience minus the one that you want to delete.


Metadata Types Audience

To delete all the targets from an audience, deploy the audience with empty targets tags. For example:

```
     <?xml version="1.0" encoding="UTF-8"?>

     <Audience

       xmlns="http://soap.sforce.com/2006/04/metadata">

       <audienceName>testAudience</audienceName>

       <container>testContainer</container>

       <criteria>

          <criterion>

            <criteriaNumber>1</criteriaNumber>

            <criterionValue>

               <country>United States</country>

               <subdivision>Nevada</subdivision>

            </criterionValue>

            <operator>Equal</operator>

            <type>GeoLocation</type>

          </criterion>

       </criteria>

       <formulaFilterType>AllCriteriaMatch</formulaFilterType>

       <isDefaultAudience>false</isDefaultAudience>

       <targets>

       </targets>

     </Audience>

```

**Update an audience without updating targets**
To update an audience without updating targets, deploy the audience without targets tags. For example:

```
     <?xml version="1.0" encoding="UTF-8"?>

     <Audience

       xmlns="http://soap.sforce.com/2006/04/metadata">

       <audienceName>testAudience</audienceName>

       <container>testContainer</container>

       <criteria>

          <criterion>

            <criteriaNumber>1</criteriaNumber>

            <criterionValue>

               <country>United States</country>

               <subdivision>Nevada</subdivision>

            </criterionValue>

            <operator>Equal</operator>

            <type>GeoLocation</type>

          </criterion>

       </criteria>

       <formulaFilterType>AllCriteriaMatch</formulaFilterType>

       <isDefaultAudience>false</isDefaultAudience>

     </Audience>

```

**Create targets**
To create a target, deploy the entire list of targets for the audience plus the one that you want to create.

**Update the priority of a target**
To change the priority of a target within an audience, deploy the entire list of targets for the audience with the new priority values
for the targets.

To change the priority of a target that affects priority in another audience, deploy both audiences with their entire list of targets with
the new priority values for the targets.


### Metadata Types AuraDefinitionBundle

**Update the target assignment for an audience**
To reassign a target to a new audience, deploy both audiences with their entire list of targets. Deploy one list with the target removed,
and the other list with the target added.

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### AuraDefinitionBundle

Represents an Aura definition bundle. A bundle contains an Aura definition, such as an Aura component, and its related resources, such
as a JavaScript controller. The definition can be a component, application, event, interface, or a tokens collection.

File Suffix and Directory Location

An AuraDefinitionBundle component is a folder that contains definition files. Unlike most other metadata components, an
### AuraDefinitionBundle component isn’t a single file, it’s a collection of files. Each file represents a resource in a bundle, such as markup,

applications, code files (including controllers and helpers), events, documentation, and interfaces. For example, this directory structure
shows the hierarchy of the folders and files for two bundles: `bundle1` and `bundle2` .

```
   aura

      bundle1

        bundle1.cmp

        bundle1Controller.js

      bundle2

        bundle2.app

        bundle2Controller.js

        bundle2.auradoc

```

Aura definition bundles must be under a top-level folder named `aura` . Each bundle must have its own subfolder under the `aura`
folder. The name of each definition file must start with the bundle name.

A bundle doesn’t have a suffix. Definition files can have one of these suffixes:


Metadata Types AuraDefinitionBundle

Each bundle can have only one file each with a suffix of `.app`, `.cmp`, `.design`, `.evt`, `.intf`, or `.tokens` .

Version

AuraDefinitionBundle components are available in API version 32.0 and later.

Design and SVG components are available in API version 33.0 and later.

In API version 45.0 and later, there are two types of Lightning component: Aura components and Lightning web components. This
metadata type describes an Aura component.

Special Access Rules

Definitions can be created only in organizations with defined namespaces.

Fields

**Field Name** **Field Type** **Description**

`apiVersion` double

The API version for this definition bundle. When you create an Aura
bundle, you can specify the API version to save it with. Available in API
version 35.0 and later.

`auraDefinitions` AuraDefinitions Reserved for internal use.

`controllerContent` base64Binary The content of a JavaScript client-side controller.

`description` string The specification of the Aura bundle. Available in API version 35.0 and
later.

`designContent` base64Binary The content of a design definition. Only valid inside a component bundle.

`documentationContent` base64Binary The content of a documentation definition.

`helperContent` base64Binary The content of a JavaScript helper.

`markup` base64Binary The content of the markup for a definition.

`modelContent` base64Binary Deprecated. Do not use.

`packageVersions` PackageVersion[] The list of installed managed package versions that this Aura definition
bundle references. Available in API version 35.0 and later.

`rendererContent` base64Binary The content of a JavaScript client-side renderer.

`styleContent` base64Binary The CSS for the definition.

`SVGContent` base64Binary The SVG image for the definition.


Metadata Types AuraDefinitionBundle

**Field Name** **Field Type** **Description**

`testsuiteContent` base64Binary Reserved for internal use.

```
type

```

AuraBundleType The definition type. Valid values are:
(enumeration of

**•** `Application`

type string)

**•** `Application`

**•** `Component`

**•** `Event`

**•** `Interface`

**•** `Tokens`

Declarative Metadata Sample Definition

This example shows the directory structure of an AuraDefinitionBundle component.

```
aura

   sampleCmp

     sampleCmp.cmp

     sampleCmpController.js

```

The following samples show the contents of the metadata definition files that correspond to the sample `aura` directory.

Content of `sampleCmp.cmp` :

```
<aura:component>

   <aura:attribute name="val1" type="String" default="Value"/>

   <aura:attribute name="val2" type="String" />

   <aura:handler name="init" value="{!this}" action="{!c.myAction}"/>

     <ui:outputText value='Hello world!'/>

     <ui:outputText value='{!v.val1}'/>

     <ui:outputText value='{!v.val2}'/>

</aura:component>

```

Content of `sampleCmpController.js` :

```
({

  myAction : function(component) {

   component.set('v.val1','Value1');

   component.set('v.val2','Value2');

  }

})

```

This `package.xml` references the definitions of all Lightning components that are present in the `sampleCmp` bundle.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>sampleCmp</members>

     <name>AuraDefinitionBundle</name>

   </types>

   <version>66.0</version>

</Package>

```


### Metadata Types AuthProvider

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### AuthProvider

Represents an authentication provider (auth provider). An auth provider lets users log in to Salesforce from an external service provider
such as Facebook, Google, or GitHub. This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

Authentication providers are stored in the `authproviders` directory. The file name matches the URL suffix, and the extension is
`.authprovider` . For example, an auth provider with URL suffix `FacebookProvider` is stored in
`authproviders/FacebookProvider.authprovider` .

Version

Authentication providers are available in API version 27.0 and later.

Special Access Rules

Only users with the Customize Application and Manage AuthProviders permissions can access this object.

Fields

**Field Name** **Field Type** **Description**

`appleTeam` string

`authorizeUrl` string

`consumerKey` string

Required when using Apple as a third-party authentication provider. A
10-character team ID, obtained from an Apple developer account. Available
in API version 48.0 and later.

Required when creating an OpenID Connect authentication provider. The
OAuth authorization endpoint URL. Available in API version 29.0 and later.

In API version 33.0 and later, for Salesforce-managed auth providers, leave
the field blank to let Salesforce supply and manage the value. For details,
see “Usage.”

The app’s key that is registered at the third-party (external) authentication
provider.

In API version 33.0 and later, for Salesforce-managed auth providers, leave
the field blank to let Salesforce supply and manage the value. For details,
see “Usage.”

`consumerSecret` string The consumer secret of the app that is registered at the third-party provider.
After it’s set, you can’t change the value. When using `create()`, this


Metadata Types AuthProvider

**Field Name** **Field Type** **Description**

field must be encrypted. To create an encrypted form of the consumer
secret from plaintext:

**1.** Create an authentication provider with the `consumerSecret`
plaintext value.

**2.** Save the authentication provider.

**3.** Create an outbound change set that includes the authentication
provider component.

The new change set .xml file has an entry in the form

`<consumerSecret>++XYZ++</consumerSecret>` where
++XYZ++ is the encrypted secret.

In API version 33.0 and later, for Salesforce-managed auth providers, leave
the field blank to let Salesforce supply and manage the value. For details,
see Usage.

If a consumer secret is defined on an authentication provider, the consumer
secret is always exported as a placeholder value, not as an encrypted secret.

```
controlPlane

```

`MuleSoftControlPlane` Required when using MuleSoft as a third-party authentication provider.
(enumeration of Environment where the MuleSoft Anypoint Platform control plane is hosted.
type string) The control plane is the part of the Anypoint Platform architecture that

includes Anypoint Exchange and determines the login URL. If you select
User-Specified, you must enter the Consumer Key and Consumer Secret.
Obtain the values from the MuleSoft connected app that you created to
store the authentication details for your Salesforce org. Available in API
version 57.0 and later. Valid values include:

**•** `None` —User-specified control plane. If you select `None`, you must
enter the Consumer Key and Consumer Secret. Obtain the values from
the MuleSoft connected app that you created to store the
authentication details for your Salesforce org.

**•** `US` —US control plane

**•** `EU` —EU control plane

`customMetadataTypeRecord` string

`defaultScopes` string

Required when creating a custom authentication provider plug-in. The
API name of the custom authentication provider. Available in API version
36.0 and later.

For OpenID Connect authentication providers, the scopes to send with the
authorization request, if not specified when a flow starts. Available in API
version 29.0 and later.

In API version 33.0 and later, for Salesforce-managed auth providers, leave
the field blank to let Salesforce supply and manage the value. See “Usage.”

`ecKey` string Required when using Apple as a third-party authentication provider. A
private key generated by Apple. Available in API version 48.0 and later.

`errorUrl` string A custom error URL for the authentication provider to use to report errors.


Metadata Types AuthProvider

**Field Name** **Field Type** **Description**

`executionUser` string

`flow` string

Required to specify a registration handler. The username of the Salesforce
admin or system user who runs the Apex handler or flow. The execution

user provides the context in which the registration handler runs. For
example, if the handler creates a contact, the creation can be easily traced
back to the registration process. In production, use a system user. The user
must have the Manage Users permission. Available in API version 27.0 and
later.

A flow for the registration handler. The flow must be of the Identity User
Registration Flow type.

You can use either a flow or an Apex class for the registration handler. To
use an Apex class instead, omit the `flow` field and specify an Apex class
in the `registrationHandler` field.

Available in API version 64.0 and later.

`flowDefaultAccount` string For authentication providers that use a flow registration handler, the default
account that new external users are assigned to. If you include this field,

Salesforce automatically uses it for the `defaultAccountId` variable
in the Authentication Provider User Registration standard flow.

A default account is required to use a flow registration handler to create
and update external users. You can specify a default account here or in the
flow itself. If you use both, the default account that's configured in the flow
takes precedent.

Available in API version 64.0 and later.

`flowDefaultProfile` string For authentication providers that use a flow registration handler, the default
profile that new users are assigned to. If you include this field, Salesforce

automatically uses it for the `defaultProfileId` variable in the
Authentication Provider User Registration standard flow.

A default profile is required to use a flow registration handler. You can
specify a default profile here or in the flow itself. If you use both, the default
profile that's configured in the flow takes precedent.

Available in API version 64.0 and later.

`friendlyName` string Required. A user-friendly name for the authentication provider.

`iconUrl` string

The path to an icon to use as a button on the login page. Users click the
button to log in with the associated authentication provider, such as Twitter
or Facebook. Available in API version 32.0 and later.

`idTokenIssuer` string The source of the authentication token in `https:` URI format. This field
is available when configuring an OpenID Connect or Microsoft

authentication provider. If provided, Salesforce validates the returned
`id_token` value. OpenID Connect requires returning an `id_token`
value with the `access_token` value. Available in API version 30.0 and
later.


Metadata Types AuthProvider

**Field Name** **Field Type** **Description**

`includeOrgIdInIdentifier` boolean Used to differentiate between users with the same user ID from two sources
(such as two sandboxes). If enabled ( `true` ), Salesforce stores the org ID

of the third-party identity in addition to the user ID. After you enable this
setting, you can’t disable it. Applies only to a Salesforce-managed auth
provider. Available in API version 32.0 and later.

`isPkceEnabled` boolean

Indicates whether the OAuth 2.0 Proof Key for Code Exchange (PKCE)
security extension is enabled ( `true` ) or not ( `false` ). You can enable
PKCE for these `providerType` values.

**•** `Custom`

**•** `Facebook`

**•** `Google`

**•** `Microsoft`

**•** `OpenIdConnect`

**•** `Salesforce` .

This field is available in API version 59.0 and later.

`linkKickoffUrl` string The URL for linking existing Salesforce users to a third-party account. This
field is read-only. Available in API version 43.0 and later.

`logoutUrl` string The destination for users after they log out if they authenticated using
single sign-on. The URL must be fully qualified with an http or https prefix,

such as `https://acme.my.salesforce.com` . Available in API
version 33.0 and later.

`oauthKickoffUrl` string The URL for obtaining OAuth access tokens for a third party. This field is
read-only. Available in API version 43.0 and later.

`paramForwardAllowlist` AuthProvParamFwdA **l** owlist[]

`plugin` string

An allowlisted URL parameter that can be forwarded from the
authentication provider's client configuration URLs to the authorization
URL. Available in API version 62.0 and later.

An existing Apex class that extends the
`Auth.AuthProviderPluginClass` abstract class. Available in
API version 36.0 and later.

`portal` string This field is used only with portals, which are deprecated. Salesforce doesn’t
support creating portals, but existing portals are supported.

```
providerType

```

`AuthProviderType` Required. The third-party authentication provider to use. Valid values
(enumeration of include:
type string)

**•** `Apple`

**•** `Bitbucket` —Provides authentication for a `Bitbucket` provider.
Enables you to connect to Bitbucket from a Lightning Platform
application. When logged in to Bitbucket, the app can makes calls to
Bitbucket APIs. The `Bitbucket` provider isn’t available as an SSO
provider, so users can’t log in to a Salesforce org using their Bitbucket
login credentials. Available in API version 61.0 and higher.


Metadata Types AuthProvider

**Field Name** **Field Type** **Description**

**•** `Custom` —A provider configured with a custom authentication
provider plug-in. Available in API version 36.0 and later.

**•** `Facebook` .

**•** `GitHub` —Provides authentication for a `GitHub` provider. Used to
log in users of your Lightning Platform app to GitHub using OAuth.
When logged in to GitHub, your app can make calls to GitHub APIs.
The `GitHub` provider isn’t available as an SSO provider, so users can’t
log in to your Salesforce org using their GitHub login credentials.
Available in API version 35.0 and later.

**•** `Google` .

**•** `Janrain` .

**•** `LinkedIn` . Available in API version 32.0 and later.

**•** `Microsoft` —Provides authentication for all services that can be
accessed via Microsoft Azure Active Directory. Available in API version
55.0 and later.

**•** `MicrosoftACS` —Microsoft Access Control Service typically provides
authentication for a Microsoft Office 365 service, like SharePoint Online.
The `MicrosoftACS` provider doesn't support SSO. Available in API
version 31.0 and later.

**•** `MuleSoft` . Available in API version 57.0 and later.

**•** `OpenIdConnect` . Available in API version 29.0 and later.

**•** `Salesforce` .

**•** `Slack` . Available in API version 54.0 and later.

**•** `Twitter` . Available in API version 32.0 and later.

`registrationHandler` string

An existing Apex class that implements the
`Auth.RegistrationHandler` interface.

You can use either an Apex class or a flow for the registration handler. To
use a flow instead, omit the `registrationHandler` field and specify
a flow in the `flow` field.

`requireMfa` boolean Requires multi-factor authentication (MFA) for single sign-on with this
auth provider based on the MFA status of each user. For this setting to

trigger MFA, you must apply MFA directly to users via one of two methods.
1) Enable the org setting Require multi-factor authentication (MFA) for all
direct UI logins to your Salesforce org. 2) Assign the user permission
multi-factor authentication for User Interface Logins.

`sendAccessTokenInHeader` boolean If enabled ( `true` ), the access token is sent to the `UserInfoUrl` in a
header instead of a query string. Available in API version 30.0 and later.

`sendClientCredentialsInHeader` boolean Required when creating an OpenID Connect authentication provider. If
enabled ( `true` ), the client credentials are sent in a header to the

`tokenUrl` instead of a query string. The credentials are in the standard
OpenID Connect Basic Credentials header format, which is `Basic`


Metadata Types AuthProvider

**Field Name** **Field Type** **Description**

`<token>`, where `<token>` is the base64-encoded string
`"clientkey:clientsecret"` . Available in API version 30.0 and
later.

`sendSecretInApis` boolean

`ssoKickoffUrl` string

`tokenUrl` string

`userInfoUrl` string

AuthProvParamFwdAllowlist

Determines whether the encrypted consumer secret appears in API
responses. If enabled (default), the secret appears in the response. If

disabled ( `false` ), responses don’t include the consumer secret. For
security, you can disable the setting. However, keep in mind that:

**•** By disabling this setting, the consumer secret is excluded from API
responses in all API versions.

**•** Change sets and other metadata deployments break because both
the consumer key and secret are expected. To fix this problem, insert
the consumer key manually during deployment.

Available in API version 47.0 and later.

The consumer secret is always included in the response as a placeholder
value, regardless of the value provided for `sendSecretInApis` .

The URL for performing single sign-on into Salesforce from a third party
by using its third-party credentials. This field is read-only. Available in API
version 43 and later.

The OAuth token endpoint URL of an OpenID Connect authentication
provider. Available in API version 29.0 and later.

In API version 33.0 and later, for Salesforce-managed auth providers, leave
the field blank to let Salesforce supply and manage the value. For details,
see “Usage.”

The OpenID Connect endpoint URL of the OpenID Connect authentication
provider. Available in API version 29.0 and later.

In API version 33.0 and later, for Salesforce-managed auth providers, leave
the field blank to let Salesforce supply and manage the value. For details,
see “Usage.”

Represents an allowlisted URL parameter that can be forwarded from authentication provider client configuration URLs to the authorization
URL. Use this type to add custom functionality to authentication providers. For example, allowlist a `ui_locales` parameter and use
it to send a user's language preference from Salesforce to the third-party provider's login page. You can allowlist up to 10 parameters.


Metadata Types AuthProvider

Declarative Metadata Sample Definition

Note: Starting in November 2022, enter the `consumerSecret` value as plaintext, for example,
`<consumerSecret>yourplaintextconsumersecret</consumerSecret>` . Existing consumer secrets that
were entered as encrypted values can be deployed throughout the Winter ‘23 release.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <AuthProvider xmlns="http://soap.sforce.com/2006/04/metadata">

      <consumerKey>yourappkey</consumerKey>

      <consumerSecret>PwdVxXjzu3NCZ3MD4He+wA==</consumerSecret>

      <executionUser>admin@your.org</executionUser>

      <friendlyName>FacebookAuthProvider</friendlyName>

      <providerType>Facebook</providerType>

      <registrationHandler>RegistrationHandler</registrationHandler>

      <sendSecretInApis>true</sendSecretInApis>

   </AuthProvider>

```

This example package manifest references the previous AuthProvider definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>FacebookAuthProvider</members>

        <name>AuthProvider</name>

      </types>

      <version>28.0</version>

   </Package>

```

Usage

Salesforce provides default authentication providers, called Salesforce-managed auth providers, to simplify setting up these service
providers for authentication.

**•** Apple

**•** Bitbucket

**•** Facebook

**•** GitHub

**•** Google

**•** Janrain

**•** LinkedIn

**•** Microsoft

**•** Microsoft Access Control Service

**•** MuleSoft

**•** Salesforce


### Metadata Types AutoResponseRules

**•** Slack

To use a Salesforce-managed auth provider, leave these fields blank when creating your auth provider from the Auth. Provider Setup
page.

**•** `authorizeUrl`

**•** `consumerKey`

**•** `consumerSecret`

**•** `defaultScopes`

**•** `tokenURL`

**•** `userInfoUrl`

Note: If you provide a value for one of these fields, you must also provide a value for `consumerKey` and `consumerSecret` .

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### AutoResponseRules

Represents an auto-response rule that sets conditions for sending automatic email responses to lead or case submissions based on the
attributes of the submitted record. You can access rules metadata for all applicable objects, for a specific object, or for a specific rule on
a specific object.

The `package.xml` syntax for accessing all auto-response rules for all objects is:

```
      <types>

        <members>*</members>

        <name>AutoResponseRules</name>

      </types>

```

All rules for a specific object use a similar syntax without the wildcard. For example, all auto-response rules for the Case object would
use this syntax:

```
      <types>

        <members>Case</members>

        <name>AutoResponseRules</name>

      </types>

```

You can also access specific auto-response rules for an object. The following example only accesses the “samplerule” and “newrule”
### auto-response rules on the Case object. Notice that for this example the type name syntax is AutoResponseRule and not AutoResponseRules .

```
      <types>

        <members>Case.samplerule</members>

        <members>Case.newrule</members>

        <name>AutoResponseRule</name>

      </types>

```


Metadata Types AutoResponseRules

File Suffix and Directory Location

AutoResponseRules for an object have the suffix `.autoResponseRules` and are stored in the `autoResponseRules` folder.
For example, all Case auto-response rules are stored in the `Case.autoResponseRules` file.

Version

AutoResponseRules components are available in API version 27.0 and later.

Fields

**Field Name** **Field Type** **Description**

`autoresponseRule` AutoResponseRule[] Represents the definitions of the named auto-response rules.

AutoResponseRule

Represents whether a rule is active or not and the order in which the entry is processed in the rule.

**Field Name** **Field Type** **Description**

`active` boolean Indicates whether the autoresponse rule is active ( `true` )
or not ( `false` ).

`fullname` string Inherited from Metadata, this field is defined in the WSDL
for this metadata type. It must be specified when creating,

updating, or deleting. See `createMetadata()` to see
an example of this field specified for a call.

This value can't be `null` .

`ruleEntry` RuleEntry[] Represents the type and description for the auto-response
rule.

RuleEntry

Represents the fields used by the rule.

**Field Name** **Field Type** **Description**

`booleanFilter` string Advanced filter conditions that were specified for the rule.

`criteriaItems` `FilterItem[]` The items in the list that define the assignment criteria.

`formula` string

The validation formula.

Specify either `formula` or `criteriaItems`, but not
both fields.

`replyToEmail` string The email address that appears in the reply-to header.


### Metadata Types BatchCalcJobDefinition

**Field Name** **Field Type** **Description**

`senderEmail` string The email address of the person or queue sending the email
notification.

`senderName` string The name of the person or queue sending the email
notification.

`template` string

Declarative Metadata Sample Definition

The following is an example AutoResponseRules component:

Specifies the template to use for the email that is
automatically sent to the designated recipient.

Lightning email templates aren’t packageable. We
recommend using a Classic email template.

```
<AutoResponseRules xmlns="http://soap.sforce.com/2006/04/metadata">

   <autoResponseRule>

     <fullName>ajbdeploytest2</fullName>

     <active>false</active>

     <ruleEntry>

        <criteriaItems>

          <field>Case.Description</field>

          <operation>contains</operation>

          <value>testing</value>

        </criteriaItems>

        <senderEmail>test@test.org</senderEmail>

        <senderName>tester name j</senderName>

        <replyToEmail>test@@test.org</replyToEmail>

        <template>emailtemplate</template>

     </ruleEntry>

   </autoResponseRule>

</AutoResponseRules>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### BatchCalcJobDefinition

Represents a Data Processing Engine definition.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.


Metadata Types BatchCalcJobDefinition

File Suffix and Directory Location

BatchCalcJobDefinition components have the suffix `.batchCalcJobDefinition` and are stored in the
`batchCalcJobDefinitions` folder.

Version

BatchCalcJobDefinition components are available in API version 51.0 and later.

Special Access Rules

To use this metadata type, one of these licenses is required:

**•** Loyalty Management

**•** Financial Services Cloud

**•** Rebate Management

**•** Manufacturing Cloud

**•** Net Zero Cloud

Fields

**Field Name** **Field Type** **Description**

`aggregates` BatchCalcJob Collection of aggregate nodes in a data processing engine.
Aggregate[]

`appends` BatchCalcJobUnion[] Collection of append nodes in a data processing engine.

`atomicWritebacks` BatchCalcJobAtomicWriteBack[] Collection of composite writeback nodes in a data processing engine
definition. Available in API version 62.0 and later.

`customNodes` BatchCalcJobCustomNode[] Collection of custom nodes in a data processing engine. Available in API
version 57.0 and later.

`dataSpaceApiName` string Stores the Data Space API Name from Data 360. Available in API version
60.0 and later.

`datasources` BatchCalcJob Collection of data source nodes in a data processing engine.
Datasource[]

`definitionRunMode` BatchCalcJobDefRunMode(enumeration Specifies the execution mode in a data processing engine. Valid values
of type string) are:

**•** `Batch`

**•** `OnDemand`

`description` string Description of a data processing engine definition.

`doesGenAllFailedRecords` boolean Indicates whether the error file includes a complete list of all failed
writeback records ( `true` ) or not ( `false` ). The default value is `false`,

and only the first instance of a failure is recorded in the error file. If set


Metadata Types BatchCalcJobDefinition

**Field Name** **Field Type** **Description**

to `true`, all failed records are recorded in the error file for the writeback
node.

Available in API version 65.0 and later.

`executionPlatformObjectType` ExecutionPlatformObjectType(enumeration
of type string)

The execution platform object type that's used during the read, transform,
and writeback process for the Data Processing Engine definition. Possible
values are:

**•** `CalculatedInsightsObject`

**•** `DataLakeObject`

**•** `DataModelObject`

**•** `None`

Available in API version 65.0 and later.

`executionPlatformType` ExecutionPlatformType(enumeration The platform that's used to run the Data Processing Engine definition.
of type string) Valid values are:

**•** `CRMA`

**•** `CDP`

**•** `CORE`

Available in API version 59.0 and later.

`filters` BatchCalcJobFilter[] Collection of filter nodes in a data processing engine. definition.

`forecasts` BatchCalcJobForecast[]

Collection of forecast nodes in a data processing engine. definition.

Available in API version 58.0 and later.

`hierarchyPaths` BatchCalcJobHierarchyPath[] Collection of hierarchy path nodes in a data processing engine definition.

`isTemplate` boolean Indicates whether it’s a template data processing engine definition.

`joins` BatchCalcJobSource Collection of join nodes in a data processing engine.
Join[]

`label` string The label of a data processing engine definition.

`parameters` BatchCalcJobParameter[] Collection of input variables in a data processing engine.

The process type of a data processing engine. These process types may
be available to you depending on your industry solution and permission
sets. Valid values are:

**•** `AccountingPeriodClosure`

**•** `AccountingSubledger` —This value is reserved for internal
use.

**•** `ActionableList`

**•** `AdvancedAccountForecast`

**•** `BenefitManagement`


```
processType

```

BatchCalcProcessType
(enumeration of
type string)

Metadata Types BatchCalcJobDefinition

**Field Name** **Field Type** **Description**

**•** `BillingSchedulesforInvoiceGeneration`

**•** `CDPEnrichment`

**•** `ChannelInventoryManagement` —Available in API version
63.0 and later.

**•** `CollectionPlan` —Available in API version 65.0 and later.

**•** `CriteriaBsdSearchAndFilter`

**•** `DataProcessingEngine`

**•** `DecisionMatrixDataUpload`

**•** `Decisiontable`

**•** `Education`

**•** `EmployeeService` —Available in API version 63.0 and later.

**•** `FinancialSummaryRollup`

**•** `ForeignExchangeGainLossCalculations` —Available
in API version 65.0 and later.

**•** `FSCHierarchyRollUp`

**•** `Fundraising` —Available in API version 64.0 and later.

**•** `FundraisingRollups` —Available in API version 63.0 and later.

**•** `GeneralLedgerAccountBalancesSummary` —Available
in API version 65.0 and later.

**•** `InventoryBatchSearch` —Available in API version 65.0 and
later.

**•** `InventorySearch` —Available in API version 65.0 and later.

**•** `InvoiceGeneration`

**•** `Loyalty`

**•** `LegalEntityAccountingPeriodClosureAdvanced` —Available
in API version 63.0 and later.

**•** `LifeSciencbatchcalesCommercialTerritoryAlignment` —Available
in API version 63.0 and later.

**•** `LifeSciencesCustomerEngagement` —Available in API
version 64.0 and later.

**•** `LoyaltyPartnerManagement`

**•** `LoyaltyPointsAggregation`

**•** `NextGenForecasting` —Available in API version 64.0 and
earlier.

**•** `NetZero`

**•** `PatientServicesProgram` —Available in API version 64.0
and later.

**•** `PnmRosterFileUpload`

**•** `PriceProtection`

**•** `ProductCatalogManagement`


Metadata Types BatchCalcJobDefinition

**Field Name** **Field Type** **Description**

**•** `ProgramBasedBusiness`

**•** `ProviderSearch` —This value is reserved for internal use.

**•** `Rebates`

**•** `Recruitment`

**•** `RevenueTransactionManagement` —Available in API version
63.0 and later.

**•** `SalesAgreement` —Available in API version 63.0 and later.

**•** `TestAtomicWritebackScale` —Available in API version 64.0
and later.

**•** `TestProcessType`

**•** `UsageManagement`

`status` BatchJobDefinition Status of a data processing engine definition. Valid values are:
Status

**•** `Active`
(enumeration of

**•** `Inactive`
type string)

`transforms` BatchCalcJobTransform[] Collection of data transformation nodes in a data processing engine.

`writebacks` BatchCalcJobWriteback Collection of writeback objects in which the results of the data processing
Object[] engine are written back.

BatchCalcJobAggregate

Represents a collection of fields relating to an aggregate node in a data processing engine.

Fields

**Field Name** **Field Type** **Description**

`description` string Description of an aggregate node.

`fields` BatchCalcJob Required. Collection of aggregation fields.
AggregateField[]

`groupBy` string[] Required. Collections of fields used to group data in an aggregate node.

`label` string Required. Label of an aggregate node.

`name` string Required. Name of an aggregate node.

`sourceName` string Required. Name of the source node.

BatchCalcJobAggregateField

Represents a collection of fields relating to an aggregation field in an aggregate node of a data processing engine.


Metadata Types BatchCalcJobDefinition

Fields

**Field Name** **Field Type** **Description**

Required. Function used for aggregation.

Valid values are:

**•** `Unique` —A count of unique values.

**•** `Sum` —The sum of all values.

**•** `Max` —The largest value.

**•** `Min` —The smallest value.

**•** `Avg` —The average value, calculated as the mean.

**•** `Std` —The standard deviation.

**•** `Stdp` —A standard deviation with population variance.

**•** `Var` —The variance.

**•** `VarP` —The variance with population.

**•** `Count` —The total count of values.

```
aggregateFunction

```

BatchCalcJobAggregateFunction
(enumeration of type
string)

`alias` string Required. Name that subsequent nodes within the data processing engine use
to refer to the aggregate field.

`sourceFieldName` string Required. Source node field on which the aggregate is calculated.

BatchCalcJobAtomicWriteback

Represents a node in a DPE definition that stores the details about the relationship between the writeback nodes and the composite
writeback operations between the nodes.

**Field Name** **Field Type** **Description**

`description` string Description of the composite writeback object.

`label` string Required. Name of the composite writeback object.

`name` string Required. API name of the composite writeback object.

`writebackObject` BatchCalcJobAtomicWritebackRelationship[] Specifies the relationship between the writeback objects that are involved in
`Relationships` the writeback operation.

`writebackSequence` int Sequence in which the data processing engine executes the composite write
back node.

BatchCalcJobAtomicWritebackRelationship

Represents the relationships between the writeback objects that are involved in a composite writeback operation. It captures the
relationships between these objects and the sequence in which they should be processed.


Metadata Types BatchCalcJobDefinition

**Field Name** **Field Type** **Description**

`childWriteback` string Field name that's associated with the child writeback object in a composite
`ObjectField` writeback relationship. Available in API version 63.0 and later.

`childWriteback` string Name of the child writeback object that's associated with the writeback
`ObjectName` relationship.

`parentWriteback` string Field name that's associated with the parent writeback object in a composite
`ObjectField` writeback relationship. Available in API version 63.0 and later.

`parentWriteback` string Required. Name of the parent writeback object that's associated with the
`ObjectName` writeback relationship.

`relationshipName` string Describes the relationship between the child and parent writeback objects in
a composite writeback node. Available in API version 64.0 and later.

`sequenceNumber` int Sequence number of the writeback node that's associated with its parent node
in the relationship.

BatchCalcJobCustomNode

Represents a collection of custom nodes in a data processing engine. Use a custom node to add a custom action.

Fields

**Field Name** **Field Type** **Description**

`description` string Description of a custom node.

`extensionName` string Required. Name of an extension node.

`extensionNamespace` string Required. Namespace of an extension node.

`label` string Required. Label of a custom node.

`name` string Required. Name of a custom node.

`parameters` BatchCalcJob The field mappings of an extension node.
CustomNodeParameter[]

`sources` string[] Sources of an extension node.

BatchCalcJobCustomNodeParameter

Represents the field mappings of an extension node.


Metadata Types BatchCalcJobDefinition

Fields

**Field Name** **Field Type** **Description**

`name` string Required. Name of a parameter.

`value` string Required. Value of a parameter.

BatchCalcJobDatasource

Represents a collection of fields relating to a data source node in a data processing engine.

Fields

**Field Name** **Field Type** **Description**

Specifies the field separator to read fields from a CSV file record.

Possible values are:

**•** `COMMA`

**•** `BACKQUOTE`

**•** `CARET`

**•** `PIPE`

**•** `SEMICOLON`

**•** `TAB`

The default value is `COMMA` .

The same delimiter value used for the CSV file can’t be used within any of the
column values in the file. If you mistakenly use the same delimiter value in
column values, it can cause data parsing issues.

```
CSVDelimiter

```

BatchCalcJobCSVDelimiter
(enumeration of type
string)

`description` string Description of a data source node.

`fields` BatchCalcJob Required. Collection of data source fields.
DatasourceField[]

`fileIdentifier` string Specifies the source of the file or file storage system.

`filePath` string The file path for the specified file.

Specifies the source of the file or file storage system.

Possible value is:

**•** `ContentManagement`

```
fileSource

```

BatchCalcJobFileSource
(enumeration of type
string)

`label` string Required. Label of a data source node.

`name` string Required. Name of a data source node.


Metadata Types BatchCalcJobDefinition

**Field Name** **Field Type** **Description**

`sourceName` string Required. Name of a standard or custom object from which the data source
node extracts data.

```
type

```

BatchCalcJobDataSource Required. Type of object for the source object field. Supported values are:
Type (enumeration of

**•** `Analytics`

type string)

**•** `Analytics`

**•** `CalculatedInsightsObject`

**•** `CRMObject`

**•** `CSV`

**•** `DataModelObject`

**•** `StandardObject`

.

BatchCalcJobDatasourceField

Represents a collection of fields relating to a source object field that are selected in the data source node of a data processing engine.

Fields

**Field Name** **Field Type** **Description**

`alias` string Name that subsequent nodes within the data processing engine use to refer
to the data source field. Required when the field name is lookup.

Specifies the data type of the input field when using a CSV file as a data source.

Possible values are:

**•** `Boolean` —Available in API version 65.0 and later.

**•** `Date`

**•** `DateTime`

**•** `MultiValue`

**•** `Numeric`

**•** `Text`

```
dataType

```

BatchCalcJobDataType
(enumeration of type
string)

`isPrimaryKey` boolean Indicates whether a column name is the primary key ( `true` ) or not ( `false` )
for the Data Cloud CSV file.

`name` string Required. Name of the field. Can be either of the following:

**•** Name of the source field selected in the associated data source object.

**•** Name from a nested lookup object with three child levels.

BatchCalcJobFilter

Represents a collection of fields relating to a filter node in a data processing engine.


Metadata Types BatchCalcJobDefinition

Fields

**Field Name** **Field Type** **Description**

`criteria` BatchCalcJobFilter
Criteria[]

Collection of filter criteria in a filter node.

The field is required when `isDynamicFilter` is set to `False` .

`description` string Description of the batch calculation job filter.

`filterCondition` string

Logic that is specified to apply the filter conditions.

The field is required when `isDynamicFilter` is set to `False` .

`filterParameterName` string Name of the parameter of type filter.

`isDynamicFilter` boolean Indicates whether the filter criteria is dynamic. If value is set to `True`, filter
criteria is passed in runtime with `filterParameterName` .

`label` string Required. Label of the filter node.

`name` string Required. Name of the filter node.

`sourceName` string Required. Name of the source node.

BatchCalcJobForecast

Represents a collection of fields relating to a forecast node in a data processing engine. Available in API version 58.0 and later.

Fields

**Field** **Field Type** **Description**
**Name**

`accuracyPercent` BatchCalcJobFrcstAccuracy (enumeration of type string)

The interval percentage to
account for errors in
forecasts.

Possible values are:

**•** `Eighty`

**•** `NinetyFive`

**•** `None`

The default value is `None` .

`aggregationFields` BtchCalcJobFrcstAggrFld[] The list of fields to
forecast.

`dateFieldName` string

Required.

The date field from the
source node used to


Metadata Types BatchCalcJobDefinition

**Field** **Field Type** **Description**
**Name**

forecast values for the
specified forecast length.

`description` string The description of the
forecast node.

`forecastModelType` BatchCalcJobFrcstModel (enumeration of type string)

The model used to
forecast data.

Possible values are:

**•** `Additive`

**•** `Auto`

**•** `Multiplicative`

The default value is `Auto` .

`forecastPeriodCount` int The number of time
periods to generate

forecast data. For example,
if you select Year-Month
as the forecast period
type, and 4 as the forecast
period count, the forecast
results are generated for
the next 4 months.

The minimum and the
default count is 1, and the
maximum is 100.

`forecastPeriodType` BatchCalcJobFrcstPeriodType (enumeration of type string)


Required.

The type of forecast period
to group date field values
in the forecast results.

Possible values are:

**•** `FiscalYear`

**•** `FiscalYearMonth`

**•** `FiscalYearQuarter`

**•** `FiscalYearWeek`

**•** `Year`

**•** `YearMonth`

**•** `YearMonthDay`

**•** `YearQuarter`

**•** `YearWeek`

Metadata Types BatchCalcJobDefinition

**Field** **Field Type** **Description**
**Name**

`groupFields` BatchCalcJobFrcstGrpFld[] The source fields for
grouping the data to be

processed by the forecast
node.

`label` string

`name` string

`periodStartDateName` string

`seasonality` BatchCalcJobFrcstSeasonality (enumeration of type string)


Required.

The name of the forecast
node in the UI.

Required.

A unique name for the
forecast node.

Required.

The start date of the
forecast period.

Represents the periodic
fluctuations that occur

around the same time
every year.

Possible values are:

**•** `Two`

**•** `Three`

**•** `Four`

**•** `Five`

**•** `Six`

**•** `Seven`

**•** `Eight`

**•** `Nine`

**•** `Ten`

**•** `Eleven`

**•** `Twelve`

**•** `Thirteen`

**•** `Fourteen`

**•** `Fifteen`

**•** `Sixteen`

**•** `Seventeen`

**•** `Eighteen`

**•** `Nineteen`

**•** `Twenty`

Metadata Types BatchCalcJobDefinition

**Field** **Field Type** **Description**
**Name**

**•** `TwentyOne`

**•** `TwentyTwo`

**•** `TwentyThree`

**•** `TwentyFour`

**•** `Auto`

**•** `None`

The default value is `None` .

`shouldExcludeLastPeriod` boolean Indicates whether to
ignore the last period in

the source node when it
has incomplete data
( `true` ) or not ( `false` ).

The default value is
`false` .

`sourceName` string

BtchCalcJobFrcstAggrFld

Represents a list of fields to forecast in a forecast node.

**Field Name** **Field Type** **Description**

Required.

The name of the source
node.

A source can be any node
other than the datasink
and register node.

`aggregateFunction` BatchCalcJobAggregateFunction
(enumeration of type string)


Required.

The function of the aggregate field.

Possible values are:

**•** `Avg`

**•** `Count`

**•** `Max`

**•** `Min`

**•** `Std`

**•** `StdP`

**•** `Sum`

**•** `Unique`

Metadata Types BatchCalcJobDefinition

**Field Name** **Field Type** **Description**

**•** `Var`

**•** `VarP`

`aggregationResultLabel` string

`fieldName` string

BatchCalcJobFrcstGrpFld

Required.

The name of the aggregation result generated from
the aggregation function that’s applied to the source
node field.

Required.

The name of the source field.

Represents source fields for grouping the data to be processed by the forecast node.

**Field Name** **Field Type** **Description**

`fieldName` string

`groupBy` string

BatchCalcJobHierarchyPath

Required.

The name of the source field to group the data to be processed by the
forecast node.

A comma-separated list of values to group data by.

Required when the source field type is Date or DateTime.

Possible values are:

**•** `Second`

**•** `Second Epoch`

**•** `Minute`

**•** `Hour`

**•** `Day`

**•** `Day Epoch`

**•** `Week`

**•**

**•** `Month`

**•** `Quarter`

**•** `Year`

Represents a collection of hierarchy path nodes in a data processing engine definition.


Metadata Types BatchCalcJobDefinition

Fields

**Field Name** **Field Type** **Description**

`description` string Description of the hierarchy path node.

`hierarchyFieldName` string Required. Field name that contains the hierarchy path.

`isSelfFieldValueIncluded` boolean Indicates whether the self value is included in the calculated hierarchy path
( `True` ) or not ( `False` ).

`label` string Required. Label of the hierarchy path node.

`name` string Required. Name of the hierarchy path node.

`parentFieldName` string Required. Parent field name to calculate hierarchy path.

`selfFieldName` string Required. Self field name to calculate hierarchy path.

`sourceName` string Required. Name of the source node.

BatchCalcJobFilterCriteria

Represents a collection of fields relating to a filter condition in a filter node in a data processing engine.

Fields

**Field Name** **Field Type** **Description**

`inputVariable` string Name of the input variable used as a filter.

Required. Operator that is specified in the filter condition.

Valid values are:

**•** `Equals`

**•** `NotEquals`

**•** `GreaterThan`

**•** `GreaterThanOrEqual`

**•** `LessThan`

**•** `LessThanOrEqual`

**•** `StartsWith`

**•** `EndsWith`

**•** `Contains`

**•** `DoesNotContain`

**•** `IsNull`

**•** `IsNotNull`

**•** `In`

**•** `NotIn`


```
operator

```

BatchCalcJobFilter
Operator
(enumeration of type
string)

Metadata Types BatchCalcJobDefinition

**Field Name** **Field Type** **Description**

`sequence` integer Required. Sequence number used to refer the criteria in a filter node.

`sourceFieldName` string Required. Name of the field from the source node to apply the filter.

`value` string Value used to filter data from the source node.

BatchCalcJobParameter

Represents a collection of fields relating to an input variable in a data processing engine.

Fields

**Field Name** **Field Type** **Description**

`dataType` BatchCalcJobParameter Required. Data type of the parameter. Valid values are:
DataType

**•** `Date`
(enumeration of type

**•** `DateTime`
string)

**•** `Expression`

**•** `FileIdentifier`

**•** `Filter`

**•** `Numeric`

**•** `Text`

`defaultValue` string Default value of the parameter.

`description` string Description of the batch calculation job parameter.

`isMultiValue` boolean Indicates whether the parameter has different values ( `True` ) or not ( `False` ).
This field is supported only for the `Text` data type.

`label` string Required. Label of the batch calculation job parameter.

`name` string Required. Name of the batch calculation job parameter.

BatchCalcJobSourceJoin

Represents a collection of fields relating to a join node in a data processing engine.

Fields

**Field Name** **Field Type** **Description**

`description` string Description of the join node.


Metadata Types BatchCalcJobDefinition

**Field Name** **Field Type** **Description**

`fields` BatchCalcJobJoin Collection of fields in a join node.
ResultField[]

`joinKeys` BatchCalcJobJoin Collection of mapping of fields from the primary source node and the second
Key[] source node in a join node.

`label` string Required. Label of the join node.

`name` string Required. Name of the join node.

`primarySourceName` string Required. Name associated with the node as the primary source node.

`secondarySourceName` string Required. Name associated with the node as the secondary source node.

```
type

```

BatchCalcJobSource Required. Type of join specified between the primary source node and
JoinType secondary source node. Valid values are:
(enumeration of type

**•** `LeftOuter`

string)

**•** `LeftOuter`

**•** `RightOuter`

**•** `Inner`

**•** `Outer`

**•** `Lookup`

BatchCalcJobJoinKey

Represents a collection of fields relating to a mapping of fields from the first source node and second source node in a join node of a
data processing engine.

Fields

**Field Name** **Field Type** **Description**

`primarySourceFieldName` string Required. Mapped field name of the primary source node.

`secondarySourceFieldName` string Required. Mapped field name of the secondary source node.

BatchCalcJobJoinResultField

Represents a collection of fields relating to a set of resultant fields in a join node of a data processing engine.

Fields

**Field Name** **Field Type** **Description**

`alias` string Required. Name that subsequent nodes within the data processing engine
definition use to refer to the resultant field.


Metadata Types BatchCalcJobDefinition

**Field Name** **Field Type** **Description**

`sourceFieldName` string Required. Name of field from the primary or secondary data source.

`sourceName` string Required. Source node of the primary or secondary data source.

BatchCalcJobTransform

Represents a collection of fields relating to a data transformation in a data processing engine.

Fields

**Field Name** **Field Type** **Description**

`description` string The description of the batch calculation job transform.

`droppedFields` BatchCalcJobTransform The collection of dropped fields in a data transformation. Available when the
DroppedField[] transformation type is `Slice` .

`expressionFields` BatchCalcJobTransform The collection of formula fields in a data transformation. Available when the
AddedField[] transformation type is `Expression` .

`label` string Required. The label of the batch calculation job transform.

`name` string Required. The name of the batch calculation job transform.

`orderBy` BatchCalcJobOrderByField A collection of fields that’s used to sort the records within each partition group.
on page 460[]

`partitionBy` string[] A group of fields that’s used to partition the source data into partition groups.

`sourceName` string Required. Name of the source node.

Required. The type of transformation.

Valid values are:

**•** `ComputeRelative—` This transformation calculates values based on
values of the same partition group.

**•** `Expression` —This transformation calculates values based on existing
values of fields in the same record.

**•** `Slice` —This transformation removes fields from the source node.

```
transformType

```

BatchCalcJobTransform
Type (enumeration of
type string)

BatchCalcJobTransformDroppedField

Represents a collection of fields relating to a dropped field in a data transformation of a data processing engine.


Metadata Types BatchCalcJobDefinition

Fields

**Field Name** **Field Type** **Description**

`sourceFieldName` string Required. Name of the field that is dropped.

BatchCalcJobTransformAddedField

Represents a collection of fields relating to a formula in a data transformation of a data processing engine.

Fields

**Field Name** **Field Type** **Description**

`alias` string Required. Name that subsequent nodes within the data processing engine use
to the transform node.

Required. Data type of the formula.

Valid values are:

**•** `Boolean` —Available in API version 65.0 and later.

**•** `Date`

**•** `DateTime`

**•** `MultiValue`

**•** `Numeric`

**•** `Text`

```
dataType

```

BatchCalcJobDataType
(enumeration of type
string)

`decimalPlaces` integer Number of digits to the right of a decimal point in the value. Required for the
`Numeric` data type.

`expression` string Required. Formula defined by the user.

`length` integer Total length of the value including the decimal places. Required for data types:
`Text` and `Numeric` .

BatchCalcJobOrderByField

Represents a collection of fields that are used to sort the partitioned data.

Fields

**Field Name** **Field Type** **Description**

`name` string Required. Name of the field that is used to sort data.


Metadata Types BatchCalcJobDefinition

**Field Name** **Field Type** **Description**

`orderType` BatchCalcJobOrderType(enumeration
of type string)

BatchCalcJobUnion

Order in which the data is sorted.

Valid values are:

**•** Ascending

**•** Descending

Represents a collection of fields relating to the union of data from two nodes in a data processing engine.

Fields

**Field Name** **Field Type** **Description**

`description` string Description of the batch calculation job union.

`isDisjointedSchema` boolean

Indicates whether the union is of two disjointed datasets ( `true` ) or not
( `false` ). Set to `True` to allow joining of two datasets having no common
fields.

`label` string Required. Label of the batch calculation job union.

`name` string Required. Name of the batch calculation job union.

`sources` string[] Names of the source nodes.

BatchCalcJobWritebackObject

Represents a collection of fields relating to the object in which the results of the data processing engine are written back.

Fields

**Field Name** **Field Type** **Description**

`canWrtbckToNonEditableFields` boolean

Indicates whether the non-editable fields are included in field mapping when
the action type is upsert. The default value is `false` .

Available in API version 64.0 and later.

`description` string Descriptions of the batch calculation job writeback object.

`externalIdFieldName` string

Unique external field ID for the target object name.

Available in API version 60.0 and later.

`fields` BatchCalcJobWriteback Collection of the writeback fields.
Mapping[]


Metadata Types BatchCalcJobDefinition

**Field Name** **Field Type** **Description**

`filterCondition` string

The condition that filters the records from a writeback dataset for a user.
Examples of a filter condition include a user ID, stage name, and a security
policy that returns only the records that a user owns.

Available in API version 57.0 and later.

`folderName` string The folder where the writeback dataset is saved. Available in API version 57.0
and later.

`groupBy` string Reserved for future use.

`isChangedRow` boolean Indicates whether a row in the write back object is changed. Set to `True` to
write back the changed rows.

`isExistingDataset` boolean

Indicates whether a CRM Application (CRMA) dataset or a Data 360 Data Lake
object is present ( `true` ) or will be created ( `false` ). Available in API version
62.0 and later.

`label` string Required. Name of the write back object.

`name` string Required. Name of the batch calculation job write back object.

Type of operation specified.

Valid values are:

**•** `Delete` —This value is available in API version 56.0 and later.

**•** `Insert`

**•** `Overwrite` —Available only when `storageType` is
`DataLakeObject` . This value is available in API version 60.0 and later.

**•** `Update`

**•** `Upsert`

```
operationType

```

BatchCalcJobWriteback
Opn (enumeration of
type string)

`sharingInheritanceObjectName` string The name of the source object from which the row-level sharing inheritance
settings are applied. Available in API version 57.0 and later.

`shouldCreateTargetObject` boolean Indicates whether target Data Lake Object or Salesforce Object is created in
Salesforce ( `true` ) or not ( `false` ). Available in API version 65.0 and later.

`shouldMngRowLockFor` boolean Reserved for future use.

```
GroupedRec

```

`sourceName` string Required. Name of the source node associated with the write back object.

Specifies where you want to use the data stored in the source node. Available
in API version 57.0 and later.

Valid values are:

**•** `Analytics`

**•** `DataLakeObject`

**•** `sObject`

The default value is `sObject` .


```
storageType

```

BatchCalcJobWriteback
Type (enumeration of
type string)

Metadata Types BatchCalcJobDefinition

**Field Name** **Field Type** **Description**

`targetObjectName` string Required. Object that is inserted or upserted by the data processing engine.

`writebackSequence` integer Sequence in which the target object is updated by the data processing engine.

`writebackUser` string ID of the user whose permissions decide which objects and fields of the target
object can be updated.

BatchCalcJobWritebackMapping

Represents a collection of fields relating to the mapping between results and the fields in the target object.

Fields

**Field Name** **Field Type** **Description**

`fieldType` string Target field type on the writeback object. Valid values are:

**•** Primary Key

**•** Qualifier Key

Available in API version 64.0 and later.

isAutogenerated boolean

Indicates whether the target field value on the writeback object is
autogenerated ( `true` ) or not ( `false` ).

Available in API version 64.0 and later.

`parentName` string Name of the lookup object. Required only when the `relationshipName`
field is defined.

`relationshipName` string Name of the lookup relationship.

`runtimeParameter` boolean

Indicates whether the source field from runtime parameter is `true` or `false` .
The default value is `false` .

Available in API version 59.0 and later.

`sourceFieldName` string Required. Name of the field in the source node that is written back.

`targetFieldName` string Name of the sObject field to which the results are written back.

Declarative Metadata Sample Definition

The following is an example of a BatchCalcJobDefinition component.

```
<?xml version="1.0" encoding="UTF-8"?>

<BatchCalcJobDefinition xmlns="http://soap.sforce.com/2006/04/metadata">

   <aggregates>

     <description>Aggregate Description</description>

     <fields>

```


Metadata Types BatchCalcJobDefinition

```
           <aggregateFunction>Count</aggregateFunction>

           <alias>NameCount</alias>

           <sourceFieldName>Name</sourceFieldName>

        </fields>

        <groupBy>ContactId</groupBy>

        <groupBy>Name</groupBy>

        <label>AggregateOpportunities</label>

        <name>AggregateOpportunities</name>

        <sourceName>Opportunity</sourceName>

      </aggregates>

      <forecasts>

        <description>ForecastNode Description</description>

        <label>ContactForecast</label>

        <name>ContactForecast</name>

        <sourceName>Contact</sourceName>

        <dateFieldName>CreatedDate</dateFieldName>

        <forecastPeriodType>YearMonth</forecastPeriodType>

        <shouldExcludeLastPeriod>false</shouldExcludeLastPeriod>

        <forecastPeriodCount>12</forecastPeriodCount>

        <periodStartDateName>CreatedDateYM</periodStartDateName>

        <forecastModelType>Auto</forecastModelType>

        <seasonality>None</seasonality>

        <accuracyPercent>None</accuracyPercent>

        <aggregationFields>

           <aggregateFunction>Count</aggregateFunction>

           <aggregationResultLabel>CountOfLastName</aggregationResultLabel>

           <fieldName>LastName</fieldName>

        </aggregationFields>

        <groupFields>

           <fieldName>LastModifiedDate</fieldName>

           <groupBy>Week</groupBy>

        </groupFields>

      </forecasts>

      <appends>

        <description>Append desc</description>

        <isDisjointedSchema>true</isDisjointedSchema>

        <label>AppendAllAccounts</label>

        <name>AppendAllAccounts</name>

        <sources>AccountsOfManufacturingIndustry</sources>

        <sources>ComputeRelativeManufacturingIndustry</sources>

      </appends>

      <datasources>

        <description>Desc Contact</description>

        <fields>

           <alias>Id</alias>

           <name>Id</name>

           <isPrimaryKey>false</isPrimaryKey>

           <dataType>Text</dataType>

        </fields>

        <fields>

           <alias>LastName</alias>

           <name>LastName</name>

           <isPrimaryKey>false</isPrimaryKey>

           <dataType>Text</dataType>

```


Metadata Types BatchCalcJobDefinition

```
        </fields>

        <fields>

           <alias>CreatedDate</alias>

           <name>CreatedDate</name>

           <isPrimaryKey>false</isPrimaryKey>

           <dataType>Date</dataType>

        </fields>

        <fields>

           <alias>LastModifiedDate</alias>

           <name>LastModifiedDate</name>

           <isPrimaryKey>false</isPrimaryKey>

           <dataType>Date</dataType>

        </fields>

        <label>Contact</label>

        <name>Contact</name>

        <sourceName>Contact</sourceName>

        <type>StandardObject</type>

        <fileSource>ContentManagement</fileSource>

        <fileIdentifier>069xx0000004CAeAAM</fileIdentifier>

        <CSVDelimiter>COMMA</CSVDelimiter>

        <filePath>parentFolder/childFolder</filePath>

      </datasources>

      <datasources>

        <fields>

           <alias>Name</alias>

           <name>Name</name>

           <isPrimaryKey>false</isPrimaryKey>

           <dataType>Text</dataType>

        </fields>

        <fields>

           <alias>ContactId</alias>

           <name>ContactId</name>

           <isPrimaryKey>false</isPrimaryKey>

           <dataType>Text</dataType>

        </fields>

        <label>Opportunity</label>

        <name>Opportunity</name>

        <sourceName>Opportunity</sourceName>

        <type>StandardObject</type>

        <fileSource>ContentManagement</fileSource>

        <fileIdentifier>069xx0000004CAeAAM</fileIdentifier>

        <CSVDelimiter>COMMA</CSVDelimiter>

        <filePath>parentFolder/childFolder</filePath>

      </datasources>

      <description>Calculates and creates transaction journal records based on the orders

   placed by the loyalty program members. The transaction journals are used to accrue points

    to the member.</description>

      <filters>

        <criteria>

           <operator>Equals</operator>

           <sequence>1</sequence>

           <sourceFieldName>LastName</sourceFieldName>

           <value>Salesforce</value>

        </criteria>

```


Metadata Types BatchCalcJobDefinition

```
        <description>Filter Desc</description>

        <filterCondition>1</filterCondition>

        <isDynamicFilter>false</isDynamicFilter>

        <label>AccountsOfManufacturingIndustry</label>

        <name>AccountsOfManufacturingIndustry</name>

        <sourceName>AccountOpportunities</sourceName>

      </filters>

      <hierarchyPaths>

        <description>Hierarchy Path Node</description>

        <hierarchyFieldName>Hierarchy_Path</hierarchyFieldName>

        <isAggregationRequired>true</isAggregationRequired>

        <isSelfFieldValueIncluded>true</isSelfFieldValueIncluded>

        <label>Get Hierarchy</label>

        <name>Get_Hierarchy</name>

        <parentFieldName>ContactId</parentFieldName>

        <selfFieldName>LastName</selfFieldName>

        <sourceName>AppendAllAccounts</sourceName>

        <aggregateFields>

           <aggregateFunction>Count</aggregateFunction>

           <aggregationFieldName>*</aggregationFieldName>

           <aggregateFieldAliasName>CountOfLastName</aggregateFieldAliasName>

        </aggregateFields>

      </hierarchyPaths>

      <isTemplate>false</isTemplate>

      <executionPlatformObjectType>None</executionPlatformObjectType>

      <joins>

        <description>Left Outer Join</description>

        <fields>

           <alias>ContactId</alias>

           <sourceFieldName>Id</sourceFieldName>

           <sourceName>Contact</sourceName>

        </fields>

        <fields>

           <alias>LastName</alias>

           <sourceFieldName>LastName</sourceFieldName>

           <sourceName>Contact</sourceName>

        </fields>

        <fields>

           <alias>NameCount</alias>

           <sourceFieldName>NameCount</sourceFieldName>

           <sourceName>AggregateOpportunities</sourceName>

        </fields>

        <fields>

           <alias>OpportunityName</alias>

           <sourceFieldName>Name</sourceFieldName>

           <sourceName>AggregateOpportunities</sourceName>

        </fields>

        <joinKeys>

           <primarySourceFieldName>Id</primarySourceFieldName>

           <secondarySourceFieldName>ContactId</secondarySourceFieldName>

        </joinKeys>

        <label>AccountOpportunities</label>

        <name>AccountOpportunities</name>

        <primarySourceName>Contact</primarySourceName>

```


Metadata Types BatchCalcJobDefinition

```
        <secondarySourceName>AggregateOpportunities</secondarySourceName>

        <type>LeftOuter</type>

      </joins>

      <label>Create Transaction Journals Based on Orders</label>

      <parameters>

        <dataType>Date</dataType>

        <defaultValue>2020-01-01</defaultValue>

        <description>Desc TextParameter</description>

        <isMultiValue>false</isMultiValue>

        <label>DateParameter</label>

        <name>DateParameter</name>

      </parameters>

      <parameters>

        <dataType>Filter</dataType>

        <defaultValue>{&quot;filterCondition&quot;: &quot;1 AND 2&quot;,

   &quot;criteria&quot;: [{&quot;sourceFieldName&quot;:

   &quot;NameCount&quot;,&quot;operator&quot;: &quot;GreaterThan&quot;,&quot;value&quot;:

   &quot;20&quot;,&quot;sequence&quot;: &quot;1&quot;}, {&quot;sourceFieldName&quot;:

   &quot;Name&quot;,&quot;operator&quot;: &quot;Equals&quot;,&quot;value&quot;:

   &quot;Salesforce&quot;,&quot;sequence&quot;: &quot;2&quot;}]}</defaultValue>

        <isMultiValue>false</isMultiValue>

        <label>FilterParameter</label>

        <name>FilterParameter</name>

      </parameters>

      <parameters>

        <dataType>Numeric</dataType>

        <defaultValue>5000</defaultValue>

        <description>Desc TextParameter</description>

        <isMultiValue>false</isMultiValue>

        <label>NumericParameter</label>

        <name>NumericParameter</name>

      </parameters>

      <parameters>

        <dataType>Text</dataType>

        <defaultValue>@salesforce.com</defaultValue>

        <description>Desc TextParameter</description>

        <isMultiValue>false</isMultiValue>

        <label>TextParameter</label>

        <name>TextParameter</name>

      </parameters>

      <processType>Rebates</processType>

      <definitionRunMode>Batch</definitionRunMode>

      <status>Inactive</status>

      <transforms>

        <description>transforms Desc</description>

        <expressionFields>

           <alias>NewLastName</alias>

           <dataType>Text</dataType>

           <expression>TODAY()</expression>

           <length>80</length>

        </expressionFields>

        <label>ManufacturingIndustry</label>

        <name>ManufacturingIndustry</name>

        <sourceName>AccountsOfManufacturingIndustry</sourceName>

```


Metadata Types BatchCalcJobDefinition

```
        <transformationType>Expression</transformationType>

      </transforms>

      <transforms>

        <droppedFields>

           <sourceFieldName>NewLastName</sourceFieldName>

        </droppedFields>

        <label>MediaIndustry</label>

        <name>MediaIndustry</name>

        <sourceName>ManufacturingIndustry</sourceName>

        <transformationType>Slice</transformationType>

      </transforms>

      <transforms>

        <description>compute relative transforms Desc</description>

        <expressionFields>

           <alias>NewLastName</alias>

           <dataType>Text</dataType>

           <expression>rank()</expression>

           <length>80</length>

        </expressionFields>

        <label>ComputeRelativeManufacturingIndustry</label>

        <name>ComputeRelativeManufacturingIndustry</name>

        <orderBy>

           <name>LastName</name>

           <orderType>Ascending</orderType>

        </orderBy>

        <partitionBy>LastName</partitionBy>

        <sourceName>MediaIndustry</sourceName>

        <transformationType>ComputeRelative</transformationType>

      </transforms>

      <customNodes>

        <name>RebatesCustomNode</name>

        <label>Rebates Custom Node</label>

        <description>customNodes Desc</description>

        <sources>Get_Hierarchy</sources>

        <extensionName>RebatesExpression</extensionName>

        <extensionNamespace>industries_mfg</extensionNamespace>

        <parameters>

           <name>inputColumn</name>

           <value>LastName</value>

        </parameters>

        <parameters>

           <name>isFilterCriteria</name>

           <value>true</value>

        </parameters>

        <parameters>

           <name>outputColumn</name>

           <value>GenName</value>

        </parameters>

      </customNodes>

      <writebacks>

        <fields>

           <sourceFieldName>GenName</sourceFieldName>

           <targetFieldName>LastName</targetFieldName>

        </fields>

```


### Metadata Types BatchProcessJobDefinition

```
        <isChangedRow>false</isChangedRow>

        <label>exportToContact</label>

        <name>exportToContact</name>

        <description>Export To Contact</description>

        <operationType>Insert</operationType>

        <sourceName>RebatesCustomNode</sourceName>

        <targetObjectName>Contact</targetObjectName>

        <writebackSequence>1</writebackSequence>

        <canWrtbckToNonEditableFields>false</canWrtbckToNonEditableFields>

      </writebacks>

      <writebacks>

        <fields>

           <sourceFieldName>CreatedDateYM</sourceFieldName>

           <targetFieldName>CreatedDate</targetFieldName>

        </fields>

        <isChangedRow>false</isChangedRow>

        <isExistingDataset>false</isExistingDataset>

        <label>exportToContactFC</label>

        <name>exportToContactFC</name>

        <description>Export To Contact</description>

        <operationType>Insert</operationType>

        <sourceName>ContactForecast</sourceName>

        <targetObjectName>Contact</targetObjectName>

        <writebackSequence>2</writebackSequence>

        <canWrtbckToNonEditableFields>false</canWrtbckToNonEditableFields>

      </writebacks>

   </BatchCalcJobDefinition>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <!-
     ~ Copyright 2020 Salesforce, Inc.

     ~ All Rights Reserved

     ~ Company Confidential

   -->

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

     <types>

       <members>*</members>

       <name>BatchCalcJobDefinition</name>

     </types>

     <version>60.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### BatchProcessJobDefinition

Represents the details of a Batch Management job definition.


Metadata Types BatchProcessJobDefinition

This type extends the Metadata metadata type and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

BatchProcessJobDefinition components have the suffix `.batchProcessJobDefinition` and are stored in the
`batchProcessJobDefinitions` folder.

Version

BatchProcessJobDefinition components are available in API version 51.0 and later.

Special Access Rules

To use this metadata type, your Salesforce org must have the Loyalty Management or the Rebate Management license. The Loyalty
Program Process type is only available in orgs that have Loyalty Management enabled.

Fields

**Field Name** **Field Type** **Description**

`batchSize` integer Required. Number of records that each Batch Management job can
process. Flow type Batch Management jobs can process up to 2000

records and Loyalty Program Process type Batch Management jobs can
process up to 250 records.

`dataSource` BatchDataSource Required. Source of information whose records must be processed by
on page 471[] the Batch Management job.

`description` string Description of the Batch Management job, up to 255 characters.

`executionProcessApiName` string API name of process that must be executed by the Batch Management
job. This field is available in API version 55.0 and later.

**•** If the batch job’s type is Flow, enter the API name of an active flow
that the batch job must execute.

**•** If the batch job’s type is Loyalty Program Process, enter:

**–** Transaction_Journals if you want the batch job to process
Transaction Journal records by applying the applicable active
loyalty program process of the type TransactionJournal.

**–** API name of an active loyalty process of the type TierProcessing
if you want the batch job to run the loyalty program process to
assess the tier of eligible members. The API name consists of the
name of the process, the process type, and the name of the
loyalty program separated by two consecutive underscores. For
example, the process API name is `Update Member`
`Tier__TierProcessing__Inner Circle` if the


Metadata Types BatchProcessJobDefinition

**Field Name** **Field Type** **Description**

process name is Update Member Tier, the process type is
TierProcessing, and the loyalty program name is Inner Circle.

You can use database-based APEX classes that let you use flex queues in
the Batch Management job, allowing to place more than 5 jobs in a
queue. This functionality is applicable to all Industry Clouds that use
[managed packages. See Apex Flex Queue.](https://help.salesforce.com/s/articleView?id=platform.code_apex_flex_queue.htm&type=5&language=en_US)

`flowApiName` string

API name of an active flow process that must be executed by the Batch
Management job.

You can either specify the flow API name in the
`executionProcessApiName` field or in the `flowApiName`
field.

`flowInputVariable` string Input variable of associated flow that is used by the batch job to uniquely
identify records.

`masterLabel` string Required. Name of the Batch Management job, up to 80 characters.

`processGroup` string Required. Name of the group for which the Batch Management job
processes records.

`retryCount` integer Required. Number of times this Batch Management job must be rerun
in case it fails. The maximum retry count is 3. Valid values are 1–3.

`retryInterval` integer Required. Number of milliseconds after which the Batch Management
job must be rerun in case it fails. Valid values are 1,000–10,000.

`status` string Indicates the status of the Batch Management job. Valid values are
`Active` and `Inactive` .

`type` string (enumeration The type of process that the Batch Management job must execute. This
of type string) field is available in API version 55.0 and later. Valid values are:

**•** `Flow`

**•** `Loyalty Program Process`

BatchDataSource

Represents the source of information whose records must be processed by the Batch Management job.

Fields

**Field Name** **Field Type** **Description**

`condition` string Required. Criteria defined to filter the records.

`criteria` string Type of filter criteria that’s used to filter records for processing.


Metadata Types BatchProcessJobDefinition

**Field Name** **Field Type** **Description**

`dataSourceType` string Type of data source that's used to create the batch job definition. Valid values
are:

**•** SingleSobject

**•** MultiSobject

Available in API version 64.0 and later.

`filters` BatchDataSrcFilterCriteria Filter criterion that decides which records must be processed by the Batch
on page 472[] Management job.

orderFields BatchDataSourceOrderField Fields that are used to order the records before the records are added to a
on page 473 batch in a job.

`sourceObject` string

`sourceObjectField` string

BatchDataSrcFilterCriteria

Required. API name of an object whose records must be processed by the
batch job.

If the batch job type is Loyalty Program Process, the source object must be:

**•** TransactionJournal if the batch job is used to process transaction journals
by applying the applicable loyalty program process.

**•** An object that stores the details of loyalty program members whose tier
must be assessed by the loyalty program process specified in the
executionProcessApiName field.

API name of the source object field that uniquely identifies records for which
the batch job is executed. This field is available in API version 57.0 and later.

This field is only applicable when the batch job’s type is Loyalty Program Process
and a TierProcess type active loyalty program process is specified in the

`executionProcessApiName` field. Specify the API name of a field that
is a lookup to the LoyaltyProgramMember object and uniquely identifies the
members whose tier must be assessed.

Represents the filter conditions that decide which records must be processed by the Batch Management job.

Fields

**Field Name** **Field Type** **Description**

domainObjectName string Name of the object the field is associated with. Available in API version 64.0
and later.

`dynamicValueType` string Data type of the input variable used as a filter.

`fieldName` string Required. Name of the field that must be used to filter records.

`fieldPath` string Stores the path to a field in the object. Available in API version 64.0 and later.


Metadata Types BatchProcessJobDefinition

**Field Name** **Field Type** **Description**

`fieldValue` string Required. Value of the field that must be filtered. Specify the field if
`isDynamicValue` is set to `False` .

`isDynamicValue` boolean Required. Indicates whether the filter criteria is dynamic.

`operator` string (enumeration Required. Operator that is specified in the filter criteria. Valid values are:
of type string)

**•** `equals`

**•** `excludes`

**•** `greaterThan`

**•** `greaterThanOrEqualTo`

**•** `in`

**•** `includes`

**•** `lessThan`

**•** `LessThanOrEqualTo`

**•** `GreaterOrEqual`

**•** `like`

**•** `notEquals`

**•** `notIn`

`sequenceNo` integer Required. Sequence number used to refer the criteria in a filter.

BatchDataSourceOrderField

Represents the fields that are used to group data.

Fields

**Field Name** **Field Type** **Description**

domainObjectName string Required. Name of the object the field is associated with. Available in API version
64.0 and later.

`fieldName` string Required. Name of the field that must be used to filter records. Available in API
version 64.0 and later.

`fieldPath` string Required. Stores the path to a field in the object. Available in API version 64.0
and later.

Declarative Metadata Sample Definition

The following is an example of a BatchProcessJobDefinition component.

```
   <?xml version="1.0" encoding="UTF-8"?>

```


Metadata Types BatchProcessJobDefinition

```
   <BatchProcessJobDefinition xmlns="http://soap.sforce.com/2006/04/metadata">

     <batchSize>10</batchSize>

     <dataSource>

       <condition>1</condition>

       <criteria>all</criteria>

       <filters>

         <dynamicValue>false</dynamicValue>

         <dynamicValueType>string</dynamicValueType>

         <fieldName>Name</fieldName>

         <fieldValue>abcd</fieldValue>

         <operator>equals</operator>

         <sequenceNo>1</sequenceNo>

       </filters>

       <sourceObject>Account</sourceObject>

     </dataSource>

     <flowApiName>Flow1</flowApiName>

     <flowInputVariable>recordId</flowInputVariable>

     <masterLabel>BatchJob1</masterLabel>

     <processGroup>Loyalty</processGroup>

     <retryCount>2</retryCount>

     <retryInterval>1000</retryInterval>

     <status>Inactive</status>

     <description>test</description>

     <type>Flow</type>

     <executionProcessApiName>testFlow</executionProcessApiName>

   </BatchProcessJobDefinition>

```

The following is an example of a Flow object used in Metadata API.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <!-
     ~ Copyright 2020 Salesforce, Inc.

     ~ All Rights Reserved

     ~ Company Confidential

   -->

   <Flow xmlns="http://soap.sforce.com/2006/04/metadata">

     <apiVersion>51.0</apiVersion>

     <interviewLabel>Flow1 {!$Flow.CurrentDateTime}</interviewLabel>

     <label>Flow1</label>

     <processMetadataValues>

       <name>BuilderType</name>

       <value>

         <stringValue>LightningFlowBuilder</stringValue>

       </value>

     </processMetadataValues>

     <processMetadataValues>

       <name>OriginBuilderType</name>

       <value>

         <stringValue>LightningFlowBuilder</stringValue>

       </value>

     </processMetadataValues>

     <processType>AutoLaunchedFlow</processType>

     <recordLookups>

       <name>getAcc</name>

```


Metadata Types BatchProcessJobDefinition

```
       <label>getAcc</label>

       <locationX>614</locationX>

       <locationY>465</locationY>

       <assignNullValuesIfNoRecordsFound>false</assignNullValuesIfNoRecordsFound>

       <filterLogic>and</filterLogic>

       <filters>

         <field>Id</field>

         <operator>EqualTo</operator>

         <value>

           <elementReference>recordId</elementReference>

         </value>

       </filters>

       <getFirstRecordOnly>true</getFirstRecordOnly>

       <object>Account</object>

       <storeOutputAutomatically>true</storeOutputAutomatically>

     </recordLookups>

     <start>

       <locationX>73</locationX>

       <locationY>213</locationY>

       <connector>

         <targetReference>getAcc</targetReference>

       </connector>

     </start>

     <status>Draft</status>

     <variables>

       <name>recordId</name>

       <dataType>String</dataType>

       <isCollection>false</isCollection>

       <isInput>true</isInput>

       <isOutput>false</isOutput>

     </variables>

   </Flow>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

     <types>

       <members>*</members>

       <name>BatchProcessJobDefinition</name>

     </types>

     <types>

       <members>Flow1</members>

       <name>Flow</name>

     </types>

     <version>51.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


### Metadata Types BillingSettings BillingSettings

Represents the settings for Salesforce Billing.

Parent Type and Manifest Access

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

[In the package manifest, all the settings metadata types for the org are accessed using the “Settings” name. See Settings for more details.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_settings.htm)

File Suffix and Directory Location

### The BillingSettings values are stored in the BillingSettings.settings file in the settings folder. The .settings

files are different from other named components, because there’s only one settings file for each settings component.

Version

### BillingSettings components are available in API version 62.0 and later.

Special Access Rules

These settings are available when Billing is enabled.

Fields

**Field Name** **Description**

```
acctRecGlAccount

billingContextDefinition

billingContextSourceMapping

```

**Field Type**
string

**Description**
General ledger account to record the credit amount for unrealized or realized losses
and the debit amount for unrealized or realized gains in transaction journals. Available
in API version 64.0 and later.

**Field Type**
string

**Description**
[Name of the context definition that the Create Billing Schedules for Orders API uses](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_create_billing_schedules.htm)
to understand your order data. Available in API version 64.0 and later.

**Field Type**
string

**Description**
Name of the context mapping that links Order fields to billing transaction context
nodes. Available in API version 64.0 and later.


Metadata Types BillingSettings

**Field Name** **Description**

```
billingIntraCtxtSrcMapping

defaultAPClosureDPEDefnName

defaultApplyCreditMemoFlow

defaultBillingTreatment

defaultEmailTemplate

defaultInvPreviewTemplate

defaultInvoiceDocTemplate

defaultLegalEntity

```

**Field Type**
string

**Description**
Name of the custom context mapping that maps your custom or standard Order fields
to billing transaction context nodes. Available in API version 64.0 and later.

**Field Type**
string

**Description**
Org-wide default value to specify the Data Processing Engine (DPE) definition to close
legal entity accounting periods. Available in API version 64.0 and later.

**Field Type**
string

**Description**
Default flow that’s used to apply the credit memo to invoices. Available in API version
64.0 and later.

**Field Type**
string

**Description**
Org-wide default value to specify the name of the billing treatment. Available in API
version 64.0 and later.

**Field Type**
string

**Description**
Default email template to send the generated invoice PDFs. Available in API version
64.0 and later.

**Field Type**
string

**Description**
Default template to generate PDFs of invoice previews. Available in API version 64.0
and later.

**Field Type**
string

**Description**
Default template to generate PDFs of invoices. Available in API version 64.0 and later.

**Field Type**
string


Metadata Types BillingSettings

**Field Name** **Description**

**Description**
Org-wide default value to specify the name of the legal entity. Available in API version
64.0 and later.

```
defaultTaxTreatment

enableBillingDisputeManagement

enableBillingSetup

enableCreditMemoSequenceService

enableCrMemoApplicationToPostedInvoices

enableFailedPaymentsRetry

```

**Field Type**
string

**Description**
Org-wide default value to specify the name of the tax treatment. Available in API
version 64.0 and later.

**Field Type**
boolean

**Description**
Indicates whether to enable Dispute Management ( `true` ) or not ( `false` ). The default
value is `false` . Available in API version 66.0 and later.

**Field Type**
boolean

**Description**
Indicates whether to enable Billing setting ( `true` ) or not ( `false` ). The default value
is `false` .

**Field Type**
boolean

**Description**
Indicates whether to mandate the application of sequence policy for credit memos
( `true` ) or not ( `false` ). The default value is `false` .

Available in API version 66.0 and later with Revenue Cloud Billing.

**Field Type**
boolean

**Description**

Indicates whether to enable Apply Credits to Posted Invoices setting ( `true` ) or not
( `false` ). The default value is `false` .

This setting automates settlement of invoices through application of credits to posted
invoices. The credit application level determines whether credits are automatically
applied to invoices or invoice lines.

**Field Type**
boolean


Metadata Types BillingSettings

**Field Name** **Description**

**Description**

Indicates whether to retry failed payment schedule items automatically based on the
defined payment retry rules ( `true` ) or not ( `false` ). The default value is `false` .
Available in API version 66.0 and later.

```
enableForeignExchangeTrxnJrnlCreation

enableInvoiceEmailDelivery

enableInvoicePdfGeneration

enableInvoiceSequenceService

enableNegInvoiceLnConversionToCrMemoLn

```

**Field Type**
boolean

**Description**

Indicates whether to create Transaction Journal records for invoices that hold balance
amounts (partially settled and not fully settled posted invoices) to record foreign
exchange unrealized gains or losses during the closure activity of a legal entity
accounting period. The default value is `false` . Available in API version 65.0 and later
with Revenue Cloud Billing.

**Field Type**
boolean

**Description**
Indicates whether to enable Configure Email Delivery Settings ( `true` ) or not ( `false` ).
The default value is `false` . Available in API version 63.0 and later with Revenue Cloud
Billing.

**Field Type**
boolean

**Description**
Indicates whether to enable Document Generation setting ( `true` ) or not ( `false` ).
The default value is `false` . Available in API version 63.0 and later with Revenue Cloud
Billing.

**Field Type**
boolean

**Description**

Indicates whether to mandate the application of sequence policy for posted invoices
( `true` ) or not ( `false` ). The default value is `false` .

If enabled, each posted invoice is assigned an invoice number. Available in API version
65.0 and later with Revenue Cloud Billing.

**Field Type**
boolean

**Description**
Indicates whether to enable Convert Negative Invoice Lines to Credit Memo Lines
setting ( `true` ) or not ( `false` ). The default value is `false` .


Metadata Types BillingSettings

**Field Name** **Description**

```
enablePaymentSchedulesAndItemsCreation

enableTransactionJournalCreation

enableTransactionsApplicationToInvoices

```

**Field Type**
boolean

**Description**

Indicates whether to create a default payment schedule policy and payment schedule
treatment ( `true` ) or not ( `false` ). The default value is `false` .

If enabled, payment schedules and payment schedule items are created during financial
transactions such as posting of invoices. Available in API version 64.0 and later with
Revenue Cloud Billing.

**Field Type**
boolean

**Description**

Indicates whether to create Transaction Journal records based on the defined general
ledger account assignment rules for the billing entities when billing transaction records
are created or updated ( `true` ) or not ( `false` ). The default value is `false` . Available
in API version 63.0 and later with Revenue Cloud Billing.

Billing transaction records include these transaction types.

**•** Invoice

**•** Invoice Line

**•** Invoice Line Tax

**•** Credit Memo

**•** Credit Memo Line

**•** Credit Memo Line Tax

**•** Payment

**•** Refund

**•** Payment Line Invoice

**•** Payment Line Invoice Line

**•** Credit Memo Inv Application

**•** Credit Memo Line Invoice Line

**Field Type**
boolean

**Description**

Indicates whether to enable Credit Application Level setting ( `true` ) or not ( `false` ).
The default value is `false` .

**Revenue Cloud Advanced**

This setting applies balances of credit memos to invoices or balances of credit memo
lines to invoice lines. For the latter, amounts and balances on the invoices are rolled-up
from the related invoice lines.


Metadata Types BillingSettings

**Field Name** **Description**

**Revenue Cloud Billing**

This setting applies balances of credit memos and payments to invoices or balances
of credit memo lines and payments lines to invoice lines. For the latter, amounts and
balances on the invoices are rolled-up from the related invoice lines.

```
enableTrxnAmountsStorageInCorpCurrency

realisedGainGlAccount

realisedLossGlAccount

ruleBasedCrAndPymtAppln

unrealisedGainGlAccount

unrealisedLossGlAccount

```

**Field Type**
boolean

**Description**

Indicates whether to allow conversion of amounts of the Invoice, Invoice Line, Credit
Memo, and Credit Memo Line records to your corporate currency ( `true` ) or not
( `false` ). The default value is `false` . Available in API version 63.0 and later.

Store the converted amounts in corporate currency-specific amount fields.

**Field Type**
string

**Description**
Name of the general ledger account to record realized gains in transaction journals.
Available in API version 64.0 and later.

**Field Type**
string

**Description**
Name of the general ledger account to record realized losses in transaction journals.
Available in API version 64.0 and later.

**Field Type**
string

**Description**
Automates the settlement of the posted invoices by applying payments and credits
that meet the specified application rules. The rules application level determines whether
payments or credits are applied first to the invoices. The ruleset displays a list of
selectable rules. Available in API version 66.0 and later.

**Field Type**
string

**Description**
Name of the general ledger account to record unrealized gains in transaction journals.
Available in API version 64.0 and later.

**Field Type**
string


### Metadata Types BlacklistedConsumer

**Field Name** **Description**

**Description**
Name of the general ledger account to record unrealized losses in transaction journals.
Available in API version 64.0 and later.

Declarative Metadata Sample Definition

The following is an example of a BillingSettings component.

```
   <BillingSettings xmlns="http://soap.sforce.com/2006/04/metadata">

      <enableBillingSetup>true</enableBillingSetup>

      <enableForeignExchangeTrxnJrnlCreation>true</enableForeignExchangeTrxnJrnlCreation>

      <enableInvoicePdfGeneration>true</enableInvoicePdfGeneration>

     <enableTransactionsApplicationToInvoices>true</enableTransactionsApplicationToInvoices>

     <enableCrMemoApplicationToPostedInvoices>true</enableCrMemoApplicationToPostedInvoices>

      <enableInvoiceEmailDelivery>true</enableInvoiceEmailDelivery>

      <enableInvoiceSequenceService>true</enableInvoiceSequenceService>

      <enableTransactionJournalCreation>true</enableTransactionJournalCreation>

      <enableTrxnAmountsStorageInCorpCurrency>true</enableTrxnAmountsStorageInCorpCurrency>

      <enablePaymentSchedulesAndItemsCreation>true</enablePaymentSchedulesAndItemsCreation>

   </BillingSettings>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>Billing</members>

        <name>Settings</name>

      </types>

      <version> 66.0 </version>

   </Package>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The wildcard
[applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the manifest](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_settings.htm)
[file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### BlacklistedConsumer

Represents a connected app that is inaccessible to your Salesforce org’s users.This type extends the Metadata metadata type and inherits
its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.


Metadata Types BlacklistedConsumer

File Suffix and Directory Location

BlacklistedConsumer components have the suffix `.blacklistedConsumer` and are stored in the `blacklistedConsumers`
folder.

Version

BlacklistedConsumer components are available in API version 49.0 and later.

Fields

This metadata type contains the following fields:

**Field Name** **Field Type** **Description**

`blockedByApiWhitelisting` boolean Set to `true` to apply the Permitted Users policy, `Admin approved`
`users are pre-authorized` to all connected apps in the org.

This policy limits access to only users with the associated profile or
permission set assigned to the app. Set to `false` to allow access to
the connected app. False is the default value.

`consumerKey` string

Required. A value used by the consumer for identification of the
connected app to Salesforce. Referred to as `client_id` in OAuth 2.0.

After you define and save the value, it can’t be edited. The value must
be alphanumeric, can’t contain special characters or spaces, and must
be between 8–256 characters. Consumer keys must be globally unique.

`consumerName` string Required. The name of the connected app being blocked.

`masterLabel` string Required. The primary label for the connected app record.

Declarative Metadata Sample Definition

The following is an example of a component.

```
<BlacklistedConsumer xmlns="http://soap.sforce.com/2006/04/metadata">

   <consumerKey>testConsumerKey</consumerKey>

   <consumerName>testName</consumerName>

   <blockedByApiWhitelisting>false</blockedByApiWhitelisting>

   <masterLabel>myTest</masterLabel>

</BlacklistedConsumer>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>*</members>

     <name>BlacklistedConsumer</name>

   </types>

```


### Metadata Types Bot

```
      <version>49.0</version>

   </Package>

```

Usage

Use this type judiciously for connected apps that you want to make inaccessible to your org’s users. Blocking an app ends all current
user sessions and prevents future sessions. To block malicious attempts to access your org’s data, we recommend using API Access
Control instead. This feature restricts users from accessing your Salesforce APIs unless they are pre-authorized through an approved
connected app.

### Bot

Represents a definition of an Einstein Bot configuration that can have one or more versions. Only one version can be active.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### Bot components have the suffix .bot and are stored in the bots folder.

Version

### Bot components are available in API version 43.0 and later.

Special Access Rules

### Bot is available only if Chat and Einstein Bots are enabled in your org. Bot metadata deployment and retrieval are not supported for Lead Nurturing and Sales Coach Agents.

Fields

**Field Name** **Field Type** **Description**

`agentDSLEnabled` boolean Reserved for internal use.

`agentTemplate` string If this Bot represents an agent, this field represents the name of the agent
template used to create it. Available in API version 64.0 and later.

```
agentType

```

GenAiAgentType
(enumeration of
type string)

`botMlDomain` LocalMlDomain on
page 485

Specifies the agent type for this agent. For example,
`AgentforceServiceAgent` . Available in API version 64.0 and
later.

Represents the Einstein intent set that groups intents, entities, and
variables associated with a bot. All Einstein Bot versions under the same
bot now share an intent set. Available in API version 44.0 and later.


Metadata Types Bot

**Field Name** **Field Type** **Description**

`botUser` string Specifies the username of the user account, not the first and last name
or the user ID. Available in API version 46.0 and later.

`botVersions` BotVersion on page Represents the configuration details for a specific Einstein Bots version,
505 including dialogs, intents, entities, and variables.

`contextVariables` ConversationContextVariable Represents the context variables that enable your bot to gather customer
on page 486 information regardless of channel. Available in API 45.0 and later.

`conversationChannelProviders` ConversationDefintonChannelProvider **i** Represents a list of the conversation channels linked to the bot. Available

[] on page 487 in API version 51.0 and later.

`defaultOutboundFlow` string Specifies a fallback escalation behavior if the primary agent escalation
behavior is not available. For example, Agentforce Service Agents can

route conversations to human service reps. Available in API version 65.0
and later.

`description` string A description of the bot.

`label` string Label that identifies the bot throughout the Salesforce user interface.

`logPrivateConversationData` boolean Specifies whether to log customer inputs as part of conversation data
( `true` ) or not ( `false` ). Available in API version 48.0 and later.

`pageContextVariables` PageContextVariable Provides page-level context variables for the bot. Available in API version
on page 488[] 64.0 and later.

sessionTimeout int Represents the maximum amount of minutes that a bot session can be
idle. Available in API version 58.0 and later.

```
type

```

LocalMlDomain

BotType Required. The default value is `Bot` . This field represents the configuration
(enumeration of type of the bot. Valid values are:
type string)

**•** `Bot`         - Default Einstein Bot configuration.

**•** `ExternalCopilot`         - An external-facing agent. For example,
an Agentforce Service agent.

**•** `InternalCopilot`         - An internal-facing agent. For example,
an Agentforce Employee agent.

An Einstein Intent Set local to the current bot version.

**Field Name** **Field Type** **Description**

`label` string Label that represents an Einstein Intent Set local to the current bot version
throughout the Salesforce user interface.

`mlIntents` MlIntent[] List of intents associated with this local intent set.

`mlSlotClasses` MlSlotClass[] List of entities associated with this local intent set.


Metadata Types Bot

**Field Name** **Field Type** **Description**

`name` string Required. This unique name prevents conflicts with other local Einstein Intent
Sets. This name can contain only underscores and alphanumeric characters

and must be unique in your org. It must begin with a letter, not include spaces,
not end with an underscore, and not contain two consecutive underscores.

ConversationContextVariable

A context variable local to the current bot version. Available in API version 45.0 and later.

**Field Name** **Field Type** **Description**

`contextVariableMappings` ConversationContextVariableMapping Represents the mapping between a context variable, channel type, and sObject
on page 487 field.

```
dataType

```

ConversationDataType Required. Represents the data type of the context variable. Valid values are:
(enumeration of type

**•** `Text`

string)

**•** `Text`

**•** `Number`

**•** `Boolean`

**•** `Object`

**•** `Date`

**•** `DateTime`

**•** `Currency`

**•** `Id`

`description` string A description of this variable. This value may be used by the Agentforce planner
service. Available in API version 63.0 and later.

`developerName` string Required. Represents the name of the context variable. Can contain only
underscores and alphanumeric characters and must be unique in your org. It

must begin with a letter, not include spaces, not end with an underscore, and
not contain two consecutive underscores.

`includeInPrompt` boolean Indicates whether the variable is injected into the prompt sent to the Agentforce
model. If `true`, the variable appears in the **Included Fields** section of the UI.

Note: The default variables `Id`, `EndUserId`, and
`EndUserLanguage` always appear in the **Included Fields** section
of the UI, regardless of their value of `includeInPrompt` . We
recommend that you don't change the value of `includeInPrompt`
for these default variables, as changing the value can prevent your agent
from accessing important session data.

Available in API version 63.0 and later.

`label` string Required. A label that identifies the context variable throughout the Salesforce
user interface.


Metadata Types Bot

**Field Name** **Field Type** **Description**

`SObjectType` string Valid values are:

**•** `BotDefinition`

**•** `Queue`

ConversationContextVariableMapping

Represents the mapping between a context variable, channel type, and sObject field.

**Field Name** **Field Type** **Description**

`fieldName` string Required. The API name of an SObject field to be used as part of the mapping.

```
messageType

```

MessageType Required. Represents the message channel. Valid values are:
(enumeration of type

**•** `Alexa`

string)

**•** `Alexa`

**•** `AppleBusinessChat` —Messages sent in enhanced Apple Messages
for Business channels.

**•** `EmbeddedMessaging` —Messages sent in Messaging for In-App and
Web channels. Available in API version 50.0 and later.

**•** `Facebook`

**•** `GoogleHome`

**•** `InternalCopilot`

**•** `Line`

**•** `Omega`

**•** `Phone`

**•** `Text`

**•** `WeChat`

**•** `WebChat`

**•** `WhatsApp`

`SObjectType` string Required. SObject type for the field property defined as part of the mapping.
Valid values are:

**•** `LiveChatTranscript`

**•** `MessagingEndUser`

**•** `MessagingSession`

ConversationDefinitionChannelProvider

The developer name of a conversation channel linked to the bot. Available in API version 51.0 and later.

Note: To add, edit, or remove a messaging channel, you must use the UI. If you deploy a bot with messaging channel providers,
those providers aren’t visible in Metadata API.


Metadata Types Bot

**Field Name** **Field Type** **Description**

`agentRequired` boolean Specifies whether an agent must be online for the bot to be active ( `true` ) or
not ( `false` ) The default is `false` .

`chatButtonName` string Required. The developer name of a LiveChatButton metadata component.

PageContextVariable

A page-level context variable used by the bot. Available in API version 64.0 and later.

**Field Name** **Field Type** **Description**

`SObjectType` string Specifies the sObject type associated with this page context variable.

```
dataType

```

ConversationDataType Required. Represents the data type of the page context variable. Valid values
(enumeration of type are:
string)

**•** `Text`

**•** `Number`

**•** `Boolean`

**•** `Object`

**•** `Date`

**•** `DateTime`

**•** `Currency`

**•** `Id`

`description` string A description of the page context variable.

`developerName` string Required. Represents the unique API name of the page context variable. Can
contain only underscores and alphanumeric characters and must be unique

in your org. It must begin with a letter, not include spaces, not end with an
underscore, and not contain two consecutive underscores.

`label` string Required. A label that identifies the page context variable throughout the
Salesforce user interface.

Declarative Metadata Sample Definition

The following is an example of a Bot. This example has been trimmed to make it easier to read.

```
<?xml version="1.0" encoding="UTF-8"?>

<Bot xmlns="http://soap.sforce.com/2006/04/metadata">

   <botMlDomain>

     <label>Astros Pizza</label>

     <mlIntents>

        <developerName>New_Order</developerName>

        <label>New Order</label>

        <mlIntentUtterances>

          <utterance>Today is pie day so I want pie</utterance>

```


Metadata Types Bot

```
           </mlIntentUtterances>

        </mlIntents>

        <mlSlotClasses>

           <developerName>Size</developerName>

           <extractionType>Value</extractionType>

           <label>Size</label>

           <mlSlotClassValues>

             <synonymGroup>

               <languages>en_US</languages>

               <terms>Big</terms>

               <terms>Extra Large</terms>

               <terms>X-Large</terms>

               <terms>Grande</terms>

               <terms>Huge</terms>

             </synonymGroup>

             <value>Large</value>

           </mlSlotClassValues>

        </mlSlotClasses>

        <name>Astros_Pizza_ld1</name>

      </botMlDomain>

      <botVersions>

        <fullName>v1</fullName>

        <botDialogGroups>

           <developerName>Order_Management</developerName>

           <label>Order Management</label>

        </botDialogGroups>

        <botDialogs>

           <botDialogGroup>Order_Management</botDialogGroup>

           <botSteps>

             <botMessages>

               <message> ������Pizza Time! ������ </message>

             </botMessages>

             <type>Message</type>

           </botSteps>

           <botSteps>

             <botStepConditions>

               <leftOperandName>Verified_User</leftOperandName>

               <leftOperandType>ConversationVariable</leftOperandType>

               <operatorType>Equals</operatorType>

               <rightOperandValue>false</rightOperandValue>

             </botStepConditions>

             <botSteps>

               <botNavigation>

                  <botNavigationLinks>

                    <targetBotDialog>Customer_Verification</targetBotDialog>

                  </botNavigationLinks>

                  <type>Call</type>

               </botNavigation>

               <type>Navigation</type>

             </botSteps>

             <type>Group</type>

           </botSteps>

           <botSteps>

             <botStepConditions>

```


Metadata Types Bot

```
               <leftOperandName>Location</leftOperandName>

               <leftOperandType>ConversationVariable</leftOperandType>

               <operatorType>IsNotSet</operatorType>

             </botStepConditions>

             <botSteps>

               <botNavigation>

                  <botNavigationLinks>

                    <targetBotDialog>Select_Location</targetBotDialog>

                  </botNavigationLinks>

                  <type>Call</type>

               </botNavigation>

               <type>Navigation</type>

             </botSteps>

             <type>Group</type>

           </botSteps>

           <botSteps>

             <botVariableOperation>

               <botInvocation>

                  <invocationActionName>CreateOrderService</invocationActionName>

                  <invocationActionType>apex</invocationActionType>

                  <invocationMappings>

                    <parameterName>customer</parameterName>

                    <type>Input</type>

                    <variableName>Contact</variableName>

                    <variableType>ConversationVariable</variableType>

                  </invocationMappings>

                  <invocationMappings>

                    <parameterName>location</parameterName>

                    <type>Input</type>

                    <variableName>Location</variableName>

                    <variableType>ConversationVariable</variableType>

                  </invocationMappings>

                  <invocationMappings>

                    <parameterName>output</parameterName>

                    <type>Output</type>

                    <variableName>Pizza_Order</variableName>

                    <variableType>ConversationVariable</variableType>

                  </invocationMappings>

               </botInvocation>

               <type>Set</type>

             </botVariableOperation>

             <type>VariableOperation</type>

           </botSteps>

           <botSteps>

             <botMessages>

              <message>Perfect, let&apos;s work on your order from our {!Location.Name}

    location</message>

             </botMessages>

             <type>Message</type>

           </botSteps>

           <botSteps>

             <botNavigation>

               <botNavigationLinks>

                  <targetBotDialog>Add_Items_to_Order</targetBotDialog>

```


Metadata Types Bot

```
               </botNavigationLinks>

               <type>Redirect</type>

             </botNavigation>

             <type>Navigation</type>

           </botSteps>

           <developerName>New_Order</developerName>

           <label>New Order</label>

           <mlIntent>New_Order</mlIntent>

           <showInFooterMenu>false</showInFooterMenu>

        </botDialogs>

        <conversationVariables>

           <dataType>Object</dataType>

           <developerName>Contact</developerName>

           <label>Contact</label>

        </conversationVariables>

        <conversationVariables>

           <dataType>Text</dataType>

           <developerName>Delivery_Address</developerName>

           <label>Delivery Address</label>

        </conversationVariables>

        <conversationVariables>

           <dataType>Object</dataType>

           <developerName>Pizza_Order</developerName>

           <label>Pizza Order</label>

        </conversationVariables>

        <entryDialog>Welcome</entryDialog>

        <mainMenuDialog>Main_Menu</mainMenuDialog>

      </botVersions>

      <contextVariables>

        <contextVariableMappings>

           <SObjectType>LiveChatTranscript</SObjectType>

           <fieldName>LiveChatTranscript.ChatKey</fieldName>

           <messageType>WebChat</messageType>

        </contextVariableMappings>

        <dataType>Text</dataType>

        <developerName>ChatKey</developerName>

        <label>Chat Key</label>

      </contextVariables>

      <contextVariables>

        <contextVariableMappings>

           <SObjectType>LiveChatTranscript</SObjectType>

           <fieldName>LiveChatTranscript.ContactId</fieldName>

           <messageType>WebChat</messageType>

        </contextVariableMappings>

        <dataType>Id</dataType>

        <developerName>ContactId</developerName>

        <label>Contact Id</label>

      </contextVariables>

      <contextVariables>

        <contextVariableMappings>

           <SObjectType>LiveChatTranscript</SObjectType>

           <fieldName>LiveChatTranscript.LiveChatVisitorId</fieldName>

           <messageType>WebChat</messageType>

        </contextVariableMappings>

```


### Metadata Types BotBlock

```
        <dataType>Id</dataType>

        <developerName>EndUserId</developerName>

        <label>End User Id</label>

      </contextVariables>

      <contextVariables>

        <contextVariableMappings>

           <SObjectType>LiveChatTranscript</SObjectType>

           <fieldName>LiveChatTranscript.Id</fieldName>

           <messageType>WebChat</messageType>

        </contextVariableMappings>

        <dataType>Id</dataType>

        <developerName>RoutableId</developerName>

        <label>Routable Id</label>

      </contextVariables>

   ....<conversationChannelProviders>

        <agentRequired>false</agentRequired>

        <chatButtonName>Chat_Button_For_Bot</chatButtonName>

      </conversationChannelProviders>

      <label>Astro&apos;s Pizza</label>

   </Bot>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>Pizza_Bot</members>

        <name>Bot</name>

      </types>

      <version>45.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### BotBlock

Represents the configuration details for a specific Einstein Bot block, including dialogs and variables.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### BotBlock components have the suffix .botBlock and are stored in the botBlocks folder.


Metadata Types BotBlock

Version

BotBlock components are available in API version 58.0 and later.

Special Access Rules

BotBlock is available only if Chat and Einstein Bots are enabled in your org.

Bot metadata deployment and retrieval are not supported for Lead Nurturing and Sales Coach Agents.

Fields

**Field Name** **Description**

```
botBlockVersions

description

masterLabel

richContentEnabled

```

BotBlockVersion

**Field Type**

BotBlockVersion[]

**Description**
The configuration details for specific Einstein Bot block versions, including dialogs and
variables.

**Field Type**
string

**Description**
A description of the bot block.

**Field Type**
string

**Description**

Required.

A user-friendly label for BotBlock, which is defined when the block is created.

**Field Type**
boolean

**Description**
Indicates whether the block is available for enhanced bots ( `true` ) or for only standard
bots ( `false` ). The default is `false` .

Represents the configuration details for an Einstein Bot block version, including dialogs and variables.

**Field Name** **Description**

```
botDialogs

```

**Field Type**

BotDialog[] on page 509


Metadata Types BotBlock

**Field Name** **Description**

**Description**
The list of dialogs in this bot block.

```
conversationGoals

conversationLanguages

conversationVariables

description

mlDomain

permissionSet

status

```

**Field Type**

ConversationDefinitionGoal[] on page 529

**Description**
The list of goals in this bot block. Available in API version 57.0 and later.

**Field Type**
string

**Description**

Required.

Specifies the language of the bot block.

**Field Type**

ConversationVariable[] on page 530

**Description**
A container that stores a specific piece of data collected from the customer. You can
use variables within dialog actions as both inputs and outputs. Available in API version
44.0 and later.

**Field Type**
string

**Description**
A description of the bot block.

**Field Type**

LocalMlDomain on page 485

**Description**

Required.

The Einstein Intent Set that groups intents, entities, and variables associated with a
block.

**Field Type**
string

**Description**
The permission set associated with the bot block. Available in API version 59.0 and
later.

**Field Type**
ConvDefBlockVersionStatus (enumeration of type string)


Metadata Types BotBlock

**Field Name** **Description**

**Description**

Required.

Indicates whether a block is published or is a draft.

Values are:

**•** `Published`

Declarative Metadata Sample Definition

The following is an example of a BotBlock component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <BotBlock xmlns="http://soap.sforce.com/2006/04/metadata">

      <access xsi:nil="true"/>

      <botBlockVersions>

        <fullName>Published</fullName>

        <botDialogs>

           <developerName>Test_Dialog_1646070168572</developerName>

           <label>Test_Dialog_1646070168572</label>

           <showInFooterMenu>false</showInFooterMenu>

        </botDialogs>

        <botDialogs>

           <developerName>Test_Dialog_1646070168926</developerName>

           <label>Test_Dialog_1646070168926</label>

           <showInFooterMenu>false</showInFooterMenu>

        </botDialogs>

        <botDialogs>

           <botSteps>

             <stepIdentifier>s4</stepIdentifier>

             <type>Wait</type>

           </botSteps>

           <developerName>Main_Menu</developerName>

           <label>Main Menu</label>

           <mlIntent>Main_Menu</mlIntent>

           <showInFooterMenu>false</showInFooterMenu>

        </botDialogs>

        <botDialogs>

           <botSteps>

             <botMessages>

               <message>Goodbye! Click the &quot;End Chat&quot; button to end this

   chat</message>

               <messageIdentifier>m2</messageIdentifier>

             </botMessages>

             <stepIdentifier>s6</stepIdentifier>

             <type>Message</type>

           </botSteps>

           <botSteps>

             <stepIdentifier>s7</stepIdentifier>

             <type>Wait</type>

```


Metadata Types BotBlock

```
           </botSteps>

           <developerName>End_Chat</developerName>

           <label>End Chat</label>

           <mlIntent>End_Chat</mlIntent>

           <showInFooterMenu>false</showInFooterMenu>

        </botDialogs>

        <botDialogs>

           <botSteps>

             <botMessages>

               <message>Unfortunately, there are no agents available at the

   moment</message>

               <messageIdentifier>m3</messageIdentifier>

             </botMessages>

             <stepIdentifier>s8</stepIdentifier>

             <type>Message</type>

           </botSteps>

           <botSteps>

             <stepIdentifier>s9</stepIdentifier>

             <type>Wait</type>

           </botSteps>

           <developerName>No_Agent_Available</developerName>

           <label>No Agent</label>

           <showInFooterMenu>false</showInFooterMenu>

        </botDialogs>

        <botDialogs>

           <botSteps>

             <botMessages>

               <message>Hi! I&apos;m your helpful bot.</message>

               <messageIdentifier>m1</messageIdentifier>

             </botMessages>

             <stepIdentifier>s1</stepIdentifier>

             <type>Message</type>

           </botSteps>

           <botSteps>

             <conversationRecordLookup>

               <SObjectType>Account</SObjectType>

               <conditions>

                  <leftOperand>Account.Phone</leftOperand>

                  <operatorType>Equal</operatorType>

                  <rightOperandValue>Value</rightOperandValue>

                  <sortOrder>0</sortOrder>

               </conditions>

               <lookupFields>

                  <fieldName>Account.Phone</fieldName>

               </lookupFields>

               <lookupFields>

                  <fieldName>Account.OwnerId</fieldName>

               </lookupFields>

               <maxLookupResults>1</maxLookupResults>

               <sourceVariableName>_LastCustomerInput</sourceVariableName>

               <sourceVariableType>ConversationVariable</sourceVariableType>

               <targetVariableName>MyCustomVariable</targetVariableName>

             </conversationRecordLookup>

             <stepIdentifier>s2</stepIdentifier>

```


Metadata Types BotBlock

```
             <type>RecordLookup</type>

           </botSteps>

           <botSteps>

             <botNavigation>

               <botNavigationLinks>

                  <targetBotDialog>Main_Menu</targetBotDialog>

                  <targetVariable xsi:nil="true"/>

                  <targetVariableType xsi:nil="true"/>

               </botNavigationLinks>

               <type>Redirect</type>

             </botNavigation>

             <stepIdentifier>s3</stepIdentifier>

             <type>Navigation</type>

           </botSteps>

           <developerName>Welcome</developerName>

           <label>Welcome</label>

           <mlIntent>Welcome</mlIntent>

           <showInFooterMenu>false</showInFooterMenu>

        </botDialogs>

        <conversationLanguages>en_US</conversationLanguages>

        <conversationVariables>

           <dataType>Text</dataType>

           <developerName>TestVariableABC</developerName>

           <label>TestVariableABC</label>

        </conversationVariables>

        <conversationVariables>

           <dataType>Text</dataType>

           <developerName>TestVariableXYZ</developerName>

           <label>TestVariableXYZ</label>

        </conversationVariables>

        <conversationVariables>

           <collectionType>List</collectionType>

           <dataType>Object</dataType>

           <developerName>MyCustomVariable</developerName>

           <label>MyCustomVariable</label>

        </conversationVariables>

        <description>Created for testing.</description>

        <mlDomain>

           <label>vPub</label>

           <mlIntents>

             <developerName>End_Chat</developerName>

             <label>End Chat</label>

             <mlIntentUtterances>

               <language>es</language>

               <utterance>Utterance1</utterance>

             </mlIntentUtterances>

             <mlIntentUtterances>

               <language>es</language>

               <utterance>Utterance2</utterance>

             </mlIntentUtterances>

             <mlIntentUtterances>

               <language>es</language>

               <utterance>Utterance3</utterance>

             </mlIntentUtterances>

```


### Metadata Types BotTemplate

```
           </mlIntents>

           <mlIntents>

             <description>Main Menu Intent</description>

             <developerName>Main_Menu</developerName>

             <label>Main Menu</label>

           </mlIntents>

           <mlIntents>

             <description>Welcome Intent</description>

             <developerName>Welcome</developerName>

             <label>Welcome</label>

           </mlIntents>

           <name>blockDevName0001_vPub</name>

        </mlDomain>

        <status>Published</status>

      </botBlockVersions>

      <description>Collects the user&apos;s first name, last name, email address, phone

   number, and company name.</description>

      <masterLabel>User Info Collection Block</masterLabel>

      <richContentEnabled>true</richContentEnabled>

   </BotBlock>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>AgentTransfer</members>

        <name>BotBlock</name>

      </types>

      <version>58.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### BotTemplate

Represents the configuration details for a specific Einstein Bot template, including dialogs and variables.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### BotTemplate components have the suffix .botTemplate and are stored in the botTemplates folder.


Metadata Types BotTemplate

Version

BotTemplate components are available in API version 55.0 and later.

Special Access Rules

BotTemplate is available only if Chat and Einstein Bots are enabled in your org.

Bot metadata deployment and retrieval are not supported for Lead Nurturing and Sales Coach Agents.

Fields

**Field Name** **Description**

```
botDialogGroups

botDialogs

conversationLanguages

contextVariables

conversationGoals

conversationSystemDialogs

```

**Field Type**

BotDialogGroup[] on page 508

**Description**
The list of dialog groups in this bot template.

**Field Type**

BotDialog[] on page 509

**Description**
The list of dialogs in this bot template.

**Field Type**
string

**Description**

Required.

Specifies the language of the bot template.

**Field Type**

ConversationContextVariable[] on page 486

**Description**
Represents the context variables that enable your bot to gather customer information
regardless of channel.

**Field Type**

ConversationDefinitionGoal[] on page 529

**Description**
The list of goals in this bot template. Available in API version 57.0 and later.

**Field Type**

ConversationSystemDialog[] on page 530

**Description**
A system function assigned to a dialog.


Metadata Types BotTemplate

**Field Name** **Description**

```
conversationVariables

description

entryDialog

icon

mainMenuDialog

masterLabel

mlDomain

```

**Field Type**

ConversationVariable[] on page 530

**Description**
A container that stores a specific piece of data collected from the customer. You can
use variables within dialog actions as both inputs and outputs.

**Field Type**
string

**Description**
A description of the bot template.

**Field Type**
string

**Description**
A reference to the first dialog that the bot presents to your customer. For example,
`Welcome` .

**Field Type**
string

**Description**
The icon used to identify the template.

**Field Type**
string

**Description**
A reference to the dialog identified as the main menu dialog. For example, `Main`
`Menu` .

**Field Type**
string

**Description**

Required.

A user-friendly label for BotTemplate, which is defined when the BotTemplate is created.

**Field Type**

LocalMlDomain on page 485

**Description**

Required.

Represents the Einstein Intent Set that groups intents, entities, and variables associated
with a template.


Metadata Types BotTemplate

**Field Name** **Description**

```
permissionSet

richContentEnabled

type

```

**Field Type**
string

**Description**
The permission set associated with the bot template. Available in API version 59.0 and
later.

**Field Type**
boolean

**Description**
Indicates whether the template is available for enhanced bots ( `true` ) or for standard
bots ( `false` ). The default is `false` .

**Field Type**
BotType (enumeration of type string)

**Description**
This field represents the configuration type of the bot. The default value is `Bot` .

Valid values are:

**•** `Bot` —Default Einstein Bot configuration.

**•** `ExternalCopilot`  - An external-facing agent. For example, an Agentforce
Service agent.

**•** `InternalCopilot`  - An internal-facing agent. For example, an Agentforce
Employee agent.

Declarative Metadata Sample Definition

The following is an example of a BotTemplate component.

```
<?xml version="1.0" encoding="UTF-8"?>

<BotTemplate xmlns="http://soap.sforce.com/2006/04/metadata">

   <botDialogGroups>

     <developerName>dialog_group1</developerName>

     <label>dialog group1</label>

   </botDialogGroups>

   <botDialogs>

     <developerName>Test_Dialog_1</developerName>

     <label>Test_Dialog_1</label>

     <showInFooterMenu>false</showInFooterMenu>

   </botDialogs>

   <botDialogs>

     <developerName>Test_Dialog_2</developerName>

     <label>Test_Dialog_2</label>

     <showInFooterMenu>false</showInFooterMenu>

   </botDialogs>

   <botDialogs>

     <botSteps>

```


Metadata Types BotTemplate

```
           <botMessages>

             <message>Hi! I&apos;m your helpful bot.</message>

             <messageIdentifier>m1</messageIdentifier>

           </botMessages>

           <stepIdentifier>s1</stepIdentifier>

           <type>Message</type>

        </botSteps>

        <botSteps>

          <conversationRecordLookup>

            <SObjectType>Account</SObjectType>

            <conditions>

               <leftOperand>Account.Phone</leftOperand>

               <operatorType>Equal</operatorType>

               <rightOperandValue>Value</rightOperandValue>

               <sortOrder>0</sortOrder>

            </conditions>

            <lookupFields>

               <fieldName>Account.Phone</fieldName>

            </lookupFields>

            <lookupFields>

               <fieldName>Account.OwnerId</fieldName>

            </lookupFields>

            <maxLookupResults>1</maxLookupResults>

            <sourceVariableName>_LastCustomerInput</sourceVariableName>

            <sourceVariableType>ConversationVariable</sourceVariableType>

            <targetVariableName>MyCustomVariable</targetVariableName>

          </conversationRecordLookup>

          <stepIdentifier>s2</stepIdentifier>

          <type>RecordLookup</type>

        </botSteps>

        <botSteps>

           <botNavigation>

             <botNavigationLinks>

               <targetBotDialog>Main_Menu</targetBotDialog>

             </botNavigationLinks>

             <type>Redirect</type>

           </botNavigation>

           <stepIdentifier>s3</stepIdentifier>

           <type>Navigation</type>

        </botSteps>

        <developerName>Welcome</developerName>

        <label>Welcome</label>

        <mlIntent>Welcome</mlIntent>

        <showInFooterMenu>false</showInFooterMenu>

      </botDialogs>

      <botDialogs>

        <botSteps>

           <stepIdentifier>s4</stepIdentifier>

           <type>Wait</type>

        </botSteps>

        <developerName>Main_Menu</developerName>

        <label>Main Menu</label>

        <mlIntent>Main_Menu</mlIntent>

        <showInFooterMenu>false</showInFooterMenu>

```


Metadata Types BotTemplate

```
      </botDialogs>

      <botDialogs>

        <botSteps>

           <botMessages>

             <message>Goodbye! Click the &quot;End Chat&quot; button to end this

   chat</message>

             <messageIdentifier>m2</messageIdentifier>

           </botMessages>

           <stepIdentifier>s6</stepIdentifier>

           <type>Message</type>

        </botSteps>

        <botSteps>

           <stepIdentifier>s7</stepIdentifier>

           <type>Wait</type>

        </botSteps>

        <developerName>End_Chat</developerName>

        <label>End Chat</label>

        <mlIntent>End_Chat</mlIntent>

        <showInFooterMenu>false</showInFooterMenu>

      </botDialogs>

      <botDialogs>

        <botSteps>

           <botMessages>

            <message>Unfortunately, there are no agents available at the moment</message>

             <messageIdentifier>m3</messageIdentifier>

           </botMessages>

           <stepIdentifier>s8</stepIdentifier>

           <type>Message</type>

        </botSteps>

        <botSteps>

           <stepIdentifier>s9</stepIdentifier>

           <type>Wait</type>

        </botSteps>

        <developerName>No_Agent_Available</developerName>

        <label>No Agent</label>

        <showInFooterMenu>false</showInFooterMenu>

      </botDialogs>

      <contextVariables>

        <contextVariableMappings>

           <SObjectType>LiveChatTranscript</SObjectType>

           <fieldName>LiveChatTranscript.ChatKey</fieldName>

           <messageType>WebChat</messageType>

        </contextVariableMappings>

        <dataType>Text</dataType>

        <developerName>ChatKey</developerName>

        <label>Chat Key</label>

      </contextVariables>

      <conversationLanguages>en_US</conversationLanguages>

      <conversationSystemDialogs>

        <dialog>No_Agent_Available</dialog>

        <type>TransferFailed</type>

      </conversationSystemDialogs>

      <conversationSystemDialogs>

```


Metadata Types BotTemplate

```
        <dialog>Test_Dialog_1</dialog>

        <type>ErrorHandling</type>

      </conversationSystemDialogs>

      <conversationVariables>

        <dataType>Text</dataType>

        <developerName>TestVariableXYZ</developerName>

        <label>TestVariableXYZ</label>

      </conversationVariables>

      <conversationVariables>

        <collectionType>List</collectionType>

        <dataType>Object</dataType>

        <developerName>MyCustomVariable</developerName>

        <label>MyCustomVariable</label>

      </conversationVariables>

      <description>Description of BotTemplate</description>

      <entryDialog>Test_Dialog_1</entryDialog>

      <icon>AA8qwqXXXXX</icon>

      <mainMenuDialog>Test_Dialog_2</mainMenuDialog>

      <masterLabel>Astro Bot</masterLabel>

      <mlDomain>

        <label>Astro Bot</label>

        <mlIntents>

           <developerName>End_Chat</developerName>

           <label>End Chat</label>

           <mlIntentUtterances>

             <utterance>Utterance1</utterance>

             <language>es</language>

           </mlIntentUtterances>

           <mlIntentUtterances>

             <utterance>Utterance2</utterance>

             <language>es</language>

           </mlIntentUtterances>

           <mlIntentUtterances>

             <utterance>Utterance3</utterance>

             <language>es</language>

           </mlIntentUtterances>

        </mlIntents>

        <mlIntents>

           <developerName>Main_Menu</developerName>

           <label>Main Menu</label>

           <description>Main Menu Intent</description>

        </mlIntents>

        <mlIntents>

           <developerName>Welcome</developerName>

           <label>Welcome</label>

           <description>Welcome Intent</description>

        </mlIntents>

        <name>Astro_Bot_ld1</name>

      </mlDomain>

      <richContentEnabled>true</richContentEnabled>

   </BotTemplate>

```


### Metadata Types BotVersion

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>BotTemplate</name>

      </types>

      <version>55.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### BotVersion

Represents the configuration details for a specific Einstein Bot version, including dialogs and variables.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### BotVersion components have the suffix .bot and are stored in the bot folder. BotVersion is a top-level child of Bot and shares its

suffix and file directory.

Version

### BotVersion components are available in API version 43.0 and later.

Special Access Rules

### BotVersion is available only if Chat and Einstein Bots are enabled in your org.

Bot metadata deployment and retrieval are not supported for Lead Nurturing and Sales Coach Agents.

Fields

**Field Name** **Description**

```
botDialogGroups

```

**Field Type**

BotDialogGroup[] on page 508

**Description**
The list of dialog groups in this bot version.


Metadata Types BotVersion

**Field Name** **Description**

```
botDialogs

company

conversationGoals

conversationPlanner

conversationSystemDialogs

conversationVariables

copilotPrimaryLangauge

copilotSecondaryLanguages

```

**Field Type**

BotDialog[] on page 509

**Description**
The list of dialogs in this bot version.

**Field Type**
string

**Description**
Reserved for internal use.

**Field Type**

ConversationDefinitionGoal[] on page 529

**Description**
The list of goals in this bot verion. Available in API version 57.0 and later.

**Field Type**

ConversationDefinitionPlanner[] on page 529

**Description**
Represents the API name of the Agent planner service GenAiPlanner on page 1359.

Available in API version 60.0 and later.

**Field Type**

ConversationSystemDialog[] on page 530

**Description**
A system function assigned to a dialog. Available in API version 48.0 and later.

**Field Type**

ConversationVariable[] on page 530

**Description**
A container that stores a specific piece of data collected from the customer. You
can use variables within dialog actions as both inputs and outputs. Available in
API version 44.0 and later.

**Field Type**
Language (enumeration of type string)

**Description**
Represents the primary language of a Copilot or Agent.

**Field Type**
string

**Description**
Reserved for internal use.


Metadata Types BotVersion

**Field Name** **Description**

```
entryDialog

initialIntentDetectionEnabled

intentDisambiguationEnabled

intentThreshold

intentV3Enabled

knowledgeActionEnabled

knowledgeFallbackEnabled

```

**Field Type**
string

**Description**

Required.

A reference to the first dialog that the bot presents to your customer. For example,
`Welcome` .

**Field Type**
boolean

**Description**
Reserved for internal use.

**Field Type**
boolean

**Description**
Reserved for internal use.

**Field Type**
double

**Description**

Specifies how strictly a user message must match with a bot intent.

Valid values are between 1 and 5, where 1 is the least strict and 5 is the most strict.

To turn on this feature, contact Salesforce Customer Support. This field is available
in API version 63.0 and later.

**Field Type**
boolean

**Description**
Reserved for internal use.

**Field Type**
boolean

**Description**
Indicates whether a knowledge action is enabled. The default value is `false` .

**Field Type**
boolean

**Description**
Reserved for internal use.


Metadata Types BotVersion

**Field Name** **Description**

```
mainMenuDialog

nlpProviders

responseDelayMilliseconds

role

surfacesEnabled

toneType

```

BotDialogGroup

The list of dialog groups in this bot version.

**Field Type**
string

**Description**
A reference to the dialog identified as the main menu dialog. For example, `Main`
`Menu` .

**Field Type**

ConversationDefinitionNlpProvider[] on page 532

**Description**
Defines the language provider which is used for a particular language. Available
in API version 49.0 and later.

**Field Type**
int

**Description**
An optional default or custom delay after every bot response to simulate typing.

**Field Type**
string

**Description**
Reserved for internal use.

**Field Type**
boolean

**Description**
Reserved for internal use.

**Field Type**
GenAiBotToneType (enumeration of type string)

**Description**
The tone of the bot. Valid values are:

**•** `Casual`

**•** `Formal`

**•** `Neutral`


Metadata Types BotVersion

**Field Name** **Description**

```
description

developerName

label

```

BotDialog

The list of dialogs in this bot version.

**Field Type**
string

**Description**
A description of the bot dialog group.

**Field Type**
string

**Description**

Required.

This unique name prevents conflicts with other dialog groups associated with the same
bot version. This name can contain only underscores and alphanumeric characters. The
name must begin with a letter, not include spaces, not end with an underscore, and not
contain two consecutive underscores.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Field Type**
string

**Description**

Required.

A label that identifies the dialog group throughout the Salesforce user interface.

**Field Name** **Description**

```
botDialogGroup

botSteps

description

```

**Field Type**
string

**Description**
The bot dialog group that contains this bot dialog.

**Field Type**

BotStep[] on page 511

**Description**
A list of steps that are executed as part of the dialog.

**Field Type**
string


Metadata Types BotVersion

**Field Name** **Description**

**Description**
A description of the bot dialog.

```
developerName

isPlaceholderDialog

label

mlIntent

mlIntentTrainingEnabled

```

**Field Type**
string

**Description**

Required.

This unique name prevents conflicts with other dialogs associated with the same bot version.
This name can contain only underscores and alphanumeric characters. It must begin with
a letter, not include spaces, not end with an underscore, and not contain two consecutive
underscores.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Field Type**
boolean

**Description**
In a bot block, indicates whether a dialog is a placeholder ( `true` ) or not ( `false` ). In a bot
template or bot version not associated with a bot block, this field is read-only and the value
is `false` . Available in API version 58.0 and later.

**Field Type**
string

**Description**

Required.

A label that identifies the dialog throughout the Salesforce user interface.

**Field Type**
string

**Description**

Required.

A label that identifies the dialog throughout the Salesforce user interface. The name of the
intent associated with a dialog.

**Field Type**
boolean

**Description**
Indicates whether Einstein is turned on to train an intent model for the dialog intent ( `true` )
or turned off for the exact match option ( `false` ). The default value is `false` . Available
in API version 46.0 and later.


Metadata Types BotVersion

**Field Name** **Description**

```
showInFooterMenu

```

BotStep

**Field Type**
boolean

**Description**
Indicates whether to show this dialog in the Bot Options menu. The default value is `false` .

A step that is executed as part of the dialog.

**Field Name** **Description**

```
booleanFilter

botInvocation

botMessages

botNavigation

botStepConditions

botSteps

```

**Field Type**
string

**Description**
This field is reserved for future use.

**Field Type**

BotInvocation on page 513

**Description**
Bot Invocation used by a BotStep of type `Invocation` .

**Field Type**

BotMessage[] on page 515

**Description**
List of bot messages used by a BotStep of type `Message` .

**Field Type**

BotNavigation on page 515

**Description**
Bot Navigation used by a BotStep of type `Navigation` .

**Field Type**

BotStepCondition[] on page 517

**Description**
List of BotStep conditions associated with a BotStep of type `Group` .

**Field Type**

BotStep[] on page 511

**Description**
List of BotSteps associated to a Bot Step of type `Group` .


Metadata Types BotVersion

**Field Name** **Description**

```
botVariableOperation

conditionLogicType

conversationRecordLookup

conversationStepGoalMappings

conversationSystemMessage

messageDefinition

stepIdentifier

```

**Field Type**

BotVariableOperation[] on page 518

**Description**
Bot Variable Operation used by a BotStep of type `VariableOperation` .

**Field Type**
ConversationDefinitionLogicalOperatorType (enumeration of type string)

**Description**
Represents the type of conditional logic used by a BotStep. Values are:

**•** `And`

**•** `Or`

Available in API version 58.0 and later.

**Field Type**

ConversationRecordLookup[] on page 523

**Description**
A lookup action to the Conversation record. Available in API version 46.0 and later.

**Field Type**

ConversationDefinitionStepGoalMapping[] on page 527

**Description**
The API name of a goal used by a BotStep of type GoalStep. Available in API version
57.0 and later.

**Field Type**

ConversationSystemMessage[] on page 527

**Description**
System messages that represent an action for a BotStep, such as transferring to an
agent or ending a chat. Available in API version 46.0 and later.

**Field Type**

ConversationDefinitionRichMessage[] on page 528

**Description**
List of configuration details used by a BotStep that references a messaging component.
Available in API version 54.0 and later.

**Field Type**
string

**Description**
A unique key that identifies a step within a dialog. It is used to link translated labels to
labels within the step. This field is recommended for all step records and is required
for translated step labels. Available in API version 53.0 and later.


Metadata Types BotVersion

**Field Name** **Description**

If a step is created via the UI, the `stepIdentifier` is automatically generated. If
a step is created via API, the `stepIdentifier` must be provided. The
`stepIdentifier` can contain letters, numbers, dashes, and underscores, up to
255 characters.

```
type

```

BotInvocation

**Field Type**
BotStepType (enumeration of type string)

**Description**

Required.

Values are:

**•** `GoalStep` (Available in API version 57.0 and later.)

**•** `Group`

**•** `Invocation`

**•** `Message`

**•** `Navigation`

**•** `RecordLookup` (Available in API version 48.0 and later.)

**•** `RichMessage` (Available in API version 54.0 and later.)

**•** `SystemMessage`

**•** `VariableOperation`

**•** `Wait`

Bot Invocation used by a BotStep of type `Invocation` .

**Field Name** **Description**

```
invocationActionName

invocationActionType

```

**Field Type**
string

**Description**
The name of the invocable action used by a Bot Invocation.

**Field Type**
ConversationInvocableTargetType (enumeration of type string)

**Description**
Available dialog action types are:

Values are:

**•** `apex`

**•** `externalService` (Available in API version 53.0 and later.)

**•** `flow`


Metadata Types BotVersion

**Field Name** **Description**

**•** `logFeedback` (Available in API version 51.0 and later.)

**•** `logGoalAchieved` (Deprecated in API version 57.0 and later.)

**•** `standardInvocableAction`

```
invocationMappings

```

BotInvocationMapping

**Field Type**

BotInvocationMapping[] on page 514

**Description**
List of Bot Invocation Mappings for a Bot Invocation.

List of Bot Invocation Mappings for a Bot Invocation.

**Field Name** **Description**

```
parameterName

recordName

type

value

```

**Field Type**
string

**Description**

Required.

Name of an Input/Output parameter of the parent Bot Invocation target.

**Field Type**
string

**Description**
Name of the record that is used as part of an Invocation mapping. Available in API
version 54.0 and later.

**Field Type**
BotInvocationMappingType (enumeration of type string)

**Description**

Required.

Values are:

**•** `Input`

**•** `Output`

**Field Type**
string

**Description**
Literal value to be assigned to the specified parameter.


Metadata Types BotVersion

**Field Name** **Description**

```
variableName

variableType

```

BotMessage

**Field Type**
string

**Description**
Name of the Bot Variable that is used as part of an Invocation mapping.

**Field Type**
ConversationVariableType (enumeration of type string)

**Description**
This field relates to the type of variable used in this invocation mapping.

Values are:

**•** `ContextVariable`

**•** `ConversationVariable`

**•** `PageContextVariable`

A bot message used by a BotStep of type `Message` .

**Field Name** **Description**

```
message

messageIdentifier

```

BotNavigation

**Field Type**
string

**Description**

Required.

Message to display as part of an outgoing message from the bot to the customer.

**Field Type**
string

**Description**
A unique key that identifies a message within a dialog. It is used to link translated labels
to labels within the message. This field is recommended for all message records and
is required for translated message labels. Available in API version 53.0 and later.

If a message is created via the UI, the `messageIdentifier` is automatically
generated. If a message is created via API, the `messageIdentifier` must be
provided. `messageIdentifier` can contain letters, numbers, dashes, and
underscores, up to 255 characters.

Bot navigation used by a BotStep of type `Navigation` .


Metadata Types BotVersion

**Field Name** **Description**

```
botNavigationLinks

type

```

BotNavigationLink

**Field Type**

BotNavigationLink[] on page 516

**Description**
List of Bot Navigation links associated with a Bot Navigation of type `Call` or
`Redirect` .

**Field Type**
BotNavigationType (enumeration of type string)

**Description**

Required.

Values are:

**•** `Call`

**•** `Redirect`

**•** `TransferToAgent`

List of Bot Navigation links associated with a Bot Navigation of type `Call` or `Redirect` .

**Field Name** **Description**

```
label

targetBotDialog

targetVariable

targetVariableType

```

**Field Type**
string

**Description**
Label displayed when more than one Bot Navigation Link is available under a Bot
Navigation of type `Redirect` . The target dialog label is used when no label is
provided.

**Field Type**
string

**Description**
Name of the target dialog to be called as part of this Bot Navigation Link.

**Field Type**
string

**Description**
In the Redirect to Dialog Rule Action, the ID of the target object variable to be called
as part of this Bot Navigation link. Available in API version 57.0 and later.

**Field Type**
ConversationVariableType (enumeration of type string)


Metadata Types BotVersion

**Field Name** **Description**

**Description**
In the Redirect to Dialog Rule Action, the type of variable referred to in
`targetVariable` . Available in API version 57.0 and later.

Values are:

**•** `ContextVariable`

**•** `ConversationVariable`

**•** `PageContextVariable`

BotStepCondition

List of BotStep conditions associated with a BotStep of type `Group` .

**Field Name** **Description**

```
leftOperandName

leftOperandType

operatorType

```

**Field Type**
string

**Description**

Required.

Name of the variable used as the left side of the condition operation.

**Field Type**
ConversationVariableType (enumeration of type string)

**Description**

Required.

Type of the variable used as the left side of the condition operation.

Values are:

**•** `ContextVariable`

**•** `ConversationVariable`

**•** `PageContextVariable`

**Field Type**
BotStepConditionOperatorType (enumeration of type string)

**Description**

Required.

Values are:

**•** `Equals`

**•** `GreaterThan` (Available in API version 47.0 and later.)

**•** `GreaterThanOrEqualTo` (Available in API version 47.0 and later.)

**•** `IsNotSet`


Metadata Types BotVersion

**Field Name** **Description**

**•** `IsSet`

**•** `LessThan` (Available in API version 47.0 and later.)

**•** `LessThanOrEqualTo` (Available in API version 47.0 and later.)

**•** `NotEquals`

```
rightOperandValue

```

BotVariableOperation

**Field Type**
string

**Description**
Value that is used as the right side of the condition operation. This value is ignored
when using `IsSet` and `IsNotSet` operators.

Bot variable operation used by a BotStep of type `VariableOperation` .

**Field Name** **Description**

```
askCollectIfSet

autoSelectIfSingleChoice

botInvocation

```

**Field Type**
boolean

**Description**
If `true`, the bot runs a Bot Variable Operation of type `Collect` regardless of whether
the variable already has a value. When a value exists for a variable, the bot asks the
user for the relevant information, and the bot overwrites the existing value with the
user-provided value. If `false`, the bot skips variables with an existing value and
maintains the existing value. The default is `false` . Available in API version 51.0 and
later.

**Field Type**
boolean

**Description**
If `true`, the bot automatically selects the answer in the conversation flow when only
one button choice is available in a Bot Variable Operation of type `Collect` and a
`quickReplyType` value of `Dynamic` . If `false`, the bot presents the single
button choice and waits for the user’s response. The default is `false` . Available in
API version 51.0 and later.

**Field Type**

BotInvocation on page 513

**Description**
Bot Invocation used to provide Dynamic choices by a Bot Variable Operation of type
`Collect` and `quickReplyType` of `Dynamic` .


Metadata Types BotVersion

**Field Name** **Description**

```
botMessages

botQuickReplyOptions

botVariableOperands

ignoreIntentRecognition

invalidInputBotNavigation

```

messageDefinition

```
optionalCollect

```

**Field Type**

BotMessage[] on page 515

**Description**
List of Bot Messages used as prompt messages by a Bot Variable Operation of type
`Collect` .

**Field Type**

BotQuickReplyOption[] on page 521

**Description**
List of static choice options used by a Bot Variable Operation of type `Collect` and
`quickReplyType` of `Static` .

**Field Type**

BotVariableOperand[] on page 522

**Description**
List of Bot Variable Operands associated with a Bot Variable of type `Set` or `Unset` .

**Field Type**
boolean

**Description**
If `true` the bot requires a response to a Question dialog step. The bot doesn't perform
intent recognition for any user messages that do not fit the entity requirements. The
bot repeats the question until the customer's response fits the entity requirements.
Available in API version 63.0 and later.

**Field Type**

BotNavigation on page 515

**Description**
Bot Navigation used by a Bot Variable Operation of type `Collect` . This navigation
is executed when the associated Bot Invocation doesn’t return any options.

**Field Type**

ConversationDefinitionRichMessage on page 528

**Description**
Configuration details that reference a messaging component. Outputs are used by a
Bot Variable Operation of type `Set` . Available in API version 58.0 and later.

**Field Type**
boolean

**Description**
If `true`, the bot asks the repair attempts once and then moves on to the next dialog
step. The default value is `false` . Available in API version 48.0 and later.


Metadata Types BotVersion

**Field Name** **Description**

```
quickReplyOptionTemplate

quickReplyType

quickReplyWidgetType

retryMessages

sourceVariableName

sourceVariableType

```

**Field Type**
string

**Description**
Formula template used to resolve a label for Dynamic choice options of type `Object` .

**Field Type**
BotQuickReplyType (enumeration of type string)

**Description**

Values are:

**•** `Dynamic`

**•** `Static`

**Field Type**
BotWidgetType (enumeration of type string)

**Description**

Values are:

**•** `Buttons`

**•** `Menu`

**Field Type**

BotMessage[] on page 515

**Description**
[In Conversation Repair, the messages assigned to repair attempts. Available in API](https://help.salesforce.com/articleView?id=bots_service_setup_dialog_question_text.htm&language=en_US)
version 48.0 and later.

**Field Type**
string

**Description**
Name of the source `VariableName` used in the variable operation. Available in
API version 47.0 and later.

**Field Type**
ConversationVariableType (enumeration of type string)

**Description**
This name defines the data type of `VariableName` used in the variable operation.

Values are:

**•** `ContextVariable`

**•** `ConversationVariable`

**•** `PageContextVariable`


Metadata Types BotVersion

**Field Name** **Description**

```
successMessages

type

variableOperationIdentifier

```

BotQuickReplyOption

**Field Type**

BotMessage[] on page 515

**Description**
In a File dialog step, the message displayed to the customer as part of type
`CollectAttachment` to confirm a successful file upload. Available in API version
57.0 and later.

**Field Type**
BotVariableOperationType (enumeration of type string)

**Description**

Required.

Values are:

**•** `Collect`

**•** `CollectAttachment` (Available in API version 57.0 and later.)

**•** `Set`

**•** `SetConversationLanguage` (Available in API version 53.0 and later.)

**•** `Unset`

**Field Type**
string

**Description**
A unique key that identifies a variable operation within a dialog. It is used to link
translated labels to labels within the variable operation. This field is recommended for
all variable operation records and is required for translated variable operation labels.
Available in API version 53.0 and later.

If a variable operation is created via the UI, the
`variableOperationIdentifier` is automatically generated. If a variable
operation is created via API, the `variableOperationIdentifier` must be
provided. `variableOperationIdentifier` can contain letters, numbers,
dashes, and underscores, up to 255 characters.

List of static choice options used by a bot variable operation of type `Collect` and `quickReplyType` of `Static` .

**Field Name** **Description**

```
literalValue

```

**Field Type**
string

**Description**

Required.


Metadata Types BotVersion

**Field Name** **Description**

Value to be displayed as a menu or button choice to your customer.

```
quickReplyOptionIdentifier

```

BotVariableOperand

**Field Type**
string

**Description**
A unique key that identifies a quick reply option within a dialog. It is used to link
translated labels to labels within the quick reply option. This field is recommended for
all quick reply option records and is required for translated quick reply option labels.
Available in API version 53.0 and later.

If a quick reply option is created via the UI, the `quickReplyOptionIdentifier`
is automatically generated. If a message is created via API, the
`quickReplyOptionIdentifier` must be provided.
`quickReplyOptionIdentifier` can contain letters, numbers, dashes, and
underscores, up to 255 characters.

List of bot variable operands associated with a bot variable of type `Set` or `Unset` .

**Field Name** **Description**

```
disableAutoFill

sourceName

sourceType

```

**Field Type**
boolean

**Description**
Disables auto-fill behavior for a bot variable under a bot variable operation of type
`Collect` .

**Field Type**
string

**Description**
Name of the source CustomField or MlSlotClass used in the variable operation.

**Field Type**
ConversationVariableOperandSourceType (enumeration of type string)

**Description**

Values are:

**•** `BotDefinition` (Available in API version 46.0 and later.)

**•** `ContextVariable` (Available in API version 45.0 and later.)

**•** `ConversationVariable`

**•** `FlowDefinition` (Available in API version 52.0 and later.)

**•** `MlSlotClass`

**•** `Queue` (Available in API version 46.0 and later.)


Metadata Types BotVersion

**Field Name** **Description**

**•** `StandardConversationVariable`

**•** `StandardMlSlotClass`

**•** `Value`

```
sourceValue

targetName

targetType

```

**Field Type**
string

**Description**
Literal value used as the source for this variable operation.

**Field Type**
string

**Description**

Required.

Name of the target variable used in the variable operation.

**Field Type**
ConversationVariableType (enumeration of type string)

**Description**

Required.

Type of the target used in the variable operation.

Values are:

**•** `ContextVariable`

**•** `ConversationVariable`

**•** `PageContextVariable`

ConversationRecordLookup

Information related to the linked conversation. Currently only works on Lightning Knowledge. Available in API version 46.0 and later.

**Field Name** **Description**

```
SObjectType

conditions

```

**Field Type**
string

**Description**

Required.

Specifies the SObjectType of the ID stored in a bot variable.

**Field Type**

ConversationRecordLookupCondition[] on page 525


Metadata Types BotVersion

**Field Name** **Description**

**Description**
The conditions associated with this lookup. Available in API version 51.0 and later.

```
filterLogic

lookupFields

maxLookupResults

sortFieldName

sortOrder

sourceVariableName

```

**Field Type**
string

**Description**
The logical operator that connects the conditions.

Values are:

**•** `And`

**•** `Or`

Available in API version 51.0 and later.

**Field Type**

ConversationRecordLookupField[] on page 526

**Description**
Definition of the fields that are used for this lookup.

**Field Type**
int

**Description**

Required.

The maximum number of records to return (1-3).

**Field Type**
string

**Description**
The name of the field used to sort the lookup results. Available in API version 51.0 and
later.

**Field Type**
SortOrder (enumeration of type string)

**Description**
The display order of the lookup results.

Values are:

**•** `Asc`

**•** `Desc`

Available in API version 51.0 and later.

**Field Type**
string


Metadata Types BotVersion

**Field Name** **Description**

**Description**
The input for this lookup operation.

```
sourceVariableType

targetVariableName

```

**Field Type**
ConversationVariableType (enumeration of type string)

**Description**
Type of the target used in the variable operation.

Values are:

**•** `ContextVariable`

**•** `ConversationVariable`

**•** `PageContextVariable`

**Field Type**
string

**Description**

Required.

The variable that holds the results of this lookup.

ConversationRecordLookupCondition

List of conditions associated with a ConversationRecordLookup. Available in API version 51.0 and later.

**Field Name** **Description**

```
leftOperand

operatorType

```

**Field Type**
string

**Description**

Required.

Field on which the condition operation takes place.

**Field Type**
string

**Description**

Required.

The operator applied to the leftOperand.

Values are:

**•** `Equals`

**•** `NotEquals`

**•** `IsSet`


Metadata Types BotVersion

**Field Name** **Description**

**•** `IsNotSet`

**•** `GreaterThan`

**•** `LessThan`

**•** `GreaterThanOrEqualTo`

**•** `LessThanOrEqualTo`

```
rightOperandName

rightOperandType

rightOperandValue

sortOrder

```

**Field Type**
string

**Description**
The name of the variable to compare against.

**Field Type**
ConversationVariableType (enumeration of type string)

**Description**
The type of the variable to compare against.

Values are:

**•** `ContextVariable`

**•** `ConversationVariable`

**•** `PageContextVariable`

**Field Type**
string

**Description**
The custom value to compare against. This value is ignored when using `IsSet` and
`IsNotSet` operators.

**Field Type**
int

**Description**

Required.

Order in which the conditions are applied.

ConversationRecordLookupField

The fields used in a conversation record lookup. Available in API version 46.0 and later.

**Field Name** **Description**

```
fieldName

```

**Field Type**
string


Metadata Types BotVersion

**Field Name** **Description**

**Description**

Required.

Defines the field names used in the Conversation Lookup function.

ConversationDefinitionStepGoalMapping

Represents the association between a goal and a BotStep. A goal can be associated with only one BotStep and one dialog at a time.
Available in API version 57.0 and later.

**Field Name** **Description**

```
goalName

```

**Field Type**
string

**Description**
The API name of the goal.

ConversationSystemMessage

System messages that represent an action for a Bot Step, such as transferring to an agent or ending a chat. Available in API version 46.0
and later.

**Field Name** **Description**

```
systemMessageMappings

type

```

**Field Type**

ConversationSystemMessageMapping on page 527

**Description**
Defines the type of system message to be sent.

**Field Type**
ConversationSystemMessageType (enumeration of type string)

**Description**

Required.

This field defines the values available for a system message.

Values are:

**•** `EndChat`

**•** `Transfer`

ConversationSystemMessageMapping

List of mappings that indicate additional information provided for the system message. Available in API version 46.0 and later.


Metadata Types BotVersion

**Field Name** **Description**

```
mappingType

parameterType

variableName

```

**Field Type**
ConversationMappingType (enumeration of type string)

**Description**

Required.

Defines the type of mapping used in the record.

Values are:

**•** `Input`

**•** `Output`

**Field Type**
ConversationSystemMessageParamType (enumeration of type string)

**Description**

Required.

Defines the type of parameter the value is mapped to.

Values are:

**•** `Transfer`

**Field Type**
string

**Description**

Required.

Name of the variable that contains the value passed to the system message.

ConversationDefinitionRichMessage

Represents the configuration details for referencing a messaging component, such as an enhanced link. Available in API version 54.0
and later.

**Field Name** **Description**

```
messageDefinitionMappings

```

**Field Type**

BotInvocationMapping[] on page 514

**Description**
List of mappings for referencing a messaging component. Includes any input
parameters and their values. Optionally, specifies the conversation variable for storing
any outputs.

Input parameter values can be either static values or references to conversation or
context variables.


Metadata Types BotVersion

**Field Name** **Description**

```
messageDefinitionName

```

**Field Type**
string

**Description**

Required.

The API name of the messaging component referenced by the bot.

ConversationDefinitionGoal

A goal included in the bot version. Available in API version 57.0 and later.

**Field Name** **Description**

```
developerName

label

```

**Field Type**
string

**Description**

Required.

A unique name that prevents conflicts with other goals associated with the same bot
version. This name can contain only underscores and alphanumeric characters. It must
begin with a letter, not include spaces, not end with an underscore, and not contain
two consecutive underscores.

**Field Type**
string

**Description**

Required.

A label that identifies the goal throughout the Salesforce user interface. This label can
contain only underscores and alphanumeric characters. It must begin with a letter,
not include spaces, not end with an underscore, and not contain two consecutive
underscores.

ConversationDefinitionPlanner

Represents the API name for the Agent planner service. Available in API version 60.0 and later.

**Field Name** **Description**

```
genAiPlannerName

```

**Field Type**
string


Metadata Types BotVersion

**Field Name** **Description**

**Description**
The name of an agent planner service that uses a large language model (LLM) and a
reasoning strategy to decompose a given task into smaller subtasks, identify the most
suitable actions for each subtask, and invoke them.

ConversationSystemDialog

A system function assigned to a dialog. Available in API version 48.0 and later.

**Field Name** **Description**

```
dialog

type

```

ConversationVariable

**Field Type**
string

**Description**
The dialog name triggered when this system event fires.

**Field Type**
ConversationSystemDialogType (enumeration of type string)

**Description**
The type of system event. Required. Valid values are:

**•** `Disambiguation` (Reserved for Future Use)

**•** `DisambiguationFailed` (Reserved for Future Use)

**•** `ErrorHandling`

**•** `KnowledgeAction` (Available in API version 60.0.)

**•** `KnowledgeFallback` (Available in API version 51.0.)

**•** `TransferFailed`

A container that stores a specific piece of data collected from the customer. You can use variables within dialog actions as both inputs
and outputs. Available in API version 44.0 and later.

**Field Name** **Description**

```
collectionType

dataType

```

**Field Type**
ConversationVariableCollectionType (enumeration of type string)

**Description**
This field defines whether a variable is designated as a List Variable. Valid value is List.

**Field Type**
ConversationVariableCollectionType (enumeration of type string)


Metadata Types BotVersion

**Field Name** **Description**

**Description**

Required.

Valid values are:

**•** `Boolean`

**•** `Currency`

**•** `Date`

**•** `DateTime`

**•** `Id` (available in API 45.0 and later.)

**•** `Object`

**•** `Number`

**•** `Text`

```
description

developerName

includeInPrompt

```

**Field Type**
string

**Description**

A description of this variable. This value may be used by the Agentforce planner service.
Available in API version 63.0 and later.

**Field Type**
string

**Description**

Required.

This name can contain only underscores and alphanumeric characters and must be unique
in your org. It must begin with a letter, not include spaces, not end with an underscore, and
not contain two consecutive underscores. Only users with View DeveloperName OR View
Setup and Configuration permission can view, group, sort, and filter this field.

**Field Type**
boolean

**Description**
Indicates whether the variable is injected into the prompt sent to the Agentforce model. If
`true`, the variable appears in the **Included Fields** section of the UI.

Note: The default variables `Id`, `EndUserId`, and `EndUserLanguage` always
appear in the **Included Fields** section of the UI, regardless of their value of

`includeInPrompt` . We recommend that you don't change the value of
`includeInPrompt` for these default variables, as changing the value can prevent
your agent from accessing important session data.

Available in API version 63.0 and later.


Metadata Types BotVersion

**Field Name** **Description**

```
label

SObjectType

visibility

```

**Field Type**
string

**Description**

Required.

Label that identifies a variable throughout the Salesforce user interface.

**Field Type**
string

**Description**
Specifies the SObjectType of the ID stored in a bot variable. Valid values are:

**•** `BotDefinition`

**•** `Queue`

**Field Type**
ConversationVariableVisibilityType (enumeration of type string)

**Description**

Required. Determines which components can set this variable. If the visibility is `internal`,
the variable can only be set by action outputs. If the visibility is `external`, the variable
can also be set by the API.

Valid values are:

**•** `internal`

**•** `external`

ConversationDefinitionNlpProvider

Defines the natural language service that is used for the language assigned to a bot version. Available in API version 49.0 and later.

**Field Name** **Description**

```
language

nlpProviderName

```

**Field Type**
Language

**Description**

Required.

The language assigned to a bot version.

**Field Type**
string

**Description**
If nlpProviderType is EinsteinAI, this field is blank. If Apex, this field holds the Apex class
name of the service.


Metadata Types BotVersion

**Field Name** **Description**

```
nlpProviderType

```

**Field Type**
ConversationDefinitionNlpProviderType (enumeration of type string)

**Description**

Required.

Default value is `EinsteinAi` . Valid values are:

**•** `EinsteinAi`

**•** `Apex`

Declarative Metadata Sample Definition

The following is an example of a BotVersion.

```
<?xml version="1.0" encoding="UTF-8"?>

<Bot xmlns="http://soap.sforce.com/2006/04/metadata">

   <botMlDomain>

     <label>Astros Pizza</label>

     <mlIntents>

        <developerName>New_Order</developerName>

        <label>New Order</label>

        <mlIntentUtterances>

          <utterance>Today is pie day so I want pie</utterance>

        </mlIntentUtterances>

     </mlIntents>

     <mlSlotClasses>

        <developerName>Size</developerName>

        <extractionType>Value</extractionType>

        <label>Size</label>

        <mlSlotClassValues>

          <synonymGroup>

            <languages>en_US</languages>

            <terms>Big</terms>

            <terms>Extra Large</terms>

            <terms>X-Large</terms>

            <terms>Grande</terms>

            <terms>Huge</terms>

          </synonymGroup>

          <value>Large</value>

        </mlSlotClassValues>

     </mlSlotClasses>

     <name>Astros_Pizza_ld1</name>

   </botMlDomain>

   <botVersions>

     <fullName>v1</fullName>

     <botDialogGroups>

        <developerName>Order_Management</developerName>

        <label>Order Management</label>

     </botDialogGroups>

     <botDialogs>

```


Metadata Types BotVersion

```
           <botDialogGroup>Order_Management</botDialogGroup>

           <botSteps>

             <botMessages>

               <message> ������Pizza Time! ������ </message>

               <messageIdentifier>Greeting_Message</messageIdentifier>

             </botMessages>

             <stepIdentifier>Greeting</stepIdentifier>

             <type>Message</type>

           </botSteps>

           <botSteps>

             <botStepConditions>

               <leftOperandName>Verified_User</leftOperandName>

               <leftOperandType>ConversationVariable</leftOperandType>

               <operatorType>Equals</operatorType>

               <rightOperandValue>false</rightOperandValue>

             </botStepConditions>

             <botSteps>

               <botNavigation>

                  <botNavigationLinks>

                    <targetBotDialog>Customer_Verification</targetBotDialog>

                  </botNavigationLinks>

                  <type>Call</type>

               </botNavigation>

               <stepIdentifier>Call_Customer_Verification</stepIdentifier>

               <type>Navigation</type>

             </botSteps>

             <stepIdentifier>Verify_User</stepIdentifier>

             <type>Group</type>

           </botSteps>

           <botSteps>

             <botStepConditions>

               <leftOperandName>Location</leftOperandName>

               <leftOperandType>ConversationVariable</leftOperandType>

               <operatorType>IsNotSet</operatorType>

             </botStepConditions>

             <botSteps>

               <botNavigation>

                  <botNavigationLinks>

                    <targetBotDialog>Select_Location</targetBotDialog>

                  </botNavigationLinks>

                  <type>Call</type>

               </botNavigation>

               <stepIdentifier>Call_Select_Location</stepIdentifier>

               <type>Navigation</type>

             </botSteps>

             <stepIdentifier>Set_Location</stepIdentifier>

             <type>Group</type>

           </botSteps>

           <botSteps>

             <botVariableOperation>

               <botInvocation>

                  <invocationActionName>CreateOrderService</invocationActionName>

                  <invocationActionType>apex</invocationActionType>

                  <invocationMappings>

```


Metadata Types BotVersion

```
                    <parameterName>customer</parameterName>

                    <type>Input</type>

                    <variableName>Contact</variableName>

                    <variableType>ConversationVariable</variableType>

                  </invocationMappings>

                  <invocationMappings>

                    <parameterName>location</parameterName>

                    <type>Input</type>

                    <variableName>Location</variableName>

                    <variableType>ConversationVariable</variableType>

                  </invocationMappings>

                  <invocationMappings>

                    <parameterName>output</parameterName>

                    <type>Output</type>

                    <variableName>Pizza_Order</variableName>

                    <variableType>ConversationVariable</variableType>

                  </invocationMappings>

               </botInvocation>

               <type>Set</type>

               <variableOperationIdentifier>Set_Order</variableOperationIdentifier>

             </botVariableOperation>

             <stepIdentifier>Create_Order</stepIdentifier>

             <type>VariableOperation</type>

           </botSteps>

           <botSteps>

             <botMessages>

              <message>Perfect, let&apos;s work on your order from our {!Location.Name}

    location</message>

               <messageIdentifier>Start_Order_Message</messageIdentifier>

             </botMessages>

             <stepIdentifier>Start_Order</stepIdentifier>

             <type>Message</type>

           </botSteps>

           <botSteps>

             <messageDefinition>

               <messageDefinitionName>Astros_Pizza_Menu</messageDefinitionName>

             </messageDefinition>

             <stepIdentifier>36e5a7cb-50c4-4279-aa06-1217eba1bf62</stepIdentifier>

             <type>RichMessage</type>

           </botSteps>

           <botSteps>

             <botNavigation>

               <botNavigationLinks>

                  <targetBotDialog>Add_Items_to_Order</targetBotDialog>

               </botNavigationLinks>

               <type>Redirect</type>

             </botNavigation>

             <stepIdentifier>Proceed_To_Add_Items</stepIdentifier>

             <type>Navigation</type>

           </botSteps>

           <developerName>New_Order</developerName>

           <label>New Order</label>

           <mlIntent>New_Order</mlIntent>

           <showInFooterMenu>false</showInFooterMenu>

```


### Metadata Types BrandingSet

```
        </botDialogs>

        <conversationVariables>

           <dataType>Object</dataType>

           <developerName>Contact</developerName>

           <label>Contact</label>

        </conversationVariables>

        <conversationVariables>

           <dataType>Text</dataType>

           <developerName>Delivery_Address</developerName>

           <label>Delivery Address</label>

        </conversationVariables>

        <conversationVariables>

           <dataType>Object</dataType>

           <developerName>Pizza_Order</developerName>

           <label>Pizza Order</label>

        </conversationVariables>

        <entryDialog>Welcome</entryDialog>

        <mainMenuDialog>Main_Menu</mainMenuDialog>

      </botVersions>

      <label>Astro&apos;s Pizza</label>

   </Bot>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>Astros Pizza_Bot.v1</members>

        <name>BotVersion</name>

      </types>

      <version>45.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

### BrandingSet

Represents the definition of a set of branding properties for an Experience Builder site or for your org's Lightning Experience theme.

This type extends the Metadata metadata type and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### BrandingSet components have the suffix brandingSet and are stored in the brandingSets folder.


Metadata Types BrandingSet

Version

BrandingSet components are available in API version 40.0 and later.

Special Access Rules

The BrandingSet type is available when at least one of the following is enabled in your org: Digital Experiences, Surveys, or Lightning
Experience. All users, including unauthenticated guest users, can access this type.

Fields

**Field Name** **Field Type** **Description**

`brandingSetProperty` BrandingSetProperty[] An array containing the name and value of each branding property, such
as `TextColor:#333` .

`description` string A description of the set of branding properties.

`masterLabel` string Required. The user interface name of the set of branding properties.

`type` string The assigned branding set definition for this BrandingSet.

BrandingSetProperty

Represents the definition of a branding property in the Theme panel in Experience Builder or in the Edit Theme page in Setup.

**Field Name** **Field Type** **Description**

`propertyName` string Required. The name of the branding property, such as `TextColor` .

`propertyValue` string The value of the branding property, such as `#333` .

Branding Properties for Lightning Experience Themes

Use these properties to describe Lightning Experience themes. Each propertyName is case-sensitive and must use all capital letters.
Some properties only apply to either Salesforce Lightning Design System (SLDS) 1 themes or SLDS 2 themes.

**Property** **Description**

```
ACCENT_COLOR_1

```

**Field Type**
string

**Description**
The primary accent color used to highlight active states of the
user interface like navigation, tabs, and hover states. Must be
a valid hex color string in the format #54C254.

Available only for SLDS 2 themes. Available in API version 64.0
and later.


Metadata Types BrandingSet

**Property** **Description**

```
ACCENT_COLOR_2

ACCENT_COLOR_3

ACCENT_CONTAINER_CONTENT_COLOR_1

ACCENT_CONTAINER_CONTENT_COLOR_2

ACCENT_CONTAINER_CONTENT_COLOR_3

```

**Field Type**
string

**Description**
A variant of the primary accent color used to highlight active
states of the user interface like navigation, tabs, and hover
states. Must be a valid hex color string in the format #54C254.

Available only for SLDS 2 themes. Available in API version 64.0
and later.

**Field Type**
string

**Description**
A variant of the primary accent color used to highlight active
states of the user interface, like navigation, tabs, and hover
states. Must be a valid hex color string in the format #54C254.

Available only for SLDS 2 themes. Available in API version 64.0
and later.

**Field Type**
string

**Description**
The primary color used for the icons and text within accent
containers. Must be a valid hex color string in the format
#54C254.

Available only for SLDS 2 themes. Available in API version 65.0
and later.

**Field Type**
string

**Description**
A variant of the primary color used for the icons and text within
accent containers. Must be a valid hex color string in the format
#54C254.

Available only for SLDS 2 themes. Available in API version 65.0
and later.

**Field Type**
string

**Description**
A variant of the primary color used for the icons and text within
accent containers. Must be a valid hex color string in the format
#54C254.


Metadata Types BrandingSet

**Property** **Description**

Available only for SLDS 2 themes. Available in API version 65.0
and later.

```
BANNER_IMAGE

BRAND_COLOR

BRAND_IMAGE

CONTAINER_ACCENT_COLOR_1

CONTAINER_ACCENT_COLOR_2

```

**Field Type**
string

**Description**
The path to the image to display in the background of your
org's pages. Use a JPG, PNG, or GIF that's 1800x360 pixels and
[smaller than 5 MB. Must refer to an asset file that already exists](https://help.salesforce.com/s/articleView?id=experience.admin_files_asset_files.htm&type=5&language=en_US)
within the org.

Available only for SLDS 1 themes.

**Field Type**
string

**Description**
The color to display on your nav bar and other important areas
of Salesforce. Must be a valid hex color string in the format
#54C254.

**Field Type**
string

**Description**
The path to the image to display as your logo. Use a JPG, PNG,
or GIF that’s 600x120 pixels and smaller than 5 MB. Must refer
[to an asset file that already exists within the org.](https://help.salesforce.com/s/articleView?id=experience.admin_files_asset_files.htm&type=5&language=en_US)

**Field Type**
string

**Description**
The primary color used for the background of branded
component containers like the brand button. Container accent
colors are also used for hover states for branded component
containers. Must be a valid hex color string in the format
#54C254.

Available only for SLDS 2 themes. Available in API version 64.0
and later.

**Field Type**
string

**Description**
A variant of the primary color used for the background of
branded component containers. Container accent colors are
also used for hover states for branded component containers.
Must be a valid hex color string in the format #54C254.


Metadata Types BrandingSet

**Property** **Description**

Available only for SLDS 2 themes. Available in API version 64.0
and later.

```
CONTAINER_ACCENT_COLOR_3

GROUP_IMAGE

GROUPS_BANNER_IMAGE

HEADER_BACKGROUND_COLOR

LINK_AS_BACKGROUND

```

**Field Type**
string

**Description**
A variant of the primary color used for the background of
branded component containers. Container accent colors are
also used for hover states for branded component containers.
Must be a valid hex color string in the format #54C254.

Available only for SLDS 2 themes. Available in API version 64.0
and later.

**Field Type**
string

**Description**
The default group avatar image. Use a JPG, PNG, or GIF that's
200x200 pixels and smaller than 5 MB. Group owners can
[change their avatar image. Must refer to an asset file that](https://help.salesforce.com/s/articleView?id=experience.admin_files_asset_files.htm&type=5&language=en_US)
already exists within the org.

**Field Type**
string

**Description**
The default banner image for group pages. Use a JPG, PNG, or
GIF that’s 1800x360 pixels and smaller than 5 MB. Group owners
[can change their banner image. Must refer to an asset file that](https://help.salesforce.com/s/articleView?id=experience.admin_files_asset_files.htm&type=5&language=en_US)
already exists within the org.

**Field Type**
string

**Description**
The color to display at the top of your org pages. Your logo,
global search, and global actions appear on top of the global
header background. Must be a valid hex color string in the
format #54C254.

Available only for SLDS 1 themes.

**Field Type**
boolean

**Description**
Indicates whether you want links in your org to use your
selected brand color ( `true` ) or not ( `false` ). The default value
is `true` .


Metadata Types BrandingSet

**Property** **Description**

Available only for SLDS 1 themes.

```
OVERRIDE_A11Y_COLOR

OVERRIDE_LOADING_PAGE

PAGE_BACKGROUND_COLOR

PROFILE_BANNER_IMAGE

USER_IMAGE

```

**Field Type**
string

**Description**
When you select a value for `BRAND_COLOR`, a color palette
that complements your brand color and is WCAG 2.0 compliant
is automatically generated. In places where your selected brand
color isn’t accessible, an accessible color is used instead. If you
provide a value for `OVERRIDE_A11Y_COLOR`, your value
is used in the instances described in place of an automatically
generated color.

Overriding the accessible brand color only updates the first tile
in your brand-based color palette, which affects colors like links
and buttons. Overriding the accessibility brand color can make
text harder to read.

Must be a valid hex color string in the format #54C254.

Available only for SLDS 1 themes.

**Field Type**
boolean

**Description**
Indicates whether your provided brand logo displays while a
Lighting Experience page loads or refreshes ( `true` ) or not
( `false` ). The default value is `false` .

**Field Type**
string

**Description**
The color used for page backgrounds. Must be a valid hex color
string in the format #54C254.

Available only for SLDS 1 themes.

**Field Type**
string

**Description**
The default banner image for user profiles. Use a JPG, PNG, or
GIF that's 1800x360 pixels and smaller than 5 MB. Users can
[change their profile banner image. Must refer to an asset file](https://help.salesforce.com/s/articleView?id=experience.admin_files_asset_files.htm&type=5&language=en_US)
that already exists within the org.

**Field Type**
string


Metadata Types BrandingSet

**Property** **Description**

**Description**
The default avatar image for user profiles. Use a JPG, PNG, or
GIF that's 200x200 pixels and smaller than 5 MB. Users can
[change their profile avatar image. Must refer to an asset file](https://help.salesforce.com/s/articleView?id=experience.admin_files_asset_files.htm&type=5&language=en_US)
that already exists within the org.

Declarative Metadata Sample Definition

The following is an example of a BrandingSet component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <BrandingSet xmlns="http://soap.sforce.com/2006/04/metadata">

      <brandingSetProperty>

        <propertyName>TextTransformStyle</propertyName>

        <propertyValue>uppercase</propertyValue>

      </brandingSetProperty>

      <brandingSetProperty>

        <propertyName>DetailTextColor</propertyName>

        <propertyValue>#696969</propertyValue>

      </brandingSetProperty>

      <brandingSetProperty>

        <propertyName>BorderColor</propertyName>

        <propertyValue>#D4D4D4</propertyValue>

      </brandingSetProperty>

      <brandingSetProperty>

        <propertyName>HeaderImage</propertyName>

        <propertyValue></propertyValue>

      </brandingSetProperty>

      <brandingSetProperty>

        <propertyName>HeaderFonts</propertyName>

        <propertyValue>Montserrat</propertyValue>

      </brandingSetProperty>

      <brandingSetProperty>

        <propertyName>CardBackgroundColor</propertyName>

        <propertyValue>rgba(255, 255, 255, 0)</propertyValue>

      </brandingSetProperty>

      <brandingSetProperty>

        <propertyName>LoginBackgroundColor</propertyName>

        <propertyValue>#F4F4F4</propertyValue>

      </brandingSetProperty>

      <brandingSetProperty>

        <propertyName>ActionColor</propertyName>

        <propertyValue>#2574A9</propertyValue>

      </brandingSetProperty>

      <brandingSetProperty>

        <propertyName>_ActionColorTrans</propertyName>

        <propertyValue>rgba(25, 124, 190, 0.9)</propertyValue>

      </brandingSetProperty>

      <brandingSetProperty>

        <propertyName>CompanyLogo</propertyName>

```


Metadata Types BrandingSet

```
        <propertyValue></propertyValue>

      </brandingSetProperty>

      <brandingSetProperty>

        <propertyName>LoginBackgroundImage</propertyName>

        <propertyValue>../../../../sfsites/picasso/core/external/

           salesforceIdentity/images/background.jpg?v=1</propertyValue>

      </brandingSetProperty>

      <brandingSetProperty>

        <propertyName>_LinkColorDarker</propertyName>

        <propertyValue>#135F90</propertyValue>

      </brandingSetProperty>

      <brandingSetProperty>

        <propertyName>_ActionColorDarker</propertyName>

        <propertyValue>#135F90</propertyValue>

      </brandingSetProperty>

      <brandingSetProperty>

        <propertyName>_HoverColor</propertyName>

        <propertyValue>rgba(25, 124, 190, 0.1)</propertyValue>

      </brandingSetProperty>

      <brandingSetProperty>

        <propertyName>ErrorFontColor</propertyName>

        <propertyValue>#ff9e9e</propertyValue>

      </brandingSetProperty>

      <brandingSetProperty>

        <propertyName>TextColor</propertyName>

        <propertyValue>#333</propertyValue>

      </brandingSetProperty>

      <brandingSetProperty>

        <propertyName>OverlayTextColor</propertyName>

        <propertyValue>#FFFFFF</propertyValue>

      </brandingSetProperty>

      <brandingSetProperty>

        <propertyName>PrimaryFont</propertyName>

        <propertyValue>Lato</propertyValue>

      </brandingSetProperty>

      <brandingSetProperty>

        <propertyName>LinkColor</propertyName>

        <propertyValue>#2574A9</propertyValue>

      </brandingSetProperty>

      <masterLabel>ex</masterLabel>

      <type>napili:branding-napili-merged</type>

   </BrandingSet>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>MyBrandingSet</members>

        <name>BrandingSet</name>

      </types>

      <version>40.0</version>

   </Package>

```


### Metadata Types BriefcaseDefinition

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### BriefcaseDefinition

Represents a briefcase definition. A briefcase makes selected records available for specific users and groups to view when they’re offline
in the Salesforce Field Service mobile app for iOS and Android. This type extends the Metadata metadata type and inherits its `fullName`
field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### BriefcaseDefinition components have the suffix .briefcaseDefinition and are stored in the briefcaseDefinitions

folder.

Version

### BriefcaseDefinition components are available in API version 50.0 and later.

Fields

**Field Name** **Field Type** **Description**

`briefcaseRules` BriefcaseRule[] A list of rules that specify which records are included in the briefcase.

`description` string Description of the briefcase.

`isActive` boolean

Required. Indicates whether the briefcase is active by default ( `true` ) or
inactive ( `false` ). Activate a briefcase to make the selected records
available to assignees.

`masterLabel` string Required. Label for the briefcase name that appears in the Salesforce
user interface.

`type` BriefcaseType Applies if multiple briefcase types are available in your org. Enum values
include:

**•** `Standard` : Standard briefcase that can be used with priming APIs.

**•** `HighVolume` : Increased capacity briefcase that’s used with
performance priming in the Salesforce Field Service mobile app.

**•** `MobileAppSync` : Automatically generated briefcase that’s used
for performance priming in the Salesforce Field Service mobile app.


Metadata Types BriefcaseDefinition

BriefcaseRule

Represents a rule that specifies records to be included in the BriefcaseDefinition.

**Field Name** **Field Type** **Description**

`briefcaseRuleFilters` BriefcaseRuleFilter[] A list of filters on a rule.

`filterLogic` string The filter logic for record selection, for example, `1 AND 2` where 1 and 2
correspond to filter 1 and filter 2. Filter logic operators include `AND` and `OR` .

`isAscendingOrder` boolean Indicates whether the records should be sorted in ascending order ( `true` ) or
descending order ( `false` ).

`isRelatedFilesRule` boolean

Indicates whether the briefcase rule is part of a hierarchical set of rules that
configure the offline priming of file attachments. Available only for the Offline
App (Salesforce Mobile App Plus).

To configure the offline priming of file attachments, create a set of four
hierarchical briefcase rules:

**•** A rule with `targetEntity` set to the object with the file attachments
at the first level

**•** A rule with `targetEntity` set to `ContentDocumentLink` at the
second level

**•** A rule with `targetEntity` set to `ContentDocument` at the third
level

**•** A rule with `targetEntity` set to `ContentVersion` at the fourth
level

See the Declarative Metadata Sample Definition section for an example briefcase
definition that configures the offline priming of file attachments.

The `ContentDocumentLink`, `ContentDocument`, and
`ContentVersion` rules must all have `isRelatedFilesRule` set to
`true` . To delete a briefcase configuration for file attachments, you must delete
the `ContentDocumentLink` rule and all of its nested rules. You can’t
delete a single rule within the hierarchy of `ContentDocumentLink`,
`ContentDocument`, and `ContentVersion` rules.

When `isRelatedFilesRule` is set to true, you must use the
`recordLimit` field to limit the number of file attachments returned by a
briefcase rule. Apply the same `recordLimit` value across the
`ContentDocumentLink`, `ContentDocument`, and
`ContentVersion` rules. You can optionally filter file attachments by file
size and file type through Briefcase Builder in Setup.

After you set a value for `isRelatedFilesRule`, you can no longer modify
the field. The value that you set persists for the life of the rule.

`orderBy` string The field to order the records by, which determines how the records can be
sorted. For example, Account Name or Created By.


Metadata Types BriefcaseDefinition

**Field Name** **Field Type** **Description**

```
queryScope

```

`FilterScope` A group of records to restrict the scope of this rule. Valid values include:
(enumeration of type

**•** `Everything`

string)

**•** `Everything`

**•** `AssignedToMe`

**•** `Mine`

The `AssignedToMe` scope is supported for the ServiceAppointment object
only.

`recordLimit` int The maximum number of records for an object on the briefcase rule. The
maximum is 50,000 records that meet the criteria. However, the records returned

by one briefcase rule must fit within the maximum limit of 50,000 records
across active briefcases. If there are more records that match the criteria than
the record limit allows, the `orderBy` field determines which records are
returned.

`relatedRules` BriefcaseRule[] A list of rules that are related to the current rule.

`relationshipField` string Required for `relatedRules` . Defines the Salesforce object field that relates
the `relatedRules` field to another `relatedRules` field or the

`briefcaseRules` field on the BriefcaseDefinition metadata type that it's
nested in. For example, an Account object rule can be related to a Contact
object rule using the Account ID object field. In this example, the value for the
related rule's `relationshipField` is `AccountID` .

```
relationshipType

```

`BriefcaseRuleRelationshipType` Required for `relatedRules` . Defines the relationship between the
(enumeration of type `relatedRules` field and another `relatedRules` field or the
string) `briefcaseRules` field on the BriefcaseDefinition metadata type that it's

nested in. Valid values include:

**•** `ParentToChild`

**•** `ChildToParent`

`targetEntity` string

BriefcaseRuleFilter

Specifies filter criteria for a BriefcaseRule.

Required. The API name of the standard object, custom object, or custom
metadata type that the briefcase rule selects records from.

If the `targetEntity` is a custom metadata type, the briefcase rule can’t
include any other fields. You can add only one briefcase rule for the same

custom metadata type in a briefcase. Custom metadata types are supported
as the `targetEntity` for top-level rules only–you can’t create a related
rule with `targetEntity` as a custom metadata type.


Metadata Types BriefcaseDefinition

**Field Name** **Field Type** **Description**

```
filterOperator

```

```
BriefcaseFilterOperator
```

(enumeration of type
string)

Required. The comparison operator for this rule filter. Capitalization matters
with date filter operators. Be sure to specify date literals in uppercase. Some
valid date literals include TODAY, YESTERDAY and TOMORROW.

Valid values include:

**•** `d` —Ends with

**•** `e` —Equals

**•** `g` —Greater than

**•** `h` —Greater than or equal

**•** `l` —Less than

**•** `m` —Less than or equal

**•** `n` —Not equals. This value is applicable only when `filterValue` is
empty.

**•** `s` —Starts with

`filterSeqNumber` int Required. The filter number. When you apply multiple filters, the filters are
numbered sequentially, 1, 2, 3, and so on.

`filterValue` string

The value that the field and criteria evaluate. For example, `true` or `false`
for a boolean field whose criteria or filter operator is Equals.

Be sure to specify date literals in uppercase. Some valid date literals include
TODAY, YESTERDAY and TOMORROW.

For `targetEntityField` values that accept a user ID, such as `OwnerId`
or `CreatedById`, enter `$User.Id` to pass the ID of the user making the
request.

To evaluate `targetEntityField` by whether the field is empty or not
empty, leave `filterValue` blank and set `filterOperator` to `e`
(equals) or `n` (not equals).

`targetEntityField` string Required. The API name of the field to filter by. This field is from the
`targetEntity` on BriefcaseRule. Compound fields aren't supported. Fields

encrypted with deterministic encryption can be used in filters with equals and
not equals operators.

Declarative Metadata Sample Definition

The following is an example of a BriefcaseDefinition component for account records.

The following is an example definition of a briefcase definition. If you include a rule filter, you must include a filter logic.

```
<?xml version="1.0" encoding="UTF-8"?>

<BriefcaseDefinition xmlns="http://soap.sforce.com/2006/04/metadata">

   <briefcaseRules>

     <briefcaseRuleFilters>

       <filterOperator>g</filterOperator>

       <filterSeqNumber>1</filterSeqNumber>

```


Metadata Types BriefcaseDefinition

```
          <filterValue>50000.00</filterValue>

          <targetEntityField>AnnualRevenue</targetEntityField>

        </briefcaseRuleFilters>

        <briefcaseRuleFilters>

           <filterOperator>l</filterOperator>

           <filterSeqNumber>2</filterSeqNumber>

           <filterValue>50</filterValue>

           <targetEntityField>NumberOfEmployees</targetEntityField>

        </briefcaseRuleFilters>

        <filterLogic>1 AND 2</filterLogic>

        <isAscendingOrder>false</isAscendingOrder>

        <orderBy>NumberOfEmployees</orderBy>

        <queryScope>Everything</queryScope>

        <recordLimit>1000</recordLimit>

        <targetEntity>Account</targetEntity>

      </briefcaseRules>

      <description>Account Briefcase</description>

      <isActive>true</isActive>

      <masterLabel>Account With Standard Fields</masterLabel>

   </BriefcaseDefinition>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>AccountWithCustomFields</members>

        <name>BriefcaseDefinition</name>

      </types>

      <version>49.0</version>

   </Package>

```

This example briefcase definition configures the offline priming of file attachments for the WorkOrder object. Files Priming is available
only for the Offline App (Salesforce Mobile App Plus).

```
   <?xml version="1.0" encoding="UTF-8"?>

   <BriefcaseDefinition xmlns="http://soap.sforce.com/2006/04/metadata"

   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

     <briefcaseRules>

        <isAscendingOrder>false</isAscendingOrder>

        <orderBy>SystemModstamp</orderBy>

        <queryScope>Everything</queryScope>

        <recordLimit>25</recordLimit>

        <targetEntity>WorkOrder</targetEntity>

        <relatedRules>

          <targetEntity>ContentDocumentLink</targetEntity>

          <relationshipField>LinkedEntityId</relationshipField>

          <relationshipType>ParentToChild</relationshipType>

          <isAscendingOrder>false</isAscendingOrder>

          <isRelatedFilesRule>true</isRelatedFilesRule>

          <queryScope>Everything</queryScope>

          <recordLimit>2</recordLimit>

          <relatedRules>

            <targetEntity>ContentDocument</targetEntity>

            <relationshipField>ContentDocumentId</relationshipField>

```


### Metadata Types BusinessProcessGroup

```
            <relationshipType>ChildToParent</relationshipType>

            <isAscendingOrder>false</isAscendingOrder>

            <isRelatedFilesRule>true</isRelatedFilesRule>

            <queryScope>Everything</queryScope>

            <recordLimit>2</recordLimit>

            <relatedRules>

               <targetEntity>ContentVersion</targetEntity>

               <relationshipField>ContentDocumentId</relationshipField>

               <relationshipType>ParentToChild</relationshipType>

               <isAscendingOrder>false</isAscendingOrder>

               <isRelatedFilesRule>true</isRelatedFilesRule>

               <queryScope>Everything</queryScope>

               <recordLimit>2</recordLimit>

            </relatedRules>

          </relatedRules>

        </relatedRules>

     </briefcaseRules>

     <description xsi:nil="true"/>

     <isActive>true</isActive>

     <masterLabel>WorkOrder with Related Files</masterLabel>

   </BriefcaseDefinition>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

Usage

Briefcase objects are available in orgs that have Briefcase Builder and Field Service enabled.

### BusinessProcessGroup

Represents the surveys used to track customers’ experiences across different stages in their lifecycle. This type extends the Metadata
metadata type and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### BusinessProcessGroup components have the suffix .businessProcessGroup and are stored in the businessProcessGroups

folder.

Version

### BusinessProcessGroup components are available in API version 49.0 and later.


Metadata Types BusinessProcessGroup

Special Access Rules

This metadata type is available in orgs with Surveys enabled with the Customer Lifecycle Designer license.

Fields

**Field Name** **Field Type** **Description**

`businessProcessDefinitions` BusinessProcessDefinition A list that defines stages in a customer lifecycle map.
on page 551[]

`customerSatisfactionMetric` SurveyQuestionType(enumeration
of type string)

Required. Types of questions that can be associated with stages in a
customer lifecycle map.

Valid values are:

**•** `Attachment`

**•** `Boolean`

**•** `CSAT`

**•** `Currency`

**•** `Date`

**•** `DateTime`

**•** `FreeText`

**•** `Image`

**•** `NPS`

**•** `Matrix`

**•** `MultiChoice`

**•** `MultiSelectPicklist`

**•** `NPS`

**•** `Number`

**•** `Picklist`

**•** `Rating`

**•** `ShortText`

**•** `Slider`

**•** `StackRank`

**•** `Toggle`

`description` string A description of the customer lifecycle map.

`masterLabel` string Required. The name of the customer lifecycle map.


Metadata Types BusinessProcessGroup

BusinessProcessDefinition

**Field Name** **Field Type** **Description**

`businessProcessFeedbacks` BusinessProcessFeedback A list of stages in a customer lifecycle map.
on page 551[]

`description` string A description of a stage in the customer lifecycle map.

`developerName` string

Required. The API name of a stage in the customer lifecycle map.

Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

`masterLabel` string Required. The name of a stage in the customer lifecycle map.

`sequenceNumber` int Required. The position of a stage in the customer lifecycle map.

BusinessProcessFeedback

**Field Name** **Field Type** **Description**

`actionName` string Required. The name of the survey used to collect feedback

`actionParam` string Required. The name of the survey question used to collect feedback.

`actionType` ExpFeedbackCo **l** Type(enumeration Required. The mode of feedback collection. Valid values are:
of type string)

**•** `PHONE_CALL`

**•** `SURVEY`

Declarative Metadata Sample Definition

The following is an example of a BusinessProcessGroup component.

```
<?xml version="1.0" encoding="UTF-8"?>

<BusinessProcessGroup xmlns="http://soap.sforce.com/2006/04/metadata">

   <businessProcessDefinitions>

     <developerName>Customer_Onboarding</developerName>

     <masterLabel>Customer Onboarding</masterLabel>

     <description>A stage in a customer's lifecycle.</description>

     <sequenceNumber>0</sequenceNumber>

     <businessProcessFeedbacks>

        <actionType>Survey</actionType>

        <actionName>New Customer CSAT</actionName>

        <actionParam>How would you rate our service?</actionParam>

     </businessProcessFeedbacks>

   </businessProcessDefinitions>

   <customerSatisfactionMetric>NPS</customerSatisfactionMetric>

   <masterLabel>Customer Lifecycle</masterLabel>

   <description>This map tracks the feedback provided by customers' at different stages

```


### Metadata Types CallCenter

```
   during their lifecycle.</description>

   </BusinessProcessGroup>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>policyholder</members>

        <name>BusinessProcessGroup</name>

      </types>

      <version>49.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### CallCenter

Represents the Call Center definition used to integrate Salesforce with a third-party computer-telephony integration (CTI) system, a
partner telephony system, or partner Contact Center as a Service (CCaaS) system.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### CallCenter components have the suffix .callCenter and are stored in the callCenters folder.

Version

### CallCenter components are available in API version 27.0 and later.

Special Access Rules

There are no additional access requirements that are specific to this type.

Fields

**Field Name** **Description**

```
adapterUrl

```

**Field Type**
string


Metadata Types CallCenter

**Field Name** **Description**

**Description**
Optional field. A URL that points to an adapter.

```
contactCenterChannels

displayName

displayNameLabel

internalNameLabel

sections

version

```

**Field Type**

ContactCenterChannel[]

**Description**
Relates Bring Your Own Channel for Contact Center as a Service (CCaaS) messaging
channels to a CallCenter and represents the routing details for a voicemail configuration.

**Field Type**
string

**Description**

Required.

The display name of this call center.

**Field Type**
string

**Description**

Required.

The label of the `displayName` field in Call Center setup page.

**Field Type**
string

**Description**

Required.

The label of the `internalName` field in Call Center setup page.

**Field Type**

CallCenterSection[]

**Description**
Custom setup items defined for this call center.

**Field Type**
string

**Description**
The version of this call center.


Metadata Types CallCenter

CallCenterSection

**Field Name** **Description**

```
items

label

name

```

CallCenterItem

**Field Type**

CallCenterItem[]

**Description**
Contains the label, name, and value that describe the sections.

**Field Type**
string

**Description**

Required.

The label of the section.

**Field Type**
string

**Description**

Required.

The name of the section.

**Field Name** **Description**

```
label

name

value

```

**Field Type**
string

**Description**

Required.

The label of the custom setup item.

**Field Type**
string

**Description**

Required.

The name of the custom setup item.

**Field Type**
string

**Description**

Required.


Metadata Types CallCenter

**Field Name** **Description**

The value of the custom setup item.

ContactCenterChannel

Represents a junction subtype that relates a Bring Your Own Channel for Contact Center as a Service (CCaaS) messaging channel to a
CallCenter type for Bring Your Own Channel for CCaaS. This subtype also represents the routing details for a voicemail configuration and
routing information for callback requests. This subtype is available in API version 56.0 and later.

**Field Name** **Description**

```
channel

contactCenter

omniCallbackFallbackQueue

omniCallbackHandler

```

**Field Type**
string

**Description**

Required.

For Bring Your Own Channel for CCaaS, this field represents the unique ID of the Bring
Your Own Channel messaging channel (MessagingChannel) that’s associated with the
contact center (CallCenterId). Available in API version 60.0 and later.

**Field Type**
string

**Description**

Required.

For Bring Your Own Channel for CCaaS, this field represents the unique ID of the contact
center (CallCenterId) that’s associated with the Bring Your Own Channel messaging
channel (MessagingChannel). Available in API version 60.0 and later.

**Field Type**
string

**Description**
If callbacks are configured for the contact center and the contact center uses
Omni-Channel Unified Routing, this field represents the unique ID of the fallback queue
to use if contact request routing through an Omni-Channel flow fails. Don't change
the value in this field. Instead, configure contact request routing in Lightning Experience.
Available in API version 65.0 and later.

**Field Type**
string

**Description**
If callbacks are configured for the contact center and the contact center uses
Omni-Channel Unified Routing, this field represents the unique ID of the flow or queue
used to route contact requests. Don't change the value in this field. Instead, configure
contact request routing in Lightning Experience. Available in API version 65.0 and later.


Metadata Types CallCenter

**Field Name** **Description**

```
voiceMailFallbackQueue

voiceMailHandler

```

**Field Type**
string

**Description**
If voicemail routing is configured for the contact center, this field represents the unique
ID of the fallback queue to use if voicemail routing fails. Don't change the value in this
field. Instead, configure voicemail routing in Lightning Experience.

**Field Type**
string

**Description**
If voicemail routing is configured for the contact center, this field represents the unique
ID of the flow used to route voicemails. Don't change the value in this field. Instead,
configure voicemail routing in Lightning Experience.

Declarative Metadata Sample Definition

The following is an example of a CallCenter component:

```
<?xml version="1.0" encoding="UTF-8"?>

<CallCenter xmlns="http://soap.sforce.com/2006/04/metadata">

   <adapterUrl>http://localhost:11000</adapterUrl>

   <displayName>Demo Call Center Adapter</displayName>

   <displayNameLabel>Display Name</displayNameLabel>

   <internalNameLabel>Internal Name</internalNameLabel>

   <sections>

     <items>

        <label>Description</label>

        <name>reqDescription</name>

        <value>Demo Call Center Adapter</value>

     </items>

     <items>

        <label>CTI Connector ProgId</label>

        <name>reqProgId</name>

        <value>DemoAdapter.DemoAdapter.1</value>

     </items>

     <items>

        <label>Version</label>

        <name>reqVersion</name>

        <value>3.0</value>

     </items>

     <items>

        <label>CTI Adapter URL</label>

        <name>reqAdapterUrl</name>

        <value>http://localhost:11000</value>

     </items>

     <label>General Information</label>

     <name>reqGeneralInfo</name>

   </sections>

```


### Metadata Types CallCenterRoutingMap

```
      <sections>

        <items>

           <label>Outside Prefix</label>

           <name>reqOutsidePrefix</name>

           <value>1</value>

        </items>

        <items>

           <label>Long Distance Prefix</label>

           <name>reqLongDistPrefix</name>

           <value>1</value>

        </items>

        <items>

           <label>International Prefix</label>

           <name>reqInternationalPrefix</name>

           <value>01</value>

        </items>

        <label>Dialing Options</label>

        <name>reqDialingOptions</name>

      </sections>

      <version>4</version>

   </CallCenter>

```

[For information about the CallCenter definition file, see Call Center Definition Files.](https://developer.salesforce.com/docs/atlas.en-us.210.0.api_cti.meta/api_cti/sforce_api_cti_call_def_file.htm)

### CallCenterRoutingMap

Represents the mapping between a user or queue in a Salesforce org to a user or queue in an external system’s call center.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### CallCenterRoutingMap components have the suffix .callCenterRoutingMap and are stored in the

`callCenterRoutingMaps` folder.

Version

### CallCenterRoutingMap components are available in API version 52.0 and later.

Special Access Rules

This type requires Contact Center Admin, Contact Center Admin (Partner Telephony), Contact Center Supervisor, or Manage Call Centers
permission.


Metadata Types CallCenterRoutingMap

Fields

**Field Name** **Description**

```
callCenter

developerName

externalId

masterLabel

quickConnect

referenceRecord

```

**Field Type**
string

**Description**

Required.

Reference to a call center.

**Field Type**
string

**Description**

Required.

The developer name is a combination of the Salesforce user ID or queue name, and
the `callCenter` value, with an underscore between these two values.

**•** `[SALESFORCE_USER_ID]_[CALL_CENTER]`

**•** `[SALESFORCE_QUEUE_NAME]_[CALL_CENTER]`

**Field Type**
string

**Description**

Required.

Unique identifier for the external system’s user or queue.

**Field Type**
string

**Description**

Required.

The master label of the CallCenterRoutingMap.

**Field Type**
string

**Description**
The Amazon Connect QuickConnectId ARN used to determine agent availability for
Omni-Channel call transfers. Available in API version 56.0 and later.

**Field Type**
string

**Description**

Required.


### Metadata Types CallCoachingMediaProvider

**Field Name** **Description**

Lookup field to a Salesforce user or queue.

Declarative Metadata Sample Definition

The following is an example of a CallCenterRoutingMap component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CallCenterRoutingMap xmlns="http://soap.sforce.com/2006/04/metadata">

      <callCenter>ExampleCallCenter</callCenter>

   <developerName>User_001ABC00000FjYIIA0_04vZ6000000Cagl</developerName>

   <externalId>arn:aws:connect:ap-northeast-1:484907484500:instance/examplestring-9c18-4aa5-b5fe-cda6f34d99a0/agent/a69f7afe-5b04-4aa8-b5ee-108a84d0f504</externalId>

      <masterLabel>001ABC00000FjYIIA0</masterLabel>

      <referenceRecord>example.d2b87b8182fa@salesforce.com</referenceRecord>

   </CallCenterRoutingMap>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>User_001ABC00000FjYIIA0_04vZ6000000Cagl</members>

        <name>CallCenterRoutingMap</name>

      </types>

      <version>64.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### CallCoachingMediaProvider

Represents the CallCoachingMediaProvider configuration. Use CallCoachingMediaProvider to configure which providers of voice recordings
that Einstein Conversation Insights can use. For example, Sales Dialer can provide voice recordings. Einstein Conversation Insights then
stores and analyzes call recordings to surface insights and trends in customer conversations.This type extends the Metadata metadata
type and inherits its `fullName` field.

File Suffix and Directory Location

### CallCoachingMediaProvider components have the suffix .callCoachingMediaProvider and are stored in the CallCoachingMediaProvider folder.

Version

### CallCoachingMediaProvider components are available in API version 49.0 and later.


### Metadata Types CampaignInfluenceModel

Special Access Rules

You must be a Sales Engagement customer to access this metadata type.

Fields

**Field Name** **Field Type** **Description**

`isActive` boolean

Indicates whether the media provider can upload voice recordings ( `true` ) or
not ( `false` ).

Default value is `false` .

`providerDescription` string Description of the media provider.

`providerName` string Name of the media provider.

Declarative Metadata Sample Definition

The following is an example of a CallCoachingMediaProvider component.

```
<?xml version="1.0" encoding="UTF-8"?>

<CallCoachingMediaProvider xmlns="http://soap.sforce.com/2006/04/metadata">

   <isActive>true</isActive>

   <providerDescription>Salesforce telephony provider</providerDescription>

   <providerName>Dialer</providerName>

</CallCoachingMediaProvider>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>*</members>

     <name>CallCoachingMediaProvider</name>

   </types>

   <version>49.0</version>

</Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### CampaignInfluenceModel

Represents a campaign influence model used by Customizable Campaign Influence. You can’t configure Customizable Campaign
Influence via the Metadata API, but you can add a campaign influence model.

This type extends the Metadata metadata type and inherits its `fullName` field.


Metadata Types CampaignInfluenceModel

[Note: This information applies only to Customizable Campaign Influence and not to Campaign Influence 1.0 .](https://help.salesforce.com/s/articleView?id=sf.campaigns_influence_original.htm&language=en_US)

File Suffix and Directory Location

CampaignInfluenceModel values are stored in the `campaignInfluenceModels` directory of the corresponding package directory.
The file name matches the model name, and the extension is `.campaignInfluenceModel` .

Version

CampaignInfluenceModel components are available in API version 38.0 and later.

Fields

**Field Name** **Field Type** **Description**

`isActive` boolean Indicates whether the model is active. Active models can generate
campaign influence records. Deactivating a model deletes its campaign

influence records. Custom models are always active and this field is
ignored. This field is available beginning with API version 40.0.

`isDefaultModel` boolean Required. Indicates if the model is the default model or not. Only
campaign influence records associated with the default model appear

on campaigns and opportunities. You can only have one default model
at a time. A model must be active to become the default model.

Activating or deactivating custom models does not automatically
generate or delete campaign influence records.

`isModelLocked` boolean Required. Indicates if the model is locked or not. Campaign Influence
records for locked models can be manipulated only via the API.

`modelDescription` string A description of the influence model.

`name` string Required. A unique name for the model.

`recordPreference` picklist The value of this field determines when to create campaign influence
records.

**•** `AllRecords` : Creates records regardless of the revenue attribution
percentage.

**•** `RecordsWithAttribution` : Creates records only when the
revenue attribution is greater than 0%.

This field is available In API version 41.0 and later.

Declarative Metadata Sample Definition

The following is an example of a CampaignInfluenceModel component that represents the default Salesforce campaign influence
attribution model. The default `isDefaultModel` value of `true` can be changed if another model is created and set as the default


### Metadata Types CaseSubjectParticle

model. The `isModelLocked` value of `true` means that Campaign Influence records for this model can be seen in the UI, but not
created, updated, or deleted.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CampaignInfluenceModel xmlns="http://soap.sforce.com/2006/04/metadata">

      <isActive>true</isActive>

      <isDefaultModel>true</isDefaultModel>

     <isModelLocked>true</isModelLocked> <recordPreference>AllRecords</recordPreference>

      <modelDescription>Primary Campaign gets 100% of the revenue share</modelDescription>

      <name>Salesforce Model</name>

   </CampaignInfluenceModel>

```

The following is an example of a CampaignInfluenceModel component that creates an influence model called Last Touch, which will
not be the default model.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CampaignInfluenceModel xmlns="http://soap.sforce.com/2006/04/metadata">

      <isActive>true</isActive>

      <isDefaultModel>false</isDefaultModel>

      <isModelLocked>true</isModelLocked>

      <modelDescription>This model gives 100% influence attribution to the last campaign

   that touched the contact.</modelDescription>

      <name>Last Touch</name>

      <recordPreference>RecordsWithAttribution</recordPreference>

   </CampaignInfluenceModel>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### CaseSubjectParticle

Represents the Social Business Rules custom format for the **Case Subject** field on cases created from inbound social posts.

File Suffix and Directory Location

### CaseSubjectParticle components have the suffix .CaseSubjectParticle and are stored in the CaseSubjectParticles

folder.

Version

### CaseSubjectParticle is available in API version 41.0 and later.


Metadata Types CaseSubjectParticle

Fields

**Field Name** **Field Type** **Description**

`index` int Required. The order in which the custom **Case Subject** is
generated, meaning if the social network is 0 and the social

message is 1, then the subject generates as `Twitter |`
`Tweet` .

`textField` string Specifies inbound social content added to **Case Subject** in
case records.

Required. Specifies the custom **Case Subject** format from
which inbound social content appears in case records. Valid
values are:

**•** `ProvidedString`

**•** `Source`

**•** `MessageType`

**•** `SocialHandle`

**•** `SocialNetwork`

**•** `Sentiment`

**•** `RealName`

**•** `Content`

**•** `PipeSeparator`

**•** `ColonSeparator`

**•** `HyphenSeparator`

```
type

```

CaseSubjectParticleType
(enumeration of type
string)

Declarative Metadata Sample Definition

This is a sample of a `.CaseSubjectParticle` file.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns=http://soap.sforce.com/2006/04/metadata"">

   <types>

     <members>*</members>

     <name>CaseSubjectParticle</name>

   </types>

   <version>41.0</version>

</Package>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.


### Metadata Types CareBenefitVerifySettings CareBenefitVerifySettings

Represents the configuration settings for benefit verification requests.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

File Suffix and Directory Location

### CareBenefitVerifySettings components have the suffix .careBenefitVerifySettings and are stored in the

`careBenefitVerifySettings` folder.

Version

### CareBenefitVerifySettings components are available in API version 52.0 and later.

Fields

**Field Name** **Description**

```
codeSetType

defaultNpi

generalPlanServiceTypeCode

isDefault

```

**Field Type**
string

**Description**
Specifies the code set type for the benefits verification service type codes.

**Field Type**
string

**Description**
Default National Provider Identifier to be used in the benefits verification request.

**Field Type**
string

**Description**
Service type code for the plan benefits as a whole.

**Field Type**
boolean

**Description**
Indicates whether this record is the default verification service `(true)` or not
`(false)` .


Metadata Types CareBenefitVerifySettings

**Field Name** **Description**

```
masterLabel

organizationName

serviceApexClass

serviceNamedCredential

serviceTypeSourceSystem

uriPath

```

**Field Type**
string

**Description**

Required.

Name of the benefits verification service.

**Field Type**
string

**Description**
Specifies the organization name for the benefits verification request service.

**Field Type**
string

**Description**
Apex class used to access the benefits verification service.

**Field Type**
string

**Description**
Credential used to access the benefits verification service.

**Field Type**
string

**Description**
Service type code for the plan benefits as a whole.

**Field Type**
string

**Description**
Link to payer endpoint.

Declarative Metadata Sample Definition

This is an example of a CareBenefitVerifySettings component.

```
<?xml version="1.0" encoding="UTF-8"?>

<CareBenefitVerifySettings xmlns="http://soap.sforce.com/2006/04/metadata">

   <generalPlanServiceTypeCode>abc</generalPlanServiceTypeCode>

   <isDefault>true</isDefault>

   <masterLabel>test</masterLabel>

   <serviceApexClass>TestApexClass</serviceApexClass>

   <serviceNamedCredential>test</serviceNamedCredential>

   <uriPath>efgh</uriPath>

```


### Metadata Types CareLimitType

```
      <serviceTypeSourceSystem>Lorem ipsum dolor</serviceTypeSourceSystem>

      <codeSetType>Code set</codeSetType>

      <defaultNpi>Npi info</defaultNpi>

      <organizationName>Organization name</organizationName>

   </CareBenefitVerifySettings>

```

This is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>CareBenefitVerifySettings</name>

      </types>

      <types>

        <members>*</members>

        <name>ApexClass</name>

      </types>

      <types>

        <members>*</members>

        <name>NamedCredential</name>

      </types>

      <version>52.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### CareLimitType

Defines the characteristics of limits on benefit provision.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

File Suffix and Directory Location

### CareLimitType components have the suffix .careLimitType and are stored in the careLimitTypes folder.

Version

### CareLimitType components are available in API version 52.0 and later.


Metadata Types CareLimitType

Fields

**Field Name** **Description**

```
isProtected

limitType

masterLabel

metricType

```

**Field Type**
boolean

**Description**
An auto-generated value that doesn’t impact the behavior of the metadata type.

**Field Type**
string

**Description**
Source of limit on benefit provision, such as a co-insurance requirement.

**Field Type**
string

**Description**

Required.

Name of the limit type.

**Field Type**
CareLimitTypeMetricType (enumeration of type string)

**Description**
Metric to be used for calculating and displaying the benefit limit, such as number of
visits, amount spent, or percentage of allowed expenditure.

Valid values are:

**•** `Amount`

**•** `Money`

**•** `Percentage`

**•** `Text`

Declarative Metadata Sample Definition

This is an example of a CareLimitType component.

```
<?xml version="1.0" encoding="UTF-8"?>

<CareLimitType xmlns="http://soap.sforce.com/2006/04/metadata">

   <limitType>test</limitType>

   <masterLabel>test</masterLabel>

   <metricType>Money</metricType>

   <isProtected>false</isProtected>

</CareLimitType>

```


### Metadata Types CareSystemFieldMapping

This is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>CareLimitType</name>

      </types>

      <version>52.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### CareSystemFieldMapping

Represents a mapping from source system fields to Salesforce objects and fields. This type extends the Metadata metadata type and
inherits its `fullName` field.

[other]: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### CareSystemFieldMapping components have the suffix .careSystemFieldMapping and are stored in the

`careSystemFieldMappings` folder.

Version

### CareSystemFieldMapping components are available in API version 49.0 and later.

Special Access Rules

To use this metadata type, your Salesforce org must have the Health Cloud or Life Sciences Cloud license and the user must have the
Health Cloud Foundation (for Health Cloud) or Health Cloud Starter (for Life Sciences Cloud) permission set.

Fields

**Field Name** **Field Type** **Description**

`externalIdField` string The ID of the field in the external system.

`isActive` boolean Indicates whether this field mapping is active ( `true` ) or not ( `false` ).
The default value is False.


Metadata Types CareSystemFieldMapping

**Field Name** **Field Type** **Description**

`isProtected` boolean An auto-generated value that doesn’t currently impact the behavior of
the metadata type.

`masterLabel` string Required. The name of the care system field mapping.

```
role

```

SourceSystemFieldRole Required. The role the field represents. Valid values are:
(enumeration of

**•** `Patient` —When the `role` field is set to `Patient`, the

type string)

Enrollment API uses the value of `externalIdField` as the
patient ID. This role can be used when `targetObject` is set to
`Account` .

**•** `RemoteMonitoringDevice` —Indicates which
`externalIdField` on the Asset object maps to the `Device`
field in the CareObservation object. This role can be used when
targetObject is set to Asset.

**•** `RemoteMonitoringPatient` —Indicates which
`externalIdField` on the Account object maps to the
`ObservedSubject` field in the Care Observation object. This
role is used when targetObject is set to Account.

**•** `ServiceProvider` —The Enrollment API uses the value of
`externalIdField` as the provider ID. This role is used when
`targetObject` is set to `Account` .

**•** `NotApplicable` —This role is used when `targetObject` is
set to `CareProgram` or `Product`, which means that there is
no applicable role.

`sourceSystem` string The system where the record originated.

`targetObject` string The name of the Salesforce object to which the external system field is
mapped.

Declarative Metadata Sample Definition

The following is an example of a CareSystemFieldMapping component.

```
<?xml version="1.0" encoding="UTF-8"?>

<CareSystemFieldMapping xmlns="http://soap.sforce.com/2006/04/metadata">

   <externalIdField>AccountNumber</externalIdField>

   <isActive>true</isActive>

   <isProtected>false</isProtected>

   <masterLabel>Map1</masterLabel>

   <role>Patient</role>

   <sourceSystem>Epic</sourceSystem>

   <targetObject>Account</targetObject>

</CareSystemFieldMapping>

```


### Metadata Types CareProviderSearchConfig

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>patient</members>

        <name>CareSystemFieldMapping</name>

      </types>

      <version>49.0</version>

   </Package>

### CareProviderSearchConfig

```

Represents the information about the fields that appear in care provider search results. This type extends the Metadata metadata type
and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### CareProviderSearchConfig components have the suffix .careProviderSearchConfig and are stored in the

`careProviderSearchConfigs` folder.

Version

### CareProviderSearchConfig components are available in API version 48.0 and later.

Fields

**Field Name** **Field Type** **Description**

`isActive` boolean Indicates whether this configuration is active ( `true` ) or not ( `false` ).

`isProtected` boolean An auto-generated value that doesn’t currently impact the behavior of
the metadata type.

Required. Indicates mapped objects.

Possible values are;

**•** HealthCarePractitionerFacility

**•** HealthCareProvider

```
mappedObject

```

ProviderSearch
ObjectMapping
(enumeration of
type string)

`masterLabel` string Required. Name of the care provider.

`sourceField` string API name of the field that is copied to the target object.

`targetField` string API name of the field to copy the data to.


### Metadata Types CareRequestConfiguration

Declarative Metadata Sample Definition

The following is an example of a CareProviderSearchConfig component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CareProviderSearchConfig xmlns="http://soap.sforce.com/2006/04/metadata">

      <sourceField>Test1__c</sourceField>

      <targetField>Test1__c</targetField>

      <mappedObject>HealthcareProvider</mappedObject>

      <isProtected>false</isProtected>

      <isActive>true</isActive>

      <masterLabel>testlabel</masterLabel>

   </CareProviderSearchConfig>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>HealthcareProvider.Test1__c</members>

        <name>CustomField</name>

      </types>

      <types>

        <members>CareProviderSearchableField.Test1__c</members>

        <name>CustomField</name>

      </types>

      <types>

        <members>Test</members>

        <name>CareProviderSearchConfig</name>

      </types>

      <version>48.0</version>

   </Package>

### CareRequestConfiguration

```

Represents the details for a record type such as service request, drug request, or admission request. One or more record types can be
associated with a care request.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

File Suffix and Directory Location

### CareRequestConfiguration components have the suffix .careRequestConfiguration and are stored in the

`careRequestConfigurations` folder.


Metadata Types CareRequestConfiguration

Version

CareRequestConfiguration components are available in API version 44.0 and later.

Fields

**Field Name** **Description**

```
careRequestRecordType

careRequestRecords

careRequestType

isActive

```

**Field Type**
string

**Description**

Required.

The record type for the care request.

**Field Type**

CareRequestRecords[]

**Description**
The list of objects you can select to configure the care request.

**Field Type**
string

**Description**

Required.

The type of care request. For example, an appeal, a service request, or an admission.

**Field Type**
boolean

**Description**
Indicates whether the care request is active ( `true` ) or not ( `false` ).

**Field Type**
boolean

**Description**
Indicates whether the record type of the care request is default ( `true` ) or not ( `false` ).

**Field Type**
string

**Description**

Required.

A user-friendly name for CareRequestConfiguration, which is defined when the
CareRequestConfiguration is created.


Metadata Types CareRequestConfiguration

CareRequestRecords

Displays a list of objects to customize the care request.

**Field Name** **Description**

```
careRequestRecord

```

**Field Type**
string

**Description**

Required.

The object selected to configure the care request.

Declarative Metadata Sample Definition

This is an example of a CareRequestConfiguration component.

```
<?xml version="1.0" encoding="UTF-8"?>

<CareRequestConfiguration xmlns="http://soap.sforce.com/2006/04/metadata">

   <careRequestRecordType>DrugRequest</careRequestRecordType>

   <careRequestRecords>

     <careRequestRecord>CareRequestItem</careRequestRecord>

   </careRequestRecords>

   <careRequestRecords>

     <careRequestRecord>CareRequestDrug</careRequestRecord>

   </careRequestRecords>

   <careRequestType>Drug Request</careRequestType>

   <isActive>false</isActive>

   <isDefaultRecordType>false</isDefaultRecordType>

   <masterLabel>DrugRequest</masterLabel>

</CareRequestConfiguration>

```

This is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>Case.DrugRequest</members>

     <name>BusinessProcess</name>

   </types>

   <types>

     <members>*</members>

     <name>CareRequestConfiguration</name>

   </types>

   <types>

     <members>CareRequest.DrugRequest</members>

     <members>CareRequestDrug.DrugRequest</members>

     <members>CareRequestItem.DrugRequest</members>

     <members>Case.DrugRequest</members>

     <name>RecordType</name>

   </types>

```


### Metadata Types Certificate

```
      <version>44.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### Certificate

Represents a certificate used for digital signatures that verify that requests are coming from your org. Certificates are used for either
authenticated single sign-on with an external website, or when using your org as an identity provider. This type extends the Metadata
With Content metadata type and inherits its `content` and `fullName` fields.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### Certificate components have the suffix .crt and are stored in the certs folder.

Version

### Certificate components are available in API version 36.0 and later.

Fields

**Field Name** **Field Type** **Description**

`caSigned` boolean Required. Indicates whether this certificate is signed by the issuer (true)
or not (false).

`encryptedWithPlatformEncryption` boolean Indicates whether this certificate is encrypted with Platform Encryption.

`expirationDate` dateTime The date that this certificate expires and is no longer usable. For
self-signed certificates, if `keySize` is 2048 bits, the expiration date is

automatically 1 year after you create the certificate. If `keySize` is 4096
bits, the expiration date is automatically 2 years after you create the
certificate. For CA-signed certificates, `expirationDate` is
automatically updated to the signed certificate’s expiration date when
a signed certificate chain is uploaded. The date format is YYYY-MM-DD.

### keySize int Certificate keys can be either 2048 bits or 4096 bits. A certificate with

4096-bit keys lasts 2 years, and a certificate with 2048-bit keys lasts 1

year. Certificates with 2048-bit keys are faster than certificates with
4096-bit keys. If `keySize` isn’t specified when you create a certificate,
the key size defaults to 2048 bits.


Metadata Types Certificate

**Field Name** **Field Type** **Description**

`masterLabel` string

`privateKeyExportable` boolean

Usage

Required. A user-friendly name for the certificate that appears in the
Salesforce user interface, such as in Certificate and Key Management.
Limit: 64 characters.

Indicates whether this certificate’s private key is exportable. If
`privateKeyExportable` isn’t specified when you create a
certificate, its default value is `true` .

The Metadata API can be used to create a self-signed or a CA-signed certificate. The .crt file’s contents are the certificate chain, which
can be updated when you renew or update the intermediate certificate chain of a CA-signed certificate. After creating a CA-signed
[certificate, the .crt file contains a certificate signing request (CSR). For details, see About Salesforce Certificates and Keys in Salesforce](https://help.salesforce.com/apex/HTViewHelpDoc?id=security_keys_about.htm&language=en_US)
Help.

To copy an existing certificate’s X.509 parameter data to a new certificate, upload the existing certificate. You can also use this procedure
to renew a certificate. A new private+public key pair is created with a new certificate. Salesforce doesn’t allow the import or export of
the private key via the API.

Using the Metadata API, you can download a CSR. After it’s CA-signed, you can upload it back to Salesforce.

After the signed certificate chain is uploaded via the Metadata API, the CSR of that certificate can’t be downloaded via the API anymore.
The content of the `.crt` file is the signed certificate chain. However, the CSR can still be downloaded via the UI.

**•** Downloading a CSR—The CSR is downloadable after a CA-signed cert is created. If a signed certificate hasn’t been uploaded to that
certificate, the content of the downloaded .crt file is the CSR.

**•** Uploading a CA-Signed Certificate—To upload the signed certificate chain back to Salesforce, save the signed certificate chain as
the content of the .crt file and update it via the Metadata API.

Declarative Metadata Sample Definition

The following is an example of a Certificate component.

```
<?xml version="1.0" encoding="UTF-8"?>

<Certificate xmlns="http://soap.sforce.com/2006/04/metadata">

   <caSigned>true</caSigned>

   <encryptedWithPlatformEncryption>true</encryptedWithPlatformEncryption>

   <expirationDate>2017-03-19</expirationDate>

   <keySize>4096</keySize>

   <masterLabel>My Certificate Name</masterLabel>

   <privateKeyExportable>true</privateKeyExportable>

</Certificate>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


### Metadata Types ChatterExtension ChatterExtension

Represents the metadata used to describe a Rich Publisher App that’s integrated with the Chatter publisher.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Retrieving ChatterExtension

Using an API tool, you can get extension information from `package.xml` using this code.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

    <types>

     <members>xw1</members>

     <name>ChatterExtension</name>

    </types>

    <version>41.0</version>

   </Package>

```

Use the `<members>` tag to name a specific extension (in this example, _`xw1`_ ), or use the wildcard (*) symbol to retrieve all your
extensions.

Here’s an example of retrieved information.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ChatterExtension xmlns="http://soap.sforce.com/2006/04/metadata">

     <compositionComponent>xwComp</compositionComponent>

     <description>des</description>

     <extensionName>xw1</extensionName>

     <headerText>h1</headerText>

     <hoverText>h2</hoverText>

     <icon>tiger</icon>

     <masterLabel>primary</masterLabel>

     <renderComponent>xwRend</renderComponent>

     <type>Lightning</type>

   </ChatterExtension>

```

Version

### ChatterExtension is a new feature in API version 41.0.

Fields

**Field** **Field Type** **Description**

`compositionComponent` string Required. The composition component of the Rich Publisher
App that you provide. It’s comprised of the

```
                              lightning:availableForChatterExtensionComposer
```

interface.

`description` string Required. The description of your custom Rich Publisher App.


### Metadata Types ChoiceList

**Field** **Field Type** **Description**

`extensionName` string Required. The name of your extension. That is, your Rich
Publisher App.

`headerText` string

`hoverText` string

The text to show in the header of your app composer. Header
text is required for Lightning type extensions. This text can be
localized.

The text to show when a user mouses over your extension’s
icon. Mouse-over text is required for Lightning type extensions.
This text can be localized.

`icon` string Required. The icon to show in the Chatter publisher. Use an
existing file asset id from your org.

`isProtected` boolean An auto-generated value. It currently has no impact.

`masterLabel` string Required. Label for the ChatterExtension object.

`renderComponent` string Required. The rendering component of the Rich Publisher App
that you provide. It’s comprised of the

```
                           lightning:availableForChatterExtensionRenderer
```

interface.

`type` ChatterExtensionType
(enumeration of type string)

Wildcard Support in the Manifest File

Required. Describes the type of the extension. Currently, the
only value supported is _`Lightning`_ . Included to allow for
other possible types in the future.

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

[Integrate Your Custom Apps into the Chatter Publisher](https://developer.salesforce.com/docs/atlas.en-us.260.0.lightning.meta/lightning/components_integrate_customapps_to_publisher.htm)

### ChoiceList

Represents the `Choicelist` dropdown field that’s used for pre-chat.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.


Metadata Types ChoiceList

File Suffix and Directory Location

ChoiceList components have the suffix `.ChoiceList` and are stored in the `ChoiceList` folder.

Version

ChoiceList components are available in API version 62 and later.

Special Access Rules

There are no additional access requirements that are specific to this type.

Fields

**Field Name** **Description**

```
choiceListValue

description

masterLabel

```

ChoiceListValue

**Field Type**

ChoiceListValue[]

**Description**
A list of choices to display in the choice list.

**Field Type**
string

**Description**
A description of the choice list.

**Field Type**
string

**Description**

Required. The label for the choice list.

Represents a choice list value in the pre-chat dropdown. ChoiceListValue is available in API version 62 or later.

**Field Name** **Description**

```
embeddedServiceCustomLabels

isDefaultValue

```

**Field Type**

EmbeddedServiceCustomLabel[] on page 1003

**Description**
Custom labels for the choicelist value.

**Field Type**
boolean


Metadata Types ChoiceList

**Field Name** **Description**

**Description**

Required. Indicates whether the choicelist value should be selected by default.

```
order

valueName

```

**Field Type**
int

**Description**

Required. The order of the choicelist value in the choicelist dropdown field.

**Field Type**
string

**Description**

Required. The value of the choicelist.

Declarative Metadata Sample Definition

The following is an example of a Choicelist component.

```
<?xml version="1.0" encoding="UTF-8"?>

<ChoiceList xmlns="http://soap.sforce.com/2006/04/metadata">

   <choiceListValue>

     <embeddedServiceCustomLabels>

<customLabel>EM_PreChat_ChoiceList_PrechatCustomFieldLabel_133xx0000004GG1_7741637</customLabel>

        <labelKey>EM_PreChat_ChoiceList_PrechatCustomFieldLabel</labelKey>

        <feature>EmbeddedMessaging</feature>

     </embeddedServiceCustomLabels>

     <isDefaultValue>true</isDefaultValue>

     <order>0</order>

     <valueName>Pizza</valueName>

   </choiceListValue>

   <choiceListValue>

     <embeddedServiceCustomLabels>

<customLabel>EM_PreChat_ChoiceList_PrechatCustomFieldLabel_133xx0000004GG2_5523047</customLabel>

        <labelKey>EM_PreChat_ChoiceList_PrechatCustomFieldLabel</labelKey>

        <feature>EmbeddedMessaging</feature>

     </embeddedServiceCustomLabels>

     <isDefaultValue>false</isDefaultValue>

     <order>1</order>

     <valueName>Burger</valueName>

   </choiceListValue>

   <masterLabel>Food</masterLabel>

   <description>Food Choice List</description>

</ChoiceList>

```


### Metadata Types ClaimFinancialSettings

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>ChoiceList</name>

      </types>

      <version>62.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### ClaimFinancialSettings

Represents the configuration settings for Insurance Claim Financial Services.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### ClaimFinancialSettings components have the suffix claimFinancialSettings and are stored in the ClaimFinancialSettings folder.

Version

### ClaimFinancialSettings components are available in API version 57.0 and later.

Special Access Rules

To access this metadata type, you require access to either InsurancePolicyAdminAccess or InsuranceClaimMgmtAccess add-on license.

Fields

**Field Name** **Description**

```
claimCovPendingAuthStatus

```

**Field Type**
string


Metadata Types ClaimFinancialSettings

**Field Name** **Description**

**Description**

Required.

The status of pending financial authority for claim coverage.

```
claimPendingAuthorityStatus

clmCovPymtDtlPendAuthSts

masterLabel

```

**Field Type**
string

**Description**

Required.

The status of pending financial authority for claim.

**Field Type**
string

**Description**

Required.

The status of pending financial authority for claim coverage payment detail.

**Field Type**
string

**Description**

Required.

The unique label that identifies the claim financial settings throughout the Salesforce
user interface.

Declarative Metadata Sample Definition

The following is an example of a ClaimFinancialSettings component.

```
<?xml version="1.0" encoding="UTF-8"?>

<ClaimFinancialSettings xmlns="http://soap.sforce.com/2006/04/metadata">

   <claimCovPendingAuthStatus>Pending Authority</claimCovPendingAuthStatus>

   <claimPendingAuthorityStatus>Pending Authority</claimPendingAuthorityStatus>

   <clmCovPymtDtlPendAuthSts>Pending Authority</clmCovPymtDtlPendAuthSts>

   <masterLabel>Claim Financial Settings</masterLabel>

</ClaimFinancialSettings>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?><!-
  ~ Copyright 2022 salesforce.com, inc.

  ~ All Rights Reserved

  ~ Company Confidential

  -->

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

```


### Metadata Types ClauseCatgConfiguration

```
        <members>*</members>

        <name>ClaimFinancialSettings</name>

      </types>

      <version>57.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### ClauseCatgConfiguration

Represents the configuration about the clause category that can be used to categorize your disclosure and compliance reports from
standardized disclosure templates in a response document.

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

File Suffix and Directory Location

### ClauseCatgConfiguration components have the suffix .clauseCatgConfiguration and are stored in the

`clauseCatgConfigurations` folder.

Version

### ClauseCatgConfiguration components are available in API version 57.0 and later.

Special Access Rules

The ClauseManagementAddOn license is required to access this object along with user access for the Clause Designer User permission
set license.

Fields

**Field Name** **Description**

```
description

isProtected

```

**Field Type**
string

**Description**
The description about the clause category configuration.

**Field Type**
boolean


Metadata Types ClauseCatgConfiguration

**Field Name** **Description**

**Description**
An auto-generated value that doesn’t impact the behavior of the metadata type. The
default is `false` .

```
masterLabel

usageType

```

**Field Type**
string

**Description**

Required.

A user-friendly name for ClauseCatgConfiguration, which is defined when the
ClauseCatgConfiguration is created.

**Field Type**
ClmCategoryUsageType

**Description**

Required.

The usage type of the clause category configuration.

Possible values are:

**•** `ContractClauseCategory`

**•** `DisclosureCategory`

Declarative Metadata Sample Definition

The following is an example of a ClauseCatgConfiguration component.

```
<?xml version="1.0" encoding="UTF-8"?>

<ClauseCatgConfiguration

 xmlns="http://soap.sforce.com/2006/04/metadata">

 <description>This is to add description for Contract Clause Category.</description>

 <usageType>ContractClauseCategory</usageType>

 <isProtected>false</isProtected>

 <masterLabel>Contract Clause Cat</masterLabel>

</ClauseCatgConfiguration>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package

 xmlns="http://soap.sforce.com/2006/04/metadata">

 <fullName>Pkg</fullName>

 <types>

  <name>ClauseCatgConfiguration</name>

 </types>

```


### Metadata Types CleanDataService

```
    <version>57.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### CleanDataService

Represents a data service that adds and updates data in standard objects.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### CleanDataService components have the .cleanDataService suffix and are stored in the cleanDataServices directory.

The name of the component file is based on the name of the object associated with the data service. For example, the component file
name `cleanDataServices/DataCloudCompanyMatch.cleanDataService` describes a data service component
called DataCloudCompanyMatch that's associated with the company name in account objects.

Version

### CleanDataService components are available in API version 66.0 and later.

Fields

**Field Name** **Field Type** **Description**

`cleanRules` CleanRule[] Required. A list of data integration rules

`description` string Required. A description of the data service

`masterLabel` string Required. Label for this data service. Although this value is displayed, it’s
an internal label for the data service and isn’t translated.

`matchEngine` string Required. A key that maps to the internal data service identifier.

CleanRule

Represents information that controls how the data service adds and updates data in an org.


Metadata Types CleanDataService

**Field Name** **Field Type** **Description**

`bulkEnabled` boolean Required. If this field is set to `true`, Salesforce applies the data integration
rule to existing records whenever the rule is updated or saved.

`bypassTriggers` boolean Required. If this field is set to `true`, Salesforce bypasses triggers when it applies
the rule; otherwise, it applies triggers after it applies the rule.

`bypassWorkflow` boolean

Required. If this field is set to `true`, Salesforce bypasses workflow rules when
it applies the data integration rule; otherwise, it applies workflow rules after it
applies the rule.

`description` string Required. User-friendly text that describes the data integration rule.

`developerName` string Required. This name can contain only underscores and alphanumeric characters,
and must be unique in your org. It must begin with a letter, not include spaces,

not end with an underscore, and not contain two consecutive underscores.
This unique name prevents conflicts with rules from other packages that have
the same `masterLabel` .

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

`fieldMappings` FieldMapping[] Required. A list of FieldMapping entries for the rule.

`masterLabel` string Required. Label for this object. This display value is the internal label that is not
translated.

`matchRule` string Required. An internal label for a matching rule in the data service that’s
associated with the CleanRule.

`sourceSobjectType` string Required. A virtual object in the data service that is associated with the
CleanRule. Specifying a non-existent object causes an error.

`status` string Required. Status of the data integration rule. Valid values are `Active` and
`Inactive` .

`targetSobjectType` string

FieldMapping

Required. A standard object that’s the target of additions and updates specified
by this CleanRule. Specifying an object that the data service does not support
causes an error.

Represents a mapping between fields in the data service and fields in an object in the org.

**Field Name** **Field Type** **Description**

`developerName` string Required. This name can contain only underscores and alphanumeric characters,
and must be unique in your org. It must begin with a letter, not include spaces,

not end with an underscore, and not contain two consecutive underscores.
This unique name prevents conflicts with field mappings from other packages
that have the same `masterLabel` .


Metadata Types CleanDataService

**Field Name** **Field Type** **Description**

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

`fieldMappingRows` FieldMappingRow[] Required. A list of FieldMappingRow entries. Each entry represents a field in a
standard object that maps to a field in the data service.

`masterLabel` string Required. Label for this object. This display value is the internal label that is not
translated.

`SObjectType` string Required. The standard object associated with this FieldMapping. Specifying
an object that the data service does not support causes an error.

FieldMappingRow

Represents the status of a CleanRule.

**Field Name** **Field Type** **Description**

`fieldName` string The display name for the field represented by the FieldMappingRow.

`fieldMappingFields` FieldMappingField[] Required. A list of FieldMappingField entries. Each entry is a field in a standard
object that maps to a field in the data service.

`mappingOperation` string The comparison operation the data service applies when it compares the value
of this FieldMappingRow to the mapped field in the object specified in

SObjectType. The value of this field is `AutoFill`, which indicates that the
data service only adds data if the object field is blank.

`SObjectType` string The standard object for the field mapped to the FieldMappingRow. Specifying
an object that the data service does not support causes an error.

FieldMappingField

Represents a field in a standard object. A FieldMappingField maps to a FieldMappingRow entry in a data service.

**Field Name** **Field Type** **Description**

`dataServiceField` string Required. A field in the data service that is mapped to this field.

`dataServiceObjectName` string

Required. An object in the data service that contains the FieldMappingRow
associated with this FieldMappingField. Specifying a non-existent object causes
an error.

`priority` int Required. Represents the priority that the data service uses when it updates
the field, relative to other update rules for the same field. Valid values are 1-100.


Metadata Types CleanDataService

Declarative Metadata Sample Definition

The following is an example of a CleanDataService component for the lead standard object.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CleanDataService xmlns="http://soap.sforce.com/2006/04/metadata">

      <cleanRules>

        <bulkEnabled>false</bulkEnabled>

        <bypassTriggers>false</bypassTriggers>

        <bypassWorkflow>false</bypassWorkflow>

        <description>Adds data info to leads</description>

        <developerName>DataService_Leads_Enrichment</developerName>

        <fieldMappings>

           <SObjectType>DataServiceCompanyObject</SObjectType>

           <developerName>DataService_Leads_Enrichment_InputMapping</developerName>

           <fieldMappingRows>

             <SObjectType>DataServiceCompanyObject</SObjectType>

             <fieldMappingFields>

               <dataServiceField>Email</dataServiceField>

               <dataServiceObjectName>Lead</dataServiceObjectName>

               <priority>1</priority>

             </fieldMappingFields>

             <fieldName>Email</fieldName>

             <mappingOperation>Autofill</mappingOperation>

           </fieldMappingRows>

           <fieldMappingRows>

             <SObjectType>DataServiceCompanyObject</SObjectType>

             <fieldMappingFields>

               <dataServiceField>Company</dataServiceField>

               <dataServiceObjectName>Lead</dataServiceObjectName>

               <priority>1</priority>

             </fieldMappingFields>

             <fieldName>Name</fieldName>

             <mappingOperation>Autofill</mappingOperation>

           </fieldMappingRows>

           <masterLabel>DataServiceInputMapping</masterLabel>

        </fieldMappings>

        <fieldMappings>

           <SObjectType>Lead</SObjectType>

           <developerName>DataService_Leads_Enrichment_OutputMapping</developerName>

           <fieldMappingRows>

             <SObjectType>Lead</SObjectType>

             <fieldMappingFields>

               <dataServiceField>EmployeesTotal</dataServiceField>

              <dataServiceObjectName>DataServiceCompanyObject</dataServiceObjectName>

               <priority>1</priority>

             </fieldMappingFields>

             <fieldName>NumberOfEmployees</fieldName>

             <mappingOperation>Autofill</mappingOperation>

           </fieldMappingRows>

           <fieldMappingRows>

             <SObjectType>Lead</SObjectType>

             <fieldMappingFields>

               <dataServiceField>Revenue</dataServiceField>

```


Metadata Types CleanDataService

```
              <dataServiceObjectName>DataServiceCompanyObject</dataServiceObjectName>

               <priority>1</priority>

             </fieldMappingFields>

             <fieldName>AnnualRevenue</fieldName>

             <mappingOperation>Autofill</mappingOperation>

           </fieldMappingRows>

           <fieldMappingRows>

             <SObjectType>Lead</SObjectType>

             <fieldMappingFields>

               <dataServiceField>Industry</dataServiceField>

              <dataServiceObjectName>DataServiceCompanyObject</dataServiceObjectName>

               <priority>1</priority>

             </fieldMappingFields>

             <fieldName>Industry</fieldName>

             <mappingOperation>Autofill</mappingOperation>

           </fieldMappingRows>

           <masterLabel>DataServiceOutputMapping</masterLabel>

        </fieldMappings>

        <masterLabel>Data Service Company Info for Leads</masterLabel>

        <matchRule>DataServiceLeadAppendMatchRule</matchRule>

        <sourceSobjectType>DataServiceCompanyObject</sourceSobjectType>

        <status>Active</status>

        <targetSobjectType>Lead</targetSobjectType>

      </cleanRules>

      <description>Data Service Companies for Leads</description>

      <masterLabel>Data Service Companies for Leads</masterLabel>

      <matchEngine>LeadEnrichmentMatchEngine</matchEngine>

   </CleanDataService>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>DataService_Leads_Enrichment</members>

        <name>CleanDataService</name>

      </types>

      <version>38.0</version>

   </Package>

```

Usage

Use CleanDataService to retrieve all the metadata that describes a data enrichment service. To configure the service in a new org, deploy
the metadata you retrieved. Avoid using CRUD-Based Calls with CleanDataService.

To make small modifications to the CleanDataService component, use the Tooling API.

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


### Metadata Types CMSConnectSource CMSConnectSource

Represents the connection information for external content management systems that feed content to Experience Builder sites. This
type extends the Metadata metadata type and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Note: For use with Change Sets, CMSConnectSource is a dependent of **Network** and **Community** .

File Suffix and Directory Location

### CMSConnectSource components have the suffix .cmsConnectSource and are stored in the cmsConnectSource folder. In

that folder, separate files exist for each network (for example, _`networkname`_ `.` _`sourcedevelopername`_ `.cmsConnectSource` ).
Each file represents a CMS connection.

Version

### CMSConnectSource components are available in API version 43.0 and later.

Special Access Rules

The **CMS Connect org** permission must be enabled.

Fields

**Field Name** **Field Type** **Description**

`cmsConnectAsset` CMSConnectAsset on Represents CSS or JavaScript defined for the connection.
page 591[]

**•** 0–10 for CSS

**•** 0–10 for JavaScript

`cmsConnectLanguage` CMSConnectLanguage 0 to more. Represents language mappings defined for the connection.
on page 591[]

`cmsConnectPersonalization` CMSConnectPersonalization[] 0 or 1. Represents personalization defined for the connection. Only
on page 591 for use when `type` is `AEM` .

`cmsConnectResourceType` CMSConnectResourceType 0–5. Represents JSON definitions defined for the connection.
on page 592[]

`connectionType` CMSSourceConnectionType(enumeration Required. Type of authentication being used with outside system.
of type string) Valid values are:

**•** `Public`

**•** `Authenticated`

`cssScope` string The class name used to prefix and scope the CSS rules.


Metadata Types CMSConnectSource

**Field Name** **Field Type** **Description**

`developerName` string Required. API name of the CMSConnectSource entity.

`languageEnabled` string Required. Valid values are:

**•** `Y` to enable language mapping for connection.

**•** `N` if no language mapping is needed.

`masterLabel` string Required. Connection name

`namedCredential` string

Required when the `connectionType` is `Authenticated` .
API name of `namedCredential` . Before deploying
`namedCredential`, it must exist on the destination org.

`personalizationEnabled` string Required. Valid values are:

**•** `Y` to enable personalization mapping for connection.

**•** Otherwise `N` .

`rootPath` string Required. Root path.

`sortOrder` int Required. Defines the load order of the connection when multiple
connections defined on page. The load order begins with 1.

`status` CMSConnectionStatus(enumeration Required. Status of connection. Valid values are:
of type string)

**•** `ACTIVE`

**•** `INACTIVE`

`type` CMSConnectionSourceType(enumeration Required. The identification of the source connection system. Valid
of type string) values are:

**•** `AEM`

**•** `Drupal`

**•** `WordPress`

**•** `SDL`

**•** `Sitecore`

**•** `Other`

`websiteUrl` string Required if `connectionType` is `Public`

Note: Because there can be existing connections when a package comes in, there’s some INSERT or UPDATE logic to consider:

**•** If you find `developerName` in the destination, then update the existing collection with all details form source.

**•** `namedCredential` is handled through `developerName` . If you don’t find `namedCredential` with
`developerName`, then an error is generated.

**•** If the destination isn’t `sortOrder` from the source, then insert or update with the source `sortOrder` .

**•** If `sortOrder` from the source is already in the destination, then increase the source `sortOrder` by 1 for connections
such that the destination `sortOrder`     - `sortOrder` from the source.


Metadata Types CMSConnectSource

CMSConnectAsset

CMSConnectAsset defines the location, types, and order of assets necessary to support the incoming content, such as JavaScript and
CSS files.

Note: Because there can be existing connections when a package comes in, there’s some INSERT or UPDATE logic to consider:

**•** If `assetPath` exists in the destination, then update the existing record, else the new `assetPath` is inserted.

**•** Always keep the `sortOrder` from the source and adjust the destination accordingly.

**Field Name** **Field Type** **Description**

`assetPath` string Relative path of the asset.

`assetType` string

When used in Apex, this value can be sent as an enum, otherwise, this field
has a type of string.

Allowed values as string

**•** `CSS`

**•** `Javascript`

Allowed values as enum

**•** `CSS`

**•** `Javascript`

`sortOrder` int Loading sequence on the page.

CMSConnectLanguage

CMSConnectLanguage components determine the presented language of the content.

**Field Name** **Field Type** **Description**

`cmsLanguage` string When a language placeholder is in the URL path, this value is used to replace
it.

`language` string

CMSConnectPersonalization

Salesforce supported language.

For information see
[https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_translations.htm](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_translations.htm)

CMSConnectPersonalization is used only with Adobe Experience Manager (AEM).

Note: Because there can be existing connections when a package comes in, there’s some INSERT or UPDATE logic to consider. If
personalization isn’t enabled in the source system, but is enabled in the destination, the destination is disabled. The record for the
connection is deleted from the table.


Metadata Types CMSConnectSource

**Field Name** **Field Type** **Description**

`connectorPage` string The path to the JSP file that you created and installed in AEM.

`connectorPageAsset` string The path to your Javascript file. Providing this path allows you to run scripts
dynamically.

CMSConnectResourceType

CMSConnectResourceType is for use only to define JSON connections.

Note: Because there can be existing connections when a package comes in, there’s some INSERT or UPDATE logic to consider. If
you find the developer name in the destination, then update the existing record with all details from the source.

**Field Name** **Field Type** **Description**

`cmsConnectResourceDefinition` cmsConnectResourceDefinition 0–10 allowed per CMSConnectResourceType.
on page 592[]

`developerName` string API name of CMSConnectResourceType.

`masterLabel` string Content type name.

`resourceType` string The only allowed value is `JSON` .

CMSConnectResourceDefinition

cmsConnectResourceDefinition is used to define JSON connections.

Note: Because there can be existing connections when a package comes in, there’s some INSERT or UPDATE logic to consider:

**•** If you find developerName in the destination, then the existing record is updated with all details from the new source, else
the new value is inserted.

**•** If the current source is DETAIL and the destination has DETAIL with a different name, then the destination is updated to LIST
and the source is inserted as DETAIL.

**Field Name** **Field Type** **Description**

`developerName` string Required. API name of CMSConnectResourceDefinition.

`masterLabel` string Required. developerName of Content Item or Content List.

`options` int

Required. Identifies whether the content from the external source is a single
item or a list.

0 for Content List

1 for Content Item

`payloadType` string Required. The only valid value is `JSON` .

`resourceIdPath` string Relative path to ID. Required for Content Item.

`resourceNamePath` string Relative path to resource name. Required for Content Item.


Metadata Types CMSConnectSource

**Field Name** **Field Type** **Description**

`resourcePath` string Required. JSON resource path.

`rootNodePath` string Only for Content List and collection. Defines the initial starting path for a
collection or list.

Declarative Metadata Sample Definition

The following is an example of a CMSConnectSource definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CMSConnectSource xmlns="http://soap.sforce.com/2006/04/metadata">

      <cmsConnectAsset>

        <assetPath>etc/designs/capricorn/app-prefixed.min.css</assetPath>

        <assetType>CSS</assetType>

        <sortOrder>1</sortOrder>

      </cmsConnectAsset>

      <cmsConnectAsset>

        <assetPath>etc/designs/capricorn/w3data.js</assetPath>

        <assetType>Javascript</assetType>

        <sortOrder>1</sortOrder>

      </cmsConnectAsset>

      <cmsConnectLanguage>

        <cmsLanguage>en</cmsLanguage>

        <language>en_US</language>

      </cmsConnectLanguage>

      <cmsConnectLanguage>

        <cmsLanguage>fr</cmsLanguage>

        <language>fr</language>

      </cmsConnectLanguage>

      <cmsConnectPersonalization>

        <connectorPage>content/salesforceConnector.js</connectorPage>

        <connectorPageAsset>content/js/capricorn/assets.js</connectorPageAsset>

      </cmsConnectPersonalization>

      <cmsConnectResourceType>

        <cmsConnectResourceDefinition>

           <developerName>Details</developerName>

           <masterLabel>Details</masterLabel>

           <options>0</options>

           <payloadType>JSON</payloadType>

           <resourceIdPath>ID</resourceIdPath>

           <resourceNamePath>title</resourceNamePath>

   <resourcePath>rest/v1.1/sites/cmstry.wordpress.com/posts/{component}</resourcePath>

        </cmsConnectResourceDefinition>

        <cmsConnectResourceDefinition>

           <developerName>List</developerName>

           <masterLabel>List</masterLabel>

           <options>1</options>

           <payloadType>JSON</payloadType>

   <resourcePath>rest/v1.1/sites/cmstry.blog.wordpress.com/posts?number={itemsPerPage}&amp;page={pageNumber}</resourcePath>

```


Metadata Types CMSConnectSource

```
        </cmsConnectResourceDefinition>

        <developerName>Posts</developerName>

        <masterLabel>Posts</masterLabel>

        <resourceType>JSON</resourceType>

      </cmsConnectResourceType>

      <connectionType>Public</connectionType>

      <cssScope>capricorn</cssScope>

      <developerName>Capricorn</developerName>

      <languageEnabled>Y</languageEnabled>

      <masterLabel>Capricorn</masterLabel>

      <personalizationEnabled>Y</personalizationEnabled>

      <rootPath>content/capricorn/{language}</rootPath>

      <sortOrder>11</sortOrder>

      <status>ACTIVE</status>

      <type>AEM</type>

      <websiteUrl>https://public-api.wordpress.com</websiteUrl>

   </CMSConnectSource>

```

The following is an example `package.xml` .

```
   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>NetworkA.*</members>

        <name>CMSConnectSource</name>

      </types>

      <version>43.0</version>

   </Package>

```

To retrieve a specific connection:

```
   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>NetworkA. DeveloperName </members>

        <name>CMSConnectSource</name>

      </types>

      <version>43.0</version>

   </Package>

```

Usage

The INSERT or UPDATE logic for the incoming information is always UPSERT. If data isn’t in the entity, then it’s inserted, otherwise the
current data is updated.

Before doing upsert, the content from the package is validated against the maximum limits for the following:

**•** CSS assets <= 10

**•** JavaScript assets <= 10

**•** Resource types < =5

**•** Resource definitions for each type <=10

For example

**1.** The validation on a new connection totals only the elements in the incoming package.


Metadata Types CMSConnectSource

**2.** Validation of existing connections totals the existing assets and new elements to assess validity. For example, if a connection on the
destination org already has six CSS definitions, and the incoming package has defined seven CSS definitions (four new + three
existing), the new total is the six current from the database. The total ignores the three repeated in the package and adds four new
definitions from the incoming package. This totals 10 definitions, which number is at or below the 10 asset threshold, and it passes
validation.

Refer to the following content for more details for how each entity how is handled while saving the details from package to destination
org:


### Metadata Types Community (Zone)

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

[Select Components for an Outbound Change Set](https://help.salesforce.com/articleView?id=changesets_outbound_components_select.htm&type=5&language=en_US)

[View and Add Dependent Components to a Change Set](https://help.salesforce.com/articleView?id=changesets_outbound_dependencies.htm&type=5&language=en_US)

[Developer Guide: Deploying and Retrieving Metadata](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based.htm)

[Salesforce Help: Use Personalized Content in CMS Connect](https://help.salesforce.com/articleView?id=communities_cms_connect_personalization.htm&type=5&language=en_US)

[Developer Guide: Translations](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_translations.htm)

### Community (Zone)

Represents a zone that contains Ideas or Chatter Answers objects. Zones are shared by the Ideas, Answers, and Chatter Answers features,
allowing you to view and create zones from those locations.This type extends the Metadata metadata type and inherits its `fullName`
field.

Note: Starting with the Summer ’13 release, Chatter Answers and Ideas “communities” have been renamed to “zones.” In API
### version 28, the API object label has changed to Zone, but the API type is still Community .

File Suffix and Directory Location

Zones have the suffix `community` and are stored in the `communities` folder.

Version

### Community (Zone) components are available in API version 27.0 and later.

Fields

Note: When `enableChatterAnswers` is set to `false`, values specified for the following fields are ignored and not saved:
`communityFeedPage`, `emailFooterDocument`, `emailHeaderDocument`, `enablePrivateQuestions`,
`emailNotificationUrl`, and `site` .

**Field Name** **Field Type** **Description**

`active` boolean Indicates whether the zone is active ( `true` ) or not ( `false` ).

`chatterAnswersFacebookSsoUrl` string (Read only) The Facebook sign-on URL, which is based on the Facebook
authentication provider selected in your Chatter Answers settings. This

field is available only if Chatter Answers and Facebook Single Sign-On
for Chatter Answers are enabled.

`communityFeedPage` string The Visualforce page that hosts the zone’s feeds. This field is available
when Chatter Answers is enabled in the organization.


Metadata Types Community (Zone)

**Field Name** **Field Type** **Description**

`description` string The description of the zone.

`emailFooterDocument` string

`emailHeaderDocument` string

`emailNotificationUrl` string

`enableChatterAnswers` boolean

`enablePrivateQuestions` boolean

The text or HTML file that incorporates your organization’s branding into
the footer of email notifications. This field is available when Chatter
Answers is enabled in the organization.

The text or HTML file that incorporates your organization’s branding into
the header of email notifications. This field is available when Chatter
Answers is enabled in the organization.

The URL that’s included in email notifications. This field is available when
Chatter Answers is enabled in the organization. This field replaces
`portalEmailNotificationUrl` in API version 28.0 and later.

Indicates whether the zone has Chatter Answers enabled ( `true` ) or not
( `false` ). This field is available when Chatter Answers is enabled in the
organization.

Indicates whether Chatter Answers questions can be escalated to cases
( `true` ) or not ( `false` ). This field is available when Chatter Answers is
enabled in the organization.

`expertsGroup` string The name of the public group that act as experts in the zone. This field
is available when eitherIdeas or Answers are enabled in the organization.

`portal` string The name of the portal in which to display the zone.

`portalEmailNotificationUrl` string

The portal URL that’s included in email notifications. This field is available
when Chatter Answers is enabled in the organization. This field has been
replaced by `emailNotificationUrl` in API version 28.0 and later.

`reputationLevels` ReputationLevels The fields that define the points and name of each reputation level you
define. You can create up to 25 reputation levels per zone.

`showInPortal` boolean Indicates whether the zone is available to all portals ( `true` ) or not
available to any portals ( `false` ).

`site` string The name of the site for the zone. This field is available when Chatter
Answers is enabled in the organization.

ReputationLevels

Represents the points and reputation label that displays on hover over a user’s photo in the feed.

**Field Name** **Field Type** **Description**

`chatterAnswersReputationLevels` ChatterAnswersReputationLevel

[]

Contains the name and value pair that describes the
reputation level for Chatter Answers. Available in API version
28.0 and later.

`ideaReputationLevels` IdeaReputationLevel Contains the name and value pair that describes the
reputation for Ideas. Available in API version 28.0 and later.


Metadata Types Community (Zone)

ChatterAnswersReputationLevel

Represents the reputation name and the number of points for that level for Chatter Answers.

**Field Name** **Field Type** **Description**

`name` string The name of the reputation level, for example, “Expert.”

`value` int The minimum number of points for the reputation level.

IdeaReputationLevel

Represents the reputation name and the number of points for that level for Ideas. Available in API version 28.0 and later.

**Field Name** **Field Type** **Description**

`name` string The name of the reputation level, for example, “Expert.”

`value` int The minimum number of points for the reputation level.

Declarative Metadata Sample Definition

The following is the definition of a community (zone) component:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Community xmlns="http://soap.sforce.com/2006/04/metadata">

      <active>true</active>

      <communityFeedPage>communityWithHeaderAndFooter_main</communityFeedPage>

      <description>Metadata Test</description>

      <emailFooterDocument>sampleFolder/emailFooter.html</emailFooterDocument>

      <emailHeaderDocument>sampleFolder/emailHeader.html</emailHeaderDocument>

      <enableChatterAnswers>true</enableChatterAnswers>

      <enablePrivateQuestions>true</enablePrivateQuestions>

      <expertsGroup>CommunityExperts</expertsGroup>

      <portal>Customer Portal</portal>

      <emailNotificationUrl>http://yourURL</emailNotificationUrl>

   <reputationLevels>

        <chatterAnswersReputationLevels>

           <name>Newbie</name>

           <value>0</value>

        </chatterAnswersReputationLevels>

        <chatterAnswersReputationLevels>

           <name>Smartie</name>

           <value>500</value>

        </chatterAnswersReputationLevels>

        <chatterAnswersReputationLevels>

           <name>Pro</name>

           <value>2000</value>

        </chatterAnswersReputationLevels>

        <chatterAnswersReputationLevels>

           <name>All Star</name>

           <value>5000</value>

```


### Metadata Types CommerceSettings

```
        </chatterAnswersReputationLevels>

        <ideaReputationLevels>

           <name>Observer</name>

           <value>0</value>

        </ideaReputationLevels>

        <ideaReputationLevels>

           <name>Contributor</name>

           <value>100</value>

        </ideaReputationLevels>

        <ideaReputationLevels>

           <name>Influencer</name>

           <value>400</value>

        </ideaReputationLevels>

        <ideaReputationLevels>

           <name>Thought Leader</name>

           <value>1500</value>

        </ideaReputationLevels>

      </reputationLevels>

      <showInPortal>true</showInPortal>

      <site>ChatterAnswersSite</site>

   </Community>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### CommerceSettings

Represents settings for various Commerce features.

Parent Type and Manifest Access

This type extends the Metadata metadata type and inherits its `fullName` field.

In the package manifest, all the settings metadata types for the org are accessed using the “Settings” name. See Settings for more details.

File Suffix and Directory Location

### CommerceSettings values are stored in the Commerce.settings file in the settings folder. The .settings files are different

from other named components, because there’s only one settings file for each settings component.

Version

Commerce Settings are available in API version 50.0 and later.

Special Access Rules

A B2B Commerce or D2C Commerce license and access to Commerce objects is required.


Metadata Types CommerceSettings

Fields

**Field Name** **Description**

```
buyerGroupExtensibility

commerceAnalyticsEnabled

commerceAppEnabled

commerceConciergeEnabled

commerceCopilotEcomEnabled

commerceDCSegmentEnabled

commerceDiscoveryExpansion

commerceEnabled

```

**Field Type**
boolean

**Description**
Indicates whether Buyer Group Extensibility is enabled ( `true` ) or not ( `false` ).
Available in API version 64.0 and later.

**Field Type**
boolean

**Description**
Indicates whether Commerce Analytics is enabled ( `true` ) or not ( `false` ).

**Field Type**
boolean

**Description**
Indicates whether Commerce App is enabled ( `true` ) or not ( `false` ).

**Field Type**
boolean

**Description**
Indicates whether Commerce Concierge bots are enabled ( `true` ) or not ( `false` ).

**Field Type**
boolean

**Description**
Indicates whether Commerce Copilot is enabled ( `true` ) or not ( `false` ).

**Field Type**
boolean

**Description**
Indicates whether the Data 360 segment integration is enabled ( `true` ) or not ( `false` ).

**Field Type**
boolean

**Description**
Indicates whether the Commerce Discovery Expansion service is enabled ( `true` ) or
not ( `false` ).

**Field Type**
boolean


Metadata Types CommerceSettings

**Field Name** **Description**

**Description**
Indicates whether Commerce is enabled ( `true` ) or not ( `false` ).

```
commerceNGPEnabled

commerceRLMSubs

generateInvPerSubscription

lowestUnitPriceTracking

messagingEngagementDataKit

```

**Field Type**
boolean

**Description**
Indicates whether NGP (“Salesforce”) Pricing is enabled ( `true` ) or not ( `false` ).

**Field Type**
boolean

**Description**
Indicates whether Commerce Revenue Lifecycle Management Subscriptions is enabled
( `true` ) or not ( `false` ).

**Field Type**
boolean

**Description**
Indicates whether a separate invoice is generated per subscription ( `true` ) or not
( `false` ). Available in API version 64.0 and later.

**Field Type**
boolean

**Description**
Indicates whether lowest unit price tracking (for EU customers) is enabled ( `true` ) or
not ( `false` ).

**Field Type**
boolean

**Description**
Indicates whether Message Engagement data kit is enabled ( `true` ) or not ( `false` ).
Message Engagement data kit is a Data 360 data model object (DMO) for a user’s
engagement with a marketing message.

Declarative Metadata Sample Definition

The following is an example of a CommerceSettings component.

```
<?xml version="1.0" encoding="UTF-8"?>

<CommerceSettings xmlns="http://soap.sforce.com/2006/04/metadata">

 <buyerGroupExtensibility>false</buyerGroupExtensibility>

 <commerceAnalyticsEnabled>false</commerceAnalyticsEnabled>

 <commerceAppEnabled>false</commerceAppEnabled>

 <commerceConciergeEnabled>false</commerceConciergeEnabled>

 <commerceCopilotEcomEnabled>false</commerceCopilotEcomEnabled>

```


### Metadata Types CommunityTemplateDefinition

```
    <commerceDCSegmentEnabled>false</commerceDCSegmentEnabled>

    <commerceDiscoveryExpansion>false</commerceDiscoveryExpansion>

    <commerceEnabled>false</commerceEnabled>

    <commerceNGPEnabled>false</commerceNGPEnabled>

    <commerceRLMSubs>false</commerceRLMSubs>

    <generateInvPerSubscription>false</generateInvPerSubscription>

    <lowestUnitPriceTracking>false</lowestUnitPriceTracking>

    <messagingEngagementDataKit>false</messagingEngagementDataKit>

   </CommerceSettings>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>Commerce</members>

        <name>Settings</name>

      </types>

      <version>64.0</version>

   </Package>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The wildcard
applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the manifest
file, see Deploying and Retrieving Metadata with the Zip File.

### CommunityTemplateDefinition

Represents the definition of an Experience Builder site template. This type extends the Metadata metadata type and inherits its `fullName`
field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### CommunityTemplateDefinition components have the suffix .communityTemplateDefinition and are stored in the

`communityTemplateDefinitions` folder.

Version

### CommunityTemplateDefinition components are available in API version 38.0 and later.

Special Access Rules

This type is available only if Salesforce Digital Experiences is enabled in your org.


Metadata Types CommunityTemplateDefinition

Fields

**Field Name** **Field Type** **Description**

Denotes that this CommunityTemplateDefinition was created in API
version 41.0 or later. The only valid value is `c` . This field is available in
API 41.0 and later.

```
baseTemplate

```

CommunityBase
Template
(enumeration of
type string)

`bundlesInfo` CommunityTemplateBundleInfo[] The list of preview images and feature highlights of this
CommunityTemplateDefinition.

```
category

```

CommunityTemplate Required. The optimized use case of this CommunityTemplateDefinition.
Category Valid values are:
(enumeration of

**•** `Commerce`

type string)

**•** `Commerce`

**•** `IT`

`defaultBrandingSet` string

**•** `Marketing`

**•** `Sales`

**•** `Service`

The set of branding properties associated with this
CommunityTemplateDefinition, as defined in the Theme panel in
Experience Builder. Available in API version 40.0 and later.

In API version 44.0 and later, this field is read-only and can be
implemented in CommunityThemeDefinition on page 608.

`defaultThemeDefinition` string Required. The assigned theme definition for this
CommunityTemplateDefinition.

`description` string The optional description text of this CommunityTemplateDefinition.

`enableExtendedCleanUp` boolean False by default. Determines if deleting this
`OnDelete` CommunityTemplateDefinition attempts to delete other directly or
indirectly referenced objects automatically, for example,
CommunityThemeDefinition on page 608, Flexipage on page 1189, or
StaticResource on page 2327. Values are true or false.

`masterLabel` string Required. The label for this CommunityTemplateDefinition, which displays
in Setup.

`navigationLinkSet` NavigationLinkSet The navigation menu associated with this CommunityTemplateDefinition.
A navigation menu consists of items that users can click to go to other

parts of the site. Available in API versions 37.0 to 46.0. In API versions
47.0 and later, use NavigationMenu.

`pageSetting` CommunityTemplatePageSe **t** ing[] The list of FlexiPage of this CommunityTemplateDefinition.

`publisher` string

Defines the name of the publisher as seen in the Change Theme wizard.
If no name is provided, the name of the org from which the package
was originally exported is used.

This field is available in API version 45.0 and later.


Metadata Types CommunityTemplateDefinition

CommunityTemplateBundleInfo

**Field Name** **Field Type** **Description**

`description` string The optional description text of its CommunityTemplateBundleInfo.

`image` string Required only when the `type` is `PreviewImage`, otherwise this field is
optional. A preview image for this CommunityTemplateDefinition.

`order` int Required. An integer specifying the position of this
CommunityTemplateBundleInfo relative to others of the same `type` within

its CommunityTemplateDefinition. `1` is the first position, `3` is the maximum
position for `PreviewImage` type, and `4` is the maximum position for the
`Highlight` type.

`title` string Required. The title of this CommunityTemplateBundleInfo to use in code.

Required. Stores descriptive information about the template that’s included in
the export. The template powers the interface of the Experience Creation
Wizard. Valid values are:

**•** `Highlight` —This CommunityTemplateBundleInfo is used as a
highlighted feature. Up to 4 are supported.

**•** `PreviewImage` —This CommunityTemplateBundleInfo is used as a
preview image. Up to 3 are supported.

```
type

```

CommunityTemplate
BundleInfoType
(enumeration of type
string)

CommunityTemplatePageSetting

**Field Name** **Field Type** **Description**

`page` string Required. The list of FlexiPage of this CommunityTemplateDefinition.

`themeLayout` string

Required. The name of the FlexiPage for the theme layout.

This field is available in API version 39.0 and later.

Declarative Metadata Sample Definition

The following is an example of a CommunityTemplateDefinition component.

```
<?xml version="1.0" encoding="UTF-8"?>

<CommunityTemplateDefinition xmlns="http://soap.sforce.com/2006/04/metadata">

   <baseTemplate>c</baseTemplate>

   <bundlesInfo>

     <description>Feature Description</description>

     <order>1</order>

     <title>Feature Heading</title>

     <type>Highlight</type>

   </bundlesInfo>

   <bundlesInfo>

     <image>siteAsset_2dbe594eb6794173af78da264cd6a4a7</image>

```


Metadata Types CommunityTemplateDefinition

```
        <order>1</order>

        <title>Preview Image</title>

        <type>PreviewImage</type>

      </bundlesInfo>

      <category>Sales</category>

      <defaultThemeDefinition>communityTemplate</defaultThemeDefinition>

      <description>This is an Experience Builder template</description>

      <enableExtendedCleanUpOnDelete>true</enableExtendedCleanUpOnDelete>

      <masterLabel>communityTemplate</masterLabel>

      <navigationLinkSet>

        <navigationMenuItem>

           <label>Topics</label>

           <position>0</position>

           <publiclyAvailable>true</publiclyAvailable>

           <target>ShowMoreTopics</target>

           <type>NavigationalTopic</type>

        </navigationMenuItem>

      </navigationLinkSet>

      <pageSetting>

        <page>communityTemplate_Report_List</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Topic_Catalog</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Check_Password</page>

        <themeLayout>communityTemplate_themeLayout_Login</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Error</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_User_Settings</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Login</page>

        <themeLayout>communityTemplate_themeLayout_Login</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Stream_List</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Sfdc_Page</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Group_Detail</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

```


Metadata Types CommunityTemplateDefinition

```
      <pageSetting>

        <page>communityTemplate_Report_Related_List</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Register</page>

        <themeLayout>communityTemplate_themeLayout_Login</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_User_Profile</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Case_Detail</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Stream_Related_List</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Dashboard_Detail</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Group_List</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Canvasapp_Page</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Login_Error</page>

        <themeLayout>communityTemplate_themeLayout_Login</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Create_Record</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Group_Related_List</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Search</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_File_Detail</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Case_List</page>

```


Metadata Types CommunityTemplateDefinition

```
        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_User_List</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_File_List</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Question_Detail</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Dashboard_List</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Related_Record_List</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_File_Related_List</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Record_List</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Forgot_Password</page>

        <themeLayout>communityTemplate_themeLayout_Login</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Home</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Dashboard_Related_List</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Account_Management</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Case_Related_List</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_User_Related_List</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

```


### Metadata Types CommunityThemeDefinition

```
      <pageSetting>

        <page>communityTemplate_Stream_Detail</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Topic_Detail</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Messages</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Report_Detail</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Record_Detail</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Feed_Detail</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Contact_Support</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

   </CommunityTemplateDefinition>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>MyTemplate</members>

        <name>CommunityTemplateDefinition</name>

      </types>

      <version>66.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### CommunityThemeDefinition

Represents the definition of a theme for an Experience Builder site. This type extends the Metadata metadata type and inherits its
`fullName` field.


Metadata Types CommunityThemeDefinition

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

CommunityThemeDefinition components have the suffix `.communityThemeDefinition` and are stored in the
`communityThemeDefinitions` folder.

Version

CommunityThemeDefinition components are available in API version 38.0 and later.

Special Access Rules

This type is available only if Salesforce Digital Experiences is enabled in your org.

Fields

**Field Name** **Field Type** **Description**

`bundlesInfo` CommunityThemeBundleInfo[]

If specified, at least one preview image and one highlight are required.
Up to 3 preview images and 4 highlights are supported. Available in API
version 44.0 and later

`customThemeLayoutType` CommunityCustomThemeLayoutType[] The list of custom theme layout types available to the theme layout.

`defaultBrandingSet` string

The set of branding properties associated with this
CommunityThemeDefinition, as defined in the Theme panel in Experience
Builder. Available in API version 44.0 and later.

`description` string The optional description text of this CommunityThemeDefinition.

`enableExtendedCleanUp` boolean

```
OnDelete

```

False by default. Determines if deleting this CommunityThemeDefinition
attempts to delete other directly or indirectly referenced objects
automatically, for example, FlexiPage. Values are true or false.

`masterLabel` string Required. The label for this CommunityThemeDefinition, which displays
in Setup.

`publisher` string

Defines the name of the publisher as seen in the wizard for creating
Experience Builder sites. If no name is provided, the name of the org
from which the package was originally exported is used.

This field is available in API version 45.0 and later.

`themeRouteOverride` CommunityThemeRouteOve **r** ide[] List of theme layout type overrides for flexipages (currently only for
home). Available in API version 44.0 and later.

`themeSetting` CommunityTheme Required. The list of settings for this CommunityThemeDefinition.
Setting []


Metadata Types CommunityThemeDefinition

CommunityThemeBundleInfo

**Field Name** **Field Type** **Description**

`description` string The optional description text of its CommunityThemeBundleInfo.

`image` string Required only when the `type` is `PreviewImage`, otherwise this field is
optional. A preview image for this CommunityThemeDefinition.

`order` int Required. An integer specifying the position of this
CommunityThemeBundleInfo relative to others of the same `type` within its

CommunityThemeDefinition. `1` is the first position, `3` is the maximum position
for `PreviewImage` type, and `4` is the maximum position for the
`Highlight` type.

`title` string Required. The title of this CommunityThemeBundleInfo to use in code.

```
type

```

CommunityTemplate Required. Stores descriptive information about the theme that is included in
BundleInfoType the export. Valid values are:
(enumeration of type

**•** `Highlight` —This CommunityThemeBundleInfo is used as a highlighted

string)

feature. Up to 4 are supported.

**•** `PreviewImage` —This CommunityThemeBundleInfo is used as a preview
image. Up to 3 are supported.

CommunityCustomThemeLayoutType

**Field Name** **Field Type** **Description**

`description` string The description of the custom theme layout type.

`label` string Required. The name of the custom theme layout type. The values `Inner`,
`Home`, and `Login` are reserved.

CommunityThemeRouteOverride

**Field Name** **Field Type** **Description**

`customThemeLayoutType` string

Required when `themeLayoutType` isn’t specified. Provides the custom
theme layout type associated with the theme layout. This field and
`themeLayoutType` are mutually exclusive; you can’t specify both.

`pageAttributes` string Required. Specifies the attributes of the site page for which the default theme
layout type is overridden. The only valid value is `{"PageName":"Home"}` .

`pageType` string

Required. Specifies the type of the site page for which the default theme layout
type is overridden. The only valid value is `comm__standardPage` .


Metadata Types CommunityThemeDefinition

**Field Name** **Field Type** **Description**

```
themeLayoutType

```

CommunityTheme Required if `customThemeLayoutType` isn’t specified. Provides the default
LayoutType theme layout type associated with the theme layout. Valid values are `Inner`,
(enumeration of type `Home`, or `Login` . This field and `customThemeLayoutType` are mutually
string) exclusive; you can’t specify both.

CommunityTheme Setting

**Field Name** **Field Type** **Description**

`customThemeLayoutType` string

Required when `themeLayoutType` isn’t specified. The custom theme
layout type associated with the theme layout. This field and
`themeLayoutType` are mutually exclusive; you can’t specify both.

`themeLayout` string Required. The configuration and layout for this theme.

```
themeLayoutType

```

CommunityTheme Required when `customThemeLayoutType` isn’t specified. The default
LayoutType theme layout type associated with the theme layout. Valid values are `Inner`,
(enumeration of type `Home`, or `Login` . This field and `customThemeLayoutType` are mutually
string) exclusive; you can’t specify both.

Declarative Metadata Sample Definition

The following is an example of a CommunityThemeDefinition component.

```
<?xml version="1.0" encoding="UTF-8"?>

<CommunityThemeDefinition xmlns="http://soap.sforce.com/2006/04/metadata">

   <bundlesInfo>

     <description>Batman Feature1 description</description>

     <order>1</order>

     <title>Batman Feature1</title>

     <type>Highlight</type>

   </bundlesInfo>

   <bundlesInfo>

     <image>siteAsset_d90e2d5ce4cf4d8899e233c051091246</image>

     <order>1</order>

     <title>siteAsset_d90e2d5ce4cf4d8899e233c051091246</title>

     <type>PreviewImage</type>

   </bundlesInfo>

   <defaultBrandingSet>Batman</defaultBrandingSet>

   <description>Batman theme</description>

   <enableExtendedCleanUpOnDelete>true</enableExtendedCleanUpOnDelete>

   <masterLabel>Batman</masterLabel>

   <themeRouteOverride>

     <pageAttributes>{&quot;PageName&quot;:&quot;Home&quot;}</pageAttributes>

     <pageType>comm__standardPage</pageType>

     <themeLayoutType>Home</themeLayoutType>

   </themeRouteOverride>

   <themeSetting>

     <themeLayout>Batman_themeLayout_Login</themeLayout>

```


### Metadata Types ConnectedApp

```
        <themeLayoutType>Login</themeLayoutType>

      </themeSetting>

      <themeSetting>

        <themeLayout>Batman_themeLayout_Home</themeLayout>

        <themeLayoutType>Home</themeLayoutType>

      </themeSetting>

      <themeSetting>

        <themeLayout>Batman_themeLayout_Default</themeLayout>

        <themeLayoutType>Inner</themeLayoutType>

      </themeSetting>

   </CommunityThemeDefinition>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>Batman</members>

        <name>BrandingSet</name>

      </types>

      <types>

        <members>Batman</members>

        <name>CommunityThemeDefinition</name>

      </types>

      <types>

        <members>Batman_themeLayout_Default</members>

        <members>Batman_themeLayout_Home</members>

        <members>Batman_themeLayout_Login</members>

        <name>FlexiPage</name>

      </types>

      <types>

        <members>siteAsset_d90e2d5ce4cf4d8899e233c051091246</members>

        <name>StaticResource</name>

      </types>

      <version>66.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### ConnectedApp

Represents a connected app configuration. A connected app enables an external application to integrate with Salesforce using APIs and
standard protocols, such as SAML, OAuth, and OpenID Connect. Connected apps use these protocols to authenticate, authorize, and
provide single sign-on (SSO) for external apps. The external apps that are integrated with Salesforce can run on the customer success
platform, other platforms, devices, or SaaS subscriptions.

This type extends the Metadata metadata type and inherits its `fullName` field.


Metadata Types ConnectedApp

Important: Connected apps creation is restricted as of Spring ‘26. You can use existing connected apps during and after Spring
[‘26. However, we recommend using external client apps instead. If you must continue creating connected apps, contact Salesforce](https://help.salesforce.com/s/articleView?id=xcloud.external_client_apps.htm&language=en_US)
Support.

[See New connected apps can no longer be created in Spring ‘26 for more details.](https://help.salesforce.com/s/articleView?id=005228017&type=1&language=en_US)

File Suffix and Directory Location

ConnectedApp components have the suffix `.connectedApp` and are stored in the `connectedApps` folder.

Version

ConnectedApp components are available in API version 29.0 and later.

Fields

**Field Name** **Field Type** **Description**

`attributes` `canvasConfig` A custom attribute of the connected app.

AppCanvasConfig The configuration options of the connected app if it's exposed as a
canvas app.

`contactEmail` string Required. The email address that Salesforce uses to contact you or
your support team.

`contactPhone` string The phone number for Salesforce to use to contact you.

`description` string An optional description for your app.

`iconUrl` string Reserved for future use.

`infoUrl` string An optional URL for a web page with more information about your
app.

`ipRanges` ConnectedAppIpRange[] Specifies the ranges of IP addresses that can access the app without
requiring the user to authenticate with the connected app.

`label` string Required. The name of the app.

`logoUrl` string An optional logo for the app. The logo appears with the app’s entry
in the list of apps and on the consent page the user sees when

authenticating. The URL must use HTTPS, and the logo can't be larger
than 125 pixels high or 200 pixels wide. The default logo is a cloud.

`mobileStartUrl` string Users are directed to this URL after they've authenticated when the
app is accessed from a mobile device. If you don't give a URL, the user

is sent to the app’s default start page after authentication completes.
If the connected app that you’re creating is a canvas app, then you
can leave this field blank. The Canvas App URL field contains the URL
that gets called for the connected app.

`oauthConfig` connectedAppOauthConfig Specifies how your app communicates with Salesforce.


Metadata Types ConnectedApp

**Field Name** **Field Type** **Description**

`oauthPolicy` ConnectedAppOauthPolicy Specifies OAuth access policies associated with your connected app.
Available in API version 49.0 and later.

`permissionSetName` string

`plugin` string

Specifies the permissions required to perform different functions with
the connected app. Available in API version 46.0 and later.

You can assign multiple permission sets to the connected app, but
you must enter each permission set name on a separate line. You can’t

enter the same permission set name more than one time for each
connected app.

You can also change a permission set by replacing the current
permission set with a new permission set. Make sure that each
permission set name assigned to the connected app is unique.

You can delete individual permission sets or remove all permission
sets from a connected app by entering an empty
`permissionSetName` string on deployment of the connected
app: ( `<permissionSetName></permissionSetName>` ).

To use this field, the `isAdminApproved` field on the
ConnectedAppOauthConfig subtype must be set to `true` .

The name of a custom Apex class that extends
`Auth.ConnectedAppPlugin` to customize the behavior of the
app.

`pluginExecutionUser` string Specifies the user to run the plugin as. If the user isn’t authorized to
use the connected app, use the `authorize` method. See the

`ConnectedAppPlugin` [class in the Apex Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_namespace_Auth.htm)
Available in API version 46.0 and later.

Enter a user that is part of your org. Otherwise, the user is removed
from this field when you deploy the connected app. If you don’t want
to specify a user, you can leave this field empty.

To use this field in an org, the ConAppPluginExecuteAsUser setting
must be enabled.

`profileName` string[]

Specifies the profile (base-level user permissions) required to perform
different functions with the connected app. Available in API version
46.0 and later.

You can assign multiple profiles to the connected app, but you must
enter each profile name on a separate line. You can’t enter the same
profile name more than one time for each connected app.

You can also change profiles by replacing the current profiles with
new profiles. Make sure that each profile name assigned to the
connected app is unique.

You can also delete individual profiles or remove all profiles from a
connected app by entering an empty `profileName` string on


Metadata Types ConnectedApp

**Field Name** **Field Type** **Description**

deployment of the connected app:
( `<profileName></profileName>` ).

To use this field, the `isAdminApproved` field on the
ConnectedAppOauthConfig subtype must be set to `true` .

`samlConfig` ConnectedAppSamlConfig Controls how the app uses single sign-on.

`sessionPolicy` ConnectedAppSessionPolicy Specifies a connected app’s session policies. Available in API version
49.0 and later.

`startUrl` string If the app isn’t accessed from a mobile device, users are directed to
this URL after they've authenticated. If you don't give a URL, the user

is sent to the app’s default start page after authentication completes.
Whether you give a URL or not, the start URL can be updated later by
managing the connected app. If the app is accessed from a mobile
device, see `mobileStartUrl` . If the connected app that you’re
creating is a canvas app, then you can leave this field empty. The
Canvas App URL field contains the URL that gets called for the
connected app.

ConnectedAppAttribute

Represents the field names that make up a custom attribute when using SAML with a ConnectedApp. Customize these values to a
specific service provider.

**Field Name** **Field Type** **Description**

`formula` string Required. The value of the attribute.

`key` string Required. The attribute's identifier.

ConnectedAppCanvasConfig

Represents the configuration options of the connected app if it's exposed as a canvas app.

**Field Name** **Field Type** **Description**

`accessMethod` AccessMethod (enumeration of Required. Indicates how the canvas app initiates the OAuth
type string) authentication flow. The valid values are:

**•** `Get` —OAuth authentication is used, and the user is prompted to
allow the third-party application to access their information. When
you use this access method, the canvas app must initiate the OAuth
authentication flow.

**•** `Post` —OAuth authentication is used, but when the administrator
installs the canvas app, they implicitly allow access for users.
Therefore, the user isn’t prompted to allow the third party to access


Metadata Types ConnectedApp

**Field Name** **Field Type** **Description**

their user information. When you use this access method, the
authentication is posted directly to the canvas app URL.

`canvasUrl` string Required. The URL of the third-party app that's exposed as a canvas
app.

`lifecycleClass` string

The name of the `Canvas.CanvasLifecycleHandler` Apex
class, if you've implemented this class for custom parameters.

Available in API version 31.0 and later.

`locations` CanvasLocationOptions Indicates where the canvas app can appear to the user. The valid values
(enumeration of type string)[] are:

**•** `Aura` —The canvas app can appear in a custom Lightning
component.

**•** `AppLauncher` —Reserved for future use.

**•** `Chatter` —The canvas app can appear in the app navigation
list on the Chatter tab in Salesforce Classic.

**•** `ChatterFeed` —The canvas app can appear as a Chatter feed
item.

**•** `MobileNav` —The canvas app can appear in a mobile card in
the Salesforce mobile app. Available in API version 31.0 and later.

**•** `None` —The canvas app can appear only in the Canvas App
Previewer.

**•** `OpenCTI` —The canvas app can appear in the call control tool
in Salesforce Classic.

**•** `PageLayout` —The canvas app can appear on a page layout.
When viewed in the Salesforce mobile app, the canvas app appears
in the record detail page. Available in API version 31.0 and later.

**•** `Publisher` —The canvas app can appear as a global action.

**•** `ServiceDesk` —The canvas app can appear in the footer or
sidebars of a console in Salesforce Classic.

**•** `UserProfile` —Reserved for future use.

**•** `Visualforce` —The canvas app can appear on a Visualforce
page.

`options` CanvasOptions (enumeration of
type string)[]

Indicates whether to hide the **Share** button and header in the publisher
for your canvas app and whether the app is a canvas personal app.
Valid values are:

**•** `HideShare` —The **Share** button is hidden in the publisher for
the related canvas app. Available in API version 30.0 and later.

**•** `HideHeader` —The header is hidden in the publisher for the
related canvas app. Available in API version 30.0 and later.

**•** `PersonalEnabled` —End users can install the app as a canvas
personal app. Available in API version 32.0 and later.


Metadata Types ConnectedApp

**Field Name** **Field Type** **Description**

`samlInitiationMethod` SamlInitiationMethod If you're using SAML single sign-on (SSO), indicates which provider
(enumeration of type string) initiates the SSO flow.

**•** `IdpInitiated` —Identity provider initiated. Salesforce makes
the initial request to start the SSO flow.

**•** `SpInitiated` —Service provider initiated. The canvas app starts
the SSO flow after it's invoked.

**•** `None` —The canvas app isn't using SAML SSO. Available in API
version 31.0 and later.

ConnectedAppIpRange

Represents the list of IP addresses that can access the app without requiring the user to authenticate.

**Field Name** **Field Type** **Description**

`description` string Identifies the purpose of the range, such as which part of a network
corresponds to this range. Available in API version 31.0 and later.

`end` string Required. The last address in the IP range, inclusive.

`start` string Required. The first address in the IP range, inclusive.

ConnectedAppOauthConfig

Represents the field names that configure how your connected app communicates with Salesforce.

**Field Name** **Field Type** **Description**

`assetTokenConfig` connectedAppOauthAssetToken The OAuth asset token configuration for the connected app OAuth
settings. Available in API version 49.0 and later.

`callbackUrl` string Required. The endpoint that Salesforce calls back to your connected
app during OAuth. It’s the OAuth `redirect_uri` .

`certificate` string The PEM-encoded certificate string, if the app uses a certificate.

`consumerKey` string

A value used by the consumer for identification to Salesforce. Referred
to as `client_id` in OAuth 2.0.

In API version 32.0 and later, you can set this field’s value only during
creation. After you define and save the value, it can’t be edited. The

value must be alphanumeric, can’t contain special characters or spaces,
and must be between 8–256 characters. Consumer keys must be
globally unique.

`consumerSecret` string A value that is combined with the `consumerKey` and used by the
consumer for identification to Salesforce. Referred to as

`client_secret` in OAuth 2.0. Typically, Salesforce generates this


Metadata Types ConnectedApp

**Field Name** **Field Type** **Description**

value when you create the connected app. However, you can customize
the shared secret value during creation. After you save the value, it
can’t be edited. When set, the value isn’t returned in Metadata API
requests.

The value must be alphanumeric (no special characters and no spaces)
and a minimum of 8 characters (maximum of 256 characters). If you
specify a secret already in use for another connected app in the
organization, an error occurs.

Available in API version 32.0 and later.

`idTokenConfig` ConnectedAppOauthIdToken Specifies the ID token configuration for the connected app OAuth
settings. Available in API version 43.0 and later.

`isAdminApproved` boolean

`isClientCredentialEnabled` boolean

If set to `false` (default), anyone in the org can authorize the app.
Users must approve the app the first time they access it.

If set to `true`, only users with the appropriate profile or permission
set can access the app. These users don’t have to approve the app

before they can access it. Manage profiles for the app by editing each
profile’s Connected App Access list. Manage permission sets for the
app by editing each permission set’s Assigned Connected App list. This
setting isn’t available in Group Edition. Available in API version 46.0
and later.

Connected app consumers can edit this setting when deploying a
connected app in their org.

If set to `true`, the connected app can use the OAuth 2.0 client
credentials flow. To use the client credentials flow, you must also specify
a user for `oauthClientCredentialUser` .

If set to `false` (default), the connected app can’t use the client
credentials flow.

Available in API version 56.0 and later.

`isCodeCredentialEnabled` boolean Determines whether the app can use the Authorization Code and
Credentials Flow to provide identity services to headless, off-platform

apps. The Authorization Code and Credentials Flow is the foundation
of headless login, headless registration, headless passwordless login,
and headless guest identity.

If set to `true`, the connected app can use the Authorization Code and
Credentials Flow and all associated Headless Identity features. The
default value is `false` .

This field is available in API version 57.0 and later.

`isCodeCredentialPostOnly` boolean For the Authorization Code and Credentials Flow, determines whether
the user’s credentials must be sent in the body of the initial HTTPS POST


Metadata Types ConnectedApp

**Field Name** **Field Type** **Description**

request to the Salesforce authorization endpoint. Requiring the
credentials in the POST body instead of in the header improves security.

If set to `true`, the user’s credentials must be included in the POST
body. The default value is `false` .

This field is available in API version 57.0 and later.

`isConsumerSecretOptional` boolean

`isIntrospectAllTokens` boolean

`isNamedUserJwtEnabled` boolean

If set to `false` (default), the connected app’s client secret is required
in exchange for an access token in the OAuth 2.0 web server flow.

If the client app can’t keep the client secret confidential and it must
use the web server flow, set to `true` . A client secret is still generated

for the connected app, but this setting instructs the web server flow
not to require the `client_secret` parameter in the access token
request. We recommend the user agent flow as a more secure option
than web server flow without the secret. Available in API version 49.0
and later.

If set to `true`, authorizes the connected app to introspect all access
and refresh tokens within the entire org.

If set to `false` (default), the connected app can introspect its own
tokens. In addition, an OAuth client that directly registers OAuth 2.0

connected apps through the dynamic client registration endpoint can
check the tokens for itself and its registered apps. Available in API
version 49.0 and later.

If set to `true`, the connected app is enabled to issue JSON Web Token
(JWT)-based access tokens.

This field is generally available in API version 59.0 and later.

`isPkceRequired` boolean Determines whether the Proof Key for Code Exchange (PKCE) extension
is required for variations of the OAuth 2.0 authorization code flow

configured for the connected app, including the web server flow and
Authorization Code and Credentials Flow. For public client apps that
can’t keep the consumer secret confidential, such as mobile apps, the
PKCE extension helps ensure that the client that initiates an
authorization flow is the same client that completes it. For this reason,
we always recommend implementing PKCE for public clients. We also
strongly recommend that you implement PKCE for private clients.

If set to `true`, the PKCE extension is required and any authorization
code flow variations that don’t implement it fail. If set to `false`, you
can still implement PKCE but it isn’t required. The default value is
`false` .

This field is available in API version 59.0 and later.

`isRefreshTokenRotationEnabled` boolean If set to `true`, the connected app issues a new refresh token each
time the OAuth refresh token flow is invoked. The old refresh token is


Metadata Types ConnectedApp

**Field Name** **Field Type** **Description**

automatically invalidated. If a user tries to use a previous refresh token
that’s been invalidated, the current refresh token and its associated
access tokens get deleted. If set to `false`, the refresh token can be
used to obtain multiple access tokens.

This field is available in API version 60.0 and later.

`isSecretRequiredForRefreshToken` boolean If set to `true` (default), the app’s client secret is required in the
authorization request of a refresh token and hybrid refresh token flow.

If set to `false` and an app sends the client secret in the authorization
request, Salesforce still validates it.

Select this option for web-server based apps that can protect client
secrets. For apps that can’t protect client secrets, such as mobile apps
or apps installed on a user’s computer, we recommend against selecting
this option. Available in API version 51.0 and later.

`isSecretRequiredForTokenExchange` boolean If set to `true`, the connected app must include its consumer secret
( `client_secret` ) in the token request during the OAuth 2.0 token

exchange flow. For security, set this field to `true` only if your app has
a private client backend where it can keep the secret safe. For public
client apps, such as single-page apps and mobile apps, set this field to
`false` and don’t include the consumer secret.

This field is available in API version 60.0 and later.

`isTokenExchangeEnabled` boolean

`oauthClientCredentialUser` string

If set to `true`, the connected app can use the OAuth 2.0 token
exchange flow to exchange tokens from an external identity provider
for Salesforce tokens.

This field is available in API version 60.0 and later.

The execution user for the OAuth 2.0 client credentials flow. Salesforce
returns access tokens on behalf of this user. This user must have the
API Only permission.

To use this field, set `isClientCredentialEnabled` to `true`
and specify a `consumerKey` .

Available in API version 56.0 and later.

`scopes` ConnectedAppOauthAccessScope The permissions given by the user running the connected app. When
(enumeration of type string)[] deploying metadata, valid values are:

**•** `Basic` —Allows access to your identity URL service (the same
behavior as deploying `Address`, `Email`, `Phone`, and
`Profile` ).

**•** `Api` —Allows access to the logged-in user's account over the APIs.

**•** `Web` —Allows use of the `access_token` on the web. This
usage also includes `visualforce`, allowing access to Visualforce
pages.


Metadata Types ConnectedApp

**Field Name** **Field Type** **Description**

**•** `Full` —Allows access to all data accessible by the logged-in user.

**•** `Chatter` —Allows access to only the Connect REST API resources.

**•** `CustomApplications` —Provides access to custom
applications, such as those using Visualforce.

**•** `RefreshToken` —Allows a refresh token to be returned if you’re
eligible to receive one (the same behavior as deploying
`OfflineAccess` ).

**•** `OpenID` —Allows access to the logged-in user's unique identifier
for OpenID Connect apps.

**•** `Profile` —Allows access to the logged-in user's profile (the
same behavior as deploying `Basic` ).

**•** `Email` —Allows access to the logged-in user's email address (the
same behavior as deploying `Basic` ).

**•** `Address` —Allows access to the logged-in user's street address
(the same behavior as deploying `Basic` ).

**•** `Phone` —Allows access to the logged-in user's phone number
value (the same behavior as deploying `Basic` ).

**•** `OfflineAccess` —Allows the app to interact with the user's
data while the user is offline and get a refresh token (the same
behavior as deploying `RefreshToken` ).

**•** `CustomPermissions` —Allows access to the custom
permissions in an organization associated with the connected app
and shows whether the current user has each permission enabled.

**•** `Wave` —Allows access to the Analytics REST API resources. Available
in API version 35.0 and later.

**•** `Eclair` —Allows access to the Analytics REST API Charts Geodata
resource. Available in API version 35.0 and later.

**•** `Pardot` —Allows access to Pardot API services on behalf of the
user. The full extent of accessible services is managed by the Pardot
account. Available in API version 49.0 and later.

**•** `Lightning` —Allows hybrid apps to directly obtain Lightning
child sessions through the OAuth 2.0 hybrid app token flow and
hybrid app refresh token flow. Available in API version 51.0 and
later.

**•** `Content` —Allows hybrid apps to directly obtain content child
sessions through the OAuth 2.0 hybrid app token flow and hybrid
app refresh token flow. Available in API version 51.0 and later.

**•** `CDPIngest` —Allows access to Data Cloud ingest API services.
Customers use these API services to upload and maintain external
datasets in the Data 360. Available in API version 52.0 and later.

**•** `Chatbot` —Allows access to Einstein Bot API services. Available
in API version 54.0 and later.


Metadata Types ConnectedApp

**Field Name** **Field Type** **Description**

**•** `ForgotPassword` —Allows access to Headless Forgot Password
API. Assign to an internal integration user to get an access token
for authenticated requests to this API. Available in API version 57.0
and later.

**•** `UserRegistration` —Allows access to Headless Registration
API. Assign to an internal integration user to get an access token
for authenticated requests to this API. Available in API version 58.0
and later.

**•** `PwdlessLogin` —Allows access to Headless Passwordless Login
API. Assign to an internal integration user to get an access token
for authenticated requests to this API. Available in API version 59.0
and later.

When retrieving metadata, valid values are:

**•** `Api` —Allows access to the logged-in user’s account over the APIs.

**•** `Basic` —Allows access to the user’s identity URL service, and
includes `Address`, `Email`, `Phone`, and `Profile` .

**•** `Chatter` —Allows access to only the Connect REST API resources.

**•** `CustomApplications` —Allows access to custom
applications, such as those using Visualforce.

**•** `Full` —Allows access to all data accessible by the logged-in user.

**•** `OpenID` —Allows access to the logged-in user's unique identifier
for OpenID Connect apps.

**•** `CDPIngest` —Allows access to Data Cloud ingest API services.
Customers use these API services to upload and maintain external
datasets in the Data 360. Available in API version 52.0 and later.

**•** `Pardot` —Allows access to Pardot API services on behalf of the
user. The full extent of accessible services is managed by the Pardot
account. Available in API version 49.0 and later.

**•** `Lightning` —Allows hybrid apps to directly obtain Lightning
child sessions through the OAuth 2.0 hybrid app token flow and
hybrid app refresh token flow. Available in API version 51.0 and
later.

**•** `Content` —Allows hybrid apps to directly obtain content child
sessions through the OAuth 2.0 hybrid app token flow and hybrid
app refresh token flow. Available in API version 51.0 and later.

**•** `RefreshToken` —Allows a refresh token to be returned if you’re
eligible to receive one and is synonymous with allowing
`OfflineAccess` .

**•** `Wave` —Allows access to the Analytics REST API resources. Available
in API version 35.0 and later.

**•** `Eclair` —Allows access to the Analytics REST API Charts Geodata
resource. Available in API version 35.0 and later.


Metadata Types ConnectedApp

**Field Name** **Field Type** **Description**

**•** `Web` —Allows usage of the `access_token` on the web. This
usage also includes `visualforce`, allowing access to Visualforce
pages.

**•** `Chatbot` —Allows access to Einstein Bot API services. Available
in API version 54.0 and later.

**•** `ForgotPassword` —Allows access to Headless Forgot Password
API. Assign to an internal integration user to get an access token
for authenticated requests to this API. Available in API version 57.0
and later.

**•** `UserRegistration` —Allows access to Headless Registration
API. Assign to an internal integration user to get an access token
for authenticated requests to this API. Available in API version 58.0
and later.

**•** `PwdlessLogin` —Allows access to Headless Passwordless Login
API. Assign to an internal integration user to get an access token
for authenticated requests to this API. Available in API version 59.0
and later.

`singleLogoutUrl` string The single logout endpoint. This URL is the endpoint where Salesforce
sends a logout request when users log out of Salesforce.

ConnectedAppOauthAssetToken

Specifies an OAuth asset token configuration for the connected app OAuth settings. Available in API version 49.0 and later.

**Field Name** **Field Type** **Description**

`assetAudiences` string Required. The audience claim associated with the asset token payload.
This claim identifies who the JWT is intended for. Value is an array of

case-sensitive strings, each containing a `StringOrURI` value. An
audience is specified for each intended consumer of the asset token.

`assetIncludeAttributes` boolean

`assetIncludeCustomPerms` boolean

`assetSigningCertId` string

`assetValidityPeriod` int

Required. If set to `true` (default), custom attributes associated with
the connected app are included in the asset token payload. If set to
`false`, these attributes aren’t included.

Required. If set to `true` (default), custom permissions associated with
the connected app are included in the asset token payload. If set to
`false`, these permissions aren’t included.

Required. The ID of the JWT certificate’s signing secret. The certificate
size can’t exceed 4 KB. If it does, try using a DER encoded file to reduce
the size.

Required. The asset token’s validity period. The validity must be the
expiration time of the assertion within 3 minutes, expressed as the
number of seconds from 1970-01-01T0:0:0Z measured in UTC.


Metadata Types ConnectedApp

ConnectedAppOauthIdToken

Specifies the ID token configuration for the connected app OAuth settings. Available in API version 43.0 and later.

**Field Name** **Field Type** **Description**

`idTokenAudience` string The audiences that this ID token is intended for. The value is an array
of case-sensitive strings. If no audiences are specified, the OAuth

2.0 `client_id` of the relying party is returned as the default
audience. Otherwise, the other audiences are returned with the
`client_id` in the `aud` value.

`idTokenIncludeAttributes` boolean Indicates whether attributes are included in the ID token.

`idTokenIncludeCustomPerms` boolean Indicates whether custom permissions are included in the ID token.

`idTokenIncludeStandardClaims` boolean Indicates whether standard claims about the authentication event are
included in the ID token.

`idTokenValidity` int The length of time that the ID token is valid for after it’s issued. The
value can be from 1 to 720 minutes. The default is 2 minutes.

ConnectedAppOauthPolicy

Specifies OAuth access policies for the connected app. Available in API version 49.0 and later.

**Field Name** **Field Type** **Description**

`ipRelaxation` string Required. Specifies whether a user’s access to the connected app is
restricted by IP ranges. Valid options are:

**•** `ENFORCE` (default)—Enforces the IP restrictions configured for
the org, such as the IP ranges assigned to a user profile.

**•** `BYPASS_2FACTOR` —Allows a user running the app to bypass
the org’s IP restrictions when either of these conditions is true.

**–** The app has a list of allowed IP ranges and is using the web
server OAuth authorization flow. Requests coming from only
these IPs are allowed.

**–** The app doesn’t have a list of allowed IP ranges, but it uses the
web server authentication flow. And the user successfully
completes identity verification if accessing Salesforce from a
new browser or device.

**•** `BYPASS` —Allows a user to run this app without org IP restrictions.

**•** `ENFORCE_RELAXREFRESH` —Enforces the IP restrictions
configured for the org, such as the IP ranges assigned to a user
profile. However, this option bypasses these restrictions when the
connected app uses refresh tokens to get access tokens.


Metadata Types ConnectedApp

**Field Name** **Field Type** **Description**

`refreshTokenPolicy` string

Required. Specifies how long a refresh token is valid for.

If refresh tokens are provided, users can continue to access the
OAuth-enabled connected app without having to reauthorize when

the access token expires, as defined by the session timeout value. The
connected app exchanges the refresh token with an access token to
start a new session. The Refresh Token policy is evaluated only during
usage of the issued refresh token and doesn’t affect a user’s current
session. Refresh tokens are required only when a user’s session has
expired or isn’t available. For example, you set a refresh token policy
to expire the token after 1 hour. If a user uses the app for 2 hours, the
user isn’t forced to reauthenticate after 1 hour. However, the user is
required to authenticate again when the session expires and the client
attempts to exchange its refresh token for a new session.

Valid options are:

**•** `zero` —The refresh token is invalid immediately. The user can use
the current session (access token) already issued, but can’t obtain
a new session when the access token expires.

**•** `infinite` —The refresh token is used indefinitely, unless revoked
by the user or Salesforce admin. Default setting.

**•** `specific_lifetime:` _**`number`**_ `:` _**`HOURS, DAYS,`**_
_**`MONTHS`**_ —The refresh token is valid for a fixed amount of time.
For example, if the policy states
`specific_lifetime:1:DAYS`, the user can obtain new
sessions for only 24 hours.

**•** `specific_inactivity:` _**`number`**_ `:` _**`HOURS, DAYS,`**_
_**`MONTHS`**_ —The refresh token is valid as long as it’s been used
within the specified amount of time. For example, if set to
`specific_inactivity:7:DAYS`, and the refresh token
isn’t exchanged for a new session within seven days, the next
attempt to use the token fails. The expired token can’t generate
new sessions. If the refresh token is exchanged within seven days,
the token is valid for another seven days. The monitoring period
of inactivity also resets.

`singleLogoutUrl` string If single logout is enabled, specify the single logout URL. Salesforce
sends logout requests to this URL when users log out of Salesforce.

The single logout URL must be an absolute URL starting with
`https://` .

ConnectedAppSamlConfig

Specifies how an app uses single sign-on.


Metadata Types ConnectedApp

**Field Name** **Field Type** **Description**

`acsUrl` string Required. The assertion consumer service URL from the service provider.

`certificate` string The PEM-encoded certificate string, if the app uses a certificate.

`encryptionCertificate` string The name of the certificate to use for encrypting SAML assertions to
the service provider. This certificate is saved in the organization's

Certificate and Key Management list. Available in API version 30.0 and
later.

```
encryptionType

```

When Salesforce is the identity provider, the SAML configuration can
SamlEncryptionType
specify the encryption method used for encrypting SAML assertions

(enumeration of type string)

to the service provider. The service provider detects the encryption
method in the SAML assertion for decryption. Valid values are:

**•** `AES_128` —128–bit key

**•** `AES_256` —256–bit key

Available in API version 30.0 and later.

`entityUrl` string Required. The entity ID from your service provider.

`issuer` string

A URI that sends the SAML response. A service provider can use this
URI to determine which identity provider sent the response. Available
in API version 29.0 and later.

`samlIdpSLOBindingEnum` SamlIdpSLOBinding (enumeration The SAML HTTP binding type from the service provider used for single
of type string) logout. Available in API version 40.0 and later. Valid values are:

**•** `PostBinding`

**•** `RedirectBinding`

`samlNameIdFormat` SamlNameIdFormatType
(enumeration of type string)

Indicates the format the service provider (SP) requires for the user's
single sign-on identifier. Available in API version 29.0 and later. Valid
values are:

**•** `Unspecified` (default)—No format given.

**•** `EmailAddress` —Used if the subject type is the user's name
or a federation ID (an ID internal to the SP).

**•** `Persistent` —Used with the user ID and persistent ID subject
types.

**•** `Transient` —Used when the subject type is a custom attribute
and can change every time the user logs in.

`samlSigningAlgoType` SamlSigningAlgoType Indicates the signing algorithm applied to SAML requests and responses
(enumeration of type string) when Salesforce is the identity provider. The selected signing algorithm

is applied to both single sign-on and single logout responses from your
org. Available in API version 50.0 and later. Valid values are:

**•** `SHA1`

**•** `SHA256`


Metadata Types ConnectedApp

**Field Name** **Field Type** **Description**

`samlSloUrl` string The SAML single-logout endpoint of the connected app service provider
(SP). This endpoint is where SAML LogoutRequests and

LogoutResponses are sent when users log out of Salesforce. The SP
provides this endpoint. Available in API version 40.0 and later.

`samlSubjectCustomAttr` string

If the `samlSubjectType` is `CustomAttr`, include that custom
value here; otherwise, leave empty. Available in API version 29.0 and
later.

`samlSubjectType` SamlSubjectType (enumeration of Required. The single sign-on identifier for the user. Valid values are:
type string)

**•** `Username` —The user's Salesforce name.

**•** `FederationId` —The user's identifier at the service provider.
Get this value from the service provider.

**•** `UserId` —The user's 15-character Salesforce identifier.

**•** `PersistentID` —A persistent opaque identifier that is specific
to the identity provider and a service provider.

**•** `CustomAttr` —The identifier is taken from a custom field value
in `samlSubjectCustomAttr` .

ConnectedAppSessionPolicy

Specifies the configuration options for a connected app’s session policies. Use these policies to define how long a user’s session can last
before reauthenticating, to block user access to the connected app, or to require multi-factor authentication (MFA) to access the app.
Available in API version 49.0 and later.

**Field Name** **Field Type** **Description**

`policyAction` string If the High Assurance session security level is applied to the connected
app, specify associated high assurance action. Valid values are:

**•** `Block` —Makes the connected app inaccessible to your org’s
users. Blocking an app ends all current user sessions with the
connected app and prevents all new sessions.

**•** `RaiseSessionLevel` —Requires users to verify their identity
with multi-factor authentication when they log in to the connected
app. This setting applies to authorization flows that include a user
approval step for API logins. These flows are the OAuth 2.0 refresh
token flow, web server flow, and user-agent flow. All other flows,
such as the JSON Web Token (JWT) bearer token flow, don’t include
a user approval step. For flows without a user approval step, API
logins with the High Assurance session security level are blocked.

`sessionLevel` string

Applies the High Assurance session security level to the connected
app. This session level requires users to verify their identity with
multi-factor authentication when they log in to the connected app.


Metadata Types ConnectedApp

**Field Name** **Field Type** **Description**

`sessionTimeout` int The length of time the connected app’s session lasts. If you don’t set
a value, Salesforce uses the timeout value in the connected app user’s

profile. If the user’s profile doesn’t specify a timeout value, Salesforce
uses the timeout value in the org’s Session Settings.

Declarative Metadata Sample Definition

The following is an example of a ConnectedApp component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ConnectedApp xmlns="http://soap.sforce.com/2006/04/metadata">

      <attributes>

        <formula>$Api.Enterprise_Server_URL_100</formula>

        <key>test</key>

      </attributes>

      <attributes>

        <formula>$Api.Partner_Server_URL_60</formula>

        <key>test1</key>

      </attributes>

     <canvasConfig>

        <accessMethod>Get</accessMethod>

        <canvasUrl>https://salesforce.com</canvasUrl>

        <lifecycleClass>MyCanvasListener</lifecycleClass>

        <locations>Chatter</locations>

        <locations>Visualforce</locations>

        <locations>Aura</locations>

        <locations>Publisher</locations>

        <locations>ChatterFeed</locations>

        <locations>OpenCTI</locations>

        <locations>MobileNav</locations>

        <locations>PageLayout</locations>

        <options>HideShare</options>

        <options>HideHeader</options>

        <options>PersonalEnabled</options>

        <samlInitiationMethod>None</samlInitiationMethod>

      </canvasConfig>

      <canvas>

      <locationOptions>NONE</locationOptions>

      <samlInitiationMethod>None</samlInitiationMethod>

      <accessMethod>Get</accessMethod>

      <canvasOptions>PE</canvasOptions>

      <lifecycleClass>MyCanvasListener</lifecycleClass>

      <canvasUrl>https://salesforce.com</canvasUrl>

    </canvas>

      <contactEmail>example@salesforce.com</contactEmail>

      <contactPhone>1231231234</contactPhone>

      <description>Test App</description>

   <iconUrl>https://c1.sfdcstatic.com/content/dam/sfdc-docs/www/logos/salesforce-logo-cloud.png</iconUrl>

```


Metadata Types ConnectedApp

```
   <infoUrl>https://c1.sfdcstatic.com/content/dam/sfdc-docs/www/logos/salesforce-logo-cloud.png</infoUrl>

      <startUrl>https://www.salesforce.com</startUrl>

      <ipRanges>

        <end>000.0.0.1</end>

        <start>000.0.0.2</start>

    <description>Test</description>

      </ipRanges>

      <ipRanges>

        <end>000.0.0.1</end>

        <start>000.0.0.2</start>

    <description>Test1</description>

      </ipRanges>

      <label>TestApp</label>

   <logoUrl>https://c1.sfdcstatic.com/content/dam/sfdc-docs/www/logos/salesforce-logo-cloud.png</logoUrl>

      <profileName>Test</profileName>

      <permissionSetName>TestPermission</permissionSetName>

      <mobileStartUrl>http://www.mobile.com</mobileStartUrl>

      <mobileAppConfig>

        <applicationBinaryFile></applicationBinaryFile>

        <applicationBinaryFileName>test</applicationBinaryFileName>

        <applicationBundleIdentifier>testtest</applicationBundleIdentifier>

        <applicationIconFileName>test</applicationIconFileName>

    <applicationIconFile>test</applicationIconFile>

    <applicationFileLength>5</applicationFileLength>

        <applicationInstallUrl>https://salesforce.com</applicationInstallUrl>

        <devicePlatform>ios</devicePlatform>

        <deviceType>minitablet</deviceType>

        <minimumOsVersion>2</minimumOsVersion>

        <privateApp>true</privateApp>

        <version>2</version>

      </mobileAppConfig>

      <oauthConfig>

        <assetTokenConfig>

           <assetAudiences>http://asset.audience.com</assetAudiences>

           <assetIncludeAttributes>true</assetIncludeAttributes>

           <assetIncludeCustomPerms>true</assetIncludeCustomPerms>

           <assetSigningCertId>${cert.id}</assetSigningCertId>

           <assetValidityPeriod>1440</assetValidityPeriod>

        </assetTokenConfig>

        <callbackUrl>https://www.callback.com</callbackUrl>

        <!-- NOTE, TEST.orgId will get replaced with the org ID of the context org, so

   we will have a unique consumer key in every scratch org. -->

        <consumerKey>3MVG9AOp4kbriZOcnmoLmTrguy9ryzcLbBjoNY...${TEST.orgId}</consumerKey>

     <consumerSecret>3MVG9AOp4k...</consumerSecret>

     <certificate>3MVG9AOp4kbriZOInmoLmTrguy9ryzcLbBjoNY...</certificate>

        <scopes>Basic</scopes>

        <scopes>Chatter</scopes>

        <scopes>OpenID</scopes>

        <scopes>CustomPermissions</scopes>

     <singleLogoutUrl>https://www.logout.com</singleLogoutUrl>

```


Metadata Types ConnectedApp

```
        <isAdminApproved>false</isAdminApproved>

        <isConsumerSecretOptional>false</isConsumerSecretOptional>

        <isIntrospectAllTokens>false</isIntrospectAllTokens>

     <idTokenConfig>

     <idTokenAudience>https://idtoken.audience.com</idTokenAudience>

     <idTokenIncludeAttributes>true</idTokenIncludeAttributes>

     <idTokenIncludeCustomPerms>true</idTokenIncludeCustomPerms>

     <idTokenIncludeStandardClaims>true</idTokenIncludeStandardClaims>

     <idTokenValidity>20</idTokenValidity>

     </idTokenConfig>

      </oauthConfig>

      <oauthPolicy>

        <ipRelaxation>ENFORCE</ipRelaxation>

        <refreshTokenPolicy>infinite</refreshTokenPolicy>

        <singleLogoutUrl>https://www.logout.com</singleLogoutUrl>

      </oauthPolicy>

      <plugin>ConnectedAppPluginTest</plugin>

      <pluginExecutionUser>testuser@salesforce.com</pluginExecutionUser>

      <samlConfig>

        <acsUrl>http://www.acs.com</acsUrl>

        <encryptionType>AES_128</encryptionType>

    <encryptionCertificate>3MVG9AOp4kbriZOInmoLmTrguy9ryzcLbBjoNY...</encryptionCertificate>

    <certificate>3MVG9AOp4kbriZOInmoLmTrguy9ryzcLbBjoNY...</certificate>

    <samlSubjectCustomAttr>test</samlSubjectCustomAttr>

        <entityUrl>http://www.entity.com</entityUrl>

        <issuer>https://salesforce.com</issuer>

        <samlIdpSLOBindingEnum>RedirectBinding</samlIdpSLOBindingEnum>

        <samlNameIdFormat>Unspecified</samlNameIdFormat>

        <samlSloUrl>https://www.salesforce.com</samlSloUrl>

        <samlSubjectType>CustomAttribute</samlSubjectType>

      </samlConfig>

      <sessionPolicy>

        <policyAction>RaiseSessionLevel</policyAction>

        <sessionLevel>HIGH_ASSURANCE</sessionLevel>

        <sessionTimeout>720</sessionTimeout>

      </sessionPolicy>

   </ConnectedApp>

```

You can enter multiple callback URL values. At run time, Salesforce validates the callback URL specified by the app by matching it with
one of the values. You must separate each callback URL with line breaks. To enter a new line programmatically, use the `\r` line break
character.

Here's an example of a ConnectedApp component with multiple callback URLs.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ConnectedApp xmlns="http://soap.sforce.com/2006/04/metadata">

    <contactEmail>example@salesforce.com</contactEmail>

    <label>MyConnectedApp</label>

    <oauthConfig>

    <callbackUrl>https://example.com/callback1

   https://example.com/callback2

   https://example.com/callback3</callbackUrl>

    <consumerKey>3MVG9AOp4kbriZOcnmoLmTrguy9ryzcLbBjoNY...</consumerKey>

    <isAdminApproved>false</isAdminApproved>

```


### Metadata Types ContentAsset

```
    <isConsumerSecretOptional>false</isConsumerSecretOptional>

    <isIntrospectAllTokens>false</isIntrospectAllTokens>

    <isSecretRequiredForRefreshToken>true</isSecretRequiredForRefreshToken>

    <scopes>Full</scopes>

    <scopes>RefreshToken</scopes>

    </oauthConfig>

    <oauthPolicy>

    <ipRelaxation>ENFORCE</ipRelaxation>

    <refreshTokenPolicy>infinite</refreshTokenPolicy>

    </oauthPolicy>

   </ConnectedApp>

```

The following is an example package manifest used to deploy or retrieve the ConnectedApp metadata for an organization.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>PortalTestApp</members>

        <name>ConnectedApp</name>

      </types>

      <version>29.0</version>

   </Package>

```

Usage

If you're constructing a SAML-enabled connected app using Metadata API, and must set the `IdP-Initiated Login URL` for
your service provider, you have two options:

You can use the service provider app ID with the `app` parameter in the following format. This value is displayed in the Salesforce user
interface. From Setup, enter _`Connected Apps`_ in the Quick Find box, then select **Connected Apps**, then click the name of the
connected app to see its detail page.

```
   https:// <Salesforce_base_URL> /idp/login?app= <app_id>

```

Or, if you're configuring the connected app using Metadata API only, you can use the `apiName` parameter of the service provider app
in the following format. The `apiName` parameter is the `fullName` inherited from the Metadata type.

```
   https:// <Salesforce_base_URL> /idp/login?apiName= <fullName>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### ContentAsset

Represents the metadata for creating an asset file. Asset files enable a Salesforce file to be used for org setup and configuration purposes.
This type extends the MetadataWithContent metadata type and inherits its `content` and `fullName` fields.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.


Metadata Types ContentAsset

File Suffix and Directory Location

ContentAsset components have the suffix `.asset` and are stored in the `contentassets` folder.

Version

ContentAsset components are available in API version 38.0 and later.

Special Access Rules

The system prevents metadata retrieval if the total size of the asset’s file content exceeds 30 MB. All pre-existing limits for packaging
apply to asset files.

Fields

**Field Name** **Field Type** **Description**

```
format

```

ContentAssetFormat Describes the format of the asset file. Valid values are:
(enumeration of

**•** `Original` —A single asset file version.

type string)

**•** `Original` —A single asset file version.

**•** `ZippedVersions` —Contains multiple versions of the asset file.

`isVisibleByExternalUsers` boolean

Indicates whether unauthenticated users can see the asset file ( `true` )
or not ( `false` ). If not specified, the default value is `false` . This field
is available in API version 44.0 and later.

`language` string Required. The language of the asset file label.

`masterLabel` string Required. The label for the asset file record, which displays in Setup.

`originNetwork` string For deploys, the name of the Experience Cloud site the file is assigned
upon creation. For retrievals, the name of the Experience Cloud site the

file is assigned to appears in the field value. If `null`, the file wasn’t
assigned to an Experience Cloud site.

`relationships` ContentAssetRelationships The list of ContentAssetLinks that describe whether the asset file can be
shared with the org.

`versions` ContentAssetVersions Required. Captures basic information about the file version included the
asset metadata. Typically the file has only one version.

ContentAssetRelationships

Represents the relationships between an asset file and the locations it's linked with.

**Field Name** **Field Type** **Description**

`emailTemplate` ContentAsset[] An array of email templates the content asset is related to. This field is available
in API version 51.0 and later.


Metadata Types ContentAsset

**Field Name** **Field Type** **Description**

`insightsApplication` ContentAsset[] An array of the insights applications that use the content asset. This field is
available in API version 39.0 and later.

`network` ContentAsset[] An array of networks that use the content asset. This field is available in API
version 39.0 and later.

`organization` ContentAsset[] Stores information about sharing the asset file with the org. Maps to
ContentDocumentLink. This field is available in API version 39.0 and later.

`workspace` ContentAsset[] An array of workspaces and libraries that own or share the content asset. This
field is available in API version 39.0 and later.

ContentAssetLink

Represents a relationship link for an asset file, and includes details about the level of access for the link.

**Field Name** **Field Type** **Description**

```
access

```

ContentAssetAccess Required. The permission granted to the user of the shared file, determined by
(enumeration of type the permission the user already has. Valid values are:
string)

**•** `VIEWER`

**•** `COLLABORATOR`

**•** `INFERRED`

`isManagingWorkspace` boolean

Indicates whether the content asset resides in the workspace or not. When
`true`, the content asset resides in the workspace. If not specified, the default
value is `false` . This field is available in API version 39.0 and later.

`name` string Reserved for future use.

ContentAssetVersions

Represents information about all file versions included in the asset metadata.

**Field Name** **Field Type** **Description**

`version` ContentAssetVersion[] A list of file versions for the asset.

ContentAssetVersion

Represents information about one file version included in the asset metadata.

**Field Name** **Field Type** **Description**

`number` string Required. The version number. This field is based on, or sets, the ContentVersion.


Metadata Types ContentAsset

**Field Name** **Field Type** **Description**

`pathOnClient` string

`zipEntry` string

Required. Describes the original filename of the file. This field maps to
ContentVersion.PathOnClient. It provides the data for the ContentVersion Title
field.

If the asset file has more than one version, `format` is `ZippedVersions` .
In this case, `zipEntry` is the name of the file within the zip. If the asset file
has only one version, this field is empty.

Declarative Metadata Sample Definition

The following is an example of a ContentAsset component.

```
<?xml version="1.0" encoding="UTF-8"?>

<ContentAsset xmlns="http://soap.sforce.com/2006/04/metadata">

   <masterLabel>some asset</masterLabel>

   <relationships>

     <organization>

        <access>VIEWER</access>

     </organization>

   </relationships>

   <versions>

     <version>

        <number>1</number>

        <pathOnClient>some asset.txt</pathOnClient>

     </version>

   </versions>

</ContentAsset>

```

For assets that include just one version, the format field can be omitted or specified with the value as `Original` . File assets with more
than one version have versions wrapped in a zip file.

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>MyAsset</members>

     <name>ContentAsset</name>

   </types>

   <version>66.0</version>

</Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


### Metadata Types ContentTypeBundle ContentTypeBundle

Represents the definition of enhanced custom content types for use with enhanced CMS workspaces. When you create an enhanced
custom content type, deploy this bundle to your org. Enhanced custom content types are displayed as forms with defined fields. When
deployed, enhanced custom content types are available for use with enhanced LWR site channels. To use enhanced custom content
types with Aura and non-enhanced LWR site channels, use enhanced CMS workspaces resources.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata type and inherits its `fullName` field.

### ContentTypeBundle Structure and Directory Location ContentTypeBundle components are stored in the contentTypes folder. Here’s an example of how the folder is structured.

```
   +--myMetadataPackage

      +--contentTypes (1)

        +--bbHost (2)

          +--schema.json (3)

```

**•** The contentTypes folder (1) contains a folder for each enhanced custom content type.

**•** Each enhanced custom content type folder is named in the format _`contentTypeName`_ . In this example (2), the name is _`bbHost`_ .

**•** Each contentTypeName folder contains a JSON file, `schema.json` (3), that defines the enhanced custom content type. The JSON
file contains a title and one or more Lightning property types. Use this file to edit the properties of the enhanced custom content
type on your local machine or scratch org and then deploy it.

Version

### ContentTypeBundle components are available in version 64.0 and later.

Special Access Rules

### ContentTypeBundle is available only when Salesforce CMS and digital experiences are enabled for your org.

Fields

**Name** **Description**

```
description

```

**Type**
string

**Description**
Explanatory text about the content type.


Metadata Types ContentTypeBundle

**Name** **Description**

```
masterLabel

resources

```

**Type**
string

**Description**
Required.

A name for ContentTypeBundle, which is defined when the ContentTypeBundle is
created.

**Type**

ContentTypeBundleResource[]

**Description**
A list of source files in the ContentTypeBundle folder.

ContentTypeBundleResource

Represents the resource file inside the ContentTypeBundle.

**Name** **Description**

```
fileName

filePath

source

```

**Type**
string

**Description**
Required.

The name of the resource file.

**Type**
string

**Description**
Required.

The path to the resource.

**Type**
base64Binary

**Description**
Required.

The content of the resource.


Metadata Types ContentTypeBundle

Declarative Metadata Sample Definition

This `package.xml` retrieves all of the ContentTypeBundle components in an org.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>ContentTypeBundle</name>

      </types>

      <version>64.0</version>

   </Package>

```

In the retrieved `.zip` file, each enhanced custom content type is nested under a contentTypes folder.

This example shows the directory structure in the `.zip` file of an enhanced custom content type. The enhaced custom content type
is named bbHost and in this example it represents the profile of a bed and breakfast host.

```
   contentTypes

      bbHost

        schema.json

```

Here are the example contents of the `schema.json` file in the contentTypes directory. The bbHost is a complex type that includes
subproperties for `fullName`, `aboutMe`, `interests`, `profilePicture`, `dateOfBirth`, `lastModified`,
`personalWebsite`, `hostIdentityVerified`, `hostingExperienceInYears`, `rating`, `residenceCountry`,
and `preferredModeOfContact` . Each subproperty is a primitive type. The subproperty types included in the `schema.json`
file are completely configurable and must include a `lightning:type` for each property.

```
   {

     "title": "Bed & Breakfast Host",

     "description": "Schema for capturing B&B host details",

     "lightning:type": "lightning__objectType",

     "lightning:mixinTypes": {

      "sfdc_cms:metadataContent": {}

     },

     "properties": {

      "fullName": {

       "title": "Full Name",

       "lightning:type": "lightning__textType",

       "lightning:textIndexed": true,

       "minLength": 5,

       "maxLength": 50,

       "lightning:uiOptions": {

        "placeholderText": "Enter your full name (e.g., John Doe)"

       },

       "lightning:localizable": false

      },

      "aboutMe": {

       "title": "About Me",

       "lightning:type": "lightning__richTextType",

       "minLength": 10,

       "maxLength": 3000,

       "lightning:textIndexed": false,

       "lightning:uiOptions": {

        "placeholderText": "Write something about yourself"

```


Metadata Types ContentTypeBundle

```
       },

       "lightning:localizable": true

      },

      "interests": {

       "title": "Interests and Hobbies",

       "lightning:type": "lightning__multilineTextType",

       "lightning:textIndexed": true,

       "minLength": 10,

       "maxLength": 500,

       "lightning:uiOptions": {

        "placeholderText": "Summarize your interests and hobbies in a few lines"

       },

       "lightning:localizable": true

      },

      "profilePicture": {

       "title": "Profile Picture",

       "lightning:type": "lightning__imageType",

       "lightning:uiOptions": {

        "placeholderText": "Upload a professional headshot"

       },

       "lightning:localizable": false

      },

      "dateOfBirth": {

       "title": "Date of Birth",

       "lightning:type": "lightning__dateType",

       "lightning:localizable": true,

       "lightning:uiOptions": {

        "placeholderText": "Select your date of birth"

       }

      },

      "lastModified": {

       "title": "Last Profile Update",

       "lightning:type": "lightning__dateTimeType",

       "lightning:localizable": false,

       "lightning:uiOptions": {

        "placeholderText": "Auto-filled on profile update"

       }

      },

      "personalWebsite": {

       "title": "Personal Website",

       "lightning:type": "lightning__urlType",

       "lightning:localizable": false,

       "lightning:uiOptions": {

        "placeholderText": "https://yourwebsite.com"

       }

      },

      "hostIdentityVerified": {

       "title": "Host Identity Verified",

       "lightning:type": "lightning__booleanType",

       "lightning:uiOptions": {

        "placeholderText": "Check if host identity is verified"

       }

      },

      "hostingExperienceInYears": {

```


Metadata Types ContentTypeBundle

```
       "title": "Years of Experience hosting B&B",

       "lightning:type": "lightning__integerType",

       "minimum": 0,

       "maximum": 50,

       "lightning:localizable": false,

       "lightning:uiOptions": {

        "placeholderText": "Enter total years of experience being a B&B host"

       }

      },

      "rating": {

       "title": "Rating",

       "lightning:type": "lightning__numberType",

       "minimum": 0.0,

       "maximum": 5.0,

       "lightning:localizable": false,

       "lightning:uiOptions": {

        "placeholderText": "e.g., 4.5"

       }

      },

      "residenceCountry": {

       "title": "Country of Residence",

       "lightning:type": "lightning__textType",

       "const": ["India"]

      },

      "preferredModeOfContact": {

       "title": "Preferred Mode of Contact",

       "lightning:type": "lightning__textType",

       "enum": ["email", "SMS", "phone"],

       "lightning:uiOptions": {

        "placeholderText": "Choose your preferred mode of contact"

       }

      }

     },

     "required": ["fullName", "hostIdentityVerified"]

```

Usage

For each custom content type that you create, you must also create a CMS content page created in the enhanced LWR, LWR, or Aura
[site that displays the content. Each content page serves as the detail page for all content of a single content type. See Create Custom](https://help.salesforce.com/articleView?id=community_builder_create_page.htm&language=en_US)
[Site Pages with Experience Builder.](https://help.salesforce.com/articleView?id=community_builder_create_page.htm&language=en_US)

To use enhanced custom content types with Aura and non-enhanced LWR site channels, use the enhanced CMS workspaces resources
[for CMS Delivery Contents](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/connect_resources_cms_delivery_contents.htm) [and CMS Delivery Content.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/connect_resources_cms_delivery_content.htm)

Wildcard Support in the Manifest

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving with the Zip .


### Metadata Types ContextDefinition ContextDefinition

Represents the details of a context definition that describe the relationship between the node structures within a context.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

File Suffix and Directory Location

### ContextDefinition components have the suffix .contextDefinition and are stored in the contextDefinitions folder.

Version

### ContextDefinition components are available in API version 59.0 and later.

Special Access Rules

Enable the organization preference ContextDefinitionsEnabled to access the ContextDefinition metadata type.

Fields

**Field Name** **Description**

```
canBeReferenceDefinition

clonedFrom

contextDefinitionReferences

```

**Field Type**
boolean

**Description**
Indicates whether the context definition can be referred by other context definitions
( `true` ) or not ( `false` ). Available in API version 63.0 and later.

The default value is `false` .

**Field Type**
string

**Description**
The name of the context definition that's used to clone the current context definition.

**Field Type**
### ContextDefinitionReference[]

**Description**
References of the context definition.


Metadata Types ContextDefinition

**Field Name** **Description**

```
contextDefinitionVersions

contextTtl

description

hasSystemTags

inheritedFrom

inheritedFromVersion

isProtected

```

**Field Type**

ContextDefinitionVersion[]

**Description**
Version of the context definition.

**Field Type**
int

**Description**

Duration to persist the data, which is loaded in the run-time context instances created
by this context definition, in the cache.

The default value is 10 minutes.

**Field Type**
string

**Description**
Description of the context definition.

**Field Type**
boolean

**Description**
Indicates whether the context definition has system tags ( `true` ) or not ( `false` ).
Available in API version 63.0 and later.

The default value is `false` .

**Field Type**
string

**Description**
Name of the parent context definition that's used to derive the current context
definition.

**Field Type**
string

**Description**
Version number of the parent definition that's used to derive the current context
definition.

**Field Type**
boolean

**Description**
Auto-generated value that doesn’t impact the behavior of the metadata type.


Metadata Types ContextDefinition

**Field Name** **Description**

```
masterLabel

title

```

**Field Type**
string

**Description**

Required.

User-friendly name for the context definition, which is defined when the context
definition is created.

**Field Type**
string

**Description**

Required.

Name of the context definition.

ContextDefinitionReference

Represents details about the context definition reference.

**Field Name** **Description**

```
inheritedFrom

referenceContextDefinition

```

**Field Type**
string

**Description**
ID of the parent context definition reference that's used to derive the current context
definition reference.

**Field Type**
string

**Description**

Required.

ID or name of the referred context definition.

ContextDefinitionVersion

Represents details about the context definition version. Only one version can be active at a time.

**Field Name** **Description**

```
contextMappings

```

**Field Type**

ContextMapping[]


Metadata Types ContextDefinition

**Field Name** **Description**

**Description**
Mapping of attributes and nodes to related objects.

```
contextNodes

endDate

isActive

startDate

versionNumber

```

ContextMapping

**Field Type**

ContextNode[]

**Description**
Details of the structure of the nodes within the context.

**Field Type**
string

**Description**
Date and time when the context definition version becomes inactive.

**Field Type**
boolean

**Description**
Indicates whether the context definition version is active ( `true` ) or not ( `false` ).

The default value is `false` .

**Field Type**
string

**Description**

Required.

Date and time when the context definition version becomes active.

**Field Type**
int

**Description**

Required.

Version number of the context definition.

Represents the mapping of attributes and nodes to related objects.

**Field Name** **Description**

```
contextMappingIntents

```

**Field Type**

ContextMappingIntent[]

**Description**
Purpose associated to a context mapping.


Metadata Types ContextDefinition

**Field Name** **Description**

```
contextNodeMappings

default

description

inheritedFrom

title

```

ContextMappingIntent

**Field Type**

ContextNodeMapping[]

**Description**
Mapping of the node in the context and values in the input schema.

**Field Type**
boolean

**Description**
Indicates whether the mapping for a context definition version is default ( `true` ) or
not ( `false` ).

The default value is `false` .

**Field Type**
string

**Description**
Description of the context mapping.

**Field Type**
string

**Description**
Name of the parent mapping that's used to derive the current mapping.

**Field Type**
string

**Description**

Required.

Name of the context mapping.

Represents the purpose associated to a context mapping.

**Field Name** **Description**

```
mappingIntent

```

**Field Type**
ContextMappingIntentType (enumeration of type string)

**Description**

Required.

Specifies the purpose that's used to identify the type of context mapping required.

Valid values are:


Metadata Types ContextDefinition

**Field Name** **Description**

**•** `hydration`

**•** `association`

**•** `persistence`

**•** `translation`

ContextNodeMapping

Represents the relationship between the node in the context and values in the input schema.

**Field Name** **Description**

```
contextAttributeMappings

contextNode

contextNodeAttrDictionaries

inheritedFrom

mappedContextDefinition

object

```

**Field Type**

ContextAttributeMapping[]

**Description**
Mapping of the attribute defined in the context and the values in the related objects.

**Field Type**
string

**Description**
Context node record associated with the context node mapping.

**Field Type**

ContextNodeAttrDictionary[]

**Description**
Facilitates relationships between context node mapping and context dictionary.
Additionally, it records the relationship between context node and context dictionary.

**Field Type**
string

**Description**
Name of the parent context node mapping that's used to derive the current context
node mapping.

**Field Type**
string

**Description**
API name of the context definition for existing context-to-context mappings.

**Field Type**
string

**Description**
Name of the object used for the mapping.


Metadata Types ContextDefinition

ContextAttributeMapping

Represents the relationship between the attributes defined in the context and the values in the related objects.

**Field Name** **Description**

```
contextAttrHydrationDetails

contextAttribute

contextInputAttributeName

ctxAttrHydrationCtxs

inheritedFrom

```

**Field Type**

ContextAttrHydrationDetail[]

**Description**
Details of the SOQL (database) queries that fetch data for a chosen attribute from the
input schema.

**Field Type**
string

**Description**
Context attribute record associated with the context attribute mapping.

**Field Type**
string

**Description**

Required.

Name of the input attribute.

**Field Type**

CtxAttrHydrationCtx[]

**Description**
Query that fetches data for a chosen attribute from the input schema for
context-to-context mapping.

**Field Type**
string

**Description**
Name of the parent context attribute mapping that's used to derive the current context
attribute mapping.

ContextAttrHydrationDetail

Represents the SOQL (database) queries that fetch data for a chosen attribute from the input schema.

**Field Name** **Description**

```
contextAttrHydrationDetails

```

**Field Type**

ContextAttrHydrationDetail[]


Metadata Types ContextDefinition

**Field Name** **Description**

**Description**
Details of the query that fetches the data for the specific query attribute.

```
inheritedFrom

objectName

queryAttribute

```

CtxAttrHydrationCtx

**Field Type**
string

**Description**
Name of the parent context attribute hydration detail that's used to derive the current
context attribute hydration detail.

**Field Type**
string

**Description**

Required.

Name of the object used for the attribute hydration detail.

**Field Type**
string

**Description**

Required.

The SOQL query that is the source of the hydration.

Represents the queries that fetch data for a chosen attribute from the input schema for context-to-context mapping.

**Field Name** **Description**

```
contextQueryAttribute

inheritedFrom

```

**Field Type**
string

**Description**

Required.

Attribute in context definition that's the source of context hydration.

**Field Type**
string

**Description**
Name of the parent context attribute hydration detail that's used to derive the current
context attribute.


Metadata Types ContextDefinition

ContextNodeAttrDictionary

Represents the relationship between a context node and the context attribute dictionary.

**Field Name** **Description**

```
contextAttrDictIdentifier

contextNodeTagPrefix

```

ContextNode

**Field Type**
string

**Description**

Required.

Developer name of the context attribute dictionary.

**Field Type**
string

**Description**

Required.

Tag prefix of the context node that's used to create the unique identifier of the parent
context node.

Represents details of the structure of the nodes within the context. Each node can have other nodes related to them and attributes to
describe the object. You can also define a hierarchy for the nodes.

**Field Name** **Description**

```
canonicalNode

contextAttributes

contextNodeAttrDictionaries

contextTags

```

**Field Type**
string

**Description**
Canonical node that's associated with the context node.

**Field Type**

ContextAttribute[]

**Description**
Details of the attribute used to describe the context node.

**Field Type**

ContextNodeAttrDictionary[]

**Description**
Facilitates relationships between context node and context dictionary. Additionally,
it records the relationship between context node and context dictionary.

**Field Type**

ContextTag[]


Metadata Types ContextDefinition

**Field Name** **Description**

**Description**
Unique identifier of the attribute or node.

```
displayName

inheritedFrom

title

transposable

```

ContextAttribute

**Field Type**
string

**Description**
Display name of the context node.

**Field Type**
string

**Description**
Name of the parent context node that's used to derive the current context node.

**Field Type**
string

**Description**

Required.

Name of the context node.

**Field Type**
boolean

**Description**
Indicates whether the data in the Context Node record can be converted to field names
( `true` ) or not ( `false` ).

The default value is `false` .

Represents details of an attribute used to describe a context node. Each node can have one or many associated attributes.

**Field Name** **Description**

```
contextTags

dataType

```

**Field Type**

ContextTag[]

**Description**
Shortened name of the attribute or node.

**Field Type**
ContextAttributeDataType (enumeration of type string)

**Description**

Required.


Metadata Types ContextDefinition

**Field Name** **Description**

Type of data that's stored in the context attribute.

Valid values are:

**•** `boolean`

**•** `currency`

**•** `date`

**•** `datetime`

**•** `number`

**•** `percent`

**•** `picklist`

**•** `reference`

**•** `string`

**•** `selfreference` —Available in API version 63.0 and later.

```
description

displayName

domainSet

fieldType

```

**Field Type**
string

**Description**
Description of the context attribute.

**Field Type**
string

**Description**
Display name of the context attribute.

**Field Type**
string

**Description**
List of node references to show the parent-child relationship between the nodes in a
definition.

**Field Type**
ContextAttributeFieldType (enumeration of type string)

**Description**

Required.

List of node references to depict the parent-child relation between the nodes in a
definition.

Valid values are:

**•** `aggregate`

**•** `input`

**•** `inputoutput`

**•** `output`


Metadata Types ContextDefinition

**Field Name** **Description**

```
inheritedFrom

key

title

transient

value

```

ContextTag

**Field Type**
string

**Description**
Name of the parent attribute that's used to derive the current attribute.

**Field Type**
boolean

**Description**
Indicates whether the attribute is a key attribute in the node ( `true` ) or not ( `false` ).

The default value is `false` .

**Field Type**
string

**Description**

Required.

Name of the context attribute.

**Field Type**
boolean

**Description**
Indicates if an attribute is skipped in context persistence ( `true` ) or not ( `false` ).
Available in API version 63.0 and later.

The default value is `false` .

**Field Type**
boolean

**Description**
Indicates whether the attribute identifies as a value in a node ( `true` ) or not ( `false` ).

The default value is `false` .

Represents a unique identifier of an attribute or node instead of a fully qualified tag structure name.

**Field Name** **Description**

```
title

```

**Field Type**
string

**Description**

Required.


Metadata Types ContextDefinition

**Field Name** **Description**

Name of the context tag.

```
inheritedFrom

```

**Field Type**
string

**Description**
Name of the parent context tag that's used to derive the current context tag.

Declarative Metadata Sample Definition

The following is an example of a ContextDefinition component.

```
<?xml version="1.0" encoding="UTF-8"?>

<ContextDefinition xmlns="http://soap.sforce.com/2006/04/metadata">

   <fullName>Test</fullName>

   <contextDefinitionVersions>

     <contextMappings>

        <contextNodeMappings>

          <contextNodeAttrDictionaries>

            <contextAttrDictIdentifier>Context Attribute Dictionary

Name</contextAttrDictIdentifier>

            <contextNodeTagPrefix>Context Node Tag Prefix</contextNodeTagPrefix>

          </contextNodeAttrDictionaries>

          <contextAttributeMappings>

            <contextAttrHydrationDetails>

               <objectName>CustomAccount__c</objectName>

               <queryAttribute>Name</queryAttribute>

<inheritedFrom>StandardDefinition/version/CustomAccountMapping/Praneeth/AccountName/hydrationInfo-1</inheritedFrom>

            </contextAttrHydrationDetails>

            <ctxAttrHydrationCtxs>

               <contextQueryAttribute>StandardDefinition</contextQueryAttribute>

<inheritedFrom>StandardDefinition/version/AccountMapping/Praneeth/AccountName/ctxToCtxhydrationInfo-1</inheritedFrom>

            </ctxAttrHydrationCtxs>

            <contextAttribute>AccountName</contextAttribute>

            <contextInputAttributeName>AccountName</contextInputAttributeName>

<inheritedFrom>StandardDefinition/version/CustomAccountMapping/Praneeth/AccountName</inheritedFrom>

          </contextAttributeMappings>

          <contextAttributeMappings>

            <contextAttrHydrationDetails>

               <objectName>CustomAccount__c</objectName>

               <queryAttribute>CustomAccountName__c</queryAttribute>

<inheritedFrom>StandardDefinition/version/CustomAccountMapping/Praneeth/CustomAccountName/hydrationInfo-1</inheritedFrom>

```


Metadata Types ContextDefinition

```
               </contextAttrHydrationDetails>

               <ctxAttrHydrationCtxs>

                  <contextQueryAttribute>StandardDefinition</contextQueryAttribute>

   <inheritedFrom>StandardDefinition/version/AccountMapping/Praneeth/AccountName/ctxToCtxhydrationInfo-1</inheritedFrom>

               </ctxAttrHydrationCtxs>

               <contextAttribute>CustomAccountName</contextAttribute>

             <contextInputAttributeName>CustomAccountName</contextInputAttributeName>

   <inheritedFrom>StandardDefinition/version/CustomAccountMapping/Praneeth/CustomAccountName</inheritedFrom>

             </contextAttributeMappings>

             <contextNode>Praneeth</contextNode>

             <object>CustomAccount__c</object>

   <inheritedFrom>StandardDefinition/version/CustomAccountMapping/Praneeth</inheritedFrom>

            <mappedContextDefinition>CustomContextDefinition</mappedContextDefinition>

           </contextNodeMappings>

           <contextMappingIntents>

             <mappingIntent>hydration</mappingIntent>

           </contextMappingIntents>

           <default>true</default>

           <title>CustomAccountMapping</title>

          <inheritedFrom>StandardDefinition/version/CustomAccountMapping</inheritedFrom>

        </contextMappings>

        <contextMappings>

           <contextNodeMappings>

             <contextNodeAttrDictionaries>

               <contextAttrDictIdentifier>Context Attribute Dictionary

   Name</contextAttrDictIdentifier>

               <contextNodeTagPrefix>Context Node Tag Prefix</contextNodeTagPrefix>

             </contextNodeAttrDictionaries>

             <contextAttributeMappings>

               <contextAttrHydrationDetails>

                  <objectName>Account</objectName>

                  <queryAttribute>Name</queryAttribute>

   <inheritedFrom>StandardDefinition/version/AccountMapping/Praneeth/CustomAccountName/AccountName/hydrationInfo-1</inheritedFrom>

               </contextAttrHydrationDetails>

               <ctxAttrHydrationCtxs>

                  <contextQueryAttribute>StandardDefinition</contextQueryAttribute>

   <inheritedFrom>StandardDefinition/version/AccountMapping/Praneeth/AccountName/ctxToCtxhydrationInfo-1</inheritedFrom>

               </ctxAttrHydrationCtxs>

               <contextAttribute>AccountName</contextAttribute>

               <contextInputAttributeName>AccountName</contextInputAttributeName>

```


Metadata Types ContextDefinition

```
   <inheritedFrom>StandardDefinition/version/AccountMapping/Praneeth/CustomAccountName/AccountName</inheritedFrom>

             </contextAttributeMappings>

             <contextAttributeMappings>

               <contextAttrHydrationDetails>

                  <objectName>Account</objectName>

                  <queryAttribute>CustomAccountName__c</queryAttribute>

   <inheritedFrom>StandardDefinition/version/AccountMapping/Praneeth/CustomAccountName/hydrationInfo-1</inheritedFrom>

               </contextAttrHydrationDetails>

               <ctxAttrHydrationCtxs>

                  <contextQueryAttribute>StandardDefinition</contextQueryAttribute>

   <inheritedFrom>StandardDefinition/version/AccountMapping/Praneeth/AccountName/ctxToCtxhydrationInfo-1</inheritedFrom>

               </ctxAttrHydrationCtxs>

               <contextAttribute>CustomAccountName</contextAttribute>

             <contextInputAttributeName>CustomAccountName</contextInputAttributeName>

   <inheritedFrom>StandardDefinition/version/AccountMapping/Praneeth/CustomAccountName</inheritedFrom>

             </contextAttributeMappings>

             <contextNode>Praneeth</contextNode>

             <object>Account</object>

   <inheritedFrom>StandardDefinition/version/AccountMapping/Praneeth</inheritedFrom>

            <mappedContextDefinition>CustomContextDefinition</mappedContextDefinition>

           </contextNodeMappings>

           <contextMappingIntents>

             <mappingIntent>persistence</mappingIntent>

           </contextMappingIntents>

           <description>Account Mapping</description>

           <default>false</default>

           <title>AccountMapping</title>

           <inheritedFrom>StandardDefinition/version/AccountMapping</inheritedFrom>

        </contextMappings>

        <contextNodes>

           <contextNodeAttrDictionaries>

             <contextAttrDictIdentifier>Context Attribute Dictionary

   Name</contextAttrDictIdentifier>

             <contextNodeTagPrefix>Context Node Tag Prefix</contextNodeTagPrefix>

           </contextNodeAttrDictionaries>

           <contextAttributes>

             <contextTags>

               <title>AccountName</title>

   <inheritedFrom>StandardDefinition/version/Praneeth/AccountName/AccountName</inheritedFrom>

             </contextTags>

```


Metadata Types ContextDefinition

```
             <dataType>string</dataType>

             <fieldType>inputoutput</fieldType>

             <key>false</key>

             <title>AccountName</title>

             <displayName>AccountName</displayName>

             <description>Test Description</description>

             <value>false</value>

   <inheritedFrom>StandardDefinition/version/Praneeth/AccountName</inheritedFrom>

           </contextAttributes>

           <contextAttributes>

             <dataType>string</dataType>

             <fieldType>inputoutput</fieldType>

             <key>false</key>

             <title>CustomAccountName</title>

             <value>false</value>

             <displayName>CustomAccountName</displayName>

             <description>Test Description</description>

   <inheritedFrom>StandardDefinition/version/Praneeth/CustomAccountName</inheritedFrom>

           </contextAttributes>

           <contextTags>

             <title>Praneeth</title>

            <inheritedFrom>StandardDefinition/version/Praneeth/Praneeth</inheritedFrom>

           </contextTags>

           <title>Praneeth</title>

           <transposable>false</transposable>

           <inheritedFrom>StandardDefinition/version/Praneeth</inheritedFrom>

           <canonicalNode></canonicalNode>

           <displayName>Praneeth</displayName>

        </contextNodes>

        <endDate>2097-05-10 00:00:00</endDate>

        <startDate>2023-05-10 00:00:00</startDate>

        <versionNumber>1</versionNumber>

        <isActive>true</isActive>

      </contextDefinitionVersions>

      <description>Test Description</description>

      <contextTtl>10</contextTtl>

      <inheritedFrom>StandardDefinition</inheritedFrom>

      <inheritedFromVersion>1.0</inheritedFromVersion>

      <clonedFrom>OriginalDefinition</clonedFrom>

      <isProtected>false</isProtected>

      <masterLabel>Test Label</masterLabel>

      <title>TestTitle</title>

      <displayName>TestTitle</displayName>

   </ContextDefinition>

```

The following is an example `package.xml` that references the previous definition.

```
   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>Test</members>

        <name>ContextDefinition</name>

      </types>

```


### Metadata Types ConversationMessageDefinition

```
      <types>

        <members>Account.CustomAccountName__c</members>

        <name>CustomField</name>

      </types>

      <types>

        <members>CustomAccount__c</members>

        <name>CustomObject</name>

      </types>

      <version>64.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### ConversationMessageDefinition

Represents a messaging component in an Enhanced Messaging channel or Messaging for In-App and Web session.

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

File Suffix and Directory Location

### ConversationMessageDefinition components have the suffix .conversationMessageDefinition and are

stored in the `conversationMessageDefinitions` folder.

Version

### ConversationMessageDefinition is supported for use in enhanced Messaging channels and Messaging for In-App and

Web, and is available in API version 59.0 and later.

Fields

**Field Name** **Description**

```
constants

description

```

**Field Type**

ConversationMessageConstant[]

**Description**
An array of constants that defines the messaging components. Constants support
multiple data types, including text, URL, and image.

**Field Type**
string


Metadata Types ConversationMessageDefinition

**Field Name** **Description**

**Description**
The description of the conversation message definition.

```
label

language

messageHandlers

messageLayouts

optionsParameter

parameters

type

```

**Field Type**
string

**Description**
A user-friendly name for `ConversationMessageDefinition`, which is defined
when `ConversationMessageDefinition` is created.

**Field Type**
string

**Description**
The language of the conversation message definition.

**Field Type**

ConversationMessageHandler[]

**Description**
An array of message handlers.

**Field Type**

ConversationMessageLayout[]

**Description**
An array of message layouts.

**Field Type**

ConversationMessageOptionsParameter[]

**Description**
An array of options parameter of the `ConversationMessageDefinition` .

**Field Type**

ConversationMessageParameter[]

**Description**
An array of parameters.

**Field Type**
ConversationMessageDefinitionType (enumeration of type string)

**Description**

Required. The type of the conversation message definition. Valid values are:

**•** `Action`

**•** `ApexForm`

**•** `AuthenticationRequest`


Metadata Types ConversationMessageDefinition

**Field Name** **Description**

**•** `AutoResponse`

**•** `Link`

**•** `Notification`

**•** `PaymentRequest`

**•** `Picklist`

**•** `RecordPicker`

**•** `RecordView`

**•** `TimePicker`

ConversationMessageConstant

Represents a constant value on the messaging component. When a messaging component is created in the UI, the text and images
entered during creation are saved as standard constants. Custom constants can also be added.

**Field Name** **Description**

```
compositeValues

constantType

label

name

```

**Field Type**

ConversationMessageConstantCompositeValue[]

**Description**
An array of composite values of `ConversationMessageConstant` .

**Field Type**
ConversationMessageConstantType (enumeration of type string)

**Description**

Required. The conversation message constant type. Valid values are:

**•** `Custom`

**•** `Image`

**•** `Options`

**•** `SubTitle`

**•** `Title`

**•** `Url`

**Field Type**
string

**Description**
The UI label of the conversation message constant.

**Field Type**
string


Metadata Types ConversationMessageDefinition

**Field Name** **Description**

**Description**
The name of the conversation message constant.

```
primitiveValues

valueType

```

**Field Type**

ConversationMessageConstantPrimitiveValue (enumeration of type string)

**Description**
An array of primitive values of `ConversationMessageConstant` .

**Field Type**
ConversationMessageValueType (enumeration of type string)

**Description**

The type of the conversation message constant value. Valid values are:

**•** `Boolean`

**•** `Date`

**•** `DateTime`

**•** `Double`

**•** `ImageId`

**•** `Integer`

**•** `RecordId`

**•** `Text`

**•** `Url`

ConversationMessageConstantCompositeValue

Represents the composite values of the ConversationMessageConstant.

**Field Name** **Description**

```
constantItems

identifier

```

**Field Type**

ConversationMessageConstant[]

**Description**
An array of constant items.

**Field Type**
string

**Description**
Required. The client identifier.


Metadata Types ConversationMessageDefinition

ConversationMessageConstantPrimitiveValue

Represents the primitive values of the ConversationMessageConstant.

**Field Name** **Description**

```
contentAssetName

textValue

type

urlValue

```

**Field Type**
string

**Description**
Represents the value for type = ImageAsset

**Field Type**
string

**Description**
Represents the value for type = Text

**Field Type**
ConversationMessageConstantValueType (enumeration of type string)

**Description**

Required. The type of the conversation message constant primitive value. Valid values
are:

**•** `ImageAsset`

**•** `Text`

**•** `Url`

**Field Type**
string

**Description**
Represents the value for type = Url

ConversationMessageHandler

Represents the conversation message handler.

**Field Name** **Description**

```
activeRequestDurationMinutes

handlerName

```

**Field Type**
int

**Description**
Required. The duration of an active request in minutes.

**Field Type**
string


Metadata Types ConversationMessageDefinition

**Field Name** **Description**

**Description**
Required. The name of the message handler.

```
handlerType

```

**Field Type**
ConversationMessageHandlerType (enumeration of type string)

**Description**

Required. The type of message handler. Valid values are:

**•** `ApexFormProvider` . Available in API version 65.0 and later.

**•** `AuthProvider`

**•** `PaymentProvider`

**•** `QuickAction`

**•** `Survey` . Available in API version 65.0 and later.

ConversationMessageLayout

Represents the conversation message layout.

**Field Name** **Description**

```
externalTemplates

formatType

```

**Field Type**

ConvMsgExternalTemplateVersion[]

**Description**
The external template version of the `ConversationMessageLayout` .

**Field Type**
ConversationMessageFormatType (enumeration of type string)

**Description**

Required. The format type of the conversation message layout. Valid values are:

**•** `Application`

**•** `Buttons`

**•** `Carousel`

**•** `EncryptedOAuthToken`

**•** `ExternalTemplate`

**•** `Flow`

**•** `Inputs`

**•** `ListPicker`

**•** `Media`

**•** `Payment`

**•** `QuickReplies`


Metadata Types ConversationMessageDefinition

**Field Name** **Description**

**•** `RichLink`

**•** `Text`

**•** `TimePicker`

**•** `WebView`

```
layoutItems

messageType

```

**Field Type**

ConversationMessageLayoutItem[]

**Description**
An array of layout items.

**Field Type**
ConversationMessageType (enumeration of type string)

**Description**

Required. The conversation message type. Valid values are:

**•** `AuthenticationRequest`

**•** `Choices`

**•** `Form`

**•** `PaymentRequest`

**•** `StaticContent`

ConvMsgExternalTemplateVersion

Represents the external template version of the conversation message layout.

**Field Name** **Description**

```
accountIdentifier

accountName

language

```

**Field Type**
string

**Description**
Required. The account identifier. For WhatsApp channels, this is the WABA ID.

**Field Type**
string

**Description**
Required. The account name.

**Field Type**
string

**Description**
Required. The language of the conversation message external template.


Metadata Types ConversationMessageDefinition

**Field Name** **Description**

```
status

templateName

templateVersionIdentifier

```

**Field Type**
ConvMsgExternalTemplateVersionStatus (enumeration of type string)

**Description**

Required. The status of the conversation message external template. Valid values are:

**•** `Approved` . The template version is approved.

**•** `Blocked` . The template version is blocked. Available in API version 65.0 and later.

**•** `Deleted` . The template version is deleted. Available in API version 65.0 and later.

**•** `Disabled` . The template version is disabled because of recurring negative
customer feedback.

**•** `InAppeal` . The rejected template version is being appealed. Available in API
version 65.0 and later.

**•** `LimitExceeded` . Available in API version 65.0 and later.

**•** `OutOfSync` . The template versions in the messaging service and Salesforce are
out of sync. Available in API version 65.0 and later.

**•** `Paused` . The template version is paused because of recurring negative customer
feedback or low read rates.

**•** `Pending` . The template version awaits Meta's approval.

**•** `PendingDeletion` . The template version is pending deletion. Available in
API version 65.0 and later.

**•** `Rejected` . The template version was rejected during Meta’s review process.

**Field Type**
string

**Description**
Required. The name of the conversation message external template.

**Field Type**
string

**Description**
Required. The template version identifier.

ConversationMessageLayoutItem

Represents the conversation message layout item.

**Field Name** **Description**

```
collectionType

```

**Field Type**
ConversationMessageCollectionType (enumeration of type string)


Metadata Types ConversationMessageDefinition

**Field Name** **Description**

**Description**

Required. The type of conversation message collection. Valid values are:

**•** `DynamicList`

**•** `None`

**•** `StaticList`

```
compositeValues

name

primitiveValues

```

**Field Type**

ConversationMessageLayoutCompositeValue[]

**Description**
An array of composite values of the `ConversationMessageLayoutItem` .

**Field Type**
string

**Description**
The name of the conversation message layout item.

**Field Type**

ConversationMessageLayoutPrimitiveValue[]

**Description**
An array of primitive values of the `ConversationMessageLayoutItem` .

ConversationMessageLayoutCompositeValue

Represents the composite value of the ConversationMessageLayoutItem.

**Field Name** **Description**

```
compositeTypeName

layoutItems

valueSourceReference

```

**Field Type**
string

**Description**
Required. The name of the conversation message layout composite value type.

**Field Type**

ConversationMessageLayoutItem[]

**Description**
An array of layout items.

**Field Type**
string

**Description**
The source of the conversation message layout composite value.


Metadata Types ConversationMessageDefinition

ConversationMessageLayoutPrimitiveValue

Represents the primitive value of the ConversationMessageLayoutItem.

**Field Name** **Description**

```
contentAssetName

fieldName

formulaTemplate

literalValue

mergeFields

type

```

**Field Type**
string

**Description**
The content asset name.

**Field Type**
string

**Description**
The name of the conversation message layout primitive value field.

**Field Type**
string

**Description**
The formula template defines the content for each entry in the list.

**Field Type**
string

**Description**
The literal primitive value of the conversation message layout.

**Field Type**

ConversationMessageMergeField[]

**Description**
Inserts multiple values to a list.

**Field Type**
ConversationMessageLayoutValueType (enumeration of type string)

**Description**

Required. The type of the conversation message layout primitive value. Valid values
are:

**•** `FormulaTemplate`

**•** `Literal`

**•** `MediaAsset`

**•** `SourcePrimitiveValue`

**•** `SourceSobjectField`

**•** `SourceSobjectFieldValue`

**•** `SourceSobjectFormula`


Metadata Types ConversationMessageDefinition

**Field Name** **Description**

```
valueFormula

valueSourceReference

```

**Field Type**
string

**Description**
The formula of the conversation message layout primitive value.

**Field Type**
string

**Description**
The source of the conversation message layout primitive value.

ConversationMessageMergeField

Merge field is used to insert multiple values to a list.

**Field Name** **Description**

```
formulaTemplate

mergeFieldType

name

valueSourceReference

```

**Field Type**
string

**Description**
Required. The formula template of the conversation message merge field.

**Field Type**
ConversationMessageMergeFieldType (enumeration of type string)

**Description**
Required. The type of the conversation message merge field. Valid value is ListTemplate.

**Field Type**
string

**Description**
Required. The name of the conversation message merge field.

**Field Type**
string

**Description**
Required. The source of the conversation message merge field value.

ConversationMessageOptionsParameter

Represents a conversation message options parameter.


Metadata Types ConversationMessageDefinition

**Field Name** **Description**

```
compositeTypeDetails

optionsParameterType

primitiveTypeDetails

```

**Field Type**

ConversationMessageParameterCompositeDetails[]

**Description**
An array of composite details of `ConversationMessageOptionsParameter` .

**Field Type**
ConversationMessageOptionsParameterType (enumeration of type string)

**Description**

Required. The type of conversation message options parameter. Valid values are:

**•** `CustomCompositeOptions`

**•** `CustomPrimitiveOptions`

**•** `RecordIdOptions`

**•** `TimeSlotOptions`

**Field Type**
ConversationMessageParameterPrimitiveDetails

**Description**
The primitive type details of conversation message options parameter.

ConversationMessageParameterCompositeDetails

Represents the composite details of a conversation message parameter.

**Field Name** **Description**

```
compositeChildItems

isList

isRequired

```

**Field Type**
ConversationMessageParameterCompositeDetails[]

**Description**
The composite child items of the conversation message parameter.

**Field Type**
boolean

**Description**
Indicates whether the conversation message parameter composite details field is a
list item ( `true` ) or not ( `false` ). The default value is false.

**Field Type**
boolean

**Description**
Indicates whether the conversation message parameter is required ( `true` ) or not
( `false` ). The default value is false.


Metadata Types ConversationMessageDefinition

**Field Name** **Description**

```
label

maxListItems

name

primitiveChildItems

```

**Field Type**
string

**Description**
The UI label of the conversation message parameter composite details field.

**Field Type**
int

**Description**
The maximum number of list items in the conversation message parameter composite
details field.

**Field Type**
string

**Description**
The name of the conversation message parameter composite details field.

**Field Type**

ConversationMessageParameterPrimitiveDetails[]

**Description**
An array of primitive child items.

ConversationMessageParameterPrimitiveDetails

Represents the primitive details of the conversation message parameter.

**Field Name** **Description**

```
isList

isRequired

label

```

**Field Type**
boolean

**Description**
Indicates whether the conversation message parameter primitive details field is a list
item ( `true` ) or not ( `false` ). The default value is false.

**Field Type**
boolean

**Description**
Indicates whether the conversation message parameter primitive details field is required
( `true` ) or not ( `false` ). The default value is false.

**Field Type**
string


Metadata Types ConversationMessageDefinition

**Field Name** **Description**

**Description**
The UI label of the conversation message parameter primitive details field.

```
maxListItems

name

sobjectType

valueType

```

**Field Type**
int

**Description**
The maximum number of list items that are allowed in the conversation message
parameter primitive details field.

**Field Type**
string

**Description**
The name of the conversation message parameter primitive details field.

**Field Type**
string

**Description**
The sObject type.

**Field Type**
ConversationMessageValueType (enumeration of type string)

**Description**

The type of the conversation message parameter value. Valid values are:

**•** `Boolean`

**•** `Date`

**•** `DateTime`

**•** `Double`

**•** `ImageId`

**•** `Integer`

**•** `RecordId`

**•** `Text`

**•** `Url`

ConversationMessageParameter

Represents a conversation message parameter.

**Field Name** **Description**

```
compositeTypeDetails

```

**Field Type**

ConversationMessageParameterCompositeDetails


Metadata Types ConversationMessageDefinition

**Field Name** **Description**

**Description**
An array of composite type details.

```
parameterType

primitiveTypeDetails

```

**Field Type**
ConversationMessageParameterType (enumeration of type string)

**Description**

Required. The type of conversation message parameter. Valid values are:

**•** `CustomComposite`

**•** `CustomPrimitive`

**•** `RecordIds`

**Field Type**

ConversationMessageParameterPrimitiveDetails

**Description**
An array of primitive type details.

Declarative Metadata Sample Definition

The following is an example of a `ConversationMessageDefinition` component.

```
<?xml version="1.0" encoding="UTF-8"?>

<ConversationMessageDefinition xmlns="http://soap.sforce.com/2006/04/metadata">

   <constants>

     <constantType>Custom</constantType>

     <label>imageAsset</label>

     <name>imageAsset</name>

     <primitiveValues>

        <contentAssetName>Screenshot_20240402_at_32437PM</contentAssetName>

        <type>ImageAsset</type>

     </primitiveValues>

     <valueType>ImageId</valueType>

   </constants>

   <constants>

     <constantType>Custom</constantType>

     <label>message</label>

     <name>message</name>

     <primitiveValues>

        <textValue>Favourite Season</textValue>

        <type>Text</type>

     </primitiveValues>

     <valueType>Text</valueType>

   </constants>

   <constants>

     <constantType>Custom</constantType>

     <label>Prompt1</label>

     <name>Prompt1</name>

```


Metadata Types ConversationMessageDefinition

```
        <primitiveValues>

           <textValue>Choose one option</textValue>

           <type>Text</type>

        </primitiveValues>

        <valueType>Text</valueType>

      </constants>

      <constants>

        <compositeValues>

           <constantItems>

             <constantType>Image</constantType>

             <primitiveValues>

               <contentAssetName>Screenshot_20240321_at_53957PM3</contentAssetName>

               <type>ImageAsset</type>

             </primitiveValues>

           </constantItems>

           <constantItems>

             <constantType>SubTitle</constantType>

             <primitiveValues>

               <textValue>January</textValue>

               <type>Text</type>

             </primitiveValues>

           </constantItems>

           <constantItems>

             <constantType>Title</constantType>

             <primitiveValues>

               <textValue>Jan</textValue>

               <type>Text</type>

             </primitiveValues>

           </constantItems>

           <identifier>1c6f8c4d-7bce-1649-fa45-db587bcfbb29</identifier>

        </compositeValues>

        <compositeValues>

           <constantItems>

             <constantType>Image</constantType>

             <primitiveValues>

               <contentAssetName>Screenshot_20240321_at_53957PM4</contentAssetName>

               <type>ImageAsset</type>

             </primitiveValues>

           </constantItems>

           <constantItems>

             <constantType>SubTitle</constantType>

             <primitiveValues>

               <textValue>December</textValue>

               <type>Text</type>

             </primitiveValues>

           </constantItems>

           <constantItems>

             <constantType>Title</constantType>

             <primitiveValues>

               <textValue>Dec</textValue>

               <type>Text</type>

             </primitiveValues>

           </constantItems>

           <identifier>fb8bb328-7bc7-2830-6194-2ae7ece055ad</identifier>

```


Metadata Types ConversationMessageDefinition

```
        </compositeValues>

        <compositeValues>

           <constantItems>

             <constantType>Image</constantType>

             <primitiveValues>

               <contentAssetName>Screenshot_20240321_at_53912PM1</contentAssetName>

               <type>ImageAsset</type>

             </primitiveValues>

           </constantItems>

           <constantItems>

             <constantType>SubTitle</constantType>

             <primitiveValues>

               <textValue>March</textValue>

               <type>Text</type>

             </primitiveValues>

           </constantItems>

           <constantItems>

             <constantType>Title</constantType>

             <primitiveValues>

               <textValue>March</textValue>

               <type>Text</type>

             </primitiveValues>

           </constantItems>

           <identifier>570baa88-fa4d-4b31-0e84-92f87b35af0a</identifier>

        </compositeValues>

        <constantType>Options</constantType>

      </constants>

      <constants>

        <constantType>Title</constantType>

        <primitiveValues>

           <textValue>What is your favourite month?</textValue>

           <type>Text</type>

        </primitiveValues>

      </constants>

      <label>Favourite Month</label>

      <language>en_US</language>

      <messageLayouts>

        <formatType>Buttons</formatType>

        <layoutItems>

           <collectionType>DynamicList</collectionType>

           <compositeValues>

             <compositeTypeName>TitleOptionItem</compositeTypeName>

             <layoutItems>

               <collectionType>None</collectionType>

               <compositeValues>

                  <compositeTypeName>TitleItem</compositeTypeName>

                  <layoutItems>

                    <collectionType>None</collectionType>

                    <name>title</name>

                    <primitiveValues>

                       <type>SourcePrimitiveValue</type>

   <valueSourceReference>Constants.Options.ListItem.SubTitle</valueSourceReference>

                    </primitiveValues>

```


Metadata Types ConversationMessageDefinition

```
                  </layoutItems>

               </compositeValues>

               <name>titleItem</name>

             </layoutItems>

             <valueSourceReference>Constants.Options</valueSourceReference>

           </compositeValues>

           <name>optionItems</name>

        </layoutItems>

        <layoutItems>

           <collectionType>None</collectionType>

           <name>text</name>

           <primitiveValues>

             <type>SourcePrimitiveValue</type>

             <valueSourceReference>Constants.Title</valueSourceReference>

           </primitiveValues>

        </layoutItems>

        <messageType>Choices</messageType>

      </messageLayouts>

      <messageLayouts>

        <formatType>ListPicker</formatType>

        <layoutItems>

           <collectionType>None</collectionType>

           <compositeValues>

             <compositeTypeName>TitleImageItem</compositeTypeName>

             <layoutItems>

               <collectionType>None</collectionType>

               <name>imageId</name>

               <primitiveValues>

                  <type>SourcePrimitiveValue</type>

                  <valueSourceReference>Constants.imageAsset</valueSourceReference>

               </primitiveValues>

             </layoutItems>

             <layoutItems>

               <collectionType>None</collectionType>

               <name>title</name>

               <primitiveValues>

                  <type>SourcePrimitiveValue</type>

                  <valueSourceReference>Constants.Title</valueSourceReference>

               </primitiveValues>

             </layoutItems>

           </compositeValues>

           <name>message</name>

        </layoutItems>

        <layoutItems>

           <collectionType>DynamicList</collectionType>

           <compositeValues>

             <compositeTypeName>TitleOptionItem</compositeTypeName>

             <layoutItems>

               <collectionType>None</collectionType>

               <compositeValues>

                  <compositeTypeName>TitleImageItem</compositeTypeName>

                  <layoutItems>

                    <collectionType>None</collectionType>

```


Metadata Types ConversationMessageDefinition

```
                    <name>imageId</name>

                    <primitiveValues>

                       <type>SourcePrimitiveValue</type>

   <valueSourceReference>Constants.Options.ListItem.Image</valueSourceReference>

                    </primitiveValues>

                  </layoutItems>

                  <layoutItems>

                    <collectionType>None</collectionType>

                    <name>title</name>

                    <primitiveValues>

                       <type>SourcePrimitiveValue</type>

   <valueSourceReference>Constants.Options.ListItem.Title</valueSourceReference>

                    </primitiveValues>

                  </layoutItems>

               </compositeValues>

               <name>titleItem</name>

             </layoutItems>

             <valueSourceReference>Constants.Options</valueSourceReference>

           </compositeValues>

           <name>optionItems</name>

        </layoutItems>

        <layoutItems>

           <collectionType>None</collectionType>

           <compositeValues>

             <compositeTypeName>TitleImageItem</compositeTypeName>

             <layoutItems>

               <collectionType>None</collectionType>

               <name>imageId</name>

               <primitiveValues>

                  <type>SourcePrimitiveValue</type>

                  <valueSourceReference>Constants.imageAsset</valueSourceReference>

               </primitiveValues>

             </layoutItems>

             <layoutItems>

               <collectionType>None</collectionType>

               <name>title</name>

               <primitiveValues>

                  <type>SourcePrimitiveValue</type>

                  <valueSourceReference>Constants.message</valueSourceReference>

               </primitiveValues>

             </layoutItems>

           </compositeValues>

           <name>reply</name>

        </layoutItems>

        <layoutItems>

           <collectionType>None</collectionType>

           <name>title</name>

           <primitiveValues>

             <type>SourcePrimitiveValue</type>

             <valueSourceReference>Constants.Title</valueSourceReference>

           </primitiveValues>

```


Metadata Types ConversationMessageDefinition

```
        </layoutItems>

        <messageType>Choices</messageType>

      </messageLayouts>

      <messageLayouts>

        <formatType>Carousel</formatType>

        <layoutItems>

           <collectionType>DynamicList</collectionType>

           <compositeValues>

             <compositeTypeName>TitleItemWithInteractions</compositeTypeName>

             <layoutItems>

               <collectionType>StaticList</collectionType>

               <compositeValues>

                  <compositeTypeName>TitleOptionItem</compositeTypeName>

                  <layoutItems>

                    <collectionType>None</collectionType>

                    <compositeValues>

                       <compositeTypeName>TitleItem</compositeTypeName>

                       <layoutItems>

                         <collectionType>None</collectionType>

                         <name>title</name>

                         <primitiveValues>

                           <literalValue>Select One</literalValue>

                           <type>Literal</type>

                         </primitiveValues>

                       </layoutItems>

                    </compositeValues>

                    <name>titleItem</name>

                  </layoutItems>

               </compositeValues>

               <name>interactionItems</name>

             </layoutItems>

             <layoutItems>

               <collectionType>None</collectionType>

               <compositeValues>

                  <compositeTypeName>TitleImageItem</compositeTypeName>

                  <layoutItems>

                    <collectionType>None</collectionType>

                    <name>imageId</name>

                    <primitiveValues>

                       <type>SourcePrimitiveValue</type>

   <valueSourceReference>Constants.Options.ListItem.Image</valueSourceReference>

                    </primitiveValues>

                  </layoutItems>

                  <layoutItems>

                    <collectionType>None</collectionType>

                    <name>subTitle</name>

                    <primitiveValues>

                       <type>SourcePrimitiveValue</type>

   <valueSourceReference>Constants.Options.ListItem.SubTitle</valueSourceReference>

                    </primitiveValues>

                  </layoutItems>

                  <layoutItems>

```


Metadata Types ConversationMessageDefinition

```
                    <collectionType>None</collectionType>

                    <name>title</name>

                    <primitiveValues>

                       <type>SourcePrimitiveValue</type>

                     <valueSourceReference>Constants.Title</valueSourceReference>

                    </primitiveValues>

                  </layoutItems>

               </compositeValues>

               <name>titleItem</name>

             </layoutItems>

             <valueSourceReference>Constants.Options</valueSourceReference>

           </compositeValues>

           <name>items</name>

        </layoutItems>

        <messageType>Choices</messageType>

      </messageLayouts>

      <messageLayouts>

        <formatType>Text</formatType>

        <layoutItems>

           <collectionType>None</collectionType>

           <name>text</name>

           <primitiveValues>

             <formulaTemplate>{!$Constants.Title}

   {!$Constants.Prompt1}:

   {!$ListTemplates.OptionsList}</formulaTemplate>

             <mergeFields>

               <formulaTemplate>{!$ListItem.Index}.

   {!$ListItem.Value.Title}{!BR()}</formulaTemplate>

               <mergeFieldType>ListTemplate</mergeFieldType>

               <name>OptionsList</name>

               <valueSourceReference>Constants.Options</valueSourceReference>

             </mergeFields>

             <type>FormulaTemplate</type>

           </primitiveValues>

        </layoutItems>

        <messageType>StaticContent</messageType>

      </messageLayouts>

      <type>Picklist</type>

   </ConversationMessageDefinition>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>Favourite_Month</members>

        <name>ConversationMessageDefinition</name>

      </types>

      <version>61.0</version>

   </Package>

```


### Metadata Types ConversationMessageDefinitionTranslation

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### ConversationMessageDefinitionTranslation

Represents translated labels and constant values for conversation message definitions in Enhanced Messaging and Messaging for In-App
and Web.

Note: This complex type is used as a nested element within the ConversationMessageDefinition metadata type and is not deployed
as a standalone metadata component. It enables multilingual support by allowing constant values and labels to be translated into
different languages for customer-facing messaging.

Parent Type

This type is used as a nested complex type within the ConversationMessageDefinition on page 656 metadata type.

Version

### ConversationMessageDefinitionTranslation is available in API version 61.0 and later.

Fields


Metadata Types ConversationMessageDefinitionTranslation

ConversationMessageConstantValueTranslation

Represents a translated constant value for conversation message definitions. Available in API version 61.0 and later.

Usage Example

This complex type is used within ConversationMessageDefinition to provide translations. Here's an example context:

```
<?xml version="1.0" encoding="UTF-8"?>

<ConversationMessageDefinition xmlns="http://soap.sforce.com/2006/04/metadata">

   <fullName>Welcome_Message</fullName>

   <label>Welcome Message</label>

   <conversationMessageDefinitionTranslations>

     <constantValueTranslations>

        <name>greeting_text</name>

        <value>Bienvenido</value>

     </constantValueTranslations>

     <label>Mensaje de Bienvenida</label>

     <name>Welcome_Message</name>

   </conversationMessageDefinitionTranslations>

</ConversationMessageDefinition>

```


### Metadata Types ConversationVendorInfo ConversationVendorInfo

Represents the connection between the partner vendor system and the Service Cloud feature. For example, for Service Cloud Voice, this
type contains information about the partner telephony system or Contact Center as a Service (CCaaS) system. For Bring Your Own
Channel for Messaging or Bring Your Own Channel for CCaaS, this type contains information about the partner messaging system or
CCaaS system.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### ConversationVendorInfo components have the suffix .ConversationVendorInformation and are stored in the ConversationVendorInformation folder.

Version

### ConversationVendorInfo components are available in API version 52.0 and later.

Special Access Rules

This type requires an add-on license for Service Cloud Voice for Partner Telephony or Digital Engagement.

Fields

The fields in the ConversationVendorInfo type apply to all Service Cloud features unless otherwise stated in the field description. For
example, if a field applies to just one Service Cloud Voice telephony model setup or is applied differently by different partner systems,
this is stated in the field description.

**Field Name** **Description**

```
agentSSOSupported

```

**Field Type**
boolean

**Description**
If set to `true`, agents can single sign-on (SSO) into their contact center using Salesforce
as the identity provider (IdP). Behind the scenes, Salesforce is used as the SAML IdP in
the Single Sign-On connected app for the contact center. If set to `false`, an IdP other
than Salesforce is used or an IdP isn’t used at all. The default value is `false` .

If this value is set to `false` and you want to use Salesforce as the IdP for your contact
center, set this value and the `namedCredentialSupported` value to `true`
and configure the `service_cloud_voice.PartnerSSO` interface in your
Apex integration class.


Metadata Types ConversationVendorInfo

**Field Name** **Description**

Available in API version 53.0 and later.

Applies to the following implementations:

**•** Service Cloud Voice with Partner Telephony

**•** Service Cloud Voice with Partner Telephony from Amazon Connect

**•** Bring Your Own Channel for CCaaS

```
awsAccountKey

awsRootEmail

awsTenantVersion

bridgeComponent

```

**Field Type**
string

**Description**
The 12-digit AWS subaccount ID that’s automatically provisioned for you when Service
Cloud Voice was turned on. Available in API version 55.0 and later.

Applies to the following implementation:

**•** Service Cloud Voice with Amazon Connect

**Field Type**
string

**Description**
The email address used by Salesforce to create the root user for the provisioned AWS
subaccount when Service Cloud Voice was turned on. Available in API version 55.0
and later.

Applies to the following implementation:

**•** Service Cloud Voice with Amazon Connect

**Field Type**
double

**Description**
The version number of the SVCTenantStack AWS CloudFormation stack that’s deployed.
The stack is deployed in AWS region "us-east-1". Available in API version 55.0 and later.

Applies to the following implementation:

**•** Service Cloud Voice with Amazon Connect

**Field Type**
string

**Description**
The Lightning component used to communicate between the telephony or messaging
system and other Lightning components.

Applies to the following implementations:

**•** Service Cloud Voice with Partner Telephony

**•** Service Cloud Voice with Partner Telephony from Amazon Connect

**•** Bring Your Own Channel for CCaaS


Metadata Types ConversationVendorInfo

**Field Name** **Description**

```
clientAuthMode

connectorUrl

customConfig

customIcon

```

**Field Type**
ClientAuthMode (enumeration of type string)

**Description**
The client authentication mode.

Values are:

**•** `Custom`

**•** `Mixed`

**•** `SSO`

Applies to the following implementations:

**•** Service Cloud Voice with Partner Telephony

**•** Service Cloud Voice with Partner Telephony from Amazon Connect

**Field Type**
string

**Description**
The URL that hosts your Service Cloud Voice or Bring Your Own Channel for CCaaS
connector. This value could be a Visualforce page or a public URL.

Applies to the following implementations:

**•** Service Cloud Voice with Partner Telephony

**•** Service Cloud Voice with Partner Telephony from Amazon Connect

**•** Bring Your Own Channel for CCaaS

**Field Type**
string

**Description**
The foreign key to the CustomEntityDefinition, which contains partner-specific custom
settings. Available in API version 53.0 and later.

Applies to the following implementations:

**•** Service Cloud Voice with Partner Telephony

**•** Service Cloud Voice with Partner Telephony from Amazon Connect

**•** Bring Your Own Channel for CCaaS

**Field Type**
string

**Description**
ID of the static resource used to identify the contact center integration, such as a
Contact Center as a Service (CCaaS) provider logo. The static resource must be in SVG
format. This field is optional. Available in API version 62.0 and later.

Applies to the following implementations:

**•** Service Cloud Voice with Partner Telephony


Metadata Types ConversationVendorInfo

**Field Name** **Description**

**•** Bring Your Own Channel for CCaaS

```
customLoginUrl

developerName

einsteinConversationInsightsSupported

integrationClass

integrationClassName

```

**Field Type**
string

**Description**
The URL that hosts your telephony system or CCaaS system login page.

Applies to the following implementations:

**•** Service Cloud Voice with Partner Telephony

**•** Service Cloud Voice with Partner Telephony from Amazon Connect

**•** Bring Your Own Channel for CCaaS

**Field Type**
string

**Description**
The unique name of the type in the API.

**Field Type**
boolean

**Description**
If set to `true`, Einstein Conversation Insights is turned on. The default value is `false` .
Available in API version 53.0 and later.

Applies to the following implementations:

**•** Service Cloud Voice with Partner Telephony

**•** Service Cloud Voice with Partner Telephony from Amazon Connect

**Field Type**
string

**Description**
The foreign key to the partner Apex class implementing supported interfaces. Available
in API version 53.0 and later.

Applies to the following implementations:

**•** Service Cloud Voice with Partner Telephony

**•** Service Cloud Voice with Partner Telephony from Amazon Connect

**•** Bring Your Own Channel for CCaaS

**Field Type**
string

**Description**
Deprecated in API version 53.0. Don't set this field. Instead, use
`integrationClass` .

Applies to the following implementations:


Metadata Types ConversationVendorInfo

**Field Name** **Description**

**•** Service Cloud Voice with Partner Telephony

**•** Service Cloud Voice with Partner Telephony from Amazon Connect

```
intelligenceSupported

isTaxCompliant

keyProvisioningSupported

masterLabel

```

**Field Type**
boolean

**Description**
If set to `true`, Salesforce ingests real-time signals sent from a partner telephony
system. If set to `false`, Salesforce won't ingest real-time intelligence signals from a
partner telephony system. The default value is `false` . Available in API version 59.0
and later.

Applies to the following implementations:

**•** Service Cloud Voice with Partner Telephony

**Field Type**
boolean

**Description**
Indicates whether the Amazon tax settings for the AWS subaccount provisioned for
Service Cloud Voice have been confirmed ( `true` ). The default value is `false` .
Available in API version 55.0 and later.

Applies to the following implementation:

**•** Service Cloud Voice with Amazon Connect

**Field Type**
boolean

**Description**
If set to `true`, key provisioning and renewal are automated. The default value is
`false` . Available in API version 54.0 and later.

Applies to the following implementations:

**•** Service Cloud Voice with Partner Telephony

**•** Service Cloud Voice with Partner Telephony from Amazon Connect

**Field Type**
string

**Description**
The partner vendor's display name as it appears in the UI. This name appears in several
places in the UI, so include the partner vendor name for easy identification. For Service
Cloud Voice, this label also represents the telephony provider name in the contact
center record.

For Service Cloud Voice with Amazon Connect, this field is always set to `Service`
`Cloud Voice` .


Metadata Types ConversationVendorInfo

**Field Name** **Description**

```
namedCredential

namedCredentialSupported

partnerContactCenterListSupported

partnerPhoneNumbersSupported

```

**Field Type**
string

**Description**
A sample-named credential that can be used for Apex callouts to the partner system.
Available in API version 53.0 and later.

Applies to the following implementations:

**•** Service Cloud Voice with Partner Telephony

**•** Service Cloud Voice with Partner Telephony from Amazon Connect

**•** Bring Your Own Channel for CCaaS

**Field Type**
boolean

**Description**
A sample-named credential that can be used for Apex callouts to the partner system.
Available in API version 53.0 and later.

Applies to the following implementations:

**•** Service Cloud Voice with Partner Telephony

**•** Service Cloud Voice with Partner Telephony from Amazon Connect

**•** Bring Your Own Channel for CCaaS

**Field Type**
boolean

**Description**
If set to `true`, enables the customer to select one contact center from a list of multiple
contact centers to connect with Salesforce. The default value is `false` . Available in
API version 53.0 and later.

Applies to the following implementations:

**•** Service Cloud Voice with Partner Telephony

**•** Service Cloud Voice with Partner Telephony from Amazon Connect

**•** Bring Your Own Channel for CCaaS

**Field Type**
boolean

**Description**
If set to `true`, displays a list of phone numbers used to create contact center channels.
The default value is `false` . Available in API version 54.0 and later.

Applies to the following implementations:

**•** Service Cloud Voice with Partner Telephony

**•** Service Cloud Voice with Partner Telephony from Amazon Connect


Metadata Types ConversationVendorInfo

**Field Name** **Description**

```
partnerTransferDestinationsSupported

queueManagementSupported

serverAuthMode

telephonySettingsComponent

```

**Field Type**
boolean

**Description**
If set to `true`, allows Salesforce to fetch contact center queues so that Salesforce and
contact center queues can be mapped. The default value is `false` . Available in API
version 53.0 and later.

Applies to the following implementations:

**•** Service Cloud Voice with Partner Telephony

**•** Service Cloud Voice with Partner Telephony from Amazon Connect

**•** Bring Your Own Channel for CCaaS

**Field Type**
boolean

**Description**
If set to `true`, support queue management. The default value is `false` . Available
in API version 56.0 and later.

Applies to the following implementations:

**•** Service Cloud Voice with Partner Telephony

**•** Service Cloud Voice with Partner Telephony from Amazon Connect

**•** Bring Your Own Channel for CCaaS

**Field Type**
ServerAuthMode (enumeration of type string)

**Description**
Deprecated in API 53.0. Server authentication mode. Set this value to `None` .

Values are:

**•** `None`

**•** `OAuth`

Applies to the following implementations:

**•** Service Cloud Voice with Partner Telephony

**•** Service Cloud Voice with Partner Telephony from Amazon Connect

**Field Type**
string

**Description**
The name of the Lightning Web Component (LWC) that is used to display additional
agent settings in the Omni-Channel widget. This value is in the format
`mynamespace:componentName`, where `mynamespace` is the namespace
associated with the Service Cloud Voice package that was created, and
`componentName` is the FQDN of the Lightning component.


Metadata Types ConversationVendorInfo

**Field Name** **Description**

Available in API version 54.0 and later.

Applies to the following implementation:

**•** Service Cloud Voice with Partner Telephony

```
unifiedRoutingSupported

(Beta)

universalCallRecordingAccessSupported

userSyncingSupported

vendorType

```

**Field Type**
boolean

**Description**
Indicates whether unified routing is supported ( `true` ) or not supported ( `false` ) for
voice calls in voice channels. The default value is `false` . Once this value is set to
`true`, it can’t be changed to `false` .

Available in API version 63.0 and later.

Applies to the following implementation:

**•** Service Cloud Voice with Partner Telephony

**Field Type**
boolean

**Description**
If set to `true`, Universal Call Recording Access is turned on. The default value is
`false` .

If this value is set to `false` and you want to turn on Universal Call Recording, set
this value to `true` and configure the service_cloud_voice.RecordingMediaProvider
interface in your Apex integration class.

Available in API version 54.0 and later.

Applies to the following implementations:

**•** Service Cloud Voice with Partner Telephony

**•** Service Cloud Voice with Partner Telephony from Amazon Connect

**Field Type**
boolean

**Description**
If set to `true`, supports automated user syncing whenever a user is added to or
removed from a contact center. The default value is `false` . Available in API version
53.0 and later.

Applies to the following implementations:

**•** Service Cloud Voice with Partner Telephony

**•** Service Cloud Voice with Partner Telephony from Amazon Connect

**•** Bring Your Own Channel for CCaaS

**Field Type**
ConversationVendorType (enumeration of type string)


Metadata Types ConversationVendorInfo

**Field Name** **Description**

**Description**
The Service Cloud feature the partner vendor supports.

Possible values are:

**•** `Amazon_Connect`                     - For Service Cloud Voice with Amazon Connect.

**•** `BringYourOwnChannelPartner`                     - For Bring Your Own Channel for
Messaging. Available in API version 60.0 and later.

**•** `BringYourOwnContactCenter`                     - For Bring Your Own Channel for Contact
Center as a Service (CCaaS). Available in API version 60.0 and later.

**•** `ServiceCloudVoicePartner`                     - For Service Cloud Voice with Partner
Telephony or Service Cloud Voice with Partner Telephony from Amazon Connect.

Available in API version 53.0 and later.

Declarative Metadata Sample Definition

The following is an example of a ConversationVendorInfo component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ConversationVendorInfo xmlns="http://soap.sforce.com/2006/04/metadata"

   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

      <einsteinConversationInsightsSupported>true</einsteinConversationInsightsSupported>

      <partnerContactCenterListSupported>true</partnerContactCenterListSupported>

      <namedCredentialSupported>true</namedCredentialSupported>

      <partnerTransferDestinationsSupported>true</partnerTransferDestinationsSupported>

      <agentSSOSupported>true</agentSSOSupported>

      <keyProvisioningSupported>true</keyProvisioningSupported>

      <universalCallRecordingAccessSupported>true</universalCallRecordingAccessSupported>

      <partnerPhoneNumbersSupported>true</partnerPhoneNumbersSupported>

      <queueManagementSupported>true</queueManagementSupported>

      <clientAuthMode>SSO</clientAuthMode>

      <connectorUrl>https://exampleconnectorurl.com</connectorUrl>

      <customConfig>exampleCustomConfig__c</customConfig>

      <customLoginUrl>testurl</customLoginUrl>

      <integrationClass>ExampleIntegrationImpl</integrationClass>

      <masterLabel>Example Partner Name</masterLabel>

      <developerName>exampledevname</developerName>

      <namedCredential>exampleNamedCredential</namedCredential>

      <userSyncingSupported>true</userSyncingSupported>

      <vendorType>BringYourOwnContactCenter</vendorType>

   </ConversationVendorInfo>

```

The following is an example `package.xml` that references the previous definition.

```
   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>ConversationVendorInfo</name>

      </types>

```


### Metadata Types ConvIntelligenceSignalRule

```
      <version>59.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### ConvIntelligenceSignalRule

Represents the conversation intelligence signal rule. The rule triggers actions based on real-time intelligence signals from your telephony
system or keywords mentioned by support reps or customers. The rule contains a set of conditions (subrules) and the filter logic used
to evaluate those conditions to determine whether to trigger actions.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### ConvIntelligenceSignalRule components have the suffix .ConvIntelligenceSignalRule and are stored in the ConvIntelligenceSignalRule folder.

Version

### ConvIntelligenceSignalRule components are available in API version 62.0 and later.

Special Access Rules

This type requires an add-on license for Service Cloud Voice for Amazon Connect, Service Cloud Voice for Partner Telephony with Amazon
Connect, Service Cloud Voice for Partner Telephony, or Digital Engagement.

Fields

**Field Name** **Description**

```
actionType

```

**Field Type**
ConvIntelligenceActionType (enumeration of type string)

**Description**

Required. The conversation intelligence signal type. Values are:

**•** `AlertSupervisor` –Sends an alert to the supervisor.

**•** `AlertSupervisorAndAgent` –Sends an alert to the rep and supervisor.

**•** `LaunchFlow` –Triggers an auto-launched flow. If set, also set `ActionValue` .


Metadata Types ConvIntelligenceSignalRule

**Field Name** **Description**

**•** `LaunchNBA` –Recommends the next best action to the rep.

```
actionValue

active

channelAddressIdentifier

channelType

criteria

```

**Field Type**
string

**Description**

Action to perform based on the `actionType` specified.

If `actionType` is set to LaunchFlow, this value is the `developerName` of the
flow to be launched. For example, EmailAlert.

For all other `actionType` values, don’t set this parameter.

**Field Type**
boolean

**Description**
Required. Indicates whether the conversation intelligence signal rule is active ( `true` )
or inactive ( `false` ). The default value is `false` .

**Field Type**
string

**Description**

Required. ID ( `ChannelAddressIdentifier` ) of the Messaging channel or name
( `InternalName` ) of the Voice channel.

**Field Type**
string

**Description**

Required. Channel type.

For Messaging, possible values are:

**•** `AppleBusinessChat` —Represents Apple Messages for Business.

**•** `Custom` —Represents Bring Your Own Channel for Messaging or Bring Your Own
Channel for CCaaS.

**•** `EmbeddedMessaging` —Represents Messaging for In-App and Web.

**•** `Facebook`

**•** `Text`

**•** `WhatsApp`

For Voice, set this parameter to `Phone` .

**Field Type**
string


Metadata Types ConvIntelligenceSignalRule

**Field Name** **Description**

**Description**
Required. Filter logic applied to the rule conditions (subrules). For example, ((1 AND
2) OR 3). The numbers in the formula are derived from the
`ConvIntelligenceSignalSubRule.order` value plus 1. For example, filter
logic (1 AND 2) is calculated by adding the first condition ( `order` =0) with the second
condition ( `order` =1).

```
developerName

participantRole

ruleName

service

subrule

```

**Field Type**
string

**Description**
Required. API name of the conversation intelligence signal rule.

**Field Type**
ConvParticipantRole (enumeration of type string)

**Description**
If `service` is set to KeywordMatch, this value determines whether the rule applies
to utterances made by reps, customers, or both roles. Possible values are:

Possible values are:

**•** `Agent`

**•** `AgentOrCustomer`

**•** `Customer`

If `Service` is not set to KeywordMatch, don’t set this parameter.

**Field Type**
string

**Description**
Required. Name of the conversation intelligence signal rule.

**Field Type**
ConvIntelligenceService (enumeration of type string)

**Description**

Required. Salesforce- or partner-provided intelligence source.

For Salesforce-provided intelligence sources, set this parameter to `KeywordMatch` .

For partner-provided intelligence sources, possible values are:

**•** `KeywordMatch`

**•** `AmazonConnectContactLens`

If none of the options apply to you, contact your Salesforce representative for the
service name.

**Field Type**

ConvIntelligenceSignalSubRule[]


Metadata Types ConvIntelligenceSignalRule

**Field Name** **Description**

**Description**
A set of intelligence rules used to measure an agent or customer’s sentiment during
a voice call.

ConvIntelligenceSignalSubRule

Represents a condition (subrule) within a conversation intelligence signal rule.

**Field Name** **Description**

```
operandValue

operator

order

type

```

**Field Type**
string

**Description**

Required. Value of the signal type used to determine if the rule condition is met.

**Field Type**
ConvIntelligenceOperator (enumeration of type string)

**Description**
Required. Filter logic operator used to determine if the rule condition is met. Possible
values are:

**•** `Equals`

**•** `GreaterThan`

**•** `In`

**•** `LessThan`

**•** `NotEquals`

**Field Type**
int

**Description**

Required. Order the condition appears in relation to the other conditions in the list,
with zero (0) being the first condition listed. If `type` is set to Keyword, the maximum
value is 24. For all other `type` values, the maximum value is 4. This value is used when
applying filter logic to the rule.

**Field Type**
ConvIntelligenceType (enumeration of type string)

**Description**

Required. Type of conversation intelligence signal used by the rule to determine
whether to trigger an action. This value depends on the
`ConvIntelligenceSignalRule.channelType` and
`ConvIntelligenceSignalRule.service` values.


Metadata Types ConvIntelligenceSignalRule

**Field Name** **Description**

If `service` is set to KeywordMatch, possible values are:

**•** `Keyword` –A word or group of words spoken or typed.

If `service` is set to `AmazonConnectContactLens`, possible values are:

**•** `Category` –Category name defined in your telephony system.

If `service` is set to another value, contact your Salesforce representative for the
conversation intelligence signal types available for your intelligence source.

Declarative Metadata Sample Definition

The following is an example of a ConvIntelligenceSignalRule component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ConvIntelligenceSignalRule xmlns="http://soap.sforce.com/2006/04/metadata">

      <actionType>AlertSupervisor</actionType>

      <active>true</active>

   <channelAddressIdentifier>a12bc345-1303-44c2-866c-f30d546b58de</channelAddressIdentifier>

      <channelType>Phone</channelType>

      <criteria>1 OR 2</criteria>

      <developerName>ConvIntelligenceRuleAPIName</developerName>

      <participantRole>AgentOrCustomer</participantRole>

      <ruleName>ConvIntelligenceRuleName</ruleName>

      <service>KeywordMatch</service>

      <subrule>

        <operandValue>escalate_level_1</operandValue>

        <operator>Equals</operator>

        <order>0</order>

        <type>Keyword</type>

      </subrule>

      <subrule>

        <operandValue>escalate_level_2</operandValue>

        <operator>Equals</operator>

        <order>1</order>

        <type>Keyword</type>

      </subrule>

   </ConvIntelligenceSignalRule>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>ConversationIntelligenceSignalRule</name>

      </types>

      <version>62.0</version>

   </Package>

```


### Metadata Types CorsWhitelistOrigin

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### CorsWhitelistOrigin

Represents an origin in the CORS allowlist.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this metadata type’s name.

File Suffix and Directory Location

### CorsWhitelistOrigin components have the suffix .corswhitelistorigin and are stored in the corswhitelistorigins

folder.

Version

### CorsWhitelistOrigin components are available in API version 32.0 and later.

Fields

**Field Name** **Field Type** **Description**

`urlPattern` String

A URL pattern for the origin.

The origin URL pattern must include the HTTPS protocol and a domain
name, and can include a port. The wildcard character (*) is supported

and must be in front of a second-level domain name. For example,
`https://*.example.com` adds all subdomains of
`example.com` to the allowlist.

Google Chrome [™] and Mozilla [®] Firefox [®] browser extensions are also
allowed as resources in API version 53 and later. Chrome extensions
must use the prefix `chrome-extension://` and 32 characters
without digits or capital letters, for example
`chrome-extension://abdkkegmcbiomijcbdaodaflgehfffed` .
Firefox extensions must use the prefix `moz-extension://` and
an 8-4-4-4-12 format of small alphanumeric characters, for example
`moz-extension://1234ab56-78c9-1df2-3efg-4567891hi1j2` .

The origin URL pattern can be an IP address. But an IP address and a
domain that resolve to the same address aren’t the same origin, and
you must add them to the CORS allowlist as separate entries.


### Metadata Types CspTrustedSite

Declarative Metadata Sample Definition

Here’s an example package manifest used to deploy or retrieve the CorsWhitelistOrigin metadata for an organization.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>CorsWhitelistOrigin</name>

      </types>

      <version>32.0</version>

   </Package>

```

Here’s an example of a CorsWhitelistOrigin component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CorsWhitelistOrigin xmlns="http://soap.sforce.com/2006/04/metadata">

      <developerName>CorsWhitelistEntry1</developerName>

      <urlPattern>https://*.example.com</urlPattern>

   </CorsWhitelistOrigin>

```

Usage

[CORS (cross-origin resource sharing) is a W3C recommendation that enables Web browsers to request resources from origins other than](http://www.w3.org/TR/cors/)
their own. For example, using CORS, a JavaScript script at `https://www.example.com` could request a resource from
`https://www.salesforce.com` .

If a browser that supports CORS makes a request to an origin in your allowlist, Salesforce returns the origin in the
`Access-Control-Allow-Origin` HTTP header, along with any additional CORS HTTP headers. If the origin isn’t allow listed,
Salesforce returns HTTP status code 404.

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### CspTrustedSite

Represents a trusted URL. For each CspTrustedSite component, you can specify Content Security Policy (CSP) directives and permissions
policy directives. Each CSP directive allows Lightning components, third-party APIs, and WebSocket connections to access a resource
type from the trusted URL. If the Permissions-Policy HTTP header is enabled, each permissions policy directive grants the trusted URL
access to a browser feature. In API version 58.0 and earlier, CspTrustedSite components included only CSP directives and were referred
to as CSP Trusted Sites.

This type extends the Metadata metadata type and inherits its `fullName` field.

Declarative Metadata File Suffix and Directory Location

### CspTrustedSite components are stored in the cspTrustedSites directory of the corresponding package directory. The file name

matches the unique name of the trusted site, and the extension is `.cspTrustedSite` .


Metadata Types CspTrustedSite

Version

CspTrustedSite components are available in API version 39.0 and later.

Fields

**Field** **Field Type** **Description**

`canAccessCamera` boolean

`canAccessMicrophone` boolean

Indicates whether this CspTrustedSite can access the user’s
camera ( `true` ) or not ( `false` ). The default value is `false` .

This field takes effect only when the
`enablePermissionsPolicy` field equals `true` and

the `grantCameraAccess` field equals `TrustedUrls`
in the SecuritySettings metadata API type.

This field is available in API version 59.0 and later.

Indicates whether this CspTrustedSite can access the user’s
microphone ( `true` ) or not ( `false` ). The default value is
`false` .

This field takes effect only when the
`enablePermissionsPolicy` field equals `true` and

the `grantMicrophoneAccess` field equals
`TrustedUrls` in the SecuritySettings metadata API type.

This field is available in API version 59.0 and later.

`context` CspTrustedSiteContext Declares the scope of the CSP directives for this trusted URL.
(enumeration of type string)

**•** `All` —Apply the CSP directives to all supported context
types.

**•** `Communities` —Apply the CSP directives to Experience
Builder sites only.

**•** `FieldServiceMobileExtension` —Apply the CSP
directives to the Field Service Mobile Extensions only. This
value is available in API version 47.0 and later.

**•** `LEX` —Apply the CSP directives to Lightning Experience
pages only.

**•** `LightningOut` —Reserved for future use. Available in
API version 64.0 and later

**•** `VisualForce` —Apply the CSP directives to custom
Visualforce pages only. This value is available in API version
55.0 and later.

For custom Visualforce pages, content is restricted to trusted
URLs only if the page’s `cspHeader` attribute is set to `true` .

This field is available in API version 44.0 and later.

`description` string The description of this trusted URL.


Metadata Types CspTrustedSite

**Field** **Field Type** **Description**

`endpointUrl` string

Required. The URL for this CspTrustedSite.

This field must include a domain name and can include a port.
For example, `https://example.com` or
`https://example.com:8080` .

To reduce repetition, you can use the wildcard character `*`
(asterisk). For example, `*.example.com` . For a third-party
API, the URL must begin with https://. For example,
`https://example.com` . For a WebSocket connection,
the URL must begin with wss://. For example,
`wss://example.com` .

Otherwise, the URL cannot be malformed. Examples of
malformed URLs that fail a syntax check are
`malformed^url.example.com`, and
`https://{subdomain}.example.com` .

To add an `EndpointUrl` based on parameters, build the
URL before you add it to this Metadata Type.

`isActive` boolean Required. Indicates whether this CspTrustedSite is active ( `true` )
or not ( `false` ). The default value is `true` .

`isApplicableToConnectSrc` boolean Indicates whether Lightning components, third-party APIs, and
WebSocket connections can load URLs using script interfaces

from this trusted URL ( `true` ) or not ( `false` ). This field has a
default value of `false` .

This field is available in API version 48.0 and later.

`isApplicableToFontSrc` boolean

Indicates whether Lightning components, third-party APIs, and
WebSocket connections can load fonts from this trusted URL
( `true` ) or not ( `false` ). This field has a default value of `false` .

This field is available in API version 48.0 and later.

`isApplicableToFrameSrc` boolean Indicates whether Lightning components, third-party APIs, and
WebSocket connections can load resources contained in

`<iframe>` elements from this trusted URL ( `true` ) or not
( `false` ). This field has a default value of `false` .This field is
available in API version 48.0 and later.

`isApplicableToImgSrc` boolean Indicates whether Lightning components, third-party APIs, and
WebSocket connections can load images from this trusted URL

( `true` ) or not ( `false` ). This field has a default value of `false` .
This field is available in API version 48.0 and later.

`isApplicableToMediaSrc` boolean Indicates whether Lightning components, third-party APIs, and
WebSocket connections can load audio and video from this

trusted URL ( `true` ) or not ( `false` ). This field has a default
value of `false` .


Metadata Types CspTrustedSite

**Field** **Field Type** **Description**

In API version 59.0 and later, for each trusted URL, at least one
CSPTrustedSite starting with `isApplicable` or
`canAccess` must be set to `true.`

In API version 50.0 to 58.0, if all `isApplicable` fields are
`false`, the `isApplicableToImgSrc` field is set to
`true` . In API version 49.0 and earlier, if all `isApplicable`
fields are `false`, these fields all default to `true` .

This field is available in API version 48.0 and later.

`isApplicableToStyleSrc` boolean Indicates whether Lightning components, third-party APIs, and
WebSocket connections can load style sheets from this trusted

URL ( `true` ) or not ( `false` ). This field has a default value of
`false` . This field is available in API version 48.0 and later.

`mobileExtension` string Reserved for future use.

Declarative Metadata Sample Definition

A sample XML definition of a trusted site is shown below.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CspTrustedSite xmlns="http://soap.sforce.com/2006/04/metadata">

      <canAccessCamera>false</canAccessCamera>

      <canAccessMicrophone>true</canAccessMicrophone>

      <description>Used for Lightning component callout to mapping web service</description>

      <context>LEX</context>

      <endpointUrl>https://www.maptestsite.net/</endpointUrl>

      <isActive>true</isActive>

      <isApplicableToConnectSrc>true</isApplicableToConnectSrc>

      <isApplicableToFontSrc>true</isApplicableToFontSrc>

      <isApplicableToFrameSrc>false</isApplicableToFrameSrc>

      <isApplicableToImgSrc>true</isApplicableToImgSrc>

      <isApplicableToMediaSrc>false</isApplicableToMediaSrc>

      <isApplicableToStyleSrc>true</isApplicableToStyleSrc>

   </CspTrustedSite>

```

Usage

For each CSPTrustedSite component, at least one field starting with `grantAccess` or `isApplicableTo` must be set to `true.`

In API versions 50.0 to 58.0, if all `isApplicable` fields are `false`, the `isApplicableToImgSrc` field is set to `true` . In API
version 49.0 and earlier, if all `isApplicable` fields are `false`, those fields all default to `true` .

To ensure smooth integration across Salesforce products, Salesforce includes URLs in each of the CSP directives that correspond to the
`isApplicable` fields, even though those URLs aren’t defined as CspTrustedSite components. Salesforce regularly updates those
URLs based on the latest requirements.


### Metadata Types CustomApplication

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### CustomApplication CustomApplication represents a custom or standard application. In API version 29.0 and earlier, CustomApplication represents only a

custom application. An application is a list of tab references, with a description and a logo. This type extends the Metadata metadata
type and inherits its `fullName` field.

File Suffix and Directory Location

Custom and standard applications have the suffix `.app` and are stored in the `applications` folder.

Note: Retrieving a component of this metadata type in a project makes the component appear in any Profile and PermissionSet
components that are retrieved in the same package.

Version

Custom applications are available in API version 10.0 and later. Standard applications are available in API version 30.0 and later.

Fields

**Field Name** **Field Type** **Description**

`actionOverrides` AppActionOverride[]

`brand` AppBrand

`consoleConfig` ServiceCloudConsoleConfig

Represents an action override for an application. Use it
to create, update, edit, or delete action overrides.

This field is available for Lightning Experience in API
version 38.0 and later.

The color scheme and logo used for the app.

This field is available for Lightning Experience in API
version 38.0 and later.

Represents configuration settings for a Salesforce console
app.

This field is available in API version 42.0 and later.

`defaultLandingTab` string The `fullName` of a standard tab or custom tab that
opens when this application is selected.

`description` string The optional description text of the application.


Metadata Types CustomApplication

**Field Name** **Field Type** **Description**

`formFactors` FormFactor (enumeration of type Indicates the form factors for which the app is visible for
string) Lightning Experience. Valid values are:

**•** `Null` (no value)—For a desktop using Salesforce
Classic

**•** `Small` —For a mobile device using the Salesforce
mobile app

**•** `Medium` —Reserved for future use

**•** `Large` —For a desktop using Lightning Experience

This field is available in API version 38.0 and later.

As of API version 38.0, `formFactors` is set to `Large`
for existing Salesforce Classic apps, except for Salesforce
Classic consoles. Salesforce Classic apps installed from
packages created before API version 38.0 also have
`formFactors` set to `Large` . For Salesforce Classic
apps in packages created with API 38.0 or later, you must
set `formFactors` to `Large` for Salesforce Classic
apps to appear in the Lightning Experience desktop.

As of API version 47.0, the `Small` value is supported
for Lightning apps. The `formFactors` field can be
set to `Small` or `Large` for Lightning apps, and it can
be set to `Null` or `Large` for Salesforce Classic apps.

`isNavAutoTempTabsDisabled` boolean Indicates whether the navigation automatically creates
temporary tabs settings. Applies only to Lightning apps

with standard navigation. Available in API version 43.0
and later.

`isNavPersonalizationDisabled` boolean

Indicates whether navigation personalization is disabled.
Applies only to Lightning apps. Available in API version
43.0 and later.

`isNavTabPersistenceDisabled` boolean Indicates whether workspace tabs are cleared for each
new console session ( `true` ) or not ( `false` ). Applies

only to Lightning apps with console navigation. Available
in API version 54.0 and later.

`isServiceCloudConsole` boolean

Indicates if the application is a Salesforce Classic console
app. For Lightning Experience console apps, this field is
`null` and the `navType` field is set to `Console` .

`label` string The name of the application.

`logo` string The optional reference to the image document for a
Salesforce app or Salesforce console app.

`navType` NavType (enumeration of type string) Not updateable. Indicates the type of navigation the app
uses. The value `Standard` is for a Lightning app with


Metadata Types CustomApplication

**Field Name** **Field Type** **Description**

standard navigation. The value `Console` is for a
Lightning app with console navigation.

This field is available in API version 38.0 and later.

`preferences` AppPreferences

Represents the preferences for a Salesforce Classic
console app. All of the AppPreferences fields are required.

This field is available in API version 42.0 and later.

`profileActionOverrides` AppProfileActionOverride[] A list of the Lightning Experience record page
ProfileActionOverrides that are assigned to this custom

app. When a user invokes the custom app, a matching
ProfileActionOverride assignment takes precedence over
existing overrides for the record page specified in
ActionOverride. You can override a record page for the
custom app by record type and profile.

In API version 45.0 and later, you can override a home
page for the custom app by profile.

`setupExperience` string The type of Setup experience associated with the app.
Valid values are:

**•** `all` —Represents the full Setup tree.

**•** `essentials` —Represents the Essentials Setup
tree, which contains a subset of Setup items
configured for Essentials edition.

**•** `service` —Represents the Service Setup tree,
which contains a subset of Setup items configured
for Service Console.

A `null` value is equivalent to `all` .

Previous valid values `AllSetup`, `ServiceSetup`,
and `EssentialsSetup` have been deprecated.

This field is available in API version 39.0 and later.

`subscriberTabs` string[]

Represents the list of tabs appended by a subscriber to
a Lightning app installed from a managed package.
Records in a subscriber tab always open as primary tabs.

This field is available in API version 41.0 and later.

`tabs` string[] The list of tabs included in this application. In API version
12.0, the `fullName` for built-in tabs like Home,

Account, and Reports, is the name of the tab (Home, for
example). In API version 13.0 and later, built-in tabs are
prefixed with `standard-` . For example, to reference
the Account tab you would use `standard-Account` .


Metadata Types CustomApplication

**Field Name** **Field Type** **Description**

In API version 42.0, this field was renamed from `tab` to
`tabs` .

`uiType` UiType (enumeration of type string) Not updateable. Identifies the type of custom app. The
value is:

**•** `Aloha` for Salesforce Classic

**•** `Lightning` for Lightning Experience

This field is available in API version 38.0 and later.

`utilityBar` string

The developer name of the utility bar associated with
this app.

We recommend assigning a utility bar to only one
Lightning App, because utility bars are shared. Sharing

means that if you change the utility bar in one app, it
automatically changes in all apps associated with it.

This field is available in API version 38.0 and later.

`workspaceConfig` AppWorkspaceConfig Represents how records open in a Salesforce console
app. Required if `isServiceCloudConsole` is

`true` . In API version 42.0, this field was renamed to
`workspaceConfig` from `workspaceMappings` .

AppActionOverride

Represents an action override for an application. Use it to create, update, edit, or delete action overrides. AppActionOverride inherits
from ActionOverride and extends it by one field, `pageOrSobjectType` . Available for Lightning Experience in API version 38.0 and
later.

**Field Name** **Field Type** **Description**

`actionName` string The only valid value is `view` for API version 43.0 and earlier. The value
`tab` is supported for API version 44.0 and later.

`comment` string Any comments you want associated with the override.

`content` string

`formFactor` FormFactor(enumeration
of type string)

Set this field if `type` is set to `flexipage` . It refers to the name of the
page to use as the override. To reference installed components, use the
format of _**`Component_namespace`**_ `__` _**`Component_name`**_ .

The size of the page being overridden.

If the `type` field is set to `flexipage`, set this field to `Large` to
override the View action with a Lightning page in Lightning Experience.

The `Large` value represents the Lightning Experience desktop
environment and is valid only for the `flexipage` and
`lightningcomponent` types. The `Small` value represents the
Salesforce mobile app on a phone or tablet. The `Medium` value is


Metadata Types CustomApplication

**Field Name** **Field Type** **Description**

reserved for future use. The `null` value (which is the same as specifying
no value) represents Salesforce Classic.

This field is available in API version 37.0 and later and is part of the feature
for creating and editing record pages in Lightning Experience.

Lightning component overrides return different `FormFactor` values
depending on the API version used.

**•** In API version 41.0 and earlier, Lightning component overrides return
only the `null` value (no value), representing the Salesforce Classic
environment.

**•** In API version 42.0, if you specify different Lightning component
overrides for Lightning Experience and mobile, one component is
selected randomly for both overrides and its `FormFactor` value
is returned. If there’s a conflict between Lightning components, and
a Visualforce page override is also specified for Salesforce Classic, the
Visualforce page takes precedence.

**•** In API version 43.0 and later, a Lightning component override for
Lightning Experience returns the `Large` value and a Lightning
component override for mobile returns the `Small` value, as
expected.

`pageOrSobjectType` string

The name of the sObject type being overridden. Valid values are
`standard` and `custom` .

This value must be `standard-home` when actionName is `tab` .

`skipRecordTypeSelect` boolean Set this field to `true` if you prefer that any new records created by this
action override aren’t forwarded to the record type selection page. This

field is only valid if the `actionName` is a “create” type (like `new` ), and
`type` is set to `visualforce` .

Required. Represents the type of action override. The valid values are
`Flexipage` and `Default` .

A `Flexipage` AppActionOverride set to App Default can’t be deleted
via Metadata API. Instead, remove the override using the page assignment
wizard in the Lightning App Builder UI.

```
type

```

AppBrand

ActionOverrideType
(enumeration of type
string)

The color scheme and logo used for the app. Available for Lightning apps in API version 38.0 and later.

**Field Name** **Field Type** **Description**

`footerColor` string Optional. Determines the footer color in the app. Specify the color with
a hexadecimal code, such as #0000FF for blue.


Metadata Types CustomApplication

**Field Name** **Field Type** **Description**

`headerColor` string Optional. Determines the header color in the app. Specify the color with
a hexadecimal code, such as #0000FF for blue.

`logo` string The optional reference to the image document for the application.

`logoVersion` int An optional version number for the logo.

`shouldOverrideOrgTheme` boolean Indicates whether to override the global theme for the org. When `true`,
the color scheme and logo that the user has set are used. When `false`,

the global theme for the org is used, even if the user has set a color
scheme and logo.

AppComponentList

Represents custom console components (Visualforce pages) assigned to a Salesforce console app. In API version 42.0, this type was
renamed from CustomApplicationComponents to AppComponentList.

**Field Name** **Field Type** **Description**

`alignment` string Required. Determines how custom console components are aligned in
the footer of a Salesforce console app.

`components` string[]

AppPreferences

The name of a custom console component assigned to a Salesforce
console app. In API version 42.0, this field was renamed from
`customApplicationComponent` to `components` .

Represents the preferences for a Salesforce Classic console app. All of the AppPreferences fields are required. Available in API version
42.0 and later.

**Field Name** **Field Type** **Description**

`enableCustomizeMyTabs` boolean

Indicates if a Salesforce Classic console app has Customize My Tabs
enabled. If enabled, users can hide, display, and organize items in the
navigation tab.

`enableKeyboardShortcuts` boolean Indicates if a Salesforce Classic console app has keyboard shortcuts
enabled. Shortcuts let users perform actions by pressing a combination

of keys instead of having to use a mouse. After keyboard shortcuts are
enabled, several default shortcuts are available for customization. Before
you can create custom shortcuts, a developer must define the shortcut’s
action with the `addEventListener()` method in the Salesforce
Console Integration Toolkit. You can’t create keyboard shortcuts for
actions performed outside of the console. This field is required if
`isServiceCloudConsole` is `true` .

`enableListViewHover` boolean Indicates if a Salesforce Classic console app has list view hovers enabled.
If set to `true`, summary information is displayed about a record in a


Metadata Types CustomApplication

**Field Name** **Field Type** **Description**

responsive list when the user hovers over a record name. For cases, hover
over the subject field.

`enableListViewReskin` boolean Indicates if Salesforce Classic console apps use responsive list views
instead of Salesforce Classic lists views.

`enableMultiMonitorComponents` boolean Indicates if a Salesforce Classic console app has multi-monitor
components enabled, which lets users move portions of a console from

their browsers to locations on their screens. This field is required if
`isServiceCloudConsole` is `true` .

`enablePinTabs` boolean Indicates if a Salesforce Classic console app has pinned tabs enabled,
which lets users pin primary tabs to the tab bar for quick access.

`enableTabHover` boolean

`enableTabLimits` boolean

Indicates if a Salesforce Classic console app has tab hover enabled. If
enabled, summary information is displayed about a record in an overlay
when the user hovers over a tab.

Indicates whether limits are enabled on the number of primary tabs and
subtabs that can be opened in a Salesforce Classic console session. When
`true`, values for `tabLimitConfig` are required

`saveUserSessions` boolean Indicates if a Salesforce Classic console app saves user sessions
automatically. If enabled, when console users close their browsers or log

out of Salesforce, any previously open tabs display when users log in
again. Required if `isServiceCloudConsole` is `true` .

AppProfileActionOverride

Represents a ProfileActionOverride for a custom app. This type inherits from ProfileActionOverride on page 1744 and extends it by one
field, `profile` . Available for Lightning Experience in API version 39.0 and later. In API version 45.0 and later, you can override a home
page for the custom app by profile.

**Field Name** **Field Type** **Description**

`actionName` string

Required. The name of the action. The only valid values are `Tab` and
`View` .

If `pageOrSobjectType` is `record-home`, this field must be
`View` . The `View` action is supported only when ProfileActionOverride
is being specified as part of a CustomApplication.

In API version 45.0 and later, this action is supported only when
ProfileActionOverride is being specified as part of a CustomApplication,
`pageOrSobjectType` is `standard-home`, and this field is `Tab` .

`content` string Read-only. Represents the name of the Lightning page being used as
the override.


Metadata Types CustomApplication

**Field Name** **Field Type** **Description**

```
formFactor

```

FormFactor Required. The size of the page being overridden. The `Large` value
(enumeration of type represents the Lightning Experience desktop environment.
string)

`pageOrSobjectType` string

Required. The name of the page being overridden. The only valid values
are `record-home` and `standard-home` . If the `actionName`
is `Tab`, this field must be `standard-home`

`profile` string The profile associated with the ProfileActionOverride.

`recordType` string

The record type associated with the override.If `pageOrSobjectType`
is `standard-home`, this field must be `null` . This field is required
when `actionName` is set to `View` .

```
type

```

ActionOverrideType Required. Read-only. The type of action override. The only valid value is
(enumeration of type `flexipage` .
string)

AppWorkspaceConfig

Represents how records open in a Salesforce console app. Required if `isServiceCloudConsole` is `true` . Available for Salesforce
Classic console apps in API version 25.0 and later. Available for Lightning console apps in API version 41.0 and later. In API version 42.0,
this type was renamed from WorkspaceMappings to AppWorkspaceConfig.

**Field Name** **Field Type** **Description**

`mappings` WorkspaceMappingSingle[] Represents how records for a specific tab open in a Salesforce console
app. Required for each tab specified in the CustomApplication. In API

version 42.0, this field was renamed from `workspaceMapping` to
`mappings` .

WorkspaceMapping

Represents how records for a specific tab open in a Salesforce console app. Required for each tab specified in the CustomApplication.
Available in API version 25.0 and later for Salesforce Classic console apps. Available in API version 41.0 and later for Lightning console
apps.

**Field Name** **Field Type** **Description**

`fieldName` string The name of the field that specifies the primary tab in which to display
`tab` as a subtab. If not specified, `tab` opens as a primary tab.

`tab` string Required. Name of the tab.


Metadata Types CustomApplication

CustomShortcut

Represents custom keyboard shortcuts assigned to a Salesforce console app in Salesforce Classic. Before you can create custom shortcuts,
a developer must define the shortcut’s action with the `addEventListener()` method in the Salesforce Console Integration Toolkit.
You can’t create keyboard shortcuts for actions performed outside of the console. Available in API version 28.0 and later.

**Field Name** **Field Type** **Description**

`action` string Required. The action performed in the console when a user presses the
keyboard shortcut.

`active` boolean Required. Indicates whether the keyboard shortcut is active ( `true` ) or
not ( `false` ).

`keyCommand` string Required. The combination of keys a user presses to trigger the keyboard
shortcut. Keyboard shortcuts aren’t case-sensitive, but they display as

uppercase on setup pages in the Salesforce user interface so that they’re
easier to read.

Each key command can include up to four modifier keys followed by one
non-modifier key. Modifier and non-modifier keys are separated by the
`+` key. Modifier keys can occur in any order, but you must place
non-modifier keys at the end of the key command sequence. For example,
`SHIFT+CTRL+ALT+META +A` .

Valid modifier keys are:

**•** `SHIFT`

**•** `CTRL`

**•** `ALT`

**•** `META` (represents the COMMAND key on Macs)

Valid non-modifier keys are letters A through Z and numbers 0 through
9. Other valid keys are:

**•** `TAB`

**•** `ENTER`

**•** `PAUSE/BREAK`

**•** `CAPS LOCK`

**•** `ESC`

**•** `SPACE`

**•** `PAGE UP`

**•** `PAGE DOWN`

**•** `END`

**•** `HOME`

**•** `LEFT ARROW`

**•** `UP ARROW`

**•** `RIGHT ARROW`

**•** `DOWN ARROW`


Metadata Types CustomApplication

**Field Name** **Field Type** **Description**

**•** `PRINT SCREEN`

**•** `INSERT`

**•** `DELETE`

**•** `RIGHT WINDOW`

**•** `NUMPAD 0`

**•** `NUMPAD 1`

**•** `NUMPAD 2`

**•** `NUMPAD 3`

**•** `NUMPAD 4`

**•** `NUMPAD 5`

**•** `NUMPAD 6`

**•** `NUMPAD 7`

**•** `NUMPAD 8`

**•** `NUMPAD 9`

**•** `MULTIPLY`

**•** `ADD`

**•** `SUBTRACT`

**•** `DECIMAL POINT`

**•** `DIVIDE`

**•** `F1`

**•** `F2`

**•** `F3`

**•** `F4`

**•** `F5`

**•** `F6`

**•** `F7`

**•** `F8`

**•** `F9`

**•** `F10`

**•** `F11`

**•** `F12`

**•** `NUM LOCK`

**•** `SCROLL LOCK`

**•** `;`

**•** `=`

**•** `,`

**•** `—`

**•** `.`


Metadata Types CustomApplication

**Field Name** **Field Type** **Description**

**•** `/`

**•** `‘`

**•** `[`

**•** `]`

**•** `\`

**•** `'`

`description` string The optional description text for the keyboard shortcut.

`eventName` string Required. Code available to developers who want to add custom shortcut
functions to the console via the Salesforce Console Integration Toolkit.

DefaultShortcut

Represents default keyboard shortcuts assigned to a Salesforce console app. After you enable keyboard shortcuts for a console, several
default shortcuts are available for customization. These include opening and closing tabs, moving between tabs, and saving records.
Available in API version 28.0 and later.

**Field Name** **Field Type** **Description**

`action` string Required. The action performed in the console when a user presses the
keyboard shortcut. Valid values are:

**•** `FOCUS_CONSOLE`

**•** `FOCUS_NAVIGATOR_TAB`

**•** `FOCUS_DETAIL_VIEW`

**•** `FOCUS_PRIMARY_TAB_PANEL`

**•** `FOCUS_SUBTAB_PANEL`

**•** `FOCUS_LIST_VIEW`

**•** `FOCUS_FIRST_LIST_VIEW`

**•** `FOCUS_SEARCH_INPUT`

**•** `MOVE_LEFT`

**•** `MOVE_RIGHT`

**•** `UP_ARROW`

**•** `DOWN_ARROW`

**•** `OPEN_TAB_SCROLLER_MENU`

**•** `OPEN_TAB`

**•** `CLOSE_TAB`

**•** `ENTER`

**•** `EDIT`

**•** `SAVE`


Metadata Types CustomApplication

**Field Name** **Field Type** **Description**

`active` boolean Required. Indicates whether the keyboard shortcut is active ( `true` ) or
not ( `false` ).

`keyCommand` string Required. The combination of keys a user presses to trigger the keyboard
shortcut. Keyboard shortcuts aren’t case-sensitive, but they display as

uppercase on setup pages in the Salesforce user interface so that they’re
easier to read.

Each key command can include up to four modifier keys followed by one
non-modifier key. Modifier and non-modifier keys are separated by the
`+` key. Modifier keys can occur in any order, but you must place
non-modifier keys at the end of the key command sequence. For example,
`SHIFT+CTRL+ALT+META +A` .

Valid modifier keys are:

Valid non-modifier keys are letters A through Z and numbers 0 through
9. Other valid keys are:

KeyboardShortcuts

Represents keyboard shortcuts assigned to a Salesforce console app. Required if `isServiceCloudConsole` is `true` . Available
in API version 28.0 and later.

**Field Name** **Field Type** **Description**

`customShortcuts` CustomShortcut[] Represents custom keyboard shortcuts assigned to a Salesforce console
app in Salesforce Classic. Before you can create custom shortcuts, a

developer must define the shortcut’s action with the
`addEventListener()` method in the Salesforce Console
Integration Toolkit. You can’t create keyboard shortcuts for actions
performed outside of the console.

In API version 42.0, this field was renamed from `customShortcut`
to `customShortcuts` .

`defaultShortcuts` DefaultShortcut[] Represents default keyboard shortcuts assigned to a Salesforce console
app. After you enable keyboard shortcuts for a console, several default

shortcuts are available for customization. These include opening and
closing tabs, moving between tabs, and saving records.

In API version 42.0, this field was renamed from `defaultShortcut`
to `defaultShortcuts` .

ListPlacement

Represents how lists display in a Salesforce console app. Required if `isServiceCloudConsole` is `true` . Available in API version
25.0 and later.


Metadata Types CustomApplication

**Field Name** **Field Type** **Description**

`height` int Height of the list in pixels or percentage. Required if `location` is top.

`location` string Required. Location of the list on the screen. Valid values are:

**•** full

**•** top

**•** left

`units` string Required. Represents if `height` or `width` is in pixels or percentage.

`width` int Width of the list in pixels or percentage. Required if `location` is left.

LiveAgentConfig

Represents your organization's settings for using Chat in the Salesforce Console.

**Field Name** **Field Type** **Description**

`enableLiveChat` boolean Specifies whether Chat is enabled in your organization ( `true` ) or not
( `false` ).

`openNewAccountSubtab` boolean

Specifies whether to open a new Account subtab in a Salesforce console
app automatically ( `true` ) or not ( `false` ) when an agent accepts a
chat.

`openNewCaseSubtab` boolean Specifies whether to open a new Case subtab in a Salesforce console app
automatically ( `true` ) or not ( `false` ) when an agent accepts a chat.

`openNewContactSubtab` boolean

`openNewLeadSubtab` boolean

`openNewVFPageSubtab` boolean

`pageNamesToOpen` string [array of strings]

Specifies whether to open a new Contact subtab in a Salesforce console
app automatically ( `true` ) or not ( `false` ) when an agent accepts a
chat.

Specifies whether to open a new Lead subtab in a Salesforce console
app automatically ( `true` ) or not ( `false` ) when an agent accepts a
chat.

Specifies whether to open a new Visualforce page as a subtab in a
Salesforce console app automatically ( `true` ) or not ( `false` ) when an
agent accepts a chat.

Specifies the Visualforce pages to open in subtabs when an agent accepts
a chat in a Salesforce console app.

This field is available in API version 42.0 and later.

`showKnowledgeArticles` boolean Specifies whether to display the Knowledge component while using
Chat in a Salesforce console app ( `true` ) or not ( `false` ).


Metadata Types CustomApplication

PushNotification

Represents a set of push notifications, which are visual indicators on lists and detail pages that show when a record or field has changed
during a user’s session. Available for use if `isServiceCloudConsole` is `true` . Available in API version 28.0 and later.

**Field Name** **Field Type** **Description**

`fieldNames` string] The name of the field or fields that trigger push notifications for the
selected object.

`objectName` string Required. Name of the object that triggers push notifications.

ServiceCloudConsoleConfig

Represents configuration settings for a Salesforce console app. Available in API version 42.0 and later.

**Field Name** **Field Type** **Description**

`componentList` AppComponentList Represents custom console components (Visualforce pages) assigned to
a Salesforce console app.

`detailPageRefreshMethod` string Determines how detail pages refresh in a Salesforce console app. Required
if `isServiceCloudConsole` is `true` . The valid values are:

**•** `none`

**•** `autoRefresh`

**•** `flag`

`footerColor` string Determines the footer color in a Salesforce console app.Specify the color
with a hexadecimal code, such as #0000FF for blue.

`headerColor` string Determines the header color in a Salesforce console app. Specify the
color with a hexadecimal code, such as #0000FF for blue.

`keyboardShortcuts` KeyboardShortcuts

Represents the keyboard shortcuts for a Salesforce console app. Keyboard
shortcuts let users perform actions by pressing a combination of keys
instead of having to use a mouse.

`listPlacement` ListPlacement Represents how lists display in a Salesforce console app. Required if
`isServiceCloudConsole` is `true` .

`listRefreshMethod` string Determines how lists refresh in a Salesforce console app. Required if
`isServiceCloudConsole` is `true` . The valid values are:

**•** `none`

**•** `refreshList`

**•** `refreshListRows`

`liveAgentConfig` LiveAgentConfig Represents the configurations for using Chat in the Salesforce Console.

`primaryTabColor` string Determines the primary tab color in a Salesforce console app.Specify the
color with a hexadecimal code, such as #0000FF for blue.


Metadata Types CustomApplication

**Field Name** **Field Type** **Description**

`pushNotifications` PushNotification[] Represents push notifications for a Salesforce console app. Push
notifications are visual indicators on lists and detail pages that show when

a record or field has changed during a user’s session. For example, assume
that two support agents are working on the same case. If one agent
changes the `Priority`, a push notification displays to the other agent
so the agent notices the change and doesn’t duplicate the effort.

`tabLimitConfig` TabLimitConfig

Represents the maximum number of primary tabs and subtabs allowed
in one Salesforce console session. Required if `enableTabLimits` is
`true` .

`whiteListedDomains` string[] Any external domains that users can access from within a Salesforce
console app. For example, `www.yourdomain.com` .

TabLimitConfig

Represents the maximum number of primary tabs and subtabs allowed in one Salesforce console session. Required if
`enableTabLimits` is `true` . Available in API version 36.0 and later.

**Field Name** **Field Type** **Description**

`maxNumberOfPrimaryTabs` string The maximum number of primary tabs allowed in one console session.
Valid values are:

**•** 5

**•** 10

**•** 20

**•** 30

`maxNumberOfSubTabs` string The maximum number of subtabs allowed in one console session. Valid
values are:

**•** 5

**•** 10

**•** 15

Usage

You can't delete custom app ProfileActionOverrides by deploying with `destructiveChange.xml` . To delete a ProfileActionOverride,
retrieve the app. In the app definition file, find the `<profileActionOverrides>` section, and remove the `<content>` row.
