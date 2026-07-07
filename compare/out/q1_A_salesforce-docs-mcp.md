# Q1: How do I write a SOQL query with a LIMIT clause in Apex, and what is the maximum LIMIT value?

## Approach: A_salesforce-docs-mcp
- latency: 2062 ms

---

{
  "chunks": [
    {
      "content": "LIMIT\n\n`LIMIT` is an optional clause that can be added to a `SELECT` statement of a SOQL query to specify the maximum number of rows to return.\n\nThe syntax for `LIMIT` is:",
      "score": 0.8274335676590278,
      "documentPath": "soql_sosl/sforce_api_calls_soql_select_limit.html",
      "url": "https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_select_limit.htm",
      "chunkIndex": 0,
      "metadata": {
        "title": "LIMIT",
        "app_area": "soql_sosl"
      },
      "collection": "legacydeveloper/soql_sosl"
    },
    {
      "content": "| Feature | Limit | Limit Description |\n| --- | --- | --- |\n| SOQL statements | Maximum length of SOQL statements | By default, 100,000 characters. For details on SOQL statement limits, including information on queries that involve external objects, see [Understanding Relationship Query Limitations](https://developer.salesforce.com/docs/atlas.en-us.262.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_relationships_query_limits.htm).<br>Long, complex SOQL statements, such as statements that contain many formula fields, can result in a `QUERY_TOO_COMPLICATED` error. The error occurs because the statement is expanded internally when processed by Salesforce, even though the original SOQL statement is under the 100,000 character limit. To avoid this error, reduce the complexity of your SOQL statement.<br><br>Page layouts in Lightning with more than 250 fields can also cause a `QUERY_TOO_COMPLICATED` error. Lightning uses auto-generated SOQL to retrieve fields for a record page layout, so the error can occur even if there isn’t any customer-written SOQL.<br><br>The character limit can also be reached by including too many currency fields. Currency fields require SOQL to use a format method, roughly doubling the field API name length for each currency field.<br><br>The SOQL statement character limit does not apply when using SOQL with dynamic Apex. |\n| SOQL statements | Maximum number of junction IDs | 500 IDs per query. If a query includes 501 or more junction IDs, the query fails and returns the MALFORMED_QUERY exception. |\n| SOQL `WHERE` clause | Strings in SOQL `WHERE` clauses | 4,000 characters for each string within a `WHERE` clause. |\n| SOQL query results | Maximum rows returned | 2,000 results per request (API version 28.0 and later), unless you specify custom limits in the query. This limit includes results from child objects. Previous API versions return 200 results. When a query is executed from within an Apex class, additional limits apply. See [Apex Governor Limits](https://developer.salesforce.com/docs/atlas.en-us.262.0.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_apexgov.htm) for more information. |\n| SOQL query results | Availability | 2 days, including results in nested queries. |\n| SOQL query timeout | Maximum runtime for a SOQL query | 32 minutes total for both executing the operation and processing the results, but a query can time out at either the execution or processing stage. A query operation has 2 minutes to execute and 30 minutes to process results before timeout occurs. |\n| SOSL statements | Maximum length of SOSL statements | By default, 100,000 characters. This limit is tied to the SOQL statement character limit defined for your org. |\n| SOSL search query strings | Maximum length of `SearchQuery` string | If the `SearchQuery` string is longer than 10,000 characters, no result rows are returned. If `SearchQuery` is longer than 4,000 characters, any logical operators are removed. For example, the `AND` operator in a statement with a `SearchQuery` that’s 4,001 characters defaults to the `OR` operator, which could return more results than expected. |\n| SOSL query results | Maximum rows returned | 2,000 results total (API version 28.0 and later), unless you specify custom limits in the query. This limit includes results from child objects. Previous API versions return 200 results. |\n| Relationship queries | Relationship query limits | No more than 55 child-to-parent relationships can be specified in a query. A custom object allows up to 40 relationships, so you can reference all the child-to-parent relationships for a custom object in one query.<br><br>A single query of polymorphic fields can count multiple times against the child-to-parent relationship limit. For more information, see [Understanding Relationship Query Limitations](https://developer.salesforce.com/docs/atlas.en-us.262.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_relationships_query_limits.htm).<br><br>No more than 20 parent-to-child relationships can be specified in a query.<br><br>In each specified relationship, no more than five levels can be specified in a child-to-parent relationship. For example, `Contact.Account.Owner.FirstName` (three levels).<br><br>In API version 57.0 and earlier, only two levels of parent-to-child relationship can be specified in a query.<br><br>In API version 58.0 and later, up to five levels of parent-to-child relationship can be queried via REST, SOAP, and Apex query calls for standard and custom objects. SOQL queries with five-level parent-to-child relationships aren't supported for big objects, external objects, or Bulk API and Bulk API 2.0. |\n| FOR VIEW and FOR REFERENCE | Maximum RecentlyViewed records allowed | The RecentlyViewed object is updated every time the logged-in user views or references a record. It is also updated when records are retrieved using the `FOR VIEW` or `FOR REFERENCE` clause in a SOQL query. To ensure that the most recent data is available, RecentlyViewed data is periodically truncated down to 200 records per object. RecentlyViewed data is retained for 90 days, after which it is removed on a periodic basis. |\n| OFFSET clause | Maximum number of rows skipped by OFFSET | The maximum offset is 2,000 rows. Requesting an offset greater than 2,000 results in a `NUMBER_OUTSIDE_VALID_RANGE` error. |\n| ORDER BY clause in SOQL statement | ORDER BY fields limit | The `ORDER BY` clause in the `SELECT` statement of a SOQL query controls the order of the query results, such as alphabetically beginning with z. If records are null, you can use `ORDER<br>BY` to display the empty records first or last. |",
      "score": 0.818799907326739,
      "documentPath": "salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_soslsoql.html",
      "url": "https://developer.salesforce.com/docs/atlas.en-us.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_soslsoql.htm",
      "chunkIndex": 0,
      "metadata": {
        "title": "SOQL and SOSL Limits for Search Queries",
        "app_area": "salesforce_app_limits_cheatsheet"
      },
      "collection": "legacydeveloper/salesforce_app_limits_cheatsheet"
    },
    {
      "content": "LIMIT n\n\n`LIMIT` is an optional clause that can be added to a SOSL query to specify the maximum number of rows that are returned in the text query, which can be up to 2,000 results. If unspecified, the default is the maximum 2,000 results.\n\nThe default of 2,000 results is the largest number of rows that can be returned for API version 28.0 and later. Previous versions return up to 200 results.\n\nThe LIMIT clause can’t increase the maximum number of records returned. See [SOSL Limits on Search Results](https://developer.salesforce.com/docs/atlas.en-us.262.0.soql_sosl.meta/soql_sosl/sforce_api_calls_sosl_limits.htm).\n\nYou can set limits on individual objects or on an entire query.\n\nWhen you set a limit on the entire query, results are evenly distributed among the objects returned. For example, let’s say you set an overall query limit of 20 and don’t define any limits on individual objects. If 19 of the results are accounts and 35 are contacts, then only 10 accounts and 10 contacts are returned.",
      "score": 0.8172522514011773,
      "documentPath": "soql_sosl/sforce_api_calls_sosl_limit.html",
      "url": "https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_sosl_limit.htm",
      "chunkIndex": 0,
      "metadata": {
        "title": "LIMIT n",
        "app_area": "soql_sosl"
      },
      "collection": "legacydeveloper/soql_sosl"
    },
    {
      "content": "Code context:\n`LIMIT` is an optional clause that can be added to a `SELECT` statement of a SOQL query to specify the maximum number of rows to return.\n\nThe syntax for `LIMIT` is:\n\n```soql\nSELECT fieldList\nFROM objectType\n[WHERE conditionExpression] \n  [LIMIT numberOfRows]\n```",
      "score": 0.8107138131347379,
      "documentPath": "soql_sosl/sforce_api_calls_soql_select_limit.html",
      "url": "https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_select_limit.htm",
      "chunkIndex": 1,
      "metadata": {
        "title": "LIMIT",
        "app_area": "soql_sosl"
      },
      "collection": "legacydeveloper/soql_sosl"
    },
    {
      "content": "Code context:\nThis query returns the first 125 Account records whose Industry is `Media`.\n\nYou can use `LIMIT` with `count()` as the `fieldList` to count up to the maximum specified.\n\nYou can't use a `LIMIT` clause in a query that uses an aggregate function, but does not use a `GROUP BY` clause. For example, the following query is invalid:\n\n```soql\nSELECT MAX(CreatedDate)\nFROM Account LIMIT 1\n```",
      "score": 0.8049058427113316,
      "documentPath": "soql_sosl/sforce_api_calls_soql_select_limit.html",
      "url": "https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_select_limit.htm",
      "chunkIndex": 4,
      "metadata": {
        "title": "LIMIT",
        "app_area": "soql_sosl"
      },
      "collection": "legacydeveloper/soql_sosl"
    }
  ],
  "total": 5,
  "returned": 5,
  "metrics": {
    "queryTimeMs": 119,
    "searchMode": "auto (semantic)",
    "embeddingTimeMs": 107,
    "fallbackTriggered": false,
    "embeddingModel": "nomic"
  }
}
