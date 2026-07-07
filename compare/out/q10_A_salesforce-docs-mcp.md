# Q10: How do I use the Flow Transform element, and what advantages does it have over a Flow Loop?

## Approach: A_salesforce-docs-mcp
- latency: 2372 ms

---

{
  "chunks": [
    {
      "content": "Transform Element\n\nSelect the flow resources for mapping and transforming source data to target data. You can use the Transform element in screen flows, autolaunched flows with no triggers, and record-triggered flows.",
      "score": 0.7484628631290403,
      "documentPath": "admin/platform/260-0-0/flow_ref_elements_transform.html",
      "url": "https://help.salesforce.com/s/articleView?id=platform.flow_ref_elements_transform.htm&release=260&type=5",
      "chunkIndex": 0,
      "metadata": {
        "title": "Transform Element",
        "app_area": "Flow Builder",
        "breadcrumb_path": "Salesforce Help|Docs|Automate Your Business Processes",
        "required_editions": "[View supported editions.](flow_ref_supported_editions.htm)"
      },
      "collection": "admin/platform"
    },
    {
      "content": "See Also\n\n- [Transform Element](flow_ref_elements_transform.htm)\n\n- [Connecting to an API Without a Connector Using HTTP Callout](flow_http_callout.htm)\n\n- [Sum or Count Items in Collections with the Transform Element](flow_build_logic_transform_sum_or_count.htm)",
      "score": 0.7122784297715242,
      "documentPath": "admin/platform/260-0-0/flow_build_logic_transform.html",
      "url": "https://help.salesforce.com/s/articleView?id=platform.flow_build_logic_transform.htm&release=260&type=5",
      "chunkIndex": 5,
      "metadata": {
        "title": "Transform Data in a Flow",
        "app_area": "Flow Builder",
        "breadcrumb_path": "Salesforce Help|Docs|Automate Your Business Processes",
        "required_editions": "[View supported editions.](flow_ref_supported_editions.htm)",
        "required_permissions": "To open, edit, create, activate or deactivate a flow using all flow types, elements, and features available in Flow Builder, including Einstein and Agentforce for Flow: Manage Flow",
        "required_permission_names": [
          "Manage Flow"
        ]
      },
      "collection": "admin/platform"
    },
    {
      "content": "A flow approval process can contain Decision elements and Stage elements, but there’s no Loop element like there is for a flow. Instead, to repeat a sequence of one or more elements in a flow approval process, use Go To connectors.\n\nTo add a Go To connector, you must have at least 2 elements in your flow approval process.\n\n1. Directly after the element that you want to change the connector for, click [Image: ../images/flow_builder_new_plus_sign_icon.png](https://sf-zdocs-cdn-prod.zoominsoftware.com/tdta-platform_automation-260-0-0-production-enus/d37a74fb-154b-4def-9acf-bf1572b40109/platform_automation/images/orchestration/orchestrator_fbuilder_circleplus.png).\n\n2. Click `Connect to element`.\n\n3. Click [Image: plus sign on an element in the connect to element mode](https://sf-zdocs-cdn-prod.zoominsoftware.com/tdta-platform_automation-260-0-0-production-enus/d37a74fb-154b-4def-9acf-bf1572b40109/platform_automation/images/flow_builder_element_plus_sign_for_connector.png) on the element that you want to connect to.\n\nThe original element has a dotted line connection to the specified element.",
      "score": 0.7087695462658329,
      "documentPath": "admin/platform/260-0-0/automate_automated_approvals_build_logic_route.html",
      "url": "https://help.salesforce.com/s/articleView?id=platform.automate_automated_approvals_build_logic_route.htm&release=260&type=5",
      "chunkIndex": 3,
      "metadata": {
        "title": "Control Which Element Runs Next in a Flow Approval Process",
        "app_area": "Flow Builder",
        "breadcrumb_path": "Salesforce Help|Docs|Automate Your Business Processes",
        "required_editions": "[View supported editions for Flow Approval Processes.](automate_automated_approvals_about_supported_editions.htm)",
        "required_permissions": "To open, edit, or create a flow approval process in Flow Builder: Manage Flow",
        "required_permission_names": [
          "Manage Flow"
        ]
      },
      "collection": "admin/platform"
    },
    {
      "content": "Watch this demo (English only) of transforming data in Flow Builder.\n\n[Embedded media: video](https://play.vidyard.com/qVDjGpPHCncKNrwKZ5JoB4)\n\nFor another viewing option, see [Transform Your Data with Flow Builder (English Only)](https://salesforce.vidyard.com/watch/qVDjGpPHCncKNrwKZ5JoB4).\n\nBefore you begin, understand the structure of your source and target data, such as whether the data contains multiple levels of collections within other collections. Mapping fields in a collection requires rules to preserve data integrity. See [Transform Element](flow_ref_elements_transform.htm).\n\n1. Add the Transform element to your flow.\n\n1.1. Enter the label, API name, and description.\n\n1.2. For Source Data, click the Add Resource button [Image: Add Resource button](https://sf-zdocs-cdn-prod.zoominsoftware.com/tdta-platform_automation-260-0-0-production-enus/d37a74fb-154b-4def-9acf-bf1572b40109/platform_automation/images/flow/flow_transform_add_resource.png) and select the flow resource to transform the data.\n\n1.3. For Target Data, click the Add Resource button [Image: Add Resource button](https://sf-zdocs-cdn-prod.zoominsoftware.com/tdta-platform_automation-260-0-0-production-enus/d37a74fb-154b-4def-9acf-bf1572b40109/platform_automation/images/flow/flow_transform_add_resource.png) and select the data type.\n\n1.4. If the target data is a collection, select `Allow multiple values\n(collection)`.\n\n1.5. If the data type is a record or Apex-defined, select the Apex class or object for the target data that the Transform element generates.\nFor example, if you specified that the target data is a collection and that the record data type is the Account object, the Transform element generates an account collection. If you didn’t specify a collection, the target data is a single account.\n\n2. Map the source and target data.\nThe Transform element adds a dashed line to indicate mappings within a collapsed object or collection. The Transform element adds dotted lines to identify the collections that contain the mapped fields so that you can easily view the collections in both resource data structures. When mapping fields in a collection, the source and target fields must be at the same hierarchical level in their respective resources. See [Flow Element: Transform](flow_ref_elements_transform.htm).\n\n2.1. Hover over a source data field and click the Map button [Image: Circled bullet](https://sf-zdocs-cdn-prod.zoominsoftware.com/tdta-platform_automation-260-0-0-production-enus/d37a74fb-154b-4def-9acf-bf1572b40109/platform_automation/images/flow/flow_transform_circled_bullet_blue.png).\n\n2.2. Next to a target data field, click the Map button [Image: Circled bullet](https://sf-zdocs-cdn-prod.zoominsoftware.com/tdta-platform_automation-260-0-0-production-enus/d37a74fb-154b-4def-9acf-bf1572b40109/platform_automation/images/flow/flow_transform_circled_bullet_blue.png).\nIf a target field doesn’t have the Map button [Image: Map icon](https://sf-zdocs-cdn-prod.zoominsoftware.com/tdta-platform_automation-260-0-0-production-enus/d37a74fb-154b-4def-9acf-bf1572b40109/platform_automation/images/flow/flow_transform_circled_bullet_blue.png), you can’t map to it.\n\n2.3. To view a mapping tip next to a target field or collection that’s unavailable for mapping, hover over the target field or collection, and then hover over the error icon.\n[Image: Mapping tip of an unavaiable target field in Transform element](https://sf-zdocs-cdn-prod.zoominsoftware.com/tdta-platform_automation-260-0-0-production-enus/d37a74fb-154b-4def-9acf-bf1572b40109/platform_automation/images/flow/flow_builder_transform_mapping_tip.png)\n\n2.4. To view a mapping tip of a misconfiguration error, hover over the error icon [Image: Error icon](https://sf-zdocs-cdn-prod.zoominsoftware.com/tdta-platform_automation-260-0-0-production-enus/d37a74fb-154b-4def-9acf-bf1572b40109/platform_automation/images/flow/flow_builder_transform_error_icon_red.png) shown next to a target data field or collection.\n[Image: Mapping tip of misconfiguration error in Transform element](https://sf-zdocs-cdn-prod.zoominsoftware.com/tdta-platform_automation-260-0-0-production-enus/d37a74fb-154b-4def-9acf-bf1572b40109/platform_automation/images/flow/flow_builder_transform_error_tip.png)\n\n3. To transform data with a formula, click the mapped field name, and then click [Image: Formula button](https://sf-zdocs-cdn-prod.zoominsoftware.com/tdta-platform_automation-260-0-0-production-enus/d37a74fb-154b-4def-9acf-bf1572b40109/platform_automation/images/flow/flow_transform_fx_gray.png) then `Formula`.\n\n4. To delete a mapping, click the field name, and then click the Delete button [Image: Delete button](https://sf-zdocs-cdn-prod.zoominsoftware.com/tdta-platform_automation-260-0-0-production-enus/d37a74fb-154b-4def-9acf-bf1572b40109/platform_automation/images/flow/flow_transform_delete_gray.png).\nAfter you finish transforming data, you can save the target data to Salesforce or to an external system.\n\nTo save the target data to Salesforce, add the Update Records element, and then configure it to reference the resource with the same name as the Transform element. For example, if the API name of the Transform element is Return_Order, select Return_Order for Record or Record Collection in the Update Records element.\n\nTo save the target data to an external system, create an HTTP callout action that uses a method like POST.",
      "score": 0.7014458032616683,
      "documentPath": "admin/platform/260-0-0/flow_build_logic_transform.html",
      "url": "https://help.salesforce.com/s/articleView?id=platform.flow_build_logic_transform.htm&release=260&type=5",
      "chunkIndex": 3,
      "metadata": {
        "title": "Transform Data in a Flow",
        "app_area": "Flow Builder",
        "breadcrumb_path": "Salesforce Help|Docs|Automate Your Business Processes",
        "required_editions": "[View supported editions.](flow_ref_supported_editions.htm)",
        "required_permissions": "To open, edit, create, activate or deactivate a flow using all flow types, elements, and features available in Flow Builder, including Einstein and Agentforce for Flow: Manage Flow",
        "required_permission_names": [
          "Manage Flow"
        ]
      },
      "collection": "admin/platform"
    },
    {
      "content": "Before you begin, understand the structure of your source and target data, such as whether the data contains multiple levels of collections within other collections. Mapping fields in a collection requires rules to preserve data integrity. See [Flow Element: Transform](flow_ref_elements_transform.htm).\n\nCount the number of items in a source collection, or add the field values on each item in the source collection to calculate their sum.\n\n1. Add the Transform element to your flow.\n\n1.1. Enter the label, API name, and description.\n\n1.2. For Source Data, click the Add Resource button [Image: Add Resource button](https://sf-zdocs-cdn-prod.zoominsoftware.com/tdta-platform_automation-260-0-0-production-enus/d37a74fb-154b-4def-9acf-bf1572b40109/platform_automation/images/flow/flow_transform_add_resource.png) and select the flow resource to transform the data.\nSelect a resource that references a collection to aggregate.\n\n1.3. For Target Data, click the Add Resource button [Image: Add Resource button](https://sf-zdocs-cdn-prod.zoominsoftware.com/tdta-platform_automation-260-0-0-production-enus/d37a74fb-154b-4def-9acf-bf1572b40109/platform_automation/images/flow/flow_transform_add_resource.png) and select the data type.\n\n1.4. If the target data is a collection, select `Allow multiple values\n(collection)`.\n\n1.5. For a Record or Apex-Defined data type, select the Apex class or object for the target data that the Transform element generates.\nFor example, if you specified that the target data is a collection and that the record data type is the Account object, the Transform element generates an account collection. If you didn’t specify a collection, the target data is a single account.\n\n2. Map the source collection to the target data field that’s a Number data type.\n\n2.1. Hover over a source collection and click the Map button [Image: Circled bullet](https://sf-zdocs-cdn-prod.zoominsoftware.com/tdta-platform_automation-260-0-0-production-enus/d37a74fb-154b-4def-9acf-bf1572b40109/platform_automation/images/flow/flow_transform_circled_bullet_blue.png).\n\n2.2. Next to a target data field that’s a Number data type, click the Map button [Image: Circled bullet](https://sf-zdocs-cdn-prod.zoominsoftware.com/tdta-platform_automation-260-0-0-production-enus/d37a74fb-154b-4def-9acf-bf1572b40109/platform_automation/images/flow/flow_transform_circled_bullet_blue.png).\nIf a target field doesn’t have the Map button [Image: Circled bullet](https://sf-zdocs-cdn-prod.zoominsoftware.com/tdta-platform_automation-260-0-0-production-enus/d37a74fb-154b-4def-9acf-bf1572b40109/platform_automation/images/flow/flow_transform_circled_bullet_blue.png), you can’t map to it. When mapping fields in a collection, the source and target fields must be at the same hierarchical level in their respective resources. See [Flow Element: Transform](flow_ref_elements_transform.htm).\n\n3. For Aggregate Type, select `Count` or `Sum`.\n\n4. For Field to Transform, select the source data field on each item in the source collection to calculate the transformed value.\nThis field is available only for the sum aggregate type.\n\n5. Save your flow.",
      "score": 0.6965041213937023,
      "documentPath": "admin/platform/260-0-0/flow_build_logic_transform_sum_or_count.html",
      "url": "https://help.salesforce.com/s/articleView?id=platform.flow_build_logic_transform_sum_or_count.htm&release=260&type=5",
      "chunkIndex": 3,
      "metadata": {
        "title": "Sum or Count Items in Collections with the Transform Element",
        "app_area": "Flow Builder",
        "breadcrumb_path": "Salesforce Help|Docs|Automate Your Business Processes",
        "required_editions": "[View supported editions.](flow_ref_supported_editions.htm)",
        "required_permissions": "To open, edit, create, activate or deactivate a flow using all flow types, elements, and features available in Flow Builder, including Einstein and Agentforce for Flow: Manage Flow",
        "required_permission_names": [
          "Manage Flow"
        ]
      },
      "collection": "admin/platform"
    }
  ],
  "total": 5,
  "returned": 5,
  "metrics": {
    "queryTimeMs": 75,
    "searchMode": "auto (semantic)",
    "embeddingTimeMs": 26,
    "fallbackTriggered": false,
    "embeddingModel": "nomic"
  }
}
