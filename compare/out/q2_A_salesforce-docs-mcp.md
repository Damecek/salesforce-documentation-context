# Q2: How do I configure an OAuth 2.0 JWT bearer token flow for a connected app in Salesforce?

## Approach: A_salesforce-docs-mcp
- latency: 1952 ms

---

{
  "chunks": [
    {
      "content": "To configure a JWT bearer flow, you must first deploy an external client app on your Salesforce org. [Deploy an External Client App That References the Source Org’s Global OAuth Settings File](deploy_external_client_app_that_references_the_source_org.htm), or [Deploy an External Client App with a New Global OAuth Settings File](deploy_external_client_app_with_global_settings_file.htm).\n\n1. Create an X.509 certificate by following the steps in [OAuth 2.0 JWT Bearer Flow for Server-to-Server Integration](remoteaccess_oauth_jwt_flow.htm).\n\n2. Open the extlClntAppGlobalOauthSettings file.\n\n3. If the certificate field doesn’t exist, add it and enter the X.509 certificate as the value for the certificate field.\n\n4. Save the extlClntAppGlobalOauthSets file.\n\n5. Create a JWT following the steps in the [OAuth 2.0 JWT Bearer Flow for Server-to-Server Integration](remoteaccess_oauth_jwt_flow.htm).\n\n6. Use this cURL command to request the token for deploying your external client app.\nThis returns a bearer token you can use to authorize in other flows.",
      "score": 0.8505278051528941,
      "documentPath": "admin/xcloud/260-0-0/meta_configure_oauth_jwt_flow_external_client_apps.html",
      "url": "https://help.salesforce.com/s/articleView?id=xcloud.meta_configure_oauth_jwt_flow_external_client_apps.htm&release=260&type=5",
      "chunkIndex": 2,
      "metadata": {
        "title": "Configure OAuth 2.0 JWT Bearer Flow for External Client Apps",
        "app_area": "Security",
        "breadcrumb_path": "Salesforce Help|Docs|Identify Your Users and Manage Access",
        "required_permissions": "To view all external client apps, view their settings, and edit their OAuth policies file: View all External Client Apps, view their settings, and edit their policies",
        "required_permission_names": [
          "View all External Client Apps",
          "view their settings",
          "and edit their policies"
        ]
      },
      "collection": "admin/xcloud"
    },
    {
      "content": "To configure a JWT bearer flow, you must first have an external client app on your Salesforce org. See [Create an External Client App](create_a_local_external_client_app.htm).\n\n1. To create an X.509 certificate, follow the steps in [OAuth 2.0 JWT Bearer Flow for Server-to-Server Integration](remoteaccess_oauth_jwt_flow.htm).\n\n2. From Setup, in the Quick Find box, enter `External Client Apps\nManager`, and then select `External Client Apps\nManager`.\n\n3. From the actions dropdown list for the external client app that you want to configure, select `Edit Settings`.\n\n4. In the OAuth Settings section, select `Enable OAuth`.\n\n5. Configure [basic OAuth settings](configure_external_client_app_oauth_settings.htm).\n\n6. Select `Enable JWT Bearer Flow`.\n\n7. Select `Upload Files` and then choose the X.509 certificate.\n\n8. Save the settings.\n\n9. Create a JWT by following the steps in [OAuth 2.0 JWT Bearer Flow for Server-to-Server Integration](remoteaccess_oauth_jwt_flow.htm).",
      "score": 0.8484200744879667,
      "documentPath": "admin/xcloud/260-0-0/configure_oauth_jwt_flow_external_client_apps.html",
      "url": "https://help.salesforce.com/s/articleView?id=xcloud.configure_oauth_jwt_flow_external_client_apps.htm&release=260&type=5",
      "chunkIndex": 3,
      "metadata": {
        "title": "Configure a JWT Bearer Flow",
        "app_area": "Security",
        "breadcrumb_path": "Salesforce Help|Docs|Identify Your Users and Manage Access",
        "required_editions": "Available in: Lightning Experience; Available in: Professional, Performance, Unlimited, and Developer Editions",
        "available_editions": [
          "Professional",
          "Performance",
          "Unlimited",
          "Developer"
        ],
        "required_permissions": "To configure an external client app for OAuth 2.0 JWT Bearer Flows: View all External Client Apps, view their settings, and edit their policies",
        "available_experiences": [
          "Lightning Experience"
        ],
        "required_permission_names": [
          "View all External Client Apps",
          "view their settings",
          "and edit their policies"
        ]
      },
      "collection": "admin/xcloud"
    },
    {
      "content": "- For a connected app to request access, integrate the app with the Salesforce API using the OAuth 2.0 JSON Web Token (JWT) bearer flow.\nThe private key associated with the connected app is used to sign the certificate, and is also used in this flow to sign the JWT request.\nImportant We recommend that you manually create or generate the certificate and the private key every year.",
      "score": 0.8300087046644042,
      "documentPath": "admin/ind/260-0-0/task_create_a_certificate_and_private_key.html",
      "url": "https://help.salesforce.com/s/articleView?id=ind.task_create_a_certificate_and_private_key.htm&release=260&type=5",
      "chunkIndex": 4,
      "metadata": {
        "title": "Create a Certificate and a Private Key",
        "app_area": "Industry Solutions",
        "breadcrumb_path": "Salesforce Help|Docs|Einstein Relationship Insights",
        "required_permissions": "To create, edit, and manage certificates: Modify All Data and Customize Application",
        "required_permission_names": [
          "Modify All Data and Customize Application"
        ]
      },
      "collection": "admin/ind"
    },
    {
      "content": "With the OAuth 2.0 JWT bearer token flow, the client posts a JWT to the Salesforce OAuth token endpoint. Salesforce processes the JWT, which includes a digital signature, and issues an access token based on prior approval of the app.\n\nThis example shows the steps taken in the flow.\n\n1. A report service begins its nightly batch report.\n\n2. The connected app sends the JWT to the Salesforce token endpoint. The JWT enables identity and security information to be shared across security domains.\n\n3. Salesforce validates the JWT based on a signature using a previously configured certificate and additional parameters.\n\n4. Assuming that the JWT is valid and that the connected app has prior approval, Salesforce issues an access token. Prior approval happens in one of these ways:\nNote For both options, Salesforce issues a new access token only when the original access token includes at least one standard scope other than the `refresh_token` scope.\n\n- If your connected app policy is set to `Admin approved users are\npre-authorized`, you can use profiles and permission sets.\n\n- If your connected app policy is set to `All users may\nself-authorize`, you can use end-user approval and issuance of a refresh token. However, the client isn’t required to have a current or stored refresh token. The client also isn’t required to pass a client secret to the token endpoint.",
      "score": 0.8278655102012606,
      "documentPath": "admin/xcloud/260-0-0/remoteaccess_oauth_jwt_flow_ca.html",
      "url": "https://help.salesforce.com/s/articleView?id=xcloud.remoteaccess_oauth_jwt_flow_ca.htm&release=260&type=5",
      "chunkIndex": 3,
      "metadata": {
        "title": "OAuth 2.0 JWT Bearer Flow for Server-to-Server Integration",
        "app_area": "Security",
        "breadcrumb_path": "Salesforce Help|Docs|Identify Your Users and Manage Access",
        "required_editions": "Available in: both Salesforce Classic and Lightning Experience; Available in: All Editions",
        "available_experiences": [
          "Salesforce Classic",
          "Lightning Experience"
        ]
      },
      "collection": "admin/xcloud"
    },
    {
      "content": "With the OAuth 2.0 JWT bearer token flow, the client posts a JWT to the Salesforce OAuth token endpoint. Salesforce processes the JWT, which includes a digital signature, and issues an access token based on prior approval of the app.\n\nThis example shows the steps taken in the flow.\n\n1. A report service begins its nightly batch report.\n\n2. The connected app sends the JWT to the Salesforce token endpoint. The JWT enables identity and security information to be shared across security domains.\n\n3. Salesforce validates the JWT based on a signature using a previously configured certificate and additional parameters.\n\n4. Assuming that the JWT is valid and that the connected app has prior approval, Salesforce issues an access token. Prior approval happens in one of these ways:\nNote For both options, Salesforce issues a new access token only when the original access token includes at least one standard scope other than the `refresh_token` scope.\n\n- If your connected app policy is set to `Admin approved users are\npre-authorized`, you can use profiles and permission sets.\n\n- If your connected app policy is set to `All users may\nself-authorize`, you can use end-user approval and issuance of a refresh token. However, the client isn’t required to have a current or stored refresh token. The client also isn’t required to pass a client secret to the token endpoint.",
      "score": 0.8278655102012606,
      "documentPath": "admin/xcloud/260-0-0/remoteaccess_oauth_jwt_flow.html",
      "url": "https://help.salesforce.com/s/articleView?id=xcloud.remoteaccess_oauth_jwt_flow.htm&release=260&type=5",
      "chunkIndex": 2,
      "metadata": {
        "title": "OAuth 2.0 JWT Bearer Flow for Server-to-Server Integration",
        "app_area": "Security",
        "breadcrumb_path": "Salesforce Help|Docs|Identify Your Users and Manage Access",
        "required_editions": "Available in: both Salesforce Classic and Lightning Experience; Available in: All Editions",
        "available_experiences": [
          "Salesforce Classic",
          "Lightning Experience"
        ]
      },
      "collection": "admin/xcloud"
    }
  ],
  "total": 5,
  "returned": 5,
  "metrics": {
    "queryTimeMs": 108,
    "searchMode": "auto (semantic)",
    "embeddingTimeMs": 95,
    "fallbackTriggered": false,
    "embeddingModel": "nomic"
  }
}
