# Q6: How do I write a multiline string literal in Apex, and can I use the null coalescing operator?

## Approach: B_context7-our-library
- latency: 3283 ms
- libraryId: /damecek/salesforce-documentation-context

---

===============
LIBRARY RULES
===============
From library maintainers:
- Do not infer product behavior beyond what is stated in the markdown.
- Preserve product terminology as written in the source markdown.



### Multiline String Declaration

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/apex-developer-guide-part-01.md

Shows how to declare a multiline string literal in Apex, useful for representing blocks of text like JSON.

```Apex
String multilineStr = '''

{

   "Name" : "John Doe",

   "Type" : "New Customer"

}''';
```

--------------------------------

### Concatenating Multiline Strings in Apex

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/apex-developer-guide-part-01.md

Use the '\' escape sequence at the end of a line to concatenate multiple lines into a single string without newlines. This is useful for long strings that need to be broken up for readability.

```Apex
String str = '''

      This is a string that doesn\'t fit on one line \

      but I don\'t want it to contain newlines \

   ....so I am using this escape sequence to \

   ....prevent them from being inserted''';
```

--------------------------------

### Null Coalescing Operator Usage

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/apex-developer-guide-part-01.md

The null coalescing operator provides a more concise syntax for assigning default values when a variable might be null. Ensure type compatibility between operands.

```Apex
Integer notNullReturnValue = anInteger ?? 100;
```

--------------------------------

### Null Coalescing Operator with SOQL Query (No Rows)

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/apex-developer-guide-part-01.md

This example demonstrates using the null coalescing operator to handle SOQL queries that might not return any rows. If the SOQL query returns no rows, the defaultAccount from the right-hand operand is returned.

```Apex
Account defaultAccount = new Account(name = 'Acme');

   // Left operand SOQL is empty, return defaultAccount from right operand:

   Account a = [SELECT Id FROM Account

     WHERE Id = '001000000FAKEID'] ?? defaultAccount;

   Assert.areEqual(defaultAccount, a);
```

--------------------------------

### Null Coalescing Operator with Safe Navigation and SOQL

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/apex-developer-guide-part-01.md

This example shows how the null coalescing operator can be combined with the safe navigation operator to handle potentially null fields returned from a SOQL query, providing a default value if the field is null or the record doesn't exist.

```Apex
string city = [Select BillingCity

      From Account

      Where Id = '001xx000000001oAAA']?.BillingCity;

   System.debug('Matches count: ' + city?.countMatches('San Francisco') ?? 0 );
```
