# Q7: How do I display a toast message in a Salesforce screen flow?

## Approach: B_context7-our-library
- latency: 3013 ms
- libraryId: /damecek/salesforce-documentation-context

---

===============
LIBRARY RULES
===============
From library maintainers:
- Do not infer product behavior beyond what is stated in the markdown.
- Preserve product terminology as written in the source markdown.



### Show Toast Notification

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/lightning-aura-components-developer-guide-part-01.md

Use lightning:notificationsLibrary to display a success toast message. This toast is announced by screen readers with role="alert".

```html
<lightning:notificationsLibrary aura:id="notifLib"/>

<lightning:button name="toast" label="Show Toast" onclick="{!c.handleShowToast}"/>
```

```javascript
({    
    handleShowToast : function(component, event, helper) {
        component.find('notifLib').showToast({
           "title": "Success!",
           "message": "The record has been updated successfully."
        });
    }
})
```

--------------------------------

### Conditionally Display Toast Notification

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/lightning-aura-components-developer-guide-part-02.md

This snippet shows how to fire a force:showToast event in Salesforce mobile app and Lightning Experience, with a fallback implementation for standalone apps. Use this to display toast messages based on component loading status.

```javascript
displayToast : function (component, event, helper) {

      var toast = $A.get("e.force:showToast");

      if (toast){

        //fire the toast event in Salesforce app and Lightning Experience

        toast.setParams({

           "title": "Success!",

           "message": "The component loaded successfully."

        });

        toast.fire();

      } else {

        //your toast implementation for a standalone app here

      }

   }
```

--------------------------------

### Display Toast Message in Aura Components

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/lightning-aura-components-developer-guide-part-01.md

Use $A.get("e:force:showToast") to display success or error messages to the user. This is typically used after an action completes, such as loading data.

```javascript
var toastEvent = $A.get("e:force:showToast");

            if (state === 'SUCCESS'){

               toastEvent.setParams({

                 "title": "Success!",

                 "message": " Your contacts have been loaded successfully."

               });

            }

            else {

               toastEvent.setParams({

                   "title": "Error!",

                   "message": " Something has gone wrong."

               });

            }

            toastEvent.fire();
```

--------------------------------

### Customize Error Handling in lightning:recordForm

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/lightning-aura-components-developer-guide-part-02.md

Use the onsuccess and onerror event handlers to customize behavior when a record is saved or an error is encountered. Displays a toast notification for success or error messages.

```html
<aura:component implements="flexipage:availableForRecordHome, force:hasRecordId">

      <!-- Displays a toast notification -->

      <lightning:notificationsLibrary aura:id="notifLib" />

      <lightning:recordForm

        recordId = "{!v.recordId}"

        objectApiName="Account"

        layoutType="Compact"

        mode="edit"

        onsuccess="{!c.handleSuccess}"

        onerror="{!c.handleError}"/>

   </aura:component>
```

```javascript
({ 

      handleSuccess: function (cmp, event, helper) { 

        cmp.find('notifLib').showToast({

           "title": "Record updated!",

           "message": "The record "+ event.getParam("id") + " has been updated

   successfully.",

           "variant": "success"

        }); 

      },

      handleError: function (cmp, event, helper) { 

        cmp.find('notifLib').showToast({

           "title": "Something has gone wrong!",

           "message": event.getParam("message"),

           "variant": "error"

        }); 

      }

   })
```

### Salesforce Anywhere Core Flow Actions (Beta) > Considerations

Source: https://github.com/damecek/salesforce-documentation-context/blob/v1.3.0/documentation/automate-your-business-processes-part-03.md

If a flow launched from an action button encounters an error without fault paths, a generic error message is displayed. To provide a helpful error message, add fault paths to the launched flow, set an output variable to {!$Flow.FaultMessage} on each fault path, and conditionally display this message using a Display Text component on the flow screen with the action button. Note that screen readers do not announce the content of a Display Text component as an error message.
