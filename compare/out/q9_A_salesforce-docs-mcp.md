# Q9: How do I get the list of picklist values for a given record type in Apex?

## Approach: A_salesforce-docs-mcp
- latency: 1747 ms

---

{
  "chunks": [
    {
      "content": "Extract Picklist Values Based on Record Type\n\nGet the values for all picklist fields for a particular record type by using the new `ConnectApi.RecordUi.getPicklistValuesByRecordType(objectApiName, recordTypeId)` method. We delivered this feature due to your idea on IdeaExchange.\n\nWhere:The feature is available in Lightning Experience and Salesforce Classic in Enterprise, Performance, Unlimited, and Developer editions.\n\nWhy:Previously, in Apex, you couldn't directly get picklist values that were specific to a record type without making callouts.\n\nHow:This method is especially useful for getting dependent picklist values. For example, if an object has a tree of dependent picklists, such as `Continents__c`, `Countries__c`, `Cities__c`, use this method to get all the values for each picklist in one request via the `ConnectApi.PicklistValuesCollection`.\n\nSee Also\n\n- [Idea Exchange: Getting Picklist values based on Record Type](https://ideas.salesforce.com/s/idea/a0B8W00000GdVwoUAF/getting-picklist-values-based-on-record-type)\n\n- [New Connect in Apex Classes](rn_connect_in_apex_classes.htm)\n\n- [Apex Reference Guide: getPicklistValuesByRecordType()](https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_ConnectAPI_RecordUi_static_methods.htm#apex_ConnectAPI_RecordUi_getPicklistValuesByRecordType_1)",
      "score": 0.8311234116554319,
      "documentPath": "admin/release-notes/260-0-0/rn_apex_extract_picklist_values.html",
      "url": "https://help.salesforce.com/s/articleView?id=release-notes.rn_apex_extract_picklist_values.htm&release=260&type=5",
      "chunkIndex": 0,
      "metadata": {
        "title": "Extract Picklist Values Based on Record Type",
        "app_area": "Cross Cloud Packages Solutions",
        "breadcrumb_path": "Salesforce Help|Docs|Salesforce Release Notes"
      },
      "collection": "admin/release-notes"
    },
    {
      "content": "Get Values for All Picklist Fields of a Record Type\n\nUse this resource to get the values for all the picklist fields of a specific record type. This resource is especially useful for getting dependent picklist values. For example, if an object has a tree of dependent picklists (Continents__c, Countries__c, Cities__c), use this resource to get all the values for each picklist in one request.\n\nThis resource is available as a static method in Apex in API version 66.0 and later. See [`getPicklistValuesByRecordType(objectApiName, recordTypeId)`](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_ConnectAPI_RecordUi_static_methods.htm#apex_ConnectAPI_RecordUi_getPicklistValuesByRecordType_1) in the Apex Reference Guide.\n\n- Resource: `objectApiName`—The API name of a [supported](ui_api_get_started_supported_objects.htm#ui_api_get_started_supported_objects) object.\n\n`recordTypeId`—The ID of the record type.\n- Available Version: 42.0\n- HTTP Method: GET\n- Response Body: [Picklist Values Collection](ui_api_responses_picklist_values_collection.htm#ui_api_responses_picklist_values_collection)",
      "score": 0.8204866158672218,
      "documentPath": "uiapi/ui_api_resources_picklist_values_collection.html",
      "url": "https://developer.salesforce.com/docs/atlas.en-us.uiapi.meta/uiapi/ui_api_resources_picklist_values_collection.htm",
      "chunkIndex": 0,
      "metadata": {
        "title": "Get Values for All Picklist Fields of a Record Type",
        "app_area": "uiapi"
      },
      "collection": "legacydeveloper/uiapi"
    },
    {
      "content": "Usage\n\nPicklist values are scoped to a record type. `getPicklistValuesByRecordType` returns a collection of picklist values for all of the picklists of a specified record type. For more information, see [Build UI for Picklists](https://developer.salesforce.com/docs/atlas.en-us.uiapi.meta/uiapi/ui_api_features_records_dependent_picklist.htm).\n\nTo retrieve picklist values for a specific field, use [`getPicklistValues`](reference-wire-adapters-picklist-values.md) instead.",
      "score": 0.8018584965551809,
      "documentPath": "lwc/lwc/guides/reference/wire-adapters/reference-wire-adapters-picklist-values-record.html",
      "url": "https://developer.salesforce.com/docs/platform/lwc/guide/reference-wire-adapters-picklist-values-record.html",
      "chunkIndex": 7,
      "metadata": {
        "title": "getPicklistValuesByRecordType",
        "app_area": "developer"
      },
      "collection": "developer/lwc"
    },
    {
      "content": "[Note] note: To retrieve all picklists of a record type, use [`getPicklistValuesByRecordType`](reference-wire-adapters-picklist-values-record.md) instead.",
      "score": 0.7939594510817869,
      "documentPath": "lwc/lwc/guides/reference/wire-adapters/reference-wire-adapters-picklist-values.html",
      "url": "https://developer.salesforce.com/docs/platform/lwc/guide/reference-wire-adapters-picklist-values.html",
      "chunkIndex": 9,
      "metadata": {
        "title": "getPicklistValues",
        "app_area": "developer"
      },
      "collection": "developer/lwc"
    },
    {
      "content": "Picklist\n\n- APEX Provided List of Values: You can retrieve the list of possible values for a picklist. The APEX callable classes are called to retrieve the values. In the `WizardComponent`metadata, specify from which APEX callable class and method we want to get the values from.",
      "score": 0.7904467111559697,
      "documentPath": "retail_api/metadata_components.html",
      "url": "https://developer.salesforce.com/docs/atlas.en-us.retail_api.meta/retail_api/metadata_components.htm",
      "chunkIndex": 32,
      "metadata": {
        "title": "Metadata Components",
        "app_area": "retail_api"
      },
      "collection": "legacydeveloper/retail_api"
    }
  ],
  "total": 5,
  "returned": 5,
  "metrics": {
    "queryTimeMs": 79,
    "searchMode": "auto (semantic)",
    "embeddingTimeMs": 36,
    "fallbackTriggered": false,
    "embeddingModel": "nomic"
  }
}
