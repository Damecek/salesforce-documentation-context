# Q5: How do I use the @future annotation for asynchronous Apex, and what are its restrictions?

## Approach: A_salesforce-docs-mcp
- latency: 1915 ms

---

{
  "chunks": [
    {
      "content": "[Note] If you set a checkpoint in a method with the [`@future` annotation](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_classes_annotation_future.htm), you must keep the Developer Console open until the `@future` method completes asynchronously.",
      "score": 0.8287428429740085,
      "documentPath": "admin/platform/260-0-0/code_dev_console_checkpoints_setting.html",
      "url": "https://help.salesforce.com/s/articleView?id=platform.code_dev_console_checkpoints_setting.htm&release=260&type=5",
      "chunkIndex": 3,
      "metadata": {
        "title": "Set Checkpoints in Apex Code",
        "app_area": "Platform",
        "breadcrumb_path": "Salesforce Help|Docs|Enhance Salesforce with Code"
      },
      "collection": "admin/platform"
    },
    {
      "content": "Future Annotation\n\nUse the `Future` annotation to identify methods that run asynchronously. A future method runs when Salesforce has available resources.\n\nImportant\n\nSalesforce now recommends that you use Queueable Apex instead of Apex future methods. Queueables have the same use cases as future methods but offer extra benefits, including job IDs, support for non-primitive types, and job chaining.\nSee [Queueable Apex](apex_queueing_jobs.htm).\n\nSee [Queueable Apex](apex_queueing_jobs.htm).\n\nFor example, you can use the `Future` annotation when making an asynchronous web service callout to an external service. Without the annotation, the web service callout is made from the same thread that is running the Apex code. Then no additional processing can occur until the callout is complete (synchronous processing).\n\nMethods with the `Future` annotation must be static methods, and can only return a void type. The specified parameters must be primitive data types, arrays of primitive data types, or collections of primitive data types. Methods with the `Future` annotation can’t take sObjects or objects as arguments.\n\nTo make a method in a class execute asynchronously, define the method with the `Future` annotation. For example:",
      "score": 0.7951059829936294,
      "documentPath": "apexcode/apex_classes_annotation_future.html",
      "url": "https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_classes_annotation_future.htm",
      "chunkIndex": 0,
      "metadata": {
        "title": "Future Annotation",
        "app_area": "apexcode"
      },
      "collection": "legacydeveloper/apexcode"
    },
    {
      "content": "Code context:\nSee [Queueable Apex](apex_queueing_jobs.htm).\n\nFor example, you can use the `Future` annotation when making an asynchronous web service callout to an external service. Without the annotation, the web service callout is made from the same thread that is running the Apex code. Then no additional processing can occur until the callout is complete (synchronous processing).\n\nMethods with the `Future` annotation must be static methods, and can only return a void type. The specified parameters must be primitive data types, arrays of primitive data types, or collections of primitive data types. Methods with the `Future` annotation can’t take sObjects or objects as arguments.\n\nTo make a method in a class execute asynchronously, define the method with the `Future` annotation. For example:\n\n```\npublic with sharing class MyFutureClass {\n\n    @Future \n    static void myMethod(String a, Integer i) {\n        System.debug('Method called with: ' + a + ' and ' + i);\n        // Perform long-running code\n    }\n}\n```",
      "score": 0.7805835997015108,
      "documentPath": "apexcode/apex_classes_annotation_future.html",
      "url": "https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_classes_annotation_future.htm",
      "chunkIndex": 1,
      "metadata": {
        "title": "Future Annotation",
        "app_area": "apexcode"
      },
      "collection": "legacydeveloper/apexcode"
    },
    {
      "content": "Future Method Limits\n\nMethods with the `Future` annotation have these limits.\n\n- No more than 0 in batch and future contexts; 50 in queueable context method calls per Apex invocation. Asynchronous calls, such as `Future` or `executeBatch`, that are called in a `startTest` or `stopTest` block don’t count against your limits for the number of queued jobs.\nNote\nHaving multiple future methods fan out from a queueable job isn’t a recommended practice as it can rapidly add many future methods to the asynchronous queue. Request processing can be delayed and you can quickly hit the daily maximum limit for asynchronous Apex method executions. See [Future Method Performance Best Practices](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_invoking_future_methods.htm) and [Lightning Platform Apex Limits](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_gov_limits.htm#in_topic_non_transactional_gov_limits_section).\n\nNote\n\n- The maximum number of `Future` method invocations per a 24-hour period is 250,000 or the number of user licenses in your organization multiplied by 200, whichever is greater. This limit is for your entire org and is shared with all asynchronous Apex: Batch Apex, Queueable Apex, scheduled Apex, and future methods. To check how many asynchronous Apex executions are available, make a request to REST API `limits` resource. See [List Organization Limits](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_rest.meta/api_rest/dome_limits.htm) in the [REST API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_rest.meta/api_rest/). If the number of asynchronous Apex executions needed by a job exceeds the available number that’s calculated by using the 24-hour rolling limit, an exception is thrown. For example, if your async job requires 10,000 method executions and the available 24-hour rolling limit is 9,500, you get the AsyncApexExecutions Limit exceeded exception. The license types that count toward this limit include full Salesforce and Salesforce Platform user licenses, App Subscription user licenses, Chatter Only users, Identity users, and Company Communities users.\n\n- The execution of a queued job counts one time against the shared limit for asynchronous Apex method executions. See [Salesforce Platform Apex Limits](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_gov_limits.htm).\n\n- You can process queueable jobs that exceed the daily shared limit for asynchronous Apex executions at a throttled rate. See [Elastic Limits for Asynchronous Apex Executions (Beta)](apex_limits_elastic_limits.htm).\n\nNote\n\nFuture jobs queued by a transaction aren’t processed if the transaction rolls back.\n\nFuture method jobs queued before a Salesforce service maintenance downtime remain in the queue. After service downtime ends and when system resources become available, the queued future method jobs are executed. If a future method was running when downtime occurred, the future method execution is rolled back and restarted after the service comes back up.\n\n- Future jobs queued by a transaction aren’t processed if the transaction rolls back.\n\n- Future method jobs queued before a Salesforce service maintenance downtime remain in the queue. After service downtime ends and when system resources become available, the queued future method jobs are executed. If a future method was running when downtime occurred, the future method execution is rolled back and restarted after the service comes back up.",
      "score": 0.7674179770297003,
      "documentPath": "apexcode/apex_invoking_future_methods.html",
      "url": "https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_invoking_future_methods.htm",
      "chunkIndex": 11,
      "metadata": {
        "title": "Future Methods",
        "app_area": "apexcode"
      },
      "collection": "legacydeveloper/apexcode"
    },
    {
      "content": "For more information, see [Handle Slack Actions](../build/actions.md).\n\nTo make a call to Slack from an Apex trigger, use the [`@future` annotation](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_classes_annotation_future.htm), queuable apex, or another [asynchronous method](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_async_overview.htm).",
      "score": 0.7599479532366127,
      "documentPath": "salesforce-slack-sdk/apex-slack-sdk/guides/apex_ref/apex_ref.html",
      "url": "https://developer.salesforce.com/docs/platform/salesforce-slack-sdk/guide/apex_ref.html",
      "chunkIndex": 2,
      "metadata": {
        "title": "Apex Reference for Slack",
        "app_area": "developer"
      },
      "collection": "developer/salesforce-slack-sdk"
    }
  ],
  "total": 5,
  "returned": 5,
  "metrics": {
    "queryTimeMs": 103,
    "searchMode": "auto (semantic)",
    "embeddingTimeMs": 66,
    "fallbackTriggered": false,
    "embeddingModel": "nomic"
  }
}
