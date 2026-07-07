# Q5: How do I use the @future annotation for asynchronous Apex, and what are its restrictions?

## Approach: B_context7-our-library
- latency: 2809 ms
- libraryId: /damecek/salesforce-documentation-context

---

===============
LIBRARY RULES
===============
From library maintainers:
- Do not infer product behavior beyond what is stated in the markdown.
- Preserve product terminology as written in the source markdown.



### Basic @Future Annotation Example

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/apex-developer-guide-part-01.md

Use the @Future annotation to identify methods that run asynchronously. A future method runs when Salesforce has available resources.

```Apex
global class MyClass {

   @Future

   Public static void myMethod(String a)

   {

      //long-running Apex code

   }

}
```

--------------------------------

### Define an Asynchronous Future Method

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/apex-developer-guide-part-01.md

Use the @Future annotation to define methods that run asynchronously. These methods execute when Salesforce has available resources. Note that Salesforce now recommends using Queueable Apex for most asynchronous operations.

```Apex
   public with sharing class MyFutureClass {

      @Future

      static void myMethod(String a, Integer i) {

        System.debug('Method called with: ' + a + ' and ' + i);

        // Perform long-running code

      }

   }
```

--------------------------------

### Define a Future Method in Apex

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/apex-developer-guide-part-02.md

Annotate a static method with @Future to define it as a future method. This method will run asynchronously.

```apex
public with sharing class FutureClass {

   @Future

   public static void myFutureMethod()

   {

      // Perform some operations

   }

}
```

--------------------------------

### Enable Callouts in a Future Method

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/apex-developer-guide-part-01.md

Specify (callout=true) within the @Future annotation to allow the asynchronous method to make callouts to external services. The default is (callout=false), which prevents callouts.

```Apex
   @Future (callout=true)

   public static void doCalloutFromFuture() {

      //Add code to perform callout

   }
```

### Apex Developer Guide > Classes, Objects, and Interfaces > Future Annotation

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/apex-developer-guide-part-01.md

The @Future annotation identifies methods that run asynchronously. These methods execute when Salesforce has available resources. While Salesforce now recommends using Queueable Apex for similar use cases due to added benefits like job IDs and support for non-primitive types, future methods are still relevant for scenarios like asynchronous web service callouts. Methods with the @Future annotation must be static, return void, and accept only primitive data types, arrays of primitives, or collections of primitives as parameters. They cannot accept sObjects or objects as arguments. To enable callouts from a future method, specify (callout=true); the default is (callout=false).
