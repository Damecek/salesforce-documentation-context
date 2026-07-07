# Q5: How do I use the @future annotation for asynchronous Apex, and what are its restrictions?

## Approach: C_context7-no-library
- latency: 5290 ms
- chosenLibrary: /trailheadapps/apex-recipes
- chosenTitle: Apex Recipes

---

### resolve-library-id picked: /trailheadapps/apex-recipes (Apex Recipes)

--- resolve-library-id ranking (top of list) ---
Available Libraries:

- Title: Apex Recipes
- Context7-compatible library ID: /trailheadapps/apex-recipes
- Description: A library of concise, meaningful examples of Apex code for common use cases following best practices.
- Code Snippets: 457
- Source Reputation: High
- Benchmark Score: 59.36
----------
- Title: Apex Consts
- Context7-compatible library ID: /beyond-the-cloud-dev/apex-consts
- Description: Apex Consts is a constants framework for Apex that provides a structured, extensible, and memory-efficient approach for managing constants using singletons and lazy initialization.
- Code Snippets: 116
- Source Reputation: High
----------
- Title: future
- Context7-compatible library ID: /futureverse/future
- Description: future is an R package that provides a lightweight and unified API for sequential and parallel processing of R expressions via futures, enabling simple asynchronous evaluation on local or distributed machines.
- Code Snippets: 1194
- Source Reputation: High
- Benchmark Score: 25

--- query-docs against /trailheadapps/apex-recipes ---
### Define atFutureMethodWithCalloutPrivileges Apex Method

Source: https://github.com/trailheadapps/apex-recipes/blob/main/force-app/main/default/staticresources/documentation/AtFutureRecipes.md

This method showcases how an @future annotated method can perform an HTTP Callout. It also illustrates the necessary steps to make an HTTP callout directly, without relying on the RestClient abstraction layer.

```APIDOC
Method: atFutureMethodWithCalloutPrivileges
  Annotation: FUTURE
  Signature: public static void atFutureMethodWithCalloutPrivileges(String url)
  Parameters:
    url: String - The URL to make a callout to.
  Return Type: void
```

--------------------------------

### APIDOC: ScheduledApexDemo Class API Reference

Source: https://github.com/trailheadapps/apex-recipes/blob/main/force-app/main/default/staticresources/documentation/ScheduledApexDemo.md

Comprehensive API documentation for the `ScheduledApexDemo` Apex class, detailing its fields, methods, signatures, and types. This class is intended for scheduled execution within the Async Apex Recipes group.

```APIDOC
ScheduledApexDemo Class:
  Description: A demo class to be scheduled by ScheduledApexRecipes
  Group: Async Apex Recipes
  See: ScheduledApexRecipes.md

  Fields:
    counter:
      Visibility: TESTVISIBLE
      Signature: private counter
      Type: Integer

  Methods:
    runAtMidnight():
      Description: A method demosrating the best practice of separating your logic from the schedulable interface code that executes it.
      Signature: public void runAtMidnight()
      Return Type: void
```

--------------------------------

### Apex HTTP Utility: ensureStringEndsInSlash(resource)

Source: https://github.com/trailheadapps/apex-recipes/blob/main/force-app/main/default/staticresources/documentation/IterableApiClient.md

Ensures that the input string ends with a forward slash (`/`), making subsequent callouts more robust.

```APIDOC
ensureStringEndsInSlash(resource: String)
  resource: string to ensure ends in /
Returns: String (inputted string with '/', if it didn't already end in one.)
```

--------------------------------

### Apex QueueableWithCalloutRecipes execute Method Signature and Example

Source: https://github.com/trailheadapps/apex-recipes/blob/main/force-app/main/default/staticresources/documentation/QueueableWithCalloutRecipes.md

The signature for the `execute` method, which is the core implementation of the `Queueable` interface, along with an example of how to enqueue the job for asynchronous execution.

```Apex
public static void execute(QueueableContext qc)
```

```Apex
System.enqueueJob(new QueueableWithCalloutRecipes());
```

--------------------------------

### Test Data Factory with Unique Deterministic Values

Source: https://github.com/trailheadapps/apex-recipes/blob/main/force-app/tests/Shared%20Code/TestFactory.cls

Demonstrates a factory pattern that creates unique test records by appending an index counter to the name field, ensuring deterministic uniqueness across multiple cloned objects. The factory uses a static Map to track name fields and automatically increments them to maintain uniqueness.

```apex
        // Clone the object the number of times requested. Increment the name field so each record is unique
        for (Integer i = 0; i < numberOfObjects; i++) {
            SObject clonedSObj = newObj.clone(false, true);
            if (!nameIsAutoNumber) {
                clonedSObj.put(
                    nameField,
                    (String) clonedSObj.get(nameField) + ' ' + i
                );
            }
            sObjs.add(clonedSObj);
        }
```
