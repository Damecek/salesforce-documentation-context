# Q11: How do I create a headless quick action with LWC (like Aura headless actions), and since which API version is it supported?

## Approach: B_context7-our-library
- latency: 3067 ms
- libraryId: /damecek/salesforce-documentation-context

---

===============
LIBRARY RULES
===============
From library maintainers:
- Do not infer product behavior beyond what is stated in the markdown.
- Preserve product terminology as written in the source markdown.



### lwcComponent

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/metadata-api-developer-guide-part-06.md

Triggers the LWC component that targets the lightning__FlowAction target in the XML configuration file and that's referenced by actionName. Available in API version 63.0 and later.

```APIDOC
## lwcComponent

### Description
Triggers the LWC component that targets the lightning__FlowAction target in the XML configuration file and that's referenced by actionName.

### Endpoint
lwcComponent

### Parameters
None specified.
```

--------------------------------

### getShowQuickActionLcHeader()

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/apex-reference-guide-part-12.md

Returns an indication of whether the Lightning component quick action header and footer are shown.

```APIDOC
## getShowQuickActionLcHeader()

### Description
Indicates whether the header and footer of the Lightning component quick action are displayed. If false, the header (with title) and footer (with Save and Cancel buttons) are not shown.

### Signature
```apex
public Boolean getShowQuickActionLcHeader()
```

### Return Value
Type: Boolean
```

### QuickAction

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/metadata-api-developer-guide-part-08.md

The `type` field defines the kind of quick action, with options such as 'Canvas', 'Create', 'Flow', 'LightningComponent', 'LogACall', 'Post', 'SendEmail', 'SocialPost', 'Update', and 'VisualforcePage'. Some types have specific API version availability.

--------------------------------

### Configure Components for Custom Actions

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/lightning-aura-components-developer-guide-part-01.md

To enable an Aura component for use as a custom action, implement either the `force:lightningQuickAction` or `force:lightningQuickActionWithoutHeader` interface. Components using `force:lightningQuickAction` display with standard action controls like a 'Cancel' button, while `force:lightningQuickActionWithoutHeader` provides complete UI control without predefined controls. These interfaces are mutually exclusive. Ensure all required component attributes have default values.

--------------------------------

### Configure Components for Record-Specific Actions

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/lightning-aura-components-developer-guide-part-01.md

When a component is designed for use as a quick action, it should implement both the `force:lightningQuickActionWithoutHeader` and `force:hasRecordId` interfaces. `force:lightningQuickActionWithoutHeader` makes the component available as an action and hides standard controls, while `force:hasRecordId` automatically provides the record ID when the component is invoked in a record context.
