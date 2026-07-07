# Q4: How do I create a record-triggered flow that runs after a record is saved?

## Approach: A_salesforce-docs-mcp
- latency: 1989 ms

---

{
  "chunks": [
    {
      "content": "Create a Simple After-Save Record-Triggered Flow\n\nLearn how to build an after-save record-triggered flow that automatically creates a record. This example creates a follow-up task whenever a user creates a lead record, ensuring your team never misses an important next step.",
      "score": 0.8159139108914533,
      "documentPath": "admin/platform/260-0-0/automate_flow_build_get_started_record_triggered_example_create_record.html",
      "url": "https://help.salesforce.com/s/articleView?id=platform.automate_flow_build_get_started_record_triggered_example_create_record.htm&release=260&type=5",
      "chunkIndex": 0,
      "metadata": {
        "title": "Create a Simple After-Save Record-Triggered Flow",
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
      "content": "Create a Record-Triggered Flow\n\nConfigure the initial trigger and entry conditions for the order object.\n\n1. From Setup, in the Quick Find box, enter `Flows`, and then select `Flows`.\n\n2. Click `New Flow`.\n\n3. Select `Start from Scratch` and click `Next`.\n\n4. Select `Record-Triggered Flow` and click `Create`.\n\n5. Select `Order` as the object.\n\n6. Select `A record is updated` for the trigger configuration.\n\n7. In the Set Entry Conditions section, specify these details.\n\n- Condition Requirements: `All Conditions Are Met\n(AND)`\n\n- Field: `Status`\n\n- Operator: `Equals`\n\n- Value: `Activated`\n\n8. Select `Only when a record is updated to meet the condition\nrequirements` for the run frequency.",
      "score": 0.7994740963922922,
      "documentPath": "admin/ind/260-0-0/qocal_example_automate_order_submission_for_fulfillment.html",
      "url": "https://help.salesforce.com/s/articleView?id=ind.qocal_example_automate_order_submission_for_fulfillment.htm&release=260&type=5",
      "chunkIndex": 3,
      "metadata": {
        "title": "Example: Automate Order Submission for Fulfillment",
        "app_area": "Revenue Cloud",
        "breadcrumb_path": "Salesforce Help|Docs|Revenue Cloud",
        "required_editions": "Available in: Lightning Experience; Available in: Enterprise, Unlimited, and Developer Editions of Revenue Cloud where Transaction Management is enabled",
        "available_editions": [
          "Enterprise",
          "Unlimited",
          "Developer"
        ],
        "required_permissions": "To open, edit, or create a flow in Flow Builder: Manage Flow; To submit orders to Dynamic Revenue Orchestrator and call the invocable actions: Submit Transaction User",
        "available_experiences": [
          "Lightning Experience"
        ],
        "required_permission_names": [
          "Manage Flow",
          "Submit Transaction User"
        ]
      },
      "collection": "admin/ind"
    },
    {
      "content": "Create a Record-Triggered Flow\n\n1. From Setup, in the Quick Find box, enter `Flows`, and then select `Flows`.\n\n2. Click `New Flow`.\n\n3. Select `Record-Triggered Flow` and click `Create`.\n\n4. Select `Order` as the object.\n\n5. Select `A record is updated` for the trigger configuration.\n\n6. In the Set Entry Conditions section, specify these details.\n\n- Condition Requirements: `All Conditions Are Met\n(AND)`\n\n- Field: `Status`\n\n- Operator: `Equals`\n\n- Value: `Activated`",
      "score": 0.7980791215708193,
      "documentPath": "admin/ind/260-0-0/qocal_automate_creation_and_update_of_assets.html",
      "url": "https://help.salesforce.com/s/articleView?id=ind.qocal_automate_creation_and_update_of_assets.htm&release=260&type=5",
      "chunkIndex": 4,
      "metadata": {
        "title": "Automate Asset Creation from Orders",
        "app_area": "Revenue Cloud",
        "breadcrumb_path": "Salesforce Help|Docs|Revenue Cloud",
        "required_editions": "Available in: Lightning Experience; Available in: Enterprise, Unlimited, and Developer Editions of Revenue Cloud where Transaction Management is enabled",
        "available_editions": [
          "Enterprise",
          "Unlimited",
          "Developer"
        ],
        "required_permissions": "To open, edit, or create a flow in Flow Builder: Manage Flow; To activate object state definitions: Assetize Order permission set",
        "available_experiences": [
          "Lightning Experience"
        ],
        "required_permission_names": [
          "Manage Flow",
          "Assetize Order"
        ]
      },
      "collection": "admin/ind"
    },
    {
      "content": "What's Next\n\nYou've built an after-save record-triggered flow that automatically creates a record. Now, whenever anyone creates a lead, your flow creates a follow-up task automatically—no manual work required.\n\nYou learned important new skills:\n\n- Creating an after-save record-triggered flow.\n\n- Using the Create Records element to create a record.\n\n- Setting field values on the new record, including references to the triggering record.\n\n- Creating a simple formula to calculate a date.\n\n- Linking related records together (the task to the lead).\nNow, you can give your flow more functionality by adding other elements. Look at these examples of record-triggered flows for more ideas.\n\n- [Flow Example: Send an Email from a Flow](automate_flow_build_example_send_email_from_a_flow.htm)\n\n- [Flow Example: Send a Custom Notification with a Flow](automate_flow_build_example_send_custom_notification.htm)",
      "score": 0.7970137484041087,
      "documentPath": "admin/platform/260-0-0/automate_flow_build_get_started_record_triggered_example_create_record.html",
      "url": "https://help.salesforce.com/s/articleView?id=platform.automate_flow_build_get_started_record_triggered_example_create_record.htm&release=260&type=5",
      "chunkIndex": 9,
      "metadata": {
        "title": "Create a Simple After-Save Record-Triggered Flow",
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
      "content": "Decide Between Before-Save and After-Save Record-Triggered Flows\n\nRecord-triggered flows run when someone creates, updates, or deletes a record in Salesforce. Before-save flows run before Salesforce saves the record. After-save flows run after Salesforce saves the record. Use this guide to pick the right type for your automation.",
      "score": 0.7932954923402314,
      "documentPath": "admin/platform/260-0-0/automate_flow_build_get_started_record_triggered_before_or_after_save.html",
      "url": "https://help.salesforce.com/s/articleView?id=platform.automate_flow_build_get_started_record_triggered_before_or_after_save.htm&release=260&type=5",
      "chunkIndex": 0,
      "metadata": {
        "title": "Decide Between Before-Save and After-Save Record-Triggered Flows",
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
    "queryTimeMs": 87,
    "searchMode": "auto (semantic)",
    "embeddingTimeMs": 75,
    "fallbackTriggered": false,
    "embeddingModel": "nomic"
  }
}
