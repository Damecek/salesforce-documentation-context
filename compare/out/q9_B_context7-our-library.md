# Q9: How do I get the list of picklist values for a given record type in Apex?

## Approach: B_context7-our-library
- latency: 3079 ms
- libraryId: /damecek/salesforce-documentation-context

---

===============
LIBRARY RULES
===============
From library maintainers:
- Do not infer product behavior beyond what is stated in the markdown.
- Preserve product terminology as written in the source markdown.



### Get Picklist Values by Record Type

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/apex-reference-guide-part-07.md

Retrieves all picklist field values for a specific record type. Useful for dependent picklists.

```Apex
ConnectApi.PicklistValuesCollection getPicklistValuesByRecordType(String

objectApiName, String recordTypeId)
```

--------------------------------

### getPicklistValuesByRecordType(objectApiName, recordTypeId)

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/apex-reference-guide-part-07.md

Retrieves all picklist field values for a specific record type of a given object. This method is particularly useful for handling dependent picklists.

```APIDOC
## getPicklistValuesByRecordType(objectApiName, recordTypeId)

### Description
Get the values for all the picklist fields of a specific record type.

### Method
Apex Static Method

### Signature
`public static ConnectApi.PicklistValuesCollection getPicklistValuesByRecordType(String objectApiName, String recordTypeId)`

### Parameters
#### Path Parameters
- **objectApiName** (String) - Required - API name of a User Interface API supported object.
- **recordTypeId** (String) - Required - ID of a record type.

### Return Value
- **ConnectApi.PicklistValuesCollection** - A collection of picklist values.
```

--------------------------------

### RecordUi

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/apex-reference-guide-part-03.md

Get picklist values by record type.

```APIDOC
## RecordUi

### Description
Retrieves picklist values based on record type.

### Class
RecordUi
```

--------------------------------

### Get Picklist Values

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/apex-reference-guide-part-12.md

Retrieves a list of Schema.PicklistEntry objects from a field's describe result, representing the available picklist values.

```apex
Schema.DescribeFieldResult F = Account.Industry.getDescribe();
   List<Schema.PicklistEntry> P = F.getPicklistValues();
```

### Apex Reference Guide RecordUi Class > RecordUi Methods

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/apex-reference-guide-part-07.md

The `getPicklistValuesByRecordType(objectApiName, recordTypeId)` method retrieves all picklist field values for a specific record type. This is particularly useful for obtaining dependent picklist values, such as hierarchical country and city lists, in a single request. Note that this Apex method cannot be used in packages that utilize push upgrades.
