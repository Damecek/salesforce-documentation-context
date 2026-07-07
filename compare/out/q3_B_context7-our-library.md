# Q3: What is the maximum number of SOQL queries allowed in a single synchronous Apex transaction?

## Approach: B_context7-our-library
- latency: 3069 ms
- libraryId: /damecek/salesforce-documentation-context

---

===============
LIBRARY RULES
===============
From library maintainers:
- Do not infer product behavior beyond what is stated in the markdown.
- Preserve product terminology as written in the source markdown.



### Get Maximum SOQL Queries Limit

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/apex-reference-guide-part-14.md

Retrieves the total number of SOQL queries that can be issued per transaction. This is a fundamental limit for data retrieval operations.

```Apex
public static Integer getLimitQueries()
```

--------------------------------

### Limits.getLimitQueries()

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/apex-reference-guide-part-14.md

Retrieves the number of SOQL queries that have been executed in the current transaction. This method is part of the Limits class, which provides access to governor limit information.

```APIDOC
## Limits.getLimitQueries()

### Description
Retrieves the number of SOQL queries that have been executed in the current transaction. This method is part of the Limits class, which provides access to governor limit information.

### Method
None (Static method call)

### Endpoint
N/A (Apex method)

### Parameters
None

### Response
#### Success Response
- **Return Value** (Integer) - The number of SOQL queries executed.
```

--------------------------------

### Get Current SOQL Queries Count

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/apex-reference-guide-part-14.md

Returns the number of SOQL queries that have been issued in the current transaction. Track this to manage SOQL query limits.

```Apex
public static Integer getQueries()
```

### Apex Developer Guide > Apex Transactions and Governor Limits > Execution Governors and Limits > Per-Transaction Apex Limits

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/apex-developer-guide-part-02.md

The following are key per-transaction Apex limits: Total number of SOQL queries issued is 100 for synchronous and 200 for asynchronous Apex. Total number of records retrieved by SOQL queries is 50,000 for both. Total number of DML statements issued is 150 for both. Total number of records processed by DML statements is 10,000 for both. Total stack depth for recursively firing triggers is 16. Total number of callouts is 100 for both. Maximum cumulative timeout for all callouts is 120 seconds for both. The maximum number of methods with the `future` annotation allowed per Apex invocation is 50 in queueable context, and 50 in batch and future contexts.

--------------------------------

### Apex Developer Guide > Apex Transactions and Governor Limits

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/apex-developer-guide-part-03.md

Governor limits are enforced per transaction. For instance, a single transaction can accommodate up to 100 SOQL queries and 150 DML statements. Some limits, like the number of batch jobs that can be queued or active concurrently, are not bound by individual transactions.
