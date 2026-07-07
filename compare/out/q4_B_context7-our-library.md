# Q4: How do I create a record-triggered flow that runs after a record is saved?

## Approach: B_context7-our-library
- latency: 3091 ms
- libraryId: /damecek/salesforce-documentation-context

---

===============
LIBRARY RULES
===============
From library maintainers:
- Do not infer product behavior beyond what is stated in the markdown.
- Preserve product terminology as written in the source markdown.



### FlowRecordVersion > Record-Triggered After Save Flow

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/object-reference-for-the-salesforce-platform-part-09.md

Record-Triggered After Save Flow launches after a record is created or updated and saved. It can only modify related records and runs in the background without user interaction.

--------------------------------

### FlowRecordVersion > Record-Triggered After Save Orchestration

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/object-reference-for-the-salesforce-platform-part-09.md

Record-Triggered After Save Orchestration launches after a record is created or updated.

--------------------------------

### FlowRecord

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/object-reference-for-the-salesforce-platform-part-09.md

Prompt Template Capability-Triggered Flows add prompt instructions to associated templates and run in the background. Recommendation Strategy Autolaunched Flows build personalized recommendation lists, used with Einstein Next Best Action and displayed via components in Lightning App Builder and Experience Builder. Record-Triggered After Save Flows launch after a record is saved, can modify related records, and run in the background. Record-Triggered After Save Orchestrations launch on record creation or update to manage multi-step, multi-user approval processes.

--------------------------------

### FlowRecordVersion > Customer Lifecycle Record-Triggered After Save Flow

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/object-reference-for-the-salesforce-platform-part-09.md

Customer Lifecycle Record-Triggered After Save Flow launches after a customer lifecycle map is saved, modifying records related to the triggering record in the background without user interaction.

--------------------------------

### Standard Objects FlowRecord

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/object-reference-for-the-salesforce-platform-part-09.md

Record-Triggered Before Delete Flows launch when a record is deleted and run in the background. Record-Triggered Before Save Flows launch after a record is created or updated but before it's saved, allowing modifications only to the triggering record and running in the background. Record Queries, available from API version 67.0, perform actions or send messages to individuals from queried CRM records on a schedule. Routing Autolaunched Flows handle work item routing for chat, voice, or messaging conversations, running in the background.
