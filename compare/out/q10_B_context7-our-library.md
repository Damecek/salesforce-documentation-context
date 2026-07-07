# Q10: How do I use the Flow Transform element, and what advantages does it have over a Flow Loop?

## Approach: B_context7-our-library
- latency: 3255 ms
- libraryId: /damecek/salesforce-documentation-context

---

===============
LIBRARY RULES
===============
From library maintainers:
- Do not infer product behavior beyond what is stated in the markdown.
- Preserve product terminology as written in the source markdown.



### Flow Element: Transform

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/automate-your-business-processes-part-02.md

The Transform element is used in screen flows, autolaunched flows without triggers, and record-triggered flows to map and transform source data to target data. However, when transforming a collection, the transformation cannot include joining, sorting, or filtering data. For these operations, use the Collection Filter or Collection Sort element instead.

--------------------------------

### Sum or Count Items in Collections with the Transform Element

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/automate-your-business-processes-part-01.md

The Transform element in Salesforce Flow allows you to aggregate data from a source collection. You can either count the number of items in the collection or calculate the sum of a specific field's values across all items in the collection. The result of this aggregation is then assigned to a target data field.

--------------------------------

### Flow Elements Reference > Flow Element: Transform

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/automate-your-business-processes-part-02.md

Transform elements map and transform source data to target data, usable in screen flows, autolaunched flows without triggers, and record-triggered flows. Update Records elements identify records for updating and set new values using record variables or specified conditions.
