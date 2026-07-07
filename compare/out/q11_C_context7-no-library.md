# Q11: How do I create a headless quick action with LWC (like Aura headless actions), and since which API version is it supported?

## Approach: C_context7-no-library
- latency: 4771 ms
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
----------
- Title: Expo Quick Actions
- Context7-compatible library ID: /evanbacon/expo-quick-actions
- Description: A comprehensive React Native library for implementing home screen quick actions, allowing developers to define actions with titles, subtitles, icons, and parameters.
- Code Snippets: 375
- Source Reputation: High
- Benchmark Score: 92.2
----------
- Title: Aura Router
- Context7-compatible library ID: /auraphp/aura.router
- Description: Powerful, flexible web routing for PSR-7 requests.
- Code Snippets: 576
- Source Reputation: High

--- query-docs against /salesforce/lwc ---
### Run test suites or individual files locally in headless Chrome

Source: https://github.com/salesforce/lwc/blob/master/packages/@lwc/integration-wdio/README.md

Run test suites or individual files locally in headless Chrome.

```shell
yarn local --suite SUITE_NAME
```

```shell
yarn local --spec path/to/my/spec.js
```

--------------------------------

### Run Chrome tests in non-headless mode

Source: https://github.com/salesforce/lwc/blob/master/packages/@lwc/integration-wdio/README.md

To run Chrome tests in non-headless mode, set `process.env.HEADLESS_CHROME` to `false`.

```javascript
process.env.HEADLESS_CHROME = false;
```

--------------------------------

### transformSync API

Source: https://github.com/salesforce/lwc/blob/master/packages/@lwc/compiler/README.md

Transform the content of individual file using transformSync.

```js
import { transformSync } from '@lwc/compiler';

const source = `
    import { LightningElement } from 'lwc';
    export default class App extends LightningElement {}
`;

const filename = 'app.js';

const options = {
    namespace: 'c',
    name: 'app',
};

const { code } = transformSync(source, filename, options);
```

### LWC Compiler > APIs > transform (deprecated)

Source: https://github.com/salesforce/lwc/blob/master/packages/@lwc/compiler/README.md

Deprecated asynchronous equivalent of `transformSync`.

--------------------------------

### LWC Compiler > APIs > version

Source: https://github.com/salesforce/lwc/blob/master/packages/@lwc/compiler/README.md

Return
- `version` (string) - the current version of the compiler ex: `0.25.1`.
