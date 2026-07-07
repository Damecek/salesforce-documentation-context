# Q7: How do I display a toast message in a Salesforce screen flow?

## Approach: A_salesforce-docs-mcp
- latency: 1964 ms

---

{
  "chunks": [
    {
      "content": "Add Visually Distinct and Accessible Messages to Screen Flows\n\nWith the new Message screen component, you can add an eye-catching a11y-compliant message to a screen to show information, a success, an error, or a warning.\n\nWhere:This change applies to Lightning Experience and Salesforce Classic in Essentials, Professional, Enterprise, Unlimited, and Developer editions.\n\nHow:Add the Message display component to a flow screen. The message type determines the color and icon used for the message. Screen readers are able to read the message type to their users. For the message, you can enter text or select a flow resource to use as the message.\n\n[Image: Message component configuration](https://sf-zdocs-cdn-prod.zoominsoftware.com/tdta-salesforce_release_notes-260-0-0-production-enus/ba62a63b-6cd1-440e-8d24-e867afab0363/salesforce_release_notes/images/automate/rn_automate_flow_builder_screen_message_component.png)\n\n[Image: Message component configuration](https://sf-zdocs-cdn-prod.zoominsoftware.com/tdta-salesforce_release_notes-260-0-0-production-enus/ba62a63b-6cd1-440e-8d24-e867afab0363/salesforce_release_notes/images/automate/rn_automate_flow_builder_screen_message_component.png)\n\nSee Also\n\n- [Salesforce Help: Flow Example: Keep Users Informed With a Message Screen Component](https://help.salesforce.com/s/articleView?id=automate_flow_build_example_message_screencmp.htm&type=5&language=en_US)\n\n- [Salesforce Help: Flow Screen Output Component: Message Screen Component](https://help.salesforce.com/s/articleView?id=flow_ref_elements_screencmp_message.htm&type=5&language=en_US)",
      "score": 0.7628216743469455,
      "documentPath": "admin/release-notes/260-0-0/rn_automate_flow_builder_screen_message_component.html",
      "url": "https://help.salesforce.com/s/articleView?id=release-notes.rn_automate_flow_builder_screen_message_component.htm&release=260&type=5",
      "chunkIndex": 0,
      "metadata": {
        "title": "Add Visually Distinct and Accessible Messages to Screen Flows",
        "app_area": "Cross Cloud Packages Solutions",
        "breadcrumb_path": "Salesforce Help|Docs|Salesforce Release Notes"
      },
      "collection": "admin/release-notes"
    },
    {
      "content": "When a flow sends an automated message, Salesforce does three things.\n\n- Create a messaging user record for the recipient, if one doesn’t exist already.\n\n- Create a messaging session record with a transcript of the sent message and an unchanging status of Ended.\n\n- Add any message errors to the Standard Messaging Error Log page in Setup.\n\n1. From Setup, in the Quick Find box, enter `Flows`, then select `Flows`.\n\n2. Click `New Flow`.\n\n3. Select the flow type, and click `Next`.\nThe Flow Builder canvas opens.\n\n4. Add an action to the canvas.\nThe New Action window opens.\n\n5. Enter `Message Notification` in the search, and then select `Message Notification`.\n\n6. Fill out the fields for the Message Notification core action.\n\nYou can use values from earlier in a flow to set inputs for the message notification. If the message notification fields don’t contain valid inputs, the flow fails.",
      "score": 0.7497061341825924,
      "documentPath": "admin/service/260-0-0/livemessage_automatic_notifications_flows.html",
      "url": "https://help.salesforce.com/s/articleView?id=service.livemessage_automatic_notifications_flows.htm&release=260&type=5",
      "chunkIndex": 3,
      "metadata": {
        "title": "Create a Flow to Send Messages in Standard Channels",
        "app_area": "Service",
        "breadcrumb_path": "Salesforce Help|Docs|Agentforce Contact Center",
        "required_editions": "[View supported editions.](https://help.salesforce.com/s/articleView?id=service.messaging_editions.htm&type=5&language=en_US) [View supported editions.](https://help.salesforce.com/s/articleView?id=service.messaging_editions.htm&type=5&language=en_US); Yes This article applies to: Standard Facebook Messenger and Standard SMS channels; No This article doesn’t apply to: Enhanced In-App Chat, Enhanced Web Chat v1, Enhanced Web Chat v2, Enhanced WhatsApp, Enhanced Facebook Messenger, Enhanced SMS, Enhanced Apple Messages for Business, Enhanced LINE, and Bring Your Own Channel",
        "required_permissions": "To open, edit, or create a flow in Flow Builder: Manage Flow",
        "required_permission_names": [
          "Manage Flow"
        ]
      },
      "collection": "admin/service"
    },
    {
      "content": "Code context:\nWhere:This change applies to Lightning Experience, and Salesforce Classic in Essentials, Professional, Enterprise, Performance, Unlimited, and Developer editions.\n\nHow:In your Salesforce Developer Experience (SFDX) project, create a Lightning web component and deploy it in your org. Then, in Flow Builder, click `Add\nElement` and then click `Action`. In the list of available actions, select your component. Here’s an example of the configuration file and JavaScript for a component that displays a toast message on a flow screen.\n\n```\n<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<LightningComponentBundle xmlns=\"http://soap.sforce.com/2006/04/metadata\">\n   <apiVersion>65.0</apiVersion>\n   <isExposed>true</isExposed>\n   <targets>\n       <target>lightning__FlowAction</target>\n   </targets>\n   <targetConfigs>\n       <targetConfig targets=\"lightning__FlowAction\">\n           <property name=\"toastTitle\" type=\"String\" label=\"Toast title to display\" />\n           <property name=\"toastMessage\" type=\"String\" label=\"Toast message to display\" />\n       </targetConfig>\n   </targetConfigs>\n</LightningComponentBundle>\n```",
      "score": 0.725307729876968,
      "documentPath": "admin/release-notes/258-0-0/rn_lc_lwc_local_actions.html",
      "url": "https://help.salesforce.com/s/articleView?id=release-notes.rn_lc_lwc_local_actions.htm&release=258&type=5",
      "chunkIndex": 1,
      "metadata": {
        "title": "Use LWC Components for Local Actions in Screen Flows",
        "app_area": "Cross Portfolio",
        "breadcrumb_path": "Salesforce Help|Docs|Salesforce Release Notes"
      },
      "collection": "admin/release-notes"
    },
    {
      "content": "Update Omni-Channel Flow for Embedded Messaging\n\nReturn to the Omni-Channel flow that you created when you prepared a Salesforce org, and add the autolaunched flow as a subflow.\n\n1. From Setup, in the Quick Find box, enter `Flows`, and select `Flows`.\n\n2. From the list, find and select your previous Omni-Channel flow.\n\n3. Add a Subflow element after Start, and select the autolaunched flow that you previously created.\n\n4. Specify the label, API name, and description.\n\n5. Set input values for the autolaunched flow by passing the `userID` and `recordID` variable values from the Omni-Channel flow.\n\n6. Activate the flow.\nWith this flow, a service representative sees the employee's account ID, contact ID, and full name in the messaging session record. The incoming chat notification shows the employee's name.",
      "score": 0.7225977447745547,
      "documentPath": "admin/service/260-0-0/es_update_messaging_session_with_contact_details.html",
      "url": "https://help.salesforce.com/s/articleView?id=service.es_update_messaging_session_with_contact_details.htm&release=260&type=5",
      "chunkIndex": 4,
      "metadata": {
        "title": "Update Messaging Session with Employee Details",
        "app_area": "Service",
        "breadcrumb_path": "Salesforce Help|Docs|Agentforce Service",
        "required_editions": "[View supported editions](https://help.salesforce.com/s/articleView?id=service.service_editions_reference.htm&language=en_US).",
        "required_permissions": "To open, edit, or create a flow in Flow Builder: Manage Flow",
        "required_permission_names": [
          "Manage Flow"
        ]
      },
      "collection": "admin/service"
    },
    {
      "content": "In Flow Builder, add an Action element to your flow. In the New Action window, select `Slack`, and then select `Send Slack Direct Message to\nSalesforce App`.",
      "score": 0.7211626435712202,
      "documentPath": "admin/platform/260-0-0/flow_ref_elements_actions_slack_send_slack_direct_message_to_salesforce_app.html",
      "url": "https://help.salesforce.com/s/articleView?id=platform.flow_ref_elements_actions_slack_send_slack_direct_message_to_salesforce_app.htm&release=260&type=5",
      "chunkIndex": 2,
      "metadata": {
        "title": "Send Slack Direct Message to Salesforce App Action",
        "app_area": "Flow Builder",
        "breadcrumb_path": "Salesforce Help|Docs|Automate Your Business Processes",
        "required_editions": "[View supported editions.](flow_ref_supported_editions.htm)"
      },
      "collection": "admin/platform"
    }
  ],
  "total": 5,
  "returned": 5,
  "metrics": {
    "queryTimeMs": 145,
    "searchMode": "auto (semantic)",
    "embeddingTimeMs": 88,
    "fallbackTriggered": false,
    "embeddingModel": "nomic"
  }
}
