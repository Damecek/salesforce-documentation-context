# Benchmark Questions

Five Salesforce questions chosen to spread across the doc types that matter for
this corpus: SOQL syntax, security/auth config, hard governor limits, an admin
UI procedure, and an Apex async code pattern.

| # | Question | Probes |
|---|----------|--------|
| 1 | How do I write a SOQL query with a LIMIT clause in Apex, and what is the maximum LIMIT value? | factual syntax + a specific number |
| 2 | How do I configure an OAuth 2.0 JWT bearer token flow for a connected app in Salesforce? | multi-step security procedure |
| 3 | What is the maximum number of SOQL queries allowed in a single synchronous Apex transaction? | exact governor-limit value (canonical answer: 100) |
| 4 | How do I create a record-triggered flow that runs after a record is saved? | admin/UI "how-to" (no code) |
| 5 | How do I use the @future annotation for asynchronous Apex, and what are its restrictions? | code example + constraints |
| 6 | How do I write a multiline string literal in Apex, and can I use the null coalescing operator? | recent syntax (triple-quote, `??`) |
| 7 | How do I display a toast message in a Salesforce screen flow? | flow-vs-component nuance |
| 8 | What is the difference between LWC, LWR and LWS, and from which API version are they available and enforced? | conceptual + version facts |
| 9 | How do I get the list of picklist values for a given record type in Apex? | exact API method |
| 10 | How do I use the Flow Transform element, and what advantages does it have over a Flow Loop? | newer feature + comparison |
| 11 | How do I create a headless quick action with LWC (like Aura headless actions), and since which API version is it supported? | LWC feature parity with Aura + version fact |
