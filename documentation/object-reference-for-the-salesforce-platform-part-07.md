specific row is logged. When multiple rows are updated, only a single ID is logged.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The key prefix of the entity type that was saved

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects DatabaseSaveEventLog

**Field** **Details**

**Description**
The string that ties together all events in a given user’s login session. The session starts with
a login event and ends with either a logout event or the user session expiring. For example,
`lUqjLPQTWRdvRG4` .

```
RequestIdentifier

RowCount

SampleFactor

SessionKey

Timestamp

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same RequestIdentifier.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total number of records in the result set.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Rate at which entities are logged. If the sample factor is 1 that means every entity saved was
logged. If it is 100 that means that 1/100 logs.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT. For example, 2020-01-20T19:12:26.965Z.


### Standard Objects DatacloudCompany

**Field** **Details**

```
UserIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.

### DatacloudCompany

Represents the fields for Data.com company records. This object is available in API version 30.0 or later.

Note: When your Data.com Prospector or Data.com Clean contract expires, Data.com features, objects, and fields are removed
from your org.

To support customers’ needs around compliance and to remain a leader in trust and privacy, Salesforce removed all contact data
from the Data.com service on February 1, 2021.

[For more information, see Data.com Prospector and Clean Retirement.](https://help.salesforce.com/articleView?id=000270376&language=en_US&type=1)

Supported Calls

`describeLayout()`, `describeSObjects()`, `query()`

Fields

**Field Name** **Details**

```
ActiveContacts

AnnualRevenue

```

**Type**
int

**Properties**
Nillable

**Description**

The number of active contacts that are associated with a company.

**Type**
currency

**Properties**
Filter, Nillable

**Description**

The amount of money that the company makes in 1 year. Annual revenue is
measured in US dollars.


Standard Objects DatacloudCompany

**Field Name** **Details**

```
City

CompanyId

Country

CountryCode

Description

DunsNumber

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

The name of the city where the company is located.

**Type**
string

**Properties**
Filter, Nillable

**Description**

A unique numerical identifier for the company and theData.com identifier for a
company.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

A string that represents the standard abbreviation for the country where the
company is located.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist

**Description**

A standardized name for countries of the world.

**Type**
string

**Properties**
Nillable

**Description**

A brief synopsis of the company that provides a general overview of the company
and what it does.

**Type**
string


Standard Objects DatacloudCompany

**Field Name** **Details**

**Properties**
Filter, Nillable

**Description**

A randomly generated nine-digit number that’s assigned by Dun & Bradstreet
(D&B) to identify unique business establishments.

```
EmployeeQuantityGrowthRate

ExternalId

Fax

FortuneRank

FullAddress

```

**Type**
double

**Properties**
Nillable

**Description**
The yearly growth rate of the number of employees in a company expressed as
a decimal percentage. The data includes the total employee growth rate for the
past two years.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

A unique numerical identifier for the company. The `ExternalId` is a
system-generated number.

**Type**
phone

**Properties**
Nillable

**Description**

The telephone number that’s used to send and receive faxes.

**Type**
int

**Properties**
Defaulted on create, Group, Nillable

**Description**
The numeric value of the company’s Fortune 1000 ranking. A null or blank value
means that the company isn’t ranked as a Fortune 1000 company.

**Type**
string


Standard Objects DatacloudCompany

**Field Name** **Details**

**Properties**
Group, Nillable

**Description**
The complete address of a company, including Street, City, State, and Zip.

```
IncludedInSnP500

Industry

IsInCrm

IsInactive

IsOwned

```

**Type**
string

**Properties**
Group, Nillable

**Description**
A true or false value. If `true`, the company is listed in the S&P 500 Index. If
`false`, the company isn’t listed in the S&P 500 Index.

**Type**
string

**Properties**
Nillable

**Description**
A description of the type of industry such as Telecommunications, Agriculture,
or Electronics.

**Type**
boolean

**Properties**
Defaulted on create, Group

**Description**

Whether the record is in Salesforce (true) or not (false).

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**

A true or false response. True, the company record is not active. False, the
company record is active.

**Type**
boolean

**Properties**
Defaulted on create


Standard Objects DatacloudCompany

**Field Name** **Details**

**Description**

A true or false value. True, your organization owns the record. False, your
organization doesn’t own the record.

```
NaicsCode

NaicsDesc

Name

NumberOfEmployees

Ownership

```

**Type**
string

**Properties**
Filter, Nillable

**Description**

A value that represents the North American Industry Classification System (NAICS)
code. NAICS was created to provide details about a business’s service orientation.
The code descriptions are focused on what a business does.

**Type**
string

**Properties**
Nillable

**Description**

A description of the NAICS classification.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

The company’s name.

**Type**
int

**Properties**
Filter, Nillable

**Description**

The number of employees working for the company.

**Type**
string

**Properties**
Filter, Nillable

**Description**

The type of ownership of the company:


Standard Objects DatacloudCompany

**Field Name** **Details**

**•** `Public`

**•** `Private`

**•** `Government`

**•** `Other`

```
Phone

PremisesMeasure

PremisesMeasureReliability

PremisesMeasureUnit

PriorYearEmployees

```

**Type**
phone

**Properties**
Nillable

**Description**

A numeric string containing the primary telephone number for the company.

**Type**
int

**Properties**
Group, Nillable

**Description**
A numeric value for the measurement of the premises.

**Type**
string

**Properties**
Group, Nillable

**Description**
A descriptive accuracy of the measurement such as actual, estimated, or modeled.

**Type**
string

**Properties**
Group, Nillable

**Description**
A descriptive measurement unit such as acres, square meters, or square feet.

**Type**
int

**Properties**
Group, Nillable

**Description**

The total number of employees for the prior year.


Standard Objects DatacloudCompany

**Field Name** **Details**

```
PriorYearRevenue

SalesTurnoverGrowthRate

Sic

SicCodeDesc

SicDesc

Site

```

**Type**
double

**Properties**
Nillable

**Description**

The annual revenue for the prior year.

**Type**
double

**Properties**
Nillable

**Description**
The increase in annual revenue from the previous value for an equivalent period
expressed as a decimal percentage.

**Type**
string

**Properties**
Filter, Nillable

**Description**

A numeric value that represents the Standard Industrial Codes (SIC). SIC is a
numbering convention that indicates what type of service a business provides.
It is a four-digit value.

**Type**
string

**Properties**
Group, Nillable

**Description**
The SIC numeric code and description for a company.

**Type**
string

**Properties**
Nillable

**Description**

A description of the SIC classification.

**Type**
picklist


Standard Objects DatacloudCompany

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist

**Description**

An organizational status of the company.

**•** Branch: a secondary location to a headquarter location

**•** Headquarter: a parent company with branches or subsidiaries

**•** Single Location: a single business with no subsidiaries or branches

```
State

StateCode

Street

TickerSymbol

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

The two-letter standard abbreviation for a state.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist

**Description**

A standard two-letter abbreviation for states and territories of the United States.
The state where the company is located. The abbreviation can also be a province
or other equivalent to a state, depending on the country where the company is
located.

**Type**
string

**Properties**
Nillable

**Description**

A postal address for the company.

**Type**
string

**Properties**
Nillable

**Description**

The symbol that uniquely identifies companies that are traded on public stock
exchanges.


Standard Objects DatacloudCompany

**Field Name** **Details**

```
TradeStyle

UpdatedDate

Website

YearStarted

Zip

```

Usage

**Type**
string

**Properties**
Nillable

**Description**

A legal name under which a company conducts business.

**Type**
dateTime

**Properties**
Nillable, Sort

**Description**

The last date and time when the information for this company was updated.

**Type**
url

**Properties**
Nillable

**Description**

The standard URL for the company’s home page.

**Type**
string

**Properties**
Nillable

**Description**

The year when the company was founded.

**Type**
string

**Properties**
Filter, Nillable

**Description**

A numeric postal code that’s designated for the address.

Use the DatacloudCompany object to search the Data.com database for companies with the specific criteria that you enter. Use this
object to find company records that you are interested in purchasing for your organization. Data.com APIs use the term “company,”
which is similar to Salesforce term “accounts.”


### Standard Objects DatacloudContact

Important: DatacloudCompany can’t be used in Apex test methods, because an external web service call is required to access
it. These calls are not allowed in Apex test methods.

### DatacloudContact

The fields and properties for Data.com contact records. This object is available in API version 30.0 or later.

Note: When your Data.com Prospector or Data.com Clean contract expires, Data.com features, objects, and fields are removed
from your org.

To support customers’ needs around compliance and to remain a leader in trust and privacy, Salesforce removed all contact data
from the Data.com service on February 1, 2021.

[For more information, see Data.com Prospector and Clean Retirement.](https://help.salesforce.com/articleView?id=000270376&language=en_US&type=1)

Supported Calls

`describeSObjects()`, `query()`

Fields

**Field Name** **Details**

```
City

CompanyId

CompanyName

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

The city where the company is located.

**Type**
string

**Properties**
Filter, Nillable

**Description**

The unique numerical identifier for the company and the Data.com company
identification number or Data.com Key.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**

The name of the company.


Standard Objects DatacloudContact

**Field Name** **Details**

```
ContactId

Country

Department

Email

```

**Type**
string

**Properties**
Filter, Nillable

**Description**

The unique numeric identifier for this contact.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

The standard abbreviation or name for the country where the company is located.

Note: You can enter a comma-separated list of countries; however, for
a country that uses a comma in its name, leave out the comma. For
example, enter “Taiwan, ROC” as `Taiwan ROC` .

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist

**Description**

The department in the company that the contact is affiliated with. The values of
this field are fixed enumerated values.

**•** `Engineering`

**•** `Finance`

**•** `Human Resources`

**•** `IT`

**•** `Marketing`

**•** `Operations`

**•** `Other`

**•** `Sales`

**•** `Support`

**Type**
email

**Properties**
Filter, Nillable


Standard Objects DatacloudContact

**Field Name** **Details**

**Description**

A business email address for the contact.

```
ExternalId

FirstName

IsInCrm

IsInactive

IsOwned

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

A unique system-generated numerical identifier for the contact.

**Type**
string

**Properties**
Filter, Nillable

**Description**

The first name of the contact.

**Type**
boolean

**Properties**
Defaulted on create, Group

**Description**
Whether the record is in Salesforce (true) or not (false).

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Whether the record is active (false) or not (true).

**Type**
boolean

**Properties**
Defaulted on create

**Description**

**•** `True` : You own this record.

**•** `False` : You do not own this record.


Standard Objects DatacloudContact

**Field Name** **Details**

```
LastName

Level

Phone

SocialHandles

State

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

The last name of the contact.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist

**Description**

A human resource label that designates a person’s level in the company. The
values of this field are fixed enumerated values.

**•** `C-Level`

**•** `VP`

**•** `Director`

**•** `Manager`

**•** `Staff`

**•** `Other`

**Type**
phone

**Properties**
Nillable

**Description**
The direct-dial telephone number for the contact.

**Type**
string

**Description**
The social handles for this contact. Social handles are a normalized URL and user
name for social media accounts such as, LinkedIn, Facebook, and Twitter. This
field is response-only.

The DatacloudSocialHandles object is a child of the DatacloudContact object.

**Type**
string

**Properties**
Filter, Nillable, Sort


Standard Objects DatacloudContact

**Field Name** **Details**

**Description**

The state where the company is located, which can also be a province or other
equivalent to a state, depending on the country where the company is located.

```
Street

Title

UpdatedDate

Zip

```

Usage

**Type**
string

**Properties**
Nillable

**Description**

The street address for the company where the contact works.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Title of the contact such as CEO or Vice President.

**Type**
dateTime

**Properties**
Nillable, Sort

**Description**

The last date and time when the information for a contact was updated.

**Type**
string

**Properties**
Filter, Nillable

**Description**

The postal or zip code for the address.

This object searches the Data.com database for contacts with the specific criteria that you enter. Use this object to find contact records
that you are interested in purchasing for your organization.

Important: DatacloudContact can’t be used in Apex test methods, because an external web service call is required to access it.
These calls are not allowed in Apex test methods.


### Standard Objects DatacloudDandBCompany DatacloudDandBCompany

Represents a set of read-only fields that are used to return D&B company data from Data.com API calls. This object is available in API
version 30.0 or later.

Note: When your Data.com Prospector or Data.com Clean contract expires, Data.com features, objects, and fields will be removed
from your org.

To support customers’ needs around compliance and to remain a leader in trust and privacy, Salesforce removed all contact data
from the Data.com service on February 1, 2021.

[For more information, see Data.com Prospector and Clean Retirement.](https://help.salesforce.com/articleView?id=000270376&language=en_US&type=1)

Supported Calls

`describeSObjects()`, `query()`

Fields

**Field Name** **Details**

```
City

CompanyCurrencyIsoCode

CompanyId

```

**Type**
string

**Properties**
Nillable

**Description**

The name of the city where the company is physically located.

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**

The code used to represent a company’s local currency. This data is provided by
the International Organization for Standardization (ISO) and is based on their
three-letter currency codes. For example, USD is the ISO code for United States
Dollar.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

A unique numeric identifier for a company.


Standard Objects DatacloudDandBCompany

**Field Name** **Details**

```
Country

CountryAccessCode

CurrencyCode

Description

DomesticUltimateBusinessName

DomesticUltimateDunsNumber

```

**Type**
string

**Properties**
Nillable

**Description**

The country where a company is physically located.

**Type**
string

**Properties**
Nillable

**Description**

The required code for international calls.

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**

The currency in which the company’s sales volume is expressed.

**Type**
string

**Properties**
Nillable

**Description**

A brief description of the company, which may include information about its
history, its products and services, and its influence on a particular industry.

**Type**
string

**Properties**
Nillable

**Description**

The primary name of the Domestic Ultimate, which is the highest ranking
subsidiary, specified by country, within an organization’s corporate structure.

**Type**
string


Standard Objects DatacloudDandBCompany

**Field Name** **Details**

**Properties**
Nillable

**Description**

The D-U-N-S number for the Domestic Ultimate, which is the highest-ranking
subsidiary, specified by country, within an organization’s corporate structure.

```
DunsNumber

EmployeeQuantityGrowthRate

EmployeesHere

EmployeesHereReliability

```

**Type**
string

**Properties**
Filter, Nillable

**Description**

The Data Universal Numbering System (D-U-N-S) number is a unique, nine-digit
number assigned to every business location in the Dun & Bradstreet database
that has a unique, separate, and distinct operation. D-U-N-S numbers are used
by industries and organizations around the world as a global standard for business
identification and tracking.

**Type**
double

**Properties**
Nillable

**Description**
The yearly growth rate of the number of employees in a company expressed as
a decimal percentage. The data includes the total employee growth rate for the
past two years.

**Type**
double

**Properties**
Nillable

**Description**

The number of employees at a specified location, such as a branch location.

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**

The reliability of the `EmployeesHere` figure. Available values are _`Actual`_
_`number`_, _`Low`_, _`Estimated (for all records)`_, _`Modeled (for`_
_`non-US records)`_ . A blank value indicates this data is unavailable.


Standard Objects DatacloudDandBCompany

**Field Name** **Details**

```
EmployeesTotal

EmployeesTotalReliability

ExternalId

FamilyMembers

Fax

```

**Type**
double

**Properties**
Nillable

**Description**

The total number of employees in the company, including all subsidiary and
branch locations. This data is available only on records that have a value of
_`Headquarters/Parent`_ in the `LocationStatus` field.

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**

The reliability of the `EmployeesTotal` figure. Available values are _`Actual`_
_`number`_, _`Low`_, _`Estimated (for all records)`_, _`Modeled (for`_
_`non-US records)`_ . A blank value indicates this data is unavailable.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

A system generated numeric identification.

**Type**
int

**Properties**
Nillable

**Description**

The total number of family members, worldwide, within an organization, including
the Global Ultimate, its subsidiaries (if any), and its branches (if any).

**Type**
phone

**Properties**
Nillable

**Description**

The company’s facsimile number.


Standard Objects DatacloudDandBCompany

**Field Name** **Details**

```
FifthNaics

FifthNaicsDesc

FifthSic

FifthSic8

FifthSic8Desc

FifthSicDesc

```

**Type**
string

**Properties**
Nillable

**Description**

A NAICS code that’s used to further classify an organization by industry.

**Type**
string

**Properties**
Nillable

**Description**

A brief description of an organization’s line of business, based on the
corresponding NAICS code.

**Type**
string

**Properties**
Nillable

**Description**

A Standard Industrial Classification (SIC) code that’s used to further classify an
organization by industry.

**Type**
string

**Properties**
Group, Nillable

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

**Type**
string

**Properties**
Group, Nillable

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
string


Standard Objects DatacloudDandBCompany

**Field Name** **Details**

**Properties**
Nillable

**Description**

A brief description of an organization’s line of business, based on the
corresponding SIC code.

```
FipsMsaCode

FipsMsaDesc

FortuneRank

FourthNaics

FourthNaicsDesc

```

**Type**
string

**Properties**
Nillable

**Description**

The Federal Information Processing Standards (FIPS) and the Metropolitan
Statistical Area (MSA) codes identify the organization’s location. The MSA codes
are defined by the US Office of Management and Budget.

**Type**
string

**Properties**
Nillable

**Description**

A brief description of an organization’s FIPS MSA code.

**Type**
int

**Properties**
Defaulted on create, Group, Nillable

**Description**
The numeric value of the company’s Fortune 1000 ranking. A null or blank value
means that the company isn’t ranked as a Fortune 1000 company.

**Type**
string

**Properties**
Nillable

**Description**

A NAICS code used to further classify an organization by industry.

**Type**
string

**Properties**
Nillable


Standard Objects DatacloudDandBCompany

**Field Name** **Details**

**Description**

A brief description of an organization’s line of business, based on the
corresponding NAICS code.

```
FourthSic

FourthSic8

FourthSic8Desc

FourthSicDesc

GeoCodeAccuracy

```

**Type**
string

**Properties**
Group, Nillable

**Description**

A SIC code used to further classify an organization by industry.

**Type**
string

**Properties**
Group, Nillable

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

**Type**
string

**Properties**
Group, Nillable

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
string

**Properties**
Nillable

**Description**

A brief description of an organization’s line of business, based on the
corresponding SIC code.

**Type**
picklist

**Properties**
Nillable, Restricted picklist


Standard Objects DatacloudDandBCompany

**Field Name** **Details**

**Description**

The level of accuracy of a location’s geographical coordinates compared with its
physical address. Available values include _`Rooftop level`_, _`Street`_
_`level`_, _`Block level`_, _`Census tract level`_, _`Mailing address`_
_`level`_, _`ZIP code level`_, _`Geocode could not be assigned`_,
_`Places the address in the correct city`_, _`Not matched`_,
_`State or Province Centroid`_, _`Street intersection`_, _`PO`_
_`BOX location`_, _`Non-US rooftop accuracy`_, _`County Centroid`_,
_`Sub Locality-Street Level`_, and _`Locality Centroid`_

```
GlobalUltimateBusinessName

GlobalUltimateDunsNumber

GlobalUltimateTotalEmployees

ImportExportAgent

```

**Type**
string

**Properties**
Nillable

**Description**

The primary name of the Global Ultimate, which is the highest entity within an
organization’s corporate structure and may oversee branches and subsidiaries.

**Type**
string

**Properties**
Filter, Nillable

**Description**

The D-U-N-S number of the Global Ultimate, which is the highest-ranking entity
within an organization’s corporate structure and can oversee branches and
subsidiaries.

**Type**
double

**Properties**
Nillable

**Description**

The total number of employees at the Global Ultimate, which is the highest entity
within an organization’s corporate structure and may oversee branches and
subsidiaries.

**Type**
picklist

**Properties**
Nillable, Restricted picklist


Standard Objects DatacloudDandBCompany

**Field Name** **Details**

**Description**

Identifies whether a business imports goods or services, exports goods or services,
and/or is an agent for goods.

```
IncludedInSnP500

Industry

IsOwned

IsParent

Latitude

```

**Type**
string

**Properties**
Group, Nillable

**Description**
A true or false value. If `true`, the company is listed in the S&P 500 Index. If
`false`, the company isn’t listed in the S&P 500 Index.

**Type**
string

**Properties**
Group, Nillable

**Description**
A description of the type of industry such as Telecommunications, Agriculture,
or Electronics.

**Type**
boolean

**Properties**
Defaulted on create

**Description**

A true or false value. True, your organization owns the record. False, your
organization doesn’t own the record.

**Type**
boolean

**Properties**
Defaulted on create,

**Description**
A true or false value. True, the company is a parent company. False, the company
isn’t a parent company. A parent company owns other companies.

**Type**
string

**Properties**
Nillable


Standard Objects DatacloudDandBCompany

**Field Name** **Details**

**Description**

Used with longitude to specify a precise location, which is used to assess the
Geocode Accuracy.

```
LegalStatus

LocationStatus

Longitude

```

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**

Identifies the legal structure of an organization. Available values include
_`Cooperative`_, _`Nonprofit organization`_, _`Local government`_
_`body`_, _`Partnership of unknown type`_, and _`Foreign company`_ .

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**

Identifies the organizational status of a company. A numeric value represents
each value.

Note: Only the numeric value is accepted in an API request.

**Type**
string

**Properties**
Nillable


Standard Objects DatacloudDandBCompany

**Field Name** **Details**

**Description**

Used with latitude to specify a precise location, which is used to assess the
Geocode Accuracy.

```
MailingCity

MailingCountry

MailingState

MailingStreet

MailingZip

```

**Type**
string

**Properties**
Nillable

**Description**

The city where a company has its mail delivered.

**Type**
string

**Properties**
Nillable

**Description**

The country where a company has its mail delivered.

**Type**
string

**Properties**
Nillable

**Description**

The state where a company has its mail delivered.

**Type**
string

**Properties**
Nillable

**Description**

The street address where a company has its mail delivered.

**Type**
string

**Properties**
Nillable

**Description**

The postal zip code for the company.


Standard Objects DatacloudDandBCompany

**Field Name** **Details**

```
MarketingPreScreen

MarketingSegmentationCluster

MinorityOwned

Name

NationalId

```

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**

The probability that a company pays with a significant delay compared to the
agreed terms. The risk level is based on the standard Commercial Credit Score,
and ranges from low risk to high risk. Available values are _`High risk of`_
_`delinquency`_, _`Low risk of delinquency`_, and _`Moderate risk`_
_`of delinquency`_ .

Important: Use this information for marketing pre-screening purposes
only.

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**
Twenty-two distinct, mutually exclusive profiles, created as a result of cluster
analysis of Dun & Bradstreet data for US organizations. Available values include

```
  High-Tension Branches of Insurance/Utility
```

_`Industries`_, _`Rapid-Growth Large Businesses`_,
_`Labor-Intensive Giants`_, _`Spartans`_, _`Main Street USA`_ .

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**

Indicates whether an organization is owned or controlled by a member of a
minority group.

**Type**
string

**Properties**
Filter, Nillable

**Description**

The primary or registered name of a company.

**Type**
string


Standard Objects DatacloudDandBCompany

**Field Name** **Details**

**Properties**
Nillable

**Description**

The identification number used in some countries for business registration and
tax collection.

```
NationalIdType

OutOfBusiness

OwnOrRent

ParentOrHqBusinessName

ParentOrHqDunsNumber

```

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**

A code value that identifies the type of national identification number that’s used.

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**

Indicates whether the company at the specified address has discontinued
operations.

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**

Indicates whether a company owns or rents the building it occupies.

**Type**
string

**Properties**
Nillable

**Description**

The primary name of the parent or headquarters company.

**Type**
string

**Properties**
Filter, Nillable


Standard Objects DatacloudDandBCompany

**Field Name** **Details**

**Description**

The D-U-N-S number for the parent or headquarters.

```
Phone

PremisesMeasure

PremisesMeasureReliability

PremisesMeasureUnit

PrimaryNaics

```

**Type**
phone

**Properties**
Nillable

**Description**
A company’s primary telephone number.

**Type**
int

**Properties**
Group, Nillable

**Description**
A numeric value for the measurement of the premises.

**Type**
string

**Properties**
Group, Nillable

**Description**
A descriptive accuracy of the measurement such as actual, estimated, or modeled.

**Type**
string

**Properties**
Group, Nillable

**Description**
A descriptive measurement unit such as acres, square meters, or square feet.

**Type**
string

**Properties**
Nillable

**Description**

The six-digit North American Industry Classification System (NAICS) code is the
standard used by business and government to classify business establishments
according to their economic activity for the purpose of collecting, analyzing, and
publishing statistical data related to the US business economy.


Standard Objects DatacloudDandBCompany

**Field Name** **Details**

```
PrimaryNaicsDesc

PrimarySic

PrimarySic8

PrimarySic8Desc

PrimarySicDesc

```

**Type**
string

**Properties**
Nillable

**Description**

A brief description of an organization’s line of business, based on its NAICS code.

**Type**
string

**Properties**
Nillable

**Description**

The four-digit SIC code that’s used to categorize business establishments by
industry.

**Type**
string

**Properties**
Group, Nillable

**Description**
The eight-digit Standard Industrial Classification (SIC) code is used to categorize
business establishments by industry. The full list of values can be found at the
[Optimizer Resources page maintained by Dun & Bradstreet. Maximum size is 8](http://www.dnboptimizer.com/knowledge-center/optimizer-resources.html)
characters.

**Type**
string

**Properties**
Group, Nillable

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
string

**Properties**
Nillable

**Description**

A brief description of an organization’s line of business, based on its SIC code.


Standard Objects DatacloudDandBCompany

**Field Name** **Details**

```
PriorYearEmployees

PriorYearRevenue

PublicIndicator

Revenue

SalesTurnoverGrowthRate

SalesVolume

```

**Type**
int

**Properties**
Group, Nillable

**Description**

The total number of employees for the prior year.

**Type**
double

**Properties**
Nillable

**Description**

The annual revenue for the prior year.

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**

Indicates whether ownership of the company is public or private.

**Type**
double

**Properties**
Nillable

**Description**

The annual revenue of a company in US dollars.

**Type**
double

**Properties**
Nillable

**Description**
The increase in annual revenue from the previous value for an equivalent period
expressed as a decimal percentage.

**Type**
double

**Properties**
Nillable


Standard Objects DatacloudDandBCompany

**Field Name** **Details**

**Description**

The total annual sales revenue in the headquarters’ local currency. Dun &
Bradstreet tracks revenue data for publicly traded companies, Global Ultimates,
Domestic Ultimates, and some headquarters.

```
SalesVolumeReliability

SecondNaics

SecondNaicsDesc

SecondSic

SecondSic8

```

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**

The reliability of the `SalesVolume` figure.

**Type**
string

**Properties**
Nillable

**Description**

A NAICS code used to further classify an organization by industry.

**Type**
string

**Properties**
Nillable

**Description**

A brief description of an organization’s line of business, based on the
corresponding NAICS code.

**Type**
string

**Properties**
Nillable

**Description**

A SIC code used to further classify an organization by industry.

**Type**
string

**Properties**
Group, Nillable


Standard Objects DatacloudDandBCompany

**Field Name** **Details**

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

```
SecondSic8Desc

SecondSicDesc

SixthNaics

SixthNaicsDesc

SixthSic

```

**Type**
string

**Properties**
Group, Nillable

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
string

**Properties**
Nillable

**Description**

A brief description of an organization’s line of business, based on the
corresponding SIC code.

**Type**
string

**Properties**
Nillable

**Description**

A NAICS code used to further classify an organization by industry.

**Type**
string

**Properties**
Nillable

**Description**

A brief description of an organization’s line of business, based on the
corresponding SIC code.

**Type**
string

**Properties**
Nillable

**Description**

A SIC code used to further classify an organization by industry.


Standard Objects DatacloudDandBCompany

**Field Name** **Details**

```
SixthSic8

SixthSic8Desc

SixthSicDesc

SmallBusiness

State

StockExchange

```

**Type**
string

**Properties**
Group, Nillable

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

**Type**
string

**Properties**
Group, Nillable

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
string

**Properties**
Nillable

**Description**

A brief description of an organization’s line of business, based on the
corresponding SIC code.

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**

Indicates whether the company is designated a small business as defined by the
Small Business Administration of the US government.

**Type**
string

**Properties**
Nillable

**Description**

The state where a company is physically located.

**Type**
string


Standard Objects DatacloudDandBCompany

**Field Name** **Details**

**Properties**
Nillable

**Description**

The corresponding exchange for a company’s stock symbol, for example, NASDAQ
or NYSE.

```
StockSymbol

Street

Subsidiary

ThirdNaics

ThirdNaicsDesc

```

**Type**
string

**Properties**
Nillable

**Description**

The abbreviation that’s used to identify publicly traded shares of a particular
stock.

**Type**
string

**Properties**
Nillable

**Description**

The street address where a company is physically located.

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**

Indicates whether a company is more than 50 percent owned by another
organization.

**Type**
string

**Properties**
Nillable

**Description**

A NAICS code used to further classify an organization by industry.

**Type**
string

**Properties**
Nillable


Standard Objects DatacloudDandBCompany

**Field Name** **Details**

**Description**

A brief description of an organization’s line of business, based on the
corresponding NAICS code.

```
ThirdSic

ThirdSic8

ThirdSic8Desc

ThirdSicDesc

TradeStyle1

```

**Type**
string

**Properties**
Nillable

**Description**

A SIC code used to further classify an organization by industry.

**Type**
string

**Properties**
Group, Nillable

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

**Type**
string

**Properties**
Group, Nillable

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
string

**Properties**
Nillable

**Description**

A brief description of an organization’s line of business, based on the
corresponding SIC code.

**Type**
string

**Properties**
Nillable


Standard Objects DatacloudDandBCompany

**Field Name** **Details**

**Description**

A name, different from its legal name, that an organization may use for conducting
business. Similar to “Doing business as” or “DBA”.

```
TradeStyle2

TradeStyle3

TradeStyle4

TradeStyle5

UsTaxId

```

**Type**
string

**Properties**
Nillable

**Description**

A tradestyle used by the organization.

**Type**
string

**Properties**
Nillable

**Description**

A tradestyle used by the organization.

**Type**
string

**Properties**
Nillable

**Description**

A tradestyle used by the organization.

**Type**
string

**Properties**
Nillable

**Description**

A tradestyle used by the organization.

**Type**
string

**Properties**
Nillable

**Description**

The identification number for the company used by the Internal Revenue Service
(IRS) in the administration of tax laws. Also referred to as Federal Taxpayer
Identification Number.


Standard Objects DatacloudDandBCompany

**Field Name** **Details**

```
Website

WomenOwned

YearStarted

Zip

```

Usage

**Type**
url

**Properties**
Filter, Group, Nillable

**Description**

An organization’s primary website address.

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**

Indicates whether a company is more than 50 percent owned or controlled by
a woman.

**Type**
string

**Properties**
Nillable

**Description**

The year when the company was established or the year when current ownership
or management assumed control of the company.

**Type**
string

**Properties**
Nillable

**Description**

A five or nine-digit code that’s used to help sort mail.

Use this object to return D&B Company information. These fields are read-only.

Important: DatacloudDandBCompany can’t be used in Apex test methods, because an external web service call is required to
access it. These calls are not allowed in Apex test methods.


### Standard Objects DatacloudOwnedEntity DatacloudOwnedEntity

Represents fields in the DatacloudOwnedEntity object. The DatacloudOwnedEntity object tracks user-purchased records. This object is
available in API version 30.0 or later.

Note: When your Data.com Prospector or Data.com Clean contract expires, Data.com features, objects, and fields are removed
from your org.

To support customers’ needs around compliance and to remain a leader in trust and privacy, Salesforce removed all contact data
from the Data.com service on February 1, 2021.

[For more information, see Data.com Prospector and Clean Retirement.](https://help.salesforce.com/articleView?id=000270376&language=en_US&type=1)

Supported Calls

`create()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
DataDotComKey

DatacloudEntityType

Name

```

**Type**
string

**Properties**
Create, Filter, Sort

**Description**

The Data.com contact or company record identification number used by the
DatacloudPurchaseUsage object to keep track of purchased records. This is
equivalent to the Data.com record ID for a contact or company.

**Type**
picklist

**Properties**
Create, Filter, Restricted picklist, Sort

**Description**

The type of Data.com record you want to purchase.

**•** 0—contact

**•** 1—company

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort


### Standard Objects DatacloudPurchaseUsage

**Field Name** **Details**

**Description**

An optional field used to name your record.

```
PurchaseType

PurchaseUsageId

UserId

```

Usage

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

A read only field set by the API to identify the purchase type.

**•** Added

**•** Export

**•** API

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The unique identification number for the DatacloudPurchaseUsage object created
by making a REST POST request.

**•** 0—contact

**•** 1—company

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

A unique identifier for the user making the purchase.

The Datacloud object that tracks records that are purchased and owned by a specific user.

### DatacloudPurchaseUsage

Represents an object used to identify and track Data.com record purchases. This object is available in API version 30.0 or later.


Standard Objects DatacloudPurchaseUsage

Note: When your Data.com Prospector or Data.com Clean contract expires, Data.com features, objects, and fields are removed
from your org.

To support customers’ needs around compliance and to remain a leader in trust and privacy, Salesforce removed all contact data
from the Data.com service on February 1, 2021.

[For more information, see Data.com Prospector and Clean Retirement.](https://help.salesforce.com/articleView?id=000270376&language=en_US&type=1)

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
DatacloudEntityType

Description

Name

PurchaseType

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The type of Data.com record you want to purchase.

**•** 0—indicates contact entity type.

**•** 1—indicates company entity type.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

An optional field. You can add a description for your purchase.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**

An optional field used to name your record.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort


Standard Objects DatacloudPurchaseUsage

**Field Name** **Details**

**Description**

A read only field set by the API to identify the purchase type.

**•** Added

**•** Export

**•** API

```
Usage

UserId

UserType

```

Usage

**Type**
double

**Properties**
Filter, Sort

**Description**

A read only field set by the API. It is used to track the points used to purchase
records.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

A read only field set by the API that identifies the user purchasing the records.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

A read only field set by the API with 2 user types.

**•** Monthly Usage

**•** List Pool User

The DatacloudPurchaseUsage object allows you to track Data.com record purchases for CRM users.


### Standard Objects DataDetectJobObjectSession DataDetectJobObjectSession

For internal use only. This object is available in API version 63.0 and later.

SEE ALSO:

_[Salesforce Help](https://help.salesforce.com/s/articleView?id=xcloud.einstein_data_detect.htm&type=5&language=en_US)_ : Data Detect

### DataDetectJobSession

Represents a run of a DataDetect scan policy that's triggered manually. This object is available in API version 63.0 and later.

Supported Calls

`delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`search()`, `undelete()`

Fields

**Field** **Details**

```
DataDetectPolicyId

DataDetectPolicySnapshotId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the scan policy associated with this job session.

This field is a relationship field.

**Relationship Name**
DataDetectPolicy

**Refers To**
DataDetectPolicy

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the snapshot of the scan policy associated with this job session.

This field is a relationship field.

**Relationship Name**
DataDetectPolicySnapshot


Standard Objects DataDetectJobSession

**Field** **Details**

**Relationship Type**
Master-Detail

**Refers To**
DataDetectPolicySnapshot

```
EndTime

HasClassicEncryptedField

Name

NamedEntityCount

PolicyJobStatus

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Time and date when the data scan completes.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates that if the user is permitted to view classic encrypted fields, they can view these
fields in the scan results.

The default value is false.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Auto-generated name of the job session.

**Type**
int

**Properties**
Create, Filter, Nillable, Update

**Description**
Aggregate count of PII found during the data scan.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Status of the data scan. Valid values are:


### Standard Objects DataDetectJobSessSummary

**Field** **Details**

**•** `Stopped`

**•** `Completed`

**•** `Failed`

**•** `PartialSuccess`

**•** `Running`

**•** `Scheduled`

**•** `TimedOut`

The default value is `Scheduled` .

```
RunByUser

SessionStartTime

```

Associated Objects

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
User who started the job session or data scan.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Time and date when the data scan begins.

This object has this associated object. If the API version isn’t specified, it's available in the same API version as this object. Otherwise, it's
available in the specified API version and later.

**[DataDetectJobSessionFeed](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

SEE ALSO:

_[Salesforce Help](https://help.salesforce.com/s/articleView?id=xcloud.einstein_data_detect.htm&type=5&language=en_US)_ : Data Detect

### DataDetectJobSessSummary

For internal use only. This object is available in API version 66.0 and later.


### Standard Objects DataDetectPolicy DataDetectPolicy

Represents a set of parameters that specifies the types of sensitive data for search with in a data scan. DataDetect scan policies can also
apply filters to a data scan, along with specific objects and fields for scanning. This object is available in API version 60.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
Description

EndTime

IsScheduled

Name

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the scan policy.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Time and date when the data scan completes.

**Type**
Boolean

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Determines if the policy is scheduled or not.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the scan policy.


### Standard Objects DataDetectPolicyObject

**Field** **Details**

```
OwnerId

ScanType

StartTime

```

SEE ALSO:

_[Salesforce Help](https://help.salesforce.com/s/articleView?id=xcloud.einstein_data_detect.htm&type=5&language=en_US)_ : Data Detect

**Type**
reference

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The UserID of the person who owns the record. This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Designates whether the data scan type is `AIInference` or `PatternMatching` .

The default value is `PatternMatching` .

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Time and date when the data scan begins. Data scans can start anytime within a 30-day
window from the current date.

### DataDetectPolicyObject

Represents an object of the DataDetect scan policy to be scanned. This object is available in API version 62.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`


### Standard Objects DataDetectScanResult

Fields

**Field** **Details**

```
DataDetectPolicyId

Name

ObjectReference

```

SEE ALSO:

_[Salesforce Help](https://help.salesforce.com/s/articleView?id=xcloud.einstein_data_detect.htm&type=5&language=en_US)_ : Data Detect

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the scan policy associated with this scan policy object.

This field is a relationship field.

**Relationship Name**
DataDetectPolicy

**Relationship Type**
Master-Detail

**Refers To**
DataDetectPolicy

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the scan policy object.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Name of the scan policy object to be scanned.

### DataDetectScanResult

Represents the results of a DataDetect data policy scan. This object is available in API version 63.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`


Standard Objects DataDetectScanResult

Fields

**Field** **Details**

```
CreatedDate

DataDetectJobSessionId

FieldName

NamedEntityCount

NamedEntityType

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Time and date when an instance of PII is added to the scan result.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the job session associated with the scan policy.

This field is a relationship field.

**Relationship Name**
DataDetectJobSession

**Relationship Type**
Lookup

**Refers To**
DataDetectJobSession

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
UMD name from standard fields, or custom field ID from custom fields.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Number of times PII is found.

**Type**
string

**Properties**
Filter, Group, Sort


### Standard Objects DataDetectPolicyObjField

**Field** **Details**

**Description**
Type of PII found in the record of the scan policy object.

```
ObjectName

RecordIdentifier

SensitiveValues

```

SEE ALSO:

_[Salesforce Help](https://help.salesforce.com/s/articleView?id=xcloud.einstein_data_detect.htm&type=5&language=en_US)_ : Data Detect

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
KeyPrefix of the scan policy object that contains PII.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Unique identifier for the record.

**Type**
text

**Properties**
Filter, Nillable, Sort

**Description**
Stores the excerpts in the form of encrypted text.

### DataDetectPolicyObjField

Represents an object field of the DataDetect scan policy object to be scanned. This object is available in API version 64.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`


### Standard Objects DataDetectPolicySnapshot

Fields

**Field** **Details**

```
DataDetectPolicyObjectId

FieldName

```

SEE ALSO:

_[Salesforce Help](https://help.salesforce.com/s/articleView?id=xcloud.einstein_data_detect.htm&type=5&language=en_US)_ : Data Detect

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the scan policy object associated with the scan policy object's field.

This field is a relationship field.

**Relationship Name**
DataDetectPolicyObject

**Relationship Type**
Master-Detail

**Refers To**
DataDetectPolicyObject

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Name of the scan policy object field.

### DataDetectPolicySnapshot

For internal use only. This object is available in API version 64.0 and later.

SEE ALSO:

_[Salesforce Help](https://help.salesforce.com/s/articleView?id=xcloud.einstein_data_detect.htm&type=5&language=en_US)_ : Data Detect

### DataDetPlcyDataSrchExps

Represents data search expressions for scanning DataDetect scan policies based on Java regex. This object is available in API version 64.0
and later.

Note: When working with regex, Salesforce recommends Java 17 or later.


Standard Objects DataDetPlcyDataSrchExps

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
DataDetectPolicyId

Expression

IsCaseSensitive

IsKeywordSearch

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the scan policy associated with the data search expression.

This field is a relationship field.

**Relationship Name**
DataDetectPolicy

**Relationship Type**
Master-Detail

**Refers To**
DataDetectPolicy

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Regular expression that represents sensitive data to be scanned.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Designates whether the expression is case-sensitive `(true)` or not `(false)` .

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


### Standard Objects DataDetPlcyMdatScanCrit

**Field** **Details**

**Description**
Designates whether the expression can be used as a search keyword `(true)` or not
`(false)` .

The default value is `false` .

```
Name

```

SEE ALSO:

_[Salesforce Help](https://help.salesforce.com/s/articleView?id=xcloud.einstein_data_detect.htm&type=5&language=en_US)_ : Data Detect

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the expression.

### DataDetPlcyMdatScanCrit

Represents inclusion and exclusion criteria that filter what DataDetect scan policy object fields are to be scanned based on metadata
tags. This object is available in API version 64.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
Criteria

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Defines category of inclusion or exclusion criteria applied to fields during scan policy creation.
Valid values are:

**•** `ComplianceCategory` —Compliance acts, definitions, or regulations related to the
field's data.

**•** `DataSensitivity` —Level of data sensitivity related to the field's data.


Standard Objects DataDetPlcyMdatScanCrit

**Field** **Details**

**•** `FieldUsage` —Data planned for deprecation, or intended to be hidden, related to
the active and visible field's data.

```
DataDetectPolicyId

Name

Type

Value

```

SEE ALSO:

_[Salesforce Help](https://help.salesforce.com/s/articleView?id=xcloud.einstein_data_detect.htm&type=5&language=en_US)_ : Data Detect

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the policy associated with the data search expression.

This field is a relationship field.

**Relationship Name**
DataDetectPolicy

**Relationship Type**
Master-Detail

**Refers To**
DataDetectPolicy

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the criteria.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Defines what criteria, `inclusion` or `exclusion`, is applied to a field in the policy scan
object.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Value of the criteria applied to filters.


### Standard Objects DataDetPlcySstvDataCatg DataDetPlcySstvDataCatg

Represents the sensitive data categories that the DataDetect scan policy is required to scan. This object is available in API version 64.0
and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
DataCategory

DataDetectPolicyId

Name

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Sensitive data category associated with the scan policy.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the scan policy associated with the sensitive data category.

This field is a relationship field.

**Relationship Name**
DataDetectPolicy

**Relationship Type**
Master-Detail

**Refers To**
DataDetectPolicy

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort


### Standard Objects DataEncryptionKey

**Field** **Details**

**Description**
Name of the sensitive data category.

SEE ALSO:

_[Salesforce Help](https://help.salesforce.com/s/articleView?id=xcloud.einstein_data_detect.htm&type=5&language=en_US)_ : Data Detect

### DataEncryptionKey

The DataEncryptionKey object is part of the Bring Your Own Key (BYOK) feature, which allows users to upload a data encryption key
(DEK) using a public key generated by the Salesforce Shield Key Management Service (KMS). Customers create their own DEKs and
upload them to Salesforce. Users access this entity via the API to list DEK keys for auditing purposes. They can also programmatically use
this object to create the certificate and to upload key material. This object is available in API version 63.0 and later.

DEKs are used to encrypt and decrypt data. They reside in either the Salesforce database or in an external KMS. They’re created by root
keys, and when persisted, wrapped by root keys as well.

Supported Calls

`create()`, `describeSObjects()`, `query(), queryAll()`

Special Access Rules

This object is available as part of the Shield and Salesforce Platform Encryption add-on subscriptions.

Fields

**Field** **Details**

```
CreatedBy

### `DataEncryptionKeyCertName`

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The email address of the user who created the DEK. For example, `user@example.com` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the certificate whose public key is used to encrypt the `DEK` during a remote
key callout. When you want to create a BYOK-compatible certificate, use this property in a


Standard Objects DataEncryptionKey

**Field** **Details**

call to create() to name the certificate. You need to know the name to retrieve the certificate
later. Specify only the file name. Salesforce will add the .crt extension when it creates the
file.

```
Description

DoesUseKeyDerivation

LastModifiedBy

RootKeyIdentifier

RootKeyKmsIdentifier

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user-defined description of the root key.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the DEK is intended to be used as part of a derived key ( `true` ) or not
( `false` [). See Components Involved in Deriving Keys for information on derived keys.](https://developer.salesforce.com/docs/atlas.en-us.262.0.securityImplGuide.meta/securityImplGuide/security_pe_components.htm)

The default value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The email address of the user who most recently modified the key. For example,
`user@example.com` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique key identifier assigned by Salesforce to the root key used to create the DEK.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects DataEncryptionKey

**Field** **Details**

**Description**
The unique key identifier from the external KMS, such as an AWS Amazon Resource Name
(ARN). For example,

```
                   arn:aws:kms:us-west-2:123456789000:key/123ab456-7cd8-9012-3e4f-5gh678i901j2

```

```
SecretValue

SessionToken

Source

Status

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**

The encrypted 256-bit secret value encoded in base64.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Contains the token for the session that was active when the DEK was last wrapped. If the
session is inactive, a new certificate is required in order to transmit the DEK.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The source of the encryption key material. Values are:

**•** `AWS` —A tenant secret or DEK fetched from the Amazon Key Management Service DEKs
with a `Source` value of `AWS` are listed as Fetched on the Key Management page in
Setup.

**•** `Salesforce` —A Salesforce-generated DEK.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The status of the key.

Possible values are:

**•** `Activation Pending` —Salesforce is waiting for confirmation of a valid key policy
in the external key store.

**•** `Active` —Can be used to encrypt new DEKs and decrypt existing DEKs.


Standard Objects DataEncryptionKey

**Field** **Details**

**•** `Archived` —Can’t encrypt new DEKs. Can be used to decrypt previously created DEKs.

**•** `Canceled` —Root key activation canceled by a user.

**•** `Inactive` —The root key, and the DEKs that it encrypts, are inaccessible. Inaccessible
DEKs can’t be used to decrypt data, which renders that data also inaccessible.

```
Type

Version

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of DEK. This value appears in the `Type` picklist:

**•** `Search Index` —search index files.

For Hyperforce orgs on API version 63.0 and later, create secrets of type `SearchIndex`
using the DataEncryptionKey object. For Hyperforce orgs on API versions 62.0 and earlier,
and for all non-Hyperforce orgs, create secrets of type `SearchIndex` using the
TenantSecret object.

You also specify a type of `SearchIndex` when you are creating a BYOK-compatible
certificate using the DataEncryptionKey object.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The version number of this secret. The version number is unique within your org.

Four functions are available: `describe()`, `create()`, `query()` and `queryAll()` .

**•** Use `create()` to create BYOK-compatible certificates and DEKs.

**•** Use `query()` or `queryAll()` to list one or all of your DEKs.

**•** Use `describe()` to get information abut the DataEncryptionKey object.

You use `create()` and `queryAll()` together to upload a Search Index Encryption DEK. Check the Examples section for how to
do each of these steps.

**•** Create a BYOK-compatible certificate with `create()` . This will create a temporary DEK to contain the certificate reference. Specify
a Type of `Search Index` and a name for the certificate file.

**•** Use `queryAll()` to list your DEKs. The temporary DEK will include the name of your certificate file in the
`DataEncryptionKeyCertName` attribute. It will also include a session token in the `sessionToken` attribute. Save this
value for later.


Standard Objects DataEncryptionKey

**•** Downlad the certificate using the metadata object API. Specify _`Certificate`_ for the object name node, and the
_`DataEncryptionKeyCertName`_ for the members node. The certificate file will be in the zip file returned by the metadata
object API.

**•** [Run the BYOK Search Index Encryption script to generate the](https://help.salesforce.com/s/articleView?id=xcloud.security_pe_byok_script_seas_tle.htm&type=5&language=en_US) **payload.bin** file which contains the plaintext of your new DEK. Use
the certificate file you created when you run the script. Alternatively, generate a key using a method of your choice. It must meet
[the specifications outlined in Bring Your Own Key Overview.](https://help.salesforce.com/s/articleView?id=xcloud.security_pe_byok.htm&type=5&language=en_US)

**•** Generate a b64 string from the contents of the **payload.bin** file.

**•** Run the `DataEncryptionKey.create()` method again, this time with the the b64 string and the session token. Specify:

```
     "SecretValue":"<b64 string>"

     "SessionToken":"<session token string>"

     "Type":"SearchIndex"

```

With success, the temporary DEK is replaced by the uploaded secret. The certificate is deleted, and the session token eventually
expires. A call to `queryAll()` will show the new DEK. The DEK will also appear on the Search Index Encryption Key Management
page.

Examples

[Use your preferred developer environment to run the examples. Use the Salesforce developer Introduction to REST API for basic information](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_rest.meta/api_rest/intro_rest.htm)
[on making REST calls into Salesforce. Also, Introducing the Salesforce Shield Platform Encryption REST API gives you starter information](https://developer.salesforce.com/docs/atlas.en-us.262.0.platform_encryption_rest_api_guide.meta/platform_encryption_rest_api_guide/api_rest_encryption.htm)
on using REST to work with Shield Platform Encryption.

**Create a BYOK-compatible certificate with** **`create()`**

To create a BYOK-compatible certificate, use a POST method to create an sObject of type `DataEncryptionKey` . Specify a Type
of `search index` (case insensitive), and an appropriate string value for DataEncryptionKeyCertName. You need to name the
certificate to retrieve it later. Specify just the name. Salesforce will add the .crt extension to the file.

```
     curl --location 'https://DOMAIN.my.salesforce.com/services/data/v62.0/sobjects/'\

                  DataEncryptionKey/create'

        --header 'Content-Type: application/json' \

        --header 'Authorization: Bearer TOKEN' \

        --data '{

             "Type": "search index",

             "DataEncryptionKeyCertName": "my-byok-compatible-cert"

            }'

```

**List all DEKs with** **`queryAll()`**

To retrieve DEKs, use `query` or `queryAll` on the `DataEncryptionKey` sObject. You must specify a limit for the query. All
DEKs are retrieved, including archived DEKs. You use `queryAll` to get the session token.

```
     curl --location

     'https://DOMAIN.my.salesforce.com/services/data/v63.0/queryAll/?q=SELECT+FIELDS(ALL)+FROM+DataEncryptionKey+LIMIT+10'

      \

                  --header 'Authorization: Bearer TOKEN'

```

**Download your Certificate**

[Retrieve the certificate using Metadata API. object to download your new certificate.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/file_based_zip_file.htm)

```
     <?xml version="1.0" encoding="UTF-8"?>

     <Package xmlns="http://soap.sforce.com/2006/04/metadata">

       <types>

```


Standard Objects DataEncryptionKey

```
         <members>DataEncryptionKeyCertName</members>

         <name>Certificate</name>

       </types>

       <version>65.0</version>

     </Package>

```

Your certificate will be contained in the cert folder.

**Create a DEK with** **`create()`**

To create the final DEK, use a POST method to create an sObject of type `DataEncryptionKey` . Specify a Type of `search`
`index` (case insensitive).

```
     curl --location

     'https://DOMAIN.my.salesforce.com/services/data/v63.0/sobjects/DataEncryptionKey/create'

      \

     --header 'Content-Type: application/json' \

     --header 'Authorization: Bearer TOKEN' \

     --data '{

       "SecretValue":"b64-secret"

       "SessionToken":"session-token value"

       "Type": "search index"

     }'

```

**Describe a DataEncryptionKey with** **`describe()`**

To get information about the DataEncryptionKey sObject, use `describe` .

```
     curl --location 'https://DOMAIN.my.salesforce.com/services/data/v62.0/sobjects/'\

                  DataEncryptionKey/describe'

                  --header 'Content-Type: application/json' \

                  --header 'Authorization: Bearer TOKEN'

```

On success, the response is the full JSON description of the DataEncryptionKey sObject.

**Return Values for Create()**

The response for creating a certificate or DEK are the same. On success, the response is be similar to

```
     {

       "totalSize": (COUNT),

       "done": true,

       "records": [

         {

          "attributes": {

          "type": "DataEncryptionKey",

          "url": "/services/data/v63.0/sobjects/DataEncryptionKey/(ID)"

          },

          ATTRIBUTE LIST

         },

       ]

```

On error, the response is similar to

```
     [

       {

         "message": "ERROR MESSAGE",

         "errorCode": "ERROR CODE"

```


### Standard Objects DataIntegrationRecordPurchasePermission

```
       }

     ]

### DataIntegrationRecordPurchasePermission

```

Indicates Lightning Data purchase credits that a Salesforce admin has granted to users.

This object is available in API versions 42.0 and later.

Supported Calls

`describeSObjects()`, `create()`, `delete()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

As of Spring ’20 and later, only your Salesforce org's internal users can access this object.

Fields

**Field Name** **Details**

```
ExternalObject

UserId

UserRecordPurchaseLimit

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the name of the data service record matched to the Salesforce record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Indicates the ID of a user to whom purchase credits are assigned.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

**Type**
int


### Standard Objects DataKitDeployEvent

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Represents the number of purchase credits assigned to a user.

### DataKitDeployEvent

Represents a data kit deployment event that notifies subscribers of the status of the data kit component deployment. This object is
available in API version 61.0 or later.

Supported Calls

`create()`, `describeSObjects()`

Special Access Rules

Users that have access to Data Cloud.

Fields

**Field** **Details**

```
DataKitDeployStatus

DataKitName

```

**Type**
picklist

**Properties**
Create, Nillable, Restricted picklist

**Description**
The deployment status of the components deployed from a data kit. This field is available in
API version 63.0 and later. Possible values are:

**•** `Active`

**•** `Deleting`

**•** `Error`

**•** `Inactive`

**•** `Processing`

**Type**
string

**Properties**
Create, Nillable


Standard Objects DataKitDeployEvent

**Field** **Details**

**Description**
Name of the data kit from which a component is deployed.

```
DataspaceName

DeployStartTime

ErrorDetails

EventCreationDate

EventPublishDate

EventType

```

**Type**
string

**Properties**
Create, Nillable

**Description**
Name of the data space into which a component is deployed.

**Type**
dateTime

**Properties**
Create, Nillable

**Description**
The date and time the deployment starts.

**Type**
textarea

**Properties**
Create, Nillable

**Description**
Explanation of the error.

**Type**
dateTime

**Properties**
Create, Nillable

**Description**
The date and time the data kit deploy creation event was created.

**Type**
dateTime

**Properties**
Create, Nillable

**Description**
The date and time of the data kit deploy publish event.

**Type**
picklist

**Properties**
Create, Nillable, Restricted picklist


Standard Objects DataKitDeployEvent

**Field** **Details**

**Description**
The event type action of the data kit components. Available in API version 66.0 and later.
Possible values are:

**•** `Deploy`

**•** `Undeploy`

```
EventUuid

IsDataKitDeployStatusSuccess

JobIdentifier

ReplayId

TemplateName

```

**Type**
string

**Properties**
Nillable

**Description**
The unique ID of the event.

**Type**
string

**Properties**
Create, Nillable

**Description**
Status of the data kit component deployment. Possible values are:

**•** `Active`

**•** `Failure`

**Type**
string

**Properties**
Create, Nillable

**Description**
Data kit component deployment job identifier.

**Type**
string

**Properties**
Nillable

**Description**
The ID of the data kit deploy event replay.

**Type**
string

**Properties**
Create, Nillable


### Standard Objects DataKitDeploymentLog

**Field** **Details**

**Description**
The template name from which the data kit deploy event is created.

### DataKitDeploymentLog

Represents the log details of a data kit component deployment. This object is available in API version 61.0 or later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

Users that have access to Data Cloud.

Fields

**Field** **Details**

```
BundleName

ComponentName

ComponentTemplateId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Name of the data stream bundle if a data stream is deployed from a data kit.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Name of the component that’s deployed from a data kit.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the data kit template from which the component is deployed. This field is a polymorphic
relationship field.


Standard Objects DataKitDeploymentLog

**Field** **Details**

**Relationship Name**
ComponentTemplate

**Refers To**
DataSourceBundle

```
ComponentType

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of the component for which the deployment is tracked in the log details.

Possible values are:

**•** `MktCalculatedInsight`

**•** `MktDataLakeObject`

**•** `MktDataModelObject`

**•** `MktDataStream`

**•** `MktDataTransform`

Possible values available in API version 63.0 and later are:

**•** `ActivationTarget`

**•** `DataAction`

**•** `DataActionTarget`

**•** `DataGraph`

**•** `DataSemanticSearch`

**•** `EngagementSignal`

**•** `ExtDataShare`

**•** `IdentityResolution`

**•** `MarketSegment`

**•** `MarketSegmentActivation`

**•** `MktDataConnection`

**•** `MktMLModel`

**•** `PersonalizationObjective`

**•** `PersonalizationRecommender`

Possible values available in API version 64.0 and later are:

**•** `IrRelatedListEnrichment`

**•** `MktCalculatedInsight`

**•** `MktDataLakeObject`

**•** `MktDataStream`

**•** `MktDataTransform`


Standard Objects DataKitDeploymentLog

**Field** **Details**

**•** `PersonalizationPoint`

**•** `PersonalizationSchema`

Possible values available in API version 66.0 and later are:

**•** `CopyFieldEnrichment`

**•** `SemanticModel`

```
DataKitName

DataPackageKitDefinition

DataSpaceName

DeployJob

DeploymentAction

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Name of the data kit being deployed.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
ID of the data kit being deployed. Available in API version 63.0 and later.

Possible values are:

**•** `1dk.Collections`

**•** `1dk.SalesNextGenForecastingDatakit`

**•** `1dk.Test_Fbdk`

**•** `1dk.sf_mktg_ae__Marketing_Account_Engagement_CRM_Data`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Name of the data space the components are deployed to.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The deployment job ID.

**Type**
picklist


Standard Objects DataKitDeploymentLog

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Deployment action of the data kit components.

Possible values are:

**•** `Deploy`

**•** `Undeploy`

```
DeploymentError

DeploymentStatus

FileBasedComponentTemplate

FlowInterviewIdentifier

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Contains the error details if the data kit deployment fails.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Deployment status of the data kit components.

Possible values are:

**•** `Failed`

**•** `Started`

**•** `Successful`

**Type**
string

**Properties**
Create, Filter, Sort, Update

**Description**
ID of the file-based component template that corresponds to the deployment log entry.
Available in API version 63.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Identifier of the flow interview if the deployment was triggered using a flow.


Standard Objects DataKitDeploymentLog

**Field** **Details**

```
JobIdentifier

LastReferencedDate

LastViewedDate

Name

OwnerId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Identifier of the data kit component deployment job. Available in API version 66.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed the deployment log file.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this deployment log.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The name of the deployment log.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user that owns the deployment.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User


Standard Objects DataKitDeploymentLog

**Field** **Details**

```
PublisherOrgComponentId

SubscriberOrgComponentId

TemplateVersion

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the component in the publisher org.

This field is a polymorphic relationship field.

**Relationship Name**
PublisherOrgComponent

**Refers To**
MktCalculatedInsight, MktDataTransform

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the component in the subscriber org in which the components of a data kit are
deployed.

This field is a polymorphic relationship field.

**Relationship Name**
SubscriberOrgComponent

**Refers To**
ActivationTarget, DataGraph, DataStream, ExtDataShare, IdentityResolution, MarketSegment,
MarketSegmentActivation, MktCalculatedInsight, MktDataTransform

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The version of the template from which the deployment was done.

Use the DataKitDeploymentLog object to track the deployment of a data kit component.


### Standard Objects DatasetExport DatasetExport

Represents a dataset exported from CRM Analytics. When a dataset is exported, the data is converted into a .csv file and the schema is
stored in a separate JSON file. These files are stored in two objects: DatasetExport and DatasetExportPart. DatasetExport acts as the header
and includes the JSON schema.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
CompressedMetadataLength

Metadata

MetadataLength

Owner

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field is required when a record in an object contains a BLOB (binary large object) field.
In the DataExport object, Metadata is the BLOB field.

**Type**
base64

**Properties**
Nillable

**Description**
Contains the JSON schema that describes the data in the CSV. This schema includes column
metadata such as type, format, and defaultValue.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field is required when a record in an object contains a BLOB (binary large object) field.
In the DataExport object, Metadata is the BLOB field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects DatasetExport

**Field** **Details**

**Description**
User ID of the owner, as specified in the `userId` parameter in the export node of the
dataflow that created the record. Only the specified owner can read the content of the record.

```
PublisherInfo

PublisherType

Status

```

**Type**
string

**Properties**
Filter, idLookup, Sort

**Description**
Identifies the export record to facilitate searching when a user has multiple export records.
By default, this column is set to the ID of the dataflow that generated the export record,
concatenated with the name of the specific export node. PublisherInfo is unique within your
organization.

Note: A dataflow can have multiple export nodes.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Target of the export, as specified in the `target` parameter in the export node of the
dataflow that created the record. The value must be _`EinsteinDiscovery`_ .

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Status of the export. The possible values are:

**•** New

**•** InProgress

**•** Completed

**•** Canceled

**•** Failed

Note: The content of the Metadata field can be downloaded when the status is
Completed.


### Standard Objects DatasetExportPart

Usage

This object is used with the DatasetExportPart object for exporting data from a dataset in CRM Analytics for use in Einstein Discovery.
An export is initiated using the export node in an Analytics dataflow.

SEE ALSO:

### DatasetExportPart DatasetExportPart

Represents a dataset exported from CRM Analytics. When a dataset is exported, the data is converted into a .csv file and the schema is
stored in a separate JSON file. These files are stored in two objects: DatasetExport and DatasetExportPart. DatasetExportPart contains
parts of the .csv file.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
CompressedDataFileLength

DataFile

DataFileLength

```

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
This field is required when a record in an object contains a BLOB (binary large object) field.
In the DataExportPart object, DataFile is the BLOB field.

**Type**
base64

**Description**
Contains a part of the dataset data from the generated .csv file. Maximum size is 32 MB.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
This field is required when a record in an object contains a BLOB (binary large object) field.
In the DataExportPart object, DataFile is the BLOB field.


### Standard Objects DataMaskCustomValueLibrary

**Field** **Details**

```
 DatasetExportId

 Owner

 PartNumber

```

Usage

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the parent record that the part record is associated with.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
User ID of the owner, as specified in the `userId` parameter in the export node of the
dataflow that created the record. Only the specified owner can read the content of the record.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Used with the DatasetExportId to uniquely identify the data part. Parts are assembled
sequentially based on their numbers.

This object is used with the DatasetExport object for exporting data from a dataset in CRM Analytics for use in Einstein Discovery. An
export is initiated using the export node in an Analytics dataflow.

SEE ALSO:

DatasetExport

### DataMaskCustomValueLibrary

Represents a set of user-inputted values in a custom library in Data Mask. This object is available in API version 64.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects DataMaskCustomValueLibrary

Special Access Rules

This object is available with the Sandbox Data Mask managed package.

Fields

**Field** **Details**

```
ContentType

Description

IsActive

LastReferencedDate

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of value used in a field of the custom library.

Possible values are:

**•** `email`

**•** `number`

**•** `phone_number`

**•** `string`

**•** `url`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the value in the custom library.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Represents whether the library is active or inactive for use.

The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.


Standard Objects DataMaskCustomValueLibrary

**Field** **Details**

```
LastViewedDate

Name

OwnerId

Type

Values

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the custom library.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the custom library.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Represents how the values were added to the library.

Possible values are:

**•** `default`

**•** `user_defined`

**Type**
textarea

**Properties**
Create, Nillable, Update


### Standard Objects DataStatistics

**Field** **Details**

**Description**
The content of the value field for masking data.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**DataMaskCustomValueLibraryOwnerSharingRule on page 65**
Sharing rules are available for the object.

**DataMaskCustomValueLibraryShare on page 67**
Sharing is available for the object.

### DataStatistics

For internal use only.

### DataUseLegalBasis

Represents the legal basis for contacting a customer, such as billing or contract. This object is available in API version 45.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available if Data Protection and Privacy is enabled.

Fields

**Field Name** **Details**

```
Description

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the data use legal basis.


Standard Objects DataUseLegalBasis

**Field Name** **Details**

```
LastReferencedDate

LastViewedDate

Name

OwnerId

Source

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this
record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is
null, it’s possible that this record was referenced ( `LastReferencedDate` )
and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Specifies a name for the legal basis. For example, “billing” or “contract”.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the account associated with this customer.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
string


### Standard Objects DataUsePurpose

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the source of the legal basis. For example, the URL of a contract.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**DataUseLegalBasisChangeEvent (API version 62.0)**
Change events are available for the object.

**DataUseLegalBasisHistory**

History is available for tracked fields of the object.

**DataUseLegalBasisOwnerSharingRule**

Sharing rules are available for the object.

**DataUseLegalBasisShare**

Sharing is available for the object.

### DataUsePurpose

Represents the reason for contacting a prospect or customer, such as for billing, marketing, or surveys. This object is available in API
version 45.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available if Data Protection and Privacy is enabled.

Fields

**Field Name** **Details**

```
CanDataSubjectOptOut

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects DataUsePurpose

**Field Name** **Details**

**Description**
Required. Indicates whether the customer can decline contact for the described
purpose.

```
Description

LastReferencedDate

LastViewedDate

LegalBasisId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the purpose for contacting a customer.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this
record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is
null, it’s possible that this record was referenced ( `LastReferencedDate` )
and not viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Identifies the legal basis record associated with the data use purpose.

This is a relationship field.

**Relationship Name**
LegalBasis

**Relationship Type**
Lookup

**Refers To**
DataUseLegalBasis


Standard Objects DataUsePurpose

**Field Name** **Details**

```
Name

OwnerId

PurposeId

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Identifies the reason for contacting a customer. For example, billing or
marketing.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the account associated with this customer.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of an object containing data specific to the data use purpose.

This is a polymorphic relationship field.

**Relationship Name**
Purpose

**Relationship Type**
Lookup

**Refers To**
Asset, CareProgram, CareRegisteredDevice, or Product2

This object has the following associated objects. Unless noted, they’re available in the same API version as this object.


### Standard Objects DataWeaveResource

**DataUsePurposeChangeEvent (API version 62.0)**
Change events are available for the object.

**DataUsePurposeHistory**

History is available for tracked fields of the object.

**DataUsePurposeOwnerSharingRule**

Sharing rules are available for the object.

**DataUsePurposeShare**

Sharing is available for the object.

### DataWeaveResource

Represents the DataWeaveScriptResource class that is generated for all DataWeave scripts. This object is available in API version 58.0
and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`

Fields

**Field** **Details**

```
ApiVersion

BodyLength

ContentType

```

**Type**
double

**Properties**
Filter, Sort

**Description**
The API version of this component.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Size of the DataWeave script (in bytes).

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort


Standard Objects DataWeaveResource

**Field** **Details**

**Description**
Possible value:

**•** `dwl` : The metadata file for the DataWeave scripts that are deployed to an org.

```
DeveloperName

IsGlobal

IsProtected

Language

MasterLabel

NamespacePrefix

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique name of the object in the API.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
When set to true, the generated `DataWeaveScriptResource` class is global. The
default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Not used

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language of the MasterLabel.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Required. The name of the resource.

**Type**
string


### Standard Objects DatedConversionRate

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can
refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that aren’t Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

Usage

Although the `DataWeaveResource` object supports the create and update field properties, a runtime exception occurs if you try
to create, update, or delete using the API. Instead, use the Salesforce Extensions for Visual Studio Code.

### DatedConversionRate

Represents the dated exchange rates used by an organization for which the multicurrency and the effective dated currency features are
enabled.

Supported Calls

`delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

Special Access Rules

Customer Portal users can't access this object.

Fields

**Field** **Details**

```
ConversionRate

```

**Type**
double


### Standard Objects DealIndirectPartner

**Field** **Details**

**Properties**
Filter, Update

**Description**
Required. Conversion rate of this currency type against the corporate currency.

```
IsoCode

NextStartDate

StartDate

```

Usage

**Type**
picklist

**Properties**
Filter, Restricted picklist

**Description**
Required. ISO code of the currency. Must be one of the valid alphabetic, three-letter currency
ISO codes defined by the ISO 4217 standard, such as `USD`, `GBP`, or `JPY` . Must be unique
within your organization. Label is **Currency ISO Code** . The `CUC` (Cuban Convertible Peso)
picklist value is not available in API version 65.0 and later. Existing
`DatedConversionRate` records for `CUC` are no longer supported.

**Type**
date

**Properties**
Filter, Nillable

**Description**
Read only. The date on which the next effective dated exchange rate will start. Effectively
the day after the end date for this exchange rate.

**Type**
date

**Properties**
Filter

**Description**
The date on which the effective dated exchange rate starts. The timestamp is determined
by the base calendar of the API.

This object is for multicurrency organizations with advanced currency management enabled. Use this object to define the exchange
rates your organization uses for a date range. This object is not available in single-currency organizations, nor is it available if the
organization does not have advanced currency management enabled.

### DealIndirectPartner

Represents an indirect partner’s involvement in a deal. This object is available in API version 63.0 and later.


Standard Objects DealIndirectPartner

A DealIndirectPartner record can be created manually or through automation when a partner is associated with an opportunity, lead,
or account, capturing role and contact information.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AccountId

LastReferencedDate

LastViewedDate

LeadId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The account associated with the indirect partner on the deal.

This field is a relationship field.

**Relationship Name**
Account

**Refers To**
Account

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the record was last referenced by the user or system.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and the timestamp when the record was last viewed in the Salesforce UI. Helps monitor
user access and engagement.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects DealIndirectPartner

**Field** **Details**

**Description**
Reference to a lead associated with this indirect partner record.

This field is a relationship field.

**Relationship Name**
Lead

**Refers To**
Lead

```
Name

OpportunityId

OwnerId

PartnerName

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
System-generated unique identifier for the record, used for lookup and reference purposes.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Opportunity associated with the indirect partner.

This field is a relationship field.

**Relationship Name**
Opportunity

**Refers To**
Opportunity

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
User or group that owns this record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
string


Standard Objects DealIndirectPartner

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Name of the indirect partner participating in the deal. This field captures the business or
entity name.

```
PartnerRoleType

PrimaryContactFirstName

PrimaryContactLastName

PrimaryContactName

PrimaryContactSalutation

```

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The role played by the indirect partner in the deal. Common values might include Reseller,
Distributor, and so on.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
First name of the primary contact at the partner organization.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Last name of the primary contact at the partner organization.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Full name of the primary contact. This field may be auto-generated by combining first and
last names or used for reporting purposes.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects DeclinedEventRelation

**Field** **Details**

**Description**
Salutation for the primary contact.

Possible values are:

**•** `Dr.`

**•** `Mr.`

**•** `Mrs.`

**•** `Ms.`

**•** `Mx.`

**•** `Prof.`

### DeclinedEventRelation Represents event participants (invitees or attendees) with the status Declined for a given event.This object is available in API versions

29.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
EventId

RelationId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the ID of the event.

This is a relationship field.

**Relationship Name**
Event

**Relationship Type**
Lookup

**Refers To**
Event

**Type**
reference


Standard Objects DeclinedEventRelation

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the ID of the invitee.

This is a polymorphic relationship field.

**Relationship Name**
Relation

**Relationship Type**
Lookup

**Refers To**
Calendar, Contact, Lead, User

```
RespondedDate

Response

Type

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Indicates the most recent date and time when the invitee declined an invitation
to the event.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the content of the response field. Label is `Comment` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates whether the invitee is a user, lead or contact, or resource.


### Standard Objects DelegatedAccount

Usage

**Query invitees who have declined an invitation to an event**

```
     SELECT eventId, type, response FROM DeclinedEventRelation WHERE eventid='00UTD000000ZH5LA'

```

SEE ALSO:

AcceptedEventRelation

UndecidedEventRelation

### DelegatedAccount

Represents the external managed account. This object is available in API version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `update()`, `upsert()`

Special Access Rules

You must have a Partner or Customer Community Plus license. You can't edit the visibility of DelegatedAccount metadata on user profiles.

Fields

**Field** **Details**

```
AccessBuyFor

AccessManageUsers

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
The access that an admin authorizes for an external user to buy for other accounts. This field
is available in API version 50.0 and later. A B2B Commerce license is required to use
AccessBuyFor.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
The access that an admin authorizes for an external user to manage external users on other
accounts. This includes managing permission sets, membership, passwords, and activation.


Standard Objects DelegatedAccount

**Field** **Details**

This field is available in API version 50.0 and later. Delegated External User Administrator
permission is required to use AccessManageUsers.

```
LastReferencedDate

LastViewedDate

ManagedById

Name

OwnerId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced ( `LastReferencedDate` ) and not viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the managing user.

This is a relationship field.

**Relationship Name**
ManagedBy

**Relationship Type**
Lookup

**Refers To**
User

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the external managed account.

**Type**
reference


Standard Objects DelegatedAccount

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the record owner.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

```
ParentId

TargetId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the managing users account. This field is available in API version 50.0 and later.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the account being managed.

This is a relationship field.

**Relationship Name**
Target

**Relationship Type**
Lookup

**Refers To**
Account


### Standard Objects DeleteEvent DeleteEvent

Represents a record that has been soft deleted. Search on this object was available in API version 48.0, then removed in API version 50.0.

### DeleteEvent is a read-only object. You can't create, update, or delete it directly. To create a DeleteEvent record, soft delete a record of

[another type, like an Account. To remove a DeleteEvent record, use the emptyRecycleBin() API or hard delete the corresponding](https://developer.salesforce.com/docs/atlas.en-us.262.0.api.meta/api/sforce_api_calls_emptyrecyclebin.htm) `Record` .

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
DeletedById

DeletedDate

Record

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user who deleted the record.

This is a relationship field.

**Relationship Name**
DeletedBy

**Relationship Type**
Lookup

**Refers To**
User

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the record was deleted.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the record that was deleted.


### Standard Objects DeliveryEstimationSetup

**Field** **Details**

```
RecordName

SobjectName

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the record that was deleted.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of record that was deleted, for example, Account.

### DeliveryEstimationSetup

Shows the configuration options for the commerce delivery service offered through a web store or sales channel. Includes settings such
as delivery location group, channel, fulfillment types, and default fulfillment time. This object is available in API version 61.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The DeliveryEstimationSetup object is available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

`Channel` Id

`DefaultBusinessHours` Id

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID for the web store or sales channel associated with the delivery estimation configuration.

**Type**
reference


Standard Objects DeliveryEstimationSetup

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID for the default business hours.

This is a relationship field.

**Relationship Name**
DefaultBusinessHours

**Refers To**
BusinessHours

```
DefaultPickupTime

DefaultProcessingTime

DefaultProcessingTimeUnit

ExternalReference

```

**Type**
time

**Properties**
Create, Filter, Sort, Update

**Description**
Default pickup time.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Default processing time.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Default processing time unit. Possible values are:

**•** `Hours`

**•** `Days`

**•** `Weeks`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


Standard Objects DeliveryEstimationSetup

**Field** **Details**

**Description**
Unique code, reference, or identifier for the delivery estimation configuration record used
by external systems. Can be the name of the web store or sales channel associated with the
configuration to ensure a unique ID within the organization.

For example, `DefaultWebstore123` .

```
isEnabled

LastReferencedDate

LastSyncedById

LastSyncedDate

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the given delivery estimation configuration is active.

The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the record was last modified. Its label in the user interface is `Last`
`Modified Date` .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
User ID of who performed the last sync for this delivery estimation configuration. This field
is available in API version 62.0 and later.

This is a relationship field.

**Relationship Name**
LastSyncedBy

**Refers To**
User

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects DeliveryEstimationSetup

**Field** **Details**

**Description**
Date the delivery estimation configuration was last synced. This field is available in API version
62.0 and later.

```
LastSyncedMessage

LastViewedDate

LocationGroupId

Name

OwnerId

```

**Type**
textarea

**Properties**
Nillable

**Description**
Message that occurred during the last sync. This field is available in API version 62.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Last time the delivery estimation configuration was viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Represents a group of Omnichannel Inventory locations.

This is a relationship field.

**Relationship Name**
LocationGroup

**Refers To**
LocationGroup

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the delivery estimation setup configuration.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects DeliveryEstimationSetup

**Field** **Details**

**Description**
ID of the user who currently owns this DeliveryEstimationSetup object. Default value is the
user logged in to the API to perform the create.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

```
RoutingType

ServiceRegion

SyncStatus

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Determines an order's route and calculates delivery estimations. This field is available in API
version 65.0 and later.

Possible values are:

**•** `DRE`

**•** `None`

**•** `Standard`

The default value is `None` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
An org's commerce delivery service provisioning region (North America, Europe, or Asia)
that's set when Delivery Estimation is enabled in the Order Management app. It can't be
changed. If the field is empty, provisioning hasn't occurred yet. Available in API version 63.0
and later.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Sync status of the delivery estimation setup configuration.

Possible values are:

**•** `Deleting`

**•** `Deprovisioned`


### Standard Objects DigitalSignature

**Field** **Details**

**•** `Error`

**•** `None`

**•** `Synced`

**•** `Syncing`

The default value is `NONE` . This field is available in API version 62.0 and later.

### DigitalSignature

Represents a signature captured on a service report in field service.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,

```
   undelete()

```

Special Access Rules

Field Service must be enabled.

Fields

**Field Name** **Details**

### `DigitalSignatureNumber`

```
DocumentBody

DocumentContentType

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated number identifying the signature.

**Type**
base64

**Properties**
Create

**Description**
The captured signature image.

**Type**
picklist


Standard Objects DigitalSignature

**Field Name** **Details**

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The data type of the captured signature. Possible values are:

**•** `audio/acc`

**•** `audio/amr`

**•** `audio/ogg`

**•** `video/3gpp2`

**•** `video/3gpp`

**•** `image/avif`

**•** `text/calendar`

**•** `audio/x-caf`

**•** `image/webp`

```
DocumentLength

DocumentName

ParentId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The length of the captured signature.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The name of the captured signature image.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the service appointment, work order, or work order line item that the service
report is generated for.

This is a polymorphic relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup


Standard Objects DigitalSignature

**Field Name** **Details**

**Refers To**
AuthorizationFormConsent, Order, ServiceAppointment, WorkOrder,
WorkOrderLineItem

```
Place

SignatureType

SignedBy

SignedDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The place where the report was signed.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort

**Description**
The role of the person signing the service report. Your org comes with one
signature type, `Default` . A service report template can only contain one
signature per type. If you plan to collect multiple signatures on service reports,
create additional values for the Signature Type field.

Create at least one value for every role that might need to sign a service report.
For example, `Technician`, `Customer`, `Supervisor`, or `Supplier` . If
some service reports will be signed by multiple people in one role—for example,
all technicians present at an appointment—create numbered types:
`Technician 1`, `Technician 2`, and so forth.

Note: You can create up to 1,000 signature types. You can’t delete
signature types, but you can deactivate them so they can’t be used in
service report templates. When you deactivate a type, it still appears on
service report templates that used it, but you can’t use it on new service
report templates.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The name of the person signing.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort


### Standard Objects DigitalWallet

**Field Name** **Details**

**Description**
The date and time of the signing.

Usage

Add signature blocks to service report templates to determine which signatures need to be gathered on reports that use the template.
Service report templates can contain up to 20 signatures, and each signature must use a different Signature Type. For example, create
a standard service report template that contains a customer signature and a technician signature.

[To learn more about digital signatures, see Guidelines for Using Signatures on Service Reports.](https://help.salesforce.com/articleView?id=fs_signature_guidelines.htm&language=en_US)

Associated Objects

This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**DigitalSignatureChangeEvent (Available in API version 57.0)**
Change events are available for the object.

### DigitalWallet

Represents a customer’s digital wallet service. Salesforce Payments can use a digital wallet as a payment source when processing
payments through a payment gateway. This object is available in API version 48.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

To access Salesforce Payments objects with the API, your org must have one or more of these licenses: Salesforce Payments, Salesforce
Order Management, B2B Commerce, or D2C Commerce. Salesforce Payments objects are available only in Lightning Experience.

Fields

**Field** **Details**

```
AccountId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The account of the customer owns the digital wallet.


Standard Objects DigitalWallet

**Field** **Details**

This field is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

```
AuditEmail

BillingName

Comments

CompanyName

Customer

```

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Email address of the digital wallet owner where audit information about payments gets sent.

This field is available in API v49.0 and later. It doesn’t appear in the UI by default for Salesforce
orgs that upgraded from v48.0. Users must add it to the DigitalWallet page layout on their
own.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Billing name linked to customer's digital wallet. Available in API version 64.0 and later.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Users can provide additional details about the digital wallet. Supports a maximum of 1000
characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Company of the digital wallet owner.

**Type**
string


Standard Objects DigitalWallet

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Customer name of the digital wallet owner.

```
DigitalWalletNumber

Email

ExtendedPaymentMethodType

GatewayToken

GatewayTokenDetails

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
System-generated reference number for the digital wallet.

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Email of the digital wallet owner.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Other digital payment methods used for the transaction. This field value is required when
the value of the `PaymentMethodType` field is
`extd_altrn_payment_method_type` or `extd_wallet` . This field is available
in API version 66.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Unencrypted unique token ID generated by the payment gateway to represent the digital
wallet during transactions. This field is available for backward compatibility. To secure the
token, use the `GatewayTokenEncrypted` field.

If you try to record a GatewayToken for a digital wallet that already has a GatewayToken or
GatewayTokenEncrypted value, Salesforce throws an error.

**Type**
textarea


Standard Objects DigitalWallet

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Unique ID generated by the payment gateway for the card for future transactions.

```
GatewayTokenEncrypted

IpAddress

IsAutoPayEnabled

LastReferencedDate

```

**Type**
encryptedstring

**Properties**
Create, Nillable, Update

**Description**
Encrypted unique token ID generated by the payment gateway to represent the digital wallet
during transactions. Encrypted using Salesforce Classic Encryption for custom fields.

Available in API v52.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The IP address of the digital wallet owner.

This field is available in API v49.0 and later. It doesn’t appear in the UI by default for Salesforce
orgs that upgraded from v48.0. Users must add it to the DigitalWallet page layout on their
own.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

Indicates whether the payment method can be used for recurring payments (True) or not
(False). The default value is False.

This field is available in API v55.0 and later. For orgs that upgraded from v54.0, you must add
this field to the Digital Wallet page layout in the UI. It isn't automatically added.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.


Standard Objects DigitalWallet

**Field** **Details**

```
LastViewedDate

MacAddress

NickName

PaymentGatewayId

PaymentMethodAddress

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it's
possible the user only referenced this record (LastReferencedDate) but not viewed it.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The MAC address of the digital wallet owner.

This field is available in API v49.0 and later. It doesn’t appear in the UI by default for Salesforce
orgs that upgraded from v48.0. Users must add it to the DigitalWallet page layout on their
own.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
User-defined nickname for the digital wallet.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Gateway used with transactions for the digital wallet.

This field is a relationship field.

**Relationship Name**
PaymentGateway

**Relationship Type**
Lookup

**Refers To**
PaymentGateway

**Type**
address


Standard Objects DigitalWallet

**Field** **Details**

**Properties**
Filter, Nillable

**Description**
Full address associated with the digital wallet payment method. For more information about
address fields, see Address Compound Fields

```
PaymentMethodCity

PaymentMethodCountry

PaymentMethodDetails

PaymentMethodGeocodeAccuracy

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Part of the address for the payment method.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Part of the address for the payment method.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Optional information about the payment method type. This field is available in API version
57.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Accuracy level of the geocode for the payment method address. An accuracy level contains
information about the location of a latitude and longitude. For more information about
geolocation fields, see Geolocation Compound Field.

Possible values are:

**•** `Address`

**•** `Block`

**•** `City`

**•** `County`


Standard Objects DigitalWallet

**Field** **Details**

**•** `ExtendedZip`

**•** `NearAddress`

**•** `Neighborhood`

**•** `State`

**•** `Street`

**•** `Unknown`

**•** `Zip`

```
PaymentMethodLatitude

PaymentMethodLongitude

PaymentMethodPostalCode

PaymentMethodState

PaymentMethodStreet

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Latitude of the payment method address. Used with the PaymentMethodLongitude to
specify the precise geolocation of the address. For details on geolocation compound fields,
see Compound Field Considerations and Limitations.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Latitude of the payment method address. Used with the PaymentMethodLatitude to specify
the precise geolocation of the address. For details on geolocation compound fields, see
Compound Field Considerations and Limitations.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Part of the address for the payment method.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Part of the address for the payment method.

**Type**
textarea


Standard Objects DigitalWallet

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Part of the address for the payment method.

```
PaymentMethodSubType

PaymentMethodType

Phone

ProcessingMode

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
More information about the payment method. For example, if the PaymentMethodType is
Visa, this field can be digital wallet. This field is available in API version 57.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Payment method used for the transaction. Possible values include credit cards such as Visa
and American Express, digital wallets like Apple Pay and PayPal, direct debits such as ACH,
BECS, Bacs, non-card payments methods such as EPS, SEPA, and iDEAL, extended alternate
payments methods, and extended wallets. This field is available in API version 57.0 and later.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Phone number of the digital wallet owner.

This field is available in API v49.0 and later. It doesn’t appear in the UI by default for Salesforce
orgs that upgraded from v48.0. Users must add it to the DigitalWallet page layout on their
own.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Defines whether the digital wallet is used for transactions made inside or outside the payment
platform.

Possible values are:

**•** `External` —Transactions happened outside of the Salesforce payments platform.


### Standard Objects DirectMessage

**Field** **Details**

**•** `Salesforce` —Salesforce made and recorded an external call to the payment platform.

This field is available in API v49.0 and later. It doesn’t appear in the UI by default for Salesforce
orgs that upgraded from v48.0. Users must add it to the DigitalWallet page layout on their
own.

Important: `ProcessingMode` is required to create a DigitalWallet entity.

```
SavedPaymentMethodId

Status

### DirectMessage

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the saved payment method record.

**Relationship Name**
SavedPaymentMethod

**Relationship Type**
Lookup

**Refers To**
SavedPaymentMethod

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Defines the state of the digital wallet as a payment source.

Possible values are:

**•** `Active` —Customers can make payments with the digital wallet.

**•** `Canceled` —The digital wallet can no longer be used for payments. This status can’t
be changed.

**•** `InActive` —The digital wallet can’t be used for payments until a user changes its
status to Active.

Represents a direct message conversation between multiple users in Chatter. This object is available in API version 38.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`, `update()`


### Standard Objects Division

Special Access Rules

You must have the Manage Chatter Messages and Direct Messages permission enabled to access the DirectMessage object.

Fields

**Field** **Details**

```
 Name

 Subject

```

Usage

**Type**
string

**Properties**
Filter, Group, idLookup, Sort, Update

**Description**
A default value that isn’t visible to users.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Subject of the overall direct message conversation.

DirectMessage is an object used by Salesforce to control DirectMessage conversations. It represents a record of a direct message
conversation, but doesn’t include conversation data, such as posts or comments. It is most frequently used to moderate direct message
data in order to meet data compliance regulations.

### Division

A logical segment of your organization's data. For example, if your company is organized into different business units, you could create
a division for each business unit, such as “North America,” “Healthcare,” or “Consulting.” Available only if the organization has the Division
permission enabled.

Supported Calls

`create()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

### • Divisions must be enabled for your organization to access this object. To discover whether divisions have been enabled for an

organization, inspect the User or Group object for the `DefaultDivision` field—if it is present, then divisions have been enabled,
and this field (the field is named Division in objects other than User and Group) will be available in all relevant objects.

**•** Customer Portal users can’t access this object.


Standard Objects Division

Fields

**Field** **Details**

```
IsActive

IsGlobalDivision

Name

SortOrder

```

Usage

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Update

**Description**
Indicates whether the division is active ( `true` ) or not ( `false` ). Label is **Active** .

**Type**
boolean

**Properties**
Defaulted on createFilter

**Description**
Indicates whether the division is your organization’s global default division ( `true` )
or not ( `false` ). Label is **Global Division** .

**Type**
string

**Properties**
Create, Filter, Update

**Description**
A descriptive name for the division. Limit: 80 characters.

**Type**
int

**Properties**
Create, Filter, Nillable, Update

**Description**
The order in which this division name appears in the Division picklist field when
creating or editing users in the Salesforce user interface.

The values available for that field are the global division ID for the organization, created when divisions are first enabled, and any other
division IDs that have been created. The division ID associated with a user is populated in the objects owned or created by the user.

You can use the division ID to make searches, reports, and list views run more quickly and return more relevant results if an organization
has very large data sets. For more information, see the Salesforce online help, in the Fields description for the object.

You can use WITH in SOSL to pre-filter results based on division. This is faster than specifying the division in a WHERE clause.


### Standard Objects DivisionLocalization Note: The User object has a Division field that is unrelated to this object. The Division field is a standard text field similar

to Company or Department that has no special properties. Do not confuse it with the `DefaultDivision` field, which does
relate to this object.

SEE ALSO:

Overview of Salesforce Objects and Fields

### DivisionLocalization

When the Translation Workbench is enabled for your organization, the DivisionLocalization object provides the translation of the label
for a division.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Special Access Rules

**•** Your organization must be using Professional, Enterprise, Developer, Unlimited, or Performance Edition and be enabled for the
Translation Workbench.

**•** To view this object, you must have the “View Setup and Configuration” permission.

Fields

**Field** **Details**

```
Language

NamespacePrefix

```

**Type**
string

**Properties**
Create, Filter, Nillable, Restricted picklist

**Description**
The language for this translated label.

**Type**
string

**Properties**
Filter, Nillable

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org
that creates a managed package has a unique namespace prefix. Limit: 15 characters.
You can refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.


### Standard Objects DocAtchDownloadEventLog

**Field** **Details**

The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix
of the org for all objects that support it, unless an object is in an installed managed
package. In that case, the object has the namespace prefix of the installed
managed package. This field’s value is the namespace prefix of the Developer
Edition org of the package developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set only
for objects that are part of an installed managed package. All other objects have
no namespace prefix.

```
 ParentId

 Value

```

Usage

**Type**
reference

**Properties**
Create, Filter, Nillable

**Description**
The ID of the Division associated with the label that is being translated.

**Type**
string

**Properties**
Create, Filter, Nillable, Update

**Description**
The actual translated label for the division. Label is **Translation** .

Use this object to translate the labels of your divisions into the different languages supported by Salesforce.

### DocAtchDownloadEventLog

Document Attachment Downloads events contain details of document and attachment downloads. This object is available in API version
65.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.


Standard Objects DocAtchDownloadEventLog

Fields

**Field** **Details**

```
FileType

ObjectIdentifier

RequestIdentifier

Timestamp

UserIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of the file or attachment.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the object that’s associated with the document or attachment.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same REQUEST_ID..

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.

For example: `00530000009M943`


### Standard Objects Document Document

Represents a file that a user has uploaded. Unlike Attachment records, documents are not attached to a parent object.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

You must have the “Edit” permission on documents and the appropriate access to the Folder that contains a document in order to create
or update a document in that Folder.

Fields

**Field** **Details**

```
AuthorId

Body

BodyLength

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the User who is responsible for the Document.

This is a relationship field.

**Relationship Name**
Author

**Relationship Type**
Lookup

**Refers To**
User

**Type**
base64

**Properties**
Create, Nillable, Update

**Description**
Required. Encoded file data. If specified, then do not specify a URL.

**Type**
int

**Properties**
Filter, Group, Sort


Standard Objects Document

**Field** **Details**

**Description**
Size of the file (in bytes).

```
ContentType

Description

DeveloperName

FolderId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Type of content. Label is **Mime Type** . Limit: 120 characters.

If the `Don't allow HTML uploads as attachments or document`
`records` security setting is enabled for your organization, you cannot upload files with
the following file extensions: `.htm`, `.html`, `.htt`, `.htx`, `.mhtm`, `.mhtml`, `.shtm`,
`.shtml`, `.acgi`, `.svg` .

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Text description of the Document. Limit: 255 characters.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization. Label is **Document Unique Name** .

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance may slow while
Salesforce generates one for each record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. ID of the Folder that contains the document.


Standard Objects Document

**Field** **Details**

This is a relationship field.

**Relationship Name**
Folder

**Relationship Type**
Lookup

**Refers To**
Folder, User

```
IsBodySearchable

IsDeleted

IsInternalUseOnly

IsPublic

Keywords

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the contents of the object can be searched using a SOSL `FIND` call. The
`ALL FIELDS` search group includes the content as a searchable field.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is **Deleted** .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the object is only available for internal use ( `true` ) or not ( `false` ). Label
is **Internal Use Only** .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the object is available for external use ( `true` ) or not ( `false` ). Label is
**Externally Available** .

**Type**
string


Standard Objects Document

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Keywords. Limit: 255 characters.

```
LastReferencedDate

LastViewedDate

Name

NamespacePrefix

```

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced ( `LastReferencedDate` ) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Name of the document. Label is **Document Name** .

**Type**
string

**Properties**
Filter, Group, Sort, Nillable

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can
refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.


### Standard Objects DocumentAttachmentMap

**Field** **Details**

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

```
 Type

 Url

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
File type of the Document. In general, the values match the file extension for the type of
Document (such as pdf or jpg). Label is **File Extension** .

**Type**
string

**Properties**
Create, Filter, Nillable, Group, Sort, Update

**Description**
URL reference to the file (instead of storing it in the database). If specified, do not specify the
`Body` or `BodyLength` .

When creating or updating a document, you can specify a value in either the `Body` or `Url` fields, but not both.

Encoded Data

The API sends and receives the binary file data encoded as a base64 data type. Prior to creating a record, clients must encode the binary
file data as base64. Upon receiving an API response, clients must decode the base64 data to binary (this conversion is usually handled
for you by the SOAP client).

Maximum Document Size

You can only create or update documents to a maximum size of 5 MB.

SEE ALSO:

Overview of Salesforce Objects and Fields

### DocumentAttachmentMap

Maps the relationship between an EmailTemplate and its attachment, which is stored as a Document.


Standard Objects DocumentAttachmentMap

Supported Calls

`create()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Customer Portal users can’t access this object.

Fields

**Field** **Details**

```
 DocumentId

 DocumentSequence

 ParentId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the document that this object tracks.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Represents the order that the attachments will be included in the email defined by the
EmailTemplate specified by the `DocumentId` . Label is **Attachment Sequence** . The first
attachment is given a value of 0, and each subsequent attachment is given a value
incremented by 1.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the EmailTemplate parent. The attachment identified by `DocumentId` is attached
to the EmailTemplate specified in this field.

Use this object to map the relationship of an EmailTemplate to its attachments, and to specify the order of the attachments.

SEE ALSO:

EmailTemplate


### Standard Objects DocumentRecipient DocumentRecipient

Connects a Service Report to a Digital Signature. This object is available in API version 55.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
DigitalSignatureId

DigitalSignatureUrl

DocumentId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Digital Signature to be used on the Service Report.

This field is a relationship field.

**Relationship Name**
DigitalSignature

**Relationship Type**
Lookup

**Refers To**
DigitalSignature

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Link to request signature from Experience Cloud site.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The document sent to the recipient.

This field is a polymorphic relationship field.

**Relationship Name**
### Document


Standard Objects DocumentRecipient

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
ServiceReport

```
DocumentRecipient

LastReferencedDate

LastViewedDate

OwnerId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Number automatically assigned to a new record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view ( `LastReferencedDate` ) but
not viewed it.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of this object. ID of the creator of this object.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup


Standard Objects DocumentRecipient

**Field** **Details**

**Refers To**
Group, User

QuoteDocumentId

```
RecipientId

SignatureIdentifier

SignatureStatus

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The quote document sent to the recipient.

This field is a relationship field.

**Relationship Name**
QuoteDocument

**Refers To**
QuoteDocument

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The recipient to sign the document.

This field is a polymorphic relationship field.

**Relationship Name**
Recipient

**Relationship Type**
Lookup

**Refers To**
Contact, User

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A unique identifier that associates `DocumentRecipient` with a signature Lightning
web component (LWC) on the report page layout, telling you where on the report the
signature goes.

**Type**
picklist


Standard Objects DocumentRecipient

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the signature. The default value is `Completed` . Possible values are:

**•** `Completed`

**•** `Skipped`

```
SignatureStatusReason

Status

StatusReason

```

Associated Objects

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
An explanation for the signature status. For example, a reason why the signature was skipped.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the document recipient record.

Possible values are:

**•** `Completed`

**•** `Declined`

**•** `Delivered`

**•** `None`

**•** `Sent`

The default value is `None` .

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The final status reason.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


### Standard Objects DocumentTag

**DocumentRecipientFeed on page 55**
Feed tracking is available for the object.

**DocumentRecipientOwnerSharingRule on page 65**
Sharing rules are available for the object.

**DocumentRecipientShare on page 67**
Sharing is available for the object.

### DocumentTag

Associates a word or short phrase with a Document.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
ItemId

Name

TagDefinitionId

```

**Type**
reference

**Properties**
Create, Filter

**Description**
ID of the tagged item.

**Type**
string

**Properties**
Create, Filter

**Description**
Name of the tag. If this value does not already exist, a new TagDefinition is created and
becomes the parent of this Tag object. Otherwise, a TagDefinition with the same name
becomes the parent of this Tag object. Parent relationships are created automatically.

**Type**
reference

**Properties**
Filter

**Description**
ID of the parent TagDefinition object that owns the tag.


### Standard Objects Domain

**Field Name** **Details**

```
Type

```

Usage

**Type**
picklist

**Properties**
Create, Filter, Restricted picklist

**Description**
Defines the visibility of a tag.

Valid values:

**•** `Public` —The tag can be viewed and manipulated by all users in an organization.

**•** `Personal` —The tag can be viewed or manipulated only by a user with a matching
`OwnerId` .

DocumentTag stores the relationship between its parent TagDefinition and the Document being tagged. Tag objects act as metadata,
allowing users to describe and organize their data.

When a tag is deleted, its parent TagDefinition will also be deleted if the name is not being used; otherwise, the parent remains. Deleting
a TagDefinition sends it to the Recycle Bin, along with any associated tag entries.

### Domain

Read-only object that represents a custom Web address assigned to a site in your organization. This object is available in API version
26.0 and later.

### To access this object, Salesforce Sites, Digital Experiences, or Site.com must be enabled for your organization. DomainSite contains

records for domains that serve your Experience Cloud sites only when enhanced domains are deployed. The system-managed site
hostnames for those Experience Cloud sites end in `.my.site.com` . This object doesn’t contain records for legacy domains that serve
Experience Cloud sites with hostnames that end in `.force.com` .

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

**•** Customer Portal users can’t access this object.

**•** To view this object, you must have either the View Setup and Configuration or Manage Custom Domains permission.

**•** Site.com Publisher users have read-only API access to the Domain and DomainSite objects.


Standard Objects Domain

Fields

**Field** **Description**

```
CnameTarget

Domain

DomainType

HttpsOption

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The canonical name (CNAME) of the external host or server. If you use a custom
domain with a non-Salesforce provider, such as your own external server or CDN
provider, to serve your domain, this field points to the CNAME of the external
provider. This field is available in API version 43.0 and later.

**Type**
string

**Properties**
Filter, idLookup, Sort

**Description**
The branded custom Web address within the global namespace identified by
this domain's type. In the Domain Name System (DNS) global namespace, this
field is the custom Web address that you registered with a third-party domain
name registrar. The custom Web address can be used to access the site of this
domain.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The global namespace that this custom Web address belongs to. This value is
set to DNS for custom Web addresses in the global DNS.

DomainType can have the following value:

**•** `DNS` —Domain Name System (DNS)

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Current HTTPS option. Values include:

**•** `CdnPartner` —Salesforce serves the custom domain, such as
`https://www.example.com`, with the Salesforce Content Delivery
Network (CDN) partner.


Standard Objects Domain

**Field** **Description**

**•** `Community` —The system-managed Experience Cloud sites domain that
ends in `.force.com` . This option applies only to orgs without enhanced
domains.

**•** `CommunityAlt` —The system-managed Experience Cloud sites domain
that ends in `.my.site.com` . This option applies only to orgs with
enhanced domains.

**•** `ExternalHttps` —An external service or CDN serves the custom domain,
such as `https://www.example.com` .

**•** `LegacyDomain` —A previous system-managed domain for this org. This
option is rarely used.

**•** `NoHttps` —Salesforce serves the custom domain, such as
`http://www.example.com`, via HTTP. Used to configure your custom
domain before selecting a permanent HTTPS option.

**•** `OrgDomain` —The system-managed My Domain login URL for this org.

**•** `Sites` —The system-managed Salesforce Sites domain that ends in
`.force.com` . This option applies only to orgs without enhanced domains.

**•** `SitesAlt` —The system-managed Salesforce Sites domain that ends in
`.my.salesforce-sites.com` . This option applies only to orgs with
enhanced domains.

**•** `SitesRuntime` —Salesforce serves the custom domain, such as
`https://www.example.com`, using your HTTPS certificate on Salesforce
servers.

This field is available in API version 47.0 and higher.

[To get the current system-managed domains for your org, use the Domain Apex](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_class_System_Domain.htm)
class.

```
OptionsHstsPreload

```

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the `preload` directive is added to the HSTS header so that
the domain is eligible for HSTS preloading registration ( `true` ) or not ( `false` ).
This field is available in API version 52.0 and later.

After this field is set to `true`, to ensure that HTTPS connections are always used
in browsers that support HSTS, you must also register the domain at
[https://hstspreload.org.](https://hstspreload.org)

We only modify the HSTS headers of domains that are eligible for registration.
Domain names can consist of a public suffix plus one additional label. For more
[information, see Add a Domain in Salesforce Help.](https://help.salesforce.com/articleView?id=platform.domain_mgmt.htm&type=5&language=en_US)


### Standard Objects DomainSite

Usage

Use this read-only object to query the domains that are associated with each site in your organization.

### DomainSite

Read-only junction object that joins the Site and Domain objects. This object is available in API version 26.0 and later.

### To access this object, Salesforce Sites, Digital Experiences, or Site.com must be enabled. DomainSite contains records for domains

that serve your Experience Cloud sites only when enhanced domains are deployed. The system-managed site hostnames for those
Experience Cloud sites end in `.my.site.com` . This object doesn’t contain records for legacy domains that serve Experience Cloud
sites with hostnames that end in `.force.com` .

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

**•** Customer Portal users can’t access this object.

**•** To view this object, you must have either the View Setup and Configuration or Manage Custom Domains permission.

**•** Site.com Publisher users have read-only API access to the Domain and DomainSite objects.

Fields

**Field** **Description**

```
DomainId

PathPrefix

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

The ID of the associated Domain.

This is a relationship field.

**Relationship Name**
### Domain

**Relationship Type**
Lookup

**Refers To**
### Domain

**Type**
string


### Standard Objects DsarPolicy

**Field** **Description**

**Properties**
Filter, Group, Sort

**Description**
Shows where a site’s root exists on a domain. Can only be set for custom Web
addresses. Always begins with a `/` .

```
SiteId

```

Usage

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

The ID of the associated Site.

This is a relationship field.

**Relationship Name**
Site

**Relationship Type**
Lookup

**Refers To**
Site

Use this read-only object to query or retrieve information about your sites.

### DsarPolicy

Represents a Data Subject Access Request (DSAR) policy created in the Privacy Center managed package. DSAR policies anonymize or
transfer personal data from your org at your customer’s request. This object is available in API version 50.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

This object is for Privacy Center customers with the ReadAllData or PrivacyDataAccess permissions.


Standard Objects DsarPolicy

Fields

**Field** **Details**

```
Description

DeveloperName

IsActive

Language

```

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
Description of the policy. The description is limited to 255 characters.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Developer name of the policy.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this policy can be used ( `true` ) or not ( `false` ) for data subject (customer)
requests. The default value is `false` .

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language of the MasterLabel.

Possible values are:

**•** `da` —Danish

**•** `de` —German

**•** `en_US` —English

**•** `es` —Spanish

**•** `es_MX` —Spanish (Mexico)

**•** `fi` —Finnish

**•** `fr` —French


### Standard Objects DsarPolicyLog

**Field** **Details**

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

```
MasterLabel

```

Associated Objects

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Label of the policy.

This object has the following associated objects. Unless noted, they are available in the same API version as the object.

### **DsarPolicyLog**

Sharing is available for the object.

### DsarPolicyLog

Represents the history of Data Subject Access Request (DSAR) policy execution requests. This log records the status and results of executed
DSAR policies for a customer. This object is available in API version 50.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

This object is for Privacy Center customers with the ReadAllData or PrivacyDataAccess permissions.


Standard Objects DsarPolicyLog

Fields

**Field** **Details**

```
CompletionDateTime

DataSubjectId

DeletedDateTime

DeveloperName

DownloadedDateTime

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the data subject access request was completed. Available in API
version 51.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15–18 character ID of the data subject making the request. Available in API version 51.0
and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the file generated for the data subject’s request is deleted. Available
in API version 51.0 and later.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Developer name of the policy.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The most recent date and time when the data subject downloaded the file generated at
their request. Available in API version 51.0 and later.


Standard Objects DsarPolicyLog

**Field** **Details**

```
DsarError

DsarPolicyId

FileURL

Language

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Represents an error in generating the file for the data subject access request. Available in
API version 51.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the DSAR policy.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The result of the DSAR policy execution. The URL links to a downloadable file that contains
the customer data.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language of the MasterLabel.

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


Standard Objects DsarPolicyLog

**Field** **Details**

**•** `nl_NL` —Dutch

**•** `no` —Norwegian

**•** `pt_BR` —Portuguese (Brazil)

**•** `ru` —Russian

**•** `sv` —Swedish

**•** `th` —Thai

**•** `zh_CN` —Chinese (Simplified)

**•** `zh_TW` —Chinese (Traditional)

```
MasterLabel

RequestDateTime

RequestStatus

RequestUserId

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Label of the policy.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when a data subject requested access to their data in the org. Available
in API version 51.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of the policy execution.

Possible values are:

**•** `Complete`

**•** `Deleted`

**•** `Downloaded`

**•** `Expired`

**•** `Failed`

**•** `In Progress`

**Type**
reference


### Standard Objects DuplicateJob

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the org employee or admin making the request on behalf of the data subject.
Available in API version 51.0 and later.

Associated Objects

This object has the following associated objects. Unless noted, they’re available in the same API version as the object.

**DsarPolicy**

Sharing is available for the object.

### DuplicateJob

Represents an instance of a job that identifies duplicates among existing records in the system.

This object is available in API versions 42.0 and later.

A duplicate job is the parent of the DuplicateRecordSet instances that it generates. The duplicate record items in a set generated by a
duplicate job are of one object type.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`

Special Access Rules

As of Summer ’20 and later, only users with the View Setup and Configuration permission can access this object.

Fields

**Field Name** **Details**

### `DuplicateJobDefinitionId` `DuplicateJobStatus`

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
The ID of the corresponding duplicate job definition.

**Type**
picklist


Standard Objects DuplicateJob

**Field Name** **Details**

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The current status of a duplicate job. Valid values are `Not Started`, `In`
`Progress`, `Completed`, `Canceled`, `Failed`, `Results Deleted` .

```
EndDateTime

LastReferencedDate

LastViewedDate

Name

NumDuplicateRecordItems

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when a duplicate job was completed.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when a duplicate job was last referenced.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when a duplicate job was last viewed.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort, Update

**Description**
The name of a duplicate job.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The total number of duplicate records identified as a result of invoking a duplicate
job.


### Standard Objects DuplicateJobDefinition

**Field Name** **Details**

```
NumDuplicateRecordSets

NumRecordsScanned

ResultListViewId

StartDateTime

### DuplicateJobDefinition

```

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of duplicate record sets identified as a result of invoking a duplicate
job.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of records scanned as a result of invoking a duplicate job.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
List view metadata for displaying the duplicate record sets identified as result of
invoking a duplicate job.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date and time when a duplicate job was invoked.

Setup object defining a job that identifies duplicate record items globally.

This object is available in API versions 42.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects DuplicateJobDefinition

Special Access Rules

As of Summer ’20 and later, only users with the View Setup and Configuration permission can access this object.

Fields

**Field Name** **Details**

```
DeveloperName

Language

MasterLabel

SobjectSubtype

SobjectType

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The name of the user who created a duplicate job.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language in the user’s personal settings.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The label of the duplicate job.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The object subtype. Valid values are `Person Account` or `None` .

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort


### Standard Objects DuplicateJobMatchingRule

**Field Name** **Details**

**Description**
The object type: account, contact, or lead.

### DuplicateJobMatchingRule

Represents a MatchingRule to be used with a DuplicateJob sharing the corresponding DuplicateJobMatchingRuleDefinition.

This object is available in API versions 42.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

As of Summer ’20 and later, only users with the View Setup and Configuration permission can access this object.

Fields

**Field Name** **Details**

```
DuplicateJobId

DuplicateJobMatchRuleDefId

MatchingRuleBooleanFilter

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the corresponding DuplicateJob.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the matching rule defined for the corresponding
### DuplicateJobMatchingRuleDefinition.

**Type**
textarea

**Properties**
Filter, Sort


### Standard Objects DuplicateJobMatchingRuleDefinition

**Field Name** **Details**

**Description**
Boolean logic of the MatchingRule for this DuplicateJobMatchingRule.

```
MatchingRuleDescription

MatchingRuleName

```

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
Description of the matching rule for this DuplicateJobMatchingRule.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The name of the matching rule defined for this particular DuplicateJob invocation.

### DuplicateJobMatchingRuleDefinition

Setup object specifying a MatchingRule to use with DuplicateJob instances that share a DuplicateJobDefinition.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

This object is available in API versions 42.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `search()`

Special Access Rules

As of Summer ’20 and later, only users with the View Setup and Configuration permission can access this object.

Fields

**Field Name** **Details**

```
DuplicateJobDefinitionId

```

**Type**
reference

**Properties**
Filter, Group, Sort


### Standard Objects DuplicateRecordItem

**Field Name** **Details**

**Description**
ID of DuplicateJobDefinition (master) for this DuplicateJobMatchingRuleDefinition
(detail).

```
MatchingRuleId

### DuplicateRecordItem

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the MatchingRule to be used with this DuplicateJobMatchingRuleDefinition.

Represents a record that’s been identified as a duplicate. DuplicateRecordItems are included in a DuplicateRecordSet, which are processed
in duplicate jobs. Use this object to create custom report types for duplicates.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

To access this object, enable Duplicate Management. A Salesforce admin can grant access to any user with a Sales Cloud or CRM user
license.

Fields

**Field Name** **Details**

```
DuplicateRecordSetId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The duplicate record set that the duplicate record item is assigned to.

This is a relationship field.

**Relationship Name**
DuplicateRecordSet


### Standard Objects DuplicateRecordSet

**Field Name** **Details**

**Relationship Type**
Lookup

**Refers To**
### DuplicateRecordSet

```
Name

RecordId

### DuplicateRecordSet

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**

### The autogenerated name that’s given to the Duplicate Record Item. Label is Duplicate

`Record Item Name` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The name of the record as it appears on the record’s detail page.

This is a polymorphic relationship field.

**Relationship Name**
Record

**Relationship Type**
Lookup

**Refers To**
Account, Contact, Individual, Lead

Represents a group of records that have been identified as duplicates. Each duplicate record set contains one or more duplicate record
items. Use this object to create custom report types and view the results of duplicate jobs.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

To access this object, activate duplicate rules. A Salesforce admin must give users read and write access.


Standard Objects DuplicateRecordSet

Fields

**Field Name** **Details**

```
DuplicateRuleId

LastReferencedDate

LastViewedDate

Name

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The duplicate rule used to identify this list of duplicate records.

**Label**

Duplicate Rule ID

This is a relationship field.

**Relationship Name**
DuplicateRule

**Relationship Type**
Lookup

**Refers To**
DuplicateRule

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The timestamp when the current user last accessed this record, a record related to this record, or a list
view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The timestamp when the current user last viewed this record or list view. If this value is null, the user
might have only accessed this record or list view ( `LastReferencedDate` ) but not viewed it.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort


### Standard Objects DuplicateRule

**Field Name** **Details**

**Description**

The autogenerated name that’s given to the duplicate record set. Label is `Duplicate Record`
`Set Name` .

```
RecordCount

ParentId

### DuplicateRule

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of record items in the set.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The `ParentId` represents the parent of a duplicate rule or duplicate job. A `ParentId` is polymorphic.
The label is Parent. This field is available in API versions 42.0 and later.

Represents a duplicate rule for detecting duplicate records.

Supported Calls

`describeSObjects()`, `describeLayout()`, `query()`, `retrieve()`, `search()`

Special Access Rules

As of Summer ’20 and later, only users with the View Setup and Configuration permission can access this object.

Fields

**Field Name** **Details**

```
DeveloperName

```

**Type**
string

**Properties**
Filter, Group, Sort


Standard Objects DuplicateRule

**Field Name** **Details**

**Description**
The developer name for the duplicate rule.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

```
IsActive

Language

LastViewedDate

MasterLabel

NamespacePrefix

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a duplicate rule is active ( `true` ) or not ( `false` ). This field is
read only.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language for the duplicate rule.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. This
field is available in API version 41.0 or later.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The label for the duplicate rule.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition
org that creates a managed package has a unique namespace prefix. Limit: 15


Standard Objects DuplicateRule

**Field Name** **Details**

characters. You can refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace
prefix of the org for all objects that support it, unless an object is in an installed
managed package. In that case, the object has the namespace prefix of the
installed managed package. This field’s value is the namespace prefix of the
Developer Edition org of the package developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set
only for objects that are part of an installed managed package. All other
objects have no namespace prefix.

```
SobjectSubtype

sObjectType

```

Usage

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The subtype of object the duplicate rule is defined for. This field is available in
API version 39.0 or later.

Possible values are:

**•** `None`

**•** `PersonAccount`

The default value is `None` .

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of object the duplicate rule is defined for.

Possible values are:

**•** `Account`

**•** `Contact`

**•** `Individual`

**•** `Lead`

You can use the API to view a duplicate rule’s details. To create, edit, or delete duplicate rules, use the UI.

Use DuplicateRule to get the sObject type.


### Standard Objects DynamicDataCapture

DuplicateRule is unavailable in some orgs.

### DynamicDataCapture DynamicDataCapture is a junction object that adds a Form tab to Work Order Overview, and to the related list of a work order, work

order line item, or service appointment in the Field Service mobile app. This object is available in API version 62.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ActionDefinition

ActionType

Description

ExecutionOrder

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The associated Data Capture Flow to execute.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of platform action that the form is associated with. Possible values are:

Possible values are:

**•** `Flow`

The default value is `Flow` .

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the form.

**Type**
int


Standard Objects DynamicDataCapture

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The order in which the Data Capture flow is executed. Positive integer values or null are
supported.

```
IsRequired

LastReferencedDate

Name

OwnerId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Boolean value that specifies if this form needs to be completed before moving on to the
next form.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The order in which the Data Capture flow is executed. Positive integer values or null are
supported.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the form.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID that refers to user who owns the Dynamic Data Capture object.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
ServiceAppointment, WorkOrder, WorkOrderLineItem (the parent object), Timesheet


Standard Objects DynamicDataCapture

**Field** **Details**

```
ParentRecordId

ParentRecordType

PausedFlowInterviewId

ProcessType

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID that refers to a work order, work order line item, or service appointment that serves
as the parent record for junction object.

This field is a polymorphic relationship field.

**Relationship Name**
ParentRecord

**Relationship Type**
Parent-child

**Refers To**
ServiceAppointment, WorkOrder, WorkOrderLineItem (the parent object)

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of parent object associated with the junction object.

Possible values are:

**•** `Work Order`

**•** `Work Order Line Item`

**•** `Service Appointment`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the flow interview that has been paused by a user.

This field is a relationship field.

**Relationship Name**
PausedFlowInterview

**Refers To**
FlowInterview

**Type**
picklist


Standard Objects DynamicDataCapture

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The flow process type for the form.

Possible values are:

**•** `DataCaptureFlow` —Data Capture Flow

The default value is `DataCaptureFlow` .

```
ServiceDocumentTemplate

ServiceReportLanguage

StatusCategory

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The category that each status value belongs to.

Possible values are:

**•** `Completed`

**•** `InProgress` —In Progress

**•** `New`

**•** `NotApplicable` —Not Applicable

**•** `Paused`

The default value is `New` .

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


### Standard Objects ElectronicMediaGroup

**DynamicDataCaptureChangeEvent on page 68(API Version 64.0)**
Change events are available for the object.

**DynamicDataCaptureOwnerSharingRule on page 65(API Version 64.0)**
Sharing rules are available for the object.

**DynamicDataCaptureShare on page 67(API Version 64.0)**
Sharing is available for the object.

### ElectronicMediaGroup

Represents the type of media that you can associate with a product or category.This object is available in API version 49.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

You must have the B2B Commerce license and a CMS workspace to access a web store.

Fields

**Field** **Details**

```
CurrencyIsoCode

Description

DeveloperName

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**

The default value is `USD` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Description of the store.

**Type**
string

**Properties**
Filter, Group, Sort


Standard Objects ElectronicMediaGroup

**Field** **Details**

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

```
LastReferencedDate

LastViewedDate

Name

OwnerId

UsageType

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced ( `LastReferencedDate` ) and not viewed.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Name of the media group.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the owner of the ElectronicMediaGroup object. For external routing, allows the
object to be used in the Streaming API to listen to events whenever a ElectronicMediaGroup
record is created, modified, or deleted.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort


### Standard Objects ElectronicMediaUse

**Field** **Details**

**Description**
Possible values are:

**•** `Attachment`

**•** `Banner`

**•** `Listing`

**•** `Standard`

**•** `Tile`

### ElectronicMediaUse

Represents the usage of media. This object is available in API version 49.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

You must have the B2B Commerce license and a CMS workspace to access a web store.

Fields

**Field** **Details**

```
CurrencyIsoCode

ElectronicMediaGroupId

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**

The default value is `USD` . Possible values are:

**•** `USD` —U.S. Dollar

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the electronic media group.


### Standard Objects EmailContent

**Field** **Details**

```
ElectronicMediaId

ImplementorType

SortOrder

### EmailContent

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the electronic media.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of implementor. Available implementors of ElectronicMediaUse include:

**•** ProductMedia

**•** ProductCategoryMedia

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The order that electronic media is displayed in.

Represents a marketing email asset for use with Account Engagement. This object is available in API version 50.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `update()`, `upsert()`

Special Access Rules

### EmailContent is only available for orgs that use Account Engagement. The Manage Email Content user permission is required. Users also

need the CRM User, Sales, or Service User permission set. EmailContent isn’t available for custom portal or guest users.


Standard Objects EmailContent

Fields

**Field** **Details**

```
ClickThroughRate

ClickToOpenRatio

DeliveryRate

Description

HtmlBody

LastReferencedDate

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of visitors who click links contained in emails delivered (sent minus bounces)
to them. Multiple clicks for a same link are counted.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The number of unique clicks divided by unique HTML opens.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of the emails that were delivered compared to the number that bounced
(soft and hard). Note: this data includes emails that were delivered to the recipient's spam
folder.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the email content, for example, Promotion Mass Mailing.

**Type**
textarea

**Properties**
Nillable

**Description**
The body of the email in HTML format. The field is read-only.

**Type**
dateTime


Standard Objects EmailContent

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp that indicates when the current user last viewed the record.

```
LastViewedDate

Name

OpenRate

OptOutRate

SpamComplaintRate

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, the
record could have been referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the email asset.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of unique HTML opens compared to the total number of emails delivered
(sent minus bounces).

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of users that have opted out compared to the total number of emails sent.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of spam complaints compared to the total number emails sent.


Standard Objects EmailContent

**Field** **Details**

```
Subject

TemplateId

TextBody

TotalDelivered

TotalHardBounced

TotalOpens

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Update

**Description**
Content of the subject line.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The Email Template field is mostly read-only. You can populate the Email Template field only
during record create to prevent overwriting data on the email content record.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The body of the email in plain text format. The character limit is 384, 000.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of emails minus hard and soft bounces. Note: this data includes emails
that were delivered to the recipient's spam folder.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
The total number of emails that permanently returned to the sender because the address is
invalid. A hard bounce can occur because the domain name doesn't exist or because the
recipient is unknown.

**Type**
int


Standard Objects EmailContent

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
The total number of times a prospect’s email client loaded the images in the HTML version
of the email. We also record an open if the prospect clicks a link within the HTML or text
email without downloading images. A click indicates that they viewed the message. Some
email clients (Outlook, Apple Mail, Thunderbird) do not display images by default. Account
Engagement counts an open each time the images load.

```
TotalSent

TotalSoftBounced

TotalSpamComplaints

TotalTrackedLinkClicks

UniqueClickThroughRate

```

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Read-only field. The total number of list emails sent, including bounced, opted-out, and
invalid To: addresses.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Read-only field. The total number of times a recipient’s mail server acknowledged the email,
but returned it to the sender. Sometimes it is because the recipient's mailbox is full or the
mail server is temporarily unavailable. After 5 soft bounces, Account Engagement opts the
prospect out of emails.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Read-only field. The total number of prospects that reported the email as spam.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Read-only field. The number of times prospects clicked a link in the email.

**Type**
percent


### Standard Objects EmailDomainFilter

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
Read-only field. The percentage of visitors who clicked a link contained in an email

```
UniqueOpens

UniqueOptOuts

UniqueTrackedLinkClicks

### EmailDomainFilter

```

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Read-only field. The number of prospects who loaded the images in the HTML version of
the email. The Unique Opens category counts each recipient only one time, even if the
prospect loaded images more than once.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Read-only field. The total number of prospects that have clicked the link to unsubscribe or
opted out of all emails in the Email Preference Center. They are removed from future email
sends.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Read-only field. The number of times a prospect clicked a link in the email. This metric doesn’t
include multiple clicks of the same link.

Represents a filter that determines whether an email relay is restricted to a specific list of domains. This object is available in API version
43.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects EmailDomainFilter

Special Access Rules

You must have the “Email Administration,” “Customize Application,” and “View Setup” user permissions to use this object.

You must create an email relay in Setup or through the EmailRelay object before you can use the `EmailDomainFilter` object.

Fields

**Field Name** **Details**

```
EmailRelayId

FromDomain

IsActive

PriorityNumber

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The ID of the EmailRelay record.

This is a relationship field.

**Relationship Name**
EmailRelay

**Relationship Type**
Lookup

**Refers To**
EmailRelay

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**

Restricts the email relay to send emails based on the sender domains
( `FromDomain` ) listed in this field. This field is optional, accepts a list of
comma-separated values, and supports the wildcard character.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether the email domain filter is active ( `true` ) or not ( `false` ). Use
this field to enable or disable the email domain filter.

**Type**
int


### Standard Objects EmailDomainKey

**Field Name** **Details**

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**

Indicates the order in which the email domain filter is processed. Filters are
evaluated in ascending order. The priority number must be unique. If this field
is left blank, it is assigned the next available number and is processed last.
Processing stops after the first matching filter is applied.

```
ToDomain

```

Usage

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**

Restricts the email relay to send emails based on the recipient domains
( `ToDomain` ) listed in this field. This field is optional, accepts a list of
comma-separated values, and supports the wildcard character.

Tip: If you also plan to activate Bounce Management and Email Compliance Management, confirm with your email admin that
[your company allows relaying email sent from Salesforce. For more information on bounce management, see Configure Deliverability](https://help.salesforce.com/articleView?id=emailadmin_send_through_salesforce_configure_deliverability.htm&language=en_US)
[Settings for Emails Sent from Salesforce.](https://help.salesforce.com/articleView?id=emailadmin_send_through_salesforce_configure_deliverability.htm&language=en_US)

### EmailDomainKey

Represents a domain key for an organization’s domain, used to authenticate outbound email that Salesforce sends on the organization’s
behalf. This object is available in API version 28.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

As of Summer ’20 and later, only authenticated internal and external users can access this object.

We’ve upgraded and replaced the original DKIM (DomainKeys Identified Mail) key feature, so that you can create a DKIM key with
[increased email security. For more information, see Setting Up More Secure DKIM Keys.](https://help.salesforce.com/articleView?id=emailadmin_setup_dkim_key.htm&type=0&language=en_US)


Standard Objects EmailDomainKey

Fields

**Field Name** **Details**

```
AlternatePublicKey

AlternateSelector

AlternateTxtRecordName

Domain

DomainMatch

```

**Type**
textarea

**Properties**
Nillable

**Description**

Read-only. Alternate public keys are used by Salesforce to auto-rotate domain
keys. This field is available in API version 44.0 and later after activating the Critical
Update.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The text used to distinguish the DKIM key from any other DKIM keys your
organization uses for the specified domain. This field is available in API version
44.0 and later after activating the Critical Update.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The alternate TXT record name is used to create the CNAME record. Refer to the
Usage section for more information. This field is available in API version 44.0 and
later after activating the Critical Update.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The organization’s domain name that the DKIM key is generated for.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


Standard Objects EmailDomainKey

**Field Name** **Details**

**Description**

The specificity of match required on the sending domain name before signing
with this DKIM key. Valid values are:

**•** `DomainOnly` —Sign if sending domain matches at the domain level only
(example.com but not mail.example.com)

**•** `SubdomainsOnly` —Sign if sending domain matches at the subdomain
level only (mail.example.com but not example.com)

**•** `DomainAndSubdomains` —Sign if sending domain matches at the
domain and subdomain levels (example.com and mail.example.com)

```
IsActive

KeySize

PrivateKey

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether this DKIM key is active ( `true` ) or not ( `false` ).

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort

**Description**

Indicates the RSA key size, in bits. The possible values are:

**•** 1024

**•** 2048

This field is available in API version 45.0 and later.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**

Once you activate the Critical Update, this field is no longer visible.

The private portion of the DKIM key pair used to encrypt mail headers from your
domain. Salesforce generates an encrypted `PrivateKey` if you don’t specify
a value when creating the DKIM key. If you do specify a value, it must be an
existing valid `PrivateKey` from another EmailDomainKey object.

This field doesn’t contain the actual private key, but a value that represents the
key in our system. Therefore:

**•** The actual private key can’t be leaked.


Standard Objects EmailDomainKey

**Field Name** **Details**

**•** You can’t use the value to do your own email signing.

```
PublicKey

Selector

TxtRecordName

TxtRecordsPublishState

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**

Part of the domain key pair that mail recipients retrieve to decrypt the DKIM
header and verify your domain. Add the `PublicKey` value to your domain’s
DNS records before you start signing with this domain key.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**

Text used to distinguish the DKIM key from any other DKIM keys your organization
uses for the specified domain.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Read-only. The TXT record name is used to create the CNAME record. Refer to
the Usage section for more information. This field is available in API version 44.0
and later after activating the Critical Update.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

The possible values are:

**•** Published

**•** Publishing in progress

**•** Publishing failed

This field is available in API version 44.0 and later after activating the Critical
Update.


### Standard Objects EmailInsight

Usage

**Create DKIM Keys with Increased Security**

**1.** If your Salesforce org was created before Winter ’19, enable the Critical Update. From Setup, enter _`Critical Updates`_ in the
Quick Find box, and then select **Critical Updates** . For Enable Redesigned DomainKeys Identified Mail (DKIM) Key Feature with
Increased Email Security, click **Activate** .

**2.** Insert `Domain`, `DomainMatch`, `Selector`, and `AlternateSelector` . Salesforce publishes your TXT record to DNS.

**3.** Retrieve the `TxtRecordName` and `AlternateTxtRecordName` and use them to create and publish the CNAME and
Alternate CNAME record to your domain’s DNS.

**a.** Create CNAME record using: _**`<selector>`**_ `._domainkey.` _**`<domain>`**_ `IN CNAME` _**`txtRecordName`**_ .

**b.** Create Alternate CNAME record using: _**`<alternateSelector>`**_ `._domainkey.` _**`<domain>`**_ `IN CNAME`
_**`alternateTxtRecordName`**_ .

**4.** Set the `IsActive` field to true.

**Create DKIM Keys (pre-Winter ‘19 Version)**

Note: The critical update activates for everyone on October 15, 2019. After that date, this approach to creating DKIM keys will no
longer be available.

When you create a DKIM key, Salesforce generates a public and private key pair. Publish the public key in the DNS.

For each domain key you create, we recommend this sequence:

**1.** Insert the `Domain`, `DomainMatch`, and `Selector` .

**2.** Update your domain’s DNS records.

**a.** Locate the DNS record at _**`selector`**_ `._domainkey.` _**`domain`**_ . For example, `mail._domainkey.mail.example.com` .

**b.** Add the `PublicKey` value, like this: `V=DKIM1; p=` _**`public_key`**_ .

DKIM Signing Outbound Email

**a.** In addition, you can optionally put the record in testing mode, which instructs recipients to not make decisions based on the
email signature. Add parameter `t=y` to the DNS entry: `V=DKIM1; t=y; p=` _**`public_key`**_ .

**3.** Update the key via the API or UI to be active.

SEE ALSO:

_Salesforce Help_ [: Considerations for Creating DKIM Keys](https://help.salesforce.com/articleView?id=emailadmin_considerations_dkim.htm&type=0&language=en_US)

_Salesforce Help_ [: Setting Up More Secure DKIM Keys](https://help.salesforce.com/articleView?id=emailadmin_setup_dkim_key.htm&type=0&language=en_US)

### EmailInsight

Represents an insight generated from an email interaction. EmailInsights acts as a central place to store various types of insights related
to email messages. The insights stored include status, type, and time of generation. Only certain types of insights can be created based
on a pre-configured list of insight types. This object is available in API version 63.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects EmailInsight

Special Access Rules

EmailStream permission must be enabled.

EmailStreamPref and SyncEmailToCoreActivity Org prefs must be enabled.

To be able to see SyncEmailToCoreActivity preference, EACLegacyEmailSyncAWS Org permission, AnalyticsActivity, UnifiedActivities,
and ActivityMetrics must be disabled. In addition, license to Standard Einstein Activity Capture and turning on Einstein Activity Capture
and EmailInsights provisions the required permissions and preferences.

Fields

**Field** **Details**

```
EmailMessageId

GeneratedDate

InsightTypeDescription

InsightTypeIdentifier

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Required. The ID of the email message the insight is generated for.

This field is a relationship field.

**Relationship Name**
EmailMessage

**Refers To**
EmailMessage

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
Required. The date and time when the insight was generated in the legacy system.

**Type**
textarea

**Properties**
None

**Description**
Required. Description of the insight type.

**Type**
string

**Properties**
Filter, Group, Sort


Standard Objects EmailInsight

**Field** **Details**

**Description**
Required. The ID of the insight type based on which the insight is generated.

```
InsightTypeLabel

IsLocked

LegacyInsightIdentifier

MayEdit

RowVersion

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Required. The display name of the insight type.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the email insight record is locked or not.

The default value is false.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Required. The unique ID of the insight that was generated and stored in the legacy system.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the email insight record can be edited or not.

The default value is false.

**Type**
string

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
A system-generated, read-only field that tracks the version of a record. Each time a record
is created or updated, the RowVersion value increments, providing a mechanism to detect
changes and manage concurrency.


### Standard Objects EmailInsightAction

**Field** **Details**

```
Status

### EmailInsightAction

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Required. The status of the insight record.

Possible values are:

**•** `Active`

**•** `Completed`

**•** `Deprecated`

**•** `Dismissed`

The default value is `Active` .

Represents the actions that have been taken, or could be taken, in relation to email insights. It logs different types of actions and associated
metadata, helping to track and manage the activities and decisions made based on email insights. This object is available in API version
63.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

EmailStream permission must be enabled.

EmailStreamPref and SyncEmailToCoreActivity Org prefs must be enabled.

To be able to see SyncEmailToCoreActivity preference, EACLegacyEmailSyncAWS Org permission, AnalyticsActivity, UnifiedActivities,
and ActivityMetrics must be disabled. In addition, license to Standard Einstein Activity Capture and turning on Einstein Activity Capture
and EmailInsights provisions the required permissions and preferences.

Fields

**Field** **Details**

```
ActionMetadata

```

**Type**
textarea

**Properties**
Nillable


Standard Objects EmailInsightAction

**Field** **Details**

**Description**
The metadata for the action.

```
EmailInsightId

InsightAction

IsLocked

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Required. The ID of the email insight where the action is applied.

This field is a relationship field.

**Relationship Name**
EmailInsight

**Refers To**
EmailInsight

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Required. The action that's taken on the email insight.

Possible values are:

**•** `CreateCalendarEvent`

**•** `CreateTaskWithDate`

**•** `EciCreateEmail`

**•** `EciScheduleMeetings`

**•** `EciSendEmail`

**•** `EmailReply`

**•** `EmailReplyLater`

**•** `EmailReplyWithTemplate`

**•** `InsertFreeTime`

**•** `PostOnChatter`

**•** `ViewCalendar`

**•** `ViewContactProfile`

The default value is `EmailReply` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


### Standard Objects EmailMessage

**Field** **Details**

**Description**
Indicates whether the email insight action record is locked or not.

The default value is false.

```
MayEdit

RowVersion

### EmailMessage

```

Represents an email in Salesforce.

Supported Calls

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the email insight action record can be edited or not.

The default value is false.

**Type**
string

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
A system-generated, read-only field that tracks the version of a record. Each time a record
is created or updated, the RowVersion value increments, providing a mechanism to detect
changes and manage concurrency.

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

### EmailMessage is only available for orgs that use Email-to-Case or Enhanced Email, which is automatically enabled for most customers.

To use reply and forward functionality, `FromAddress` must specify an email address that exists in EmailMessageRelation, with a
`RelationType` of `FromAddress` .

The `Status` field is mostly read-only. You can change the status only from _`New`_ to _`Read`_ .

The `HtmlBody` and `RelatedToId` fields are supported in Classic list views but not in Lightning list views. In related lists and search
results in Lightning Experience, these fields either don’t appear, show blank values, or result in an error.


Standard Objects EmailMessage

`update()` is supported when an email record is in `Draft` status, and `IsPrivateDraft` is `false` . It’s also supported if the
email status is `Draft`, `IsPrivateDraft` is `true,` and `CreatedBy` is associated with the current user. When the email record
isn’t in `Draft` status, the `IsExternallyVisible` field and custom fields only can be updated.

Set the Update Email Messages user permission for users, such as an Automated Case User, who run automated processes that modify
email message-related records. With the Update Email Message permission set, users’ processes can modify EmailMessageRelation and
ContentDocumentLink records that are related to an email message that isn’t in Draft status. Don’t set this user permission for other
users.

Access to an email message depends on the associated object. The user who created the email is specified in `CreatedById` and
always has access, unless that user is a guest user. Guest users have read access if the message is marked as `IsExternallyVisible` .

The object that’s used to determine access differs for Email-to-Case and Enhanced Email.

**•** Email-to-Case—When Email-to-Case is enabled and the email is Case-based (the `ParentId` field is Case), access depends on the
user’s access to the related Case record. If the email message is a draft, only the user in the `CreatedById` field or users with the
Modify All Data permission can access it.

**•** Enhanced Email—Access is activity-based. The `ActivityId` field specifies an associated Task record. You can control access to
[activity-based objects with the Access Activities permission. Users with the Modify All Data permission can also access the message.](https://help.salesforce.com/s/articleView?id=sales.activity_access_user_perm.htm&type=5&language=en_US)

When you use the API to insert EmailMessage records in bulk, the same access rules apply: access is based on cases in `ParentId`
fields or by tasks in `ActivityId` fields. When inserting a single record, set the `CreatedById` field to the user performing the
operation or leave it blank.

Fields

**Field** **Details**

```
ActivityId

AttachmentIds

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the activity that is associated with the email. Usually represents an open task
that is created for the case owner when a new unread email message is received.
`ActivityId` can only be specified for emails on cases. It’s auto-created for other
entities.

If an EmailMessage has a related task, and fields on the email record are updated, we
may delete the related task and create a new related task.

**Type**
string

**Properties**
Create, Nillable, Update

**Description**
A comma-separated list of email attachments. This is used by the Send Email quick
action when you use Salesforce Classic email templates. Maximum length is 32, 768
characters.


Standard Objects EmailMessage

**Field** **Details**

```
AutomationType

BccAddress

BccIds

CcAddress

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
A picklist value that determines if an outgoing email was manually created or
AI-generated.

Possible values are:

**•** `AiAssisted` –Email is AI-generated, but sent by human.

**•** `AiAutomated` –Email is generated and sent by AI.

**•** `Null` –Email is created and sent by human.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A string array of email addresses for recipients who were sent a visually impaired
carbon copy of the email message. Include only email addresses that aren’t associated
with Contact, Lead, or User records in Salesforce. If the recipient is a contact, lead, or
user, add their ID to the `BccIds` field instead of adding their email address to the
`BccAddress` field. When adding their ID, the email message is automatically
associated with the contact, lead, or user. For an Experience Cloud site user who isn’t
the sender of the email, this field returns null.

You can’t send emails unless there’s at least one recipient.

**Type**
JunctionIdList

**Properties**
Create, Update

**Description**
A string array of IDs for contacts, leads, and users who were sent a visually impaired
carbon copy of the email message. Each ID is linked to an
`EmailMessageRelation` record, which represents the relationship between
an email message and a Contact, Lead, or User record. For an Experience Cloud site
user who isn’t the sender of the email, this list is empty.

Adding a `JunctionIdList` field name to the `fieldsToNull` property deletes
all related junction records. This action can’t be undone.

**Type**
string


Standard Objects EmailMessage

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A string array of email addresses for recipients who were sent a carbon copy of the
email message. Include only email addresses that aren’t associated with Contact,
Lead, or User records in Salesforce. If the recipient is a contact, lead, or user, add their
ID to the `CcIds` field instead of adding their email address to the `CcAddress`
field. Then the email message is automatically associated with the contact, lead, or
user.

You can’t send emails unless there’s at least one recipient.

```
CcIds

ClientThreadIdentifier

ContentDocumentIds

```

**Type**
JunctionIdList

**Properties**
Create, Update

**Description**
A string array of IDs for contacts, leads, and users who were sent a carbon copy of the
email message. Each ID is linked to an `EmailMessageRelation` record, which
represents the relationship between an email message and a Contact, Lead, or User
record.

Adding a `JunctionIdList` field name to the `fieldsToNull` property deletes
all related junction records. This action can’t be undone.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A value used by third-party email clients to identify which thread an email belongs
[to. See Email-to-Case Threading for more information.](https://help.salesforce.com/s/articleView?id=service.support_email_to_case_threading.htm&type=5&language=en_US)

Available in API versions 56.0 and later.

**Type**
JunctionIdList

**Properties**
Create, Update

**Description**
A string array of IDs for content documents such as files and attachments that are
associated with an email. Each ID is linked to a `ContentDocumentLink` record,
which represents the relationship between an email message and a content document
record.


Standard Objects EmailMessage

**Field** **Details**

Adding a `JunctionIdList` field name to the `fieldsToNull` property deletes
all related junction records. This action can’t be undone.

```
Division

EmailRoutingAddressId

EmailTemplateId

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
A logical segment of your organization's data. For example, if your company is
organized into different business units, you could create a division for each business
unit, such as “North America,” “Healthcare,” or “Consulting.” Available only if the
organization has the Division permission enabled.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Stores the ID of the email routing address used to create the email. This value is set
when the email is processed by Email-to-Case service. When this field is set,
EmailMessage.Incoming cannot be `false` .

**Relationship Name**
EmailRoutingAddress

**Relationship Type**
Lookup

**Refers To**
EmailRoutingAddress

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The email template, if any, that was chosen for the email. This field is populated in
Lightning Experience only.

This is a relationship field.

**Relationship Name**
EmailTemplate

**Relationship Type**
Lookup

**Refers To**
EmailTemplate


Standard Objects EmailMessage

**Field** **Details**

```
FirstOpenedDate

FromAddress

FromId

FromName

HasAttachment

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date the email was first opened.

To see this field, enable email tracking in your org.

**Type**
email

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The address that originated the email. When using this field, specify an email address
that exists in EmailMessageRelation, with a `RelationType` of `FromAddress` .

EmailMessages in Draft status with `IsPrivateDraft` set to `true` must use
the user's address, a verified org-wide email address, or a verified Email-to-Case routing
address in the `FromAddress` field.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The contact, lead, or user who sent the email. Maximum length is 18 characters.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The sender’s name. When using this field, specify an email address that exists in
EmailMessageRelation, with a `RelationType` of `FromAddress` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the email was sent with an attachment ( `true` ) or not ( `false` ).


Standard Objects EmailMessage

**Field** **Details**

```
Headers

HtmlBody

Incoming

IsBounced

IsClientManaged

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The Internet message headers of the incoming email. Used for debugging and tracing
purposes. Doesn’t apply to outgoing emails.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The body of the email in HTML format.

You can’t send emails unless at least one of these fields has content.

**•** Subject field

**•** HTML Body or Text Body field

As the sender, you can provide the content, or it can be automatically inserted using
predefined values. An email template can also include the content for these fields.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the email was received ( `true` ) or sent ( `false` ).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the email bounced.

This field is set to True for bounced emails in orgs using Lightning Threading. It’s not
set to True for orgs using Ref ID threading.

To see this field, enable bounce management in your org.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort


Standard Objects EmailMessage

**Field** **Details**

**Description**
If EmailMessage is created with `IsClientManaged` set to `true`, users can modify
`EmailMessage.ContentDocumentIds` to link file attachments even when
the `Status` of the EmailMessage isn’t set to `Draft` . When this field is set to `true`
and Enhanced Email is enabled, a Task record is created for the EmailMessage
regardless of Email-to-Case settings.

```
IsDeleted

IsExternallyVisible

IsOpened

```

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not
( `false` ). Label is **Deleted** .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If the Experience Cloud site case feed is enabled, `IsExternallyVisible`
controls the external visibility of emails in sites. When `IsExternallyVisible`
is set to `true` —its default value—external users see the email message in the case
feed.

**•** Emails remain visible in the Emails related list whether or not this field is set to
true. For security reasons, we recommend that you remove this related list from
your case page layout for external community users.

**•** Only emails with a value in the `ParentId` field can be made externally visible
in sites.

**•** This field can’t be updated if the email’s `Status` is set to `Draft` .

**•** The `Enable Case Feeds in Experience Cloud Sites`
organization preference in Setup makes case-related emails, comments, and
updates visible to site members.

When this preference is off, `IsExternallyVisible` is True by default for
the EmailMessage. When this preference is on, `IsExternallyVisible`
defaults to True only if the case contact email is the sender or the recipient of the
`EmailMessage.` Otherwise, `IsExternallyVisible` defaults to False.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects EmailMessage

**Field** **Details**

**Description**
Indicates whether the email has been opened.

To see this field, enable email tracking in your org.

```
IsPrivateDraft

IsTracked

LastOpenedDate

MessageDate

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
If `IsPrivateDraft` is set to `true`, then only the `CreatedById` user can
view, update, and send this email draft. If `IsPrivateDraft` is set to `false`,
then any user with permissions to work on the case can see these drafts. After the
email is sent, then this field is updated to be `false` . Public drafts are loaded and
visible in Salesforce Classic while Private Drafts are only used in Lightning Experience.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the email is being tracked.

To see this field, enable email tracking in your org.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date the email was last opened.

To see this field, enable email tracking in your org.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date the email was created.

For inbound emails, Email-to-Case sets this field using the Date header. The Date
header is set by the email client and is subject to the sender's time preferences.


Standard Objects EmailMessage

**Field** **Details**

```
MessageIdentifier

Name

ParentId

RelatedToId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The ID of the email message.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
A name for the email message that's derived from the first 255 characters of the
Subject field. If the Subject field is empty, a localized string of `[No Subject]` is
used. This field is read-only and can’t be created or updated. Available in API versions
56.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the case that’s associated with the email.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Case

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The `RelatedToId` represents nonhuman objects such as accounts, opportunities,
campaigns, cases, or custom objects. RelatedToIds are polymorphic. Polymorphic
means a RelatedToId is equivalent to the ID of a related object.

You must have access to at least one entity listed under Refers To to access RelatedToId.

You can update `RelatedToId` when `IsClientManaged` is set to `true` .


Standard Objects EmailMessage

**Field** **Details**

`RelatedtoId` and `ParentId` should have the same value when `ParentId`
is set. You might see unexpected results otherwise.

This is a polymorphic relationship field.

**Relationship Name**
RelatedTo

**Relationship Type**
Lookup

**Refers To**
Account, Accreditation, AssessmentIndicatorDefinition, AssessmentTask,
AssessmentTaskContentDocument, AssessmentTaskDefinition, AssessmentTaskOrder,
Asset, AssetRelationship, AssignedResource, Award, BoardCertification, BusinessLicense,
BusinessMilestone, BusinessProfile, Campaign, CareBarrier, CareBarrierDeterminant,
CareBarrierType, CareDeterminant, CareDeterminantType, CareDiagnosis,
CareInterventionType, CareMetricTarget, CareObservation,
CareObservationComponent, CarePgmProvHealthcareProvider, CarePreauth,
CarePreauthItem, CareProgram, CareProgramCampaign, CareProgramEligibilityRule,
CareProgramEnrollee, CareProgramEnrolleeProduct, CareProgramEnrollmentCard,
CareProgramGoal, CareProgramProduct, CareProgramProvider,
CareProgramTeamMember, CareProviderAdverseAction, CareProviderFacilitySpecialty,
CareProviderSearchableField, CareRegisteredDevice, CareRequest, CareRequestDrug,
CareRequestExtension, CareRequestItem, CareSpecialty, CareSpecialtyTaxonomy,
CareTaxonomy, Case, CommSubscriptionConsent, ContactEncounter,
ContactEncounterParticipant, ContactRequest, Contract, CoverageBenefit,
CoverageBenefitItem, CreditMemo, DelegatedAccount, DocumentChecklistItem,
EnrollmentEligibilityCriteria, HealthcareFacility, HealthcareFacilityNetwork,
HealthcarePayerNetwork, HealthcarePractitionerFacility, HealthcareProvider,
HealthcareProviderNpi, HealthcareProviderSpecialty, HealthcareProviderTaxonomy,
IdentityDocument, Image, IndividualApplication, Invoice, ListEmail, Location,
MemberPlan, Opportunity, Order, OtherComponentTask, PartyConsent,
PersonLifeEvent, PlanBenefit, PlanBenefitItem, ProcessException, Product2,
ProductItem, ProductRequest, ProductRequestLineItem, ProductTransfer,
PurchaserPlan, ReceivedDocument, ResourceAbsence, ReturnOrder,
ReturnOrderLineItem, ServiceAppointment, ServiceResource, Shift, Shipment,
ShipmentItem, Solution, Visit, VisitedParty, VolunteerProject, WorkOrder,
WorkOrderLineItem

```
ReplyToEmailMessageId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the inbound or outbound email message the current email message is a reply
to. It’s not possible to reply to a message whose `Status` is `Draft` .

This is a relationship field.


Standard Objects EmailMessage

**Field** **Details**

This is only set for Case related Email replies at setup.

**Relationship Name**
ReplyToEmailMessage

**Relationship Type**
Lookup

**Refers To**
EmailMessage

```
Source

Status

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
When Sync Email as Salesforce Activity is enabled, this value reflects from where the
email was captured automatically. Available in API version 64.0 and later.

Possible values are:

**•** `Einstein Activity Capture` –Captured as an entire email message by
Einstein Activity Capture.

**•** `Einstein Activity Capture Limited` –Captured as a header-only
email by Einstein Activity Capture. The sender, recipients, date, and time of the
message were captured, not the subject or body.

**•** `Email Integration App Manual` -Captured to track the email message
records created or edited from the mailapp.

**•** `Migrated Captured Email` -An email that was captured in Einstein
Activity Capture and migrated to an updated version of Einstein Activity Capture
in which Sync Email as Activity is turned on. Available in API version 65.0 and later.

**•** `Migrated Captured Email Header Only` -An email that was captured
in Einstein Activity Capture and migrated as header-only data to an updated
version of Einstein Activity Capture in which Sync Email as Activity is turned on.
Available in API version 65.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the email.

The `Status` field is mostly read-only. You can change the status only from _`New`_ to
_`Read`_ .

Possible values are:

**•** `0` (New)


Standard Objects EmailMessage

**Field** **Details**

**•** `1` (Read)

**•** `2` (Replied)

**•** `3` (Sent)

**•** `4` (Forwarded)

**•** `5` (Draft)

For emails not sent as part of a case, only the status `3` (Sent) is valid.

```
Subject

TextBody

ThreadIdentifier

```

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The subject line of the email.

You can’t send emails unless at least one of these fields has content.

**•** Subject field

**•** HTML Body or Text Body field

As the sender, you can provide the content, or it can be automatically inserted using
predefined values. An email template can also include the content for these fields.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The body of the email, in plain text format. If `TextBody` isn’t set, then it’s extracted
from `HtmlBody` .

You can’t send emails unless at least one of these fields has content.

**•** Subject field

**•** HTML Body or Text Body field

As the sender, you can provide the content, or it can be automatically inserted using
predefined values. An email template can also include the content for these fields

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The ID of the email thread the email message belongs to. This field is used by features
that sync emails directly from an inbox into Salesforce. This field is not used by
On-Demand Email-to-Case.


Standard Objects EmailMessage

**Field** **Details**

```
ToAddress

ToIds

ValidatedFromAddress

```

Usage

EmailMessage is limited to 50 custom fields.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A string array of email addresses for recipients who were sent the email message.
Include only email addresses that aren’t associated with Contact, Lead, or User records
in Salesforce. If the recipient is a contact, lead, or user, add their ID to the `ToIds`
field instead of adding their email address to the `ToAddress` field. Then the email
message is automatically associated with the contact, lead, or user.

You can’t send emails unless there’s at least one recipient.

**Type**
JunctionIdList

**Properties**
Create, Update

**Description**
A string array of IDs for contacts, leads, and users who were sent a carbon copy of the
email message. Each ID is linked to an `EmailMessageRelation` record, which
represents the relationship between an email message and a Contact, Lead, or User
record.

Adding a `JunctionIdList` field name to the `fieldsToNull` property deletes
all related junction records. This action can’t be undone.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

A picklist value with either the sender's address, org-wide email addresses, or
Email-to-Case routing address. The email address must be verified. If the sender’s
email address is used, the sender must be the current user.

`ValidatedFromAddress` isn’t suitable for use in Group By or Sort By statements.
Use `FromAddress` instead.

If your org uses Email-to-Case, a case is created when an email is sent to one of your company’s addresses. The email, which is related
to the case by the `ParentID` field, is stored as an EmailMessage record. When users view the email, they see the EmailMessage record.


Standard Objects EmailMessage

If your org uses Enhanced Email, each email is stored as an EmailMessage record and a Task record. When users view an email, they see
the EmailMessage record.

Note: In an org with Email-to-Case enabled, an inbound (Incoming = true) email with case as the parent record won’t create a
task automatically. This functionality respects the Create Task from Email setting for each Email-to-Case routing address.

If you would like to change the recipients or contents of an outbound email, don’t use automation tools, like Flows or Apex triggers, to
update EmailMessage records. Unless they are for a draft, updates to EmailMessage records will not be reflected in the actual sent email.
[To update an email’s data before it’s sent, use Quick Action predefined values or a QuickActionDefaultsHandler.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_interface_QuickAction_QuickActionDefaultsHandler.htm)

When a Flow creates an EmailMessage with set values in the audit fields (like CreatedBy and CreatedDate), any FeedItem automatically
created for that EmailMessage will not share the same audit field values.

Sample Code—Apex

This sample logs email activity in Salesforce.

```
   // if EnhancedEmail Perm is not enabled, continue logging the email as a task

   // if EnhancedEmail Perm is enabled, create an EmailMessage object

   EmailMessage emailMessage = new EmailMessage();

   emailMessage.status = '3'; // email was sent

   emailMessage.relatedToId = '006B0000003weZGIAY'; // related to record e.g. an opportunity

   emailMessage.fromAddress = 'sender@example.com'; // from address

   emailMessage.fromName = 'Dan Perkins'; // from name

   emailMessage.subject = 'This is the Subject!'; // email subject

   emailMessage.htmlBody = '<html><body><b>Hello</b></body></html>'; // email body

   // Contact, Lead or User Ids of recipients

   String[] toIds = new String[]{'003B000000AxcEjIAJ'};

   emailMessage.toIds = toIds;

   // additional recipients who don’t have a corresponding contact, lead or user id in the

   Salesforce org (optional)

   emailMessage.toAddress = 'emailnotinsalesforce@toexample.com, anotherone@toexample.com';

   insert emailMessage; // insert

   // Add Email Message Relation for id of the sender

   EmailMessageRelation emr = new EmailMessageRelation();

   emr.emailMessageId = emailMessage.id;

   emr.relationId = '005B0000003qHvOIAU'; // user id of the sender

   emr.relationType = 'FromAddress';

   insert emr;

```

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**EmailMessageChangeEvent (API version 48.0)**
Change events are available for the object.

SEE ALSO:

Case

Overview of Salesforce Objects and Fields


### Standard Objects EmailMessageMigration EmailMessageMigration

For internal use only.

### EmailMessageRelation

Represents the relationship between an email and contacts, leads, and users. This object is available in API version 37.0 and later.

Special Access Rules

### EmailMessageRelation is only available for organizations that use Email-to-Case or Enhanced Email, which is automatically enabled for

most customers.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Fields

**Field Name** **Details**

```
EmailMessageId

RelationAddress

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
### The ID of the EmailMessage record.

This is a relationship field.

**Relationship Name**
### EmailMessage

**Relationship Type**
Lookup

**Refers To**
### EmailMessage

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The email address of the sender or recipient.


Standard Objects EmailMessageRelation

**Field Name** **Details**

Note: If a record relates an email to an existing contact, lead, or user record
in Salesforce, the value of `RelationAddress` is the current value of
the email address. If the value is not set, it is auto-populated from
`RelationId` .

```
RelationId

RelationObjectType

RelationType

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The `RecordId` of the sender or recipient.

Note: If a record relates an email to an email address that’s not associated
with an existing contact, lead, or user record in Salesforce, the value of
`RelationId` is null.

This is a polymorphic relationship field.

**Relationship Name**
Relation

**Relationship Type**
Lookup

**Refers To**
Contact, Lead, User

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API name of the object type of the `RecordId` in the `RelationId` field.
It can be a contact, lead, or user.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of relationship the contact, lead, or user has with the email message.
Possible values include:

**•** `ToAddress`

**•** `CcAddress`

**•** `BccAddress`

**•** `FromAddress`


### Standard Objects EmailRelay

**Field Name** **Details**

**•** `OtherAddress`

For an Experience Cloud site user who is not the sender of the email, no
`BccAddress` relations are returned.

Usage

EmailMessageRelation allows an email to be related to contacts, leads, and users.

### EmailRelay

Represents the configuration for sending an email relay. An email relay routes email sent from Salesforce through your company’s email
servers. This object is available in API version 43.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

You must have the Email Administration, Customize Application, and View Setup user permissions to use this object.

Fields

**Field Name** **Details**

```
AuthType

Host

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted Picklist, Sort, Update

**Description**

Specifies which SASL mechanism Salesforce uses for SMTP authentication. This
field is available when Enable SMTP Auth is selected. Select an option:

**•** PLAIN- Salesforce uses PLAIN SASL mechanism for SMTP authentication.
Default.

**•** LOGIN- Salesforce uses LOGIN SASL mechanism for SMTP authentication

This field is available in API version 52.0 and later.

**Type**
string


Standard Objects EmailRelay

**Field Name** **Details**

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**

Indicates the host name or IP address of your company's SMTP server.

```
IsRequireAuth

Password

Port

TlsSetting

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether (true) or not (false) authentication is required. When setting
this field to true, the `TlsSetting` must be set to **`RequiredVerify`** . This
field is available in API version 44.0 and later.

**Type**
encryptedstring

**Properties**
Create, Nillable, Update

**Description**

Specifies the password for relay host STMP authentication. When
`IsRequireAuth` is set to true, this field is required. This field is available in
API version 44.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

Indicates the port number of your company's SMTP server.

**•** 25

**•** 587

**•** 10025

**•** 11025

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

Specifies whether Salesforce uses TLS for SMTP sessions.


Standard Objects EmailRelay

**Field Name** **Details**

**•** `Off` : TLS is turned off. SMTP session continues through an insecure
connection.

**•** `Preferred` : If the remote server supports TLS, Salesforce upgrades the
current SMTP session to use TLS. If TLS is unavailable, Salesforce continues
the session without TLS.

**•** `Required` : Salesforce continues the session only if the remote server
supports TLS. If TLS is unavailable, Salesforce terminates the session without
delivering the email.

**•** `PreferredVerify` : If the remote server supports TLS, Salesforce upgrades
the current SMTP session to use TLS. Before the session begins, Salesforce
verifies that the certificate is signed by a valid certificate authority, and that
the common name presented in the certificate matches the domain or mail
exchange of the current connection. If TLS is available but the certificate is
not signed or the common name does not match, Salesforce disconnects
the session and does not deliver the email. If TLS is unavailable, Salesforce
continues the session without TLS.

**•** `RequiredVerify` : Salesforce continues the session only if the remote
server supports TLS, the certificate is signed by a valid certificate authority,
and the common name presented in the certificate matches the domain or
mail exchange to which Salesforce is connected. If any of these criteria are
not met, Salesforce terminates the session without delivering the email.

```
Username

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Specifies the username for relay host STMP authentication. When
`IsRequireAuth` is set to true, this field is required. This field is available in
API version 44.0 and later.

An email relay must be associated with an active email domain filter to take effect. If you set up multiple email relays in one org, they
are processed in the priority order of their email domain filters.

Tip: If you also plan to activate Bounce Management and Email Compliance Management, confirm with your email admin that
[your company allows relaying email sent from Salesforce. For more information on bounce management, see Configure Deliverability](https://help.salesforce.com/articleView?id=emailadmin_send_through_salesforce_configure_deliverability.htm&language=en_US)
[Settings for Emails Sent from Salesforce.](https://help.salesforce.com/articleView?id=emailadmin_send_through_salesforce_configure_deliverability.htm&language=en_US)

SEE ALSO:

EmailServicesFunction

EmailDomainFilter


### Standard Objects EmailRoutingAddress EmailRoutingAddress

An email address used for Email-to-Case. Email routing addresses store a unique email services address provided by Salesforce and
configuration options for emails received by this address.

Supported Calls

`create()`, `describeSObjects()`, `delete()`, `update()`, `query()`, `retrieve()`, `upsert()`

Special Access Rules

To access this object, Email-to-Case must be enabled. Only admin users can access this object.

Fields

**Field** **Details**

```
PersonalName

Address

EmailServicesAddress

```

SEE ALSO:

EmailServicesAddress

**Type**
string

**Properties**
Create, Filter, Sort, Update

**Description**
The display name of the EmailRoutingAddress. Maximum size is 300 characters.

**Type**
email

**Properties**
Create, Filter, Sort, Update

**Description**
The email address to which your customers direct their questions. Emails are forwarded from
this address.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A unique, Salesforce-generated email address. This field value is read-only and can't be
modified. Emails are forwarded to this address.


### Standard Objects EmailServicesAddress EmailServicesAddress

An email service address.

Each email service has one or more email addresses to which users can send messages for processing. An email service only processes
messages it receives at one of its addresses.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Special Access Rules

As of Summer ’20 and later, only authenticated internal and external users can access this object.

Fields

**Field** **Details**

```
AuthorizedSenders

DeveloperName

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Configures the email service address to only accept messages from the email addresses or
domains listed in this field. If the email service address receives a message from an unlisted
email address or domain, the email service performs the action specified in the
`AuthorizationFailureAction` field of its associated email service. Leave this field
blank if you want the email service address to receive email from any email address.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The name of the object in the API. This name can contain only underscores and alphanumeric
characters and must be unique in your org. It must begin with a letter, not include spaces,
not end with an underscore, and not contain two consecutive underscores. This 25-character
field must be unique among other EmailServicesAddress records under the same
EmailServiceFunction parent.

In managed packages, this field prevents naming conflicts on package installations. This field
is automatically generated, but you can supply your own value if you create the record using
the API. With this field, a developer can change the object’s name in a managed package
and the changes are reflected in a subscriber’s organization.


Standard Objects EmailServicesAddress

**Field** **Details**

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance might be slow
while Salesforce generates one for each record.

```
EmailDomainName

FunctionId

IsActive

LocalPart

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A read only field you can query that contains the system-generated domain part of this email
service address. The system generates a unique domain-part for each email service address
to ensure that no two email service addresses are identical.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the email service for which the email service address receives messages.

This is a relationship field.

**Relationship Name**
Function

**Relationship Type**
Lookup

**Refers To**
EmailServicesFunction

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this object is active (true) or not (false).

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The local-part of the email service address. The local-part of the address is the string that
comes before the @ symbol.


### Standard Objects EmailServicesFunction

**Field** **Details**

For the local-part of a Salesforce email address, all alphanumeric characters are valid, plus
the following special characters:

```
                   ! # $ % & amp; ' * / = ? ^ _ + - ` { | } ~,

```

The dot character (.) is also valid as long as it's not the first or last character.

Email addresses aren’t case-sensitive.

```
RunAsUserId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The username of the user whose permissions the email service assumes when processing
messages sent to this address.

This object supports the email services feature, which allows you to create automated processes that use Apex classes to process the
contents, headers, and attachments of inbound email. For example, you can create an email service that automatically creates contact
records based on contact information in messages.

SEE ALSO:

### EmailServicesFunction EmailServicesFunction

An email service.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
upsert()

```

Special Access Rules

As of Summer ’20 and later, only authenticated internal and external users can access this object.


Standard Objects EmailServicesFunction

Fields

**Field** **Details**

```
AddressInactiveAction

ApexClassId

AttachmentOption

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates what the email service does with messages received at an email address that is
inactive.

One of the following values:

**•** `UseSystemDefault` —The system default is used. (In API version 41.0 and earlier,
the value specified for this choice is `0` .)

**•** `Bounce` —The email service returns the message to the sender with a notification that
explains why the message was rejected. (In API version 41.0 and earlier, the value specified
for this choice is `1` .)

**•** `Discard` —The email service deletes the message without notifying the sender. (In
API version 41.0 and earlier, the value specified for this choice is `2` .)

**•** `Requeue` —The email service queues the message for processing in the next 24 hours.
If the message is not processed within 24 hours, the email service returns the message
to the sender with a notification that explains why the message was rejected. (In API
version 41.0 and earlier, the value specified for this choice is `3` .)

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. The ID of the Apex class that the email service uses to process inbound messages.

This field is required for API version 12.0 and later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates the types of attachments the email service accepts. One of the following values:

**•** `None` —The email service accepts the message but discards any attachment. (In API
version 41.0 and earlier, the value specified for this choice is `0` .)

**•** `NoContent` —The attachment metadata (filename, MIME type, and so on) is provided
to the Apex class, but the body is set to `null` . There was no previous numeric value for
this choice.


Standard Objects EmailServicesFunction

**Field** **Details**

**•** `TextOnly` —The email service only accepts the following types of attachments:

**–** Attachments with a Multipurpose Internet Mail Extension (MIME) type of text.

**–** Attachments with a MIME type of application/octet-stream and a file name that ends
with either a .vcf or .vcs extension. These are saved as text/x-vcard and text/calendar
MIME types, respectively.

(In API version 41.0 and earlier, the value specified for this choice is `1` .)

**•** `BinaryOnly` —The email service only accepts binary attachments, such as image,
audio, application, and video files. (In API version 41.0 and earlier, the value specified for
this choice is `2` .)

**•** `All` —The email service accepts any type of attachment. (In API version 41.0 and earlier,
the value specified for this choice is `3` .)

```
AuthenticationFailureAction

AuthorizationFailureAction

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates what the email service does with messages that fail or do not support any of the
authentication protocols if the `IsAuthenticationRequired` field is true.

One of the following values:

**•** `UseSystemDefault` —The system default is used. (In API version 41.0 and earlier,
the value specified for this choice is `0` .)

**•** `Bounce` —The email service returns the message to the sender with a notification that
explains why the message was rejected. (In API version 41.0 and earlier, the value specified
for this choice is `1` .)

**•** `Discard` —The email service deletes the message without notifying the sender. (In
API version 41.0 and earlier, the value specified for this choice is `2` .)

**•** `Requeue` —The email service queues the message for processing in the next 24 hours.
If the message is not processed within 24 hours, the email service returns the message
to the sender with a notification that explains why the message was rejected. (In API
version 41.0 and earlier, the value specified for this choice is `3` .)

**Type**
picklist

**Properties**
Defaulted on create, Group, Sort, Create, Filter, Nillable, Restricted picklist, Update

**Description**
Indicates what the email service does with messages received from senders who are not
listed in the `AuthorizedSenders` field on either the email service or email service
address.

One of the following values:


Standard Objects EmailServicesFunction

**Field** **Details**

**•** `UseSystemDefault` —The system default is used. (In API version 41.0 and earlier,
the value specified for this choice is `0` .)

**•** `Bounce` —The email service returns the message to the sender with a notification that
explains why the message was rejected. (In API version 41.0 and earlier, the value specified
for this choice is `1` .)

**•** `Discard` —The email service deletes the message without notifying the sender. (In
API version 41.0 and earlier, the value specified for this choice is `2` .)

**•** `Requeue` —The email service queues the message for processing in the next 24 hours.
If the message is not processed within 24 hours, the email service returns the message
to the sender with a notification that explains why the message was rejected. (In API
version 41.0 and earlier, the value specified for this choice is `3` .)

```
AuthorizedSenders

ErrorRoutingAddress

FunctionInactiveAction

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Configures the email service to only accept messages from the email addresses or domains
listed in this field. If the email service receives a message from an unlisted email address or
domain, the email service performs the action specified in the
`AuthorizationFailureAction` field. Leave this field blank if you want the email
service to receive email from any email address.

**Type**
email

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The destination email address for error notification email messages when
`IsErrorRoutingEnabled` is `true` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates what the email service does with messages it receives when the email service itself
is inactive.

One of the following values:

**•** `UseSystemDefault` —The system default is used. (In API version 41.0 and earlier,
the value specified for this choice is `0` .)


Standard Objects EmailServicesFunction

**Field** **Details**

**•** `Bounce` —The email service returns the message to the sender with a notification that
explains why the message was rejected. (In API version 41.0 and earlier, the value specified
for this choice is `1` .)

**•** `Discard` —The email service deletes the message without notifying the sender. (In
API version 41.0 and earlier, the value specified for this choice is `2` .)

**•** `Requeue` —The email service queues the message for processing in the next 24 hours.
If the message is not processed within 24 hours, the email service returns the message
to the sender with a notification that explains why the message was rejected. (In API
version 41.0 and earlier, the value specified for this choice is `3` .)

```
FunctionName

IsActive

IsAuthenticationRequired

IsErrorRoutingEnabled

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the email service.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this object is active ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Configures the email service to verify the legitimacy of the sending server before processing
a message. The email service uses the SPF, SenderId, and DomainKeys protocols to verify the
sender's legitimacy: If the sending server passes at least one of these protocols and does not
fail any, the email service accepts the email. If the server fails a protocol or does not support
any of the protocols, the email service performs the action specified in the
`AuthenticationFailureAction` field.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
When incoming email messages can’t be processed, indicates whether error notification
email messages are routed to a chosen address or to the senders.


Standard Objects EmailServicesFunction

**Field** **Details**

```
IsTextAttachmentsAsBinary

IsTextTruncated

IsTlsRequired

OverLimitAction

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If `true`, text attachments are supplied to the Apex code as a
`Messaging.BinaryAttachment` instead of as a
`Messaging.TextAttachment` . This means that the body is supplied as an Apex Blob
instead of as an Apex String.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
This field is deprecated. It is not available as of API version 23.0 and is deprecated and hidden
in versions 17.0 through 22.0. In all API versions, the email service now accepts inbound
email messages up to the 10 MB size limit, without truncating the text. Previously, it indicated
whether the email service truncated and accepted email messages with HTML body text,
plain body text, and text attachments over approximately 100,000 characters ( `true` ) or
rejected these email messages and notified the sender ( `false` ).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Not currently in use.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates what the email service does with messages if the total number of messages
processed by all email services combined has reached the daily limit for your organization.

One of the following values:

**•** `UseSystemDefault` —The system default is used. (In API version 41.0 and earlier,
the value specified for this choice is `0` .)

**•** `Bounce` —The email service returns the message to the sender with a notification that
explains why the message was rejected. (In API version 41.0 and earlier, the value specified
for this choice is `1` .)


### Standard Objects EmailStatus

**Field** **Details**

**•** `Discard` —The email service deletes the message without notifying the sender. (In
API version 41.0 and earlier, the value specified for this choice is `2` .)

**•** `Requeue` —The email service queues the message for processing in the next 24 hours.
If the message is not processed within 24 hours, the email service returns the message
to the sender with a notification that explains why the message was rejected. (In API
version 41.0 and earlier, the value specified for this choice is `3` .)

The system calculates the limit by multiplying the number of user licenses by 1,000.

Usage

This object supports the email services feature, which allows you to create automated processes that use Apex classes to process the
contents, headers, and attachments of inbound email. For example, you can create an email service that automatically creates contact
records based on contact information in messages.

SEE ALSO:

EmailServicesAddress

### EmailStatus

Represents the status of email sent.

Supported Calls

```
   describeSObjects()

```

Special Access Rules

Customer Portal users can’t access this object.

Fields

**Field** **Details**

```
EmailTemplateName

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the EmailTemplate.


Standard Objects EmailStatus

**Field** **Details**

```
FirstOpenDate

LastOpenDate

TaskId

TimesOpened

WhoId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date when the email was first opened by recipient. Label is **Date Opened** .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date when the email was last opened by recipient.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The activity (task or event) associated with the email. Label is **Activity ID** .

This is a relationship field.

**Relationship Name**
Task

**Relationship Type**
Lookup

**Refers To**
Task

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Number of times the recipient opened the email.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects EmailTemplate

**Field** **Details**

**Description**
The WhoId represents a human such as a lead or a contact. WhoIds are polymorphic.
Polymorphic means a WhoId is equivalent to a contact’s ID or a lead’s ID. The label is `Name`
`ID` .

This is a polymorphic relationship field.

**Relationship Name**
Who

**Relationship Type**
Lookup

**Refers To**
Contact, Lead

SEE ALSO:

### EmailTemplate EmailTemplate

Represents a template for an email, mass email, list email, or Sales Engagement email. Supported in first-generation managed packages
only.

Note: You can’t send a mass email using a Visualforce email template.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `update()`, `upsert()`

Special Access Rules

Customer Portal users can’t access this object.

Fields

**Field** **Details**

```
ApiVersion

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The API version for this class. Every class has an API version specified at creation.


Standard Objects EmailTemplate

**Field** **Details**

```
Body

BrandTemplateId

DeliveryRate

Description

DeveloperName

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Content of the email. Limit: 384 KB.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. ID of the BrandTemplate associated with this email template. The brand template
supplies letterhead information for the email template.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**

Read-only. The percentage of the emails that were delivered compared to the number that
bounced (soft and hard). Note: this data includes emails that were delivered to the recipient's
spam folder.

This field is available in API version 46.0 and later. To access this field, your org must use Sales
Engagement and users need the Sales Engagement User or Sales Engagement Cadence
Creator permission set. This field value includes emails sent via the ListEmail object or Sales
Engagement cadences.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Description of the template, for example, Promotion Mass Mailing.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not


Standard Objects EmailTemplate

**Field** **Details**

include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization. Label is **Template Unique Name** .

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance may slow while
Salesforce generates one for each record.

```
Encoding

EnhancedLetterheadId

EntityType

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Character set encoding for the template.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the enhanced letterhead associated with the email template.

Note: To use an enhanced letterhead, associate it with a Lightning email template
that uses the HML merge language.

This is a relationship field.

**Relationship Name**
EnhancedLetterhead

**Relationship Type**
Lookup

**Refers To**
EnhancedLetterhead

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort,

**Description**
When `UIType` is `2` (Lightning Experience) or `3` (Lightning ExperienceSample),
`EntityType` indicates which entities this template can be used with (for example, account
or lead). Valid values are standard object ID prefixes: 001 for account, 003 for contact, 006
for opportunity, and 00Q for lead, 500 for case, and 701 for campaign.

This field has been removed in API version 39.0. Use `RelatedEntityType` instead.


Standard Objects EmailTemplate

**Field** **Details**

```
FolderId

FolderName

HasSalesforceFiles

HtmlValue

IsActive

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the folder that contains the template.

This is a relationship field.

**Relationship Name**
Folder

**Relationship Type**
Lookup

**Refers To**
Folder, Organization, User

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The name of the folder that contains the template.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If the email template has attachments from Salesforce Files. The default value is false.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
This field contains the content of the email message, including HTML coding to render the
email message. Limit: 384 KB.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects EmailTemplate

**Field** **Details**

**Description**
Indicates that this template is active if `true`, or inactive if `false` .

```
IsBuilderContent

LastUsedDate

Markup

Name

NamespacePrefix

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If the email template was made in Email Template Builder. The default value is false.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when this email template was last used.

Used with Salesforce Classic templates.

Not typically used with Lightning Experience templates.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The Visualforce markup, HTML, JavaScript, or any other Web-enabled code that defines the
content of the template.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the template. Label is **Email Template Name** .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can


Standard Objects EmailTemplate

**Field** **Details**

refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

This field can’t be accessed unless the logged-in user has the Customize Application
permission.

```
OwnerId

RelatedEntityType

Subject

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of the template.

This is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
When `UIType` is `2` (Lightning Experience) or `3` (Lightning ExperienceSample),
`RelatedEntityType` indicates which entities this template can be used with. Valid
values are the entity API name: "Account" for account, "Contact" for contact, "Opportunity"
for opportunity, "Lead" for lead, and so on. The value can be any entity the user has read
access to (including custom entities) but not virtual entities, setup entities, or platform entities.

No restrictions exist at the schema level.

**Type**
string


Standard Objects EmailTemplate

**Field** **Details**

**Properties**
Create, Nillable, Sort, Update

**Description**
Content of the subject line.

The limit is 1,000 characters for Lightning email templates and 230 characters for Classic
email templates.

```
TemplateStyle

TemplateType

TimesUsed

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Style of the template.

Possible values are:

**•** `formalLetter` —Formal Letter

**•** `freeForm` —Free Form Letter

**•** `newsletter` —Newsletter

**•** `none` —No Email Layout

**•** `products` —Products

**•** `promotionLeft` —Promotion (Left)

**•** `promotionRight` —Promotion (Right)

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Type of template.

Possible values are:

**•** `custom` —Custom

**•** `html` —HTML

**•** `text` —Text

**•** `visualforce` —Visualforce

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of times this email template has been used.


Standard Objects EmailTemplate

**Field** **Details**

Used with Salesforce Classic templates.

Not typically used with Lightning Experience templates.

```
TotalDelivered

TotalHardBounced

TotalOpens

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

Read-only. The total number of emails sent minus hard and soft bounces. Note: this data
includes emails that were delivered to the recipient's spam folder.

This field is available in API version 46.0 and later. To access this field, your org must use Sales
Engagement and users need the Sales Engagement User or Sales Engagement Cadence
Creator permission set. This field value includes emails sent via the ListEmail object or Sales
Engagement cadences.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

Read-only. The total number of emails that permanently bounced back to the sender because
the address is invalid. A hard bounce can occur because the domain name doesn't exist or
because the recipient is unknown.

This field is available in API version 46.0 and later. To access this field, your org must use Sales
Engagement and users need the Sales Engagement User or Sales Engagement Cadence
Creator permission set. This field value includes emails sent via the ListEmail object or Sales
Engagement cadences.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

Read-only. The total number of times a prospect’s email client loaded the images in the
HTML version of the email. We also record an open if the prospect clicks a link within the
HTML or text email without downloading images. A click indicates that they viewed the
message. Some email clients (Outlook, Apple Mail, Thunderbird) don’t display images by
default. Pardot counts an open each time the images load.

This field is available in API version 46.0 and later. To access this field, your org must use Sales
Engagement and users need the Sales Engagement User or Sales Engagement Cadence
Creator permission set. This field value includes emails sent via the ListEmail object or Sales
Engagement cadences.


Standard Objects EmailTemplate

**Field** **Details**

```
TotalSent

TotalSoftBounced

UIType

```

Usage

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Read-only. The total number of emails sent, including bounced, opted-out, and invalid To:
addresses.

This field is available in API version 46.0 and later. To access this field, your org must use Sales
Engagement and users need the Sales Engagement User or Sales Engagement Cadence
Creator permission set. This field value includes emails sent via the ListEmail object or Sales
Engagement cadences.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

Read-only. The total number of times a recipient’s mail server acknowledged the email, but
returned it to the sender. Sometimes it is because the recipient's mailbox is full or the mail
server is temporarily unavailable. A soft bounce message can sometimes be delivered at
another time. After 5 soft bounces, Pardot opts the prospect out of emails.

This field is available in API version 46.0 and later. To access this field, your org must use Sales
Engagement and users need the Sales Engagement User or Sales Engagement Cadence
Creator permission set. This field value includes emails sent via the ListEmail object or Sales
Engagement cadences.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the user interface where this template is usable.

Possible values are:

**•** `Aloha`

**•** `SFX`

**•** `SFX_Sample` —SFXSample

To retrieve this object, issue a describe call on an object, which returns a query result for each activity since the object was created. You
can't query these records.


### Standard Objects EmailTemplateMonthlyMetric

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**EmailTemplateChangeEvent (API version 48.0)**
Change events are available for the object.

SEE ALSO:

Attachment

EmailStatus

DocumentAttachmentMap

### EmailTemplateMonthlyMetric

Represents the monthly engagement metrics for an email template. This object is available in API version 53.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Sales Engagement must be enabled.

Fields

**Field** **Details**

```
AllEmailsBouncedCount

AllEmailsDeliveredCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total of hard and soft bounced emails for this email template in the month.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of successfully delivered emails for this email template in the month.

This is a calculated field.


Standard Objects EmailTemplateMonthlyMetric

**Field** **Details**

```
AllEmailsHardBouncedCount

AllEmailsLinkClickedCount

AllEmailsNotDeliveredCount

AllEmailsOpenedCount

AllEmailsOutOfOfficeCount

AllEmailsRepliedCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of hard bounced emails for this email template in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails containing a link clicked by the recipient for this email template in
the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails not delivered for this email template in the month. This field is available
in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails opened by the recipient for this email template in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that triggered an out-of-office reply for this email template in the
month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects EmailTemplateMonthlyMetric

**Field** **Details**

**Description**
The number of emails replied to for this email template in the month.

```
AllEmailsSentCount

AllEmailsSoftBouncedCount

AllEmailsTrackedSentCount

AllEmailsUntrackedSentCount

DeliveredRecipientCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent for this email template in the month.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails soft bounced for this email template in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with engagement tracking enabled for this email template in the
month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent without engagement tracking for this email template in the
month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who were successfully delivered an email for this email template
in the month. This field is available in API version 54.0 and later.


Standard Objects EmailTemplateMonthlyMetric

**Field** **Details**

This is a calculated field.

```
DeliveredRecipientRate

EmailTemplateId

HardBounceTrackableSends

HrdBncTrackableRecipientSends

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of unique recipients that received an email you sent. This field is available
in API version 54.0 and later.

This is a calculated field.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related email template.

This is a relationship field.

**Relationship Name**
EmailTemplate

**Relationship Type**
Lookup

**Refers To**
EmailTemplate

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with hard bounce tracking. This field is available in API version
54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who received an email with hard bounce tracking. This field is
available in API version 54.0 and later.


Standard Objects EmailTemplateMonthlyMetric

**Field** **Details**

```
IsLocked

LinkClickTrackableSends

LinkClkTrackableRecipientSends

MayEdit

Month

MonthInt

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the monthly metric record is locked or not.

The default value is 'false'.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with link click tracking for the email template in the month. This
field is available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who received an email with link tracking for the email template in
the month. This field is available in API version 54.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the monthly metric record can be edited or not.

The default value is 'false'.

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
The month in which the engagement occurred.

**Type**
int


Standard Objects EmailTemplateMonthlyMetric

**Field** **Details**

**Properties**
Filter, Group, idLookup, Sort

**Description**
The month in which the engagement occurred, in yyyymm format.

```
OooTrackableRecipientSends

OpenTrackableRecipientSends

OpenTrackableSends

OutOfOfficeTrackableSends

RecipientReplies

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who received an email with out-of-office tracking for the email
template in the month. Out-of-office tracking requires Inbox. This field is available in API
version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who received an email with open tracking for the email template
in the month. This field is available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with open tracking for the email template in the month. This field
is available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with out-of-office tracking for the email template in the month.
This field is available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects EmailTemplateMonthlyMetric

**Field** **Details**

**Description**
The number of unique recipients who replied to an email for this email template in the
month. This field is available in API version 54.0 and later.

```
RecipientSends

RecipientsHardBounced

RecipientsOutOfOffice

RecipientsSoftBounced

ReplyTrackableRecipientSends

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique email recipients for this email template in the month. This field is
available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients that hard-bounced an email for this email template in the month.
Hard bounces can mean that the recipient's email address doesn't exist or is misspelled. This
field is available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients that responded with an out-of-office reply for the email template
in the month. This field is available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients that soft-bounced an email for the email template in the month.
A soft bounce often indicates a temporary issue with the recipient's email server, such as a
full inbox. This field is available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects EmailTemplateMonthlyMetric

**Field** **Details**

**Description**
The number of recipients who received an email with reply tracking for this email template
in the month. This field is available in API version 54.0 and later.

```
ReplyTrackableSends

SftBncTrackableRecipientSends

SoftBounceTrackableSends

SomeEmailsDeliveredCount

SomeEmailsDeliveredRate

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with reply tracking for the email template in the month. This field
is available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who received an email with soft bounce tracking for the email
template in the month. This field is available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with soft bounce tracking for the email template in the month.
This field is available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of sent emails that were successfully delivered to at least one of its recipients
for the email template in the month. This field is available in API version 54.0 and later.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort


Standard Objects EmailTemplateMonthlyMetric

**Field** **Details**

**Description**
The percentage of sent and tracked emails that were successfully delivered to at least one
of their recipients for the email template in the month. This field is available in API version
54.0 and later.

This is a calculated field.

```
TrackableRecipientSendHrdBncRt

TrackableRecipientSendOooRate

TrackableRecipientSendReplyRt

TrackableRecipientSendSftBncRt

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to unique recipients with hard bounce tracking that hard
bounced for the email template in the month. This field is available in API version 54.0 and
later.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with out-of-office tracking that received out-of-office replies
from unique recipients for the email template in the month. This field is available in API
version 54.0 and later.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with reply tracking that received replies from unique recipients
for the email template in the month. This field is available in API version 54.0 and later.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort


Standard Objects EmailTemplateMonthlyMetric

**Field** **Details**

**Description**
The percentage of emails sent to unique recipients with soft bounce tracking that
soft-bounced for the email template in the month. This field is available in API version 54.0
and later.

This is a calculated field.

```
TrackableSendHardBounceRate

TrackableSendLinkClickRate

TrackableSendOpenRate

TrackableSendOutOfOfficeRate

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with hard bounce tracking that hard bounced for the email
template in the month. This field is available in API version 54.0 and later.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with link tracking that had link clicks for the email template
in the month. This field is available in API version 54.0 and later.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with open tracking that were opened by the recipient for the
email template in the month. This field is available in API version 54.0 and later.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with out-of-office tracking that received out-of-office replies
for the email template in the month. This field is available in API version 54.0 and later.

This is a calculated field.


Standard Objects EmailTemplateMonthlyMetric

**Field** **Details**

```
TrackableSendReplyRate

TrackableSendSoftBounceRate

UniqueEmailsLinkClickedCount

UniqueEmailsOpenedCount

UniqueEmailsRepliedCount

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with reply tracking that received replies for the email template
in the month. This field is available in API version 54.0 and later.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with soft bounce tracking that soft bounced for the email
template in the month. This field is available in API version 54.0 and later.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of link clicks by unique recipients for the email template in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times an email you sent was opened by a unique recipient for the email
template in the month. When you send a list email, this field increments each time a recipient
opens the received email.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of replies from unique recipients for the email template in the month.


### Standard Objects EmbeddedServiceDetail EmbeddedServiceDetail

Represents a metadata catalog object that exposes fields from the underlying Embedded Service setup objects defined in each
EmbeddedServiceConfig deployment for guest users. Guest users don’t have direct access to the Embedded Service setup objects.
Available in API version 39.0 and later.

Supported SOAP Calls

`describeSObjects()`, `query()`

Supported REST HTTP Methods

```
   GET

```

Fields

**Field** **Details**

```
AvatarImg

ContrastInvertedColor

ContrastPrimaryColor

CustomMinimizedComponent

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
URL of the image used as the agent avatar image.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Accent branding color used in the embedded component, displayed as a hexadecimal value.
Changes made to this field in the API aren’t reflected in the embedded component.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Value of the `ContrastPrimaryColor` field in the EmbeddedServiceBranding setup
object.

**Type**
string


Standard Objects EmbeddedServiceDetail

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The custom Aura component that’s used for the minimized state for this Embedded Chat
deployment.

```
CustomPrechatComponent

DurableId

FieldServiceConfirmCardImg

FieldServiceHomeImg

FieldServiceLogoImg

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The custom Aura component that’s used for the pre-chat page for this Embedded Chat
deployment.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Developer name for the EmbeddedServiceConfig.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
URL of the image used for the confirmation card in embedded Appointment Management
(beta).

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
URL of the image used for the home screen in embedded Appointment Management (beta).

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
URL of the logo used for the home screen in embedded Appointment Management (beta).


Standard Objects EmbeddedServiceDetail

**Field** **Details**

```
Font

FontSize

HeaderBackgroundImg

Height

IsFieldServiceEnabled

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Font used in the chat text of the Embedded Chat window.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Font size for the embedded component.

Possible values are:

**•** Small

**•** Medium

**•** Large

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
URL of the image used for the header background in Embedded Chat. This field is removed
in API version 49.0 and later. The header background image is no longer supported.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Height of the embedded component.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether Field Service is enabled for this Embedded Service deployment ( `true` )
or not ( `false` ). Embedded Appointment Management is currently beta.


Standard Objects EmbeddedServiceDetail

**Field** **Details**

```
IsLiveAgentEnabled

IsOfflineCaseEnabled

IsPrechatEnabled

IsQueuePositionEnabled

NavBarColor

NavBarTextColor

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether Chat is enabled for this Embedded Service deployment ( `true` ) or not
( `false` ).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether offline support is enabled for this Embedded Chat deployment ( `true` )
or not ( `false` ).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Value of the `PrechatEnabled` field in the EmbeddedServiceLiveAgent setup object.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether queue position (displaying the customer’s place in line while they wait
for an agent) is enabled for this Embedded Chat deployment ( `true` ) or not ( `false` ).

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Value of the `NavBarColor` field in the EmbeddedServiceBranding setup object.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects EmbeddedServiceDetail

**Field** **Details**

**Description**
This field is used to set the text color for the header.

```
OfflineCaseBackgroundImg

PrechatBackgroundImg

PrimaryColor

SecondaryColor

SecondaryNavBarColor

ShouldHideAuthDialog

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
URL of the image used for the background for the offline support case form in Embedded
Chat.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
URL of the image used for the background for the pre-chat form in Embedded Chat.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Value of the `PrimaryColor` field in the EmbeddedServiceBranding setup object.

**Type**
string

**Properties**
Filter, Group, Nillable Sort

**Description**
Value of the `SecondaryColor` field in the EmbeddedServiceBranding setup object.

**Type**
string

**Properties**
Filter, Group, Nillable Sort

**Description**
This field is used to set the color of a secondary header.

**Type**
boolean


Standard Objects EmbeddedServiceDetail

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether the prompt that the customer log in again during a flow should be hidden
( `true` ) or not ( `false` ). When it’s hidden, the customer is taken directly to your login page.

```
ShouldShowExistingAppointment

ShouldShowNewAppointment

Site

SmallCompanyLogoImg

WaitingStateBackgroundImg

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether to display a button on the home screen for customers to access their
existing appointments ( `true` ) or not ( `false` ) for embedded Appointment Management
(beta).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether to display a button on the home screen for customers to create a new
appointment ( `true` ) or not ( `false` ) for embedded Appointment Management (beta).

**Type**
string

**Properties**
Filter, Group, Nillable Sort

**Description**
Value of the `Site` field in the EmbeddedServiceConfig setup object.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
URL of the logo image used with Embedded Chat.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects EmbeddedServiceLabel

**Field** **Details**

**Description**
URL of the image used for the background image in Embedded Chat while the customer
waits to be connected with a support agent.

```
Width

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Width of the embedded component.

Note: Any changes you make to the image fields override what you’ve entered in Setup. We recommend setting your image
URLs in Setup.

### EmbeddedServiceLabel

Represents a customized label in Embedded Chat or embedded Appointment Management.This object is available in API version 44.0
and later.

Supported SOAP Calls

`describeSObjects()`, `query()`

Supported REST HTTP Methods

```
GET

```

Fields

**Field** **Details**

```
CustomLabelName

DurableId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The developer name for the custom label.

**Type**
string


### Standard Objects Employee

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique name containing `EmbeddedServiceConfig.labelKey` .

```
EmbeddedServiceConfigDeveloperName

LabelKey

### Employee

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Developer name for the EmbeddedServiceConfig.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of label for this embedded component. The value corresponds to the label within
a label group (substate of chat state or page type).

Represents an employee within a company or organization. This object is available in API version 48.0 and later. In API version 49.0 and
later, this object supports reports, criteria-based sharing rules, and history tracking, plus you can exclude individual fields from custom
page layouts.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search() undelete()`, `update()`, `upsert()`

Special Access Rules

To access this object, you must have a Workplace Command Center permission set license and the Provides access to Workplace
Command Center features system permission or have the Employee Management and Employee User add-on licenses.


Standard Objects Employee

Fields

**Field** **Details**

```
AboutMe

AlternateEmail

Availability

AvailabilityEndDate

AvailabilityStartDate

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Information about the employee, such as areas of interest or skills. Values can be provided
on Employee’s profile page. This field is available even if Chatter is disabled.

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The employee’s alternate email address.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The employee’s availability status.

Possible values are:

**•** `In The Office`

**•** `Out Of Office`

**•** `Out Sick`

**•** `PTO`

**•** `Volunteering Time Off`

**•** `Working Remotely`

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The end date of the Employee’s availability, inclusive of the date.

**Type**
dateTime


Standard Objects Employee

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The start date of the Employee’s availability, inclusive of the date.

```
BannerPhotoUrl

CurrentWellnessStatus

DateOfBirth

Email

EmployeeNumber

```

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
Read only. The URL for the employee's banner photo. Available in API v51.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The employee’s current wellness status.

Possible values are:

**•** `Available To Work`

**•** `Remote Work Only`

**•** `Unavailable`

**•** `Unknown`

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The employee’s date of birth.

**Type**
email

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The employee’s email address. This field is unique within your organization.

**Type**
string


Standard Objects Employee

**Field** **Details**

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. The employee's employment ID for the organization they were hired into. This
field is unique within your organization.

```
EmployeeStatus

EmploymentType

FirstName

FullPhotoUrl

```

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The employee's current work status.

Possible values are:

**•** `Active`

**•** `Inactive`

**•** `Leave`

**•** `Terminated`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The employee's full-time or part-time status.

Possible values are:

**•** `Full-Time`

**•** `Part-Time`

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The employee’s first name.

**Type**
url

**Properties**
Filter, Nillable, Sort


Standard Objects Employee

**Field** **Details**

**Description**
Read only. The URL for the employee's profile photo. The URL is updated every time a photo
is uploaded and reflects the most recent photo. If a newer photo has been uploaded, the
URL returned for an older photo isn’t guaranteed to return a photo. Query this field for the
URL of the most recent photo. Available in API v51.0 and later.

```
Gender

HomeAddress

HomeCity

HomeCountry

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The employee’s gender.

Possible values are:

**•** `Female`

**•** `Male`

**•** `Non-Binary / Non-Conforming`

**•** `Other`

**•** `Prefer Not to State`

**•** `Transgender Female`

**•** `Transgender Male`

**Type**
address

**Properties**
Filter, Nillable

**Description**
The employee’s home address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city for the employee’s home address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The county for the employee’s home address.


Standard Objects Employee

**Field** **Details**

```
HomeGeocodeAccuracy

HomeLatitude

HomeLongitude

HomePhone

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The level of accuracy of an employee’s home address geographical coordinates compared
with its physical address. A geocoding service typically provides this value based on the
address’s latitude and longitude coordinates.

Possible values are:

**•** `Address`

**•** `Block`

**•** `City`

**•** `County`

**•** `ExtendedZip`

**•** `NearAddress`

**•** `Neighborhood`

**•** `State`

**•** `Street`

**•** `Unknown`

**•** `Zip`

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with HomeLongitude to specify the precise geolocation of the employee’s home
address. Acceptable values are numbers between –90 and 90 with up to 15 decimal places.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with HomeLatitude to specify the precise geolocation of the employee’s home address.
Acceptable values are numbers between –180 and 180 with up to 15 decimal places.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects Employee

**Field** **Details**

**Description**
The employee’s home phone number.

```
HomePostalCode

HomeState

HomeStreet

IndividualId

InternalOrganizationUnitId

JobProfile

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code for the employee’s home address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The state for the employee’s home address.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street for the employee’s home address.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A reference to the Individual record that this employee is assigned to.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A reference to the InternalOrganizationUnit this employee is assigned to.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects Employee

**Field** **Details**

**Description**
The employee’s job profile at the company.

```
LastName

LastReferencedDate

LastViewedDate

LocationId

ManagerId

MediumPhotoUrl

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The employee’s last name.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced (LastReferencedDate) and not viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A reference to the Location that this employee is assigned to.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A reference to the Employee record of the employee's manager.

**Type**
url


Standard Objects Employee

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
Read only. The URL for the medium-sized employee's profile photo. The URL is updated
every time a photo is uploaded and reflects the most recent photo. If a newer photo has
been uploaded, the URL returned for an older photo isn’t guaranteed to return a photo.
Query this field for the URL of the most recent photo. Available in API v51.0 and later.

```
MiddleName

Name

NameSuffix

OutOfOfficeMessage

OwnerId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The employee’s middle name.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
A compound field of `Employee.FirstName`, `Employee.MiddleName`, and
`Employee.LastName` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The employee’s suffix.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The message portion of the employee availability. This message can provide reasons or
details about the change in availability. The maximum length of this string is 40 characters.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects Employee

**Field** **Details**

**Description**
The ID of the user who currently owns this record. Default value is the user logged in to the
API to perform the create operation.

```
PreferredFirstName

PreferredPronoun

RelatedPersonId

SmallPhotoUrl

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name the employee prefers to be called.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The employee's preferred pronoun.

Possible values are:

**•** `He/Him/His`

**•** `Other/Ask Me`

**•** `She/Her/Hers`

**•** `They/Them/Theirs`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Links an employee to a person account with a unique value. Reserved for future use. Don’t
edit it.

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
Read only. The URL for the small-sized employee's profile photo. The URL is updated every
time a photo is uploaded and reflects the most recent photo. If a newer photo has been
uploaded, the URL returned for an older photo isn’t guaranteed to return a photo. Query this
field for the URL of the most recent photo. Available in API v51.0 and later.


Standard Objects Employee

**Field** **Details**

```
StatusAsOf

StatusEndDate

TimeZone

UserId

WorkPhone

WorkerType

```

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
Required. Start date of the employee’s current status.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Planned end date for the employee’s status.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The time zone which the employee’s work hours fall within.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Lookup field to associate an Employee record with a user in the org. The field is optional and
unique.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The employee's formatted work phone number including country code and extension.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


### Standard Objects Employee2

**Field** **Details**

**Description**
Required. The type of worker for the employee.

Possible values are:

**•** `Alumnus`

**•** `Contractor`

### • Employee

**•** `Intern`

**•** `Temporary`

```
WorkingHoursEnd

WorkingHoursStart

```

Associated Objects

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The end time of the employee’s working hours.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The start time of the employee’s working hours.

This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**EmployeeHistory (API version 49.0)**
History is available for tracked fields of the object.

**EmployeeOwnerSharingRule**

Sharing rules are available for the object.

**EmployeesShare (API version 49.0)**
Sharing is available for the object.

SEE ALSO:

_[Workplace Command Center for Work.com Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.workdotcom_dev_guide.meta/workdotcom_dev_guide/wdc_cc_dev_workplace_cc_solution.htm)_ : Extend Work.com with Custom Solutions

### Employee2

Represents an employee within a company or an organization. This object is available in API version 62.0 and later.


Standard Objects Employee2

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available if Talent Recruitment Management is enabled in your org. It’s also available to customers who purchase the
Unified Employee license.To access the object, you need one of these permission sets.

**User Type** **Permission Set**

Internal Users HR Service Workspace Personnel

Salesforce Platform Users
Employee Hub Community User

OR

Unified Employee Permission Set

OR

Work.com License

Unified Employee Users Unified Employee Permission Set

Fields

**Field** **Details**

```
AlternateEmail

ContactId

```

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The employee’s alternate email address.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The contact associated with the employee.

**Relationship Name**
Contact


Standard Objects Employee2

**Field** **Details**

**Relationship Type**
Master-detail

**Refers To**
Contact (the master object)

```
CurrencyIsoCode

EmployeeNumber

EmployeeStatus

EmployeeType

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The ISO currency code for the post-authorization request.

Valid value is:

**•** `USD` —U.S. Dollar

The default value is `USD` .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The employee's unique ID for their organization.

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The employee's current work status.

Valid values are:

**•** `Active`

**•** `Inactive`

**•** `Leave`

**•** `Terminated`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The employee's full-time or part-time status.


Standard Objects Employee2

**Field** **Details**

Valid values are:

**•** `Alumnus`

**•** `Contractor`

**•** `Permanent`

**•** `Intern`

**•** `Temporary`

```
EmploymentType

InternalOrganizationUnitId

LastReferencedDate

LastViewedDate

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The employee's full-time or part-time status.

Valid values are:

**•** `Full-Time`

**•** `Part-Time`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The internal organization unit associated with the employee.

**Relationship Name**
InternalOrganizationUnit

**Refers To**
InternalOrganizationUnit

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects Employee2

**Field** **Details**

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that the user only accessed the record or a related list view
( `LastReferencedDate` ), but not viewed the record itself.

```
Name

StatusEndDate

StatusStartDate

User

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the employee record.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The planned end date for the employee’s status.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The start date of the employee’s current status.

**Type**
reference

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The user associated with the employee. After this field is set to a non-null value, you can’t
update it.

**Relationship Name**
User

**Description**
User


### Standard Objects EmployeeCrisisAssessment EmployeeCrisisAssessment

Represents a crisis assessment of an Employee. This object is available in API version 48.0 and later. In API version 49.0 and later, this
object supports reports, criteria-based sharing rules, and history tracking, plus you can exclude individual fields from custom page layouts.

For Work.com, when an employee responds to a wellness survey, an EmployeeCrisisAssessment record is created based on an employee's
answers.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

To access this object, you must be assigned a Workplace Command Center permission set license and the Provides access to Workplace
Command Center features system permission.

Fields

**Field** **Details**

```
Assessment

AssessmentDate

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The employee’s COVID-19 status at the time of the assessment.

Possible values are:

**•** `COVID-19 Immune or Recovered`

**•** `COVID-19 No Symptoms`

**•** `COVID-19 Symptoms or Exposed`

**•** `COVID-19 Test Negative`

**•** `COVID-19 Test Positive`

**•** `Declined`

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date of the assessment. Required


Standard Objects EmployeeCrisisAssessment

**Field** **Details**

```
AssessmentNumber

CrisisId

EmployeeId

LastReferencedDate

LastViewedDate

OwnerId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The assessment record number.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Crisis that this assessment is associated with.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The Employee that this assessment is associated with.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced (LastReferencedDate) and not viewed.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


### Standard Objects EmpUserProvisioningProcess

**Field** **Details**

**Description**
The ID of the user who currently owns this record. Default value is the user logged in to the
API to perform the create operation.

```
SourceAssessment

SourceSystem

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The record in the source system that drove this assessment.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The source system that drove this assessment.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**EmployeeCrisisAssessmentHistory (API version 49.0)**
History is available for tracked fields of the object.

**EmployeeCrisisAssessmentOwnerSharingRule**

Sharing rules are available for the object.

**EmployeeCrisisAssessmentShare (API version 49.0)**
Sharing is available for the object.

SEE ALSO:

_[Workplace Command Center for Work.com Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.ajax.meta/workdotcom_dev_guide/wdc_cc_overview.htm)_ : Extend Work.com with Custom Solutions

### EmpUserProvisioningProcess

Represents an employee-user provisioning process. This object is available in API version 52.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`


Standard Objects EmpUserProvisioningProcess

Special Access Rules

This object requires a Workplace Command Center add-on license, or an Employee Experience add-on license.

Fields

**Field** **Details**

```
EndTime

ErrorRecordCount

LastReferencedDate

LastViewedDate

Name

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time that the user provisioning process ended.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of records that encountered an error during the user provisioning process.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the user provisioning process was last referenced, with a precision
of one second.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the user provisioning process was last viewed, with a precision of
one second.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the user provisioning process.


Standard Objects EmpUserProvisioningProcess

**Field** **Details**

```
ProcessStatus

StartTime

SuccessRecordCount

TotalRecordCount

```

Usage

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the user provisioning process.

Possible values are:

**•** `Aborted`

**•** `Cancelled`

**•** `Failed`

**•** `Finished`

**•** `Initializing`

**•** `Processing`

**•** `Queued`

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time that the user provisioning process started.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of records that were successfully provisioned during the user provisioning
process.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The total number of records in the user provisioning process.

Use the EmpUserProvisioningProcess to view the status of an employee-user provisioning process.


### Standard Objects EmpUserProvisionProcessErr EmpUserProvisionProcessErr

Represents an employee-user provisioning process error. This object is available in API version 52.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object requires a Workplace Command Center add-on license, or an Employee Experience add-on license.

Fields

**Field** **Details**

```
AccountId

EmployeeId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Person Account linked to the employee record associated with the error.

This is a relationship field.

**Relationship Name**
Account

**Refers To**
Account

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the employee record associated with the error.

This is a relationship field.

**Relationship Name**
Employee

**Relationship Type**
Lookup

**Refers To**
Employee


Standard Objects EmpUserProvisionProcessErr

**Field** **Details**

```
ErrorCode

ErrorMessage

LastReferencedDate

LastViewedDate

Name

ProvisioningProcessId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The error code if the provisioning isn’t successful.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If an error occurred, this field contains the error message.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the error was last referenced, with a precision of one second.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the error was last viewed, with a precision of one second.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the error.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the associated user provisioning process.


### Standard Objects EnablementMeasureDefinition

**Field** **Details**

This is a relationship field.

**Relationship Name**
ProvisioningProcess

**Relationship Type**
Lookup

**Refers To**
EmpUserProvisioningProcess

Usage

Use the EmpUserProvisionProcessErr to view the errors for an employee-user provisioning process.

### EnablementMeasureDefinition

Represents an Enablement measure, which specifies the job-related activity that a user performs to complete a milestone or outcome
in an Enablement program. A measure identifies a source object and optional related objects, with optional field filters and filter logic,
for tracking the activity. This object also represents Enablement measure information in Metadata API. This object is available in API
version 56.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To access this object, the Design and Deliver Enablement Programs permission is required. This permission is enabled by default as part
of the Manage Enablement Essentials permission set, which comes with the Enablement add-on license.

Fields

**Field** **Details**

```
AggregateFieldApiName

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The unique name in the API for the field that the `AggregateFunction` uses for
calculating.


Standard Objects EnablementMeasureDefinition

**Field** **Details**

For example, if you’re measuring how much revenue a sales rep has won, the value of
`aggregateFunction` is `Sum` and the value of `aggregateFieldApiName` is
`Amount`, which is the API name of the Amount field on the Opportunity object.

```
AggregateFunction

Description

DeveloperName

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The method for calculating progress towards the milestone or outcome from records that
qualify for the measure’s criteria.

Possible values are:

**•** `Average`

**•** `Count`

**•** `Sum`

For example, if you’re measuring the number of deals won, the function is `Count` .

If the function is `Average` or `Sum`, then `AggregateFieldApiName` specifies the
API name of the field to use for calculating progress.

**Type**
string

**Properties**
Create, Filter, Sort, Update

**Description**
An internal description for the measure to help Enablement admins understand the activity
that’s tracked.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. The name:

**•** must be 40 characters or fewer

**•** must begin with a letter

**•** can contain only underscores and alphanumeric characters

**•** can’t include spaces

**•** can’t end with an underscore

**•** can’t contain 2 consecutive underscores


Standard Objects EnablementMeasureDefinition

**Field** **Details**

In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

```
DisplayFieldApiName

IsValid

Language

MasterLabel

```

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The unique name in the API for the field that primarily identifies records that qualify for the
activity you’re measuring. For example, if you’re measuring the number of deals won, you’re
tracking the Opportunity object, and maybe you want to identify opportunities by their
name. In this case, this field can be `Name`, the API name of the Opportunity Name field on
the Opportunity object.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether the measure is valid. A measure becomes invalid and stops tracking
progress under these circumstances:

**•** An object or field is removed.

**•** An object label or API name is renamed.

**•** A field’s API name is renamed.

Default is `false` . A measure only becomes invalid after a breaking change is saved the
[corresponding outcome or milestone progress is calculated. See Considerations for Creating](https://help.salesforce.com/s/articleView?id=sales.enablement_measures_considerations.htm&type=5&language=en_US)
[and Editing Measures.](https://help.salesforce.com/s/articleView?id=sales.enablement_measures_considerations.htm&type=5&language=en_US)

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Reserved for future use. Don’t edit this field.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


Standard Objects EnablementMeasureDefinition

**Field** **Details**

**Description**
Label for this EnablementMeasureDefinition value. This display value is the internal label that
doesn't get translated.

```
NamespacePrefix

PublishedDateTime

SourceMeasureObjectId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can
refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that aren’t Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

Available in API version 62.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the measure was activated for use in Enablement programs.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the EnblMeasureObjectDefinition that specifies the criteria for the source object
that tracks the activity you're measuring. This field is a relationship field.

**Relationship Name**
SourceMeasureObject

**Relationship Type**
Lookup


### Standard Objects EnablementProgram

**Field** **Details**

**Refers To**
EnblMeasureObjectDefinition

```
SourceObjectApiName

Status

```

Usage

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The unique name in the API for the source object that tracks the activity you're measuring.
This value is a derived value. For example, if you're measuring the number of deals won, this
value is `Opportunity`, the API name for the Opportunity object.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The availability of the measure for use in Enablement programs.

Possible values are:

**•** `Archived` —Available in API versions 56.0 to 60.0.

**•** `Draft` —The measure is saved, but not activated for use in programs.

**•** `Published` —The measure is activated for use in programs. In Lightning Experience,
this value is Active.

An EnablementMeasureDefinition can have multiple EnblMeasureObjectDefinition references, depending on the number of related
objects in the measure. Consider an example measure that tracks activity on the Opportunity source object and the Account related
object.

**•** The EnablementMeasureDefinition identifies the Opportunity source object.

**•** An EnblMeasureObjectDefinition specifies the criteria on the Opportunity source object.

**•** An EnblMeasureObjectDefinition specifies the criteria on the Account related object.

### EnablementProgram

Represents an Enablement program, which includes exercises and measurable milestones to help users such as sales reps achieve specific
outcomes related to your company’s revenue goals. This object is available in API version 56.0 and later.


Standard Objects EnablementProgram

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

**•** For Enablement admins to create, update, and delete Enablement programs, the Design and Deliver Enablement Programs permission
is required. This permission is enabled by default as part of the Manage Enablement Essentials permission set, which comes with
the Enablement add-on license.

**•** For users who take Enablement programs, the Take Enablement Programs permission is required. This permission is enabled by
default as part of the Use Enablement Programs permission set, which comes with the Enablement add-on license.

**•** For partner users who take Partner Enablement programs, the Take Partner Enablement Programs permission is required. This
permission is enabled by default as part of the Use Partner Enablement Programs permission set, which comes with the Enablement
[add-on license. Partner Enablement also requires a supported Partner Relationship Management (PRM) add-on license.](https://help.salesforce.com/s/articleView?id=slack.prm_support_license_template.htm&type=5&language=en_US)

Fields

**Field** **Details**

```
Description

DoesAllowSelfEnrollment

EnablementProgramDefinitionId

```

**Type**
textarea

**Properties**
Create, Update

**Description**

A summary of the program’s goals and content that’s visible to users.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether users can self-enroll in programs that are shared with them ( `true` ) or
take only assigned programs ( `false` ). The default value is `false` .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The representation for the program in Metadata API. This field is a relationship field.

Available in API version 61.0 and later.

**Relationship Name**
EnablementProgramDefinition


Standard Objects EnablementProgram

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
EnablementProgramDefinition

```
IsOutcomeBased

LastReferencedDate

LastViewedDate

Name

NetworkId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the program includes a final, measurable outcome ( `true` ) or not ( `false` ).
The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for example, through
a list view or related record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record. If this value is null, maybe the
user accessed this record ( `LastReferencedDate` ) but not viewed it yet.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the program that’s visible to users. For example, `AE Onboarding`, `Event`
`Prep`, or `New Product Launch` .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects EnablementProgram

**Field** **Details**

**Description**
The ID of the supported Experience Cloud site where a partner program is available. For site
[requirements, see Considerations for Partner Enablement Programs.](https://help.salesforce.com/s/articleView?id=sales.enablement_partner_considerations.htm&type=5&language=en_US)

Available in API version 60.0 and later.

**Relationship Name**
Network

**Relationship Type**
Lookup

**Refers To**
Network

```
OwnerId

PublishedDateTime

Status

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of the program. This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the program is published.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The status of the program. Only a published program is available for an Enablement admin
to assign to users or share with users so they can self-enroll.

Possible values are:

**•** `Archived`

**•** `Draft`


Standard Objects EnablementProgram

**Field** **Details**

**•** `Published`

```
TotalAssigned

TotalBehind

TotalCompleted

TotalDays

Type

```

**Type**
int

**Properties**
Nillable

**Description**
The number of assignments in this program. For example, if the program is assigned to 3
users, then `TotalAssigned=3` .

**Type**
int

**Properties**
Nillable

**Description**
The number of assignments that are behind in this program. For example, if the program is
assigned to 3 users, and 2 users are behind on their assignments, then `TotalBehind=2`

**Type**
int

**Properties**
Nillable

**Description**
The number of completed assignments in this program. For example, if the program is
assigned to 3 users, and 1 user has completed the program, then `TotalCompleted=1` .

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Total days of the program. This value is derived from the latest day of all items in the program,
including exercises, milestones, and the outcome. This field is a calculated field. For example,
a program has Task A on day 1 and Task B on day 2. Since Task B has the latest days of all
tasks, then `TotalDays=2` .

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of the program. Possible values are:


### Standard Objects EnablementProgramDefinition

**Field** **Details**

### • Enablement —A sales program in Lightning Experience.

**•** `PtnrEnablement` —A partner program in a supported Experience Cloud site. Available
in API version 60.0 and later.

**•** `EmployeeServiceEnablement` —An employee enablement program in Employee
Portal. Available in API version 63.0 and later.

Associated Objects

This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**EnablementProgramOwnerSharingRule (API version 60.0)**
Sharing rules are available for the object.

**EnablementProgramShare (API version 60.0)**
Sharing is available for the object.

### EnablementProgramDefinition

Represents Enablement program information in Metadata API. This object is available in API version 61.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

To access this object, the Design and Deliver Enablement Programs permission is required. This permission is enabled by default as part
of the Manage Enablement Essentials permission set, which comes with the Enablement add-on license.

Fields

**Field** **Details**

```
DeveloperName

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique name of the object in the API. The name:

**•** must be 40 characters or fewer


Standard Objects EnablementProgramDefinition

**Field** **Details**

**•** must begin with a letter

**•** can contain only underscores and alphanumeric characters

**•** can’t include spaces

**•** can’t end with an underscore

**•** can’t contain 2 consecutive underscores

In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

```
EnablementProgramId

Language

MasterLabel

NamespacePrefix

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Enablement program to reference in Metadata API.

This field is a relationship field.

**Relationship Name**
EnablementProgram

**Relationship Type**
Lookup

**Refers To**
EnablementProgram

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Reserved for future use. Don’t edit this field.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Label for this EnablementProgramDefinition value. This display value is the internal label
that doesn't get translated.

**Type**
string


### Standard Objects EnblMeasureObjectDefinition

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can
refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that aren’t Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

Available in API version 62.0 and later.

### EnblMeasureObjectDefinition

Represents the criteria for an object that tracks the job-related activity for an Enablement measure in an Enablement program. A separate
### EnblMeasureObjectDefinition is used for a measure's source object and each optional related object. This object is available in API version

56.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To access this object, the Design and Deliver Enablement Programs permission is required. This permission is enabled by default as part
of the Manage Enablement Essentials permission set, which comes with the Enablement add-on license.

Fields

**Field** **Details**

```
DeveloperName

```

**Type**
string


Standard Objects EnblMeasureObjectDefinition

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. The name:

**•** must be 40 characters or fewer

**•** must begin with a letter

**•** can contain only underscores and alphanumeric characters

**•** can’t include spaces

**•** can’t end with an underscore

**•** can’t contain 2 consecutive underscores

In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

```
EnablementMeasureDefinitionId

FilterLogic

Language

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The measure that the EnblMeasureObjectDefinition applies to. This field is a relationship
field.

**Relationship Name**
EnablementMeasureDefinition

**Relationship Type**
Lookup

**Refers To**
EnablementMeasureDefinition

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An expression that determines how to evaluate the optional field filters for the object.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Reserved for future use. Don’t edit this field.


Standard Objects EnblMeasureObjectDefinition

**Field** **Details**

```
MasterLabel

NamespacePrefix

ObjectApiName

SequenceNumber

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label for the EnblMeasureObjectDefinition value. This display value is the internal label that
doesn't get translated.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can
refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that aren’t Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

Available in API version 62.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The unique name in the API for the measure's source object or optional related object that
the EnblMeasureObjectDefinition describes.

For example, if you're measuring the number of deals won for a specific product, this field
on one EnblMeasureObjectDefinition references the API name of the Opportunity source
object and this field on another EnblMeasureObjectDefinition references the API name of
the Opportunity Product related object.

**Type**
int


### Standard Objects EnblPgmTaskMeasureProgress

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
A number that specifies the order of the EnblMeasureObjectDefinition, relative to other
EnblMeasureObjectDefinition records under the same EnablementMeasureDefinition, starting
at 1.

Usage

An EnablementMeasureDefinition can have multiple EnblMeasureObjectDefinition references, depending on the number of related
objects in the measure. Consider an example measure that tracks activity on the Opportunity source object and the Account related
object.

**•** The EnablementMeasureDefinition identifies the Opportunity source object.

**•** An EnblMeasureObjectDefinition specifies the criteria on the Opportunity source object.

**•** An EnblMeasureObjectDefinition specifies the criteria on the Account related object.

### EnblPgmTaskMeasureProgress

Represents a user’s progress through the object and field requirements that an Enablement measure defines for an outcome or milestone
in an Enablement program. This object is available in API version 61.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

**•** For Enablement admins to create, update, and delete Enablement programs, the Design and Deliver Enablement Programs permission
is required. This permission is enabled by default as part of the Manage Enablement Essentials permission set, which comes with
the Enablement add-on license.

**•** For users who take Enablement programs, the Take Enablement Programs permission is required. This permission is enabled by
default as part of the Use Enablement Programs permission set, which comes with the Enablement add-on license.

**•** For partner users who take Partner Enablement programs, the Take Partner Enablement Programs permission is required. This
permission is enabled by default as part of the Use Partner Enablement Programs permission set, which comes with the Enablement
[add-on license. Partner Enablement also requires a supported Partner Relationship Management (PRM) add-on license.](https://help.salesforce.com/s/articleView?id=slack.prm_support_license_template.htm&type=5&language=en_US)


Standard Objects EnblPgmTaskMeasureProgress

Fields

**Field** **Details**

```
ContributingRecordCount

EnblProgramTaskMeasureId

EnblProgramTaskProgressId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of records that qualify for a user’s progress towards completing an outcome or
milestone. To qualify, the activity must meet the criteria that the corresponding Enablement
measure defines for specific objects, fields, and field values.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the record that represents the connection between a specific Enablement measure
and a specific milestone or outcome in an Enablement program.

This field is a relationship field.

**Relationship Name**
EnblProgramTaskMeasure

**Relationship Type**
Lookup

**Refers To**
EnblProgramTaskMeasure

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the record that represents the progress through the milestone or outcome.

This field is a relationship field.

**Relationship Name**
EnblProgramTaskProgress

**Relationship Type**
Master-detail

**Refers To**
EnblProgramTaskProgress (the master object)


### Standard Objects EnblProgramSection

**Field** **Details**

```
MeasureComputationResult

```

**Type**
double

**Properties**
Filter, Sort

**Description**
The calculated progress through the measure’s requirements for a milestone or outcome.
For example, if the measure is the dollar amount of all closed opportunities, then the field
value is measured in dollars.

For a composite milestone or a composite outcome, this value represents the progress
through only one measure associated with the milestone or outcome.

### EnblProgramSection

Represents an optional section in an Enablement program. A section can include other program items, such as milestones and exercises.
This object is available in API version 60.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

**•** For Enablement admins to create, update, and delete Enablement programs, the Design and Deliver Enablement Programs permission
is required. This permission is enabled by default as part of the Manage Enablement Essentials permission set, which comes with
the Enablement add-on license.

**•** For users who take Enablement programs, the Take Enablement Programs permission is required. This permission is enabled by
default as part of the Use Enablement Programs permission set, which comes with the Enablement add-on license.

**•** For partner users who take Partner Enablement programs, the Take Partner Enablement Programs permission is required. This
permission is enabled by default as part of the Use Partner Enablement Programs permission set, which comes with the Enablement
[add-on license. Partner Enablement also requires a supported Partner Relationship Management (PRM) add-on license.](https://help.salesforce.com/s/articleView?id=slack.prm_support_license_template.htm&type=5&language=en_US)

Fields

**Field** **Details**

```
DeveloperName

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique name of the object in the API. The name:


Standard Objects EnblProgramSection

**Field** **Details**

**•** must be 40 characters or fewer

**•** must begin with a letter

**•** can contain only underscores and alphanumeric characters

**•** can’t include spaces

**•** can’t end with an underscore

**•** can’t contain 2 consecutive underscores

In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

Available in API version 61.0 and later.

```
EnablementProgramId

Name

SequenceNumber

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The Enablement program that contains the section. This field is a relationship field.

**Relationship Name**
EnablementProgram

**Relationship Type**
Lookup

**Refers To**
EnablementProgram

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The title of the section that’s visible to users when they take the program.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
A number that specifies the order of the section, relative to other sections, starting at 0.


### Standard Objects EnblProgramTaskDefinition EnblProgramTaskDefinition

Represents an outcome, a milestone, or an exercise in an Enablement program. A program task is also known as a program item. This
object is available in API version 60.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

**•** For Enablement admins to create, update, and delete Enablement programs, the Design and Deliver Enablement Programs permission
is required. This permission is enabled by default as part of the Manage Enablement Essentials permission set, which comes with
the Enablement add-on license.

**•** For users who take Enablement programs, the Take Enablement Programs permission is required. This permission is enabled by
default as part of the Use Enablement Programs permission set, which comes with the Enablement add-on license.

**•** For partner users who take Partner Enablement programs, the Take Partner Enablement Programs permission is required. This
permission is enabled by default as part of the Use Partner Enablement Programs permission set, which comes with the Enablement
[add-on license. Partner Enablement also requires a supported Partner Relationship Management (PRM) add-on license.](https://help.salesforce.com/s/articleView?id=slack.prm_support_license_template.htm&type=5&language=en_US)

Fields

**Field** **Details**

```
CompositeMilestoneType

CustomEnblPgmTaskSubCategoryId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of logic to use for evaluating the activity from two Enablement measures in a
composite milestone.

Possible values are:

**•** `Addition`

**•** `Division`

**•** `Percentage`

Available in API version 61.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects EnblProgramTaskDefinition

**Field** **Details**

**Description**
The ID of the EnblProgramTaskSubCategory record associated with a custom exercise type.
This field is required when the `TaskSubCategory` field’s value is `CustomExercise` .

This field is a relationship field.

Available in API version 62.0 and later.

**Relationship Name**
CustomEnblPgmTaskSubCategory

**Relationship Type**
Lookup

**Refers To**
EnblProgramTaskSubCategory

```
Day

Description

EnablementProgramId

```

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The day of the program when the item is due, relative to the program's start date. For example,
if a user is expected to complete an exercise where they watch a product demo by day 2,
this field’s value is 2. For an outcome, this field specifies the number of days the full program
takes. For example, if your program lasts 60 days, the value of this field is 60 for the outcome.
This field’s value contributes to the program’s due date that users see when they take the
program.

**Type**
textarea

**Properties**
Create

**Description**
A summary of the outcome, milestone, or exercise that’s visible to users when they take the
program.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the Enablement program that contains the outcome, milestone, or exercise. This
field is a relationship field.

**Relationship Name**
EnablementProgram


Standard Objects EnblProgramTaskDefinition

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
EnablementProgram

```
EnblProgramSectionId

IsMilestoneAnOutcome

LearningItemId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of an optional program section that contains the milestone or exercise. This field is a
relationship field.

**Relationship Name**
EnblProgramSection

**Relationship Type**
Lookup

**Refers To**
EnblProgramSection

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the program item is the program’s final outcome ( `true` ) or an incremental
milestone ( `false` ). The default value is `false` .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the learning item record for the outcome, milestone, or exercise. This field is a
relationship field.

**Relationship Name**
LearningItem

**Relationship Type**
Lookup

**Refers To**
LearningItem


Standard Objects EnblProgramTaskDefinition

**Field** **Details**

```
MilestoneTarget

MinimumSampleSize

Name

SequenceNumber

StandardCustomExerciseType

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The target value for a user to achieve to get credit for completing the outcome or milestone.
The unit depends on the specific measure used with the outcome or milestone. For example,
if the measure is the dollar amount of all closed opportunities, then the field value is measured
in dollars.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of records to evaluate when calculating progress for an outcome or milestone
that uses an average-based measure. Use this field with `MilestoneTarget` . For example,
if you want users to achieve an average deal size of $50,000 after closing 4 deals, then this
field’s value is `4` and `MilestoneTarget` is `50000` .

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The title of the outcome, milestone, or exercise that’s visible to users when they take the
program.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
A number that specifies the order of the milestone or exercise, relative to other milestones
or exercises that have the same due date in the program or in the same section, starting at
0. This number determines the order of items that users see for that day in the program.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


### Standard Objects EnblProgramTaskMeasure

**Field** **Details**

**Description**
Reserved for future use.

```
TaskCategory

TaskSubCategory

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of program item. Possible values are:

**•** `Exercise`

**•** `Milestone`

`Milestone` is used for both the program’s final outcome and incremental milestones.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of exercise. This value determines the content associated with the exercise. For
example, if the field value is `Video`, the exercise must reference video content from the
Enablement workspace in the Digital Experiences app. The `LearningItemId` field
specifies the reference to that video content. Possible values are:

**•** `ActionItem`

**•** `AudioRecording`

**•** `CustomExercise` —Available in API version 62.0 and later.

**•** `Document`

**•** `FeedbackRequest`

**•** `Other`

**•** `OtherExercise`

**•** `ScheduledEvent`

**•** `StandardCustomExercise` —Reserved for future use.

**•** `TextLesson`

**•** `Trailhead`

**•** `Video`

### EnblProgramTaskMeasure

Represents the connection between an Enablement measure and a specific milestone or outcome in an Enablement program. This
object is available in API version 61.0 and later.


Standard Objects EnblProgramTaskMeasure

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

To access this object, the Design and Deliver Enablement Programs permission is required. This permission is enabled by default as part
of the Manage Enablement Essentials permission set, which comes with the Enablement add-on license.

Fields

**Field** **Details**

```
EnablementMeasureDefinitionId

EnblProgramTaskDefinitionId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the Enablement measure to use with a milestone or outcome.

This field is a relationship field.

**Relationship Name**
EnablementMeasureDefinition

**Relationship Type**
Lookup

**Refers To**
EnablementMeasureDefinition

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the outcome or milestone that uses the Enablement measure.

This field is a relationship field.

**Relationship Name**
EnblProgramTaskDefinition

**Relationship Type**
Master-detail

**Refers To**
EnblProgramTaskDefinition (the master object)


### Standard Objects EnblProgramTaskProgress

**Field** **Details**

```
SequenceNumber

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
A number that specifies the order of the Enablement measure when multiple measures are
used with one outcome or milestone, starting at 0. For example, in a composite milestone
that uses the Percentage function, the measure that provides the numerator value is sequence
0 and the measure that provides the denominator value is sequence 1.

### EnblProgramTaskProgress

Represents a user’s progress towards completing an outcome, a milestone, or an exercise in an Enablement program. This object is
available in API version 60.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

**•** For Enablement admins to create, update, and delete Enablement programs, the Design and Deliver Enablement Programs permission
is required. This permission is enabled by default as part of the Manage Enablement Essentials permission set, which comes with
the Enablement add-on license.

**•** For users who take Enablement programs, the Take Enablement Programs permission is required. This permission is enabled by
default as part of the Use Enablement Programs permission set, which comes with the Enablement add-on license.

**•** For partner users who take Partner Enablement programs, the Take Partner Enablement Programs permission is required. This
permission is enabled by default as part of the Use Partner Enablement Programs permission set, which comes with the Enablement
[add-on license. Partner Enablement also requires a supported Partner Relationship Management (PRM) add-on license.](https://help.salesforce.com/s/articleView?id=slack.prm_support_license_template.htm&type=5&language=en_US)

Fields

**Field** **Details**

```
CompletedDateTime

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the user completed the outcome, milestone, or exercise.


Standard Objects EnblProgramTaskProgress

**Field** **Details**

```
CompletedOnDay

CompletedPercent

ContributingRecordCount

DueDate

EnblProgramTaskDefinitionId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of days that the user took to complete the outcome, milestone, or exercise.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
Percentage of the outcome, milestone, or exercise that’s complete.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of records that qualify for a user’s progress towards completing an outcome or
milestone. To qualify, the activity must meet the criteria that the corresponding Enablement
measure defines for specific objects, fields, and field values.

Available in API version 61.0 and later.

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
The date the outcome, milestone, or exercise is due.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the outcome, milestone, or exercise definition. This field is a relationship field.

**Relationship Name**
EnblProgramTaskDefinition

**Relationship Type**
Lookup


Standard Objects EnblProgramTaskProgress

**Field** **Details**

**Refers To**
EnblProgramTaskDefinition

```
IsCompleted

IsNoLongerTracking

LearningItemProgressId

MilestoneComputationResult

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Whether the outcome, milestone, or exercise is complete ( `true` ) or not ( `false` ). The
default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If the user hasn’t completed the outcome or milestone and 30 days have elapsed since the
program’s due date, the value is `true` . Otherwise, the value is `false` . The default value
is `false` [. For details, see Completion Statuses in Enablement Analytics.](https://help.salesforce.com/s/articleView?id=sales.enablement_analytics_completion_statuses.htm&type=5&language=en_US)

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the record that tracks the user's progress through the program that includes this
outcome, milestone, or exercise. This field is a relationship field.

**Relationship Name**
LearningItemProgress

**Relationship Type**
Lookup

**Refers To**
LearningItemProgress

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Derived from the associated EnblProgramTaskDefinition record. For example, if a milestone
has a single measure A with a result of 5, this field’s value is 5.


### Standard Objects EnblProgramTaskSubCategory

**Field** **Details**

```
ProgressStatus

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Status of the outcome, milestone, or exercise progress. Possible values are:

**•** `Behind`

**•** `Completed Late`

**•** `Completed On Time`

**•** `No Longer Tracking`

**•** `Not Completed`

**•** `Overdue`

[For details, see Completion Statuses in Enablement Analytics.](https://help.salesforce.com/s/articleView?id=sales.enablement_analytics_completion_statuses.htm&type=5&language=en_US)

### EnblProgramTaskSubCategory

Represents a custom exercise type that an Enablement admin adds to an Enablement program in Program Builder. A custom exercise
type also requires a corresponding EnblProgramTaskDefinition record for Program Builder and corresponding LearningItem and
LearningItemType records for when users take the exercise in the Guidance Center. This object is available in API version 62.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

**•** For Enablement admins to create, update, and delete Enablement programs, the Design and Deliver Enablement Programs permission
is required. This permission is enabled by default as part of the Manage Enablement Essentials permission set, which comes with
the Enablement add-on license.

**•** For users who take Enablement programs, the Take Enablement Programs permission is required. This permission is enabled by
default as part of the Use Enablement Programs permission set, which comes with the Enablement add-on license.

Important: Custom exercises aren’t compatible with Partner Enablement programs.

Fields

**Field** **Details**

```
DeveloperName

```

**Type**
string


Standard Objects EnblProgramTaskSubCategory

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. The name:

**•** must be 40 characters or fewer

**•** must begin with a letter

**•** can contain only underscores and alphanumeric characters

**•** can’t include spaces

**•** can’t end with an underscore

**•** can’t contain 2 consecutive underscores

In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

```
Icon

Language

LearningItemTypeId

```

**Type**
textarea

**Properties**
Create, Update

**Description**
The icon to use for the custom exercise type in Program Builder.

Use the format _**`iconType`**_ `:` _**`iconName`**_, where the values correspond to icon categories
[and names from the Salesforce Lightning Design System.](https://www.lightningdesignsystem.com/icons/)

**•** _**`iconType`**_ is the type of icon, such as `standard` or `doctype` .

**•** _**`iconName`**_ is the icon name, such as `flow` or `slide` .

For example, to use the Standard type Flow icon, this value is `standard:flow` . For details,
[see Implement Custom Exercise Types for Enablement Programs in the](https://developer.salesforce.com/docs/sales/enablement/guide/enablement-custom-exercises-intro.html) _Sales Programs and_
_Partner Tracks with Enablement Developer Guide_ .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Reserved for future use. Don’t edit this field.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update


### Standard Objects EngagementChannelType

**Field** **Details**

**Description**
The ID of the learning item type record that represents this custom exercise type in the
Guidance Center when users take a program.

This field is a relationship field.

**Relationship Name**
LearningItemType

**Refers To**
LearningItemType

```
MasterLabel

NamespacePrefix

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label for this EnblProgramTaskSubCategory value. This display value is the internal label that
doesn't get translated.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can
refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that aren’t Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

### EngagementChannelType

Represents a channel through which a customer can be reached for communication. This object is available in API version 48.0 and later.


Standard Objects EngagementChannelType

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ContactPointType

LastReferencedDate

LastViewedDate

Name

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The contact point type of the channel.

Possible values are:

**•** `Email`

**•** `MailingAddress`

**•** `Phone`

**•** `Social`

**•** `Web`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced ( `LastReferencedDate` ) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Name of the communication subscription consent record.


### Standard Objects EngagementSignal

**Field** **Details**

```
 OwnerId

```

Associated Objects

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the account owner associated with this customer.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**EngagementChannelTypeChangeEvent (API version 61.0)**
Change events are available for the object.

**EngagementChannelTypeFeed**

Feed tracking is available for the object.

**EngagementChannelTypeHistory**

History is available for tracked fields of the object.

**EngagementChannelTypeOwnerSharingRule**

Sharing rules are available for the object.

**EngagementChannelTypeShare**

Sharing is available for the object.

### EngagementSignal

Represents data about an individual’s engagement action, such as a web click, an email response, or a PDF download. This object is
available in API version 62.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects EngagementSignal

Fields

**Field** **Details**

```
DataSpaceId

Description

DeveloperName

IsRemote

LastReferencedDate

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Required. Unique identifier that refers to the data space where the engagement signal
originates.

This field is a relationship field.

**Relationship Name**
DataSpace

**Refers To**
DataSpace

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
An optional text description of the engagement signal.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Required. API name for the engagement signal that's system-or user-generated.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates if the engagement signal object is owned by a different org in Data 360.

The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects EngagementSignal

**Field** **Details**

**Description**
Timestamp that indicates the last time the engagement signal was referenced by the current
user.

```
LastViewedDate

Name

Status

```

Usage

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp that indicates the last time the current user viewed the engagement signal record.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Required. Text label that identifies the engagement signal.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Picklist value that indicates the current status of the engagement signal.

Possible values are:

**•** `Active`

**•** `CreateError` —Error

**•** `DeleteError` —Error

**•** `Deleting`

**•** `EditError` —Error

**•** `Preparing`

**•** `Processing`

The default value is `Processing` .

Use this object to define foundational data for your business objectives and recommendations in Salesforce Personalization. Use mapped
data model object (DMO) fields to identify and track an individual’s engagement actions. For example, use data about a web click, an
email response, or a PDF download to help achieve your personalization goals.


### Standard Objects EngagementSignalCmpndMetric EngagementSignalCmpndMetric

Represents a rate metric that measures the ratio between two engagement signal metrics, such as product orders and product views
to calculate a conversion rate, or email clicks and email opens to determine a click-through rate. Use this object to create complex
measurements for A/B testing and web experimentation. This object is available in API version 62.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CompoundMetricFormula

DenomEngmtSignalMetricId

IsRemote

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
A read-only formula field that concatenates the three core components of a Compound
Metric—the primary metric, the operator, and the secondary metric—into a single string.
This field is unique within your Salesforce org.

This field is a calculated field.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Points to the `EngagementSignalMetric` record that serves as the denominator of
the compound metric.

This field is a relationship field.

**Relationship Name**
DenomEngmtSignalMetric

**Refers To**
EngagementSignalMetric

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects EngagementSignalCmpndMetric

**Field** **Details**

**Description**
Indicates if the engagement signal compound metric object is owned by a different org in
Data 360.

The default value is `false` .

```
LastReferencedDate

LastViewedDate

Name

NumerEngmtSignalMetricId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp that indicates the last time the engagement signal compound metric was
referenced by the current user.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp that indicates the last time the current user viewed the engagement signal
compound metric record.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Required. Text label that identifies the engagement signal compound metric.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Points to the `EngagementSignalMetric` record that serves as the numerator of the
compound metric.

This field is a relationship field.

**Relationship Name**
NumerEngmtSignalMetric

**Refers To**
EngagementSignalMetric


Standard Objects EngagementSignalCmpndMetric

**Field** **Details**

```
Operator

OwnerId

```

Usage

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Represents the mathematical operation that combines the numerator and denominator
metrics in the compound metric formula.

Possible values are:

**•** `Ratio`

The default value is `Ratio` .

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Represents the ID of the user or group that owns the engagement signal compound metric.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

Use this object to create rate metrics for A/B testing and web experimentation. To measure the effectiveness of personalization experiences,
divide the numerator metric by the denominator metric. These metrics help you make data-driven decisions to compare content
performance. This object is used for measurement and isn’t used for machine learning model training.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**EngagementSignalCmpndMetricShare on page 67**
Sharing is available for the object.


### Standard Objects EngagementSignalMetric EngagementSignalMetric

Represents a measurable quantity that’s derived from an engagement signal, such as the sum of revenue or a count of clicks. Use this
object to track user engagement for A/B tests, machine learning model training, and attribution configurations. This object is available
in API version 62.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AggregateFunction

EngagementSignalId

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Defines the type of calculation used on the metric field.

Possible values are:

**•** `Avg`

**•** `Count`

**•** `Distinct`

**•** `Select`

**•** `Sum`

The default value is `Count` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. Represents the ID of the engagement signal that’s associated with the metric.

This field is a relationship field.

**Relationship Name**
### EngagementSignal

**Relationship Type**
Master-detail

**Refers To**
EngagementSignal (the master object)


### Standard Objects EnhancedLetterhead

**Field** **Details**

```
IsRemote

LastReferencedDate

LastViewedDate

Name

```

Usage

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates if the engagement signal metric object is owned by a different org in Data 360.

The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp that indicates the last time the engagement signal metric was referenced by the
current user.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp that indicates the last time the current user viewed the engagement signal metric
record.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Required. Text label that identifies the engagement signal metric.

These derived metrics serve as the core unit of measurement across the personalization platform. Use them to train machine learning
models, measure performance in A/B tests, track outcomes in attribution models, and define custom objectives or compound metrics.

### EnhancedLetterhead

Represents an enhanced letterhead that can be associated with a Lightning email template that doesn’t use the Salesforce Merge
Language (SML). This object is available in API version 46.0 and later.


Standard Objects EnhancedLetterhead

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `describeLayout()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
Description

LastReferencedDate

LastViewedDate

LetterheadFooter

LetterheadHeader

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the contents of the header and footer.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when this enhanced letterhead was last used.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when this enhanced letterhead was last viewed.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The contents of the enhanced letterhead’s footer.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The contents of the enhanced letterhead’s header.


### Standard Objects Entitlement

**Field** **Details**

```
Name

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the enhanced letterhead, such as Standard Company Letterhead.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**EnhancedLetterheadFeed**

Feed tracking is available for the object.

### Entitlement

Represents the customer support an account or contact is eligible to receive. This object is available in API version 18.0 and later.
### Entitlements may be based on an asset, product, or service contract.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AccountId

AssetId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the Account associated with the entitlement.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Required. ID of the Asset associated with the entitlement. Must be a valid asset ID.


Standard Objects Entitlement

**Field** **Details**

```
AssetWarrantyID

BusinessHoursId

CasesPerEntitlement

ContractLineItemId

EndDate

IsPerIncident

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The identifier of the asset warranty record. Must be a valid asset warranty ID.
AssetWarranty is available only with Field Service.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Required. ID of the BusinessHours associated with the entitlement. Must be a valid
business hours ID.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of cases the entitlement supports.

This field is only available if `IsPerIncident` is `true` .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Required. ID of the ContractLineItem associated with the entitlement. Must be a valid
ID.

**Type**
date

**Properties**
Create, Filter, Nillable, Update

**Description**
The last day the entitlement is in effect.

**Type**
boolean


Standard Objects Entitlement

**Field** **Details**

**Properties**
Defaulted on create, Filter, Update

**Description**
Indicates whether the entitlement is limited to supporting a specific number of cases
( `true` ) or not ( `false` ).

```
LastReferencedDate

LastViewedDate

LocationID

Name

SvcApptBookingWindowsId

```

**Type**
date

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp when the current user last accessed this record, a record related to
this record, or a list view.

**Type**
date

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp when the current user last viewed this record or list view. If this value
is null, the user might have only accessed this record or list view
( `LastReferencedDate` ) but not viewed it.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Location associated with the entitlement. Must be a valid location ID.

**Type**
string

**Properties**
Create, Filter, Update

**Description**
Required. Name of the entitlement.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Nillable, Update


Standard Objects Entitlement

**Field** **Details**

**Description**
The operating hours that the entitlement’s work orders should respect. The label in
the user interface is `Operating Hours` . Available only if Field Service is enabled.

```
RemainingCases

RemainingWorkOrders

ServiceContractId

SlaProcessId

StartDate

```

**Type**
int

**Properties**
Create, Filter, Nillable, Update

**Description**
The number of cases the entitlement can support. This field decreases in value by
one each time a case is created with the entitlement.

This field is only available if `IsPerIncident` is selected.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of agreed work orders remaining to be created.

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
Required. ID of the ServiceContract associated with the entitlement. Must be a valid
ID.

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
ID of the SlaProcess associated with the entitlement. This field is available in version
19.0 and later.

**Type**
date

**Properties**
Create, Filter, Nillable, Update

**Description**
The first date the entitlement is in effect.


Standard Objects Entitlement

**Field** **Details**

```
Status

SvcApptBookingWindows

Type

WorkOrdersPerEntitlement

```

Associated Objects

**Type**
picklist

**Properties**
Filter, Nillable

**Description**
Status of the entitlement, such as `Expired` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Nillable, Update

**Description**
The operating hours of the entitlement. This field is visible only if Field Service is
enabled.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Nillable, Update

**Description**
The type of entitlement, such as Web or phone support.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Total number of work orders available for this entitlement.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**EntitlementChangeEvent (API version 44.0)**
Change events are available for the object.

**EntitlementFeed (API version 23.0)**
Feed tracking is available for the object.


### Standard Objects EntitlementContact

**EntitlementHistory**

History is available for tracked fields of the object.

SEE ALSO:

### EntitlementContact

SlaProcess

### EntitlementContact

Represents a Contact eligible to receive customer support via an Entitlement. This object is available in API version 18.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,

```
   undelete()

```

Fields

**Field** **Details**

```
ContactId

EntitlementId

IsDeleted

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the Contact associated with the entitlement. Must be a valid ID.

**Type**
reference

**Properties**
Create, Filter

**Description**
Required. ID of the Entitlement associated with the entitlement contact. Must be a
valid ID.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not
( `false` ). Label is **Deleted** .


### Standard Objects EntitlementTemplate

**Field** **Details**

```
Name

```

Usage

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Nillable

**Description**
Required. Name of the entitlement contact.

Use to query and manage entitlement contacts.

SEE ALSO:

### Entitlement EntitlementTemplate

Represents predefined terms of customer support for a product (Product2). This object is available in API version 18.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

As of Summer ’20 and later, only Salesforce admins, users with access to the Case, Entitlement, or Work Order objects, and users with
the View Setup and Configuration permission can access this object.

Fields

**Field** **Details**

```
BusinessHoursId

CasesPerEntitlement

```

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
ID of the BusinessHours associated with the entitlement template. Must be a valid
business hours ID.

**Type**
int


Standard Objects EntitlementTemplate

**Field** **Details**

**Properties**
Create, Filter, Nillable, Update

**Description**
The total number of cases the entitlement template supports.

This field is only available if `IsPerIncident` is `true` .

```
IsPerIncident

Name

NamespacePrefix

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Update

**Description**
Indicates whether the entitlement template is limited to supporting a specific number
of cases ( `true` ) or not ( `false` ).

**Type**
string

**Properties**
Create, Filter, idLookup, Update

**Description**
Required. Name of the entitlement template.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org
that creates a managed package has a unique namespace prefix. Limit: 15 characters.
You can refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix
of the org for all objects that support it, unless an object is in an installed managed
package. In that case, the object has the namespace prefix of the installed
managed package. This field’s value is the namespace prefix of the Developer
Edition org of the package developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set only
for objects that are part of an installed managed package. All other objects have
no namespace prefix.

Available in version 34.0 and later.


### Standard Objects EntityHistory

**Field** **Details**

```
SlaProcessId

Term

Type

```

Usage

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
ID of the SlaProcess associated with the entitlement template. This field is available
in API version 19.0 and later.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Nillable, Update

**Description**
Number of days that the entitlement template is valid.

**Type**
picklist

**Properties**
Create, Filter, Nillable, Update

**Description**
The type of entitlement template, such as Web or phone support.

Use this object to manage entitlement templates.

### EntityHistory

Represents historical information about an object’s changed field values. This object is only available to users with the “View All Data”
[permission. This object is unavailable beginning with API version 8.0. Use the object-specific Historyobjects instead.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.xml)

Supported Calls

`describeSObjects()`, `getUpdated()`, `getDeleted()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)


Standard Objects EntityHistory

Fields

**Field** **Details**

```
FieldName

IsDeleted

NewValue

OldValue

ParentId

ParentSobjectType

```

**Type**
picklist

**Properties**
Filter, Restricted picklist

**Description**
ID of the standard or custom field.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not
( `false` ). Label is **Deleted** .

**Type**
anyType

**Properties**
Nillable

**Description**
New value of the modified field.

**Type**
anyType

**Properties**
Nillable

**Description**
Previous value of the modified field.

**Type**
reference

**Properties**
Filter

**Description**
ID of the object that contains the field.

**Type**
picklist

**Properties**
Filter, Restricted picklist


### Standard Objects EntityMilestone

**Field** **Details**

**Description**
The kind of object that contains the field.

Usage

In API version 7.0 and later, this object works with Case, Contract, and Solution objects:

**•** This object is always read-only in the online application.

**•** When a field is modified, this object records both the old and new field values. There are exceptions to this behavior for certain fields
such as long text areas and multi-select picklists. These fields appear in this object to indicate that the field was changed, but the
old and new values are not recorded.

**•** Two rows are added to this object when foreign key fields change. One row contains the foreign key object names that display in
the online application. For example, “Jane Doe” is recorded as the name of a contact. The other row contains the actual foreign key
ID that is only returned to and visible from the API.

**•** Up to a total of twenty fields (standard or custom) can be tracked for a given object.

**•** In the online application, you can specify which fields are tracked or not tracked at any time.

**•** As soon as tracking is turned on for a field, all changes to its value are recorded in the database.

**•** Turning off tracking for a field stops further changes from being recorded, but the history data is not deleted.

**•** Be advised that deleting a custom field also permanently deletes the history data for that custom field.

### EntityMilestone

Represents a required step in a customer support process on a work order. The Salesforce user interface uses the term “object milestone.
This object is available in API version 37.0 and later.

Note: Milestones on cases use the CaseMilestone object type.

Supported Calls

`delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`,

```
   update()

```

Special Access Rules

**•** As of Summer ’20 and later, only Salesforce admins, users with access to the Case, Entitlement, or Work Order objects, and users with
the View Setup and Configuration permission can access this object.

**•** Entitlement management must be enabled.

**•** Work orders or Field Service must be enabled.


Standard Objects EntityMilestone

Fields

**Field Name** **Details**

```
ActualElapsedTimeInDays

ActualElapsedTimeInHrs

ActualElapsedTimeInMins

BusinessHoursId

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The number of days that it took to complete a milestone. (Elapsed Time) –
(Stopped Time) = (Actual Elapsed Time)

Note: To display this field, select **Enable stopped time and actual**
**elapsed time** on the Entitlement Settings page and add the field to the
object milestone page layout.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The number of hours that it took to complete a milestone. (Elapsed Time) –
(Stopped Time) = (Actual Elapsed Time)

Note: To display this field, select **Enable stopped time and actual**
**elapsed time** on the Entitlement Settings page and add the field to the
object milestone page layout.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of minutes that it took to complete a milestone. (Elapsed Time) –
(Stopped Time) = (Actual Elapsed Time)

Note: To display this field, select **Enable stopped time and actual**
**elapsed time** on the Entitlement Settings page and add the field to the
object milestone page layout.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects EntityMilestone

**Field Name** **Details**

**Description**
The business hours on the milestone. If business hours aren’t specified, the
entitlement process business hours are used. If business hours are also not
specified on the entitlement process, the business hours on the record are used.

```
CompletionDate

CurrencyIsoCode

ElapsedTimeInDays

ElapsedTimeInHrs

ElapsedTimeInMins

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort, Update

**Description**
The date and time the milestone was completed.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The number of days it took to complete a milestone, including time during which
the milestone was stopped. Automatically calculated to include the business
hours on the record. Elapsed time is calculated only after the Completion Date
field is populated. (Elapsed Time) – (Stopped Time) = (Actual Elapsed Time).

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The number of hours it took to complete a milestone, including time during
which the milestone was stopped. Automatically calculated to include the
business hours on the record. Elapsed time is calculated only after the Completion
Date field is populated. (Elapsed Time) – (Stopped Time) = (Actual Elapsed Time).

**Type**
int


Standard Objects EntityMilestone

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of minutes it took to complete a milestone, including time during
which the milestone was stopped. Automatically calculated to include the
business hours on the record. Elapsed time is calculated only after the Completion
Date field is populated. (Elapsed Time) – (Stopped Time) = (Actual Elapsed Time).

```
IsCompleted

IsViolated

MilestoneTypeId

Name

ParentEntityId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Green checkmark icon that indicates a milestone completion.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Red exclamation point icon that indicates a milestone violation.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The ID of the milestone (for instance, First Response).

**Type**
string

**Properties**
Filter, Group, Sort, Update

**Description**
The name of the milestone.

**Type**
reference

**Properties**
Filter, Group, Sort


Standard Objects EntityMilestone

**Field Name** **Details**

**Description**
The ID of the record—for example, a work order—that contains the milestone.

```
SlaProcessId

StartDate

StoppedTimeInDays

StoppedTimeInHrs

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The entitlement process associated with the milestone.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort, Update

**Description**
The date and time that milestone tracking started.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The number of days that an agent has been blocked from completing a milestone.
For example, an agent may be waiting for a customer to reply with more
information.

Note: To display this field, select **Enable stopped time and actual**
**elapsed time** on the Entitlement Settings page and add the field to the
object milestone page layout.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The number of hours that an agent has been blocked from completing a
milestone. For example, an agent may be waiting for a customer to reply with
more information.

Note: To display this field, select **Enable stopped time and actual**
**elapsed time** on the Entitlement Settings page and add the field to the
object milestone page layout.


Standard Objects EntityMilestone

**Field Name** **Details**

```
StoppedTimeInMins

TargetDate

TargetResponseInDays

TargetResponseInHrs

TargetResponseInMins

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of minutes that an agent has been blocked from completing a
milestone. For example, an agent may be waiting for a customer to reply with
more information.

Note: To display this field, select **Enable stopped time and actual**
**elapsed time** on the Entitlement Settings page and add the field to the
object milestone page layout.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time to complete the milestone.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The number of days to complete the milestone. Automatically calculated to
include the business hours on the record.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The number of hours to complete the milestone. Automatically calculated to
include the business hours on the record.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of minutes to complete the milestone. Automatically calculated to
include the business hours on the record.


Standard Objects EntityMilestone

**Field Name** **Details**

```
TimeRemainingInDays

TimeRemainingInHrs

TimeRemainingInMins

TimeSinceTargetInDays

TimeSinceTargetInHrs

TimeSinceTargetInMins

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The days that remain before a milestone violation. Automatically calculated to
include the business hours on the record.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The hours that remain before a milestone violation. Automatically calculated to
include the business hours on the record.

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
The minutes that remain before a milestone violation. Automatically calculated
to include the business hours on the record.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The days that have elapsed since a milestone violation. Automatically calculated
to include the business hours on the record.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The hours that have elapsed since a milestone violation. Automatically calculated
to include the business hours on the record.

**Type**
string


### Standard Objects EntitySubscription

**Field Name** **Details**

**Properties**
Group, Nillable, Sort

**Description**
The minutes that have elapsed since a milestone violation. Automatically
calculated to include the business hours on the record.

Usage

When you create an entitlement process, you select its type based on the type of record that you want the process to run on: Case or
Work Order. Processes created before Summer ’16 use the Case type. When a Work Order entitlement process runs on a work order, the
resulting milestones on the work order are object milestones. Conversely, when a Case entitlement process runs on a case, the resulting
milestones are case milestones, a separate standard object.

Tip: If an entitlement has an entitlement process associated with it, don’t use the entitlement for multiple types of support records.
An entitlement process works only on records that match the process’s type. For example, when a Case entitlement process is
applied to an entitlement, the process runs only on cases associated with that entitlement. If a work order is also associated with
the entitlement, the process doesn’t run on the work order. To ensure that the milestones you set up work as expected, associate
a customer’s work orders and cases with different entitlements.

Customize page layouts, validation rules, and more for object milestones from the Object Milestones node in Setup under Entitlement
Management.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**EntityMilestoneFeed**

Feed tracking is available for the object.

**EntityMilestoneHistory**

History is available for tracked fields of the object.

### EntitySubscription

Represents a subscription for a user following a record or another user. This object is available in API version 34.0 and later.

A user can subscribe to a record or to another user. Changes to the record and updates from the users are displayed in the Chatter feed
on the user's home page, which is a useful way to stay up-to-date with other users and with changes made to records in Salesforce.
Feeds are available in API version 18.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects EntitySubscription

Fields

**Field** **Details**

```
NetworkId

ParentId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the Experience Cloud site where the user is following the record or user. This field is
available in API version 26.0 and later, if digital experiences is enabled for your org.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the record or user which the user is following.

This is a polymorphic relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Account, Accreditation, ActivationTarget, ActivationTrgtIntOrgAccess, ApiAnomalyEventStore,
AssessmentIndicatorDefinition, AssessmentTask, AssessmentTaskContentDocument,
AssessmentTaskDefinition, AssessmentTaskIndDefinition, AssessmentTaskOrder, Asset,
AssetRelationship, AssignedResource, Award, BoardCertification, BusinessLicense,
BusinessMilestone, BusinessProfile, Campaign, CareBarrier, CareBarrierDeterminant,
CareBarrierType, CareDeterminant, CareDeterminantType, CareDiagnosis,
CareInterventionType, CareMetricTarget, CareObservation, CareObservationComponent,
CarePgmProvHealthcareProvider, CarePreauth, CarePreauthItem, CareProgram,
CareProgramCampaign, CareProgramEligibilityRule, CareProgramEnrollee,
CareProgramEnrolleeProduct, CareProgramEnrollmentCard, CareProgramGoal,
CareProgramProduct, CareProgramProvider, CareProgramTeamMember,
CareProviderAdverseAction, CareProviderFacilitySpecialty, CareProviderSearchableField,
CareRegisteredDevice, CareRequest, CareRequestDrug, CareRequestExtension,
CareRequestItem, CareSpecialty, CareSpecialtyTaxonomy, CareTaxonomy, Case, CodeSet,
CollaborationGroup, CommSubscription, CommSubscriptionChannelType,
CommSubscriptionConsent, CommSubscriptionTiming, ConsumptionSchedule, Contact,
ContactEncounter, ContactEncounterParticipant, ContentDocument, Contract,
CoverageBenefit, CoverageBenefitItem, CredentialStuffingEventStore, CreditMemo,
CreditMemoLine, Dashboard, DashboardComponent, DataStream, DelegatedAccount,
DocumentChecklistItem, EngagementChannelType, EnhancedLetterhead,
EnrollmentEligibilityCriteria, Event, HealthcareFacility, HealthcareFacilityNetwork,
HealthcarePayerNetwork, HealthcarePractitionerFacility, HealthcareProvider,


Standard Objects EntitySubscription

**Field** **Details**

HealthcareProviderNpi, HealthcareProviderSpecialty, HealthcareProviderTaxonomy, Identifier,
Image, IndividualApplication, Invoice, InvoiceLine, Lead, Location, MarketSegment,
MarketSegmentActivation, MemberPlan, MessagingSession, MktCalculatedInsight,
OperatingHours, Opportunity, Order, OrderItem, OtherComponentTask, PartyConsent,
PersonEducation, PersonLanguage, PersonLifeEvent, PersonName, PlanBenefit,
PlanBenefitItem, Product2, ProductFulfillmentLocation, ProductItem, ProductItemTransaction,
ProductRequest, ProductRequestLineItem, ProductRequired, ProductTransfer, ProfileSkill,
ProfileSkillEndorsement, ProfileSkillUser, ProviderSearchSyncLog, PurchaserPlan,
PurchaserPlanAssn, ReceivedDocument, Report, ReportAnomalyEventStore, ResourceAbsence,
ResourcePreference, ReturnOrder, ReturnOrderLineItem, ServiceAppointment, ServiceResource,
ServiceResourceSkill, ServiceTerritory, ServiceTerritoryMember, ServiceTerritoryWorkType,
SessionHijackingEventStore, Shift, Shipment, ShipmentItem, Site, SkillRequirement, SocialPost,
Solution, Task, ThreatDetectionFeedback, Topic, User, Visit, VisitedParty, Visitor, VoiceCall,
VolunteerProject, WorkBadgeDefinition, WorkOrder, WorkOrderLineItem, WorkType,
WorkTypeGroup, WorkTypeGroupMember

```
SubscriberId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the user who is following the record or user.

This is a relationship field.

**Relationship Name**
Subscriber

**Relationship Type**
Lookup

**Refers To**
User

Consider this when following records and users:

**•** Users can only follow records that they can see.

**•** Users can see which records other users are following, unless they don’t have access to the records.

**•** Administrators and users with the “Modify All Data” permission can configure a user to follow records that the user has read access
to.

**•** Administrators and users with the “Modify All Data” permission can configure users to stop following records.

**•** Following topics is available in API version 29.0 and later. For this reason, a topic ID is now a supported value for the `ParentId`
field.

**•** If you deactivate a user, any EntitySubscription where the user is associated with the ParentId or SubscriberId field, meaning all
subscriptions both to and from the user, are soft deleted. If the user is reactivated, the subscriptions are restored. However, if you


### Standard Objects EnvironmentHubMember

deactivate multiple users at once and these users follow each other, their subscriptions are hard deleted. In this case, the user-to-user
EntitySubscription is deleted twice (double deleted). Such subscriptions can’t be restored upon user reactivation.

When using `query()` with EntitySubscription,

**•** Note the following SOQL restriction. No SOQL limit if logged-in user has “View All Data” permission. If not, specify a LIMIT clause of
1,000 records or fewer.

**•** A query using a `WHERE` clause can only filter by fields on the EntitySubscription object.

**•** If user sharing is enabled and the querying user is not an administrator, a SOQL query must be constrained either by the `ParentId`
or `SubscriberId` . Otherwise, the query behavior at run time is undefined, meaning the result set can be incomplete or inconsistent
from invocation to invocation. For an unconstrained query, the sharing check limits imposed on a non-adminstrative user are likely
to be exceeded before the query completes, because access checks are run against both parent and subject, for each row of the
result set. We recommend using the Connect REST API to query EntitySubscription data instead of running a SOQL query.

**•** Users without the “View All Data” permission

**–** Need read access on the object associated with the `ParentId` field to see which users are following records for the object.

**–** Can use an `ORDER BY` clause in a query only to order by fields on the EntitySubscription object. For example, if the subscription
relates to an Account record, the query can `ORDER BY ParentId`, but it can’t `ORDER BY Account.Name` .

**–** Don’t always get all matching subscriptions when running a query. For these users, a query evaluates visibility criteria on a
maximum of 500 records to reduce the prospect of long-running queries. If a user runs a query to see the CEO's subscriptions,
it might scan a large number of records. The query only returns matches within the first 500 records scanned. It is possible that
there are more subscriptions that are visible to the user, but they are not returned. To mitigate this, we recommend using a
`WHERE` clause, if possible, to reduce the scope of the query.

Sample—SOQL

The following SOQL query returns subscriptions for all the accounts that a subscriber is following that have more than 10 employees:

```
   SELECT Id

   FROM EntitySubscription

   WHERE SubscriberId = '005U0000000Rg2CIAS'

   AND ParentId IN (

     SELECT Id FROM Account

     WHERE NumberOfEmployees > 10

   )

   LIMIT 200

```

SEE ALSO:

Custom Object__Feed

### EnvironmentHubMember

Represents a member organization in the Environment Hub. This object is available in API version 29.0 and later.

[Note: You can create only 20 member orgs per day. If you need to create additional orgs, log a support case in the Salesforce](https://partners.salesforce.com)
[Partner Community. For product, specify](https://partners.salesforce.com) **Platform** . For topic, specify **AppExchange & Managed Packages** .


Standard Objects EnvironmentHubMember

Supported Calls

`delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`

Fields

**Field Name** **Details**

```
Description

DisplayName

EnvironmentHubId

Instance

IsFedIdSsoMatchAllowed

```

**Type**
textarea

**Properties**
Nillable, Update

**Description**
A brief description of this org.

**Type**
string

**Properties**
Filter, Group, Nillable,Sort, Update

**Description**
The name that the user has specified for this member org.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The Org ID of this member’s Environment Hub org.

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the instance where the Environment Hub member org resides.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if single sign-on (SSO) has been enabled based on matching the Federation
ID. The default is `false` .


Standard Objects EnvironmentHubMember

**Field Name** **Details**

```
IsSandbox

MemberEntity

MemberType

Name

OrgEdition

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the member org is a sandbox ( `true` ) or not ( `false` ). This field is available
in API version 36.0 and later.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The unique Org ID of the member org for this record.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of member org for this record. Possible values include `Branch Org`, `Patch`
`Org`, `Release Org`, `Sandbox Org`, `Trialforce Management Org`,
and `Trialforce Source Org` .

Note: Only one member type at a time is stored. Member type is determined
according to this hierarchy: (1) Sandbox, (2) Release, (3) Trialforce Source Org
(TSO), (4) Patch, (5) Branch, and (6) Trialforce Management Org (TMO). For
example, if an org is both a sandbox and a TMO, the value of `MemberType` is
`Sandbox Org` .

**Type**
string

**Properties**
Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the member org for this record.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The org’s edition, for example, Enterprise Edition or Unlimited Edition.


Standard Objects EnvironmentHubMember

**Field Name** **Details**

```
OrgStatus

Origin

SSOMappedUsers

ServiceProviderId

ShouldAddRelatedOrgs

ShouldEnableSSO

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The licensing or creation status of this org. Possible values include `Active`, `Demo`,
`Deleted`, `Free`, `Inactive`, and `Trial` .

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The method by which this org was added to the Environment Hub. Possible values are
`autoDiscovered`, `userAdded`, and `provisioned` .

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of mapped users in this member org. This field is available in API
version 36.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The ID of the service provider for this member org. This field is available in API version
36.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Status of the connection of related orgs to the hub. Possible values are `done`,
`notRequested`, `pending`, and `requested` .

**Type**
boolean


### Standard Objects Event

**Field Name** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
If SSO should be enabled when this member org is added. The default is `false` .

```
SsoStatus

SsoUsernameFormula

```

Usage

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
If SSO has been enabled for this org. Possible values are:

**•** `Enabled` —Single sign-on is enabled.

**•** `Disabled` —Single sign-on is disabled.

**•** `Pending` —Single sign-on is in the process of being enabled.

**•** `Failed` —Single sign-on enablement failed. Contact Salesforce support for
assistance.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The custom formula for matching users in the hub and member orgs.

Use this object to access and modify settings of member orgs in the Environment Hub.

### Event

Represents an event in the calendar. In the user interface, event and task records are collectively referred to as activities.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Note:

**•** An EventRelation object can’t be related to a child event, and child events don’t include the invitee related list.

**•** `query()`, `delete()`, and `update()` aren’t allowed with events related to more than one contact in API versions 25.0
and earlier.

**•** `create()` and `update()` aren’t available for read-only fields on Lightning Experience event series.


Standard Objects Event

**•** `upsert()` and `undelete()` aren’t supported for syncing changes made to events through the API using the feature
Lightning Sync.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AcceptedEventInviteeIds

AccountId

```

**Type**
JunctionIdList

**Properties**
Create, Update

**Description**
A string array of contact or lead IDs who accepted this event. This `JunctionIdList` is
linked to the `AcceptedEventRelation` child relationship.

Warning: Adding a `JunctionIdList` field name to the `fieldsToNull`
property deletes all related junction records. This action can’t be undone.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the ID of the related account. The `AccountId` is determined as follows.

If the value of `WhatId` is any of the following objects, then Salesforce uses that object’s
`AccountId` .

**•** Account

**•** Opportunity

**•** Contract

**•** Custom object that’s a child of Account

If the value of the `WhatId` field is any other object, and the value of the `WhoId` field is a
contact object, then Salesforce uses that contact’s `AccountId` . If your org uses Shared
Activities, Salesforce uses the `AccountId` of the primary contact.

Otherwise, Salesforce sets the value of the `AccountId` field to `null` .

For information on IDs, see ID Field Type.

This is a relationship field.

**Relationship Name**
Account


Standard Objects Event

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Account

```
ActivityDate

ActivityDateTime

ClientGuid

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Contains the event’s due date if the `IsAllDayEvent` flag is set to `true` . Doesn’t contain
the event’s latest due date if the `IsAllDayEvent` flag is set to `false` . When
`IsAllDayEvent` flag is set to `true`, use `ActivityDateTime` or `StartDateTime` .
This field is a date field with a timestamp that’s always set to midnight in the Coordinated
Universal Time (UTC) time zone. Don’t attempt to alter the timestamp to account for time
zone differences. Label is **Due Date Only** .

This field is required in API versions 12.0 and earlier if the `IsAllDayEvent` flag is set to
`true` .

The value for this field and `StartDateTime` must match, or one of them must be `null` .

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Contains the event’s due date if the `IsAllDayEvent` flag is set to `false` . The time
portion of this field is always transferred in the Coordinated Universal Time (UTC) time zone.
Translate the time portion to or from a local time zone for the user or the application, as
appropriate. Label is **Due Date Time** .

This field is required in API versions 12.0 and earlier if the `IsAllDayEvent` flag is set to
`false` .

The value for this field and `StartDateTime` must match, or one of them must be `null` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The client globally unique identifier identifies the external API client used to create the event.
Label is **Client GUID** .


Standard Objects Event

**Field** **Details**

```
CurrencyIsoCode

DeclinedEventInviteeIds

Description

Division

DurationInMinutes

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO code for
any currency allowed by the organization.

**Type**
JunctionIdLIst

**Properties**
Create, Update

**Description**
A string array of contact, lead, or user IDs who declined this event. This `JunctionIdList`
is linked to the `DeclinedEventRelation` child relationship.

Warning: Adding a `JunctionIdList` field name to the `fieldsToNull`
property deletes all related junction records. This action can’t be undone.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Contains a text description of the event. Limit: 32,000 characters.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
A logical segment of your organization's data. For example, if your company is organized
into different business units, you could create a division for each business unit, such as “North
America,” “Healthcare,” or “Consulting.” Available only if the organization has the Division
permission enabled.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Contains the event length, in minutes. Even though this field represents a temporal value,
it’s an integer type—not a Date/Time type.


Standard Objects Event

**Field** **Details**

Required in API versions 12.0 and earlier if `IsAllDayEvent` is false.

In API versions 13.0 and later, this field is optional, depending on the following:

**•** If `IsAllDayEvent` is true, you can supply a value for either `DurationInMinutes`
or `EndDateTime` . Supplying values in both fields is allowed if the values add up to
the same amount of time. If both fields are `null`, the duration defaults to one day.

**•** If `IsAllDayEvent` is false, a value must be supplied for either
`DurationInMinutes` or `EndDateTime` . Supplying values in both fields is allowed
if the values add up to the same amount of time.

If the multiday event feature is enabled, then API versions 13.0 and later support values
greater than 1440 for the `DurationInMinutes` field. API versions 12.0 and earlier can’t
access event objects whose `DurationInMinutes` is greater than 1440. For more
information, see **Multiday Events** .

Depending on your API version, errors with the `DurationInMinutes` and
`EndDateTime` fields may appear in different places.

**•** Versions 38.0 and before—Errors always appear in the `DurationInMinutes` field.

**•** Versions 39.0 and later—If there’s no value for the `DurationInMinutes` field, errors
appear in the `EndDateTime` field. Otherwise, they appear in the
`DurationInMinutes` field.

```
EndDate

EndDateTime

```

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Read-only. Available in API versions 46.0 and later. This field supplies the date value that
appears in the EndDateTime field. This field is a date field with a timestamp that is always
set to midnight in the Coordinated Universal Time (UTC) time zone.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Available in API versions 13.0 and later. The time portion of this field is always transferred in
the Coordinated Universal Time (UTC) time zone. Translate the time portion to or from a
local time zone for the user or the application, as appropriate.

This field is optional, depending on the following:

**•** If `IsAllDayEvent` is true, you can supply a value for either `DurationInMinutes`
or `EndDateTime` . Supplying values in both fields is allowed if the values add up to
the same amount of time. If both fields are `null`, the duration defaults to one day.


Standard Objects Event

**Field** **Details**

**•** If `IsAllDayEvent` is false, a value must be supplied for either
`DurationInMinutes` or `EndDateTime` . Supplying values in both fields is allowed
if the values add up to the same amount of time.

Depending on your API version, errors with the `DurationInMinutes` and
`EndDateTime` fields may appear in different places.

**•** Versions 38.0 and before—Errors always appear in the `DurationInMinutes` field.

**•** Versions 39.0 and later—If there’s no value for the `DurationInMinutes` field, errors
appear in the `EndDateTime` field. Otherwise, they appear in the
`DurationInMinutes` field.

```
EventSubtype

EventWhoIds

GroupEventType

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Provides standard subtypes to facilitate creating and searching for events. This field isn’t
updateable.

**Type**
JunctionIdList

**Properties**
Create, Update

**Description**
A string array of contact or lead IDs used to create many-to-many relationships with a shared
event. `EventWhoIds` is available when the shared activities setting is enabled. The first
contact or lead ID in the list becomes the primary `WhoId` if you don’t specify a primary
`WhoId` . If you set the `EventWhoIds` field to null, all entries in the list are deleted and
the value of `WhoId` is added as the first entry.

Warning: Adding a `JunctionIdList` field name to the `fieldsToNull`
property deletes all related junction records. This action can’t be undone.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Read-only. Available in API versions 19.0 and later.

The possible values are:

**•** `0` (Non–group event)—An event with no invitees.

**•** `1` (Group event)—An event with invitees.

**•** `2` (Proposed event)—An event created when a user requests a meeting with a contact,
lead, or person account using the Salesforce user interface. When the user confirms the


Standard Objects Event

**Field** **Details**

meeting, the proposed event becomes a group event. You can’t create, edit, or delete
proposed events in the API. This value is no longer used in API version 41.0 and later.

**•** `3` (IsRecurrence2 Series Pattern)—An event representing a template for a series
recurrence pattern in Lightning Experience. You can't view, create, edit, or delete these
events in the API.

```
IsAllDayEvent

IsArchived

IsChild

IsClientManaged

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the `ActivityDate` field ( `true` ) or the `ActivityDateTime` field
( `false` ) is used to define the date or time of the event. Label is **All-Day Event** . See also
`DurationInMinutes` and `EndDateTime` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the event has been archived.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the event is a child of another event ( `true` ) or not ( `false` ).

For a child event, you can update `IsReminderSet` and `ReminderDateTime` only.
You can query and delete a child event. If the objects related to the child event are different
from those objects related to the parent event (this difference is possible if you use API
version 25.0 or earlier) and one of the objects related to the child event is deleted, the objects
related to the parent event are updated to ensure data integrity.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the event is managed by an external client. If the value of this field is false,
the event isn’t owned or managed by an external client, and Salesforce can be used to update
it. If the value is true, Salesforce can be used to change only noncritical fields on the event.
Label is **Is Client Managed** .


Standard Objects Event

**Field** **Details**

```
IsGroupEvent

IsPrivate

IsRecurrence

IsRecurrence2

IsRecurrence2Exception

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the event is a group event—that is, whether it has invitees ( `true` ) or not
( `false` ).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether users other than the creator of the event can ( `false` ) or can’t ( `true` )
see the event details when viewing the event user’s calendar. However, users with the View
All Data or Modify All Data permission can see private events in reports and searches, or
when viewing other users’ calendars. Private events can’t be associated with opportunities,
accounts, cases, campaigns, contracts, leads, or contacts. Label is **Private** .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a Salesforce Classic event is scheduled to repeat itself ( `true` ) or only
occurs one time ( `false` ). This field is read-only when updating records, but not when
creating them. If this field value is `true`, then `RecurrenceEndDateOnly`,
`RecurrenceStartDateTime`, `RecurrenceType`, and any recurrence fields
associated with the given recurrence type must be populated. Label is **Create recurring**
**series of events** .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read-only. This field is available in API version 44.0 and later. Indicates whether a Lightning
Experience event is scheduled to repeat ( `true` ) or only occurs one time ( `false)` . If this
field value is true, then `Recurrence2PatternText` and
`Recurrence2PatternVersion` must be populated. Label is **Repeat** .

**Type**
boolean


Standard Objects Event

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether an individual event in a series is different from the other events in the
series, making it an exception. Changes made to the series aren’t made to an event that is
an exception. Available in API version 44.0 and later.

Read-only in API version 66 and earlier.

```
IsRecurrence2Exclusion

IsReminderSet

IsVisibleInSelfService

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read-only. This field is available in API version 44.0 and later. Indicates when updates to a
Lightning Experience event series recurrence pattern have been made, but affect future
event occurrences only. For past event occurrences, `IsRecurrence2Exclusion` is
set to `true`, excluding past occurrences from the series recurrence pattern.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the activity is a reminder ( `true` ) or not ( `false` ).

To set `IsReminderSet` to `true`, the `ReminderDateTime` field must contain a valid
date and time to trigger the reminder.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether an event associated with an object can be viewed in the Customer Portal
( `true` ) or not ( `false` ). If your org has enabled digital experiences, events marked
`IsVisibleInSelfService` are visible to any external user in the Experience Cloud
site, as long as the user has access to the record the event was created on. This field is available
when

**•** Customer Portal or partner portal is enabled

OR

**•** Digital experiences is enabled and you have Customer Portal or partner portal licenses


Standard Objects Event

**Field** **Details**

```
Location

OwnerId

Recurrence2PatternStartDate

Recurrence2PatternText

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Contains the location of the event.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Contains the ID of the user or public calendar who owns the event. Label is **Assigned to ID** .

This is a polymorphic relationship field.

Important: By default, the event is assigned to the user who created it. If the event
is created by the Automated Process user, add a different value for OwnerId. The
Automated Process user isn’t a valid value for the OwnerId field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Calendar, User

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Read-only. This field is available in API version 44.0 and later. Indicates the date and time
when the Lightning Experience event series begins. The time portion of this field is always
transferred in the Coordinated Universal Time (UTC) time zone. Translate the time portion
to or from a local time zone for the user or the application, as appropriate.

**Type**
textarea

**Properties**
Create, Nillable

**Description**
The RRULE that describes the recurrence pattern for Lightning Experience event series.
Supports a subset of the RFC 5545 standard for internet calendaring and scheduling. See the


Standard Objects Event

**Field** **Details**

Event Series section in this topic for usage examples. This field has a maximum length of 512
characters.

This field is available in API version 44.0 and later, and has the `Create` property in API
version 52.0 and later.

```
Recurrence2PatternTimeZone

Recurrence2PatternVersion

RecurrenceActivityId

RecurrenceDayOfMonth

RecurrenceDayOfWeekMask

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field is available in API version 44.0 and later. Indicates the time zone in which the
Lightning Experience event series was created or updated. This field uses standard Java
TimeZone IDs. For example, America/Los_Angeles.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort,

**Description**
For internal use only. This field is available in API version 44.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Read-only. Not required on create. Contains the ID of the main record of the Salesforce Classic
recurring event. Subsequent occurrences have the same value in this field.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the day of the month on which the event repeats.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects Event

**Field** **Details**

**Description**
Indicates the day or days of the week on which the Salesforce Classic recurring event repeats.
This field contains a bitmask. The values are as follows:

**•** Sunday = `1`

**•** Monday = `2`

**•** Tuesday = `4`

**•** Wednesday = `8`

**•** Thursday = `16`

**•** Friday = `32`

**•** Saturday = `64`

Multiple days are represented as the sum of their numerical values. For example, Tuesday
and Thursday = 4 + 16 = 20.

```
RecurrenceEndDateOnly

RecurrenceInstance

RecurrenceInterval

RecurrenceMonthOfYear

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the last date on which the event repeats. For multiday Salesforce Classic recurring
events, this date is the day on which the last occurrence starts. This field is a date field with
a timestamp that is always set to midnight in the Coordinated Universal Time (UTC) time
zone. Don’t attempt to alter the timestamp to account for time zone differences.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the frequency of the Salesforce Classic event’s recurrence. For example, `2nd` or
`3rd` .

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the interval between Salesforce Classic recurring events.

**Type**
picklist


Standard Objects Event

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the month in which the Salesforce Classic recurring event repeats.

```
RecurrenceStartDateTime

RecurrenceTimeZoneSidKey

RecurrenceType

ReminderDateTime

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates the date and time when the Salesforce Classic recurring event begins. The value
must precede the `RecurrenceEndDateOnly` . The time portion of this field is always
transferred in the Coordinated Universal Time (UTC) time zone. Translate the time portion
to or from a local time zone for the user or the application, as appropriate.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the time zone associated with a Salesforce Classic recurring event. For example,
“UTC-8:00” for Pacific Standard Time.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates how often the Salesforce Classic event repeats. For example, daily, weekly, or every
nth month (where “nth” is defined in `RecurrenceInstance` ).

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Represents the time when the reminder is scheduled to fire, if `IsReminderSet` is set to
`true` . If `IsReminderSet` is set to `false`, then the user may have deselected the
reminder checkbox in the Salesforce user interface, or the reminder has already fired at the
time indicated by the value.


Standard Objects Event

**Field** **Details**

```
ShowAs

StartDateTime

Subject

Type

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates how this event appears when another user views the calendar: Busy, Out of Office,
or Free. Label is **Show Time As** .

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates the start date and time of the event. Available in versions 13.0 and later.

If the Event `IsAllDayEvent` flag is set to true (indicating that it’s an all-day Event), then
the event start date information is contained in the `StartDateTime` field. The time
portion of this field is always transferred in the Coordinated Universal Time (UTC) time zone.
Translate the time portion to or from a local time zone for the user or the application, as
appropriate.

If the Event `IsAllDayEvent` flag is set to false (indicating that it isn’t an all-day event),
then the event start date information is contained in the `StartDateTime` field. The time
portion is always transferred in the Coordinated Universal Time (UTC) time zone. You need
to translate the time portion to or from a local time zone for the user or the application, as
appropriate.

If this field has a value, then `ActivityDate` and `ActivityDateTime` must either
be `null` or match the value of this field.

**Type**
combobox

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The subject line of the event, such as Call, Email, or Meeting. Limit: 255 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the event type, such as Call, Email, or Meeting.


Standard Objects Event

**Field** **Details**

```
UndecidedEventInviteeIds

WhatCount

WhatId

```

**Type**
JunctionIdList

**Properties**
Create, Update

**Description**
A string array of contact, lead, or user IDs who are undecided about this event. This
`JunctionIdList` is linked to the `UndecidedEventRelation` child relationship.

Warning: Adding a `JunctionIdList` field name to the `fieldsToNull`
property deletes all related junction records. This action can’t be undone.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Available if your organization has enabled Shared Activities. Represents the count of related
EventRelations pertaining to the `WhatId` . The count of the `WhatId` must be _`1`_ or less.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The `WhatId` represents nonhuman objects such as accounts, opportunities, campaigns,
cases, or custom objects. `WhatId` s are polymorphic. Polymorphic means a `WhatId` is
equivalent to the ID of a related object. The label is `Related To ID` .

This is a polymorphic relationship field.

**Relationship Name**
What

**Relationship Type**
Lookup

**Refers To**
Account, Accreditation, AssessmentIndicatorDefinition, AssessmentTask,
AssessmentTaskContentDocument, AssessmentTaskDefinition, AssessmentTaskOrder, Asset,
AssetRelationship, AssignedResource, Award, BoardCertification, BusinessLicense,
BusinessMilestone, BusinessProfile, Campaign, CareBarrier, CareBarrierDeterminant,
CareBarrierType, CareDeterminant, CareDeterminantType, CareDiagnosis,
CareInterventionType, CareMetricTarget, CareObservation, CareObservationComponent,
CarePgmProvHealthcareProvider, CarePreauth, CarePreauthItem, CareProgram,
CareProgramCampaign, CareProgramEligibilityRule, CareProgramEnrollee,
CareProgramEnrolleeProduct, CareProgramEnrollmentCard, CareProgramGoal,
CareProgramProduct, CareProgramProvider, CareProgramTeamMember,


Standard Objects Event

**Field** **Details**

CareProviderAdverseAction, CareProviderFacilitySpecialty, CareProviderSearchableField,
CareRegisteredDevice, CareRequest, CareRequestDrug, CareRequestExtension,
CareRequestItem, CareSpecialty, CareSpecialtyTaxonomy, CareTaxonomy, Case,
CommSubscriptionConsent, ContactEncounter, ContactEncounterParticipant, ContactRequest,
Contract, CoverageBenefit, CoverageBenefitItem, CreditMemo, DelegatedAccount,
DocumentChecklistItem, EnrollmentEligibilityCriteria, HealthcareFacility,
HealthcareFacilityNetwork, HealthcarePayerNetwork, HealthcarePractitionerFacility,
HealthcareProvider, HealthcareProviderNpi, HealthcareProviderSpecialty,
HealthcareProviderTaxonomy, IdentityDocument, Image, IndividualApplication, Invoice,
ListEmail, Location, MemberPlan, Opportunity, Order, OtherComponentTask, PartyConsent,
PersonLifeEvent, PlanBenefit, PlanBenefitItem, ProcessException, Product2, ProductItem,
ProductRequest, ProductRequestLineItem, ProductTransfer, PurchaserPlan,
ReceivedDocument, ResourceAbsence, ReturnOrder, ReturnOrderLineItem,
ServiceAppointment, ServiceResource, Shift, Shipment, ShipmentItem, Solution, Visit,
VisitedParty, VolunteerProject, WorkOrder, WorkOrderLineItem

```
WhoCount

WhoId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Available to organizations that have Shared Activities enabled. Represents the count of
related EventRelations pertaining to the `WhoId` .

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The WhoId represents a human such as a lead or a contact. WhoIds are polymorphic.
Polymorphic means a WhoId is equivalent to a contact’s ID or a lead’s ID. The label is `Name`
`ID` .

If Shared Activities is enabled, the value of this field is the ID of the related lead or primary
contact. If you add, update, or remove the WhoId field, you might encounter problems with
triggers, workflows, and data validation rules that are associated with the record. The label
is `Name ID` .

If the `JunctionIdList` field is used, all `WhoId` s are included in the relationship list.

Beginning in API version 37.0, if the contact or lead ID in the `WhoId` field isn't in the
`EventWhoIds` list, no error occurs and the ID is added to the `EventWhoIds` as the
primary `WhoId` . If `WhoId` is set to null, an arbitrary ID from the existing `EventWhoIds`
list is promoted to the primary position.

This is a polymorphic relationship field.

**Relationship Name**
Who


Standard Objects Event

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Contact, Lead

Usage

Use Event to manage calendar appointments.

**Querying and Filtering Events**

Queries on events are denied before they time out if they involve amounts of data that are deemed too large. In such cases, the exception
code `OPERATION_TOO_LARGE` is returned. If you receive `OPERATION_TOO_LARGE`, refactor your query to return or scan a
smaller amount of data.

When querying for events with a specific due date, you must filter on both the `ActivityDateTimeand` and `ActivityDate`
fields. For example to find all events with a due date of February 14, 2003, you need two filters:

**•** One filter with the `ActivityDate` field equal to the Coordinated Universal Time (UTC) time zone on February 14, 2003.

**•** One filter with the `ActivityDate` field greater than or equal to midnight on February 14, 2003 in the user’s local time zone AND
less than or equal to midnight on February 15, 2003 in the user’s local time zone.

Alternatively, in API version 13.0 and later, you can find events with a specific due date by filtering on `StartDateTime` . For example,
to find all events with a due date of February 14, 2003, filter with the `StartDateTime` greater than or equal to midnight on February
14, 2003 in the user's local time zone AND less than or equal to midnight on February 15, 2003 in the user's local time zone.

The `EventId` field of an EventRelation object always points to the master record. An invitee on a group event can query the EventRelation
object to view the master record.

**Multiday Events**

**•** Multiday events are available in API version 13.0 and later. Also, in earlier versions SOQL queries don’t return multiday events.

**•** Multiday events are enabled through the user interface from Setup by entering _`Activity Settings`_ in the `Quick Find`
box, then selecting **Activity Settings** .

**•** If the multiday event feature is enabled, then API versions 13.0 and later support values greater than 1440 for the
`DurationInMinutes` field. API versions 12.0 and earlier can’t access event objects whose `DurationInMinutes` is greater
than 1440.

**•** Multiday events can’t exceed 14 days.

**Event Series and Recurring Events**

In Lightning Experience, events with multiple occurrences are called event series, and are indicated when the `IsRecurrence2` field
is set to `true` . In Salesforce Classic, events with multiple occurrences are called recurring events, and are indicated when the
`IsRecurrence` field is set to `true` . Both fields can’t be set to true for the same event.

**•** Lightning Experience event series are available in API version 44.0 and later as read-only fields. Recurrence patterns, specified by the
Recurrence2PatternText field, are creatable in API version 52.0 and later. Salesforce Classic recurring events are available in API version
7.0 and later. In earlier versions, SOQL queries don’t return any Lightning Experience event series.

**•** After an event is created, you can’t change the values of `IsRecurrence2` or `IsRecurrence` from `true` to `false` or vice
versa.

**•** You can’t set fields associated with `IsRecurrence2` for events where `IsRecurrence` is set to `true`, or vice versa.


Standard Objects Event

**•** For Lightning Experience event series where `IsRecurrence2` is `true`, if you’d like to delete a single or all remaining events,
use the REST API call. For Salesforce Classic recurring events where `IsRecurrence` is `true`, all past and future events in the
series are removed when you delete the recurring event series through the API. However, when you delete the recurring event series
through the user interface, only future occurrences are removed.

**•** For Lightning Experience event series in API version 58.0 and later, when you change a future event, events in the entire series also
change. When you change a past event, `IsRecurrence2Exception` is set to `true` and only that past event changes.

**•** When creating a Salesforce Classic recurring event series, the duration of the event must be 24 hours or less. When the Salesforce
Classic recurring event series is created, you can extend the length of individual occurrences beyond 24 hours if Multiday events are
enabled; see **Multiday Events** .

**•** For Salesforce Classic recurring events, `RecurrenceStartDateTime`, `RecurrenceEndDateOnly`, `RecurrenceType`,
and any properties associated with the given recurrence type (see the Recurrence Field Usage for Salesforce Classic Recurring Events
table) must be populated.

**•** When updating a Salesforce Classic recurring event series, it’s not possible to update the `EventRelation` for the event series
object and the EventRelation for the series object occurrences at the same time.

**•** Lightning Experience event series have no series ID, so it’s not possible to locate other occurrences in the series. In Salesforce Classic
recurring events, you can use `RecurrenceActivityId` to locate other occurrences.

**•** For both Lightning Experience event series and Salesforce Classic recurring events, when a series repeats every day, month, or year,
you can only schedule occurrences one time per day, month, or year. The week option lets you schedule occurrences multiple days
per week.

[Limits for Lightning Experience event series and limits for Salesforce Classic recurring events also apply.](https://help.salesforce.com/s/articleView?id=sales.creating_events_lex.htm&type=5&language=en_US)

**Lightning Experience Event Series and Recurring Events**

Use the `Recurrence2PatternText` field to specify the recurrence pattern for Lightning Experience event series. These recurrence
patterns, called reference rules or RRULES, support a subset of the RFC 5545 standards. This table includes common RRULE examples.

The RRULE defined by `Recurrence2PatternText` supports a subset of the RFC 5545 standard for internet calendaring and
scheduling. Supported RRULE parts include FREQ, BYMONTH, BYMONTHDAY, BYDAY, WKST, BYSETPOS, INTERVAL, UNTIL, and COUNT.

When the event record is saved, the RRULE might be modified to follow the required format:

**•** The RRULE parts are placed in the following order: FREQ, BYMONTH, BYMONTHDAY, BYDAY, WKST, BYSETPOS, INTERVAL, UNTIL, and
COUNT.

**•** Any missing default values are inserted. For example, if the RRULE doesn't include INTERVAL, then `INTERVAL=1` is added.


Standard Objects Event

**•** The RRULE is prefaced with `RRULE:` if that preface is missing.


Standard Objects Event


Standard Objects Event

**Salesforce Classic Event Series and Recurring Events**

This table describes the usage of recurrence fields for Salesforce Classic recurring events. Each recurrence type must have all of its
properties set. All unused properties must be set to null.

**RecurrenceType Value** **Properties** **Example Pattern**

RecursDaily RecurrenceInterval Every second day

RecursEveryWeekday RecurrenceDayOfWeekMask Every weekday - can’t be Saturday or Sunday

RecursMonthly RecurrenceDayOfMonth Every second month, on the third day of the month
RecurrenceInterval

RecursMonthlyNth RecurrenceInterval RecurrenceInstance Every second month, on the last Friday of the month
RecurrenceDayOfWeekMask

RecursWeekly RecurrenceInterval Every three weeks on Wednesday and Friday
RecurrenceDayOfWeekMask

RecursYearly RecurrenceDayOfMonth Every March on the 26th day of the month
RecurrenceMonthOfYear

RecursYearlyNth RecurrenceDayOfWeekMask The first Saturday in every October
RecurrenceInstanceRecurrenceMonthOfYear

**Attendees, Invitees, and Resources**

The field `GroupEventType` indicates that event participants are included on an event. You can add a resource to an event only
when the resource is available. The only attendance status that can be assigned to resources is Accepted. Events can’t be saved when
resources you’ve added aren’t available.

Child attendee events aren’t supported in Apex Triggers. When a recurring event has attendees, Salesforce creates child event records
for each attendee for each recurrence. However, these child attendee event records don’t appear in `Trigger.new` or other trigger
context variables. Only the host’s event records are accessible in the trigger context.

**JunctionIdList**

To create an event using `JunctionIdList`, IDs are pulled from the related contacts and both the event and the `EventRelation`
records are created in one API call. If the `EventRelation` fails, the event is rolled back because it’s all done in a single API call.

```
   public void createEventNew(Contact[] contacts) {

    String[] contactIds = new String[contacts.size()];

    for (int i = 0; i < contacts.size(); i++) {

     contactIds[i] = contacts[i].getID();

    }

    Event event = new Event();

    event.setSubject("New Event");

    event.setEventWhoIds(contactIds);

```


### Standard Objects EventLogFile

```
    SaveResult[] results = null;

    try {

     results = connection.create(new Event[] {

     task

     });

    } catch (ConnectionException ce) {

     ce.printStackTrace();

    }

   }

```

**Syncing Events with Lightning Sync**

Attendee statuses (Accepted or Maybe, Declined, or No Response) sync from Microsoft [®] Exchange or Google to Salesforce, but not from
Salesforce to Exchange or Google. Be wary of creating API flows that update attendee status in Salesforce for users set up to sync both
ways. Eventually the original Exchange or Google status overrides the update made in Salesforce.

**Shared Field-Level Security for Event and Task Objects**

Metadata deployments for the Event object must include the field-level security for the Task object. Shared field-level security prevents
each object from changing the field-level security of the associated object.

Metadata deployments that include field-level security for only one of either the Event or Task objects can cause field-level security
changes to the other object that aren't reflected in the metadata.

**•** If field-level security is enabled for one object, then field-level security is enabled for both objects.

**•** If field-level security is disabled for one object, then it's disabled for both objects.

Note: A missing entry in the metadata is treated as field-level security being disabled.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**EventChangeEvent (API version 44.0)**
Change events are available for the object.

**EventFeed (API version 20.0)**
Feed tracking is available for the object.

SEE ALSO:

Overview of Salesforce Objects and Fields

### EventLogFile

Represents event log files for event monitoring. The event monitoring product gathers information about your Salesforce org’s operational
events, which you can use to analyze usage trends and user behavior. This object is available in API version 32.0 and later. The `Interval`
and `Sequence` fields are available only in API version 37.0 and later.

You can interact with event monitoring data by querying fields on the EventLogFile object (like `EventType` and `LogDate` ).
`CreatedDate` tracks when the log file was generated. To view the underlying event data, query the `LogFile` field. The `EventType`
determines the schema of this field. Log files don’t count towards your org’s data or file storage allocations. For more information, see
### EventLogFile Supported Event Types.


Standard Objects EventLogFile

Composite requests that include multiple API requests in a single call aren’t supported. In the event of a composite request, EventLogFile
captures only the parent request.

Note: Log data schema for each `EventType` can change. With each new release, use the `LogFileFieldNames` and
`LogFileFieldTypes` fields to validate the schema changes. In the unlikely case in which no log files are generated for 24
hours, contact Salesforce Customer Support.

Tip: Debug and troubleshoot performance issues by correlating logs using the customizable Request Identifier field, available in
all Event Monitoring logs. To correlate logs pertaining to an API request call, set the `X-SFDC-REQUEST-ID` header with a 32
character OTEL compatible TraceId or a 22 -character alphanumeric Id. Using SOQL, search for the Event Monitoring logs with this
RequestId to correlate the logs and see the unit of work performed as a part of the API transaction.

[For details about event monitoring, see the Trailhead Event Monitoring module.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Special Access Rules

