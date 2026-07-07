# Q8: What is the difference between LWC, LWR and LWS in Salesforce, and from which API version are they available and enforced?

## Approach: B_context7-our-library
- latency: 2947 ms
- libraryId: /damecek/salesforce-documentation-context

---

===============
LIBRARY RULES
===============
From library maintainers:
- Do not infer product behavior beyond what is stated in the markdown.
- Preserve product terminology as written in the source markdown.



### FlowVariableView Object

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/object-reference-for-the-salesforce-platform-part-09.md

Represents a variable within a Salesforce flow version. Available in API version 46.0 and later.

```APIDOC
## FlowVariableView Object

### Description
Represents a variable within a Salesforce flow version. Available in API version 46.0 and later.

### Supported Calls
`describeSObjects()`, `query()`

### Fields

#### ApiName
- **Type**: string
- **Properties**: Filter, Group, Nillable, Sort
- **Description**: The API name of the flow variable.

#### DataType
- **Type**: string
- **Properties**: Filter, Group, Nillable, Sort
- **Description**: The data type of the flow variable. Valid values are:
    - Apex (API version 46.0+)
    - Boolean
    - Currency
    - Date
    - DateTime (API version 30.0+)
    - Number
    - Multipicklist (API version 34.0+)
    - Picklist (API version 34.0+)
    - String
    - sObject

#### Description
- **Type**: string
- **Properties**: Filter, Group, Nillable, Sort
- **Description**: Flow variable information, specified by the org’s admin.

#### DurableId
- **Type**: string
- **Properties**: Filter, Group, Nillable, Sort
- **Description**: The Id of the flow variable.

#### FlowVersionViewId
- **Type**: string
- **Properties**: Filter, Nillable, Sort
- **Description**: The Id of the flow version.
- **Relationship Name**: FlowVersionView
- **Relationship Type**: Lookup

### Usage
Use this object to query information about flow variables. A query must be filtered by FlowVersionViewId to get results. Only variables with IsInput or IsOutput marked as true are visible.

### Fields (continued)

#### IsCollection
- **Type**: boolean
- **Properties**: Defaulted on create, Filter, Group, Sort
- **Description**: Indicates whether or not the flow variable is a collection of values.

#### IsInput
- **Type**: boolean
- **Properties**: Defaulted on create, Filter, Group, Sort
- **Description**: Indicated whether or not the flow variable is available for input.

#### IsOutput
- **Type**: boolean
- **Properties**: Defaulted on create, Filter, Group, Sort
- **Description**: Indicates whether or not the flow variable is available for output.

#### ObjectType
- **Type**: string
- **Properties**: Filter, Group, Nillable, Sort
- **Description**: If the data type is sObject, this field indicates which object.
```

--------------------------------

### Connection and Description Fields

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/object-reference-for-the-salesforce-platform-part-02.md

These fields relate to Salesforce to Salesforce connections and general account descriptions. ConnectionSentId is available in older API versions and has specific limitations.

```Salesforce
ConnectionSentId
Description
```

### ObjectRelatedUrl > Fields > ParentId

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/object-reference-for-the-salesforce-platform-part-12.md

The ObjectRelatedUrl object has specific availability in API versions: Product2 and ProductCategory are available in LWR Commerce stores from API version 58.0 onwards. Custom object pages on enhanced LWR sites are available from API version 60.0 onwards. Account and contact pages on enhanced LWR sites are available from API version 61.0 onwards.

--------------------------------

### Salesforce DX Project Structure and Source Format

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/salesforce-dx-developer-guide-part-01.md

Lightning web components must be placed in an `lwc` directory within the `<package directory>`.

--------------------------------

### Metadata Types > FlexiPage

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/metadata-api-developer-guide-part-05.md

The FlexiPage metadata type represents different types of Lightning pages used in Salesforce, such as flow pages, global search result pages, login pages, and object pages. Each subtype has a specific purpose and is available from a certain API version. For example, CommFlowPage is available from API version 45.0 and later, while HomePage is available from API version 37.0 and later.
