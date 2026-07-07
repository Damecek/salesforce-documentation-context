# Q8: What is the difference between LWC, LWR and LWS in Salesforce, and from which API version are they available and enforced?

## Approach: C_context7-no-library
- latency: 4625 ms
- chosenLibrary: /salesforce/lwc
- chosenTitle: LWC

---

### resolve-library-id picked: /salesforce/lwc (LWC)

--- resolve-library-id ranking (top of list) ---
Available Libraries:

- Title: LWC
- Context7-compatible library ID: /salesforce/lwc
- Description: ⚡️ LWC - A Blazing Fast, Enterprise-Grade Web Components Foundation
- Code Snippets: 345
- Source Reputation: High
- Benchmark Score: 47.11

--- query-docs against /salesforce/lwc ---
### version API

Source: https://github.com/salesforce/lwc/blob/master/packages/@lwc/compiler/README.md

Get the current version of the compiler.

```js
import { version } from '@lwc/compiler';

console.log(version);
```

### ARCHITECTURE.md/Unique design decisions in LWC/Component-level API versioning

Source: https://github.com/salesforce/lwc/blob/master/ARCHITECTURE.md

LWC's unique design decisions include component-level API versioning, driven by the need for backwards compatibility on the Salesforce Lightning platform. Breaking changes contained within a component's internals should be handled through this versioning mechanism.

--------------------------------

### External integrations

Source: https://github.com/salesforce/lwc/blob/master/ARCHITECTURE.md

The LWC open-source monorepo depends purely on open-source projects, including those authored at Salesforce. Today this includes: `observable-membrane` for core reactivity logic and `@locker/babel-plugin-transform-unforgeables` for a special Babel transform for Lightning Web Security. LWC also has several tight integrations with Salesforce-internal projects: `lwc-platform-public` for core integration logic, Locker/Lightning Web Security as a security layer with several integration points, and Lightning Web Runtime as a meta-framework similar to Next.js for LWC. Some open-source projects live in the same 'cinematic universe' but are less tightly coupled to LWC, including `lwc-test` for LWC Jest testing utilities and `eslint-plugin-lwc` for LWC ESLint linting utilities.

--------------------------------

### README.md

Source: https://github.com/salesforce/lwc/blob/master/packages/lwc/README.md

Lightning Web Components (LWC) is an enterprise-grade web components foundation for building user interfaces. LWC provides a simple authoring format for UI components, which is compiled into low-level Web Component APIs. The `lwc` package is the main entry point for dependencies.

--------------------------------

### LWC Compiler > APIs > version

Source: https://github.com/salesforce/lwc/blob/master/packages/@lwc/compiler/README.md

Return
- `version` (string) - the current version of the compiler ex: `0.25.1`.
