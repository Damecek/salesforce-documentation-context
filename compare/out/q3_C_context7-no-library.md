# Q3: What is the maximum number of SOQL queries allowed in a single synchronous Apex transaction?

## Approach: C_context7-no-library
- latency: 4070 ms
- chosenLibrary: /beyond-the-cloud-dev/soql-lib
- chosenTitle: SOQL Lib

---

### resolve-library-id picked: /beyond-the-cloud-dev/soql-lib (SOQL Lib)

--- resolve-library-id ranking (top of list) ---
Available Libraries:

- Title: SOQL Lib
- Context7-compatible library ID: /beyond-the-cloud-dev/soql-lib
- Description: SOQL Lib provides functional constructs for SOQL queries in Apex, enabling more fluent and structured data retrieval from Salesforce.
- Code Snippets: 1145
- Source Reputation: High
- Benchmark Score: 95
----------
- Title: SOQL
- Context7-compatible library ID: /forcedotcom/go-soql
- Description: This package provides `soql` tags for Go structs, enabling developers to marshal Go structs into SOQL queries for interacting with the Salesforce API.
- Code Snippets: 435
- Source Reputation: High
- Benchmark Score: 95

--- query-docs against /beyond-the-cloud-dev/soql-lib ---
### SOQL Query Exception Handling

Source: https://github.com/beyond-the-cloud-dev/soql-lib/blob/main/website/docs/soql/advanced/mocking.md

Illustrates that mocked queries in SOQL Lib count towards the SOQL query limit, throwing a 'QueryException: Too many SOQL queries.' if the limit is exceeded, mirroring Salesforce's native behavior.

```apex
QueryException: Too many SOQL queries.
```

### Queries Issued Count

Source: https://github.com/beyond-the-cloud-dev/soql-lib/blob/main/website/docs/soql/advanced/mocking.md

Mocked queries in SOQL Lib are counted towards the SOQL query limit, just like real queries. If the number of issued queries exceeds the limit, SOQL Lib will throw a QueryException: Too many SOQL queries. This behavior is consistent with Salesforce’s native limits, ensuring that your unit tests accurately reflect potential production scenarios.

--------------------------------

### SOQL Lib Critique > Additional Processing Time

Source: https://github.com/beyond-the-cloud-dev/soql-lib/blob/main/website/src/pages/critique.md

SOQL Lib constructs query strings and utilizes the `Database.queryWithBinds` method. Performance tests indicate that building complex queries dynamically with SOQL Lib takes less than 2ms, and simple queries take around 1ms. Even with 100 complex queries in a transaction, SOQL Lib uses approximately 200ms of the available 10,000ms CPU limit.
