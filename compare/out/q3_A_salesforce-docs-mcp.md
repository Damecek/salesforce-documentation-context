# Q3: What is the maximum number of SOQL queries allowed in a single synchronous Apex transaction?

## Approach: A_salesforce-docs-mcp
- latency: 1722 ms

---

{
  "chunks": [
    {
      "content": "For ‌best performance, Salesforce recommends limiting the total number of records retrieved by SOQL queries to 50,000 records per Apex transaction. See [Apex Governor Limits](https://developer.salesforce.com/docs/atlas.en-us.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_apexgov.htm).",
      "score": 0.8528464524241431,
      "documentPath": "admin/ind/260-0-0/netzero_manager_generate_esrs_report.html",
      "url": "https://help.salesforce.com/s/articleView?id=ind.netzero_manager_generate_esrs_report.htm&release=260&type=5",
      "chunkIndex": 5,
      "metadata": {
        "title": "Create ESRS Disclosures Report by Using the Net Zero Cloud Template",
        "app_area": "Net Zero Cloud",
        "breadcrumb_path": "Salesforce Help|Docs|Report and Reduce Your Carbon Footprint with Net Zero Cloud",
        "required_editions": "Available in: Lightning Experience; Available in: Enterprise, Performance, Unlimited, and Developer Editions with the Net Zero Cloud Growth license. To edit Word documents, you need a Microsoft 365 license",
        "available_editions": [
          "Enterprise",
          "Performance",
          "Unlimited",
          "Developer"
        ],
        "required_permissions": "To use the Disclosure and Compliance Hub: Disclosure and Compliance Hub User; To generate disclosure documents: Omnistudio Admin or Omnistudio User and DocGen Designer; To generate disclosure reports using the Disclosure and Compliance Hub plugin for Microsoft 365: Disclosure and Compliance Hub plugin for Microsoft 365",
        "available_experiences": [
          "Lightning Experience"
        ],
        "required_permission_names": [
          "Disclosure and Compliance Hub User",
          "Omnistudio Admin or Omnistudio User and DocGen Designer",
          "Disclosure and Compliance Hub plugin for Microsoft 365"
        ]
      },
      "collection": "admin/ind"
    },
    {
      "content": "[Note] Salesforce enforces a limit of 100 SOQL queries per Apex transaction. If you exceed this limit while extracting objects, the Data Mapper execution fails, and an error message is displayed. See [Per-Transaction Apex Limits](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_gov_limits.htm#in_topic_per_transaction_section).",
      "score": 0.8317706089156518,
      "documentPath": "admin/xcloud/260-0-0/os_define_the_initial_extraction_45906.html",
      "url": "https://help.salesforce.com/s/articleView?id=xcloud.os_define_the_initial_extraction_45906.htm&release=260&type=5",
      "chunkIndex": 4,
      "metadata": {
        "title": "Configure an Omnistudio Data Mapper Extract",
        "app_area": "Omnistudio",
        "breadcrumb_path": "Salesforce Help|Docs|Omnistudio"
      },
      "collection": "admin/xcloud"
    },
    {
      "content": "| Description | Limit |\n| --- | --- |\n| Default timeout of callouts (HTTP requests or Web services calls) in a transaction | 10 seconds |\n| Maximum size of callout request or response (HTTP request or Web services call)^1 | 6 MB for synchronous Apex or 12 MB for asynchronous Apex |\n| Maximum SOQL query run time before Salesforce cancels the transaction | 120 seconds |\n| Maximum number of class and trigger code units in a deployment of Apex | 7500 |\n| Apex trigger batch size^2 | 200 |\n| For loop list batch size | 200 |\n| Maximum number of records returned for a Batch Apex query in `Database.QueryLocator` | 50 million |",
      "score": 0.8096241468415187,
      "documentPath": "apexcode/apex_gov_limits.html",
      "url": "https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_gov_limits.htm",
      "chunkIndex": 10,
      "metadata": {
        "title": "Execution Governors and Limits",
        "app_area": "apexcode"
      },
      "collection": "legacydeveloper/apexcode"
    },
    {
      "content": "| Description | Limit |\n| --- | --- |\n| Default timeout of callouts (HTTP requests or Web services calls) in a transaction | 10 seconds |\n| Maximum size of callout request or response (HTTP request or Web services call)^1 | 6 MB for synchronous Apex or 12 MB for asynchronous Apex |\n| Maximum SOQL query run time before Salesforce cancels the transaction | 120 seconds |\n| Maximum number of class and trigger code units in a deployment of Apex | 7500 |\n| Apex trigger batch size^2 | 200 |\n| For loop list batch size | 200 |\n| Maximum number of records returned for a Batch Apex query in `Database.QueryLocator` | 50 million |",
      "score": 0.8096241468415187,
      "documentPath": "salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_apexgov.html",
      "url": "https://developer.salesforce.com/docs/atlas.en-us.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_apexgov.htm",
      "chunkIndex": 10,
      "metadata": {
        "title": "Apex Governor Limits",
        "app_area": "salesforce_app_limits_cheatsheet"
      },
      "collection": "legacydeveloper/salesforce_app_limits_cheatsheet"
    },
    {
      "content": "| Description | Limit |\n| --- | --- |\n| Default timeout of callouts (HTTP requests or Web services calls) in a transaction | 10 seconds |\n| Maximum size of callout request or response (HTTP request or Web services call)^1 | 6 MB for synchronous Apex or 12 MB for asynchronous Apex |\n| Maximum SOQL query run time before Salesforce cancels the transaction | 120 seconds |\n| Maximum number of class and trigger code units in a deployment of Apex | 7500 |\n| Apex trigger batch size^2 | 200 |\n| For loop list batch size | 200 |\n| Maximum number of records returned for a Batch Apex query in `Database.QueryLocator` | 50 million |",
      "score": 0.8096241468415187,
      "documentPath": "pages/pages_apex_governor_limits.html",
      "url": "https://developer.salesforce.com/docs/atlas.en-us.pages.meta/pages/pages_apex_governor_limits.htm",
      "chunkIndex": 10,
      "metadata": {
        "title": "Execution Governors and Limits",
        "app_area": "pages"
      },
      "collection": "legacydeveloper/pages"
    }
  ],
  "total": 5,
  "returned": 5,
  "metrics": {
    "queryTimeMs": 68,
    "searchMode": "auto (semantic)",
    "embeddingTimeMs": 59,
    "fallbackTriggered": false,
    "embeddingModel": "nomic"
  }
}
