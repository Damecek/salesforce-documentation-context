# Q8: What is the difference between LWC, LWR and LWS in Salesforce, and from which API version are they available and enforced?

## Approach: A_salesforce-docs-mcp
- latency: 1745 ms

---

{
  "chunks": [
    {
      "content": "Table context:\nHere's how Salesforce releases map to LWC API versions and LWC open source (LWC OSS) versions.\n\n| Salesforce Release | LWC API Version | LWC OSS |\n| --- | --- | --- |\n| Spring ’25 | 63.0 | v8.0.0 |\n| Winter ’25 | 62.0 | v7.0.0 |\n| Summer ’24 | 61.0 | v6.0.0 |\n| Spring ’24 | 60.0* | v5.0.0 |\n| Winter ’24 | 59.0 | v3.0.0 |\n| Summer ’23 | 58.0 and earlier | v2.50.0 and earlier |",
      "score": 0.8083367461957501,
      "documentPath": "lwc/lwc/guides/create/create-version-alignment.html",
      "url": "https://developer.salesforce.com/docs/platform/lwc/guide/create-version-alignment.html",
      "chunkIndex": 1,
      "metadata": {
        "title": "Salesforce Releases and LWC API Versions",
        "app_area": "developer"
      },
      "collection": "developer/lwc"
    },
    {
      "content": "Salesforce Releases and LWC API Versions\n\nHere's how Salesforce releases map to LWC API versions and LWC open source (LWC OSS) versions.",
      "score": 0.7997784614562988,
      "documentPath": "lwc/lwc/guides/create/create-version-alignment.html",
      "url": "https://developer.salesforce.com/docs/platform/lwc/guide/create-version-alignment.html",
      "chunkIndex": 0,
      "metadata": {
        "title": "Salesforce Releases and LWC API Versions",
        "app_area": "developer"
      },
      "collection": "developer/lwc"
    },
    {
      "content": "Differences Between LWC Open Source and LWC on the Salesforce Platform\n\nLightning Web Components on the Salesforce platform is a managed version of Lightning Web Components: Open Source. When working off the Salesforce platform, you can [download LWC](https://github.com/salesforce/lwc), configure it your way, deploy your application on any hosting environment, and chose when to upgrade. When working on the Salesforce platform, Salesforce manages the configuration, deployment, and upgrade of LWC for all customers.\n\nLWC OSS and LWC on the platform have different release schedules. The LWC engineering team usually [releases LWC OSS](https://github.com/salesforce/lwc/releases) weekly, whereas the [Salesforce platform is released](https://help.salesforce.com/articleView?id=release-notes.salesforce_release_notes.htm) three times a year. Because of this difference, the version of LWC on the Salesforce platform is 3–6 months behind the open-source version of LWC.\n\nThe open-source LWC engine is identical to the LWC engine on the Salesforce platform. The difference is how the engine is configured at the compiler level and at run time.",
      "score": 0.7941569089889526,
      "documentPath": "lwc/lwc/guides/get-started/get-started-oss.html",
      "url": "https://developer.salesforce.com/docs/platform/lwc/guide/get-started-oss.html",
      "chunkIndex": 2,
      "metadata": {
        "title": "Lightning Web Components: Open Source",
        "app_area": "developer"
      },
      "collection": "developer/lwc"
    },
    {
      "content": "* LWC API version 60.0 also includes changes from LWC OSS [v4.0.0](https://github.com/salesforce/lwc/releases/tag/v4.0.0).",
      "score": 0.7876598834991455,
      "documentPath": "lwc/lwc/guides/create/create-version-alignment.html",
      "url": "https://developer.salesforce.com/docs/platform/lwc/guide/create-version-alignment.html",
      "chunkIndex": 2,
      "metadata": {
        "title": "Salesforce Releases and LWC API Versions",
        "app_area": "developer"
      },
      "collection": "developer/lwc"
    },
    {
      "content": "[Note] note: LWC open source follows [semantic versioning](https://semver.org/) (semver) characteristics. See [LWC Open Source: LWC Versioning](https://lwc.dev/guide/versioning). While LWC on the Salesforce platform uses the same code base as [LWC open source](../get-started/get-started-oss.md), the version of LWC on the Salesforce platform is 3-6 months behind the open source version. For example, LWC OSS released v3.0.0 in June 2023 and the same was available to Salesforce platform developers as part of the Winter ’24 release.",
      "score": 0.7875328063964844,
      "documentPath": "lwc/lwc/guides/create/create-version-alignment.html",
      "url": "https://developer.salesforce.com/docs/platform/lwc/guide/create-version-alignment.html",
      "chunkIndex": 3,
      "metadata": {
        "title": "Salesforce Releases and LWC API Versions",
        "app_area": "developer"
      },
      "collection": "developer/lwc"
    }
  ],
  "total": 5,
  "returned": 5,
  "metrics": {
    "queryTimeMs": 88,
    "searchMode": "auto (semantic)",
    "embeddingTimeMs": 55,
    "fallbackTriggered": false,
    "embeddingModel": "nomic"
  }
}
