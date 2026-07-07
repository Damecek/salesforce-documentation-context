# Q6: How do I write a multiline string literal in Apex, and can I use the null coalescing operator?

## Approach: A_salesforce-docs-mcp
- latency: 1909 ms

---

{
  "chunks": [
    {
      "content": "Code context:\nUnlike regular Apex strings, multiline strings also support unescaped single quotes (`'`). However, to use a single quote directly before the closing single quotes ( `'' '`), first escape the single quote. (`\\ '' ''`). For example, the second single quote in this multiline string requires an escape character, whereas the first one doesn’t.\n\n```\nString str = '''\n    I want a single quote here '\n    And also right before the string ends\\'''';\n```",
      "score": 0.741678551335433,
      "documentPath": "apexcode/langCon_apex_primitives.html",
      "url": "https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/langCon_apex_primitives.htm",
      "chunkIndex": 17,
      "metadata": {
        "title": "Primitive Data Types",
        "app_area": "apexcode"
      },
      "collection": "legacydeveloper/apexcode"
    },
    {
      "content": "Multiline String Usage\n\nUnlike regular Apex strings, multiline strings also support unescaped single quotes (`'`). However, to use a single quote directly before the closing single quotes ( `'' '`), first escape the single quote. (`\\ '' ''`). For example, the second single quote in this multiline string requires an escape character, whereas the first one doesn’t.",
      "score": 0.7372855450638454,
      "documentPath": "apexcode/langCon_apex_primitives.html",
      "url": "https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/langCon_apex_primitives.htm",
      "chunkIndex": 16,
      "metadata": {
        "title": "Primitive Data Types",
        "app_area": "apexcode"
      },
      "collection": "legacydeveloper/apexcode"
    },
    {
      "content": "Multiline String Usage\n\nEscape Sequences: Multiline strings support the same escape sequences as regular Apex strings.\n\nUse the `\\s` escape sequence at the end of a line to create intentional trailing whitespace. In this example, three trailing whitespace characters are preserved on the first and fifth lines of the string. The trailing whitespace on the third line of the string is stripped.",
      "score": 0.7308930812084453,
      "documentPath": "apexcode/langCon_apex_primitives.html",
      "url": "https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/langCon_apex_primitives.htm",
      "chunkIndex": 12,
      "metadata": {
        "title": "Primitive Data Types",
        "app_area": "apexcode"
      },
      "collection": "legacydeveloper/apexcode"
    },
    {
      "content": "Code context:\nEscape Sequences: Multiline strings support the same escape sequences as regular Apex strings.\n\nUse the `\\s` escape sequence at the end of a line to create intentional trailing whitespace. In this example, three trailing whitespace characters are preserved on the first and fifth lines of the string. The trailing whitespace on the third line of the string is stripped.\n\n```\nString str = '''\n. . . . . . . . <html> . . . . \\s\n. . . . . . . . . . . . <body>\n. . . . . . . . . . . . . . . . <p>Hello, world</p> . . . .\n. . . . . . . . . . . . </body>\n. . . . . . . . </html> . . . . \\s\n. . . . . . . .''';\n```",
      "score": 0.7232497169524276,
      "documentPath": "apexcode/langCon_apex_primitives.html",
      "url": "https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/langCon_apex_primitives.htm",
      "chunkIndex": 13,
      "metadata": {
        "title": "Primitive Data Types",
        "app_area": "apexcode"
      },
      "collection": "legacydeveloper/apexcode"
    },
    {
      "content": "While using the null coalescing operator, always keep operator precedence in mind. In some cases, using parentheses is necessary to obtain the desired results. For example, the expression `top ?? 100 - bottom ?? 0` evaluates to `top ?? (100 - bottom ?? 0)` and not to `(top ?? 100) - (bottom ?? 0)`.\n\nApex supports assignment of a single resultant record from a SOQL query, but throws an exception if there are no rows returned by the query. The null coalescing operator can be used to gracefully deal with the case where the query doesn’t return any rows. If a SOQL query is used as the left-hand operand of the operator and rows are returned, then the null coalescing operator returns the query results. If no rows are returned, the null coalescing operator returns the right-hand operand.\n\nWarning\n\nSalesforce recommends against using multiple SOQL queries in a single statement that also uses the null coalescing operator.\n\nThese examples work with Account objects.",
      "score": 0.7221754027709618,
      "documentPath": "apexcode/langCon_apex_NullCoalescingOperator.html",
      "url": "https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/langCon_apex_NullCoalescingOperator.htm",
      "chunkIndex": 3,
      "metadata": {
        "title": "Null Coalescing Operator",
        "app_area": "apexcode"
      },
      "collection": "legacydeveloper/apexcode"
    }
  ],
  "total": 5,
  "returned": 5,
  "metrics": {
    "queryTimeMs": 94,
    "searchMode": "auto (semantic)",
    "embeddingTimeMs": 28,
    "fallbackTriggered": false,
    "embeddingModel": "nomic"
  }
}
