# Q11: How do I create a headless quick action with LWC (like Aura headless actions), and since which API version is it supported?

## Approach: A_salesforce-docs-mcp
- latency: 1713 ms

---

{
  "chunks": [
    {
      "content": "LWC Quick Actions\n\nLWC quick actions can be a screen action or a headless action. A screen quick action appears in a modal window. A headless quick action executes custom code without a modal window. You can also use a headless quick action to [navigate to another page](../use/use-navigate-quick-action.md) using the `lightning/navigation` module. For more information, see [Configure a Component for Quick Actions](../use/use-config-for-quick-actions.md).\n\nA common use case for using an LWC quick action is to provide custom functionality that's not available with [standard quick actions](https://help.salesforce.com/s/articleView?id=platform.actions_overview.htm) or [default actions](https://help.salesforce.com/s/articleView?id=platform.default_actions_overview.htm). For example, you want to display a modal with information, and then include a button that displays a create record modal. In an Aura quick action, you can call `force:recordCreate` when the button is clicked. When you migrate to an LWC quick action, you can use the `lightning/navigation` module to achieve the same behavior.",
      "score": 0.7876222639984679,
      "documentPath": "lwc/lwc/guides/migrate/migrate-quick-actions.html",
      "url": "https://developer.salesforce.com/docs/platform/lwc/guide/migrate-quick-actions.html",
      "chunkIndex": 6,
      "metadata": {
        "title": "Migrate Quick Actions",
        "app_area": "developer"
      },
      "collection": "developer/lwc"
    },
    {
      "content": "Create Headless Quick Actions\n\nA headless quick action executes custom code in a Lightning web component. Unlike a screen action, a headless action doesn’t open a modal window.\n\nTo enable your component to be used as a headless quick action, configure a target. See [Configure a Component for Quick Actions](../use/use-config-for-quick-actions.md).\n\nUnlike other [Lightning web components on record pages](../use/use-record-context.md), LWC quick actions don’t pass in `recordId` in `connectedCallback()`. If you need access to `recordId`, set the value of `recordId` in your code.",
      "score": 0.7818642182674109,
      "documentPath": "lwc/lwc/guides/use/use-quick-actions-headless.html",
      "url": "https://developer.salesforce.com/docs/platform/lwc/guide/use-quick-actions-headless.html",
      "chunkIndex": 0,
      "metadata": {
        "title": "Create Headless Quick Actions",
        "app_area": "developer"
      },
      "collection": "developer/lwc"
    },
    {
      "content": "Code context:\nA headless quick action executes custom code in a Lightning web component. Unlike a screen action, a headless action doesn’t open a modal window.\n\nTo enable your component to be used as a headless quick action, configure a target. See [Configure a Component for Quick Actions](../use/use-config-for-quick-actions.md).\n\nUnlike other [Lightning web components on record pages](../use/use-record-context.md), LWC quick actions don’t pass in `recordId` in `connectedCallback()`. If you need access to `recordId`, set the value of `recordId` in your code.\n\n```javascript\n_recordId;\n\n@api\nget recordId() {\n    return this._recordId;\n}\n\nset recordId(recordId) {\n    if (recordId !== this._recordId) {\n        this._recordId = recordId;\n   }\n}\n```",
      "score": 0.7578190546467389,
      "documentPath": "lwc/lwc/guides/use/use-quick-actions-headless.html",
      "url": "https://developer.salesforce.com/docs/platform/lwc/guide/use-quick-actions-headless.html",
      "chunkIndex": 1,
      "metadata": {
        "title": "Create Headless Quick Actions",
        "app_area": "developer"
      },
      "collection": "developer/lwc"
    },
    {
      "content": "[Note] note: LWC quick actions are available only on record pages in Lightning Experience. They’re not supported in Aura Experience Builder sites or on the Salesforce mobile app. The Field Service org supports Lightning web component actions on additional objects. These actions appear only in the Field Service mobile app and not in Lightning Experience on mobile or desktop.",
      "score": 0.7552112474408129,
      "documentPath": "lwc/lwc/guides/use/use-quick-actions.html",
      "url": "https://developer.salesforce.com/docs/platform/lwc/guide/use-quick-actions.html",
      "chunkIndex": 1,
      "metadata": {
        "title": "Quick Actions",
        "app_area": "developer"
      },
      "collection": "developer/lwc"
    },
    {
      "content": "[Note] Headless Lightning web component quick actions are available only on record pages in Lightning Experience and LWR sites created in Experience Cloud. They’re not supported in Aura Experience Builder sites or on the Salesforce mobile app. Orgs with the Salesforce Field Service (SFS) mobile app support Lightning web component actions on additional objects. These actions appear only in the SFS mobile app and not in Lightning Experience on mobile or desktop.",
      "score": 0.7339161672792245,
      "documentPath": "admin/platform/260-0-0/lightning_web_component_actions_create.html",
      "url": "https://help.salesforce.com/s/articleView?id=platform.lightning_web_component_actions_create.htm&release=260&type=5",
      "chunkIndex": 8,
      "metadata": {
        "title": "Create a Lightning Web Component Action",
        "app_area": "Platform",
        "breadcrumb_path": "Salesforce Help|Docs|Extend Salesforce with Clicks, Not Code",
        "required_editions": "Available in: Lightning Experience; Available in: Group, Professional, Enterprise, Performance, Unlimited, Contact Manager, Database.com, and Developer Editions",
        "available_editions": [
          "Developer"
        ],
        "required_permissions": "To create actions: Customize Application",
        "available_experiences": [
          "Lightning Experience"
        ],
        "required_permission_names": [
          "Customize Application"
        ]
      },
      "collection": "admin/platform"
    }
  ],
  "total": 5,
  "returned": 5,
  "metrics": {
    "queryTimeMs": 83,
    "searchMode": "auto (semantic)",
    "embeddingTimeMs": 49,
    "fallbackTriggered": false,
    "embeddingModel": "nomic"
  }
}
