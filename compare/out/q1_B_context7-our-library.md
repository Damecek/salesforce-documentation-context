# Q1: How do I write a SOQL query with a LIMIT clause in Apex, and what is the maximum LIMIT value?

## Approach: B_context7-our-library
- latency: 2939 ms
- libraryId: /damecek/salesforce-documentation-context

---

===============
LIBRARY RULES
===============
From library maintainers:
- Do not infer product behavior beyond what is stated in the markdown.
- Preserve product terminology as written in the source markdown.



### SOQL Query: Limit Clause

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/object-reference-for-the-salesforce-platform-part-13.md

Example of using the LIMIT clause in a SOQL query to restrict the number of returned records.

```soql
SELECT ExternalReferenceIdentifier FROM PendingOrderSummary WHERE
    ExternalReferenceIdentifier = 'a' LIMIT 1
```

--------------------------------

### SOQL Query with WHERE and LIMIT

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/soql-and-sosl-reference.md

Returns a specified number of Account records that match a given industry. This is a common use case for the LIMIT clause.

```soql
   SELECT Name

   FROM Account

   WHERE Industry = 'Media' LIMIT 125

```

--------------------------------

### SOQL Query with GROUP BY and LIMIT

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/soql-and-sosl-reference.md

This SOQL query is valid because it includes a GROUP BY clause when using a LIMIT clause with an aggregated function.

```soql
SELECT Name, Max(CreatedDate)

     FROM Account

     GROUP BY Name

     LIMIT 5
```

--------------------------------

### Query Specific Activities with Limits and Ordering

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/object-reference-for-the-salesforce-platform-part-12.md

This SOQL query retrieves a limited and ordered set of OpenActivities for a specific Account, demonstrating constraints on inner clauses.

```soql
SELECT
	(SELECT ActivityDate, Description
	 FROM OpenActivities
	 ORDER BY ActivityDate ASC NULLS LAST, LastModifiedDate DESC
	 LIMIT 500)
FROM Account
WHERE Name = 'Acme'
LIMIT 1
```

### Salesforce Object Query Language (SOQL) LIMIT > LIMIT Clause

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/soql-and-sosl-reference.md

The LIMIT clause in SOQL is an optional clause that can be added to a SELECT statement to specify the maximum number of rows to return. It can be used with the count() function to count up to a specified maximum, but cannot be used in queries with aggregate functions that do not use a GROUP BY clause.
